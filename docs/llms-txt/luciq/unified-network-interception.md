# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/logs-and-profiling/unified-network-interception.md

# Unified Network Interception

### Overview

Previously, capturing network logs required integrating multiple interceptors for different products. The Unified Network Interceptor consolidates this into one approach that:

* Captures network requests automatically with minimal setup via the Gradle plugin
* Supports all Luciq products from a single integration
* Works with popular networking libraries: OkHttp, UrlConnection, and gRPC
* Centralizes network log customization through a single listener API

{% hint style="info" %}
Minimum SDK Version

Unified Network Interception is available starting from **SDK v19.0.0**.
{% endhint %}

***

### Quickstart

The fastest way to get started is using the Luciq Gradle Plugin. Add the plugin to your project and enable network interception.

App-level `build.gradle` or `build.gradle.kts`:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("luciq")
}

luciq {
    networkInterception {
        enabled = true
    }
}
```

{% endcode %}

{% hint style="info" %}
That's all you need to get started! The plugin handles everything automatically. Continue reading below only if you need to customize the configuration or integrate manually.
{% endhint %}

***

### Getting Started

The recommended approach is to use the Luciq Gradle Plugin for automatic network interception. This eliminates the need for manual interceptor setup in most cases.

#### Prerequisites

Before enabling unified network interception, ensure your project includes the required dependencies:

* For OkHttp: Both dependencies are required:
  * `ai.luciq.library:luciq-with-okhttp-interceptor`
  * `ai.luciq.library:luciq-apm-okhttp-interceptor`
* For UrlConnection: No additional dependencies required - included with the main SDK.
* For gRPC: The gRPC interceptor dependency is required:
  * `ai.luciq.library:luciq-grpc-interceptor`

***

### Plugin Integration (Recommended)

The Luciq Gradle Plugin automatically instruments your networking libraries, eliminating the need to manually add interceptors to each `OkHttpClient` or replace `url.openConnection()` calls throughout your codebase. This is the preferred approach because it:

* Reduces integration complexity — No need to modify existing networking code
* Ensures consistent coverage — Automatically captures requests from all networking libraries
* Simplifies maintenance — Future updates are handled through plugin configuration
* Provides fallback support — The plugin can include legacy interceptors as backup automatically

Choose the setup that matches your project configuration.

#### Gradle Kotlin DSL

Root `build.gradle.kts`:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("ai.luciq.library") version "$luciqVersion" apply false
}
```

{% endcode %}

App-level `build.gradle.kts`:

{% code title="Kotlin" overflow="wrap" %}

```kotlin
plugins {
    id("luciq")
}

luciq {
    networkInterception {
        enabled = true // enables both OkHttp and UrlConnection integration, defaults to false
    }
}

dependencies {
    // app dependencies
}
```

{% endcode %}

#### Gradle Groovy DSL

Root `build.gradle`:

{% code title="Groovy" overflow="wrap" %}

```groovy
buildscript {
    dependencies {
        classpath "ai.luciq.library:luciq-plugin:$luciqVersion"
    }
}
```

{% endcode %}

App-level `build.gradle`:

{% code title="Groovy" overflow="wrap" %}

```groovy
plugins {
    id("luciq")
}

luciq {
    networkInterception {
        enabled = true // enables both OkHttp and UrlConnection integration, defaults to false
    }
}

dependencies {
    // app dependencies
}
```

{% endcode %}

#### Version Catalog (TOML)

If you're using Gradle's version catalog feature, you can manage the plugin version centrally.

`libs.versions.toml`:

{% code title="TOML" %}

```toml
[versions]
luciq = "x.y.z"

[libraries]
// app libraries here

[plugins]
luciq-plugin = { id = "ai.luciq.library", version.ref = "luciq" }
```

{% endcode %}

Root `build.gradle.kts`:

{% code title="Kotlin" %}

```kotlin
plugins {
    alias(libs.plugins.luciq.plugin) apply false
}
```

{% endcode %}

App-level `build.gradle.kts`:

{% code title="Kotlin" overflow="wrap" %}

```kotlin
plugins {
    id("luciq")
}

luciq {
    networkInterception {
        enabled = true // enables both OkHttp and UrlConnection integration, defaults to false
    }
}

dependencies {
    // app dependencies
}
```

{% endcode %}

***

### Customizing Plugin Configuration

When `networkInterception` is enabled, both OkHttp and UrlConnection automatic integration are active by default. You can customize which libraries are instrumented based on your app's needs:

{% code title="KotlinGroo" overflow="wrap" %}

