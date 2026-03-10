# Source: https://developers.webflow.com/data/reference/rest-introduction/quick-start.mdx

***

title: Getting Started
hidden: false
'og:title': 'Getting Started with Webflow Apps: Data Clients'
'og:description': >-
A quick guide to help you set up an App and start making request to Webflow's
REST API
--------

In this guide, you'll create your first Data Client app to authorize with Webflow and make your first request to the Webflow REST API.

#### Before you start

To successfully follow along with this guide, make sure you have the following:

* A Webflow site for development and testing
  -[A registered app on your Workspace](/data/docs/register-an-app) with the `sites:read` scope enabled
* An IDE of your choice
* Node.js installed on your machine.

<br />

## Quick Start (5 minutes)

This quick start will get you up and running with a data client app

<Steps>
  ### Clone the starter app

  ```bash
  git clone https://github.com/Webflow-Examples/webflow-app-starter-v2
  cd webflow-app-starter-v2
  npm install
  ```

  ### Add your credentials to `.env`

  Navigate to your Workspace settings in the Webflow dashboard and find your Client ID and Secret in the Apps & Integrations -> App Development section. Replace the placeholder values in the `.env.example` file with your own Client ID and Secret. Then save the file as `.env`.

  ```env
  WEBFLOW_CLIENT_ID=your_client_id
  WEBFLOW_SECRET=your_client_secret
  ```

  ### Start the server

  ```bash
  npm run dev
  ```

  ### Update your redirect URI

  In your workspace settings, navigate to the app development section and your app's details, update the redirect URI to `http://localhost:3000/auth`

  <Frame>
    ![Redirect URI](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/69e85591af4d8656da1d69e8c57622c2ef69bd6d1e70a235a7e89d803df62671/products/data/pages/Apps/data-clients/getting-started-data-clients/redirect-uri.png)
  </Frame>

  ### Visit your app

  Visit `http://localhost:3000` (or the port of your choice)and click "Connect with Webflow" to see your Webflow sites!
  <Frame>![Webflow App Example](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/b6bdd02fce8f20d398ead866ebee2aa4cdc6779393013cedff5ff2bef9ec74bf/products/data/pages/Apps/data-clients/getting-started-data-clients/new-user.png)</Frame>
</Steps>

## Understanding the example

