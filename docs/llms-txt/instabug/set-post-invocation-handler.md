# Source: https://docs.instabug.com/references/sdk-event-handlers/set-post-invocation-handler.md

# Set Did-Dismiss Handler

Use this handler to run any code right after the Luciq view is dismissed.

This block is executed on the UI thread. Could be used for performing any UI changes after the SDK's UI has been dismissed.

For **iOS**:\
The `didDismissHandler` block has the following

* `LCQDismissType`: How the SDK was dismissed.
* `LCQReportCategory`: Type of report that has been sent. Will be set to `LCQReportCategoryBug` in case the SDK has been dismissed without selecting a report type, so you might need to check `issueState` before `LCQReportCategory`.

For **Android**:\
The `setOnDismissCallback` block has the following

* `DismissType`: How the SDK was dismissed.
* `ReportType`: The type of report that was sent. If the SDK was dismissed without selecting a report type, it will be set to bug, so you might need to check `issueState` before `reportType`.

For **React Native**:\
The `onSDKDismissedHandler` block has the following

* `dismissType`: How the SDK was dismissed.
* `reportType`: The type of report that was sent. If the SDK was dismissed without selecting a report type, it will be set to bug, so you might need to check `issueState` before `reportType`.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.didDismissHandler = { (dismissType, reportType) in
    someObject.setSomeState()
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.didDismissHandler = ^(LCQDismissType dismissType, LCQReportType reportType) {
    [someObject setSomeState];
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setOnDismissCallback(new OnSdkDismissCallback() {
            @Override
            public void call(DismissType issueState, ReportType reportType) {
                
            }
        });
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setOnDismissCallback { issueState, reportType -> }
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.onSDKDismissedHandler(function (dismissType, reportType) {
    // Perform any UI changes after the SDK's UI has been dismissed.
});
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setOnDismissCallback(Function function);
```

{% endtab %}
{% endtabs %}
