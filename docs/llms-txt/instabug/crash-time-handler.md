# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-crash-reporting/crash-time-handler.md

# Crash-Time Handler

#### Set Custom Values Before Sending a Crash

When an application crashes, details about the app’s runtime state are gathered and prepared for submission to Luciq on the next launch. However, what if you want to run some code after generating the report? This is where the `onCrashHandler` kicks in.

The `onCrashHandler` hook enables you to run custom code after the crash report has been generated. The information then becomes accessible in the **“User Data”** section of the dashboard after the next launch, during the `didSendCrashReportHandler` phase.

The callback is executing at crash-time, it must be async safe, which means that Objective-C code cannot be used. A C function can be registered

Here's an example of the code to be called on a crashing session:

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
void onCrashedHandler(LCQCrashReportWriter *writer) {
    writer->addUIntegerElement(writer, "total_memory", [NSProcessInfo processInfo].physicalMemory);
    CFTimeInterval timeInSeconds = CFAbsoluteTimeGetCurrent() + kCFAbsoluteTimeIntervalSince1970;
    writer->addUIntegerElement(writer, "timestamp", (unsigned long)timeInSeconds);
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

It should also be set in the Luciq's Crash Reporter:

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQCrashReporting setOnCrashHandler:onCrashedHandler];
```

{% endcode %}
{% endtab %}

{% tab title="Swift" %}

```swift
LCQCrashReporting.onCrashHandler = onCrashedHandler
```

{% endtab %}
{% endtabs %}

#### Checking if the Last Session Crashed

If you want to check whether the last session was a crashing session, you can use the following API. This API returns a boolean value indicating whether the app crashed in the previous session.

```
LCQCrashReporting.didLastSessionCrash
```

This property is particularly useful if you need to take specific actions based on whether the last session crashed or not.

***

#### Exporting Crash Data for Additional Insights

Beyond determining if the last session ended in a crash, you can capture detailed information about the crash itself. The `didSendCrashReportHandler` API lets you export various metadata about the crash, including:

* **Crash Type:** the error type including Fatal, non-fatal, OOM..
* **Error Code:** The specific error code associated with the crash.
* **Error Description:** A textual description providing further context about the error.
* **User Attributes:** User attributes associated with the session.
* **Additional Crash Data:** additional metadata added by the `onCrashHandler` callback

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQCrashReporting.didSendCrashReportHandler = ^(IBGCrashMetaData *metadata) {
  ...
};
```

{% endcode %}
{% endtab %}

{% tab title="Swift" %}

```python
CrashReporting.didSendCrashReportHandler = { metadata in
  ...
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %} <mark style="color:blue;">Note:</mark>

* Any function called within a signal handler must be asynchronous-safe. This means that Objective-C code, among others, is not safe to use in this context.
* This is enabled through a Feature flag. So, please contact our support team at <support@luciq.ai> to enable it
  {% endhint %}
