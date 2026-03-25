# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-application-performance-monitoring/disabling-enabling-apm.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-application-performance-monitoring/disabling-enabling-apm.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-application-performance-monitoring/disabling-enabling-apm.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-application-performance-monitoring/disabling-enabling-apm.md

# Disabling/Enabling APM

You can disable APM by calling the following API right after initializing the SDK. This completely prevents the SDK from collecting any performance data or executing any APM related logic:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
APM.enabled = true
APM.enabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQAPM.enabled = YES;
LCQAPM.enabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Please note that disabling APM will also clear any data that has already been collected and stored on your users' devices but hasn't been synced to our servers yet.
{% endhint %}
