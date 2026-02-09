# Source: https://smartcar.com/docs/getting-started/how-to/get-an-access-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Get an API Access Token

> Learn how to obtain your first Smartcar API access token by exchanging an authorization code.

To make requests to the Smartcar API, you first need to obtain an access token. This guide walks you through the process of getting the authorization code and exchanging it for an access token for the first time.

<Steps>
  <Step title="1. Launch Smartcar Connect">
    Direct your user to the Smartcar Connect URL. The user will:

    * Select their vehicle brand
    * Log in with their connected services account
    * Approve the requested permissions

    After successful authorization, Smartcar will redirect the user to your application's `redirect_uri` with an authorization `code` as a query parameter.
  </Step>

  <Step title="2. Handle the Redirect and Extract the Code">
    Your application should listen for requests to the `redirect_uri`. When Smartcar redirects the user, extract the `code` parameter from the query string.
    <b>Example redirect:</b>

    ```
    https://your-app.com/callback?code=AUTH_CODE&state=STATE
    ```
  </Step>

  <Step title="3. Exchange the Code for an Access Token">
    Use the authorization code to request an access token and refresh token from [Smartcar’s OAuth token endpoint](/api-reference/authorization/auth-code-exchange).

    Here is an example using the Smartcar Node.js SDK:

    ```javascript  theme={null}
    const smartcar = require('smartcar'); //Smartcar backend Node SDK

    smartcar.OAuth.getToken({
      client_id: 'YOUR_CLIENT_ID',
      client_secret: 'YOUR_CLIENT_SECRET',
      grant_type: 'authorization_code',
      code: 'AUTH_CODE', //extracted from the URL query parameter
      redirect_uri: 'YOUR_REDIRECT_URI'
    });
    ```

    The response will include an `access_token`, an `expires_in` field, and a `refresh_token`. Store these securely in your backend database.
    The `access_token` expires after two hours, and the `refresh_token` expires after 60 days.
  </Step>
</Steps>

***

## What’s Next

* [How to Manage API Tokens](/getting-started/how-to/manage-api-tokens)
* [Refreshing API Access Tokens](/api-reference/authorization/refreshing-access-token)
