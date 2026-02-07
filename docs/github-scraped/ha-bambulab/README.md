# Bambu Lab Home Assistant Integration (ha-bambulab)

A Home Assistant integration for controlling and monitoring Bambu Lab 3D printers.

**Repository:** https://github.com/greghesp/ha-bambulab

## Overview

ha-bambulab is an open-source Home Assistant integration that connects your Bambu Lab 3D printer to Home Assistant. The integration supports reading printer data and controlling printer functionality through both cloud and local connections.

### Key Features

- Real-time printer monitoring (temperature, print progress, layer count)
- AMS (Automatic Material System) control and monitoring
- Print job control (pause, resume, stop)
- Filament management and RFID reading
- Device triggers for automations
- Actions for printer control via automations
- Multi-printer support
- Camera stream support (for chamber monitoring)
- Device diagnostics and debugging

### Supported Printers

The integration works with Bambu Lab printers including:
- X1 / X1 Carbon
- P1 / P1 Pro
- P2 / P2 Pro
- A1 / A1 Mini
- H2 / H2D

Note: Feature availability varies by printer model (e.g., AMS is not available on A1/A1 Mini, chamber camera varies by model).

## Installation

### Via HACS (Recommended)

The easiest way to install is through HACS:

1. Open Home Assistant
2. Go to Settings > Devices & Services
3. Click "Create Automation"
4. Search for "ha-bambulab" in HACS
5. Click "Install"
6. Restart Home Assistant

### Automatic HACS Installation Button

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=greghesp&repository=ha-bambulab&category=Integration)

### Manual Installation

Clone the repository to your Home Assistant custom_components directory:

```bash
git clone https://github.com/greghesp/ha-bambulab.git ~/.homeassistant/custom_components/bambu_lab
```

## Setup and Configuration

### Adding a Printer to Home Assistant

1. Navigate to Home Assistant Settings > Devices & Services
2. Click "Create Automation" (or "Add Integration")
3. Search for and select "Bambu Lab"
4. Follow the configuration wizard

### Connection Methods

#### Bambu Cloud Connection (Recommended)

For the most features, use your Bambu Cloud credentials:

- **Advantages:** Access to cloud features (print history, cover images), remote connection
- **Disadvantages:** Does not support 2FA, does not support passwordless OAuth accounts

**Configuration:**
- Bambu Cloud username
- Bambu Cloud password
- (Optional) Local printer IP for more efficient connection

#### LAN Mode Connection

For printers set to LAN Only Mode or if you want local-only connectivity:

**Required Information:**
- Printer Serial Number (format: `a1b2c3d4e5f6a1b2`, not the `3DP-000-000` name)
- Local printer IP address (from printer network settings)
- Access Code (from printer settings)

**Optional Advanced Settings:**
- Disable SSL verification (for MQTT, FTP, chamber camera connections - unsafe, not recommended)
- Enable "LAN Only Liveview" for chamber camera access

#### OAuth Setup

If you created your Bambu account with OAuth (social login):

1. Open Bambu mobile app
2. Tap person icon (bottom right)
3. Go to Account Security > Change Password
4. Set a password
5. Use this password in the Home Assistant integration

### Firmware Compatibility

**Important:** Bambu Lab has implemented authorization controls in newer firmware versions:

**Affected Firmware:**
- X1C: 01.08.05.00 and later
- P1: 01.08.02.00 and later
- A1: 01.05.00.00 and later

**Impact:**
- **Read functionality:** Always works
- **Write functionality (control commands):** Limited or disabled in cloud-connected mode

**Options:**
1. Don't update firmware if you rely on Home Assistant write controls
2. Enable Developer LAN Mode on printer (disables Bambu Cloud connectivity)
3. Use LAN Only Mode (loses remote Bambu access)

For older firmware (P1 01.07.00.00 and similar), hybrid mode (local connection to cloud printer) limits write control to chamber light only.

## Sensors and Entities

### Temperature Sensors

