# Source: https://docs.statsig.com/client/Android.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Android Client SDK

> Statsig's SDK for Experimentation and Feature Flags in Java & Kotlin Android applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/android-sdk" target="_blank" rel="noreferrer">statsig-io/android-sdk</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    v4.37.1 and higher are published to only [Maven Central](https://central.sonatype.com/artifact/com.statsig/android-sdk). To install the SDK, set the Maven Central repository in your build.gradle.

    ```java  theme={null}
    dependencies {
        implementation "com.statsig:android-sdk:4.37.1"
    }
    ```

    Legacy versions (\<=V4.37.0) can be installed with [Jitpack](https://jitpack.io/#statsig-io/android-sdk).
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    <CodeGroup dropdown>
      ```java MainActivity.java theme={null}
      import com.statsig.androidsdk.*;
      ...

      public class MainActivity extends AppCompatActivity implements IStatsigCallback {

          ...
          StatsigOptions options = new StatsigOptions();
          options.setTier(Tier.PRODUCTION);
          StatsigUser user = new StatsigUser("UUID");
          Statsig.initializeAsync(app, "client-key", user, this, options);
          ...
          // SDK is usable, but values will be from the cache or defaults (false for gates, {} for configs)
          // Once onStatsigInitialize fires, then


          @Override
          public void onStatsigInitialize() {
              // SDK is initialized and has the most up to date values
          }

          @Override
          public void onStatsigUpdateUser() {
              // User has been updated and values have been refetched for the new user
          }

      }
      ```

      ```kotlin MainActivity.kt theme={null}
      import com.statsig.androidsdk.*

      ...

      async {
          Statsig.initialize(
              this.application,
              "my_client_sdk_key",
              StatsigUser("user_id"),
          )
      }.await()
      ```
    </CodeGroup>
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

<CodeGroup>
  ```java Java theme={null}
  DynamicConfig config = Statsig.getConfig("awesome_product_details");

  // The 2nd parameter is the default value to be used in case the given parameter name does not exist on
  // the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
  // value has not been cached on the client.
  String itemName = config.getString("product_name", "Awesome Product v1");
  Double price = config.getDouble("price", 10.0);
  Boolean shouldDiscount = config.getBoolean("discount", false);
  ```

  ```kotlin Kotlin theme={null}
  val config = Statsig.getConfig("awesome_product_details")

  // The 2nd parameter is the default value to be used in case the given parameter name does not exist on
  // the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
  // value has not been cached on the client.
  val itemName = config.getString("product_name", "Awesome Product v1")
  val price = config.getDouble("price", 10.0)
  val shouldDiscount = config.getBoolean("discount", false)
  ```
</CodeGroup>

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

<CodeGroup>
  ```java Java theme={null}
  if (Statsig.checkGate("new_homepage_design")) {
    // Gate is on, show new home page
  } else {
    // Gate is off, show old home page
  }
  ```

  ```kotlin Kotlin theme={null}
  if (Statsig.checkGate("new_homepage_design")) {
    // Gate is on, show new home page
  } else {
    // Gate is off, show old home page
  }
  ```
</CodeGroup>

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

<CodeGroup>
  ```java Java theme={null}
  // Values via getLayer

  Layer layer = Statsig.getLayer("user_promo_experiments")
  String promoTitle = layer.getString("title", "Welcome to Statsig!");
  Double discount = layer.getDouble("discount", 0.1);

  // or, via getExperiment

  DynamicConfig titleExperiment = Statsig.getExperiment("new_user_promo_title");
  DynamicConfig priceExperiment = Statsig.getExperiment("new_user_promo_price");

  String promoTitle = titleExperiment.getString("title", "Welcome to Statsig!");
  Double discount = priceExperiment.getDouble("discount", 0.1);

  ...

  Double price = msrp * (1 - discount);
  ```

  ```kotlin Kotlin theme={null}
  // Values via getLayer

  val layer = Statsig.getLayer("user_promo_experiments")
  val promoTitle = layer.getString("title", "Welcome to Statsig!")
  val discount = layer.getDouble("discount", 0.1)

  // or, via getExperiment

  val titleExperiment = Statsig.getExperiment("new_user_promo_title")
  val priceExperiment = Statsig.getExperiment("new_user_promo_price")

  val promoTitle = titleExperiment.getString("title", "Welcome to Statsig!")
  val discount = priceExperiment.getDouble("discount", 0.1)

  ...

  val price = msrp * (1 - discount);
  ```
</CodeGroup>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

<CodeGroup>
  ```java Java theme={null}
  Statsig.logEvent("purchase", 2.99, Map.of("item_name", "remove_ads"));
  ```

  ```kotlin Kotlin theme={null}
  Statsig.logEvent("purchase", 2.99, Map.of("item_name" to "remove_ads"))
  ```
</CodeGroup>

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

### Getting a Parameter Store

To fetch a set of parameters, use the following api:

<CodeGroup>
  ```java Java theme={null}
  ParameterStore homepageStore = Statsig.getParameterStore("homepage");
  ```

  ```kotlin Kotlin theme={null}
  val homepageStore = Statsig.getParameterStore("homepage")
  ```
</CodeGroup>

### Getting a parameter

You can then access parameters like this:

<CodeGroup>
  ```java Java theme={null}
  String title = homepageStore.getString(
      "title", //parameter name
      "Welcome" // default value
  );

  boolean shouldShowUpsell = homePageStore.getBoolean("upsell_upgrade_now", false);
  ```

  ```kotlin Kotlin theme={null}
  val title = homepageStore.getString(
    "title",   // parameter name
    "Welcome", // default value
  )

  val shouldShowUpsell = homepageStore.getBoolean("upsell_upgrade_now", false)
  ```
</CodeGroup>

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

<CodeGroup>
  ```java Java theme={null}
  StatsigUser newUser = new StatsigUser("new_user_id");
  Statsig.updateUserAsync(newUser, this); // this must implement IStatsigCallback

  ...

  @Override
  public void onStatsigUpdateUser() {
      // User has been updated and values have been refetched for the new user
  }
  ```

  ```kotlin Kotlin theme={null}
  Statsig.updateUser(StatsigUser("new_user_id"))
  ```
</CodeGroup>

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` and `user` during initialization to customize the Statsig client.

<ResponseField name="api" type="String" default="https://api.statsig.com/v1/">
  Default endpoint for all SDK network requests. Do not override unless you implement the Statsig API elsewhere.
</ResponseField>

<ResponseField name="disableCurrentActivityLogging" type="Boolean" default="false">
  Include the current top-level activity on logged events by default. Set to `true` to disable.
</ResponseField>

<ResponseField name="disableDiagnosticsLogging" type="Boolean" default="false" deprecated post={["deprecated"]}>
  Deprecated. Previously prevented the SDK from sending diagnostic information.
</ResponseField>

<ResponseField name="initTimeoutMs" type="Long" default="3000">
  Milliseconds to wait for the initial request before completing. Set to `0` to wait indefinitely.
</ResponseField>

<ResponseField name="enableAutoValueUpdate" type="Boolean" default="false">
  Periodically fetch updated values for the current user when enabled.
</ResponseField>

<ResponseField name="autoValueUpdateIntervalMinutes" type="Double" default="1.0">
  Frequency (in minutes) for auto value refresh. Minimum is `1` minute.
</ResponseField>

<ResponseField name="overrideStableID" type="String?" default="null">
  Override the SDK-generated `stableID` for the user.
</ResponseField>

<ResponseField name="loadCacheAsync" type="Boolean" default="false">
  Whether the SDK should block on loading saved values from disk.
</ResponseField>

<ResponseField name="initializeValues" type="Map<String, Any>?" default="null">
  Provide the initialize response directly to bootstrap the client synchronously. See NodeJS Server SDK for generating values and the Bootstrap docs.
</ResponseField>

<ResponseField name="disableHashing" type="Boolean?" default="false">
  When `true`, gate/config/experiment names are not hashed and remain readable. Requires special authorization from Statsig.
</ResponseField>

<ResponseField name="customCacheKey" type="((sdkKey: String, user: StatsigUser) -> String)">
  Override how the cache key is generated for stored values when the default does not fit your needs.
</ResponseField>

<ResponseField name="evaluationCallback" type="((config: BaseConfig) -> Unit)">
  Callback invoked whenever a gate, config, experiment, or layer is checked. Receives the evaluated `BaseConfig`.
</ResponseField>

<ResponseField name="lifetimeCallback" type="IStatsigLifetimeCallback?" default="null">
  Callbacks that may trigger multiple times over the lifetime of the client SDK.
  They will be called on the main thread.

  * `onValuesUpdated()` - called whenever the fired when new values are received and available for use. May be called after `Statsig.updateUser()`, `Statsig.updateUserAsync()`, or auto value updates (see `enableAutoValueUpdate` above)
</ResponseField>

#### Methods

* **setTier | setEnvironmentParameter | getEnvironment**
  * used to signal the environment tier the user is currently in.
  * `setTier` can be PRODUCTION, STAGING or DEVELOPMENT. e.g. passing in a value of `Tier.STAGING` will allow your users to pass any condition that pass for the staging environment tier, and fail any condition that only passes for other environment tiers.
  * `setEnvironmentParameter` can be used for custom tiers, eg `options.setEnvironmentParameter("tier", "test")`

#### Runtime Options

Starting in `V4.43.0`, a subset of options can be set during initialization and later updated while the Statsig client is running.

These options are defined in `StatsigRuntimeMutableOptions` (which `StatsigOptions` extends) and are detailed below.

Call `Statsig.updateRuntimeOptions(runtimeMutableOptions: StatsigRuntimeMutableOptions)` or the corresponding method in `StatsigClient` to update the Statsig client with new values.

* **loggingEnabled**: `Boolean`, default `true`
  * Setting this value to `false` will prevent the Statsig client from sending logging events over the network or saving events to its on-disk cache. The 1000 most recent events will be queued in memory. They can be logged to network (or cached) if `loggingEnabled` is set to `true` later during that session.
  * Calling `Statsig.flush()` after setting `loggingEnabled` to `true` will immediately clear the queue and minimize loss of older log events
  * This can be useful for cases where it is necessary for users to grant permission before events should be logged, or in any other cases where logging should not be enabled

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

<CodeGroup>
  ```java Java theme={null}
  Statsig.shutdown();
  ```

  ```kotlin Kotlin theme={null}
  Statsig.shutdown()
  ```
</CodeGroup>

## Using Persistent Evaluations

If you want to ensure that a user's variant stays consistent while an experiment is running, regardless of changes to allocation or targeting, you can use persistent storage. The Android SDK supports a minimal implementation using the keepDeviceValues flag, see the [Client Persistent Assignment Doc](/client/concepts/persistent_assignment#support-in-ios-and-android-sdks) for more info.

## Local Overrides

If you want to locally override gates/configs/experiments/layers for testing, Statsig offers convenient methods for a quick local override. Unless you call the remove method, these will be persisted session-to-session on the client's device. Note that these overrides only apply locally - they don't impact definitions in the console or elsewhere.

```kotlin  theme={null}
// Overrides the given gate to the specified value
overrideGate(gateName: String, value: Boolean)

// Overrides the given config (dynamic config or experiment) to the provided value
overrideConfig(configName: String, value: Map<String, Any>)

// Removes any overrides associated with the provided gate/config/experiment name
removeOverride(name: String)

// Removes all overrides
removeAllOverrides()

// Returns the set of gate and config overrides currently in place on the client
getAllOverrides(): StatsigOverrides

class StatsigOverrides(
    @SerializedName("gates")
    val gates: MutableMap<String, Boolean>,

    @SerializedName("configs")
    val configs: MutableMap<String, Map<String, Any>>
    ) {}
```

## Manual Exposures

<Warning>Manual logging is error-prone and can often introduce issues like uneven exposures, which compromise experiment results.</Warning>

You can query your gates/experiments without triggering an exposure, and manually log the exposures later:

<Tabs>
  <Tab title="Check Gate">
    To check a gate without an exposure being logged:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      val result = Statsig.checkGateWithExposureLoggingDisabled("a_gate_name")
      ```

      ```java Java theme={null}
      boolean result = Statsig.checkGateWithExposureLoggingDisabled("a_gate_name");
      ```
    </CodeGroup>

    Later, to manually log the gate exposure:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      Statsig.manuallyLogGateExposure("a_gate_name")
      ```

      ```java Java theme={null}
      Statsig.manuallyLogGateExposure("a_gate_name");
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Get Config">
    To get a dynamic config without an exposure being logged:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      val config = Statsig.getConfigWithExposureLoggingDisabled("a_config_name")
      ```

      ```java Java theme={null}
      DynamicConfig config = Statsig.getConfigWithExposureLoggingDisabled("a_config_name");
      ```
    </CodeGroup>

    Later, to manually log the config exposure:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      Statsig.manuallyLogConfigExposure("a_config_name")
      ```

      ```java Java theme={null}
      Statsig.manuallyLogConfigExposure("a_config_name");
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Get Experiment">
    To get an experiment without an exposure being logged:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      val experiment = Statsig.getExperimentWithExposureLoggingDisabled("an_experiment_name")
      ```

      ```java Java theme={null}
      DynamicConfig experiment = Statsig.getExperimentWithExposureLoggingDisabled("an_experiment_name");
      ```
    </CodeGroup>

    Later, to manually log the experiment exposure:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      Statsig.manuallyLogExperimentExposure("an_experiment_name", false)
      ```

      ```java Java theme={null}
      Statsig.manuallyLogExperimentExposure("an_experiment_name", false);
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Get Layer">
    To get a layer parameter without an exposure being logged:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      val layer = Statsig.getLayerWithExposureLoggingDisabled("a_layer_name", false)
      val result = layer.getString("a_parameter_name", "fallback")
      ```

      ```java Java theme={null}
      Layer layer = Statsig.getLayerWithExposureLoggingDisabled("a_layer_name");
      String result = layer.getString("a_parameter_name", "fallback");
      ```
    </CodeGroup>

    Later, to manually log the layer parameter exposure:

    <CodeGroup>
      ```kotlin Kotlin theme={null}
      Statsig.manuallyLogLayerParameterExposure("a_layer_name", "a_parameter_name", false)
      ```

      ```java Java theme={null}
      Statsig.manuallyLogLayerParameterExposure("a_layer_name", "a_parameter_name", false);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## StableID

Each client SDK has the notion of stableID, a devive-level identifier that is generated the first time the SDK is initialized and is stored locally for all future sessions. Unless storage is wiped (or app deleted), the stableID will not change.
This allows us to run device level experiments and experiments when other user identifiable information is unavailable (Logged out users).

```kotlin  theme={null}
// Retrieve the StableID
Statsig.getStableID(); 

// Override the StableID before initializing, if you have something you'd prefer to use instead
val opts = StatsigOptions(overrideStableID = "my_stable_id")
Statsig.initialize(app, "client-xyx", options = opts)
```

## Using multiple instances of the SDK

Up to this point, we've used the SDK's singleton. We also support creating multiples instances of the SDK - the `Statsig` singleton wraps a single instance of the SDK (typically called a `StatsigClient`) that you can instantiate.

<Note> You must use a different SDK key for each sdk instance you create for this to work. Various functionality of the Statsig client is keyed on the SDK key being used. Using the same key will lead to collisions. </Note>

All top level static methods from the singleton carry over as instance methods.  To create an instance of the Statsig sdk:

<CodeGroup>
  ```java Java theme={null}
  StatsigClient client = new StatsigClient();
  client.initializeAsync(application, sdkKey, user, callback, options);
  ```

  ```kotlin Kotlin theme={null}
  var client: StatsigClient = StatsigClient()
  client.initialize(application, sdkKey, user, options)
  ```
</CodeGroup>

## Initialize Response

The SDK provides a method to access the raw values that are used internally for gate, config, and layer value. This can be useful for debugging or for advanced use cases where you need to access the underlying data. For example, you can use these values to bootstrap another SDK, like the javascript SDK when you open an in-app browser.

The `getInitializeResponseJson` method returns an `ExternalInitializeResponse` object that contains:

1. A JSON string representation of the initialize response values
2. Evaluation details that provide metadata about how the values were obtained (network, cache, etc.)

<CodeGroup>
  ```java Java theme={null}
  // Get the raw values that the SDK is using internally to provide gate/config/layer results
  ExternalInitializeResponse response = Statsig.getInitializeResponseJson();

  // Get the JSON string representation of the initialize response
  String jsonValues = response.getInitializeResponseJSON();

  // Get the evaluation details
  EvaluationDetails details = response.getEvaluationDetails();
  ```

  ```kotlin Kotlin theme={null}
  // Get the raw values that the SDK is using internally to provide gate/config/layer results
  val response = Statsig.getInitializeResponseJson()

  // Get the JSON string representation of the initialize response
  val jsonValues = response.getInitializeResponseJSON()

  // Get the evaluation details
  val details = response.getEvaluationDetails()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).