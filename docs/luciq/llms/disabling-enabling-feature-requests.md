# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/in-app-feature-requests/disabling-enabling-feature-requests.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-feature-requests/disabling-enabling-feature-requests.md

# Disabling/Enabling Feature Requests

You can completely prevent any feature request related features from displaying by disabling it using the API below.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
//Enable
FeatureRequests.enabled = true

//Disable
FeatureRequests.enabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
//Enable
LCQFeatureRequests.enabled = YES;

//Disable
LCQFeatureRequests.enabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}
