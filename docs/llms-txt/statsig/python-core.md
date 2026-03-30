# Source: https://docs.statsig.com/server-core/python-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Python Server SDK

> Statsig's Next-gen Python Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-pyo3" target="_blank" rel="noreferrer">Python Core on Github</a>
</Callout>

<Tip>Migrating from the Legacy Python SDK? See our [Migration Guide](/server-core/migration-guides/python).</Tip>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Installation

    ```shell  theme={null}
    pip install statsig-python-core
    ```

    ## Tested Platforms

    <Accordion title="Specific Platform Info">
      Docker base images where the Python Core SDK has been tested and verified:

      | Docker Base Image                   | Description                                          |
      | ----------------------------------- | ---------------------------------------------------- |
      | `python:3.7-alpine`                 | Python 3.7 on Alpine Linux                           |
      | `python:3.7-buster`                 | Python 3.7 on Debian Buster                          |
      | `python:3.7-slim`                   | Python 3.7 slim variant                              |
      | `quay.io/pypa/manylinux2014_x86_64` | Manylinux 2014 x86\_64 for broad Linux compatibility |
      | `python:3.10-alpine`                | Python 3.10 on Alpine Linux                          |
      | `python:3.10-slim`                  | Python 3.10 slim variant                             |
    </Accordion>
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    ```python  theme={null}
    from statsig_python_core import Statsig, StatsigOptions # note, import statement has underscores while install has dashes

    options = StatsigOptions()
    options.environment = "development"

    statsig = Statsig("secret-key", options)
    statsig.initialize().wait()

    # If you're running this in a script, be sure to wait for shutdown at the end to flush event logs to statsig
    statsig.shutdown().wait()
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.

    ### ⚠️ Warning: Process Forking and WSGI Servers

    **Important:** Never fork processes after calling `statsig.initialize()`. Doing so will put Statsig in an undefined state and may cause deadlock.

    The Python Core SDK uses internal threading and async runtime components that do not work correctly when copied across process boundaries. When a process forks after initialization, these components can become corrupted, leading to:

    * Deadlocks in event logging
    * Hanging initialization calls
    * Unpredictable SDK behavior
    * Silent failures in feature evaluation

    ### Initializing with WSGI servers

    For production deployments using WSGI servers like uWSGI or Gunicorn, ensure Statsig is initialized **after** the worker processes are forked, not in the main process.

    <Tabs>
      <Tab title="uWSGI">
        #### ✅ Correct: uWSGI example

        ```python expandable theme={null}
        # app.py
        from statsig_python_core import Statsig, StatsigOptions
        from flask import Flask

        app = Flask(__name__)
        statsig = None

        def init_statsig():
            global statsig
            if statsig is None:
                options = StatsigOptions()
                options.environment = "production"
                statsig = Statsig("your-server-secret-key", options)
                statsig.initialize().wait()

        # Initialize in each worker process
        @app.before_first_request
        def before_first_request():
            init_statsig()

        @app.route('/')
        def index():
            # Use statsig here
            return "Hello World"
        ```

        ```ini  theme={null}
        # uwsgi.ini
        [uwsgi]
        module = app:app
        master = true
        processes = 4
        # Statsig will be initialized in each worker process
        ```
      </Tab>

      <Tab title="Gunicorn">
        #### ✅ Correct: Gunicorn example

        ```python  theme={null}
        # gunicorn_config.py
        def post_fork(server, worker):
            # Initialize Statsig after worker process is forked
            from app import init_statsig
            init_statsig() # as defined above

        # ...app.py
        ```

        ```bash  theme={null}
        # Start Gunicorn with post-fork hook
        gunicorn --config gunicorn_config.py app:app
        ```
      </Tab>

      <Tab title="FastAPI">
        #### ✅ Correct: FastAPI example

        ```python expandable theme={null}
        from fastapi import FastAPI
        from statsig_python_core import Statsig, StatsigOptions

        app = FastAPI()
        statsig = None

        @app.on_event("startup")
        async def startup_event():
            global statsig
            options = StatsigOptions()
            options.environment = "production"
            statsig = Statsig("your-server-secret-key", options)
            statsig.initialize().wait()

        @app.on_event("shutdown")
        async def shutdown_event():
            if statsig:
                statsig.shutdown().wait()

        @app.get("/")
        async def root():
            # Use statsig here
            return {"message": "Hello World"}
        ```
      </Tab>
    </Tabs>

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```python  theme={null}
user = StatsigUser("a-user")

