# Source: https://getlago.com/docs/integrations/crm/salesforce-crm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Salesforce CRM

> Lago syncs billing data to Salesforce in real-time.

<Info>
  **PREMIUM ADD-ON** ✨

  This integration is only available to users with a specific paying add-on. Please
  **[contact us](mailto:hello@getlago.com)** to get access to Salesforce CRM integration.
</Info>

## Object mapping

<Frame caption="Lago to Salesforce object mapping">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=327cb949a5c44c2e85701e06dbc790e6" data-og-width="4852" width="4852" data-og-height="4802" height="4802" data-path="integrations/images/lago-salesforce-object-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2f37cb43a2263743b00f0ec41450861e 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=7952a75790aabca7bd6e06655425f749 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=00e766ae3bda706245dee5ffa2225b31 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c9f2523916cb5f4244aa09816a1e0784 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c7f1be66a5392a3936d4824de5b338ec 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/lago-salesforce-object-mapping.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=dd0a996e71ffed58598364150782a518 2500w" />
</Frame>

## I. Integration configuration

### Create integration for Salesforce on Lago Side

To gain premium access to our Salesforce Package application, please don't hesitate to contact us. Login to Lago as admin user, navigate to Settings > Integrations > *Salesforce* (allowed only if team has enabled it for your account), and click "Create new". Enter the following details:

* Name
* Code
* Salesforce Instance (URL of your Salesforce instance)

<Frame caption="Create new Salesforce integration in Lago">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8e702f7cc2e5996e8ad72a9d1029c77e" data-og-width="525" width="525" data-og-height="400" height="400" data-path="integrations/data/images/create-salesforce-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=2e09b01c5fe05c52ffcdd4e57a2ed085 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e053dedb0adb28acd1c6bc637c6d7c2e 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=287b12f2c322ac12a46cef8baf47ca1f 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=3a6bafbcc24b161716c4874cf7e42eb1 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d360a10147ffd6a8b306dfda3f7e093a 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/create-salesforce-integration.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=06ede403d3d46b3430fbd2e6e84bd0ed 2500w" />
</Frame>

Make note of the integration code as shown in the connection details - you'll need this later:

<Frame caption="Salesforce integration connection details">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1248d6de1e17b52e1166b6612870321e" data-og-width="649" width="649" data-og-height="433" height="433" data-path="integrations/data/images/salesforce-integration-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9c85646394fca314384fa769697aa0a2 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=bd1aa6d0b94eaa219d2babc42a6602bf 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=00385971c3c661228ddf80e2c51516cc 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1544b6beba50ff5200669ece20cb45ff 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=499b7f1710e69e04cd44dc115d515d81 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-integration-details.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=81a04e985bcaa24c7e13d7f26d5b69de 2500w" />
</Frame>

### Install Salesforce CRM Package

You can initiate the installation process **by clicking on the provided link**, which will direct you to the installation
page where you can follow step-by-step instructions for a seamless integration. If you have any questions or need assistance
during the installation, our dedicated support team is here to help you every step of the way.

<Frame caption="Install Lago Salesforce App package">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4579cd3c2b53cc46bdeac3edf344bc9c" data-og-width="2598" width="2598" data-og-height="1492" height="1492" data-path="integrations/data/images/lago-install-salesforce-package.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e9b7a9f25c532adbe2de24f582d42946 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=4a534dd654157a342d6acd121e5a3da2 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1e5b0a2ae64c1b234db845f439a39672 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=fd78656bd44b2d425a1cb6fb3aeb908f 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=03f6c766006092d31c5730c0c789d65e 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-install-salesforce-package.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=a3b3352450d92d65579c929797c92606 2500w" />
</Frame>

To ensure a successful installation, please follow these steps:

1. We recommend selecting the **"Install for all users"** option;
2. Click on the **"Install" button**;
3. Make sure to **check the box to grant access to these third-party websites**; and
4. Once completed, you'll have **successfully installed** the Lago Salesforce App.

<Info>
  Please note that the installation process may take a few minutes to complete.
  However, rest assured that you will receive an email confirmation once the installation is finished.
</Info>

### Webhook config: sync real-time data

