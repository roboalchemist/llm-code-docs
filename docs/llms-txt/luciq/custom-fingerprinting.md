# Source: https://docs.luciq.ai/references/crash-reporting/custom-fingerprinting.md

# Custom Fingerprinting

In the event that you'd like to report the exception manually with a custom grouping fingerprint in mind, you can use the below APIs to do so.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

<pre class="language-swift"><code class="lang-swift">CrashReporting.reportError(error, withGroupingString: "grouping string")
<strong>CrashReporting.report(exception, withGroupingString: "grouping string")
</strong></code></pre>

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQCrashReporting reportException:exception groupingString:@"grouping string"];
[LCQCrashReporting reportError:error groupingString:@"grouping string"];
```

{% endtab %}

{% tab title="And - Java" %}

```java
CrashReporting.reportException(throwable, "exception identifier", userAttrsMap, "grouping fingerprint");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
CrashReporting.reportException(throwable, "exception identifier", userAttrsMap, "grouping fingerprint")
```

{% endtab %}
{% endtabs %}
