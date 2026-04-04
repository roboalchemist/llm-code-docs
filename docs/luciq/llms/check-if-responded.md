# Source: https://docs.luciq.ai/references/in-app-surveys/check-if-responded.md

# Check if Responded

You can pass a survey token to this API to check if a particular user has responded to the survey before showing it. This method takes a string token as an argument and returns a boolean.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let hasResponded = Surveys.hasRespondedToSurvey(withToken: "TOKEN")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
BOOL hasResponded = [LCQSurveys hasRespondedToSurveyWithToken:@"TOKEN"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.hasRespondToSurvey("TOKEN");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.hasRespondToSurvey("TOKEN")
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.hasRespondedToSurvey("SURVEY_TOKEN", function(hasResponded) {
  alert("Has Responded: "+hasResponded);
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
final hasResponded = Surveys.hasRespondedToSurvey("SURVEY_TOKEN");
```

{% endtab %}
{% endtabs %}
