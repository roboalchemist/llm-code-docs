# Source: https://docs.statsig.com/client/javascript-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript Client SDK (Web)

> Statsig's JavaScript SDK for browser and React applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    To install the Statsig Web SDK, add the package via your preferred package manager. Include optional packages if you plan to enable Session Replay or Auto Capture.

    <Tabs>
      <Tab title="npm">
        ```bash  theme={null}
        npm install @statsig/js-client @statsig/session-replay @statsig/web-analytics
        ```
      </Tab>

      <Tab title="yarn">
        ```bash  theme={null}
        yarn add @statsig/js-client @statsig/session-replay @statsig/web-analytics
        ```
      </Tab>
    </Tabs>

    <Info>
      If you don't need Session Replay or Auto Capture, omit the `@statsig/session-replay` and `@statsig/web-analytics` packages.
    </Info>

    After installation, configure the SDK in your app entry point before rendering your UI.
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    ```tsx  theme={null}
    import { StatsigClient } from '@statsig/js-client';

    const client = new StatsigClient(
      'client-xyz',
      { userID: 'a-user' },
      {
        environment: { tier: 'development' },
      },
    );

    await client.initializeAsync();
    ```

    Use `initializeAsync` when you need to await the latest values. For a non-blocking approach, you can call `initializeAsync()` without awaiting and rely on cached values until the promise resolves.
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```tsx  theme={null}
if (client.checkGate('new_homepage_design')) {
  // Gate is on, show new experience
} else {
  // Gate is off, render the default experience
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```tsx  theme={null}
const config = client.getDynamicConfig('awesome_product_details');
const itemName = config.get('product_name', 'Some Fallback');
const price = config.value.price ?? 10.0;

if (config.value.is_discount_enabled === true) {
  // apply discount logic
}
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```tsx  theme={null}
// Reading values via getLayer
const layer = client.getLayer('user_promo_experiments');
const promoTitle = layer.get('title', 'Welcome to Statsig!');
const discount = layer.get('discount', 0.1);
```

```tsx  theme={null}
// Reading values via getExperiment
const titleExperiment = client.getExperiment('new_user_promo_title');
const priceExperiment = client.getExperiment('new_user_promo_price');

const experimentTitle = titleExperiment.value.title ?? 'Welcome to Statsig!';
const experimentDiscount = priceExperiment.value.discount ?? 0.1;
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```tsx  theme={null}
client.logEvent('my_simple_event');

client.logEvent({
  eventName: 'add_to_cart',
  value: 'SKU_12345',
  metadata: {
    price: '9.99',
    item_name: 'diet_coke_48_pack',
  },
});
```

### Typed Getters

`Layer`, `Experiment`, and `DynamicConfig` objects support a typed `get` method. Using a fallback that matches the expected type helps avoid returning unintended values.

```tsx  theme={null}
// config value: { "my_value": 1 }
const dynamicConfig = client.getDynamicConfig('a_config');

const fallbackString = dynamicConfig.get('my_value', 'fallback'); // returns 'fallback'
const fallbackNumber = dynamicConfig.get('my_value', 0); // returns 1
const rawValue = dynamicConfig.get('my_value'); // returns 1
```

Passing a fallback of the wrong type returns that fallback. When type safety is not needed, omit the fallback to receive the raw value.

### Evaluation Details

Each gate, config, experiment, and layer exposes `details` describing how the value was resolved.

* `reason` explains the source (e.g., `Network:Recognized`, `Cache:Unrecognized`).
* `lcut` is the last time any configuration changed in your project.
* `receivedAt` marks when this response was received, useful for judging cache staleness.

```tsx  theme={null}
const gate = client.getFeatureGate('a_gate');
console.log(gate.details);
// { reason: 'Cache:Recognized', lcut: 1713837126636, receivedAt: 1713838137598 }

const config = client.getDynamicConfig('a_config');
console.log(config.details);
// { reason: 'Cache:Unrecognized', lcut: 1713837126636, receivedAt: 1713838137598 }
```

See [`/sdk/debugging`](/sdk/debugging) for the full list of `reason` values.

### Sample Projects

Explore end-to-end examples in the [`js-client-monorepo` samples folder](https://github.com/statsig-io/js-client-monorepo/tree/main/samples) for React, Next.js, precomputed clients, and more.

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

```tsx  theme={null}
const homepageStore = client.getParameterStore('homepage');