if statsig.check_gate(user, "a_gate"):
    # Gate is on, enable new feature
else:
    # Gate is off
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```python  theme={null}
# Get a dynamic config for a specific user
config = statsig.get_dynamic_config(StatsigUser("my_user"), "a_config")

# Access config values with type-safe getters and fallback values
product_name = config.get_string("product_name", "Awesome Product v1")  # returns String
price = config.get_float("price", 10.0)  # returns float
should_discount = config.get_bool("discount", False)  # returns bool
quantity = config.get_integer("quantity", 1)  # returns int64

# Advanced Usage:
# You can disable exposure logging for this specific check
options = DynamicConfigEvaluationOptions(disable_exposure_logging=True)
config = statsig.get_dynamic_config(user, "a_config", options)

# The config object also provides metadata about the evaluation
print(config.rule_id)  # The ID of the rule that served this config
print(config.id_type)  # The type of the evaluation (experiment, config, etc)
```

The `get_dynamic_config()` method returns a DynamicConfig object that allows you to:

* Fetch typed values with fallback defaults using `get_string()`, `get_float()`, `get_boolean()`, and `get_integer()`
* Access evaluation metadata through properties like `rule_id` and `id_type`
* Configure evaluation behavior using `DynamicConfigEvaluationOptions`

By default, Statsig logs exposures automatically when configs are evaluated. You can disable this for specific checks using the evaluation options.

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```Python  theme={null}
# Values via get_layer
layer = statsig.get_layer(StatsigUser("my_user"), "user_promo_experiments")
title = layer.get_string("title", "Welcome to Statsig!")
discount = layer.get_float("discount", 0.1)

# Via get_experiment
title_exp = statsig.get_experiment(StatsigUser("my_user"), "new_user_promo_title")
price_exp = statsig.get_experiment(StatsigUser("my_user"), "new_user_promo_price")

title = title_exp.get_string("title", "Welcome to Statsig!")
discount = price_exp.get_float("discount", 0.1)
```

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```python  theme={null}
gate = statsig.get_feature_gate(user, "example_gate")
print(gate.rule_id)
print(gate.value)
```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

```python  theme={null}
# Get a Parameter Store by name
param_store = statsig.get_parameter_store(user, "my_parameter_store")
```

### Retrieving Parameter Values

Parameter Store provides methods for retrieving values of different types with fallback defaults.

```python  theme={null}
# String parameters
string_value = param_store.get_string("string_param", "default_value")

# Boolean parameters
bool_value = param_store.get_bool("bool_param", False)

# Numeric parameters
float_value = param_store.get_float("float_param", 0.0)
integer_value = param_store.get_integer("integer_param", 0)

# Complex parameters
default_array = ["item1", "item2"]
array_value = param_store.get_array("array_param", default_array)

default_map = {"key": "value"}
map_value = param_store.get_map("map_param", default_map)
```

### Evaluation Options

You can disable exposure logging when retrieving a parameter store:

```python  theme={null}
from statsig_python_core import ParameterStoreEvaluationOptions

options = ParameterStoreEvaluationOptions(disable_exposure_logging=True)
param_store = statsig.get_parameter_store(user, "my_parameter_store", options)
```

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```Python  theme={null}
statsig.log_event(
    user=StatsigUser("user_id"),  # Replace with your user object
    event_name="add_to_cart",
    value="SKU_12345",
    metadata={
        "price": "9.99",
        "item_name": "diet_coke_48_pack"
    }
)
```

### Sending Events to Log Explorer

