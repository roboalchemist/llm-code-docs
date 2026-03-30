# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/brands-and-merchants.mdx

***

## stoplight-id: 619ffe4c8f558

# Brands and Merchants

## Relevant Terms

* **Client:** The developer that is making API calls to the Cash App Pay API. A client can create and update brands and merchants as needed.
* **Brand:** A Customer-facing business entity that aggregates related merchants within Cash App. Related merchants under a single business entity are aggregated into a Brand within Cash App. Customers will see their transactions grouped by brand within Cash App.
* **Merchant:** A business that a Customer can transact with. This could be an e-commerce store, a physical brick and mortar store, etc.

## Brand and Merchant Hierarchy

Brands have a one-to-many relationship with merchants. The Brand should always reflect the Customer-facing brand entity and not the corporate umbrella entity. For example, Block has several business units including Square, Cash App, Afterpay, Tidal. Separate Brands must be created for each of these business units instead of one Brand for “Block”.

> **Example:** Good Pour Coffee is a Brand and the Good Poor Coffee Shop at 1 Market St. is a Merchant under the Good Pour Coffee Brand.

When a customer request is created, it can be scoped to either the Client, Brand, or Merchant depending on the Customer request payment action. For example:

* **One-Time Payment:** Client, Brand, Merchant
* **On-File Payment:** Client, Brand

The value that is passed along has implications on what is presented to the Customer during the grant approval process and after the transaction is completed, within the Customer’s Cash App activities page.

The table below shows the different values passed and what is presented to the Customer during Grant approval:

| Value passed | What is presented to the Customer during Grant approval                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Client**   | <ul><li>Client name and icon will be displayed during the customer linking process</li> <li>A valid grant scoped to a given client can be used to process a payment for any merchant associated with said client</li> </ul>           |
| **Brand**    | <ul><li>Brand name and icon will be displayed during the customer linking process</li> <li> A valid grant scoped to a given client can be used to process a payment for any merchant associated with said brand</li> </ul>            |
| **Merchant** | <ul><li>Brand name and icon associated with the merchant will be displayed during the customer linking process.</li> <li>A valid grant scoped to a given merchant can only be used to process a payment with said merchant</li> </ul> |

### Example

The “Cash by Cash App” brand icon and name are displayed to the customer during the customer linking desktop flow.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/scan-to-pay.png" alt="Scan to Pay" />

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/icon-and-brand.png" alt="Icon and Brand example" />

## Best Practices

* Brands and merchants should be created asynchronously from the customer request flow. This will minimize unnecessary API calls when the customer is utilizing Cash App Pay.
* Brands and merchants should be created with associated reference IDs.
* Brand and merchant data should be kept up to date with relevant brand and merchant data.