const title = homepageStore.get('title', 'Welcome');
const showUpsell = homepageStore.get('upsell_upgrade_now', false);
```

## Statsig User

You need to provide a StatsigUser object to check/get your configurations. You should pass as much
information as possible in order to take advantage of advanced gate and config conditions.

Most of the time, the `userID` field is needed in order to provide a consistent experience for a given
user (see [logged-out experiments](/guides/first-device-level-experiment) to understand how to correctly run experiments for logged-out
users).

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on
StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to
create targeting based on them.

Once the user logs in or has an update/changed, make sure to call `updateUser`
with the updated `userID` and/or any other updated user attributes:

### Updating Users

Call `updateUserAsync` when the signed-in user changes to fetch fresh values for that identity.

```tsx  theme={null}
const user = { userID: 'a-user' };
await client.updateUserAsync(user);
```

For advanced flows—such as bootstrapping or prefetching users—see [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter).

### Prefetching Users

Use `prefetchData` to prepare values for another user so you can switch synchronously later.

```tsx  theme={null}
const nextUser = { userID: 'my-other-user' };

await client.dataAdapter.prefetchData(nextUser);
// Optionally handle failures without blocking the UI
client.dataAdapter.prefetchData(nextUser).catch((err) => {
  console.warn('Failed to prefetch', err);
});

client.updateUserSync(nextUser);
const gate = client.getFeatureGate('a_gate');
console.log(gate.value, gate.details.reason); // true, 'Prefetch:Recognized'
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

## Manual Exposures

<Warning>Manual logging is error-prone and can often introduce issues like uneven exposures, which compromise experiment results.</Warning>

You can query your gates/experiments without triggering an exposure, and manually log the exposures later:

<Tabs>
  <Tab title="Feature Gates">
    ```tsx  theme={null}
    const result = client.checkGate('a_gate_name', { disableExposureLog: true });
    // ...
    client.checkGate('a_gate_name'); // later, when ready to log the exposure
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```tsx  theme={null}
    const config = client.getConfig('a_dynamic_config_name', { disableExposureLog: true });
    client.getConfig('a_dynamic_config_name');
    ```
  </Tab>

  <Tab title="Experiments">
    ```tsx  theme={null}
    const experiment = client.getExperiment('an_experiment_name', { disableExposureLog: true });
    client.getExperiment('an_experiment_name');
    ```
  </Tab>

  <Tab title="Layers">
    ```tsx  theme={null}
    const layer = client.getLayer('a_layer_name', { disableExposureLog: true });
    const value = layer.get('param_name', 'fallback');

    // When ready to log
    const exposure = client.getLayer('a_layer_name');
    exposure.get('param_name', 'fallback');
    ```
  </Tab>
</Tabs>

## Session Replay

Install `@statsig/session-replay` and register the plugin to record user sessions.

```tsx  theme={null}
import { StatsigProvider } from '@statsig/react-bindings';
import { StatsigSessionReplayPlugin } from '@statsig/session-replay';

<StatsigProvider
  sdkKey="client-xyz"
  user={{ userID: 'a-user' }}
  loadingComponent={<div style={{ height: 100, width: 300, padding: 16 }}>Loading...</div>}
  options={{ plugins: [new StatsigSessionReplayPlugin()] }}
>
  <App />
</StatsigProvider>;
```

## Web Analytics / Auto Capture

By including the [`@statsig/web-analytics`](https://www.npmjs.com/package/@statsig/web-analytics) package in your project, you can automatically capture common web events like clicks and page views.

For more information on filtering events, enabling console log capture, and other configuration options available in web analytics, see the [Web Analytics Configuration](/webanalytics/overview#event-filtering-and-console-configuration) documentation.

```tsx  theme={null}
import { StatsigProvider } from '@statsig/react-bindings';
import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

<StatsigProvider
  sdkKey="client-xyz"
  user={{ userID: 'a-user' }}
  loadingComponent={<div style={{ height: 100, width: 300, padding: 16 }}>Loading...</div>}
  options={{ plugins: [new StatsigAutoCapturePlugin()] }}
