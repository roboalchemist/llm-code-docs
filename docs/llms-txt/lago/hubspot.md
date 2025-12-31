# Source: https://getlago.com/docs/integrations/crm/hubspot.md

# HubSpot

> Lago syncs billing data to HubSpot in real-time.

<Info>
  **PREMIUM ADD-ON** ✨

  This integration is only available to users with a specific paying add-on. Please
  **[contact us](mailto:hello@getlago.com)** to get access to HubSpot CRM integration.
</Info>

<Warning>
  This integration is a one-way sync, where Lago continuously syncs billing data to HubSpot in real time.
  Currently, it doesn’t support fetching information or taking actions from HubSpot back to Lago.
</Warning>

## Object mapping

<Info>
  As Lago needs to sync billing data to HubSpot custom objects, your HubSpot account needs to be on the **Sales Hub Enterprise** plan.
</Info>

<Frame caption="Lago to HubSpot object mapping">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=38d032e0fd593f1066da319382f7cf3c" data-og-width="4852" width="4852" data-og-height="3334" height="3334" data-path="integrations/images/hubspot-crm-integration-objects-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d49ee8514d90e44ff4e7a8299c0b20d1 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e0a2b33920a35346a26a3e84c39540f7 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=92d8d201f06b8372c3dd546feda7115e 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=44124049515b6cb0eea4396b3185ba88 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b63cc27fe786ab355a2a2b1c5077592b 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-crm-integration-objects-mapping.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=135554a188a08deed26d5292ab9cccc5 2500w" />
</Frame>

## Integration configuration

### oAuth connection

<Frame caption="Connect Lago to HubSpot through an oAuth connection">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=aede79be375948fb2411ffe12c7e1c30" data-og-width="2960" width="2960" data-og-height="1614" height="1614" data-path="integrations/images/hubspot-integration-connect-screen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b6843fc3c6e19d2f607d0c164a94e824 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=93b1653a60c68582e7e9adeda72f6b0f 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0b1d28acad8751cc318bc3b0db3d3b3f 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7918a6140569061bc7deac4804c0b0d5 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7f7972169345dc1c1697aec51c4df530 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-connect-screen.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=39d1dce8a81a696835c0fd4ccdbc2635 2500w" />
</Frame>

To fully integrate Lago with HubSpot, start by connecting your Lago instance to a new HubSpot connection. You can have an unlimited number of HubSpot connections. First, link your HubSpot account to Lago. Once connected, activate the specific syncs and actions required for your use case. This ensures that your Lago instance is properly configured to communicate with HubSpot, enabling seamless data synchronization and management.

1. In Lago, navigate to **Integrations** > **HubSpot**;
2. Create a **new HubSpot connection**;
3. Assign a unique **name** and **code** to the connection;
4. Select the **default targeted object** for Lago customers between HubSpot Contacts or Companies; and
5. Use OAuth2 to grant access to the desired HubSpot account.

There you go, Lago is fully connected to HubSpot!

<Frame caption="Lago to HubSpot - oAuth connection flow">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4fdaa2061cb2d1dc5de11dc8eeb585a9" data-og-width="2818" width="2818" data-og-height="914" height="914" data-path="integrations/images/hubspot-integration-oauth-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cd1f45ffa7509697a17f48aaba33e35e 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5cf953a83299c4f30275cb5e34670c34 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1467a4dbf116ac81b6318968292f97aa 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=db8c4167f030108e3dfb1ff1996265e2 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5520e1a4175c9e4c002ac533196ca8b0 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-oauth-flow.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=169842d1de0d6ab0b14fbfd3d297b9f8 2500w" />
</Frame>

### List of scopes

Here's a list of scopes you grant to Lago when connecting your HubSpot instance: `oauth`, `crm.objects.companies.read`, `crm.objects.companies.write`,
`crm.objects.custom.read`, `crm.objects.custom.write`, `crm.schemas.companies.read`, `crm.schemas.companies.write`, `crm.schemas.custom.read`,
`crm.objects.contacts.read`, `crm.objects.contacts.write`, `crm.schemas.contacts.read`, `crm.schemas.contacts.write` and `crm.schemas.custom.write`.

### Custom properties deployment

By connecting HubSpot to Lago, **custom properties are automatically added to both your HubSpot Companies and Contacts** (native objects).
These fields are used to sync customer data between HubSpot and Lago.

* `lago_customer_id`: internal id of a Lago customer (unique);
* `lago_customer_external_id`: your customer's external id in Lago;
* `lago_billing_email`: your customer's billing email in Lago;
* `lago_tax_identification_number`: your customer's tax identification number in Lago; and
* `lago_customer_link`: the URL path to the related Lago customer.

<Frame caption="Custom properties deployed by Lago to HubSpot Companies and Contacts">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=363058945ac35435cb019928cead3d46" data-og-width="2540" width="2540" data-og-height="1070" height="1070" data-path="integrations/images/hubspot-integration-custom-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d5f2e626436f6edce39014ae53a9c1b0 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=23f6e87b2369b2efed55bbec82f35ccc 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9d45a197d8a86386f63c205e5fad663f 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7765cc95132b31410d18858d6f7a9dfb 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=53f0d1e4a60e0c89dceb94efa2e41be4 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-custom-properties.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9580632923e18b967e9ef2098519fda5 2500w" />
</Frame>

