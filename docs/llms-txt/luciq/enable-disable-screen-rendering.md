# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-screen-rendering/enable-disable-screen-rendering.md

# Enable/Disable Screen Rendering

Luciq collects Screen Rendering performance metrics out of the box. If needed, you can disable it by calling the following API after initializing the SDK.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
// Enable/disable Screen Rendering
APM.setScreenRenderingEnabled(enabled:Boolean)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
// Enable/disable Screen Rendering
APM.setScreenRenderingEnabled(boolean enabled);
```

{% endcode %}
{% endtab %}
{% endtabs %}
