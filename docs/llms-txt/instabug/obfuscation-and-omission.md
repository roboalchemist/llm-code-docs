# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/network-logging-ktor/obfuscation-and-omission.md

# Obfuscation & Omission

Before network data is sent to the native Luciq SDK, you can modify it (obfuscation) or prevent it from being logged (omission).

### Obfuscate logs

Use `NetworkLoggerKmp.obfuscateLog` to strip or mask sensitive data (e.g. auth headers, tokens, PII):

{% code title="Kotlin" %}

```kotlin
NetworkLoggerKmp.obfuscateLog { data ->
    data.copy(
        requestHeaders = data.requestHeaders.filterKeys { it != "Authorization" },
        requestBody = null  // or redact parts of the body
    )
}
```

{% endcode %}

The callback receives `NetworkData` and returns a modified `NetworkData`. The returned object is what gets sent to the native SDK.

### Omit logs

Use `NetworkLoggerKmp.omitLog` to skip logging for certain requests (e.g. internal or health-check endpoints):

{% code title="Kotlin" %}

```kotlin
NetworkLoggerKmp.omitLog { data ->
    data.url.contains("/internal/") || data.url.contains("/health")
}
```

{% endcode %}

If the callback returns `true`, the network call is not logged.
