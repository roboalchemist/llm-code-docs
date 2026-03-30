# Source: https://docs.luciq.ai/references/in-app-surveys/show-survey-welcome-message.md

# Show Survey Welcome Message

Any survey usually starts off getting straight to the point. You can have the survey instead start with a simple welcome message. To enable the welcome message, you can use this API.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.shouldShowWelcomeScreen = true
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQSurveys.shouldShowWelcomeScreen = YES;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.setShouldShowWelcomeScreen(true);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.setShouldShowWelcomeScreen(true);
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.setShouldShowWelcomeScreen(true);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.setShouldShowWelcomeScreen(true);
```

{% endtab %}
{% endtabs %}
