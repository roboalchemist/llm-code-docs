# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-bug-reporting/set-up-proactive-reporting.md

# Set up Proactive Reporting

### Enabling Proactive Reporting

By default, the Proactive Reporting is disabled. You can use the below API to:

* Enable/disable the feature.
* Configure the gap between two pop-ups for the same user.
* Configure the gap between the app launch and the first pop-up.

{% hint style="info" %}
The gap calculation starts when our SDK detects a Force Restart or a Crash occurrence, usually a few milliseconds after the launch.
{% endhint %}

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
ProactiveReportingConfigs configs = new ProactiveReportingConfigs.Builder()
                .setGapBetweenModals(24) // Time in seconds
                .setModalDelayAfterDetection(20) // Time in seconds
                .isEnabled(true) //Enable/disable
                .build();

        BugReporting.setProactiveReportingConfigurations(configs);
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
val configurations = ProactiveReportingConfigs.Builder() 
                      .isEnabled(true) //Enable/disable
                      .setGapBetweenModals(24) // Time in seconds
                      .setModalDelayAfterDetection(30) // Time in seconds
                      .build() 
BugReporting.setProactiveReportingConfigurations(configurations)
```

{% endcode %}
{% endtab %}
{% endtabs %}
