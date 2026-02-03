# Source: https://getlago.com/docs/integrations/taxes/avalara.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Avalara

> Lago's native integration with Avalara allows you to automatically update your invoices with tax amounts sourced directly from Avalara. This integration ensures compliance with international tax regulations by calculating taxes for US & non-US obligations, like VAT.

<Info>
  **PREMIUM ADD-ON** ✨

  This integration is available upon request only. Please **[contact us](mailto:hello@getlago.com)** to get access to this premium feature.
</Info>

## Overview

Lago’s native integration with **AvaTax** (by Avalara) enables seamless tax calculation, application, and reporting throughout the invoicing process.

When an invoice is in `draft` status, Lago creates a `SalesOrder` in AvaTax to estimate the applicable taxes.
This preliminary calculation allows teams to preview tax amounts before finalizing the invoice.

Once the invoice is `finalized` in Lago, a corresponding `SalesInvoice` is created in AvaTax.
This marks the transaction as final and eligible for reporting to the appropriate tax authorities, ensuring compliance and traceability.

To calculate tax, Lago includes both the `ShipFrom` and `ShipTo` addresses for each invoice.
AvaTax uses these details to apply tax rules based on the nexus jurisdictions you’ve configured in your Avalara account.

The calculated tax data is returned from AvaTax and automatically applied to the Lago invoice.

Lago also keeps your records in sync by automatically updating AvaTax whenever an invoice is voided or disputed, or when a credit note is issued.
This ensures that your tax reporting in Avalara remains accurate and up to date at all times.

## Prerequisites

