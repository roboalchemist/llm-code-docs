# Source: https://docs.instabug.com/references/crash-reporting/report-error.md

# Report Error

You can manually report errors to the dashboard using this API. The method takes an error as an argument.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

<pre class="language-swift"><code class="lang-swift">let error = NSError(domain: "domain", code: 500, userInfo: nil)
<strong>CrashReporting.reportError(error)
</strong></code></pre>

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSError *error = [[NSError alloc] initWithDomain:@"domain" code:500 userInfo:nil];
[LCQCrashReporting reportError:error];
```

{% endtab %}

{% tab title="And - Java" %}

```java
CrashReporting.reportException(new NullPointerException("Test issue"));
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
CrashReporting.reportException(new NullPointerException("Test issue"))
```

{% endtab %}

{% tab title="RN" %}

```javascript
try {
      throw new SyntaxError();
    } catch (error) {
      alert(error.name);
      Luciq.reportJSException(error);
    }
```

{% endtab %}
{% endtabs %}
