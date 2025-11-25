# Source: https://smartcar.com/docs/api-reference/signals/hvac.md

# HVAC Signals

### Cabin Target Temperature

Signal code: `hvac-cabintargettemperature`

The target temperature set for the vehicle's cabin.

<ParamField path="unit" type="string" required={false}>
  The temperature unit (e.g., celsius, fahrenheit)
</ParamField>

<ParamField path="value" type="number" required={false}>
  The target temperature value
</ParamField>

```json Example theme={null}
{
  "unit": "celsius",
  "value": 22
}
```

### Is Cabin HVACActive

Signal code: `hvac-iscabinhvacactive`

A boolean value indicating if the cabin HVAC system is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Front Defroster Active

Signal code: `hvac-isfrontdefrosteractive`

A boolean value indicating if the front windshield defroster is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Rear Defroster Active

Signal code: `hvac-isreardefrosteractive`

A boolean value indicating if the rear windshield defroster is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Steering Heater Active

Signal code: `hvac-issteeringheateractive`

A boolean value indicating if the steering wheel heater is active.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```
