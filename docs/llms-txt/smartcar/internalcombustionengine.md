# Source: https://smartcar.com/docs/api-reference/signals/internalcombustionengine.md

# InternalCombustionEngine Signals

### Amount Remaining

Signal code: `internalcombustionengine-amountremaining`

The quantity of fuel remaining in the vehicle's tank

<ParamField path="unit" type="string" required={false}>
  The unit of measurement for the fuel amount (e.g., liters, gallons)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The quantity value of remaining fuel
</ParamField>

```json Example theme={null}
{
  "unit": "liters",
  "value": 45.5
}
```

### Fuel Level

Signal code: `internalcombustionengine-fuellevel`

The current amount of fuel in the vehicle's tank, expressed as a percentage (0 - 100)

<ParamField path="unit" type="string" required={false}>
  The unit for fuel level (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The fuel level as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 75
}
```

### Oil Life

Signal code: `internalcombustionengine-oillife`

The engine oil’s remaining life span based on the current quality of the oil, expressed as a percentage. 100 indicates the oil was changed recently and 0 indicates the oil should be changed immediately. It is not a representation of how much oil is left in the vehicle.

<ParamField path="unit" type="string" required={false}>
  The unit for oil life (always percent)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The oil life remaining as a percentage between 0 and 100
</ParamField>

```json Example theme={null}
{
  "unit": "percent",
  "value": 85
}
```

### Range

Signal code: `internalcombustionengine-range`

The estimated driving distance possible with the current amount of fuel

<ParamField path="unit" type="string" required={false}>
  The unit for range measurement (e.g., kilometers, miles)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The estimated driving distance value
</ParamField>

```json Example theme={null}
{
  "unit": "kilometers",
  "value": 450
}
```
