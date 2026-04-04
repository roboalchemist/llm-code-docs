# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/disputes/dispute-life-cycle.mdx

***

## stoplight-id: 8d59416c362bc

# Dispute Lifecycle

The Cash App Pay dispute process exists to protect our customers from bad actors and merchant errors. Customers have the option to dispute any Cash App Pay transaction, which will initiate the dispute process.

## RESPONSE\_REQUIRED

New disputes will be created in the `RESPONSE_REQUIRED` state where our systems will wait for text and file-based evidence to be submitted by the merchant, or for the merchant to accept the dispute without contest. The merchant can upload any information to help decide the outcome of the dispute.

<br />When all evidence has been submitted, the dispute may be challenged to start the adjudication process. The dispute will move to the `PROCESSING` state where it will remain until the dispute is adjudicated.
<Note> On the 13th day, we will automatically challenge any dispute with evidence. Any disputes without evidence, will be lost after 13 days. </Note>
Alternatively, the dispute may be accepted by the merchant to complete processing and transition immediately to the ACCEPTED state. When a dispute is created, the disputed amount will be withheld from that day’s settlement until the settlement following a resolution.

## PROCESSING

Disputes that have been challenged with evidence will show up in the processing state while they await adjudication, which can take up to 45 days.
<Note> During this time, you cannot submit any more evidence to the challenged disputes. </Note>
Once a dispute has been adjudicated, it will end up in one of the following terminal states:

* WON
* PARTIALLY\_WON
* LOST

<Note>
   See 

  [Dispute timelines](/cash-app-pay-partner-api/guides/technical-guides/payment-processing/disputes/introduction#dispute-timelines)

   for the length of time a Merchant has to respond before the dispute is forfeited. 
</Note>

## WON

A dispute will transition to the `WON` state if the dispute has been adjudicated in favor of the merchant or the customer withdraws their dispute.

In either case, merchants will be reimbursed their withheld settlement for this dispute at the next settlement.

## PARTIALLY\_WON

A dispute will transition to the `PARTIALLY_WON` state if the dispute has been adjudicated in favor of the customer for less than the disputed amount. The amount lost will be communicated to merchants via dispute reports and the amount lost will not be reimbursed to the merchant at the next settlement.

## LOST

A dispute will transition to the `LOST` state if the dispute has been adjudicated in favor of the customer for the entire disputed amount. The amount lost will be communicated to merchants via dispute reports and merchants will not receive their withheld settlement for this dispute.

## ACCEPTED

A dispute will transition to the `ACCEPTED` state if the merchant chooses to forgo the adjudication process and accept an automatic loss of the dispute. The amount lost will be communicated to merchants via dispute reports and merchants will not receive their withheld settlement for this dispute.

## NO\_RESPONSE\_REQUIRED

A dispute will be created in the `NO_RESPONSE_REQUIRED` state if Cash App has accepted liability for the dispute. These disputes are displayed via the API for transparency, however, the merchant is not obligated to take any action and is not liable for the dispute.

## State Machine

![disputes-payment-flow.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/disputes-payment-flow.png)
