# Source: https://render.com/docs/deploy-shopify-app.md

# Deploy a Shopify App

You can deploy a custom [Shopify app](https://shopify.dev/docs/apps/getting-started) to Render to extend Shopify's core capabilities for Shopify store owners. A Shopify app might add features to an existing Shopify store, introduce new admin functionality, or pull in Shopify merchant data for processing and analysis.

## Getting started

You can clone our [example repository](https://github.com/render-examples/render-shopify-example) if you already have your Shopify API and secret values, and you know which scopes you want to use. Otherwise, follow the steps below to create a new Shopify app and deploy it to Render.

## Create your project with the Shopify CLI

Following the steps in [Shopify's App tutorial](https://shopify.dev/docs/apps/getting-started/create), let's create a new app from your terminal using the Shopify CLI. Note that the steps differ slightly depending on whether you're building an "app" or an "extension", so make sure to create the right project for your use case. The process to deploy to Render is similar in either case.

> Before you begin these steps, make sure you have recent versions of Node.js and npm installed on your system. [See additional requirements](https://shopify.dev/docs/apps/tools/cli#requirements).

1. Run `npm init @shopify/app@latest`

   This prompts you for an app name, asks whether you want to use Remix (recommended), and asks whether to use JavaScript or TypeScript. A folder is created with the name you provide, and the app is initialized in that folder. If you choose not to use Remix, you will need additional environment setup discussed later in the tutorial.

   The final output should show you that the process succeeded:

   ```bash
   ╭─ success ──────────────────────────────────────────────────────────────╮
   │                                                                        │
   │  render-sample-app is ready for you to build!                          │
   │                                                                        │
   │  Next steps                                                            │
   │    • Run `cd render-sample-app`                                        │
   │    • For extensions, run `npm run generate extension`                  │
   │    • To see your app, run `npm run dev`                                │
   │                                                                        │
   │  Reference                                                             │
   │    • Shopify docs                                                      │
   │    • For an overview of commands, run `npm run shopify app -- --help`  │
   │                                                                        │
   ╰────────────────────────────────────────────────────────────────────────╯
   ```

2. Change into the new project folder, and run `npm run dev` to continue building the app. (If you're building an extension, use `npm run generate extension` instead.)

   This command creates a local SQLite database, along with its database migration schema.

   The command _also_ prompts you to associate the project with a registered Shopify app and creates a "development store" that you will need later on. You can choose to either create a new app or associate the project with an existing app (Shopify displays a list of your existing apps). This step may require authentication to Shopify.

> *Pay close attention to the terminal output as you go through these steps.* It provides helpful information about accessing your application, resetting your database, and more.

   ```bash
   ╭─ info ─────────────────────────────────────────────────────────────────────╮
   │                                                                            │
   │  Using shopify.app.toml:                                                   │
   │                                                                            │
   │    • Org:             Render Sample App                                    │
   │    • App:             render-test-walkthrough                              │
   │    • Dev store:       render-example-app.myshopify.com                     │
   │    • Update URLs:     Not yet configured                                   │
   │                                                                            │
   │   You can pass `--reset` to your command to reset your app configuration.  │
   │                                                                            │
   ╰────────────────────────────────────────────────────────────────────────────╯
   ```

> Note the value of your `Dev store` for use in a later step.

3. Once the app is running in development mode, press `p` in the terminal prompt to open the app in your browser, and install it to your test store. If this succeeds, you can press `q` to quit the development mode runtime and continue.

> *Your Shopify app uses a local SQLite database by default.* On Render, locally stored files are lost with each deploy of your service. We strongly recommend that you configure your app to use PostgreSQL instead. Learn how to [set up PostgreSQL on Render](postgresql-creating-connecting), and see the [Shopify CLI docs](https://shopify.dev/apps/tools/cli) for more information on connecting to a dedicated database.

4. Fetch your Shopify API details and scopes using `npm run shopify app env show`.

   This outputs a few lines of text showing you your `SHOPIFY_API_KEY`, `SHOPIFY_API_SECRET`, and `SCOPES` variables. You'll need to add these values to your Render service for it to connect to Shopify successfully.

## Prepare your Render deployment

1. Commit your code and push it to a repository on GitHub/GitLab/Bitbucket. You'll connect this repo to your Render service.
2. In the [Render Dashboard](https://dashboard.render.com), click *New > Web Service*.
3. In the service creation flow, connect your project's Git repository and give the service a name such as `shopify-example-app`
   - Render assigns your web service an `onrender.com` subdomain based on its name (e.g., a name of "Shopify Example App" might produce `https://shopify-example-app.onrender.com`). *You will need this URL later.*
4. Set the service's *Language* field to `Docker` and choose an instance type (such as Free or Starter).
5. Add the following environment settings to your service:
   | Variable Name | Value |
   | -------- | ----- |
   | `SHOPIFY_API_KEY` | Obtain by running `npm run shopify app env show` |
   | `SHOPIFY_API_SECRET` | Obtain by running `npm run shopify app env show` |
   | `SCOPES` | Obtain by running `npm run shopify app env show` |
   | `SHOPIFY_APP_URL` | Use the Render web service's URL from above (e.g., `https://shopify-example-app.onrender.com`) for Remix-based applications
   | `HOST` | Set to the same fully-qualified domain name (FQDN) as the `SHOPIFY_APP_URL` above, but only for non-Remix based applications |
   | `NODE_ENV` | Set this to `production`. |

6. Click *Create Web Service*.

Render kicks off your service's first deploy.

You're all done on the Render side! Your Docker container successfully deploys on Render within a few minutes. From your service's page in the Render Dashboard, click its `onrender.com` URL to view the running app. As you continue to build, you can push updates to your GitHub/GitLab/Bitbucket repository, and Render will automatically redeploy your service with the updated code.

Note your app's URL (such as `https://shopify-example-app.onrender.com/`), because you'll need it to configure your Shopify app below.

## Finish configuration in Shopify

There are two proposed ways of finishing your Shopify application setup which includes setting up callback URLs. The first method described below will modify a configuration file and deploy using the Shopify CLI. The second method will be done directly in the Shopify developer portal.

### Method 1: Local configuration and deployment using Shopify CLI

When you created the Shopify application using the Shopify CLI tool, a configuration file named `shopify.app.toml` was created in your project's root directory. This file contains the necessary URL configurations to change.

1. Look for the line that contains `application_url` and change it to your Render service's `onrender.com` URL. For example, if your service's URL is `https://shopify-example-app.onrender.com`, the line should look like this:

   ```toml
   application_url = "https://shopify-example-app.onrender.com"
   ```

2. Next, under the `[auth]` section in the configuration file, find the `redirect_urls` list and change the callback URLs to match your Render service's URL. For example:

   ```toml
   redirect_urls = [
       "https://shopify-example-app.onrender.com/auth/callback",
       "https://shopify-example-app.onrender.com/auth/shopify/callback",
       "https://shopify-example-app.onrender.com/api/auth/callback"
   ]
   ```

3. Save the file and run `shopify app deploy` to deploy your app to Shopify. You should see a confirmation that shows the changes in the `application_url` and `auth` sections. Confirm the changes.

   ```bash
   ╭─ info ───────────────────────────────────────────────────────────────────────────────────────────────╮
   │                                                                                                      │
   │  Using shopify.app.toml:                                                                             │
   │                                                                                                      │
   │    • Org:             Render Example                                                                 │
   │    • App:             shopify-example-app                                                            │
   │    • Include config:  Yes                                                                            │
   │                                                                                                      │
   │   You can pass `--reset` to your command to reset your app configuration.                            │
   │                                                                                                      │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────╯

   ?  Release a new version of render-test?

   ┃  Configuration:
   ┃  • application_url (updated)
   ┃  • auth (updated)
   ┃  • name
   ┃  • handle
   ┃  • access_scopes
   ┃  • webhooks
   ┃  • pos
   ┃  • embedded
   ┃
   ┃  Extensions:
   ┃  None

   (y) Yes, release this new version
   (n) No, cancel
   ```

You can confirm these changes were applied by logging into the Shopify developer portal, selecting your app, selecting the latest version, and checking the URLs displayed on the screen.

### Method 2: Direct configuration in Shopify developer portal

If you're more comfortable making these changes directly in the Shopify developer portal, you can do so instead.

Log in to your [Shopify developer portal](https://shopify.dev/) and open your *partner account page* (it has a URL like `https://partners.shopify.com/12345`). You'll perform a few different actions here to finish setting up your app.

### Add callbacks to your Shopify app

From your partner account page, click *Apps* in the left menu and select the app you created with the Shopify CLI.

Click *Configuration* in the left menu and find the *URLs* section.

In this section, do the following:

1. Provide your Render service's `onrender.com` URL in the *App URL* field.
2. In the *Allowed redirection URL(s)* field, add three entries that each start with your Render service's `onrender.com` URL and end with the following paths:

   - `/auth/callback` (eg, `https://shopify-example-app.onrender.com/auth/callback`)
   - `/auth/shopify/callback`
   - `/api/auth/callback`

   When you're done, the URLs section should look like this:

   [image: Setting up Shopify callback URLs]

3. Click *Save and release* at the top of the page.

## Configure your development store

> If you have already followed the step-by-step instructions above, you will have already created a development store and installed your app within that store and do not need any further configuration.

If you have not already installed your app on a development store, or if you want to install your application on a different development store, you will need to follow the steps below.

First, we need to choose and configure a store to use your deployed Render application.

1. From your partner account page, click *Stores* in the left menu and choose one of your stores.
2. Verify whether your app has already been installed in your store.
3. Click *Apps* in the left menu and select the app you created with the Shopify CLI.
4. You'll see a panel that says *Test your app*. Click *Select store*, hover over your development store, and click *Install app*.

   [image: Installing the app on your development store]

5. You may be prompted to verify some settings. Click *Install* to continue.
6. You're redirected to the store's admin page, which displays the following:

   [image: Congratulations, your Shopify app is working]

   This indicates that your app is working as expected.

> If your Render service is running on the Free instance type, it might take up to a minute to spin back up if it hasn't received traffic for a while. You can visit your service's `onrender.com` URL to spin it up before opening your admin page.
