# Source: https://smartcar.com/docs/api-reference/signals/transmission.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Transmission Signals

### Gear State

Signal code: `transmission-gearstate`

The current gear selection of the vehicle's transmission.

<ParamField path="value" type="string" required={true}>
  The current gear selection of the vehicle's transmission.

  **Possible values:** `PARK`, `DRIVE`, `REVERSE`, `NEUTRAL`
</ParamField>

### Drive Mode

Signal code: `transmission-drivemode`

Represents the current drive mode selected in the vehicle's transmission system

<ParamField path="canonical" type="string" required={true}>
  The standardized drive mode value
</ParamField>

<ParamField path="oemDisplayName" type="string" required={true}>
  The display name for the drive mode as shown by the OEM
</ParamField>

```json Example theme={null}
{
  "canonical": "NORMAL",
  "oemDisplayName": "everyday"
}
```
