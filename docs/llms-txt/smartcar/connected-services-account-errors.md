# Source: https://smartcar.com/docs/errors/api-errors/connected-services-account-errors.md

# Connected Services Account Errors

> Thrown when there are issues with the user's connected service account.

# `ACCOUNT_ISSUE`

Action needed in the user’s connected services account. The user needs to log in and complete an outstanding task in their connected services account.

Examples:

* The user needs to accept the connected services app’s Terms of Service.
* The user has created but not yet fully activated their connected services account.
* If you've received this error while testing with Vehicle Simulator, it likely means a simulation has not been started for the vehicle. Visit the Simulator tab in the Smartcar Dashboard to start a simulation for the vehicle.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "ACCOUNT_ISSUE",
  "description": "Action needed in the user’s connected services account. Please prompt the user to log into their connected services account and complete any outstanding tasks.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#account-issue",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Action required in your connected services account. Please log into your connected services app or web portal and complete any outstanding tasks (e.g. finish activating your account or accept the Terms of Service)." 
}
```

### Suggested resolution

The user can resolve this error by logging into their connected services account and completing any outstanding tasks.

### Troubleshooting steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to try triggering an action on their car, e.g. locking the doors or flashing the lights.
* At this point, the app should prompt the user to complete their outstanding task.

### Suggested user message

> Action required in your connected services account. Please log into your connected services app or web portal and complete any outstanding tasks (e.g. finish activating your account or accept the Terms of Service).

***

# `AUTHENTICATION_FAILED`

Smartcar was unable to authenticate with the user’s connected services account. This error usually occurs when the user has updated their connected
services account credentials and not yet re-authenticated in Smartcar Connect. The user should re-authenticate using Smartcar Connect.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "AUTHENTICATION_FAILED",
  "description": "Smartcar was unable to authenticate with the user’s connected services account. Please prompt the user to re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#authentication-failed",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
    "type": "REAUTHENTICATE",
    "url": "https://connect.smartcar.com/oauth/reauthenticate?response_type=vehicle_id&client_id=8229df9f-91a0-4ff0-a1ae-a1f38ee24d07&vehicle_id=sc4a1b01e5-0497-417c-a30e-6df6ba33ba46"
  },
  "suggestedUserMessage": "Your car got disconnected from <app name>. Please use this link to re-connect your car: <link to Smartcar Connect>."
}
```

### Suggested resolution

Please provide the user with a link to Smartcar Connect Re-authentication and prompt them to re-connect their vehicle.
The resolution field contains a partially constructed URL for Smartcar Connect Re-authentication, please see the API reference for more detail.

### Suggested user message

> Your car got disconnected from \<app name>. Please use this link to re-connect your car: \<link to Smartcar Connect>.

***

# `NO_VEHICLES`

No vehicles found in the user’s connected services account. The user might not yet have added their vehicle to their account, or they might not yet have activated connected services for the vehicle.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "NO_VEHICLES",
  "description": "No vehicles found in the user’s connected services account. Please prompt the user to add their vehicle to their connected services account and re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#no-vehicles",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null }, 
  "suggestedUserMessage": "Your car got disconnected from <app name>. Please use this link to re-connect your car: <link to Smartcar Connect>."
}
```

### Suggested resolution

Please provide the user with a link to Smartcar Connect Re-authentication and prompt them to re-connect their vehicle.
The resolution field contains a partially constructed URL for Smartcar Connect Re-authentication, please see the API reference for more detail.

### Troubleshooting Steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to check whether there are any vehicles listed in their account.
* If there are no vehicles listed, prompt the user to add their vehicle.
* If there are one or more vehicles listed, this means that none of the vehicles have had their connected services activated. Prompt the user to activate connected services for at least one vehicle.
* Provide the user with a link to Smartcar Connect and prompt them to re-connect their vehicle.

### Suggested user message

> Your car got disconnected from \<app name>. Please use this link to re-connect your car: \<link to Smartcar Connect>.

***

# `PERMISSION`

This error occurs when a vehicle owner had initially granted Smartcar access to their OEM account, but has since revoked it via the OEM's management portal.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "PERMISSION",
  "description": "The vehicle owner has revoked Smartcar’s access to their OEM account.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#permission",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
	  "type" : "REAUTHENTICATE"
  }
}
```

