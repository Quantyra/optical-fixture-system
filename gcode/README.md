# Original machine-specific G-code

Three files retain their original filenames and bytes. [manifest.json](manifest.json) lists file sizes, SHA-256, candidate meshes, mapping confidence, raw parsed header values, control commands and model outer-wall bounds. No new G-code was generated. Exact source slicing is not established for any file.

| Filename stem | Candidate mesh | Outer-wall centerline span X x Y / final wall Z (mm) |
| --- | --- | --- |
| source_stand_34mm_edge_alignment#1 | source_stand_34mm.stl | 33.578 x 27.578 / 25 |
| detector_cradle | detector_cradle.stl | 49.578 x 31.578 / 14 |
| ambient_cover_110mm_roof_down | ambient_cover_110mm_roof_down.stl | 93.578 x 93.578 / 112 |

These are extruding `WALL-OUTER` paths after layer markers, excluding purge, brim and travel. With roughly 0.4 mm outer lines, they are consistent with 34 x 28 x 25, 50 x 32 x 14 and 94 x 94 x 112 parts respectively. This does not prove identical interior geometry or exact source provenance. Header MIN/MAX bounds include non-model paths and cannot establish part size. The current stand file maps dimensionally to the 34 mm stand. The 32 mm STL remains supported but has no current G-code.

The replacement stand header estimates 1079.63 s and 1.24335 m filament (previously 1067.81 s and 1.20646 m). The cradle estimates 1070.81 s (previously 1070.86 s) and retains 2.45646 m filament. Stand acceleration commands vary with the new paths; cradle control-command inventory is unchanged. Outer-wall spans and final wall Z for the cradle and unchanged cover remain as tabulated. Stand/cradle layer counts remain 125/70. Cradle header MAXZ 20.101 includes non-model motion; final extruding outer-wall Z is 14 mm.

## Profile and command inspection

Filenames specify **Ender-3 V3 KE**, 0.4 mm and CR-PETG; this is not an Ender-3 V3 SE profile. All headers report Creality Print V4.3.8.6674 / CXEngine, Marlin flavor, machine `F005`, 220 x 220 x 240 mm, PETG / CR-PETG_1.75, 1.75 mm filament, 0.2 mm layers, two walls, 0.8 mm wall and top/bottom thickness, 15% grid infill, support disabled and brim adhesion. Raw nozzle-diameter field `1000` and initial-height field `200` have ambiguous units and do not verify nozzle size. Filenames and 0.4 mm outer / 0.42 mm inner line widths supply context. A `Screen Size:Sermoon D3` field further limits machine identity confidence.

All files actually command **M190 S80**, **M104 S230**, **M109 S230**: 80 C bed and 230 C nozzle. Startup resets flow/extrusion, uses absolute coordinates/extrusion, homes with `G28`, purges at X=-2 with Z=0.28, and sets `M900 K0.05` linear advance. Negative-X purge travel and linear advance support depend on the actual machine/firmware. There is no explicit `G29`, bed-mesh load, leveling command or named start/end macro. Homing behavior is firmware-dependent; do not assume a bed mesh is active.

Header target speeds (mm/s): outer wall 200, inner wall/infill 300, top/bottom 200, travel 300, initial layer/brim 100. Actual F words span 600–18000 mm/min (10–300 mm/s), including non-print moves; these are commands, not measured speeds. Retraction is 1.2 mm at 40 mm/s. M204 varies acceleration, including 500, 2000 and 5000 mm/s². Review machine limits instead of adopting these as recommended PETG settings.

All files contain fan S0, S63.8 and S127.5 (nominally 0%, 25%, 50% on a 255 scale). Stand and cradle also use S255 (100%); hood does not. End sequences shut bed/nozzle/fans off, including `M106 P2 S0`, retract and raise Z in relative mode, return to absolute coordinates, present at X2 Y218 and disable X/Y/E steppers with `M84 X Y E`. Fan channel P2 support depends on firmware.

Brim adhesion is enabled, but exact brim width is not explicitly recorded in the textual header. The 5 mm brim in the assembly guide is starting guidance, not a recovered setting. Header settings and command lists remain in the manifest for inspection.

Prefer re-slicing the intended STL with a reviewed profile for your exact printer, firmware and filament. These files are profile-specific examples, not universal ready-to-run files or hardware-test evidence. The user's hood print observation does not establish completed fit or light exclusion.
