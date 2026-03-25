# Source: https://docs.statsig.com/server/go.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Legacy Go Server SDK

> Statsig's legacy Server SDK for Go applications; use Go Core for new projects

<Callout type="warning" title="Legacy SDK">
  This page covers the legacy Go SDK. For new implementations, use the [Go Core SDK](/server-core/go-core) built on the Server Core framework.
</Callout>

<Card title="GitHub Repository" icon="github" href="https://github.com/statsig-io/go-sdk">
  View the Go SDK source code and releases
</Card>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    via the `go get` CLI:

    ```bash  theme={null}
    go get github.com/statsig-io/go-sdk
    ```

    Or, add a dependency on the most recent version of the SDK in go.mod:

    ```go  theme={null}
    require (
      github.com/statsig-io/go-sdk v1.26.0
    )
    ```

    See the [Releases tab in GitHub](https://github.com/statsig-io/go-sdk/releases) for the latest versions.
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    ```go  theme={null}
    import (
      statsig "github.com/statsig-io/go-sdk"
    )

    statsig.Initialize("server-secret-key")

    // Or, if you want to initialize with certain options
    statsig.InitializeWithOptions("server-secret-key", &Options{Environment: Environment{Tier: "staging"}})
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```go  theme={null}
user := statsig.User{UserID: "some_user_id"}
feature := statsig.CheckGate(user, "use_new_feature")
if feature {
  // Gate is on, enable new feature
} else {
  // Gate is off
}
```

## Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```go  theme={null}
user := statsig.User{UserID: "some_user_id"}
feature := statsig.GetGate(user, "use_new_feature")
if feature.Value {
  // Gate is on, enable new feature
  fmt.Print(feature.EvaluationDetails.Reason)
}
```

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

```go  theme={null}
config := statsig.GetConfig(user, "awesome_product_details")

// The 2nd parameter is the default value to be used in case the given parameter name does not exist on
// the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
// value has not been cached on the client.
itemName := config.GetString("product_name", "Awesome Product v1");
double price = config.GetNumber("price", 10.0);
bool shouldDiscount = config.GetBool("discount", false);

// Or just get the whole json object backing this config if you prefer
json := config.Value

```

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```go  theme={null}
// Values via getLayer

layer := Statsig.GetLayer(user, "user_promo_experiments");
promoTitle := layer.GetString("title", "Welcome to Statsig!");
discount := layer.GetDouble("discount", 0.1);

// or, via getExperiment

titleExperiment := Statsig.GetExperiment(user, "new_user_promo_title");
priceExperiment := Statsig.GetExperiment(user, "new_user_promo_price");

promoTitle := titleExperiment.GetString("title", "Welcome to Statsig!");
discount := priceExperiment.GetNumber("discount", 0.1);

...

price := msrp * (1 - discount);

// getting the layer name that an experiment belongs to

userPromoLayer := Statsig.GetExperimentLayer("new_user_promo_title");
```

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```go  theme={null}
statsig.LogEvent(Event{
		User: user,
		EventName: "add_to_cart",
                Value: "SKU_12345",
		Metadata: map[string]string{"price": "9.99","item_name": "diet_coke_48_pack"},
	})

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

You can specify optional parameters with `options` when initializing using `InitializeWithOptions()`

```go  theme={null}
type Options struct {
	API                string      `json:"api"`
	Environment        Environment `json:"environment"`
	LocalMode          bool        `json:"localMode"`
	ConfigSyncInterval time.Duration
	IDListSyncInterval time.Duration
  BootstrapValues      string
	RulesUpdatedCallback func(rules string, time int64)
}
```

* **Environment**: default nil
  * An object you can use to set environment variables that apply to all of your users in the same session and will be used for targeting purposes.
  * The most common usage is to set the environment tier (string), and have feature gates pass/fail for specific environments. The accepted values are "production", "staging" and "development".
* **LocalMode**: default false
  * Restricts the SDK to not issue any network requests and only respond with default values (or local overrides)
* **ConfigSyncInterval**: default 10 seconds
  * The interval to poll for gate/experiment/config changes.
* **IDListSyncInterval**: default 1 minute
  * The interval to poll for ID list changes.
* **BootstrapValues**: default nil
  * A string that represents all rules for all feature gates, dynamic configs and experiments. It can be provided to bootstrap the Statsig server SDK at initialization in case your server runs into network issue or Statsig server is down temporarily.
* **RulesUpdatedCallback**: default nil
  * The callback that gets invoked whenever the rulesets are updated. It's called with a JSON string that represents the rulesets, and a timestamp for when the rules were updated.
* **UserPersistentStorage**: IUserPersistentStorage default nil
  * A persistent storage adapter for running sticky experiments.
* **DisableIdList**: default false
  * A flag to disable fetching the id list during initialization and background polling for both network and data adapter.

### Client Initialize Response Options

When using `getClientInitializeResponse()`, you can specify additional options through the `GCIROptions` struct:

```go  theme={null}
type GCIROptions struct {
	IncludeLocalOverrides bool
	ClientKey             string
	TargetAppID           string
	HashAlgorithm         string
	IncludeConfigType     bool
	ConfigTypesToInclude  []ConfigType
}
```

* **IncludeLocalOverrides**: default false
  * When set to true, local overrides will be included in the client initialize response.
  * This allows you to test local changes to configurations without affecting other users.
  * Useful for development and testing environments.

* **ClientKey**: default empty string
  * The client SDK key to use for the initialize response.
  * This key is used to identify the client application and determine which configurations it should receive.
  * Required when generating a client initialize response for client SDKs.

* **TargetAppID**: default empty string
  * Specifies a target application ID to filter configurations (feature gates, dynamic configs, experiments, and layers).
  * When specified, the SDK will only return configurations that are targeted to this application ID.
  * This is useful in multi-tenant or multi-application environments where you want to ensure that only configurations relevant to a specific application are evaluated and returned.
  * If not specified, the SDK will attempt to determine the target app ID from the provided client key.

* **HashAlgorithm**: default empty string
  * Specifies the hashing algorithm to use for generating stable IDs in the client.
  * Common values include "djb2" (default if not specified) and "sha256".
  * This should match the hashing algorithm used by the client SDK.

* **IncludeConfigType**: default false (deprecated)
  * When set to true, the type of each configuration will be included in the response.
  * This allows clients to differentiate between different types of configurations (e.g., feature gates, dynamic configs, experiments).
  * Note: This option is deprecated and may be removed in future versions.

* **ConfigTypesToInclude**: default empty array
  * An array of configuration types to include in the response.
  * If specified, only configurations of the specified types will be included.
  * Possible values include FeatureGateType, DynamicConfigType, ExperimentType, and LayerType.
  * If empty, all configuration types will be included (subject to other filtering options).

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

```go  theme={null}
statsig.Shutdown()
```

## Local Overrides

You can override the values returned by the SDK for testing purposes. This can be useful for local development when you want to test specific scenarios.

```go  theme={null}
func OverrideGate(gate string, val bool)

func OverrideConfig(config string, val map[string]interface{})
```

## Client SDK Bootstrapping

The Statsig server SDK can be used to generate the initialization values for a client SDK. This is useful for server-side rendering (SSR) or when you want to pre-fetch values for a client.

```go  theme={null}
user := statsig.User{UserID: "some_user_id"}
options := statsig.GCIROptions{}
options.ClientKey = "client-YOUR_CLIENT_KEY"

result := statsig.GetClientInitializeResponseWithOptions(user, &options)

// You can then pass 'result' into a Statsig Client SDK
```

## Data Store

A data store can be used to synchronize the configuration/value downloads across multiple SDK instances, and to bootstrap the SDK in offline environments.

### Interface

```go  theme={null}
type IDataAdapter interface {
	/**
	 * Returns the data stored for a specific key
	 */
	Get(key string) string
	/**
	 * Updates data stored for each key
	 */
	Set(key string, value string)
	/**
	 * Startup tasks to run before any get/set calls can be made
	 */
	Initialize()
	/**
	 * Cleanup tasks to run when statsig is shutdown
	 */
	Shutdown()
	/**
		 * Determines whether the SDK should poll for updates from
	   * the data adapter (instead of Statsig network) for the given key
	*/
	ShouldBeUsedForQueryingUpdates(key string) bool
}
```

### Example Implementation

```go  theme={null}
type dataAdapterExample struct {
	store map[string]string
	mu    sync.RWMutex
}

func (d *dataAdapterExample) Get(key string) string {
	d.mu.RLock()
	defer d.mu.RUnlock()
	return d.store[key]
}

func (d *dataAdapterExample) Set(key string, value string) {
	d.mu.Lock()
	defer d.mu.Unlock()
	d.store[key] = value
}

func (d *dataAdapterExample) Initialize() {}

func (d *dataAdapterExample) Shutdown() {}

func (d *dataAdapterExample) ShouldBeUsedForQueryingUpdates(key string) bool {
	return false
}
```

## User Persistent Storage

User Persistent Storage is a storage adapter for running sticky experiments. It allows you to persist user assignments across sessions.

### Interface

```go  theme={null}
type IUserPersistentStorage interface {
	/**
	 * Returns the data stored for a specific key
	 */
	Load(key string) (string, bool)

	/**
	 * Updates data stored for a specific key
	 */
	Save(key string, data string)
}
```

### Example Implementation

```go  theme={null}
type userPersistentStorageExample struct {
	store      map[string]string
	loadCalled int
	saveCalled int
}

func (d *userPersistentStorageExample) Load(key string) (string, bool) {
	d.loadCalled++
	val, ok := d.store[key]
	return val, ok
}

func (d *userPersistentStorageExample) Save(key string, value string) {
	d.saveCalled++
	d.store[key] = value
}
```

## Multi-Instance Usage

If you need to create multiple independent instances of the Statsig SDK (for example, to use different API keys or configurations), you can use the instance-based approach:

```go  theme={null}
sdkInstance := NewClientWithOptions(sdkKey, &Options{})
```

## FAQ

#### How do I run experiments for logged out users?

See the guide on [device level experiments](/guides/first-device-level-experiment)

#### How can I mock Statsig in tests

We recommend using the [Local Override](#local-overrides) APIs in v1.3.0+, in combination with the `LocalMode` option in `StatsigOptions` to force gate/config values in test environments and remove network access to statsig servers.

For example:

```go  theme={null}
c := NewClientWithOptions(secret, &Options{LocalMode: true})

user := User{
    UserID: "123",
}
gateDefault := c.CheckGate(user, "any_gate")
// "any_gate" is false by default

c.OverrideGate("any_gate", true)
// "any_gate" is now true
```

See also [https://github.com/statsig-io/go-sdk/blob/main/overrides\_test.go](https://github.com/statsig-io/go-sdk/blob/main/overrides_test.go)

## Reference

### StatsigUser

```go  theme={null}
// User specific attributes for evaluating Feature Gates, Experiments, and DynamicConfigs
//
// Learn more why a UserID or a customID is required: https://docs.statsig.com/sdks/user#why-is-an-id-always-required-for-server-sdks
// PrivateAttributes are only used for user targeting/grouping in feature gates, dynamic configs,
// experiments and etc; they are omitted in logs.
type User struct {
	UserID             string                 `json:"userID"`
	Email              string                 `json:"email,omitempty"`
	IpAddress          string                 `json:"ip,omitempty"` // Many jurisdictions categorize this as PII; verify whether you should log this. 
	UserAgent          string                 `json:"userAgent,omitempty"`
	Country            string                 `json:"country,omitempty"`
	Locale             string                 `json:"locale,omitempty"`
	AppVersion         string                 `json:"appVersion,omitempty"`
	Custom             map[string]interface{} `json:"custom,omitempty"`
	PrivateAttributes  map[string]interface{} `json:"privateAttributes,omitempty"`
	StatsigEnvironment map[string]string      `json:"statsigEnvironment,omitempty"`
	CustomIDs          map[string]string      `json:"customIDs"`
}
```

### StatsigOptions

```go  theme={null}
// Advanced options for configuring the Statsig SDK
type Options struct {
	API                   string      `json:"api"`
	APIOverrides          APIOverrides `json:"api_overrides"`
	Environment           Environment `json:"environment"`
	LocalMode             bool        `json:"localMode"`
	ConfigSyncInterval    time.Duration
	IDListSyncInterval    time.Duration
	LoggingInterval       time.Duration
	LoggingMaxBufferSize  int
	BootstrapValues       string
	RulesUpdatedCallback  func(rules string, time int64)
	InitTimeout           time.Duration
	DataAdapter           IDataAdapter
	OutputLoggerOptions   OutputLoggerOptions
	StatsigLoggerOptions  StatsigLoggerOptions
	EvaluationCallbacks   EvaluationCallbacks
	DisableCDN            bool // Disables use of CDN for downloading config specs
	UserPersistentStorage IUserPersistentStorage
	IPCountryOptions      IPCountryOptions
	UAParserOptions       UAParserOptions
}

type APIOverrides struct {
	DownloadConfigSpecs string `json:"download_config_specs"`
	GetIDLists          string `json:"get_id_lists"`
	LogEvent            string `json:"log_event"`
}

type EvaluationCallbacks struct {
	GateEvaluationCallback       func(name string, result bool, exposure *ExposureEvent)
	ConfigEvaluationCallback     func(name string, result DynamicConfig, exposure *ExposureEvent)
	ExperimentEvaluationCallback func(name string, result DynamicConfig, exposure *ExposureEvent)
	LayerEvaluationCallback      func(name string, param string, result DynamicConfig, exposure *ExposureEvent)
	ExposureCallback             func(name string, exposure *ExposureEvent)
	IncludeDisabledExposures     bool
}

type OutputLoggerOptions struct {
	LogCallback            func(message string, err error)
	EnableDebug            bool
	DisableInitDiagnostics bool
	DisableSyncDiagnostics bool
}

type StatsigLoggerOptions struct {
	DisableInitDiagnostics bool
	DisableSyncDiagnostics bool
	DisableApiDiagnostics  bool
	DisableAllLogging      bool
}

type IPCountryOptions struct {
	Disabled     bool // Fully disable IP to country lookup
	LazyLoad     bool // Load in background
	EnsureLoaded bool // Wait until loaded when needed
}

type UAParserOptions struct {
	Disabled     bool // Fully disable UA parser
	LazyLoad     bool // Load in background
	EnsureLoaded bool // Wait until loaded when needed
}

// See https://docs.statsig.com/guides/usingEnvironments
type Environment struct {
	Tier   string            `json:"tier"`
	Params map[string]string `json:"params"`
}

// options for getClientInitializeResponse
type GCIROptions struct {
	IncludeLocalOverrides bool
	ClientKey             string
	HashAlgorithm         string //supports "sha256", "djb2", "none", default "sha256"
}
```

### Event

```go  theme={null}
type Event struct {
	EventName string            `json:"eventName"`
	User      User              `json:"user"`
	Value     string            `json:"value"`
	Metadata  map[string]string `json:"metadata"`
	Time      int64             `json:"time"`
}
```

### FeatureGate

```go  theme={null}
type FeatureGate struct {
	Name              string             `json:"name"`
	Value             bool               `json:"value"`
	RuleID            string             `json:"rule_id"`
	IDType            string             `json:"id_type"`
	GroupName         string             `json:"group_name"`
	EvaluationDetails *EvaluationDetails `json:"evaluation_details"`
}
```

### DynamicConfig

```go  theme={null}
type DynamicConfig struct {
	Name              string                 `json:"name"`
	Value             map[string]interface{} `json:"value"`
	RuleID            string                 `json:"rule_id"`
	IDType            string             	 `json:"id_type"`
	GroupName         string                 `json:"group_name"`
	EvaluationDetails *EvaluationDetails     `json:"evaluation_details"`
  AllocatedExperimentName string           `json:"allocated_experiment_name"`
  GetString(key string, fallback string) string
  GetNumber(key string, fallback float64) float64
  GetBool(key string, fallback bool) bool
  GetSlice(key string, fallback []interface{}) []interface{}
  GetMap(key string, fallback map[string]interface{}) map[string]interface{}
}
```


Built with [Mintlify](https://mintlify.com).