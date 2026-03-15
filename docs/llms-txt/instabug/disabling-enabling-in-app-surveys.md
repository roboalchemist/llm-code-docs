# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-in-app-surveys/disabling-enabling-in-app-surveys.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-in-app-surveys/disabling-enabling-in-app-surveys.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-in-app-surveys/disabling-enabling-in-app-surveys.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/setup-in-app-surveys/disabling-enabling-in-app-surveys.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-in-app-surveys/disabling-enabling-in-app-surveys.md

# Disabling/Enabling In-App Surveys

You can completely disable any surveys from being shown to your app users with the following API. Please note that this also disables manually shown surveys, as this method disables any request related to surveys.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Surveys.enabled = false;
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQSurveys setEnabled:YES];
```

{% endcode %}
{% endtab %}
{% endtabs %}
