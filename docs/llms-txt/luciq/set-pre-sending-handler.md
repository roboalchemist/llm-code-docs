# Source: https://docs.luciq.ai/references/sdk-event-handlers/set-pre-sending-handler.md

# Set Pre-Sending Handler

Use this handler to run any code right before sending a bug or crash report

This block is executed in the background before sending each report and could be used for attaching logs and extra data to reports, for example.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

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

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.willSendReportHandler = ^LCQReport * _Nonnull(LCQReport * _Nonnull report) {
    [report appendTag:@"tag1"];
    [report logVerbose:@"Verbose log."];
    [report appendToConsoleLogs:@"Console log statement"];
    [report setUserAttribute:@"value" withKey:@"key"];

    return report;
};
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.onReportSubmitHandler(new Report.OnReportCreatedListener() {
            @Override
            public void onReportCreated(Report report) {
                
            }
        });
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.onReportSubmitHandler{report -> }
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.onReportSubmitHandler((report) => {
    // Attach logs and extra data to reports.
});
```

{% endtab %}
{% endtabs %}
