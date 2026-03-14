# Source: https://docs.statsig.com/server-core/rust-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Rust Server SDK

> Statsig's Next-gen Rust Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-rust" target="_blank" rel="noreferrer">Rust Core on Github</a>,
  <a href="https://crates.io/crates/statsig-rust" target="_blank" rel="noreferrer">Cargo Package</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    To use the SDK, add the Statsig Rust package to your Cargo.toml file:

    ```toml  theme={null}
    [dependencies]
    statsig-rust = "X.Y.Z"  # Replace with the latest version
    ```

    Or, you can use the cargo command:

    ```shell  theme={null}
    cargo add statsig-rust
    ```

    You can find the latest version and documentation at [crates.io/crates/statsig-rust](https://crates.io/crates/statsig-rust).
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```rust  theme={null}
    use statsig_rust::{Statsig, StatsigOptions};
    use std::sync::Arc;

    // Simple initialization
    let statsig = Statsig::new("server-secret-key", None);
    statsig.initialize().await?;

    // Or with StatsigOptions
    let mut options = StatsigOptions::default();
    options.environment = Some("development".to_string());

    let statsig = Statsig::new("server-secret-key", Some(Arc::new(options)));
    statsig.initialize().await?;

    // Don't forget to shutdown when done
    statsig.shutdown().await?;
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder};

let user = StatsigUserBuilder::new_with_user_id("a-user".to_string()).build();

if statsig.check_gate(&user, "a_gate") {
    // Gate is on, enable new feature
} else {
    // Gate is off
}
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder, DynamicConfigEvaluationOptions};
use std::sync::Arc;

// Get a dynamic config for a specific user
let user = StatsigUserBuilder::new_with_user_id("my_user".to_string()).build();
let config = statsig.get_dynamic_config(&user, "a_config");

// Access config values with type-safe getters and fallback values
let product_name = config.get_string("product_name", "Awesome Product v1"); // returns String
let price = config.get_double("price", 10.0); // returns f64
let should_discount = config.get_bool("discount", false); // returns bool
let quantity = config.get_int("quantity", 1); // returns i64

// Advanced Usage:
// You can disable exposure logging for this specific check
let mut options = DynamicConfigEvaluationOptions::default();
options.disable_exposure_logging = Some(true);
let config = statsig.get_dynamic_config_with_options(&user, "a_config", &options);

// The config object also provides metadata about the evaluation
println!("{}", config.rule_id); // The ID of the rule that served this config
println!("{}", config.id_type); // The type of the evaluation (experiment, config, etc)
```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder};

// Values via get_layer
let user = StatsigUserBuilder::new_with_user_id("my_user".to_string()).build();
let layer = statsig.get_layer(&user, "user_promo_experiments");
let title = layer.get_string("title", "Welcome to Statsig!");
let discount = layer.get_double("discount", 0.1);

// Via get_experiment
let title_exp = statsig.get_experiment(&user, "new_user_promo_title");
let price_exp = statsig.get_experiment(&user, "new_user_promo_price");

let title = title_exp.get_string("title", "Welcome to Statsig!");
let discount = price_exp.get_double("discount", 0.1);
```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

```jsx  theme={null}
let param_store = statsig.get_parameter_store("my_parameters");
let param_store_value = param_store.get(&user, "my_parameter_value", false); //false is fallback value
println!("param_store_value: {}", param_store_value);
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder};
use std::collections::HashMap;
use crate::evaluation::dynamic_value::DynamicValue;

// Create a user
let user = StatsigUserBuilder::new_with_user_id("user_id".to_string()).build();

// Create metadata hashmap
let mut metadata = HashMap::new();
metadata.insert("price".to_string(), "9.99".into());
metadata.insert("item_name".to_string(), "diet_coke_48_pack".into());

// Log the event
statsig.log_event(
    &user,
    "add_to_cart",
    Some("SKU_12345".into()),  // value as DynamicValue
    Some(metadata)
);
```

Learn more about identifying users, group analytics, and best practices for logging events in the [logging events guide](/guides/logging-events).

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder};

// Create a user
let user = StatsigUserBuilder::new_with_user_id("user_id".to_string()).build();

// Get a feature gate
let gate = statsig.get_feature_gate(&user, "example_gate");

// Access gate properties
println!("{}", gate.rule_id);
println!("{}", gate.value);  // Boolean value of the gate
```

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

