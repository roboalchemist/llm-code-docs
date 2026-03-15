# Source: https://docs.instabug.com/references/application-performance-monitoring/app-launch/warm-app-launch.md

# Warm App Launch

Luciq automatically captures your warm app launch latency; however, you can disable it using the following APIs.

{% tabs fullWidth="true" %}
{% tab title="And - Java" %}

```java
// Disable
APM.setWarmAppLaunchEnabled(false);

// Enable
APM.setWarmAppLaunchEnabled(true);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Disable
APM.setColdAppLaunchEnabled(false)
  
//Enable
APM.setWarmAppLaunchEnabled(true)
```

{% endtab %}
{% endtabs %}