| Sensor | Notes |
|--------|-------|
| Bed Temperature | Current bed temperature |
| Target Bed Temperature | Target bed temperature |
| Nozzle Temperature | Current nozzle temp (H2D has three: left, right, active) |
| Target Nozzle Temperature | Target nozzle temp |
| Chamber Temperature | P2/X1/H2 only |

### Print Progress Sensors

| Sensor | Notes |
|--------|-------|
| Print Progress | Percentage complete (0-100) |
| Current Layer | Current layer number |
| Total Layer Count | Total layers in print |
| Print Status | Current state (printing, idle, paused, etc.) |
| Current Stage | Current print stage |
| Start Time | When print started (estimated or from cloud) |
| Remaining Time | Estimated time until print completes |
| End Time | Estimated completion time |
| Print Weight | Grams (requires Bambu credentials) |
| Print Length | Length of filament in mm (requires Bambu credentials) |
| Print Bed Type | Textured/Cool/Custom, etc. |
| Total Usage Hours | Running estimate (needs calibration) |
| Cover Image | Print preview image |

### Filament and AMS Sensors

#### AMS Sensors (if equipped)

| Sensor | Notes |
|--------|-------|
| Active Tray | Currently active AMS tray |
| Active Tray Index | Index of active tray |
| Humidity | AMS humidity (P1/P2/X1/H2 only) |
| Temperature | AMS internal temperature |
| Remaining Drying Time | For AMS 2 Pro/AMS HT |
| Drying | Whether drying is active (AMS 2 Pro/AMS HT only) |

**Per-Tray Attributes:**
- Color (RGBA format)
- Empty status
- K Value (P1/A1 only)
- Name
- Nozzle min/max temperature
- Remaining filament percentage
- Spool serial number
- Filament type

#### External Spool Sensors

Similar attributes to AMS trays when using external filament supply.

### Miscellaneous Sensors

| Sensor | Notes |
|--------|-------|
| Nozzle Diameter | Current nozzle size (H2D has three) |
| Nozzle Type | Type of nozzle (H2D has three) |
| Speed Profile | Current speed profile |
| Timelapse Active | Whether timelapse recording is enabled |
| Extruder Filament Status | Filament loaded status |
| Tool Module State | H2D only (none, laser, cutter, unavailable) |

### Diagnostic Sensors

| Sensor | Notes |
|--------|-------|
| Developer LAN Mode | Whether Developer LAN Mode is enabled |
| Enclosure Door | Door status (X1/P2/H2 only) |
| Firmware Update Available | New firmware available |
| Force Refresh | Manual data refresh button |
| HMS Errors | Active hardware maintenance system errors |
| IP Address | Printer's local IP address |
| MQTT Connection Mode | Bambu Cloud or Local |
| MQTT Encryption Firmware | Whether printer requires MQTT encryption |
| Online Status | Whether printer is reachable |
| Print Error | Whether a print error is active |
| SD Card Status | SD card state |
| Total Usage Hours | Total hours printer has run |
| WiFi Signal | WiFi signal strength (RSSI) |

### Fan Controls

| Fan | Notes |
|-----|-------|
| Aux Fan | |
| Chamber Fan | Not on A1/A1 Mini |
| Cooling Fan | |
| Secondary Aux Fan | P2S only |

### Control Switches

| Control | Notes |
|---------|-------|
| Chamber Light | On/Off |
| Heatbed Light | H2D only, initial state unknown |
| Pause Print | Pause active print |
| Resume Print | Resume paused print |
| Stop Print | Stop active print |
| Bed Temperature | Set bed temp (not in P1/A1 hybrid mode) |
| Nozzle Temperature | Set nozzle temp (not in P1/A1 hybrid mode) |
| Buzzer | H2D only, 3 modes |
| Allow Prompt Sound | A1 and H2D, startup/print sounds |

### Camera Streams

| Camera | Notes |
|--------|-------|
| Chamber Camera | P1/A1/A1Mini: requires host IP; X1: enable "LAN Mode LiveView" |

## Actions and Automations

### Available Actions

#### Send GCODE Command

Send arbitrary GCODE to the printer:

```yaml
action: bambu_lab.send_command
data:
  device_id: <device_id>
  command: M104 S200
```

