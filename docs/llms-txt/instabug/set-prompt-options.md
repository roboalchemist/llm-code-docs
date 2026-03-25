# Source: https://docs.instabug.com/references/invocation/set-prompt-options.md

# Set Prompt Options (Disabling Features)

This API is used to change the options shown in the Luciq invocation. Any number of prompt options can be passed to this API. Only the options set will show. Below are all the possible options:

* Show the "Report a Bug" option
* Show the "Suggest an Improvement" option
* Show the "Ask a Question" option

While disabling the Bug Reporting option, removes all three of "Report a Bug", "Suggest an Improvement" and "Ask a Question", you can also set the enabled report types if you'd only like one or the other.

**Enable or Disable Feature**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
// Disable the Bugs & Feedback. If disabled, both "Report a problem" & "Suggest an improvement" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.enabled = false

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.enabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
// Disable the Bugs & Feedback. If disabled, both "Report a problem" & "Suggest an improvement" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
LCQBugReporting.enabled = NO;

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
LCQReplies.enabled = NO;
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Disable the Bugs & Feedback. If disabled, both "Report a problem" & "Suggest an improvement" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.setState(Feature.State.DISABLED);

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.setState(Feature.State.DISABLED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Disable the Bugs & Feedback. If disabled, both "Report a problem" & "Suggest an improvement" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.setState(Feature.State.DISABLED)

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.setState(Feature.State.DISABLED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
// Disable the Bugs & Feedback. If disabled, both "Report a problem" & "Suggest an improvement" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.setEnabled(true);

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.setEnabled(true);
```

{% endtab %}

{% tab title="Flutter" %}

```csharp
// Disable the Bugs, Feedback, & Questions. If disabled, "Report a problem" "Suggest an improvement" & "Ask a Question" are removed from the Luciq's prompt, and manually showing the bug reporting or feedback doesn't have an effect.
BugReporting.setEnabled(true);

// Disable the Replies. If disabled, the chats list button is removed from Luciq's prompt, the in-app notifications are disabled, and manually showing the chats list doesn't have an effect. 
Replies.setEnabled(true);
```

{% endtab %}
{% endtabs %}

**Set Enabled Report Types**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.promptOptionsEnabledReportTypes = [.bug, .feedback]
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.promptOptionsEnabledReportTypes = LCQBugReportingReportTypeBug | LCQBugReportingReportTypeFeedback;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setReportTypes(BugReporting.ReportType.ReportTypeBug, BugReporting.ReportType.ReportTypeFeedback);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setReportTypes(BugReporting.ReportType.ReportTypeBug, BugReporting.ReportType.ReportTypeFeedback)
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Arguments: chat, bug, feedback all boolean values
BugReporting.setReportTypes([BugReporting.reportType.bug, BugReporting.reportType.feedback]);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setReportTypes([ReportType.bug, ReportType.feedback, ReportType.question]);
```

{% endtab %}
{% endtabs %}

**Report Types:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Show New Bug
.bug
//Show New Feedback
.feedback
//Show New Question
.question
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Show New Bug
LCQBugReportingReportTypeBug
//Show New Feedback
LCQBugReportingReportTypeFeedback
//Show New Question
LCQBugReportingReportTypeQuestion
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Show New Bug
BugReporting.ReportType.BUG
//Show New Feedback
BugReporting.ReportType.FEEDBACK
//Show New Question
BugReporting.ReportType.QUESTION
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Show New Bug
BugReporting.ReportType.BUG
//Show New Feedback
BugReporting.ReportType.FEEDBACK
//Show New Question
BugReporting.ReportType.QUESTION
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Show New Bug
BugReporting.reportType.bug
//Show New Feedback
BugReporting.reportType.feedback
//Show New Question
BugReporting.reportType.question
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Show New Bug
BugReporting.reportType.bug
//Show New Feedback
BugReporting.reportType.feedback
//Show New Question
BugReporting.reportType.question
```

{% endtab %}
{% endtabs %}