You can forward logs to Logs Explorer for convenient analysis using the Forward Log Line Event API. This lets you include custom metadata and event values with each log.

```python  theme={null}
user = StatsigUser(
    user_id="a-user",
    custom={
        "service": "my-service",
        "pod": "my-pod",
        "namespace": "my-namespace",
        "container": "my-container",
        # ...include any service-specific metadata
    }
)

# levels: trace, debug, info, log, warn, error
statsig.forward_log_line_event(user, "warn", "script failed to load", {
    "custom_metadata": "script_name:my-script"
    # ... include any event-specific metadata
})
```

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

```python  theme={null}
# Create a shared instance that can be accessed globally
statsig = Statsig.new_shared("secret-key", options)
statsig.initialize().wait()

# Access the shared instance from anywhere in your code
shared_statsig = Statsig.shared()
is_feature_enabled = shared_statsig.check_gate(StatsigUser("user_id"), "feature_name")

# Check if a shared instance exists
if Statsig.has_shared_instance():
    # Use the shared instance
    pass

# Remove the shared instance when no longer needed
Statsig.remove_shared()
```

The shared instance functionality provides a singleton pattern where a single Statsig instance can be created and accessed globally throughout your application. This is useful for applications that need to access Statsig functionality from multiple parts of the codebase without having to pass around a Statsig instance.

