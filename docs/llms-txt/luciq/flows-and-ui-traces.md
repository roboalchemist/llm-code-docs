# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/flows-and-ui-traces.md

# Flows & UI Traces

### Flows (user journeys)

Start and end named flows to measure how long users spend on a journey:

{% code title="Kotlin" %}

```kotlin
APMKmp.startFlow("checkout")
// ... user goes through checkout ...
APMKmp.endFlow("checkout")
```

{% endcode %}

Add attributes to a flow for filtering or segmentation:

{% code title="Kotlin" %}

```kotlin
APMKmp.setFlowAttribute("checkout", "payment_method", "card")
APMKmp.setFlowAttribute("checkout", "discount", null)  // remove attribute
```

{% endcode %}

### UI traces

Track a named UI operation (e.g. a screen or modal):

{% code title="Kotlin" %}

```kotlin
APMKmp.startUITrace("SettingsScreen")
// ... screen is visible ...
APMKmp.endUITrace()
```

{% endcode %}

Only one UI trace is active at a time; `endUITrace()` ends the current one.

### Automatic UI traces

You can enable or disable automatic UI trace tracking:

{% code title="Kotlin" %}

```kotlin
APMKmp.setAutoUITraceEnabled(true)
```

{% endcode %}
