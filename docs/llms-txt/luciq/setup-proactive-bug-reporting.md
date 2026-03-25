# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-bug-reporting/setup-proactive-bug-reporting.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-bug-reporting/setup-proactive-bug-reporting.md

# Setup Proactive Bug Reporting

### Enabling Proactive Reporting

By default, the Proactive Reporting is disabled. You can use the below API to:

* Enable/disable the feature.
* Configure the gap between two pop-ups for the same user.
* Configure the gap between the app launch and the first pop-up.

{% hint style="info" %}
The gap calculation starts when our SDK detects a Force Restart or a Crash occurrence, usually a few milliseconds after the launch.
{% endhint %}

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let configurations = ProactiveReportingConfigurations()
configurations.enabled = true //Enable/disable
configurations.gapBetweenModals = 2 // Time in seconds
configurations.modalDelayAfterDetection = 60 // Time in seconds
BugReporting.setProactiveReportingConfigurations(configurations)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
   LCQProactiveReportingConfigurations *configurations = [[LCQProactiveReportingConfigurations alloc] init];
    configurations.enabled = YES; //Enable/disable
    configurations.gapBetweenModals = @2; // Time in seconds
    configurations.modalDelayAfterDetection = @60; // Time in seconds
  [LCQBugReporting setProactiveReportingConfigurations:configurations];
```

{% endcode %}
{% endtab %}
{% endtabs %}
