# Transaction Event Codes

A transaction event code is a five-digit code that classifies the transaction type based on money movement and debit or credit. A transaction event code, or T-code, is a five-character alphanumeric string, such as T0001.

A T-code has the following format:

```
T<event-group><event-type-code>
```

Where:

- `<event-group>` is a two-digit general accounting event group. The event group portion of the T-code is sufficient for reconciliation and report parsing.
- `<event-type-code>` is a two-digit event type code.

## Transaction event code tables

These tables list the transaction event codes that you use to classify a transaction.

### T00nnPayPal account-to-PayPal account payment

| T-code | Description |
| --- | --- |
| T0000 | General: received payment of a type not belonging to the other T00nncategories. |
| T0001 | MassPay payment. |
| T0002 | Subscription payment. Either payment sent or payment received. |
| T0003 | Pre-approved payment (BillUser API). Either sent or received. |
| T0004 | eBay auction payment. |
| T0005 | Direct payment API. |
| T0006 | PayPal Checkout APIs. |
| T0007 | Website payments standard payment. |
| T0008 | Postage payment to carrier. |
| T0009 | Gift certificate payment. Purchase of gift certificate. |
| T0010 | Third-party auction payment. |
| T0011 | Mobile payment, made through a mobile phone. |
| T0012 | Virtual terminal payment. |
| T0013 | Donation payment. |
| T0014 | Rebate payments. |
| T0015 | Third-party payout. |
| T0016 | Third-party recoupment. |
| T0017 | Store-to-store transfers. |
| T0018 | PayPal Here payment. |
| T0019 | Generic instrument-funded payment. |
| T0021 | Cryptocurrency payment. |

### T01nnNon-payment-related fees

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0100 | General non-payment fee of a type not belonging to the other T01nncategories. |  |
| T0101 | Website payments. Pro account monthly fee. |  |
| T0102 | Foreign bank withdrawal fee. |  |
| T0103 | WorldLink check withdrawal fee. |  |
| T0104 | Mass payment batch fee. |  |
| T0105 | Check withdrawal. |  |
| T0106 | Chargeback processing fee. | Chargeback processing, or handling, fee. Charged against account that received a chargeback for a previous transaction. |
| T0107 | Payment fee. |  |
| T0108 | ATM withdrawal. |  |
| T0109 | Auto-sweep from account. |  |
| T0110 | International credit card withdrawal. |  |
| T0111 | Warranty fee for warranty purchase. |  |
| T0112 | Gift certificate expiration fee. |  |
| T0113 | Partner fee. |  |
| T0114 | Dispute fee. |  |

### T02nnCurrency conversion

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0200 | General currency conversion. | Transfer of funds from one currency balance to a different currency balance. |
| T0201 | User-initiated currency conversion. |  |
| T0202 | Currency conversion required to cover negative balance. PayPal-system generated. |  |

### T03nnBank deposit into PayPal account

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0300 | General funding of PayPal account. | Deposit to PayPal balance from a bank account. |
| T0301 | PayPal balance manager funding of PayPal account. | PayPal-system generated. |
| T0302 | ACH funding for funds recovery from account balance. |  |
| T0303 | Electronic funds transfer (EFT) (German banking). |  |

### T04nnBank withdrawal from PayPal account

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0400 | General withdrawal from PayPal account. | Settlement withdrawal or user-initiated. |
| T0401 | AutoSweep. |  |
| T0403 | You initiated a transfer from your PayPal balance to your bank account. |  |

### T05nnDebit card

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0500 | General PayPal debit card transaction. | Requires a PayPal debit card associated with the PayPal account. |
| T0501 | Virtual PayPal debit card transaction. |  |
| T0502 | PayPal debit card withdrawal to ATM. |  |
| T0503 | Hidden virtual PayPal debit card transaction. |  |
| T0504 | PayPal debit card cash advance. |  |
| T0505 | PayPal debit authorization. |  |

### T06nnCredit card withdrawal

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0600 | General credit card withdrawal. | Reversal of purchase with a credit card. Seen only in PayPal account of the credit card owner. |

