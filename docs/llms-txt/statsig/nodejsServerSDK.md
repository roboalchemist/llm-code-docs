# Source: https://docs.statsig.com/server/nodejsServerSDK.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Legacy Node.js Server SDK

> Statsig's Legacy Server SDK for Node.js applications

[Github Repository](https://github.com/statsig-io/node-js-server-sdk)

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    The Node.js SDK is hosted [here](https://www.npmjs.com/package/statsig-node). You can install the SDK using NPM or Yarn:

    <CodeGroup>
      ```bash npm theme={null}
      npm install statsig-node
      ```

      ```bash yarn theme={null}
      yarn add statsig-node
      ```
    </CodeGroup>
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    ```javascript  theme={null}
    const Statsig = require("statsig-node");

    await Statsig.initialize(
      "server-secret-key",
      { environment: { tier: "staging" } } // optional, if not set, for >v6.0.0, sdk will default to be production  
    );
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```javascript  theme={null}
const user = {
  userID: '12345',
  email: '12345@gmail.com',
  ...
};

const showNewDesign = Statsig.checkGate(user, 'new_homepage_design');
if (showNewDesign) {
  // show new design here
} else {
  // show old design here
}
```

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

```javascript  theme={null}
const config = Statsig.getConfig(user, "awesome_product_details");

// The 2nd parameter is the default value to be used in case the given parameter name does not exist on
// the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
// value has not been cached on the client.
const itemName = config.get("product_name", "Awesome Product v1");
const price = config.get("price", 10.0);
const shouldDiscount = config.get("discount", false);
```

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```javascript  theme={null}
// Values via getLayer

const layer = Statsig.getLayer(user, "user_promo_experiments");
const promoTitle = layer.get("title", "Welcome to Statsig!");
const discount = layer.get("discount", 0.1);

// or, via getExperiment

const promoExperiment = Statsig.getExperiment(user, "new_user_promo");

const promoTitle = promoExperiment.get("title", "Welcome to Statsig!");
const discount = promoExperiment.get("discount", 0.1);

...

const price = msrp * (1 - discount);
```

## Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```javascript  theme={null}
const gate = Statsig.getFeatureGate(user, 'new_homepage_design');
console.log(gate.name); // 'new_homepage_design'
console.log(gate.value); // true or false
console.log(gate.ruleID); // rule ID that was evaluated
console.log(gate.evaluationDetails); // evaluation metadata
```

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```javascript  theme={null}
Statsig.logEvent(user, "add_to_cart", "SKU_12345", {
  price: "9.99",
  item_name: "diet_coke_48_pack",
});
```

Learn more about identifying users, group analytics, and best practices for logging events in the [logging events guide](/guides/logging-events).

## Statsig User

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to create targeting based on them.

Note that while typing is lenient on the `StatsigUser` object to allow you to pass in numbers, strings, arrays, objects, and potentially even enums or classes, the evaluation operators will only be able to operate on primitive types - mostly strings and numbers. While we attempt to smartly cast custom field types to match the operator, we cannot guarantee evaluation results for other types. For example, setting an array as a custom field will only ever be compared as a string - there is no operator to match a value in that array.

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

`initialize()` takes an optional parameter `options` in addition to the secret key that you can provide to customize the Statsig client. Here are the current options and we are always adding more to the list:

`initialize()` takes an optional parameter `options` in addition to the secret key that you can provide to customize the Statsig client. Here are the current options and we are always adding more to the list:

<ResponseField name="api" type="string" default="https://statsigapi.net/v1">
  The base url to use for all network requests. Defaults to the statsig API.
</ResponseField>

<ResponseField name="environment" type="StatsigEnvironment" default="null">
  An object you can use to set environment variables that apply to all of your users in the same session and will be used for targeting purposes.

  The most common usage is to set the environment tier ('production', 'staging' or 'development'), e.g. `{ tier: 'staging' }`, and have feature gates pass/fail for specific environments. Since v6.0.0 default environment tier is production
</ResponseField>

<ResponseField name="bootstrapValues" type="string" default="null">
  A string that represents all rules for all feature gates, dynamic configs and experiments. It can be provided to bootstrap the Statsig server SDK at initialization in case your server runs into network issue or Statsig server is down temporarily.
</ResponseField>

<ResponseField name="rulesUpdatedCallback" type="function" default="null">
  A callback function that's called whenever we have an update for the rules; it's called with a JSON string (used as is for `bootstrapValues` mentioned above) and a timestamp, like below:

  ```
  options.rulesUpdatedCallback(specsString, timeStamp)
  ```
</ResponseField>

<ResponseField name="logger" type="LoggerInterface" default="console.log">
  The logger interface to use for printing to stdout/stderr
</ResponseField>

<ResponseField name="localMode" type="boolean" default="false">
  Disables all network access, so the SDK will only return default (or overridden) values. Useful in testing.
</ResponseField>

<ResponseField name="initTimeoutMs" type="number" default="0">
  Sets a maximum time to wait for the config download network request to resolve before considering the SDK initialized and resolving the call to `initialize()`
</ResponseField>

<ResponseField name="dataAdapter" type="IDataAdapter" default="null">
  An adapter with custom storage behavior for config specs. Can be used to bootstrap Statsig server (takes priority over `bootstrapValues`). Can also be used to continuously fetch updates in place of the Statsig network. See [Data Stores](/server/concepts/data_store).

  For example, see our 1P implementation via Redis [statsig-node-redis](https://github.com/statsig-io/node-js-server-sdk-redis).
</ResponseField>

<ResponseField name="UserPersistentStorage" type="IUserPersistentStorage" default="nil">
  A persistent storage adapter for running sticky experiments. See [examples](/server/nodejsServerSDK#user-persistent-storage).
</ResponseField>

<ResponseField name="rulesetsSyncIntervalMs" type="number" default="10000">
  Sets the polling interval for the SDK to ask Statsig backend for changes on the rulesets.
</ResponseField>

<ResponseField name="idListsSyncIntervalMs" type="number" default="60000">
  Sets the polling interval for the SDK to ask Statsig backend for changes on the ID Lists.
</ResponseField>

<ResponseField name="loggingIntervalMs" type="number" default="60000">
  Sets the interval for the SDK to periodically flush all logging events to Statsig backend.
</ResponseField>

<ResponseField name="loggingMaxBufferSize" type="number" default="1000">
  Sets the maximum number of events the SDK's logger will batch before flushing them all to Statsig backend.
</ResponseField>

<ResponseField name="disableDiagnostics" type="boolean" default="false">
  Disables diagnostics events from being logged and sent to Statsig
</ResponseField>

<ResponseField name="initStrategyForIP3Country" type="'await' | 'lazy' | 'none'" default="'await'">
  Method of initializing IP to country lookup on `statsig.initialize()`.
</ResponseField>

<ResponseField name="initStrategyForIDLists" type="'await' | 'lazy' | 'none'" default="'await'">
  Method of initializing ID lists on `statsig.initialize()`.
</ResponseField>

<ResponseField name="postLogsRetryLimit" type="number" default="5">
  The maximum number of retry attempts when sending `/log_event` requests to Statsig server
</ResponseField>

<ResponseField name="postLogsRetryBackoff" type="number | (retry: number) => number" default="1000">
  A fixed number or callback on the retry attempt number to configure the time in ms to wait between each `/log_event` retry.

  If using a fixed number, a 10x multiplier will be applied on each subsequent retry
</ResponseField>

<ResponseField name="evaluationCallbacks" type="EvaluationCallbacks" default="{}">
  Provides callback functions for handling custom logic during evaluations of gates, dynamic configs, experiments, or layers. You can provide specific callbacks for each evaluation type to perform tasks such as custom logging (if you prefer not to use Statsig's default logging), or side effects.

  **Note:** if you'd like to turn off Statsig's default logging, set `disableExposureLogging: true` when making checks.

  Available callbacks:

  ```
  gateCallback?: (gate: FeatureGate, user: StatsigUser, event: LogEvent) => void;
  dynamicConfigCallback?: (config: DynamicConfig, user: StatsigUser, event: LogEvent) => void;
  experimentCallback?: (config: DynamicConfig, user: StatsigUser, event: LogEvent) => void;
  layerCallback?: (layer: Layer, user: StatsigUser) => void;
  layerParamCallback?: (layer: Layer, paramName: string, user: StatsigUser, event: LogEvent) => void;
  ```
</ResponseField>

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

```javascript  theme={null}
statsig.shutdown();
```

## Flush

To manually flush logged events:

```javascript  theme={null}
await statsig.flush();
```

## Client SDK Bootstrapping

The Statsig server SDK can be used to generate the initialization values for a client SDK. This is useful for server-side rendering (SSR) or when you want to pre-fetch values for a client.

```typescript  theme={null}
const values = Statsig.getClientInitializeResponse(user); // Record<string, unknown> | null

if (values != null) {
  // Bootstrap the Statsig React Client SDK
  return <StatsigSynchronousProvider initializeValues={values} ... />;
}
```

## Local Overrides

You can override the values returned by the SDK for testing purposes. This can be useful for local development when you want to test specific scenarios.

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Overrides the given gate to the specified value
  Statsig.overrideGate("a_gate_name", true, "a_user_id");
  	
  // Overrides the given config (dynamic config or experiment) to the provided value
  Statsig.overrideConfig("a_config_or_experiment_name", { key: "value" }, "a_user_id");
  	
  // Overrides the given layer to the provided value
  Statsig.overrideLayer("a_layer_name", { key: "value" }, "a_user_id");
  ```

  ```javascript JavaScript theme={null}
  // Overrides the given gate to the specified value
  Statsig.overrideGate("a_gate_name", true, "a_user_id");
  	
  // Overrides the given config (dynamic config or experiment) to the provided value
  Statsig.overrideConfig("a_config_or_experiment_name", { key: "value" }, "a_user_id");
  	
  // Overrides the given layer to the provided value
  Statsig.overrideLayer("a_layer_name", { key: "value" }, "a_user_id");
  ```
</CodeGroup>

These can be used to set an override for a specific user, or for all users (by not providing a specific user ID). Experiments/Autotune are overridden with the `overrideConfig` API.

### Overriding in getClientInitializeResponse

You can also override feature gates, dynamic configs, experiments, and layers when calling `getClientInitializeResponse`. This is useful when you need to provide specific values to the client SDK.

<CodeGroup>
  ```typescript TypeScript theme={null}
  // Get client initialize response with overrides
  const response = Statsig.getClientInitializeResponse(user, clientSDKKey, {
    overrides: {
      // Override feature gates
      featureGates: {
        'my_gate': true,  // Override gate value to true
      },
      
      // Override dynamic configs and experiments
      dynamicConfigs: {
        // Override config value directly
        'price_config': {
          value: { price: 9.99 }
        },
        
        // Override experiment by setting the group assignment
        'color_experiment': {
          groupName: 'Control'  // Uses the value for the Control group
        },
        
        // Override both value and group assignment
        'spacing_experiment': {
          value: { spacing: 64 },
          groupName: 'Variant_B'
        }
      },
      
      // Override layers
      layers: {
        'my_layer': {
          value: { param: 123 }
        }
      }
    }
  });
  ```

  ```javascript JavaScript theme={null}
  // Get client initialize response with overrides
  const response = Statsig.getClientInitializeResponse(user, clientSDKKey, {
    overrides: {
      // Override feature gates
      featureGates: {
        'my_gate': true,  // Override gate value to true
      },
      
      // Override dynamic configs and experiments
      dynamicConfigs: {
        // Override config value directly
        'price_config': {
          value: { price: 9.99 }
        },
        
        // Override experiment by setting the group assignment
        'color_experiment': {
          groupName: 'Control'  // Uses the value for the Control group
        },
        
        // Override both value and group assignment
        'spacing_experiment': {
          value: { spacing: 64 },
          groupName: 'Variant_B'
        }
      },
      
      // Override layers
      layers: {
        'my_layer': {
          value: { param: 123 }
        }
      }
    }
  });
  ```
</CodeGroup>

For experiments, you can override them in two ways:

1. By setting a `value` override on their dynamic config to directly specify the parameter values
2. By setting the `groupName` assignment to use the value for that group name (e.g., "Control" or "Test")

You can also combine both approaches to override both the group assignment and the parameter values.

## Manual Exposures

Statsig SDKs automatically log an exposure event every time a gate/experiment/config is checked. In some scenarios, you may want to control when to log an exposure.

You can disable the automatic logging like this:

### Gates

```javascript  theme={null}
const result = Statsig.checkGate(aUser, 'a_gate_name', {disableExposureLogging: true});
```

Then, to manually log the exposure:

```javascript  theme={null}
Statsig.manuallyLogGateExposure(aUser, 'a_gate_name');
```

### Dynamic Configs

```javascript  theme={null}
const config = Statsig.getConfigWithExposureLoggingDisabledSync(aUser, 'a_dynamic_config_name');
```

Then, to manually log the exposure:

```javascript  theme={null}
Statsig.manuallyLogConfigExposure(aUser, 'a_dynamic_config_name');
```

### Experiments

```javascript  theme={null}
const experiment = Statsig.getExperimentWithExposureLoggingDisabledSync(aUser, 'an_experiment_name');
```

Then, to manually log the exposure:

```javascript  theme={null}
Statsig.manuallyLogExperimentExposure(aUser, 'an_experiment_name');
```

### Layers

```javascript  theme={null}
const layer = Statsig.getLayerWithExposureLoggingDisabledSync(aUser, 'a_layer_name');
const paramValue = layer.get('a_param_name', 'fallback_value');
```

Then, to manually log the layer parameter exposure:

```javascript  theme={null}
Statsig.manuallyLogLayerParameterExposure(aUser, 'a_layer_name', 'a_param_name');
```

## Cloudflare Workers Setup

### Polling for updates

The SDK cannot poll for updates across requests since Cloudflare does not allow for timers.

To solve for this, a manual sync API is available for independently updating the SDK internal store.

```javascript  theme={null}
if (env.lastSyncTime < Date.now() - env.syncInterval) {
  env.lastSyncTime = Date.now();
  context.waitUntil(Statsig.syncConfigSpecs());
}
```

### Flushing events

The SDK enqueues logged events and flushes them in batches. In order to ensure events are properly flushed, we recommend calling `flush` using [`context.waitUntil`](https://developers.cloudflare.com/workers/runtime-apis/handlers/fetch/#contextwaituntil).
This will keep the request handler alive until events are flushed without blocking the response.

```javascript  theme={null}
context.waitUntil(Statsig.flush());
```

### Node.JS Compatibility

Many native JavaScript API and Node standard libraries can be accessed in Cloudflare via the [`nodejs_compat`](https://developers.cloudflare.com/workers/runtime-apis/nodejs/) compatibility flag.

The SDK is now compatible with `nodejs_compat` (since v5.16.0). In older versions, manual polyfilling is required.

## User Persistent Storage

User Persistent Storage is a storage adapter for running sticky experiments. It allows you to persist user assignments across sessions.

### Interface

```typescript  theme={null}
export interface IUserPersistentStorage {
  /**
   * Returns the full map of persisted values for a specific user key
   * @param key user key
   */
  load(key: string): UserPersistedValues;

  /**
   * Save the persisted values of a config given a specific user key
   * @param key user key
   * @param configName Name of the config/experiment
   * @param data Object representing the persistent assignment to store for the given user-config
   */
  save(key: string, configName: string, data: StickyValues): void;

  /**
   * Delete the persisted values of a config given a specific user key
   * @param key user key
   * @param configName Name of the config/experiment
   */
  delete(key: string, configName: string): void;
}
```

### Example Implementation

```typescript  theme={null}
class UserPersistentStorageExample implements IUserPersistentStorage {
  public store: Record<string, UserPersistedValues> = {};
  load(key: string): UserPersistedValues {
    return this.store[key];
  }
  save(key: string, configName: string, data: StickyValues): void {
    if (!(key in this.store)) {
      this.store[key] = {};
    }
    this.store[key][configName] = data;
  }
  delete(key: string, configName: string): void {
    delete this.store[key][configName];
  }
}
```

## Multi-Instance Usage

If you need to create multiple independent instances of the Statsig SDK (for example, to use different API keys or configurations), you can use the instance-based approach:

```javascript  theme={null}
// Statsig.initialize becomes:
const sdkInstance = new StatsigServer(secretKey, options);
await sdkInstance.initializeAsync();
```

## Forward Proxy Configuration

You can configure the SDK to use a forward proxy for network requests:

```javascript  theme={null}
const proxyAddress = "0.0.0.0:50051"
const options = {
      proxyConfigs: {
        'download_config_specs': {
          "proxyAddress": proxyAddress,
          "protocol": "grpc_websocket" as NetworkProtocol
        }
      }
    }
await Statsig.initialize(secretKey, options)
```

## FAQs

### How can I use the node SDK for server side rendering?

See [Client SDK Bootstrapping | SSR](#bootstrap)

### How can I mock Statsig for testing?

See [LocalOverrides](#local-overrides)

## Reference

### Type StatsigUser

```typescript  theme={null}
export type StatsigUser =
  // at least one of userID or customIDs must be provided
  ({ userID: string } | { customIDs: Record<string, string> }) & {
    userID?: string;
    customIDs?: Record<string, string>;
    email?: string;
    ip?: string;
    userAgent?: string;
    country?: string;
    locale?: string;
    appVersion?: string;
    custom?: Record<
      string,
      string | number | boolean | Array<string> | undefined
    >;
    privateAttributes?: Record<
      string,
      string | number | boolean | Array<string> | undefined
    > | null;
    statsigEnvironment?: StatsigEnvironment;
  }
```

### Type StatsigOptions

```typescript  theme={null}
export type StatsigOptions = {
  api: string;
  apiForDownloadConfigSpecs: string;
  apiForGetIdLists: string;
  bootstrapValues: string | null;
  environment: StatsigEnvironment | null;
  rulesUpdatedCallback: RulesUpdatedCallback | null;
  logger: LoggerInterface;
  localMode: boolean;
  initTimeoutMs: number;
  dataAdapter: IDataAdapter | null;
  rulesetsSyncIntervalMs: number;
  idListsSyncIntervalMs: number;
  loggingIntervalMs: number;
  loggingMaxBufferSize: number;
  disableDiagnostics: boolean;
  initStrategyForIP3Country: InitStrategy;
  initStrategyForIDLists: InitStrategy;
  postLogsRetryLimit: number;
  postLogsRetryBackoff: RetryBackoffFunc | number;
  disableRulesetsSync: boolean;
  disableIdListsSync: boolean;
  disableAllLogging: boolean;
};

export type RulesUpdatedCallback = (rulesJSON: string, time: number) => void;
export type RetryBackoffFunc = (retriesRemaining: number) => number;

export type StatsigEnvironment = {
  tier?: 'production' | 'staging' | 'development' | string;
  [key: string]: string | undefined;
};

export type InitStrategy = 'await' | 'lazy' | 'none';

export interface LoggerInterface {
  debug?(message?: any, ...optionalParams: any[]): void;
  info?(message?: any, ...optionalParams: any[]): void;
  warn(message?: any, ...optionalParams: any[]): void;
  error(message?: any, ...optionalParams: any[]): void;
  logLevel: 'none' | 'debug' | 'info' | 'warn' | 'error';
}
```

### Type FeatureGate

```typescript  theme={null}
export type FeatureGate = {
  readonly name: string;
  readonly ruleID: string;
  readonly idType: string | null;
  readonly value: boolean;
  readonly evaluationDetails: EvaluationDetails | null;
  readonly groupName: null; // deprecated
};
```

### Type DynamicConfig

```typescript  theme={null}
export default class DynamicConfig {
  name: string;
  value: Record<string, unknown>;
  get<T>(
    key: string,
    defaultValue: T,
    typeGuard: ((value: unknown) => value is T | null) | null = null,
  ): T;
  getValue(
    key: string,
    defaultValue?: boolean | number | string | object | Array<any> | null,
  ): unknown | null;
  getRuleID(): string;
  getGroupName(): string | null;
  getIDType(): string | null;
  getEvaluationDetails(): EvaluationDetails | null;
```

### Type Layer

```typescript  theme={null}
export default class Layer {
  name: string;
  public get<T>(
    key: string,
    defaultValue: T,
    typeGuard: ((value: unknown) => value is T) | null = null,
  ): T;
  getValue(
    key: string,
    defaultValue?: boolean | number | string | object | Array<any> | null,
  ): unknown | null;
  getRuleID(): string;
  getGroupName(): string | null;
  getAllocatedExperimentName(): string | null;
  getEvaluationDetails(): EvaluationDetails | null;
```

### DataAdapter

```typescript  theme={null}
export interface IDataAdapter {
  get(key: string): Promise<AdapterResponse>;
  set(key: string, value: string, time?: number): Promise<void>;
  initialize(): Promise<void>;
  shutdown(): Promise<void>;
  supportsPollingUpdatesFor(key: DataAdapterKey): boolean;
}
```

### EvaluationDetails

```typescript  theme={null}
export class EvaluationDetails {
  readonly configSyncTime: number;
  readonly initTime: number;
  readonly serverTime: number;
  readonly reason: EvaluationReason;
}
```

### EvaluationReason

```typescript  theme={null}
export type EvaluationReason =
  | 'Network'
  | 'LocalOverride'
  | 'Unrecognized'
  | 'Uninitialized'
  | 'Bootstrap'
  | 'DataAdapter'
  | 'Unsupported';
```


Built with [Mintlify](https://mintlify.com).