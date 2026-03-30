# Source: https://www.apollographql.com/docs/graphos/routing/customization/native-plugins.md

# Writing Native Rust Plugins

Your federated graph might have specific requirements that aren't supported by the built-in [configuration options](https://www.apollographql.com/docs/router/configuration/overview/) of the GraphOS Router or Apollo Router Core. For example, you might need to further customize the behavior of:

* Authentication/authorization
* Logging
* Operation tracing

In these cases, you can create custom plugins for the router.

⚠️ Apollo doesn't recommend creating native plugins for the Apollo Router Core or GraphOS Router, for the following reasons:

* Native plugins require familiarity with programming in Rust.
* Native plugins require compiling a custom router binary from source, which can introduce unexpected behavior in your router that's difficult to diagnose and support.

The recommended approach for router customizations is to use a [Rhai script](https://www.apollographql.com/docs/graphos/routing/customization/rhai/). For more advanced use cases, you can use an [external coprocessor](https://www.apollographql.com/docs/router/customizations/coprocessor). Both options are officially supported by Apollo and provide strong separation of concerns and fault isolation.

Although you can still use native plugins and custom router binaries, Apollo Support can't provide troubleshooting support or fixes for these customizations.

If you must create a native plugin, please [open a GitHub issue](https://github.com/apollographql/router/issues), and Apollo can investigate adding the custom capability to the stock router binary.

The Apollo Router Core source code and all its distributions are made available under the [Elastic License v2.0 (ELv2) license](https://www.apollographql.com/docs/resources/elastic-license-v2-faq/#can-i-extend-or-modify-the-gateway-or-router-by-creating-plugins).

## Planning a plugin

When designing a new plugin, you first want to determine which of the router's **services** the plugin should hook into to achieve its use case.

For descriptions of these services, see [Router request lifecycle](https://www.apollographql.com/docs/graphos/routing/customization/rhai#router-request-lifecycle).

## Building a plugin

To demonstrate building a plugin, we'll walk through the [hello world example plugin](https://github.com/apollographql/router/tree/main/examples/hello-world) in the router repo.

### 1. Add modules

Most plugins should start by including the following set of `use` declarations:

```rust title=hello_world.rs
use apollo_router::plugin::Plugin;
use apollo_router::register_plugin;
use apollo_router::services::*;
use schemars::JsonSchema;
use serde::Deserialize;
use tower::{BoxError, ServiceBuilder, ServiceExt};
```

When your plugin is complete, the compiler will provide helpful warnings if any of these modules *aren't* necessary. Your plugin can also `use` modules from other crates as needed.

### 2. Define your configuration

All plugins require an associated configuration. At a minimum, this configuration contains a boolean that indicates whether the plugin is enabled, but it can include anything that can be deserialized by `serde`.

Create your configuration struct like so:

```rust title=hello_world.rs
#[derive(Debug, Default, Deserialize, JsonSchema)]
struct Conf {
    // Put your plugin configuration here. It's deserialized from YAML automatically.
}
```

> **Note:** You need to `derive` `JsonSchema` so that your configuration can participate in [JSON schema generation](https://www.apollographql.com/docs/router/configuration/overview/#configuration-awareness-in-your-text-editor).

Then define the plugin itself and specify the configuration as an associated type:

```rust title=hello_world.rs
#[async_trait::async_trait]
impl Plugin for HelloWorld {
    type Config = Conf;
}
```

### 3. Implement the `Plugin` trait

All router plugins must implement the `Plugin` trait. This trait defines lifecycle hooks that enable hooking into a router's services.

The trait also provides a default implementations for each hook, which returns the associated service unmodified.

```rust title=hello_world.rs
// This is a bare-bones plugin that you can duplicate when creating your own.
use apollo_router::plugin::PluginInit;
use apollo_router::plugin::Plugin;
use apollo_router::services::*;

#[async_trait::async_trait]
impl Plugin for HelloWorld {
    type Config = Conf;

    // This is invoked once after the router starts and compiled-in
    // plugins are registered
    fn new (init: PluginInit<Self::Config>) -> Result<Self, BoxError> {
        Ok(HelloWorld { configuration: init.config })
    }

    // Only define the hooks you need to modify. Each default hook
    // implementation returns its associated service with no changes.
    fn router_service(
        &self,
        service: router::BoxService,
    ) -> router::BoxService {
        service
    }

    fn supergraph_service(
        &self,
        service: supergraph::BoxService,
    ) -> supergraph::BoxService {
        service
    }

    fn execution_service(
        &self,
        service: execution::BoxService,
    ) -> execution::BoxService {
        service
    }

    // Unlike other hooks, this hook also passes the name of the subgraph
    // being invoked. That's because this service might invoke *multiple*
    // subgraphs for a single request, and this is called once for each.
    fn subgraph_service(
        &self,
        name: &str,
        service: subgraph::BoxService,
    ) -> subgraph::BoxService {
        service
    }
}
```

### 4. Define individual hooks

To define custom logic for a service hook, you can use [`ServiceBuilder`](https://docs.rs/tower/0.3.1/tower/builder/struct.ServiceBuilder.html).

`ServiceBuilder` provides common building blocks that remove much of the complexity of writing a plugin. These building blocks are called layers.

```rust title=hello_world.rs
// Replaces the default definition in the example above
use tower::ServiceBuilderExt;
use apollo_router::ServiceBuilderExt as ApolloServiceBuilderExt;

fn supergraph_service(
    &self,
    service: router::BoxService,
) -> router::BoxService {
    // Always use service builder to compose your plugins.
    // It provides off-the-shelf building blocks for your plugin.
    ServiceBuilder::new()
        // Some example service builder methods:
        // .map_request()
        // .map_response()
        // .rate_limit()
        // .checkpoint()
        // .timeout()
        .service(service)
        .boxed()
}
```

The [tower-rs](https://github.com/tower-rs) library (which the router is built on) comes with many "off-the-shelf" layers. In addition, Apollo provides layers that cover common functionality and integration with third-party products.

Some notable layers are:

* **buffered** - Make a service `Clone`. Typically required for any `async` layers.
* **checkpoint** - Perform a sync call to decide if a request should proceed or not. Useful for validation.
* **checkpoint\_async** - Perform an async call to decide if the request should proceed or not. e.g. for Authentication. Requires `buffered`.
* **oneshot\_checkpoint\_async** - Perform an async call to decide if the request should proceed or not. e.g. for Authentication. Does not require `buffered` and should be preferred to `checkpoint_async` for that reason.
* **instrument** - Add a tracing span around a service.
* **map\_request** - Transform the request before proceeding. e.g. for header manipulation.
* **map\_response** - Transform the response before proceeding. e.g. for header manipulation.

Before implementing a layer yourself, always check whether an existing layer implementation might fit your needs. Reusing layers is significantly faster than implementing layers from scratch.

### 5. Define necessary context

Sometimes you might need to pass custom information between services. For example:

* Authentication information obtained by the `SupergraphService` might be required by `SubgraphService`s.
* Cache control headers from `SubgraphService`s might be aggregated and returned to the client by the `SupergraphService`.

Whenever the router receives a request, it creates a corresponding `context` object and passes it along to each service. This object can store anything that's Serde-compatible (e.g., all simple types or a custom type).

All of your plugin's hooks can interact with the `context` object using the following functions:

#### `insert`

```rust
context.insert("key1", 1)?;
```

Adds a value to the `context` object. Serialization and deserialization happen automatically. You might sometimes need to specify the type in cases where the Rust compiler can't figure it out by itself.

If multiple threads might write a value to the same `context` key, use [`upsert`](https://www.apollographql.com/docs/graphos/routing/customization/native-plugins.md#upsert) instead.

#### `get`

```rust
let value : u32 = context.get("key1")?;
```

Fetches a value from the `context` object.

#### `upsert`

```rust
context.upsert("key1", |v: u32| v + 1)?;
```

Use `upsert` if you might need to resolve multiple simultaneous writes to a single `context` key (this is most likely for the `subgraph_service` hook, because it might be called by multiple threads in parallel). Rust is multithreaded, and you will get unexpected results if multiple threads write to `context` at the same time. This function prevents issues by guaranteeing that modifications happen serially.

Note: `upsert` requires v to implement `Default`.

### 6. Register your plugin

To enable the router to discover your plugin, you need to **register** the plugin.

To do so, use the `register_plugin!()` macro provided by `apollo-router`. This takes 3 arguments:

* A group name
* A plugin name
* A struct implementing the `Plugin` trait

For example:

```rust title=hello_world.rs
register_plugin!("example", "hello_world", HelloWorld);
```

Choose a group name that represents your organization and a name that represents your plugin's functionality.

### 7. Configure your plugin

After you register your plugin, you need to add configuration for it to your [YAML configuration file](https://www.apollographql.com/docs/router/configuration/overview/#yaml-config-file) in the `plugins:` section:

```yaml
plugins:
  example.hello_world:
    # Any values here are passed to the plugin as part of your configuration
```

## Observability

### Add custom metrics

Make sure to [configure a metrics exporter](https://www.apollographql.com/docs/graphos/routing/observability/telemetry/metrics-exporters/overview) if you want to have metrics generated by the router.

To create custom metrics, you can use the [OpenTelemetry](https://docs.rs/opentelemetry/0.24.0/opentelemetry/) crates.

To publish a new metric, get the OpenTelemetry [`MeterProvider`](https://docs.rs/opentelemetry/0.24.0/opentelemetry/metrics/struct.MeterProvider.html) and register an instrument:

```rust
use apollo_router::metrics::meter_provider;

let meter = meter_provider().meter("apollo/router");
// The instrument will publish metrics until it is dropped.
let _instrument = meter.u64_observable_gauge("foo")
    .with_description("The amount of active foos")
    .with_callback(|gauge| {
        gauge.observe(count_the_foos());
    })
    .init();
```

### Add custom spans

Make sure to [enable OpenTelemetry tracing](https://www.apollographql.com/docs/router/configuration/telemetry/exporters/tracing/overview) in your configuration if you want customize the traces generated and linked by the router.

To create custom spans and traces you can use [`tracing` macros](https://docs.rs/tracing/latest/tracing/index.html#macros) to generate a span.

```rust
use tracing::info_span;

info_span!("my_span");
```

### Accessing operation IDs

When writing plugins, you can access [GraphOS Studio operation IDs](https://www.apollographql.com/docs/graphos/platform/insights/operation-signatures) by reading the value of `apollo::supergraph::operation_id` from [`context`](https://www.apollographql.com/docs/graphos/routing/customization/native-plugins.md#5-define-necessary-context).

## Plugin lifecycle

Like individual requests, plugins follow their own strict lifecycle that helps provide structure to the router's execution.

### Creation

When the router starts or reloads, it calls `new` to create instances of plugins that have configuration in the `plugins:` section of the [YAML configuration file](https://www.apollographql.com/docs/router/configuration/overview/#yaml-config-file). If any of these calls fail, the router terminates with helpful error messages.

There is no sequencing for plugin registration, and registrations might even execute in parallel. A plugin should *never* rely on the existence of *another* plugin during initialization.

### Request and response lifecycle

Within a given service (router, subgraph, etc.), a *request* is handled in the following order:

* [Rhai script](https://www.apollographql.com/docs/graphos/routing/customization/rhai)
* [External coprocessor](https://www.apollographql.com/docs/router/customizations/coprocessor)
* Rust plugins, in the same order they're declared in your [YAML configuration file](https://www.apollographql.com/docs/router/configuration/overview/#yaml-config-file).

The corresponding *response* is handled in the opposite order.
This ordering is relevant for communicating through [the `context` object](https://www.apollographql.com/docs/graphos/routing/customization/native-plugins.md#5-define-necessary-context).

When a single supergraph request involves multiple subgraph requests, the handling of each subgraph request and response is ordered as above but different subgraph requests may be handled in parallel, making their relative ordering non-deterministic.

### Router lifecycle notes

If a router is listening for dynamic changes to its configuration, it also triggers lifecycle events when those changes occur.

Before switching to an updated configuration, the router ensures that the new configuration is valid. This process includes starting up replacement plugins for the new configuration. This means that a plugin should *not* assume that it's the *only* executing instance of that plugin in a single router.

After the new configuration is deemed valid, the router shifts to it. The previous configuration is dropped and its corresponding plugins are shut down. Errors during the shutdown of these plugins are logged and do not affect router execution.

### Testing plugins

Unit testing of a plugin is typically most helpful and there are extensive examples of plugin testing in the examples and plugins directories.

If you need a unique identifier for your request, use the functionality provided in the `apollo_router::tracer` module.
