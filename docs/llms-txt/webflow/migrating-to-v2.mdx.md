# Source: https://developers.webflow.com/data/docs/migrating-to-v2.mdx

***

title: Migrating to v2
slug: data/docs/migrating-to-v2
hidden: false
'og:title': Webflow API Docs - Migrating to API v2
--------------------------------------------------

<Warning title="Webflow API v1 is deprecated.">
  For more details about this deprecation, timeline, and its implications, please refer to the [Webflow API v1 deprecation notice](/data/docs/webflow-v1-api-deprecation-notice).
</Warning>

## v2 Apps and APIs

Webflow's new v2 Apps and APIs enhance security, efficiency, and developer experience. With [scopes](/data/reference/scopes) and an expanded [resources](/data/reference/structure-1), both developers and users gain more control and clarity over their Webflow data. Follow the sections below to migrate from v1 Apps, site tokens, webhooks, or APIs.

## Migrating to API v2 for site owners

Did you receive a notification that your site may be using v1 APIs? Read the below section for instructions on how to transition to using v2 APIs by the deprecation date.

<Accordion title="Migrating to v2 site tokens, webhooks, and v2 Apps">
  <Tabs>
    <Tab title="Site Tokens">
      <Note>
        <b>Action Item:</b> Create a new v2 site token.

        <ul>
          <li>
            <b>Site tokens with third-party integrations</b>

             \- Reach out to the external integration provider for guidance on how to use the v2 API Site Token with their Webflow integrations
          </li>

          <li>
            <b>Site tokens for custom integrations</b>

             \- Replace v1 Site Token with the new v2 Site Token and 

            [update v1 API calls](/data/changelog/webflow-api-changed-endpoints)

             to 

            [v2 APIs](/data/reference/token/authorized-by)
          </li>
        </ul>
      </Note>

      ### Third-party integrations

      If you're using v1 site tokens with third-party tools — for example, integrations or chrome extensions that have asked for your API Key — you'll want to replace them with a new [v2 API site token](/data/reference/site-token) to persist any critical workflows you have in place. These new tokens are more secure and can be used to call v2 Webflow APIs.

      To check for v1 API Site Tokens, go to <b>Apps & Integrations -> API access</b> in your site settings. v1 tokens will show a warning about using the legacy API.

      <Frame background="subtle">
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/d15b0e4360ec40076d41196823f0481e70c74071657402b3a8f8e2100669df61/products/data/pages/Resources/migrating-to-v2/v1-site-token-warning.png" alt="v1 Site Token warning" />
      </Frame>

      First, check to see if the token is still needed by seeing if the "Last used" date is recent. If it is, you'll want to generate a new v2 API token. To persist existing, active workflows, [generate a new v2 API token](https://help.webflow.com/hc/en-us/articles/33961356296723-Intro-to-Webflow-s-APIs) and update your integration to use the new token.

      When generating a new API token, you'll have the option to select the needed [permissions](/data/reference/scopes) for the token. If you're not sure which permissions to set, reach out to the integration provider for guidance.

      ### Third-party tools that don't support v2 site tokens

      If your third-party tool doesn't accept v2 site tokens, contact their support team for guidance. You can also email [developers@webflow.com](mailto:developers@webflow.com) to let us know which tool you're using so we can help ensure they add v2 support.

      ## Custom integrations

      If your team built and/or owns a custom integration that uses a v1 site token, in addition to switching to use a v2 API site token, you'll need to update the requests your integration is making from v1 APIs to v2 APIs.

      You can find more information about the changes from v1 to v2 in the [changelog](/data/changelog/webflow-api-changed-endpoints), and explore the new [v2 API structure and resources in the v2 API reference docs](/data/reference/structure-1).

      For more details on site tokens and how to use them for calling Webflow APIs, see the [site token guide](/data/reference/site-token).
    </Tab>

    <Tab title="Webhooks">
      <Note>
        <b>
          Action Item:
        </b>

        * **Create a new API V2 webhook** in the **Apps & Integrations -> Webhooks** section of your site settings
        * **Delete the old v1 Webhook** once you've confirmed your workflows still persist as expected
      </Note>

      If you're using v1 webhooks to recieve notifications about your site, you'll need to create new v2 webhooks to persist existing data workflows.

      To check for v1 webhooks, navigate to the <b>Apps & Integrations -> Webhooks</b> section of your site's settings to see a list of webhooks. Each webhook will show the event type, as well as the API version of the webhook.

      <Frame background="subtle">
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/f30472cc8b9c525a8c8f46cf2a6347d7b917c2cba3024808656ed55791ad4e28/products/data/pages/Resources/migrating-to-v2/webhook.png" alt="v1 webhook" />
      </Frame>

      To replace any active v1 webhooks, create an equivalent v2 webhook with the same even type to match functionality. You can do this by clicking the "Add webhook" button to create a v2 Webhook for the relevant event. Once you have equivalent v2 webhooks established alongside your v1 webhooks and tested that automations work with the new webhook, feel free to remove the v1 Webhook.

      ### Webhooks created by third-party Webflow Apps

      If a third-party Webflow App created the v1 webhook (i.e. Zapier),  migrate your workflow by using the newest version of the Webflow App.
    </Tab>

    <Tab title="Apps">
      <Note>
        <b>Action Item:</b> Re-authorize any v1 Apps with their updated v2 App in the [App Marketplace](https://webflow.com/apps).

        One way to note if an App is a v2 App if it lists Permissions on the App Listing (see screenshot below)

        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/c19db51ae33caaaaad73264364427656ed9defd377cecdd9c465e2b1d8577a32/assets/images/migration-to-v2-permissions.png" alt="v2 App Listing with permissions" />
      </Note>

      If you're using Webflow Apps to help manage your Webflow data, make sure you're using the v2 version of the App if it exists.

      To check if you're using the latest version of the App, navigate to the <b>Apps & Integrations -> Connected Apps</b> section of your site and/or workspace settings. There, you'll see a list of all the Apps connected to your site and/or workspace. Each App will have a "View details" button. Clicking this will show you more information about the App, including the permissions it requests.

      <Tabs>
        <Tab title="v1 App indicator">
          v1 authorizations do not list the permissions the App requires on install. See below for an example of a v1 App authorization

          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/d2585390b410446679722881e656f098dc9d4027254f0b65c053c67b3d558ddd/assets/images/migration-to-v2-v1-app-auth.png" alt="v1 App indicator example" />
        </Tab>

        <Tab title="v2 App indicator">
          In contrast, v2 App authorizations list the permissions the App requires on install. See below for an example of a v2 App authorization

          <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/4512b25d974ed975bfa16b5afb8dd3a15e436047d2ccaa8cb586370c6c4bacb8/assets/images/migration-to-v2-v2-app-auth.png" alt="v2 App indicator example" />
        </Tab>
      </Tabs>

      ### Third-party Apps that don't support v2

      If you cannot find a v2 version of the App in the marketplace, please reach out to that App developer for more support on how to migrate existing workflows to use v2 APIs. Additionally, you can search in the App Marketplace for other v2 Apps that are compatible with your use case.
    </Tab>
  </Tabs>
</Accordion>

## Migrating to API v2 for App developers

Are you a developer using v1 APIs and need guidance on implementing v2 APIs for a new v2 App? Read this section below.

<Accordion title="Building v2 Apps">
  We know migrating APIs can be challenging, but we're excited to help you upgrade to v2. The new version brings powerful capabilities that will let you build even better experiences for your users. Let's walk through how to migrate your existing v1 App:

  <Steps>
    ### Register a new v2 App

    To use the v2 API, you'll need to create a brand new App with a new Client ID and secret. Additionally, you'll need to add permissions to your App to align with the [v2 API scopes](/data/reference/scopes). Please use this [App registraton guide to help create a new v2 App.](/data/docs/register-an-app)

    ### Update your App's OAuth flow

    Update your App's [OAuth flow](/data/reference/oauth-app) to use your new client ID and secret. Additionally, you will need to use the new [v2 API scopes](/data/reference/scopes) in your App's Authorization URI. For a full guide on how to update your App's OAuth flow, see the [OAuth flow guide](/data/reference/oauth-app).

    ### Update your App to use v2 APIs

    Update the logic in your App to make requests to the new [v2 resources and endpoints.](/data/reference/structure-1) Additionally, you can use the updated [JavaScript or Python SDKs](/data/reference/sdks) to make requests to the new v2 APIs.

    ### Submit your v2 App to the Marketplace

    Once you've updated your App to use scopes and v2 endpoints, you can share these updates by [submitting your new App to the Marketplace](https://developers.webflow.com/submit). Before submitting your App, please refer to Webflow's [guidance on Marketplace submissions and listings](/apps/docs/marketplace-guidelines) to make sure your App is compliant with Webflow's guidelines.

    <Note title="Avoiding disruption">
      To avoid disrupting any existing workflows for users on the v1 App version, you'll want to support both v1 and v2 Apps in production until you've migrated all users to the v2 App.
    </Note>

    ### Instruct users to migrate to your v2 App

    Webflow won't automatically migrate or notify users of your new v2 App. Instead, **users must create a new authorization for the v2 App**. It's recommended that you reach out to existing v1 App users with migration instructions on how to safely migrate their existing workflows to your approved, v2 Marketplace App. This could include:

    * Notifications in your v1 App that tell users about the upcoming deprecation and the need to migrate to the v2 App
    * A link to your new v2 App Authorization page and/or a link to your v2 App in the Webflow App Marketplace
    * A migration tool in your v1 App that automatically replaces existing v1 integrations with v2 integrations
    * A blog post or migration guide on how to migrate from v1 to v2
  </Steps>

  ## v2 Apps and API changes

  * **v1 Apps are now named ‘Data Clients’**
    The v2 equivalent of v1 Apps are named [‘Data Clients’](/data/docs/data-clients). This is a change from the previous naming convention of ‘Apps’. Here's a quick rundown of what that means:
    * Data Clients access site data, spanning from the [CMS](/data/reference/cms/collection-items/staged-items/get-item) to [Ecommerce](/data/reference/ecommerce/settings/get-settings), as well as new resources like [assets](/data/reference/assets/assets/list), [pages](/data/reference/pages/list), and [custom code](/data/reference/custom-code). For an overview of the v2 API resources, see the [v2 API reference docs](/data/reference/structure-1).
    * Data Clients leverage Webflow's REST APIs to fetch this information.
    * For use cases that require real-time updates, Data Clients can send event notifications through [webhooks.](/data/reference/webhooks/list)

  * **Data API changes**
    The v2 API includes significant changes to Webflow's REST APIs, including updates, additions, and removals to key endpoints. For a thorough overview of what's changed, visit the changelog of:

    * [Changed Endpoints](/data/changelog/webflow-api-changed-endpoints)
    * [New Endpoints](/data/changelog/webflow-api-new-endpoints)
    * [Removed Endpoints](/data/changelog/webflow-api-removed-endpoints)

    To explore the current v2 API offerings, check out the [reference docs](https://developers.webflow.com/data/reference/token/authorized-by).

  * **Introduction of scopes**
    The new version of the API incorporates [scopes](/data/reference/scopes) into the authorization process. Scopes specify an App's permissions, ensuring that users have clearer control over the data an App can access and act upon. It's a step towards more transparency and security. For a granular approach to permissions, make sure you're aligned with [Webflow's guidance on scopes.](/data/reference/scopes)

  * **Updates to the JavaScript SDK**
    We're currently revamping the JavaScript SDK to provide robust support for the v2 APIs. In the meantime, if you're using the [JavaScript SDK](https://github.com/webflow/js-webflow-api), please:

    * Update to the most recent SDK version.
    * Use TypeScript/Intellisense in your code editor to guide API usage after instantiating a client. You may also find SDK snippets in the API reference docs examples. Here's a brief example on usage:

    <CodeBlocks>
      ```javascript JavaScript
         import { WebflowClient } from "webflow-api";

         const webflow = new WebflowClient({ accessToken });

         // Env. variables
         // in format of string, e.g.: "639656400769508adc12fe42"
         const siteId = process.env.SITE_ID;
         const customDomainId1 = process.env.CUSTOM_DOMAIN_ID_1;
         const customDomainId2 = process.env.CUSTOM_DOMAIN_ID_2;

         // Sites

         // List Sites
         const sites = await webflow.sites.list();

         // Get Site
         const site = await webflow.sites.get(siteId);

         // Get Custom Domains
         const customDomains = await webflow.sites.getCustomDomain(siteId);

         // Publish Site
         const site = await webflow.sites.publish(siteId, {
            customDomains: [customDomainId1, customDomainId2],
            publishToWebflowSubdomain: true,
         });
      ```
    </CodeBlocks>
</Accordion>