### Suggested resolution

For Tesla Owners:

* Prompt the vehicle owner to go through the Connect flow again or use our [reauthentication flow](/help/oem-integrations/tesla/developers#stand-alone-flow) to streamline the process.

***

# `SUBSCRIPTION`

The vehicle’s connected services subscription is inactive or does not support the requested API endpoint.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "SUBSCRIPTION",
  "description": "The vehicle’s connected services subscription is inactive or does not support the requested API endpoint.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#subscription",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to <app name>. Please activate your subscription or contact us to upgrade your subscription."
}
```

### Suggested resolution

The user can resolve this error by logging into their connected services account and either (re-)activating their subscription or purchasing the required subscription package.

### Troubleshooting Steps

If you don’t know which subscription package the user needs to purchase, please contact our team for help.

### Suggested user message

> Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to \<app name>. Please activate your subscription or contact us to upgrade your subscription.

***

# `VEHICLE_MISSING`

This vehicle is no longer associated with the user’s connected services account. The user might have removed it from their account.
The user needs to log into their connected services account and either re-add the vehicle or re-activate its subscription.

If you've received this error while testing with Vehicle Simulator, it likely means the simulated vehicle has not been found in your application. Visit the Simulator tab in the Smartcar Dashboard to create a simulated vehicle to test with.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "VEHICLE_MISSING",
  "description": "This vehicle is no longer associated with the user’s connected services account. Please prompt the user to re-add the vehicle to their account.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#vehicle-missing",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car’s connected services subscription has either expired or it doesn’t support the necessary features to connect to <app name>. Please activate your subscription or contact us to upgrade your subscription."
}
```

### Suggested resolution

The user can resolve this issue by logging into their connected services account and either re-adding the vehicle or re-activating its subscription.

If the user wishes to disconnect their vehicle from your app, please make a request to our Disconnect endpoint and refrain from making API requests to this vehicle in the future.

### Troubleshooting Steps

* Prompt the user to log into their connected services account using the app or web portal.
* Prompt the user to check whether the vehicle is listed under their account.
* If the vehicle is not listed, prompt the user to add the vehicle to their account.
* If the vehicle is listed, prompt the user to activate the vehicle’s connected services subscription.

### Suggested user message

> This car is no longer associated with your connected services account. Please log into your account and re-add this car.

***

# `VIRTUAL_KEY_REQUIRED`

The vehicle owner has granted your application access to the vehicle through Smartcar. However, additional steps are needed on the owners part in order to perform this specific request.

```json  theme={null}
{
  "type": "CONNECTED_SERVICES_ACCOUNT",
  "code": "VIRTUAL_KEY_REQUIRED",
  "description": "The vehicle owner needs to grant additional access to Smartcar in order to perform this request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/connected-services-account-errors#virtual-key-required",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": {
	  "type" : "ACTION_REQUIRED",
	  "url" : "https://www.tesla.com/_ak/smartcar.com"
  }
  "suggestedUserMessage": "In order to perform this request you’ll need to add a Third-Party Virtual key to your vehicle. Please open this link on the phone with your Tesla App to complete this step."
}
```

### Suggested resolution

For Tesla Owners:

* The vehicle owner needs to add Smartcar’s Third-Party Virtual Key. As of late 2023, Tesla is starting to require virtual keys for Third-Party applications to perform commands.
* In order to issue commands, please prompt the vehicle owner to add Smartcar’s Third-Party virtual key: [https://www.tesla.com/\_ak/smartcar.com](https://www.tesla.com/_ak/smartcar.com)

### Troubleshooting steps

* Please direct the vehicle owner to add Smartcar’s [Third-Party Virtual Key (tesla.com)](https://www.tesla.com/_ak/smartcar.com) in order to allow your application to issue commands to the vehicle.

### Suggested user message

> In order to perform this request you’ll need to add a Third-Party Virtual key to your vehicle. Please open [this](https://www.tesla.com/_ak/smartcar.com) link on the phone with your Tesla App to complete this step.
