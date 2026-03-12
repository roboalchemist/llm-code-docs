# Source: https://docs.statsig.com/server/erlang.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Legacy Erlang/Elixir Server SDK

> Statsig's Legacy Server SDK for Erlang and Elixir applications

<Danger> Support for the Legacy Erlang SDK ends April 30, 2026. Migrate to the [new Elixir SDK](/server-core/elixir-core) soon. </Danger>

<Warning>
  The erlang SDK repository, and this docs site, are a work in progress. If you are trying to use Statsig in erlang or elixir, please reach out to our support team, your sales contact, or in our [Slack community](https://statsig.com/slack).
</Warning>

[Github Repository](https://github.com/statsig-io/erlang-sdk)

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    Add a dependency on statsig to your:

    **mix.exs**:

    ```elixir  theme={null}
    {:statsig, "~> 0.0.1"}
    ```

    **rebar.config**:

    ```erlang  theme={null}
    {statsig, "0.0.1"}.
    ```

    **erlang.mk**:

    ```makefile  theme={null}
    dep_statsig = hex 0.0.1
    ```
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Do NOT embed your Server Secret Key in client-side applications, or expose it in any external-facing documents. However, if you accidentally expose it, you can create a new one in the Statsig console.
    </Warning>

    <CodeGroup>
      ```erlang Erlang theme={null}
      statsig:initialize(<<"secret-key">>).

      % or with options
      Options = #{environment => #{tier => <<"staging">>}},
      statsig:initialize(<<"secret-key">>, Options).
      ```

      ```elixir Elixir theme={null}
      Statsig.initialize("secret-key")

      # or with options
      options = %{environment: %{tier: "staging"}}
      Statsig.initialize("secret-key", options)
      ```
    </CodeGroup>

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Working with the SDK

## Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

<CodeGroup>
  ```erlang Erlang theme={null}
  User = #{<<"userID">> => <<"user-id">>},
  GateValue = statsig:check_gate(User, <<"gate_name">>).
  ```

  ```elixir Elixir theme={null}
  user = %{"userID" => "user-id"}
  gate_value = Statsig.check_gate(user, "gate_name")
  ```
</CodeGroup>

## Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be able send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it.

<CodeGroup>
  ```erlang Erlang theme={null}
  Config = statsig:get_config(User, <<"config_name">>),
  Value = statsig_config:get(Config, <<"param">>, <<"default">>).
  ```

  ```elixir Elixir theme={null}
  config = Statsig.get_config(user, "config_name")
  value = StatsigConfig.get(config, "param", "default")
  ```
</CodeGroup>

## Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but we recommend the use of [layers](/layers) to enable quicker iterations with parameter reuse.

<CodeGroup>
  ```erlang Erlang theme={null}
  Layer = statsig:get_layer(User, <<"layer_name">>),
  ParamValue = statsig_layer:get(Layer, <<"param">>, <<"default">>).
  ```

  ```elixir Elixir theme={null}
  layer = Statsig.get_layer(user, "layer_name")
  param_value = StatsigLayer.get(layer, "param", "default")
  ```
</CodeGroup>

## Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig - simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

<CodeGroup>
  ```erlang Erlang theme={null}
  statsig:log_event(User, <<"event_name">>).
  ```

  ```elixir Elixir theme={null}
  Statsig.log_event(user, "event_name")
  ```
</CodeGroup>

Learn more about identifying users, group analytics, and best practices for logging events in the [logging events guide](/guides/logging-events).

## Statsig User

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides `userID`, we also have `email`, `ip`, `userAgent`, `country`, `locale` and `appVersion` as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the `custom` field and be able to create targeting based on them.

Note that while typing is lenient on the `StatsigUser` object to allow you to pass in numbers, strings, arrays, objects, and potentially even enums or classes, the evaluation operators will only be able to operate on primitive types - mostly strings and numbers. While we attempt to smartly cast custom field types to match the operator, we cannot guarantee evaluation results for other types. For example, setting an array as a custom field will only ever be compared as a string - there is no operator to match a value in that array.

### Private Attributes

Have sensitive user PII data that should not be logged? No problem, we have a solution for it! On the StatsigUser object we also have a field called `privateAttributes`, which is a simple object/dictionary that you can use to set private user attributes. Any attribute set in `privateAttributes` will only be used for evaluation/targeting, and removed from any logs before they are sent to Statsig server.

For example, if you have feature gates that should only pass for users with emails ending in "@statsig.com", but do not want to log your users' email addresses to Statsig, you can simply add the key-value pair `{ email: "my_user@statsig.com" }` to `privateAttributes` on the user and that's it!

## Shutdown

To gracefully shutdown the SDK and ensure all events are flushed:

<CodeGroup>
  ```erlang Erlang theme={null}
  statsig:shutdown().
  ```

  ```elixir Elixir theme={null}
  Statsig.shutdown()
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).