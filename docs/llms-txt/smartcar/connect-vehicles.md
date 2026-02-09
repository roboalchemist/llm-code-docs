# Source: https://smartcar.com/docs/getting-started/connect-vehicles.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Vehicles

> Learn how to connect vehicles to your Smartcar application using Smartcar Connect.

Smartcar Connect is the starting point for connecting vehicles to your application. It uses Smartcar's patented and secure [OAuth 2.0](https://oauth.net/2/) flow to let vehicle owners grant your app access to their car data and control features.

### Prerequisites

Before you begin, make sure you have [configured](/getting-started/configure-application) your Smartcar application in the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration). You will need:

* Your application's `Client ID` and `Client Secret`
* A valid `redirect_uri` for your application
* The vehicle data you want to access (e.g., odometer, location, etc.)

<Steps>
  <Step title="Step 1: Launch Smartcar Connect">
    Direct your users to the Smartcar Connect URL. This can be done using the Smartcar SDK for your platform (web, iOS, or Android) or copying the URL from the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration). The user will:

    * Select their vehicle brand
    * Log in with their connected services account
    * Review and approve the requested permissions
  </Step>

  <Step title="Step 2: Handle the Redirect and Get the Authorization Code">
    After the user authorizes access, Smartcar will redirect them back to your application using the default `redirect_uri` you provided in your app configuration. The redirect will include an authorization `code` as a query parameter.
  </Step>

  <Step title="Step 3: Exchange the Code for an Access Token">
    Your backend exchanges the authorization code for an access token and refresh token by making a request to [Smartcar’s token endpoint](/api-reference/authorization/auth-code-exchange). You’ll need your app’s `client_id`, `client_secret`, and the same `redirect_uri`.

    ```
    POST https://auth.smartcar.com/oauth/token
    Content-Type: application/x-www-form-urlencoded

    client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&code=AUTH_CODE&redirect_uri=YOUR_REDIRECT_URI
    ```

    The response will include an `access_token` and a `refresh_token`.
  </Step>

  <Step title="Step 4: Store Tokens">
    Store the `access_token` and `refresh_token` securely in your application's database. These tokens are sensitive credentials that allow access to vehicle data and actions, so:

    * Use encrypted storage or a secrets manager whenever possible.
    * Never log tokens or expose them in client-side code.
    * Associate tokens with the correct user and vehicle in your database for easy lookup and management. Here is a [recommended architecture structure](/getting-started/how-to/architecture-design).
    * The `access_token` expires after two hours. You will need to use the `refresh_token` to obtain new access tokens when needed. The `refresh_token` expires after 60 days. If the `refresh_token` expires, the user will need to reauthorize your application.
  </Step>
</Steps>

<Info>
  Vehicle owners may occasionally need to re-authenticate due to OEM platform migrations, credential changes, or permission updates. Build your integration to handle these scenarios gracefully. See [Handle Re-authentication](/connect/re-auth/oem-migrations) for implementation guidance.
</Info>

## What’s Next

* [Build your first integration](/getting-started/integration-overview).
* [See more about Smartcar Connect](/connect/what-is-connect)
* [Explore available API endpoints](/api-reference)
* [Learn about permissions and scopes](/api-reference/permissions)
