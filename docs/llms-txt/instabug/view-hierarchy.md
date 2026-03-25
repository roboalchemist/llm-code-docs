# Source: https://docs.instabug.com/references/report-data/view-hierarchy.md

# View Hierarchy

View Hierarchy is disabled by default; however, if you would like to have it enabled, you can do so by adding the API found below.

This feature gives you the ability to visually inspect each layer in your app and see all the properties and constraints of each subview so you can spot errors at a glance. This helps out in the process of finding the problem and fixing it faster. Any editable text or text fields will automatically be replaced with asterisks.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.shouldCaptureViewHierarchy = true
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.shouldCaptureViewHierarchy = YES;
```

{% endtab %}

{% tab title="And - Java" %}

```java
new Luciq.Builder(this, "APP_TOKEN")
    .setViewHierarchyState(Feature.State.ENABLED)
    .build();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.Builder(this, "c626fd74f74eb721f1ab9c41478cf46f")
            .setViewHierarchyState(Feature.State.DISABLED)
            .build()
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setViewHierarchyEnabled(true);
```

{% endtab %}
{% endtabs %}

*Example: If you receive a report that a certain UI view is missing, you can use View Hierarchy to easily discover if the missing view is hidden behind a higher layer, out of the parent view's bounds, or missing from the window.*
