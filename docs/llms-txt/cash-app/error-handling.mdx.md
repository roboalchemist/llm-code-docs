# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-handling.mdx

***

## stoplight-id: 3e58304fa25c0

# Error Handling

## What do errors look like in the Cash App Pay API?

The Cash App Pay API follows a standard pattern for representing errors in API responses:

1. A non HTTP 2XX response code is returned (typically a 4XX or 5XX)
2. An array of errors is present under the `errors` field at the top level of the response (see the sample below)

### Example Error

```json
{
  "errors": [
    {
      "category": "INVALID_REQUEST_ERROR",
      "code": "MISSING_REQUIRED_FIELD",
      "detail": "Missing required parameter 'amount'",
      "field": "amount"
    }
  ]
}
```

## How should I check for errors in my code?

The simplest way to check for errors is to see if a non HTTP 2XX code was returned. If a non HTTP 2XX code was returned, you can then log the `errors` array to get more information about what went wrong.

PII (personally identifiable information) will never be present in the errors, so you don't need to worry about scrubbing them before logging.

## What errors do I need to handle as part of my integration?"

There are different types of errors that can be returned by the API, each of which should be handled differently.

### Errors you need to handle

* [**Payment processing errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#payment-processing-errors) indicate that a payment or refund was declined. **You need to handle these errors in your integration.** Dealing with declined payments or deactivated customers is something your integration will need to do on a regular basis, and should elegantly handle these failures.

* [**Grant errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#grant-errors) can occur when a customer revokes an on-file payment grant in Cash App, causing on-file payments to fail. **You need to handle these errors in your integration.** This is considered a common use case, and your integration should elegantly handle it.

* [**API errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#api-errors) indicate that something is wrong with the Cash App Pay APIs themselves. An integration should consider itself degraded if these errors are encountered, and temporarily remove the Cash App Pay functionality from their websites and / or point of sale devices.

### Errors that indicate bugs in the integration

* [**Authentication errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#authentication-errors) indicate that the integration has faulty authorization headers set, or isn't managing API key rotation properly. This should be caught at development time, and should never be present in a production integration. Integrations shouldn't expect to handle these errors.

* [**Invalid request errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#validation-errors) indicate that the integration is sending invalid requests to the API. These errors should be caught at development time, and should never be present in a production integration. Integrations shouldn't expect to handle these errors.

* [**Rate limit errors**](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#rate-limit-errors) indicate that the integration is making requests too quickly to the Cash App Pay API. You should either lower the number of requests you're making to the API, or reach out to Cash App Pay support to get the limits raised. Note that payment processing and merchant registration endpoints are never rate limited - only reporting and management endpoints are.
