# Source: https://docs.luciq.ai/references/crash-reporting/enable-or-disable-crash-reporting.md

# Enable or Disable Crash Reporting

By default, crash reporting is enabled and will send crashes to your dashboard as soon as you integrate the SDK. If you would prefer to disable this feature, you can this API, and pass it a boolean to enable or disable it.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
CrashReporting.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQCrashReporting.enabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Enable
CrashReporting.setState(Feature.State.ENABLED);
// Disable
CrashReporting.setState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Enable
CrashReporting.setState(Feature.State.ENABLED)
// Disable
CrashReporting.setState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
CrashReporting.setEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```javascript
CrashReporting.setEnabled(false);
```

{% endtab %}
{% endtabs %}
