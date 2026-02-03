# Source: https://smartcar.com/docs/api-reference/signals/lowvoltagebattery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LowVoltageBattery Signals

### State Of Charge

Signal code: `lowvoltagebattery-stateofcharge`

Indicates the current charge level of the low voltage battery as a percentage (0 - 100)

<ParamField path="unit" type="string" required={false}>
  The unit for state of charge (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The battery charge level as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 95
}
```

### Status

Signal code: `lowvoltagebattery-status`

Represents the current operational status of the low voltage battery. (GOOD, WARN, BAD)

<ParamField path="value" type="string" required={false}>
  The operational status of the battery

  **Possible values:** `GOOD`, `WARN`, `BAD`
</ParamField>

```json Example theme={null}
{
  "value": "GOOD"
}
```