### T07nnCredit card deposit

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0700 | General credit card deposit. | Purchase with a credit card. |
| T0701 | Credit card deposit for negative PayPal account balance. |  |

### T08nnBonus

| T-code | Description | Example transaction |
| --- | --- | --- |
| T0800 | General bonus of a type not belonging to the other T08nncategories. |  |
| T0801 | Debit card cash back bonus. | Requires a PayPal debit card associated with the PayPal account. |
| T0802 | Merchant referral account bonus. | Must have created a merchant referral bonus link. |
| T0803 | Balance manager account bonus. |  |
| T0804 | PayPal buyer warranty bonus. |  |
| T0805 | PayPal protection bonus, payout for PayPal buyer protection, payout for full protection with PayPal buyer credit. |  |
| T0806 | Bonus for first ACH use. |  |
| T0807 | Credit card security charge refund. |  |
| T0808 | Credit card cash back bonus. |  |

### T09nnIncentive

| T-code | Description |
| --- | --- |
| T0900 | General incentive or certificate redemption. |
| T0901 | Gift certificate redemption. |
| T0902 | Points incentive redemption. |
| T0903 | Coupon redemption. |
| T0904 | eBay loyalty incentive. |
| T0905 | Offers used as funding source. |

### T10nnBill pay

| T-code | Description |
| --- | --- |
| T1000 | Bill pay transaction. |

### T11nnReversal

| T-code | Description | Example transaction |
| --- | --- | --- |
| T1100 | General reversal of a type not belonging to the other T11nncategories. |  |
| T1101 | Reversal of ACH withdrawal transaction. | Reversal of a withdrawal from PayPal balance to a bank account. |
| T1102 | Reversal of debit card transaction. | Reversal of a debit card payment. Requires a PayPal debit card. |
| T1103 | Reversal of points usage. |  |
| T1104 | Reversal of ACH deposit. |  |
| T1105 | Reversal of general account hold. |  |
| T1106 | Payment reversal, initiated by PayPal. |  |
| T1107 | Payment refund, initiated by merchant. |  |
| T1108 | Fee reversal. |  |
| T1109 | Fee refund. |  |
| T1110 | Hold for dispute investigation (T15nn). | To cover possible chargeback. |
| T1111 | Cancellation of hold for dispute resolution. | Cancellation of temporary hold to cover possible chargeback. |
| T1112 | MAM reversal. |  |
| T1113 | Non-reference credit payment. |  |
| T1114 | MassPay reversal transaction. |  |
| T1115 | MassPay refund transaction. |  |
| T1116 | Instant payment review (IPR) reversal. |  |
| T1117 | Rebate or cash back reversal. |  |
| T1118 | Generic instrument/Open Wallet reversals (seller side). |  |
| T1119 | Generic instrument/Open Wallet reversals (buyer side). |  |

### T12nnAdjustment

| T-code | Description | Example transaction |
| --- | --- | --- |
| T1200 | General account adjustment. |  |
| T1201 | Chargeback. |  |
| T1202 | Chargeback reversal. |  |
| T1203 | Charge-off adjustment. |  |
| T1204 | Incentive adjustment. |  |
| T1205 | Reimbursement of chargeback. |  |
| T1207 | Chargeback re-presentment rejection. | Adjustment to PayPal account for reversal of payment based on rejection of the re-presentment for a chargeback in the PayPal system. |
| T1208 | Chargeback cancellation. | Adjustment to PayPal account for reversal of chargeback reversal based on cancellation of a chargeback in the PayPal system. |

### T13nnAuthorization

**Note:** Appears in transaction detail report and not in settlement report.

| T-code | Description |
| --- | --- |
| T1300 | General authorization. |
| T1301 | Reauthorization. |
| T1302 | Void of authorization. |

### T14nnDividend

| T-code | Description |
| --- | --- |
| T1400 | General dividend. |

### T15nnHold for dispute or other investigation

