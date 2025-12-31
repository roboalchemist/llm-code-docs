# Source: https://developers.notion.com/docs/build-a-link-preview-integration.md

# Build a Link Preview integration

A Link Preview is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user pastes a supported link in their workspace.

Developers can build Link Preview integrations to customize how links unfurl in Notion workspaces for domains they own.

![An example Link Preview for a GitHub workflow](https://files.readme.io/26b3cd4-link_unfurling_v2.gif)

This guide explains how to use the Notion Link Previews API to create Link Previews for your product. After you’ve read this guide, you’ll know how to:

1. [Configure Link Preview settings in the integration dashboard](https://www.notion.so/profile/integrations)
2. [Set up the authorization flow](#-set-up-the-authorization-flow)
3. [Use the Unfurl Callback URL](#-use-the-unfurl-callback-url)
4. [Manage updates to Link Previews](#-manage-updates-to-link-previews)
5. [Submit a Link Preview integration for security review](#-submit-your-integration-for-security-review)

> 🚧To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

## 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

## 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 2](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 3](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 📘If you don't see `Enable link preview` as an option, then:
> 
> - Make sure that you've applied and received access to the Link Previews API.
> - Confirm that you're logged in to the Notion account that you used to request access.
> - Reach out to **[developers@makenotion.com](mailto:developers@makenotion.com)** if you continue to have issues.

### 1. Fill out the External Authorization Setup form

The External Authorization Setup settings give Notion the information that it needs to let a user authenticate with your service when they paste a Link Preview enabled URL in Notion.

| Field               | Description                                                                                           | Example value                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| OAuth Authorize URL   | The URL that Notion redirects the user to when they connect your integration to their account.<br><br>
When Notion redirects to this URL, it passes a `code` as a query param in the request. Your integration trades the `code` for an `access_token` to make authenticated requests to the Link Previews APIs. | ![Image 4](https://files.readme.io/e384135-external_authorize_url.png) |

---

## 🛠️ Set up the authorization flow

Before users can paste a Link Preview-enabled URL into a Notion workspace, they need to authorize your app to access their Notion data. This is done by prompting them to click "Connect with my domain" or "Connect with my apps." When they do this, Notion redirects them to the URL that you provided in the External Authorization URL field.

![Image 5](https://files.readme.io/1108000-authorization_flow.png)

When Notion redirects to this URL, it passes a `code` as a query param in the request. Your integration trades the `code` for an `access_token` to make authenticated requests to the Link Previews APIs.

![Image 6](https://files.readme.io/1108001-authorization_flow_2.png)

### 2. Use the Unfurl Callback URL

After a user authorizes your app and redirects to your URL, you receive a `code` as a query parameter. You can use the `code` to exchange for an `access_token` and trigger the `Unfurling Domains` callback URL.

#### 📝 Code snippet

```javascript
const { WebhookClient } = require('@notionhq/node-sdk');
const webhookClient = new WebhookClient({ url: YOUR_UNFURLING_DOMAIN_CALLBACK_URL });

// Exchange for an access token
const response = await webhookClient.exchangeForAccessToken({
  grant_type: 'authorization_code',
  client_id: process.env.NOTION_CLIENT_ID,
  client_secret: process.env.NOTION_CLIENT_SECRET,
  code: YOUR_CODE,
});

// Now you have the access token!
response.access_token;
```

#### 📜 Unfurling Domain &amp; Patterns

After receiving the `access_token`, you can use it to fetch the list of domains and patterns that you want to include in your Link Previews.

```javascript
const { WebhookClient } = require('@notionhq/node-sdk');
const { models } = require('/@notionhq/node-sdk/models');

// Assuming you have an access token from step 1
const access_token = YOUR_ACCESS_TOKEN;

// Fetch the list of domains and patterns
async function getUnfurlingDomainsAndPatterns() {
  try {
    const response = await webhookClient.getUnfurlingDomainsAndPatterns(access_token);
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

getUnfurlingDomainsAndPatterns();
```

---

## 🛠️ Use the Unfurl Callback URL

After a user authorizes your app and redirects to your URL, you receive a `code` as a query parameter. You can use the `code` to exchange for an `access_token` and trigger the `Unfurling Domains` callback URL.

### 📝 Code snippet

```javascript
const { WebhookClient } = require('@notionhq/node-sdk');
const webhookClient = new WebhookClient({ url: YOUR_UNFURLING_DOMAIN_CALLBACK_URL });

// Exchange for an access token
const response = await webhookClient.exchangeForAccessToken({
  grant_type: 'authorization_code',
  client_id: process.env.NOTION_CLIENT_ID,
  client_secret: process.env.NOTION_CLIENT_SECRET,
  code: YOUR_CODE,
});

// Now you have the access token!
response.access_token;
```

### 📜 Unfurling Domain &amp; Patterns

After receiving the `access_token`, you can use it to fetch the list of domains and patterns that you want to include in your Link Previews.

```javascript
const { WebhookClient } = require('@notionhq/node-sdk');
const { models } = require('/@notionhq/node-sdk/models');

// Assuming you have an access token from step 1
const access_token = YOUR_ACCESS_TOKEN;

// Fetch the list of domains and patterns
async function getUnfurlingDomainsAndPatterns() {
  try {
    const response = await webhookClient.getUnfurlingDomainsAndPatterns(access_token);
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

getUnfurlingDomainsAndPatterns();
```

---

## 🛠️ Manage updates to Link Previews

As you add more Link Previews to your integration, you’ll need to update the `Unfurling Domains` callback URL in your integration’s settings.

### 📝 Code snippet

```javascript
const { WebhookClient } = require('@notionhq/node-sdk');
const webhookClient = new WebhookClient({ url: YOUR_UPDATE_DOMAIN_CALLBACK_URL });

// Update the Unfurling Domains callback URL
async function updateUnfurlingDomainsCallbackUrl() {
  try {
    const response = await webhookClient.updateUnfurlingDomainsCallbackUrl({ url: YOUR_UPDATE_DOMAIN_CALLBACK_URL });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}

updateUnfurlingDomainsCallbackUrl();
```

---

## 🛠️ Submit a Link Preview integration for security review

Before submitting your Link Preview integration for security review, review the Link Preview security checklist to ensure that your integration meets all the necessary standards.

### 📝 Checklist

- Verify that your integration has been authorized and has access to the Link Preview API.
- Ensure that your integration is configured correctly according to the documentation.
- Check that your integration provides proper error handling and logging.
- Confirm that your integration includes a mechanism to handle unauthorized access attempts.
- Make sure that your integration does not leak any sensitive information.
- Verify that your integration complies with Notion's terms of service and privacy policy.

### 📜 Additional resources

- Read the [Link Previews overview](https://developers.notion.com/docs/link-previews).
- Review the [Authorization guide](https://developers.notion.com/docs/authorization).
- Explore the [Notion developer portal](https://developers.notion.com/).
- Familiarize yourself with the [Notion API reference](https://developers.notion.com/reference).

---

## 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

## 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

## 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 7](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 8](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 9](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 10](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 11](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 12](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 13](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 14](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 15](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 16](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 17](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 18](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 19](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 20](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 21](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 22](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 23](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 24](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 25](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 26](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 27](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 28](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 29](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 30](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 31](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 32](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](https://developers.notion.com/docs/authorization).

### 🛠️ Configure Link Preview settings in the integration dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a Link Preview section in the Configuration tab.

![Image 33](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 34](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain &amp; Patterns form.

In the next section, we'll review how to fill out these forms.

> 🚧 To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.

### 🌱 Create a public Notion integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public

# OAuth Integration Setup

| Field | Description | Example value |
| --- | --- | --- |
| Unfurl Callback URL | The URL that shares data to be displayed in the Link Preview with Notion. Notion sends POST and DELETE requests to this URL when a user adds or deletes a Link Preview.<br><br>You can leave this blank as you set up OAuth and return to it once you’ve created your unfurl attributes. Refer to [Step 3](#step-3-use-the-unfurl-callback-url-to-set-unfurl-attributes-for-a-link-preview-handle-errors-and-manage-updates) for details.<br><br>Must be an internet-accessible URL that can and should be protected by authentication. | `https://<your_domain>.com/unfurl` |
| Unfurl URL Domain | The root domain that maps to this integration.<br><br>After you add a domain, follow the prompts to verify your domain with Notion. | `<your_domain>.com` |
| URL matching and placeholder | The pattern that a URL must match in order to unfurl as a Link Preview.<br><br>You can provide multiple patterns for one integration. | Refer to the table below. |

The URL matching and placeholder field includes its own fields:

| Field | Description | Example value |
| --- | --- | --- |
| Rule name | A name for the pattern. | `"item"` |
| Sample URLs | An example URL that matches the pattern and triggers a Link Preview. | `https://acme.com/items/23487` |
| Pattern | A Regex pattern that Notion can use to identify URLs that trigger Link Previews.<br><br>If the Regex pattern fails to match any sample URL, then an error prompt appears when you save settings. | `^(?&lt;site&gt;https\:\/\/acme\.com)\/items\/(?&lt;itemNo&gt;\d+)$` |
| Unfurl Regex Attributes | An array of JSON objects. Each JSON object contains placeholders, populated from Regex capture groups, for a Link Preview’s unfurl attributes. Placeholders are displayed when a Link Preview is waiting for data to populate from your service.<br><br>You can leave this blank as you set up OAuth and return to it once you’ve created your unfurl attributes. | ```[{ "id": "title", "name": "Title", "type": "inline", "inline": { "title": { "value": "Acme Item #$<itemNo>", "section": "title" } } }, { "id": "itemId", "name": "Item Id", "type": "inline", "inline": { "plain_text": { "value": "$<itemNo>", "section": "identifier" } } }, { "id": "dev", "name": "Developer Name", "type": "inline", "inline": { "plain_text": { "value": "Acme Inc", "section": "secondary" } } }]``` |

After you've filled out the External Authorization Setup and Unfurling Domain & Patterns settings, click `"Submit ->"` to create the integration.

## Set up the authorization flow

There are two high-level parts to the auth flow for a Link Preview:

- **Your service authenticates with Notion.** Notion sends a `code` to your OAuth Authorize URL. Your integration exchanges this `code` for a Notion `access_token` that enables your service to make authenticated requests to the Link Previews APIs.
- **Notion authenticates with your service.** Your service responds to Notion’s request with a `code`. Notion exchanges this token for your service’s `access_token` via your OAuth Token URL. This allows Notion to embed the data from your service in Link Previews.

The tokens **need to be exchanged the first time** a user attempts to add your Link Preview enabled URL to a page. After the initial exchange, the Notion `access_token` is long-lived and doesn’t need to be updated. If you prefer, Notion can also [support refresh tokens](#how-to-use-refresh-tokens-optional) and fetch new tokens from your service.

The auth flow begins when a user shares your Link Preview enabled URL in Notion. Notion recognizes the link and redirects to the OAuth Authorize URL that you provided in the integration settings.

Notion includes the following query parameters to kick off the OAuth flow with your service:

| Parameter | Description | Value |
| --- | --- | --- |
| `code` | A UUID that Notion generates to authenticate with your service. | `614846ff-b061-4eac-a511-fc20c3f0838a` (example value) |
| `redirect_uri` | A constant string. Your service redirects a user to this URL after they grant permission for it to access Notion.<br><br>To prevent attackers from providing arbitrary URIs, your service should validate that the redirect URI matches this value. | `https://notion.so/externalIntegrationAuthCallback` |
| `client_id` | The OAuth Client ID that you provided when you created the integration. | `mRkZGFjM` (example value) |
| `scope` (optional) | The OAuth Scopes value that you provided when you created the integration. | `unfurl`, `user_name` (example values) |
| `response_type` | A constant string. | `code` |
| `state` | A randomized string for security validation. | `tga@YNV9cfw4yrv0thw` (example value) |

Your implementation begins after Notion sends the request.

### 1. Provide OAuth form

Listen for requests to your OAuth Authorize URL. When you detect a request from Notion, present a UI that asks the user to allow the authentication process to continue.

For example, Slack shares the following interstitial when a user initiates a Link Preview from a Slack URL:

![An example interstitial from a Slack Link Preview auth flow](https://files.readme.io/4fb21e9-slack_interstitial.png)

### 2. Authenticate with Notion's `access_token`

In your integration implementation, retrieve the `code` that Notion sent when it called your OAuth Authorize URL. Then, send the `code` as part of a POST request to Notion’s token URL: `https://api.notion.com/v1/oauth/token`.

> **📘**
>
> The Notion `code` is valid for 10 minutes. If the `code` expires, then an error is returned and you need to reinitiate the auth flow for Notion to authenticate with your service ([Step 2a](#step-2a-provide-an-interstitial-for-the-auth-flow)).
>
> To explore other possible errors, refer to the [OAuth 2.0 documentation](https://www.oauth.com/oauth2-servers/server-side-apps/possible-errors/). Default to re-initiating the auth flow to handle errors.

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`: `CLIENT_ID:CLIENT_SECRET`. You can find these values on the integration settings page. Visit [notion.so/profile/integrations](https://www.notion.so/profile/integrations), find your integration, and click `View integration`.
```

# 3. Redirect to the `redirect_uri` with `code`

When a user selects `"Allow"` to grant Notion the requested permissions, redirect to the `redirect_uri`, the constant string [notion.so/externalIntegrationAuthCallback](http://notion.so/externalIntegrationAuthCallback), with your service’s unique `code` and the `state` that Notion sent to your service when it initiated the auth flow.

When Notion receives the redirect, it sends a POST request to the OAuth Token URL that you provided with the following body:

```plaintext
code
redirect_uri
grant_type
```

The body is sent in the `application/x-www-form-urlencoded` format and expects a JSON response.

## 4. Share the `access_token` with Notion

From your OAuth Token URL, respond to Notion’s POST request with an `access_token` body parameter in your 200 response.

Notion saves the `access_token` to send in future requests. Notion sends a request to your Unfurl Callback URL every time that the user associated with the token pastes a new Link Preview enabled URL or revisits a page with an existing Link Preview to refresh data.

### How Notion handles OAuth errors

Notion handles error responses as described by the [OAuth Error Spec](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1). The message that Notion displays to the user varies depending on the information that you provide.

For example, you can respond with an example access token:

```json
{
  "access_token": "ABC",
  "bot_id": "3d592781-2dcc-4d4b-bcf3-776a2a7ad7b8",
  "duplicated_template_id": null,
  "owner": {
    "id": "12345678-9011-2233-4455-66778899"
  },
  "token_type": "bearer",
  "workspace_id": "3d592781-2dcc-4d4b-bcf3-776a2a7ad7b8",
  "workspace_icon": "🍩",
  "workspace_name": "My Team Workspace"
}
```

# 📘

## How to use refresh tokens (optional)

### Skip to [Step 2e](#step-2e-test-the-auth-flow) if you’re creating long-living access tokens. This section only applies to temporary access tokens.

#### Return a `refresh_token`

Instead of creating a long-living `access_token`, you can send a `refresh_token` alongside a temporary access token. Notion can then use the `refresh_token` to fetch new tokens from your service.

If you return a `refresh_token`, then you need to also return an `expires_in` integer, as in the following example:

```json
{
  "access_token": "ABC",
  "refresh_token": "XYZ",
  "expires_in": 60000
}
```

`expires_in` represents the number of seconds until the `access_token` expires.

#### Notion requests to refresh a token

If Notion detects that the `access_token` is expired, meaning that the current time exceeds the time of the last refresh plus the `expires_in` value, then Notion refreshes the tokens when it calls your endpoints.

To refresh the token, Notion sends a POST request to your OAuth Token URL with the following parameters:

| Parameter | Description | Value |
| --- | --- | --- |
| `refresh_token` | The unique random string returned in the response to the previous request. | `"ABC"` (example value) |
| `client_id` | The OAuth Client ID that you provided when you created the integration. | `mRkZGFjM` (example value) |
| `client_secret` | The OAuth Client Secret that you provided when you created the integration. | `ZGVmMjMz` (example value) |
| `redirect_uri` | A constant string. | `https://notion.so/externalIntegrationAuthCallback` |
| `grant_type` | A constant string. | `refresh_token` |

#### Respond to Notion’s request to refresh a token

From your OAuth Token URL, return an `access_token` in your 200 response. You can optionally return new `refresh_token` and `expires_in` values.

## 5. Test the auth flow in Notion

To test the auth flow, make sure that you’ve added the integration to a workspace. Then, navigate to `"My connections"` in the workspace settings. Click `"Show all"`. Find the integration that you created in the list, and select `"Connect"` to kick off the auth flow.

![Image 1: 1606](https://files.readme.io/f60c3b9-discover_new_apps.png)

> If you don’t see your integration in the list, then refresh the page. Notion only loads new integrations on page load.

If the auth flow is successful, then you’ll see a new entry under the `"My connections"` menu.

![Image 2: 2000](https://files.readme.io/de0ca4c-my_connections.png)

To verify that the `key` for this connection is unique, repeat the auth flow multiple times using the same credentials to validate that you only get a single entry.

## 📞 Use the Unfurl Callback URL

### 1. Configure unfurl attributes

After a user pastes a Link Preview enabled link and completes the auth flow, Notion sends a POST request to the Unfurl Callback URL that you provided in the integration settings.

![Image 3: 1800](https://files.readme.io/4e59123-diagram-4.png)

> Notion sends the `access_token` from your service in a POST to the Unfurl Callback URL that you provide

The request includes a Bearer authorization with the user’s `access_token` from your service, and the payload is a single field called `uri` that includes the link that the user shared:

```bash
curl -d '{"uri":"http://example.com/file/123"}' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer <ACCESS_TOKEN>' \
     -X POST https://example.com/unfurl
```

Set up the Unfurl Callback URL to respond to Notion’s request with a 200 OK including the `uri`, and an array of all of the unfurl attributes, the values to display in the Link Preview. **The array must include a `title` attribute that gives the Link Preview a title and a _dev_ attribute that indicates the developer or company that created the Link Preview**.

The following is an example response:

```json
{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": [
        "attributes"
      ],
      "set": [
        {
          "id": "title",
          "name": "Title",
          "type": "inline",
          "inline": {
            "title": {
              "value": "The Link Preview's Title",
              "section": "title"
            }
          }
        },
        {
          "id": "dev",
          "name": "Developer Name",
          "type": "inline",
          "inline": {
            "plain_text": {
              "value": "Acme Inc",
              "section": "secondary"
            }
          }
        },
        {
          "id": "color",
          "name": "Color",
          "type": "inline",
          "inline": {
            "color": {
              "value": {
                "r": 235,
                "g": 64,
                "b": 52
              },
              "section": "background"
            }
          }
        }
      ]
    }
  ]
}
```

To preview how different response objects unfurl in a Link Preview, explore the integration's Link Preview Lab.

> To learn more about unfurl attributes, refer to the Link Preview [unfurl attributes reference](https://developers.notion.com/reference/unfurl-attribute-object).
```

# Link Previews

A Link Preview is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user pastes a supported link in their workspace.

Developers can build Link Preview integrations to customize how links unfurl in Notion workspaces for domains they own.

![An example Link Preview for a GitHub workflow](https://files.readme.io/26b3cd4-link_unfurling_v2.gif)

This guide explains how to use the Notion Link Previews API to create Link Previews for your product. After you’ve read this guide, you’ll know how to:

1. [Configure Link Preview settings in the integration dashboard](https://www.notion.so/profile/integrations)
2. [Set up the authorization flow](#-set-up-the-authorization-flow)
3. [Use the Unfurl Callback URL](#-use-the-unfurl-callback-url)
4. [Manage updates to Link Previews](#-manage-updates-to-link-previews)
5. [Submit a Link Preview integration for security review](#-submit-your-integration-for-security-review)

> 📚 **When updating a Link Preview’s unfurl attributes, there’s no need to clear the `error`. If no `error` is sent, then the `error` is automatically cleared.**

## Requirements

- You’ve [requested and received access to the Link Previews API](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).
- You own the domain that you’re using to create Link Previews. You’ll need to share a verification code from Notion with your domain host when you initialize the integration.
- Your application supports OAuth 2.0.
- You’ve read the [Link Previews overview](/docs/link-previews), so you have a good idea of what you’re building and how it works.
- You’ve read the [Authorization guide](/docs/authorization) and have familiarized yourself with Notion integrations.

With those requirements met, read on!

> 🚧 **To build a Link Preview integration, you must first request access to the Link Preview API. Fill out the [Link Preview request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) before proceeding if you haven’t already.**

## Create a Public Notion Integration

Link Preview integrations are a type of public integration. To create a Link Preview integration, you must first create a public integration. Once the public integration is created, you can enable the link preview setting through the [integration's settings](https://www.notion.so/profile/integrations).

To learn how to create a public integration, follow the [Authorization guide](/docs/authorization).

## Configure Link Preview Settings in the Integration Dashboard

This step will guide you through enabling link previews for your integration, as well as filling out the link preview integration forms found in your [integration settings](https://www.notion.so/profile/integrations).

To start, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a "Link Preview" section in the Configuration tab.

![Image 2](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 3](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain & Patterns form.

In the next section, we'll review how to fill out these forms.

> 📘 **If you don't see `Enable link preview` as an option, then:**
>
> - Make sure that you’ve [applied](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com) and received access to the Link Previews API.
> - Confirm that you’re logged in to the Notion account that you used to request access.
> - Reach out to **[email@example.com](mailto:%7Bemail_address%7D)** if you continue to have issues.

### 1. Fill out the External Authorization Setup Form

The External Authorization Setup settings give Notion the information that it needs to let a user authenticate with your service when they paste a Link Preview enabled URL in Notion.

| Field | Description | Example value |
| --- | --- | --- |
| OAuth Authorize URL | The URL that Notion redirects the user to when they connect your integration to their account.<br/><br/>When Notion redirects to this URL, it passes a `code` as a query param in the request. Your integration trades the `code` for an `access_token` to make authenticated requests to the Link Previews APIs. | `https://<your_domain>.com/notion/authorize` |
| OAuth Token URL | The URL that responds to a Notion POST request with an `access_token` for |

![Image 4](https://files.readme.io/264bfdf-diagram-delete.png)

**Note:** Notion sends a DELETE request to your `/unfurl` endpoint when a user deletes all Link Previews associated with a URL from their workspace.

Listen for the request to perform any associated actions, like deleting the record from your service.

## Set Up the Authorization Flow

This step outlines the process of setting up the authorization flow for your Link Preview integration.

To begin, navigate to the public integration you will be using for your link preview integration. It can be found in the [integration dashboard](https://www.notion.so/profile/integrations). If you have access to the Link Preview API, you will see a "Link Preview" section in the Configuration tab.

![Image 5](https://files.readme.io/c71bc87-integrations_5.png)

This page contains a toggle input to enable link previews for your integration. Switching it on will display the External Authorization Setup form that you need to fill out and save.

![Image 6](https://files.readme.io/c60a3e2-integrations_6.png)

Once the link preview toggle is turned on for the integration, you will need to fill out two forms in the following order:

1. The External Authorization Setup form.
2. The Unfurling Domain & Patterns form.

In the next section, we'll review how to fill out these forms.

## Use the Unfurl Callback URL

This section provides instructions on how to set up the Unfurl Callback URL to handle requests from Notion when a user pastes a Link Preview enabled URL.

To set up the Unfurl Callback URL, follow these steps:

1. Navigate to the Unfurl Callback URL settings in your integration's configuration.
2. Enter the URL where you want Notion to redirect users after they paste a Link Preview enabled URL. This URL should return an `access_token` to your integration.
3. Save the Unfurl Callback URL and confirm that it's working correctly.

## Manage Updates to Link Previews

This section explains how to manage updates to Link Previews.

If the unfurl attributes from your service change over time, then you can alert Notion to update the Link Preview to mirror those changes.

When your service detects changes to data that is referenced by a Link Preview, send a PATCH request to Notion’s `/v1/external/object` endpoint to update the unfurl attributes.

![Image 7](https://files.readme.io/1ed6985-diagram-2.png)

**Note:** Include all of the same objects from the Unfurl Callback URL response in the request, including the attributes that haven’t changed.

## Submit Your Integration for Security Review

This section details how to submit your integration for security review.

Before a Link Preview integration can be publicly distributed, it needs to pass a security review.

[Fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSd94UcRziV-1yFv6udO0qZwohLyXxhYYadUqEJyyEd03RAj1w/viewform) to submit your integration for review.

## Next Steps

- To learn more about customizing a Link Preview’s unfurl attributes, refer to the [reference docs](https://developers.notion.com/reference/unfurl-attribute-object).
```

# Link Preview Integration

## Overview

Link previews are a powerful feature that allow users to embed content from external services directly into your Notion pages. To enable link previews, you need to have an integration setup with Notion. This integration provides the necessary endpoints for your Notion service to interact with the Notion API.

## Required Information

Before you begin setting up the integration, ensure you have the following information:

| Field | Description | Example Value |
| --- | --- | --- |
| Access Token | The token used to access Notion's APIs. | `https://&lt;your_domain&gt;.com/notion/token` |
| OAuth Client ID | The client ID that Notion uses in its requests to your Authorize and OAuth Token URLs. | `mRkZGFjM` |
| OAuth Client Secret | The client secret that Notion uses in its requests to the Authorize and Token URLs. | `ZGVmMjMz` |
| OAuth Scopes (optional) | An optional scope string for Notion to send as a parameter in the request to your OAuth Authorize URL. | `unfurl`, `user_name` |
| Deleted Token Callback URL (optional) | A URL that Notion sends a DELETE request to when a user removes a Link Preview from a Notion page or disconnects your integration from their workspace, so that you can delete their tokens. <br/> You can use the request body that Notion sends to look up the user and deactivate their associated `access_token`s from your service. <br/> Whether or not you use a deleted token callback, Notion invalidates any Notion-side tokens corresponding to the user and the Link Preview that they delete. | `https://&lt;your_domain&gt;.com/notion/deletion` |

After you’ve filled out this information, click `"Submit ->"` to continue to Unfurling Domain & Patterns.

## Unfurling Domain & Patterns Form

The Unfurling Domain & Patterns settings give Notion the information that it needs to recognize the URLs that you want to unfurl Link Previews.

| Field | Description | Example Value |
| --- | --- | --- |
| Unfurl Callback URL | The URL that shares data to be displayed in the Link Preview with Notion. Notion sends POST and DELETE requests to this URL when a user adds or deletes a Link Preview. <br/> You can leave this blank as you set up OAuth and return to it once you’ve created your unfurl attributes. Refer to [Step 3](#step-3-use-the-unfurl-callback-url-to-set-unfurl-attributes-for-a-link-preview-handle-errors-and-manage-updates) for details. <br/> Must be an internet-accessible URL that can and should be protected by authentication. | `https://&lt;your_domain&gt;.com/unfurl` |
| Unfurl URL Domain | The root domain that maps to this integration. <br/> After you add a domain, follow the prompts to verify your domain with Notion. | `<your_domain>.com` |
| URL matching and placeholder | The pattern that a URL must match in order to unfurl as a Link Preview. <br/> You can provide multiple patterns for one integration. | Refer to the table below. |

The URL matching and placeholder field includes its own fields:

| Field | Description | Example Value |
| --- | --- | --- |
| Rule name | A name for the pattern. | `"item"` |
| Sample URLs | An example URL that matches the pattern and triggers a Link Preview. | `https://acme.com/items/23487` |
| Pattern | A Regex pattern that Notion can use to identify URLs that trigger Link Previews. <br/> If the Regex pattern fails to match any sample URL, then an error prompt appears when you save settings. | `^(?&lt;site&gt;https\:\/\/acme\.com)\/items\/(?&lt;itemNo&gt;\d+) $` |
| Unfurl Regex Attributes | An array of JSON objects. Each JSON object contains placeholders, populated from Regex capture groups, for a Link Preview’s unfurl attributes. Placeholders are displayed when a Link Preview is waiting for data to populate from your service. <br/> You can leave this blank as you set up OAuth and return to it once you’ve created your unfurl attributes. | ``` 
[
  {
    "id": "title",
    "name": "Title",
    "type": "inline",
    "inline": {
      "title": {
        "value": "Acme Item #$&lt;itemNo&gt;",
        "section": "title"
      }
    }
  },
  {
    "id": "itemId",
    "name": "Item Id",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "#$&lt;itemNo&gt;",
        "section": "identifier"
      }
    }
  },
  {
    "id": "dev",
    "name": "Developer Name",
    "type": "inline",
    "inline": {
      "plain_text": {
        "value": "Acme Inc",
        "section": "secondary"
      }
    }
  }
] 
```

After you've filled out the External Authorization Setup and Unfurling Domain & Patterns settings, click `"Submit ->"` to create the integration.

## Authorization Flow

There are two high-level parts to the auth flow for a Link Preview:

- **Your service authenticates with Notion.** Notion sends a `code` to your OAuth Authorize URL. Your integration exchanges this `code` for a Notion `access_token` that enables your service to make authenticated requests to the Link Previews APIs.
- **Notion authenticates with your service.** Your service responds to Notion’s request with a `code`. Notion exchanges this token for your service’s `access_token` via your OAuth Token URL. This allows Notion to embed the data from your service in Link Previews.

The tokens **need to be exchanged the first time** a user attempts to add your Link Preview enabled URL to a page. After the initial exchange, the Notion `access_token` is long-living and doesn’t need to be updated. If you prefer, Notion can also [support refresh tokens](#how-to-use-refresh-tokens-optional) and fetch new tokens from your service.

The auth flow begins when a user shares your Link Preview enabled URL in Notion. Notion recognizes the link and redirects to the OAuth Authorize URL that you provided in the integration settings.

Notion includes the following query params to kick off the OAuth flow with your service:

| Parameter | Description | Value |
| --- | --- | --- |
| `code` | A UUID that Notion generates to authenticate with your service. | `614846ff-b061-4eac-a511-fc20c3f0838a` (example value) |
| `redirect_uri` | A constant string. Your service redirects a user to this URL after they grant permission for it to access Notion. <br/> To prevent attackers from providing arbitrary URIs, your service should validate that the redirect URI matches this value. | `https://notion.so/externalIntegrationAuthCallback` |
| `client_id` | The OAuth Client ID that you provided when you created the integration. | `mRkZGFjM` (example value) |
| `scope` (optional) | The OAuth Scopes value that you provided when you created the integration. | `unfurl`, `user_name` (example values) |
| `response_type` | A constant string. | `code` |
| `state` | A randomized string for security validation. | `tga@YNV9cfw4yrv0thw` (example value) |

Your implementation begins after Notion sends the request.

### Provide OAuth Form

Listen for requests to your OAuth Authorize URL. When you detect a request from Notion, present a UI that asks the user to allow the authentication process to continue.

For example, Slack shares the following interstitial when a user initiates a Link Preview from a Slack URL:

![Image 1: 500](https://files.readme.io/4fb21e9-slack_interstitial.png)

An example interstitial from a Slack Link Preview auth flow

### Authenticate with Notion’s `access_token`

In your integration implementation, retrieve the `code` that Notion sent when it called your OAuth Authorize URL. Then, send the `code` as part of a POST request to Notion’s token URL: `https://api.notion.com/v1/oauth/token`.

> **📘**
> The Notion `code` is valid for 10 minutes. If the `code` expires, then an error is returned and you need to reinitiate the auth flow for Notion to authenticate with your service ([Step 2a](#step-2a-provide-an-interstitial-for-the-auth-flow)).
> 
> To explore other possible errors, refer to the [OAuth 2.0 documentation](https://www.oauth.com/oauth2-servers/server-side-apps/possible-errors/). Default to re-initiating the auth flow to handle errors.

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`: `CLIENT_ID:CLIENT_SECRET`. You can find these values on the integration settings page. Visit [notion.so/profile/integrations](https://www.notion.so/profile/integrations), find your integration, and click `View integration`.

![Image 2: 1006](https://files.readme.io/924df53-secrets.png)

You can find your integration's client ID and client secret on the integration settings page

> **📘**
> Note that in [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header. Notion also requires the word `Basic` before the `base64` encoded string. A complete code param looks something like the following:
> 
> ```
> Basic NjQ5Mzc0OTIzNzQ5MjM4NDc5MjM4NDc5MjM0NzkyMzc0OjQ3Mzg5Mjc0OTIzODQ3Mjk0ODcyMzkzNDgyNzk0ODcyMzQ5
> ```
> 
> For more information, read about HTTP Basic Authentication in our [Authorization guide](/docs/authorization#step-3-send-the-code-in-a-post-request-to-the-notion-api).

The body of the request contains the following JSON-encoded fields:

| Parameter | Description | Value |
| --- | --- | --- |
| `code` | A unique random code that Notion generates to authenticate with your service, generated when a user initiates the auth flow. | `"ABC"` (example value) |
| `grant_type` | A constant string. | `authorization_code` |
| `external_account` | Object with `key` and `name` properties. <br/> `key` should be a unique identifier for the account. Notion uses the `key` to determine whether or not the user is re-connecting the same account. <br/> `name` should be some way for the user to know which account they used to authenticate with your service. | Refer to the example below. |

The following example shows how the `external_account` object is structured:

```json
{
  "key": "unique_account_key",
  "name": "Account Name"
}
```

# How to Use the Notion API to Preview a Slack Link

e demonstrates an `external_account` object for `[@username]` (where `@` is the username), a Notion employee account, to authenticate with Slack to use a Slack Link Preview.

```json
{
  "key": "A83823453409384",
  "name": "Notion - [@username]"
}
```

The account `name` appears in the `"My connections"` settings page, where a user can review their authentications for your integration.

![An example authenticated Slack connection listed in a user’s "My connections" settings page.](https://files.readme.io/c8d2418-my_connections.png)

A complete POST request looks like the below:

```curl
curl --location --request POST 'https://api.notion.com/v1/oauth/token' \
--header 'Authorization: Basic "$BASE64_ENCODED_ID_AND_SECRET"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2022-06-28' \
--data '{
  "grant_type": "authorization_code",
  "code": "e202e8c9-0990-40af-855f-ff8f872b1ec6",
  "external_account": {
    "key": "A83823453409384",
    "name": "Notion - [@username]"
  }
}'
```

Notion responds to the request with a 200 OK and the following response body:

| Parameter | Description | Value |
| --- | --- | --- |
| `access_token` | A unique random string that Notion generates, in exchange for the `code`. You can use the `access_token` to make authorized requests to the Notion API. | `"ABC"` (example value) |
| `bot_id` | A UUID representing this authorization. | `"3d592781-2dcc-4d4b-bcf3-776a2a7ad7b8"` (example value) |
| `duplicated_template_id` | Always `null` for Link Preview integrations. Create a [standard public integration](/docs/getting-started#public-notion-integrations) to use template URLs with the API. | `null` |
| `owner` | An object indicating who owns the authorized workspace. Refer to the [bot object](/reference/user#bots) documentation. | Refer to the [bot object](/reference/user#bots) documentation. |
| `token_type` | A constant string. | `"bearer"` |
| `workspace_id` | A UUID representing the ID of the Notion workspace where the authorization flow took place. | `"3d592781-2dcc-4d4b-bcf3-776a2a7ad7b8"` (example value) |
| `workspace_icon` | A URL to an image, or a string of characters, that identifies the workspace. This could be useful if you’d like to display this authorization in your service’s UI. | `"🍩"` |
| `workspace_name` | A string representing a human-readable name that can be used to display this authorization in your service’s UI. | `"My Team Workspace"` (example value) |

Store the Notion response, and associate it with the user who initiated the OAuth flow. Notion stores the token that you provided.

> For tips on storing `access_token`s, check out [the auth guide](/docs/authorization#step-5-the-integration-stores-the-access_token-for-future-requests).

## 3. Redirect to the `redirect_uri` with `code`

When a user selects `"Allow"` to grant Notion the requested permissions, redirect to the `redirect_uri`, the constant string `notion.so/externalIntegrationAuthCallback`, with your service’s unique `code` and the `state` that Notion sent to your service when it initiated the auth flow.

When Notion receives the redirect, it sends a POST request to the OAuth Token URL that you provided with the following body:

| Parameter | Description | Value |
| --- | --- | --- |
| `code` | A unique random string that your service generates, retrieved from your service’s request to the `redirect_uri`. Notion is sending back the code that you sent. | `WQtaEYNV9jfL4yr89KJA0thw` |
| `client_id` | The OAuth Client ID that you provided when you created the integration. | `mRkZGFjM` (example value) |
| `client_secret` | The OAuth Client Secret that you provided when you created the integration. | `ZGVmMjMz` (example value) |
| `redirect_uri` | A constant string. | `notion.so/externalIntegrationAuthCallback` |
| `grant_type` | A constant string. | `authorization_code` |

The body is sent in the `application/x-www-form-urlencoded` format and expects a JSON response.

## 4. Share the `access_token` with Notion

From your OAuth Token URL, respond to Notion’s POST request with an `access_token` body parameter in your 200 response.

Notion saves the `access_token` to send in future requests. Notion sends a request to your Unfurl Callback URL every time that the user associated with the token pastes a new Link Preview enabled URL or revisits a page with an existing Link Preview to refresh data.

### How Notion handles OAuth errors

Notion handles error responses as described by the [OAuth Error Spec](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1). The message that Notion displays to the user varies depending on the information that you provide.

For example, you can respond with an `error` and a standard error code like `access_denied`:

```http
https://notion.so/externalintegrationauthcallback?error=access_denied
```

In this instance, Notion shares the following message:

![The message that Notion displays in the UI when it receives an `access_denied` error code from your service.](https://files.readme.io/6efcf27-example_message.png)

You can also add an `error_description` to the response:

```http
https://notion.so/externalintegrationauthcallback?error=access_denied&error_description=The+user+has+denied+your+application+access
```

If Notion detects a description, then it replaces the standard dialogue prompt with the specified description, as in the below:

![If you provide an `error_description` parameter, then the message in the Notion UI displays it.](https://files.readme.io/24b20be-specific_message.png)

If Notion doesn’t recognize the error code, then it notes that the error is unknown:

![The message that Notion displays in the UI when it doesn’t recognize an error code.](https://files.readme.io/fa0a2b4-unknown_error.png)

> For more details on standard error codes, refer to the [OAuth spec](https://www.rfc-editor.org/rfc/rfc6749#section-4.2.2.1).

#### How to use refresh tokens (optional)

> Skip to [Step 2e](#step-2e-test-the-auth-flow) if you’re creating long-living access tokens. This section only applies to temporary access tokens.

##### Return a `refresh_token`

Instead of creating a long-living `access_token`, you can send a `refresh_token` alongside a temporary access token. Notion can then use the `refresh_token` to fetch new tokens from your service.

If you return a `refresh_token`, then you need to also return an `expires_in` integer, as in the following example:

```json
{
  "access_token": "ABC",
  "refresh_token": "XYZ",
  "expires_in": 60000
}
```

`expires_in` represents the number of seconds until the `access_token` expires.

##### Notion requests to refresh a token

If Notion detects that the `access_token` is expired, meaning that the current time exceeds the time of the last refresh plus the `expires_in` value, then Notion refreshes the tokens when it calls your endpoints.

To refresh the token, Notion sends a POST request to your OAuth Token URL with the following parameters:

| Parameter | Description | Value |
| --- | --- | --- |
| `refresh_token` | The unique random string returned in the response to the previous request. | `WQtaEYNV9jfL4yr89KJA0thw` |
| `grant_type` | A constant string. | `authorization_code` |

The body is sent in the `application/x-www-form-urlencoded` format and expects a JSON response.
```

# 📝 Respond to Notion’s request to refresh a token

From your OAuth Token URL, return an `access_token` in your 200 response. You can optionally return new `refresh_token` and `expires_in` values.

## 5. Test the auth flow in Notion

To test the auth flow, make sure that you’ve added the integration to a workspace. Then, navigate to `"My connections"` in the workspace settings. Click `"Show all"`. Find the integration that you created in the list, and select `"Connect"` to kick off the auth flow.

![Image 1: 1606](https://files.readme.io/f60c3b9-discover_new_apps.png)

*Guess which icon represents our test integration*

> **📘**
> If you don’t see your integration in the list, then refresh the page. Notion only loads new integrations on page load.

If the auth flow is successful, then you’ll see a new entry under the `"My connections"` menu.

![Image 2: my_connections.png](https://files.readme.io/de0ca4c-my_connections.png)

*The new entry that appeared when we connected a much happier test Link Preview integration*

To verify that the `key` for this connection is unique, repeat the auth flow multiple times using the same credentials to validate that you only get a single entry.

## 📞 Use the Unfurl Callback URL

### 1. Configure unfurl attributes

After a user pastes a Link Preview enabled link and completes the auth flow, Notion sends a POST request to the Unfurl Callback URL that you provided in the integration settings.

![Image 3: diagram-4.png](https://files.readme.io/4e59123-diagram-4.png)

*Notion sends the `access_token` from your service in a POST to the Unfurl Callback URL that you provide*

The request includes a Bearer authorization with the user’s `access_token` from your service, and the payload is a single field called `uri` that includes the link that the user shared:

```bash
curl -d '{"uri":"http://example.com/file/123"}' \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <ACCESS_TOKEN>" \
    -X POST https://example.com/unfurl
```

Set up the Unfurl Callback URL to respond to Notion’s request with a 200 OK including the `uri`, and an array of all of the unfurl attributes, the values to display in the Link Preview. **The array must include a `title` attribute that gives the Link Preview a title and a _dev_ attribute that indicates the developer or company that created the Link Preview**.

The following is an example response:

```json
{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": [
        "attributes"
      ],
      "set": [
        {
          "id": "title",
          "name": "Title",
          "type": "inline",
          "inline": {
            "title": {
              "value": "The Link Preview's Title",
              "section": "title"
            }
          }
        },
        {
          "id": "dev",
          "name": "Developer Name",
          "type": "inline",
          "inline": {
            "plain_text": {
              "value": "Acme Inc",
              "section": "secondary"
            }
          }
        },
        {
          "id": "color",
          "name": "Color",
          "type": "inline",
          "inline": {
            "color": {
              "value": {
                "r": 235,
                "g": 64,
                "b": 52
              },
              "section": "background"
            }
          }
        }
      ]
    }
  ]
}
```

To preview how different response objects unfurl in a Link Preview, explore the integration's Link Preview Lab.

> **📘**
> To learn more about unfurl attributes, refer to the Link Preview [unfurl attributes reference](/reference/unfurl-attribute-object).

### 2. Handle unfurl request errors

Set up the Unfurl Callback URL to handle errors, as in the following example.

```json
{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": ["error"],
      "set": { "status": 404, "message": "Content not found" }
    }
  ]
}
```

## 🔁 Manage updates to Link Previews

### Update Link Previews to reflect data shared in unfurl attributes

If the unfurl attributes from your service change over time, then you can alert Notion to update the Link Preview to mirror those changes.

When your service detects changes to data that is referenced by a Link Preview, send a PATCH request to Notion’s `/v1/external/object` endpoint to update the unfurl attributes.

![Image 4: diagram-2.png](https://files.readme.io/1ed6985-diagram-2.png)

*To update the unfurl attributes displayed in a Link Preview, send a PATCH request to Notion’s `/v1/external/object` endpoint using all of the attributes from the original Unfurl Callback URL response*

Include all of the same objects from the Unfurl Callback URL response in the request, including the attributes that haven’t changed, as in the following example:

```bash
curl -d `{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": ["attributes"],
      "set": [
        {
          "id": "title",
          "name": "Title",
          "type": "inline",
          "inline": {
            "title": {
              "value": "The Link Preview's NEW Title",
              "section": "title"
            }
          }
        },
        {
          "id": "color",
          "name": "Color",
          "type": "inline",
          "inline": {
            "color": {
              "value": {
                "r": 235,
                "g": 64,
                "b": 52
              },
              "section": "background"
            }
          }
        }
      ]
    }
  ]
}` 
    -H "Content-Type: application/json" 
    -H "Authorization: Bearer <ACCESS_TOKEN>" 
    -H "Notion-Version: 2021-08-16" 
    -X PATCH https://api.notion.com/v1/external/object
```

It’s also possible to set a new error request. For example, if the data originally shared in a Link Preview can’t be found, then you could send an update request as follows:

```bash
curl -d `{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": ["error"],
      "set": { "status": 404, "message": "Content not found" }
    }
  ]
}` 
    -H "Content-Type: application/json" 
    -H "Authorization: Bearer <ACCESS_TOKEN>" 
    -H "Notion-Version: 2021-08-16" 
    -X PATCH https://api.notion.com/v1/external/object
```

You can also set both new attributes and an error request at the same time, as in the below example:

```bash
curl -d `{
  "uri": "http://example.com/file/123",
  "operations": [
    {
      "path": ["attributes"],
      "set": [
        {
          "id": "title",
          "name": "Title",
          "type": "inline",
          "inline": {
            "title": {
              "value": "The Link Preview's Title",
              "section": "title"
            }
          }
        },
        {
          "id": "color",
          "name": "Color",
          "type": "inline",
          "inline": {
            "color": {
              "value": {
                "r": 235,
                "g": 64,
                "b": 52
              },
              "section": "background"
            }
          }
        }
      ]
    },
    {
      "path": ["error"],
      "set": { "status": 404, "message": "Content not found" }
    }
  ]
}` 
    -H "Content-Type: application/json" 
    -H "Authorization: Bearer <ACCESS_TOKEN>" 
    -H "Notion-Version: 2021-08-16" 
    -X PATCH https://api.notion.com/v1/external/object
```

> **📘**
> When updating a Link Preview’s unfurl attributes, there’s no need to clear the `error`. If no `error` is sent, then the `error` is automatically cleared.

#### Notion updates your service when a user deletes Link Preview enabled URLs

When a user deletes all Link Previews associated with a URL from their workspace, Notion sends a DELETE request to your Unfurl Callback URL.

![Image 5: diagram-delete.png](https://files.readme.io/264bfdf-diagram-delete.png)

*Notion sends a DELETE request to your `/unfurl` endpoint.*

Listen for the request to perform any associated actions, like deleting the record from your service.

## 💫 Submit your integration for security review

Before a Link Preview integration can be publicly distributed, it needs to pass a security review. [Fill out this form](https://docs.google.com/forms/d/e/1FAIpQLSd94UcRziV-1yFv6udO0qZwohLyXxhYYadUqEJyyEd03RAj1w/viewform) to submit your integration for review.

## 👀 Next steps

- To learn more about customizing a Link Preview’s unfurl attributes, refer to the [reference docs](/reference/unfurl-attribute-object)
```

# How to Integrate Unfurling

## Table of Contents

*   [Overview](#overview)
*   [Getting Started](#getting-started)
    *   [1\. Set up your environment](#1-set-up-your-environment)
        *   [✅ Install the necessary tools](#install-the-necessary-tools)
        *   [✅ Create a new Notion workspace](#create-a-new-notion-workspace)
        *   [✅ Get your API token](#get-your-api-token)
        *   [✅ Set up your domain](#set-up-your-domain)
        *   [✅ Set up the authorization flow](#set-up-the-authorization-flow)
            *   [1\. Provide OAuth form](#1-provide-oauth-form)
            *   [2\. Authenticate with Notion’s `access_token`](#2-authenticate-with-notions-access_token)
            *   [3\. Redirect to the `redirect_uri` with `code`](#3-redirect-to-the-redirect_uri-with-code)
            *   [4\. Share the `access_token` with Notion](#4-share-the-access_token-with-notion)
            *   [5\. Test the auth flow in Notion](#5-test-the-auth-flow-in-notion)
    *   [2\. Use the Unfurl Callback URL](#2-use-the-unfurl-callback-url)
        *   [1\. Configure unfurl attributes](#1-configure-unfurl-attributes)
        *   [2\. Handle unfurl request errors](#2-handle-unfurl-request-errors)
    *   [🔁 Manage updates to Link Previews](#unrelated-manage-updates-to-link-previews)
        *   [Update Link Previews to reflect data shared in unfurl attributes](#update-link-previews-to-reflect-data-shared-in-unfurl-attributes)
    *   [💫 Submit your integration for security review](#submit-your-integration-for-security-review)
    *   [👀 Next steps](#next-steps)

## Overview

Unfurling is a powerful feature that allows users to embed link previews into your Notion workspace. This feature provides users with a quick and easy way to access information about links they encounter on social media or other online platforms.

In this tutorial, you'll learn how to integrate Unfurling and provide your users with this valuable functionality.

## Getting Started

### 1\. Set up your environment

#### ✅ Install the necessary tools

Install the following tools:

*   Node.js: [Download Node.js](https://nodejs.org/en/download/)
*   npm: [Install npm](https://www.npmjs.com/get-npm)
*   git: [Install git](https://git-scm.com/downloads/mac-os)

#### ✅ Create a new Notion workspace

Create a new workspace using the following command:

```bash
notion workspaces:create myworkspace
```

#### ✅ Get your API token

Get your API token from the Notion Developers website:

[Notion Developers website](https://developers.notion.so/)

#### ✅ Set up your domain

Set up your domain by adding a CNAME record to your DNS provider. The value of the CNAME record should be set to the subdomain of your Notion workspace name (e.g., `myworkspace.tld`). You can choose any domain that matches your workspace's name, but ensure it's not already registered by another user.

#### ✅ Set up the authorization flow

Follow these steps to set up the authorization flow:

##### 1\. Provide OAuth form

Open your web browser and navigate to the Notion developer portal:

[Notion developer portal](https://developers.notion.so/)

Click on "OAuth." Then click "Create App."

![Image 1](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1531c177174_Authentication%20-%20Notion%20Developer%20Portal.png)

Enter a name for your app, select the scope that you need, then click "Create App." Note that "Users have to grant access to this app" means that users will need to grant permission for your app to access their data.

![Image 2](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1630e177175_Authentication%20-%20Notion%20Developer%20Portal%20(1).png)

On the next screen, enter the URL where your callback function is located. For example, if your callback function is at `http://localhost:3000/oauth-callback`, enter `http://localhost:3000/oauth-callback`.

![Image 3](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e10144177176_Authentication%20-%20Notion%20Developer%20Portal%20(2).png)

Click "Continue."

![Image 4](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1e904177177_Authentication%20-%20Notion%20Developer%20Portal%20(3).png)

On the next screen, click "Generate client ID and client secret."

![Image 5](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e166ef177178_Authentication%20-%20Notion%20Developer%20Portal%20(4).png)

Copy both the client ID and client secret values.

![Image 6](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1512a177179_Authentication%20-%20Notion%20Developer%20Portal%20(5).png)

Go back to the OAuth page and click "Enable."

![Image 7](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1570c17717a_Authentication%20-%20Notion%20Developer%20Portal%20(6).png)

The final screen looks like this:

![Image 8](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1572017717b_Authentication%20-%20Notion%20Developer%20Portal%20(7).png)

Now you're ready to start integrating Unfurling!

##### 2\. Authenticate with Notion’s `access_token`

To authenticate with Notion’s `access_token`, you'll need to make a POST request to the `/oauth/token` endpoint with the following headers:

| Header | Value |
| --- | --- |
| Authorization | `Bearer <access_token>` |
| Content-Type | `application/json` |
| Accept | `application/json` |

Send the following JSON body as the request body:

```json
{
  "grant_type": "client_credentials",
  "client_id": "<client_id>",
  "client_secret": "<client_secret>",
  "scope": "<scope>"
}
```

If everything goes well, you'll receive a `Bearer Token` response in JSON format.

##### 3\. Redirect to the `redirect_uri` with `code`

After authenticating with Notion, you'll be redirected to the `redirect_uri` with a `code` parameter. Extract the `code` value and store it in a variable.

##### 4\. Share the `access_token` with Notion

Send a POST request to the `/oauth/token/{code}` endpoint to share the `access_token` with Notion. Include the `access_token` in the request body as the `token` parameter.

```http
POST https://www.notion.so/oauth/token/ HTTP/1.1
Host: www.notion.so
Authorization: Bearer <access_token>
Content-Type: application/json
Accept: application/json

{"token": <access_token>}
```

##### 5\. Test the auth flow in Notion

Visit your Notion workspace and look for a link with a preview of the link you provided earlier. Click on the link to test the auth flow.

## 📥 Use the Unfurl Callback URL

### 1\. Configure unfurl attributes

In your Notion workspace, go to **Settings** > **Embed Links** > **Link Preview Settings**.

![Image 9](https://assets-global.website-files.com/60879b1c83d4e10f6717715c/60879b1c83d4e1459817717c_Link%20Preview%20Attributes.png)

Configure the following attributes:

*   **URL**: The URL of the link you want to embed.
*   **Title**: The title of the link.
*   **Description**: The description of the link.
*   **Thumbnail URL**: The URL of the thumbnail image for the link preview.

### 2\. Handle unfurl request errors

In your callback function, handle potential errors that may occur during the Unfurl process. Here are some common error scenarios:

*   **Error 400 - Invalid URL**: If the provided URL is invalid or malformed, return an error message indicating that the URL is incorrect.
*   **Error 401 - Unauthorized**: If the user does not have access to the requested URL, return an error message indicating that the user is unauthorized to view the link.
*   **Error 404 - Page Not Found**: If the requested URL does not exist, return an error message indicating that the page cannot be found.

Here's an example of how you might handle errors in a callback function:

```javascript
// Assuming `url` is the URL you provided in the Unfurl attributes
try {
  const response = await fetch(`https://www.notion.so${url}`);
  const data = await response.json();
  const { link } = data;
  // Display the link preview here
} catch (error) {
  console.error('Error handling Unfurl request:', error);
}
```

## 🔽 Manage updates to Link Previews

### Update Link Previews to reflect data shared in unfurl attributes

When a link is unfetched, Notion needs to update the link previews to match the data provided in the Unfurl attributes. You can achieve this by making a PUT request to the `/link-preview/update` endpoint with the `token` parameter containing the `access_token` shared in the Unfurl attributes.

Here's an example of how you might update link previews when a link is unfetched:

```http
PUT https://www.notion.so/link-preview/update/ HTTP/1.1
Host: www.notion.so
Authorization: Bearer <access_token>
Content-Type: application/json
Accept: application/json

{
  "title": link.title,
  "description": link.description,
  "thumbnail_url": link.thumbnail_url
}
```

Replace `<access_token>` with the actual `access_token` shared in the Unfurl attributes.

By updating the link previews with the latest data, you ensure that users always have accurate and up-to-date information about the links they encounter.

## 💫 Submit your integration for security review

Before submitting your integration for security review, carefully review the Notion Developer Portal Terms of Service to ensure compliance.

## 👀 Next steps

Now that you've completed the setup process, you're ready to start integrating Unfurling into your Notion workspace. With this integration, users will be able to quickly access valuable information about links they encounter, enhancing their overall experience.

To further enhance the functionality of your integration, consider the following next steps:

*   Implement additional features, such as customizable link preview styles or automated notifications upon link click.
*   Conduct thorough testing to ensure seamless integration and optimal performance.
*   Document the integration thoroughly to provide comprehensive guidance to your users.

By following these next steps, you'll be well-positioned to maximize the benefits of Unfurling in your Notion workspace and provide users with an exceptional experience.
```