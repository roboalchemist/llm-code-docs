# Source: https://docs.instabug.com/references/application-performance-monitoring/custom-traces/addedit-attribute.md

# Add/Edit Attribute

You can add/edit a custom attribute using the following APIs, passing a `string` key and a `string` value.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
// Add custom attributes to an existing trace
trace?.setAttributeWithKey("key", value: "value")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
// Add custom attributes to an existing trace
[trace setAttributeWithKey:@"key" value:@"value"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Add custom attributes to an existing trace
trace.setAttribute("key", "value");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Add custom attributes to an existing trace
trace?.setAttribute("key", "value")
```

{% endtab %}

{% tab title="RN" %}

```javascript
// Add custom attributes to an existing trace
trace.setAttribute('key', 'value')
```

{% endtab %}

{% tab title="Flutter" %}

```javascript
// Add custom attributes to an existing trace
trace.setAttribute('key', 'value')
```

{% endtab %}
{% endtabs %}
