# Source: https://docs.luciq.ai/references/crash-reporting/report-error/adding-level-to-error.md

# Adding Level To Error

You can set different levels for manually reported errors using the following API:

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
let error = NSError(domain: "com.service.method", code: 404)
if let nonFatalError = CrashReporting.error(error) {
    nonFatalError.level = .critical
    nonFatalError.report()
}
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSError *error = [NSError errorWithDomain:@"com.service.method" code:404 userInfo:nil];
LCQNonFatalError *nonFatalError = [LCQCrashReporting error:error];
nonFatalError.level = LCQNonFatalLevelWarning;
[nonFatalError report];
```

{% endtab %}
{% endtabs %}

Here are the different severity levels available. In case no level is indicated, the default level would be error.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
.warning
.error
.critical
.info
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQNonFatalLevelWarning
LCQNonFatalLevelError
LCQNonFatalLevelCritical
LCQNonFatalLevelInfo
```

{% endtab %}
{% endtabs %}
