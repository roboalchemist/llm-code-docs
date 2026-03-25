# Source: https://docs.statsig.com/server-core/dotnet-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# .NET Server SDK

> Statsig's Next-gen .NET Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-dotnet" target="_blank" rel="noreferrer">.NET Core on Github</a>,
  <a href="https://www.nuget.org/packages/Statsig.Dotnet/" target="_blank" rel="noreferrer">NuGet Package</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Installation

    ```bash  theme={null}
    dotnet add package Statsig.Dotnet
    ```

    Or add the package reference to your `.csproj` file:

    ```xml  theme={null}
    <PackageReference Include="Statsig.Dotnet" Version="X.X.X" />
    ```

    ### Requirements:

    * **.NET 8.0** or later
    * **Windows, macOS, or Linux** (x64 and ARM64 supported)
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```csharp  theme={null}
    using Statsig;

    var statsig = new Statsig.Statsig("server-secret-key");
    await statsig.Initialize();
    ```

    You can also provide custom options:

    ```csharp  theme={null}
    var options = new StatsigOptionsBuilder()
        .SetSpecsSyncIntervalMs(10000)
        .SetDisableAllLogging(false)
        .Build();

    var statsig = new Statsig("server-secret-key", options);
    await statsig.Initialize();
    ```

    For shared instance usage:

    ```csharp  theme={null}
    var sharedStatsig = Statsig.NewShared("server-secret-key", options);
    await sharedStatsig.Initialize();

    var statsig = Statsig.Shared();
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .SetEmail("user@example.com")
    .Build();

var gateValue = statsig.CheckGate(user, "new_feature_gate");
if (gateValue)
{
    // Gate is on, enable new feature
}
else
{
    // Gate is off
}
```

You can also disable exposure logging for this evaluation:

```csharp  theme={null}
var options = new EvaluationOptions(disableExposureLogging: true);
var gateValue = statsig.CheckGate(user, "new_feature_gate", options);
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

var config = statsig.GetDynamicConfig(user, "product_config");

var productName = config.Get<string>("product_name", "Default Product");
var price = config.Get<double>("price", 9.99);
var isEnabled = config.Get<bool>("enabled", false);
var features = config.Get<List<string>>("features", new List<string>());

Console.WriteLine($"Config Name: {config.Name}");
Console.WriteLine($"Group Name: {config.GroupName}");
Console.WriteLine($"Rule ID: {config.RuleID}");
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

var experiment = statsig.GetExperiment(user, "button_color_test");

var buttonColor = experiment.Get<string>("color", "blue");
var fontSize = experiment.Get<int>("font_size", 14);
var showBorder = experiment.Get<bool>("show_border", true);

Console.WriteLine($"Experiment Name: {experiment.Name}");
Console.WriteLine($"Group Name: {experiment.GroupName}");
Console.WriteLine($"Rule ID: {experiment.RuleID}");
Console.WriteLine($"Button Color: {buttonColor}");
```

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

var layer = statsig.GetLayer(user, "user_prefs_layer");

var theme = layer.Get<string>("theme", "light");
var language = layer.Get<string>("language", "en");
var notifications = layer.Get<bool>("notifications_enabled", true);

Console.WriteLine($"Layer Name: {layer.Name}");
Console.WriteLine($"Allocated Experiment: {layer.AllocatedExperimentName}");
Console.WriteLine($"Group Name: {layer.GroupName}");
Console.WriteLine($"Rule ID: {layer.RuleID}");
```

Note: Layer parameter access automatically logs exposure events unless disabled with `EvaluationOptions`.

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

statsig.LogEvent(user, "button_clicked");

statsig.LogEvent(user, "purchase_completed", 29.99);

statsig.LogEvent(user, "page_view", "homepage", new Dictionary<string, string>
{
    ["referrer"] = "google",
    ["campaign"] = "summer_sale"
});

statsig.LogEvent(user, "video_watched", 120, new Dictionary<string, string>
{
    ["video_id"] = "abc123",
    ["quality"] = "1080p"
});
```

