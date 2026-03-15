# Source: https://docs.luciq.ai/references/in-app-surveys/enable-or-disable-surveys-auto-showing.md

# Enable or Disable Auto-Showing

By default, surveys will show automatically within 10 seconds of launching the application provided the user meets the criteria required. This automatic showing of surveys can be disabled and enabled using this API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.autoShowingEnabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQSurveys.autoShowingEnabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.setAutoShowingEnabled(false);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.setAutoShowingEnabled(false)
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.setAutoShowingEnabled(false);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.setAutoShowingEnabled(false);
```

{% endtab %}
{% endtabs %}
