# Source: https://docs.statsig.com/client/jsOnDeviceEvaluationSDK.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JavaScript On-Device Evaluation Client SDK

> Statsig's JavaScript SDK for on-device evaluation with browser and Node.js applications.

export const StatsigUserNotes = ({sdkName}) => <>
    {sdkName && <Note>
        For the {sdkName} On-Device Evaluation SDK, you pass the `StatsigUser` object {sdkName === "JavaScript" ? "into" : "directly into"} each evaluation method (`checkGate`, `getConfig`, etc.) rather than during initialization.
      </Note>}
    
    <Note>
      Unlike precomputed evaluation SDKs, the on-device evaluation SDK does not have an `updateUser` method since it evaluates gates/configs/experiments in real-time for any user object you pass in.
    </Note>
  </>;

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/js-client-monorepo" target="_blank" rel="noreferrer">statsig-io/js-client-monorepo</a>
</Callout>

<Info>
  Statsig's normal (remote evaluation) SDKs are recommended for most client applications. Understand the use case and privacy risks by reading the [On-Device Eval SDK overview](/client/onDevice). On-device evaluation SDKs are for Enterprise & Pro Tier only.
</Info>

These SDKs use a different paradigm than their precomputed counterparts: [JS](/client/javascript-sdk), [Android](/client/Android), [iOS](/client/iosClientSDK), they behave more like Server SDKs. Rather than requiring a user up front, you can check gates/configs/experiments for any set of user properties, because the SDK downloads a complete representation of your project and evaluates checks in real time.

### Pros

* No need for a network request when changing user properties - just check the gate/config/experiment locally
* Can bring your own CDN or synchronously initialize with a preloaded project definition
* Lower latency to download configs cached at the edge, rather than evaluated for a given user (which cannot be cached as much)

### Cons