The `LogEvent` method supports multiple overloads:

* `LogEvent(user, eventName)`
* `LogEvent(user, eventName, stringValue, metadata)`
* `LogEvent(user, eventName, intValue, metadata)`
* `LogEvent(user, eventName, doubleValue, metadata)`

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

var gate = statsig.GetFeatureGate(user, "new_feature_gate");

Console.WriteLine($"Gate Name: {gate.Name}");
Console.WriteLine($"Gate Value: {gate.Value}");
Console.WriteLine($"Rule ID: {gate.RuleID}");
Console.WriteLine($"ID Type: {gate.IDType}");

if (gate.EvaluationDetails != null)
{
    Console.WriteLine($"Config Sync Time: {gate.EvaluationDetails.ConfigSyncTime}");
    Console.WriteLine($"Init Time: {gate.EvaluationDetails.InitTime}");
    Console.WriteLine($"Reason: {gate.EvaluationDetails.Reason}");
}
```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

```csharp  theme={null}
# Get a Parameter Store by name
param_store = statsig.getParameterStore(user, "my_parameter_store")
```

### Retrieving Parameter Values

Parameter Store provides methods for retrieving values of different types with fallback defaults.

<Accordion title="Param Store Methods">
  * **GetBool(string, default(bool))**: Pulls key value of type boolean
  * **GetString(string, "")**: Pulls key value of type string
  * **GetLong(string, default(long))**: Pulls key value of type long
  * **GetDouble(string, default(double))**: Pulls key value of type double
  * **GetList(string, new List\<>())**: Pulls key value of type list
  * **GetDictionary(string, new Dictionary\<string, object>())**: Pulls key value of type Dictionary
</Accordion>

### Evaluation Options

You can disable exposure logging when retrieving a parameter store:

```csharp  theme={null}
var store = statsig.GetParameterStore(user, name!, options);

if (store == null)
{
    throw new Exception($"Parameter store {name} not found");
}

var x = store.GetBool(paramName, default(bool));

var y = store.GetString(paramName, "");

var z = store.GetDictionary(paramName, new Dictionary<string, object>());
```

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

```csharp  theme={null}
var sharedStatsig = Statsig.NewShared("server-secret-key");
await sharedStatsig.Initialize();

// Later, anywhere in your codebase
var statsig = Statsig.Shared();

// Use the shared instance
var result = statsig.CheckGate(user, "my_gate");
```

The shared instance is useful for:

* Singleton pattern usage across your application
* Dependency injection scenarios
* Avoiding multiple SDK instances

Remember to clean up the shared instance on shutdown:

```csharp  theme={null}
var statsig = Statsig.Shared();
await statsig.FlushEvents();
await statsig.Shutdown();

Statsig.RemoveSharedInstance();
```

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

All of the main SDK functions (`CheckGate`, `GetDynamicConfig`, `GetExperiment`, `GetLayer`) accept an optional `EvaluationOptions` parameter. When `disableExposureLogging` is set to `true`, the SDK will not automatically log an exposure event. You can then manually log the exposure at a later time using the corresponding manual exposure logging method:

<Tabs>
  <Tab title="Feature Gates">
    ```csharp  theme={null}
    var result = statsig.CheckGate(user, "a_gate_name", new EvaluationOptions(disableExposureLogging: true));
    ```

    ```csharp  theme={null}
    statsig.ManuallyLogGateExposure(user, "a_gate_name");
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```csharp  theme={null}
    var config = statsig.GetDynamicConfig(user, "a_dynamic_config_name", new EvaluationOptions(disableExposureLogging: true));
    ```

    ```csharp  theme={null}
    statsig.ManuallyLogDynamicConfigExposure(user, "a_dynamic_config_name");
    ```
  </Tab>

  <Tab title="Experiments">
    ```csharp  theme={null}
    var experiment = statsig.GetExperiment(user, "an_experiment_name", new EvaluationOptions(disableExposureLogging: true));
    ```

    ```csharp  theme={null}
    statsig.ManuallyLogExperimentExposure(user, "an_experiment_name");
    ```
  </Tab>

  <Tab title="Layers">
    ```csharp  theme={null}
    var layer = statsig.GetLayer(user, "a_layer_name", new EvaluationOptions(disableExposureLogging: true));
    var paramValue = layer.Get("a_param_name", "fallback_value");
    ```

    ```csharp  theme={null}
    statsig.ManuallyLogLayerParameterExposure(user, "a_layer_name", "a_param_name");
    ```
  </Tab>
