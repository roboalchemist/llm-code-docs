# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/network-logging-ktor.md

# Network Logging (Ktor)

The Luciq KMP library provides automatic network logging for **Ktor HttpClient**: it intercepts requests and responses, injects W3C trace headers for distributed tracing, and sends logs to the native Luciq SDK for bug reports and APMKmp.

### Install the plugin

Add the plugin to your `HttpClient`:

{% code title="Kotlin" %}

```kotlin
import ai.luciq.kmp.interceptors.LuciqKtorPlugin

val client = HttpClient(Engine) {
    install(LuciqKtorPlugin)
}
```

{% endcode %}

All requests made with this client are logged (URL, method, headers, body, timing, status). The plugin also injects a W3C `traceparent` header when the native SDK supports it.

### How it works

1. **Request**: The plugin captures URL, method, headers, and body, and may add a `traceparent` header.
2. **Response**: It captures status, headers, and body, computes duration, and sends a `NetworkData` record to the native SDK via `NetworkLoggerKmp.networkLog`.
3. **Errors**: Failed requests are logged with error domain and message.

Body size may be truncated by the native SDK. Obfuscation and omission callbacks (see [Obfuscation & Omission](https://docs.luciq.ai/kmp/setup-luciq-for-kmp/network-logging-ktor/obfuscation-and-omission)) are applied before sending to the native SDK.

### Manual logging

If you use another HTTP client, build a `NetworkData` instance and call:

{% code title="Kotlin" %}

```kotlin
scope.launch {
    NetworkLoggerKmp.networkLog(networkData)
}
```

{% endcode %}

You can get a W3C header for your request with:

{% code title="Kotlin" %}

```kotlin
val header = NetworkLoggerKmp.getW3CHeaderForRequest(requestHeaders, startTime)
// Attach header to your request
```

{% endcode %}

### Body and auto-masking

{% code title="Kotlin" %}

```kotlin
NetworkLoggerKmp.setNetworkLogBodyEnabled(true)
NetworkLoggerKmp.setNetworkAutoMaskingEnabled(true)
```

{% endcode %}

* [Obfuscation & Omission](https://docs.luciq.ai/kmp/setup-luciq-for-kmp/network-logging-ktor/obfuscation-and-omission) – Remove or mask sensitive data and skip certain requests
