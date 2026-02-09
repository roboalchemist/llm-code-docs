# Source: https://smartcar.com/docs/errors/api-errors/permission-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Permission Errors

> Thrown when Smartcar does not support a make or feature for a vehicle.

# `NULL`

Your application has insufficient permissions to access the requested resource. Please prompt the user to re-authenticate using Smartcar Connect.

If you receive this error while testing with Vehicle Simulator, it is likely because the simulated vehicle has not yet been connected to your application, or your application doesn't have access to the requested permission.
Visit the Simulator documentation to learn how to connect the vehicle to your application.

```json  theme={null}
{
  "type": "PERMISSION",
  "code": null,
  "description": "Your application has insufficient permissions to access the requested resource. Please prompt the user to re-authenticate using Smartcar Connect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/permission-errors#null",
  "statusCode": 403,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "REAUTHENTICATE" }  
}
```

### Suggested Resolution

You can resolve this error by ensuring that the scope parameter contains all the permissions that your application requires and prompting the user to re-authenticate using Smartcar Connect.

### Troubleshooting Steps

* Ensure that the scope parameter contains all the permissions that your application requires.
* Ensure that you spell all permission names in the scope parameter correctly.
* Prompt the user to re-authenticate using Smartcar Connect.
