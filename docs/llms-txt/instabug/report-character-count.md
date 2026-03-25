# Source: https://docs.instabug.com/references/bug-reporting/report-character-count.md

# Minimum Report Character Count

Using the API below, you can set the minimum number of characters your user can input within the comment field whenever our SDK is invoked. This API takes the report type and an integer limit as its parameters.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Report types are optional
BugReporting.setCommentMinimumCharacterCountForReportTypes([.bug, .feedback, .question], withLimit:3)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Report types are optional
[LCQBugReporting setCommentMinimumCharacterCountForReportTypes:LCQBugReportingReportTypeBug | LCQBugReportingReportTypeFeedback | LCQBugReportingReportTypeQuestion withLimit:3];
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setCommentMinimumCharacterCount(20, ReportType.BUG, ReportType.FEEDBACK, ReportType.QUESTION);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setCommentMinimumCharacterCount(20, ReportType.BUG, ReportType.FEEDBACK, ReportType.QUESTION)
```

{% endtab %}

{% tab title="RN" %}

```javascript
// All report types
BugReporting.setCommentMinimumCharacterCount(20);

// Specific reports
BugReporting.setCommentMinimumCharacterCount(20, [
   BugReporting.reportType.bug,
   BugReporting.reportType.feedback,
   BugReporting.reportType.question
]);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
// For all report types
BugReporting.setCommentMinimumCharacterCount(20);

// For specific report types
BugReporting.setCommentMinimumCharacterCount(20, [ReportType.bug, ReportType.feedback, ReportType.question]);
```

{% endtab %}
{% endtabs %}

**Report Type Parameters**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
.bug
.feedback
.question
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReportingReportTypeBug
LCQBugReportingReportTypeFeedback
LCQBugReportingReportTypeQuestion
```

{% endtab %}

{% tab title="Android" %}

```java
ReportType.BUG
ReportType.FEEDBACK
ReportType.QUESTION
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.reportType.bug
BugReporting.reportType.feedback
BugReporting.reportType.question
```

{% endtab %}

{% tab title="Flutter" %}

```dart
ReportType.bug
ReportType.feedback
ReportType.question
```

{% endtab %}
{% endtabs %}
