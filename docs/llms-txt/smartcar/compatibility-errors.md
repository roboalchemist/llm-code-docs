# Source: https://smartcar.com/docs/errors/api-errors/compatibility-errors.md

# Compatibility Errors

> Thrown when Smartcar does not support a make, or feature for a vehicle.

# `MAKE_NOT_COMPATIBLE`

Smartcar is not yet compatible with this vehicle’s make in the country you specified.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "MAKE_NOT_COMPATIBLE",
  "description": "Smartcar is not yet compatible with this vehicle’s make in the country you specified.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#make-not-compatible",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Suggested User Messaging**<br />
`<your app name>` is not yet able to connect to your car brand.

<br />

# `PLATFORM_NOT_CAPABLE`

You're connected to the vehicle using an OEM integration that does not support this endpoint. This can be a result of the OEM migrating to a newer API or requiring vehicle owners to migrate to a new application they have released.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "PLATFORM_NOT_CAPABLE",
  "description": "You're connected to the vehicle using an OEM integration that does not support this endpoint.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#platform-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "REAUTHENTICATE" } 
}
```

**Troubleshooting Steps**<br />
For Tesla vehicles please have the owner re-authenticate using the latest Tesla authorization flow.

<br />

# `SMARTCAR_NOT_CAPABLE`

Smartcar does not yet support this feature for this vehicle.

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "SMARTCAR_NOT_CAPABLE",
  "description": "Smartcar does not yet support this feature for this vehicle.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#smartcar-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Troubleshooting Steps**<br />
Please check that the vehicles make and engine type support the feature you are trying to use.

Please contact us to learn when this feature will become available.
If you have a vehicle that supports this feature and would like to help out, check out Smartcar’s Research Fleet.

<br />

# `VEHICLE_NOT_CAPABLE`

This error occurs when a physical limitation makes the vehicle incapable of performing your request
(e.g. battery electric vehicles are incapable of responding to read fuel requests).

```json  theme={null}
{
  "type": "COMPATIBILITY",
  "code": "VEHICLE_NOT_CAPABLE",
  "description": "The vehicle is incapable of performing your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/compatibility-errors#vehicle-not-capable",
  "statusCode": 501,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

**Suggested User Messaging**<br />
Your car is unable to perform this request.

<br />
