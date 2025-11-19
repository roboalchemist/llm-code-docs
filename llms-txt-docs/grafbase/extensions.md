# Source: https://grafbase.com/docs/gateway/configuration/extensions.md

# Source: https://grafbase.com/docs/gateway/extensions.md

# Extensions

Extensions are a powerful feature of the Grafbase Gateway that lets you extend its functionality with custom code. You write extensions in Rust and compile them into a WebAssembly module that the [Grafbase Gateway](https://grafbase.com/docs/gateway/installation.md) loads. Extensions implement custom authentication, authorization, and resolving logic, and integrate with external services and APIs.

<Image
  src="/images/docs/extensions/card-extensions--dark.png"
  alt="Grafbase Extensions"
  width={960}
  height={584}
  priority="true"
/>

Read more about [configuring the extensions in gateway](https://grafbase.com/docs/gateway/configuration/extensions.md), and [a guide on implementing one](/guides/implementing-a-gateway-resolver-extension).

## Extensions Architecture

An extension is a WebAssembly module with a JSON manifest. You add them to your gateway installation through configuration, and the gateway loads them automatically when it starts.

Two types of extensions exist: resolver extensions and authentication extensions. Resolver extensions extend the functionality of the gateway's resolvers, while authentication extensions extend the functionality of the gateway's authentication system.

We mainly support Rust to implement extensions. Grafbase provides a [Rust SDK](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/) that makes implementing extensions easy. The SDK provides traits that you implement to extend the functionality of the gateway's resolvers and authentication system.

## Extension Manifest

The extension manifest is a JSON file that describes the extension's metadata and configuration. The Grafbase Gateway uses it to load and configure the extension.

The manifest file must contain the following fields:

- `name`: The name of the extension.
- `version`: The version of the extension.
- `kind`: The type of the extension (`resolver` or `authentication`).
- `sdk_version`: The version of the Grafbase SDK used to implement the extension.
- `minimum_gateway_version`: The minimum version of the Grafbase Gateway required to run the extension.
- `sdl`: The GraphQL directives and types the extension provides.

This file is called `manifest.json` in the extension's root directory.

## Extension Implementation

The extension logic compiles into a WebAssembly component and implements the [WASI Preview 2](https://github.com/WebAssembly/WASI/blob/main/wasip2/README.md) standard. This gives WebAssembly components more tooling to perform previously impossible tasks. These include network access with TCP or UDP, file system access, environment variable access and more.

An extension configuration defines what features the specific extension can access in its sandbox. You configure per-extension options in the gateway configuration to control what the extension can and cannot access.

The [Grafbase Rust SDK](https://docs.rs/grafbase-sdk/latest/grafbase_sdk/) provides the traits for implementing an extension, and the [Grafbase CLI](https://grafbase.com/docs/cli/installation.md) provides the commands for building and deploying extensions.

## Vision

We believe the Grafbase Gateway should serve as a platform to combine multiple data sources into a single GraphQL API. Extensions enable us to provide faster implementation of connections that were not previously feasible in the gateway itself. Our simple development tooling makes it easier for you to implement such connections.

For example, if your company uses a service that requires a custom protocol, you can implement an extension to connect to that service.

Although we license the Grafbase Gateway under the Mozilla Public License 2.0, we do not expect you to follow the same licensing with extensions. You can either submit a pull request with your extension code to make it available to the community, or keep it private for internal use.