After installation in Salesforce CRM, set up a webhook URL in Salesforce to receive real-time data from Lago.
This involves **configuring a new "Site" in Salesforce's setup section**.
Note that the four main actions described below should be performed by a Salesforce Admin and is only required during the initial setup.

<Steps titleSize="h3">
  <Step title="Access the Site section in Salesforce" titleSize="h3">
    1. Click the gear icon in the upper right to access **Salesforce Setup**;
    2. Search and navigate to the Sites section; and
    3. Create a new Site (see picture below).

    <Frame caption="Create a new Site in Salesforce">
      <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ed85aeb0165c9c1b4ece92ce0451d8ea" data-og-width="3008" width="3008" data-og-height="1872" height="1872" data-path="integrations/data/images/create-new-site-salesforce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=8676dd7ea03d17760a758ebdb0d91a1d 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6f325eaed1c6e38512547afe535ac0fb 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=6cfa13d18a2d5379af804516d53b40ee 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=9b19d0717cefdbd618444cc2ae7fa1ae 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=00b45d190cd6b1050864ace2c66fb9dd 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/create-new-site-salesforce.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=57c6248853b0b6b92d504b42b6bb0348 2500w" />
    </Frame>
  </Step>

  <Step title="Create a new Site in Salesforce" titleSize="h3">
    When creating a new site, follow these steps:

    1. Set a unique **Site Label**;
    2. Specify a unique **Site Name**;
    3. Optionally, add a **Site Description**;
    4. Ensure the **Site Contact** and **Default Record Owner** are filled;
    5. Set the **Default Web Address** prefix to `getPushNotification`;
    6. Choose `SiteLogin` as the **Active Site Home Page**; and
    7. Don't forget to **save the new site**: and
    8. **Activate the newly created site** by going to the Site Details and clicking the `Activate` button.

    <Frame caption="New site creation flow in Salesforce">
      <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e7c06d136a9a177ebe38ee8fcc739f4f" data-og-width="3002" width="3002" data-og-height="1864" height="1864" data-path="integrations/data/images/new-site-creation-flow-salesforce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0c0d62582d2cf567dd961709beeca44a 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d35a590f4a0105fbb2e795a843b0d297 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5b6f8633bebef177cc43db96b70bdf1d 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ff38b2a620f834d8deccecfbb5fe25bf 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=58b9b80e4a78fd486e5d985fba3adac5 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/new-site-creation-flow-salesforce.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8690b321201acfd88bf3be3467dc8dce 2500w" />
    </Frame>
  </Step>

  <Step title="Edit Public Access Settings in Salesforce" titleSize="h3">
    To edit Public Access Settings for your new Site:

    1. Visit the site and click **Public Access Settings**;
    2. In the **Enabled Apex Class Access** section, click "edit";
    3. Add `LagoWebHookSubscriptionController` to **Enabled Apex Classes**; and
    4. Save your changes.

    <Frame caption="Edit Salesforce's site Public Access Settings">
      <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5def29ad6c6b60a05f4f28ef3fb8f608" data-og-width="3008" width="3008" data-og-height="1238" height="1238" data-path="integrations/data/images/edit-public-access-settings-salesforce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7faf3c8e1fd125ee51e30810d2a0eac8 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f16f3d90b7880e74a19cbdb588408f2c 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9ff5f452c2ed432973d4f38cca1c6811 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5023ba90bdb460da2adc3c29342bcc6a 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=78d76f800b1bfbddfe6ee8cf8019a7db 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/edit-public-access-settings-salesforce.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c8841e4681746ddde3af087321609f3c 2500w" />
    </Frame>
  </Step>

  <Step title="Paste the Webhook URL into Your Lago App" titleSize="h3">
    To set up the webhook URL for real-time data syncing between Lago and Salesforce, follow these steps:

    1. Return to your newly created site;
    2. Locate the **Custom URLs** section;
    3. Copy the **domain name** *(e.g., lago.my.salesforce-sites.com)*;
    4. Add the `https://` prefix to this domain name (e.g., `https://lago.my.salesforce-sites.com`); and
    5. Append `/services/apexrest/lago/api/Webhooks/incoming/pushDetails/` to the domain name (e.g., `https://lago.my.salesforce-sites.com/services/apexrest/lago/api/Webhooks/incoming/pushDetails/`).

    <Frame caption="Find Salesforce's site domain name">
      <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=5364ebdf4baaf2644c4be193a1e71bdb" data-og-width="2992" width="2992" data-og-height="862" height="862" data-path="integrations/data/images/find-domain-url-salesforce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=240b5d79b3d55b8498542a22bc17f6dc 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c89c2c3cb5ddc12054588f1565072aaa 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9d9d11317c1c1ff795cec9b546698ef0 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8ab7aca54676c85fec819b5e40667e3b 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8f00d6a83f8e4248001b9d79753cc518 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/find-domain-url-salesforce.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=f34b3d82704bf0e51b5db7e023a8b8e0 2500w" />
    </Frame>

    Now, go to your Lago app and past this webhook into the webhook’s settings:

    1. Within Lago, navigate to **Developers**;
    2. Visit the **Webhooks** tab;
    3. Choose `HMAC` as the **mandatory signature type**;
    4. Paste your Salesforce webhook URL; and
    5. Save this webhook endpoint.

    Congratulations! You're ready to sync real-time data from Lago to Salesforce! 🎉

    <Frame caption="Paste Salesforce webhook URL to Lago">
      <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/integrations/data/images/add-salesforce-webhook-url.gif?s=888f1af4a3801f7a412f21ec98ad699e" data-og-width="1160" width="1160" data-og-height="720" height="720" data-path="integrations/data/images/add-salesforce-webhook-url.gif" data-optimize="true" data-opv="3" />
    </Frame>
  </Step>
