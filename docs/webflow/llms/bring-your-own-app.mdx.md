# Source: https://developers.webflow.com/webflow-cloud/bring-your-own-app.mdx

***

title: Bring your own app
slug: bring-your-own-app
subtitle: Deploy your own Next.js or Astro app on Webflow Cloud.
description: Configure your Next.js or Astro app to work with Webflow Cloud
hidden: false
'og:title': Bring your own app
'og:description': Configure your Next.js or Astro app to work with Webflow Cloud
--------------------------------------------------------------------------------

Webflow Cloud deploys your app using on the [Edge runtime](/webflow-cloud/environment), enabling fast, globally distributed hosting. Before deploying to Webflow Cloud, your project may require some configuration to ensure compatibility with the Edge environment.

In this guide, you'll learn how to create projects and environments, configure your app for Webflow Cloud, and deploy your app to your Webflow site,

<Note title="Get Started with Webflow Cloud">
  To familiarize yourself with Webflow Cloud, it's recommended to create your first Webflow Cloud project from the Webflow CLI before configuring a custom project.

  [Get started with Webflow Cloud → ](/webflow-cloud/getting-started).
</Note>

**Time Estimate:** 30 minutes

**Prerequisites:**

* A Webflow account
* A Webflow site with components
* A GitHub account
* One of the following:
  * An Astro project
  * A Next.js project (version 15 or higher)
* Node.js 20.0.0 or higher and `npm` installed
  * **Note:** Currently, Webflow Cloud only supports using the `npm` package manager

## 1. Create a new Webflow Cloud project

Connect GitHub to Webflow Cloud, create a project, and configure an environment for automated deployments.

<div>
  <Frame>
    <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/30d8677b2c56ca954b661772eaaff5eb0fd48441a118f5cf59f1d11c7808268c/products/webflow-cloud/pages/introduction/assets/project-setup-05-09.png" alt="Webflow Cloud project creation" />
  </Frame>
</div>

<Steps>
  <Step title="Open Webflow Cloud">
    In Webflow, navigate to your site's settings and select "Webflow Cloud" from the sidebar.
  </Step>

  <Step title="Authenticate with Github">
    Click the “Login to GitHub” button to connect your GitHub account. Then click the “Install GitHub” button. Follow the instructions to allow Webflow Cloud to access your GitHub repositories.
  </Step>

  <Step title="Create a new Webflow Cloud project">
    Click "Create New Project"
  </Step>

  <Step title="Add project details">
    * Choose a **name** for your Webflow Cloud project.
    * Provide the URL of your newly created **GitHub repository.**
    * Optionally, enter a **description** for your app.
    * Click **"Create project"** to save your project.
  </Step>

  <Step title="Create a new Environment">
    <div>
      <Frame>
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/2036670eb1d95bef297542eeb93354e0f844a3a31ccf92d3f4841c2e5c114874/products/webflow-cloud/pages/introduction/assets/github-setup.png" alt="Webflow Cloud environment creation" />
      </Frame>
    </div>

    * Choose a **branch** to deploy your project from.
    * Choose a **mount path** for your project (for example, /admin → mysite.webflow\.io/admin).
    * Click **"Create environment"** to save a new environment for the project.
  </Step>

  <Step title="Publish your Webflow Site">
    If you have never published your site before, publish it now. This will ensure your environment is properly set up.
  </Step>
</Steps>

## 2. Configure your project for Webflow Cloud

Webflow Cloud deploys your app on the [Edge runtime](/webflow-cloud/environment), enabling fast, globally distributed hosting. The Edge runtime environment differs from traditional Node.js servers, requiring specific configurations for compatibility.

The following steps outline common migration patterns to help you adapt your application for Webflow Cloud. Depending on your application's specific requirements, you may need to make additional adjustments beyond these configurations.

