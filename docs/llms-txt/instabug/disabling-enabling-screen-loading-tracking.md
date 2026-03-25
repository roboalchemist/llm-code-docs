# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-loading/disabling-enabling-screen-loading-tracking.md

# Disabling/Enabling Screen Loading Tracking

If APM is enabled, our SDK starts collecting data about your screen loading time by default. If needed, you can always toggle this on and off by updating the relevant flag after the SDK is initialized:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
APM.screenLoadingEnabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQAPM.screenLoadingEnabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}
