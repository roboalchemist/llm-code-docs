# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/disputes.mdx

***

## stoplight-id: n0yxglp64burx

# Disputes

## Overview

Customers can raise and manage disputes related to non-delivery of goods directly through the Afterpay Customer Portal. Merchants can manage and respond to these disputes via the Disputes API and the Afterpay Business Hub. If a resolution can't be reached, Afterpay can step in to adjudicate.

<Info>
  At this time, Cash App Afterpay supports only 

  `product_not_received`

   as a dispute reason.
</Info>

## Dispute lifecycle

1. A customer raises a dispute through their Cash App Afterpay dashboard or app and provides evidence to support their case.

2. Cash App Afterpay notifies the merchant using methods including email, the Business Hub, API, and webhooks.

3. The merchant responds to the dispute. They can accept the dispute (which closes the dispute in the customer's favor) or contest the dispute by providing evidence via the API or the Business Hub.

4. If the merchant provides evidence, the dispute is returned to the customer.  The customer can either accept the merchant’s decision (which closes the dispute in the merchant's favor) or can reject the merchant’s evidence.

5. If the customer rejects the merchant's evidence, an Afterpay agent steps in. The agent decides the outcome of the dispute based on the available evidence. Both parties are notified of the decision.

### **Merchant Side Dispute Lifecycle Diagram**

<div>
  ```mermaid
  ---
  config:
    layout: dagre
  ---
  %%{
    init: {
      'theme': 'base',
      'themeVariables': {
        'primaryColor': '#FFF',
        'primaryTextColor': '#000',
        'primaryBorderColor': '#000',
        'lineColor': '#000',
        'secondaryColor': '#fff',
        'tertiaryColor': '#fff',
        'noteBkgColor': '#fff',
        'noteBorderColor': '#000'
      }
    }
  }%%
  flowchart TD
      id1(("start")) --> id2(["Needs Merchant Response"])
      id2 -- Merchant Challenge --> id3(["Under Review"])
      id2 -- Merchant Accept --> id6(["Merchant Lost"])
      id3 -- Consumer Accept --> id5(["Merchant Won"])
      id3 -- Consumer Reject --> id4(["$AP Adjudication"])
      id4 -- Merchant Favor --> id5
      id4 -- Consumer Favor --> id6
      id5:::termState
      id6:::termState
  ```
</div>

## Dispute windows

Cash App Afterpay updates dispute statuses and sends dispute notifications according to the following time frames:

| Window                         | Description                                                                                                                                        | Time frame |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Dispute open                   | The maximum window of time (from the transaction date) for a dispute to be opened. 60 days after the statement date, dispute claims may be denied. | 120 days   |
| Merchant’s evidence submission | The allowed time between the merchant being notified of a dispute and the final time for evidence submission.                                      | 13 days    |
| Cash App Afterpay’s decision   | The allowed time from the moment of evidence submission to Cash App Afterpay’s final decision.                                                     | 30 days    |

## Dispute statuses

Cash App Afterpay supports the following dispute statuses:

| Status              | Description                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `needs_response`    | Cash App Afterpay has created the dispute and notified the merchant, but the merchant has not taken action.                                              |
| `under_review`      | Merchant has submitted evidence to Cash App Afterpay, and it is currently under review.                                                                  |
| `won`               | The evidence submitted is accepted by Cash App Afterpay and the dispute is won by the merchant. Note that this is a terminal state.                      |
| `lost`              | The evidence submitted is rejected by Cash App Afterpay and the dispute is lost by the merchant. Note that this is a terminal state.                     |
| `merchant_refunded` | Merchant has issued a refund. If the refund is equal to or greater than the dispute amount, then this is a terminal state.                               |
| `merchant_voided`   | Merchant has canceled all or a portion of the order. If the voided amount is equal to or greater than the dispute amount, then this is a terminal state. |

## Closing reasons

A closing reason indicating how the final decision on the dispute was reached is displayed to the merchant. The following closing reasons are accepted:

| Merchant-facing Closing Reason | Description                                                                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `merchant_accepted`            | Merchant accepted the dispute.                                                                                                      |
| `evidence_accepted`            | Merchant submitted evidence which was accepted. The dispute was closed in the merchant’s favor.                                     |
| `evidence_rejected`            | Merchant submitted the evidence but it was rejected and the dispute was closed in the customer’s favor.                             |
| `deadline_expired`             | Merchant failed to submit evidence for the dispute and the submission window timed out. Dispute was closed in the customer's favor. |
| `customer_cancelled`           | Customer withdrew the dispute and therefore it was closed in the merchant’s favor.                                                  |

<Info>
  All dispute records are saved in the Cash App Afterpay system and are accessible through the Dispute APIs; dispute records are not deleted.

  In financial reporting, there will be a separate record for a dispute. Order ID, Dispute ID, financial changes (+/-) are included in the record. Afterpay only gathers funds from the merchant after the merchant loses the dispute.
</Info>
