# Source: https://docs.statsig.com/client/Next.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Next.js Client SDK

> Statsig's SDK for Experimentation and Feature Flags in Next.js applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Set Up the SDK

### AI-powered Setup

Setup Statsig in 90 seconds by copying this AI prompt into your IDE:

```text expandable Prompt theme={null}
# Statsig SDK Integration for Next.js

You are a frontend engineer integrating the Statsig SDK into a **Next.js application**. Follow all steps below one by one:

---

## Full Integration Instructions

1. **Detect the package manager** by checking for:
   - `package-lock.json` → use `npm`
   - `yarn.lock` → use `yarn`
   - `pnpm-lock.yaml` → use `pnpm`

2. **Detect the Next.js router type** by checking for:
   - `app/` directory → **App Router**
   - `pages/` directory → **Pages Router**

3. **Install the Statsig package** using the correct package manager:

# For npm
npm install @statsig/react-bindings @statsig/session-replay @statsig/web-analytics

# For yarn
yarn add @statsig/react-bindings @statsig/session-replay @statsig/web-analytics

# For pnpm
pnpm add @statsig/react-bindings @statsig/session-replay @statsig/web-analytics

4. Add your Statsig client key to .env.local:

NEXT_PUBLIC_STATSIG_CLIENT_KEY=ask the user for their CLIENT KEY and use that input

5. Integrate Statsig into the app (auto-detect router type):

### If the project uses the App Router (has an app/ directory):

// Create app/my-statsig.tsx
"use client";

import React from "react";
import { LogLevel, StatsigProvider } from "@statsig/react-bindings";

export default function MyStatsig({ children }: { children: React.ReactNode }) {
  const id = typeof userID !== "undefined" ? userID : "a-user";

  const user = {
    userID: id,
    // Optional additional fields:
    // email: 'user@example.com',
    // customIDs: { internalID: 'internal-123' },
    // custom: { plan: 'premium' }
  };

  return (
    <StatsigProvider
      sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
      user={user}
      options={{ logLevel: LogLevel.Debug }}
    >
      {children}
    </StatsigProvider>
  );
}

// Update app/layout.tsx to wrap children with MyStatsig
import MyStatsig from "./my-statsig";

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>
        <MyStatsig>
          {children} {/* Preserve all existing layout content */}
        </MyStatsig>
      </body>
    </html>
  );
}

### If the project uses the Pages Router (has a pages/ directory):

// Update pages/_app.tsx
import type { AppProps } from "next/app";
import { LogLevel, StatsigProvider } from "@statsig/react-bindings";

export default function App({ Component, pageProps }: AppProps) {
  const id = typeof userID !== "undefined" ? userID : "a-user";

  const user = {
    userID: id,
    // Optional additional fields:
    // email: 'user@example.com',
    // customIDs: { internalID: 'internal-123' },
    // custom: { plan: 'premium' }
  };

  return (
    <StatsigProvider
      sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
      user={user}
      options={{ logLevel: LogLevel.Debug }}
    >
      <Component {...pageProps} /> {/* Preserve all existing pages */}
    </StatsigProvider>
  );
}

### Final Notes

- The system must **detect the router type** and **apply the correct integration automatically**.
- **Do not remove or change any existing JSX or layout structure** — only wrap the app with `StatsigProvider`.
- **Preserve the file's language**: if it's TypeScript (`.tsx`), keep it as TypeScript; if it's JavaScript (`.jsx`), keep it as JavaScript.
- After these steps, Statsig will be integrated across the entire app, with **feature gates, configs, and experiments** available everywhere.
```

### Manual Setup

