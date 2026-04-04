# Source: https://smartcar.com/docs/api-reference/signals/connectivitystatus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# ConnectivityStatus Signals

### Is Asleep

Signal code: `connectivitystatus-isasleep`

Boolean indicator that shows whether the vehicle is in a low-power or sleep state.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": false
}
```

### Is Digital Key Paired

Signal code: `connectivitystatus-isdigitalkeypaired`

Boolean indicator that shows whether a digital key has been successfully paired with the vehicle.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```

### Is Online

Signal code: `connectivitystatus-isonline`

Boolean indicator that shows the connectivity status of the vehicle.

<ParamField path="value" type="boolean" required={false} />

```json Example theme={null}
{
  "value": true
}
```