```rust  theme={null}
// Create a shared instance that can be accessed globally
let statsig = Statsig::new_shared("server-secret-key", None).unwrap();
statsig.initialize().await?;

// Access the shared instance from anywhere in your code
let shared_statsig = Statsig::shared();
let is_feature_enabled = shared_statsig.check_gate(&user, "feature_name");

// Check if a shared instance exists
if Statsig::has_shared_instance() {
    // Use the shared instance
}

// Remove the shared instance when no longer needed
Statsig::remove_shared();
```

The shared instance functionality provides a singleton pattern where a single Statsig instance can be created and accessed globally throughout your application. This is useful for applications that need to access Statsig functionality from multiple parts of the codebase without having to pass around a Statsig instance.

* `Statsig::new_shared(sdk_key, options)`: Creates a new shared instance of Statsig that can be accessed globally
* `Statsig::shared()`: Returns the shared instance
* `Statsig::has_shared_instance()`: Checks if a shared instance exists (useful when you aren't sure if the shared instance is ready yet)
* `Statsig::remove_shared()`: Removes the shared instance (useful when you want to switch to a new shared instance)

<Note>
  `has_shared_instance()` and `remove_shared()` are helpful in specific scenarios but aren't required in most use cases where the shared instance is set up near the top of your application.

  Also note that only one shared instance can exist at a time. Attempting to create a second shared instance will result in an error.
</Note>

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

All of the main SDK functions (`check_gate`, `get_dynamic_config`, `get_experiment`, `get_layer`) accept an options parameter with a `disable_exposure_logging` field. When this is set to `true`, the SDK will not automatically log an exposure event. You can then manually log the exposure at a later time using the corresponding manual exposure logging method:

<Tabs>
  <Tab title="Feature Gates">
    ```rust  theme={null}
    result = statsig.check_gate_with_options(&user, 'a_gate_name', FeatureGateEvaluationOptions {disable_exposure_logging: true});
    ```

    ```rust  theme={null}
    statsig.manually_log_gate_exposure(&user, 'a_gate_name')
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```rust  theme={null}
    config = statsig.get_dynamic_config_with_options(&user, 'a_dynamic_config_name', DynamicConfigEvaluationOptions {disable_exposure_logging: true});
    ```

    ```rust  theme={null}
    statsig.manually_log_dynamic_config_exposure(&user, 'a_dynamic_config_name')
    ```
  </Tab>

  <Tab title="Experiments">
    ```rust  theme={null}
    experiment = statsig.get_experiment_with_options(&user, 'an_experiment_name', ExperimentEvaluationOptions {disable_exposure_logging: true});
    ```

    ```rust  theme={null}
    statsig.manually_log_experiment_exposure(&user, 'an_experiment_name')
    ```
  </Tab>

  <Tab title="Layers">
    ```rust  theme={null}
    layer = statsig.get_layer_with_options(&user, 'a_layer_name',  LayerEvaluationOptions {disable_exposure_logging: true});
    paramValue = layer.get('a_param_name', 'fallback_value')
    ```

    ```rust  theme={null}
    statsig.manually_log_layer_parameter_exposure(&user, 'a_layer_name', 'a_param_name')
    ```
  </Tab>
</Tabs>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```rust  theme={null}
use statsig_rust::StatsigUserBuilder;
use std::collections::HashMap;

// Create a user with just a user ID
let user = StatsigUserBuilder::new_with_user_id("user-123".to_string())
    .build();

// Or create a user with custom IDs
let mut custom_ids = HashMap::new();
custom_ids.insert("employee_id".to_string(), "emp-456".to_string());
let user_with_custom_ids = StatsigUserBuilder::new_with_custom_ids(custom_ids)
    .build();

// Create a user with several properties
let mut custom_fields = HashMap::new();
custom_fields.insert("plan".to_string(), "premium".into());
custom_fields.insert("age".to_string(), 25.into());

let user = StatsigUserBuilder::new_with_user_id("user-123".to_string())
    .email(Some("user@example.com".to_string()))
    .ip(Some("192.168.1.1".to_string()))
    .user_agent(Some("Mozilla/5.0...".to_string()))
    .country(Some("US".to_string()))
    .locale(Some("en-US".to_string()))
    .app_version(Some("1.0.0".to_string()))
    .custom(Some(custom_fields))
    .build();

// Private Attributes (not forwarded to integrations)
let mut private_attrs = HashMap::new();
private_attrs.insert("internal_id".to_string(), "emp-123".into());

let user_with_private = StatsigUserBuilder::new_with_user_id("user-123".to_string())
    .email(Some("user@example.com".to_string()))
    .private_attributes(Some(private_attrs))
    .build();
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  <ResponseField name="data_store" type="Option<Arc<dyn DataStoreTrait>>">
    External data store for Statsig values.
  </ResponseField>

  <ResponseField name="disable_all_logging" type="Option<bool>">
    When true, disables all event logging.
  </ResponseField>

  <ResponseField name="disable_network" type="Option<bool>">
    When `true`, disables all network functions: event & exposure logging, spec downloads, and ID List downloads. Formerly called "localMode".
  </ResponseField>

  <ResponseField name="enable_id_lists" type="Option<bool>">
    Enable/disable ID list functionality. **Required to be `true` when using segments with more than 1000 IDs.** See [ID List segments](/segments/add-id-list) for more details.
  </ResponseField>

  <ResponseField name="disable_user_agent_parsing" type="Option<bool>" default="false">
    If set to true, the SDK will NOT attempt to parse UserAgents (attached to the user object) into browserName, browserVersion, systemName, systemVersion, and appVersion at evaluation time, when needed for evaluation.
  </ResponseField>

  <ResponseField name="wait_for_user_agent_init" type="Option<bool>" default="false">
    When set to true, the SDK will wait until user agent parsing data is fully loaded during initialization. This may slow down by \~1 second startup but ensures that parsing of the user's userAgent string into fields like browserName, browserVersion, systemName, systemVersion, and appVersion is ready before any evaluations.
  </ResponseField>

  <ResponseField name="disable_user_country_lookup" type="Option<bool>" default="false">
    If set to true, the SDK will NOT attempt to parse IP addresses (attached to the user object at user.ip) into Country codes at evaluation time, when needed for evaluation.
  </ResponseField>

  <ResponseField name="wait_for_country_lookup_init" type="Option<bool>" default="false">
    When set to true, the SDK will wait for country lookup data (e.g., GeoIP or YAML files) to fully load during initialization. This may slow down by \~1 second startup but ensures that IP-to-country parsing is ready at evaluation time.
  </ResponseField>

  <ResponseField name="environment" type="Option<String>">
    Environment parameter for evaluation.
  </ResponseField>

  <ResponseField name="event_logging_adapter" type="Option<Arc<dyn EventLoggingAdapter>>">
    Custom adapter for event logging.
  </ResponseField>

  <ResponseField name="event_logging_flush_interval_ms" type="Option<u32>">
    How often events are flushed to Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="event_logging_max_queue_size" type="Option<u32>">
    Maximum number of events to queue before forcing a flush.

    * Default is `2000`
    * event\_logging\_max\_queue\_size \* event\_logging\_max\_pending\_batch\_queue\_size is the upper limit on how many events are queued
    * See also `event_logging_max_pending_batch_queue_size`
  </ResponseField>

  <ResponseField name="event_logging_max_pending_batch_queue_size" type="Option<u32>">
    Maximum number of event batches to hold in buffer to retry.

    * Default is `100`.
    * event\_logging\_max\_queue\_size \* event\_logging\_max\_pending\_batch\_queue\_size is the upper limit on how many events are queued
    * eg: 2000 \* 100 means the SDK can process 200k event per second before events start getting dropped
    * See also `event_logging_max_queue_size`.
  </ResponseField>

  <ResponseField name="fallback_to_statsig_api" type="Option<bool>">
    Whether to fallback to the Statsig API if custom endpoints fail.
  </ResponseField>

  <ResponseField name="id_lists_adapter" type="Option<Arc<dyn IdListsAdapter>>">
    Custom adapter for ID lists.
  </ResponseField>

  <ResponseField name="id_lists_sync_interval_ms" type="Option<u32>">
    How often the SDK updates ID lists from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="id_lists_url" type="Option<String>">
    Custom URL for fetching ID lists.
  </ResponseField>

  <ResponseField name="init_timeout_ms" type="Option<u64>">
    Sets the maximum timeout for initialization requests (in milliseconds).
  </ResponseField>

  <ResponseField name="log_event_url" type="Option<String>">
    Custom URL for logging events.
  </ResponseField>

  <ResponseField name="observability_client" type="Option<Weak<dyn ObservabilityClient>>">
    Client for collecting observability data.
  </ResponseField>

  <ResponseField name="output_log_level" type="Option<LogLevel>">
    Controls the verbosity of SDK logs.
  </ResponseField>

  <ResponseField name="override_adapter" type="Option<Arc<dyn OverrideAdapter>>">
    Custom adapter for overrides.
  </ResponseField>

  <ResponseField name="spec_adapters_config" type="Option<Vec<SpecAdapterConfig>>">
    Configuration for specification adapters.
  </ResponseField>

  <ResponseField name="specs_adapter" type="Option<Arc<dyn SpecsAdapter>>">
    Custom adapter for specifications.
  </ResponseField>

  <ResponseField name="specs_sync_interval_ms" type="Option<u32>">
    How often the SDK updates specifications from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="specs_url" type="Option<String>">
    Custom URL for fetching feature specifications.
  </ResponseField>

  <ResponseField name="global_custom_fields" type="Option<HashMap<String, DynamicValue>>">
    Global custom fields to include with all evaluations.
  </ResponseField>

  <ResponseField name="proxy_config" type="Option<ProxyConfig>">
    Configuration for connecting through a proxy server. The `ProxyConfig` struct has the following properties:

    * `proxy_host`: Option\<String> - Specifies the proxy server host
    * `proxy_port`: Option\<u16> - Specifies the proxy server port
    * `proxy_auth`: Option\<String> - For proxy authentication (format: `"username:password"`)
    * `proxy_protocol`: Option\<String> - Specifies the protocol (e.g., `"http"`, `"https"`)
  </ResponseField>

  ### Example Usage

  ```rust  theme={null}
  use statsig_rust::{Statsig, StatsigOptions};
  use std::sync::Arc;

  // Initialize StatsigOptions with custom parameters
  let mut options = StatsigOptions::default();
  options.environment = Some("development".to_string());
  options.init_timeout_ms = Some(3000);
  options.disable_all_logging = Some(false);
  options.enable_id_lists = Some(true);
  options.output_log_level = Some(LogLevel::Info); // LogLevel enum, not a string

  // Pass the options object into Statsig::new()
  let statsig = Statsig::new("server-secret-key", Some(Arc::new(options)));
  statsig.initialize().await?;

  // Or, use the builder pattern for a more fluent interface
  let options = StatsigOptions::builder()
      .environment(Some("development".to_string()))
      .init_timeout_ms(Some(3000))
      .disable_all_logging(Some(false))
      .enable_id_lists(Some(true))
      .specs_sync_interval_ms(Some(30000))
      // Configure proxy settings
      .proxy_config(Some(ProxyConfig {
          proxy_host: Some("proxy.example.com".to_string()),
          proxy_port: Some(8080),
          proxy_protocol: Some("https".to_string()),
          proxy_auth: None, // Use Some("username:password".to_string()) if authentication is required
      }))
      .build();

  // Pass the options object into Statsig::new()
  let statsig = Statsig::new("server-secret-key", Some(Arc::new(options)));
  statsig.initialize().await?;
  ```
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```rust  theme={null}
statsig.shutdown().await?;
```

Alternatively, you can manually flush events without shutting down:

```rust  theme={null}
// Manually flush events to the server
statsig.flush_events().await;
```

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

```rust  theme={null}
use statsig_rust::{Statsig, StatsigUserBuilder, sdk_event_emitter::SdkEvent};

let statsig = Statsig::new("server-secret-key", None)?;
statsig.initialize().await?;

// Subscribe to gate evaluation events
let gate_sub_id = statsig.subscribe(SdkEvent::GATE_EVALUATED, |event| {
    if let SdkEvent::GateEvaluated { gate_name, value, rule_id, reason } = event {
        println!("Gate evaluated: {} = {}, rule: {}, reason: {}", 
                 gate_name, value, rule_id, reason);
    }
});

// Subscribe to dynamic config evaluation events
let config_sub_id = statsig.subscribe(SdkEvent::DYNAMIC_CONFIG_EVALUATED, |event| {
    if let SdkEvent::DynamicConfigEvaluated { dynamic_config } = event {
        println!("Config evaluated: {}", dynamic_config.name);
    }
});

// Subscribe to experiment evaluation events
let experiment_sub_id = statsig.subscribe(SdkEvent::EXPERIMENT_EVALUATED, |event| {
    if let SdkEvent::ExperimentEvaluated { experiment } = event {
        println!("Experiment evaluated: {} -> {}", 
                 experiment.name, experiment.group_name);
    }
});

// Subscribe to layer evaluation events
let layer_sub_id = statsig.subscribe(SdkEvent::LAYER_EVALUATED, |event| {
    if let SdkEvent::LayerEvaluated { layer } = event {
        println!("Layer evaluated: {}", layer.name);
    }
});

// Subscribe to all events
let all_events_sub_id = statsig.subscribe(SdkEvent::ALL, |event| {
    println!("Event received: {}", event.get_name());
});

// Unsubscribe from specific event types
statsig.unsubscribe(SdkEvent::GATE_EVALUATED);

// Unsubscribe using subscription ID
statsig.unsubscribe_by_id(&config_sub_id);

// Unsubscribe from all events
statsig.unsubscribe_all();
```

## Local Overrides

Local Overrides are a way to override the values of gates, configs, experiments, and layers for testing purposes. This is useful for local development or testing scenarios where you want to force a specific value without having to change the configuration in the Statsig console.

```Rust  theme={null}
// Overrides the given gate to the specified value
statsig.override_gate("test_gate", true, None);
	
// Overrides the given dynamic config to the provided value
statsig.override_dynamic_config("test_1", my_map.clone(), None); //my_map is HashMap<String, Value>

// Overrides the given experiment to the provided value
statsig.override_experiment("test_xp_1", my_map.clone(), None); //my_map is HashMap<String, Value>
	
// Overrides the given layer to the provided value
statsig.override_layer("user_promo_experiments", my_map.clone(), None); //my_map is HashMap<String, Value>

//Alternatively, get the Experiment object for a given groupName
let group_exp = statsig.get_experiment_by_group_name("pricing_experiment", "premium_group");
let premium_price = group_exp.get_double("price", 9.99);
```

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

```rust  theme={null}
pub trait PersistentStorageTrait: Send + Sync {
    fn load(&self, key: &str) -> Result<Option<UserPersistedValues>, PersistentStorageErrorEnum>;
    fn save(&self, key: &str, config_name: &str, data: &StickyValues) -> Result<(), PersistentStorageErrorEnum>;
    fn delete(&self, key: &str, config_name: &str) -> Result<(), PersistentStorageErrorEnum>;
}
```

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

```rust  theme={null}
pub trait DataStoreTrait: Send + Sync {
    fn initialize(&self) -> Result<(), DataStoreErrorEnum>;
    fn shutdown(&self) -> Result<(), DataStoreErrorEnum>;
    fn get(&self, key: &str) -> Result<Option<DataStoreResponse>, DataStoreErrorEnum>;
    fn set(&self, key: &str, value: &str, time: Option<u64>) -> Result<(), DataStoreErrorEnum>;
    fn support_polling_updates_for(&self, key: &str) -> Result<bool, DataStoreErrorEnum>;
}

pub struct DataStoreResponse {
    pub result: String,
    pub time: Option<u64>,
}
```

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

```rust  theme={null}
pub trait OutputLogProvider: Send + Sync {
    fn initialize(&self);
    fn debug(&self, tag: &str, msg: String);
    fn info(&self, tag: &str, msg: String);
    fn warn(&self, tag: &str, msg: String);
    fn error(&self, tag: &str, msg: String);
    fn shutdown(&self);
}
```

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

```rust  theme={null}
pub trait ObservabilityClient: Send + Sync {
    fn init(&self);
    fn increment(&self, metric_name: &str, value: f64, tags: &HashMap<String, String>);
    fn gauge(&self, metric_name: &str, value: f64, tags: &HashMap<String, String>);
    fn dist(&self, metric_name: &str, value: f64, tags: &HashMap<String, String>);
    fn error(&self, tag: &str, error: &str);
}
```

## Fields Needed Methods (Enterprise Only)

<Info>
  This is available for Enterprise contracts. Please reach out to our support team, your sales contact, or via our [Slack community](https://statsig.com/slack) if you want this enabled.
</Info>

These methods allow you to retrieve a list of user fields that are used in the targeting rules for gates, configs, experiments, and layers.

### Description

These methods return an array of strings representing the user fields that are referenced in the targeting rules or conditions of the specified feature. This can be useful for understanding which user properties influence a particular feature's behavior.

```rust  theme={null}
// Get fields needed for a gate
let fields_needed: Vec<String> = statsig.get_fields_needed_for_gate("gate_name");

// Get fields needed for a dynamic config
let fields_needed: Vec<String> = statsig.get_fields_needed_for_dynamic_config("config_name");

// Get fields needed for an experiment
let fields_needed: Vec<String> = statsig.get_fields_needed_for_experiment("experiment_name");

// Get fields needed for a layer
let fields_needed: Vec<String> = statsig.get_fields_needed_for_layer("layer_name");
```

### Field Mapping

The fields returned by these methods correspond to the following user properties:

```rust  theme={null}
// Field mapping between user properties and internal field names
let field_mapping = std::collections::HashMap::from([
    ("userID", "u"),
    ("email", "e"),
    ("ip", "i"),
    ("userAgent", "ua"),
    ("country", "c"),
    ("locale", "l"),
    ("appVersion", "a"),
    ("time", "t"),
    ("stableID", "s"),
    ("environment", "en"),
    ("targetApp", "ta"),
]);

// Custom fields are prefixed with "cf:"
// Example: fields.add("cf:" + field_name);
```

## FAQ

<AccordionGroup>
  <Accordion title="How do I run experiments for logged out users?">
    See the guide on [device level experiments](/guides/device-level-experiments)
  </Accordion>
</AccordionGroup>

## Reference

### Fields Needed Methods (Enterprise Only)

```rust  theme={null}
// Get user fields needed for a gate evaluation
pub fn get_fields_needed_for_gate(&self, gate_name: &str) -> Vec<String>

// Get user fields needed for a dynamic config evaluation
pub fn get_fields_needed_for_dynamic_config(&self, config_name: &str) -> Vec<String>

// Get user fields needed for an experiment evaluation
pub fn get_fields_needed_for_experiment(&self, experiment_name: &str) -> Vec<String>

// Get user fields needed for a layer evaluation
pub fn get_fields_needed_for_layer(&self, layer_name: &str) -> Vec<String>
```

<Info>
  This is available for Enterprise contracts. Please reach out to our support team, your sales contact, or via our [Slack community](https://statsig.com/slack) if you want this enabled.
</Info>

These methods allow you to retrieve a list of user fields that are used in the targeting rules for gates, configs, experiments, and layers.

#### Description

These methods return an array of strings representing the user fields that are referenced in the targeting rules or conditions of the specified feature. This can be useful for understanding which user properties influence a particular feature's behavior.

#### Field Mapping

The fields returned by these methods correspond to the following user properties:

```
// Field mapping between user properties and internal field names
const fieldMapping = {
  userID: 'u',
  email: 'e',
  ip: 'i',
  userAgent: 'ua',
  country: 'c',
  locale: 'l',
  appVersion: 'a',
  time: 't',
  stableID: 's',
  environment: 'en',
  targetApp: 'ta',
};

// Custom fields are prefixed with "cf:"
// Example: fields.add('cf:' + field);
```


Built with [Mintlify](https://mintlify.com).