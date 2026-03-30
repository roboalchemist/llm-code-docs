# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/optimizing-performance-with-request-chaining.mdx

***

## stoplight-id: je4o1jepzulaj

# Optimizing Performance with Request Chaining

If you send multiple consecutive API requests, consider using request chaining to improve performance. Request chaining allows you to combine multiple requests into a single API call. Since all requests stay within Cash App's infrastructure, it significantly reduces roundtrip latency.

<Note>
  In internal test, chaining 3 requests—create brand, create merchant, and create customer —reduced latency by 50–70%. Actual performance gains may vary, depending on your infrastructure and the number of requests chained.
</Note>

Example usage:

* Create Brand > Create Merchant > Create Customer Request
* Upsert Brand > Upsert Merchant > Create Payment
* Retrieve Fee Plan > Upsert Merchant
* Create API Key > Update Webhook Endpoint

<Note>
  For example code snippets and implementation details, see the request chaining [API page](/cash-app-pay-partner-api/api-reference/management-api/create-request-chain).
</Note>

## Request chaining errors

### What happens if there's an error making a request?

It depends on where the error occurred, for example:

* If the error happened at the requested endpoint, such as while creating a brand, then request chaining will stop executing subsequent requests. It will return the error in the list of responses and all subsequent requests will be marked as `not started`.
* If the error happened in the request chaining logic, such as accessing a previous response's value, then it will return a validation error with a status code `400`.
