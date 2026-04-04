# Source: https://planetscale.com/docs/api/reference/oauth.md

# OAuth

> Using PlanetScale OAuth enables your users to connect their accounts to PlanetScale.

## Overview

Creating an OAuth application within PlanetScale allows your application to access your users’ PlanetScale accounts.

With PlanetScale OAuth applications, you can choose what access your application needs, and a user will allow (or deny) your application those accesses on their PlanetScale account. The organization that you create the OAuth application in is the "owner" of the application.

## Getting started

### 1. Creating an OAuth application in PlanetScale

1. To create a new OAuth application, log into your organization and click **Settings > OAuth applications**.
2. Create a new OAuth application by clicking **Create new application**.
3. You will need to fill out the following fields:

* **Name**: A user-friendly name for your OAuth application.
* **Domain**: The full URL to your application's domain.
* **Redirect URI**: The full URL PlanetScale should redirect users on completion of the authorization flow, also known as the callback URL. It must have the same domain as the domain above.
* **Avatar**: An image that represents your OAuth application. (Optional but recommended.)

<Warning>
  You will also be agreeing, on behalf of your organization, to prominently display a privacy policy and obtain consent to your organization's terms of use from all users of your products and services.
</Warning>

### 2. Credentials to copy to your application code

Once you have created your OAuth application in PlanetScale, you will need the following credentials to use the OAuth authorization flow:

* **ID**: Your OAuth application's ID.
* **Client ID**: Your OAuth application's client ID.
* **Redirect URL**: The full URL PlanetScale should redirect users on completion of the authorization flow, also known as the callback URL.
* **Client secret**: Your OAuth application's client secret, used to exchange *access grants* for service tokens. (This will only be shown once, make sure to save it!)

Later in this document, we will go through how you use each of these credentials. We recommend saving them as environment variables.

### 3. OAuth application access scopes

Every OAuth application in PlanetScale will request from its users a specific set of permissions in the users' databases. We call these permissions "access scopes." They are broken into:

* User access
* Organization access
* Database access
* Branch access

Access is scoped to a resource. For example, selecting `write_branches` on an organization allows you to write branches across all databases in organizations the user gives permission to, while `write_branches` on a database enables you to only write branches in databases the user gives permission to.

The API reference for each endpoint will say what scope is needed.

In this step, select the access scopes you think your application will need on a user's account and click the **Save access scopes** button.

<Frame caption="This is only a partial list of the OAuth access scopes. For a full list of scopes, see the OAuth access scopes documentation.">
  <a href="/docs/api/reference/oauth-access-scopes">
    <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=1b1552118e5f4a3fa1ee4731c5cd19fb" alt="OAuth access scopes selection interface" data-og-width="1075" width="1075" data-og-height="893" height="893" data-path="docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=1eb76259611eb188489f77652598c55f 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=d5ef28c0b11d1100e2627e917811f413 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=2688c3f22c9e5db3b7a115b70d536404 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=f87dd4ccb484aa72e8a3602aedde8937 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b7ef6e925aab9cb3f3d502dbf6ea288c 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/31ea0ef-CleanShot_2024-02-01_at_15.32.27.jpg?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=3271bedac3736ad0eed765875d0db16c 2500w" />

    <span className="sr-only">View OAuth access scopes documentation</span>
  </a>
</Frame>

## OAuth Authorization Flow

PlanetScale's OAuth implementation supports the [Authorization Code grant type](https://oauth.net/2/grant-types/authorization-code/). The following diagram walks through the flow.

<Frame caption="OAuth authorization flow diagram">
  <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=af734aec19f3da002b77cb6a561b4485" alt="OAuth authorization flow diagram" data-og-width="2000" width="2000" data-og-height="1321" height="1321" data-path="docs/images/reference/c46b041-oauth_diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ad8f2e1e7b8886a96b93850255c9e3ca 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=6d6b73206c39d80e0cda34dbc9b48934 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=afa4c8c62431393d44171afdee3a62a4 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=18f2167435e9430288533aadc1dfeb3b 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=8dc62c4c8d7ad43a9035669ed5285cd3 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/c46b041-oauth_diagram.png?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=a7137c6b769a5a1085d0c585273309b1 2500w" />
</Frame>

### 0. Prerequisites

You must have [created a service token](/docs/api/reference/service-tokens) in your OAuth application's organization.

Copy and paste the ID and service token into your code, where the rest of your important credentials are stored.

A service token is needed to use the PlanetScale API to create OAuth tokens as a part of the OAuth authorization flow. You will need the following organization-level accesses on the service token in order to complete the flow: `read_oauth_applications`, `write_oauth_tokens`, `read_oauth_tokens`.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=ba4bfc9acde96505e0f6033a8fd7f529" alt="Shows the read_oauth_applications, write_oauth_tokens, read_oauth_tokens scopes selected." data-og-width="644" width="644" data-og-height="504" height="504" data-path="docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=280&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=213fb94f3b80dc95938ab3c0a6d84c4c 280w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=560&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=95aa170974763e1d335372793a28fd93 560w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=840&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=eab7cac792f05293885c23ce4d027464 840w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=1100&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=b69ac5bbdcee567db1df54143940a595 1100w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=1650&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=5854f20ea18280aab61ea22502fd0d31 1650w, https://mintcdn.com/planetscale-cad1a68a/bmpntbyCIjsL6T87/docs/images/reference/e3a5f65-CleanShot_2024-02-01_at_15.43.31.jpg?w=2500&fit=max&auto=format&n=bmpntbyCIjsL6T87&q=85&s=536f86901690369fffad4fe5fc0ad9cc 2500w" />
</Frame>

### 1. User authorizes your OAuth application on their account

