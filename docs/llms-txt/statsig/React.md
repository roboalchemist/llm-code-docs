# Source: https://docs.statsig.com/client/React.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# React Client SDK

> Use Statsig in React apps with hooks, providers, and optional plugins for session replay and auto capture.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    <Info>
      If you need a starter project, follow the official <a href="https://react.dev/learn/build-a-react-app-from-scratch" target="_blank" rel="noreferrer">React quickstart</a>. Looking for Next.js instead? See the <a href="/client/Next">Next.js SDK</a> docs.
    </Info>

    ### AI-powered Setup

    Setup Statsig in 90 seconds by copying this AI prompt into your IDE:

    ```text expandable theme={null}
    You are a frontend engineer integrating the Statsig SDK into a React app. Follow these instructions carefully:
    1. Install the required Statsig packages:
         npm install @statsig/react-bindings @statsig/session-replay @statsig/web-analytics

    2. In the main component file (`App.jsx` or `App.tsx`):
       - Import `StatsigProvider` and `useClientAsyncInit` from `@statsig/react-bindings`
       - Import `StatsigAutoCapturePlugin` from `@statsig/web-analytics` and `StatsigSessionReplayPlugin` from `@statsig/session-replay`
       - Initialize the SDK using your client key: 'YOUR-CLIENT-API-KEY'
       - Use `userID` from an existing variable if it's already declared in the file; otherwise, default to `'a-user'`
       - Wrap the existing app content inside `<StatsigProvider>`, using `<div>Loading...</div>` as the `loadingComponent`

    3. DO NOT remove any existing JSX content from the component. Just wrap it.

    4. Here is what the final file structure should look like:

        import { StatsigProvider, useClientAsyncInit } from '@statsig/react-bindings';
        import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';
        import { StatsigSessionReplayPlugin } from '@statsig/session-replay';
        import YourApp from './YourApp';

        function App() {
          const id = typeof userID !== 'undefined' ? userID : 'a-user';
          const { client } = useClientAsyncInit(
            'YOUR-CLIENT-API-KEY',
            { userID: id },
            { plugins: [new StatsigAutoCapturePlugin(), new StatsigSessionReplayPlugin()] }
          );

          return (
            <StatsigProvider client={client} loadingComponent={<div>Loading...</div>}>
              <YourApp />
            </StatsigProvider>
          );
        }

    5. Ask the user to provide their CLIENT-API-KEY and insert it where prompted above.
    ```

    ### Install Packages

    <Tabs>
      <Tab title="npm">
        ```bash  theme={null}
        npm install @statsig/react-bindings
        ```
      </Tab>

      <Tab title="yarn">
        ```bash  theme={null}
        yarn add @statsig/react-bindings
        ```
      </Tab>
    </Tabs>

    <Tip>
      Add `@statsig/session-replay` and `@statsig/web-analytics` if you plan to enable Session Replay or Auto Capture.
    </Tip>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    ### Wrap Your App With `StatsigProvider`

    Provide your client SDK key and initial user when you render the provider.

    ```tsx  theme={null}
    import { StatsigProvider } from '@statsig/react-bindings';

    function App() {
      return (
        <StatsigProvider sdkKey="client-KEY" user={{ userID: '1234', email: 'example@statsig.com' }}>
          <div>Hello world</div>
        </StatsigProvider>
      );
    }
    ```

    ### Typical Project Structure

    Most projects render a root component inside the provider.

    ```tsx  theme={null}
    // App.tsx
    import RootPage from './RootPage';
    import { StatsigProvider } from '@statsig/react-bindings';

    export default function App() {
      return (
        <StatsigProvider sdkKey="client-KEY" user={{ userID: '1234' }}>
          <RootPage />
        </StatsigProvider>
      );
    }
    ```

    ```tsx  theme={null}
    // RootPage.tsx
    export default function RootPage() {
      return <div>Hello World</div>;
    }
    ```

    <Info>
      Need to balance startup speed with freshness? Review <a href="/client/concepts/initialize">Initialization Strategies</a> for bootstrap and async options.
    </Info>
  </Step>
