# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-bug-reporting/disabling-enabling-bug-reporting.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-bug-reporting/disabling-enabling-bug-reporting.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-bug-reporting/disabling-enabling-bug-reporting.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-bug-reporting/disabling-enabling-bug-reporting.md

# Disabling/Enabling Bug Reporting

When your users [invoke the SDK](https://docs.luciq.ai/ios/setup-luciq-for-ios/showing-luciq#invocation-events), a popup appears with default [Prompt Options](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/sdk-customization/prompt-options) for them to "Report a bug" (submit a bug), "Suggest an improvement" (send you feedback), or "Ask a question" (send you a chat).

These options can be disabled or enabled separately. When only a single option is enabled, it becomes the default [invocation mode](https://docs.luciq.ai/ios/setup-luciq-for-ios/showing-luciq#invocation-events) and the Prompt Options menu doesn't appear.

The below API completely disables all forms of bug, improvement, and question reports.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
BugReporting.enabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQBugReporting.enabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can also specify whether to show any of the Report a bug, Suggest an improvement, Ask a question options, or all using this API:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// Specify which of the feedback or bug options appear in the prompt options
BugReporting.promptOptionsEnabledReportTypes = [.bug, .feedback, .question]
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// Specify which of the feedback or bug options appear in the prompt options
LCQBugReporting.promptOptionsEnabledReportTypes = LCQBugReportingReportTypeBug | LCQBugReportingReportTypeFeedback | LCQBugReportingReportTypeQuestion;
```

{% endcode %}
{% endtab %}
{% endtabs %}

By default, all three options are enabled if they are available in your current subscription plan.
