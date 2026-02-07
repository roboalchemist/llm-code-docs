# Ha-bambulab Actions Reference

Complete reference for all actions available in ha-bambulab automations.

## Action Syntax

All actions require either a `device_id` or `entity_id` in the data field:

```yaml
# For most actions (device_id)
action: bambu_lab.<action_name>
data:
  device_id: <printer_device_id>
  <other_parameters>

# For AMS/spool tray actions (entity_id)
action: bambu_lab.<action_name>
data:
  entity_id: <tray_entity_id>
  <other_parameters>
```

## Send Command

Send arbitrary GCODE commands to printer.

**Action ID:** `bambu_lab.send_command`

```yaml
action: bambu_lab.send_command
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  command: M104 S200
```

**Parameters:**
- `command` (string, required): GCODE command (e.g., `M104 S200`)

**Warning:** Does not verify printer state; ensure printer is idle before sending.

---

## Print Project File

Print a 3MF file from printer SD card.

**Action ID:** `bambu_lab.print_project_file`

```yaml
action: bambu_lab.print_project_file
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  filepath: cache/filename.3mf
  plate: 1
  timelapse: true
  bed_leveling: false
  flow_cali: false
  vibration_cali: false
  layer_inspect: false
  use_ams: true
  ams_mapping: -1,-1,2,-1
```

**Parameters:**
- `filepath` (string, required): Path to 3MF file on SD card (relative to root, e.g., `cache/filename.3mf`)
- `plate` (number, optional): Plate number to print
- `timelapse` (boolean, optional): Record timelapse of print
- `bed_leveling` (boolean, optional): Perform bed leveling before print
- `flow_cali` (boolean, optional): Perform flow calibration before print
- `vibration_cali` (boolean, optional): Perform vibration calibration (XY Mech Sweep) before print
- `layer_inspect` (boolean, optional): Enable first layer inspection during print
- `use_ams` (boolean, optional): Use AMS (external spool used if false)
- `ams_mapping` (string, optional): AMS tray mapping (e.g., `2,-1,0`)

**Notes:**
- 3MF file must be on SD card root or cache folder
- File must contain sliced GCODE (export as "Export sliced file" from slicer)
- AMS mapping is comma-separated values; -1 means tray not used

---

## Extrude or Retract Filament

Extrude or retract filament through the extruder.

**Action ID:** `bambu_lab.extrude_retract`

```yaml
action: bambu_lab.extrude_retract
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  type: Extrude
  force: false
```

**Parameters:**
- `type` (string, required): `Extrude` or `Retract`
- `force` (boolean, optional): Force operation even if nozzle temperature < 170°C

---

## Load Filament

Load filament from AMS tray or external spool into extruder.

**Action ID:** `bambu_lab.load_filament`

```yaml
action: bambu_lab.load_filament
data:
  entity_id: sensor.ams_tray_1
  temperature: 220
```

**Parameters:**
- `temperature` (number, optional): Target nozzle temperature after load; uses filament midpoint if not specified

**Notes:**
- `entity_id` must be an AMS or external spool tray entity
- Works with filament settings from RFID tags

---

## Unload Filament

Unload filament from nozzle.

**Action ID:** `bambu_lab.unload_filament`

```yaml
action: bambu_lab.unload_filament
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
```

**Parameters:** None

---

## Set Filament

Set filament type and properties for AMS tray or external spool.

**Action ID:** `bambu_lab.set_filament`

```yaml
action: bambu_lab.set_filament
data:
  entity_id: sensor.ams_tray_1
  tray_info_idx: GFL96
  tray_color: FF00FF00
  tray_type: PLA
  nozzle_temp_min: 190
  nozzle_temp_max: 240
```

**Parameters:**
- `tray_info_idx` (string, required): Bambu filament ID (e.g., `GFL96` for Generic PLA Silk)
- `tray_color` (string, required): RGBA color value (e.g., `FF0000FF` for opaque red)
- `tray_type` (string, required): Filament type (e.g., `PLA`, `PETG`, `TPU`)
- `nozzle_temp_min` (number, required): Minimum recommended nozzle temperature
- `nozzle_temp_max` (number, required): Maximum recommended nozzle temperature