</Tabs>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

`StatsigUser` represents the user context for feature flag evaluation. Use `StatsigUserBuilder` to create user instances:

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .SetEmail("user@example.com")
    .SetIP("192.168.1.1")
    .SetUserAgent("Mozilla/5.0...")
    .SetCountry("US")
    .SetLocale("en-US")
    .SetAppVersion("1.2.3")
    .SetCustomIDs(new Dictionary<string, string>
    {
        ["employee_id"] = "emp_456",
        ["team_id"] = "team_789"
    })
    .AddCustomID("department_id", "dept_123")
    .SetCustomProperties(new Dictionary<string, object>
    {
        ["subscription_tier"] = "premium",
        ["account_age_days"] = 365,
        ["is_beta_user"] = true
    })
    .AddCustomProperty("last_login", DateTime.UtcNow)
    .SetPrivateAttributes(new Dictionary<string, object>
    {
        ["internal_user_score"] = 0.85,
        ["risk_level"] = "low"
    })
    .AddPrivateAttribute("pii_hash", "abc123def456")
    .Build();
```

## Builder Methods

<Accordion title="Builder Methods">
  * **SetUserID(string)**: Set the primary user ID
  * **SetEmail(string)**: Set user email
  * **SetIP(string)**: Set user IP address
  * **SetUserAgent(string)**: Set browser user agent
  * **SetCountry(string)**: Set user country
  * **SetLocale(string)**: Set user locale
  * **SetAppVersion(string)**: Set app version
  * **SetCustomIDs(Dictionary\<string, string>)**: Set all custom IDs
  * **AddCustomID(string, string)**: Add a single custom ID
  * **SetCustomProperties(Dictionary\<string, object>)**: Set all custom properties
  * **AddCustomProperty(string, object)**: Add a single custom property
  * **SetPrivateAttributes(Dictionary\<string, object>)**: Set all private attributes
  * **AddPrivateAttribute(string, object)**: Add a single private attribute
  * **Build()**: Create the StatsigUser instance
</Accordion>

Remember to dispose of StatsigUser instances when done:

```csharp  theme={null}
using var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  `StatsigOptions` can be configured using the `StatsigOptionsBuilder` pattern:

  ```csharp  theme={null}
  var options = new StatsigOptionsBuilder()
      .SetSpecsURL("https://custom-api.statsig.com/v1/download_config_specs")
      .SetLogEventURL("https://custom-api.statsig.com/v1/rgstr")
      .SetEnvironment("production")
      .SetSpecsSyncIntervalMs(30000)
      .SetEventLoggingMaxQueueSize(1000)
      .SetWaitForCountryLookupInit(true)
      .SetWaitForUserAgentInit(true)
      .SetDisableCountryLookup(false)
      .SetDisableUserAgentParsing(false)
      .SetDisableAllLogging(false)
      .SetInitTimeoutMs(3000)
      .SetFallbackToStatsigApi(false)
      .SetEnableIDLists(true)
      .SetIDListsURL("https://custom-api.statsig.com/v1/get_id_lists")
      .SetIDListsSyncIntervalMs(60000)
      .SetGlobalCustomFields(new Dictionary<string, object>
      {
          ["app_version"] = "1.2.3",
          ["build_number"] = "456"
      })
      .Build();

  var statsig = new Statsig("server-secret-key", options);
  ```

  ## Available Options

  * **SetSpecsURL(string)**: Override the default specs download endpoint
  * **SetLogEventURL(string)**: Override the default event logging endpoint
  * **SetEnvironment(string)**: Set the environment tier (e.g., "production", "staging")
  * **SetSpecsSyncIntervalMs(int)**: How often to sync configuration specs (default: 10000ms)
  * **SetEventLoggingMaxQueueSize(int)**: Maximum events to queue before flushing
  * **SetWaitForCountryLookupInit(bool)**: Wait for country lookup initialization
  * **SetWaitForUserAgentInit(bool)**: Wait for user agent parsing initialization
  * **SetDisableCountryLookup(bool)**: Disable automatic country detection
  * **SetDisableUserAgentParsing(bool)**: Disable user agent parsing
  * **SetDisableAllLogging(bool)**: Disable all event logging
  * **SetInitTimeoutMs(int)**: Maximum time in milliseconds to wait for SDK initialization (default: 3000ms)
  * **SetFallbackToStatsigApi(bool)**: Fallback to Statsig API when custom adapters fail (default: false)
  * **SetEnableIDLists(bool)**: Enable ID list targeting
  * **SetIDListsURL(string)**: Override the default ID lists endpoint
  * **SetIDListsSyncIntervalMs(int)**: How often to sync ID lists (default: 60000ms)
  * **SetGlobalCustomFields(Dictionary\<string, object>)**: Global custom fields for all events
  * **SetProxyConfig(ProxyConfig)**: Configuration for connecting through a proxy server

  ## Proxy Configuration

  The `ProxyConfig` class allows you to configure the SDK to connect through a proxy server. This is useful when your application runs in an environment that requires all outbound HTTP traffic to go through a proxy.

  ```csharp  theme={null}
  var proxyConfig = new ProxyConfig
  {
      ProxyHost = "proxy.example.com",
      ProxyPort = 8080,
      ProxyAuth = "username:password", // Optional
      ProxyProtocol = "http" // Optional: "http" or "https"
  };

  var options = new StatsigOptionsBuilder()
      .SetProxyConfig(proxyConfig)
      .Build();

  var statsig = new Statsig("server-secret-key", options);
  ```

  ### ProxyConfig Properties

  * **ProxyHost** (string): The hostname or IP address of the proxy server
  * **ProxyPort** (int): The port number of the proxy server
  * **ProxyAuth** (string, optional): Authentication credentials in the format "username:password"
  * **ProxyProtocol** (string, optional): The protocol to use for the proxy connection ("http" or "https")
