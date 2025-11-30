# Source: https://www.electronjs.org/docs/latest/api/structures/transaction

# Transaction Object

- `transactionIdentifier` string - A string that uniquely identifies a successful payment transaction.
- `transactionDate` string - The date the transaction was added to the App Storeâ€™s payment queue.
- `originalTransactionIdentifier` string - The identifier of the restored transaction by the App Store.
- `transactionState` string - The transaction state, can be `purchasing`, `purchased`, `failed`, `restored` or `deferred`.
- `errorCode` Integer - The error code if an error occurred while processing the transaction.
- `errorMessage` string - The error message if an error occurred while processing the transaction.
- `payment` Object
  - `productIdentifier` string - The identifier of the purchased product.
  - `quantity` Integer - The quantity purchased.
  - `applicationUsername` string - An opaque identifier for the userâ€™s account on your system.
  - `paymentDiscount` [PaymentDiscount](/docs/latest/api/structures/payment-discount) (optional) - The details of the discount offer to apply to the payment.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/transaction.md)