>
  <App />
</StatsigProvider>;
```

## Content Security Policy

Add Statsig endpoints to your CSP `connect-src` directive when running the web SDK.

```js  theme={null}
const cspConfig = {
  directives: {
    'connect-src': [
      'api.statsig.com',
      'featuregates.org',
      'statsigapi.net',
      'events.statsigapi.net',
      'api.statsigcdn.com',
      'featureassets.org',
      'assetsconfigcdn.org',
      'prodregistryv2.org',
      'cloudflare-dns.com',
      'beyondwickedmapping.org',
    ],
  },
};
```

<Info>
  Statsig occasionally updates its network domains. Verify the latest list in [Statsig Domains](/infrastructure/statsig_domains).
</Info>

## Lifecycle & Advanced Usage

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

```tsx  theme={null}
await client.shutdown();
```

## StableID

Each client SDK has the notion of stableID, a devive-level identifier that is generated the first time the SDK is initialized and is stored locally for all future sessions. Unless storage is wiped (or app deleted), the stableID will not change.
This allows us to run device level experiments and experiments when other user identifiable information is unavailable (Logged out users).

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

## Using multiple instances of the SDK

Up to this point, we've used the SDK's singleton. We also support creating multiples instances of the SDK - the `Statsig` singleton wraps a single instance of the SDK (typically called a `StatsigClient`) that you can instantiate.

<Note> You must use a different SDK key for each sdk instance you create for this to work. Various functionality of the Statsig client is keyed on the SDK key being used. Using the same key will lead to collisions. </Note>

All top level static methods from the singleton carry over as instance methods.  To create an instance of the Statsig sdk:

```tsx  theme={null}
import { StatsigClient } from '@statsig/js-client';

const mainClient = new StatsigClient('client-xyz', { userID: 'a-user' });
const secondaryClient = new StatsigClient('client-abc', { userID: 'another-user' });

await Promise.all([
  mainClient.initializeAsync(),
  secondaryClient.initializeAsync(),
]);

if (mainClient.checkGate('a_gate')) {
  // ...
}

if (secondaryClient.checkGate('some_other_gate')) {
  // ...
}
```

## Override Adapter

Use the `LocalOverrideAdapter` to define local overrides for gates, configs, experiments, or layers.

```tsx  theme={null}
import { LocalOverrideAdapter } from '@statsig/js-local-overrides';
import { StatsigClient, LogLevel } from '@statsig/js-client';

const overrideAdapter = new LocalOverrideAdapter();
overrideAdapter.overrideGate('gate_a', false);
overrideAdapter.overrideGate('gate_b', true);

const client = new StatsigClient('client-xyz', { userID: 'a-user' }, {
  logLevel: LogLevel.Debug,
  overrideAdapter,
});
```

### Persisting Overrides

Pass your client SDK key to the adapter to persist overrides between sessions when using multi-instance setups.

```tsx  theme={null}
const overrideAdapter = new LocalOverrideAdapter('client-xyz');
```

## Using Persistent Evaluations

Persist experiment assignments so users keep the same variant even if targeting rules change.

```tsx  theme={null}
import { StatsigClient } from '@statsig/js-client';
import { UserPersistentOverrideAdapter } from '@statsig/js-user-persisted-storage';

class LocalStorageUserPersistedStorage {
  load(key: string) {
    return JSON.parse(localStorage.getItem(key) ?? '{}');
  }

  save(key: string, experiment: string, data: string) {
    const values = JSON.parse(localStorage.getItem(key) ?? '{}');
    values[experiment] = JSON.parse(data);
    localStorage.setItem(key, JSON.stringify(values));
  }

  delete(key: string, experiment: string) {
    const data = JSON.parse(localStorage.getItem(key) ?? '{}');
    delete data[experiment];
    localStorage.setItem(key, JSON.stringify(data));
  }
}

const storage = new LocalStorageUserPersistedStorage();
const adapter = new UserPersistentOverrideAdapter(storage);
const client = new StatsigClient('client-xyz', { overrideAdapter: adapter });

await client.initializeAsync({ userID: '123' });

