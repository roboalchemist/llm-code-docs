# Source: https://www.apollographql.com/docs/graphos/routing/customization/custom-binary.md

# Creating a Custom Apollo Router Core Binary

Learn how to compile a custom binary from Apollo Router Core source, which is required to create custom native Rust plugins for the router.

⚠️ Apollo doesn't recommend creating native plugins for the Apollo Router Core or GraphOS Router, for the following reasons:

* Native plugins require familiarity with programming in Rust.
* Native plugins require compiling a custom router binary from source, which can introduce unexpected behavior in your router that's difficult to diagnose and support.

The recommended approach for router customizations is to use a [Rhai script](https://www.apollographql.com/docs/graphos/routing/customization/rhai/). For more advanced use cases, you can use an [external coprocessor](https://www.apollographql.com/docs/router/customizations/coprocessor). Both options are officially supported by Apollo and provide strong separation of concerns and fault isolation.

Although you can still use native plugins and custom router binaries, Apollo Support can't provide troubleshooting support or fixes for these customizations.

If you must create a native plugin, please [open a GitHub issue](https://github.com/apollographql/router/issues), and Apollo can investigate adding the custom capability to the stock router binary.

The Apollo Router Core source code and all its distributions are made available under the [Elastic License v2.0 (ELv2) license](https://www.apollographql.com/docs/resources/elastic-license-v2-faq/#can-i-extend-or-modify-the-gateway-or-router-by-creating-plugins).

## Prerequisites

To compile the router, you need to have [Rust 1.91.1 or later](https://www.rust-lang.org/tools/install) installed.

## 1. Create a new project

1. Use the `cargo new` command to create a project for your custom router:

   ```bash
   cargo new --bin starstuff
   ```

For the purposes of this tutorial, set your project's name to `starstuff`.

2. After your project is created, change to the `starstuff` directory:

   ```bash
   cd starstuff
   ```

Write the source code for your custom binary.

## 2. Compile the router

Create a debug build of the router with the following command:

```bash
cargo build
```

The resulting debug binary is located in `target/debug/router`.

To create a release build for production environments, use this command instead:

```bash
cargo build --release
```

The resulting release binary is now located in `target/release/router`.

## 3. Run the compiled binary

Now you can test out your compiled router with an example supergraph schema.

1. Download the example schema with the following command:

   ```bash
   curl -sSL https://supergraph.demo.starstuff.dev/ > supergraph-schema.graphql
   ```

2. Run the router and provide the example schema like so:

   ```bash
   cargo run -- --hot-reload --config router.yaml --supergraph supergraph-schema.graphql
   ```

   During development, it's helpful to use `cargo run` to run the router.

If you're using managed federation, you set the `APOLLO_KEY` and `APOLLO_GRAPH_REF` environment variables instead of specifying the supergraph schema as a file. For details, see [this section](https://www.apollographql.com/docs/federation/managed-federation/setup#4-connect-your-router-to-graphos).

## 4. Create a plugin

1. From within your project directory, implement your new plugin.

2. Add configuration options for the created plugin to your `router.yaml` file:

   ```yaml title=router.yaml
   plugins:
     starstuff.hello_world:
       message: "starting my plugin"
   ```

3. Run the router again:

   ```bash
   cargo run -- --hot-reload --config router.yaml --supergraph supergraph-schema.graphql
   ```

   This time, you should see a log line like the following:

   ```bash
   2022-05-21T09:16:33.160288Z  INFO router::plugins::hello_world: starting my plugin
   ```

Nice work! You now have a custom router binary with an associated plugin. Next, you can extend the plugin with the functionality you need or add more plugins.

## Memory allocator

On Linux the `apollo-router` crate sets [jemalloc](http://jemalloc.net/)
as [the global memory allocator for Rust](https://doc.rust-lang.org/std/alloc/index.html#the-global_allocator-attribute)
to reduce memory fragmentation.
Future versions may do so on more platforms, or switch to yet a different allocator.
This is enabled by default and controlled by a `global-allocator` Cargo feature flag.
If you want to choose a different allocator, disable it in your `Cargo.toml`:

```toml
[dependencies]
apollo-router = {version = "[…]", default-features = false}
```

If you make a library crate, also specify `default-features = false`
in order to leave the choice open for the eventual executable crate.
(Cargo default features are only disabled if *all* dependents specify `default-features = false`.)

## Related topics

* [Optimizing Custom Router Builds](https://www.apollographql.com/docs/graphos/routing/self-hosted/containerization/optimize-build)
