# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-in-app-surveys/survey-event-handlers.md

# Survey Event Handlers

You can execute code in a handler that gets called before a survey is shown and after it has been dismissed. You can use this for things like pausing and resuming a game, for example.

### Before showing the survey

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Surveys.willShowSurveyHandler = {
    // Change some state
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSurveys.willShowSurveyHandler = ^{
    // Change some state
};
```

{% endcode %}
{% endtab %}
{% endtabs %}

### After the survey has been dismissed

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Surveys.didFinishSurveyHandler = { (state, info, identifier) -> Void in
    // Code here
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSurveys.didFinishSurveyHandler = ^(LCQSurveyFinishedState state, NSDictionary * _Nonnull info, NSString * _Nonnull identifier) {
    // Code here
};
```

{% endcode %}
{% endtab %}
{% endtabs %}