</Steps>

## Use the SDK

Use `useStatsigClient` inside components to retrieve the client when you need to evaluate something.

```tsx  theme={null}
import { useStatsigClient } from '@statsig/react-bindings';

const { client } = useStatsigClient();
```

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```tsx  theme={null}
import {
  useFeatureGate,
  useGateValue,
  useStatsigClient,
} from '@statsig/react-bindings';

const { checkGate } = useStatsigClient();
const gateValue = useGateValue('my_gate');
const gate = useFeatureGate('my_gate');

return (
  <div>
    {checkGate('my_gate') && <p>Passing</p>}
    {gateValue && <p>Passing</p>}
    {gate.value && <p>Passing ({gate.details.reason})</p>}
  </div>
);
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```tsx  theme={null}
import { useDynamicConfig, useStatsigClient } from '@statsig/react-bindings';

const config = useDynamicConfig('my_dynamic_config');
const { getDynamicConfig } = useStatsigClient();

return (
  <div>
    <p>Reason: {config.details.reason}</p>
    <p>Value: {config.get('a_value', 'fallback_value')}</p>
    <p>Another Value: {getDynamicConfig('my_dynamic_config').get('a_bool', false)}</p>
  </div>
);
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```tsx  theme={null}
import { useExperiment, useStatsigClient } from '@statsig/react-bindings';

const experiment = useExperiment('my_experiment');
const { getExperiment } = useStatsigClient();

return (
  <div>
    <p>Group: {getExperiment('my_experiment').groupName}</p>
    <p>Value: {experiment.get('a_value', 'fallback_value')}</p>
  </div>
);
```

```tsx  theme={null}
import { useLayer, useStatsigClient } from '@statsig/react-bindings';

const layer = useLayer('my_layer');
const { getLayer } = useStatsigClient();

return (
  <div>
    <p>Group: {getLayer('my_layer').groupName}</p>
    <p>Value: {layer.get('a_value', 'fallback_value')}</p>
  </div>
);
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```tsx  theme={null}
import { useStatsigClient } from '@statsig/react-bindings';

const { logEvent } = useStatsigClient();

return <button onClick={() => logEvent('my_event')}>Click Me</button>;
```

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

## Manage Users

### Updating User Properties

Switch identities when a user logs in or when you collect richer attributes.

```tsx  theme={null}
import { useGateValue, useStatsigUser } from '@statsig/react-bindings';

export default function AccountBanner() {
  const gateValue = useGateValue('check_user');
  const { updateUserAsync } = useStatsigUser();

  return (
    <div>
      <div>Gate is {gateValue ? 'passing' : 'failing'}.</div>
      <button onClick={() => updateUserAsync({ userID: '2' })}>Login</button>
    </div>
  );
}
```

## Loading State

Wait for the latest values during initialization with either the provider or the async hook.

<Tabs>
  <Tab title="StatsigProvider">
    ```tsx  theme={null}
    import { StatsigProvider } from '@statsig/react-bindings';

    export function App() {
      return (
        <StatsigProvider
          sdkKey="client-KEY"
          user={{ userID: 'a-user' }}
          loadingComponent={<div>Loading...</div>}
        >
          <YourComponent />
        </StatsigProvider>
      );
    }
    ```
  </Tab>

  <Tab title="useClientAsyncInit">
    ```tsx  theme={null}
    import { StatsigProvider, useClientAsyncInit } from '@statsig/react-bindings';

    export function App() {
      const { client, isLoading } = useClientAsyncInit(
        'client-KEY',
        { userID: 'a-user' },
      );

      if (isLoading) {
        return <div>Loading...</div>;
      }

      return (
        <StatsigProvider client={client}>
          <YourComponent />
        </StatsigProvider>
      );
    }
    ```
  </Tab>
</Tabs>

## React Hooks

<Warning>
  Hooks that read gates, configs, experiments, or layers will log exposures on render. Use `useStatsigClient` to defer checks until you actually change the UI.
</Warning>

### Feature Gate Hooks

* Recommended: `useStatsigClient().checkGate` logs when invoked.
* `useGateValue` returns the boolean value and logs immediately.
* `useFeatureGate` returns the full gate object with details.

```tsx  theme={null}
import {
  useFeatureGate,
  useGateValue,
  useStatsigClient,
} from '@statsig/react-bindings';

