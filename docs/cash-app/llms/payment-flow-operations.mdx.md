# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/payment-flow-operations.mdx

***

## stoplight-id: 52e006365c821

# Payment Flow Operations

Cash App Pay (CAP) Payments follow a dual-message, authorization-capture model. Additionally, Payments require a separate Customer Request to complete a Payment.

Thus, there are three actions required to process a payment:

1. Customer request
2. Payment authorization
3. Payment capture

> For the purposes of this Payment Flow Operations section, M/PSP refers to a Merchant or PSP acting on behalf of a Merchant.",

## Customer Request and Grant

To get permission to initiate a Payment or issue a Refund, a M/PSP must obtain a Grant after receiving a Customer Request to use CAP. A Grant represents a Customer’s approval for a Merchant to take a specific Transaction-related action on their behalf. These actions are listed in **Action Types** below.

> Once a Grant is obtained, a M/PSP can perform the action on behalf of the Customer.",

### Action types

The following table describes what action is permitted with a Grant for each action type:

| Action             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ONE\_TIME\_PAYMENT | Initiate a one-time Payment from a Customer to a Merchant in a specified amount                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ON\_FILE\_PAYMENT  | Store a Customer's Cash App Account, allowing a M/PSP to create Payments or issue Refunds without requiring the Customer to repeat the Customer Request approval process.<br /><br />The scope of this Grant must be provided to and approved by the Customer, which determines which Merchants can use the on-file Payment Grant to initiate Payments or issue Refunds.  The scope of Grant may be at a Merchant, Brand, or PSP level. A Merchant-specific Grant may be used by a single merchant, a brand-level Grant may be used by any Merchant associated with the Brand, and a PSP-level Grant may be used by all Merchants managed by the PSP. |

![one-time-and-on-file-payment.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/one-time-and-on-file-payment.png)

## Payment Authorization

Authorizations are valid for and must be captured within seven days to complete a Payment. Authorizations not captured within seven days will be voided, and a new authorization will be required to complete a Payment.

Some Payment types require additional data during authorization:

* **Recurring Payments**: Authorizations for recurring payments should indicate that the Payment is part of a recurring series. Failure to do so may result in elevated decline rates.

### Payment Authorization Failure Scenarios & Codes

| Failure                                        | Code	Description                                                                                                                                                                                               |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GRANT\_CONSUMED                                | The Grant presented has already been used to take a Payment and cannot be reused.                                                                                                                              |
| GRANT\_EXPIRED                                 | The Grant presented is expired and cannot be used to take a Payment.                                                                                                                                           |
| GRANT\_NOT\_FOUND                              | The CAP API could not find the Grant presented.                                                                                                                                                                |
| GRANT\_REVOKED                                 | The Grant presented has been revoked and cannot be used to take a Payment.                                                                                                                                     |
| GRANT\_ACTION\_MISMATCH                        | The Grant presented is not usable for taking Payments. M/PSP must initiate a new Customer Request for Payment using a “ONE\_TIME\_PAYMENT” or “ON\_FILE\_PAYMENT” action.                                      |
| CUSTOMER\_DISABLED                             | The Cash App Account of the Customer authorizing the Payment is deactivated.                                                                                                                                   |
| MERCHANT\_DISABLED                             | Merchant is deactivated in CAP and cannot accept Payments. Merchants can be disabled by a PSP or Block.                                                                                                        |
| MERCHANT\_PENDING                              | Merchant onboarding has not yet completed and the merchant cannot accept Payments.                                                                                                                             |
| PAYMENT\_DECLINED\_COMPLIANCE                  | Payment is declined by Block for compliance reasons, including violation of Cash App Terms of Service, these [Program Rules](/cash-app-pay-partner-api/guides/partnerships/program-rules), or applicable laws. |
| PAYMENT\_DECLINED\_INSUFFICIENT\_FUNDS         | Customer does not have funds available to complete the Payment.                                                                                                                                                |
| PAYMENT\_DECLINED\_LIMIT\_REACHED              | Customer has reached a limit for the amount of funds that can be moved out of their Cash App Account during a given time period and must wait before making additional Payments.                               |
| PAYMENT\_DECLINED\_OTHER                       | Payment is declined for an unknown reason. Used as a fallback when a more specific reason is not applicable.                                                                                                   |
| PAYMENT\_DECLINED\_RISK                        | Payment is declined due to riskiness. Block’s risk models will decline Payments if they detect potentially fraudulent or otherwise risky activity.                                                             |
| PAYMENT\_DECLINED\_CUSTOMER\_BLOCKED\_MERCHANT | Payment is declined because the Customer has blocked the Merchant on Cash App.                                                                                                                                 |
| PAYMENT\_INVALID\_AMOUNT\_MISMATCH             | Payment amount did not match the amount shown to the Customer during Customer Request for Payment.                                                                                                             |
| PAYMENT\_INVALID\_CURRENCY\_MISMATCH           | Payment currency did not match the currency shown to the Customer during Customer Request for Payment, or the currency of the Merchant did not match the Payment’s currency.                                   |
| PAYMENT\_INVALID\_TOO\_LARGE                   | The requested Payment amount is too high. CAP’s maximum Payment size may be adjusted to prevent fraud, though this is not equivalent to a risk decline.                                                        |
| PAYMENT\_INVALID\_TOO\_SMALL                   | The requested Payment amount is too low (below \$0.01 USD).                                                                                                                                                    |

## Payment Capture

