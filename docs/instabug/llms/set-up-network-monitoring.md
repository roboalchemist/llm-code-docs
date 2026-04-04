# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-network-monitoring.md

# Set up Network Monitoring

### Getting Started

In order to allow Luciq [App Performance Monitoring](https://www.luciq.ai/product/app-performance-monitoring) to capture network requests, you will need to include our Gradle plugin in your project. Currently, we support capturing requests made via `OkHttpClient` and `HTTPURLConnection`.

1. Add the dependency to your project's `build.gradle` file.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
plugins {
  id("ai.luciq.library") version "18.0.0" apply false // adds luciq plugin
}
```

{% endcode %}
{% endtab %}

{% tab title="Groovy" %}
{% code overflow="wrap" %}

```java
buildscript {
    dependencies {
        // ...
        classpath 'com.luciq.library:luciq-plugin:13.0.1'
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

2. Add the plugin in your application's `build.gradle`:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
plugins { 
  id("luciq-apm") // Luciq APM Plugin
}
```

{% endcode %}
{% endtab %}

{% tab title="Groovy" %}
{% code overflow="wrap" %}

```java
apply plugin: 'luciq-apm'
```

{% endcode %}
{% endtab %}
{% endtabs %}

> 📘 The Plugin DSL in Kotlin is supported starting SDK version 12.4.1.

{% hint style="success" %}
The Plugin DSL in Kotlin is supported starting SDK version 12.4.1.
{% endhint %}

**Plugin Alternatives:**

You can always use a manual approach to capture requests made via the `OkHttpClient` by adding our Interceptor and EventListener using the below code snippets:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
OkHttpClient.Builder()
    // add your interceptors here
    .addInterceptor(LuciqAPMOkhttpInterceptor())

    // Add Luciq EventListener
    .eventListener(LuciqApmOkHttpEventListener(/** optional: add your own EventListener here **/))
    // Or Add Luciq EventListenerFactory
    .eventListenerFactory(LuciqApmOkHttpEventListener.Factory(/** optional: add your own EventListener factory here **/))
    .build()
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
new OkHttpClient.Builder()
        // add your interceptors here
        .addInterceptor(new LuciqAPMOkhttpInterceptor())

        // Add Luciq EventListener
        .eventListener(new LuciqApmOkHttpEventListener(/** optional: add your own EventListener here **/))
        // Or Add Luciq EventListenerFactory
        .eventListenerFactory(new LuciqApmOkHttpEventListener.Factory(/** optional: add your own EventListener factory here **/))
        .build();
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="success" %}

### GraphQL Support

Luciq supports capturing requests made via the `OkHttpClient` including `GraphQl` and `HTTPURLConnection`.
{% endhint %}

{% hint style="info" %}

### APM Network Logs are independent from Bug and Crash Reporting

Please note that [Network Logs](https://docs.luciq.ai/android/logs-and-profiling/report-logs-for-android#network-logs) that are captured in Bug and Crash reports will **not** be captured by APM, the only way to enabled Network performance monitoring in APM is by adding this plugin. Enabling Network performance monitoring has **no** effect on Network Logs captured in Bug and Crash reports, these are configured separately and are completely independent from APM.
{% endhint %}

***

### gRPC Support

Luciq supports the logging of gRPC requests. You'll first need to add the gRPC intereceptor module to your dependencies.

#### Integration

With Luciq already integrated and added to your dependencies, you'll only need to add the following dependency to your applications `build.gradle`:

{% tabs %}
{% tab title="Gradle" %}
{% code overflow="wrap" %}

```gradle
implementation 'ai.luciq.library:luciq-apm-grpc-interceptor:$LUCIQ_VERSION
```

{% endcode %}
{% endtab %}
{% endtabs %}

> 📘 Minimum SDK Version
>
> The gRPC interceptor is supported starting SDK version 10.13.0.

{% hint style="success" %}

### Minimum SDK Version

The gRPC interceptor is supported starting SDK version 10.13.0.
{% endhint %}

#### Intercepting gRPC requests

When creating a gRPC channel using your preferred builder, create a new instance of `LuciqAPMGrpcInterceptor` and attach it to the builder using intercept method as shown in the example below:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
OkHttpChannelBuilder.forAddress(host, port)
    .intercept(LuciqAPMGrpcInterceptor())
    .build()
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
OkHttpChannelBuilder.forAddress(host, port)
    .intercept(LuciqAPMGrpcInterceptor())
    .build();
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### Trace Attributes

Sometimes, you may need to add additional data or attributes to your network traces. This can be done using the API below.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
APM.addOnNetworkTraceListener(
    object: OnNetworkTraceListener(
                UrlPredicate { url:String ->
                    // Add filter here the URL 
                    // return boolean
                }
    )
    {
        override fun addAttributesOnFinish(trace: NetworkTrace?): MutableMap<String, String?> {
            // Return map of Pairs (i.e. keys and values)
            return mutableMapOf(
              			// Up to five attributes
                    Pair("Key", "Value")
            )
        }
    }
)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
APM.addOnNetworkTraceListener(new OnNetworkTraceListener(
    new UrlPredicate() {
        @Override
        public boolean check(@NonNull String url) {
            // Add filter here the URL 
            // return boolean
        }
    }); 
    {
        @Override
        public Map<String, String> addAttributesOnFinish(NetworkTrace trace) {
            Map<String, String> map;
            map.put("Key", "Value");
            // Up to five attributes
            return map;
        }
    }
);
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
You can add up to **20 unique trace attributes** per each trace.
{% endhint %}

***

### Payload Size

By default, Luciq captures the payload size of the request and response; this should help with determining if the payload size could be causing any issues with network delays. The payload size is the size of the payload itself, so it does not include the header's size.

Luciq automatically buckets payload sizes into different buckets based on the distribution of the data per network group, with a minimum sensitivity of 10 bytes per bucket.

***

### Disabling/Enabling Network Performance Monitoring

Once you include the plugin as described in the [Getting Started](#getting-started) section, capturing network requests is enabled by default. However, you can still disable Network performance monitoring by configuring the plugin in your `build.gradle` file as described below:

{% tabs %}
{% tab title="Groovy" %}
{% code overflow="wrap" %}

```groovy
Luciq {
    APM {
        networkInterceptingEnabled false
    }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Please note that Luciq does **not** control network logs captured in Bug and Crash reports, it only controls APM.
{% endhint %}