```kotlin
luciq {
    networkInterception {
        enabled = true
        okHttp { okHttpConfig ->
            okHttpConfig.enabled = false // enables/disables OkHttp automatic integration, defaults to true
        }
        urlConnection { urlConnectionConfig ->
            urlConnectionConfig.enabled = false // enables/disables UrlConnection automatic integration, defaults to true
        }
    }
}
```

{% endcode %}

### Configuration for Non-APM Users

If you are not using the APM product, you can optimize your configuration by excluding legacy APM interception:

{% code title="Groovy" %}

```groovy
luciq {
    networkInterception {
        enabled = true
        okHttp { okHttpConfig ->
            okHttpConfig.legacyApmInterceptionEnabled = false
        }
        urlConnection { urlConnection ->
            urlConnection.enabled = true
            urlConnection.legacyInterceptionEnabled = false
        }
    }
}
```

{% endcode %}

{% hint style="warning" %}

### Important

Only exclude legacy APM interception if you are using the unified approach exclusively. If you are using legacy interceptors (`LuciqOkhttpInterceptor`, `LuciqAPMOkhttpInterceptor`) and exclude the APM OkHttp dependencies (`ai.luciq.library:luciq-apm-okhttp-interceptor`), your app will crash. The legacy interceptors require these dependencies to function properly.
{% endhint %}

***

### Manual Integration

If you prefer not to use the plugin or need to instrument a specific client instance (for example, when working with third-party libraries that create their own `OkHttpClient` instances), you can integrate manually.

#### OkHttp

Use the unified interceptor from `ai.luciq.library.okhttp.v2.LuciqOkHttpInterceptor` and event listener factory `ai.luciq.library.okhttp.v2.LuciqOkHttpEventListener.Factory`:

{% code title="Kotlin" %}

```kotlin
val client = OkHttpClient.Builder()
    .addInterceptor(LuciqOkHttpInterceptor())
    .eventListenerFactory(LuciqOkHttpEventListener.Factory())
    .build()
```

{% endcode %}

Using an existing EventListener.Factory:

{% code title="Kotlin" %}

```kotlin
val myEventListenerFactory: EventListener.Factory = CustomEventListener.Factory()

val client = OkHttpClient.Builder()
    .addInterceptor(LuciqOkHttpInterceptor())
    .eventListenerFactory(LuciqOkHttpEventListener.Factory(myEventListenerFactory))
    .build()
```

{% endcode %}

Recommended: Include legacy interceptors as backup:

{% code title="Kotlin" %}

```kotlin
val client = OkHttpClient.Builder()
    .addInterceptor(LuciqOkHttpInterceptor()) // new unified interceptor
    .addInterceptor(LuciqOkhttpInterceptor()) // legacy core interceptor
    .addInterceptor(LuciqAPMOkhttpInterceptor()) // legacy APM interceptor
    .eventListenerFactory(LuciqOkHttpEventListener.Factory( // new unified event listener factory
        LuciqApmOkHttpEventListener.Factory()) // legacy APM event listener factory
    ).build()
```

{% endcode %}

#### UrlConnection

UrlConnection support is packaged with the main SDK - no extra dependencies needed.

Replace `url.openConnection()` with `Luciq.openMonitoredConnection(url)`. The method returns a monitored connection if available, or falls back to the standard connection.

Before:

{% code title="Kotlin" %}

```kotlin
val url = URL("https://api.mydomain.com/")
val connection = url.openConnection()
connection.connect()
```

{% endcode %}

After:

{% code title="Kotlin" %}

```kotlin
val url = URL("https://api.mydomain.com/")
val connection = Luciq.openMonitoredConnection(url) ?: url.openConnection()
connection.connect()
```

{% endcode %}

{% hint style="info" %}

### When to use manual UrlConnection integration?

Manual integration is useful when you have specific `HttpURLConnection` instances that need monitoring, or when working with code that doesn't use the standard `URL.openConnection()` pattern. For most cases, the plugin's automatic integration is sufficient.
{% endhint %}

#### gRPC

gRPC is only supported in the APM product and currently requires manual integration. Automatic gRPC interception may be added in a future update.

Add the dependency `ai.luciq.library:luciq-grpc-interceptor`, then use `ai.luciq.library.grpc.LuciqGrpcInterceptor`:

{% code title="Kotlin" %}

```kotlin
OkHttpChannelBuilder.forAddress(address, port)
    .intercept(LuciqGrpcInterceptor())
    .build()
```

{% endcode %}

Recommended: Include legacy interceptor as backup:

