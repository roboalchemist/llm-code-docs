# Source: https://docs.instabug.com/references/report-data/logging/user-steps.md

# User Steps

By default, user steps are collected by the SDK. These are all the steps the user has done up to the latest report. This feature can be disabled using this API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.trackUserSteps = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.trackUserSteps = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setTrackingUserStepsState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setTrackingUserStepsState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.setTrackUserSteps(false);
```

{% endtab %}
{% endtabs %}
