# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-application-performance-monitoring/instrumentation-for-android.md

# Instrumentation for Android

## Spans

Spans allow you to understand better the root causes of the latencies that occur during your app’s launch and screen loading. This section provides a detailed breakdown of the duration of the platform life cycle stages, network calls, and more information during the app launch and screen loading.

![](https://files.readme.io/17dfcdc-Spans_Android.png)

### Spans Table Breakdown

|                  |                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Span Name        | This shows the stage or request name to identify its source.                                                                                                                               |
| P50              | This is the 50th percentile, which is the maximum latency that 50% of all the occurrences have in the selected time period and is shown in ms.                                             |
| P95              | This is the 95th percentile, which is the maximum latency that 95% of all the occurrences have in the selected time period and is shown in ms.                                             |
| P50 & P95 Change | This shows the change rate of P50 & P95 durations in comparison to the last period based on the selected date filter.                                                                      |
| Average Calls    | This shows how many times the span happened per single occurrence to understand its redundancy better. To get the overall duration of this span, multiply the Average Call by the P50/P95. |
| Frequency        | This is how many times the span happened per all occurrences of the specified metric.                                                                                                      |

### Supported Span Types

These are the currently supported Span Types:

* View Loading
* Network
* App Initialization
* Fragments Loading
* Composable Loading

{% hint style="info" %}
If you are using the EndAppLaunch or EndScreenLoading APIs, Luciq captures the duration from the start of the app launch or screen loading up until the call of any of both APIs.
{% endhint %}

## Fragments

Luciq does not capture Fragments by default on Android, so you can use the following steps to capture and display them on your dashboard.

1. Add the below dependency to your project's *build.gradle* file.

```groovy
buildscript {
    dependencies {
        // ...
        classpath 'ai.luciq.library:luciq-plugin:x.x.x' // Replace x.x.x with your current SDK version
    }
}
```

2. Add the below plugin to your application's *build.gradle* file.

```groovy
apply plugin: 'luciq-apm'

luciq {
    apm {
        fragmentSpansEnabled = true
    }
}
```

{% hint style="info" %}
Luciq supports Fragments starting from `androidx.fragment:fragment:1.2.0` or above and starting from SDK version `11.7.0`.
{% endhint %}

### Enable/Disable Fragments

Capturing Fragments can be enabled or disabled accordingly by using the API below:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Enable
APM.setFragmentSpansEnabled(true)
//Disble
APM.setFragmentSpansEnabled(false)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Enable
APM.setFragmentSpansEnabled(true)
//Disble
APM.setFragmentSpansEnabled(false)
```

{% endcode %}
{% endtab %}
{% endtabs %}

## Composable Loading

Composable views are supported on several products in different forms. When it comes to Performance Monitoring, we capture the composable views loading that took place in the App Launch or Screen Loading as a span inside the Activity and show it in the spans table.

![](https://files.readme.io/0551d22-image.png)

You can read more about configuring Luciq to capture composable loading and stability [here](https://docs.luciq.ai/android/set-up-luciq-for-android/integrate-luciq-on-android/jetpack-compose-integration).

## Spans Table in Network Metric

To help you have a better understanding of what's causing the bulk delays inside your network calls, either from the Client, Server, or Network sides, you'll be able to see a detailed breakdown of the latencies caused by the stages/operations that were made to send the network request and receive its response from the server on aggregation and occurrence levels inside the network metric.

To help you have a better understanding of what's causing the bulk delays inside your network calls, either from the Client, Server, or Network sides, you'll be able to see a detailed breakdown of the latencies caused by the stages/operations that were made to send the network request and receive its response from the server on aggregation and occurrence levels inside the network metric.
