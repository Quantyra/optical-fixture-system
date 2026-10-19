"""Offline package integrity and basic mesh checks; Python standard library only."""
from pathlib import Path
import hashlib
import json
import re
import struct

ROOT = Path(__file__).resolve().parents[1]


def triangles(path):
    data = path.read_bytes()
    if len(data) >= 84 and 84 + 50 * struct.unpack_from('<I', data, 80)[0] == len(data):
        return [tuple(tuple(struct.unpack_from('<3f', data, i + 12 + j * 12))
                      for j in range(3)) for i in range(84, len(data), 50)]
    vertices = [tuple(map(float, v)) for v in re.findall(
        r'vertex\s+([-+\deE.]+)\s+([-+\deE.]+)\s+([-+\deE.]+)', data.decode('ascii'))]
    assert len(vertices) % 3 == 0
    return [tuple(vertices[i:i + 3]) for i in range(0, len(vertices), 3)]


def mesh_info(path):
    tris = triangles(path)
    assert tris, f'Empty mesh: {path}'
    edges = {}
    volume = 0
    for a, b, c in tris:
        volume += (a[0]*(b[1]*c[2]-b[2]*c[1]) +
                   a[1]*(b[2]*c[0]-b[0]*c[2]) + a[2]*(b[0]*c[1]-b[1]*c[0])) / 6
        for u, v in [(a, b), (b, c), (c, a)]:
            edge = tuple(sorted((u, v)))
            edges[edge] = edges.get(edge, 0) + 1
    assert all(n == 2 for n in edges.values()), f'Non-manifold edge: {path}'
    assert volume > 0, f'Non-positive signed volume: {path}'
    bounds = [[min(v[i] for t in tris for v in t), max(v[i] for t in tris for v in t)]
              for i in range(3)]
    return dict(triangles=len(tris), bounds_mm=bounds, signed_volume_mm3=volume,
                closed_edge_incidence=True)


def main():
    listed = set()
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ', 1)
        p = ROOT/name
        assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == digest, name
        listed.add(name)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts
              and p.name != 'SHA256SUMS'}
    assert actual == listed, f'Inventory mismatch: {actual ^ listed}'
    manifest = json.loads((ROOT/'manifest.json').read_text())
    for entry in manifest['files']:
        p = ROOT/entry['path']
        assert p.stat().st_size == entry['bytes']
        assert hashlib.sha256(p.read_bytes()).hexdigest() == entry['sha256']
    z = json.loads((ROOT/'.zenodo.json').read_text())
    assert z['version'] == manifest['version'], 'Package/Zenodo version mismatch'
    assert z['license'] == 'cern-ohl-s-2.0'
    assert z['creators'] and 'doi' not in z
    cff = (ROOT/'CITATION.cff').read_text()
    assert 'cff-version: 1.2.0' in cff and 'CERN-OHL-S-2.0' in cff
    gcode_manifest = json.loads((ROOT/'gcode/manifest.json').read_text())
    assert gcode_manifest['version'] == manifest['version'], 'G-code version mismatch'
    assert re.search(r'^version: [\"\']?' + re.escape(manifest['version']) + r'[\"\']?$',
                     cff, re.MULTILINE), 'CFF version mismatch'
    assert {e['path'] for e in manifest['files']} == actual - {'manifest.json'}
    assert {e['filename'] for e in gcode_manifest['files']} == {
        p.name for p in (ROOT/'gcode').glob('*.gcode')}
    for entry in gcode_manifest['files']:
        p = ROOT/'gcode'/entry['filename']
        assert p.stat().st_size == entry['bytes']
        assert hashlib.sha256(p.read_bytes()).hexdigest() == entry['sha256']
        assert (ROOT/entry['modeled_counterpart']).is_file()
    meshes = {p.name: mesh_info(p) for p in sorted((ROOT/'stl').glob('*.stl'))}
    print(json.dumps(dict(status='PASS',checked_files=len(listed),meshes=meshes), indent=2))


if __name__ == '__main__':
    main()
