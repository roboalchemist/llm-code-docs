# Integrate API

The Payouts API enables you to send payouts programmatically to your recipients. This page explains everything you need to know about making payouts using the Payouts API.

## How it works

When you initiate a payouts request, the Payouts API:

1. Validates your request and processes the payouts.
2. Sends you a status report.
3. Notifies recipients that they have a payment.

## Know before you code

- Complete the steps in [Get started](/api/rest/) to get the following sandbox account information from the Developer Dashboard:
  - Your personal and business sandbox accounts
  - Your access token
- [Request access to PayPal Payouts](https://www.paypal.com/payoutsweb/landing)
- Set up your PayPal business account for Payouts:
  - [Confirm your identity](https://www.paypal.com/policy/flow/verifyCip)
  - [Confirm your email](https://www.paypal.com/in/cshelp/article/how-do-i-confirm-my-email-address-help138)
  - [Link your bank account](https://www.paypal.com/businessexp/money/addbank)
  - Add enough money to cover your payout total, including [fees](https://www.paypal.com/us/webapps/mpp/merchant-fees#paypal-payouts)
  - You can send up to 15,000 payments in one API call.
- This integration uses the [Payouts REST API](/docs/api/payments.payouts-batch/v1/)
- Use Postman to explore and test PayPal APIs.

## Step result

A successful request returns:

- A return status code of HTTP 201 Created.
- A JSON response body with the `payout_batch_id`. Use the `payout_batch_id` in the [show payout batch details](/docs/api/payments.payouts-batch/v1/#payouts_get) endpoint to get a detailed record of each item in the payout.

## Error messages

For information on Payouts API error messages, see [Payouts Error Messages](/docs/api/payments.payouts-batch/v1/#errors).

## Next

[Customize your integration](/docs/payouts/standard/integrate-api/customize)

## See also

- [PayPal API Executor](https://www.paypal.com/apex/product-profile/payouts/getAccessToken) — Make test calls to the Payouts API.
- [Payouts REST API](/docs/api/payments.payouts-batch/v1/)