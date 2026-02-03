# Source: https://docs.datadoghq.com/feature_flags/client/android.md

# Source: https://docs.datadoghq.com/error_tracking/frontend/mobile/android.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/android.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/android.md

---
title: Tracing Android Applications
description: Collect traces from your Android applications.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing Android Applications
---

# Tracing Android Applications

Send [traces](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/android/otel) to Datadog from your Android applications with [Datadog's `dd-sdk-android-trace` client-side tracing library](https://github.com/open-telemetry/opentelemetry-java?tab=readme-ov-file#requirements) and leverage the following features:

- Create custom [spans](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/android/otel/?tab=kotlin) for operations in your application.
- Add `context` and extra custom attributes to each span sent.
- Optimized network usage with automatic bulk posts.

{% alert level="info" %}
Datadog charges for **ingested and indexed** spans sent from your Android applications, but does not charge for the underlying devices. Learn more in the [APM billing documentation](https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/).
{% /alert %}

The Datadog Tracer implements the [OpenTelemetry](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/android/otel) standard, and Datadog recommends using it as an interface for tracing your application because it's vendor-neutral, supports many languages and frameworks, and unifies traces, metrics, and logs under one standard. See instructions on [setting up OpenTelemetry integration with the SDK](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/android/otel/?tab=kotlin).

**Note:** The OpenTelemetry specification library requires [desugaring](https://github.com/open-telemetry/opentelemetry-java?tab=readme-ov-file#requirements) to be enabled for projects with a `minSdk` < `26`. If you cannot enable desugaring in your project, you can still use the Trace product with the Datadog API instead.

**Note**: The *Datadog API* implementation helps you transition from OpenTracing to OpenTelemetry.

## Setup{% #setup %}

1. Add the Gradle dependency by declaring the library as a dependency in your `build.gradle` file:

   ```groovy
   dependencies {
       implementation "com.datadoghq:dd-sdk-android-trace:x.x.x"
   }
   ```

1. Initialize Datadog SDK with your application context, tracking consent, and the [Datadog client token](https://docs.datadoghq.com/account_management/api-app-keys/#client-tokens). For security reasons, you must use a client token: you cannot use [Datadog API keys](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) to configure Datadog SDK as they would be exposed client-side in the Android application APK byte code. For more information about setting up a client token, see the [client token documentation](https://docs.datadoghq.com/account_management/api-app-keys/#client-tokens):
Important note for users on the following Datadog sites: app.datadoghq.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       ).build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
         .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}




Important note for users on the following Datadog sites: app.datadoghq.eu: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.EU1)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
           .useSite(DatadogSite.EU1)
           .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}


Important note for users on the following Datadog sites: us3.datadoghq.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.US3)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
           .useSite(DatadogSite.US3)
           .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}


Important note for users on the following Datadog sites: us5.datadoghq.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.US5)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
         .useSite(DatadogSite.US5)
         .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}


Important note for users on the following Datadog sites: app.ddog-gov.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.US1_FED)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
         .useSite(DatadogSite.US1_FED)
         .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}


Important note for users on the following Datadog sites: ap1.datadoghq.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.AP1)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
         .useSite(DatadogSite.AP1)
         .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}


Important note for users on the following Datadog sites: ap2.datadoghq.com: 


   {% tab title="Kotlin" %}

   ```kotlin
   class SampleApplication : Application() {
     override fun onCreate() {
       super.onCreate()
       val configuration = Configuration.Builder(
            clientToken = "<CLIENT_TOKEN>",
            env = "<ENV_NAME>",
            variant = "<APP_VARIANT_NAME>"
       )
         .useSite(DatadogSite.AP2)
         .build()
   
       Datadog.initialize(this, configuration, trackingConsent)
     }
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   public class SampleApplication extends Application {
     @Override
     public void onCreate() {
       super.onCreate();
       Configuration configuration = new Configuration.Builder("<CLIENT_TOKEN>", "<ENV_NAME>", "<APP_VARIANT_NAME>")
         .useSite(DatadogSite.AP2)
         .build();
   
       Datadog.initialize(this, configuration, trackingConsent);
     }
   }
   ```

   {% /tab %}



