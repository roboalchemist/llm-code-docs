# Source: https://getlago.com/docs/integrations/accounting/xero.md

# Xero

> Lago seamlessly integrates with Xero, enabling real-time synchronization of billing data with your preferred accounting tool.

<Info>
  **PREMIUM ADD-ON** ✨

  This integration is available upon request only. Please **[contact us](mailto:hello@getlago.com)** to get access to this premium integration.
</Info>

## Connecting Lago to Xero

To fully integrate Lago with Xero, start by connecting your Lago instance to a new Xero connection.
You can have an unlimited number of Xero connections. First, link your Xero account to Lago.
Once connected, activate the specific syncs and actions required for your use case.
This ensures that your Lago instance is properly configured to communicate with Xero, enabling seamless data synchronization and management.

1. In Lago, navigate to **Integrations > Xero**;
2. Create a **new Xero connection**;
3. Assign a unique **name** and **code** to the connection; and
4. Use OAuth2 to **grant access** to your Xero instance.

There you go, Lago is fully connected to Xero!

<Frame caption="Granting access to Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=136dcfdc508d4455ac20cd92ca9a0d07" data-og-width="1704" width="1704" data-og-height="1274" height="1274" data-path="integrations/images/xero-grant-access-lago.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=6a8abe996a41098fa5cac165692fa105 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=78bde6b6e1cf0e78e2f5e474a0fe5a0b 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=38559d471a47fac75ded96f73c48177e 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d469947557008e44473584c282448c84 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=9def0658b3587e28f0c1042e8e3f302a 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-grant-access-lago.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=cddd21cb972256cd38328dd4989a2652 2500w" />
</Frame>

## Enable actions and syncs

Here is a list of syncs and actions that Lago uses with Xero. Some are mandatory, while others are optional:

* `Accounts`: Fetch account data from Xero *(mandatory)*;
* `Customers`: Syncs or fetch customer data from Xero *(mandatory)*;
* `Items`: Fetch item data from Xero *(mandatory)*;
* `Invoices`: Syncs invoice data to Xero *(mandatory)*;
* `Credit Notes`: Syncs credit note data to Xero *(optional)*; and
* `Payments`: Syncs payment data to Xero *(optional)*.

<Frame caption="Granting access to Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=66956b6c07a4508bd59561103ca3679d" data-og-width="2172" width="2172" data-og-height="1416" height="1416" data-path="integrations/images/xero-syncs-and-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=eefadf3561c6dab06780b7c821eddd13 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=626ff82213aee3dd289fccb6aae8c8e2 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1197be77e5912525e6899cf6722a3e6e 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=7a8fec385c2e2660ff4e39ae1b42caa9 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d0923dc89f2afa2fe782f8390ddd3b5c 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-syncs-and-actions.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=199e6ed68bcf8d612aca4d530a570d76 2500w" />
</Frame>

## Mapping items between Lago and Xero

To sync invoices, credit notes and payments to Xero, Lago maps each Lago object to a corresponding Xero object (one-to-one). You can define mappings per Lago entity when different entities require distinct Xero items. If the same mapping applies across entities, configure a default mapping. It will be used for any entity that doesn't have a specific override.

Follow these steps to map an item:

* **Access a Xero Connection in Lago:** navigate to your connected Xero integration within the Lago platform;
* **Select the Item to map:** click on the specific item in Lago that you wish to map to a corresponding Xero item;
* **Fetch Items from Xero:** Lago will automatically retrieve the relevant items from your Xero instance;
* **Map the Item:** choose the appropriate Xero item from the list provided by Lago; and
* **Click 'Save'** to finalize the mapping.

### Mapping a fallback item (mandatory)

The fallback item is a dummy item used as a backup in case the mapping of other objects fails.
To ensure continuous data synchronization between Lago and Xero, this fallback item will be used whenever there is a mapping issue.

<Info>
  This mapping follows a one-to-many structure, meaning that a single fallback item can be used to handle multiple mapping issues.
</Info>

