# Source: https://docs.luciq.ai/references/application-performance-monitoring/ui-hangs/enable-or-disable-auto-ui-trace.md

# Enable or Disable Auto UI Trace

Luciq collects UI hangs out of the box. You can disable/enable this using the following API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.setAutoUITraceEnabled(true)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQAPM.UIHangsEnabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
APM.setUIHangEnabled(boolean disabled);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.setUIHangEnabled(boolean disabled)
```

{% endtab %}

{% tab title="RN" %}

```javascript
// Enable
APM.setAutoUITraceEnabled(true);

// Disable
APM.setAutoUITraceEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```javascript
// Enable Auto UI Traces
APM.setAutoUITraceEnabled(true);

// Disable Auto UI Traces
APM.setAutoUITraceEnabled(false);
```

{% endtab %}
{% endtabs %}