[This example](https://github.com/Webflow-Examples/webflow-app-starter-v2) is a simple Node.js app that handles authorization and makes a single request to the Webflow REST API.

Review the code in `server.js`to understand how the App works.

<Accordion title="Installation and configuration">
  The app uses [Fastify](https://www.fastify.io/) to create a lightweight server, [Level](https://github.com/Level/level) as a database, and the [Webflow JavaScript SDK](https://www.npmjs.com/package/webflow-api) to make authenticated requests to the Webflow REST API. To keep things simple, the frontend of the app is built with vanilla JavaScript and CSS, with a simple HTML file served from the `public` directory.

  In the beginning of `server.js`, imports the necessary dependencies, loads environment variables, and initializes the Fastify server. Here, security headers are added to the server to protect against common web vulnerabilities. Also, it initializes the database for storing access tokens.

  ```javascript title="server.js" maxLines=10
  import { WebflowClient } from "webflow-api";
  import Fastify from "fastify";
  import fastifyStatic from "@fastify/static";
  import path from "path";
  import url from "url";
  import { Level } from "level";
  import fs from "fs/promises";

  // Load environment variables from .env file
  const {
  WEBFLOW_CLIENT_ID,
  WEBFLOW_SECRET,
  PORT
  NODE_ENV = "development",
  } = process.env;

  // Validate required environment variables
  if (!WEBFLOW_CLIENT_ID || !WEBFLOW_SECRET) {
  console.error(
     "Missing required environment variables. Please check your .env file:"
  );
  console.error("WEBFLOW_CLIENT_ID and WEBFLOW_SECRET are required");
  process.exit(1);
  }

  // Initialize our server with basic security headers
  const server = Fastify({
  logger: true,
  trustProxy: true, // Required for secure cookies behind a proxy
  });

  // Add security headers
  server.addHook("onSend", async (request, reply) => {
  reply.headers({
     "X-Content-Type-Options": "nosniff", // Prevent MIME type sniffing
     "X-Frame-Options": "DENY", // Prevent clickjacking
     "Strict-Transport-Security": "max-age=31536000; includeSubDomains", // Enforce HTTPS
  });
  });

  // Initialize the database (Note: Use a proper database in production)
  const db = new Level("data", { valueEncoding: "json" });
  await db.open();
  ```
</Accordion>

<Accordion title="OAuth Authentication">
  The App implements OAuth 2.0 authentication through a dedicated `/auth` route that handles both initiating the authorization flow and processing Webflow's callback response. When a user clicks "Connect with Webflow", this route first redirects them to Webflow's authorization page. After the user grants permission, Webflow redirects back to this route with an authorization code that the App exchanges for an access token.

  For a comprehensive walkthrough of implementing OAuth 2.0 authentication in your App, refer to the detailed [OAuth 2.0 guide](/data/reference/oauth-app).

  #### Start the OAuth 2.0 authorization flow

  This route will check for a `code` query parameter. If the code isn't present, Webflow will redirect the user to the Webflow OAuth 2.0 authorization page using the `authorizeURL` method of the Webflow JavaScript SDK.

  ```javascript server.js
  // OAuth 2.0 authentication endpoint
  server.get("/auth", async (req, reply) => {
    const { code, error, error_description } = req.query;

    // If no code is provided, redirect to the authorization URL
    if (!code) {
      const installUrl = WebflowClient.authorizeURL({
        scope: scopes,
        clientId: WEBFLOW_CLIENT_ID,
        // Optional: Add state parameter for CSRF protection
        state: Math.random().toString(36).substring(7),
      });
      return reply.redirect(installUrl);
    }
  });
  ```

  #### Request an access token

  If the `code` query parameter is present, we'll use it to request an access token from Webflow using the `getAccessToken` method of the Webflow JavaScript SDK. We'll also store the access token in the database and redirect the user to the root URL of the App.

  ```javascript server.js
  // OAuth 2.0 authentication endpoint
  server.get("/auth", async (req, reply) => {

  // Previous Code //

    try {
      // Exchange the code for an access token
      const token = await WebflowClient.getAccessToken({
        clientId: WEBFLOW_CLIENT_ID,
        clientSecret: WEBFLOW_SECRET,
        code: code,
      });

      // Store the token in the database
      await db.put("token", token);

      if (NODE_ENV === "development") {
        console.log("\nAccess Token Received:", token, "\n");
      }

      return reply.redirect("/?authorized=true");
    } catch (error) {
      console.error("Auth Error:", error);
      return reply.code(500).send({
        error: "Authentication failed",
        message: error.message,
      });
    }
  });
  ```

  <Warning>
    The example App stores and retrieves a single access token directly in the Level database. In a production app, you'll want to implement proper user management and token storage, including:

    * Storing tokens securely per user/workspace
    * Encrypting sensitive data
    * Using secure session management

    Consider using dedicated auth services or implementing these security measures using libraries like Passport.js, JWT tokens, and proper database encryption.
  </Warning>
</Accordion>

<Accordion title="Making requests to the REST API">
  After the user has authorized the App, it can make requests to the REST API using the `WebflowClient` object. Here, the `/sites` route makes a request to the "[List Sites](https://developers.webflow.com/data/reference/sites/list)" endpoint.

  Before calling the API, the App retrieves the access token from the database and creates a new, authenticated `WebflowClient` object.

  ```javascript server.js
  // Example API endpoint
  server.get("/sites", async (req, reply) => {
    try {
      const accessToken = await db.get("token");

      const webflow = new WebflowClient({ accessToken });

      const sites = await webflow.sites.list();
      return sites;

    } catch (error) {
      console.error("API Error:", error);

      // Handle different types of errors
      if (error.response?.status === 401) {
        return reply.code(401).send({
          error: "Invalid token",
          message: "Please authenticate again",
        });
      }

      return reply.code(500).send({
        error: "Server error",
        message: "Failed to fetch sites",
      });
    }
  });
  ```
</Accordion>

## Next Steps

Now that you have a working app, you can:

{/* <!-- vale off --> */}

1. **Add more API endpoints**: Explore the [API Reference](/data/reference) and the [Data Client Guides](/data/docs/data-clients) to add functionality
2. **Add Designer Extension capabilities**: Learn how to [add Designer Extension capabilities](/designer/docs/getting-started-designer-extensions) to your App.
3. **Authenticate a Hybrid App**: [Learn how to implement authentication](/apps/docs/authenticating-users-with-id-tokens) for Apps using Data Client and Designer Extension capabilities.
4. **Prepare your Marketplace app**: Learn how to [prepare your App for submission to the Webflow Marketplace](/apps/docs/marketplace/submitting-your-app)

{/* <!-- vale on --> */}

### FAQs

<Accordion title="Why can't other users install my app on their sites?">
  Only apps published to the Webflow Marketplace, either [publicly](/apps/docs/marketplace/submitting-your-app) or [privately](/apps/docs/private-apps), can be installed by other users. Submit your app for review to make it available for installation.

  **Want to test with a few users before publishing?**
  Email [developers@webflow.com](mailto:developers@webflow.com) with up to **5** Webflow user emails. Our team can add them to a test group so they can install and use your app with the [install URL](/apps/docs/marketplace/submitting-your-app#installation-configuration).
</Accordion>
