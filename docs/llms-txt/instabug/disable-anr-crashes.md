# Source: https://docs.instabug.com/references/crash-reporting/enable-or-disable-crash-reporting/disable-anr-crashes.md

# Disable ANR Crashes

By default, if Crash Reporting is enabled, Luciq captures any ANR that occurs within your app, along with the stack trace of the crash.

You can disable/enable ANR reporting using the following API:

{% tabs fullWidth="false" %}
{% tab title="And - Java" %}

```java
CrashReporting.setAnrState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
CrashReporting.setAnrState(Feature.State.DISABLED)
```

{% endtab %}
{% endtabs %}
