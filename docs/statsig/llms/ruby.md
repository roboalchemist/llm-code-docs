# Source: https://docs.statsig.com/server/ruby.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ruby Server SDK

> Statsig's Server SDK for Ruby applications

<Card title="GitHub Repository" icon="github" href="https://github.com/statsig-io/ruby-sdk">
  View the Ruby SDK source code and releases
</Card>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    If you are using Bundler, add the [gem](https://rubygems.org/gems/statsig) to your Gemfile from command line:

    ```shell  theme={null}
    bundle add statsig
    ```

    or directly include it in your Gemfile and run `bundle install`:

    ```shell  theme={null}
    gem "statsig", ">= X.Y.Z"
    ```

    Check out the latest versions on [https://rubygems.org/gems/statsig](https://rubygems.org/gems/statsig)
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    ```ruby  theme={null}
    require 'statsig'

    Statsig.initialize('server-secret-key')
    ```

    ```ruby  theme={null}
    # Or, if you want to initialize with certain options
    options = StatsigOptions.new({'tier' => 'staging'}, network_timeout: 5)

    # And a callback when the initialization network request fails
      def error_callback(e)
        puts e
      end


    ...
    Statsig.initialize('server-secret-key', options, method(:error_callback))
    ```

    ### Initializing Statsig in a Rails Application

    If your application is using Rails, you should initialize Statsig in `config/initializers/statsig.rb`:

    ```ruby  theme={null}
    Statsig.initialize('server-secret-key', options)
    ```

    ### Initializing Statsig when using Unicorn, Puma, Passenger, or Sidekiq

    For **Unicorn**, you should initialize Statsig within an `after_fork` hook in your `unicorn.rb` config file:

    ```ruby  theme={null}
    after_fork do |server,worker|
      Statsig.initialize('server-secret-key', options)
    end
    ```

    For **Puma**, you should initialize Statsig within an `on_worker_boot` hook in your `puma.rb` config file:

    ```ruby  theme={null}
    on_worker_boot do
      Statsig.initialize('server-secret-key', options)
    end
    ```

    For **Passenger**, you should initialize Statsig in your `config.ru` config file:

    ```ruby  theme={null}
    if defined?(PhusionPassenger)
      PhusionPassenger.on_event(:starting_worker_process) do |forked|
        Statsig.initialize('server-secret-key', options)
      end
    end
    ```

    For **Sidekiq**, you should initialize Statsig in your `sidekiq.rb`/server configuration file:

    ```ruby  theme={null}
    Sidekiq.configure_server do |config|
      config.on(:startup) do
        Statsig.initialize
      end

      config.on(:shutdown) do
        Statsig.shutdown
      end
    end
    ```

    If you are using Rails in combination with any of the above, you should be sure to initialize using the specific process lifecycle hooks exposed by the respective tool. You can initialize in multiple places, which should ensure the SDK is fully usable including all background processing.

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```ruby  theme={null}
user = StatsigUser.new({'userID' => 'some_user_id'})
if Statsig.check_gate(user, 'use_new_feature')
  # Gate is on, enable new feature
else
  # Gate is off
end
```

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

```ruby  theme={null}
config = Statsig.get_config(user, 'awesome_product_details')

# The 2nd parameter is the default value to be used in case the given parameter name does not exist on
# the Dynamic Config object. This can happen when there is a typo, or when the user is offline and the
# value has not been cached on the client.
item_name = config.get('product_name', 'Awesome Product v1');
price = config.get('price', 10.0);
shouldDiscount = config.get('discount', false);

# Or just get the whole json object backing this config if you prefer
json = config.value

```

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

```ruby  theme={null}
# Values via getLayer

layer = Statsig.get_layer(user, "user_promo_experiments")
title = layer.get("title", "Welcome to Statsig!")
discount = layer.get("discount", 0.1)

# or, via getExperiment

title_exp = Statsig.get_experiment(user, "new_user_promo_title")
price_exp = Statsig.get_experiment(user, "new_user_promo_price")

title = title_exp.get("title", "Welcome to Statsig!")
discount = price_exp.get("discount", 0.1)

...

price = msrp * (1 - discount)


```

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```ruby  theme={null}
Statsig.log_event(
  user,
  'add_to_cart',
  'SKU_12345',
  {
    'price' => '9.99',
    'item_name' => 'diet_coke_48_pack'
  }
)
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

You can specify optional parameters with `options` when initializing.

* **environment**: Hash, default `nil`
  * a Hash you can use to set environment variables that apply to all of your users in the same session and will be used for targeting purposes.
  * The most common usage is to set the "tier" (string), and have feature gates pass/fail for specific environments. The accepted values are "production", "staging" and "development", e.g. `StatsigOptions.New({ 'tier' => 'staging' })`.
* **download\_config\_specs\_url**: String, default `"https://api.statsigcdn.com/v2/download_config_specs/"`
  * The url used specifically to call download\_config\_specs
* **log\_event\_url**: String, default `"https://statsigapi.net/v1/log_event"`
  * The url used specifically to call log\_event
* **get\_id\_lists\_url**: String, default `"https://statsigapi.net/v1/get_id_lists"`
  * The url used specifically to call get\_id\_lists
* **rulesets\_sync\_interval**: Number, default `10`
  * The interval (in seconds) to poll for changes to your Statsig configuration
* **idlists\_sync\_interval**: Number, default `60`
  * The interval (in seconds) to poll for changes to id lists
* **disable\_rulesets\_sync**: Boolean, default `false`
  * Disable background syncing for rulesets
* **disable\_idlists\_sync**: Boolean, default `false`
  * Disable background syncing for id lists
* **logging\_interval\_seconds**: Number, default `60`
  * How often to flush logs to Statsig
* **logging\_max\_buffer\_size**: Number, default `1000`, can be set lower but anything over 1000 will be dropped on the server
  * The maximum number of events to batch before flushing logs to the server
* **local\_mode**: Boolean, default `false`
  * Restricts the SDK to not issue any network requests and only respond with default values (or local overrides)
* **bootstrap\_values**: String, default `nil`
  * A string that represents all rules for all feature gates, dynamic configs and experiments. It can be provided to bootstrap the Statsig server SDK at initialization in case your server runs into network issue or Statsig server is down temporarily.
* **rules\_updated\_callback**: function, default `nil`
  * A callback function that will be called anytime the rulesets are updated
* **data\_store**: IDataStore, default `nil`
  * A class that extends IDataStore. Can be used to provide values from a common data store (like Redis) to initialize the Statsig SDK.
* **idlist\_threadpool\_size**: Number, default `3`
  * The number of threads allocated to syncing IDLists
* **logger\_threadpool\_size**: Number, default `3`
  * The number of threads allocated to posting event logs
* **disable\_diagnostics\_logging**: Boolean, default `false`
  * Should diagnostics be logged. These include performance metrics for initialize
* **disable\_sorbet\_logging\_handlers**: Boolean, default `false`
  * Statsig utilizes Sorbet ([https://sorbet.org](https://sorbet.org)) to ensure type safety of the SDK. This includes logging to console when errors are detected. You can disable this logging by setting this flag to true.
* **network\_timeout**: Number, default `nil`
  * Maximum number of seconds to wait for a network call before timing out
* **post\_logs\_retry\_limit**: Number, default `3`
  * Number of times to retry sending a batch of failed log events
* **post\_logs\_retry\_backoff**: Number/Function, default `nil`
  * The number of seconds, or a function that returns the number of seconds based on the number of retries remaining which overrides the default backoff time between retries
* **user\_persistent\_storage**: IUserPersistentStorage, default `nil`
  * A storage adapter for persisted values. Can be used for sticky bucketing users in experiments. Implements Statsig::Interfaces::IUserPersistentStorage.

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

```ruby  theme={null}
Statsig.shutdown
```

## Client SDK Bootstrapping

The Statsig server SDK can be used to generate the initialization values for a client SDK. This is useful for server-side rendering (SSR) or when you want to pre-fetch values for a client.

```ruby  theme={null}
values = Statsig.get_client_initialize_response(user); # Hash[String, Any] | Nil
```

## Local Overrides

You can override the values returned by the SDK for testing purposes. This can be useful for local development when you want to test specific scenarios.

```ruby  theme={null}
# Adding gate overrides
Statsig.override_gate("a_gate_name", true)

# Adding config overrides
Statsig.override_config("a_config_name", {"key" => "value"})
```

<Note>
  1. These only apply locally - they do not update definitions in the Statsig console or elsewhere.
  2. The local override API is not designed to be a full mock. They are only a convenient way to override the value of the gate/config/etc.
</Note>

## Manual Exposures

Statsig SDKs automatically log an exposure event every time a gate/experiment/config is checked. In some scenarios, you may want to control when to log an exposure.

**Gates**

```ruby  theme={null}
result = Statsig.check_gate(user, 'a_gate_name', CheckGateOptions.new(disable_log_exposure: true))
```

```ruby  theme={null}
Statsig.manually_log_gate_exposure(user, 'a_gate_name')
```

**Configs**

```ruby  theme={null}
config = Statsig.get_config(user, 'a_dynamic_config_name', GetConfigOptions.new(disable_log_exposure: true))
```

```ruby  theme={null}
Statsig.manually_log_config_exposure(user, 'a_dynamic_config_name')
```

**Experiments**

```ruby  theme={null}
experiment = Statsig.get_experiment(user, 'an_experiment_name', GetExperimentOptions.new(disable_log_exposure: true))
```

```ruby  theme={null}
Statsig.manually_log_experiment_exposure(user, 'an_experiment_name')
```

**Layers**

```ruby  theme={null}
layer = Statsig.get_layer(user, 'a_layer_name', GetLayerOptions.new(disable_log_exposure: true))
paramValue = layer.get('a_param_name', 'fallback_value')
```

```ruby  theme={null}
Statsig.manually_log_layer_parameter_exposure(user, 'a_layer_name', 'a_param_name')
```

## User Persistent Storage

User Persistent Storage is a storage adapter for running sticky experiments. It allows you to persist user assignments across sessions.

### Interface

### Interface

```ruby  theme={null}
class IUserPersistentStorage
	def load(key)
		nil
	end

	def save(key, data) end
end
```

### Example Implementation

```ruby  theme={null}
class DummyPersistentStorageAdapter < Statsig::Interfaces::IUserPersistentStorage
  attr_accessor :store

  def initialize
    @store = {}
  end

  def load(key)
    return nil unless @store&.key?(key)

    @store[key]
  end

  def save(key, data)
    @store[key] = data
  end
end
```

## Multi-Instance Usage

If you need to create multiple independent instances of the Statsig SDK (for example, to use different API keys or configurations), you can use the instance-based approach:

```ruby  theme={null}
sdk_instance = StatsigDriver.new(secret_key, options, error_callback)
```

## FAQ

#### How do I run experiments for logged out users?

See the guide on [device level experiments](/guides/first-device-level-experiment)

#### How can I mock or override the SDK for testing?

Starting in `v1.12.0+`, the Ruby SDK supports `localMode` and `overrides`, see [Local Overrides](#local-overrides)

* `localMode` is a boolean parameter in `StatsigOptions` when initializing the SDK. It restricts all network traffic,
  so the SDK operates offline and only returns default or override values.

#### Can I generate the initialize response for a client SDK using the Ruby server SDK?

Yes. See [Client SDK Bootstrapping](#client-sdk-bootstrapping).

## Reference

### Type StatsigUser

```ruby  theme={null}
export type StatsigUser = {
class StatsigUser
  attr_accessor :user_id
  attr_accessor :email
  attr_accessor :ip
  attr_accessor :user_agent
  attr_accessor :country
  attr_accessor :locale
  attr_accessor :app_version
  attr_accessor :statsig_environment
  attr_accessor :custom_ids # Hash of key:string value:string
  attr_accessor :private_attributes # Hash of key:string value:string
  
  @custom # Hash of key:string value:string
  
  def initialize(user_hash)
    @statsig_environment = Hash.new
    if user_hash.is_a?(Hash)
      @user_id = user_hash['userID'] || user_hash['user_id']
      @user_id = @user_id.to_s unless @user_id.nil?
      @email = user_hash['email']
      @ip = user_hash['ip']
      @user_agent = user_hash['userAgent'] || user_hash['user_agent']
      @country = user_hash['country']
      @locale = user_hash['locale']
      @app_version = user_hash['appVersion'] || user_hash['app_version']
      @custom = user_hash['custom'] if user_hash['custom'].is_a? Hash
      @statsig_environment = user_hash['statsigEnvironment']
      @private_attributes = user_hash['privateAttributes'] if user_hash['privateAttributes'].is_a? Hash
      custom_ids = user_hash['customIDs'] || user_hash['custom_ids']
      @custom_ids = custom_ids if custom_ids.is_a? Hash
    end
  end
end
```

### Type StatsigOptions

```ruby  theme={null}
class StatsigOptions
  attr_accessor :environment
  attr_accessor :download_config_specs_url
  attr_accessor :log_event_url
  attr_accessor :get_id_lists_url
  attr_accessor :rulesets_sync_interval
  attr_accessor :idlists_sync_interval
  attr_accessor :disable_rulesets_sync
  attr_accessor :disable_idlists_sync
  attr_accessor :logging_interval_seconds
  attr_accessor :logging_max_buffer_size
  attr_accessor :local_mode
  attr_accessor :bootstrap_values
  attr_accessor :rules_updated_callback
  attr_accessor :data_store
  attr_accessor :idlist_threadpool_size
  attr_accessor :logger_threadpool_size
  attr_accessor :disable_diagnostics_logging
  attr_accessor :disable_sorbet_logging_handlers
  attr_accessor :network_timeout
  attr_accessor :post_logs_retry_limit
  attr_accessor :post_logs_retry_backoff
  attr_accessor :user_persistent_storage

  def initialize(
    environment = nil,
    download_config_specs_url: nil,
    log_event_url: nil,
    get_id_lists_url: nil,
    rulesets_sync_interval: 10,
    idlists_sync_interval: 60,
    disable_rulesets_sync: false,
    disable_idlists_sync: false,
    logging_interval_seconds: 60,
    logging_max_buffer_size: 1000,
    local_mode: false,
    bootstrap_values: nil,
    rules_updated_callback: nil,
    data_store: nil,
    idlist_threadpool_size: 3,
    logger_threadpool_size: 3,
    disable_diagnostics_logging: false,
    disable_sorbet_logging_handlers: false,
    network_timeout: nil,
    post_logs_retry_limit: 3,
    post_logs_retry_backoff: nil,
    user_persistent_storage: nil
  )
  end
end
```

### DataStore

```ruby  theme={null}
module Statsig
  module Interfaces
    class IDataStore
      def init
      end

      def get(key)
        nil
      end

      def set(key, value)
      end

      def shutdown
      end
    end
  end
end
```


Built with [Mintlify](https://mintlify.com).