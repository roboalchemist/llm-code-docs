# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-android/advanced-operations.mdx

# Pay Kit Android: Advanced Operations

<Tip>
  See [Getting Started with the Pay Kit Android SDK](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-android) first to get set up.
</Tip>

## Existing customer requests

When you use `createCustomerRequest`, the system returns a `CustomerResponseData` object. This object contains the `Request ID`.

<Note>
  If required, you can save this ID to retrieve the request at a later time.
</Note>

For existing customer requests, start the SDK by calling `startWithExistingCustomerRequest` and pass the `Request ID`.

```kotlin
cashAppPay.startWithExistingCustomerRequest(customerRequestID)
```

<Note>
  * You must call this function *only* when you start on a new SDK instance.
  * You must register for state updates before calling this function.
</Note>

## Update an existing customer request

Update an existing customer request by calling `updateCustomerRequest` and passing in the `Request ID` and a new `CashAppPayPaymentAction` object.

```kotlin
fun updateCustomerRequest(
    requestId: String,
    paymentAction: CashAppPayPaymentAction,
)
```

Use this function only after you've already started the SDK with a customer request.
