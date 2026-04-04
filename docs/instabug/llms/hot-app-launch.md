# Source: https://docs.instabug.com/references/application-performance-monitoring/app-launch/hot-app-launch.md

# Hot App Launch

Luciq automatically captures your hot app launch latency.; however, you can disable it using the following APIs.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
// Disable
APM.hotAppLaunchEnabled = false

// Enable
APM.hotAppLaunchEnabled = true
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
// Disable
LCQAPM.hotAppLaunchEnabled = NO;

// Enable
LCQAPM.hotAppLaunchEnabled = YES;
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.setHotAppLaunchEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.setHotAppLaunchEnabled(false)
```

{% endtab %}
{% endtabs %}
