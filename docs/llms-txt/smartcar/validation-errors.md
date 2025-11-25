# Source: https://smartcar.com/docs/errors/api-errors/validation-errors.md

# Validation Errors

> Thrown if there is an issue with the format of the request or body.

# `NULL`

Request invalid or malformed. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.

```json  theme={null}
{
  "type": "VALIDATION",
  "code": null,
  "description": "Request invalid or malformed. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/validation-errors#null",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified.

### Troubleshooting Steps

* Ensure that you spell and case all parameters correctly.

* Ensure that your request has the correct content-type (i.e. application/json or application/x-www-form-urlencoded).

* Ensure that your request has the correct URL and HTTP method.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `PARAMETER`

Your request is formatted correctly, but one or more of the provided parameters is incorrect.

```json  theme={null}
{
  "type": "VALIDATION",
  "code": null,
  "description": "Your request is formatted correctly, but one or more of the provided parameters is incorrect.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/validation-errors#parameter",
  "statusCode": 400,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified.

For Ford or Lincoln vehicles:

* Please check the coordinates provided for setting a charge schedule are associated with a saved charging location for this vehicle.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.
