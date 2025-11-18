# Source: https://docs.klarna.com/payments/after-payments/settlements/additional-resources/which-report-type-to-choose.md

# Which report type to chose?

| Task | Recommended report | How to get the report |
|----|------------------|---------------------|
| * Transaction-level reconciliation of payments to your bank account. * Bookkeep Klarna fees | | 1. CSV Settlement Report (fully configurable) 1. Order details in your PDF settlement report for a low amount of orders 1. Settlements App -> Settlement detail page (by clicking on the payment reference) 1. JSON API | | * Merchant Portal -> Settlements App * Settlements API * SFTP |
| * Overview of all captured or refunded orders in a month or any other period * Estimation of the next payout amount * Tax (VAT/GST) on the services or products sold by you to your end-costumers (consumer VAT) for a period of time | | Custom Report | * Merchant Portal -> Settlements App -> Custom Report |
| Summary of all settlements towards you in a period of time | * PDF summary report * CSV summary report | | * Merchant Portal -> Settlements App * Settlements API |
| Tax (VAT/GST) invoice for fees if those are being deducted from your settlement (net-settlement) | PDF Settlement Report | * Merchant Portal -> Settlements App * Settlements API * SFTP |
| Tax (VAT/GST) invoice for fees if those are not being deducted from your settlement (gross-settlement) | Invoice | * Merchant Portal -> Settlements App -> Invoices * Email |