const { checkGate } = useStatsigClient();
const gateValue = useGateValue('my_gate');
const gate = useFeatureGate('my_gate');

return (
  <div>
    {checkGate('my_gate') && <p>Passing</p>}
    {gateValue && <p>Passing</p>}
    {gate.value && <p>Passing ({gate.details.reason})</p>}
  </div>
);
```

### Dynamic Config Hooks

* Recommended: `useStatsigClient().getDynamicConfig` defers exposure until called.
* `useDynamicConfig` logs on render.

```tsx  theme={null}
import { useDynamicConfig, useStatsigClient } from '@statsig/react-bindings';

const config = useDynamicConfig('my_dynamic_config');
const { getDynamicConfig } = useStatsigClient();

return (
  <div>
    <p>Reason: {config.details.reason}</p>
    <p>Value: {config.get('a_value', 'fallback_value')}</p>
    <p>Another Value: {getDynamicConfig('my_dynamic_config').get('a_bool', false)}</p>
  </div>
);
```

### Experiment Hooks

* Recommended: `useStatsigClient().getExperiment` to control exposures.
* `useExperiment` logs on render.

```tsx  theme={null}
import { useExperiment, useStatsigClient } from '@statsig/react-bindings';

const experiment = useExperiment('my_experiment');
const { getExperiment } = useStatsigClient();

return (
  <div>
    <p>Group: {getExperiment('my_experiment').groupName}</p>
    <p>Value: {experiment.get('a_value', 'fallback_value')}</p>
  </div>
);
```

### Layer Hooks

Layers only log exposures when you call `.get()`.

```tsx  theme={null}
import { useLayer, useStatsigClient } from '@statsig/react-bindings';

const layer = useLayer('my_layer');
const { getLayer } = useStatsigClient();

return (
  <div>
    <p>Group: {getLayer('my_layer').groupName}</p>
    <p>Value: {layer.get('a_value', 'fallback_value')}</p>
  </div>
);
```

### Parameter Store Hooks

```tsx  theme={null}
import { useParameterStore } from '@statsig/react-bindings';

function MyComponent() {
  const store = useParameterStore('my_parameter_store');
  const title = store.get('page_title', 'Default Title');
  const maxItems = store.get('max_items', 10);
  const isEnabled = store.get('feature_enabled', false);

  const storeNoExposure = useParameterStore('my_parameter_store', {
    disableExposureLog: true,
  });

  return <div>{title}</div>;
}
```

### Log Events From Hooks

```tsx  theme={null}
import { useStatsigClient } from '@statsig/react-bindings';

const { logEvent } = useStatsigClient();

return <button onClick={() => logEvent('my_event')}>Click Me</button>;
```

### StatsigUser Hook

```tsx  theme={null}
import { useStatsigUser } from '@statsig/react-bindings';

const { user, updateUserSync } = useStatsigUser();

return (
  <div>
    <p>Current User: {user.userID}</p>
    <button onClick={() => updateUserSync({ userID: 'some-other-user' })}>
      Update User
    </button>
  </div>
);
```

### Direct Access to the Client

```tsx  theme={null}
import { useStatsigClient } from '@statsig/react-bindings';

const { client } = useStatsigClient();
console.log('stableID', client.getContext().stableID);
```

### Client Initialization Hooks

* `useClientAsyncInit` — fetches the latest values before rendering.
* `useClientBootstrapInit` — bootstrap from server-provided values.

<Info>
  You can also initialize your own client instance manually. See <a href="/client/concepts/initialize">Initialization Strategies</a> for alternatives.
</Info>

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

## Testing

Mock Statsig hooks in Jest to isolate component logic.

```tsx  theme={null}
import { StatsigProvider, useFeatureGate, useExperiment } from '@statsig/react-bindings';

