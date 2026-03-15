# Source: https://posthog.com/docs/product-analytics/installation/elixir.md

# Source: https://posthog.com/docs/feature-flags/installation/elixir.md

# Source: https://posthog.com/docs/libraries/elixir.md

# Elixir - Docs

This library provides an Elixir HTTP client for PostHog. [See the repository](https://github.com/posthog/posthog-elixir) for more information.

## Installation

> This library was built by the community but it's being maintained by the PostHog core team since v1.0.0. Thank you to [Nick Kezhaya](https://github.com/nkezhaya) for building it originally. Thank you to [Alex Martsinovich](https://github.com/martosaur) for contributing v2.0.0.

The package can be installed by adding `posthog` to your list of dependencies in `mix.exs`:

Elixir

PostHog AI

```elixir
def deps do
  [
    {:posthog, "~> 2.2.0"}
  ]
end
```

### Configuration

config/config.exs

PostHog AI

```elixir
config :posthog,
  enable: true,
  api_host: "https://us.i.posthog.com",
  api_key: "<ph_project_token>",
  in_app_otp_apps: [:my_app]
```

You can see all the available configuration options in the [PostHog.Config](https://hexdocs.pm/posthog/PostHog.Config.html) module.

Optionally, you might want to enable the [Plug integration](https://hexdocs.pm/posthog/PostHog.Integrations.Plug.html) to automatically capture events from your Plug-based applications including Phoenix.

#### Development/Test mode

For a test environment, you can pass in `test_mode: true` value to the config. This causes events to be dropped instead of sent to PostHog.

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

## Capturing events

To capture an event, use `PostHog.capture/2`:

Elixir

PostHog AI

```elixir
PostHog.capture("user_signed_up", %{distinct_id: "distinct_id_of_the_user"})
```

> **Tip:** We recommend using a `[object] [verb]` format for your event names, where `[object]` is the entity that the behavior relates to, and `[verb]` is the behavior itself. For example, `project created`, `user signed up`, or `invite sent`.

### Setting event properties

Optionally, you can include additional information with the event by including a [properties](/docs/data/events.md#event-properties) object:

Elixir

PostHog AI

```elixir
PostHog.capture("user_signed_up", %{
  distinct_id: "distinct_id_of_the_user",
  login_type: "email",
  is_free_trial: true
})
```

### Context

Carrying `distinct_id` around all the time might not be the most convenient approach, so PostHog lets you store it and other properties in a context.

The context is stored in the `Logger` metadata and PostHog automatically attaches these properties to any events you capture with `PostHog.capture/2`, as long as they happen in the same process.

Elixir

PostHog AI

```elixir
PostHog.set_context(%{distinct_id: "distinct_id_of_the_user"})
PostHog.capture("page_opened")
```

You can also scope the context to a specific event name:

Elixir

PostHog AI

```elixir
PostHog.set_event_context("sensitive_event", %{"$process_person_profile": false})
```

### Batching events

Events are automatically batched and sent to PostHog via a background job.

### Special events

`PostHog.capture/2` is very powerful and enables you to send events that have special meaning.

In other libraries you'll usually find helpers for these special events, but they must be explicitly sent in Elixir.

For example:

#### Create alias

Elixir

PostHog AI

```elixir
PostHog.capture("$create_alias", %{distinct_id: "frontend_id", alias: "backend_id"})
```

#### Group analytics

Elixir

PostHog AI

```elixir
PostHog.capture("$groupidentify", %{
  distinct_id: "static_string_used_for_all_group_events",
  "$group_type": "company",
  "$group_key": "company_id_in_your_db"
})
```

## Feature flags

PostHog's [feature flags](/docs/feature-flags.md) enable you to safely deploy and roll back new features as well as target specific users and groups with them.

`PostHog.FeatureFlags.check/2` is the main function for checking a feature flag in Elixir. More documentation on it can be found in the [HexPM Docs](https://hexdocs.pm/posthog/PostHog.FeatureFlags.html).

#### Boolean feature flags

Elixir

PostHog AI

```elixir
iex> PostHog.FeatureFlags.check("example-feature-flag-1", "user123")
{:ok, true}
```

It will attempt to take `distinct_id` from the context if it's not provided.

Elixir

PostHog AI

```elixir
iex> PostHog.set_context(%{distinct_id: "user123"})
:ok
iex> PostHog.FeatureFlags.check("example-feature-flag-1")
{:ok, true}
```

#### Multivariate feature flags

Elixir

PostHog AI

```elixir
iex> PostHog.FeatureFlags.check("example-feature-flag-1", "user123")
{:ok, "variant2"}
```

### Errors

We'll return an error if the feature flag doesn't exist.

Elixir

PostHog AI

```elixir
iex> PostHog.FeatureFlags.check("example-feature-flag-3", "user123")
{:error, %PostHog.UnexpectedResponseError{message: "Feature flag example-feature-flag-3 was not found in the response", response: ...}}
```

You can also use `PostHog.FeatureFlags.check!/2` if you're feeling adventurous or running a script and prefer errors to be raised instead.

## Error tracking

Error tracking is enabled by default. It will automatically captures exceptions thrown by the application.

As a matter of fact, since this is built on top of Elixir's `Logger` module, it automatically captures any `Logger.error` calls.

You can always disable it by setting `enable_error_tracking` to false:

Elixir

PostHog AI

```elixir
config :posthog,
  enable_error_tracking: false
```

## Advanced configuration

By default, PostHog starts its own supervision tree and attaches a logger handler.

In certain cases, you might want to run this supervision tree yourself. You can do this by disabling the default supervisor and adding PostHog.Supervisor to your application tree with its own configuration:

config.exs

PostHog AI

```elixir
config :posthog, enable: false
config :my_app, :posthog,
  api_host: "https://us.i.posthog.com",
  api_key: "<ph_project_token>"
```

application.ex

PostHog AI

```elixir
defmodule MyApp.Application do
  use Application
  def start(_type, _args) do
    posthog_config = Application.fetch_env!(:my_app, :posthog) |> PostHog.Config.validate!()
    :logger.add_handler(:posthog, PostHog.Handler, %{config: posthog_config})
    children = [
      {PostHog.Supervisor, posthog_config}
    ]
    Supervisor.start_link(children, strategy: :one_for_one)
  end
end
```

### Multiple instances

In even more advanced cases, you might want to interact with more than one PostHog project. In this case, you can run multiple PostHog supervision trees, one of which can be the default one:

config.exs

PostHog AI

```elixir
config :posthog,
  api_host: "https://us.i.posthog.com",
  api_key: "<ph_project_token>"
config :my_app, :another_posthog,
  api_host: "https://us.i.posthog.com",
  api_key: "a_different_project_api_key",
  supervisor_name: AnotherPostHog
```

application.ex

PostHog AI

```elixir
defmodule MyApp.Application do
  use Application
  def start(_type, _args) do
    posthog_config = Application.fetch_env!(:my_app, :another_posthog) |> PostHog.Config.validate!()
    children = [
      {PostHog.Supervisor, posthog_config}
    ]
    Supervisor.start_link(children, strategy: :one_for_one)
  end
end
```

Then, each function in the PostHog module accepts an optional first argument with the name of the PostHog supervisor tree that will process the capture:

Elixir

PostHog AI

```elixir
PostHog.capture(AnotherPostHog, "user_signed_up", %{distinct_id: "user123"})
```

## Thanks

The library is maintained by the PostHog team since February 2025. Thanks to [nkezhaya](https://github.com/nkezhaya) for contributing v0.1.0. Thanks to [martosaur](https://github.com/martosaur) for contributing v2.0.0.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better