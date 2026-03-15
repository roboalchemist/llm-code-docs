# Source: https://docs.trackjs.com/node-agent/integrations/nextjs/

Title: Integrating with NextJS

URL Source: https://docs.trackjs.com/node-agent/integrations/nextjs/

Markdown Content:
NextJS runs on both the client and server, and errors can occur in either context. To get full coverage of errors, the TrackJS agent must be installed in both the browser and server side of NextJS. We provide a [node package specifically built for NextJS](https://www.npmjs.com/package/trackjs-nextjs) to make this easier.

**Supported Versions:** The `trackjs-nextjs` package supports **NextJS** versions **14**, **15**, and **16**. Use our [legacy Next.js integrations](https://docs.trackjs.com/browser-agent/integrations/legacy) for older versions of NextJS.

[Install the package](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#install-the-package "Permalink Here")
-------------------------------------------------------------------------------------------------------------------------

First, install the TrackJS-NextJS integration package:

npm install trackjs-nextjs
[Client-Side Error Handling with App Router](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#client-side-error-handling-with-app-router "Permalink Here")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

To capture client-side errors in App Router based pages, use the `TrackJSAgent` component inserted into the head of your root at `app/layout.tsx`. Provide the agent with your TrackJS token and any other custom settings you may have.

### [Root Layout](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#root-layout "Permalink Here")

import { TrackJSAgent } from "trackjs-nextjs"import "./global.css"export default function RootLayout({ children,}: { children: React.ReactNode}) { return ( <html lang="en"> <head> <TrackJSAgent config={{ token: "YOUR_TOKEN", /* Other settings, like application identifier: application: "YOUR_APP_ID" */ }} /> </head> <body> {children} </body> </html> )}

[app/layout.tsx](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-app-layout-tsx)

### [Global Error Handler](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#global-error-handler "Permalink Here")

Some NextJS render errors are only exposed through NextJS error handling. To catch these errors, create a `global-error.tsx` in the root of `app`. This can be customized to show your own user error UI in addition to tracking the error.

"use client";import NextError from "next/error";import { useEffect } from "react";import { TrackJS } from "trackjs-nextjs";export default function GlobalError({ error, reset }) { useEffect(() => { TrackJS.track(error); }, [error]); return ( <html> <body> {/* This is the default Next.js error component. */} <NextError statusCode={undefined as any} /> </body> </html> );}

[app/global-error.tsx](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-app-global-error-tsx)

**NOTE**`global-error.tsx` is only enabled in production builds of NextJS. To verify it’s functionality, build and run the code in production mode.

### [Error Boundaries (Optional)](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#error-boundaries-optional "Permalink Here")

Some NextJS applications use additional error boundaries. Errors handled by an error boundary do not bubble to the global error handler. To log these errors, add `TrackJS.track(error)` to your existing error boundary. A simple example is below:

'use client'import { useEffect } from 'react'import { TrackJS } from "trackjs-nextjs";export default function Error({ error, reset }) { // Insert this in all error boundaries to capture errors with TrackJS useEffect(() => { TrackJS.track(error); }, [error]) // End return ( <div> <h2>Example Error boundary</h2> <p>This is an example. Your error boundary will look different.</p> </div> )}

[app/my-page/error.tsx](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-app-my-page-error-tsx)

[Client-Side Error Handling with Pages Router (Optional)](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#client-side-error-handling-with-pages-router-optional "Permalink Here")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using the Pages Router, additional configuration is needed to enable client-side error tracking.

**Pages Router Only** If you don’t use the Pages Router, skip this step.

### [App Component](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#app-component "Permalink Here")

Install the `TrackJS` agent at the start of your `pages/_app.tsx` App component. Create this file if it does not yet exist. Be sure to include your TrackJS token and any other custom settings you may have.

import App from "next/app";import { TrackJS } from "trackjs-nextjs";if (typeof window !== "undefined" && !TrackJS.isInstalled()) { TrackJS.install({ token: "YOUR_TOKEN", /* Other settings, like application identifier: application: "YOUR_APP_ID" */ });}// The default next.js app or your custom app here if you have oneexport default App;

[pages/_app.tsx](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-pages-app-tsx)

[Server-Side Error Handling](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#server-side-error-handling "Permalink Here")
---------------------------------------------------------------------------------------------------------------------------------------

There are some cases where the server-side components of NextJS will throw an error. To capture these, you need to ensure that the TrackJS agent is installed in the server context as well.

### [Instrumentation](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#instrumentation "Permalink Here")

Install TrackJS using the `instrumentation.tsx` file in the root of your project. Instrumentation captures errors in the NodeJS server side of NextJS for both App Router and Pages Router based pages.

import { TrackJSServer } from "trackjs-nextjs";export async function register() { TrackJSServer.install({ token: "YOUR_TOKEN", /* Other settings, like application identifier: application: "YOUR_APP_ID" */ });}

[instrumentation.ts](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-instrumentation-ts)

### [Enable Instrumentation (NextJS 14 Only)](https://docs.trackjs.com/browser-agent/integrations/nextjs16/#enable-instrumentation-nextjs-14-only "Permalink Here")

**NextJS 14 Requires An Additional Step:** By default, this version does not execute `instrumentation.tsx`.

Enable execution by creating a `next.config.js` file in the root of your project:

var nextConfig = { // Your Next.js config here... // Enable instrumentation.tsx execution experimental: { instrumentationHook: true }}; module.exports = nextConfig;

[next.config.js](https://docs.trackjs.com/node-agent/integrations/nextjs/#code-next-config-js)

The NextJS ecosystem is evolving rapidly, so if you have any trouble with the integration, let us know!
