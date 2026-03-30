# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/payment-processing/settlement.mdx

***

## stoplight-id: 3216cd8313115

# Settlement

Cash App settles [captured payments](/cash-app-pay-partner-api/api-reference/network-api/capture-payment) with the PSP (Payment Service Provider) client (also referred to as client in the technical specifications below) via ACH using a batch process. We capture the transaction-level details of each Settlement  as a Reconciliation report and upload them to a client-provided SFTP server.

<Note>
   Cash App will provide a net Settlement process, deducting Refunds and Dispute amounts from Settlement amounts. 
</Note>

Cash App will deliver funds to the client for all unsettled eligible transactions before a configurable designated cutoff time. The Settlement process follows the [Federal Reserve calendar](https://www.federalreserve.gov/aboutthefed/k8.htm) for availability. Which means that, Settlement is not available on Saturdays, Sundays, and holidays.

<Note>
   Settlement for Cash App Pay Transactions captured prior to 11:00 PM UTC will be initiated the same business day, subject to U.S. federal holidays. 
</Note>

For each daily batch of processed transactions that must be settled (i.e., CAPTURE, REFUND, CHARGEBACK), Cash App will issue a single-batched ACH Transfer with the client's configured Bank account as the destination. Each settlement includes an ACH payment and a series of associated Reconciliation reports that can contain up to 9,999 transactions per report.

| Property            | Type                                                                        | Description                                                                                                                                                                  |
| :------------------ | :-------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Settlement Time     | String <br />The time in a 24-hour clock ("hh:mm") in UTC (ISO 8601-1:2019) | This is the cutoff time for settling any unsettled eligible transactions. The batch will span the previous cutoff (on a business day) to the current one. (default: "23:00") |
| Bank routing number | String <br />ABA routing transit number is nine numerical digits            | This is the routing number of the destination bank where the funds will be deposited via ACH (required)                                                                      |
| Bank account number | String                                                                      | This is the account number of the destination bank where the funds will be deposited via ACH (required)                                                                      |

## Reconciliation Reports

Each net Settlement will have a corresponding Reconciliation report showing the amount of each Payment, applicable fees, Refunds, and Dispute-related adjustments used in the calculation of the Settlement amount. This report is delivered daily via Secure File Transfer Protocol (SFTP) to the PSP.
Cash App uploads Reconciliation reports to a client-provided SFTP server. To do this, we want the following information:

* SFTP hostname

* SFTP port

* Username of the PSP's SFTP server

* SFTP user's private RSA key

* SFTP server host's public RSA key (optional)

* Destination folder path (filepath for uploading the reports)

<br />

<Note>
   Reports are in CSV format and use a UTF-8 encoding. 
</Note>

<Note>
  As an additional security benefit, Cash App Pay can optionally PGP encrypt settlement files before they’re uploaded to the client SFTP server.
</Note>

<br />

## Activity Reconciliation Report

We give each activity Reconciliation report  a unique filename to avoid upload collisions using the following convention:\
`<yyyymmdd>_settlement_report_client_<client-id>_batch_<batch-id>_chunk_<chunk index>.csv`

<br />

> `<yyyymmdd>` is the date of settlement for settlement batch. For manually generated activity reconciliation reports, `<yyyymmdd>` is the date the report was generated.

<br />

### CSV Schema

Activity Reconciliation report files can contain up to 9,999 records. Each file will contain headers in the top row, and then each subsequent row will have the following schema:

| Column Name             | Type                                             | Description                                                                                                                                                                                    |
| :---------------------- | :----------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| merchant\_id            | String                                           | Cash App identifier for the associated Merchant.                                                                                                                                               |
| merchant\_reference\_id | String                                           | Client-provided reference ID specified on the Merchant associated with the payment or refund.                                                                                                  |
| settlement\_batch\_id   | String                                           | Cash App identifier of the batch of transactions this transactions was settled with. If possible, this identifier will be forwarded as metadata with the ACH transfer settling this payment.   |
| payment\_id             | String                                           | Cash App identifier for the associated payment. This identifier can be used to cross-reference settlement transactions of type `CHARGEBACK` with the associated dispute on the Dispute report. |
| payment\_reference\_id  | String                                           | Client specified reference id during [payment creation](/cash-app-pay-partner-api/api-reference/network-api/create-payment)                                                                    |
| refund\_id              | String                                           | Cash App identifier for the associated refund.                                                                                                                                                 |
| refund\_reference\_id   | String                                           | Client specified reference id during [refund creation](/cash-app-pay-partner-api/api-reference/network-api/create-refund)                                                                      |
| dispute\_id             | String                                           | Cash App identifier for the associated dispute                                                                                                                                                 |
| transaction\_type       | String                                           | The type of transaction {`CAPTURE`, `REFUND`, `CHARGEBACK`}                                                                                                                                    |
| transaction\_time       | String(datetime using RFC 3339 standard in UTC)  | The time at which the transaction event occurred. **NOTE**: for `CAPTURE`, this is the time of capture, for `REFUND`, it is the time of refund, etc.                                           |
| net\_amount             | Number (Integer)                                 | The net amount (after fees) being settled for this transaction event.                                                                                                                          |
| gross\_amount           | Number (Integer)                                 | The gross amount of the this transaction event. This is the sum of the net amount and the fee amount.                                                                                          |
| fee\_amount             | Number (Integer)                                 | The fee associated with this transaction event                                                                                                                                                 |
| fee\_variable           | Number (Integer)                                 | The variable fee associated with this transaction event                                                                                                                                        |
| fee\_fixed              | Number (Integer)                                 | The fixed fee associated with this transaction event                                                                                                                                           |
| currency\_code          | String (ISO 4217 Alpha-3 Currency code)          | Client's configured currency. Amounts use the smallest-denomination unit available in this currency. (for example, amount = 100 for \$1 USD, where the smallest unit is a cent)                |
| settled\_at             | String (datetime using RFC 3339 standard in UTC) | Time at which the ACH transfer that settled this transaction originated                                                                                                                        |

#### CSV Sample

```
merchant_id,merchant_reference_id,settlement_batch_id,payment_id,payment_reference_id,refund_id,refund_reference_id,dispute_id,transaction_type,transaction_time,net_amount,gross_amount,fee_amount,fee_variable,fee_fixed,currency_code,settled_at
MMI_9w89nidchumz9ktrcpnalg2ny,vt9bsxyv0c0xsgwtwrxnsymt7,PWCS_fg2sxvvhg1ff9p4tj1731sdy3,PWC_g74t4d97rr2qg1qe37gpa6bma,payment_reference1,,,,CAPTURE,2021-01-02T10:24:21Z,9700,10000,300,100,200,USD,2021-01-02T23:02:00Z
MMI_9w89nidchumz9ktrcpnalg2ny,vt9bsxyv0c0xsgwtwrxnsymt7,PWCS_fg2sxvvhg1ff9p4tj1731sdy3,PWC_g74t4d97rr2qg1qe37gpa6bma,payment_reference1,PWCR_g74d6d97rr2qg1qe37gpa6bma,refund_reference1,,REFUND,2021-01-02T10:24:21Z,-10000,-10000,0,0,0,USD,2021-01-02T23:02:00Z
MMI_9w89nidchumz9ktrcpnalg2ny,vt9bsxyv0c0xsgwtwrxnsymt7,PWCS_fg2sxvvhg1ff9p4tj1731sdy3,PWC_dmwmsh0zrskryvdthvbm8ddgs,payment_reference2,,,DSPT_jjdbzt6gvkecemz2s6q1cbfp2,CHARGEBACK,2021-01-02T10:24:21Z,-11000,-10000,1000,0,1000,USD,2021-01-02T23:02:00Z
```

## Balance Summary Report

The Balance Summary report contains the client's starting balance and ending balance, activity and payout details for a given processing window—to help understand daily payout, and provide information on carried-forward balances. Each report is given a unique filename to avoid upload collisions using the following convention:
`<yyyymmdd>_balance_summary_report_client_<client-id>_batch_<batch-id>.csv`

<br />

> `<yyyymmdd>` is the date of settlement for the settlement batch.

<br />

### CSV Schema

Each file will contain headers in the top row, and then exactly four rows with the following schema:

| Column Name | Type                                    | Description                                                                                                                                                                                                                                                                                                        |
| :---------- | :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| category    | String                                  | The record category `{`starting\_balance`, `ending\_balance`, `payout`, `activity`}`                                                                                                                                                                                                                               |
| description | String                                  | Description of the record category, as follows: <br />`starting balance`: "Starting Balance ( `ISO 8061 starting date of this settlement batch`)" <br />`ending balance`: "Ending Balance ( `ISO 8061 ending date of this settlement batch`)" <br />`payout`: "Total Payouts" <br />`activity`: "Payment Activity" |
| currency    | String (ISO 4217 Alpha-3 Currency code) | Client's configured currency. Amounts use the smallest-denomination unit available in this currency. (ex. amount = 100 for \$1 USD, where the smallest unit is a cent)                                                                                                                                             |
| net\_amount | Number(Integer)                         | Net amount for the given category.                                                                                                                                                                                                                                                                                 |

#### CSV Sample

```csv
"category","description","currency","net_amount"
"starting_balance","Starting Balance (2021-07-23)","USD","0"
"ending_balance","Ending Balance (2021-07-24)","USD","0"
"payout","Total Payouts","USD","187434"
"activity","Payment Activity","USD","187434"
```

### Negative net settlements

If a given processing window has a negative net settlement, no funds will be delivered to the client and Cash App will carry-forward the negative balance to the following day. The Balance Summary Report will reflect this negative balance as shown below:

#### CSV Sample

```csv
"category","description","currency","net_amount"
"starting_balance","Starting Balance (2023-03-21)","USD","0"
"ending_balance","Ending Balance (2023-03-22)","USD","-26285"
"payout","Total Payouts","USD","0"
"activity","Payment Activity","USD","-26285"
```

## Activity Summary Report

The Activity Summary report contains the net amount, gross amount, and fee amount totals for each transaction category. Each report is given a unique filename to avoid upload collisions using the following convention:
`<yyyymmdd>_activity_summary_report_client_<client-id>_batch_<batch-id>.csv`

<br />

> `<yyyymmdd>` is the date of settlement for the settlement batch.

<br />

### CSV Schema

Each file will contain headers in the top row, and then exactly three rows(one row per transaction type) with the following schema:

| Column Name       | Type                                    | Description                                                                                                                                                            |
| :---------------- | :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| count             | Number(Integer)                         | Number of transactions processed for this transaction type                                                                                                             |
| currency          | String (ISO 4217 Alpha-3 Currency code) | Client's configured currency. Amounts use the smallest-denomination unit available in this currency. (ex. amount = 100 for \$1 USD, where the smallest unit is a cent) |
| transaction\_type | String                                  | The type of transaction {`CAPTURE`, `REFUND`, `CHARGEBACK`}                                                                                                            |
| gross\_amount     | Number(Integer)                         | The sum of gross amounts of all transactions in this transaction batch                                                                                                 |
| net\_amount       | Number(Integer)                         | The sum of net amounts of all transactions in this transaction batch                                                                                                   |
| fee\_amount       | Number(Integer)                         | The sum of fee amounts of all transactions in this transaction batch                                                                                                   |

#### CSV Sample

```text
"count","currency","transaction_type","gross_amount","net_amount","fee_amount"
"7","USD","CAPTURE","5667","5508","159"
"2","USD","REFUND","1619","1573","45"
"1","USD","CHARGEBACK","809","786","22"
```

> Fraud disputes where Cash App Pay takes on liability are included here for informational purposes only and do not impact settlement.
