# Source: https://docs.statsig.com/server/pythonSDK.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Legacy Python Server SDK

> Statsig's Legacy Server SDK for Python applications

[Github Repository](https://github.com/statsig-io/python-sdk)

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    Install the sdk using [pip3](https://pypi.org/project/statsig/):

    <Note>
      The Statsig SDK is not compatible with python 2. You must be on python 3.7+ to use the Statsig SDK.
    </Note>

    ```bash  theme={null}
    pip3 install statsig
    ```
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a [StatsigOptions](#statsig-options) to customize the SDK.

    ```python  theme={null}
    from statsig import statsig

    statsig.initialize("server-secret-key")

    # or with StatsigOptions
    options = StatsigOptions(tier=StatsigEnvironmentTier.development)
    statsig.initialize("server-secret-key", options)

    # check if sdk is initialized
    initialized = statsig.is_initialized()
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```python  theme={null}
from statsig.statsig_user import StatsigUser

...

statsig.check_gate(StatsigUser("user-id"), "gate-name")
```

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

```python  theme={null}
config = statsig.get_config(StatsigUser("user-id"), "config-name")

config_json = config.get_value()
```

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```python  theme={null}
# Values via getLayer

layer = statsig.get_layer(user, "user_promo_experiments")
title = layer.get("title", "Welcome to Statsig!")
discount = layer.get("discount", 0.1)

# or, via getExperiment

title_exp = statsig.get_experiment(user, "new_user_promo_title")
price_exp = statsig.get_experiment(user, "new_user_promo_price")

title = title_exp.get("title", "Welcome to Statsig!")
discount = price_exp.get("discount", 0.1)

...

price = msrp * (1 - discount)
```

## Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```python  theme={null}
gate = statsig.get_feature_gate(StatsigUser("user-id"), "gate-name")
print(gate.name)  # 'gate-name'
print(gate.value)  # True or False
print(gate.rule_id)  # rule ID that was evaluated
print(gate.evaluation_details)  # evaluation metadata
```

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```python  theme={null}
from statsig.statsig_user import StatsigUser
from statsig.statsig_event import StatsigEvent

statsig.log_event(StatsigEvent(StatsigUser("user-id"), "event-name"))
```

Python supports `retry_queue_size`, which allows you to adjust the memory allocated for handling retries.
While service outages are rare, increasing the retry\_queue\_size can help minimize event loss by providing additional memory to buffer events during such occurrences.
This option is generally not needed for typical use but offers added flexibility in exceptional situations.

## Statsig User

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to create targeting based on them.

Note that while typing is lenient on the `StatsigUser` object to allow you to pass in numbers, strings, arrays, objects, and potentially even enums or classes, the evaluation operators will only be able to operate on primitive types - mostly strings and numbers. While we attempt to smartly cast custom field types to match the operator, we cannot guarantee evaluation results for other types. For example, setting an array as a custom field will only ever be compared as a string - there is no operator to match a value in that array.

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Statsig Options

`initialize()` takes an optional parameter `options` in addition to the secret key that you can provide to customize the Statsig client. Here are the current options and we are always adding more to the list:

Create a `StatsigOptions` class to pass in with the following available parameters:

(unit of measure for time related options is seconds)

<ResponseField name="tier" type="StatsigEnvironmentTier | str" default="None">
  Sets the environment tier (for gates to evaluate differently in development and production)

  You can set an environment tier with the `StatsigEnvironmentTier` enum or just as a `str`
</ResponseField>

<ResponseField name="timeout" type="int" default="None">
  Enforces a minimum timeout on network requests from the SDK
</ResponseField>

<ResponseField name="init_timeout" type="int" default="None">
  Sets the maximum timeout on download config specs and id lists network requests for initialization
</ResponseField>

<ResponseField name="rulesets_sync_interval" type="int" default="10">
  How often the SDK updates rulesets from Statsig servers
</ResponseField>

<ResponseField name="idlists_sync_interval" type="int" default="60">
  How often the SDK updates idlists from Statsig servers
</ResponseField>

<ResponseField name="local_mode" type="bool" default="False">
  Disables all network requests. SDK returns default values and will not log events. Useful in combination with overrides to mock behavior for tests
</ResponseField>

<ResponseField name="bootstrap_values" type="str" default="null">
  a string that represents all rules for all feature gates, dynamic configs and experiments. It can be provided to bootstrap the Statsig server SDK at initialization in case your server runs into network issue or Statsig server is down temporarily.
</ResponseField>

<ResponseField name="rules_updated_callback" type="typing.Callable" default="None">
  a callback function that's called whenever we have an update for the rules; it's called with a logical timestamp and a JSON string (used as is for bootstrapValues mentioned above). Note that as of v0.6.0, this will be called from a background thread that the SDK uses to update config values.
</ResponseField>

<ResponseField name="event_queue_size" type="int" default="500">
  The number of events to batch before flushing the queue to the network. Default 500.

  Note that events are also batched every minute by a background thread
</ResponseField>

<ResponseField name="data_store" type="IDataStore" default="None">
  A data store with custom storage behavior for config specs. Can be used to bootstrap Statsig server (takes priority over `bootstrap_values`).
</ResponseField>

<ResponseField name="proxy_configs" type="Optional[Dict[NetworkEndpoint, ProxyConfig]]" default="None">
  Configuration network for each endpoint, for example, download\_config\_spec, get\_id\_lists
</ResponseField>

<ResponseField name="fallback_to_statsig_api" type="Optional[bool]" default="False">
  Fallback to Statsig CDN for download config specs and get id lists if the overridden api failed.
</ResponseField>

<ResponseField name="initialize_sources" type="Optional[List[DataSource]]" default="None">
  List of sources SDK tries to get download\_config\_specs from when initialize. The list is ordered, SDK tries to get source from first element, and stops when getting dcs successfully
</ResponseField>

<ResponseField name="config_sync_sources" type="Optional[List[DataSource]]" default="None">
  List of sources SDK tries to get download\_config\_specs from when downloading. The list is ordered, SDK tries to get source from first element, and stops when getting dcs successfully
</ResponseField>

Example:

```python  theme={null}
from statsig import statsig, StatsigEnvironmentTier, StatsigOptions

options = StatsigOptions(None, StatsigEnvironmentTier.development)
statsig.initialize("secret-key", options).wait()
```

You can also use the `set_environment_parameter` function, but that takes in string values only:

```python  theme={null}
from statsig import statsig, StatsigEnvironmentTier, StatsigOptions

options = StatsigOptions()
options.set_environment_parameter("tier", StatsigEnvironmentTier.development.value)
statsig.initialize("secret-key", options).wait()
```

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

```python  theme={null}
statsig.shutdown()
```

## Client SDK Bootstrapping

The Statsig server SDK can be used to generate the initialization values for a client SDK. This is useful for server-side rendering (SSR) or when you want to pre-fetch values for a client.

```python  theme={null}
values = statsig.get_client_initialize_response(user); # dict() | None

# To apply local overrides, set include_local_overrides = True (python sdk v0.32.0+)
values = statsig.get_client_initialize_response(user=user, include_local_overrides=True); # dict() | None
```

## Local Overrides

You can override the values returned by the SDK for testing purposes. This can be useful for local development when you want to test specific scenarios.

```python  theme={null}
# Adding/Removing gate overrides
statsig.override_gate("a_gate_name", true, "a_user_id")
statsig.remove_gate_override("a_gate_name", "a_user_id")

# Adding/Removing config overrides
statsig.override_config("a_config_name", {"key": "value"}, "a_user_id")
statsig.remove_config_override("a_config_name", "a_user_id")

# Adding/Removing experiment overrides
statsig.override_experiment("an_experiment_name", {"key": "value"}, "a_user_id")
statsig.remove_experiment_override("an_experiment_name", "a_user_id")

# Remove All Overrides
statsig.remove_all_overrides()

# You can also override with custom ids
custom_id_user = StatsigUser("a_user_id", custom_ids={"statsigId": "a_statsig_id"})
statsig.override_gate("a_gate_name", true, "a_statsig_id")

# Local overrides will prioritize override with userId, then look up the custom id to override. 
# To prevent clashing overrides, it is recommended to not use the same value for userId and customIds for different users. 
```

## Multi-Instance Usage

If you need to create multiple independent instances of the Statsig SDK (for example, to use different API keys or configurations), you can use the instance-based approach:

```python  theme={null}
sdk_instance = StatsigServer()
sdk_instance.initialize(secret_key, options);
```

## Forward Proxy Configuration

You can configure the SDK to use a forward proxy for network requests:

Basic setup to stream download config spec from forward proxy:

```python  theme={null}
  proxyAddress = "0.0.0.0:50051" // local address update to your address
  Statsig.initialize(secret_key, StatsigOptions(proxy_configs={
            NetworkEndpoint.DOWNLOAD_CONFIG_SPECS: ProxyConfig(NetworkProtocol.GRPC_WEBSOCKET, proxyAddress)}))
```

When the SDK is disconnected from forward proxy when use grpc\_websocket, the sdk will retry connection with exponential backoff, after `push_worker_failover_threshold` retries, the sdk will start polling from Statsig until reconnecting to the forward proxy.
You can customize Streaming Failover Behavior. You can also define the sources/endpoints SDK poll from, SDK will try from source at index 0, and stops trying if get a response.

```python  theme={null}

statsigOptions = StatsigOptions(
    proxy_configs={
        NetworkEndpoint.DOWNLOAD_CONFIG_SPECS: ProxyConfig(
            protocol=NetworkProtocol.GRPC_WEBSOCKET,
            proxy_address=address,
            push_worker_failover_threshold=1, # start polling from Statsig endpoint after 1 retry failed
            # 1st retry 5000 ms later, 2nd retry 2 * 5000ms = 10 seconds ....
            retry_backoff_multiplier=2, 
            max_retry_attempt=8,
            retry_backoff_base_ms=5000
        )
    },
    # Get from network first, which is forward proxy here, if fails, try datastore, if fails try poll from Statsig endpoint
    initialize_sources=[
        DataSource.NETWORK,
        DataSource.DATASTORE,
        DataSource.STATSIG_NETWORK,
    ],
)
```

## FAQs

### How can I mock Statsig for testing?

The python server SDK, starting in version 0.5.1+, supports a few features to make testing easier.

First, there is a `StatsigOption` parameter called `localMode`. Setting `localMode` to true will cause the SDK to never hit the network, and only return default values. This is perfect for dummy environments or test environments that should not access the network.

Next, there are the `overrideGate` and `overrideConfig` APIs on the global `statsig` interface, see [Local Overrides](#local-overrides)

These can be used to set a gate or config override for a specific user, or for all users (by not providing a specific user ID).

We suggest you enable `localMode` and then override gates/configs/experiments to specific values to test the various code flows you are building.

### Can I generate the initialize response for a client SDK using the Python server SDK?

Yes. See [Client Initialize Response](#bootstrap).

## Reference

### StatsigUser

```python  theme={null}
@dataclass
class StatsigUser:
    """An object of properties relating to the current user
    user_id or customID is required: https://docs.statsig.com/sdks/user#why-is-an-id-always-required-for-server-sdks
    Provide as many as possible to take advantage of advanced conditions in the statsig console
    A dictionary of additional fields can be provided under the custom field
    Set private_attributes for any user property you need for gate evaluation but prefer stripped from logs/metrics
    """
    user_id: Optional[str] = None
    email: Optional[str] = None
    ip: Optional[str] = None
    user_agent: Optional[str] = None
    country: Optional[str] = None
    locale: Optional[str] = None
    app_version: Optional[str] = None 
    custom: Optional[dict] = None # key: string, value: string
    private_attributes: Optional[dict] = None # key: string, value: string
    custom_ids: Optional[dict] = None # key: string, value: string
```

### StatsigOptions

```python  theme={null}
class StatsigOptions:
    """An object of properties for initializing the sdk with additional parameters"""

    def __init__(
        self,
        api: Optional[str] = None,
        api_for_download_config_specs: Optional[str] = None,
        api_for_get_id_lists: Optional[str] = None,
        api_for_log_event: Optional[str] = None,
        tier: Union[str, StatsigEnvironmentTier, None] = None,
        init_timeout: Optional[int] = None,
        timeout: Optional[int] = None,
        rulesets_sync_interval: int = DEFAULT_RULESET_SYNC_INTERVAL,
        idlists_sync_interval: int = DEFAULT_IDLIST_SYNC_INTERVAL,
        local_mode: bool = False,
        bootstrap_values: Optional[str] = None,
        rules_updated_callback: Optional[Callable] = None,
        event_queue_size: Optional[int] = DEFAULT_EVENT_QUEUE_SIZE,
        data_store: Optional[IDataStore] = None,
        idlists_thread_limit: int = DEFAULT_IDLISTS_THREAD_LIMIT,
        logging_interval: int = DEFAULT_LOGGING_INTERVAL, #deprecated
        disable_diagnostics: bool = False,
        custom_logger: Optional[OutputLogger] = None,
        enable_debug_logs = False,
        disable_all_logging = False,
        evaluation_callback: Optional[Callable[[Union[Layer, DynamicConfig, FeatureGate]], None]] = None,
        retry_queue_size: int = DEFAULT_RETRY_QUEUE_SIZE,
        proxy_configs: Optional[Dict[NetworkEndpoint, ProxyConfig]] = None,
        fallback_to_statsig_api: Optional[bool] = False,
        initialize_sources: Optional[List[DataSource]] = None,
        config_sync_sources: Optional[List[DataSource]] = None,
    ):
```

### FeatureGate

```python  theme={null}
class FeatureGate:

    def get_value(self):
        """Returns the underlying value of this FeatureGate"""

    def get_name(self):
        """Returns the name of this FeatureGate"""

    def get_evaluation_details(self):
        """Returns the evaluation detail of this FeatureGate"""
```

### DynamicConfig

```python  theme={null}
class DynamicConfig:
    def get(self, key, default=None):
        """Returns the value of the config at the given key
        or the provided default if the key is not found
        """

    def get_typed(self, key, default=None):
        """Returns the value of the config at the given key
        iff the type matches the type of the provided default.
        Otherwise, returns the default value
        """

    def get_value(self):
        """Returns the underlying value of this DynamicConfig"""

    def get_name(self):
        """Returns the name of this DynamicConfig"""

    def get_evaluation_details(self):
        """Returns the evaluation detail of this DynamicConfig"""
```

### Layer

```python  theme={null}
class Layer:
    def get(self, key, default=None):
        """Returns the value of the layer at the given key
        or the provided default if the key is not found
        """

    def get_typed(self, key, default=None):
        """Returns the value of the layer at the given key
        iff the type matches the type of the provided default.
        Otherwise, returns the default value
        """

    def get_name(self):
        """Returns the name of this Layer"""

    def get_values(self):
        """Returns all the values in this Layer but does not trigger an exposure log"""

    def get_evaluation_details(self):
        """Returns the evaluation detail of this Layer"""
```

### EvaluationDetails

```python  theme={null}
class EvaluationDetails:
    reason: EvaluationReason
    config_sync_time: int
    init_time: int
    server_time: int

class EvaluationReason(str, Enum):
    network = "Network"
    local_override = "LocalOverride"
    unrecognized = "Unrecognized"
    uninitialized = "Uninitialized"
    bootstrap = "Bootstrap"
    data_adapter = "DataAdapter"
    unsupported = "Unsupported"
    error = "error"
```

### DataStore

```python  theme={null}
class IDataStore:
    def get(self, key: str) -> Optional[str]:
        return None

    def set(self, key: str, value: str):
        pass

    def shutdown(self):
        pass

    def should_be_used_for_querying_updates(self, key: str) -> bool:
        return False
```

### ForwardProxy - ProxyConfig

```python  theme={null}
class NetworkProtocol(Enum):
    HTTP = "http"
    GRPC = "grpc"
    GRPC_WEBSOCKET = "grpc_websocket"


class NetworkEndpoint(Enum):
    LOG_EVENT = "log_event"
    DOWNLOAD_CONFIG_SPECS = "download_config_specs"
    GET_ID_LISTS = "get_id_lists"
    ALL = "all"

class ProxyConfig:
    def __init__(
        self,
        protocol: NetworkProtocol,
        proxy_address: str,
        # Websocket worker failover config
        max_retry_attempt: Optional[int] = None, # default is 10
        retry_backoff_multiplier: Optional[int] = None, # default is # default is 5
        retry_backoff_base_ms: Optional[int] = None, # default is 10,000 ms
        # Push worker failback to polling threshold, fallback immediate set 0,
        # n means fallback after n retry failed
        push_worker_failover_threshold: Optional[int] = None, # default is 4, about 30 minutes
    ):
        self.proxy_address = proxy_address
        self.protocol = protocol
        self.max_retry_attempt = max_retry_attempt
        self.retry_backoff_multiplier = retry_backoff_multiplier
        self.retry_backoff_base_ms = retry_backoff_base_ms
        self.push_worker_failover_threshold = push_worker_failover_threshold
```


Built with [Mintlify](https://mintlify.com).