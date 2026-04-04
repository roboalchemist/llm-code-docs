# Source: https://docs.klarna.com/payments/after-payments/settlements/settlement-reporting-getting-started.md

# Before you start

## After capturing your first order you will be automatically paid out according to the payout schedule and payout defined. Get started here and have everything in place to reconcile your first payment.

## Understand payout terms

You can either find your payout schedule **payout schedule** and **payout delay** in the terms and conditions of your contract or by simply visiting the Settlements App in the Merchant Portal. A payout delay acts as safety net for both of us and it's main purpose is to prevent money for invoices from being sent back and forth between Klarna and you and also to cover cases where you would register a return.  Let's say you agreed to have weekly payouts on Wednesdays and a payout delay of one week. If you capture an order on Friday, it will not be settled on the Wednesday in the following week, but one week later on Wednesday, due to the payout delay. One day later, on Thursday, you will receive the **Settlement report** via the [Merchant Portal Settlements App](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/payments.md), the [Settlements API](https://docs.klarna.com/api/settlements/)or via a [pre-configured SFTP](https://docs.klarna.com/payments/after-payments/settlements/additional-resources/how-to-get-settlement-reports-via-sftp.md). On the same day, the payment is leaving our bank account and will be credited to your bank account in the following days. For each payout we will provide you with settlement reports to reconcile the payment against the orders in your system. Use the payment reference in the bank statement to match the related settlement report. The most popular way to access Settlement reports is to use our CSV report for order-level reconciliation and the PDF report as a summary and for your tax reporting since it serves as the VAT invoice for our fees in the European Union, Australia, and Canada. 


![ Example: Payout schedule weekly on Wednesday and Payment delay 1 week ](Zr9xo0aF0TcGJASI_Settlementdelay.jpeg)
*Example:Payout schedule weekly on Wednesday and Payment delay 1 week*

**\*Settlement time zones:**

- EU in GMT (GB time zone)
- US in EST (UTC+6)
- AP in AEST (UTC+10)

## Consider an automated integration via API or SFTP

Our settlement reports are always available for manual download via the Settlements App. Additionally, you can retrieve both the CSV and PDF report automatically via [SFTP](https://docs.klarna.com/payments/after-payments/settlements/additional-resources/how-to-get-settlement-reports-via-sftp.md) or an \[ API\] to reduce your manual effort.

## Customize your CSV settlement report

Instead of adjusting your accounting system, you can easily customize our CSV settlement reports within a few minutes. Simply add or remove data, adjust the delimiter, date, or amount formats.