</Accordion>

<Accordion title="EvaluationOptions">
  `EvaluationOptions` allows you to customize the behavior of feature flag evaluations:

  ```csharp  theme={null}
  var options = new EvaluationOptions(disableExposureLogging: true);

  var gateValue = statsig.CheckGate(user, "feature_gate", options);
  var config = statsig.GetDynamicConfig(user, "product_config", options);
  var experiment = statsig.GetExperiment(user, "button_test", options);
  var layer = statsig.GetLayer(user, "user_prefs_layer", options);
  ```

  ## Options

  * **DisableExposureLogging**: When `true`, prevents automatic exposure event logging for this evaluation. Useful when you want to evaluate a feature flag without affecting analytics or experiment results.

  ## Use Cases

  * **Internal Tools**: Check flag values for debugging without affecting user metrics
  * **Conditional Logic**: Evaluate flags as part of complex logic where exposure should be logged manually later

  When exposure logging is disabled, you can manually log exposures later using the manual exposure methods:

  ```csharp  theme={null}
  var options = new EvaluationOptions(disableExposureLogging: true);
  var gateValue = statsig.CheckGate(user, "feature_gate", options);

  if (shouldLogExposure)
  {
      statsig.ManuallyLogGateExposure(user, "feature_gate");
  }
  ```
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```csharp  theme={null}
await statsig.FlushEvents();

await statsig.Shutdown();

statsig.Dispose();
```

For shared instances:

```csharp  theme={null}
var statsig = Statsig.Shared();
await statsig.FlushEvents();
await statsig.Shutdown();

Statsig.RemoveSharedInstance();
```

## Methods