<Frame caption="Map a fallback item between Lago and Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e77837d63e7aff761b0e1e5ef4f4709d" data-og-width="2092" width="2092" data-og-height="1242" height="1242" data-path="integrations/images/xero-mapping-fallback-item.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=849f74bda445e6f92f3437d3d79fdb5e 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=69e18a0ddebb968fafa9803e42a7af92 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=b5f11bb5d7a1967b28e2f4f201bff621 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=952b09b69b506d7c63da8c648804ca48 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=8196a6b20a42fd38555d91f945d1fc54 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-fallback-item.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5382cc4e65703c28c9673c3d897d3fee 2500w" />
</Frame>

### Mapping a payment account (mandatory)

To synchronize invoice payments between Lago and Xero, ensure that at least one payment account is mapped.

To set up a payment account in Xero, follow these steps:

1. Log in to your Xero instance;
2. Navigate to **Accounting > Chart of Accounts**;
3. Select an existing revenue account or create a new one; and
4. When editing or creating the account, ensure the **'Enable payments to this account'** checkbox is selected.

In Lago, you can now map it in the dedicated section '**Account linked to payments**'.

<Frame caption="Map a fallback item between Lago and Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=46159cc8ebefb9bab73989fa04a7fa7a" data-og-width="2176" width="2176" data-og-height="1386" height="1386" data-path="integrations/images/xero-create-payment-account.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c540f8ea4105cb6c03c291b9fceb0009 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=085a694c6b32552ee64da4467509c828 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c64420bd6c7d126a34808cad728b60aa 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=fbca42295842c131e23db6230d81e229 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f3d03b80ec0ba82c8cd80c2bffe5bd9b 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-create-payment-account.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1670120d7d014c0bcfec8f1f2534a090 2500w" />
</Frame>

### Mapping custom objects

Billable metrics and add-ons require a one-to-one mapping. Each billable metric, used for usage-based billing, must represent a specific SKU in your Xero instance.
You need to map each of these individually. Lago will use the mapped items whenever any of these metrics or add-ons appear on the final invoice sent to Xero.

<Info>
  This mapping follows a one-to-one structure, meaning each billable metric or add-on must be mapped to a specific Xero item.
</Info>

<Frame caption="Map custom items between Lago and Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=fe85c274e9dbe82d23b3aae7a5f3f400" data-og-width="2092" width="2092" data-og-height="1232" height="1232" data-path="integrations/images/xero-mapping-custom-objects.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=bb89a4aaf7a921e78c5dfb3ad616a97a 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=37ec3d51b73924236e5f1c6cb6869fd4 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=19b8991b694e0b73bc430327c4a5a060 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=8a781d6baa843551bd65489cc8f7e518 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=8d7d4e4edceed71722ca6fd44a70651b 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-mapping-custom-objects.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=aa135cec45f3a1750f7c6be786a31052 2500w" />
</Frame>

## Customers synchronization

When creating or updating a Lago customer, you can choose to link it to a Xero customer.

The first option is to **automatically create a new customer from Lago to Xero**. Follow these steps:

1. Create or update a new Lago customer;
2. Select the targeted Xero connection;
3. Check the box labeled 'Create this customer automatically in Xero'; and
4. Save and create this new customer.

If the customer is successfully created in Xero, a new field will be displayed in the Lago customer view, providing a direct link to the corresponding Xero customer.

<Info>
  Customer creation from Lago to Xero happens in real-time with only a few seconds of delay.
</Info>

<Frame caption="Lago customer integrated with Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=b2f8bb8271f0afc2ce8cf9ed33d18391" data-og-width="2368" width="2368" data-og-height="992" height="992" data-path="integrations/images/xero-sync-customers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=042c4265d037d56d143030b5a77b7675 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4f81251b5d873d16dcaf47ae95dcf585 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=03ba2ba7cad4911d70b37aaa3c6b1577 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4327f5006d46c13331f0c05f9241e343 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a52830360dc0c7802ed54b66d48ecebf 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-customers.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=6a3b7893b45c7228d77991cabc769e79 2500w" />
</Frame>

The second option is to **import an existing Xero customer to a Lago customer**. Follow these steps:

1. Create or update a Lago customer;
2. Select the targeted Xero connection;
3. Ensure the box labeled 'Create this customer automatically in Xero' is unchecked;
4. Paste the Xero customer ID in the appropriate field; and
5. Save and create this new customer.

**Here is the list of fields that is currently synced to Xero:**

