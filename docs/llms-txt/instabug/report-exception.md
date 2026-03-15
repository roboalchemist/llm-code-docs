# Source: https://docs.instabug.com/references/crash-reporting/report-exception.md

# Report Exception

You can manually report exceptions to the dashboard using this API. The method takes an exception as an argument.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
CrashReporting.report(exception)
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[LCQCrashReporting reportException:exception];
```

{% endtab %}

{% tab title="And - Java" %}

```java
LCQNonFatalException exception = new LCQNonFatalException.Builder(new NullPointerException("Test Exception"))
.setUserAttributes(new HashMap<>())
.setFingerprint("My Custom Fingerprint")
.setLevel(LCQNonFatalException.Level.CRITICAL)
.build();
CrashReporting.report(exception);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
val exception = LCQNonFatalException.Builder(NullPointerException("Test Exception"))
.setUserAttributes(mapOf("height" to "tall"))
.setFingerprint("My Custom Fingerprint")
.setLevel(LCQNonFatalException.Level.CRITICAL)
.build()
CrashReporting.report(exception)
```

{% endtab %}

{% tab title="RN" %}

```javascript
try {
      throw new SyntaxError();
    } catch (err) {
      if (err instanceof Error) {
        CrashReporting.reportError(err);
      }
    }
```

{% endtab %}

{% tab title="Flutter" %}

```dart
CrashReporting.reportHandledCrash(error, stackTrace);
```

{% endtab %}
{% endtabs %}
