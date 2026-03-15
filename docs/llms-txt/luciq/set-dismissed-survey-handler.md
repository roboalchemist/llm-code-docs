# Source: https://docs.luciq.ai/references/sdk-event-handlers/set-dismissed-survey-handler.md

# Set Dismissed-Survey Handler

This handler can be used to run a block code right after a survey is dismissed.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.didFinishSurveyHandler = { (state, info, identifier) -> Void in
    // Code here
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQSurveys.didFinishSurveyHandler = ^(LCQSurveyFinishedState state, NSDictionary * _Nonnull info, NSString * _Nonnull identifier) {
    // Code here
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.setOnFinishCallback(new OnFinishCallback() {
            @Override
            public void onFinish(String surveyId, String state, JSONObject response) {
            }
        });
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.setOnFinishCallback(OnFinishCallback {
            }
        )
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.setOnDismissHandler(() => {
  //Perform any changes before the survey disappears.
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.setOnDismissCallback(Function function);
```

{% endtab %}
{% endtabs %}
