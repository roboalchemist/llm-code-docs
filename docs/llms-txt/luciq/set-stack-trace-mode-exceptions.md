# Source: https://docs.luciq.ai/references/crash-reporting/report-exception/set-stack-trace-mode-exceptions.md

# Set Stack Trace Mode for Exceptions

You can use the below API to set the stack trace mode you want to capture when reporting exceptions

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
if let nonFatal = CrashReporting.report(exception) {
    nonFatal.stackTraceMode = .callerThreadOnly 
    nonFatal.report()
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQNonFatalError *nonFatal = [LCQCrashReporting error:error];
nonFatal.stackTraceMode = LCQNonFatalStackTraceModeCallerThreadOnly
```

{% endtab %}
{% endtabs %}

Below are the different modes available:

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
.full //default
.callerThreadOnly
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQNonFatalStackTraceModeFull //default
LCQNonFatalStackTraceModeCallerThreadOnly
```

{% endtab %}
{% endtabs %}