**Warning:** Does not check if printer is busy; verify printer state before sending.

#### Print 3MF File

Print a 3MF file stored on the printer's SD card:

```yaml
action: bambu_lab.print_project_file
data:
  device_id: <device_id>
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
- `filepath`: Filename on SD card (relative to root)
- `plate`: Plate number to print
- `timelapse`: Record timelapse (boolean)
- `bed_leveling`: Perform bed leveling (boolean)
- `flow_cali`: Flow calibration (boolean)
- `vibration_cali`: XY mechanical sweep (boolean)
- `layer_inspect`: First layer inspection (boolean)
- `use_ams`: Use AMS (boolean, uses external spool if false)
- `ams_mapping`: Tray mapping (e.g., "2,-1,0")

#### Extrude or Retract Filament

```yaml
action: bambu_lab.extrude_retract
data:
  device_id: <device_id>
  type: Extrude  # or Retract
  force: false   # Force even if nozzle < 170°C
```

#### Load Filament

Load filament from AMS or external spool:

```yaml
action: bambu_lab.load_filament
data:
  entity_id: <entity_id>  # AMS or external spool tray
  temperature: 220  # Optional, uses filament midpoint if not set
```

#### Unload Filament

```yaml
action: bambu_lab.unload_filament
data:
  device_id: <device_id>
```

#### Set Filament

Set filament type and properties for AMS or external spool tray:

```yaml
action: bambu_lab.set_filament
data:
  entity_id: <entity_id>  # AMS or external spool tray
  tray_info_idx: GFL96  # Bambu filament ID
  tray_color: FF00FF00  # RGBA color
  tray_type: PLA  # Filament type
  nozzle_temp_min: 190
  nozzle_temp_max: 240
```

Common filament IDs: GFL96 (Generic PLA Silk), etc.

#### Get Filament Data

Get JSON with all known filaments:

```yaml
action: bambu_lab.get_filament_data
data:
  device_id: <device_id>
```

#### Move Axis

Move printer axis:

```yaml
action: bambu_lab.move_axis
data:
  device_id: <device_id>
  axis: X  # X, Y, or Z
  distance: 10  # mm, negative values reverse direction
```

**Note:** Axis meanings vary by printer (X1/P1: X/Y move printhead Z moves bed; A1: Z moves gantry, Y moves bed, X moves printhead).

#### Skip Objects

Skip objects during active print:

```yaml
action: bambu_lab.skip_objects
data:
  device_id: <device_id>
  objects: 409,1463  # Object IDs from printable objects entity
```

#### Read RFID Tag

Trigger AMS to re-read spool RFID tag:

```yaml
action: bambu_lab.read_rfid
data:
  entity_id: <entity_id>  # AMS tray entity
```

#### Filament Drying

Start AMS filament drying (AMS 2 Pro/AMS HT):

```yaml
action: bambu_lab.start_filament_drying
data:
  device_id: <device_id>
  temp: 65  # AMS 2 max: 65C, AMS HT max: 85C
  rotate_tray: false
  duration: 12  # hours
```

Stop drying:

```yaml
action: bambu_lab.stop_filament_drying
data:
  device_id: <device_id>
```

### Device Triggers for Automations

Create automations using device triggers:

**Available Triggers:**
- Print started
- Print finished
- Print canceled
- Print failed (X1 only)
- HMS error detected
- Print error detected

**Trigger Data Payload:**
- `device_id`: Printer device ID
- `name`: Printer name
- `type`: Unlocalized event type
- `code`: Error code (for errors)
- `error`: Error description
- `url`: Wiki link for error (for HMS errors)

**Using Trigger Data in Actions:**

Access trigger data with Jinja2 templates:

```yaml
# Notification example
title: "Printer Error on {{ trigger.event.data.name }}"
message: "{{ trigger.event.data.code }}: {{ trigger.event.data.error }}"
action: |
  action: notify.notify
  data:
    title: "{{ trigger.event.data.name }}"
    message: "{{ trigger.event.data.code }}: {{ trigger.event.data.error }}"
