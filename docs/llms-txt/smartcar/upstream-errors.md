# Source: https://smartcar.com/docs/errors/api-errors/upstream-errors.md

# Upstream Errors

> Thrown when the OEM servers or vehicle failed to process the request.

<Info>
  <b>Check Smartcar Reliability & Status</b><br />
  For upt-to-date information on Smartcar's platform and brand reliability, visit our:

  <ul>
    <li><a href="https://brandreliability.smartcar.com/" target="_blank" rel="noopener">Brand Reliability page</a></li>
    <li><a href="https://status.smartcar.com/" target="_blank" rel="noopener">Platform Status page</a></li>
  </ul>
</Info>

# `INVALID_DATA`

One of Smartcar’s upstream sources provided data that is malformed, invalid, or logically invalid (e.g. 65535 psi for tire pressure).

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "INVALID_DATA",
  "description": "Smartcar received invalid data from an upstream source. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#invalid-data",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `KNOWN_ISSUE`

Smartcar received an error from an upstream source. This error usually occurs when an upstream source experiences an error that we have previously investigated and categorized as a known issue.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "KNOWN_ISSUE",
  "description": "Smartcar received an error from an upstream source. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#known-issue",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue." 
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `NO_RESPONSE`

One of Smartcar’s upstream sources failed to respond. This error usually occurs when one of Smartcar’s upstream sources is experiencing issues and is currently unavailable.
This error can also occur when a specific vehicle in located in an area with weak cellular reception and fails to respond to your request in a timely manner.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "NO_RESPONSE",
  "description": "One of Smartcar’s upstream sources failed to respond. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#no-response",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by retrying your request at a later time.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `RATE_LIMIT`

Your application’s requests have exceeded this vehicle’s rate limit.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "NO_RESPONSE",
  "description": "One of Smartcar’s upstream sources failed to respond. Please retry your request at a later time.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#rate-limit",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

You can resolve this error by refraining from making API requests to this specific vehicle for a period of time.
If your application automatically retries requests, please disable automatic retries or implement a backoff period to retry less frequently.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***

# `UNKNOWN_ISSUE`

Smartcar received an unknown error from an upstream source. This error usually occurs when one of Smartcar’s upstream sources experiences an error that we have not yet investigated or mitigated.

There are several reasons why we might not have investigated this error yet:

* The feature or vehicle make is still in beta.
* This error does not occur very frequently.
* This is the first time we have received this error.

```json  theme={null}
{
  "type": "UPSTREAM",
  "code": "UNKNOWN_ISSUE",
  "description": "Smartcar received an unknown error from an upstream source. Please retry your request at a later time and contact us if the issue persists.",
  "docURL": "https://smartcar.com/docs/errors/api-errors/upstream-errors#unknown-issue",
  "statusCode": 502,
  "requestId": "5dea93a1-3f79-4246-90c5-89610a20471b",
  "resolution": { "type": "RETRY_LATER" },
  "suggestedUserMessage": "Your car is temporarily unable to connect to <app name>. Please be patient while we’re working to resolve this issue."
}
```

### Suggested resolution

Given the broad range of situations that can cause this error, you might or might not be able to resolve this error by retrying your request at a later time.
If you retry your request and the issue persists, please contact us to help you mitigate this error.

### Suggested user message

> Your car is temporarily unable to connect to \<app name>. Please be patient while we’re working to resolve this issue.

***