* **FlushEvents()**: Immediately flush any pending events to Statsig servers
* **Shutdown()**: Gracefully shutdown the SDK, flushing events and cleaning up resources
* **Dispose()**: Release native resources (implements IDisposable)

It's recommended to call `FlushEvents()` before `Shutdown()` to ensure all events are sent, and always call `Dispose()` or use `using` statements to properly clean up resources.

## Client SDK Bootstrapping | SSR

If you are using the Statsig client SDK in a browser or mobile app, you can bootstrap the client SDK with the values from the server SDK to avoid a network request on the client. This is useful for server-side rendering (SSR) or when you want to reduce the number of network requests on the client.

```csharp  theme={null}
var user = new StatsigUserBuilder()
    .SetUserID("user_123")
    .Build();

var initResponse = statsig.GetClientInitializeResponse(user);

var options = new ClientInitResponseOptions
{
    HashAlgorithm = "sha256",
    ClientSDKKey = "client-sdk-key",
    IncludeLocalOverrides = false
};

var customInitResponse = statsig.GetClientInitializeResponse(user, options);
```

The `GetClientInitializeResponse` method returns a JSON string containing the initialization data needed by client-side SDKs. This enables server-side rendering and reduces client initialization time.

## ClientInitResponseOptions

* **HashAlgorithm**: Hash algorithm for response integrity (default: "djb2")
* **ClientSDKKey**: Client SDK key to include in response
* **IncludeLocalOverrides**: Whether to include local overrides in the response (default: false)

### Working with IP or UserAgent Values

The server SDK will not automatically use the `ip`, or `userAgent` for gate evaluation as Statsig servers would, since we don't have access to the request headers. If you'd like to use the attributes we derive from these properties, like Browser Name/Version, OS Name/Version & Country, you must manually set the `ip` and `userAgent` fields on the user object when calling `GetClientInitializeResponse`.

### Working with IDs

To ensure that the server SDK evaluates each config accurately, they need access to all user attributes that the client SDK leverages. We recommend passing all of these attributes to the server SDK - using tools like Cookies if needed to ensure they're attached on first requests. If the user objects on the client and server aren't identical, modern SDKs will throw an InvalidBootstrap warning.

