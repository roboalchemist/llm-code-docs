# Source: https://docs.statsig.com/client/Expo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Expo Client SDK

> Statsig's SDK for Experimentation and Feature Flags in Expo applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ```shell  theme={null}
    npx expo install @statsig/expo-bindings
    ```

    ### Peer Dependencies

    The `@statsig/expo-bindings` package has peer dependencies which may also need to be installed if they are not already in your project.

    ```shell  theme={null}
    npx expo install expo-device expo-application @react-native-async-storage/async-storage
    ```
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    The setup for an Expo environment is very similar to a plain [React environment](/client/React).
    The only difference is that you need to use the Expo specific `StatsigProviderExpo`.
    This automatically switches out the storage layer used by the SDK, utilizing [AsyncStorage](https://github.com/react-native-async-storage) instead of LocalStorage (which isn't available in RN environments).

    ```tsx  theme={null}
    import { StatsigProviderExpo, useFeatureGate } from "@statsig/expo-bindings";

    function Content() {
      const gate = useFeatureGate("a_gate");

      return <Text>Reason: {gate.details.reason}</Text>; // Reason: Network or NetworkNotModified
    }

    function App() {
      return (
        <StatsigProviderExpo
          sdkKey={YOUR_CLIENT_KEY}
          user={{ userID: "a-user" }}
          options={{ environment: { tier: "development" } }} // (Optional)
          loadingComponent={<Text>Loading...</Text>}
        >
          <Content />
        </StatsigProviderExpo>
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
import { useStatsigClient } from "@statsig/expo-bindings";

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
If you are using `StatsigProviderExpo`, you can pass in a `loadingComponent` prop to display a loading state while the SDK is initializing.
If you are using the `useClientAsyncInitExpo` hook, you can check the `isLoading` prop to determine if the SDK is still loading.

<Tabs>
  <Tab title="StatsigProviderExpo">
    ```tsx  theme={null}
    export function App() {
      const loadingComponent = <div>Loading...</div>;

      return (
        <StatsigProviderExpo
          ...
          loadingComponent={loadingComponent} // <- Pass in the loading component
        >
            <YourComponent />
        </StatsigProviderExpo>
      );
    }
    ```
  </Tab>

  <Tab title="useClientAsyncInitExpo">
    ```tsx  theme={null}
    export function App() {
      const { client, isLoading } = useClientAsyncInitExpo(...);

      if (isLoading) {
        return <div>Loading...</div>;
      }

      return (
        <StatsigProviderExpo client={client}>
          <YourComponent />
        </StatsigProviderExpo>
      );
    }
    ```
  </Tab>
</Tabs>

## Advanced

### Expo Without React

In some scenarios, you may need to use the `StatsigClient` when you are not in the React component tree. Things like background tasks or handling notifications.
For these, you can use the Expo specific `StatsigClientExpo`.

```tsx  theme={null}
import { StatsigClientExpo } from '@statsig/expo-bindings';

const myClient = new StatsigClientExpo(
  YOUR_CLIENT_KEY,
  { userID: "a-user" }
);

await myClient.initializeAsync();

if (myClient.checkGate("my_gate")) {
  // do something cool
}
```

### Synchronous Storage with MMKV

If you are utilizing [MMKV](https://github.com/mrousavy/react-native-mmkv) in your project, and would prefer to use that instead of the default ([AsyncStorage](https://github.com/react-native-async-storage)).
You can provide you own `StorageProvider` via `StatsigOptions`.

Something like:

```tsx  theme={null}
import { MMKV } from "react-native-mmkv";
import { StorageProvider } from "@statsig/client-core";
import { StatsigProviderExpo } from "@statsig/expo-bindings";

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
    <StatsigProviderExpo
      sdkKey={YOUR_CLIENT_KEY}
      user={{ userID: "a-user" }}
      options={{
        storageProvider, // <- Passed into StatsigOptions
      }}
    >
      <Text>...</Text>
    </StatsigProviderExpo>
   );
}
```

## Debugging

### Network Issues

Some users have reported a `ERROR: A networking error occured during POST request` messages when first initializing Statsig. This issue is solved in releases of the SDK after 3.1.0, so upgrading your SDK should solve the issue. If it persists, reach out to us in [Slack](https://statsig.com/slack).


Built with [Mintlify](https://mintlify.com).