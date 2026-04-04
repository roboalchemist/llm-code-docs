# Source: https://getlago.com/docs/integrations/accounting/netsuite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# NetSuite

> Lago seamlessly integrates with NetSuite, enabling real-time synchronization of billing data with your preferred accounting tool.

<Info>
  **PREMIUM ADD-ON** ✨

  This integration is available upon request only. Please **[contact us](mailto:hello@getlago.com)** to get access to this premium integration.
</Info>

## RESTlet script configuration

Lago's native integration with NetSuite utilizes a [custom RESTlet script](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4618456517.html) to provide maximum flexibility in fetching or pushing billing data. To set up the Lago RESTlet script in your NetSuite instance, follow these steps:

### Upload Lago Scripts

1. In NetSuite, go to **Documents > Files > File Cabinet**;
2. Under `SuiteScripts`, create a new folder named `Lago`;
3. **Upload `ramda.min.js`**: This library is essential for using Lago and can be downloaded from [here](https://github.com/ramda/ramda/blob/master/dist/ramda.min.js); and
4. Upload another file into the `Lago` folder and **paste the script provided by your Lago Account Manager**.

<Frame caption="Upload scripts provided by Lago">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=6eecd5b84c99da35e7bf5ab62eb11558" data-og-width="1448" width="1448" data-og-height="446" height="446" data-path="integrations/images/upload-netsuite-scripts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=b93c866c559879fac3e473ed58d04f60 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f9c91675d2fa7f8aef628f43ae8006f3 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=9dd5f36b9d1d55baae994010da69ee7e 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1315d8ce3bf23065c6f8f40b2fb91797 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=ac0022905399f739f2b9721b89ba2be3 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/upload-netsuite-scripts.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=df2297e51ccafce7849975ea3f37eaa8 2500w" />
</Frame>

### Deploy Lago Scripts

1. Navigate to **Customization > Scripting > Scripts > Create a New Script**;
2. Deploy the Lago script for **All roles** and **All employees** (you can create custom roles if needed); and
3. Make sure to change the script status to `released`.

By deploying this script, you'll generate a **custom endpoint url** that is crucial for the authentication process and enables seamless data synchronization between Lago and NetSuite.

## Mandatory NetSuite settings

To ensure the sync doesn't fail, verify that the following settings are correctly configured. This will enable Lago to sync data to NetSuite properly.

### Remove Locations on invoices and credit memos

Lago doesn't recognize the location field on invoices, which is mandatory by default. To resolve this, remove the location requirement from your invoice form:

1. Navigate to **Customization > Forms > Transaction Forms**;
2. Locate the form related to your invoices;
3. Go to the **Screen Fields** tab; and
4. Find the Location field and **uncheck both the Show and Mandatory checkboxes**.

<Frame caption="Remove Locations on invoices">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1e948c38f227b06419704bd395549d10" data-og-width="2498" width="2498" data-og-height="424" height="424" data-path="integrations/images/netsuite-remove-locations-field.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2c876f022206d75caa3950dbe088ad3b 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=47bc9f39e21011cf743113d1adb59fbe 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5290baec73bce86bd3798d7de6280af1 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=b9c008f28477fdb6ac659de556645e10 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=f4d9d79f5d16c4b3ce8bdd8122b3234e 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-remove-locations-field.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a0ce8a7b4837fc7e5743839441c3016e 2500w" />
</Frame>

<Info>
  You can repeat the same operation for Credit Memos
</Info>

### Create Lago Tax Nexus, Type and Code

To have Lago override the tax details for your invoice line items, follow these steps. If not, Lago will send the amount excluding taxes to NetSuite.

<Steps>
  <Step title="Step 1: Create a Lago Tax Nexus">
    1. Go to **Setup** > **Tax** > **Nexuses** > **New**;
    2. Choose a brand new **Nexus** (⚠️ ensure it's unused by other existing tax nexuses. It can be a new state for an existing country, or a new country.);
    3. Enter `Lago Tax Nexus` in the **Description** field;
    4. Create a new **Tax Agency** by clicking the **+** button. Name it `Lago Tax Agency` and assign it to the relevant parent subsidiary;
    5. Save your new Nexus;
    6. Add this newly created Nexus to the targeted NetSuite Subsidiaries by navigating to **Setup > Company > Subsidiaries**. Select the parent subsidiary, and add this new nexus in the **Tax Registrations** tab; and
    7. Ensure that the tax engine for this registration is set to `SuiteTax Engine`.
  </Step>

  <Step title="Step 2: Create a Lago Tax Type">
    1. Navigate to **Setup** > **Tax** > **Tax Types** > **New**;
    2. Select the same **Country** as the one used in the Lago Tax Nexus;
    3. Name it `Lago Tax Type`;
    4. **Link the Lago Tax Nexus** in the Nexus section;
    5. Add a **Payables Account** and a **Receivables Account** to this new Tax Type; and
    6. Save it.
  </Step>

  <Step title="Step 3: Create a Lago Tax Code">
    1. Go to **Setup** > **Tax** > **Tax Code** > **New**;
    2. Enter a **Name**, like `Lago Tax`;
    3. Select and tie the previously created Lago Tax Type; and
    4. Save your settings.
  </Step>
</Steps>

### Define Taxable items

To enable tax amount overrides for your Lago invoices synced to NetSuite, ensure all items are marked as taxable. If any item is non-taxable, the invoice sync will fail. To update an item:

1. Go to **Lists > Accounting > Items**;
2. Edit the item associated with a Lago object;
3. Navigate to the **Accounting** tab;
4. Locate the **Tax / Tariff** section; and
5. Set the item to **Taxable**.

<Frame caption="Define Taxable items">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2edaea6acfbfc0c833cec14ad30786d8" data-og-width="2622" width="2622" data-og-height="830" height="830" data-path="integrations/images/netsuite-taxable-items.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=30ebfba50a6c1625a077581ce6faa563 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=0068c6594aecbabaee7a4a98ede71e21 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a88064467c3160ac5fe633f416732751 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4ada2521c44be20c0438557a029e4d70 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=0d180d2e33be40de3d57cf2727ecafd4 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-taxable-items.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=005654905d06fa26f1d4e89c8e3f7d4d 2500w" />
</Frame>

## Connecting Lago to NetSuite

To fully integrate Lago with NetSuite, start by connecting your Lago instance to a new NetSuite connection.
You can have an unlimited number of NetSuite connections. First, link your NetSuite account to Lago.
Once connected, activate the specific syncs and actions required for your use case.
This ensures that your Lago instance is properly configured to communicate with NetSuite, enabling seamless data synchronization and management.

### Create a new integration in NetSuite

After logging into your NetSuite account, navigate to **Setup > Integration > Manage Integrations > New**.
Enter the required integration details and follow these steps:

* Make sure the [oAuth feature is enabled](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157771482304.html#To-enable-OAuth-2.0-feature%3A) for your NetSuite instance;
* Make sure the *SOAP WEB SERVICES* and *REST WEB SERVICES* features are enabled in **NetSuite > Company > Enable Features > SuiteCloud**;
* Under Authentication, select **TOKEN-BASED AUTHENTICATION**;
* Disable *TBA: AUTHORIZATION FLOW* and *AUTHORIZATION CODE GRANT*; and
* Save your new integration.

The Client Credentials will be displayed. **Copy the `Consumer Key/Client ID` and `Consumer Secret/Client Secret`** and save them in a secure document for future reference, as this information will not be accessible once you leave the screen.

<Frame caption="Create a new NetSuite Integration">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a8c34b0dd01da9ec2874b39812faee4e" data-og-width="2860" width="2860" data-og-height="1592" height="1592" data-path="integrations/images/netstuite-tba-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=bbb468eb034f0622002442219f14d264 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=93089bdd89ba9fbb2ca6c5b8cf98f515 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=bd9df02554760ec33074b3dc4793128c 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=cc88e1db00b8b7bbe3f000525693abc7 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e94e557e3881251171f3528a2ef5bf5f 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netstuite-tba-integration.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=fc4cb0ce1c2b25691041b02514a8952e 2500w" />
</Frame>

### Create a new access token in NetSuite

* Log into your NetSuite account and navigate to the homepage by **clicking the home icon**;
* In the **Settings** section at the bottom left corner, locate and click the **Manage Access Tokens** button;
* Select the **Application Name** created for this integration;
* Enter a **token Name**; and
* Save your new access token.

The Token Credentials will be displayed. **Copy the `Token ID` and `Token Secret`** and save them in a secure document for future reference, as this information will not be accessible once you leave the screen.

<Frame caption="Create a new NetSuite My Access Token">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=63d76160ad91e24ec83ffbbf75fb5116" data-og-width="2892" width="2892" data-og-height="1344" height="1344" data-path="integrations/images/create-netsuite-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d9f265287dba3e6b681a798c9761607c 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=2f41cd34115038b014994600cbe974a2 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0c79bf7d4b7ed71d11b1754cdc859ad0 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9a1a1185aabc529ef880e5d7d99480ba 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4d8200259d1777cc3bf6aa2900151750 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/create-netsuite-token.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=fb926bd48da233bc7be0c1cfbebeba7e 2500w" />
</Frame>

### Authentication flow

The authentication process connects Lago and NetSuite through OAuth2.
To establish this connection, you need to provide the following mandatory fields:

* **Connection Name:** an internal name for the connection within Lago;
* **Unique Connection Code:** an internal code for the connection within Lago;
* **NetSuite Account ID:** your NetSuite [account identifier](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1498754928.html#:~:text=You%20can%20find%20your%20NetSuite,an%20underscore%2C%20for%20example%20123456_RP.);
* **NetSuite Client ID:** the [client ID](/integrations/accounting/netsuite#create-a-new-integration-in-netsuite) from your NetSuite account;
* **NetSuite Client Secret:** the [client secret](/integrations/accounting/netsuite#create-a-new-integration-in-netsuite) from your NetSuite account;
* **NetSuite Token Id:** the [token ID](/integrations/accounting/netsuite#create-a-new-access-token-in-netsuite) from your NetSuite account;
* **NetSuite Token Secret:** the [token secret](/integrations/accounting/netsuite#create-a-new-access-token-in-netsuite) from your NetSuite account;
* **Custom RESTlet Endpoint:** The endpoint created from the [custom RESTlet script](/integrations/accounting/netsuite#restlet-script-configuration).

### Enable actions and syncs

Here is a list of syncs and actions that Lago uses with NetSuite. Some are mandatory, while others are optional:

* `Customers`: Syncs or fetch customer data from NetSuite Customers *(mandatory)*;
* `Invoices`: Syncs invoice data to NetSuite Invoices *(optional)*;
* `Credit Notes`: Syncs credit note data to NetSuite Credit Memos *(optional)*; and
* `Payments`: Syncs payment data to NetSuite Customer Payments *(optional)*.

<Frame caption="Connect Lago to NetSuite">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=80b151fa5eb11750e0c1edb4ecc72bbe" data-og-width="3288" width="3288" data-og-height="1870" height="1870" data-path="integrations/images/connect-netsuite-to-lago.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=cb7d3dfdd209f8a8f79017d24ed9e0be 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=68d65bfd478e50f1aba9f0361b3b491b 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=47812b46f83278765d174aa15c546c9f 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=72c012d4b32549f4eb040592e7f25f17 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6f033566615a0fbe2f310024c5fc12b7 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/connect-netsuite-to-lago.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6c4a8aca124a847877ce51ab71a1fe48 2500w" />
</Frame>

## Mapping items between Lago and NetSuite

**Mapping between Lago and NetSuite is done by Lago Entity → NetSuite Subsidiary**. You can define a
default mapping that applies across all subsidiaries, but a single item (including tax items)
can be mapped differently for each subsidiary. When a mapping is defined for a specific Lago
entity, that entity-specific mapping overrides the default mapping for the corresponding
NetSuite subsidiary. If all your entities share the same mapping, you only need to configure
the default mapping.

Follow these steps to map items or tax items between Lago and NetSuite:

1. Navigate to the **NetSuite Integration** page in Lago;
2. Select the **Item Mapping** tab;
3. Click on the item you want to map;
4. Fill all the required fields; and
5. Save your mapping.

<Frame caption="Map items per entity and subsidiary between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=5fcd8b92b7829e8ca3af43e487d35546" data-og-width="1451" width="1451" data-og-height="837" height="837" data-path="integrations/images/netsuite-entity-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=a9cfd318cafb91595783ee17c06f66c4 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=8201428b05475caf351da9e31443960c 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=f6c235a199ffe20046b72e8625495f3e 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=038f9a865b868ebec7e63c9ac22fc6fa 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=ea887bcfbd32fb814bd4ad3925e7fc3e 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-entity-mapping.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=4b6d56466ee55a6ad328ad5a94db907c 2500w" />
</Frame>

<Info>
  The item mapping must be completed before syncing invoices, credit notes, or payments to NetSuite. Anytime a new item is created in Lago, it must be mapped to a NetSuite item to ensure successful synchronization.
</Info>

### Mapping a fallback item

The fallback item is a dummy item used as a backup in case the mapping of other objects fails.
To ensure continuous data synchronization between Lago and NetSuite, this fallback item will be used whenever there is a mapping issue.

<Info>
  This mapping follows a one-to-many structure, meaning that a single fallback item can be used to handle multiple mapping issues.
</Info>

<Frame caption="Map a fallback item between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4d8243bb7a7f9335799d6245f83649ff" data-og-width="2384" width="2384" data-og-height="752" height="752" data-path="integrations/images/netsuite-fallback-item.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1246955d7d6bd78588a870d9350d2251 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=709c95d07c3ed7735df29187606488c4 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=af08879aff174e2674c82e271cd58814 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=ceca0638545d0931b0580505667f2946 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=a3aab40a5f5d91522066bdf96cc97816 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/netsuite-fallback-item.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1276454acedef57a900019af71c26757 2500w" />
</Frame>

### Mapping a tax item

To override the tax amount for an invoice, sales order, or credit note, you need to map a single tax item from NetSuite.
This mapped item will be used to assign the correct tax amount.

**To ensure taxes are sent from Lago to NetSuite, complete the tax mapping** for the following [tax fields you created here](#create-lago-tax-nexus-type-and-code):

1. Tax Nexus;
2. Tax Type; and
3. Tax Code.

Use the `id` for each item, found either in the UI or in the URL of the specific item. You can define a specific tax mapping for each Lago entity or NetSuite Subsidiary.

<Info>
  This mapping follows a one-to-many structure, meaning that a single tax item can be mapped to override all tax amounts issued by Lago.
</Info>

<Frame caption="Map a tax item between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=b2c9e1b898589ab0c3a57007494eddde" data-og-width="1438" width="1438" data-og-height="978" height="978" data-path="integrations/images/mapping-tax-item-netsuite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=e20b69e45fac6cd566242def41f5b4f9 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=690c4fc3250a5a91ce44f40db203e84c 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=0cbde9be85b191e2b5914960f57fa880 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=b8afce8238b862617c5e5f425e23c95d 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=b1d71b304e57ee02273619cfb4722aac 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-tax-item-netsuite.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=548340b76caf34c83cf602fda3fb03f0 2500w" />
</Frame>

### Mapping default objects

Coupons, credit notes, subscription fees, minimum commitments, and prepaid credits require a one-to-many mapping.
Each of these objects must be mapped to a single default item from your NetSuite instance. Lago will use this mapped item
whenever any of these objects appear on the final invoice sent to NetSuite. You can override the default mapping for each Lago entity or NetSuite Subsidiary if needed.

<Info>
  This mapping follows a one-to-many structure, meaning a single item can handle multiple mappings for coupons, credit notes, subscription fees, minimum commitments, and prepaid credits.
</Info>

<Frame caption="Map default items between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=d61fe929ecb657d575cd727aaa9e75ca" data-og-width="1458" width="1458" data-og-height="981" height="981" data-path="integrations/images/mapping-default-items-netsuite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=3f73d6b5b11289d9e6185e0eccdbeaa6 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=e818162ffecaf65388db752e3df9a859 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=769949f2549f74c97a740e159145064a 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=fbdcf0c2f5780c43a5ae014b5150e97f 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=2b0e3349a3f4312bdedf46e41b43788b 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-default-items-netsuite.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=40091a94f419426f5a3223c58acb7850 2500w" />
</Frame>

### Mapping custom objects

Billable metrics and add-ons require a one-to-one mapping. Each billable metric, used for usage-based billing, must represent a specific SKU in your NetSuite instance.
You need to map each of these individually. Lago will use the mapped items whenever any of these metrics or add-ons appear on the final invoice sent to NetSuite.
You can override the default mapping for each Lago entity or NetSuite Subsidiary if needed.

<Info>
  This mapping follows a one-to-one structure, meaning each billable metric or add-on must be mapped to a specific NetSuite item.
</Info>

<Frame caption="Map custom items between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=e16372bfc57049e757d73ee551585332" data-og-width="1416" width="1416" data-og-height="906" height="906" data-path="integrations/images/mapping-custom-items-netsuite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=6c60b25017c560ac7e9445ecd0408c56 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=1143165facffa85a1cd87a46100e87c0 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=b38479bd657f494845c0bada74d9f800 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=a3fbe15ddd2d60289b927a6a91381318 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=ff485d25a6a8acf49d8c1f5b3bfd71e0 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/mapping-custom-items-netsuite.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=cc2a734ebfcebd0fc9c2326d2bb514c8 2500w" />
</Frame>

## Mapping currencies between Lago and NetSuite

As NetSuite supports multiple currencies for a single customer, it's essential to map the currencies used in Lago to those in NetSuite.
This ensures that all financial data is accurately represented and synchronized between the two systems. To map currencies, follow these steps:

1. Navigate to the **NetSuite Integration** page in Lago;
2. Select the **Currency Mapping** tab;
3. Click the **Add Currency mapping** button; and
4. Map the Lago currency code with the currency ID used in NetSuite.

<Frame caption="Map currencies between Lago and NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=1231174d97ea078c22137b8469400d05" data-og-width="1442" width="1442" data-og-height="968" height="968" data-path="integrations/images/netsuite-currency-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=e7e24f91d5d2884d754aa501bbde743d 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=4deabff55563fe0f91019f6aeca4527f 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=8cdb3daf0811985d4ce85077a34d766b 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=6ab6e8cd8149dc56913683eeefc09a3d 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=684312d02ac0a2408ee45c2670da7aa7 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/netsuite-currency-mapping.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=9b5808b7c3fa194f082e301dbaa46dd2 2500w" />
</Frame>

## Customers synchronization

When creating or updating a Lago customer, you can choose to link it to a NetSuite customer.

The first option is to **automatically create a new customer from Lago to NetSuite**. Follow these steps:

1. Create or update a new Lago customer;
2. Select the targeted NetSuite connection;
3. Check the box labeled 'Create this customer automatically in NetSuite';
4. Choose a NetSuite subsidiary from the list (Lago will fetch the list of subsidiaries from your NetSuite instance); and
5. Save and create this new customer.

If the customer is successfully created in NetSuite, a new field will be displayed in the Lago customer view, providing a direct link to the corresponding NetSuite customer.

<Info>
  Customer creation from Lago to NetSuite happens in real-time with only a few seconds of delay.
</Info>

<Frame caption="Lago customer integrated with NetSuite">
  <img src="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=fa84f22cdf6785724db0610dc16dd730" data-og-width="1701" width="1701" data-og-height="799" height="799" data-path="integrations/images/sync-customers-netsuite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=280&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=82c0239a56e426cfad7ce3e610dbee1d 280w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=560&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=b7bc25377cbb748f46a0bf8069c5273f 560w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=840&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=cf3510eca624a8247c91e629a9684b90 840w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=1100&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=324d7a7aa76d00384f4c7760d5719767 1100w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=1650&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=a2106e03bc5e5a4aa22ef511e981d694 1650w, https://mintcdn.com/lago-docs/L98tGNZj-YiXbIo-/integrations/images/sync-customers-netsuite.png?w=2500&fit=max&auto=format&n=L98tGNZj-YiXbIo-&q=85&s=4beafd2eb65f94a60a80eb26d5f25116 2500w" />
</Frame>

The second option is to **import an existing NetSuite customer to a Lago customer**. Follow these steps:

1. Create or update a Lago customer;
2. Select the targeted NetSuite connection;
3. Ensure the box labeled 'Create this customer automatically in NetSuite' is unchecked;
4. Paste the NetSuite customer ID in the appropriate field; and
5. Save and create this new customer.

## Invoices synchronization

If a Lago customer is linked to a NetSuite customer, Lago syncs invoices to NetSuite Invoices in real-time.

It's important to note the following:

* Each fee issued by Lago is synced as a line item on a NetSuite invoice;
* The Lago fee `units` are synced to NetSuite as `quantity`;
* The Lago fee `precise_unit_amount` is synced to NetSuite as `rate`;
* Lago overrides the total tax amount of a NetSuite invoice using the tax item, as NetSuite does not support tax details at the line item level; and
* Any discounts on an invoice (coupon, credit note, or prepaid credits) are synced as negative line items on the NetSuite invoice.

If the invoice is successfully created in NetSuite, a new field will be displayed in the Lago invoice view, providing a direct link to the corresponding NetSuite invoice.

<Info>
  Invoice creation from Lago to NetSuite happens in real-time with only a few seconds of delay.
</Info>

<Frame caption="Sync Lago invoices to NetSuite">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=138ffe3d14f171fe12c32b929be37e5b" data-og-width="2832" width="2832" data-og-height="1890" height="1890" data-path="integrations/images/sync-invoices-netsuite.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=ba3171839997f090b736f8791360325c 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4c88c9a1f427ef3db994faff3ff3a1fe 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5c9704f9605cbd526dbd7888f11a3552 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=8ecaaa6f005976320b5b550e8e719dd5 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e5f93f6364d4f30105e6cf6162e17c36 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-invoices-netsuite.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=9f7270edc88dae99849d1b98160ccafd 2500w" />
</Frame>

## Credit Notes synchronization

If a Lago customer is linked to a NetSuite customer, Lago syncs credit notes to NetSuite Credit Memos in real-time.

It's important to note the following:

* Each fee refunded by Lago is synced as a line item on a NetSuite Credit Memo;
* Lago overrides the total tax amount of a NetSuite credit memo using the tax item, as NetSuite does not support tax details at the line item level; and
* Any discounts on an credit note (like coupon, for instance) are synced as line items on the NetSuite Credit Memo.

If the credit note is successfully created in NetSuite, a new field will be displayed in the Lago credit note view, providing a direct link to the corresponding NetSuite Credit Memo.

<Info>
  Credit note creation from Lago to NetSuite happens in real-time with only a few seconds of delay.
</Info>

## Payments synchronization

If a Lago invoice is tied to a NetSuite invoice, Lago automatically syncs payments occurring in Lago to NetSuite, updating in-real time the payment status of the invoice in NetSuite.
You can also retrieve payments for invoices paid directly in NetSuite.

## Integration logs

Whenever an issue occurs in NetSuite, Lago will notify you through a [webhook message](/api-reference/webhooks/messages#accounting-provider-error) called `customer.accounting_provider_error`.
You can also **view integration logs inside NetSuite** for troubleshooting and auditing purposes.
