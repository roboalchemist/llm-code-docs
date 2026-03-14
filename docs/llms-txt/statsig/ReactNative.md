# Source: https://docs.statsig.com/client/ReactNative.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# React Native Client SDK

> Statsig's SDK for Experimentation and Feature Flags in React Native applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Installation

    Statsig uses a multi-package strategy, so you will need to install both the Statsig client and the React Native specific bindings.

    <CodeGroup>
      ```shell NPM theme={null}
      npm install @statsig/react-native-bindings
      ```

      ```shell Yarn theme={null}
      yarn add @statsig/react-native-bindings
      ```
    </CodeGroup>

    ### Peer Dependencies

    The `@statsig/react-native-bindings` package has peer dependencies which may also need to be installed if they are not already in your project.

    <CodeGroup>
      ```shell NPM theme={null}
      npm install react-native-device-info @react-native-async-storage/async-storage
      ```

      ```shell Yarn theme={null}
      yarn add react-native-device-info @react-native-async-storage/async-storage
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    ## React Native + React Specific Setup

    The setup for a ReactNative environment is very similar to a plain [React environment](/client/React).
    The only difference is that you need to use the ReactNative specific `StatsigProviderRN`.
    This automatically switches out the storage layer used by the SDK, utilizing [AsyncStorage](https://github.com/react-native-async-storage) instead of LocalStorage (which isn't available in RN environments).

    ```tsx  theme={null}
    import {
      StatsigProviderRN,
      useFeatureGate,
    } from "@statsig/react-native-bindings";

    function Content() {
      const gate = useFeatureGate("a_gate");

      // Reason: Network or NetworkNotModified
      return (
        <View>
          <Text>Value: {gate.value ? "Pass" : "Fail"}</Text>
          <Text>Reason: {gate.details.reason}</Text>
        </View>
      );
    }

    function App() {
      return (
        <StatsigProviderRN
          sdkKey={YOUR_CLIENT_KEY}
          user={{ userID: "a-user" }}
          loadingComponent={<Text>Loading...</Text>}
        >
          <Content />
        </StatsigProviderRN>
      );
    }
    ```

    <Warning>
      **Avoid iOS 18.4 on Simulator**: Apple introduced a networking bug in iOS 18.4 that causes requests to fail when running in the Simulator. For more details, see [this thread on Apple's forums](https://developer.apple.com/forums/thread/777999).
    </Warning>
  </Step>
</Steps>

## Use the SDK

You can get an instance of the StatsigClient to check gates, experiments, dynamic configs, layers, and log events.

```jsx  theme={null}
import { useStatsigClient } from "@statsig/react-native-bindings";

const { client } = useStatsigClient();
```

See the methods you can call on the client below.

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

You can evaluate a gate by getting the client with the `useStatsigClient` hook, and then calling `checkGate`

```tsx  theme={null}
const { client } = useStatsigClient();
return (
  <div>Gate is {client.checkGate('check_user') ? 'passing' : 'failing'}.</div>
);
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

You can get a DynamicConfig value by getting the client with the `useStatsigClient` hook, and then calling `getConfig`

```tsx  theme={null}
const { client } = useStatsigClient();
const config = client.getConfig('app_properties');

return (
  <div>{config.get('title', 'Default Title')}</div>
);
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

You can access the experiment variant and parameters for the user by getting the client with the `useStatsigClient` hook, and then calling `getExperiment`.

```tsx  theme={null}
const { client } = useStatsigClient();
const experiment = client.getExperiment('headline_test');

return (
  <div>Headline Parameter: {experiment.get('headline', 'Default')}.</div>
);
```

You can access layers and layer parameters for the user by getting the client with the `useStatsigClient` hook, and then calling `getLayer`.

```tsx  theme={null}
const { client } = useStatsigClient();
const layer = client.getLayer('homepage_layer');

return (
  <div>Headline Parameter: {layer.get('hero_text', 'Welcome')}.</div>
);
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

