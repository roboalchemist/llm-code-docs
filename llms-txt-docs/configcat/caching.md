# Source: https://configcat.com/docs/advanced/caching.md

# Polling modes & Caching

There are 3 different ways (polling modes) to control caching.

## Auto polling (default)[​](#auto-polling-default "Direct link to Auto polling (default)")

In auto polling mode, the ConfigCat SDK downloads the latest feature flags and settings from the ConfigCat CDN automatically and stores them in the cache. By default, this happens every 60 seconds. You can set the polling interval to any value between 1 and 2,147,483 seconds.

## Lazy loading[​](#lazy-loading "Direct link to Lazy loading")

In lazy loading mode, the ConfigCat SDK downloads the latest feature flags and settings from the ConfigCat CDN only if they are not already present in the cache, or if the cache has expired. By default, the cache Time To Live (TTL) value is 60 seconds. You can set it to any value between 1 and 2,147,483,647 seconds.

## Manual polling[​](#manual-polling "Direct link to Manual polling")

Manual polling gives you full control over when the feature flags and settings are downloaded from the ConfigCat CDN. The ConfigCat SDK will not download them automatically. You can (and should) update the cache manually, by calling a `forceRefresh()` - this will download the latest feature flags and settings and update the cache.

This animation explains the different polling modes:

## Caching[​](#caching "Direct link to Caching")

ConfigCat SDKs in their default setup store all the information they need for feature flag evaluation in memory. This behavior is extendable with custom cache implementations that you can use for pointing the SDK to your own data storage.

The main reason for caching is to accelerate serving feature flag evaluation requests when your application is in a stateless environment or frequently restarts. When the SDK notices that it has a valid cache entry to work with, it will use the data from the cache rather than initiating a new HTTP request towards ConfigCat. The cache's validity is based on the polling interval in case of [auto polling](#auto-polling-default) or on the TTL in case of [lazy loading](#lazy-loading).

info

See the [SDK specific docs](https://configcat.com/docs/docs/sdk-reference/overview/.md) for your desired platform to learn how to use custom cache implementations.

### Offline mode[​](#offline-mode "Direct link to Offline mode")

ConfigCat SDKs have the capability to go offline. In offline mode, they work only from the configured cache and never communicate with ConfigCat over HTTP.

This allows you to set up a centralized cache that only one online ConfigCat SDK writes, but serves many offline ones.

info

See the [SDK specific docs](https://configcat.com/docs/docs/sdk-reference/overview/.md) for your desired platform to learn how to enable offline mode.

### Shared cache[​](#shared-cache "Direct link to Shared cache")

As of certain versions, ConfigCat SDKs support using a shared cache. To achieve that, each SDK constructs the key for identifying a specific cache entry based on the SDK key passed at initialization. This means each platform specific SDK that uses the same SDK key will use the same cache entry.

Mixing this behavior with [offline mode](#offline-mode), you can have a centralized shared cache that serves many SDKs regardless of what platform they run on.

Support for shared caching was introduced in these SDK versions:

| SDK                                                                             | Version                                                           |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| .NET                                                                            | >= [v8.1.0](https://github.com/configcat/.net-sdk/releases)       |
| Android (Java)                                                                  | >= [v9.0.0](https://github.com/configcat/android-sdk/releases)    |
| C++                                                                             | >= [v3.0.0](https://github.com/configcat/cpp-sdk/releases)        |
| Dart (Flutter)                                                                  | >= [v3.0.0](https://github.com/configcat/dart-sdk/releases)       |
| Elixir                                                                          | >= [v3.0.0](https://github.com/configcat/elixir-sdk/releases)     |
| Go                                                                              | >= [v8.0.0](https://github.com/configcat/go-sdk/releases)         |
| Java                                                                            | >= [v8.2.0](https://github.com/configcat/java-sdk/releases)       |
| JavaScript (Browser, Bun, Chromium Extension, Cloudflare Worker, Deno, Node.js) | >= [v1.0.0](https://github.com/configcat/js-unified-sdk/releases) |
| JS - Legacy                                                                     | >= [v8.0.0](https://github.com/configcat/js-sdk/releases)         |
| JS SSR - Legacy                                                                 | >= [v7.0.0](https://github.com/configcat/js-ssr-sdk/releases)     |
| Kotlin                                                                          | >= [v2.0.0](https://github.com/configcat/kotlin-sdk/releases)     |
| Node.js - Legacy                                                                | >= [v10.0.0](https://github.com/configcat/node-sdk/releases)      |
| PHP                                                                             | >= [v8.0.0](https://github.com/configcat/php-sdk/releases)        |
| Python                                                                          | >= [v8.0.0](https://github.com/configcat/python-sdk/releases)     |
| React                                                                           | >= [v3.0.0](https://github.com/configcat/react-sdk/releases)      |
| Ruby                                                                            | >= [v7.0.0](https://github.com/configcat/ruby-sdk/releases)       |
| Rust                                                                            | >= [v0.1.0](https://github.com/configcat/rust-sdk/releases)       |
| Swift (iOS)                                                                     | >= [v10.0.0](https://github.com/configcat/swift-sdk/releases)     |
