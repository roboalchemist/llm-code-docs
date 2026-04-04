# Source: https://smartcar.com/docs/errors/api-errors/vehicle-state-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vehicle State Errors

> Thrown when a request fails due to the state of a vehicle or logically cannot be completed e.g. you can't start a vehicle charging if it's not plugged in.

# `ASLEEP`

The vehicle is in a sleep state and temporarily unable to perform your request. Either the vehicle has been inactive for a certain period of time (time periods vary between makes and models) or the user has manually triggered the vehicle’s sleep state.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "ASLEEP",
  "description": "The vehicle is in a sleep state and temporarily unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#asleep",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is in a sleep state. This request was not sent to preserve battery life. "
}
```

### Suggested resolution

The vehicle is in a sleep state and temporarily unable to perform your request.

### Troubleshooting Steps

* Prompt the user to start the vehicle’s engine (required) and to drive the vehicle for a short distance (optional).
* Wait for a few minutes and retry your request.
* Ensure that the vehicle’s 12-volt battery is sufficiently charged.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please start your car and take it for a short drive.

***

# `CHARGING_IN_PROGRESS`

The vehicle is currently charging and unable to perform your request. This error usually occurs when you make a request to the start charge endpoint while the vehicle is already charging.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_IN_PROGRESS",
  "description": "The vehicle is currently charging and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-in-progress",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is already charging."
}
```

### Suggested resolution

You usually don’t need to resolve this error. If you believe that this error should not have occurred, please follow the troubleshooting steps below.

### Troubleshooting Steps

* Prompt the user to stop charging their vehicle and/or unplug the charger.
* Wait for a few minutes and retry your request.

### Suggested user message

> Your car is already charging.

***

# `CHARGING_PLUG_CONNECTED`

The vehicle is connected to an EV charger and unable to perform your request.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_PLUG_CONNECTED",
  "description": "The vehicle is connected to an EV charger and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-plug-connected",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "We’re unable to issue the command because the vehicle is currently plugged in."
}
```

### Suggested resolution

The user can resolve this error by unplugging the vehicle.

### Suggested user message

> We're unable to issue the command because the vehicle is currently plugged in. Please ensure that you have unplugged the vehicle from an EV charger.

***

# `CHARGING_PLUG_NOT_CONNECTED`

The vehicle is not connected to an EV charger and unable to perform your request. This error usually occurs when you make a request to the start charge endpoint
but the vehicle’s charge port does not have an EV charger plugged into it.

If testing an electric vehicle with Vehicle Simulator, you will receive this error when attempting a start or stop charge request while the vehicle is in a parked
or driving state (not charging).

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGING_PLUG_NOT_CONNECTED",
  "description": "The vehicle is not connected to an EV charger and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charging-plug-not-connected",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is not plugged in."
}
```

### Suggested resolution

The user can resolve this error by plugging an EV charger into the vehicle’s charge port.

### Troubleshooting Steps

* Prompt the user to plug an EV charger into the vehicle’s charge port.
* If this doesn’t resolve the issue, prompt the user to ensure that the EV charger is connected to a working power source, that it isn’t faulty, and that it is compatible with the user’s vehicle. For example, prompt the user to try out other EV chargers and to check the vehicle’s owner manual for a list of compatible chargers.

### Suggested user message

> Your car isn’t able to start charging. Please ensure that you have plugged an EV charger into your car’s charge port.

***

# `DOOR_OPEN`

The vehicle could not perform your request because one or more of its doors are open. This error usually occurs when you make a request to the lock endpoint while one or more of the vehicle’s doors stand open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "DOOR_OPEN",
  "description": "The vehicle could not perform your request because one or more of its doors are open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#door-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to lock. Please ensure that all doors and the trunk are fully closed."
}
```

### Suggested resolution

The user can resolve this error by fully closing all of the vehicle’s doors and the trunk.

### Troubleshooting Steps

* Prompt the user to ensure that there is nothing preventing the doors from fully closing and/or locking properly.
* Prompt the user to ensure that the vehicle’s trunk is fully closed.

### Suggested user message

> Your car was unable to lock. Please ensure that all doors and the trunk are fully closed.

***

# `FULLY_CHARGED`

The vehicle is unable to perform your request because its EV battery is fully charged. This error usually occurs when you make a request to the start charge endpoint while the vehicle is already fully charged.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "FULLY_CHARGED",
  "description": "The vehicle is unable to perform your request because its EV battery is fully charged.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#fully-charged",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is already fully charged."
}
```

