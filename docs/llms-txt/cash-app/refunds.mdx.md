# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/refunds.mdx

***

## stoplight-id: aa4127e12ac8d

# Refunds

List of topics in this article

* [Refunds](#refunds)

* [Issue a Refund (Authorization)](#refund-authorization)

* [Capture a Refund](#refund-capture)

* [Void a Refund](#void-a-refund)

# Refunds

Refunds allow a Merchant/PSP to send funds from a Merchant to a Customer.

Refunds are linked to a previously captured Cash App Pay Payment. They must not have an amount greater than the captured amount on the original Payment. Read more [here](/cash-app-pay-partner-api/guides/resources/frequently-asked-questions/returns-and-refunds)

<Note>
  Cash App has set a maximum time limit of 7 years to issue a refund.
</Note>

<Note>
  Refunds typically process in several business days following initiation, except for Stored Value Balance (SVB) which is immediate. Transaction fees will not be returned to the PSP in the event of a refund.
</Note>

![refunds.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/refunds.png)

## Refund Authorization

Authorizations are valid for and must be captured within 7 days to complete a Refund. Authorizations not captured within 7 days are voided, and a new authorization will be required to complete a Refund.

<Note>
  Refunds can be authorized and captured via a single API call by setting <code>capture=true</code>. See the API reference for more information.
</Note>

### Refund Authorization Failure Scenarios and Error Codes

| Action                                    | Description                                                                                                                                                                             |
| :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PAYMENT\_NOT\_FOUND (linked refunds only) | Cash App could not find the Payment to Refund.                                                                                                                                          |
| CUSTOMER\_DISABLED                        | The Cash App account of the Customer receiving the Refund is deactivated.                                                                                                               |
| MERCHANT\_DISABLED                        | Merchant is deactivated in Cash App Pay and cannot issue Refunds.                                                                                                                       |
| MERCHANT\_PENDING                         | Merchant onboarding has not yet completed and the Merchant cannot issue Refunds.                                                                                                        |
| REFUND\_DECLINED\_COMPLIANCE              | Refund is declined by Block for compliance reasons, including violation of Cash App Terms of Service, Program Rules, or applicable laws.                                                |
| REFUND\_DECLINED\_OTHER                   | Refund is declined for an unknown reason.                                                                                                                                               |
| REFUND\_DECLINED\_RISK                    | Refund is declined due to riskiness. Block’s risk models will decline Refunds if they detect potentially fraudulent or otherwise risky activity.                                        |
| REFUND\_INVALID\_AMOUNT\_MISMATCH         | Refund amount did not match the amount shown to the Customer during the Customer Request for Refund.                                                                                    |
| REFUND\_INVALID\_CURRENCY\_MISMATCH       | Refund currency did not match the currency shown to the Customer during the Customer Request for Refund, or the currency of the Merchant did not match the Refund’s currency.           |
| REFUND\_INVALID\_PAYMENT\_UNCAPTURED      | The Payment being refunded has not been captured and therefore cannot be refunded.                                                                                                      |
| REFUND\_INVALID\_TOO\_LARGE               | The requested Refund amount is too high. Cash App Pay’s maximum Refund size may be adjusted to prevent fraud, though this is not equivalent to a risk decline (`REFUND_DECLINED_RISK`). |
| REFUND\_INVALID\_TOO\_SMALL               | The requested Refund amount is too low (below \$0.01 USD).                                                                                                                              |

## Refund Capture

Once a Refund has been authorized, it must be captured within 7 days to complete the Refund and trigger the Settlement process. Only the **exact** amount that was authorized is captured since Refunds should not be over or under-captured.

## Void a Refund

Once a Refund has been authorized but before it has been captured, it can be voided. This cancels the authorization and is a terminal state for the Refund. This is only applicable while the Refund authorization is valid.

<Note>
  If a Refund is not captured seven days after authorization, it will be automatically voided.
</Note>
