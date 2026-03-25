# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/screen-loading-and-rendering.md

# Screen Loading & Rendering

### Screen loading

When enabled, the SDK automatically tracks screen loading times:

{% code title="Kotlin" %}

```kotlin
APMKmp.setScreenLoadingEnabled(true)
```

{% endcode %}

### Screen rendering

When enabled, the SDK tracks screen rendering metrics:

{% code title="Kotlin" %}

```kotlin
APMKmp.setScreenRenderingEnabled(true)
```

{% endcode %}

Behavior and availability may vary by platform; the native Luciq SDK drives the actual metrics.