Client SDKs also auto-generate a StableID, and its important to manage the lifecycle of this ID to be sure that it is consistent on client and server side. Managing this with a cookie is often easiest, see [Keeping StableID Consistent](/client/javascript-sdk-stable-id#keeping-stableid-consistent). If StableID differs between Client and Server, you'll see a BootstrapStableIDMismatch warning, and checks with this warning won't contribute to your experiment analyses.

### getClientInitializeResponse and the legacy JS SDK

If you are migrating from the legacy JS Client, you will need to make some updates to how your server SDK generates values. The default hashing algorithm was changed from `sha256` to `djb2` for performance and size reasons.

## Local Overrides

Local Overrides are a way to override the values of gates, configs, experiments, and layers for testing purposes. This is useful for local development or testing scenarios where you want to force a specific value without having to change the configuration in the Statsig console.

```csharp  theme={null}
statsig.OverrideGate("test_gate", true);

statsig.OverrideDynamicConfig("test_config", new Dictionary<string, object>
{
    ["color"] = "red",
    ["size"] = 42,
    ["enabled"] = true
});

statsig.OverrideExperiment("test_experiment", new Dictionary<string, object>
{
    ["variant"] = "treatment",
    ["multiplier"] = 1.5
});

statsig.OverrideExperimentByGroupName("test_experiment", "treatment_group");

statsig.OverrideLayer("test_layer", new Dictionary<string, object>
{
    ["theme"] = "dark",
    ["font_size"] = 16
});

statsig.OverrideParameterStore("testing123", new Dictionary<string, object>()
{
    ["brush_color"] = "blue",
    ["monochromatic"] = true,
    ["weight"] = 42,
    ["gradient"] = 3.14,
    ["pen_sizes"] = [1, 2, 3, 4, 5],
    ["artwork"] = new Dictionary<string, object>()
        {
            ["nesting"] = "treatment"
        }
});
```

You can also specify a user ID for targeted overrides:

```csharp  theme={null}
statsig.OverrideGate("test_gate", true, "user_123");

statsig.OverrideDynamicConfig("test_config", new Dictionary<string, object>
{
    ["special_feature"] = true
}, "user_123");
```

Local overrides are useful for:

* Testing specific configurations during development
* QA testing with known values
* Debugging feature flag behavior
* Integration testing with predictable results

Note: Overrides persist for the lifetime of the Statsig instance and affect all evaluations unless a specific user ID is provided.

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

```csharp  theme={null}
using System.Collections.Generic;
using Statsig;

// Implement PersistentStorage to control how user stickiness is stored.
public class MyPersistentStorage : PersistentStorage
{
    private readonly Dictionary<string, Dictionary<string, StickyValues>> _store = new();

    public override IDictionary<string, StickyValues> Load(string key)
    {
        // Load persisted values for this user from your backing store.
        return _store.TryGetValue(key, out var configs)
            ? new Dictionary<string, StickyValues>(configs)
            : new Dictionary<string, StickyValues>();
    }

    public override void Save(string key, string configName, StickyValues data)
    {
        // Persist the sticky assignment (database, Redis, etc.).
        if (!_store.TryGetValue(key, out var configs))
        {
            configs = new Dictionary<string, StickyValues>();
            _store[key] = configs;
        }

        configs[configName] = data;
    }

    public override void Delete(string key, string configName)
    {
        // Remove the persisted value for this config/user.
        if (_store.TryGetValue(key, out var configs))
        {
            configs.Remove(configName);
        }
    }
}
```

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

Data stores allow you to customize how the SDK fetches and caches feature specifications, enabling advanced use cases like using Redis or other distributed caches.

<CodeGroup>
  ```csharp Csharp theme={null}
  using System.Threading.Tasks;
  using Statsig;

  public class MyDataStore : DataStore
  {
      public Task Initialize()
      {
          // Perform any initialization needed for your data store.
          return Task.CompletedTask;
      }

      public Task Shutdown()
      {
          // Clean up resources.
          return Task.CompletedTask;
      }

      public DataStoreResponse Get(string key)
      {
          // Retrieve data for the given key.
          // This is called during SDK evaluation.
          return Task.FromResult<DataStoreResponse?>(null);
      }

      public void Set(string key, string value, long? time = null)
      {
          // Store data for the given key.
          // Called when SDK receives updates from Statsig.
          return Task.CompletedTask;
      }

      public bool SupportsPollingUpdatesFor(string key)
      {
          // Return true if your store supports polling updates for this key, false otherwise.
          return Task.FromResult(false).CompletedTask;
      }
  }

  // Use data store
  var options = new StatsigOptionsBuilder()
      .SetDataStore(new MyDataStore())
      .Build();

  var statsig = new Statsig("server-secret-key", options);
  await statsig.Initialize();
  ```
</CodeGroup>

## Performance Benefits

The .NET Core SDK leverages Statsig's high-performance Rust evaluation engine through FFI bindings, details:

* Native Rust evaluation engine handles all rule processing
* .NET wrapper provides familiar C# APIs and type safety
* Automatic memory management between .NET and Rust boundaries
* Thread-safe operations across the FFI boundary

## Async/Await Support

All network operations are fully async:

```csharp  theme={null}
await statsig.Initialize();
await statsig.FlushEvents();
await statsig.Shutdown();
```

Evaluation methods are synchronous for optimal performance:

```csharp  theme={null}
var result = statsig.CheckGate(user, "gate_name");
```

## Thread Safety

The Statsig instance is thread-safe and can be used concurrently across multiple threads. Consider using the shared instance(singleton) pattern for application-wide usage:

```csharp  theme={null}
var sharedStatsig = Statsig.NewShared("server-secret-key");
await sharedStatsig.Initialize();

var statsig = Statsig.Shared();
```


Built with [Mintlify](https://mintlify.com).