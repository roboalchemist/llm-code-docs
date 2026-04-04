# Source: https://docs.luciq.ai/references/crash-reporting/report-exception/adding-level-to-exception.md

# Adding Level to Exception

You can set different levels for manually reported exceptions using the following API:

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

<pre class="language-swift"><code class="lang-swift"><strong>let exception = NSException(name: NSExceptionName("some_exception"), reason: "Exception reason")
</strong>if let nonFatalException = CrashReporting.exception(exception) {
    nonFatalException.level = .critical
    nonFatalException.report()
}
</code></pre>

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSException *exception = [NSException exceptionWithName:@"some_exception" reason:@"Exception reason" userInfo:nil];
LCQNonFatalException *nonFatalException = [LCQCrashReporting exception:exception];
nonFatalException.level = LCQNonFatalLevelWarning;
[nonFatalException report];
```

{% endtab %}

{% tab title="And - Java" %}

```java
LCQNonFatalException exception = new LCQNonFatalException.Builder(new NullPointerException("Test Exception"))
	.setLevel(LCQNonFatalException.Level.CRITICAL)
	.build();
CrashReporting.report(exception);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
val exception = LCQNonFatalException.Builder(NullPointerException("Test Exception"))
	.setLevel(LCQNonFatalException.Level.CRITICAL)
	.build()
CrashReporting.report(exception)
```

{% endtab %}
{% endtabs %}

Here are the different severity levels available. In case no level is indicated, the default level would be ERROR.

{% tabs fullWidth="true" %}
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

{% tab title="Android" %}

```java
LCQNonFatalException.Level.WARNING
LCQNonFatalException.Level.ERROR
LCQNonFatalException.Level.CRITICAL
LCQNonFatalException.Level.INFO
```

{% endtab %}
{% endtabs %}
