# Source: https://smartcar.com/docs/errors/api-errors/rate-limit-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limit Errors

> Thrown when there is an issue with the frequency of your requests.

# `SMARTCAR_API`

Your application has exceeded its rate limit. Please retry your request in a few minutes.

```json  theme={null}
{
  "type": "RATE_LIMIT",
  "code": "SMARTCAR_API",
  "description": "Your application has exceeded its rate limit. Please retry your request in a few minutes.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/rate-limit-errors#smartcar-api",
  "statusCode": 429,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests for a certain period of time.
If your application automatically retries requests for certain errors, please disable automatic retries or implement a backoff period to retry certain requests less frequently.

### Troubleshooting steps

If you believe that you received this error by mistake and your application didn’t actually exceed its rate limit, please contact us and we’ll be happy to assist you.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `VEHICLE`

You have reached the throttling rate limit for this vehicle. Please see the `retry-after` header (seconds) for when to retry the request.

This limit is in place to prevent excessive vehicle requests that could:

* Lead to 12v battery drain.
* Trigger UPSTREAM:RATE\_LIMIT errors that prevent you from making requests for a longer period of time.

```json  theme={null}
{
  "type": "RATE_LIMIT",
  "code": "VEHICLE",
  "description": "You have reached the throttling rate limit for this vehicle. Please see the retry-after header for when to retry the request.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/rate-limit-errors#vehicle",
  "statusCode": 429,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your vehicle is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
 
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests. Please see the retry-after header for when to try again. If your application automatically retries requests for certain errors, please disable them for this one.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***
