# Source: https://docs.statsig.com/server-core/node-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Node Server SDK

> Statsig's next-gen Node Server SDK built on our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-node" target="_blank" rel="noreferrer">Node Core on Github</a>,
  <a href="https://www.npmjs.com/package/@statsig/statsig-node-core" target="_blank" rel="noreferrer">NPM Package</a>
</Callout>

<Tip>Migrating from the Legacy Node SDK? See our [Migration Guide](/server-core/migration-guides/node).</Tip>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ```shell  theme={null}
    npm i @statsig/statsig-node-core
    ```

    The Node SDK is pre-built and compiled for different OSs & CPU architectures. Package managers will resolve the correct version automatically.

    <AccordionGroup>
      <Accordion title="Frozen Lockfile Setup">
        If your service has locked dependencies with package-lock.json or pnpm-lock.yml, you'll need to include all versions you need. For example, if you develop locally on macOS, and deploy to linux, then you have to include:

        ```
        dependencies {
            "@statsig/statsig-node-core-darwin-arm64": "0.1.0" // for macOS
            "@statsig/statsig-node-core-linux-x64-gnu": "0.1.0" // for linux x64 machines
        }
        ```
      </Accordion>

      <Accordion title="Usage with Next.js/Webpack/esbuild">
        `statsig-node-core` uses native binary files that can't be packaged with webpack/esbuild. To prevent errors, take the following steps:

        <Tabs>
          <Tab title="Next.js">
            In your `next.config.js` file, add the `@statsig/statsig-node-core` package to the `serverExternalPackages` array:

            ```jsx  theme={null}
            const nextConfig = {
              serverExternalPackages: ['@statsig/statsig-node-core'],
            }
            ```
          </Tab>

          <Tab title="esbuild">
            Add the `--packages=external` flag to your build script:

            ```shell  theme={null}
            esbuild --packages=external
            ```
          </Tab>
        </Tabs>
      </Accordion>
    </AccordionGroup>
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```jsx  theme={null}
    // Basic initialization
    import { Statsig, StatsigUser } from '@statsig/statsig-node-core';
    //Or, in common JS, const { Statsig, StatsigUser } = require('@statsig/statsig-node-core');

    const statsig = new Statsig("secret-key");
    await statsig.initialize();

    // or with StatsigOptions
    const options: StatsigOptions = { environment: "staging" };

    const statsigWithOptions = new Statsig("secret-key", options);
    await statsigWithOptions.initialize();
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```jsx  theme={null}
const user = new StatsigUser({ userID: "a-user" });

