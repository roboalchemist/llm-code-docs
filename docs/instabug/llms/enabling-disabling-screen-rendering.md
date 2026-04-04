# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-rendering/enabling-disabling-screen-rendering.md

# Enabling/Disabling Screen Rendering

Luciq collects Screen Rendering performance metrics out of the box. If needed, you can disable it by calling the following API after initializing the SDK.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// Disable Screen Rendering
APM.screenRenderingEnabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// Disable Scren Rendering
LCQAPM.screenRenderingEnabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}