Your application should direct your users to the PlanetScale authorization page (see URL below) so that they can grant your application access to their PlanetScale account:

<CodeGroup>
  ```text Text theme={null}
  http://app.planetscale.com/oauth/authorize?client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&state=STATE
  ```
</CodeGroup>

### Query parameters:

| Name               | Type   | Description                                                                                                                                                                                                            |
| :----------------- | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`        | string | Your OAuth application's client id                                                                                                                                                                                     |
| `redirect_uri`     | string | The full URL PlanetScale should redirect users on completion of the authorization flow, also known as the callback URL.                                                                                                |
| `state` (optional) | string | You may also optionally pass a state parameter, which exists to prevent third-party attacks. Pass a random string, and PlanetScale will return it in step 2. Compare to ensure the request came from your application. |

## 2. The authorization code returns to your application

Upon authorization, PlanetScale will redirect the user to your `redirect_uri` with an authorization code in the query parameters. The authorization code is only good for one use. It will look like the following URL:

```
https://my-redirect-uri.com?code=AUTHORIZATION_CODE&state=STATE
```

### Query parameters:

| Name                          | Type   | Description                                                                                                                                              |
| :---------------------------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `code`                        | string | An authorization code to be exchanged for an access token.                                                                                               |
| `state` (if you provided one) | string | Compare with the original `state` parameter to ensure they match. Abort the process if they do not because the request may have come from a third party. |

### 3a. Exchange authorization code for an OAuth token

Your application can now exchange the authorization code for an access token.

**POST**

```
https://api.planetscale.com/v1/organizations/:organization_name/oauth-applications/:application_id/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&code=CODE&grant_type=authorization_code&redirect_uri=REDIRECT_URI
```

The `POST` request will need the following:

### Headers:

`Authorization: <SERVICE_TOKEN_ID>:<SERVICE_TOKEN>`

### Path parameters:

| Name                | Type   | Description                                         |
| :------------------ | :----- | :-------------------------------------------------- |
| `organization_name` | string | Your organization name.                             |
| `application_id`    | string | Your OAuth application's ID (12 character long ID). |

### Query parameters:

| Name            | Type   | Description                                                                                                             |
| :-------------- | :----- | :---------------------------------------------------------------------------------------------------------------------- |
| `client_id`     | string | Your OAuth application's client ID.                                                                                     |
| `client_secret` | string | Your OAuth application's client secret.                                                                                 |
| `code`          | string | The code located in the query parameters of the previous step.                                                          |
| `grant_type`    | string | Set to `authorization_code`.                                                                                            |
| `redirect_uri`  | string | The full URL PlanetScale should redirect users on completion of the authorization flow, also known as the callback URL. |

The response will look similar to the following:

<CodeGroup>
  ```json JSON theme={null}
  {
    "id": "cv4d3zi653gv",
    "type": "ServiceToken",
    "display_name": "My OAuth App's Service Token cv4d3zi653gv",
    "avatar_url": "https://my-oauth-app.com/avatar.png",
    "created_at": "2022-08-01T20:19:41.886Z",
    "updated_at": "2022-08-01T20:19:41.886Z",
    "expires_at": "2022-09-01T20:19:41.887Z",
    "last_used_at": null,
    "name": "my-oauth-app",
    "token": "pscale_tkn_O4KbFjH97uOz2bLWJtQXjYgDsqkGgC8bNNlrzgo6YUY",
    "plain_text_refresh_token": "pscale_tkn_W_zjmZ1a14sczj15bxJdsW_kiv063OrHG4CBh0IXR9M",
    "actor_id": "r80q66antldo",
    "actor_display_name": "[email protected]",
    "actor_type": "User",
    "service_token_accesses": [...]
  }
  ```
</CodeGroup>

The three most essential credentials in the response are:

* `id`: Your access token's ID.
* `token`: Your access token.
* `plain_text_refresh_token`: A refresh token that can refresh your access token when it expires. See step 3b for more info.

You will need both the `id` and `token` to make API calls on behalf of the user.

### 3b. Refreshing an OAuth token

When an OAuth token expires, you can refresh it:

**POST**

```
https://api.planetscale.com/v1/organizations/:organization_name/oauth-applications/:application_id/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=refresh_token&refresh_token=REFRESH_TOKEN
```

The `POST` request will need the following:

### Headers:

`Authorization: <SERVICE_TOKEN_ID>:<SERVICE_TOKEN>`

#### Path parameters:

| Name                | Type   | Description                  |
| :------------------ | :----- | :--------------------------- |
| `organization_name` | string | Your organization name.      |
| `application_id`    | string | Your OAuth application's ID. |

#### Query parameters:

| Name            | Type   | Description                                                      |
| :-------------- | :----- | :--------------------------------------------------------------- |
| `client_id`     | string | Your OAuth application's client ID.                              |
| `client_secret` | string | Your OAuth application's client secret.                          |
| `refresh_token` | string | The refresh token sent in the initial token response in step 3a. |
| `grant_type`    | string | Set to `refresh_token`.                                          |

The response will look similar to the response in 3a.

### 4. Using the OAuth token

Now your application can make requests to the PlanetScale API on behalf of the user. To make requests to the API, add the `id` and `token` in the `Authorization` header in your HTTP API request using the following format:

<CodeGroup>
  ```text Text theme={null}
  Authorization: <OAUTH_TOKEN_ID>:<OAUTH_TOKEN>
  ```
</CodeGroup>

Now your application can make requests to the PlanetScale API on behalf of the user. To make requests to the API, add the `id` and `token` in the `Authorization` header in your HTTP API request using the following format:

<CodeGroup>
  ```text Text theme={null}
  Authorization: <OAUTH_TOKEN_ID>:<OAUTH_TOKEN>
  ```
</CodeGroup>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt