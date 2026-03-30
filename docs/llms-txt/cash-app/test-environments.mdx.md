# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/test-environments.mdx

***

## stoplight-id: 5vnq7vdlmpwit

# Test environments

## Sandbox

Cash App Afterpay provides a sandbox environment for development and testing. Your Cash App Afterpay account manager will provide you with sandbox credentials.

Accounts created within a Cash App Afterpay sandbox only exist within the sandbox. When you make a transaction in the sandbox, no money actually moves.

API calls in the sandbox use the base URL `https://global-api-sandbox.afterpay.com`.

### Sandbox Business Hub

Contact your Cash App Afterpay account manager or delivery manager to request access to the sandbox Business Hub. The sandbox Business Hub provides the same functionality as the production Business Hub.

You can log into the sandbox Business Hub at [https://portal.sandbox.afterpay.com/merchant/](https://portal.sandbox.afterpay.com/merchant/)

You can view all sandbox orders and settlement files, but no settlements are made to your bank account.

### Test customer accounts

You can create test customer accounts in the sandbox environment within your test checkout flow. Each customer account requires a unique email address and phone number.

<Note>
  No SMS messages are sent in the sandbox. Use `111111` as the verification code.
</Note>

### Test credit cards

The sandbox capture response (approved/declined) is determined by the CVV value. Use `000` for approval and `051` for decline.

You can use any dummy Visa or Mastercard number and future expiry date,  as long as it passes a mod 10 check and hasn’t already been used by a different sandbox customer account. You can also use these dummy cards:

| Card Type  | Card Number         | Expiry | CCV | Response |
| ---------- | ------------------- | ------ | --- | -------- |
| Visa       | 4111 1111 1111 1111 | 01/28  | 000 | Approved |
| Visa       | 4111 1111 1111 1111 | 01/28  | 051 | Declined |
| Mastercard | 5215 0977 9282 6659 | 01/28  | 000 | Approved |
| Mastercard | 5215 0977 9282 6659 | 01/28  | 051 | Declined |

### Test Pay Monthly

The Sandbox Pay Monthly Approval response (approved/declined) is determined by the Cart Total value.

| Cart Total Value           | Response                  |
| -------------------------- | ------------------------- |
| $100.00 - $399.99 USD      | 3, 6, or 12 month offers  |
| $400.00 - $3,999.99 USD    | 6, 12, or 24 month offers |
| $4,000.00 - $10,000.00 USD | 6, 12, or 24 month offers |

## Postman collection

You can test the Cash App Afterpay API using Postman, a free-to-download tool for making HTTP requests. To start using Postman, create an account on [postman.com](https://www.postman.com/).

To test the Cash App Afterpay API using postman:

1. Go to the [Afterpay Online API V2](https://www.postman.com/afterpay-1-426879/afterpay-online-apis-v2/overview) public workspace.
2. Fork the collection.
3. Choose a label, workspace, and environment for your fork.
4. Regularly pull the latest changes to update your forked collection.
