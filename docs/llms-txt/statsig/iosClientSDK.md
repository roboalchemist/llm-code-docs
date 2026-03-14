# Source: https://docs.statsig.com/client/iosClientSDK.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# iOS/tvOS/macOS Client SDK

> Statsig's SDK for Experimentation and Feature Flags in iOS, tvOS, and macOS applications.

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    To use the SDK in your project, you must add Statsig as a dependency.

    <Tabs>
      <Tab title="Swift Package Manager">
        In your Xcode, select File > Swift Packages > Add Package Dependency
        and enter the URL [https://github.com/statsig-io/statsig-kit.git](https://github.com/statsig-io/statsig-kit.git).

        You can also include it directly in your project's Package.swift. Find out the latest release version on our [GitHub page](https://github.com/statsig-io/statsig-kit/releases).

        ```swift  theme={null}
        //...
        dependencies: [
            // see the latest version on https://github.com/statsig-io/statsig-kit/releases
            .package(url: "https://github.com/statsig-io/statsig-kit.git", .upToNextMinor("X.Y.Z")),
        ],
        //...
        targets: [
            .target(
                name: "YOUR_TARGET",
                dependencies: ["Statsig"]
            )
        ],
        //...
        ```
      </Tab>

      <Tab title="Cocoapods">
        If you are using CocoaPods, our pod name is 'Statsig', and you can include the following line to your Podfile:

        ```ruby  theme={null}
        use_frameworks!
        target 'TargetName' do
          //...
          pod 'Statsig', '~> X.Y.Z'
        end
        ```

        Find the latest versions by searching [cocoapods.org](https://cocoapods.org/) or on [Github](https://github.com/statsig-io/statsig-kit/releases).
      </Tab>
    </Tabs>
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    <CodeGroup>
      ```swift Swift theme={null}
      Statsig.initialize(
          sdkKey: "my_client_sdk_key",
          user: StatsigUser(userID: "my_user_id"),
          options: StatsigOptions(environment: StatsigEnvironment(tier: .Staging)))
      { error in

        // Statsig has finished fetching the latest feature gate and experiment values for your user.
        // If you need the most recent values, you can get them now.

        // You can also check error.message and error.code for any debugging information.

      }
      ```

      ```objective-c Objective C theme={null}
      StatsigUser *user = [[StatsigUser alloc] initWithUserID:@"my_user_id"];
      [Statsig initializeWithSDKKey:@"my_client_sdk_key" user:user completion:^(StatsigClientError * error) {
        // Statsig has finished fetching the latest feature gate and experiment values for your user.
        // If you need the most recent values, you can get them now.

        // You can also check error.message and error.code for any debugging information.
      }];
      ```
    </CodeGroup>

    The completion block is called after the network request to fetch the latest feature gate and experiment values for your user.
    If you try to get any value before the completion block is called, you could get either the cached value from the previous session,
    or the default value. If you need the latest value, please wait for the completion block to be called first.

    <Warning>
      **Avoid iOS 18.4 on Simulator**: Apple introduced a networking bug in iOS 18.4 that causes requests to fail when running in the Simulator. For more details, see [this thread on Apple's forums](https://developer.apple.com/forums/thread/777999).
    </Warning>
  </Step>
</Steps>

## Use the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's check a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

<CodeGroup>
  ```swift Swift theme={null}
  if Statsig.checkGate("new_homepage_design") {
    // Gate is on, show new home page
  } else {
    // Gate is off, show old home page
  }
  ```

  ```objective-c Objective C theme={null}
  if ([Statsig checkGateForName:@"new_homepage_design"]) {
    // Gate is on, show new home page
  } else {
    // Gate is off, show old home page
  }
  ```
</CodeGroup>

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, **Dynamic Configs** can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

<CodeGroup>
  ```swift Swift theme={null}
  let config = Statsig.getConfig("awesome_product_details")

  // The 2nd parameter is the default value to be used in case the given parameter name does not exist on
  // the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
  // value has not been cached on the client.
  let itemName = config.getValue(forKey: "product_name", defaultValue: "Awesome Product v1")
  let price = config.getValue(forKey: "price", defaultValue: 10.0)
  let shouldDiscount = config.getValue(forKey: "discount", defaultValue: false)
  ```

  ```objective-c Objective C theme={null}
  DynamicConfig *config = [Statsig getConfigForName:@"awesome_product_details"];

  // The 2nd parameter is the default value to be used in case the given parameter name does not exist on
  // the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
  // value has not been cached on the client.
  NSString *itemName = [config.getStringForKey:@"product_name" defaultValue:@"Awesome Product v1"];
  double price = [config getDoubleForKey:@"price" defaultValue:10.0];
  BOOL shouldDiscount = [config getBoolForKey:@"discount" defaultValue:false];
  ```
</CodeGroup>

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

<CodeGroup>
  ```swift Swift theme={null}
  // Values via getLayer

  let layer = Statsig.getLayer("user_promo_experiments")
  let promoTitle = layer.getValue(forKey: "title", defaultValue: "Welcome to Statsig!")
  let discount = layer.getValue(forKey: "discount", defaultValue: 0.1)

  // or, via getExperiment

  let titleExperiment = Statsig.getExperiment("new_user_promo_title")
  let priceExperiment = Statsig.getExperiment("new_user_promo_price")

  let promoTitle = titleExperiment.getValue(forKey: "title", defaultValue: "Welcome to Statsig")
  let discount = priceExperiment.getValue(forKey: "discount", defaultValue: 0.1)

  ...

  let price = msrp * (1 - discount);
  ```

  ```objective-c Objective C theme={null}
  DynamicConfig *expConfig = [Statsig getExperimentForName:@"new_user_promo"];

  NSString *promoTitle = [expConfig.getStringForKey:@"title" defaultValue:@"Welcome to Statsig! Use discount code WELCOME10OFF for 10% off your first purchase!"];
  double discount = [expConfig getDoubleForKey:@"discount" defaultValue:0.1];

  double price = msrp * (1 - discount);
  ```
</CodeGroup>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API for the event, and you can additionally provide some value and/or an object of metadata to be logged together with the event:

<CodeGroup>
  ```swift Swift theme={null}
  Statsig.logEvent(withName: "purchase", value: 2.99, metadata: ["item_name": "remove_ads"])
  ```

  ```objective-c Objective C theme={null}
  [Statsig logEvent:@"purchase" doubleValue:2.99 metadata:@{ @"item_name" : @"remove_ads" }];
  ```
</CodeGroup>

## Parameter Stores

Parameter Stores hold a set of parameters for your mobile app. These parameters can be remapped on-the-fly from a static value to a Statsig entity (Feature Gates, Experiments, and Layers), so you can decouple your code from the configuration in Statsig. Read more about Param Stores [here](/client/concepts/parameter-stores).

## Statsig User

You need to provide a StatsigUser object to check/get your configurations. You should pass as much
information as possible in order to take advantage of advanced gate and config conditions.

Most of the time, the `userID` field is needed in order to provide a consistent experience for a given
user (see [logged-out experiments](/guides/first-device-level-experiment) to understand how to correctly run experiments for logged-out
users).

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on
StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to
create targeting based on them.

Once the user logs in or has an update/changed, make sure to call `updateUserWithResult`
with the updated `userID` and/or any other updated user attributes:

<CodeGroup>
  ```swift Swift theme={null}
  let user = StatsigUser(
    userID: "a-user-id",
    email: "user@example.com",
    ip: "192.168.1.1",
    userAgent: "Mozilla/5.0",
    country: "US",
    locale: "en_US",
    appVersion: "1.0.0",
    custom: [
      "plan": "premium",
      "age": 25
    ],
    customIDs: [
      "stableID": "stable-id-123"
    ],
    privateAttributes: [
      "email": "private@example.com"
    ]
  )
  ```

  ```objective-c Objective C theme={null}
  StatsigUser *user = [[StatsigUser alloc] initWithUserID:@"a-user-id"];
  user.email = @"user@example.com";
  user.ip = @"192.168.1.1";
  user.userAgent = @"Mozilla/5.0";
  user.country = @"US";
  user.locale = @"en_US";
  user.appVersion = @"1.0.0";
  user.custom = @{ @"plan": @"premium", @"age": @25 };
  user.customIDs = @{ @"stableID": @"stable-id-123" };
  user.privateAttributes = @{ @"email": @"private@example.com" };
  ```
</CodeGroup>

## Statsig Options

<ResponseField name="initTimeout" type="Double" default="3.0">
  Used to decide how long the Statsig client waits for the initial network request to respond before calling the completion block. The Statsig client will return either cached values (if any) or default values if checkGate/getConfig/getExperiment is called before the initial network request completes.

  If you always want to wait for the latest values fetched from Statsig server, you should set this to 0 so we do not timeout the network request.
</ResponseField>

<ResponseField name="disableCurrentVCLogging" type="Bool" default="false">
  By default, any custom event your application logs with `Statsig.logEvent()` includes the current root View Controller. This is so we can generate user journey funnels for your users. You can set this parameter to true to disable this behavior.
</ResponseField>

<ResponseField name="printHandler" type="((String) -> Void)?" default="nil">
  A handler for log messages from the SDK. If not provided, logs will be printed to the console.

  The handler receives the message string that would otherwise be printed to the console.

  Useful for redirecting logs to your own logging system, suppressing unnecessary console output, or debugging issues with the SDK.
</ResponseField>

<ResponseField name="environment" type="StatsigEnvironment" default="nil">
  StatsigEnvironment is a class for you to set environment variables that apply to all of your users in the same session and will be used for targeting purposes.

  e.g. passing in a value of `StatsigEnvironment(tier: .Staging)` will allow your users to pass any condition that pass for the staging environment tier, and fail any condition that only passes for other environment tiers.
</ResponseField>

<ResponseField name="evaluationCallback" type="EvaluationCallbackData" default="nil">
  EvaluationCallback provides a callback when an evaluation is made against one of your configurations (gate, dynamic config, experiment, layer and parameter stores). This is useful when you want to trigger specific actions or log evaluations based on the results received from Statsig.

  To use the EvaluationCallback, you need to provide a callback function during the SDK initialization via the StatsigOptions. The callback is invoked every time an evaluation occurs for feature gates, dynamic configs, experiments, layers, or parameter stores.

  The EvaluationCallbackData enum defines the different types of data that can be returned in the evaluationCallback when the Statsig iOS SDK evaluates feature gates, dynamic configs, experiments, layers, or parameter stores.

  Here is the structure of the enum:

  ```swift  theme={null}
     public enum EvaluationCallbackData {
        case gate (FeatureGate)
        case config (DynamicConfig)
        case experiment (DynamicConfig)
        case layer (Layer)
        case parameterStore (ParameterStore)
     }
  ```

  Here's an example of how to set up an evaluation callback:

  ```swift  theme={null}
      func callback(data: StatsigOptions.EvaluationCallbackData) {
         switch data {
         case .gate(let gate):
            // Handle gate evaluation
         case .config(let config):
            // Handle dynamic config evaluation
         case .experiment(let experiment):
            // Handle experiment evaluation
         case .layer(let layer):
            // Handle layer evaluation
         case .parameterStore(let paramStore):
            // Handle parameter store evaluation
         }
      }

      let opts = StatsigOptions(evaluationCallback: callback)
      Statsig.initialize(sdkKey: "client-key", options: opts)
  ```
</ResponseField>

<ResponseField name="storageProvider" type="StorageProvider" default="nil">
  Allows users to implement their own caching strategy by passing an object that conforms to the `StorageProvider` protocol.

  Default cache key: `com.statsig.cache`

  ```swift  theme={null}
     @objc public protocol StorageProvider {
        @objc func read(_ key: String) -> Data?
        @objc func write(_ value: Data, _ key: String)
        @objc func remove(_ key: String)
     }
  ```
</ResponseField>

<ResponseField name="overrideStableID" type="String" default="nil">
  Overrides the auto generated StableID that is set for the device.
</ResponseField>

<ResponseField name="enableCacheByFile" type="Bool" default="false">
  Use file caching instead of UserDefaults. Useful if you are running into size limits with UserDefaults (ie tvOS).
</ResponseField>

<ResponseField name="eventLoggingEnabled" type="Bool" default="true">
  Controls whether the SDK sends events over the network. Useful when user consent is needed before sending events. The iOS SDK stores up to 1MB of unsent request payloads
</ResponseField>

<ResponseField name="initializeValues" type="[String: Any]" default="nil">
  Provide a Dictionary representing the "initialize response" required to synchronously initialize the SDK.
  This value can be obtained from a Statsig server SDK and used to [Bootstrap](/client/concepts/initialize/#2-bootstrap-initialization) the SDK when initializing.
</ResponseField>

<ResponseField name="disableDiagnostics" type="Bool" default="false">
  Prevent the SDK from sending useful debug information to Statsig.
</ResponseField>

<ResponseField name="disableHashing" type="Bool" default="false">
  When disabled, the SDK will not hash gate/config/experiment names, instead they will be readable as plain text.

  <Info>
    This requires special authorization from Statsig. Reach out to our support team, your sales contact, or via our [Slack community](https://statsig.com/slack) if you want this enabled.
  </Info>
</ResponseField>

<ResponseField name="shutdownOnBackground" type="Bool" default="true">
  The SDK automatically shuts down when an app is put into the background.
  If you need to use the SDK while your app is in the background, set this to false.
</ResponseField>

<ResponseField name="initializationURL" type="URL" default="nil">
  Override the URL used to initialize the SDK. Learn more at [https://docs.statsig.com/custom\_proxy](https://docs.statsig.com/custom_proxy)

  ```swift  theme={null}
     StatsigOptions(initializationURL: URL(string: "https://example.com/setup"))
  ```
</ResponseField>

<ResponseField name="eventLoggingURL" type="URL" default="nil">
  Override the URL used to log events. Learn more at [https://docs.statsig.com/custom\_proxy](https://docs.statsig.com/custom_proxy)

  ```swift  theme={null}
     StatsigOptions(eventLoggingURL: URL(string: "https://example.com/info"))
  ```
</ResponseField>

## StableID

Each client SDK has the notion of stableID, a devive-level identifier that is generated the first time the SDK is initialized and is stored locally for all future sessions. Unless storage is wiped (or app deleted), the stableID will not change.
This allows us to run device level experiments and experiments when other user identifiable information is unavailable (Logged out users).

<CodeGroup>
  ```swift Swift theme={null}
  let options = StatsigOptions(overrideStableID: "my_stable_id")
  Statsig.initialize(sdkKey: "client-xyz", options: options)
  ```

  ```objective-c Objective C theme={null}
  StatsigOptions *options = [[StatsigOptions alloc] init];
  options.overrideStableID = @"my_stable_id";
  [Statsig initializeWithSDKKey:@"client-xyz" user:nil options:options completion:nil];
  ```
</CodeGroup>

## Manual Exposures

<Warning>Manual logging is error-prone and can often introduce issues like uneven exposures, which compromise experiment results.</Warning>

You can query your gates/experiments without triggering an exposure, and manually log the exposures later:

<Tabs>
  <Tab title="Feature Gates">
    <CodeGroup>
      ```swift Swift theme={null}
      // Swift - Check without logging exposure
      let result = Statsig.checkGateWithExposureLoggingDisabled("a_gate_name")
      // ...
      // Later, when ready to log the exposure
      Statsig.manuallyLogGateExposure("a_gate_name")
      ```

      ```objc Objective-C theme={null}
      // Objective C - Check without logging exposure
      bool result = [Statsig checkGateWithExposureLoggingDisabled:@"a_gate_name"];
      // ...
      // Later, when ready to log the exposure
      [Statsig manuallyLogGateExposure:@"a_gate_name"];
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Dynamic Configs">
    <CodeGroup>
      ```swift Swift theme={null}
      // Swift - Get config without logging exposure
      let config = Statsig.getConfigWithExposureLoggingDisabled("a_config_name")
      // ...
      // Later, when ready to log the exposure
      Statsig.manuallyLogConfigExposure("a_config_name")
      ```

      ```objc Objective-C theme={null}
      // Objective C - Get config without logging exposure
      DynamicConfig *config = [Statsig getConfigWithExposureLoggingDisabled:@"a_config_name"];
      // ...
      // Later, when ready to log the exposure
      [Statsig manuallyLogConfigExposure:@"a_config_name"];
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Experiments">
    <CodeGroup>
      ```swift Swift theme={null}
      // Swift - Get experiment without logging exposure
      let experiment = Statsig.getExperimentWithExposureLoggingDisabled("an_experiment_name")
      // ...
      // Later, when ready to log the exposure
      Statsig.manuallyLogExperimentExposure("an_experiment_name")
      ```

      ```objc Objective-C theme={null}
      // Objective C - Get experiment without logging exposure
      DynamicConfig *experiment = [Statsig getExperimentWithExposureLoggingDisabled:@"an_experiment_name"];
      // ...
      // Later, when ready to log the exposure
      [Statsig manuallyLogExperimentExposure:@"an_experiment_name"];
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Layers">
    <CodeGroup>
      ```swift Swift theme={null}
      // Swift - Get layer without logging exposure
      let layer = Statsig.getLayerWithExposureLoggingDisabled("a_layer_name")
      let result = layer.getValue(forKey: "a_parameter_name", defaultValue: "fallback")
      // ...
      // Later, when ready to log the exposure
      Statsig.manuallyLogLayerParameterExposure("a_layer_name", "a_parameter_name")
      ```

      ```objc Objective-C theme={null}
      // Objective C - Get layer without logging exposure
      Layer *layer = [Statsig getLayerWithExposureLoggingDisabled:@"a_layer_name"];
      NSString *result = [layer getStringForKey:@"a_parameter_name" defaultValue:@"fallback"];
      // ...
      // Later, when ready to log the exposure
      [Statsig manuallyLogLayerParameterExposure:@"a_layer_name" parameterName:@"a_parameter_name"];
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Local Overrides

If you want to locally override gates/configs/experiments/layers for testing, Statsig offers convenient methods for a quick local override. Unless you call the remove method, these will be persisted session-to-session on the client's device. Note that these overrides only apply locally - they don't impact definitions in the console or elsewhere.

## Shutting Statsig Down

In order to save users' data and battery usage, as well as prevent logged events from being dropped, we keep event logs in client cache and flush periodically.
Because of this, some events may not have been sent when your app shuts down.

To make sure all logged events are properly flushed or saved locally, you should tell Statsig to shutdown when your app is closing:

<CodeGroup>
  ```swift Swift theme={null}
  Statsig.shutdown()
  ```

  ```objective-c Objective C theme={null}
  [Statsig shutdown];
  ```
</CodeGroup>

## Using multiple instances of the SDK

Up to this point, we've used the SDK's singleton. We also support creating multiples instances of the SDK - the `Statsig` singleton wraps a single instance of the SDK (typically called a `StatsigClient`) that you can instantiate.

<Note> You must use a different SDK key for each sdk instance you create for this to work. Various functionality of the Statsig client is keyed on the SDK key being used. Using the same key will lead to collisions. </Note>

All top level static methods from the singleton carry over as instance methods.  To create an instance of the Statsig sdk:

<CodeGroup>
  ```swift Swift theme={null}
  let client = StatsigClient(
      sdkKey: "client-xyz",
      user: StatsigUser(userID: "user-1"),
      options: StatsigOptions(environment: StatsigEnvironment(tier: .Production))
  ) { error in
    // ready
  }

  let gateOn = client.checkGate("some_gate")
  ```

  ```objective-c Objective C theme={null}
  StatsigOptions *options = [[StatsigOptions alloc] initWithEnvironment:[[StatsigEnvironment alloc] initWithTier:StatsigEnvironmentTierProduction]];
  StatsigUser *user = [[StatsigUser alloc] initWithUserID:@"user-1"];
  StatsigClient *client = [[StatsigClient alloc] initWithSdkKey:@"client-xyz" user:user options:options completion:^(StatsigClientError * error) {
    // ready
  }];

  BOOL gateOn = [client checkGate:@"some_gate"];
  ```
</CodeGroup>

<Warning>
  Use a unique SDK key per instance to avoid collisions.
</Warning>

## Initialize Response

The SDK provides a method to access the raw values that are used internally for gate, config, and layer value. This can be useful for debugging or for advanced use cases where you need to access the underlying data. For example, you can use these values to bootstrap another SDK, like the javascript SDK when you open an in-app browser.

The `getInitializeResponseJson` method returns an `ExternalInitializeResponse` object that contains:

1. A JSON string representation of the initialize response values
2. Evaluation details that provide metadata about how the values were obtained (network, cache, etc.)

<CodeGroup>
  ```swift Swift theme={null}
  let response = Statsig.getInitializeResponseJson()
  if let values = response.values {
      print(values)
  }
  let details = response.evaluationDetails
  ```

  ```objective-c Objective C theme={null}
  ExternalInitializeResponse *response = [Statsig getInitializeResponseJson];
  NSString *values = response.values;
  if (values) {
      NSLog(@"%@", values);
  }
  EvaluationDetails *details = response.evaluationDetails;
  ```
</CodeGroup>

## Listening for changes

In v1.14.0+, you can listen for SDK changes using `StatsigListening`.

<CodeGroup>
  ```swift Swift theme={null}
  class MyViewController: UIViewController, StatsigListening {

      override func viewDidLoad() {
          super.viewDidLoad()

          if Statsig.isInitialized() {
              render()
          } else {
              Statsig.addListener(self)
              renderLoading()
          }
      }

      private func render() {
          let showNewUI = Statsig.checkGate("new_ui_enabled")
          if showNewUI {
              // Render the new UI
          } else {
              // Render the old UI
          }
      }

      private func renderLoading() { /* loading UI */ }
      private func renderError(error: StatsigClientError) { /* error UI */ }

      // StatsigListening
      func onInitializedWithResult(_ error: StatsigClientError?) {
          if let error = error {
              renderError(error)
              return
          }
          render()
      }

      func onUserUpdatedWithResult(_ error: StatsigClientError?) { /* optional rerender */ }
  }
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).