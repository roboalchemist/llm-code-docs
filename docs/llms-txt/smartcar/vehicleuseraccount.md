# Source: https://smartcar.com/docs/api-reference/signals/vehicleuseraccount.md

# VehicleUserAccount Signals

### Permissions

Signal code: `vehicleuseraccount-permissions`

Permissions granted by the connecting account with the OEM. These may be different than your application's Smartcar permissions as they can be managed directly with the OEM.

<ParamField path="values" type="array" required={true}>
  An array containing permissions granted by the connecting account with the OEM.
</ParamField>

```json Example theme={null}
{
  "values": [
    "vehicle_cmds",
    "vehicle_device_data"
  ]
}
```

### Role

Signal code: `vehicleuseraccount-role`

Indicates the access level to the vehicle for the connecting account as defined by the OEM. While the OEM representation may vary, these can be thought of as "secondary" and "primary" accounts where "secondary" accounts may have more limited access than an "primary" account. "secondary" accounts are granted access to vehicle by "primary" accounts.

<ParamField path="value" type="string" required={false} />

```json Example theme={null}
{
  "value": "Driver"
}
```