<Tabs>
  <Tab title="Next.js">
    <Warning title="Webflow Cloud is compatible with Next.js 15 and higher">
      Webflow Cloud is compatible with Next.js 15 and higher. If you're using a version of Next.js lower than 15, please upgrade to the latest version.
    </Warning>

    <Steps>
      <Step title="Configure your base path">
        In Webflow Cloud, your application is served from the mount path you configured in your environment settings. For example, if your mount path is `/app`, your application will be accessible at `yourdomain.webflow.io/app`. To ensure proper routing and asset loading, you must configure the `basePath` and `assetPrefix` properties in your `next.config.ts` file to match this mount path exactly.

        ```ts title="next.config.ts"
        module.exports = {
            // Configure the base path and asset prefix to reflect the mount path of your environment
            // For example, if your app is mounted at /app, set basePath and assetPrefix to '/app'
            basePath: '/app',
            assetPrefix: '/app',

            // Additional Next.js configuration options can be added here
            // For example:
            // output: 'standalone',
            // reactStrictMode: true,
        }
        ```
      </Step>

      <Step title="Install and configure OpenNext">
        OpenNext is an adapter designed specifically for deploying Next.js applications to cloud environments like Webflow Cloud. By using OpenNext, you can deploy your Next.js app without managing complex infrastructure configurations yourself.

        1. **Install OpenNext**<br />
           In your terminal, navigate to your project and run the following command to install OpenNext:

           ```bash
           npm install @opennextjs/cloudflare@1.6.5
           ```

        2. **Configure OpenNext**<br />
           Create a new configuration file named `open-next.config.ts` in your project's root directory. This file configures OpenNext to work with Webflow Cloud's deployment environment.

           ```ts title="open-next.config.ts"
           import type { NextConfig } from "next";

           import { defineCloudflareConfig } from "@opennextjs/cloudflare";

           export default defineCloudflareConfig({
           });

           ```
      </Step>

      <Step title="Set up local testing for Webflow Cloud">
        Webflow Cloud uses Wrangler - Cloudflare's CLI tool - to bridge the gap between local development and cloud deployment. By integrating Wrangler into your workflow, you can identify and resolve compatibility issues early, significantly reducing debugging time after deployment.

        1. **Install Wrangler**<br />
           To get started, install and configure Wrangler as a dev dependency in your project.

           ```bash
           npm install wrangler --save-dev
           ```

        2. **Set up your Wrangler configuration**<br />
           Create a `wrangler.jsonc` file in your project root that defines how your application will run in development.

           ```jsonc title="wrangler.jsonc"
           {
               "$schema": "node_modules/wrangler/config-schema.json",
               "name": "nextjs",
               "main": ".open-next/worker.js",
               "compatibility_date": "2025-03-01",
               "compatibility_flags": [
                   "nodejs_compat"
               ],
               "assets": {
                   "binding": "ASSETS",
                   "directory": ".open-next/assets"
               },
               "observability": {
                   "enabled": true
               }
               /** Rest of Code **/
           }
           ```

           See the Cloudflare documentation for [more details on how to configure Wrangler](https://developers.cloudflare.com/workers/wrangler/configuration/).

        3. **Create a Cloudflare environment file**<br />
           Create a new file named `cloudflare-env.d.ts` in your project's root directory. This file will allow you to use environment variables defined in your Webflow Cloud environment.

           ```ts title="cloudflare-env.d.ts"
           interface CloudflareEnv {
           }
           ```

        4. **Add the development preview command**<br />
           Add this script to your `package.json` file to enable local testing with Wrangler. This command builds your Next.js app and immediately serves it using the Edge runtime, giving you an exact preview of how your app will perform in production on Webflow Cloud:

           ```json title="package.json"
           "scripts": {
               // Existing scripts...
               "preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview", //
           }
           ```
      </Step>

      <Step title="Define your Webflow Cloud framework configuration">
        Create a `webflow.json` file at the root of your project to inform Webflow Cloud about your app's framework.

        ```json title="webflow.json"
        {
            "cloud": {
                "framework": "nextjs"
            }
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Astro">
    <Steps>
      <Step title="Configure Astro for Webflow Cloud">
        Configure Astro for deployment on Webflow Cloud by adding the following to your `astro.config.js` file:

        ```js title={"astro.config.js"}
        import { defineConfig } from "astro/config";
        import cloudflare from "@astrojs/cloudflare"; // Import the Cloudflare adapter
        import react from "@astrojs/react";

        // https://astro.build/config
        export default defineConfig({

        // Server you app and assets from the correct mount path
          base: "/YOUR_MOUNT_PATH",
          build: {
            assetsPrefix: "/YOUR_MOUNT_PATH",
          },
          output: "server", // Use the server output mode

          // Use the Cloudflare adapter
          adapter: cloudflare({
            platformProxy: {
              enabled: true,
            },
          }),

        // Enable React components
          integrations: [react()],

          // Optimize the build configuration for the Edge runtime
          vite: {
            resolve: {
              // Use react-dom/server.edge instead of react-dom/server.browser for React 19.
              // Without this, MessageChannel from node:worker_threads needs to be polyfilled.
              alias: import.meta.env.PROD
                ? {
                    "react-dom/server": "react-dom/server.edge",
                  }
                : undefined,
            },
          },
        });

        ```

        This configuration is essential for deploying your Astro app to Webflow Cloud. Here’s a breakdown of what each part does:

        * **Sets the correct mount path**: Your app is served from a specific subdirectory in your Webflow Cloud environment (e.g., `/app`). The `base` and `build.assetsPrefix` options must match this path to ensure all routes and assets load correctly.

        * **Enables Edge runtime compatibility**: Webflow Cloud uses an [Edge runtime](/webflow-cloud/environment), not a traditional Node.js server. The `@astrojs/cloudflare` adapter compiles your app to be compatible with this serverless environment.

        * **Optimizes React for the Edge**: To prevent build errors, the `vite` configuration includes a production-specific alias for React. This forces the build to use `react-dom/server.edge`, which is designed for non-Node.js environments like Webflow Cloud.
      </Step>

      <Step title="Set up local testing for Webflow Cloud">
        Webflow Cloud uses Wrangler - Cloudflare's CLI tool - to bridge the gap between local development and cloud deployment. By integrating Wrangler into your workflow, you can identify and resolve compatibility issues early, significantly reducing debugging time after deployment.

        1. **Install Wrangler**<br />
           To get started, install and configure Wrangler as a dev dependency in your project.

           ```bash
           npm install wrangler --save-dev
           ```

        2. **Set up your Wrangler configuration**<br />
           Create a `wrangler.jsonc` file in your project root that defines how your application will run in development.

           ```jsonc title="wrangler.jsonc"
           {
               "$schema": "node_modules/wrangler/config-schema.json",
               "name": "astro",
               "main": "./dist/_worker.js/index.js",
               "compatibility_date": "2025-04-15",
               "compatibility_flags": [
                   "nodejs_compat"
               ],
               "assets": {
                   "binding": "ASSETS",
                   "directory": "./dist"
               },
               "observability": {
                   "enabled": true
               }
           }
           ```

           See the Cloudflare documentation for [more details on how to configure Wrangler](https://developers.cloudflare.com/workers/wrangler/configuration/).

           <Warning title="wrangler.jsonc">
             While you can make local changes to the `wrangler.jsonc` file, Webflow Cloud will generate a default configuration when you deploy. This production file is generated automatically and can't be edited directly.
           </Warning>

        3. **Create a Cloudflare environment file**<br />
           Create a new file named `worker-configuration.d.ts` in your project's root directory. This file will allow you to use environment variables defined in your Webflow Cloud environment.

           ```ts title="worker-configuration.d.ts"
           /* eslint-disable @typescript-eslint/no-empty-interface */
           // Generated by Wrangler
           // After adding bindings to `wrangler.jsonc`, regenerate this interface via `npm run cf-typegen`
           interface Env {}
           ```

        4. **Add the development preview command**<br />
           Add this script to your `package.json` file to enable local testing with Wrangler. This command builds your Astro app and immediately serves it using the Cloudflare Workers runtime, giving you an exact preview of how your app will perform in production on Webflow Cloud:

           ```json title="package.json"
           "scripts": {
               // Existing scripts...
               "preview": "astro build && wrangler dev", //
           }
           ```
      </Step>

      <Step title="Define your Webflow Cloud framework configuration">
        Create a `webflow.json` file at the root of your project to inform Webflow Cloud about your application's framework.

        ```json title="webflow.json"
        {
            "cloud": {
                "framework": "astro"
            }
        }
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

## 3. Manage assets and APIs

<Tabs>
  <Tab title="Next.js">
    <Steps>
      <Step title="Asset references">
        How you reference assets depends on which component you're using:

        **Next.js Image component**: Local images are automatically optimized and served through Webflow's CDN.

        ```tsx title="src/app/components/Logo.tsx"
        import Image from "next/image";

        export function Logo() {
            return (
                <Image
                    src="/images/logo.png" // No prefix needed - automatically optimized
                    alt="Logo"
                    width={180}
                    height={40}
                    priority
                />
            );
        }
        ```

        **Plain img tags**: Must include `assetPrefix` to load correctly and enable CDN caching.

        ```tsx title="src/app/components/Icon.tsx"
        import config from "../../../next.config";

        // Get the asset prefix from config
        const assetPrefix = config.assetPrefix || config.basePath || '';

        export function Icon() {
            return (
                <img
                    src={`${assetPrefix}/icons/star.svg`} // Prefix required for CDN caching
                    alt="Star icon"
                />
            );
        }
        ```
      </Step>

      <Step title="APIs">
        When using Next.js with a configured base path, there's an important distinction between API route definitions and client-side requests:

        1. **Server-side API route handlers** are automatically mounted at your base path by Next.js. To ensure your API routes run on the Edge runtime, add the `export const runtime = 'edge';` directive to your API route.
        2. **Client-side fetch calls** must ***manually*** include the base path to correctly reach your endpoints

        Without these adjustments, your API routes will not build properly and your client-side fetch calls will fail by targeting the wrong URL. Implement these patterns in all your APIs and client-side data fetching functions:

        <CodeBlocks>
          ```tsx title="API Routes"
          // /src/pages/api/data.ts
          import { NextRequest, NextResponse } from 'next/server';

          export async function GET(request: NextRequest) {
              return NextResponse.json({ message: 'Hello, world!' });
          }
          ```

          ```tsx title="Client-side fetch call"
          import config from "../next.config";

          // Get the base path from config
          const basePath = config.basePath || '';

          export async function fetchData() {
          const response = await fetch(`${basePath}/api/data`);
          return response.json();
          }
          ```
        </CodeBlocks>

        <Warning title="Edge Runtime: Use `fetch` API">
          The Edge runtime has limited API support. Stick to `fetch` for API calls and avoid third-party clients like `axios` which may not be compatible.
        </Warning>
      </Step>
    </Steps>
  </Tab>

  <Tab title="Astro">
    <Steps>
      <Step title="Asset references">
        When deployed to Webflow Cloud, all your static assets must include the configured mount path to load correctly. Without this path prefix, browsers will request assets from the root domain, resulting in 404 errors.

        We recommend constructing asset paths using the `import.meta.env.ASSETS_PREFIX` variable, which references the `build.assetsPrefix` value you configured. Webflow Cloud will automatically configure a CDN for assets that use `import.meta.env.ASSETS_PREFIX` for improved loading performance.
        Implement this pattern in your components for reliable asset loading:

        ```tsx title="layouts/Layout.astro"
        ---
        // Get the assets prefix from config
        const assetsPrefix = import.meta.env.ASSETS_PREFIX || import.meta.env.BASE_URL || '';
        ---

        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width" />
                <link
                    rel="icon"
                    type="image/svg+xml"
                    // Add assets prefix to asset path
                    href={`${assetsPrefix}/favicon.svg`}
                />
                <meta name="generator" content={Astro.generator} />
                <title>Astro Basics</title>
            </head>
            <body>
                <slot />
            </body>
        </html>

        <style>
            html,
            body {
                margin: 0;
                width: 100%;
                height: 100%;
            }
        </style>
        ```
      </Step>

      <Step title="APIs">
        1. **Server-side API route handlers** are automatically mounted at your base path by Astro. However, **you must add** the following code to your API route to ensure it runs on the Edge runtime:

        ```tsx
        // Add this line to your route to ensure it runs on the Edge runtime
        export const config = {
            runtime: "edge",
        };
        ```

        2. **Client-side fetch calls** must ***manually*** include the base path to correctly reach your endpoints

        Without these adjustments, your API routes will not build properly and your client-side fetch calls will fail by targeting the wrong URL. Implement these patterns in all your APIs and client-side data fetching functions:

        <CodeBlocks>
          ```tsx title="Server-side API route" {1-4}
          // Add this line to your route to ensure it runs on the Edge runtime
          export const config = {
              runtime: "edge",
          };

          import type { APIRoute } from 'astro';

          // Sample data
          const users = [
          { id: 1, name: 'Arthur Dent', email: 'arthur@earth.com' },
          { id: 2, name: 'Ford Prefect', email: 'ford@betelgeuse.com' },
          { id: 3, name: 'Zaphod Beeblebrox', email: 'zaphod@heartofgold.com' },
          { id: 4, name: 'Trillian', email: 'trillian@earth.com' },
          { id: 5, name: 'Marvin', email: 'marvin@paranoidandroid.com' }
          ];
          export const GET: APIRoute = async ({ params, request, context }) => {
          const url = new URL(request.url);
          const id = url.searchParams.get('id');


          if (id) {
              const user = users.find(user => user.id === parseInt(id));

              if (!user) {
              return new Response(JSON.stringify({
                  error: 'User not found'
              }), {
                  status: 404,
                  headers: {
                  'Content-Type': 'application/json'
                  }
              });
              }

              return new Response(JSON.stringify(user), {
              status: 200,
              headers: {
                  'Content-Type': 'application/json'
              }
              });
          }

          return new Response(JSON.stringify(users), {
              status: 200,
              headers: {
              'Content-Type': 'application/json'
              }
          });
          };
          ```

          ```tsx title="Client-side fetch call"
          ---
          // src/components/ViewProfile.jsx
          import { useState } from 'react';

          export function ViewProfile({ userId }) {
          const [user, setUser] = useState(null);
          const [loading, setLoading] = useState(false);

          const fetchUserProfile = async () => {
              setLoading(true);

              try {
              // Get the base path for API requests
              const basePath = import.meta.env.BASE_URL || '';

              // Include the base path in the fetch URL
              const response = await fetch(`${basePath}/api/users.json?id=${userId}`);

              if (!response.ok) {
                  throw new Error('Failed to fetch user');
              }

              const userData = await response.json();
              setUser(userData);
              } catch (error) {
              console.error('Error fetching user:', error);
              } finally {
              setLoading(false);
              }
          };

          return (
              <div>
              <button
                  onClick={fetchUserProfile}
                  disabled={loading}
              >
                  {loading ? 'Loading...' : 'View Profile'}
              </button>

              {user && (
                  <div className="profile-modal">
                  <h3>{user.name}</h3>
                  <p>Email: {user.email}</p>
                  <button onClick={() => setUser(null)}>Close</button>
                  </div>
              )}
              </div>
          );
          }
          ```
        </CodeBlocks>

        <Warning title="Edge Runtime: Use `fetch` API">
          The Edge runtime has limited API support. Stick to `fetch` for API calls and avoid third-party clients like `axios` which may not be compatible.
        </Warning>
      </Step>
    </Steps>
  </Tab>
</Tabs>

## 4. Configure environment variables

<Steps>
  <Step title="Access environment variable settings">
    In Webflow Cloud, navigate to your project's environment settings:

    * Click your project name in the dashboard
    * Select the specific environment you want to configure
    * Click the **"Environment Variables"** tab
  </Step>

  <Step title="Add and configure environment variables">
    Add each environment variable that your application requires:

    * Click **"Add Variable"**
    * Enter a descriptive **"Variable Name"** (e.g., `DATABASE_URL`, `API_KEY`)
    * Enter the corresponding **"Variable Value"**
    * Toggle **"Secret"** for sensitive values that should be encrypted (API keys, tokens, etc.)
    * Click **"Add Variable"** to save

    Repeat this process for all required variables.

    <Warning title="Environment variables are only available at runtime">
      Environment variables in Webflow Cloud are injected at runtime only and are not accessible during the build process. Keep the following in mind to avoid build failures:

      * Do not include environment variable validation or required checks that run during build time
      * Use conditional logic to handle cases where environment variables might be undefined during builds
    </Warning>
  </Step>

  <Step title="Access environment variables in your code">
    Your environment variables are accessible in your code using the following methods.

    <Tabs>
      <Tab title="Next.js">
        Next.js provides environment variables through the `process.env` object.

        ```ts title="Next.js"
        process.env.VARIABLE_NAME
        ```
      </Tab>

      <Tab title="Astro">
        Astro provides several ways to access environment variables, depending on where your code runs:

        * Use `import.meta.env` for built-in variables like `BASE_URL` and `ASSETS_PREFIX`, and for any custom variables prefixed with `PUBLIC_`. Using the `PUBLIC` prefix will make the variable available on both the server and the client.
        * Use `Astro.locals.runtime.env`  in Astro server-side components to access custom environment variables.
        * Use `locals.runtime.env`  in API routes to access custom environment variables.

        To use `locals.runtime.env` variables during local development, create a `dev.vars` file in your project root. Use the same format as a standard `.env` file to define your environment variables.

        ```ts title="Accessing environment variables in Astro"
        // 1. Built-in environment variables (available everywhere)
        import.meta.env.BASE_URL
        import.meta.env.ASSETS_PREFIX

        // 2. In Astro components (e.g., src/pages/foo.astro)
        Astro.locals.runtime.env.VARIABLE_NAME

        // 3. In API routes (e.g., src/pages/api/foo.ts)
        import type { APIRoute } from 'astro';

        export const GET: APIRoute = async ({ locals }) => {
          const siteId = locals.runtime.env.WEBFLOW_SITE_ID;
          const accessToken = locals.runtime.env.WEBFLOW_SITE_API_TOKEN;
          // Use siteId and accessToken as needed
        };
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>

## 5. Deploy your project

After configuring your project:

<Steps>
  <Step title="Test your app in the local preview environment">
    Before deploying, test your app locally in an environment that simulates Webflow Cloud. The `preview` script uses Wrangler to serve your app from the correct mount path.

    ```bash
    npm run preview
    ```

    Your app will be available at `http://localhost:PORT/YOUR_MOUNT_PATH`, where `PORT` is the port number shown in your terminal and `YOUR_MOUNT_PATH` is the one you configured.
  </Step>

  <Step title="Authenticate with Webflow">
    In your terminal, run the following command to authenticate with Webflow:

    ```bash
    webflow auth login
    ```

    This command opens a browser window to authenticate your Webflow account. After you grant access, you'll be prompted in your terminal to select a site for deployment. The CLI then creates/updates a `.env` file at the root of your project with the necessary `WEBFLOW_SITE_ID` and `WEBFLOW_API_TOKEN`.
  </Step>

  <Step title="Deploy using the Webflow CLI">
    After authenticating, run the following command to deploy your project:

    ```bash
    webflow cloud deploy
    ```

    Additionally, when you commit your changes to your GitHub branch, Webflow Cloud will automatically detect the changes and deploy your project to your environment. Learn more about [deployments in the documentation.](/webflow-cloud/deployments)

    <Warning title="Your deployment may take up to 2 minutes to complete">
      View your deployment in the ["Environment Details"](/webflow-cloud/deployments#deployment-history) dashboard. Review the status of your deployment by viewing the [build logs](/webflow-cloud/deployments#build-logs).
    </Warning>
  </Step>

  <Step title="View your app at your site's URL + mount path">
    Once your app has been successfully deployed, navigate to your site's domain and mount path to see your newly deployed Webflow Cloud app!
  </Step>
</Steps>

## Next steps

Now that you've successfully deployed your app on Webflow Cloud, here's what you can do next.

<CardGroup>
  <Card
    title="Sync your Webflow design system"
    href="/devlink/reference/overview"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DevLink.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DevLink.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Learn how to use DevLink to sync your Webflow styles, variables, and components with your app
  </Card>

  <Card
    title="Optimize your app for Webflow Cloud"
    href="/webflow-cloud/environment/framework-customization"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Optimize.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Optimize.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Explore how to optimize and tailor your deployment for the best experience on Webflow Cloud.
  </Card>

  <Card
    title="Manage deployments"
    href="/webflow-cloud/deployments"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CloudUpload.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CloudUpload.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Explore deployment options and Webflow Cloud's CI/CD integration with GitHub to streamline your release process
  </Card>

  <Card
    title="Add a SQLite database to your app"
    href="/webflow-cloud/add-sqlite"
    iconSize="12"
    iconPosition="left"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CMS.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CMS.svg" alt="" className="light-icon" />
            </>
        }
  >
    Add a SQLite database to your app to store and retrieve user data.
  </Card>
</CardGroup>

## Troubleshooting

<Accordion title="I'm seeing a 404 error when I try to access my app">
  If you have never published your site before, publish it now. If you have already published your site, check your mount path, confirm the environment exists, and verify that the latest deployment succeeded.
</Accordion>

<Accordion title="A deployment doesn't start when I push to my Github repo">
  The [Webflow Cloud GitHub App](https://github.com/apps/webflow-cloud/installations/select_target) may not have access to your repository. To check, go to the `Webflow Cloud` tab in your Webflow site settings and click "Install GitHub App." Follow the prompts on GitHub to ensure Webflow has access to read from your repository. Once you grant access, try committing to the branch that Webflow Cloud should be monitoring for deployments in your app.
</Accordion>

<Accordion title="My assets or API routes aren't loading correctly">
  Check that you're correctly using the base path in all asset and API references. Look for fixed paths that might be missing the base path prefix.
</Accordion>

<Accordion title="Authentication isn't working properly">
  Verify that your callback URLs include the correct base path and that you're not duplicating the base path in your code references.
</Accordion>

<Accordion title="My build is failing in Webflow Cloud">
  Check your project's [build logs](/webflow-cloud/deployments#build-logs) in the Webflow Cloud dashboard. Common issues include:

  * Incompatible Node.js version
  * Environment variables not configured correctly
  * Missing or incorrect framework configuration in the following files:
    * `webflow.json`
    * `next.config.js` or `Astro.config.js`
    * `wrangler.jsonc`
    * `cloudflare-env.d.ts` or `worker-configuration.d.ts`
  * Custom build commands not supported (Webflow Cloud only uses `Astro build` or `next build`)
</Accordion>

<Accordion title="Caching is not working as expected">
  Webflow Cloud overrides custom cache headers from your application. Once content is cached, you can't control caching behavior through standard HTTP headers like `Cache-Control`. See more on header behavior limitations [here](/webflow-cloud/limits#header-behavior-limitations).

  This means traditional cache invalidation methods won't work - you'll need to work within Webflow Cloud's caching behavior rather than trying to override it.
</Accordion>