| T-code | Description |
| --- | --- |
| T1500 | General temporary hold of a type not belonging to the other T15nncategories. |
| T1501 | Account hold for open authorization. |
| T1502 | Account hold for ACH deposit. |
| T1503 | Temporary hold on available balance. |

### T16nnBuyer credit deposit

| T-code | Description | Example transaction |
| --- | --- | --- |
| T1600 | PayPal buyer credit payment funding. | Must have signed up for buyer credit. |
| T1601 | BML credit. Transfer from BML. |  |
| T1602 | Buyer credit payment. |  |
| T1603 | Buyer credit payment withdrawal. Transfer to BML. |  |

### T17nnNon-bank withdrawal

| T-code | Description |
| --- | --- |
| T1700 | General withdrawal to non-bank institution. |
| T1701 | WorldLink withdrawal. |

### T18nnBuyer credit withdrawal

| T-code | Description | Example transaction |
| --- | --- | --- |
| T1800 | General buyer credit payment. | Must have signed up for buyer credit. |
| T1801 | BML withdrawal. Transfer to BML. |  |

### T19nnAccount correction

| T-code | Description |
| --- | --- |
| T1900 | General adjustment without business-related event. |

### T20nnFunds transfer from PayPal account to another

| T-code | Description |
| --- | --- |
| T2000 | General intra-account transfer. |
| T2001 | Settlement consolidation. |
| T2002 | Transfer of funds from payable. |
| T2003 | Transfer to external GL entity. |
| T2004 | Receivables financing. |

### T21nnReserves and releases

| T-code | Description | Example transaction |
| --- | --- | --- |
| T2101 | General hold. |  |
| T2102 | General hold release. |  |
| T2103 | Reserve hold. | PayPal holdsn% of funds forddays as a condition for processing for you. This amount is part of your total balance and is not available for withdrawal. |
| T2104 | Reserve release. | A reserve, when released, is now available for withdrawal. |
| T2105 | Payment review hold. | A payment review hold is used to protect you against unauthorized fraud loss and for seller protection. While a transaction is on payment review hold, we recommend that you do not ship the item. We are reviewing this transaction for up to 24 hours. |
| T2106 | Payment review release. | A payment review hold, when released, is now available for withdrawal. |
| T2107 | Payment hold. | Payment holds are funds that belong to you that we set aside, such as a security deposit. This amount is part of your total balance and is not available for withdrawal. |
| T2108 | Payment hold release. | A payment hold, when released, is now available for withdrawal. |
| T2109 | Gift certificate purchase. | When a gift certificate is purchased by your buyer, that amount is placed on hold. |
| T2110 | Gift certificate redemption. | A gift certificate, when redeemed, is available for withdrawal. |
| T2111 | Funds not yet available. | While you establish a successful sales history on eBay, funds from eBay sales are usually available in 21 or fewer days, based on how you ship the order. You might get your funds faster if you print your shipping labels on eBay or PayPal, upload tracking information, or mark the item as shipped on eBay. If your buyer reports a problem with the sale, it might take longer to get funds. |
| T2112 | Funds available. | These funds are available for use. |
| T2113 | Blocked payments. |  |

### T22nnTransfers

| T-code | Description |
| --- | --- |
| T2201 | Transfer to and from a credit-card-funded restricted balance. |

### T30nnGeneric instrument and Open Wallet

| T-code | Description |
| --- | --- |
| T3000 | Generic instrument/Open Wallet transaction. |

### T50nnCollections and disbursements

| T-code | Description |
| --- | --- |
| T5000 | Deferred disbursement. Funds collected for disbursement. |
| T5001 | Delayed disbursement. Funds disbursed. |

### T97nnPayables and receivables

| T-code | Description |
| --- | --- |
| T9700 | Account receivable for shipping. |
| T9701 | Funds payable. PayPal-provided funds that must be paid back. |
| T9702 | Funds receivable. PayPal-provided funds that are being paid back. |

### T98nnDisplay only transaction

| T-code | Description |
| --- | --- |
| T9800 | Display only transaction. |

### T99nnOther

| T-code | Description |
| --- | --- |
| T9900 | Other. |