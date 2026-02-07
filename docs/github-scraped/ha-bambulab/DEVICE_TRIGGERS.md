# Ha-bambulab Device Triggers Reference

Device triggers allow you to create automations based on printer events without needing to understand the underlying sensors.

## Overview

Device triggers provide convenient event-based automation triggers. Unlike sensors which show persistent state, some triggers (like "Print canceled") are transient events that occur momentarily.

All trigger events include the printer name in the data payload, allowing you to reference it in automation actions.

## Available Triggers

### Print Started

Triggered when a print job begins.

**Type:** `bambu_lab.print_started`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_started
action:
  - action: notify.notify
    data:
      title: "Print Started"
      message: "{{ trigger.event.data.name }} has started printing"
```

---

### Print Finished

Triggered when a print job completes successfully.

**Type:** `bambu_lab.print_finished`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_finished
action:
  - action: notify.notify
    data:
      title: "Print Complete"
      message: "{{ trigger.event.data.name }} has finished printing"
  - action: light.turn_off
    target:
      entity_id: light.bedroom
```

---

### Print Canceled

Triggered when a print is canceled.

**Type:** `bambu_lab.print_canceled`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name

**Notes:** This is a transient event; there is no persistent "canceled" state on the printer.

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_canceled
action:
  - action: notify.notify
    data:
      title: "Print Canceled"
      message: "{{ trigger.event.data.name }} print was canceled"
```

---

### Print Failed (X1 Only)

Triggered when a print fails on X1 printer.

**Type:** `bambu_lab.print_failed`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name

**Notes:** Only available on X1 printers.

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_failed
action:
  - action: notify.notify
    data:
      title: "Print Failed"
      message: "{{ trigger.event.data.name }} print has failed"
```

---

### HMS Error Detected

Triggered when a hardware maintenance system (HMS) error is detected.

**Type:** `bambu_lab.hms_error`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name
- `code`: Error code (e.g., `0101`)
- `error`: Human-readable error description
- `url`: Wiki link to error documentation

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.hms_error
action:
  - action: notify.notify
    data:
      title: "Printer Error on {{ trigger.event.data.name }}"
      message: |
        Error {{ trigger.event.data.code }}: {{ trigger.event.data.error }}
        More info: {{ trigger.event.data.url }}
```

---

### Print Error Detected

Triggered when a print error occurs (distinct from HMS errors).

**Type:** `bambu_lab.print_error`

**Trigger Data:**
- `device_id`: Printer device ID
- `name`: Printer name
- `code`: Error code
- `error`: Human-readable error description

**Notes:** These are print-specific errors that aren't surfaced as HMS errors.

**Example:**

```yaml
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_error
action:
  - action: notify.notify
    data:
      title: "Print Error on {{ trigger.event.data.name }}"
      message: "{{ trigger.event.data.code }}: {{ trigger.event.data.error }}"
```

---

## Creating Automations with Device Triggers

### Method 1: From Device Page

1. Open Home Assistant Settings
2. Go to Devices & Services > Devices
3. Find your Bambu Lab printer device
4. Scroll to "Automations" section
5. Click "Create Automation"
6. Select the trigger you want
7. Configure actions

### Method 2: From Automations Page

1. Open Automations section
2. Click "Create Automation"
3. Select "Device" as trigger platform
4. Choose your Bambu Lab printer device
5. Select the trigger type
6. Configure actions

## Using Trigger Data in Templates

All trigger event data is accessible in Jinja2 templates via `trigger.event.data`:

```yaml
# Access trigger data in notifications
data:
  title: "{{ trigger.event.data.name }}"
  message: "{{ trigger.event.data.error }}"

# Access in conditionals
condition:
  - condition: template
    value_template: "{{ trigger.event.data.code == '0101' }}"

# Store in variable for later use
variables:
  printer_name: "{{ trigger.event.data.name }}"
  error_code: "{{ trigger.event.data.code }}"
```

## Common Automation Patterns

### Send Notification on Print Completion

```yaml
alias: Notify on print complete
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_finished
action:
  - action: notify.notify
    data:
      title: "Print Complete"
      message: "Your {{ trigger.event.data.name }} print is done!"
```

### Alert on Any Error

```yaml
alias: Alert on printer errors
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.hms_error
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_error
action:
  - action: notify.notify
    data:
      title: "Printer Alert: {{ trigger.event.data.name }}"
      message: "{{ trigger.event.data.code }}: {{ trigger.event.data.error }}"
```

### Turn On Light During Print

```yaml
alias: Light on during print
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_started
action:
  - action: light.turn_on
    target:
      entity_id: light.printer_area
    data:
      brightness: 255

condition: []

id: '1234567890'
```

### Clean Up After Print

```yaml
alias: Clean up after printing
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.print_finished
action:
  - action: light.turn_off
    target:
      entity_id: light.printer_area
  - action: switch.turn_off
    target:
      entity_id: switch.printer_exhaust_fan
  - delay:
      minutes: 5
  - action: notify.notify
    data:
      title: "Printer Cooled Down"
      message: "Safe to remove print from {{ trigger.event.data.name }}"
```

### Conditional Actions Based on Error Code

```yaml
alias: Handle specific errors
trigger:
  - platform: device
    device_id: a1b2c3d4e5f6g7h8i9j0
    type: bambu_lab.hms_error
action:
  - choose:
      - conditions:
          - condition: template
            value_template: "{{ trigger.event.data.code == '0101' }}"
        sequence:
          - action: notify.notify
            data:
              title: "Nozzle Error"
              message: "The nozzle needs attention"
      - conditions:
          - condition: template
            value_template: "{{ trigger.event.data.code == '0102' }}"
        sequence:
          - action: notify.notify
            data:
              title: "Bed Error"
              message: "The bed needs attention"
    default:
      - action: notify.notify
        data:
          title: "Unknown Error"
          message: "{{ trigger.event.data.error }}"
```

## Advantages Over Sensor-Based Triggers

Using device triggers instead of sensor-based automation has several benefits:

1. **Simpler automation creation** - Visual editor support without needing to understand sensors
2. **Transient events** - Can trigger on events that don't have persistent state (e.g., print canceled)
3. **Better readability** - Automations are easier to understand at a glance
4. **Structured data** - Trigger payload provides all relevant error information in one place
5. **Validation** - Device trigger editor prevents invalid configurations

## Limitations

- Device triggers can only be created through the Home Assistant UI or YAML
- Some advanced scenarios may still require sensor-based triggers for more complex logic
- Transient events are only available as triggers (not as persistent sensors)
