# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-bug-reporting/setup-proactive-reporting.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-bug-reporting/setup-proactive-reporting.md

# Setup Proactive Reporting

### Enabling Proactive Reporting

By default, Proactive Reporting is disabled. You can use the API below to:

* Enable/disable the feature.
* Configure the gap between two pop-ups for the same user.
* Configure the gap between the app launch and the first pop-up.

The gap calculation starts when our SDK detects a Force Restart or a Crash occurrence, usually a few milliseconds after the launch.

{% code title="Dart" %}

```dart
BugReporting.setProactiveReportingConfigurations(
  const ProactiveReportingConfigs(
    enabled: true,
    gapBetweenModals: 2, // time in seconds
    modalDelayAfterDetection: 2, // time in seconds
  ),
);
```

{% endcode %}