Statsig supports both [Page Router](https://nextjs.org/docs/pages) & [App Router](https://nextjs.org/docs/app), with some differences in integration patterns.

<Tabs>
  <Tab title="App Router">
    <Steps>
      <Step title="Set environment variables">
        Add the keys to your .env.local file:

        ```bash .env.local theme={null}
        # the NEXT_PUBLIC_ prefix is required for this to be available on the client side
        NEXT_PUBLIC_STATSIG_CLIENT_KEY=client-<REPLACE_WITH_YOUR_CLIENT_KEY>
        STATSIG_SERVER_KEY=secret-<REPLACE_WITH_YOUR_SERVER_KEY>
        ```
      </Step>

      <Step title="Install packages">
        For App Router, install the @statsig/next package:

        <CodeGroup>
          ```bash NPM theme={null}
          npm i @statsig/next
          ```

          ```bash Yarn theme={null}
          yarn add @statsig/next
          ```

          ```bash PNPM theme={null}
          pnpm add @statsig/next
          ```
        </CodeGroup>
      </Step>

      <Step title="Add the StatsigBootstrapProvider">
        The \<StatsigBootstrapProvider> creates both a Statsig Client and Server instance under the hood, and ["bootstraps"](/client/concepts/initialize#2-bootstrap-initialization) the client so it can render each page without a blocking network request. this will keep your app speedy and is recommended for most users. If you need more control over your setup, our [Bootstrapping](#client-bootstrapping-recommended) and [React](/client/React) docs can provide more guidance.

        Add this component around the content in your root `layout.tsx` file:

        ```tsx app/layout.tsx theme={null}
        import { StatsigBootstrapProvider } from "@statsig/next"

        export default function RootLayout({
          children,
        }: Readonly<{
          children: React.ReactNode;
        }>) {

          const user = {
            userID: "user-123", // add additional parameters as needed
          };
          return (
            <html lang="en">
              <body>
                <StatsigBootstrapProvider
                  user={user}
                  clientKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY}
                  serverKey={process.env.STATSIG_SERVER_KEY}
                >
                  {children}
                </StatsigBootstrapProvider>
              </body>
            </html>
          );
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="Page Router">
    <Steps>
      <Step title="Set environment variables">
        Add the keys to your .env.local file:

        ```bash .env.local theme={null}
        # the NEXT_PUBLIC_ prefix is required for this to be available on the client side
        NEXT_PUBLIC_STATSIG_CLIENT_KEY=client-<REPLACE_WITH_YOUR_CLIENT_KEY>
        ```
      </Step>

      <Step title="Install packages">
        Install the @statsig/react-bindings package:

        <CodeGroup>
          ```bash NPM theme={null}
          npm i @statsig/react-bindings @statsig/web-analytics
          ```

          ```bash Yarn theme={null}
          yarn add @statsig/react-bindings @statsig/web-analytics
          ```

          ```bash PNPM theme={null}
          pnpm add @statsig/react-bindings @statsig/web-analytics
          ```
        </CodeGroup>
      </Step>

      <Step title="Add StatsigProvider to _app.tsx">
        To integrate Statsig into your Page Router app you can add the `StatsigProvider` to your `_app.tsx` file.

        There is a [full example](https://github.com/statsig-io/js-client-monorepo/tree/main/samples/next-js-pages-router-sample) in the samples directory of the javascript sdk.

        ```tsx pages/_app.tsx theme={null}
        import type { AppProps } from "next/app";

        import {
          LogLevel,
          StatsigProvider,
        } from "@statsig/react-bindings";
        import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

        export default function App({ Component, pageProps }: AppProps) {
          return (
            <StatsigProvider
              sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
              user={{ userID: "a-user" }}
              options={{
                plugins: [ new StatsigAutoCapturePlugin() ],
              }}>
              <Component {...pageProps} />
            </StatsigProvider>
          );
        }
        ```
      </Step>
    </Steps>
  </Tab>
</Tabs>

See the [User (StatsigUser)](/concepts/user) doc for more info on the user property. From here, you're ready to start checking gates & experiments and sending events in any sub-file of layout.tsx!

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { useGateValue } from "@statsig/react-bindings";

    export default function Home() {
      const gate = useGateValue("my_gate");

      return (
        <div>
          Gate Value: {gate ? 'PASSED' : 'FAILED'}
        </div>
      );
    }
    ```

    <Note>
      In an App Router app, you need to use the [`use client` directive](https://nextjs.org/docs/app/building-your-application/rendering/client-components) to ensure your logic runs on the frontend.
    </Note>
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { useGateValue } from "@statsig/react-bindings";

    export default function Home() {
      const gate = useGateValue("my_gate");

      return (
        <div>
          Gate Value: {gate ? 'PASSED' : 'FAILED'}
        </div>
      );
    }
    ```
  </Tab>
</Tabs>

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { useDynamicConfig } from "@statsig/react-bindings";

    export default function Home() {
      const config = useDynamicConfig("my_dynamic_config");

      return (
        <div>
          Title: {config.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```

    <Note>
      In an App Router app, you need to use the [`use client` directive](https://nextjs.org/docs/app/building-your-application/rendering/client-components) to ensure your logic runs on the frontend.
    </Note>
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { useDynamicConfig } from "@statsig/react-bindings";

    export default function Home() {
      const config = useDynamicConfig("my_dynamic_config");

      return (
        <div>
          Title: {config.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```
  </Tab>
</Tabs>

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { useExperiment, useLayer} from "@statsig/react-bindings";

    export default function Home() {
      const layer = useLayer("my_experiment_layer");
      // or
      const experiment = useExperiment("my_experiment");

      return (
        <div>
          Title: {layer.get('title', 'Fallback Title')}
          {/* or */}
          Title: {experiment.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```

    <Note>
      In an App Router app, you need to use the [`use client` directive](https://nextjs.org/docs/app/building-your-application/rendering/client-components) to ensure your logic runs on the frontend.
    </Note>
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { useExperiment, useLayer} from "@statsig/react-bindings";

    export default function Home() {
      const layer = useLayer("my_experiment_layer");
      // or
      const experiment = useExperiment("my_experiment");

      return (
        <div>
          Title: {layer.get('title', 'Fallback Title')}
          {/* or */}
          Title: {experiment.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```
  </Tab>
</Tabs>

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { useParameterStore} from "@statsig/react-bindings";

    export default function Home() {
      const store = useParameterStore("my_param_store");

      return (
        <div>
          Title: {store.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```

    <Note>
      In an App Router app, you need to use the [`use client` directive](https://nextjs.org/docs/app/building-your-application/rendering/client-components) to ensure your logic runs on the frontend.
    </Note>
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { useParameterStore} from "@statsig/react-bindings";

    export default function Home() {
      const store = useParameterStore("my_param_store");

      return (
        <div>
          Title: {store.get('title', 'Fallback Title')}
        </div>
      );
    }
    ```
  </Tab>
</Tabs>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { useStatsigClient } from "@statsig/react-bindings";

    export default function Home() {
      const { client } = useStatsigClient();

      return (
        <div>
          <button onClick={() => client.logEvent("my_custom_event")}>
            Click Me
          </button>
        </div>
      );
    }
    ```

    <Note>
      In an App Router app, you need to use the [`use client` directive](https://nextjs.org/docs/app/building-your-application/rendering/client-components) to ensure your logic runs on the frontend.
    </Note>
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { useStatsigClient } from "@statsig/react-bindings";

    export default function Home() {
      const { client } = useStatsigClient();

      return (
        <div>
          <button onClick={() => client.logEvent("my_custom_event")}>
            Click Me
          </button>
        </div>
      );
    }
    ```
  </Tab>
</Tabs>

## Session Replay

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { StatsigProvider } from '@statsig/react-bindings';
    import { StatsigSessionReplayPlugin } from '@statsig/session-replay';

    export default function App({ children }: { children: React.ReactNode }) {
      return (
        <StatsigProvider
          sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
          user={{ userID: 'a-user' }}
          options={{ plugins: [new StatsigSessionReplayPlugin()] }}
        >
          {children}
        </StatsigProvider>
      );
    }
    ```
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { StatsigProvider } from '@statsig/react-bindings';
    import { StatsigSessionReplayPlugin } from '@statsig/session-replay';

    export default function App({ Component, pageProps }) {
      return (
        <StatsigProvider
          sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
          user={{ userID: 'a-user' }}
          options={{ plugins: [new StatsigSessionReplayPlugin()] }}
        >
          <Component {...pageProps} />
        </StatsigProvider>
      );
    }
    ```
  </Tab>
</Tabs>

## Web Analytics / Auto Capture

By including the [`@statsig/web-analytics`](https://www.npmjs.com/package/@statsig/web-analytics) package in your project, you can automatically capture common web events like clicks and page views.

For more information on filtering events, enabling console log capture, and other configuration options available in web analytics, see the [Web Analytics Configuration](/webanalytics/overview#event-filtering-and-console-configuration) documentation.

<Tabs>
  <Tab title="App Router">
    ```tsx  theme={null}
    'use client';

    import { StatsigProvider } from '@statsig/react-bindings';
    import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

    export default function App({ children }: { children: React.ReactNode }) {
      return (
        <StatsigProvider
          sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
          user={{ userID: 'a-user' }}
          options={{ plugins: [new StatsigAutoCapturePlugin()] }}
        >
          {children}
        </StatsigProvider>
      );
    }
    ```
  </Tab>

  <Tab title="Page Router">
    ```tsx  theme={null}
    import { StatsigProvider } from '@statsig/react-bindings';
    import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

    export default function App({ Component, pageProps }) {
      return (
        <StatsigProvider
          sdkKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!}
          user={{ userID: 'a-user' }}
          options={{ plugins: [new StatsigAutoCapturePlugin()] }}
        >
          <Component {...pageProps} />
        </StatsigProvider>
      );
    }
    ```
  </Tab>
</Tabs>

## Stable ID

Stable ID provides a consistent device identifier. It lets you run [logged-out experiments](/guides/first-device-level-experiment) and target gates at the device level.

### How Stable ID Works

* On first initialization the SDK generates a Stable ID and stores it in `localStorage` under `statsig.stable_id.<SDK_KEY_HASH>`.
* Subsequent sessions reuse the stored value. Each client SDK key has its own Stable ID entry.
* Local storage is scoped per domain, so cross-domain usage requires sharing the value manually (see below).

### Reading the Stable ID

<Tabs>
  <Tab title="JavaScript">
    ```tsx  theme={null}
    const context = client.getContext();
    console.log('Statsig StableID:', context.stableID);
    ```
  </Tab>

  <Tab title="React">
    ```tsx  theme={null}
    import { useStatsigClient } from '@statsig/react-bindings';

    function MyComponent() {
      const { client } = useStatsigClient();
      const context = client.getContext();

      return <div>{context.stableID}</div>;
    }
    ```
  </Tab>
</Tabs>

### Overriding the Stable ID

Provide a custom Stable ID through `StatsigUser.customIDs.stableID` if you already manage a durable device identifier.

<Tabs>
  <Tab title="JavaScript">
    ```tsx  theme={null}
    import { StatsigClient, StatsigUser } from '@statsig/js-client';

    const userWithStableID: StatsigUser = {
      customIDs: {
        stableID: 'my-custom-stable-id',
      },
    };

    const client = new StatsigClient('client-xyz', userWithStableID);
    await client.updateUserAsync(userWithStableID);
    ```
  </Tab>

  <Tab title="React">
    ```tsx  theme={null}
    import { StatsigProvider, useStatsigClient } from '@statsig/react-bindings';

    function App() {
      return (
        <StatsigProvider
          sdkKey="client-xyz"
          user={{
            customIDs: { stableID: 'my-custom-stable-id' },
          }}
        >
          <div>Your App</div>
        </StatsigProvider>
      );
    }

    function MyComponent() {
      const { client } = useStatsigClient();
      useEffect(() => {
        client.updateUserAsync({
          customIDs: { stableID: 'my-custom-stable-id' },
        });
      }, [client]);
    }
    ```
  </Tab>
</Tabs>

<Note>
  When you override the Stable ID it is persisted to local storage, so subsequent sessions reuse your custom value.
</Note>

### Sharing Stable ID Across Subdomains

Add this helper script before initializing the SDK and then copy the stored value onto your user object.

```html  theme={null}
<!-- cross domain id script -->
<script>!function(){let t="STATSIG_LOCAL_STORAGE_STABLE_ID";function e(){if(crypto&&crypto.randomUUID)return crypto.randomUUID();let t=()=>Math.floor(65536*Math.random()).toString(16).padStart(4,"0");return`${t()}${t()}-${t()}-4${t().substring(1)}-${t()}-${t()}${t()}${t()}`}let i=null,n=localStorage.getItem(t)||null;if(document.cookie.match(/statsiguuid=([\w-]+);?/)&&([,i]=document.cookie.match(/statsiguuid=([\w-]+);?/)),i&&n&&i===n);else if(i&&n&&i!==n)localStorage.setItem(t,i);else if(i&&!n)localStorage.setItem(t,i);else{let o=e();localStorage.setItem(t,o),function t(i){let n=new Date;n.setMonth(n.getMonth()+12);let o=window.location.host.split(".");o.length>2&&o.shift();let s=`.${o.join(".")}`;document.cookie=`statsiguuid=${i||e()};Expires=${n};Domain=${s};Path=/`}(o)}}();</script>

<!-- Manually attach stableID to user object -->
<script>
const userObj = {};
if (localStorage.getItem('STATSIG_LOCAL_STORAGE_STABLE_ID')) {
  userObj.customIDs = {
    stableID: localStorage.getItem('STATSIG_LOCAL_STORAGE_STABLE_ID'),
  };
}
const client = new Statsig.StatsigClient('<client-sdk-key>', userObj);
</script>
```

<small>(Use this script at your discretion and test thoroughly.)</small>

### Aligning Stable ID Between Client and Server

To share Stable ID with a backend Statsig SDK, send the value with requests and persist it server-side when missing. The server can bootstrap the client with the same Stable ID.

```tsx  theme={null}
// Server: ensure Stable ID exists, then return initialize response for the client
const values = Statsig.getClientInitializeResponse(user, YOUR_CLIENT_KEY, {
  hash: 'djb2',
});

// Client: apply the server-provided values and initialize synchronously
const { values, user: verifiedUser } = await fetch('/init-statsig-client', {
  method: 'POST',
  body: loadUserData(),
}).then((res) => res.json());

const myClient = new StatsigClient(YOUR_CLIENT_KEY, verifiedUser);
myClient.dataAdapter.setData(values);
myClient.initializeSync();
```

## Advanced Setup

### Client Bootstrapping (Recommended)

<Tabs>
  <Tab title="App Router">
    ```ts app/api/statsig-bootstrap/route.ts theme={null}
    import { Statsig, StatsigUser } from '@statsig/statsig-node-core';

    export async function POST(request: Request): Promise<Response> {
      const body = await request.json();
      const user = new StatsigUser(body?.user ?? {});

      // Ensure server SDK is initialized at startup
      // await Statsig.initialize(process.env.STATSIG_SERVER_KEY!);

      const values = Statsig.getClientInitializeResponse(user, {
        hashAlgorithm: 'djb2',
      });
      return new Response(JSON.stringify(values), { status: 200 });
    }
    ```

    ```tsx app/layout.tsx theme={null}
    import { StatsigBootstrapProvider } from '@statsig/next';

    export default function RootLayout({ children }: { children: React.ReactNode }) {
      const user = { userID: 'user-123' };
      return (
        <html lang="en">
          <body>
            <StatsigBootstrapProvider
              user={user}
              clientKey={process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY}
              serverKey={process.env.STATSIG_SERVER_KEY}
            >
              {children}
            </StatsigBootstrapProvider>
          </body>
        </html>
      );
    }
    ```
  </Tab>

  <Tab title="Page Router">
    ```ts pages/api/statsig-bootstrap.ts theme={null}
    import type { NextApiRequest, NextApiResponse } from 'next';
    import { Statsig, StatsigUser } from 'statsig-node'; // legacy Node SDK for pages router

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse<string>,
    ) {
      if (req.method !== 'POST') {
        res.status(400).send('/statsig-bootstrap only supports POST');
        return;
      }

      // Ensure server SDK is initialized at startup
      // await Statsig.initialize(process.env.STATSIG_SERVER_KEY!);

      const { user } = JSON.parse(req.body) as { user: StatsigUser };
      const values = Statsig.getClientInitializeResponse(user, { hash: 'djb2' });
      res.status(200).send(JSON.stringify(values));
    }
    ```

    ```tsx pages/_app.tsx theme={null}
    import type { AppProps } from 'next/app';
    import { StatsigProvider } from '@statsig/react-bindings';
    import { StatsigClient } from '@statsig/js-client';
    import { useEffect, useMemo, useState } from 'react';

    export default function App({ Component, pageProps }: AppProps) {
      const user = useMemo(() => ({ userID: 'a-user' }), []);
      const [client, setClient] = useState<StatsigClient | null>(null);

      useEffect(() => {
        (async () => {
          const res = await fetch('/api/statsig-bootstrap', {
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify({ user }),
          });
          const initializeValues = await res.json();
          const inst = new StatsigClient(
            process.env.NEXT_PUBLIC_STATSIG_CLIENT_KEY!,
            user,
            { initializeValues },
          );
          await inst.initializeAsync();
          setClient(inst);
        })();
      }, [user]);

      if (!client) {
        return null;
      }

      return (
        <StatsigProvider client={client}>
          <Component {...pageProps} />
        </StatsigProvider>
      );
    }
    ```
  </Tab>
</Tabs>

### Proxying Network Traffic (Optional)

<Tabs>
  <Tab title="App Router">
    ```ts app/proxy/initialize/route.ts theme={null}
    // Note: Using generic path names like "proxy" instead of "statsig-proxy"
    // to prevent ad blockers from blocking these requests
    import { generateBootstrapValues } from './statsig-backend';

    export async function POST(request: Request): Promise<Response> {
      const json = await request.json();
      if (!json || typeof json !== 'object') {
        return new Response(null, { status: 400 });
      }
      const data = await generateBootstrapValues();
      return new Response(data);
    }
    ```

    ```ts app/proxy/search.ts theme={null}
    // Note: Using generic path names like "search" instead of "log_event" or "events"
    // to prevent ad blockers from blocking these requests
    type ExtendedRequestInit = RequestInit & { duplex?: 'half' | 'full' };

    export async function POST(request: Request): Promise<Response> {
      const tail = request.url.split('?').pop();
      const logEventUrl = `https://events.statsigapi.net/v1/log_event?${tail}`;
      const fetchOptions: ExtendedRequestInit = {
        method: 'POST',
        body: request.body,
        headers: request.headers,
        duplex: 'half',
      };
      return fetch(logEventUrl, fetchOptions);
    }
    ```
  </Tab>

  <Tab title="Page Router">
    ```ts pages/api/proxy/initialize.ts theme={null}
    // Note: Using generic path names like "proxy" instead of "statsig-proxy"
    // to prevent ad blockers from blocking these requests
    import type { NextApiRequest, NextApiResponse } from 'next';
    import { StatsigUser } from 'statsig-node';
    import { getStatsigValues } from '@/pages/statsig-backend';

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse<string>,
    ) {
      if (req.method !== 'POST') {
        res.status(400).send('/initialize only supports POST');
        return;
      }
      const { user } = JSON.parse(req.body) as { user: StatsigUser };
      const values = await getStatsigValues(user);
      res.status(200).send(values);
    }
    ```

    ```ts pages/api/proxy/search.ts theme={null}
    // Note: Using generic path names like "search" instead of "log_event" or "events"
    // to prevent ad blockers from blocking these requests
    import type { NextApiRequest, NextApiResponse } from 'next';

    type ExtendedRequestInit = RequestInit & { duplex?: 'half' | 'full' };

    export default async function handler(
      req: NextApiRequest,
      res: NextApiResponse<string>,
    ): Promise<void> {
      if (req.method !== 'POST') {
        res.status(400).send('/search only supports POST');
        return;
      }

      let logEventUrl = `https://events.statsigapi.net/v1/log_event`;
      const queryParams = [] as string[];
      for (const [key, value] of Object.entries(req.query)) {
        queryParams.push(`${key}=${value}`);
      }
      if (queryParams.length > 0) {
        logEventUrl += '?' + queryParams.join('&');
      }

      const fetchOptions: ExtendedRequestInit = {
        method: 'POST',
        body: req.body as BodyInit,
        headers: req.headers as HeadersInit,
        duplex: 'half',
      };

      try {
        const response = await fetch(logEventUrl, fetchOptions);
        if (!response.ok) {
          res.status(500).send('Failed to log event');
          return;
        }
        const body = await response.text();
        res.status(response.status).send(body);
      } catch (err) {
        res.status(500).send('Failed to log event: ' + err);
      }
    }
    ```
  </Tab>
</Tabs>

```ts  theme={null}
// Assign URLs when creating the client
const inst = new StatsigClient(clientSdkKey, user, {
  networkConfig: {
    logEventUrl: '/api/proxy/search',
    initializeUrl: '/api/proxy/initialize',
    logEventCompressionMode: 'Forced',
  },
  disableCompression: true,
  disableStatsigEncoding: true,
});
```

## Statsig Site Generation (SSG)

Vercel's Static Site Generation renders HTML at build time. Because static HTML can't be responsive to per-user values, experimenting on SSG content requires one of these patterns:

* Use Vercel Edge Middleware with Statsig's Edge Config Adapter for zero-latency redirects.
* Isolate Statsig usage to hydrated client components only.

```tsx  theme={null}
// Create a single client and share it across multiple StatsigProviders
const myStatsigClient = new StatsigClient(YOUR_SDK_KEY, user, options);
await myStatsigClient.initializeAsync();

<StatsigProvider client={myStatsigClient}>
  <YourComponent />
</StatsigProvider>

<StatsigProvider client={myStatsigClient}>
  <AnotherComponent />
</StatsigProvider>
```

## Statsig Options

<ResponseField name="loggingEnabled" type="LoggingEnabledOption" default="browser-only">
  Controls logging behavior.

  * `browser-only` (default): log events from browser environments.
  * `disabled`: never send events.
  * `always`: log in every environment, including non-browser contexts.
</ResponseField>

<ResponseField name="disableLogging" type="boolean" deprecated post={["deprecated"]}>
  Use `loggingEnabled: 'disabled'` instead.
</ResponseField>

<ResponseField name="disableStableID" type="boolean" default="false">
  Skip generating a device-level Stable ID.
</ResponseField>

<ResponseField name="disableEvaluationMemoization" type="boolean" default="false">
  Recompute every evaluation instead of using the memoized result.
</ResponseField>

<ResponseField name="initialSessionID" type="string">
  Override the generated session ID.
</ResponseField>

<ResponseField name="enableCookies" type="boolean" default="false">
  Persist Stable ID in cookies for cross-domain tracking.
</ResponseField>

<ResponseField name="disableStorage" type="boolean">
  Prevent any local storage writes (disables caching).
</ResponseField>

<ResponseField name="networkConfig" type="NetworkConfig">
  Override network endpoints per request type.
</ResponseField>

<ResponseField name="environment" type="StatsigEnvironment">
  Set environment-wide defaults (for example `{ tier: 'staging' }`).
</ResponseField>

<ResponseField name="logLevel" type="LogLevel" default="Warn">
  Console verbosity.
</ResponseField>

<ResponseField name="loggingBufferMaxSize" type="number" default="50">
  Max events per log batch.
</ResponseField>

<ResponseField name="loggingIntervalMs" type="number" default="10_000">
  Interval between automatic flushes.
</ResponseField>

<ResponseField name="overrideAdapter" type="OverrideAdapter">
  Modify evaluations before returning them.
</ResponseField>

<ResponseField name="includeCurrentPageUrlWithEvents" type="boolean" default="true">
  Attach the current page URL to logged events.
</ResponseField>

<ResponseField name="disableStatsigEncoding" type="boolean" default="false">
  Send requests without Statsig-specific encoding.
</ResponseField>

<ResponseField name="logEventCompressionMode" type="LogEventCompressionMode" default="Enabled">
  Control compression for batched events.
</ResponseField>

<ResponseField name="disableCompression" type="boolean" deprecated post={["deprecated"]}>
  Use `logEventCompressionMode` instead.
</ResponseField>

<ResponseField name="dataAdapter" type="EvaluationsDataAdapter">
  Provide a custom data adapter to control caching/fetching.
</ResponseField>

<ResponseField name="customUserCacheKeyFunc" type="CustomCacheKeyGenerator">
  Override cache key generation for stored evaluations.
</ResponseField>

<Accordion title="Network Config Options">
  <ResponseField name="api" type="string" default="https://api.statsig.com">
    Base URL for all requests (append `/v1`).
  </ResponseField>

  <ResponseField name="logEventUrl" type="string" default="https://prodregistryv2.org/v1/rgstr">
    Endpoint for event uploads.
  </ResponseField>

  <ResponseField name="logEventFallbackUrls" type="string[]">
    Fallback endpoints for event uploads.
  </ResponseField>

  <ResponseField name="networkTimeoutMs" type="number" default="10000">
    Request timeout in milliseconds.
  </ResponseField>

  <ResponseField name="preventAllNetworkTraffic" type="boolean">
    Disable all outbound requests; combine with `loggingEnabled: 'disabled'` to silence log warnings.
  </ResponseField>

  <ResponseField name="networkOverrideFunc" type="function">
    Provide custom transport (e.g., Axios).
  </ResponseField>

  <ResponseField name="initializeUrl" type="string" default="https://featureassets.org/v1/initialize">
    Endpoint for initialization requests.
  </ResponseField>
</Accordion>

## Additional Resources

* [JavaScript Client SDK](/client/javascript-sdk)
* [React Client SDK](/client/React)
* [Initialization Concepts](/client/concepts/initialize)


Built with [Mintlify](https://mintlify.com).