### Suggested user message

> Your car is already fully charged.

***

# `NOT_CHARGING`

The vehicle is unable to perform your request because it is not currently charging. This error usually occurs when you request information about a vehicle’s charge session while the battery is not charging.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "NOT_CHARGING",
  "description": "The vehicle is unable to perform your request because it is not currently charging.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#not-charging",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Please ensure that you have plugged an EV charger into your car’s charge port and the vehicle is charging."
}
```

### Suggested resolution

You can resolve this error by having the user start a charge session or by sending a start charge request if the vehicle supports that capability.

### Troubleshooting Steps

* Prompt the user to start charging their vehicle.
* Wait for a few minutes and retry your request.

### Suggested user message

> Please ensure that you have plugged an EV charger into your car’s charge port and the vehicle is charging.

***

# `CHARGE_FAULT`

The vehicle is connected to an EV charger but cannot perform the request because:

* the charger is not providing any current
* there is a conflict with another charging schedule

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "CHARGE_FAULT",
  "description": "The vehicle is connected to an EV charger but cannot perform the request because 1) the charger is not providing any current, or 2) there is a conflict with another charging schedule.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#charge-fault",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to start or stop charging because of a conflict with the vehicle's charging schedule."
}
```

### Suggested resolution

The user can resolve this error by:

* Disabling any schedules that control when the charger can supply current and charge the vehicle.
* Ensuring that the charging cable is securely connected to the vehicle.
* Disabling any charge schedules on the vehicle’s infotainment system or connected service application.
* Disabling any departure timers on the vehicle’s infotainment system or connected service application.
* Removing the vehicle from other charge scheduling services.

### Troubleshooting Steps

* Prompt the user to start charging their vehicle.
* Wait for a few minutes and retry your request.

### Suggested user message

> Your car is unable to start or stop charging because of a conflict with your vehicle’s charging schedule. Please check that:
>
> * You have disabled any schedules that control when your charger is able to supply current to and charge the vehicle.
> * The charging cable is securely connected to your vehicle.
> * You have disabled any charge schedules on your vehicle’s infotainment system or connected service application.
> * You have disabled any departure timers on your vehicle’s infotainment system or connected service application.
> * Your vehicle is not connected to any other charge scheduling services.

***

# `HOOD_OPEN`

The vehicle is unable to perform your request because its hood is open. This error usually occurs when you make a request to the lock endpoint while the vehicle’s hood stands open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "HOOD_OPEN",
  "description": "The vehicle is unable to perform your request because its hood is open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#hood-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to lock. Please ensure that the vehicle's hood is fully closed."
}
```

### Suggested resolution

The user can resolve this error by ensuring that the vehicle’s hood is fully closed.

### Suggested user message

> Your car was unable to lock. Please ensure that your car’s hood is fully closed.

***

# `IGNITION_ON`

The vehicle was unable to perform your request because its engine is running. Depending on the vehicle’s make and model, this error can occur for a variety of API endpoints.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "IGNITION_ON",
  "description": "The vehicle was unable to perform your request because its engine is running.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#ignition-on",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is currently running."
}
```

### Suggested resolution

The user can resolve this error by turning off their vehicle. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name> because its engine is running. To re-establish the connection, please turn off your car’s engine.

***

# `IN_MOTION`

The vehicle is currently in motion and unable to perform your request. Depending on the vehicle’s make and model, this error can occur for a variety of API endpoints. The lock/unlock endpoint is a common example.

