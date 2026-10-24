# Original operator-supplied G-code

These files are exact original byte copies. Nothing was executed or machine-validated for this release. Prefer fresh slicing of the exact intended STL for your printer, firmware and material. Exact source slicing is not established by matching filenames or embedded dimensions.

## Current keyed pair

| Original filename | Mesh counterpart |
| --- | --- |
| `source_stand_female_taller_socket_2026-10-23-Ender-3 V3 SE_0.4_CR-PETG_30m.gcode` | `stl/source_stand_female.stl` |
| `detector_cradle_two_male_ports-Ender-3 V3 SE_0.4_CR-PETG_35m.gcode` | `stl/detector_cradle_two_male_ports.stl` |

Filenames specify Ender-3 V3 SE, 0.4 mm and CR-PETG. Embedded profiles/settings and the actual command inventory are recorded in [manifest.json](manifest.json), without correcting original metadata. The superseded 29-minute stand is not included. The operator reports a printed revised stand and stand/jig fit; that does not establish precision or qualify these programs for another machine.

Both embedded profiles report 220 × 220 × 250 mm machine volume, 0.2 mm layers, 220 °C nozzle / 70 °C bed, two walls, 10% grid infill, supports disabled and brim adhesion. Header time estimates are 1803.53 s for the stand and 2121.14 s for the cradle. These are slicer estimates, not measured print durations. The raw `ExtruderParams[0] Nozzle Diameter` field is `1000`; this does not directly agree with the filename's 0.4 mm designation and is preserved without interpretation. Confirm the actual nozzle/profile when re-slicing.

The command inventory includes `G28` homing, `G90`/`G91` positioning, `G92 E0`, `M82` absolute extrusion, heater targets/waits (`M104`, `M109`, `M140`, `M190`), fan control (`M106`), acceleration (`M204`), speed/flow scaling (`M220`/`M221`), heater shutdown and `M84 X Y E`. The manifest retains distinct control-command lines and feed-rate ranges for review; these observations do not establish machine compatibility.

## Preserved legacy programs

The three original v1.0.1 files for the 34 mm stand, original cradle and roof-down lift-off hood remain byte-for-byte unchanged. Their filenames and embedded profiles refer to Ender-3 V3 KE, not the current keyed-pair SE profile. They must not be mistaken for keyed stand/cradle programs. The 32 mm legacy stand has no supplied program.

Review the embedded heater targets, homing, coordinate/extrusion modes, motion limits, feed rates, acceleration, fan and shutdown commands against your actual firmware before use. Programs contain real machine commands, including homing and heater control. An embedded profile is not proof of firmware compatibility. No spacer G-code is included; obtain the spacer STLs and slice fresh.

All G-code is under the unchanged [CERN-OHL-S-2.0](../LICENSE). [SHA256SUMS](../SHA256SUMS) and the profile manifest identify exact bytes.
