# Source: https://docs.instabug.com/references/application-performance-monitoring/enable-or-disable-fragments.md

# Enable or Disable Fragment Capture

> 🚧 Capturing Fragments
>
> Luciq does not capture fragments by default. In order to start capturing them, you'll need to follow the instructions mentioned [here](https://docs.luciq.ai/docs/android-apm-instrumentation#fragments).

If your app is set up to capture fragments with Luciq, you can enable or disable this feature by using the API below, passing a `Boolean` variable to it:

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
//Enable
APM.setFragmentSpansEnabled(true)
//Disble
APM.setFragmentSpansEnabled(false)
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Enable
APM.setFragmentSpansEnabled(true)
//Disble
APM.setFragmentSpansEnabled(false)
```

{% endtab %}
{% endtabs %}