**Notes:**
- `entity_id` must be an AMS or external spool tray entity
- Filament IDs are from Bambu's filament database

---

## Get Filament Data

Get JSON string with all known filaments.

**Action ID:** `bambu_lab.get_filament_data`

```yaml
action: bambu_lab.get_filament_data
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
```

**Parameters:** None

**Returns:** JSON string with complete filament database

---

## Move Axis

Move printer axis (printhead, bed, gantry).

**Action ID:** `bambu_lab.move_axis`

```yaml
action: bambu_lab.move_axis
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  axis: X
  distance: 10
```

**Parameters:**
- `axis` (string, required): Axis to move (`X`, `Y`, or `Z`)
- `distance` (number, required): Distance in mm (negative reverses direction)

**Axis Meanings by Printer:**
- **X1/P1:** X/Y move printhead, Z moves bed
- **A1:** Z moves gantry, Y moves bed, X moves printhead

**Notes:**
- Negative distance values move axis in reverse direction
- Z negative moves upward (away from bed)

---

## Skip Objects

Skip specific objects during active print.

**Action ID:** `bambu_lab.skip_objects`

```yaml
action: bambu_lab.skip_objects
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  objects: 409,1463
```

**Parameters:**
- `objects` (string, required): Comma-separated object IDs to skip

**Notes:**
- Available object IDs are in the printable objects entity attributes
- Only works during active print

---

## Read RFID Tag

Trigger AMS to re-read RFID tag on current spool.

**Action ID:** `bambu_lab.read_rfid`

```yaml
action: bambu_lab.read_rfid
data:
  entity_id: sensor.ams_tray_1
```

**Parameters:** None

**Notes:**
- `entity_id` must be an AMS tray entity
- Useful for updating spool information

---

## Start Filament Drying

Start filament drying in AMS 2 Pro or AMS HT.

**Action ID:** `bambu_lab.start_filament_drying`

```yaml
action: bambu_lab.start_filament_drying
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  temp: 65
  rotate_tray: false
  duration: 12
```

**Parameters:**
- `temp` (number, required): Drying temperature in Celsius
  - AMS 2 Pro max: 65°C
  - AMS HT max: 85°C
- `rotate_tray` (boolean, required): Rotate tray during drying
- `duration` (number, required): Drying duration in hours

---

## Stop Filament Drying

Stop active filament drying.

**Action ID:** `bambu_lab.stop_filament_drying`

```yaml
action: bambu_lab.stop_filament_drying
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
```

**Parameters:** None

---

## Common Automation Examples

### Pause Print When Bed Reaches Temperature

```yaml
alias: Pause if bed overheats
trigger:
  - platform: numeric_state
    entity_id: sensor.bed_temperature
    above: 65
action:
  - action: bambu_lab.extrude_retract
    data:
      device_id: a1b2c3d4e5f6g7h8i9j0
      type: Extrude
```

### Send Custom GCODE

```yaml
alias: Home all axes
action: bambu_lab.send_command
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  command: G28
```

### Start Print from SD Card

```yaml
alias: Start test print
action: bambu_lab.print_project_file
data:
  device_id: a1b2c3d4e5f6g7h8i9j0
  filepath: cache/test_print.3mf
  use_ams: true
  timelapse: true
```

### Notify on Print Error

```yaml
alias: Notify on printer error
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_error
action:
  - action: notify.notify
    data:
      title: "Printer Error: {{ trigger.event.data.name }}"
      message: "{{ trigger.event.data.code }}: {{ trigger.event.data.error }}"
```

### Load Specific Filament

```yaml
alias: Load filament for PLA print
action: bambu_lab.load_filament
data:
  entity_id: sensor.ams_tray_1
  temperature: 210
```

### Move Printer to Safe Position

```yaml
alias: Home printer
sequence:
  - action: bambu_lab.move_axis
    data:
      device_id: a1b2c3d4e5f6g7h8i9j0
      axis: X
      distance: 0
  - action: bambu_lab.move_axis
    data:
      device_id: a1b2c3d4e5f6g7h8i9j0
      axis: Y
      distance: 0
  - action: bambu_lab.move_axis
    data:
      device_id: a1b2c3d4e5f6g7h8i9j0
      axis: Z
      distance: 0
```
