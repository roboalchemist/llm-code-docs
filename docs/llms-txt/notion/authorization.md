# Source: https://developers.notion.com/docs/authorization.md

# Authorization

This guide describes the authorization flows for internal and public Notion integrations.

## What is authorization?

Authorization is the process of granting an integration access to a user’s Notion data. That process varies depending on whether or not the integration is **public** or **internal**.

> 👍 [Link Preview integrations](https://developers.notion.com/docs/link-previews) — a subcategory of public integrations — use two-way OAuth, which differs from the authorization flow described in this guide.
>
> See the [Build a Link Preview integration guide](https://developers.notion.com/docs/build-a-link-preview-integration) to learn more about Link Preview authorization.

### What is an internal integration?

An internal integration allows Notion workspace members to interact with the workspace through the Notion REST API. Each internal integration is tied to a single, specific workspace and only members within the workspace can use the integration. After an internal integration is added to a workspace, members must manually [give the integration access to the specific pages or databases](https://www.notion.so/help/add-and-manage-connections-with-the-api#add-connections-to-pages) that they want it to use.

### What is a public integration?

Public integrations can be used by any Notion user in any workspace. They allow members to interact with their workspace using Notion’s REST API once the integration has been properly authorized.

Public integrations follow the [OAuth 2.0](https://oauth.net/2/) protocol. This allows workspace members to give access to Notion pages directly through the auth flow, without having to open each Notion workspace page directly and manually give permission to the integration. (More on this below.)

Public integrations can technically be used without permitting workspace pages access as long as the auth flow is completed and an [access token is created](https://developers.notion.com/reference/create-a-token) — a process which will be described in detail below. For example, if a public integration _only_ needs to interact with the Notion [User endpoints](https://developers.notion.com/reference/get-users), it does not need to be given access to workspace pages.

For more details on the differences between public and internal integrations, refer to the [getting started](https://developers.notion.com/docs/getting-started#integration-types) page.

Read on to learn how to set up the auth flows for internal and public integrations.

## Internal integration auth flow set-up

To use an internal integration, start by creating your integration in the [integration’s settings page](https://www.notion.so/profile/integrations).

The internal integration will be associated with the workspace of your choice. You are required to be a workspace owner to create an integration.

![Click the **New integration** button on the My integrations page to create a new integration.](https://files.readme.io/fd25d1f-integrations_7.png)

Once the integration is created, you can update its settings as needed under the `Configuration` tab and retrieve the integration token in this tab.

The integration token will be used to authenticate REST API requests. The integration sends the same token in every API request.

![Find the integration token in the integration's settings.](https://files.readme.io/69c7487-integrations_8.png)

### Integration permissions

Before an integration can interact with your Notion workspace page(s), the page must be manually shared with the integration. To share a page with an integration, visit the page in your Notion workspace, click the ••• menu at the top right of a page, scroll down to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

Once the integration is shared, you can start making API requests. If the page is not shared, any API requests made will respond with an error.

> 🚧 Keep your token secret
>
> Your integration token is a secret. To keep your integration secure, never store the token in your source code or commit it in version control. Instead, read the token from an environment variable. Use a secret manager or deployment system to set the token in the environment.
>
> [Learn more: Best Practices for Handling API Keys](https://developers.notion.com/docs/best-practices-for-handling-api-keys)

### Making API requests with an internal integration

Any time your integration is interacting with your workspace, you will need to include the integration token in the `Authorization` header with every API request. However, if you are using Notion’s [SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to interact with the REST API, the token is set once when a client is initialized.

```http
GET /v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75 HTTP/1.1
Authorization: Bearer {INTEGRATION_TOKEN}
```

```

# Public integration auth flow set-up

When an integration is made public, any Notion user in any workspace can use it.

Since a public integration is not tied to a single workspace with a single integration token, public integrations instead follow the [OAuth 2.0 protocol](https://oauth.net/2/) to authorize an integration to interact with a workspace.

## How to make a public integration

Select `New Integration` in your integration dashboard and select `Public` in the integration _Type_ during the creation flow. You may also edit an existing internal integration to convert to `Public`.

![Public integration example.](https://files.readme.io/736d786-integrations_9.png)

You will need to fill out the form with additional information, including your company name, website, and redirect URI(s).

The redirect URI is the URI your users will be redirected to after authorizing the public integration. To learn more, read [OAuth’s description of redirect URIs](https://www.oauth.com/oauth2-servers/redirect-uris/).

## Public integration authorization overview

Once your integration has been made public, you can update your integration code to use the public auth flow.

As an overview, the authorization flow includes the following steps. Each step will be described in more detail below.

1. Navigate the user to the integration’s authorization URL. This URL is provided in the [integration’s settings page](https://www.notion.so/profile/integrations).
2. After the user selects which workspace pages to share, Notion redirects the user to the integration’s redirect URI and includes a `code` query parameter. The redirect URI is the one you specified in your [integration’s settings page](https://www.notion.so/profile/integrations).
3. You will make a `POST` request to [create an access token](https://developers.notion.com/reference/create-a-token) , which will exchange the temporary `code` for an access token.
4. The Notion API responds with an access token and some additional information.
5. You will store the access token for future API requests. View the [API reference docs](https://developers.notion.com/reference/intro) to learn about available endpoints.

### Step 1: Navigate the user to the integration’s authorization URL

After your integration has been successfully made public in your [integration’s settings page](https://www.notion.so/profile/integrations), you will be able to access the integration’s secrets in the **Configuration** tab. Similarly to the internal integrations, these values should be protected and should never be included in source code or version control.

![The Authorization URL field populates after a public integration is submitted](https://files.readme.io/c535461-integrations_10.png)

As an example, your `.env` file using these secrets could look like this:

```shell
#.env

OAUTH_CLIENT_ID=<your-client-id>
OAUTH_CLIENT_SECRET=<your-client-secret>
NOTION_AUTH_URL=<your-auth-url>
```

To start the authorization flow for a public integration, you need to direct the prospective user to the authorization URL. To do this, it is common to include a hyperlink in the integration app that will be interacting with the Notion REST API. For example, if you have an app that will allow users to create new Notion pages for their workspace(s), you will first need them to first visit the authorization URL by clicking on the link.

The following example shows an authorization URL made available through a hyperlink:

```html
<a href="https://api.notion.com/v1/oauth/authorize?owner=user&amp;client_id=463558a3-725e-4f37-b6d3-0889894f68de&amp;redirect_uri=https%3A%2F%2Fexample.com%2Fauth%2Fnotion%2Fcallback&amp;response_type=code">Add to Notion</a>
```

The URL begins with `https://api.notion.com/v1/oauth/authorize` and has the following parameters:

| Parameter | Description | Required |
| --- | --- | --- |
| `client_id` | An identifier for your integration, found in the integration settings. | ✅ |
| `redirect_uri` | The URL where the user should return after granting access. | ✅ |
| `response_type` | Always use `code`. | ✅ |
| `owner` | Always use `user`. | ✅ |

Once the authorization URL is visited, the user will be shown a prompt that varies depending on whether or not the integration comes with a Notion template option.

#### Prompt for a standard integration with no template option (Default)

In the standard integration permissions flow, a prompt describes the integration [capabilities](https://developers.notion.com/reference/capabilities), presented to the user as what the integration would like to be able to do in the workspace. A user can either select pages to grant the integration access to, or cancel the request.

![Prompt for authorizing a standard integration (no template option)](https://files.readme.io/ec39f97-Screen_Shot_2021-07-22_at_2.58.28_PM.png)

If the user presses **Cancel**, they will be redirected to the redirect URI with an `error` query param added.

```plaintext
www.example.com/my-redirect-uri?error=access_denied&state=
```

You can use this `error` query parameter to conditionally update your app’s state as needed.

If the user opts to `Select pages`, then a page picker interface opens. A user can search for and select pages and databases to share with the integration from the page picker.

> The page picker only displays pages or databases to which a user has [full access](https://www.notion.so/help/sharing-and-permissions), because a user needs full access to a resource in order to be able to share it with an integration.

![Page picker interface](https://files.readme.io/a4009ce-Screen_Shot_2021-07-22_at_3.09.51_PM.png)

Users can select which pages to give the integration access to, including both private and public pages available to them. Parent pages can be selected to quickly provide access to child pages, as giving access to a parent page will provide access to all available child pages. Users can return to this view at a later time to update access settings if circumstances change.

If the user clicks `Allow access`, they are then redirected to the `redirect_uri` with a temporary authorization `code`. If the user denies access, they are redirected to the `redirect_uri` with an `error` query parameter.

If the user clicks `Allow access` and the rest of the auth flow is not completed, the integration will _not_ have access to the pages that were selected.

#### Prompt for an integration with a Notion template option

Public integrations offer the option of providing a public Notion page to use as a template during the auth flow.

To add a template to your workspace, complete the following steps:

1. Choose a public page in your workspace that you want users to be able to duplicate.
2. Navigate to your [integration’s settings](https://www.notion.so/profile/integrations) and go to the **Basic Information** tab.
3. Scroll to the bottom of your distribution settings and add the URL of the Notion page you selected to the **Notion URL for optional template** input.

![Notion URL for optional template input in integration settings.](https://files.readme.io/b4ae671-integrations11.png)

Once this URL is added, your auth flow prompt appearance will be updated.

Going back to your prompt view, if the integration offers a Notion template option, the first step in the permissions flow will describe the integration [capabilities](https://developers.notion.com/reference/capabilities). This is presented to the user as what the integration would be able to do in the workspace, and it prompts the user to click `Next`.
```

# Prompt for an integration with a Notion template option

In the next step, a user can either choose to duplicate the template that you provided or to select existing pages to share with the integration.

![Image 1: 1052](https://files.readme.io/9788bdb-template_prompt_2.png)

A user can select to duplicate a template or to share existing pages with the integration.

If the user chooses to duplicate the template, then the following happens automatically:

- The integration is added to the user’s workspace.
- The template is duplicated as a new page in the workspace.
- The new page is shared with the integration.

If the user chooses to select pages to share with the integration, then they continue to the page picker interface that’s part of the [prompt for a standard integration](#prompt-for-a-standard-integration-with-no-template-option-default).

> 📘 After a user installs a public integration, only that user is able to interact or share pages and databases with the integration. Unlike internal integrations, if multiple members in a workspace want to use a public integration, each prospective user needs to individually follow the auth flow for the integration.

## User authorization failures

User authorization failures can happen. If a user chooses to `Cancel` the request, then a failure is triggered. Build your integration to handle these cases gracefully, as needed.

In some cases, Notion redirects the user to the `redirect_uri` that you set up when you created the public integration, along with an `error` query parameter. Notion uses the common [error codes in the OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1). Use the `error` code to create a helpful prompt for the user when they’re redirected here.

### Step 2: Notion redirects the user to the integration’s redirect URI and includes a `code` parameter

When you first created the public integration, you specified a redirect URI. If the user follows the prompt to `Allow access` for the integration, then Notion generates a temporary `code` and sends a request to the redirect URI with the following information in the query string:

| Parameter | Description | Required |
| --- | --- | --- |
| `code` | A temporary authorization code. | ✅ |
| `state` | The value provided by the integration when the user was [prompted for access](#prompt-for-a-standard-integration-with-no-template-option-default). |  |

To complete the next set, you will need to retrieve the `code` query parameter provided in the redirect. How you retrieve this value will vary depending on your app’s tech stack.

In a React component, for example, the query parameters are made available through the `useRouter()` hook:

```javascript
export default function AuthRedirectPage() {
  const router = useRouter();
  const { code } = router.query;
  ...
}
```

### Step 3: Send the `code` in a `POST` request to the Notion API

The integration needs to exchange the temporary `code` for an `access_token`.

To set up this step, retrieve the `code` from the redirect URI.

Next, you will need to send the `code` as part of a `POST` request to Notion’s token endpoint: [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [creating a token](https://developers.notion.com/reference/create-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```
CLIENT_ID:CLIENT_SECRET
```

You can find both of these values in the [integration’s settings](https://www.notion.so/profile/integrations).

Note that in [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `"grant_type"` | `string` | Always use `"authorization_code"`. | ✅ |
| `"code"` | `string` | The temporary authorization code received in the incoming request to the `"redirect_uri"`. | ✅ |
| `"redirect_uri"` | `string` | The `"redirect_uri"` that was provided in the Authorization step. | ❌/❌*
* If the redirect URI was supplied as a query param in the Authorization URL, this field is required. If there are more than one redirect URIs included in your integration settings, this field is required. Otherwise, it is not allowed. Learn more in the [Create a token page](https://developers.notion.com/reference/create-a-token). |

The following is an example request to exchange the authorization code for an access token:

```http
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET" 
Content-Type: application/json

{"grant_type":"authorization_code","code":"e202e8c9-0990-40af-855f-ff8f872b1ec6", "redirect_uri":"https://example.com/auth/notion/callback"}
```

The Node-equivalent of this example would look something like this:

```javascript
...
const clientId = process.env.OAuthClientID;
const clientSecret = process.env.OAuthClientSecret;
const redirectUri = process.env.OauthRedirectURI;

// encode in base 64
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Basic ${encoded}`,
  },
  body: JSON.stringify({
    grant_type: "authorization_code",
    code: "your-temporary-code",
    redirect_uri: redirectUri,
  }),
});
...
```

### Step 4: Notion responds with an `access_token`, `refresh_token`, and additional information

Notion responds to the request with an `access_token`, `refresh_token`, and additional information. The `access_token` will be used to authenticate subsequent Notion REST API requests. The `refresh_token` will be used to refresh the access token, which generates a new `access_token`.
```

# What is authorization?

Authorization is the process of granting an integration access to a user’s Notion data. That process varies depending on whether or not the integration is **public** or **internal**.

> 👍 [Link Preview integrations](/docs/link-previews) — a subcategory of public integrations — use two-way OAuth, which differs from the authorization flow described in this guide.
>
> See the [Build a Link Preview integration guide](/docs/build-a-link-preview-integration) to learn more about Link Preview authorization.

## What is an internal integration?

An internal integration allows Notion workspace members to interact with the workspace through the Notion REST API. Each internal integration is tied to a single, specific workspace and only members within the workspace can use the integration. After an internal integration is added to a workspace, members must manually [give the integration access to the specific pages or databases](https://www.notion.so/help/add-and-manage-connections-with-the-api#add-connections-to-pages) that they want it to use.

## What is a public integration?

Public integrations can be used by any Notion user in any workspace. They allow members to interact with their workspace using Notion’s REST API once the integration has been properly authorized.

Public integrations follow the [OAuth 2.0](https://oauth.net/2/) protocol. This allows workspace members to give access to Notion pages directly through the auth flow, without having to open each Notion workspace page directly and manually give permission to the integration. (More on this below.)

Public integrations can technically be used without permitting workspace pages access as long as the auth flow is completed and an [access token is created](/reference/create-a-token) — a process which will be described in detail below. For example, if a public integration _only_ needs to interact with the Notion [User endpoints](/reference/get-users), it does not need to be given access to workspace pages.

For more details on the differences between public and internal integrations, refer to the [getting started](/docs/getting-started#integration-types) page.

Read on to learn how to set up the auth flows for internal and public integrations.

## Internal integration auth flow set-up

To use an internal integration, start by creating your integration in the [integration’s settings page](https://www.notion.so/profile/integrations).

The internal integration will be associated with the workspace of your choice. You are required to be a workspace owner to create an integration.

![Click the **New integration** button on the My integrations page to create a new integration.](https://files.readme.io/fd25d1f-integrations_7.png)

Once the integration is created, you can update its settings as needed under the `Configuration` tab and retrieve the integration token in this tab.

The integration token will be used to authenticate REST API requests. The integration sends the same token in every API request.

![Find the integration token in the integration's settings.](https://files.readme.io/69c7487-integrations_8.png)

### Integration permissions

Before an integration can interact with your Notion workspace page(s), the page must be manually shared with the integration. To share a page with an integration, visit the page in your Notion workspace, click the ••• menu at the top right of a page, scroll down to `Add connections`, and use the search bar to find and select the integration from the dropdown list.

Once the integration is shared, you can start making API requests. If the page is not shared, any API requests made will respond with an error.

> 🚧 Keep your token secret
>
> Your integration token is a secret. To keep your integration secure, never store the token in your source code or commit it in version control. Instead, read the token from an environment variable. Use a secret manager or deployment system to set the token in the environment.
>
> [Learn more: Best Practices for Handling API Keys](/docs/best-practices-for-handling-api-keys)

### Making API requests with an internal integration

Any time your integration is interacting with your workspace, you will need to include the integration token in the `Authorization` header with every API request. However, if you are using Notion’s [SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) to interact with the REST API, you can do so as shown below:

```javascript
const clientId = process.env.OAuthClientID;
const clientSecret = process.env.OAuthClientSecret;

// encode in base 64
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Basic ${encoded}`,
  },
  body: JSON.stringify({
    grant_type: "refresh_token",
    refresh_token: "your-refresh-token",
  }),
});
```
```

# Public integration auth flow set-up

When an integration is made public, any Notion user in any workspace can use it.

Since a public integration is not tied to a single workspace with a single integration token, public integrations instead follow the [OAuth 2.0 protocol](https://oauth.net/2/) to authorize an integration to interact with a workspace.

## How to make a public integration

Select `New Integration` in your integration dashboard and select `Public` in the integration _Type_ during the creation flow. You may also edit an existing internal integration to convert to `Public`.

![Public integration example.](https://files.readme.io/736d786-integrations_9.png)

You will need to fill out the form with additional information, including your company name, website, and redirect URI(s).

The redirect URI is the URI your users will be redirected to after authorizing the public integration. To learn more, read [OAuth’s description of redirect URIs](https://www.oauth.com/oauth2-servers/redirect-uris/).

### Public integration authorization overview

Once your integration has been made public, you can update your integration code to use the public auth flow.

As an overview, the authorization flow includes the following steps. Each step will be described in more detail below.

1. Navigate the user to the integration’s authorization URL. This URL is provided in the [integration’s settings page](https://www.notion.so/profile/integrations).
2. After the user selects which workspace pages to share, Notion redirects the user to the integration’s redirect URI and includes a `code` query parameter. The redirect URI is the one you specified in your [integration’s settings page](https://www.notion.so/profile/integrations).
3. You will make a `POST` request to [create an access token](https://www.notion.so/reference/create-a-token) , which will exchange the temporary `code` for an access token.
4. The Notion API responds with an access token and some additional information.
5. You will store the access token for future API requests. View the [API reference docs](https://www.notion.so/reference/intro) to learn about available endpoints.

### Step 1: Navigate the user to the integration’s authorization URL

After your integration has been successfully made public in your [integration’s settings page](https://www.notion.so/profile/integrations), you will be able to access the integration’s secrets in the **Configuration** tab. Similarly to the internal integrations, these values should be protected and should never be included in source code or version control.

![Authorization URL field.](https://files.readme.io/c535461-integrations_10.png)

As an example, your `.env` file using these secrets could look like this:

```bash
# .env

OAUTH_CLIENT_ID=<your-client-id>
OAUTH_CLIENT_SECRET=<your-client-secret>
NOTION_AUTH_URL=<your-auth-url>
```

To start the authorization flow for a public integration, you need to direct the prospective user to the authorization URL. To do this, it is common to include a hyperlink in the integration app that will be interacting with the Notion REST API. For example, if you have an app that will allow users to create new Notion pages for their workspace(s), you will first need them to first visit the authorization URL by clicking on the link.

The following example shows an authorization URL made available through a hyperlink:

```html
<a href="https://api.notion.com/v1/oauth/authorize?owner=user&client_id=463558a3-725e-4f37-b6d3-0889894f68de&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%2Fnotion%2Fcallback&response_type=code">Add to Notion</a>
```

The URL begins with `https://api.notion.com/v1/oauth/authorize` and has the following parameters:

| Parameter | Description | Required |
| --- | --- | --- |
| `client_id` | An identifier for your integration, found in the integration settings. | ✅ |
| `redirect_uri` | The URL where the user should return after granting access. | ✅ |
| `response_type` | Always use `code`. | ✅ |
| `owner` | Always use `user`. | ✅ |
| `state` | If the user was in the middle of an interaction or operation, then this parameter can be used to restore state after the user returns. It can also be used to prevent CSRF attacks. |  |

Once the authorization URL is visited, the user will be shown a prompt that varies depending on whether or not the integration comes with a Notion template option.

#### Prompt for a standard integration with no template option (Default)

In the standard integration permissions flow, a prompt describes the integration [capabilities](https://www.notion.so/reference/capabilities), presented to the user as what the integration would like to be able to do in the workspace. A user can either select pages to grant the integration access to, or cancel the request.

![Prompt for authorizing a standard integration (no template option).](https://files.readme.io/ec39f97-Screen_Shot_2021-07-22_at_2.58.28_PM.png)

If the user presses **Cancel**, they will be redirected to the redirect URI with and `error` query param added.

```plaintext
www.example.com/my-redirect-uri?error=access_denied&state=
```

You can use this `error` query parameter to conditionally update your app’s state as needed.

If the user opts to `Select pages`, then a page picker interface opens. A user can search for and select pages and databases to share with the integration from the page picker.

> The page picker only displays pages or databases to which a user has [full access](https://www.notion.so/help/sharing-and-permissions), because a user needs full access to a resource in order to be able to share it with an integration.

![Page picker interface.](https://files.readme.io/a4009ce-Screen_Shot_2021-07-22_at_3.09.51_PM.png)

Users can select which pages to give the integration access to, including both private and public pages available to them. Parent pages can be selected to quickly provide access to child pages, as giving access to a parent page will provide access to all available child pages. Users can return to this view at a later time to update access settings if circumstances change.

If the user clicks `Allow access`, they are then redirected to the `redirect_uri` with a temporary authorization `code`. If the user denies access, they are redirected to the `redirect_uri` with an `error` query parameter.

If the user clicks `Allow access` and the rest of the auth flow is not completed, the integration will _not_ have access to the pages that were selected.

#### Prompt for an integration with a Notion template option

Public integrations offer the option of providing a public Notion page to use as a template during the auth flow.

To add a template to your workspace, complete the following steps:

* Choose a public page in your workspace that you want users to be able to duplicate.
* Navigate to your [integration’s settings](https://www.notion.so/profile/integrations) and go to the **Basic Information** tab.
* Scroll to the bottom of your distribution settings and add the URL of the Notion page you selected to the **Notion URL for optional template** input.

![Notion URL for optional template input in integration settings.](https://files.readme.io/b4ae671-integrations11.png)

Once this URL is added, your auth flow prompt appearance will be updated.

Going back to your prompt view, if the integration offers a Notion template option, the first step in the permissions flow will describe the integration [capabilities](https://www.notion.so/reference/capabilities). This is presented to the user as what the integration would be able to do in the workspace, and it prompts the user to click `Next`.

![Prompt for an integration with a Notion template option.](https://files.readme.io/77076c7-template_prompt1.png)

In the next step, a user can either choose to duplicate the template that you provided or to select existing pages to share with the integration.

![A user can select to duplicate a template or to share existing pages with the integration.](https://files.readme.io/9788bdb-template_prompt_2.png)

If the user chooses to duplicate the template, then the following happens automatically:

* The integration is added to the user’s workspace.
* The template is duplicated as a new page in the workspace.
* The new page is shared with the integration.

If the user chooses to select pages to share with the integration, then they continue to the page picker interface that’s part of the [prompt for a standard integration](#prompt-for-a-standard-integration-with-no-template-option-default).

> After a user installs a public integration, only that user is able to interact or share pages and databases with the integration. Unlike internal integrations, if multiple members in a workspace want to use a public integration, each prospective user needs to individually follow the auth flow for the integration.

**User authorization failures**

User authorization failures can happen. If a user chooses to `Cancel` the request, then a failure is triggered. Build your integration to handle these cases gracefully, as needed.

In some cases, Notion redirects the user to the `redirect_uri` that you set up when you created the public integration, along with an `error` query parameter. Notion uses the common [OAuth 2.0 error response format](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1).

```plaintext
redirect_uri?error=access_denied&state=
```

# OAuth Integration Flow

## Step 1: Notion Redirects the User to the Integration’s Redirect URI and Includes a Code Parameter

When you first created the public integration, you specified a redirect URI. If the user follows the prompt to `Allow access` for the integration, then Notion generates a temporary `code` and sends a request to the redirect URI with the following information in the query string:

| Parameter | Description | Required |
| --- | --- | --- |
| `code` | A temporary authorization code. | ✅ |
| `state` | The value provided by the integration when the user was [prompted for access](#prompt-for-a-standard-integration-with-no-template-option-default). |  |

To complete the next set, you will need to retrieve the `code` query parameter provided in the redirect. How you retrieve this value will vary depending on your app’s tech stack.

In a React component, for example, the query parameters are made available through the `useRouter()` hook:

```jsx
export default function AuthRedirectPage() {
  const router = useRouter();
  const { code } = router.query;
  ...
}
```

## Step 2: Notion Redirects the User to the Integration’s Redirect URI and Includes a Code Parameter

When you first created the public integration, you specified a redirect URI. If the user follows the prompt to `Allow access` for the integration, then Notion generates a temporary `code` and sends a request to the redirect URI with the following information in the query string:

| Parameter | Description | Required |
| --- | --- | --- |
| `code` | A temporary authorization code. | ✅ |
| `state` | The value provided by the integration when the user was [prompted for access](#prompt-for-a-standard-integration-with-no-template-option-default). |  |

To complete the next set, you will need to retrieve the `code` query parameter provided in the redirect. How you retrieve this value will vary depending on your app’s tech stack.

In a React component, for example, the query parameters are made available through the `useRouter()` hook:

```jsx
export default function AuthRedirectPage() {
  const router = useRouter();
  const { code } = router.query;
  ...
}
```

## Step 3: Send the Code in a POST Request to the Notion API

The integration needs to exchange the temporary `code` for an `access_token`.

To set up this step, retrieve the `code` from the redirect URI.

Next, you will need to send the `code` as part of a `POST` request to Notion’s token endpoint: [https://api.notion.com/v1/oauth/token](https://api.notion.com/v1/oauth/token).

This endpoint is described in more detail in the API reference docs for [creating a token](/reference/create-a-token).

The request is authorized using HTTP Basic Authentication. The credential is a colon-delimited combination of the integration’s `CLIENT_ID` and `CLIENT_SECRET`, like so:

```
CLIENT_ID:CLIENT_SECRET
```

You can find both of these values in the [integration’s settings](https://www.notion.so/profile/integrations).

Note that in [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), credentials are `base64` encoded before being added to the `Authorization` header.

The body of the request contains the following JSON-encoded fields:

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| `"grant_type"` | `string` | Always use `"authorization_code"`. | ✅ |
| `"code"` | `string` | The temporary authorization code received in the incoming request to the `"redirect_uri"`. | ✅ |
| `"redirect_uri"` | `string` | The `"redirect_uri"` that was provided in the Authorization step. | ✅/❌<br/> * If the redirect URI was supplied as a query param in the Authorization URL, this field is required. If there are more than one redirect URIs included in your integration settings, this field is required. Otherwise, it is not allowed. Learn more in the [Create a token page](/reference/create-a-token). |

The following is an example request to exchange the authorization code for an access token:

```http
POST /v1/oauth/token HTTP/1.1
Authorization: Basic "$CLIENT_ID:$CLIENT_SECRET" 
Content-Type: application/json

{"grant_type":"authorization_code","code":"e202e8c9-0990-40af-855f-ff8f872b1ec6", "redirect_uri":"https://example.com/auth/notion/callback"}
```

The Node-equivalent of this example would look something like this:

```js
...
const clientId = process.env.OAuthClientId;
const clientSecret = process.env.OAuthClientSecret;
const redirectUri = process.env.OAuthRedirectUri;

// encode in base 64
const encoded = btoa(`${clientId}:${clientSecret}`);

const response = await fetch("https://api.notion.com/v1/oauth/token", {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
    Authorization: `Basic ${encoded}`,
  },
  body: JSON.stringify({
    grant_type: "authorization_code",
    code: "your-temporary-code",
    redirect_uri: redirectUri,
  }),
});
...
```

## Step 4: Notion Responds with an Access Token, Refresh Token, and Additional Information

Notion responds to the request with an `access_token`, `refresh_token`, and additional information. The `access_token` will be used to authenticate subsequent Notion REST API requests. The `refresh_token` will be used to refresh the `access_token`, which generates a new `access_token`.

The response contains the following JSON-encoded fields:

| Field | Type | Description | Not null |
| --- | --- | --- | --- |
| `"access_token"` | `string` | An access token used to authorize requests to the Notion API. | ✅ |
| `"refresh_token"` | `string` | A refresh token used to generate a new `access_token`. | ✅ |
| `"bot_id"` | `string` | An identifier for this authorization. | ✅ |
| `"duplicated_template_id"` | `string` | The ID of the new page created in the user’s workspace. The new page is a duplicate of the template that the developer provided with the integration. If the developer didn’t provide a template for the integration, then the value is `null`. |  |
| `"owner"` | `object` | An object containing information about who can view and share this integration. `{ "workspace": true }` is returned for installations of workspace-level tokens. For user level tokens, a [user object](/reference/user) is returned. | ✅ |
| `"workspace_icon"` | `string` | A URL to an image that can be used to display this authorization in the UI. |  |
| `"workspace_id"` | `string` | The ID of the workspace where this authorization took place. | ✅ |
| `"workspace_name"` | `string` | A human-readable name that can be used to display this authorization in the UI. |  |

### Token Request Failures

If something goes wrong when the integration attempts to exchange the `code` for an `access_token`, then the response contains a JSON-encoded body with an `"error"` field. Notion uses the common [error codes from the OAuth specification](https://datatracker.ietf.org/doc/html/rfc6749#section-5.2).

## Step 5: The Integration Stores the Access Token and Refresh Token for Future Requests

You need to set up a way for your integration to store both the `access_token` and `refresh_token` that it receives. The `access_token` is used to make authorized requests to the Notion API, and the `refresh_token` is used to generate a new `access_token`.

**Tips for Storing and Using Token Access**

- Setting up a database is a typical solution for storing access tokens. If you’re using a database, then build relations between an `access_token`, `refresh_token`, and the corresponding Notion resources that your integration accesses with that token. For example, if you store a Notion database or page ID, relate those records with the correct `access_token` that you use to authorize requests to read or write to that database or page, and the `refresh_token` for ongoing token lifecycle support.
- Store all of the information that your integration receives with the `access_token` and `refresh_token`. You never know when your UI or product requirements might change and you’ll need this data. It's really hard (or impossible) to send users to repeat the authorization flow to generate the information again.
- The `bot_id` returned along with your tokens should act as your primary key when storing information.

## Backwards Compatibility

When migrating an integration to use the new OAuth flow, keep the following in mind:

- When calling the Notion API directly, always include the `oauth_client_id` and `oauth_client_secret` in the request. This will ensure that the integration uses the correct credentials to authenticate and authorize its requests.
- When calling the Notion API through a library or SDK, ensure that the library or SDK supports OAuth 2.0. If it doesn't, consider using a different library or SDK that does support OAuth 2.0.
- When migrating an integration that uses the old OAuth flow, ensure that it is using the latest version of the Notion API and that it is using the correct credentials to authenticate and authorize its requests.
```

# What is authorization?

## Internal integration auth flow set-up

### Integration permissions

An integration has permissions, which determine what actions it can perform on behalf of Notion.

In your integration's settings, you can configure its permissions:

- **Read**: allows the integration to read data from Notion.
- **Write**: allows the integration to write data to Notion.
- **Full control**: allows the integration to perform all actions on a workspace.

### Making API requests with an internal integration

When an integration makes API requests, it uses its permissions to determine if the request is allowed. For example, if an integration has the Write permission, it can create, update, or delete a page.

Here’s an example of how an integration might make a GET request to the Workspace API:
```http
GET /workspace/12345678-9ABC-4DEF-5678-9ABCDEFB0123/workspace.json HTTP/1.1
Authorization: Bearer $ACCESS_TOKEN
```

And here’s an example of how an integration might make a POST request to the Page API:
```http
POST /workspace/12345678-9ABC-4DEF-5678-9ABCDEFB0123/pages -POST HTTP/1.1
Authorization: Bearer $ACCESS_TOKEN
Content-Type: application/json
```

## Public integration auth flow set-up

### How to make a public integration

To make a public integration, follow these steps:

1. **Navigate the user to the integration’s authorization URL**

   When a user visits the integration’s website, Notion redirects them to an authorization URL. This URL contains a code parameter, which the integration sends to Notion when making API requests.

2. **Notion redirects the user to the integration’s redirect URI and includes a `code` parameter**

   Notion receives the authorization code from the user and redirects them to the specified redirect URI. The redirect URL should be a secure location with appropriate access controls.

3. **Send the `code` in a `POST` request to the Notion API**

   The integration sends the authorization code to Notion in a `POST` request to the Notion API. This request includes the `code` parameter and an optional `state` parameter to ensure secure communication.

4. **Receive the `access_token`, `refresh_token`, and additional information**

   Notion responds to the `POST` request with an `access_token`, `refresh_token`, and additional metadata about the user and the integration.

5. **The integration stores the `access_token` and `refresh_token` for future requests**

   The integration stores the `access_token` and `refresh_token` received from Notion. Later, when making API requests, the integration uses these tokens to authenticate and authorize its operations.

6. **Refreshing an access token**

   To refresh an expired access token, follow these steps:

   1. Navigate the user to the integration’s authorization URL.
   2. Notion redirects the user to the integration’s redirect URI and includes a `code` parameter.
   3. Send the `code` in a `POST` request to the Notion API.
   4. Receive the refreshed `access_token` and new `refresh_token`.
   5. Store the new `access_token` and `refresh_token` in the integration’s configuration.

By following these steps, you can set up a successful public integration between Notion and your app or service.

---

**Updated 4 months ago**
```