You can get the client with the `useStatsigClient` hook, and then call `logEvent`

```tsx  theme={null}
const { client } = useStatsigClient();
return <button onClick={() => client.logEvent("button_click")}>Click Me</button>
```

## Loading State

Dependent on your setup, you may want to wait for the latest values before checking a gate or experiment.
If you are using the `StatsigProviderRN`, you can pass in a `loadingComponent` prop to display a loading state while the SDK is initializing.
If you are using the `useClientAsyncInitRN` hook, you can check the `isLoading` prop to determine if the SDK is still loading.

<Tabs>
  <Tab title="StatsigProviderRN">
    ```tsx  theme={null}
    export function App() {
      const loadingComponent = <div>Loading...</div>;

      return (
        <StatsigProviderRN
          ...
          loadingComponent={loadingComponent} // <- Pass in the loading component
        >
            <YourComponent />
        </StatsigProviderRN>
      );
    }
    ```
  </Tab>

  <Tab title="useClientAsyncInitRN">
    ```tsx  theme={null}
    export function App() {
      const { client, isLoading } = useClientAsyncInitRN(...);

      if (isLoading) {
        return <div>Loading...</div>;
      }

      return (
        <StatsigProviderRN client={client}>
          <YourComponent />
        </StatsigProviderRN>
      );
    }
    ```
  </Tab>
</Tabs>

## Advanced

### StatsigClient Outside the Component Tree

In some scenarios, you may need to use the `StatsigClient` when you are not in the React component tree. Things like background tasks or handling notifications. For these, you can use the RN-specific `StatsigClientRN`.

```tsx  theme={null}
import { StatsigClientRN } from '@statsig/react-native-bindings';

const myClient = new StatsigClientRN(
  YOUR_CLIENT_KEY,
  { userID: "a-user" }
);

await myClient.initializeAsync();

if (myClient.checkGate("my_gate")) {
  // do something cool
}
```

If you would like to access the StatsigClient instance that was created by the StatsigProvider outside of the component tree, you can use the `StatsigClientRN.instance()` method. This will return the first StatsigClient instance that was created. If you have multiple instances, you can pass in the SDK key to get a specific instance.

```tsx  theme={null}
// Inside the component tree
function App() {
  return <StatsigProviderRN sdkKey={YOUR_CLIENT_KEY} user={{ userID: "a-user" }}>
    <Text>...</Text>
  </StatsigProviderRN>
}

// Outside the component tree
const client = StatsigClientRN.instance(); // get the first created instance

const client = StatsigClientRN.instance(YOUR_CLIENT_KEY); // get a specific instance by SDK key
```

### Synchronous Storage with MMKV

Due to the lack of LocalStorage in ReactNative environments, by default the SDK will prefetch all Statsig cache entries during initialization.

If you are utilizing MMKV in your project, and would prefer to use that instead of the default (AsyncStorage). You can provide you own `StorageProvider` via `StatsigOptions`.

Something like:

```tsx  theme={null}
import { MMKV } from "react-native-mmkv";
import { StorageProvider } from "@statsig/client-core";
import { StatsigProviderRN } from '@statsig/react-native-bindings';

function App() {
    const [storageProvider] = useState<StorageProvider>(() => {
      const mmkv = new MMKV();

      return {
        isReady: () => true,
        isReadyResolver: () => null,
        getProviderName: () => "MMKV",
        getAllKeys: () => mmkv.getAllKeys(),
        getItem: (key: string) => mmkv.getString(key) ?? null,
        setItem: (key: string, value: string) => mmkv.set(key, value),
        removeItem: (key: string) => mmkv.delete(key),
      };
    });

   return (
    <StatsigProviderRN
      sdkKey={YOUR_CLIENT_KEY}
      user={{ userID: "a-user" }}
      options={{
        storageProvider, // <- Passed into StatsigOptions
      }}
    >
      <Text>...</Text>
    </StatsigProviderRN>
   );
}
```


Built with [Mintlify](https://mintlify.com).