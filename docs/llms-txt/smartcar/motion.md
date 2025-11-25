# Source: https://smartcar.com/docs/api-reference/signals/motion.md

# Motion Signals

### Current Speed

Signal code: `motion-currentspeed`

The vehicle's current driving speed, or 0 if it is not currently driving.

<ParamField path="unit" type="string" required={false}>
  The unit of speed measurement (e.g., kph, mph)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The current speed value
</ParamField>

```json Example theme={null}
{
  "unit": "kph",
  "value": 65
}
```
