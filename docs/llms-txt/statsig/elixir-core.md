# Source: https://docs.statsig.com/server-core/elixir-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Elixir Server SDK

> Statsig's Next-gen Elixir Server SDK built in our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-elixir" target="_blank" rel="noreferrer">Elixir Core on Github</a>,
  <a href="https://hex.pm/packages/statsig" target="_blank" rel="noreferrer">Hex Package</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    To use the SDK, add the following to your `mix.exs`:

    ```elixir  theme={null}
    {:statsig_elixir, "~> 0.8.0"},
    ```

    SDK is written using `rustler_precompiled`, which will download precompiled binary by default. But there is also an option to build Rust code within your project by cloning [statsig-server-core](https://github.com/statsig-io/statsig-server-core)

    ```bash  theme={null}
    cd statsig-server-core/statsig-elixir/ 
    # set the environment variable 
    FORCE_STATSIG_NATIVE_BUILD="true" mix compile
    ```
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    Statsig.ex is using GenServer to manage the actual implementation of statsig instance (which is written in Rust). Which requires you add Statsig into your Supervision Tree.

    ```elixir  theme={null}
    # Initializing, with StatsigOptions
    sdk_key = "secret-key******" # your secret key
    statsig_options = %StatsigOptions{enable_id_lists: true}

    # Add to your supervision tree 
    statsig_spec = %{id: Statsig, start: {Statsig, :start_link, [sdk_key, statsig_options]}}
    children = [
        # Other Apps
        statsig_spec
    ]
    res = Supervisor.start_link(children, opts)

    # Or directly initialize the GenServer
    {:ok,_} = Statsig.start_link(sdk_key, statsig_options)
    Statsig.initialize()
    ```

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

```elixir  theme={null}
user = %StatsigUser{
    user_id: "test_user_123"
}

{:ok, check_gate} = Statsig.check_gate("test_public", user)
# check_gate will be a boolean
```

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

```elixir  theme={null}
# Get a dynamic config for a specific user
user = %StatsigUser{
    user_id: "test_user_123"
}
{:ok, config} = Statsig.get_dynamic_config("a_config", user)

# Access the values in the dynamic config:

param_value = DynamicConfig.get_param_value(config, "header_text")

# Disable exposure
options = %Statsig.DynamicConfigEvaluationOptions{
    disable_exposure_logging = true
}
{:ok, config} = Statsig.get_dynamic_config("a_config", user, options)

```

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

```elixir  theme={null}
# Values via get_layer
user = %StatsigUser{
    user_id: "test_user_123"
}

{:ok, layer} = Statsig.get_layer("user_promo_experiments", user)
{:ok, title_string_value} = Layer.get(layer, "title", "Welcome to Statsig!")
{:ok, discount_float_value} = Layer.get(layer, "discount", 0.1)

# Via get_experiment
{:ok, experiment} = Statsig.get_experiment("user_promo_experiment", user)
title_exp = Experiment.get_param_value(experiment, "new_user_promo_title")

# Disable exposure
options = %Statsig.ExperimentEvaluationOptions{
    disable_exposure_logging = true
}
{:ok, experiment} = Statsig.get_experiment("user_promo_experiment", user, options)
```

<Note>
  If you are using layer to get value -- get param value. It will return primitive types: boolean, string, and numbers, for more complex type, SDK will return json serialized values.
</Note>

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

```elixir  theme={null}
{:ok, feature_gate} = Statsig.get_feature_gate(user, "example_gate")
# access the value, or the name off of the feature_gate object

options = %Statsig.FeatureGateEvaluationOptions{
    disable_exposure_logging = true
}
{:ok, feature_gate} = Statsig.get_feature_gate(user, "example_gate", options)

```

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

<Note>
  *Parameter stores are not yet available for this sdk. Need it now? Let us know in Slack.*
</Note>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

```elixir  theme={null}
Statsig.log_event(user, "test_event", 1, %{"metadata_1" => "value"})
```

### Sending Events to Log Explorer

You can forward logs to Logs Explorer for convenient analysis using the Forward Log Line Event API. This lets you include custom metadata and event values with each log.

<Note>
  Sending events to Log Explorer is not yet available for this sdk. Need it now? Let us know in Slack.
</Note>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

```elixir  theme={null}
user = %Statsig.User{
  user_id: "a-user-id",
  email: "user@example.com",
  ip: "192.168.1.1",
  user_agent: "Mozilla/5.0...",
  country: "US",
  locale: "en_US",
  app_version: "1.0.0",
  custom: %{
    # Custom fields
    "plan" => "premium",
    "age" => 25
  },
  custom_ids: %{
    # Custom ID types
    "stable_id" => "stable-id-123"
  },
  private_attributes: %{
    # Private attributes not forwarded to integrations
    "email" => "private@example.com"
  }
}
```

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  <ResponseField name="environment" type="string">
    The environment you're operating in (e.g., Production)
  </ResponseField>

  <ResponseField name="output_log_level" type="string">
    The type of logs you'd like exposed. (e.g., Debug)
  </ResponseField>

  <ResponseField name="init_timeout_ms" type="number">
    How long it should take for initialization to time out.
  </ResponseField>

  <ResponseField name="event_logging_flush_interval_ms" type="number">
    How often events should flush to the Statsig servers.
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

  <ResponseField name="log_event_url" type="string">
    The URL events should be logged to
  </ResponseField>

  <ResponseField name="specs_sync_interval_ms" type="number">
    How often specs should sync from the Statsig servers
  </ResponseField>

  <ResponseField name="specs_url" type="string">
    The URL Statsig should download specs from
  </ResponseField>

  <ResponseField name="enable_id_lists" type="boolean" default="false">
    Enable ID list download. **Required to be `true` when using segments with more than 1000 IDs.** See [ID List segments](/segments/add-id-list) for more details.
  </ResponseField>

  <ResponseField name="id_lists_url" type="string">
    The URL ID lists should be downloaded from
  </ResponseField>

  <ResponseField name="id_lists_sync_interval_ms" type="number">
    How often ID lists should be synced.
  </ResponseField>

  <ResponseField name="wait_for_country_lookup_init" type="boolean" default="false">
    Block initialization call until country lookup is initialized
  </ResponseField>

  <ResponseField name="wait_for_user_agent_init" type="boolean" default="false">
    Block initialization call until user\_agent is initialized
  </ResponseField>

  <ResponseField name="disable_all_logging" type="boolean" default="false">
    When `true`, disables all event logging.
  </ResponseField>

  <ResponseField name="disable_country_lookup" type="boolean" default="false">
    To improve memory usage, disable using country lookup.
  </ResponseField>

  <ResponseField name="disable_network" type="boolean" default="false">
    Turn off all network requests including get\_dcs and log\_events
  </ResponseField>

  <ResponseField name="disable_user_agent_parsing" type="boolean" default="false">
    To improve memory usage, disable using user agent parsing.
  </ResponseField>

  ***

  ```elixir  theme={null}
  # Initialize StatsigOptions with custom parameters
  statsig_options = %StatsigOptions{
    enable_id_lists: true
  }

  # Pass the options object into statsig.initialize()
  {:ok, _} = Statsig.start_link(sdk_key, statsig_options)
  Statsig.initialize()
  ```
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

```elixir  theme={null}
Statsig.shutdown()
```

## Client SDK Bootstrapping | SSR

If you are using the Statsig client SDK in a browser or mobile app, you can bootstrap the client SDK with the values from the server SDK to avoid a network request on the client. This is useful for server-side rendering (SSR) or when you want to reduce the number of network requests on the client.

```elixir  theme={null}
# Get client initialize response for a user
{:ok, response} = Statsig.get_client_init_response_as_string(user)

# Pass values to a client SDK to initialize without a network request
```

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

<Note>
  Not supported at this time.
</Note>

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

<Note>
  Not supported at this time.
</Note>

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

<Note>
  Not supported at this time.
</Note>

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

<Note>
  Not supported at this time.
</Note>

## FAQ

<AccordionGroup>
  <Accordion title="How do I run experiments for logged out users?">
    See the guide on [device level experiments](/guides/logging-events#device-level-events)
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).