# Source: https://developers.webflow.com/webflow-cloud/environment/configuration.mdx

***

title: Configuration
slug: environment/configuration
description: Configure your project for deployment on Webflow Cloud.
hidden: false
max-toc-depth: 3
'og:title': Configuration
'og:description': Configure your project for deployment on Webflow Cloud.
-------------------------------------------------------------------------

Webflow Cloud is designed to handle most of your deployment configuration, so you can focus on building your app. This page explains what's configured automatically  and what you need to know if you want to understand or troubleshoot the process.

For step-by-step setup use the following guides:

<CardGroup>
  <Card
    title="Getting Started"
    href="/webflow-cloud/getting-started"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/PublishDesigner.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/PublishDesigner.svg" alt="" className="light-icon" />
      </>
    }
  >
    Get started with Webflow Cloud by following our step-by-step guide.
  </Card>

  <Card
    title="Bring your own app"
    href="/webflow-cloud/bring-your-own-app"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Migration.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Migration.svg" alt="" className="light-icon" />
      </>
    }
  >
    Migrate an existing project to Webflow Cloud.
  </Card>
</CardGroup>

## Deployment details

Webflow Cloud hosts your app on [Cloudflare Workers](https://developers.cloudflare.com/workers/), running it at a base path within your Webflow Cloud [environment](/webflow-cloud/environments) (for example, `/app`). This base path serves as the mount point for your application.

When you [deploy your environment](/webflow-cloud/deployments), Webflow Cloud uses [Wrangler](https://developers.cloudflare.com/workers/wrangler/), Cloudflare’s official CLI, to deploy your app to the Workers platform with a standard configuration.

## Default configuration

When you [deploy an environment](/webflow-cloud/deployments) in Webflow Cloud, Webflow automatically sets up the necessary configuration for deployment to the Workers platform.

During deployment, Webflow Cloud generates a `wrangler.json` configuration file based on the framework specified in your `webflow.json` file. This file includes recommended defaults for:

* Asset handling
* Node.js API compatibility
* Observability (for example, logging and metrics)

**This production file is generated automatically and can't be edited directly.** For more details on Wrangler configuration, see the [Wrangler documentation](https://developers.cloudflare.com/workers/wrangler/configuration/).

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Next.js">
    ```json title="wrangler.json"
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
      },

      "kv_namespaces": [
        {
          "binding": "KV",
          "id": "1234567890" // Webflow Cloud will automatically generate an ID for your environment
        }
      ],
      "d1_databases": [
        {
          "binding": "DB",
          "database_name": "my-database",
          "database_id": "1234567890", // Webflow Cloud will automatically generate an ID for your environment,
          "migrations_dir": "./migrations" // Specify the directory containing your migrations
        }
      ]
    }
    ```
  </Tab>

  <Tab title="Astro">
    ```json title="wrangler.json"
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
      "kv_namespaces": [
        {
          "binding": "KV",
          "id": "1234567890" // Webflow Cloud will automatically generate a KV namespace for your environment
        }
      ],
      "d1_databases": [
        {
          "binding": "DB",
          "database_name": "my-database",
          "database_id": "1234567890" // Webflow Cloud will automatically generate a D1 database for your environment,
          "migrations_dir": "./migrations" // Optional: specify the directory containing your migrations
        }
      ]
    }
    ```
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

### Storage resources

If your app requires storage, you can declare [storage bindings](/webflow-cloud/storing-data/overview) in your `wrangler.json` file. Webflow Cloud reads these bindings during deployment and automatically creates the corresponding storage resources in your environment. All other configuration values remain managed by Webflow Cloud and can't be modified directly. Learn more about [storage in Webflow Cloud.](/webflow-cloud/storing-data/overview).

## Framework configuration

Some frameworks require additional configuration to run on Webflow Cloud and the [Workers runtime](/webflow-cloud/environment). If you've created a new project using the Webflow Cloud CLI, Webflow Cloud will automatically add the necessary configuration files to your project. If you've brought your own app, you'll need to add the necessary files to your project.

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Next.js">
    Next.js apps require the following files:

    * `next.config.js`: Configures your environment's [mount path](/webflow-cloud/environments#mount-paths) and adapter settings.
    * `.open-next.config.ts`: Optimizes Next.js for the [edge runtime](/webflow-cloud/environment).
    * `cloudflare.env.ts`: Enables your app to access your [environment variables](/webflow-cloud/environments#managing-environment-variables).

    <CodeBlocks>
      ```ts title="next.config.js"
      import type { NextConfig } from "next";

      const nextConfig: NextConfig = {
        basePath: "/YOUR_BASE_PATH", // your environment's mount path
        assetPrefix: '/YOUR_BASE_PATH', // ensure this matches your environment's mount path
      };

      export default nextConfig;
      // added by create cloudflare to enable calling `getCloudflareContext()` in `next dev`
      import { initOpenNextCloudflareForDev } from "@opennextjs/cloudflare";
      initOpenNextCloudflareForDev();

      ```

      ```ts title=".open-next.config.ts"
      import { defineCloudflareConfig } from "@opennextjs/cloudflare";

      export default defineCloudflareConfig({

      });


      ```

      ```ts title="cloudflare.env.ts"
      /* eslint-disable @typescript-eslint/no-empty-interface */
      // Generated by Wrangler
      // by running `wrangler types --env-interface CloudflareEnv cloudflare-env.d.ts`

      interface CloudflareEnv {}

      ```
    </CodeBlocks>
  </Tab>

  <Tab title="Astro">
    Astro apps require the following files:

    * `astro.config.mjs`: Configures your app's [mount path](/webflow-cloud/environments#mount-paths) and adapter settings.
    * `worker.configuration.ts`: Enables your app to access your [environment variables](/webflow-cloud/environments#managing-environment-variables).

    <CodeBlocks>
      ```ts title="astro.config.mjs"
      import { defineConfig } from "astro/config";

      import cloudflare from "@astrojs/cloudflare";

      import react from "@astrojs/react";

      // https://astro.build/config
      export default defineConfig({
        base: "/YOUR_BASE_PATH", // your environment's mount path
        build: {
          assetsPrefix: "/YOUR_BASE_PATH", // ensure this matches your environment's mount path
        },
        output: "server",
        adapter: cloudflare({  // Use the Cloudflare adapter to run your app on the Workers runtime
          platformProxy: {
            enabled: true,
          },
        }),
        integrations: [react()], // Enable React integration
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

      ```ts title="worker.configuration.ts"
      /* eslint-disable @typescript-eslint/no-empty-interface */
      // Generated by Wrangler
      // After adding bindings to `wrangler.json`, regenerate this interface via `npm run cf-typegen`
      interface Env {}
      ```
    </CodeBlocks>
  </Tab>
</Tabs>

## Mount path configuration

When you create an [environment](/webflow-cloud/environments), you set a mount path, which is the subpath where your app will be accessible.
For example, with a mount path of `/app`, your app lives at:

```
https://your-webflow-cloud-domain.com/app
```

In your framework configuration, make sure you set your app's base path and asset prefix to the mount path of your environment. When building your app, use the provided `BASE_URL` and `ASSETS_PREFIX` environment variables to construct correct paths instead of hard-coding them.

### `BASE_URL`

The `BASE_URL` variable represents the mount path of your environment. Combine this with your Webflow Cloud domain to create the URL where your application is accessible to users.

Use for:

* Navigation links and client-side routing
* Form actions and redirects

<Tabs>
  <Tab title="Next.js">
    ```ts
    // Access BASE_URL in Next.js
    import config from "../next.config";

    const baseUrl = config.basePath || '';

    // Navigation button
    <Link href={`${baseUrl}/`}>
      <button>Back to Home</button>
    </Link>

    // API fetch
    const response = await fetch(`${baseUrl}/api/users`);
    ```
  </Tab>

  <Tab title="Astro">
    ```ts
    // Access BASE_URL in Astro
    const baseUrl = import.meta.env.BASE_URL;

    // Navigation button
    <a href={`${baseUrl}/`}>
      <button>Back to Home</button>
    </a>

    // API fetch
    const response = await fetch(`${baseUrl}/api/users`);
    ```
  </Tab>
</Tabs>

### `ASSETS_PREFIX`

`ASSETS_PREFIX` is the URL for static assets and some direct API calls. The `ASSETS_PREFIX` URL points directly to the Worker handling your app.

Use for:

* Referencing static assets (images, CSS, JavaScript files)
* Uploading large files to your app

<Tabs>
  <Tab title="Next.js">
    ```ts
    // Access ASSETS_PREFIX in Next.js
    import config from "../next.config";

    const assetsPrefix = config.assetPrefix || config.basePath || '';

    // Reference an image asset
    <img src={`${assetsPrefix}/images/logo.png`} alt="Logo" />
    ```
  </Tab>

  <Tab title="Astro">
    ```ts
    // Access ASSETS_PREFIX in Astro
    const assetsPrefix = import.meta.env.ASSETS_PREFIX;

    // Reference an image asset
    <img src={`${assetsPrefix}/images/logo.png`} alt="Logo" />
    ```
  </Tab>
</Tabs>

## Troubleshooting and common questions

<Accordion title="Why can’t I edit `wrangler.json`?">
  Webflow Cloud manages this file to ensure compatibility and security.
</Accordion>

<Accordion title="How do I migrate an existing project?">
  If you're migrating an existing project, follow the steps in the [Bring your own app guide](/webflow-cloud/bring-your-own-app).
</Accordion>