</Steps>

### Establish and finalize connection

<Frame caption="Connect your Lago instance to Salesforce Lago App">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-package-api-connection.gif?s=9de33c424d0b97a67ff2ab25db668404" data-og-width="800" width="800" data-og-height="604" height="604" data-path="integrations/data/images/salesforce-package-api-connection.gif" data-optimize="true" data-opv="3" />
</Frame>

**Option 1: Configure a standard API Base URL**
To establish a connection between your Lago instance and the Salesforce Package, follow these steps:

1. Access Salesforce and locate the **App Launcher**;
2. Find and open the Lago app you recently installed;
3. Within the Lago Base Configuration tab:

* Provide your **Lago API Key** (located in Lago's Developer Section)
* Enter your Lago **API base URL**. Do not insert the `api/v1` at the end of the URL. By default, the valid URL is `https://api.getlago.com/`.
  If you want to change the API base URL to another one (e.g., `https://api.eu.getlago.com/` or a custom self-hosted one), please follow option 2.
* Enter lago app URL (**Front End Base URL**). By default, the valid URL is `https://app.getlago.com/` (it will be different for self-hosted).
* Enter Lago Integration code from Step 1 [`Salesforce integration on Lago`](/integrations/crm/salesforce-crm#create-integration-for-salesforce-on-lago-side)

4. **"Save and validate"** your connection; and

* If the **Lago API Key** is valid then only **Start Data Sync** button will be enabled.

5. Click the **"Start Data Sync"** to finalize the connection between Lago and Salesforce.

<Warning>
  Please note that data synchronization is available only for Lago customers with an `external_salesforce_id` and an existing Salesforce Account.
</Warning>

**Option 2: Configure a custom API Base URL**
If you use your own Lago API base URL (self-hosting) or one for a different server instance,
you can customize it directly in Salesforce:

1. Navigate to Salesforce's Setup;
2. Search for and select Remote Site Settings;
3. Find and access the remote site for the Lago App;
4. Click the Edit button to modify the remote site's details;
5. Update the Remote Site URL with your preferred URL; and
6. Save the changes.

## II. Sync data from Lago to Salesforce

If your webhook endpoint is configured correctly, your *customer, subbscription, and billing data will flow seamlessly in real-time*\*.

<Info>
  Please note that from all the version above Salesforce for Lago v2.7 - Customer, Subscriptions, and Invoices will be created in Salesforce via webhooks seamlessly
</Info>

### Sync customers to Salesforce (> v2.7)

<Info>
  For organizations with existing Lago customers that need to be synchronized with Salesforce, our support team provides specialized assistance with the migration process. Please contact our team to initiate this synchronization.
</Info>

To establish a new customer connection between Lago and Salesforce, follow these steps:

1. Navigate to the customer creation screen in Lago
2. Complete the standard customer information fields
3. Expand the 'Connect to external apps' section at the bottom of the form
4. Select Salesforce and choose the integration established during the initial setup
5. Choose the appropriate synchronization method:

* For new Salesforce customers: Enable the Create automatically this customer option
* For existing Salesforce customers: Enter the corresponding 'Salesforce Account ID'

<Frame caption="Customer external apps connection interface">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-connect-customer-external-apps.gif?s=f499f9c7db6efe8dee116d45b877a743" data-og-width="800" width="800" data-og-height="413" height="413" data-path="integrations/data/images/lago-connect-customer-external-apps.gif" data-optimize="true" data-opv="3" />
</Frame>

<Info>
  The system handles account creation in Salesforce based on your configuration:

  For Salesforce instances with Person Accounts enabled:

  When `Customer Type` is set to \`Individual1: Creates a Person Record type account.

  When `Customer Type` is `Company` or unspecified: Creates a standard company account using the default record type for the running user

  For Salesforce instances without Person Accounts:
  Creates all accounts using the default record type associated with the running user
</Info>

<Warning>
  Important considerations for customer record management:

  Synchronized customer records have specific update restrictions in Salesforce to maintain data integrity

  When using the Lago Integration Code (available for >= v2.7):

  The system sets `sync_with_provider` to `true`.
  This setting allows future updates from lago in Salesforce.

  Without the Lago Integration Code (for \< v2.7):

  We don't keep the data in sync from lago to Salesforce. Only initial sync is avaialble from lago to Salesforce, check below section.
</Warning>

### Sync customers to Salesforce (\< v2.7)

To synchronize Lago Customer data with Salesforce Accounts (native object), ensure that your
Salesforce Account is created first, and that the Lago Customer's `external_salesforce_id` is explicitly populated.

1. Begin by creating a new Account in Salesforce or accessing an existing one;
2. Next, create a customer in Lago and populate the `external_salesforce_id` field for a Lago Customer with the Salesforce Account Id; and
3. Finally, your Salesforce Account and Lago Customer are synchronized!

<Warning>
  Billing data will not sync unless these requirements are met.
  Lago does not create Salesforce Accounts.
  Before syncing billing data, you need to create or retrieve an existing Account in Salesforce
  and populate the Lago customer field called `external_salesforce_id`.
</Warning>

<Frame caption="Salesforce Account with Lago Customer information">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=2439df2c180d15b38aeffacc408c8e2b" data-og-width="2540" width="2540" data-og-height="574" height="574" data-path="integrations/data/images/lago-synced-account-salesforce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=ddbaaa4516d82d0f55757891bca2c6a8 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=eaa6d65c60d646efde76df27a954bb8c 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=752cfd5e521462aadb5e2db01faaca36 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=467cfab76f992cbda8f0a7f4b4108be1 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b648538ec9231f5c01f7621e33e5b5bc 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-synced-account-salesforce.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8d8134729ced1b2c26f1cc93f69df011 2500w" />
</Frame>

### Sync subscriptions to Salesforce

<Frame caption="Sync subscriptions data from Lago to Salesforce">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/sync-lago-subscriptions-salesforce.gif?s=a7a0b5a4cad68070a1cfe9ec0ec1d460" data-og-width="1156" width="1156" data-og-height="720" height="720" data-path="integrations/data/images/sync-lago-subscriptions-salesforce.gif" data-optimize="true" data-opv="3" />
</Frame>

Whenever a subscription is created for a Lago Customer, the subscription details will be automatically
synced in real-time with Salesforce using the `Lago Subscriptions` custom object.

Here is a list of Subscription fields that are automatically synced.
Note that this subcription is automatically linked to a Salesforce Account:

* Subscription Id;
* Subscription Name;
* Subscription Start Date;
* Subscription Status;
* Subscription Termination Date (synced when the subscription is terminated);
* Subscription Billing Time (either `calendar` or `anniversary`); and
* Plan Code.

### Sync invoices to Salesforce

<Frame caption="Sync invoices data from Lago to Salesforce">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/sync-lago-invoices-salesforce.gif?s=de599a22f7cc52e645b4e3c39e3008ad" data-og-width="1152" width="1152" data-og-height="720" height="720" data-path="integrations/data/images/sync-lago-invoices-salesforce.gif" data-optimize="true" data-opv="3" />
</Frame>

Whenever an invoice is issued for a Lago Customer, the invoice details will be automatically
synced in real-time with Salesforce using the `Lago Invoices` custom object.

Here is a list of Subscription fields that are automatically synced:

* Invoices Number;
* Invoice Payment Status;
* Invoice Type (`subscription` or `one-off`);
* Invoice Issuing Date;
* Invoice Amount;
* Invoice File Url; and
* Invoice Currency.

### Sync credit notes to Salesforce

Whenever a credit note is issued for a Lago Invoice, the credit note details will be automatically
synced in real-time with Salesforce using the `Lago CreditNotes` custom object.

### Sync Plans, Add-Ons, Coupons to Salesforce

Plans and Add-ons are synced to Salesforce when we initially click on **Start Data Sync** from Lago Base Configuration page.

* Plans are synced to `Lago Plans` object and `Product2` standard object. We also create a *price book entry* for all the products in `Standard Price Book` price book
* Add-Ons are synced to `Lago Add-Ons` object and `Product2` standard object. We also create a *price book entry* for all the products in `Standard Price Book` price book.

### Sync coupons and applied coupons to Salesforce

Coupons and Applied coupons are synced to Salesforce when we click on **Start Data Sync** from Lago Base Configuration page.

* Coupons are synced to `Lago Coupons` custom object. All the existing coupons will be available in Salesforce. Please note: we cannot create coupons from Salesforce to Lago, we must create coupons in Lago.
* Applied coupons are synced to `Lago Applied Coupon` custom object.

### Schedule Sync from Lago To Salesforce

We also provide option to schedule the data sync from Lago to Salesforce.

* `LagoSyncScheduleable` -- a schedulable class which helps us schedule either all the data or any one of them.
* To schedule the sync of any *ONE* of the object:
  * Create a new instance of class by passing any one of the following string: `CUSTOMER`, `SUBSCRIPTION`, `PLAN`, `ADDON`, `INVOICE`, `CREDITNOTE`
    * Ex: To sync Plans from lago to Salesforce everyday at 1PM, execute below anonymous code in Anonymous window in Developer Console. ([click here to learn more about CRON expression](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_scheduler.htm))
      ```
      //Create a new instance. Pass 'PLAN' in brackets.
      lago.LagoSyncScheduleable syncPlan = new lago.LagoSyncScheduleable('PLAN');
      //CRON expression to schedule a job everyday at 1 PM
      String schedule_cron = '0 0 13 * * ?';
      //schedule(name, cron_expression, class_instance)
      System.schedule('Sync Lago Plan', schedule_cron, syncPlan);
      ```
* To schedule the sync of  *ALL* the objects:
  * create a new instance of class by passing `true`
    * Ex: To sync **all** objects from lago to Salesforce everyday at 1PM, execute below anonymous code in Anonymous window in Developer Console. ([click here to learn more about CRON expression](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_scheduler.htm))
      ```
      //Create a new instance. Pass true in brackets.
      lago.LagoSyncScheduleable syncAll = new lago.LagoSyncScheduleable(true);
      //CRON expression to schedule a job everyday at 1 PM
      String schedule_cron = '0 0 13 * * ?';
      //schedule(name, cron_expression, class_instance)
      System.schedule('Sync Lago all', schedule_cron, syncAll);
      ```

## III. Actions from Salesforce to Lago

Beyond just syncing data from Lago to Salesforce, you can also initiate actions in Lago directly from Salesforce.
You can leverage Salesforce `Flows` to execute actions in Lago. Lago provides several customizable templates for creating customers from Salesforce Accounts, directly assigning subscriptions to customers from Salesforce, creating one-off invoice from salesforce.

### Create customers

#### Flow: `Lago Template - Create Customer in Lago on Account Create`

<Frame caption="Use Lago template to create a customer on Account creation">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=31f79ddbba7b2156ed8face59c260c6e" data-og-width="2964" width="2964" data-og-height="1242" height="1242" data-path="integrations/images/lago-salesforce-flows-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6e8a91db3f3c4331ed066d237debad17 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=6911e1262c0c6b4c51831716a18346a5 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=81d6d17475c76860435a01bb3d30c77d 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=bf738ec447f298b8cd8ee8f49d434813 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1406aaf00e1ff4974e38033677ab958e 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/lago-salesforce-flows-template.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=510f8448d5416397d40888fa262b8e93 2500w" />
</Frame>

To create a customer in Lago upon the creation of a Salesforce Account, utilize the Flow template provided by Lago.

1. Log into your Salesforce instance;
2. Access the Setup section via the settings wheel icon in Salesforce;
3. Find and select `Flows` under Process Automation in the sidebar;
4. Locate and open the `Lago Template - Create Customer in Lago on Account Create`;
5. Click 'Save As' to create and save your own version of the template; and
6. Do not forget to click the `Activate` button to activate your flow.

You have the **flexibility to modify various aspects of this flow, including the trigger conditions and field mappings**.
By default, the action is initiated when a Lago ID is absent. Additionally, you can customize how fields are mapped from your Salesforce instance to Lago. You can also configure `customer type` to 'Individual' or 'Company' which creating customer from Salesforce to Lago.

<Frame caption="Customize the flow">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/images/account-customer-flow.gif?s=4da6d2e6a0f887365090a88acfec4ad5" data-og-width="928" width="928" data-og-height="588" height="588" data-path="integrations/images/account-customer-flow.gif" data-optimize="true" data-opv="3" />
</Frame>

### Create subscriptions (automation)

Assigning a plan to a customer, adjusting negotiated prices, and initiating the subscription upon winning an opportunity represents a key action from Salesforce to Lago.
This enables sales teams to remain within Salesforce, their primary tool, and activate billing processes directly, without the need to switch platforms.

To assign a subscription and set prices in Lago directly from Salesforce, use the provided two flows via following Lago Flow templates.

#### Flow 1: `Lago Template - Create Lago SObject Records`

This Flow is used to create intermediate records in Lago Objects - `Lago Subscription`

1. Log into your Salesforce instance;
2. Access the Setup section via the settings gear icon in Salesforce;
3. Find and select `Flows` under Process Automation in the sidebar;
4. Locate and open the `Lago Template - Create Lago SObject Records`;
5. Click 'Save As' to create and save your own version of the template; and
6. Do not forget to click the `Activate` button to activate your flow.

<Steps>
  <Step title="Validate the flow">
    The default setting triggers plan assignment when a Salesforce Account links to a Lago customer and the **opportunity status changes to closed-won**.
    You can customize this flow to suit your specific needs. Moreover, you have the option to adjust the subscription fields and subscription charges fields being synchronized from Salesforce to Lago.

    <Frame caption="Customize the flow">
      <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/images/sync-subscriptions-salesforce-lago-flow.gif?s=286cb904c546a3656d93d2bafa7cbaaa" data-og-width="1491" width="1491" data-og-height="837" height="837" data-path="integrations/images/sync-subscriptions-salesforce-lago-flow.gif" data-optimize="true" data-opv="3" />
    </Frame>
  </Step>

  <Step title="Assign subscription and override prices">
    1. Create an opportunity by assigning an expected closed date and a stage;
    2. Add a Lago plan to this opportunity **as a product** (Salesforce will automatically retrieve all plans from Lago in `Standard Price Book`);
    3. Specify `1` for the quantity of the plan;
    4. Use the custom UI to either assign this plan directly or to override prices; and
    5. Click on 'Lago Override Plan' to finalize the subscription assignment.

    <Info>
      By default, the lago subscription record in salesforce is created when the opportunity is `closed-won`. You can assign multiple subscriptions for the same opportunity.
    </Info>
  </Step>
</Steps>

#### Flow 2: `Lago Template - Create Subscription in Lago on Subscription Creation/Update`

This Flow is used to create subscriptions in Lago from Salesforce

1. Log into your Salesforce instance;
2. Access the Setup section via the settings gear icon in Salesforce;
3. Find and select `Flows` under Process Automation in the sidebar;
4. Locate and open the `Lago Template - Create Subscription in Lago on Subscription Creation/Update`;
5. Click 'Save As' to create and save your own version of the template; and
6. Do not forget to click the `Activate` button to activate your flow.

The default setting triggers plan assignment when `SyncToLago` checkbox is checked. You can customize this flow to suit your specific needs.

### Create subscriptions (lago native UI)

We also have option to create subscriptions in Lago directly from Salesforce using Lago's create subscription screen.

1. Log into your Salesforce instance;
2. Access the setup section via the settings gear icon in Salesforce;
3. Go to Object manager and find and open account object;
4. Go to page layout (or Lightning record page) depending on what you are using, and open the page layout in which you'd like to add the button to create subscription.
5. Add the button `Lago Subscription`
6. Save the page layout or lightning record page.

Open any account which has `lago_id` populated. Click on `Lago Subscription` button; it will pop-up Lago Screen (make sure you've entered correct `Front End URL` in Lago Base Configuration page); enter correct username and password. Save. A new subscription will be directly created in Lago. And, if Webhooks are configured correctly, it will also create `Lago Subscription` record in Salesforce.

<Frame caption="Lago Subscription from SF (iframe)">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-lago-subscription-iframe.gif?s=637fd778740bf70ce9ca57cfd02427a3" data-og-width="1491" width="1491" data-og-height="837" height="837" data-path="integrations/data/images/salesforce-lago-subscription-iframe.gif" data-optimize="true" data-opv="3" />
</Frame>

<Info>
  We can add a new button ***Lago Subscription*** on *Account* page or *Opportunity* page
  A new Lago Subscription record will be created via webhooks (if configured).
  And after 1 minute another callout will be made to sync Charges.
</Info>

### Terminate Subscription

We can terminate the subscription from Salesforce to lago only if the subscription is already synced to lago(status is *active* or *pending*).

Go to Lago Subscription record in Salesforce, and check `Terminate Subscription` checkbox.

<Info>
  As soon as `Terminate Subscription` is checked it will terminate the subscription in Lago. It is handled from the backend via trigger.
</Info>

### Create one-off invoice

This enables sales team to create one-off invoice in lago from Salesforce.
Right from the opportunity record we add products which are related to `Lago Add-ons`, specify the quantity, description and amount.

To create one-off invoice and set prices in Lago directly from Salesforce, use the provided two flows via following Lago Flow templates.

#### Flow 1: [`Lago Template - Create Lago SObject Records`](/integrations/crm/salesforce-crm#flow-1-lago-template-create-lago-sobject-records)

The same flow as we created above to create subscription - is also used to create intermediate records in Lago Objects - `Lago Invoice`

#### Flow 2: `Lago Template - Generate Invoice in Lago On Lago Invoice Field Update`

This Flow is used to create one-off invoice in Lago from Salesforce

1. Log into your Salesforce instance;
2. Access the Setup section via the settings gear icon in Salesforce;
3. Find and select `Flows` under Process Automation in the sidebar;
4. Locate and open the `Lago Template - Generate Invoice in Lago On Lago Invoice Field Update`;
5. Click 'Save As' to create and save your own version of the template; and
6. Do not forget to click the `Activate` button to activate your flow.

The default setting triggers create invoice when `SyncToLago` checkbox is checked. You can customize this flow to suit your specific needs.

### Create one-off invoice (lago native UI)

We also have option to create one off invoice in Lago directly from Salesforce using Lago's create invoice screen.

1. Log into your Salesforce instance;
2. Access the setup section via the settings gear icon in Salesforce;
3. Go to Object manager and find and open Account object or Opportunity;
4. Go to page layout (or Lightning record page) depending on what you are using, and open the page layout in which you'd like to add the button to create Invoice.
5. Add the button `Lago Invoice`
6. Save the page layout or lightning record page.

Open any account which has `lago_id` populated. Click on `Lago Invoice` button; it will pop-up Lago Screen (make sure you've entered correct `Front End URL` in Lago Base Configuration page); enter correct username and password. Save. A new Invoice will be directly created in Lago. And, if Webhooks are configured correctly, it will also create `Lago Invoice` record in Salesforce.

<Frame caption="Lago Invoice from SF (iframe)">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/salesforce-lago-invoice-iframe.gif?s=4b2df4226d4f70052063d7a9207bdf84" data-og-width="1491" width="1491" data-og-height="837" height="837" data-path="integrations/data/images/salesforce-lago-invoice-iframe.gif" data-optimize="true" data-opv="3" />
</Frame>

<Info>
  We can add a new button ***Lago Invoice*** on *Account* page or *Opportunity* page
  A new Lago Invoice record will be created via webhooks (if configured).
  After 1 minute another callout will be made to sync invoice line items (add ons).
</Info>

### Get Invoice pdf

Now we can also get invoice pdf directly directly from Salesforce.

1. Go to Lago Invoice
2. Open any Invoice which is already synced.
3. Click `Get Invoice pdf` > it will open PDF in a new tab.

### Get Invoice Line Item Details

We can fetch Invoice line items manually for any invoices if required.

1. Go to Lago Invoice tab > Open any Invoice which is already synced.
2. Click on `Lago Sync Invoice Line Item` button. If button is not present on the layout, please add it on Page layout or Lightning record page.
3. All lago items will be synced and available in `Lago Line Items` child custom object.

<Frame caption="Get Invoice line items">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/sf-get-lago-invoice-line-items.gif?s=9eacece6db807fb218ced6de8254ec94" data-og-width="800" width="800" data-og-height="507" height="507" data-path="integrations/data/images/sf-get-lago-invoice-line-items.gif" data-optimize="true" data-opv="3" />
</Frame>

### Managing Coupons in Salesforce

The Salesforce integration allows you to manage customer coupons directly from your Salesforce interface. This section explains how to apply new coupons to customer accounts and manage existing coupons effectively.

#### Applying Coupons to Accounts

Before you begin applying coupons, you'll need to ensure your Salesforce environment is properly configured. The "Apply Coupon" action button must be available in your account page layout or lightning record page. If you don't see this button, work with your Salesforce administrator to add it through the page layout editor or lightning app builder.
Once your environment is configured, follow these steps to apply a coupon to a customer account:

1. Navigate to the Account Details> Access the account details page for the customer who will receive the coupon.
2. Initiate Coupon Application > Click the "Apply Coupon" action button. This will open a popup dialog for coupon configuration.
3. Select and Configure the Coupon. The configuration options will vary depending on the type of coupon you're applying:

* For Fixed Amount Coupons: Enter the discount amount, select the appropriate currency, Choose the frequency for applied coupon

<Info>
  If the Lago customer currency is already set in the account, the currency field will be locked to maintain consistency.
</Info>

* For recurring frequencies, specify the duration period

* For Percentage-Based Coupons: Verify or adjust the percentage rate, set the frequency of application
  * For recurring frequencies, enter the duration period

4. Complete the Application

* Click the "Apply Coupon" button to finalize the process.
* This action will:
  * Create an Applied Coupon record in Salesforce
  * Synchronize the coupon with the customer's account in Lago
  * Enable the discount for future qualifying transactions

<Frame caption="Apply Coupon on Accoun">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/sf-apply-coupon.gif?s=e27969af7660f656158111645f9eca1d" data-og-width="800" width="800" data-og-height="614" height="614" data-path="integrations/data/images/sf-apply-coupon.gif" data-optimize="true" data-opv="3" />
</Frame>

#### Terminating Active Coupons

There may be times when you need to end a coupon's application before its natural expiration. Here's how to terminate an active coupon:

1. Access the Coupon Record. Navigate to the Applied Coupon details page for the coupon you wish to terminate.
2. Initiate Termination, locate the "Terminate Coupon" checkbox in the record.
3. Confirm Termination: Check the box to initiate the termination process. Upon saving:

* The coupon status will update from "Active" to "Terminated"
* The change will synchronize with Lago
* The customer will no longer receive the discount

<Warning>
  Remember that coupon termination is permanent. Once a coupon is terminated, it cannot be reactivated. You would need to apply a new coupon if the discount needs to be reinstated.
</Warning>

This coupon management system ensures that your sales team can efficiently handle discounts and promotional offers while maintaining synchronization between Salesforce and Lago platforms.

## Debugging & logs

To ensure seamless data synchronization between Lago and Salesforce, every action and data transfer is meticulously logged.
These logs are accessible directly through the Lago package for comprehensive debugging and analysis:

1. Navigate to 'Lago Base Configuration': This is your starting point for accessing the debugging tools. and
2. Access Logs: Click on the 'Logs' tab to view a detailed record of all activities.

You can refresh logs to keep your data current or delete unnecessary logs to maintain clarity and efficiency in the debugging process.
This approach aids in promptly identifying and resolving integration issues.
