# Source: https://docs.luciq.ai/references/invocation/index/invoke-with-mode.md

# Show Specific Mode

You can show Luciq with a specific mode and option directly using these APIs. If you're showing a bug reporting mode specifically, the API has two fields, **Report Type** and **Option**.

All the possible invocation modes are listed to the right. These modes can be used to show a specific view right away. The possible modes are:

* Show New Bug Page
* Show New Feedback Page
* Show New Chat Page
* Show Chats List Page

Here are all the possible invocation options used to customize the new bug or feedback experience.

* Hide email field on new bug/feedback page
* Show email field on new bug/feedback page but only optionally
* Require user to fill comment field before submitting new feedback or bug

You can pass any number of invocation options in a single method call. If no invocation option is passed, the email field will automatically be shown and set to required and the comment field will be set to optional.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
// Compose a new bug report
BugReporting.show(with: .bug, options: [])
// Compose a new feedback
BugReporting.show(with: .feedback, options: [])
// Compose a new question
BugReporting.show(with: .question, options: [])
// Show the perevious chats list
Replies.show()
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
// Compose a new bug report
[LCQBugReporting showWithReportType:LCQBugReportingReportTypeBug options:0];
// Compose a new feedback
[LCQBugReporting showWithReportType:LCQBugReportingReportTypeFeedback options:0];
// Compose a new question
[LCQBugReporting showWithReportType:LCQBugReportingReportTypeQuestion options:0];
// Show the perevious chats list only of the the user already have a chats history. Calling this API won't have an effect otherwise.
[LCQReplies show];
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Compose a new bug report
BugReporting.show(BugReporting.ReportType.BUG);
// Compose a new feedback
BugReporting.show(BugReporting.ReportType.FEEDBACK);
// Compose a new question
BugReporting.show(BugReporting.ReportType.QUESTION);
// Show the perevious chats list
Replies.show();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Compose a new bug report
BugReporting.show(BugReporting.ReportType.BUG)
// Compose a new feedback
BugReporting.show(BugReporting.ReportType.FEEDBACK)
// Compose a new question
BugReporting.show(BugReporting.ReportType.QUESTION)
// Show the perevious chats list
Replies.show()
```

{% endtab %}

{% tab title="RN" %}

```javascript
import { ReportType, InvocationOption } from '@luciq/react-native';

// Compose a new bug report
BugReporting.show(ReportType.bug, [InvocationOption.emailFieldHidden]);
// Compose a new feedback
BugReporting.show(ReportType.feedback, [InvocationOption.emailFieldOptional]);
// Compose a new question
BugReporting.show(ReportType.question, [InvocationOption.emailFieldOptional]);
// Show the previous chats list
Replies.show();
```

{% endtab %}

{% tab title="Flutter" %}

```csharp
// Compose a new bug report
BugReporting.showWithOptions(BugReporting.reportType.bug, [BugReporting.option.emailFieldHidden]);
// Compose new feedback
BugReporting.showWithOptions(BugReporting.reportType.feedback, [BugReporting.option.emailFieldOptional]);
// Compose a new question
BugReporting.showWithOptions(BugReporting.reportType.question, [BugReporting.option.emailFieldOptional]);
// Show the previous chats list
Replies.show();
```

{% endtab %}
{% endtabs %}

**Report Type Parameters:**

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
ReportType.bug
//Show New Feedback
ReportType.feedback
//Show New Question
ReportType.question
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

**Option Parameters:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Hide email
.emailFieldHidden
//Show email as optional
.emailFieldOptional
//Make comment required
.commentFieldRequired
//Disable post sending dialog
.disablePostSendingDialog
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Hide email
LCQBugReportingInvocationOptionEmailFieldHidden
//Show email as optional
LCQBugReportingInvocationOptionEmailFieldOptional
//Make comment required
LCQBugReportingInvocationOptionCommentFieldRequired
//Disable post sending dialog
LCQBugReportingInvocationOptionDisablePostSendingDialog
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Hide email
EMAIL_FIELD_HIDDEN
//Show email as optional
EMAIL_FIELD_OPTIONAL
//Make comment required
COMMENT_FIELD_REQUIRED
//No post sending dialog
DISABLE_POST_SENDING_DIALOG
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Hide email
EMAIL_FIELD_HIDDEN
//Show email as optional
EMAIL_FIELD_OPTIONAL
//Make comment required
COMMENT_FIELD_REQUIRED
//No post sending dialog
DISABLE_POST_SENDING_DIALOG
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Hide email
InvocationOption.emailFieldHidden;
//Show email as optional
InvocationOption.emailFieldOptional;
//Make comment required
InvocationOption.commentFieldRequired;
//No post sending dialog
InvocationOption.disablePostSendingDialog;
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Hide email
BugReporting.option.emailFieldHidden
//Show email as optional
BugReporting.option.emailFieldOptional
//Make comment required
BugReporting.option.commentFieldRequired;
//No post sending dialog
BugReporting.option.disablePostSendingDialog;
```

{% endtab %}
{% endtabs %}
