# Source: https://docs.statsig.com/server-core/go-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Go Server Core SDK (Beta)

> Statsig's next-gen Go Server SDK built on our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-go" target="_blank" rel="noreferrer">Go Core on Github</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    via the `go get` CLI:

    You can install the latest version of the SDK:

    ```
    go get github.com/statsig-io/statsig-go-core@latest
    ```

    Or, add a dependency on the most recent version of the SDK in go.mod:

    ```
    require (
      github.com/statsig-io/statsig-go-core v0.10.2-beta
    )
    ```

    See the [Releases tab in GitHub](https://github.com/statsig-io/statsig-server-core/releases) for the latest versions.

    :::note
    `go get` requires a Go module project with a go.mod file.
    :::
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```go expandable theme={null}
    import (
        "log"

        statsig "github.com/statsig-io/statsig-go-core"
    )
    			
    options, err := statsig.NewOptionsBuilder().
        WithOutputLogLevel("DEBUG").
        Build()
    if err != nil {
        log.Fatalf("failed to build options: %v", err)
    }

    s, err := statsig.NewStatsigWithOptions("secret-key", options)
    if err != nil {
        log.Fatalf("failed to create Statsig client: %v", err)
    }

    s.Initialize()
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```go  theme={null}
user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()

// Basic check
if s.CheckGate(user, "a_gate") {
    // Gate is on, enable new feature
} else {
    // Gate is off
}

// With options (e.g., disable automatic exposure logging)
options := &statsig.FeatureGateEvaluationOptions{DisableExposureLogging: true}
s.CheckGateWithOptions(user, "a_gate", options)
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```go  theme={null}
user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()

// You can disable exposure logging for this specific check
dynamicConfigOptions := &statsig.DynamicConfigEvaluationOptions{DisableExposureLogging: false}

dynamic_config := "a_config"
config := s.GetDynamicConfigWithOptions(user, dynamic_config, dynamicConfigOptions)

// Access the config values
str_val := config.GetString("str_val", "default_str_val") // returns String
int_val := config.GetNumber("number_val", 100) // returns float64
bool_val := config.GetBool("bool_val", false) // returns bool
interface_val := config.GetSlice("interface_val", []any{"default_interface_val"}) // returns []any
map_val := config.GetMap("map_val", map[string]any{"default": "value"}) // returns map[string]interface{}

// The config object also provides metadata about the evaluation
fmt.Println(config.RuleID) // The ID of the rule that served this config
fmt.Println(config.IDType) // The type of the evaluation (experiment, config, etc)
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```go  theme={null}
user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()

// Getting values with GetExperiment
experimentOptions := &statsig.ExperimentEvaluationOptions{DisableExposureLogging: false}

experiment := s.GetExperimentWithOptions(user, "a_test_experiment", experimentOptions)
str_val := experiment.GetString("str_val", "default_str_val") // returns String
int_val := experiment.GetNumber("number_val", 100) // returns float64

// Getting values with GetLayer
layerOptions := &statsig.LayerEvaluationOptions{DisableExposureLogging: false}

layer := s.GetLayerWithOptions(user, "a_test_experiment", layerOptions)
str_val := layer.GetString("str_val", "default_str_val") // returns String
int_val := layer.GetNumber("number_val", 100) // returns float64

```

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```go  theme={null}
user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()

options := &statsig.FeatureGateEvaluationOptions{DisableExposureLogging: false}
featureGate := s.GetFeatureGateWithOptions(user, "a_gate", options)
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```go  theme={null}
user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()

event := statsig.EventPayload{
    EventName: "sample_event",
    Value:     "event",
    Metadata: map[string]string{
        "val_1": "log val 1",
    },
}

s.LogEvent(user, event)
```

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

All of the main SDK functions (`CheckGate`, `GetDynamicConfig`, `GetExperiment`, `GetLayer`) accept an optional options parameter with `DisableExposureLogging` field. When this is set to `true`, the SDK will not automatically log an exposure event. You can then manually log the exposure at a later time using the corresponding manual exposure logging method:

<Tabs>
  <Tab title="Feature Gates">
    ```go  theme={null}
    user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()
    options := &statsig.FeatureGateEvaluationOptions{DisableExposureLogging: true}
    result := s.CheckGateWithOptions(user, "a_gate_name", options)
    ```

    ```go  theme={null}
    s.ManuallyLogFeatureGateExposure(user, "gate_name")
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```go  theme={null}
    user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()
    options := &statsig.DynamicConfigEvaluationOptions{DisableExposureLogging: true}
    config := s.GetDynamicConfigWithOptions(user, "config_name", options)
    ```

    ```go  theme={null}
    s.ManuallyLogDynamicConfigExposure(user, "config_name")
    ```
  </Tab>

  <Tab title="Experiments">
    ```go  theme={null}
    user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()
    options := &statsig.ExperimentEvaluationOptions{DisableExposureLogging: true}
    experiment := s.GetExperimentWithOptions(user, "experiment_name", options)
    ```

    ```go  theme={null}
    s.ManuallyLogExperimentExposure(user, "experiment_name")
    ```
  </Tab>

  <Tab title="Layers">
    ```go  theme={null}
    user, _ := statsig.NewUserBuilderWithUserID("a-user").Build()
    options := &statsig.LayerEvaluationOptions{DisableExposureLogging: true}
    layer := s.GetLayerWithOptions(user, "layer_name", options)
    paramValue := layer.GetString("param_name", "fallback")
    ```

    ```go  theme={null}
    s.ManuallyLogLayerParamExposure(user, "layer_name", "param_name")
    ```
  </Tab>
</Tabs>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

### Parameters

<ResponseField name="SpecsUrl" type="string">
  Custom URL for fetching feature specifications.
</ResponseField>

<ResponseField name="LogEventUrl" type="string">
  Custom URL for logging events.
</ResponseField>

<ResponseField name="Environment" type="string">
  Environment parameter for evaluation.
</ResponseField>

<ResponseField name="EventLoggingFlushIntervalMs" type="number">
  How often events are flushed to Statsig servers (in milliseconds).
</ResponseField>

<ResponseField name="EventLoggingMaxQueueSize" type="number">
  Maximum number of events to queue before forcing a flush.
</ResponseField>

<ResponseField name="SpecsSyncIntervalMs" type="number">
  How often the SDK updates specifications from Statsig servers (in milliseconds).
</ResponseField>

<ResponseField name="OutputLogLevel" type="string">
  Controls the verbosity of SDK logs.
</ResponseField>

<ResponseField name="DisableCountryLookup" type="boolean">
  Disables country lookup based on IP address. Set to `true` to improve performance if country-based targeting is not needed.
</ResponseField>

<ResponseField name="DisableUserAgentParsing" type="boolean">
  Disables user agent parsing. Set to `true` to improve performance if device/browser-based targeting is not needed.
</ResponseField>

<ResponseField name="WaitForCountryLookupInit" type="boolean" default="false">
  When set to true, the SDK will wait for country lookup data (e.g., GeoIP or YAML files) to fully load during initialization. This may slow down by \~1 second startup but ensures that IP-to-country parsing is ready at evaluation time.
</ResponseField>

<ResponseField name="WaitForUserAgentInit" type="boolean" default="false">
  When set to true, the SDK will wait until user agent parsing data is fully loaded during initialization. This may slow down by \~1 second startup but ensures that parsing of the user's userAgent string into fields like browserName, browserVersion, systemName, systemVersion, and appVersion is ready before any evaluations.
</ResponseField>

<ResponseField name="EnableIdLists" type="boolean" default="true">
  Enables downloading ID lists; set to false to skip ID list syncing.
</ResponseField>

<ResponseField name="IdListsUrl" type="string">
  Custom URL for fetching ID lists.
</ResponseField>

<ResponseField name="IdListsSyncIntervalMs" type="number">
  How often the SDK syncs ID lists (in milliseconds).
</ResponseField>

<ResponseField name="DisableAllLogging" type="boolean" default="false">
  When set to true, the SDK will not log any events or exposures.
</ResponseField>

<ResponseField name="DisableNetwork" type="boolean" default="false">
  When set to true, the SDK will not make any network requests.
</ResponseField>

<ResponseField name="GlobalCustomFields" type="string">
  JSON string of custom fields that should be appended to every evaluation.
</ResponseField>

<ResponseField name="ObservabilityClientRef" type="number">
  Internal reference for a custom observability client created via the SDK.
</ResponseField>

<ResponseField name="DataStoreRef" type="number">
  Internal reference for a custom data store adapter created via the SDK.
</ResponseField>

<ResponseField name="PersistentStorageRef" type="number">
  Internal reference for a persistent storage adapter created via the SDK.
</ResponseField>

<ResponseField name="InitTimeoutMs" type="number" default="3000">
  Maximum time in milliseconds to wait for SDK initialization to complete. If initialization takes longer than this timeout, the SDK will continue to operate but may return default values until initialization completes.
</ResponseField>

<ResponseField name="FallbackToStatsigApi" type="boolean" default="false">
  When set to true, the SDK will fallback to using the Statsig API directly if custom adapters (like local file adapters) fail to load configurations.
</ResponseField>

***

### Example Options Usage

```go expandable theme={null}
import (
    statsig "github.com/statsig-io/statsig-go-core"
)

// Initialize StatsigOptions with custom parameters
options, err := statsig.NewOptionsBuilder().
    WithSpecsUrl("https://example.com/specsUrl").
    WithLogEventUrl("https://example.com/logUrl").
    WithEnvironment("production").
    WithEventLoggingFlushIntervalMs(2000).
    WithEventLoggingMaxQueueSize(5000).
    WithSpecsSyncIntervalMs(1000).
    WithOutputLogLevel("DEBUG").
    WithDisableCountryLookup(true).
    WithDisableUserAgentParsing(true).
    WithWaitForCountryLookupInit(false).
    WithEnableIdLists(true).
    WithIdListsSyncIntervalMs(60000).
    WithInitTimeoutMs(3000).
    WithFallbackToStatsigApi(false).
    Build()
if err != nil {
    // handle options build error
}

// Pass the options object when initializing the Statsig client
s, err := statsig.NewStatsigWithOptions("secret-key", options)
if err != nil {
    // handle init error
}
s.Initialize()
```

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```go  theme={null}
// Method signature
func (s *Statsig) Shutdown() {}

// example usage
s, err := statsig.NewStatsig("secret-key")
s.Initialize()
s.Shutdown()
```

### Flush Events

```go  theme={null}
// Method signature
func (s *Statsig) FlushEvents() {}

// example usage
s, err := statsig.NewStatsig("secret-key")
s.Initialize()
s.FlushEvents()
```

## FAQ

##### Installation FAQs

#### How do I fix undefined symbol errors/linker errors?

You may need to reset your environment variables to those found in the statsig.env or statsig.env.ps1 file which was generated during the post-install script. Running the command sets the environment variables for the current terminal session. Users may need to add in the variables to their .bashrc, .zshrc, or .ps1 file to load them automatically.


Built with [Mintlify](https://mintlify.com).