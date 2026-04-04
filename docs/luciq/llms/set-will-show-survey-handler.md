# Source: https://docs.luciq.ai/references/sdk-event-handlers/set-will-show-survey-handler.md

# Set Will-Show-Survey Handler

This handler can be used to run a block of code right before a survey is shown to the user.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Surveys.willShowSurveyHandler = {
    // Change some state
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQSurveys.willShowSurveyHandler = ^{
    // Change some state
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
Surveys.setOnShowCallback(new Runnable() {
    @Override
    public void run() {
        //Pause game
    }
});
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Surveys.setOnShowCallback(OnShowCallback {
                //Pause game
            }            
        )
```

{% endtab %}

{% tab title="RN" %}

```javascript
Surveys.setOnShowHandler(() => {
  //Perform any changes before the survey appears.
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Surveys.setOnShowCallback(Function function);
```

{% endtab %}
{% endtabs %}
