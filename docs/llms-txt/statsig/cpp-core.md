# Source: https://docs.statsig.com/server-core/cpp-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C++ Server SDK

> Statsig's Next-gen Cpp Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-cpp-core/" target="_blank" rel="noreferrer">Cpp Core on Github</a>
  <a href="https://github.com/statsig-io/statsig-server-core/" target="_blank" rel="noreferrer">Cpp Core Working Repo</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Installation

    All core logic are written in rust, and we don't require rust environment from you, so we pre-built all binaries (attached as assets with each release).
    Our CMakeLists.txt file handle all the complexity for you.

    If you encounter any installation or build issue, please reach back to us!

    ```CMake  theme={null}
    FetchContent_Declare(
        Statsig
        GIT_REPOSITORY    https://github.com/statsig-io/statsig-cpp-core.git
        GIT_TAG           0.12.2-rc.1 
    )
    FetchContent_MakeAvailable(Statsig)

    target_include_directories(CppApp PRIVATE ${statsig_SOURCE_DIR}/include)
    target_include_directories(CppApp PRIVATE ${statsig_SOURCE_DIR}/src)

    target_link_libraries(CppApp PRIVATE Statsig)
    ```

    <testedPlatforms />
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```cpp  theme={null}
    #include <statsig/statsig.h>

    statsig_cpp_core::StatsigOptionsBuilder optionsBuilder;
    ptionsBuilder.environment = "development";
    ptionsBuilder.specs_url = api_v2 + "/download_config_specs";
    optionsBuilder.log_event_url = api + "/log_event";
    optionsBuilder.id_lists_url = api + "/get_id_lists";
    statsig_cpp_core::StatsigOptions options = optionsBuilder.build();
    Statsig statsig("server-secret-key", options);
    statsig.initializeBlocking().wait();

    ```

    `initialize` will perform a network request. After `initializeBlocking` completes, virtually all SDK operations will be synchronous. The SDK will fetch updates from Statsig in the background, independently of your API calls.

    <Initialization2 />
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```cpp  theme={null}

if (statsig.checkGate(user, "a_gate")) {
    // Gate is on, enable new feature
} else {
    // Gate is off
}
```

You can also disable exposure logging for this evaluation:

```cpp  theme={null}
FeatureGateEvaluationOptions options;
options.disable_exposure_logging = true;
bool gateValue = statsig.check_gate(user, "a_gate", options);
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```cpp  theme={null}
// Get a dynamic config for a specific user
DynamicConfig config = statsig.getDynamicConfig(user, "a_config");

// Access config values (We will provide accessors)
std::string product_name = config.value.get("product_name", "Awesome Product v1");
double price = config.value.get("price", 10.0);


// Access evaluation details such as rule id 
statsig_cpp_core::EvaluationDetails detail = config.details;
std::cout << config.rule_id << std::endl;  // The ID of the rule that served this config
std::cout << config.id_type << std::endl;  // The type of the evaluation (experiment, config, etc)

// Advanced Usage:
// You can disable exposure logging for this specific check
DynamicConfigEvaluationOptions options;
options.disable_exposure_logging = true;
config = statsig.getDynamicConfig(user, "a_config", options);
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```cpp  theme={null}
// Get a experiment for a specific user
statsig_cpp_core::Experiment exp = statsig.getExpriment(user, "an_experiment");

// Access config values (We will provide accessors)
auto product_name = exp.value.get("product_name", "Awesome Product v1");
auto price = exp.value.get("price", 10.0);


// Access evaluation details such as rule id 
statsig_cpp_core::EvaluationDetails detail = exp.details;
std::cout << exp.rule_id << std::endl;  // The ID of the rule that served this config
std::cout << exp.id_type << std::endl;  // The type of the evaluation (experiment, config, etc)

// Advanced Usage:
// You can disable exposure logging for this specific check
ExperimentEvaluationOptions options;
options.disable_exposure_logging = true;
config = statsig.getExperiment(user, "an_experiment", options);


```

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```cpp  theme={null}
FeatureGate gate = statsig.getFeatureGate(user, "example_gate");
std::cout << gate.rule_id << std::endl;
std::cout << gate.value << std::endl;
```

The `get_feature_gate()` method returns a FeatureGate object that provides:

* `value`: The boolean gate value
* `rule_id`: The ID of the rule that served this gate
* `id_type`: The type of the evaluation
* `evaluation_details`: Additional metadata about the evaluation

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```cpp  theme={null}
statsig.log_event(
    user,  
    "add_to_cart",
    {
        {"price", "9.99"},
        {"item_name", "diet_coke_48_pack"}
    }  
);
```

The `log_event` method supports multiple overloads:

* `log_event(user, event_name)`
* `log_event(user, event_name, string_value)`
* `log_event(user, event_name, string_value, metadata)`

We will add support for numerical value and metadata

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```cpp  theme={null}
  statsig_cpp_core::UserBuilder builder;
  builder.setUserID(j["userID"]);
  builder.setCustomIDs(j["customIDs"]);
  builder.setCountry(j["customIDs"]);
  statsig_cpp_core::User user = builder.build();
  // UserBuilder also supports deserialize from json
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

```cpp  theme={null}
statsig_cpp_core::StatsigOptionsBuilder optionsBuilder;
ptionsBuilder.environment = "development";
ptionsBuilder.specs_url = api_v2 + "/download_config_specs";
optionsBuilder.log_event_url = api + "/log_event";
optionsBuilder.id_lists_url = api + "/get_id_lists";
statsig_cpp_core::StatsigOptions options = optionsBuilder.build();
## Available Options
std::optional<std::string> specs_url;
std::optional<std::string> id_lists_url;
std::optional<std::string> log_event_url;
std::optional<std::string> output_log_level;
std::optional<std::string> environment;
bool enable_id_lists = false;
bool disable_all_logging = false;
bool disable_country_lookup = false;
bool disable_network = false;
```

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```cpp  theme={null}
statsig.shutdownBlocking();
```

The `shutdown()` method will:

* Flush any pending events to Statsig servers
* Gracefully shutdown the SDK, cleaning up resources
* Wait for all operations to complete

It's recommended to call `shutdown()` before your application exits to ensure all events are sent.

## Reference

### API Methods

* `check_gate(user: StatsigUser, gate_name: str, options: Optional[FeatureGateEvaluationOptions] = None) -> bool`
* `get_dynamic_config(user: StatsigUser, config_name: str, options: Optional[DynamicConfigEvaluationOptions] = None) -> DynamicConfig`
* `get_experiment(user: StatsigUser, experiment_name: str, options: Optional[ExperimentEvaluationOptions] = None) -> DynamicConfig`
* `get_layer(user: StatsigUser, layer_name: str, options: Optional[LayerEvaluationOptions] = None) -> Layer`
* `get_feature_gate(user: StatsigUser, gate_name: str, options: Optional[FeatureGateEvaluationOptions] = None) -> FeatureGate`
* `log_event(user: StatsigUser, event_name: str, value: Optional[Union[str, float]] = None, metadata: Optional[Dict[str, str]] = None) -> None`
* `shutdown() -> AsyncResult[None]`

### Fields Needed Methods

The following methods return information about which user fields are needed for evaluation:

* `get_gate_fields_needed(gate_name: str) -> List[str]`
* `get_dynamic_config_fields_needed(config_name: str) -> List[str]`
* `get_experiment_fields_needed(experiment_name: str) -> List[str]`
* `get_layer_fields_needed(layer_name: str) -> List[str]`

These methods return a list of strings representing the user fields that are required to properly evaluate the specified gate, config, experiment, or layer.


Built with [Mintlify](https://mintlify.com).