If testing with Vehicle Simulator, you will receive this error when attempting a lock/unlock request while the vehicle is in a driving state along the simulation.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "IN_MOTION",
  "description": "The vehicle is currently in motion and unable to perform your request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#in-motion",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to perform the request while in motion."
}
```

### Suggested resolution

The user can resolve this error by parking their car and turning off the engine. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is in motion and temporarily unable to connect to \<app name>. To re-establish the connection, please park your car and turn off its engine.

***

# `REMOTE_ACCESS_DISABLED`

The vehicle is unable to perform your request because the user has disabled remote access for connected services.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "REMOTE_ACCESS_DISABLED",
  "description": "The vehicle is unable to perform your request because the user has disabled remote access for connected services.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#remote-access-disabled",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is unable to perform the request as remote access is disabled or unavailable."
}
```

### Suggested resolution

The user can resolve this error by re-enabling remote access inside their vehicle. If the user is unsure how to enable remote access for connected services, prompt them to refer to their vehicle’s owner manual for more details.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please make sure that remote access for connected services is enabled inside your car. Please refer to your car’s owner manual for more details.

***

# `TRUNK_OPEN`

The vehicle is unable to perform your request because its trunk is open. This error usually occurs when you make a request to the lock endpoint while the vehicle’s trunk and/or front trunk are open.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "TRUNK_OPEN",
  "description": "The vehicle is unable to perform your request because its trunk is open.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#trunk-open",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle was unable to open the trunk because it is already open."
}
```

### Suggested resolution

The user can resolve this error by closing the vehicle’s trunk and/or front trunk.

### Suggested user message

> Your car was unable to lock. Please ensure that your car’s trunk (and front trunk) is closed.

***

# `UNKNOWN`

The vehicle was unable to perform your request due to an unknown issue. This error occurs when the vehicle is in a state that makes it unable to perform your request, and we are unable to determine which state the vehicle is in.

If testing an electric vehicle with Vehicle Simulator, you will receive this error when attempting a stop charge request while the vehicle is in a charging state.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "UNKNOWN",
  "description": "The vehicle was unable to perform your request due to an unknown issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#unknown",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect due to an unknown issue. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

Please retry your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `UNREACHABLE`

The vehicle was unable to perform your request because it is currently unreachable. This error usually occurs when the vehicle is in a location with poor cellular reception (e.g. a parking garage or underground parking).

If testing with Vehicle Simulator, you will receive this error when attempting a lock/unlock or start/stop charge request while the simulation is paused or completed.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "UNREACHABLE",
  "description": "The vehicle was unable to perform your request because it is currently unreachable.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#unreachable",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is currently unreachable. Ensure the vehicle has adequate mobile coverage."
}
```

### Suggested resolution

The user can resolve this error by moving the vehicle to a location with better cellular reception. You can also resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. To re-establish the connection, please move your car to a location with a better cell phone signal.

***

# `VEHICLE_OFFLINE_FOR_SERVICE`

The vehicle was unable to perform your request because it is currently in service mode. Service mode temporarily limits or disables the vehicle’s remote capabilities.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "VEHICLE_OFFLINE_FOR_SERVICE",
  "description": "The vehicle was unable to perform your request because it is currently in service mode.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#vehicle-offline-for-service",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is in service mode and temporarily unable to perform this task."
}
```

### Suggested resolution

Please retry your request at a later time.

### Suggested user message

> Your car is in service mode and temporarily unable to connect to \<app name>. Please try again later.

***

# `LOW_BATTERY`

The vehicle was unable to perform your request because the 12v or high voltage battery is too low.

```json  theme={null}
{
  "type": "VEHICLE_STATE",
  "code": "LOW_BATTERY",
  "description": "The vehicle was unable to perform your request because the 12v or high voltage battery is too low.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/vehicle-state-errors#low-battery",
  "statusCode": 409,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle battery is too low to perform this task."
}
```

### Suggested resolution

Please retry your request at a later time.

* For EVs ensure that the battery is topped up to at least 60% SoC.
* Ensure that the vehicle’s 12-volt battery is sufficiently charged. Taking the vehicle on a short drive can help.

### Suggested user message

> \<app name> was unable to connect to your car because its battery is too low. Please ensure the battery is charged and try again later.

***
