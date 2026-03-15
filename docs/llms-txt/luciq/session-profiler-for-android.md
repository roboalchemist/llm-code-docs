# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/logs-and-profiling/session-profiler-for-android.md

# Session Profiler for Android

The Session Profiler captures the state of the device as well as your app in the 60 seconds before a report is sent. The Session Profiler is sent with both bug and crash reports.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2F695LSYVaiDOPnI8eMq0X%2Fimage.png?alt=media&#x26;token=67f214fa-74f4-4f89-b53a-27f4ce87ceaa" alt=""><figcaption></figcaption></figure>

## Data Breakdown

### Memory

This graph shows the memory usage of your user's device. While hovering over a graph, the exact memory usage is shown over the total amount of memory available, as well as the exact usage percentage. Device memory usage is captured every 0.5 seconds.

### Storage

This graph shows how much storage is used by the device. While hovering over a graph, the exact storage usage is shown over the total amount of storage available, as well as the exact usage percentage. Device storage usage is captured every 0.5 seconds.

### Connectivity

This graph shows the connectivity details of the device. While hovering over a graph, connectivity details are shown such as WiFi name, cellular connectivity type (GPRS, Edge, 3G, LTE or CDMA), carrier name, and "No connection" if there is no network connectivity. Device connectivity details are captured every two seconds.

### Battery

This graph shows the battery percentage of the device. While hovering over a graph, the exact percentage of the battery is shown, as well as whether or not the device is plugged in. Device battery state is captured every two seconds.

### Orientation

This graph shows the orientation state of the application, such as whether the application is in portrait or landscape mode. While hovering over a graph, the exact state is shown. App orientation is captured every two seconds.

## Enabling and Disabling

Session Profiler is enabled by default, however, you can use the below method to enable or disable it manually.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
Luciq.setSessionProfilerState(Feature.State.ENABLED)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
Luciq.setSessionProfilerState(Feature.State.ENABLED);
```

{% endcode %}
{% endtab %}
{% endtabs %}
