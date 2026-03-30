# Source: https://docs.luciq.ai/references/in-app-surveys/manually-show-survey.md

# Manually Show Survey

If you created a survey on the dashboard that you use to manually target users, you'll be provided with a token. You can pass this token to the show survey API to manually show it at anytime.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.showSurvey(withToken: "TOKEN")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQSurveys showSurveyWithToken:@"TOKEN"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.showSurvey("TOKEN");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.showSurvey("TOKEN")
```

{% endtab %}

{% tab title="RN" %}

```java
Surveys.showSurvey("TOKEN");
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.showSurvey("TOKEN");
```

{% endtab %}
{% endtabs %}