const userPersistedValues = adapter.loadUserPersistedValues({ userID: '123' }, 'userID');
const experiment = client.getExperiment('active_experiment', { userPersistedValues });
```

See [Client Persistent Assignment](/client/concepts/persistent_assignment) for additional patterns and storage options.

## Common Targeting Use Cases

Capture cookies or URL parameters and pass them through `StatsigUser.custom` for targeting rules.

```tsx  theme={null}
const user = {
  custom: {
    isLoggedIn: cookieLib.get('isLoggedIn'),
    utm: new URL(window.location.href).searchParams.get('utm'),
  },
};

const client = new StatsigClient('client-xyz', user, options);
```

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/client/js-common-targeting.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=130e0369901f4a762a5d3aca70e3f6a9" alt="Targeting in Console" width="1734" height="749" data-path="images/client/js-common-targeting.png" />
</Frame>

## Async Timeouts

Limit how long `initializeAsync` and `updateUserAsync` wait for network responses before falling back to cached values.

```tsx  theme={null}
await client.initializeAsync({ timeoutMs: 1000 });

await client.updateUserAsync(
  { userID: 'a-user' },
  { timeoutMs: 1000 },
);
```

### Data Adapter

`StatsigClient` uses an `EvaluationsDataAdapter` to manage caching and network fetches. The default implementation (`StatsigEvaluationsDataAdapter`) reads from local storage synchronously and refreshes values from Statsig asynchronously.

See [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter) for full examples, including bootstrapping, prefetching, and custom adapters.

### Partial User Matching

Use `customUserCacheKeyFunc` with `updateUserSync` when you need to enrich a user locally without triggering a full network refresh.

```tsx  theme={null}
const originalUser = {
  customIDs: {
    analyticsID: 'analytics-123',
  },
};

const customKey = (sdkKey: string, user: StatsigUser) => {
  const analyticsID = user.customIDs?.analyticsID ?? 'anonymous';
  return `sdkKey:${sdkKey}:analyticsID:${analyticsID}`;
};

const client = new StatsigClient('client-xyz', originalUser, {
  customUserCacheKeyFunc: customKey,
});

await client.initializeAsync();

someAsyncFunction().then((newData) => {
  const enrichedUser = {
    ...originalUser,
    userID: newData.userID,
    email: newData.email,
  };

  client.updateUserSync(enrichedUser);
});
```

<Warning>
  Custom cache keys can produce stale or incorrect evaluations if multiple users map to the same key. Await `updateUserAsync` when you need guaranteed fresh values per user.
</Warning>

### Client Event Emitter

Subscribe to Statsig client lifecycle events to respond to initialization, logging, or evaluation changes.

```tsx  theme={null}
import type {
  AnyStatsigClientEvent,
  StatsigClientEvent,
} from '@statsig/client-core';

const onAnyEvent = (event: AnyStatsigClientEvent) => {
  console.log('Statsig event', event);
};

const onLogsFlushed = (event: StatsigClientEvent<'logs_flushed'>) => {
  console.log('Logs', event.events);
};

client.on('logs_flushed', onLogsFlushed);
client.on('*', onAnyEvent);

client.off('logs_flushed', onLogsFlushed);
client.off('*', onAnyEvent);
```

| Event                       | Payload              | Description                                           |
| --------------------------- | -------------------- | ----------------------------------------------------- |
| `values_updated`            | `{ status, values }` | Fired when initialize/update refreshes cached values. |
| `session_expired`           | `{}`                 | Fired when the current session expires.               |
| `error`                     | `{ error, tag }`     | Unexpected client errors.                             |
| `pre_logs_flushed`          | `{ events }`         | Before a batch of events is sent.                     |
| `logs_flushed`              | `{ events }`         | After events are sent.                                |
| `pre_shutdown`              | `{}`                 | Before the SDK shuts down.                            |
| `initialization_failure`    | `{}`                 | Initialization failed.                                |
| `gate_evaluation`           | `{ gate }`           | When a gate is evaluated.                             |
| `dynamic_config_evaluation` | `{ dynamicConfig }`  | When a config is evaluated.                           |
| `experiment_evaluation`     | `{ experiment }`     | When an experiment is evaluated.                      |
| `layer_evaluation`          | `{ layer }`          | When a layer is evaluated.                            |
| `log_event_called`          | `{ event }`          | When `logEvent` is called.                            |

## Quality & Troubleshooting

## Testing

Mock Statsig APIs in Jest to isolate business logic.

```tsx  theme={null}
import { StatsigClient } from '@statsig/js-client';

