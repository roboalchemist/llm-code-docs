# Source: https://docs.luciq.ai/references/application-performance-monitoring/app-launch/cold-app-launch.md

# Cold App Launch

Luciq automatically captures your cold app launch latency; however, you can disable it using the following APIs.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
// Disable
APM.coldAppLaunchEnabled = false
// Enable
APM.coldAppLaunchEnabled = true
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
// Disable
LCQAPM.coldAppLaunchEnabled = NO;
// Enable
LCQAPM.coldAppLaunchEnabled = YES;
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.setColdAppLaunchEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.setColdAppLaunchEnabled(false)
```

{% endtab %}
{% endtabs %}
