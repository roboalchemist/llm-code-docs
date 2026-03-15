# Source: https://docs.luciq.ai/references/bug-reporting/make-email-field-required.md

# Email and Comment Requirement (Options)

This API is to manipulate email and comment fields requirement. By default, users will be required to enter their email but the comment section will be optional. This method can take any number of arguments with the arguments being Options.

The comments section can be required for a user to send a bug and the email field can also be hidden or set to optional. Below are all the options:

* Hide email field on new bug/feedback page
* Show email field on new bug/feedback page but only optionally
* Require user to fill comment field before submitting new feedback or bug

**Method**

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.bugReportingOptions = .emailFieldOptional
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.bugReportingOptions = LCQBugReportingOptionEmailFieldOptional;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setOptions(Option.COMMENT_FIELD_REQUIRED);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setOptions(Option.COMMENT_FIELD_REQUIRED)
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setInvocationOptions([BugReporting.invocationOptions.emailFieldOptional, BugReporting.invocationOptions.commentFieldRequired]);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setInvocationOptions(InvocationOption.emailFieldOptional)
```

{% endtab %}
{% endtabs %}

**Options Parameters:**

{% tabs fullWidth="false" %}
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
//No option
.none
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Hide email
LCQBugReportingOptionEmailFieldHidden
//Show email as optional
LCQBugReportingOptionEmailFieldOptional
//Make comment required
LCQBugReportingOptionCommentFieldRequired
//Disable post sending dialog
LCQBugReportingOptionDisablePostSendingDialog
//No option
LCQBugReportingOptionNone
```

{% endtab %}

{% tab title="Android" %}

```java
//Hide email
Option.EMAIL_FIELD_HIDDEN
//Show email as optional
Option.EMAIL_FIELD_OPTIONAL
//Make comment required
Option.COMMENT_FIELD_REQUIRED
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Hide email
BugReporting.invocationOptions.emailFieldHidden
//Show email as optional
BugReporting.invocationOptions.emailFieldOptional
//Make comment required
BugReporting.invocationOptions.commentFieldRequired
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Hide email
InvocationOption.emailFieldHidden
//Show email as optional
InvocationOption.emailFieldOptional
//Make comment required
InvocationOption.commentFieldRequired
//Disable post sending dialog
InvocationOption.disablePostSendingDialog
```

{% endtab %}
{% endtabs %}
