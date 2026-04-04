# Source: https://docs.luciq.ai/references/report-data/logging/network-logging-android.md

# Network Logging - Android

Network logs are automatically collected by Luciq when possible. There are many way to configure and manipulate these logs from the code.

### Logging `HttpUrlConnection` Requests

To log network requests, use `LuciqNetworkLog` then use the following method at the `HttpUrlConnection`, `requestBody` and `responseBody`. A more detailed example can be found [here](https://docs.luciq.ai/docs/android-logging#section-logging-httpurlconnection-requests).

**Logging `HttpUrlConnection` Requests**

{% tabs fullWidth="true" %}
{% tab title="Java" %}

```java
LuciqNetworkLog networkLog = new LuciqNetworkLog();
networkLog.Log(urlConnection, requestBody, responseBody);
```

{% endtab %}

{% tab title="Kotlin" %}

```kotlin
LuciqNetworkLog networkLog = new LuciqNetworkLog()
networkLog.Log(urlConnection, requestBody, responseBody)
```

{% endtab %}
{% endtabs %}

### Logging `Okhttp` Requests

In order to log Okhttp requests, first make sure that you compiled Luciq with a network interceptor. By adding the following to your Gradle: `implementation 'com.luciq.library:luciq-with-okhttp-interceptor:8+'`

An example of the implementation can be found on the right hand side of this section.&#x20;

**Logging `Okhttp` Requests**

First, start by compiling Luciq with a network interceptor using this API.

```groovy
implementation 'com.luciq.library:luciq-with-okhttp-interceptor:11.5.4'
```

Then to log Oktthp requests, use the `LuciqOkhttpInterceptor` as shown in the following example.

{% tabs fullWidth="true" %}
{% tab title="Java" %}

```java
LuciqOkhttpInterceptor luciqOkhttpInterceptor = new LuciqOkhttpInterceptor();

OkHttpClient client = new OkHttpClient.Builder()
    .addInterceptor(interceptor)
    .addInterceptor(luciqOkhttpInterceptor)
    .build();
```

{% endtab %}

{% tab title="Kotlin" %}

```kotlin
val luciqOkhttpInterceptor = LuciqOkhttpInterceptor()

val client = OkHttpClient.Builder()
         .addInterceptor(interceptor)
         .addInterceptor(luciqOkhttpInterceptor)
         .build()
```

{% endtab %}
{% endtabs %}

### Modifying Requests&#x20;

If you want to modify a network request before it gets sent to the dashboard, you may follow the steps below.

1. Create a `NetworkLogListener` object and modify the captured network log as shown below.

{% tabs fullWidth="true" %}
{% tab title="Java" %}

```java
NetworkLogListener networkLogListener = new NetworkLogListener() {
    @Override
    public NetworkLogSnapshot onNetworkLogCaptured(NetworkLogSnapshot networkLog) {
        //Modify the received networkLog parameter
        return networkLog;
    }
};
```

{% endtab %}

{% tab title="Kotlin" %}

```kotlin
val networkLogListener = NetworkLogListener { networkLog: NetworkLogSnapshot ->
    //Modify the received networkLog parameter
    return@NetworkLogListener networkLog
}
```

{% endtab %}
{% endtabs %}

2. Register the created `NetworkLogListener` to your `LuciqOkHttpInterceptor` object. This can be done through two different methods:

a. Pass it in the constructor.

```
val luciqOkhttpInterceptor = LuciqOkhttpInterceptor(networkLogListener)
```

b. Call registerNetworkLogsListener method on LuciqOkhttpInterceptor object.

```
val luciqOkhttpInterceptor = LuciqOkhttpInterceptor()
luciqOkhttpInterceptor.registerNetworkLogsListener(networkLogListener)
```

If you want to remove the network listener, you can do so using this API.

{% tabs fullWidth="true" %}
{% tab title="Java" %}

```java
luciqOkhttpInterceptor.removeNetworkLogsListener();
```

{% endtab %}

{% tab title="Kotlin" %}

```kotlin
luciqOkhttpInterceptor.removeNetworkLogsListener()
```

{% endtab %}
{% endtabs %}
