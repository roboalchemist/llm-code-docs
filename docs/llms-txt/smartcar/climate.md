# Source: https://smartcar.com/docs/api-reference/signals/climate.md

# Climate Signals

### External Temperature

Signal code: `climate-externaltemperature`

The current temperature measured outside the vehicle.

<ParamField path="unit" type="string" required={false}>
  The unit of temperature measurement (celsius or fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 22.5
}
```

### Internal Temperature

Signal code: `climate-internaltemperature`

The current temperature measured inside the vehicle's cabin.

<ParamField path="unit" type="string" required={false}>
  The unit of temperature measurement (celsius or fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 21.5
}
```
