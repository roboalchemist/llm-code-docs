# Source: https://getlago.com/docs/integrations/taxes/anrok.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Anrok

> Lago's native integration with Anrok allows you to automatically update your invoices with tax amounts sourced directly from Anrok. This integration ensures compliance with international tax regulations by calculating taxes for US & non-US obligations, like VAT.

<Info>
  **PREMIUM FEATURE** ✨

  This feature is only available to users with a premium license. Please
  **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago
  Self-Hosted Premium.
</Info>

## Overview

Lago’s integration with [Anrok](https://www.anrok.com/request-demo?utm_source=lago\&utm_medium=partner_website\&utm_campaign=evergreen) simplifies tax calculation and reporting by syncing invoice amounts with Anrok for filing.

When an invoice is in draft status, Lago generates an ephemeral transaction in Anrok to calculate the preliminary taxes. Once the invoice is finalized, Lago creates a permanent transaction in Anrok to calculate the final taxes, marking it for reporting to the appropriate tax authority via Anrok.

To calculate the appropriate tax for each line item, Lago sends the customer’s address, tax identifier (if applicable), and the relevant product ID to Anrok. Anrok then calculates the tax for the invoice and returns the data to Lago, which is used to update the invoice with accurate tax information. Additionally, Lago synchronizes updates for voided and disputed invoices, as well as any credit notes created, ensuring that your records remain up to date.

## Prerequisites

1. **Premium feature**: To access Anrok via Lago, you’ll need to be under the Premium license.
2. **Getting Started**: We recommend reviewing the [Anrok Getting Started Guide](https://help-center.anrok.com/hc/en-us/categories/4410165176339-Getting-Started-Guide) before initiating the setup process.
3. **Anrok Account**: Ensure you have an Anrok account. Ideally, test the connection via an Anrok sandbox account to your Lago test account. Contact the Anrok team to request a free sandbox account.
4. **Physical Nexus**: Make sure you are correctly recording physical nexus in Anrok. Add or manage your physical nexus through the "Jurisdictions" tab by clicking the “Manage Physical Nexus” button.
5. **Products in Anrok**: Create products in Anrok, assigning a tax configuration to each product you sell in Lago. You will need the IDs of these products when setting up the Anrok integration in Lago (see the mapping below).
6. **Customer Exemptions in Anrok**: If necessary, upload valid exemption certificates for your customers in Anrok. Ensure that when you create a customer profile in Lago, you use the same customer ID as in Anrok. This consistency allows Lago to correctly identify the customer and apply the exemption certificates when calculating taxes.

## Connect Anrok to Lago

Lago allows you to connect your different Anrok instances. For example, you could connect both a sandbox and a production Anrok account. To do so:

1. In Lago, please go to Settings > Integration
2. Click on Anrok
3. Define a name and code for this connection; and
4. Enter your Anrok API key

<Frame caption="Connect Anrok to Lago">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=adcaafd781d75b6cb42dab25b89d3da7" data-og-width="3456" width="3456" data-og-height="2159" height="2159" data-path="integrations/images/anrok-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4fe5c8109527df0517663bedff335b76 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f9c23f47ccbaedfca67737b993995fcd 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=38d1e936e486da128930bfc4f880b175 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=314bbcf24a8a3b4f35f8cbc939814b58 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8ccc83c91a041c1a319260f1af56e05b 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-connection.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=991a1466deb3331f0dcd8600f2a8bea1 2500w" />
</Frame>

### Mapping items between Lago and Anrok (mandatory)

To synchronize invoices and retrieve tax data, Lago needs to establish a one-to-one relationship between its objects and Anrok products.
**You can define tax mappings per Lago entity when different entities require distinct Anrok Product IDs**. If the same mapping applies across entities, configure a default mapping. It will be used for any entity that doesn't have a specific override.

Follow these steps to map an item:

1. In Anrok, navigate to the **Products IDs** section.
2. Click on a product and **copy its Product ID.**
3. In Lago, navigate to **Integration** > **Anrok** > **Mapping**.
4. Choose the item you want to associate with the Product ID selected in step 2.
5. **Paste the Product ID to map the item** — repeat this action for all items in Lago that require mapping.

<Info>
  The invoice will be marked as `failed` if any item requiring tax calculation from Anrok is not properly mapped and no fallback item is provided.
</Info>

### Mapping a fallback item (mandatory)

The fallback item serves as a backup and is used if the mapping of other items is not defined. This dummy item ensures continuous data synchronization between Lago and Anrok in the event of mapping issues.

<Frame caption="Mapping Lago item to Anrok">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e2ece0865049ddb9b2c5ad9fbfd2a242" data-og-width="3457" width="3457" data-og-height="2157" height="2157" data-path="integrations/images/anrok-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4ccbc0f39ba24dc14e7c54612c915ba8 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9ac8fda88783cd53964e1308f8bdc60c 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7d6f1eb3d26f9441fb0c0899a410cf84 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=81e8c02ae4f855218c198b3784a953f6 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8bab61ede9a808c5cee38a8b46c87a60 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-mapping.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=31fae7d34229d92557addf72f657c7ac 2500w" />
</Frame>

## Customer configuration for tax calculation

### Customer synchronization

When creating or updating a Lago customer, you can choose to link it to an existing Anrok customer.

The first option is to **automatically create a new customer from Lago to Anrok**. Follow these steps:

1. Create or update a new Lago customer;
2. Select the targeted Anrok connection;
3. Check the box labeled ‘Create this customer automatically in Anrok’; and
4. Save and create this new customer.

If the customer is successfully created in Anrok, a new field will be displayed in the Lago customer view, providing a direct link to the corresponding Anrok customer.

<Frame caption="Create customer in Anrok">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=99d478e4ae808994599e3e09ea6ca7e0" data-og-width="3456" width="3456" data-og-height="2157" height="2157" data-path="integrations/images/anrok-create-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=63f27d21a81b38cbb103c0572846bd18 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1195a6cb44857bf15f0b073e8ba7b597 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=2be1488af924b902e9a6ab09eded855a 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=34a895443acc0c4ea1df1544bb2d24f5 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6b467b6b1123e5f0ea47d8a1384ffdbb 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-create-customer.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4247cc2360331b6346c13cb812414d86 2500w" />
</Frame>

The second option is to **import an existing Anrok customer to a Lago customer**. Follow these steps:

1. Create or update a Lago customer;
2. Select the targeted Anrok connection;
3. Ensure the box labeled ‘Create this customer automatically in Anrok’ is unchecked;
4. Paste the Anrok customer ID in the appropriate field; and
5. Save and create this new customer.

If the customer is successfully synced in Anrok, a new field will be displayed in the Lago customer view, providing a direct link to the corresponding Anrok customer.

<Frame caption="Sync Anrok customer in Lago">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=527c239995a889046e3967126df84771" data-og-width="3455" width="3455" data-og-height="2162" height="2162" data-path="integrations/images/anrok-sync-customer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c0197dfe1d8e856cfe8fe7fc366f5e3c 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=97aa9fcacad0446bd9284c7ed81e09b6 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d08b3d2340a36ea90c09dd32a1cfc17d 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=463f4701ecfbbd7fae2cc61efb467fb7 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d8490e1b9e4d42574adcd554d5928a05 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-customer.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b4961d42e27afca040fddc671be7e37b 2500w" />
</Frame>

<Info>
  Please note that in both cases, the customer will be created in Anrok after the first invoice is synchronized.​
</Info>

### Address requirements

Anrok requires that each customer in Lago has a valid shipping address. If a shipping address is not available, Lago will default to using the billing address for tax calculation purposes. If both addresses are invalid or missing, Lago will be unable to generate the invoice, and the invoice status will be marked as failed. In such cases, you will be notified of the failure in the dashboard and via webhook.

<Frame caption="Mapping Lago item to Anrok">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cb9a4e3e21389d95e7a9cd3759011143" data-og-width="3457" width="3457" data-og-height="2158" height="2158" data-path="integrations/images/anrok-failed-invoice.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ec2181e6239d54dfc17191e14c5b33cc 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=37a5726a0a7fa353611e3a6c80334afe 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=fd07b9568f7f8cd672fd4a22f915ceff 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=13a5b3d9c061c2a638b1af84315f1cb5 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cf51386a1e093f0df580a794b589ca80 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-failed-invoice.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=a2b080966e79739a5527cc2d53e59442 2500w" />
</Frame>

### Tax identifier

If a customer has a `tax_identification_number` configured in Lago, this ID will be sent to Anrok for tax calculation and reporting. This ID is essential for determining whether the transaction is subject to a reverse charge in eligible VAT countries.

### Tax exempt customers

For customers who qualify for tax exemptions, you need to create a Certificate in your Anrok dashboard. Ensure that the customer profile in Lago uses the same customer ID as in Anrok in the Anrok customer ID. This consistency allows Lago to correctly identify the customer and apply the exemption certificates when calculating taxes.

## Current usage

Lago queries Anrok for the current usage and wallet ongoing balance. To ensure the best experience, Lago caches the results of current usage taxes for 24 hours.

## Error management

### Refresh draft invoice with tax errors

When an invoice is in `draft` and encounters a tax synchronization error, you have the option to refresh the invoice to recalculate the tax. The invoice remains editable during this process, and the error will not prevent the invoice from being `finalized`. However, if the error persists after attempting to finalize the invoice, the invoice will be marked as `failed`.

### Retry synchronization for failed invoice

When an invoice fails due to a tax synchronization error, you have the option to manually re-sync each invoice individually from the invoice details page or via this [endpoint](/api-reference/invoices/retry_finalization). Alternatively, you can go to the integration settings and trigger a bulk invoice synchronization.

<Frame caption="Mapping Lago item to Anrok">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=402a43d6c59f6cd5041e0245fe1a8e2a" data-og-width="3457" width="3457" data-og-height="2158" height="2158" data-path="integrations/images/anrok-sync-all-invoices.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=94f59c5268fd4a7b080900c6519c653e 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=da05f83c8715e9bb85443f9a795b1337 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3f61c07f000caff81e8a63b281eacffc 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=31068a2c97624bdfbab709b7ab6fe97b 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c96c1f7bf5525f05623d1479f973c1ac 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/anrok-sync-all-invoices.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8297352caba4f2c056d1e3362b51e292 2500w" />
</Frame>

### Retry synchronization for voided / disputed invoices

When an invoice is voided or disputed, Lago will sync this updated record with Anrok to ensure your reports are accurate. If the sync fails, you will be notified via webhook. In that case, please manually resync the voided or disputed invoice through the dashboard.

### Retry synchronization for credit notes

When a credit note is created, Lago will sync this record with Anrok to ensure your reports are accurate. If the sync fails, you will be notified via webhook. In that case, please manually resync the credit note through the dashboard.

### Pay in advance non invoiceable charge

Lago will notify you via webhook if a tax error occurs when a non-invoiceable fee paid in advance is generated. The fee will not be created. Please note that you will need to fix the issue and resend the event to generate the fee. For any assistance, please contact the Lago team.

### Tax error scenario

If Lago is unable to generate an invoice or sync it to Anrok, you will be alerted via the dashboard and webhook.
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
