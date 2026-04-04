# Source: https://smartcar.com/docs/errors/api-errors/server-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Errors

> Thrown when Smartcar runs into an unexpected issue and was unable to process the request.

# `INTERNAL`

An internal Smartcar error has occurred. Our team has been notified and is working to resolve this issue.

```json  theme={null}
{
  "type": "SERVER",
  "code": "INTERNAL",
  "description": "An internal Smartcar error has occurred. Our team has been notified and is working to resolve this issue.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#internal",
  "statusCode": 500,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested Resolution

Please contact us to learn more about the error and our steps to resolve it.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `RECORD_NOT_FOUND`

Smartcar is unable to locate a battery capacity record for this vehicle. Depending on the make of the vehicle, battery capacity may depend on upstream sources to fulfil a request if it is not directly provided by the OEM.

If you’re seeing this error then the OEM doesn’t provide all the data we aim to provide in our response and we were unable to locate this information from other sources.

```json  theme={null}
{
  "type": "SERVER",
  "code": "RECORD_NOT_FOUND",
  "description": "Smartcar was unable to locate a battery capacity record for this vehicle.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#record-not-found",
  "statusCode": 500,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "CONTACT_SUPPORT" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested Resolution

Please reach out to support to see if we are able to update capacity data for the vehicle.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `MULTIPLE_RECORDS_FOUND`

Smartcar is unable to locate a battery capacity record for this vehicle. Depending on the make of the vehicle, battery capacity may depend on upstream sources to fulfil a request if it is not directly provided by the OEM.

If you’re seeing this error then the OEM doesn’t provide all the data we aim to provide in our response and we were unable to find a specific match. Please see the error response `detail` field for possible matches.

```json  theme={null}
{
	"statusCode": 500,
	"type": "SERVER",
	"code": "MULTIPLE_RECORDS_FOUND",
	"description": "Smartcar found multiple battery capacity records for this vehicle.",
	"docURL": "https://smartcar.com/docs/errors/api-errors/server-errors#multiple-records-found",
	"resolution": {
		"type": "CONTACT_SUPPORT"
	},
	"suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue.",
	"detail": [
		{
			"capacities": [83.9, 83.9, 70.2]
		}
	],
	"requestId": "9c8dd6fa-f9d7-4d18-9fdd-2255f6cd8613"
}
```

### Suggested Resolution

For battery capacity errors please check the detail field of the error response for a list of possible options and reach out support if you need us to update the capacity value for a specific vehicle.

### Suggested User Message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.