<Info>
  Note that custom properties are deployed in the background the first time the connection is created.
</Info>

### Custom objects deployment

By connecting HubSpot to Lago, 2 custom objects are automatically deployed to your HubSpot instance: `LagoSubscriptions` and `LagoInvoices`.

<Info>
  Note that custom objects are deployed in the background the first time the connection is created. They are automatically tied to HubSpot Contacts or Companies.
</Info>

#### LagoSubscriptions

Here is the list of properties deployed with the `LagoSubscriptions` custom object:

| HubSpot Property Name            | Type        | Field Type | Has Unique Value |
| -------------------------------- | ----------- | ---------- | ---------------- |
| Lago Subscription Id             | string      | text       | true             |
| Lago External Subscription Id    | string      | text       | false            |
| Lago Subscription Name           | string      | text       | false            |
| Lago Subscription Plan Code      | string      | text       | false            |
| Lago Subscription Status         | string      | text       | false            |
| Lago Subscription Created At     | date        | date       | false            |
| Lago Subscription Started At     | date        | date       | false            |
| Lago Subscription Ending At      | date        | date       | false            |
| Lago Subscription At             | date        | date       | false            |
| Lago Subscription Terminated At  | date        | date       | false            |
| Lago Subscription Trial Ended At | date        | date       | false            |
| Lago Subscription Link           | string      | file       | false            |
| Lago Billing Time                | enumeration | radio      | false            |

#### LagoInvoices

Here is the list of properties deployed with the `LagoInvoices` custom object:

| HubSpot Property Name                 | Type   | Field Type      | Has Unique Value |
| ------------------------------------- | ------ | --------------- | ---------------- |
| Lago Invoice Id                       | string | text            | true             |
| Lago Invoice Number                   | string | text            | false            |
| Lago Invoice Issuing Date             | date   | date            | false            |
| Lago Invoice Payment Due Date         | date   | date            | false            |
| Lago Invoice Payment Overdue          | bool   | booleancheckbox | false            |
| Lago Invoice Type                     | string | text            | false            |
| Lago Invoice Status                   | string | text            | false            |
| Lago Invoice Payment Status           | string | text            | false            |
| Lago Invoice Currency                 | string | text            | false            |
| Lago Invoice Total Amount             | number | number          | false            |
| Lago Invoice Subtotal Excluding Taxes | number | number          | false            |
| Lago Invoice File URL                 | string | file            | false            |
| Lago Invoice Link                     | string | file            | false            |

## Sync data from Lago to HubSpot

### Sync customers to HubSpot

When you create or update a customer in Lago, the information is synced in real time to your HubSpot account. Please note the following:

* If `customer.customer_type` in Lago is `company`, the data is synced as a HubSpot Company record.
* If `customer.customer_type` in Lago is `individual`, the data is synced as a HubSpot Contact record.
* If `customer.customer_type` is undefined, the data is synced using the default Customer Object set at the connection level.

<Frame caption="Customer syncs from Lago to HubSpot">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4d8626209275712404ba7d3093248c0e" data-og-width="2942" width="2942" data-og-height="1262" height="1262" data-path="integrations/images/hubspot-integration-customer-sync.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7b53c78a730992c688a056dd657b6f57 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f674bd60e8d4b7ad57d78f53226fb855 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9f95490129088b491275bdcb1168c08b 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1ba243895ef167679afff17892c5b225 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=43984a900ba01f0b352a724dd7a6bbb4 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-customer-sync.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9bab8facffca2b81dfe12632dfa73341 2500w" />
</Frame>

<Frame caption="Example of a Company created by Lago">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c796ff7a1a6a393b2a54b2d8564de2d1" data-og-width="2814" width="2814" data-og-height="786" height="786" data-path="integrations/images/hubspot-integration-create-company.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3b4c35251c6bcf85530f13e43726c79d 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c769760cac40189c5cbec4fbfe43b6b5 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=91ce92d2ef335b50005c524fb01466c8 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8906f7511c05469fcacf757fb59cfb6c 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f32d3d63502d7740db5b74492f9d1360 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/hubspot-integration-create-company.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=2a0af39abdb9c3eb032179bd4decb5b7 2500w" />
</Frame>

You can instruct Lago to automatically create a new Company or Contact in your HubSpot account, or link an existing one by pasting a HubSpot ID into the corresponding Lago customer record.

### Sync subscriptions to HubSpot

Whenever a Lago customer is linked to a HubSpot Contact or Company, **Lago Subscriptions are automatically synced in real-time with the `LagoSubscriptions` object in HubSpot**.
The subscription record is then automatically associated with the corresponding Contact or Company in HubSpot.

### Sync invoices to HubSpot

Whenever a Lago customer is linked to a HubSpot Contact or Company, **Lago Invoices are automatically synced in real-time with the `LagoInvoices` object in HubSpot**.
The invoice record is then automatically associated with the corresponding Contact or Company in HubSpot.
