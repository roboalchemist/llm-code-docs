# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-bug-reporting/bug-reporting-callbacks.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-bug-reporting/bug-reporting-callbacks.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-bug-reporting/bug-reporting-callbacks.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-bug-reporting/bug-reporting-callbacks.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-bug-reporting/bug-reporting-callbacks.md

# Bug Reporting Callbacks

### Before Invoking Luciq

This block is executed on the UI thread. You can use it to perform any UI changes before the SDK's UI is shown.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
BugReporting.willInvokeHandler = {
    someObject.setSomeState()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQBugReporting.willInvokeHandler = ^{
    [someObject setSomeState];
};
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Before Sending a Report

This block is executed in the background before sending each report. You can use it to attach logs and extra data to reports. You can also use this API to run some logic after the bug is reported and before it gets synced with the backend in case you need to access some data to take specific actions.

**Data Available**: tags, luciqLogs, consoleLogs, userAttributes, fileLocations, userData

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.willSendReportHandler = { report in
    report.appendTag("tag1")
    report.logVerbose("Verbose log.")
    report.append(toConsoleLogs: "Console log statement.")
    report.setUserAttribute("value", withKey: "key")
    let data = "Data".data(using: .utf8)
    report.addFileAttachment(with: data)
    
    return report
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
Luciq.willSendReportHandler = ^LCQReport * _Nonnull(LCQReport * _Nonnull report) {
    [report appendTag:@"tag1"];
    [report logVerbose:@"Verbose log."];
    [report appendToConsoleLogs:@"Console log statement"];
    [report setUserAttribute:@"value" withKey:@"key"];

    return report;
};
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
By writing `report.` in the Event Handler, the IDE autocomplete feature will show all of the mentioned operations that you can do or access on the report automatically.
{% endhint %}

### After Dismissing Luciq

This block is executed on the UI thread. You can use it to perform any UI changes after the SDK's UI has been dismissed.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
BugReporting.didDismissHandler = { (SDKDismissType, ReportCategory) in
    someObject.setSomeState()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQBugReporting.didDismissHandler = ^(LCQDismissType dismissType, LCQReportCategory reportType) {
    [someObject setSomeState];
};
```

{% endcode %}
{% endtab %}
{% endtabs %}

The `didDismissHandler` block has the following parameters:

#### `LCQDismissType`

Returns how the SDK was dismissed. It can be set to one of the three following possibilities:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
//Indicates that the issue was submitted and will be uploaded
submit
//Indicates that the user closed the Luciq view without report submission  
cancel
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
//Indicates that the issue was submitted and will be uploaded
LCQDismissTypeSubmit
//Indicates that the user closed the Luciq view without report submission  
LCQDismissTypeCancel
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### `LCQReportCategory`

The type of report that was sent. If the SDK was dismissed without selecting a report type, it will be set to `LCQReportCategoryBug`, so you might need to check `issueState` before `LCQReportCategory`. The possible different types are below:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
bug
feedback
question
other
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQReportCategoryBug
LCQReportCategoryFeedback
LCQReportCategoryQuestion
LCQReportCategoryOther
```

{% endcode %}
{% endtab %}
{% endtabs %}