```

**Adding Device Triggers:**

1. Option 1: From printer device page > Automations > Create automation
2. Option 2: From Automations page > Create automation > Select trigger > Choose device > Select Bambu Lab trigger

## Troubleshooting and Debugging

### Enable Debug Logging

#### During Initial Setup

Add to `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.bambu_lab: debug
```

Then restart Home Assistant.

#### After Installation

Enable from Home Assistant UI:
1. Settings > Devices & Services
2. Find Bambu Lab integration
3. Click the menu (three dots)
4. Select "Enable debug logging"

### Collect Diagnostics

When reporting issues:

1. Click "Force Refresh Data" under Diagnostics section
2. Go to printer device info page
3. Click "Download Diagnostics"
4. Upload to GitHub issue or Discord

### Common Issues

**Issue: Integration won't connect with Bambu Cloud credentials**
- Verify username and password are correct
- Bambu credentials don't support 2FA; disable 2FA if enabled
- If using OAuth (social login), set a password first (see Setup section)
- Check internet connectivity to Bambu servers

**Issue: Local connection fails**
- Verify correct printer serial number format (a1b2c3d4e5f6a1b2, not 3DP-000-000)
- Verify correct local IP address
- Verify correct access code from printer settings
- Ensure printer and Home Assistant are on same network
- Check firewall rules allowing MQTT (port 8883) and FTP (port 990)

**Issue: Write functionality not working**
- Check firmware version (newer versions have restrictions)
- If cloud-connected, consider enabling Developer LAN Mode
- Verify user account has write permissions in printer settings
- Note: On latest X1C firmware, only chamber light control works in cloud mode

**Issue: Camera stream not appearing**
- Enable "LAN Only Liveview" in printer settings (for X1)
- Provide local printer IP in configuration (for P1/A1)
- Check network connectivity to printer RTSP stream
- Verify RTSP port (554) is accessible

**Issue: Sensors not updating**
- Click "Force Refresh" diagnostic button
- Check MQTT connection mode (Bambu Cloud vs Local)
- Verify printer is powered on and online
- Restart integration: Settings > Devices & Services > Bambu Lab > Restart

**Issue: AMS not appearing**
- AMS not supported on A1/A1 Mini
- Verify AMS is powered on and connected
- Check MQTT connection to printer

## Frontend Cards

Pre-made dashboard cards are available (work in progress):

1. AMS Card - Shows filament status
2. Print Control Card - Start/pause/stop print
3. Print Status Card - Current print progress
4. Spool Card - Filament information

### Using Custom Cards

1. Open Home Assistant Dashboard
2. Click 3-dot menu (top right)
3. Click "Edit Dashboard"
4. Click Plus button to add card
5. Find "Custom: Bambu" cards in list

### Pre-made Dashboard Generator

Visit https://www.wolfwithsword.com/bambulab-home-assistant-dashboard/ for a web configurator to generate a complete dashboard layout. (Note: Uses different card dependencies than the integration's built-in cards.)

## Advanced Features

### Total Usage Hours Calibration

The `total_usage_hours` sensor is a running estimate that may drift over time:

1. Find the actual usage hours on the printer's display
2. Update the value during initial setup or later via configuration
3. Integration tracks print completions to update the value
4. Periodically adjust to match printer's internal counter

### MQTT Encryption

Modern Bambu printers encrypt MQTT communications. The integration automatically detects and handles this.

### Developer LAN Mode

If you have firmware that supports it:

1. Enable Developer LAN Mode on printer (disables Bambu Cloud)
2. Use LAN Mode configuration in Home Assistant
3. Restores full write functionality on newer firmware

## Support and Community

- **Discord:** https://discord.gg/rsUHAW3DKz
- **GitHub Issues:** https://github.com/greghesp/ha-bambulab/issues
- **GitHub Discussions:** https://github.com/greghesp/ha-bambulab/discussions

## Contributing

Contributions are welcome! See [Contributing Guide](https://github.com/greghesp/ha-bambulab/blob/main/CONTRIBUTING.md).

To support development, consider [buying Adrian a coffee](https://Ko-fi.com/adriangarside).

## License

See repository for license information.