* `Statsig.new_shared(sdk_key, options)`: Creates a new shared instance of Statsig that can be accessed globally
* `Statsig.shared()`: Returns the shared instance
* `Statsig.has_shared_instance()`: Checks if a shared instance exists (useful when you aren't sure if the shared instance is ready yet)
* `Statsig.remove_shared()`: Removes the shared instance (useful when you want to switch to a new shared instance)

<Note>
  `has_shared_instance()` and `remove_shared()` are helpful in specific scenarios but aren't required in most use cases where the shared instance is set up near the top of your application.

  Also note that only one shared instance can exist at a time. Attempting to create a second shared instance will result in an error.
</Note>

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

All of the main SDK functions (`check_gate`, `get_dynamic_config`, `get_experiment`, `get_layer`) accept an optional `disable_exposure_logging` parameter. When this is set to `True`, the SDK will not automatically log an exposure event. You can then manually log the exposure at a later time using the corresponding manual exposure logging method:

<Tabs>
  <Tab title="Feature Gates">
    ```python  theme={null}
    result = statsig.check_gate(aUser, 'a_gate_name', FeatureGateEvaluationOptions(disable_exposure_logging=True))
    ```

    ```python  theme={null}
    statsig.manually_log_gate_exposure(aUser, 'a_gate_name')
    ```
  </Tab>

  <Tab title="Dynamic Configs">
    ```python  theme={null}
    config = statsig.get_dynamic_config(aUser, 'a_dynamic_config_name', DynamicConfigEvaluationOptions(disable_exposure_logging=True))
    ```

    ```python  theme={null}
    statsig.manually_log_dynamic_config_exposure(aUser, 'a_dynamic_config_name')
    ```
  </Tab>

  <Tab title="Experiments">
    ```python  theme={null}
    experiment = statsig.get_experiment(aUser, 'an_experiment_name', ExperimentEvaluationOptions(disable_exposure_logging=True))
    ```

    ```python  theme={null}
    statsig.manually_log_experiment_exposure(aUser, 'an_experiment_name')
    ```
  </Tab>

  <Tab title="Layers">
    ```python  theme={null}
    layer = statsig.get_layer(aUser, 'a_layer_name',  LayerEvaluationOptions(disable_exposure_logging=True))
    paramValue = layer.get('a_param_name', 'fallback_value')
    ```

    ```python  theme={null}
    statsig.manually_log_layer_parameter_exposure(aUser, 'a_layer_name', 'a_param_name')
    ```
  </Tab>
</Tabs>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```python expandable theme={null}
from statsig_python_core import StatsigUser

user = StatsigUser(
    user_id="a-user-id",
    email="user@example.com",
    ip="192.168.1.1",
    user_agent="Mozilla/5.0...",
    country="US",
    locale="en_US",
    app_version="1.0.0",
    custom={
        # Custom fields
        "plan": "premium",
        "age": 25
    },
    custom_ids={
        # Custom ID types
        "stable_id": "stable-id-123"
    },
    private_attributes={
        # Private attributes not forwarded to integrations
        "email": "private@example.com"
    }
)
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  <ResponseField name="specs_url" type="Optional[str]">
    Custom URL for fetching feature specifications.
  </ResponseField>

  <ResponseField name="specs_sync_interval_ms" type="Optional[int]">
    How often the SDK updates specifications from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="init_timeout_ms" type="Optional[int]">
    Sets the maximum timeout for initialization requests (in milliseconds).
  </ResponseField>

  <ResponseField name="log_event_url" type="Optional[str]">
    Custom URL for logging events.
  </ResponseField>

  <ResponseField name="disable_all_logging" type="Optional[bool]">
    When `true`, disables all event logging.
  </ResponseField>

  <ResponseField name="disable_network" type="Optional[bool]">
    When `true`, disables all network functions: event & exposure logging, spec downloads, and ID List downloads. Formerly called "localMode".
  </ResponseField>

  <ResponseField name="event_logging_flush_interval_ms" type="Optional[int]">
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

  <ResponseField name="enable_id_lists" type="Optional[bool]">
    Enable/disable ID list functionality. **Required to be `true` when using segments with more than 1000 IDs.** See [ID List segments](/segments/add-id-list) for more details.
  </ResponseField>

  <ResponseField name="disable_user_agent_parsing" type="Optional[bool]" default="false">
    If set to true, the SDK will NOT attempt to parse UserAgents (attached to the user object) into browserName, browserVersion, systemName, systemVersion, and appVersion at evaluation time, when needed for evaluation.
  </ResponseField>

  <ResponseField name="wait_for_user_agent_init" type="Optional[bool]" default="false">
    When set to true, the SDK will wait until user agent parsing data is fully loaded during initialization. This may slow down by \~1 second startup but ensures that parsing of the user's userAgent string into fields like browserName, browserVersion, systemName, systemVersion, and appVersion is ready before any evaluations.
  </ResponseField>

  <ResponseField name="disable_country_lookup" type="Optional[bool]" default="false">
    If set to true, the SDK will NOT attempt to parse IP addresses (attached to the user object at user.ip) into Country codes at evaluation time, when needed for evaluation.
  </ResponseField>

  <ResponseField name="wait_for_country_lookup_init" type="Optional[bool]" default="false">
    When set to true, the SDK will wait for country lookup data (e.g., GeoIP or YAML files) to fully load during initialization. This may slow down by \~1 second startup but ensures that IP-to-country parsing is ready at evaluation time.
  </ResponseField>

  <ResponseField name="id_lists_url" type="Optional[str]">
    Custom URL for fetching ID lists.
  </ResponseField>

  <ResponseField name="id_lists_sync_interval_ms" type="Optional[int]">
    How often the SDK updates ID lists from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="fallback_to_statsig_api" type="Optional[bool]">
    Whether to fallback to the Statsig API if custom endpoints fail.
  </ResponseField>

  <ResponseField name="environment" type="Optional[str]">
    Environment parameter for evaluation.
  </ResponseField>

  <ResponseField name="output_log_level" type="Optional[str]">
    Controls the verbosity of SDK logs.
  </ResponseField>

  <ResponseField name="persistent_storage" type="Optional[PersistentStorage]">
    Adapter / Interface to use persistent assignment within SDK. See [Persistent Assignment](/server/concepts/persistent_assignment/) for more details.
  </ResponseField>

  <ResponseField name="observability_client" type="Optional[ObservabilityClient]">
    Adapter to listen monitor the health of SDK. See [SDK Monitoring](https://docs.statsig.com/sdk_monitoring/) for more details.
  </ResponseField>

  <ResponseField name="data_store" type="Optional[DataStore]">
    Custom data store implementation for storing and retrieving configuration data. Used for advanced caching or storage strategies.
  </ResponseField>

  <ResponseField name="event_logging_max_pending_batch_queue_size" type="Optional[int]">
    Maximum number of batches of events to hold in buffer to retry.
  </ResponseField>

  <ResponseField name="global_custom_fields" type="Optional[Dict]">
    Custom fields to include in all events logged by the SDK.
  </ResponseField>

  <ResponseField name="config_compression_mode" type="Optional[str]" default="gzip">
    Compression method for exposure logging. Options: "gzip", "dictionary"
  </ResponseField>

  <ResponseField name="proxy_config" type="Optional[ProxyConfig]">
    Configuration for connecting through a proxy server. The `ProxyConfig` object has the following properties:

    * `proxy_host`: Optional string specifying the proxy server host
    * `proxy_port`: Optional number specifying the proxy server port
    * `proxy_auth`: Optional string for proxy authentication (format: "username:password")
    * `proxy_protocol`: Optional string specifying the protocol (e.g., "http", "https")
  </ResponseField>

  <ResponseField name="spec_adapter_configs" type="Optional[List[SpecAdapterConfig]]">
    Advanced configuration for customizing how the SDK fetches feature specifications. Allows you to configure multiple spec adapters with different priorities and settings.

    Each `SpecAdapterConfig` object has the following properties:

    * `adapter_type`: String specifying the adapter type (e.g., "http", "grpc")
    * `specs_url`: Optional custom URL for fetching specifications
    * `init_timeout_ms`: Optional timeout for initialization (in milliseconds)

    <Note>
      **Migration Note:** This parameter was previously named `init_resources` in earlier versions. If you're upgrading from an older version, replace `init_resources` with `spec_adapter_configs`.
    </Note>
  </ResponseField>

  ***

  ### Example Usage

  ```python  theme={null}
  from statsig_python_core import StatsigOptions, SpecAdapterConfig

  # Define proxy configuration if needed
  proxy_config = {
      "proxy_host": "proxy.example.com",
      "proxy_port": 8080,
      # "proxy_auth": "username:password",  # Uncomment if authentication is needed
      "proxy_protocol": "http"
  }

  # Initialize StatsigOptions with custom parameters
  options = StatsigOptions()
  options.environment = "development"
  options.init_timeout_ms = 3000
  options.disable_all_logging = False
  options.proxy_config = proxy_config

  # Pass the options object into statsig.initialize()
  statsig = Statsig("secret-key", options)
  statsig.initialize().wait()
  ```

  ### Using spec\_adapter\_configs with Multiple Sources

  ```python  theme={null}
  from statsig_python_core import StatsigOptions, SpecAdapterConfig

  # Configure multiple spec adapters with priority order
  # First source: Statsig CDN
  primary_adapter = SpecAdapterConfig(
      adapter_type="http",
      specs_url="https://api.statsigcdn.com/v2/download_config_specs",
      init_timeout_ms=3000
  )

  # Second source: Data Store adapter
  # The SDK will try this source if the primary source fails
  data_store_adapter = SpecAdapterConfig(
      adapter_type="data_store",
      init_timeout_ms=5000
  )

  options = StatsigOptions()
  options.spec_adapter_configs = [primary_adapter, data_store_adapter]
  options.environment = "production"

  statsig = Statsig("secret-key", options)
  statsig.initialize().wait()
  ```
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```python  theme={null}
statsig.shutdown().wait()
```

## Local Overrides

Local Overrides are a way to override the values of gates, configs, experiments, and layers for testing purposes. This is useful for local development or testing scenarios where you want to force a specific value without having to change the configuration in the Statsig console.

```python  theme={null}
# Overrides the given gate to the specified value
statsig.override_gate("a_gate_name", True)
	
# Overrides the given dynamic config to the provided value
statsig.override_dynamic_config("a_config_name", {"key": "value"})

# Overrides the given experiment to the provided value
statsig.override_experiment("an_experiment_name", {"key": "value"})
	
# Overrides the given layer to the provided value
statsig.override_layer("a_layer_name", {"key": "value"})

# Overrides the given experiment to a particular groupname, available for experiments only:
statsig.override_experiment_by_group_name("an_experiment_name", "a_group_name")
```

## Client SDK Bootstrapping | SSR

If you are using the Statsig client SDK in a browser or mobile app, you can bootstrap the client SDK with the values from the server SDK to avoid a network request on the client. This is useful for server-side rendering (SSR) or when you want to reduce the number of network requests on the client.

## Client Initialize Response

The Python Core SDK provides a method to generate a client initialize response that can be used to bootstrap client SDKs without requiring network requests.

```python  theme={null}
import json
from statsig_python_core import Statsig, StatsigUser

# Get client initialize response for a user
response_data = statsig.get_client_initialize_response(user)
response = json.loads(response_data)

# Pass response to a client SDK to initialize without a network request
```

<AccordionGroup>
  <Accordion title="Initialize Response Parameters">
    The `get_client_initialize_response` method accepts the following parameters:

    ```python  theme={null}
    def get_client_initialize_response(
        user: StatsigUser,
        hash: Optional[str] = None,
        client_sdk_key: Optional[str] = None,
        include_local_overrides: Optional[bool] = None
    ) -> str:
    ```

    * **`user`**: `StatsigUser` - The user to generate the initialize response for
    * **`hash`**: `Optional[str]` - Algorithm used for hashing gate/experiment names (default: 'djb2')
    * **`client_sdk_key`**: `Optional[str]` - Client SDK key to use for initialization
    * **`include_local_overrides`**: `Optional[bool]` - Whether to include local overrides in the response
  </Accordion>

  <Accordion title="Hash Algorithm">
    The `hash` parameter specifies which algorithm to use for hashing gate and experiment names in the client initialize response. The default is `'djb2'` for better performance and smaller payload size.

    Available options:

    * `'djb2'` (default) - DJB2 hashing algorithm for better performance
    * `'sha256'` - SHA-256 hashing algorithm
    * `'none'` - No hashing applied

    ```python  theme={null}
    # Use djb2 hashing algorithm (default)
    response_data = statsig.get_client_initialize_response(user, hash='djb2')

    # Use SHA-256 hashing algorithm
    response_data = statsig.get_client_initialize_response(user, hash='sha256')

    # Disable hashing
    response_data = statsig.get_client_initialize_response(user, hash='none')
    ```
  </Accordion>

  <Accordion title="Client SDK Key">
    The `client_sdk_key` parameter lets you filter the response to only the specific feature gates, experiments, dynamic configs, layers, or parameter stores that a particular client key has access to - effectively letting you apply [target apps](/sdk-keys/target-apps/).

    ```python  theme={null}
    # Specify a client SDK key
    response_data = statsig.get_client_initialize_response(
        user, 
        client_sdk_key='client-key'
    )
    ```
  </Accordion>

  <Accordion title="Local Overrides">
    The `include_local_overrides` parameter determines whether to consider [local overrides](#local-overrides) you've set when evaluating each config in the response.

    ```python  theme={null}
    # Include local overrides in the response
    response_data = statsig.get_client_initialize_response(
        user, 
        include_local_overrides=True
    )
    ```
  </Accordion>

  <Accordion title="Full Code Example">
    Below is a complete example of using the client initialize response to bootstrap a client SDK. Note that you may choose to parallelize or inline the initialize response data with other requests to your server, to eliminate additional requests and latency.

    ```python  theme={null}
    # Server-side code
    import json
    from statsig_python_core import Statsig, StatsigUser, StatsigOptions
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    # Initialize the server SDK
    options = StatsigOptions()
    statsig = Statsig('server-secret-key', options)
    statsig.initialize().wait()

    # In your API endpoint handler
    @app.route('/statsig-bootstrap')
    def statsig_bootstrap():
        # Create a user object from the request
        user = StatsigUser(
            user_id=request.args.get('userID', ''),
            email=request.args.get('email'),
            ip=request.remote_addr,
            user_agent=request.headers.get('User-Agent')
        )
        
        # Generate the client initialize response
        response_data = statsig.get_client_initialize_response(
            user,
            hash='djb2',
            client_sdk_key='client-sdk-key'
        )
        
        # Parse the JSON response
        statsig_values = json.loads(response_data)
        
        # Return the values to the client
        return jsonify({'statsigValues': statsig_values})
    ```

    ```javascript  theme={null}
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

  <Accordion title="Response Format">
    The method returns a JSON string containing the client initialize response. You'll need to parse this string to access the data:

    ```python  theme={null}
    response_data = statsig.get_client_initialize_response(user)
    response = json.loads(response_data)

    # Access different parts of the response
    feature_gates = response.get('feature_gates', {})
    dynamic_configs = response.get('dynamic_configs', {})
    layer_configs = response.get('layer_configs', {})
    ```

    The response includes:

    * `feature_gates`: Feature gate evaluations for the user
    * `dynamic_configs`: Dynamic config and experiment evaluations
    * `layer_configs`: Layer evaluations
    * `has_updates`: Boolean indicating if there are updates
    * `time`: Timestamp of the response
  </Accordion>
</AccordionGroup>

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

```python  theme={null}
class PersistentStorage(PersistentStorageBaseClass):
    def __init__():
        # When you initialize, remember to call super.__init__()
        super().__init__()
        self.load_fn = self.load
        self.save_fn = self.save
        self.delete_fn = self.delete

    def load(self, key: str) -> Optional[UserPersistedValues]:
        """
        Load persisted values for a user from storage

        Args:
            key: A string key that uniquely identifies a user

        Returns:
            Dictionary mapping config names to their persisted values
        """
        pass

    def save(self, key: str, config_name: str, data: StickyValues):
        """
        Save a persistent value for a user

        Args:
            key: A string key that uniquely identifies a user
            config_name: The name of the config/experiment
            data: The values to persist
        """
        pass

    def delete(self, key: str, config_name: str):
        """
        Delete a persistent value for a user

        Args:
            key: A string key that uniquely identifies a user
            config_name: The name of the config/experiment to delete
        """
        pass
```

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

```python  theme={null}
class DataStore(DataStoreBase):
    def initialize(self):
        """
        Initialize the data store. Called when the Statsig client initializes.
        """
        pass

    def shutdown(self):
        """
        Clean up resources when the Statsig client shuts down.
        """
        pass

    def get(self, key: str) -> Optional[DataStoreResponse]:
        """
        Retrieve value from the data store.
        
        Args:
            key: The key to retrieve the value for
            
        Returns:
            DataStoreResponse containing the result and time
        """
        pass

    def set(self, key: str, value: str, time: Optional[int] = None):
        """
        Store a value in the data store.
        
        Args:
            key: The key to store the value under
            value: The value to store
            time: Optional timestamp
        """
        pass

    def support_polling_updates_for(self, key: str) -> bool:
        """
        Whether the data store supports polling for updates for the given key.
        
        Args:
            key: The key to check
            
        Returns:
            True if polling is supported, False otherwise
        """
        return False
```

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

## Output Logger

The Output Logger Provider interface allows you to customize how the SDK logs internal messages.

```python  theme={null}
class OutputLoggerProvider(OutputLoggerProviderBase):
    def init(self):
        """
        Initialize the logger. Called when the Statsig client initializes.
        """
        pass

    def debug(self, tag: str, msg: str):
        """
        Log a debug message.
        
        Args:
            tag: Category/component tag for the message
            msg: The message to log
        """
        pass

    def info(self, tag: str, msg: str):
        """
        Log an info message.
        
        Args:
            tag: Category/component tag for the message
            msg: The message to log
        """
        pass

    def warn(self, tag: str, msg: str):
        """
        Log a warning message.
        
        Args:
            tag: Category/component tag for the message
            msg: The message to log
        """
        pass

    def error(self, tag: str, msg: str):
        """
        Log an error message.
        
        Args:
            tag: Category/component tag for the message
            msg: The message to log
        """
        pass

    def shutdown(self):
        """
        Clean up resources when the Statsig client shuts down.
        """
        pass
```

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

```python  theme={null}
class ObservabilityClient(ObservabilityClientBase):
    def init(self):
        """
        Initialize the observability client. Called when the Statsig client initializes.
        """
        pass

    def increment(self, metric_name: str, value: float, tags: Optional[Dict[str, str]] = None):
        """
        Report a counter metric.
        
        Args:
            metric_name: The name of the metric
            value: The amount to increment by
            tags: Optional tags to associate with the metric
        """
        pass

    def gauge(self, metric_name: str, value: float, tags: Optional[Dict[str, str]] = None):
        """
        Report a gauge metric.
        
        Args:
            metric_name: The name of the metric
            value: The current value
            tags: Optional tags to associate with the metric
        """
        pass

    def dist(self, metric_name: str, value: float, tags: Optional[Dict[str, str]] = None):
        """
        Report a distribution metric.
        
        Args:
            metric_name: The name of the metric
            value: The value to record
            tags: Optional tags to associate with the metric
        """
        pass

    def error(self, tag: str, error: str):
        """
        Report an error.
        
        Args:
            tag: Category/component tag for the error
            error: The error message
        """
        pass

    def should_enable_high_cardinality_for_this_tag(self, tag: str) -> bool:
        """
        Determine if high cardinality should be enabled for a tag.
        
        Args:
            tag: The tag to check
            
        Returns:
            True if high cardinality should be enabled, False otherwise
        """
        pass
```

## FAQ

<AccordionGroup>
  <Accordion title="How do I run experiments for logged out users?">
    See the guide on [device level experiments](/guides/first-device-level-experiment).
  </Accordion>
</AccordionGroup>

## Reference

### API Methods

* `check_gate(user: StatsigUser, gate_name: str, options: Optional[FeatureGateEvaluationOptions] = None) -> bool`
* `get_dynamic_config(user: StatsigUser, config_name: str, options: Optional[DynamicConfigEvaluationOptions] = None) -> DynamicConfig`
* `get_experiment(user: StatsigUser, experiment_name: str, options: Optional[ExperimentEvaluationOptions] = None) -> DynamicConfig`
* `get_layer(user: StatsigUser, layer_name: str, options: Optional[LayerEvaluationOptions] = None) -> Layer`
* `get_feature_gate(user: StatsigUser, gate_name: str, options: Optional[FeatureGateEvaluationOptions] = None) -> FeatureGate`
* `get_parameter_store(user: StatsigUser, parameter_store_name: str, options: Optional[ParameterStoreEvaluationOptions] = None) -> ParameterStore`
* `log_event(user: StatsigUser, event_name: str, value: Optional[Union[str, float]] = None, metadata: Optional[Dict[str, str]] = None) -> None`
* `manually_log_gate_exposure(user: StatsigUser, gate_name: str) -> None`
* `manually_log_dynamic_config_exposure(user: StatsigUser, config_name: str) -> None`
* `manually_log_experiment_exposure(user: StatsigUser, experiment_name: str) -> None`
* `manually_log_layer_parameter_exposure(user: StatsigUser, layer_name: str, parameter_name: str) -> None`
* `get_client_initialize_response(user: StatsigUser, options: Optional[ClientInitializeResponseOptions] = None) -> ClientInitializeResponse`
* `shutdown() -> AsyncResult[None]`

### Fields Needed Methods

The following methods return information about which user fields are needed for evaluation:

* `get_gate_fields_needed(gate_name: str) -> List[str]`
* `get_dynamic_config_fields_needed(config_name: str) -> List[str]`
* `get_experiment_fields_needed(experiment_name: str) -> List[str]`
* `get_layer_fields_needed(layer_name: str) -> List[str]`

These methods return a list of strings representing the user fields that are required to properly evaluate the specified gate, config, experiment, or layer.


Built with [Mintlify](https://mintlify.com).