function Content() {
  const gate = useFeatureGate('a_gate');
  const experiment = useExperiment('an_experiment');

  return (
    <div>
      <div data-testid="gate_test">a_gate: {gate.value ? 'Pass' : 'Fail'}</div>
      <div data-testid="exp_test">
        an_experiment: {experiment.get('my_param', 'fallback')}
      </div>
    </div>
  );
}

function App() {
  return (
    <StatsigProvider
      sdkKey={YOUR_CLIENT_KEY}
      user={{ userID: 'a-user' }}
      options={{
        networkConfig: {
          // Optional – disable network requests in tests
          preventAllNetworkTraffic:
            typeof process !== 'undefined' && process.env['NODE_ENV'] === 'test',
        },
      }}
    >
      <Content />
    </StatsigProvider>
  );
}
```

```tsx  theme={null}
import { render, screen } from '@testing-library/react';
import * as ReactBindings from '@statsig/react-bindings';

jest.mock('@statsig/react-bindings', () => ({
  ...jest.requireActual('@statsig/react-bindings'),
  useFeatureGate: () => ({ value: true }),
  useExperiment: () => ({ get: () => 'my_value' }),
}));

test('renders gate pass', async () => {
  render(<App />);
  const elem = await screen.findByTestId('gate_test');
  expect(elem.textContent).toContain('Pass');
});

test('renders experiment value', async () => {
  render(<App />);
  const elem = await screen.findByTestId('exp_test');
  expect(elem.textContent).toContain('my_value');
});
```

## Session Replay

Install `@statsig/session-replay` and register the plugin to record user sessions.

```tsx  theme={null}
import { StatsigProvider, useClientAsyncInit } from '@statsig/react-bindings';
import { StatsigSessionReplayPlugin } from '@statsig/session-replay';

function App() {
  const { client } = useClientAsyncInit(
   'client-KEY',
    { userID: 'a-user' },
    { plugins: [new StatsigSessionReplayPlugin()] },
  );

  return (
    <StatsigProvider client={client} loadingComponent={<div>Loading...</div>}>
      <div>Hello World</div>
    </StatsigProvider>
  );
}
```

## Web Analytics / Auto Capture

By including the [`@statsig/web-analytics`](https://www.npmjs.com/package/@statsig/web-analytics) package in your project, you can automatically capture common web events like clicks and page views.

For more information on filtering events, enabling console log capture, and other configuration options available in web analytics, see the [Web Analytics Configuration](/webanalytics/overview#event-filtering-and-console-configuration) documentation.

```tsx  theme={null}
import { StatsigProvider, useClientAsyncInit } from '@statsig/react-bindings';
import { StatsigAutoCapturePlugin } from '@statsig/web-analytics';

function App() {
  const { client } = useClientAsyncInit(
   'client-KEY',
    { userID: 'a-user' },
    { plugins: [new StatsigAutoCapturePlugin()] },
  );

  return (
    <StatsigProvider client={client} loadingComponent={<div>Loading...</div>}>
      <div>Hello World</div>
    </StatsigProvider>
  );
}
```

## Using Persistent Evaluations

Keep experiment variants stable across rerenders or user transitions by plugging in persistent storage. The React integration mirrors the [JavaScript workflow](/client/javascript-sdk#using-persistent-evaluations) and you can adapt the [Next.js sample](https://github.com/statsig-io/js-client-monorepo/tree/main/samples/next-js/src/app/persisted-user-storage-example) to your setup.

Read more in [Client Persistent Assignment](/client/concepts/persistent_assignment).

## Additional Resources

* [Initialization Concepts](/client/concepts/initialize)
* [JavaScript Client SDK](/client/javascript-sdk)
* [Persistent Assignment](/client/concepts/persistent_assignment)


Built with [Mintlify](https://mintlify.com).