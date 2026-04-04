# Source: https://docs.instabug.com/references/application-performance-monitoring/ui-hangs/start-ui-trace.md

# Start UI Trace

Use the following APIs to start a custom UI trace while passing a `string` that defines the name of the trace.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.startUITrace(withName: "name")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQAPM startUITraceWithName:@"name"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Start UI Trace
APM.startUITrace("name");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Start UI Trace
APM.startUITrace("name")
```

{% endtab %}

{% tab title="RN" %}

```javascript
APM.startUITrace("name");
```

{% endtab %}

{% tab title="Flutter" %}

```javascript
APM.startUITrace('trace_name');
```

{% endtab %}
{% endtabs %}
