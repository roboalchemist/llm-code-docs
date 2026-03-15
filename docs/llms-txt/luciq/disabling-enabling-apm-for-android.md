# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/disabling-enabling-apm-for-android.md

# Disabling/Enabling APM for Android

You can disable APM by calling the following API right after initializing the SDK. This completely prevents the SDK from collecting any performance data or executing any APM related logic:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
// Enable/disable APM
APM.setEnabled(true)
APM.setEnabled(false)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
// Enable/disable APM
APM.setEnabled(true);
APM.setEnabled(false);
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Please note that disabling APM will also clear any data that has already been collected and stored on your users' devices but hasn't been synced to our servers yet.
{% endhint %}