1. **Premium add-on feature**: To access Avatax via Lago, you must have access to the Premium add-on. If you don’t already have it enabled, please reach out to us for assistance.
2. **Getting Started**: We strongly recommend reviewing the [AvaTax Getting Started Guide](https://developer.avalara.com/documentation/sales-and-use-tax/) to familiarize yourself with the requirements and configuration steps.
3. **Billing entity address**: For accurate tax calculation, Avalara requires a valid ShipFrom address. This corresponds to the billing entity’s account address and must be configured in the Lago dashboard under **Settings > Entity > General information**.
4. **Nexus in Avalara**: Make sure your Avalara account is properly set up with all `nexus` jurisdictions. These are the states or regions where you are obligated to collect and remit sales tax.
5. **Customer exemptions**: If necessary, upload valid exemption certificates for your customers in Avalara. Ensure that when you create a customer profile in Lago, you use the same customer ID as in Avalara. This consistency allows Lago to correctly identify the customer and apply the exemption certificates when calculating taxes.

## Connect AvaTax to Lago

Lago supports connections to multiple AvaTax instances, enabling you to integrate both sandbox and production environments seamlessly.

**To connect an AvaTax instance:**

1. Navigate to **Settings > Integrations** in your Lago dashboard
2. Select **Avalara** from the available integrations
3. Create a unique name and code to identify this connection
4. Enter your Avalara credentials: Account ID, License key and Company code
5. Click **Create** to establish the connection

### Mapping items between Lago and Avalara (mandatory)

To synchronize invoices and retrieve tax data, Lago needs to establish a one-to-one relationship between its objects and Avalara products.
**You can define tax mappings per Lago entity when different entities require distinct Avalara Product IDs**. If the same mapping applies across entities, configure a default mapping. It will be used for any entity that doesn't have a specific override.

Follow these steps to map an item:

1. Navigate to the [Avalara Tax Code search](https://taxcode.avatax.avalara.com/) documentation page.
2. Click on a product and **copy its Tax code.**
3. In Lago, navigate to **Integration** > **Avalara** > **Mapping**.
4. Choose the item you want to associate with the Tax code selected in step 2.
5. **Paste the Tax code to map the item** — repeat this action for all items in Lago that require mapping.

<Info>
  The invoice will be marked as `failed` if any item requiring tax calculation from Avalara is not properly mapped and no fallback item is provided.
</Info>

### Mapping a fallback item (mandatory)

The fallback item serves as a backup and is used if the mapping of other items is not defined.
This dummy item ensures continuous data synchronization between Lago and Avalara in the event of mapping issues.

<Frame caption="Mapping Lago item to Avalara">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=be82aad6ded12c2aa8b204e7a5df46db" data-og-width="2777" width="2777" data-og-height="1632" height="1632" data-path="integrations/images/avalara-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=65ca8738ce48401d35c8b126500badb5 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b128814f8caf272b6eca742118ec6478 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8729d1743cc4b87abcff5c997fafe0b1 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d78a64933317ad7d88ba9489b2390c83 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f9fb9dee5012cd5edf25c469e29db88f 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-mapping.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=bc90f2edfb4687f7e8e1081c17f79cac 2500w" />
</Frame>

## Customer configuration for tax calculation

### Customer synchronization

When creating or updating a Lago customer, you can establish a connection to an existing Avalara customer or automatically create a new one.

**Automatically creating a new Avalara customer**

To create a new customer in Avalara directly from Lago:

1. Create or update a Lago customer;
2. Ensure the customer has a valid address;
3. Verify the customer's state uses valid two or three-character ISO 3166 region codes;
4. Select your target Avalara connection;
5. Check the box labeled "Create this customer automatically in Avalara"; and
6. Save the customer to complete the process.

<Frame caption="Automatically creating a new Avalara customer">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=25c51ba8cabba42d9bc74abd60278311" data-og-width="2777" width="2777" data-og-height="1632" height="1632" data-path="integrations/images/avalara-create-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=77518d626314cbd2d3a2fb6aac68832c 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5d672d79ef68568e765471d73a7e5f16 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ae44bb61ecd9c9f5f07a53920896db7b 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=40d47ea374a40785e2d368b99815f4b6 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=886b46a6d11e3a0efd3292e1fd952463 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-create-customer.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=034799cc9b947b61e8b2502dc7ca3b3f 2500w" />
</Frame>

**Results:**

* **Success**: A new field appears in the Lago customer information tab with a direct link to the corresponding Avalara customer
* **Failure**: The `customer.tax_provider_error` webhook is triggered to notify you of any issues

**Importing an existing Avalara customer**

To link a Lago customer to an existing Avalara customer:

1. Create or update a Lago customer
2. Select your target Avalara connection
3. Ensure the box labeled "Create this customer automatically in Avalara" is unchecked
4. Enter the existing Avalara customer ID in the designated field
5. Save the customer to complete the import

<Frame caption="Importing an existing Avalara customer">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=52886d12b136e0ef560606a412e43e77" data-og-width="2777" width="2777" data-og-height="1632" height="1632" data-path="integrations/images/avalara-sync-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3538e16d676e8db8c4ceb6c867134960 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=28a85cfc22ae1ba616031290545bfa35 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6dfe3916d921d4d9429eab5be622dbaf 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8cdaa51347941ce70db9bf7d128dfe91 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=a6e5b0a9e63b6181178b59e670d4fc4d 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/avalara-sync-customer.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5aa3b84251b793cb0bc1cab10406fe7d 2500w" />
</Frame>

**Results**:

* **Success**: A new field appears in the Lago customer information tab with with a direct link to the corresponding Avalara customer
* **Failure**: The `customer.tax_provider_error` webhook is triggered if the sync encounters issues

### Address requirements

Avalara requires that each customer in Lago has a valid shipping address with a valid state following the two or three character **ISO 3166 region codes**.
If a shipping address is not available, Lago will default to using the billing address for tax calculation purposes.
If both addresses are invalid or missing, Lago will be unable to generate the invoice, and the invoice status will be marked as failed.
In such cases, you will be notified of the failure in the dashboard and via webhook.

<Frame caption="Mapping Lago item to Avalara">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cb9a4e3e21389d95e7a9cd3759011143" data-og-width="3457" width="3457" data-og-height="2158" height="2158" data-path="integrations/images/anrok-failed-invoice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ec2181e6239d54dfc17191e14c5b33cc 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=37a5726a0a7fa353611e3a6c80334afe 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=fd07b9568f7f8cd672fd4a22f915ceff 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=13a5b3d9c061c2a638b1af84315f1cb5 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cf51386a1e093f0df580a794b589ca80 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=a2b080966e79739a5527cc2d53e59442 2500w" />
</Frame>

### Customer exemptions

If you need to apply exemptions to a customer, you can upload valid exemption certificates for your customers in Avalara.
Ensure that when you create a customer profile in Lago, you use the same customer ID as in Avalara.
This consistency allows Lago to correctly identify the customer and apply the exemption certificates when calculating taxes.

### Tax identifier

If a customer has a `tax_identification_number` configured in Lago, this ID will be sent to Avalara for tax calculation and reporting. This ID is essential for determining whether the transaction is subject to a reverse charge in eligible VAT countries.

### Tax exempt customers

For customers who qualify for tax exemptions, you need to create a Certificate in your Avalara dashboard. Ensure that the customer profile in Lago uses the same customer ID as in Avalara in the Avalara customer ID. This consistency allows Lago to correctly identify the customer and apply the exemption certificates when calculating taxes.

## Current usage

Lago queries Avalara for the current usage and wallet ongoing balance. To ensure the best experience, Lago caches the results of current usage taxes for 24 hours.

## Error management

### Refresh draft invoice with tax errors

When an invoice is in `draft` and encounters a tax synchronization error, you have the option to refresh the invoice to recalculate the tax. The invoice remains editable during this process, and the error will not prevent the invoice from being `finalized`. However, if the error persists after attempting to finalize the invoice, the invoice will be marked as `failed`.

### Retry synchronization for failed invoice

When an invoice fails due to a tax synchronization error, you have the option to manually re-sync each invoice individually from the invoice details page or via this [endpoint](/api-reference/invoices/retry_finalization). Alternatively, you can go to the integration settings and trigger a bulk invoice synchronization.

<Frame caption="Mapping Lago item to Avalara">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=402a43d6c59f6cd5041e0245fe1a8e2a" data-og-width="3457" width="3457" data-og-height="2158" height="2158" data-path="integrations/images/anrok-sync-all-invoices.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=94f59c5268fd4a7b080900c6519c653e 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=da05f83c8715e9bb85443f9a795b1337 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3f61c07f000caff81e8a63b281eacffc 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=31068a2c97624bdfbab709b7ab6fe97b 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c96c1f7bf5525f05623d1479f973c1ac 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8297352caba4f2c056d1e3362b51e292 2500w" />
</Frame>

### Retry synchronization for voided / disputed invoices

When an invoice is voided or disputed, Lago will sync this updated record with Avalara to ensure your reports are accurate. If the sync fails, you will be notified via webhook. In that case, please manually resync the voided or disputed invoice through the dashboard.

### Retry synchronization for credit notes

When a credit note is created, Lago will sync this record with Avalara to ensure your reports are accurate. If the sync fails, you will be notified via webhook. In that case, please manually resync the credit note through the dashboard.

### Pay in advance non invoiceable charge

Lago will notify you via webhook if a tax error occurs when a non-invoiceable fee paid in advance is generated. The fee will not be created. Please note that you will need to fix the issue and resend the event to generate the fee. For any assistance, please contact the Lago team.

### Tax error scenario

If Lago is unable to generate an invoice or sync it to Avalara, you will be alerted via the dashboard and webhook.
Tax synchronization and invoice generation can fail due to the following reasons:

1. Incorrect connection settings (API key).
2. Items used in objects or fallback items not mapped.
3. Missing customer shipping or billing address.
4. Timeout or internal service error.

Tax synchronization can fail during the following processes:

1. Calculating taxes in one-off-invoice form
2. Refreshing a draft invoice
3. Finalizing an invoice
4. Generating a fee paid in advance non-invoiceable
5. Fetching current usage
6. Voiding an invoice
7. Disputing an invoice
8. Creating a credit note

If an issue arises, please check the mapping, verify the customer address and launch a synchronization; or contact the Lago team for assistance.