Once a Payment has been authorized, it must be captured within seven days to complete the Payment and trigger the settlement process for the M/PSP to receive funds.

Generally, a M/PSP must capture a Payment for the amount of authorization. A M/PSP may capture an amount that is different than the authorization value in two cases:

* Pre-authorization / Partial Capture
  * A M/PSP is mitigating Payment risk from a Customer before goods are delivered or services are rendered by authorizing an amount that will be higher than the final Payment value. For example, at gas stations, rental deposits.
* Over-Capture
  * A Merchant is including supplementary items to the original authorized Payment. This is typically used to add gratuity or other incidental fees. The amount of funds captured over the authorization amount is not guaranteed.

### Capture Failure Scenarios & Codes

Generally, once a Payment is authorized, the funds are safe for capture. However, a capture may fail after a successful authorization in the following scenarios.

| Failure Code                           | Description                                                                                                                                             |
| :------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PAYMENT\_DECLINED\_INSUFFICIENT\_FUNDS | Customer does not have funds available to complete the payment.                                                                                         |
| PAYMENT\_INVALID\_TOO\_LARGE           | The requested Payment amount is too high. CAP’s maximum Payment size may be adjusted to prevent fraud, though this is not equivalent to a risk decline. |
| PAYMENT\_INVALID\_TOO\_SMALL           | The requested Payment amount is too low (below \$0.01 USD).                                                                                             |
| GATEWAY\_TIMEOUT                       | The payment failed because it took too long to process.                                                                                                 |

## Refund

Refunds allow a M/PSP to send funds from a Merchant to a Customer.

Refunds are related to a previously captured Payment. They must not have an amount greater than the captured amount on the original Payment. There is no time limit to issue a Refund.

Refunds typically process in 7 to 10 business days following initiation. Transaction fees are not returned to the PSP in the event of a Refund.

### Refund Authorization

Authorizations are valid for and must be captured within seven days to complete a Refund. Authorizations not captured within seven days are voided, and a new authorization will be required to complete a Refund.

#### Refund Authorization Failure Scenarios & Error Codes

| Error Code                                | Description                                                                                                                                                                                                   |
| :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PAYMENT\_NOT\_FOUND (linked refunds only) | Cash App could not find the Payment to Refund.                                                                                                                                                                |
| CUSTOMER\_DISABLED                        | The Cash App account of the Customer receiving the Refund is deactivated.                                                                                                                                     |
| MERCHANT\_DISABLED                        | Merchant is deactivated in CAP and cannot issue Refunds.                                                                                                                                                      |
| MERCHANT\_PENDING                         | Merchant onboarding has not yet completed and the merchant cannot issue Refunds.                                                                                                                              |
| REFUND\_DECLINED\_COMPLIANCE              | Refund is declined by Block for compliance reasons, including violation of Cash App Terms of Service, these [Program Rules](/cash-app-pay-partner-api/guides/partnerships/program-rules), or applicable laws. |
| REFUND\_DECLINED\_OTHER                   | Refund is declined for an unknown reason. Used as a fallback when a more specific reason is not applicable.                                                                                                   |
| REFUND\_DECLINED\_RISK                    | Refund is declined due to riskiness. Block’s risk models will decline Refunds if they detect potentially fraudulent or otherwise risky activity.                                                              |
| REFUND\_INVALID\_AMOUNT\_MISMATCH         | Refund amount did not match the amount shown to the Customer during Customer Request for Refund.                                                                                                              |
| REFUND\_INVALID\_CURRENCY\_MISMATCH       | Refund currency did not match the currency shown to the Customer during Customer Request for Refund, or the currency of the Merchant did not match the Refund’s currency.                                     |
| REFUND\_INVALID\_PAYMENT\_UNCAPTURED      | The Payment being refunded has not been captured and therefore cannot be refunded.                                                                                                                            |
| REFUND\_INVALID\_TOO\_LARGE               | The requested Refund amount is too high. CAP’s maximum Refund size may be adjusted to prevent fraud, though this is not equivalent to a risk decline.                                                         |
| REFUND\_INVALID\_TOO\_SMALL               | The requested Refund amount is too low (below \$0.01 USD).                                                                                                                                                    |

### Refund Capture

Once a Refund has been authorized, it must be captured within seven days to complete the Refund and trigger the settlement process. Refund captures only capture the **exact** amount that was authorized; Refunds may not be over or under-captured.

#### Refund Capture Failure Scenarios & Error Codes

Generally, once a Refund is authorized, it is safe for capture. However, a capture may fail after a successful authorization in the following scenarios:

| Error Code                   | Description                                                                                                                                                                                                   |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CUSTOMER\_DISABLED           | The Cash App account of the Customer receiving the Refund is deactivated.                                                                                                                                     |
| MERCHANT\_DISABLED           | Merchant is deactivated in CAP and cannot issue Refunds. Merchants can be disabled by a PSP or Block.                                                                                                         |
| REFUND\_DECLINED\_COMPLIANCE | Refund is declined by Block for compliance reasons, including violation of Cash App Terms of Service, these [Program Rules](/cash-app-pay-partner-api/guides/partnerships/program-rules), or applicable laws. |
| REFUND\_DECLINED\_OTHER      | Refund is declined for an unknown reason. Used as a fallback when a more specific reason is not applicable.                                                                                                   |
| REFUND\_DECLINED\_RISK       | Refund is declined due to riskiness. Block’s risk models will decline Refunds if they detect potentially fraudulent or otherwise risky activity.                                                              |