{% code title="Kotlin" %}

```kotlin
OkHttpChannelBuilder.forAddress(address, port)
    .intercept(LuciqGrpcInterceptor())
    .intercept(LuciqAPMGrpcInterceptor())
    .build()
```

{% endcode %}

***

### Modifying Network Logs

You can modify network logs before they are sent to the dashboard using a centralized listener. This replaces the previous per-interceptor registration approach, making it easier to apply consistent modifications across all network logs regardless of their source.

#### Setting a Network Log Listener

Use `Luciq.setNetworkLogListener()` to register a single listener that receives all captured network logs, regardless of their source (OkHttp, UrlConnection, gRPC, or manual logging):

{% code title="Kotlin" %}

```kotlin
val listener = NetworkLogListener { snapshot ->
    // modify network log snapshot
    // For example, redact sensitive headers:
    snapshot.requestHeaders.remove("Authorization")
    snapshot
}

Luciq.setNetworkLogListener(listener)
```

{% endcode %}

{% hint style="info" %}

### Benefits of centralized modification

With the unified approach, you only need to register your modification logic once, and it applies to all network logs captured by the SDK. This eliminates the need to register separate listeners for each interceptor type.
{% endhint %}

### Migration from Legacy Approach

If you were previously registering listeners on individual interceptors, migrate to the centralized API. This simplifies your code and ensures consistent behavior.

Before (Legacy):

{% code title="Kotlin" %}

```kotlin
val listener = NetworkLogListener { snapshot ->
    // modify network log snapshot
    snapshot
}

val luciqInterceptor = LuciqOkhttpInterceptor(listener)
APM.registerNetworkLogsListener(listener)
```

{% endcode %}

After (Unified):

{% code title="Kotlin" %}

```kotlin
val listener = NetworkLogListener { snapshot ->
    // modify network log snapshot
    snapshot
}

Luciq.setNetworkLogListener(listener)
```

{% endcode %}

{% hint style="info" %}

### Returning null from the listener

You can return `null` from the `NetworkLogListener` to exclude a network log entirely from being captured. This is useful for filtering out sensitive or unnecessary requests.
{% endhint %}

***

### Important Considerations

#### Firebase Performance Monitoring

When integrating Firebase Performance Monitoring plugin with Luciq plugins, the order of plugin declaration can cause issues with Firebase UrlConnection network logs. This happens because both plugins attempt to intercept UrlConnection requests, and the order matters for proper instrumentation.

Solution: Declare Luciq plugins before Firebase:

{% code title="Kotlin" %}

```kotlin
plugins {
    id("luciq")
    id("luciq-apm")
    id("com.google.firebase.firebase-perf")
}
```

{% endcode %}

### Existing APM Plugin Integration

If you have the APM plugin already integrated, you most likely have APM network interception set up using that plugin. The new plugin setup for network interception can work fine side by side with the APM plugin, so you don't need to remove your existing configuration immediately.

However, network interception setup by the APM plugin is planned to be removed in the future. We recommend migrating to the new unified plugin integration to avoid future breaking changes and to take advantage of the simplified approach.

#### Legacy Interceptors

Deprecated legacy interception is still available but switched off by default in favor of the new unified interception. To keep using the legacy interception, contact support to turn it on for your apps. Legacy interception is planned to be removed in a future major release, so it is not recommended for new integrations.

{% hint style="warning" %}

#### Migration timeline

Legacy interceptors will be removed in a future major release. If you're currently using legacy interceptors, plan to migrate to the unified approach before that release to avoid breaking changes.
{% endhint %}

***

## Feature Comparison

| Capability                   |                   Legacy Approach |    Unified Approach |
| ---------------------------- | --------------------------------: | ------------------: |
| OkHttp support               | Separate interceptors per product |  Single interceptor |
| UrlConnection support        |                          APM only |        All products |
| gRPC support                 |                          APM only |                 APM |
| Automatic integration        |         Partial (APM plugin only) | Full (Luciq plugin) |
| Centralized log modification |                                No |                 Yes |
| Single integration point     |                                No |                 Yes |

***

## Related Documentation

* [Report Logs for Android](https://docs.luciq.ai/android/set-up-luciq-for-android/logs-and-profiling/report-logs-for-android) - Manual network logging and log types
* [Network for Android (APM)](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-network-monitoring) - APM-specific network monitoring features
* [Integrating Luciq for Android](https://docs.luciq.ai/android/set-up-luciq-for-android/integrate-luciq-on-android) - Getting started with Luciq SDK