if (statsig.checkGate(user, "a_gate")) {
    // Gate is on, enable new feature
} else {
    // Gate is off
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```jsx  theme={null}
// Get the dynamic config
const config = statsig.getDynamicConfig(user, "a_config");

// Get typed values using the getValue() method
const itemName = config.getValue("product_name", "Awesome Product v1");
const price = config.getValue("price", 10.0);
const shouldDiscount = config.getValue("discount", false);

// Or access the entire value object directly
const value = config.value;
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```jsx  theme={null}
// Or, via individual experiments
const titleExp = statsig.getExperiment(user, "new_user_promo_title");
const priceExp = statsig.getExperiment(user, "new_user_promo_price");

const experimentTitle = titleExp.getValue("title", "Welcome to Statsig!");
const experimentDiscount = priceExp.getValue("discount", 0.1);

// Get values via Layer
const layer = statsig.getLayer(user, "user_promo_experiments");
const title = layer.getValue("title", "Welcome to Statsig!");
const discount = layer.getValue("discount", 0.1);
```

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```jsx  theme={null}
const gate = statsig.getFeatureGate(statsigUser, "example_gate")
console.log(gate.rule_id)
console.log(gate.value)
```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

```jsx  theme={null}
const paramStore = statsig.getParameterStore(statsigUser, "my_parameters")
const paramStoreValue = paramStore.getValue('my_parameter_value')
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```jsx  theme={null}
statsig.logEvent(
  user,
  "add_to_cart",
  null,
  {
    price: "9.99",
    item_name: "diet_coke_48_pack"
  }
);
```

Learn more about identifying users, group analytics, and best practices for logging events in the [logging events guide](/guides/logging-events).

### Sending Events to Log Explorer

You can forward logs to Logs Explorer for convenient analysis using the Forward Log Line Event API. This lets you include custom metadata and event values with each log.

```jsx  theme={null}
const user = new StatsigUser({ userID: "a-user", custom: {
    service: "my-service",
    pod: "my-pod",
    namespace: "my-namespace",
    container: "my-container",
    // ...include any service-specific metadata
} });

// levels: trace, debug, info, log, warn, error
statsig.forwardLogLineEvent(user, "warn", "script failed to load", {
  cusom_metadata: "script_name:my-script"
  // ... include any event-specific metadata
});
```

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

```jsx  theme={null}
// Create a shared instance that can be accessed globally
const statsig = Statsig.newShared("secret-key");
await statsig.initialize();

// Access the shared instance from anywhere in your code
const sharedStatsig = Statsig.shared();
const isFeatureEnabled = sharedStatsig.checkGate(user, "feature_name");

// Check if a shared instance exists
if (Statsig.hasSharedInstance()) {
  // Use the shared instance
}

// Remove the shared instance when no longer needed
Statsig.removeShared();
```

The shared instance functionality provides a singleton pattern where a single Statsig instance can be created and accessed globally throughout your application. This is useful for applications that need to access Statsig functionality from multiple parts of the codebase without having to pass around a Statsig instance.

* `Statsig.newShared(sdkKey, options)`: Creates a new shared instance of Statsig that can be accessed globally
* `Statsig.shared()`: Returns the shared instance
* `Statsig.hasSharedInstance()`: Checks if a shared instance exists (useful when you aren't sure if the shared instance is ready yet)
* `Statsig.removeShared()`: Removes the shared instance (useful when you want to switch to a new shared instance)

<Note>
  `hasSharedInstance()` and `removeShared()` are helpful in specific scenarios but aren't required in most use cases where the shared instance is set up near the top of your application.

  Also note that only one shared instance can exist at a time. Attempting to create a second shared instance will result in an error.
</Note>

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

All of the main SDK functions (`checkGate`, `getDynamicConfig`, `getExperiment`, `getLayer`) accept an optional `disableExposureLogging` parameter. When this is set to `true`, the SDK will not automatically log an exposure event. You can then manually log the exposure at a later time using the corresponding manual exposure logging method:

<Tabs>
  <Tab title="Feature Gates">
    ```jsx  theme={null}
    const result = statsig.checkGate(aUser, 'a_gate_name', {disableExposureLogging: true});
    ```

    ```jsx  theme={null}
    statsig.manuallyLogGateExposure(aUser, 'a_gate_name');
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```jsx  theme={null}
    const config = statsig.getDynamicConfig(aUser, 'a_dynamic_config_name',  {disableExposureLogging: true});
    ```

    ```jsx  theme={null}
    statsig.manuallyLogDynamicConfigExposure(aUser, 'a_dynamic_config_name');
    ```
  </Tab>

  <Tab title="Experiments">
    ```jsx  theme={null}
    const experiment = statsig.getExperiment(aUser, 'an_experiment_name',  {disableExposureLogging: true});
    ```

    ```jsx  theme={null}
    statsig.manuallyLogExperimentExposure(aUser, 'an_experiment_name');
    ```
  </Tab>

  <Tab title="Layers">
    ```jsx  theme={null}
    const layer = statsig.getLayer(aUser, 'a_layer_name',  {disableExposureLogging: true});
    const paramValue = layer.get('a_param_name', 'fallback_value');
    ```

    ```jsx  theme={null}
    statsig.manuallyLogLayerParameterExposure(aUser, 'a_layer_name', 'a_param_name');
    ```
  </Tab>
</Tabs>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```typescript  theme={null}
const user = new StatsigUser({
  userID: "a-user-id",
  email: "user@example.com",
  ip: "192.168.1.1",
  userAgent: "Mozilla/5.0...",
  country: "US",
  locale: "en_US",
  appVersion: "1.0.0",
  custom: {
    // Custom fields
    plan: "premium",
    age: 25
  },
  customIDs: {
    // Custom ID types
    stableID: "stable-id-123"
  },
  privateAttributes: {
    // Private attributes not forwarded to integrations
    email: "private@example.com"
  }
});
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  ### Parameters

  <ResponseField name="environment" type="string">
    Environment parameter for evaluation.
  </ResponseField>

  <ResponseField name="specsUrl" type="string">
    Custom URL for fetching feature specifications.
  </ResponseField>

  <ResponseField name="specsSyncIntervalMs" type="number">
    How often the SDK updates specifications from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="fallbackToStatsig" type="boolean" default="false">
    Turn this on if you are proxying `download_config_specs` / `get_id_lists` and want to fall back to the default Statsig endpoint to increase reliability.
  </ResponseField>

  <ResponseField name="logEventUrl" type="string">
    Custom URL for logging events.
  </ResponseField>

  <ResponseField name="disableAllLogging" type="boolean" default="false">
    If true, the SDK will not collect any logging within the session, including custom events and config check exposure events.
  </ResponseField>

  <ResponseField name="enableIDLists" type="boolean" default="false">
    Required to be `true` when using segments with more than 1000 IDs. See [ID List segments](/segments/add-id-list).
  </ResponseField>

  <ResponseField name="disableUserAgentParsing" type="boolean" default="false">
    If true, the SDK will not parse User-Agent strings into `browserName`, `browserVersion`, `systemName`, `systemVersion`, and `appVersion` when needed for evaluation.
  </ResponseField>

  <ResponseField name="waitForUserAgentInit" type="boolean" default="false">
    When true, the SDK waits until user agent parsing data is fully loaded during initialization (\~1 second), ensuring parsing is ready before any evaluations.
  </ResponseField>

  <ResponseField name="disableUserCountryLookup" type="boolean" default="false">
    If true, the SDK will not parse IP addresses (from `user.ip`) into country codes when needed for evaluation.
  </ResponseField>

  <ResponseField name="waitForCountryLookupInit" type="boolean" default="false">
    When true, the SDK waits for country lookup data (e.g., GeoIP or YAML files) to fully load during initialization (\~1 second), ensuring IP-to-country parsing is ready at evaluation time.
  </ResponseField>

  <ResponseField name="eventLoggingFlushIntervalMs" type="number">
    How often events are flushed to Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="eventLoggingMaxQueueSize" type="number">
    Maximum number of events to queue before forcing a flush.
  </ResponseField>

  <ResponseField name="dataStore" type="DataStore">
    An adapter with custom storage behavior for config specs. Can also continuously fetch updates in place of the Statsig network. See [Data Stores](#data-store). For example, see our 1P Redis implementation [statsig-node-redis](https://github.com/statsig-io/node-js-server-sdk-redis).
  </ResponseField>

  <ResponseField name="specsAdapterConfig" type="SpecAdapterConfig">
    Advanced settings to fetch from different sources (e.g., [statsig forward proxy](/infrastructure/forward-proxy), your own proxy server, data store) or to use different network protocols (HTTP vs gRPC streaming).
  </ResponseField>

  <ResponseField name="observabilityClient" type="ObservabilityClient">
    Interface to integrate observability metrics exposed by the SDK (e.g., config propagation delay, initialization time). See [details](#observability-client).
  </ResponseField>

  <ResponseField name="persistentStorage" type="PersistentStorage">
    Interface to use persistent storage within the SDK. See [details](#persistent-storage).
  </ResponseField>

  <ResponseField name="proxyConfig" type="ProxyConfig">
    Configuration for connecting through a proxy server.
  </ResponseField>

  <Accordion title="ProxyConfig">
    <ResponseField name="proxyHost" type="string">
      Proxy server host.
    </ResponseField>

    <ResponseField name="proxyPort" type="number">
      Proxy server port.
    </ResponseField>

    <ResponseField name="proxyAuth" type="string">
      Proxy authentication in the form "username:password".
    </ResponseField>

    <ResponseField name="proxyProtocol" type="string">
      Protocol (e.g., "http", "https").
    </ResponseField>
  </Accordion>

  ***

  ```typescript  theme={null}
  // Example usage:
  const options = new StatsigOptions();
  options.environment = "staging";
  options.initTimeoutMs = 3000;
  options.proxyConfig = {
    proxyHost: "proxy.example.com",
    proxyPort: 8080,
    // proxyAuth can be set if authentication is required
    proxyProtocol: "https"
  };

  const statsig = new Statsig("secret-key", options);
  await statsig.initialize();
  ```
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```jsx  theme={null}
await statsig.shutdown();
```

## Client SDK Bootstrapping | SSR

If you are using the Statsig client SDK in a browser or mobile app, you can bootstrap the client SDK with the values from the server SDK to avoid a network request on the client. This is useful for server-side rendering (SSR) or when you want to reduce the number of network requests on the client.

## Client Initialize Response

The Node Core SDK provides a method to generate a client initialize response that can be used to bootstrap client SDKs without requiring network requests.

```typescript  theme={null}
// Get client initialize response for a user
const values = statsig.getClientInitializeResponse(user, options);

// Pass values to a client SDK to initialize without a network request
```

<AccordionGroup>
  <Accordion title="Initialize Response Options">
    The `getClientInitializeResponse` method accepts an optional `options` parameter with the following properties:

    ```typescript  theme={null}
    export interface ClientInitializeResponseOptions {
      hashAlgorithm?: string;        // Algorithm used for hashing gate/experiment names (default: 'djb2')
      clientSdkKey?: string;         // Client SDK key to use for initialization
      includeLocalOverrides?: boolean; // Whether to include local overrides in the response
      featureGateFilter?: Set<string>; // Filter to only include specific feature gates
      experimentFilter?: Set<string>;  // Filter to only include specific experiments
      dynamicConfigFilter?: Set<string>; // Filter to only include specific dynamic configs
      layerFilter?: Set<string>;     // Filter to only include specific layers
      paramStoreFilter?: Set<string>; // Filter to only include specific parameter stores
    }
    ```
  </Accordion>

  <Accordion title="Hash Algorithm">
    The `hashAlgorithm` option specifies which algorithm to use for hashing gate and experiment names in the client initialize response. The default is `'djb2'` for better performance and smaller payload size.

    ```typescript  theme={null}
    // Use djb2 hashing algorithm for better performance
    const values = statsig.getClientInitializeResponse(user, {
      hashAlgorithm: 'djb2',
    });
    ```
  </Accordion>

  <Accordion title="Client SDK Key">
    The `clientSdkKey` option lets you filter the response to only the specific feature gates, experiments, dynamic configs, layers, or parameter stores that a particular client key has access to - effectively letting you apply [target apps](/sdk-keys/target-apps/).

    ```typescript  theme={null}
    // Specify a client SDK key
    const values = statsig.getClientInitializeResponse(user, {
      clientSdkKey: 'client-key',
    });
    ```
  </Accordion>

  <Accordion title="Filtering">
    The filter options allow you to reduce the payload size by only including specific feature gates, experiments, dynamic configs, layers, or parameter stores in the response.

    ```typescript  theme={null}
    // Only include specific feature gates and experiments
    const values = statsig.getClientInitializeResponse(user, {
      featureGateFilter: new Set(['my_gate_1', 'my_gate_2']),
      experimentFilter: new Set(['my_experiment']),
    });
    ```
  </Accordion>

  <Accordion title="Include Local Overrides">
    The `includeLocalOverrides` option determines whether to consider [local overrides](#local-overrides) you've set when evaluating each config in the response.

    ```typescript  theme={null}
    // Include local overrides in the response
    const values = statsig.getClientInitializeResponse(user, {
      includeLocalOverrides: true,
    });
    ```
  </Accordion>

  <Accordion title="Full Code Example">
    Below is a complete example of using the client initialize response to bootstrap a client SDK. Note that you may choose to parallelize or inline the initialize response data with other requests to your server, to eliminate additional requests and latency.

    ```typescript  theme={null}
    // Server-side code
    import { Statsig, StatsigUser } from '@statsig/node-core';

    // Initialize the server SDK
    await Statsig.initialize('server-secret-key');

    // In your API endpoint handler
    app.get('/statsig-bootstrap', (req, res) => {
      // Create a user object from the request
      const user = new StatsigUser({
        userID: req.query.userID || '',
        email: req.query.email,
        ip: req.ip,
        userAgent: req.headers['user-agent'],
      });

      // Generate the client initialize response with filters
      const values = Statsig.getClientInitializeResponse(user, {
        hashAlgorithm: 'djb2',
        featureGateFilter: new Set(['onboarding_v2', 'new_checkout']),
        experimentFilter: new Set(['pricing_experiment']),
        layerFilter: new Set(['ui_layer']),
      });

      // Return the values to the client
      res.json({ statsigValues: values });
    });
    ```

    ```typescript  theme={null}
    // Client-side code using @statsig/js-client
    import { Statsig } from '@statsig/js-client';

    // Fetch bootstrap values from your API
    const response = await fetch('/statsig-bootstrap');
    const { statsigValues } = await response.json();

    // Initialize the client SDK with the bootstrap values
    await Statsig.initialize({
      sdkKey: 'client-sdk-key',
      initializeValues: statsigValues,
    });
    ```
  </Accordion>
</AccordionGroup>

## SDK Event Subscriptions

The Statsig SDK provides an event subscription system that allows you to listen for evaluation events in real-time. This feature is useful for debugging, analytics, custom logging, and integrating with external systems.

### Supported Events

The SDK supports subscribing to the following evaluation events:

* **`gate_evaluated`** - Fired when a feature gate is evaluated for a user
* **`dynamic_config_evaluated`** - Fired when a dynamic config is retrieved for a user
* **`experiment_evaluated`** - Fired when an experiment is evaluated for a user
* **`layer_evaluated`** - Fired when a layer is evaluated for a user
* **`"*"`** - Subscribe to all evaluation events

### SDK Event Data

Each event includes relevant context about the evaluation:

* **Gate Evaluated Events** include: `gate_name`, `value` (boolean), `rule_id`, `reason`
* **Dynamic Config Events** include: the full `dynamic_config` object with values and metadata
* **Experiment Events** include: the full `experiment` object with variant assignment and parameters
* **Layer Events** include: the full `layer` object with allocated experiment and parameters

### Use Cases

Event subscriptions are particularly useful for:

* **Debugging**: Monitor which features are being evaluated and their results
* **Analytics**: Track feature usage patterns and user segments
* **Custom Logging**: Send evaluation data to your own logging systems
* **Integration**: Forward events to external analytics or monitoring tools
* **Testing**: Verify that features are being evaluated as expected

### Best Practices

* **Clean up subscriptions**: Always unsubscribe when you no longer need to listen for events to prevent memory leaks
* **Handle event data carefully**: Event objects may contain sensitive user information depending on your configuration
* **Use specific event types**: Subscribe to specific events rather than "\*" when possible for better performance
* **Avoid heavy processing**: Keep event handlers lightweight to avoid impacting SDK performance

```javascript expandable theme={null}
const statsig = new Statsig('server-secret-key');

// Subscribe to gate evaluation events
const gateSubId = statsig.subscribe('gate_evaluated', (event) => {
  console.log('Gate evaluated:', {
    gateName: event.gate_name,
    value: event.value,
    ruleId: event.rule_id,
    reason: event.reason
  });
});

// Subscribe to dynamic config evaluation events
const configSubId = statsig.subscribe('dynamic_config_evaluated', (event) => {
  console.log('Config evaluated:', {
    configName: event.dynamic_config.name,
    values: event.dynamic_config.value
  });
});

// Subscribe to experiment evaluation events
const experimentSubId = statsig.subscribe('experiment_evaluated', (event) => {
  console.log('Experiment evaluated:', {
    experimentName: event.experiment.name,
    groupName: event.experiment.group_name,
    parameters: event.experiment.value
  });
});

// Subscribe to layer evaluation events
const layerSubId = statsig.subscribe('layer_evaluated', (event) => {
  console.log('Layer evaluated:', {
    layerName: event.layer.name,
    allocatedExperiment: event.layer.allocated_experiment_name,
    parameters: event.layer.value
  });
});

// Subscribe to all events
const allEventsSubId = statsig.subscribe('*', (event) => {
  console.log('Event received:', event.event_name, event);
});

// Unsubscribe from specific event types
statsig.unsubscribe('gate_evaluated');

// Unsubscribe using subscription ID
statsig.unsubscribeById(configSubId);

// Unsubscribe from all events
statsig.unsubscribeAll();
```

## Local Overrides

Local Overrides are a way to override the values of gates, configs, experiments, and layers for testing purposes. This is useful for local development or testing scenarios where you want to force a specific value without having to change the configuration in the Statsig console.

<Tabs>
  <Tab title="Feature Gates">
    ```jsx  theme={null}
    // Overrides the given gate to the specified value
    Statsig.overrideGate("a_gate_name", true);

    // Optional third parameter, overrides the gate only for a given ID
    Statsig.overrideGate("a_gate_name", true, "userID-123");
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```jsx  theme={null}
    // Overrides the given dynamic config to the provided value
    Statsig.overrideDynamicConfig("a_config_name", { key: "value" });

    // Optional third parameter, overrides the dynamic config only for a given ID
    Statsig.overrideDynamicConfig("a_config_name", { key: "value" }, "userID-123");
    ```
  </Tab>

  <Tab title="Experiments">
    ```jsx  theme={null}
    // Overrides the given experiment to the provided value
    Statsig.overrideExperiment("an_experiment_name", { key: "value" });

    // Optional third parameter, overrides the experiment only for a given ID
    Statsig.overrideExperiment("an_experiment_name", { key: "value" }, "userID-123");

    // Overrides the given experiment to a particular groupname
    Statsig.overrideExperimentByGroupName("an_experiment_name", "a_group_name");

    // Alternatively, get the Experiment object for a given groupName
    const groupExp = statsig.getExperimentByGroupName("pricing_experiment", "premium_group");
    const premiumPrice = groupExp.getValue("price", 9.99);
    ```
  </Tab>

  <Tab title="Layers">
    ```jsx  theme={null}
    // Overrides the given layer to the provided value
    Statsig.overrideLayer("a_layer_name", { key: "value" });

    // Optional third parameter, overrides the layer only for a given ID
    Statsig.overrideLayer("a_layer_name", { key: "value" }, "userID-123");
    ```
  </Tab>
</Tabs>

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

```typescript expandable PersistentStorageInterface.ts theme={null}
export interface PersistentStorage {
  load: (key: string) => UserPersistedValues | null;
  save: (key: string, config_name: string, data: StickyValues) => void;
  delete: (key: string, config_name: string) => void;
}

export interface StickyValues {
  value: boolean;
  json_value: Record<string, unknown>;
  rule_id: string;
  group_name: string | null;
  secondary_exposures: SecondaryExposure[];
  undelegated_secondary_exposures: SecondaryExposure[];
  config_delegate: string | null;
  explicit_parameters: string[] | null;
  time: number;
  configVersion?: number | undefined;
}

export type UserPersistedValues = Record<string, StickyValues>;

export interface SecondaryExposure {
  gate: string;
  gateValue: string;
  ruleId: string;
}
```

### Usage Example

```typescript expandable PersistentStorageUsage.ts theme={null}
import { PersistentStorage, StickyValues, UserPersistedValues } from '@statsig/statsig-node-core';

class MyPersistentStorage implements PersistentStorage {
  private storage = new Map<string, UserPersistedValues>();
  constructor() {
      this.load = this.load.bind(this);
      this.save = this.save.bind(this);
      this.delete = this.delete.bind(this);
  }

  load(key: string): UserPersistedValues | null {
    return this.storage.get(key) || null;
  }

  save(key: string, config_name: string, data: StickyValues): void {
    const existing = this.storage.get(key) || {};
    existing[config_name] = data;
    this.storage.set(key, existing);
  }

  delete(key: string, config_name: string): void {
    const existing = this.storage.get(key);
    if (existing) {
      delete existing[config_name];
      this.storage.set(key, existing);
    }
  }
  
  getUserPersistedValue(user: StatsigUser, idType: string): UserPersistedValues | null {
    const storageKey = this.getStorageKey(user, idType);
    if (storageKey !== null) {
      return this.load(storageKey);
    }
    return null;
  }

  private getStorageKey(user: StatsigUser, idType: string): string | null {
    const lowerCaseIdType = idType.toLowerCase();

    if (lowerCaseIdType === "user_id" || lowerCaseIdType === "userid") {
      const id = user.userID;
      return id ? `${id}:userID` : null;
    } else if (user.customIDs) {
      const id = user.customIDs[idType];
      return id ? `${id}:${idType}` : null;
    }

    return null;
  }

}
```

<Note>Persistent storage support was added in version 0.6.1 of the Node.js SDK.</Note>

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

```typescript  theme={null}
export interface DataStore {
  initialize?: () => Promise<void>;
  shutdown?: () => Promise<void>;
  get?: (key: string) => Promise<DataStoreResponse>;
  set?: (key: string, value: string, time?: number) => Promise<void>;
  supportPollingUpdatesFor?: (key: string) => Promise<boolean>;
}

export interface DataStoreResponse {
  result?: string;
  time?: number;
}
```

For example, see our 1P implementation via Redis [statsig-node-redis](https://github.com/statsig-io/node-js-server-sdk-redis).

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

<AccordionGroup>
  <Accordion title="Logger Interface">
    ```typescript  theme={null}
    interface OutputLoggerProvider {
      initialize?: () => void;
      debug?: (tag: string, message: string) => void;
      info?: (tag: string, message: string) => void;
      warn?: (tag: string, message: string) => void;
      error?: (tag: string, message: string) => void;
      shutdown?: () => void;
    }
    ```
  </Accordion>

  <Accordion title="Implementation Example">
    ### Implementation Example

    ```typescript  theme={null}
    import { OutputLoggerProvider } from '@statsig/statsig-node-core';

    class CustomOutputLogger implements OutputLoggerProvider {
      initialize = () => {
        console.log('Logger initialized');
      };

      debug = (tag: string, message: string) => {
        console.debug(`[${tag}] ${message}`);
      };

      info = (tag: string, message: string) => {
        console.info(`[${tag}] ${message}`);
      };

      warn = (tag: string, message: string) => {
        console.warn(`[${tag}] ${message}`);
      };

      error = (tag: string, message: string) => {
        console.error(`[${tag}] ${message}`);
      };

      shutdown = () => {
        console.log('Logger shutdown');
      };
    }
    ```
  </Accordion>

  <Accordion title="Usage with StatsigOptions">
    ```typescript  theme={null}
    import { Statsig, StatsigOptions } from '@statsig/statsig-node-core';

    const customLogger = new CustomOutputLogger();

    const options: StatsigOptions = {
      outputLoggerProvider: customLogger,
      outputLogLevel: 'info', // 'none' | 'debug' | 'info' | 'warn' | 'error'
    };

    const statsig = new Statsig('secret-key', options);
    await statsig.initialize();
    ```
  </Accordion>

  <Accordion title="Notes">
    * All methods in the `OutputLoggerProvider` interface are optional
    * The `tag` parameter indicates the SDK component or category generating the log message
    * Use `outputLogLevel` in StatsigOptions to control which log levels are actually called
    * The logger is automatically initialized when the Statsig client initializes and shut down when the client shuts down
  </Accordion>
</AccordionGroup>

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

```typescript  theme={null}
export interface ObservabilityClient {
  initialize?: () => void;
  increment?: (metricName: string, value: number, tags: Record<string, string>) => void;
  gauge?: (metricName: string, value: number, tags: Record<string, string>) => void;
  dist?: (metricName: string, value: number, tags: Record<string, string>) => void;
  error?: (tag: string, error: string) => void;
}
```

## FAQs

### How do I run experiments for logged out users?

### Common Problems while installing

1. **Seeing SSL Error**

Right now the binary files will look at certain versions of SSL.

```shell  theme={null}
// Try run this
apt-get update && apt-get install libcurl4-openssl-dev -y && rm -rf /var/lib/apt/lists/*
```

2. **Docker build failing with platform-specific dependencies**

When building in Docker (Linux environment), the build may fail if your local `package-lock.json` or `yarn.lock` contains platform-specific dependencies for macOS. This happens because `npm install` locally on Mac pulls down Apple-specific variants, but Docker tries to use those same locked dependencies on Linux.

**Solution:** Either install the Linux-specific variant during your Docker build step:

```dockerfile  theme={null}
RUN npm install @statsig/statsig-node-core-linux-x64-gnu
```

Or add both platform variants as dependencies in your `package.json`:

```json  theme={null}
"dependencies": {
  "@statsig/statsig-node-core": "X.Y.Z", // Common (Required)
  "@statsig/statsig-node-core-darwin-arm64": "X.Y.Z", // Mac Specific
  "@statsig/statsig-node-core-linux-x64-gnu": "X.Y.Z" // Linux Specific
}
```

## Reference

<Accordion title="All API Methods">
  * `checkGate(user: StatsigUser, gateName: string, options?: EvaluationOptions): boolean`
  * `getDynamicConfig(user: StatsigUser, configName: string, options?: EvaluationOptions): DynamicConfig`
  * `getExperiment(user: StatsigUser, experimentName: string, options?: EvaluationOptions): DynamicConfig`
  * `getLayer(user: StatsigUser, layerName: string, options?: EvaluationOptions): Layer`
  * `getFeatureGate(user: StatsigUser, gateName: string, options?: EvaluationOptions): FeatureGate`
  * `getParameterStore(user: StatsigUser, parameterStoreName: string, options?: EvaluationOptions): ParameterStore`
  * `getPrompt(user: StatsigUser, promptName: string, options?: EvaluationOptions): Prompt`
  * `getPromptSet(user: StatsigUser, promptSetName: string, options?: EvaluationOptions): PromptSet`
  * `logEvent(user: StatsigUser, eventName: string, value?: string | number | null, metadata?: Record<string, string>): void`
  * `forwardLogLineEvent(user: StatsigUser, level: string, message: string, metadata?: Record<string, string>): void`
  * `manuallyLogGateExposure(user: StatsigUser, gateName: string): void`
  * `manuallyLogDynamicConfigExposure(user: StatsigUser, configName: string): void`
  * `manuallyLogExperimentExposure(user: StatsigUser, experimentName: string): void`
  * `manuallyLogLayerParameterExposure(user: StatsigUser, layerName: string, parameterName: string): void`
  * `getClientInitializeResponse(user: StatsigUser, options?: ClientInitializeResponseOptions): ClientInitializeResponse`
  * `shutdown(): Promise<void>`
</Accordion>

<Accordion title="Fields Needed Methods">
  The following methods return information about which user fields are needed for evaluation:

  * `getGateFieldsNeeded(gateName: string): string[]`
  * `getDynamicConfigFieldsNeeded(configName: string): string[]`
  * `getExperimentFieldsNeeded(experimentName: string): string[]`
  * `getLayerFieldsNeeded(layerName: string): string[]`

  These methods return an array of strings representing the user fields that are required to properly evaluate the specified gate, config, experiment, or layer. This can be useful for:

  * Optimizing user object creation by only including necessary fields
  * Understanding which user attributes affect a particular feature
  * Debugging evaluation issues
</Accordion>


Built with [Mintlify](https://mintlify.com).