# Source: https://smartcar.com/docs/errors/api-errors/resource-not-found-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Resource Not Found

> Thrown when the incorrect API version is used or when the endpoint URL is incorrect.

# `PATH`

The requested resource does not exist. Please check the URL and try again.

```json  theme={null}
{
  "type": "RESOURCE_NOT_FOUND",
  "code": "PATH",
  "description": "The requested resource does not exist. Please check the URL and try again.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/resource-errors#pathh",
  "statusCode": 404,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you use the correct URL for your request.

### Troubleshooting Steps

* Ensure that you spell all static parts of the URL correctly.
* Ensure that you use the correct URL path parameters (e.g. vehicle ID).
* Ensure that you use the correct HTTP method.

***

# `VERSION`

The requested resource does not exist. Your request either does not specify a version number or it specifies a version number that is not supported by this resource.

```json  theme={null}
{
  "type": "RESOURCE_NOT_FOUND",
  "code": "VERSION",
  "description": "The requested resource does not exist. Please check your specified version number and try again.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/resource-errors#version",
  "statusCode": 404,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you specify v2.0 in the URL path (e.g. `https://api.smartcar.com/v2.0/vehicles`). Version 1 has been sunset and is no longer supported.
