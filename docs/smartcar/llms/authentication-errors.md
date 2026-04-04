# Source: https://smartcar.com/docs/errors/api-errors/authentication-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication Errors

> Thrown when there is an issue with your authorization header.

# `NULL`

The authorization header is missing or malformed, or it contains invalid or expired authentication credentials (e.g. access token, client ID, client secret). Please check for missing parameters, spelling and casing mistakes, and other syntax issues.

```json  theme={null}
{
  "type": "AUTHENTICATION",
  "code": null,
  "description": "The authorization header is missing or malformed, or it contains invalid or expired authentication credentials. Please check for missing parameters, spelling and casing mistakes, and other syntax issues.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/authentication-errors",
  "statusCode": 401,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": null } 
}
```

### Suggested Resolution

You can resolve this error by referring to our API reference and ensuring that you pass all the parameters as specified. If you are certain that your request is well-formed, please try refreshing your access token.

### Troubleshooting Steps

Refer to our API reference and ensure that you use the correct authentication mechanism for your request

* Check constants like Bearer and Basic for spelling mistakes.
* If you make a request to a vehicle endpoint, verify that your access token grants you access to the correct vehicle. You can do so by making a request to the /vehicles endpoint and ensuring that the correct vehicle ID is included in the returned response.
* If you have refreshed your access token, make sure that it persists and that you use your new token to make your request.