* Entire project definition is available client side - the names and configurations of all experiments and feature flags accessible by your client key are exposed. See our [client key with server permission best practices](/sdk-keys/api-keys/#client-keys-with-server-permissions)
* Payload size is strictly larger than what is required for the traditional SDKs
* Evaluation performance is slightly slower - rather than looking up the value, the SDK must actually evaluate targeting conditions and an allocation decision
* Does not support ID list segments with > 1000 IDs
* Does not support IP or User Agent based checks (Browser Version/Name, OS Version/Name, IP, Country)

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    You can install the Statsig SDK via npm, yarn or jsdelivr:

    <CodeGroup>
      ```bash npm theme={null}
      npm install @statsig/js-on-device-eval-client
      ```

      ```bash yarn theme={null}
      yarn add @statsig/js-on-device-eval-client
      ```

      ```html CDN / <script> theme={null}
      <script src="https://cdn.jsdelivr.net/npm/@statsig/js-on-device-eval-client@1/build/statsig-js-on-device-eval-client.min.js"></script>
      ```
    </CodeGroup>

    Statsig is hosted on the [jsDelivr](https://www.jsdelivr.com/package/npm/@statsig/js-client) CDN.

    To access the current primary JavaScript bundle, use:

    `https://cdn.jsdelivr.net/npm/@statsig/js-client/build/statsig-js-client.min.js`

    To access specific files/versions:

    `https://cdn.jsdelivr.net/npm/@statsig/js-client@{version}/build/statsig-js-client.min.js`
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    <Warning>
      For On-Device Evaluation, you'll need to add the **"Allow Download Config Specs"** scope. Client keys, by default, are not able to download the project definition for on-device evaluation.

      While client keys are safe to include, Server and Console keys should always be kept private.
    </Warning>

    <Accordion title="How to add the scope">
      <Tabs>
        <Tab title="New SDK Keys">
          When creating a new client key, select **"Allow Download Config Specs"**

                    <img src="https://mintcdn.com/statsig-4b2ff144/XaVHbHME-WzKzCBE/images/local-eval/new-keys.png?fit=max&auto=format&n=XaVHbHME-WzKzCBE&q=85&s=b0ade9e04869ad975bcc6dab7c3ffe69" alt="Add DCS Scope to New Key" width="504" height="532" data-path="images/local-eval/new-keys.png" />
        </Tab>

        <Tab title="Existing SDK Keys">
          To add the scope to an existing key, under **Project Settings** → **API Keys** → **Client API Keys**, select **Actions** → **Edit Scopes**, and select **"Allow Download Config Specs"**, then **Save**.

                    <img src="https://mintcdn.com/statsig-4b2ff144/XaVHbHME-WzKzCBE/images/local-eval/existing-keys.png?fit=max&auto=format&n=XaVHbHME-WzKzCBE&q=85&s=0c3e94902e5e525b3cdb21e10cc0d299" alt="Add DCS Scope to Existing Key" width="501" height="264" data-path="images/local-eval/existing-keys.png" />
        </Tab>
      </Tabs>
    </Accordion>

    ```typescript  theme={null}
    import { StatsigOnDeviceEvalClient } from '@statsig/js-on-device-eval-client';

    const myStatsigClient = new StatsigOnDeviceEvalClient(
      YOUR_CLIENT_KEY, 
      { environment: {tier: 'development'} }
    );

    // initialize and wait for the latest values
    await myStatsigClient.initializeAsync();
    ```

    <Note>
      In advanced use cases, you may want to Prefetch or Bootstrap (Provide) values for initialization. See [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter) to learn how this can be achieved.
    </Note>
  </Step>
</Steps>

## Working with the SDK

## Setup a StatsigUser

To interact with the SDK, you will need to create a `StatsigUser` object. The full definition of this
object can be found [here](#statsig-user).

```typescript  theme={null}
const myUser = {
    userID: "a-user",
    email: "user@statsig.com"
};
```

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

```typescript  theme={null}
if (myStatsigClient.checkGate("new_homepage_design", myUser)) {
  // Gate is on, show new home page
} else {
  // Gate is off, show old home page
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```typescript  theme={null}
const dynamicConfig = myStatsigClient.getDynamicConfig("awesome_product_details", myUser);
const itemName = dynamicConfig.value["product_name"] ?? "Some Fallback";
const price = dynamicConfig.value["price"] ?? 10.0;

if (dynamicConfig.value["is_discount_enabled"] === true) {
  // apply some discount logic
}
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```typescript  theme={null}
// Values via getLayer
const layer = myStatsigClient.getLayer("user_promo_experiments", myUser);
const promoTitle = layer.get("title") ?? "Welcome to Statsig!";
const discount = layer.get("discount") ?? 0.1;

// or, via getExperiment
const titleExperiment = myStatsigClient.getExperiment("new_user_promo_title", myUser);
const priceExperiment = myStatsigClient.getExperiment("new_user_promo_price", myUser);

const promoTitle = titleExperiment.value["title"] ?? "Welcome to Statsig!";
const discount = priceExperiment.value["discount"] ?? 0.1;
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

```typescript  theme={null}
import type { StatsigEvent } from '@statsig/client-core';

// log a simple event
myStatsigClient.logEvent('my_simple_event');

// or, include more information by using a StatsigEvent object
const myEvent: StatsigEvent = {
  eventName: 'add_to_cart',
  value: 'SKU_12345',
  metadata: {
    price: '9.99',
    item_name: 'diet_coke_48_pack',
  },
};

myStatsigClient.logEvent(myEvent);
```

### Code Examples

Working sample apps are available in the repository:

* [JavaScript & TypeScript Examples](https://github.com/statsig-io/js-client-monorepo/tree/main/samples)

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

<StatsigUserNotes sdkName="JavaScript" />

## Client Event Emitter

It is possible to subscribe to StatsigClientEvents (Not to be confused with [StatsigEvent](#logging-an-event)). These events occur at various stages while using the Statsig client.
You can subscribe to specific events by specifying the StatsigClientEvent name, or, all events by using the wildcard token `'*'`.

```typescript  theme={null}
import type {
  AnyStatsigClientEvent,
  StatsigClientEvent,
  StatsigClientEventCallback,
} from '@statsig/client-core';

const onAnyClientEvent = (event: AnyStatsigClientEvent) => {
  console.log("Any Client Event", event);
};

const onLogsFlushed = (event: StatsigClientEvent<'logs_flushed'>) => {
  console.log("Logs", event.events);
};

// subscribe to an individual StatsigClientEvent
myStatsigClient.on('logs_flushed', onLogsFlushed);

// or, subscribe to all StatsigClientEvents
myStatsigClient.on('*', onAnyClientEvent);

// then later, unsubscribe from the events
myStatsigClient.off('logs_flushed', onLogsFlushed);
myStatsigClient.off('*', onAnyClientEvent);
```

The full list of events and descriptions can be found [here](https://github.com/statsig-io/js-client-monorepo/blob/main/packages/client-core/src/StatsigClientEventEmitter.ts).

## Statsig Options

You can configure certain aspects of the SDKs behavior by passing a StatsigOptions object during initialization.

<ResponseField name="api" type="string">
  The API to use for all SDK network requests. You should not need to override this unless you have another API that implements the Statsig API endpoints.
</ResponseField>

<ResponseField name="logEventUrl" type="string">
  The URL used to flush queued events via a POST request. Takes precedence over `StatsigOptions.api`.
</ResponseField>

<ResponseField name="logEventBeaconUrl" type="string">
  The URL used to flush queued events via `window.navigator.sendBeacon` (web only). Takes precedence over `StatsigOptions.api`.
</ResponseField>

<ResponseField name="downloadConfigSpecsUrl" type="string" default="https://api.statsigcdn.com/v1/download_config_specs">
  The URL used to fetch your latest Statsig specifications. Takes precedence over `StatsigOptions.api`.
</ResponseField>

<ResponseField name="environment" type="StatsigEnvironment">
  An object you can use to set environment variables that apply to all of your users in the same session.
</ResponseField>

<ResponseField name="overrideStableID" type="string">
  Overrides the auto-generated stableID that is set for the device.
</ResponseField>

<ResponseField name="logLevel" type="LogLevel" default="LogLevel.Warn">
  How much information is allowed to be printed to the console.
</ResponseField>

<ResponseField name="dataAdapter" type="SpecsDataAdapter" default="StatsigSpecsDataAdapter">
  Implementing this type allows customization of the initialization. See [Using SpecsDataAdapter](/client/js-on-device-eval-client/using-evaluations-data-adapter) to learn more.
</ResponseField>

<ResponseField name="networkTimeoutMs" type="number" default="10,000">
  The maximum amount of time (in milliseconds) that any network request can take before timing out.
</ResponseField>

<ResponseField name="loggingBufferMaxSize" type="number" default="50">
  The maximum number of events to batch before flushing logs to Statsig.
</ResponseField>

<ResponseField name="loggingIntervalMs" type="number" default="10,000">
  How often (in milliseconds) to flush logs to Statsig.
</ResponseField>

<ResponseField name="overrideAdapter" type="OverrideAdapter">
  An implementor of `OverrideAdapter`, used to alter evaluations before its returned to the caller of a check api (checkGate/getExperiment etc).
</ResponseField>

## Manual Exposures

<Warning>Manual logging is error-prone and can often introduce issues like uneven exposures, which compromise experiment results.</Warning>

You can query your gates/experiments without triggering an exposure, and manually log the exposures later:

### Gates

```typescript  theme={null}
// Check gate with exposure disabled
const result = myStatsigClient.checkGate('a_gate_name', { user, disableExposureLog: true });

// Manually log the exposure
myStatsigClient.checkGate('a_gate_name', { user });
```

### Configs

```typescript  theme={null}
// Get config with exposure disabled
const config = myStatsigClient.getConfig('a_dynamic_config_name', { user, disableExposureLog: true });

// Manually log the exposure
myStatsigClient.getConfig('a_dynamic_config_name', { user });
```

### Experiments

```typescript  theme={null}
// Get experiment with exposure disabled
const experiment = myStatsigClient.getExperiment('an_experiment_name', { user, disableExposureLog: true });

// Manually log the exposure
myStatsigClient.getExperiment('an_experiment_name', { user });
```

### Layers

```typescript  theme={null}
// Get layer with exposure disabled
const layer = myStatsigClient.getLayer('a_layer_name', { user, disableExposureLog: true });
const paramValue = layer.get('a_param_name', 'fallback_value');

// Manually log the exposure
const layer = myStatsigClient.getLayer('a_layer_name', { user });
const paramValue = layer.get('a_param_name', 'fallback_value');
```

## Lifecycle & Advanced Usage

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

```typescript  theme={null}
await myStatsigClient.shutdown();
```

## Data Adapter

The `EvaluationsDataAdapter` type outlines how the `StatsigClient` should fetch and cache data during initialize and update operations.
By default, the `StatsigClient` uses `StatsigEvaluationsDataAdapter`, a Statsig provided implementor of the `EvaluationsDataAdapter` type. `StatsigEvaluationsDataAdapter`
provides ways to fetch data synchronously from Local Storage and asynchronously from Statsig's servers.
See [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter) to learn more and see example usage.

## FAQs

#### Does the SDK use the browser local storage or cookies? If so, for what purposes?

The SDK does not use any cookies.

It does use the local storage for feature targeting and experimentation purposes only. Values for feature gates, dynamic configs and experiments are cached in the local storage, which are used as a backup in the event that your website/app cannot reach the Statsig server to fetch the latest values. If any events were logged but could not be sent to Statsig server due to issues like network failure, we also save them in the local storage to be sent again when network restores.

<AccordionGroup>
  <Accordion title="Does the SDK use the browser local storage or cookies? If so, for what purposes?">
    The SDK does not use any cookies.

    It does use the local storage for feature targeting and experimentation purposes only. Values for feature gates, dynamic configs and experiments are cached in the local storage, which are used as a backup in the event that your website/app cannot reach the Statsig server to fetch the latest values. If any events were logged but could not be sent to Statsig server due to issues like network failure, we also save them in the local storage to be sent again when network restores.
  </Accordion>

  <Accordion title="How do I run experiments for logged out users?">
    See the guide on [device level experiments](/guides/first-device-level-experiment).
  </Accordion>
</AccordionGroup>

## Additional Resources

* [On-Device Evaluation SDK Overview](/client/onDevice)
* [Client Keys with Server Permissions](/sdk-keys/api-keys/#client-keys-with-server-permissions)
* [Using EvaluationsDataAdapter](/client/javascript/using-evaluations-data-adapter)
* [Debugging SDK Evaluations](/sdk/debugging)


Built with [Mintlify](https://mintlify.com).