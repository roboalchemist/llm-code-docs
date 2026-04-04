# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/idempotency.mdx

***

## stoplight-id: a7cb5d06697a1

# Idempotency

How to work with idempotency keys and support retries without creating duplicate data

## What is idempotency?

Idempotency refers to the ability to call an endpoint multiple times and receive the same result, without causing additional side effects.

### Example: Handling a server error while creating a payment

When processing a payment, we want to prevent double-charging customers. Consider the following scenario, where an intermittent error in the Cash App Pay API requires the API client to retry a request:

![what-is-idempotency.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/what-is-idempotency.png)

1. API client tries to create a payment
2. Cash App Pay API responds with `HTTP 500`
3. API client retries creating a payment
4. Cash App Pay API responds with `HTTP 201 `

When the `HTTP 500` is returned, the API client doesn't know if a payment was created or not, because it doesn't have visibility into the cause of the error.

To prevent duplicates, the Cash App Pay API requires the API client to provide an `idempotency_key`, which acts as a unique identifier for the payment creation request. When the API client retries the request, if Cash App Pay already finds an existing payment created with the given `idempotency_key`, it will return it instead of creating one.

<Warning title="Very important">
  Idempotency keys are case-sensitive! Remember to verify the case-sensitivty of your 

  `idempotency_key`

   to avoid any issues or while troubleshooting.
</Warning>

## How do I generate an idempotency key?

Idempotency keys must be **1 to 64 characters long** and **unique** across all requests made to a single endpoint. We recommend using UUIDs for this, but any string that fits the requirements will work.

## How does the Cash App Pay API handle idempotency?

Every endpoint in the Cash App Pay API is idempotent, either implicitly (i.e., read operations) or explicitly (where an idempotency key is required).

<Warning>Idempotency keys are scoped to regions: Idempotency in the API is scoped to the `X-Region` header (see [Regions](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/regions-and-localization) for more info) provided in the request. This allows Cash App Pay to run in multiple regions at once and achieve higher availability and lower latencies.<br /><br />**Example:** <br /><br />With an `X-Region` of `PDX`, an API client creates an on file payment. The API client then retries the request with an `X-Region` of `IAD` <br />**Outcome:** 2 payments are created.<br /><br />*Make sure to always retry requests using the same X-Region header!*</Warning>
For all endpoints where an idempotency key is required, the Cash App Pay API will:

* **Scope the idempotent processing to the given `X-Region`**. Idempotency is not guaranteed to span across regions. If a request is retried with a different `X-Region` header, it may create duplicate data.
* **Enforce that an idempotency key is only associated with one payload.** If the payload is changed and the idempotency key stays the same, an [`IDEMPOTENCY_KEY_REUSED` error](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference#common-runtime-errors) is returned.
* **Cache HTTP 2XX responses and [permanent HTTP 4XX errors](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference)** for at least 30 days and return them on subsequent requests with the same idempotency key.
