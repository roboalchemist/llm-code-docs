# Source: https://docs.luciq.ai/references/report-data/logging/instabug-logging.md

# Luciq Logging

Luciq logging functions very similarly to normal logging with the added benefits of having different verbosity levels. These can be filtered on the [Luciq dashboard](https://dashboard.luciq.ai/).

The available verbosity levels are:

* Log
* Verbose
* Info
* Warning
* Debug
* Error

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
LCQLog.log("Log statement")
LCQLog.logVerbose("Verbose statement")
LCQLog.logInfo("Info statement")
LCQLog.logWarn("Warning statement")
LCQLog.logDebug("Debug statement")
LCQLog.logError("Error statement")
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQLog(@"Log message");
LCQLogVerbose(@"Verbose log message");
LCQLogDebug(@"Debug log message");
LCQLogInfo(@"Info log message");
LCQLogWarn(@"Warn log message");
LCQLogError(@"Error log message");
```

{% endtab %}

{% tab title="And - Java" %}

```java
LuciqLog.d("Message to log");
LuciqLog.v("Message to log");
LuciqLog.i("Message to log");
LuciqLog.e("Message to log");
LuciqLog.w("Message to log");
LuciqLog.wtf("Message to log");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
LuciqLog.d("Message to log")
LuciqLog.v("Message to log")
LuciqLog.i("Message to log")
LuciqLog.e("Message to log")
LuciqLog.w("Message to log")
LuciqLog.wtf("Message to log")
```

{% endtab %}

{% tab title="RN" %}

```javascript
Luciq.logVerbose("Message to log")
Luciq.logInfo("Message to log")
Luciq.logDebug("Message to log")
Luciq.logError("Message to log")
Luciq.logWarn("Message to log")
```

{% endtab %}

{% tab title="Flutter" %}

```dart
LuciqLog.logVerbose("Message to log")
LuciqLog.logInfo("Message to log")
LuciqLog.logDebug("Message to log")
LuciqLog.logError("Message to log")
LuciqLog.logWarn("Message to log")
```

{% endtab %}
{% endtabs %}
