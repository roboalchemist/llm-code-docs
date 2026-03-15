# Source: https://docs.instabug.com/references/application-performance-monitoring/set-verbosity-level.md

# Set Verbosity Level

You can control the level of verbosity of the Luciq logs using the following APIs.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
APM.logLevel = SDKLogLevel.Debug
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQAPM.logLevel = LCQLogLevelDebug;
```

{% endtab %}

{% tab title="And - Java" %}

<pre class="language-java"><code class="lang-java"><strong>APM.setLogLevel(LogLevel.DEBUG);
</strong></code></pre>

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
APM.setLogLevel(LogLevel.DEBUG)
```

{% endtab %}

{% tab title="RN" %}

```javascript
APM.setLogLevel(APM.logLevel.debug);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
APM.setLogLevel(APM.logLevel.debug);
```

{% endtab %}
{% endtabs %}

Here are the available level values.

* **`None`:** disables all APM SDK console logs.
* **`Error`:** prints errors only, we use this level to let you know if something goes wrong.
* **`Warning`:** displays warnings that will not necessarily lead to errors but should be addressed nonetheless.
* **`Info`:** this is the default level and it logs information that we think is useful without being too verbose.
* **`Debug`:** use this in case you are debugging an issue. Not recommended for production use.
* **`Verbose`:** use this only if `Debug` was not enough and you need more visibility on what is going on under the hood. Similar to the `Debug` level, this is not meant to be used on production environments.
