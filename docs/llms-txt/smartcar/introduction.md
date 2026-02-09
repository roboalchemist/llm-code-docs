# Source: https://smartcar.com/docs/getting-started/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with Smartcar

> Welcome to Smartcar's Developer Documentation! Here, you'll learn how to integrate your application with over 40 OEM brands, securely connect to vehicles, and receive the dynamic vehicle data you need, delivered directly to your systems.

<CardGroup cols={3}>
  <Card title="Start a tutorial" icon="play" href="/getting-started/tutorials/ios" icontype="duotone">Learn how to configure your first application and connect a vehicle in under 10 minutes.</Card>
  <Card title="Browse Available Data" href="/api-reference/signals/schema" icon="database" icontype="duotone">Explore the complete catalog of vehicle data points (signals) you can access.</Card>
  <Card title="Read How-To Guides" href="/getting-started/how-to/configure-permissions" icon="graduation-cap" icontype="duotone">Solve common implementation challenges with step-by-step instructions.</Card>

  <Card title="Connecting Vehicles" href="/getting-started/connect-vehicles" icon="mobile" icontype="duotone">
    Learn how to use our patented consent management authorization flow, to connect vehicles to your application.
  </Card>

  <Card title="Help Center" href="/help/what-is-smartcar" icon="life-ring" icontype="duotone">
    Visit our Help Center for FAQs, troubleshooting tips, and to contact support.
  </Card>

  <Card title="Integrations" href="/getting-started/integration-overview" icon="square-terminal" icontype="duotone">Dive deep into our Smartcar integrations and learn how to connect with various services.</Card>
  <Card title="Browse our SDKs" href="/connect/connect-sdks" icon="computer" icontype="duotone">Connect with other developers, share ideas, and get help.</Card>
</CardGroup>

Learn how to connect your app to Smartcar so you can access [vehicle data signals](/api-reference/signals/schema) like odometer, location, battery level, issue vehicle commands, and more. In this guide, you'll register your app, walk through the Smartcar Connect flow, and configure a webhook to receive data.

By the end of this guide, you’ll have a working setup with access to a vehicle’s data through Smartcar’s platform.

## Prerequisites

Before you begin, you’ll need:

* A [Smartcar Account](https://dashboard.smartcar.com)
* Your Application ID and Secret (found in the [Smartcar Dashboard](https://dashboard.smartcar.com/configuration))
* An application with a redirect URI (e.g. a local development server or staging environment)

<Steps>
  <Step title="Step 1: Register & Configure Your Application">
    1. Log in or sign up via the [Smartcar Dashboard](https://dashboard.smartcar.com)
    2. Fill in your app name, description, and redirect URI in the configuration page of the dashboard.
    3. Copy your `Client ID` and `Client Secret` in a safe location. These credentials identify your app during the authorization process. **Do not commit your client secret to version control**.
    4. Select the data you want to access from vehicles by choosing the data signals (e.g. `odometer`, `location`, etc.).

    The necessary permissions will be derived from these signals and presented to your users.
  </Step>

  <Step title="Step 2: Start Connecting Vehicles via Smartcar Connect">
    [Smartcar Connect](/connect) is an OAuth 2.0 consent flow that lets your users link their vehicles securely.

    The vehicle access tab in the Smartcar Dashboard will generate a Connect URL for you. You can also generate the URL programmatically using one of our SDKs.

    ```javascript  theme={null}

    const link = new Smartcar.AuthClient({ //Smartcar frontend SDK
      clientId: 'YOUR_CLIENT_ID',
      redirectUri: 'YOUR_REDIRECT_URI',
      scope: ['read_vehicle_info', 'read_odometer'], // add other scopes as needed
      mode: 'live', // use 'simulated' for testing with simulated vehicles
    });

    window.location.href = link.getAuthUrl();
    ```

    This will take your user to the Smartcar Connect screen to authorize access.
  </Step>

  <Step title="Step 3: Exchange Authorization Code for Access Tokens">
    After the user grants access, Smartcar redirects back to your app with an authorization code. This is where the redirect URI you configured earlier comes into play.

    Use this code in your backend to exchange for access and refresh tokens:

    ```javascript  theme={null}
    const smartcar = require('smartcar'); //Smartcar backend SDK

    const client = new smartcar.AuthClient({
      clientId: 'YOUR_CLIENT_ID',
      clientSecret: 'YOUR_CLIENT_SECRET',
      redirectUri: 'YOUR_REDIRECT_URI',
      mode: 'live', //use 'simulated' for testing with simulated vehicles
    });

    const access = await client.exchangeCode('AUTHORIZATION_CODE_FROM_QUERY');

    ```

    You’ll receive:

    * `accessToken`: used to make API calls
    * `refreshToken`: used to obtain new access tokens
  </Step>

  <Step title="Step 4: Configure an Integration To Receive Vehicle Data">
    Our recommended method is to use webhooks, allowing you to choose triggers (e.g. location changes, battery state of charge changes) and the data to be sent upon those triggers.

    **Quick Start**: Deploy a production-ready webhook receiver in minutes with our [Webhook Receiver Recipe](/getting-started/tutorials/webhook-receiver-recipe) - a complete AWS serverless solution.
  </Step>
</Steps>

#### What’s Next?

* [Learn how to configure your application](/getting-started/configure-application).
* [Connect your first vehicle](/getting-started/connect-vehicles).
* [Build your first integration](/getting-started/integration-overview).

Need help? Visit our Support Portal or contact us at [support@smartcar.com](mailto:support@smartcar.com).

Let’s get building!
