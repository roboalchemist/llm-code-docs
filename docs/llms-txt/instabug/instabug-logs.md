# Source: https://docs.instabug.com/references/report-data/logging/instabug-logs.md

# Luciq Debug Logs

Luciq provides useful console logs to have visibility over significant events that might be of interest.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.sdkDebugLogsLevel = .verbose
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
Luciq.sdkDebugLogsLevel = LCQSDKDebugLogsLevelVerbose;
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.setSdkDebugLogsLevel(LogLevel.VERBOSE);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setSdkDebugLogsLevel(LogLevel.VERBOSE)
```

{% endtab %}
{% endtabs %}

The available levels are:

* **`None`:** this will disable all APM SDK console logs.
* **`Error`:** prints errors only, we use this level to let you know if something goes wrong.
* **`Warning`:** displays warnings that will not necessarily lead to errors but should be addressed nonetheless.
* **`Info`:** this is the default level and it logs information that we think is useful without being too verbose.
* **`Debug`:** use this in case you are debugging an issue. Not recommended for production use.
* **`Verbose`:** use this only if `Debug` was not enough and you need more visibility on what is going on under the hood. Similar to the `Debug` level, this is not meant to be used on production environments.
