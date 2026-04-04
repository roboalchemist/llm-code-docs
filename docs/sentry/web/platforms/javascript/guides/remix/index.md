---
---
title: Remix
description: Learn how to set up and configure Sentry in your Remix application using the installation wizard, capture your first errors, and view them in Sentry.
---

## Step 1: Install

To install Sentry using the installation wizard, run the following command within your project:

```bash
npx @sentry/wizard@latest -i remix
```

The wizard then guides you through the setup process, asking you to enable additional (optional) Sentry features for your application beyond error monitoring.

This guide assumes that you enable all features and allow the wizard to create an example page. You can add or remove features at any time, but setting them up now will save you the effort of configuring them manually later.

- Creates or updates `entry.(client|server).tsx` to initialize the SDK
- Creates `.env.sentry-build-plugin` with an auth token to upload source maps
  (this file is automatically added to `.gitignore`)
- Updates your build script or Vite configuration to automatically upload source maps to Sentry
- Instruments your application to support Remix v2 features if you use [Remix future flags](https://remix.run/docs/en/main/pages/api-development-strategy#current-future-flags)
- Adds an example page to your application to help verify your Sentry setup

## Step 2: Server-Side Performance Monitoring

To capture performance data on the server side, wrap your Remix root component (`root.tsx`) with `withSentry`:

```tsx {filename: root.tsx}
import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";

function App() {
  return (
    <html>
      <head>
        
        
      </head>
      <body>
        
        
        
        
      </body>
    </html>
  );
}

export default withSentry(App);
```

## Step 3: Avoid Ad Blockers With Tunneling (Optional)

## Step 4: Verify Your Setup

If you haven't tested your Sentry configuration yet, let's do it now. You can confirm that Sentry is working properly and sending data to your Sentry project by using the example page created by the installation wizard:

1. Open the example page `/sentry-example-page` in your browser. For most Remix applications, this will be at localhost.
2. Click the "Throw Sample Error" button to trigger a frontend error and trace.

Don't forget to explore the example page's code in your project to understand what's happening after your button click.

### View Captured Data in Sentry

Now, head over to your project on [Sentry.io](https://sentry.io) to view the collected data (it takes a couple of moments for the data to appear).

## Next Steps

At this point, you should have integrated Sentry into your Remix application and should already be sending error and performance data to your Sentry project.

Now's a good time to customize your setup and look into more advanced topics. Our next recommended steps for you are:

- Learn how to [manually capture errors](/platforms/javascript/guides/remix/usage/)
- Continue to [customize your configuration](/platforms/javascript/guides/remix/configuration/)
- Get familiar with [Sentry's product features](/product/) like tracing, insights, and alerts

- If you encountered issues with our installation wizard, try setting up Sentry manually
- Find various topics in Troubleshooting
- [Get support](https://sentry.zendesk.com/hc/en-us/)