export async function transform(input: string): Promise<string> {
  const client = new StatsigClient('client-xyz', { userID: 'a-user' }, {
    networkConfig: {
      preventAllNetworkTraffic:
        typeof process !== 'undefined' && process.env['NODE_ENV'] === 'test',
    },
  });

  await client.initializeAsync();

  if (client.checkGate('a_gate')) {
    input = 'transformed';
  }

  const experiment = client.getExperiment('an_experiment');
  input += '-' + experiment.get('my_param', 'fallback');

  await client.shutdown();
  return input;
}
```

```tsx  theme={null}
import { StatsigClient } from '@statsig/js-client';

jest.mock('@statsig/js-client');

test('string transformations', async () => {
  jest
    .spyOn(StatsigClient.prototype, 'checkGate')
    .mockImplementation(() => true);

  jest
    .spyOn(StatsigClient.prototype, 'getExperiment')
    .mockImplementation(() => ({ get: () => 'my-value' } as any));

  const result = await transform('original');
  expect(result).toBe('transformed-my-value');
});
```

## Debugging

When results look unexpected, use these tools to inspect what the SDK is doing.

### Enable Verbose Logging

```ts  theme={null}
import { LogLevel, StatsigClient } from '@statsig/js-client';

const client = new StatsigClient('client-xyz', { userID: 'a-user' }, {
  logLevel: LogLevel.Debug,
});
```

### Inspect the `__STATSIG__` Global

Open your browser console and run `__STATSIG__` to inspect the current client instance. Useful properties include `_logger._queue` for pending events.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/client/statsig-global.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=3e3531beccc07586018fbd91708e173d" alt="Statsig Global" width="817" height="383" data-path="images/client/statsig-global.png" />
</Frame>

### Review Network Traffic

Filter network requests by `client-` to see initialization and logging calls.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/TkTlZF5H4SWQBYsY/images/client/network-logs.png?fit=max&auto=format&n=TkTlZF5H4SWQBYsY&q=85&s=ae66f92f04ca929bd296f3b39e37b14b" alt="Network Logs" width="845" height="267" data-path="images/client/network-logs.png" />
</Frame>

### Check Evaluation Reasons

```ts  theme={null}
const gate = client.getFeatureGate('a_gate');
console.log(gate.details.reason);
```

Common reasons:

* `Network` | `NetworkNotModified` — latest values from the API.
* `Cache` — loaded from local storage.
* `NoValues` — no cached values and network failed.
* `Bootstrap` — values provided via `dataAdapter.setData`.
* `Prefetch` — values from `dataAdapter.prefetchData`.

See [`/sdk/debugging`](/sdk/debugging#reasons) for full details.

## FAQs

#### Does the SDK use local storage or cookies?

Statsig's web SDK does not set cookies. It stores gate/config values and unsent events in `localStorage` so features keep working when offline.

#### Can I access the SDK instance globally?

```tsx  theme={null}
window.Statsig.instance().logEvent('test_event');
```

```ts  theme={null}
import { StatsigClient } from '@statsig/js-client';
StatsigClient.instance().logEvent('test_event');
```

<Info>
  With multiple instances, pass the SDK key: `Statsig.instance('client-YOUR_KEY')`.
</Info>

#### How do I handle consent or GDPR flows?

Start with logging disabled and storage blocked, then enable them after consent.

```tsx  theme={null}
const client = new StatsigClient('client-xyz', {}, {
  loggingEnabled: 'disabled',
  disableStorage: true,
});
await client.initializeAsync();

client.updateRuntimeOptions({
  loggingEnabled: 'browser-only',
  disableStorage: false,
});
```

The SDK buffers up to 500 events in memory and flushes them once logging is re-enabled.

## Additional Resources

* [Client Persistent Assignment](/client/concepts/persistent_assignment)
* [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter)
* [Debugging SDK Evaluations](/sdks/debugging)


Built with [Mintlify](https://mintlify.com).