# Source: https://smartcar.com/docs/api-reference/signals/odometer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Odometer Signals

### Traveled Distance

Signal code: `odometer-traveleddistance`

The total distance the vehicle has traveled since its initial use

<ParamField path="unit" type="string" required={false}>
  The unit for distance measurement (e.g., kilometers, miles)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The total distance traveled
</ParamField>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 50000
}
```
