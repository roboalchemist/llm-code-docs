# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/custom-settings/sdk-customization/prompt-options.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/custom-settings/sdk-customization/prompt-options.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/custom-settings/sdk-customization/prompt-options.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/sdk-customizations/prompt-options.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/sdk-customization/prompt-options.md

# Prompt Options

By default, when the Luciq SDK is shown, a popup appears to your app users with options for them to report a bug ("Report a bug"), share feedback ("Suggest an improvement"), or ask you a question ("Ask a question"). This popup is called the Prompt Options.

All Luciq popups follow the color theme and primary color that you set for the SDK.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2F0uZ8pqZORzjF1IrOVKTs%2Fimage.png?alt=media&#x26;token=16d9b752-e52a-4bfb-ac16-de6918f2903c" alt=""><figcaption><p><br><em>An example of the Prompt Options menu that appears to app users after Luciq is invoked.</em></p></figcaption></figure>

By default, all of your enabled products are listed in the Prompt Options menu. You can control which options appear by disabling and enabling any of the products. Each one can be enabled or disabled separately.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// Disable the Bugs, Feedback, & Questions. If disabled, "Report a problem" "Suggest an improvement" & "Ask a Question" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.enabled = false

// Specify which of the feedback, bug, or question options appear in the prompt options
BugReporting.promptOptionsEnabledReportTypes = [.bug, .feedback, .question]

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.enabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// Disable the Bugs & Feedback. If disabled, "Report a problem" "Suggest an improvement" & "Ask a Question" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
LCQBugReporting.enabled = NO;

// Specify which of the feedback or bug options appear in the prompt options
LCQBugReporting.promptOptionsEnabledReportTypes = LCQBugReportingReportTypeBug | LCQBugReportingReportTypeFeedback | LCQBugReportingReportTypeQuestion;

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
LCQReplies.enabled = NO;
```

{% endcode %}
{% endtab %}
{% endtabs %}

When only a single option is enabled, it becomes the default invocation mode. If all options are disabled, bug reporting becomes the default invocation mode and the Prompt Options menu won't appear to your users. Instead, they will be shown the bug reporting form.

By default, all three options are enabled if they are available in your current plan.