To be compliant with the GDPR regulation, the SDK requires the tracking consent value at initialization. The tracking consent can be one of the following values:

   - `TrackingConsent.PENDING`: The SDK starts collecting and batching the data but does not send it to the data collection endpoint. The SDK waits for the new tracking consent value to decide what to do with the batched data.
   - `TrackingConsent.GRANTED`: The SDK starts collecting the data and sends it to the data collection endpoint.
   - `TrackingConsent.NOT_GRANTED`: The SDK does not collect any data. You will not be able to manually send any logs, traces, or RUM events.

To update the tracking consent after the SDK is initialized, call: `Datadog.setTrackingConsent(<NEW CONSENT>)`. The SDK changes its behavior according to the new consent. For example, if the current tracking consent is `TrackingConsent.PENDING` and you update it to:

   - `TrackingConsent.GRANTED`: The SDK sends all current batched data and future data directly to the data collection endpoint.
   - `TrackingConsent.NOT_GRANTED`: The SDK wipes all batched data and does not collect any future data.

**Note**: In the credentials required for initialization, your application variant name is also required, and should use your `BuildConfig.FLAVOR` value (or an empty string if you don't have variants). This is important because it enables the right ProGuard `mapping.txt` file to be automatically uploaded at build time to be able to view de-obfuscated RUM error stack traces. For more information see the [guide to uploading Android source mapping files](https://docs.datadoghq.com/real_user_monitoring/error_tracking/mobile/android/?tab=us#upload-your-mapping-file).

Use the utility method `isInitialized` to check if the SDK is properly initialized:

   ```kotlin
   if (Datadog.isInitialized()) {
     // your code here
   }
   ```

When writing your application, you can enable development logs by calling the `setVerbosity` method. All internal messages in the library with a priority equal to or higher than the provided level are then logged to Android's Logcat:

   ```kotlin
   Datadog.setVerbosity(Log.INFO)
   ```

1. Configure and enable Trace feature:

   {% tab title="Kotlin" %}

   ```kotlin
   val traceConfig = TraceConfiguration.Builder().build()
   Trace.enable(traceConfig)
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   TraceConfiguration traceConfig = new TraceConfiguration.Builder().build();
   Trace.enable(traceConfig);
   ```

   {% /tab %}



1. Configure and register the `DatadogTracer`. You only need to do it once, usually in your application's `onCreate()` method:

   {% tab title="Kotlin" %}

   ```kotlin
   import com.datadog.android.trace.GlobalDatadogTracer
   import com.datadog.android.trace.DatadogTracing
   
   GlobalDatadogTracer.registerIfAbsent(
       DatadogTracing.newTracerBuilder()
           .build()
   )
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   import com.datadog.android.trace.GlobalDatadogTracer;
   import com.datadog.android.trace.DatadogTracing;
   
   GlobalDatadogTracer.registerIfAbsent(
       DatadogTracing.newTracerBuilder(Datadog.getInstance())
           .build()
   );
   ```

   {% /tab %}



1. (Optional) - Set the partial flush threshold to optimize the SDK's workload based on the number of spans your application generates. The library waits until the number of finished spans exceeds the threshold before writing them to disk. Setting this value to `1` writes each span as soon as it finishes.

   {% tab title="Kotlin" %}

   ```kotlin
   val tracer = DatadogTracing.newTracerBuilder()
       .withPartialFlushMinSpans(10)
       .build()
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   DatadogTracer tracer = DatadogTracing.newTracerBuilder(Datadog.getInstance())
       .withPartialFlushMinSpans(10)
       .build();
   ```

   {% /tab %}



1. Start a custom span using the following method:

   {% tab title="Kotlin" %}

   ```kotlin
   val tracer = GlobalDatadogTracer.get()
   val span = tracer.buildSpan("<SPAN_NAME>").start()
   // Do something ...
   // ...
   // Then when the span should be closed
   span.finish()
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   DatadogTracer tracer = GlobalDatadogTracer.get();
   DatadogSpan span = tracer.buildSpan("<SPAN_NAME>").start();
   // Do something ...
   // ...
   // Then when the span should be closed
   span.finish();
   ```

   {% /tab %}



1. To use scopes in synchronous calls:

   {% tab title="Kotlin" %}

   ```kotlin
   val span = tracer.buildSpan("<SPAN_NAME1>").start()
   try {
       val scope = tracer.activateSpan(span)
       scope?.use {
           // Do something ...
           // ...
           // Start a new Scope
           val childSpan = tracer.buildSpan("<SPAN_NAME2>").start()
           try {
               val innerScope = tracer.activateSpan(childSpan).use { innerScope ->
   
               }
           } catch (e: Throwable) {
               childSpan.logThrowable(e)
           } finally {
               childSpan.finish()
           }
       }
   } catch (e: Throwable) {
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   DatadogSpan span = tracer.buildSpan("<SPAN_NAME1>").start();
   try {
       DatadogScope scope = tracer.activateSpan(span);
       try {
           // Do something ...
           // ...
           // Start a new Scope
           DatadogSpan childSpan = tracer.buildSpan("<SPAN_NAME2>").start();
           try {
               DatadogScope innerScope = tracer.activateSpan(childSpan);
               try {
                   // Do something ...
               } finally {
                   innerScope.close();
               }
           } catch (Throwable e) {
               childSpan.logThrowable(e);
           } finally {
               childSpan.finish();
           }
       } finally {
           scope.close();
       }
   } catch (Throwable e) {
   }
   ```

   {% /tab %}



1. To use scopes in asynchronous calls:

   {% tab title="Kotlin" %}

   ```kotlin
   val span = tracer.buildSpan("<SPAN_NAME1>").start()
   try {
       val scope = tracer.activateSpan(span)
       scope.use {
           // Do something ...
           Thread {
               // Step 2: reactivate the Span in the worker thread
               tracer.activateSpan(span).use {
                   // Do something ...
               }
           }.start()
       }
   } catch (e: Throwable) {
       span.logThrowable(e)
   } finally {
       span.finish()
   }
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   DatadogSpan span = tracer.buildSpan("<SPAN_NAME1>").start();
   try {
       DatadogScope scope = tracer.activateSpan(span);
       try {
           // Do something ...
           new Thread(() -> {
               // Step 2: reactivate the Span in the worker thread
               DatadogScope scopeContinuation = tracer.activateSpan(span);
               try {
                   // Do something
               } finally {
                   scope.close();
               }
           }).start();
       } finally {
           scope.close();
       }
   } catch (Throwable e){
       span.logThrowable(e);
   } finally {
       span.finish();
   }
   ```

   {% /tab %}



1. (Optional) To manually distribute traces between your environments, for example, frontend to backend:

   1. Inject tracer context in the client request.
      {% tab title="Kotlin" %}

      ```kotlin
      val tracer = GlobalDatadogTracer.get()
      val span = tracer.buildSpan("<SPAN_NAME>").start()
      val tracedRequestBuilder = Request.Builder()
      tracer.propagate().inject<Request.Builder?>(
          span.context(),
          tracedRequestBuilder
      ) { builder, key, value ->
          builder?.addHeader(key, value)
      }
      val request = tracedRequestBuilder.build()
      // Dispatch the request and finish the span after.
      ```

      {% /tab %}

      {% tab title="Java" %}

      ```java
      DatadogTracer tracer = GlobalDatadogTracer.get();
      DatadogSpan span = tracer.buildSpan("<SPAN_NAME>").start();
      Request.Builder tracedRequestBuilder = new Request.Builder();
      tracer.propagate().inject(
          span.context(),
          tracedRequestBuilder,
          new Function3<Request.Builder,String,String,Unit>(){
              @Override
              public Unit invoke(Request.Builder builder, String key, String value) {
                builder.addHeader(key, value);
                return Unit.INSTANCE;
              }
          }
      );
      Request request = tracedRequestBuilder.build();
      // Dispatch the request and finish the span after.
      ```

      {% /tab %}
   1. Extract the client tracer context from headers in server code.
      {% tab title="Kotlin" %}

      ```kotlin
      val tracer = GlobalDatadogTracer.get()
      val extractedContext = tracer.propagate()
          .extract(request) { carrier, classifier ->
              val headers = carrier.headers.toMultimap()
                  .map { it.key to it.value.joinToString(";") }
                  .toMap()
      
              for ((key, value) in headers) classifier(key, value)
          }
      
      val serverSpan = tracer.buildSpan("<SERVER_SPAN_NAME>").withParentContext(extractedContext).start()
      ```

      {% /tab %}

      {% tab title="Java" %}

      ```java
      DatadogTracer tracer = GlobalDatadogTracer.get();
      DatadogSpanContext extractedContext = tracer.propagate()
        .extract(request,
          new Function2<Request, Function2<? super String, ? super String, Boolean>, Unit>() {
            @Override
            public Unit invoke(
              Request carrier,
              Function2<? super String, ? super String, Boolean> classifier
            ) {
              request.headers().forEach(pair -> {
                String key = pair.component1();
                String value = pair.component2();
      
                classifier.invoke(key, value);
              });
      
              return Unit.INSTANCE;
            }
          });
      DatadogSpan serverSpan = tracer.buildSpan("<SERVER_SPAN_NAME>").withParentContext(extractedContext).start();
      ```

      {% /tab %}

**Note**: For code bases using the OkHttp client, Datadog provides the implementation below.

1. (Optional) To provide additional tags alongside your span:

   ```kotlin
   span.setTag("http.url", url)
   ```

1. (Optional) To mark a span as having an error, log it using corresponding methods:

   ```kotlin
   span.logThrowable(throwable)
   ```

   ```kotlin
   span.logErrorMessage(message)
   ```

1. If you need to modify some attributes in your Span events before batching you can do so by providing an implementation of `SpanEventMapper` when enabling Trace feature:

   {% tab title="Kotlin" %}

   ```kotlin
   val traceConfig = TraceConfiguration.Builder()
     // ...
     .setEventMapper(spanEventMapper)
     .build()
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   TraceConfiguration config = new TraceConfiguration.Builder()
     // ...
     .setEventMapper(spanEventMapper)
     .build();
   ```

   {% /tab %}

## Kotlin Extensions{% #kotlin-extensions %}

### Running a lambda within a Span{% #running-a-lambda-within-a-span %}

To monitor the performance of a given lambda, you can use the `withinSpan()` method. By default, a scope will be created for the span, but you can disable this behavior by setting the `activate` parameter to false.

```kotlin
import com.datadog.android.trace.withinSpan
import com.datadog.android.trace.api.span.DatadogSpan

withinSpan("<SPAN_NAME>", parentSpan, activate) {
   // Your code here
}
```

### Tracing SQLite transaction{% #tracing-sqlite-transaction %}

If you are using `SQLiteDatabase` to persist data locally, you can trace the database transaction using the following method:

```kotlin
import com.datadog.android.trace.sqlite.transactionTraced
import android.database.sqlite.SQLiteDatabase

sqliteDatabase.transactionTraced("<SPAN_NAME>", isExclusive) { database ->
  // Your queries here
  database.insert("<TABLE_NAME>", null, contentValues)

  // Decorate the Span
  setTag("<TAG_KEY>", "<TAG_VALUE>")
}
```

It behaves like the `SQLiteDatabase.transaction` method provided in the `core-ktx` AndroidX package and only requires a span operation name.

## Integrations{% #integrations %}

In addition to manual tracing, the Datadog SDK provides the following integrations.

### OkHttp{% #okhttp %}

If you want to trace your OkHttp requests, you can add the provided [Interceptor](https://square.github.io/okhttp/interceptors/) (which can be found in the `dd-sdk-android-okhttp` library) as follows:

1. Add the Gradle dependency to the `dd-sdk-android-okhttp` library in the module-level `build.gradle` file:
   ```groovy
   dependencies {
     implementation "com.datadoghq:dd-sdk-android-okhttp:x.x.x"
   }
   ```
1. Add `DatadogInterceptor` to your `OkHttpClient`:
   {% tab title="Kotlin" %}

   ```kotlin
   val tracedHosts = listOf("example.com", "example.eu")
   val okHttpClient = OkHttpClient.Builder()
     .addInterceptor(
       DatadogInterceptor.Builder(tracedHosts)
         .setTraceSampler(RateBasedSampler(20f))
         .build()
     )
     .build()
   ```

   {% /tab %}

   {% tab title="Java" %}

   ```java
   List<String> tracedHosts = Arrays.asList("example.com", "example.eu");
   OkHttpClient okHttpClient = new OkHttpClient.Builder()
     .addInterceptor(
       new DatadogInterceptor.Builder(tracedHosts)
         .setTraceSampler(new RateBasedSampler(20f))
         .build()
     )
     .build();
   ```

   {% /tab %}

This creates a span around each request processed by the OkHttpClient (matching the provided hosts), with all the relevant information automatically filled (URL, method, status code, error), and propagates the tracing information to your backend to get a unified trace within Datadog.

Network traces are sampled with an adjustable sampling rate. A sampling of 100% is applied by default.

The interceptor tracks requests at the application level. You can also add a `TracingInterceptor` at the network level to get more details; for example, when following redirections.

{% tab title="Kotlin" %}

```kotlin
val tracedHosts = listOf("example.com", "example.eu")
val okHttpClient =  OkHttpClient.Builder()
  .addInterceptor(
    DatadogInterceptor.Builder(tracedHosts)
      .setTraceSampler(RateBasedSampler(20f))
      .build()
  )
  .addNetworkInterceptor(
    TracingInterceptor.Builder(tracedHosts)
      .setTraceSampler(RateBasedSampler(100f))
      .build()
  )
  .build()
```

{% /tab %}

{% tab title="Java" %}

```java
List<String> tracedHosts = Arrays.asList("example.com", "example.eu");
OkHttpClient okHttpClient = new OkHttpClient.Builder()
  .addInterceptor(
    new DatadogInterceptor.Builder(tracedHosts)
      .setTraceSampler(new RateBasedSampler(20f))
      .build()
  )
  .addNetworkInterceptor(
    new TracingInterceptor.Builder(tracedHosts)
      .setTraceSampler(new RateBasedSampler(20f))
      .build()
  )
  .build();
```

{% /tab %}

In this case, trace sampling decision made by the upstream interceptor for a particular request will be respected by the downstream interceptor.

Because the way the OkHttp Request is executed (using a Thread pool), the request span won't be automatically linked with the span that triggered the request. You can manually provide a parent span in the `OkHttp Request.Builder` as follows by using `Request.Builder.parentSpan` extension method:

{% tab title="Kotlin" %}

```kotlin
val request = Request.Builder()
  .url(requestUrl)
  .parentSpan(parentSpan)
  .build()
```

{% /tab %}

{% tab title="Java" %}

```java
Request.Builder requestBuilder = new Request.Builder()
  .url(requestUrl);

Request request = OkHttpRequestExtKt
  .parentSpan(requestBuilder, parentSpan)
  .build();
```

{% /tab %}

**Note**:

- If you use multiple Interceptors, this one must be called first.
- If you define custom tracing header types in the Datadog configuration and are using a tracer registered with `GlobalDatadogTracer`, make sure the same tracing header types are set for the tracer in use.

## Batch collection{% #batch-collection %}

All the spans are first stored on the local device in batches. Each batch follows the intake specification. They are sent as soon as network is available, and the battery is high enough to ensure the Datadog SDK does not impact the end user's experience. If the network is not available while your application is in the foreground, or if an upload of data fails, the batch is kept until it can be sent successfully.

This means that even if users open your application while being offline, no data will be lost.

The data on disk will automatically be discarded if it gets too old to ensure the SDK doesn't use too much disk space.

## Initialization{% #initialization %}

The following methods in `DatadogTracerBuilder` can be used when initializing the `DatadogTracer`:

| Method                                            | Description                                                                                                                                                                                  |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `withServiceName(<SERVICE_NAME>)`                 | Set the value for the `service`.                                                                                                                                                             |
| `withPartialFlushMinSpans(<INT>)`                 | When this threshold is reached (you have a specific `<INT>` amount of spans closed waiting), the flush mechanism is triggered and all pending closed spans are processed and sent to intake. |
| `withTag(<KEY>, <VALUE>)`                         | Set a `<KEY>:<VALUE>` pair of tags to be added to spans created by the Tracer.                                                                                                               |
| `setBundleWithRumEnabled(true)`                   | Set to `true` to enable spans to be enriched with the current RUM View information. This enables you to see all of the spans produced during a specific View lifespan in the RUM Explorer.   |
| `withSampleRate(<FLOAT>)`                         | Set a value `0-100` to define the percentage of Traces to collect.                                                                                                                           |
| `withTracingHeadersTypes(Set<TracingHeaderType>)` | Sets the tracing header styles that may be injected by the Tracer.                                                                                                                           |
| `setTraceRateLimit(<INT>)`                        | Sets the trace rate limit. This is the maximum number of traces per second that will be accepted.                                                                                            |

## Further Reading{% #further-reading %}

- [dd-sdk-android Source code](https://github.com/DataDog/dd-sdk-android)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/visualization/)