| Lago                                 | Xero         |
| ------------------------------------ | ------------ |
| customer                             | type         |
| customer.name                        | Name         |
| customer.email                       | EmailAddress |
| customer.phone                       | Phones       |
| customer.tax\_identification\_number | TaxNumber    |
| customer.address\_line\_1            | AddressLine1 |
| customer.address\_line\_2            | AddressLine2 |
| customer.city                        | City         |
| customer.zip                         | PostalCode   |
| customer.country                     | Country      |
| customer.state                       | Region       |

## Invoices synchronization

If a Lago customer is linked to a Xero customer, Lago syncs invoices to Xero Invoices in real-time.

It's important to note the following:

* Each fee issued by Lago is synced as a line item on a Xero invoice;
* The Lago fee `units` are synced to Xero as `Quantity`;
* The Lago fee `precise_unit_amount` is synced to Xero as `UnitAmount`;
* Lago can send the total tax amount for a specific line item; and
* Lago can apply discount to a specific line item.

If the invoice is successfully created in Xero, a new field will be displayed in the Lago invoice view, providing a direct link to the corresponding Xero invoice.

<Info>
  Invoice creation from Lago to Xero happens in real-time with only a few seconds of delay.
</Info>

<Frame caption="Sync Lago invoices to Xero">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f3e2d051220bb2c7295adcf257080a41" data-og-width="2470" width="2470" data-og-height="1282" height="1282" data-path="integrations/images/xero-sync-invoices.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=536ff8a2435ac4f12de743de75f47fff 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=398aeb7459e6d83a4f1d064a993c07c4 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=7403785be25cad2f18c4d079fa378db3 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d1365e5651f427088d0e2680a184157d 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=84342e829924fab2ef2bfb20911b625e 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/xero-sync-invoices.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2e9c54acb5f6b28d79627bca5ca3e95e 2500w" />
</Frame>

**Here is the list of fields that is currently synced to Xero:**

| Lago                                        | Xero           |
| ------------------------------------------- | -------------- |
| invoice                                     | type           |
| invoice.number                              | InvoiceNumber  |
| invoice.status                              | Status         |
| invoice.currency                            | CurrencyCode   |
| invoice.issuing\_date                       | Date           |
| invoice.payment\_due\_date                  | DueDate        |
| invoice.fee.units                           | Quantity       |
| invoice.fee.precise\_unit\_amount           | UnitAmount     |
| invoice.fee.amount\_cents                   | LineAmount     |
| invoice.fee.taxes\_amount\_cents            | TaxAmount      |
| invoice.fee.precise\_coupons\_amount\_cents | DiscountAmount |

## Credit Notes synchronization

If a Lago customer is linked to a Xero customer, Lago syncs credit notes to Xero Credit Notes in real-time.

It's important to note the following:

* Each fee refunded by Lago is synced as a line item on a Xero Credit Note; and
* Any discounts on an credit note (like coupon, for instance) are synced as line items on the Xero Credit Note.

If the credit note is successfully created in Xero, a new field will be displayed in the Lago credit note view, providing a direct link to the corresponding Xero Credit Note.

<Info>
  Credit note creation from Lago to Xero happens in real-time with only a few seconds of delay.
</Info>

**Here is the list of fields that is currently synced to Xero:**

| Lago                                          | Xero             |
| --------------------------------------------- | ---------------- |
| credit\_note.number                           | CreditNoteNumber |
| credit\_note.reference                        | Reference        |
| credit\_note.status                           | Status           |
| credit\_note.currency                         | CurrencyCode     |
| credit\_note.issuing\_date                    | Date             |
| credit\_note.line\_item.units                 | Quantity         |
| credit\_note.line\_item.precise\_unit\_amount | UnitAmount       |
| credit\_note.line\_item.amount\_cents         | LineAmount       |
| credit\_note.line\_item.taxes\_amount\_cents  | TaxAmount        |

## Payments synchronization

If a Lago invoice is tied to a Xero invoice, Lago automatically syncs payments occurring in Lago to Xero, updating in-real time the payment status of the invoice in Xero.

| Lago                  | Xero    |
| --------------------- | ------- |
| invoice.id            | Invoice |
| invoice.amount\_cents | Amount  |

## Integration logs

Whenever an issue occurs in Xero, Lago will notify you through a [webhook message](/api-reference/webhooks/messages#accounting-provider-error) called `customer.accounting_provider_error`.
