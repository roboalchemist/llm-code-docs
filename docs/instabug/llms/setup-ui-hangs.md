# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-application-performance-monitoring/setup-ui-hangs.md

# Setup Screen Rendering

{% hint style="warning" %}

### **Minimum Required SDK Version**

Screen Rendering is supported starting Luciq SDK version 19.0
{% endhint %}

Luciq automatically detects any frozen frames or slow frames that your user experiences while using the app. These delayed frames and other critical debugging information is grouped automatically by screen. Learn which screens are experiencing the poorest rendering performance, understand what segments of users are impacted the most, and what spans and operations might’ve caused these issues down to the single occurrence level.

### Customizing Screen Grouping

By default, screens are grouped by Activity. However, you can adjust how Frozen and Slow Frames are grouped by configuring **Custom UI Traces**. These act as their own screen, and any frozen/slow frames that occur when a custom UI trace is active will be aggregated in a new group under that custom UI trace.

* You can run only **one** custom UI trace at a given time; a trace must be ended before a new one can be started.
* The SDK will end any occurrence that wasn't explicitly ended via the end API.

#### **Start Custom UI Trace**

You can use the API below to mark the start of a UI trace. It takes as input a trace name that we use to aggregate the data of relevant occurrences together on your dashboard.

{% code title="Dart" %}

```dart
// Start UI Trace
APM.startUITrace('trace_name');
```

{% endcode %}

{% hint style="info" %}

### **Rules around creating UI Traces:**

* Trace **name** can be up to **150 characters**. Any extra characters are truncated.
* Trace name can't be nil or an empty string.
* Avoid adding any of these special characters `[, (, ), =, {, }, <, >, /, , ]` (commas not included) as they will be replaced with `_`.
* Starting a new trace has to be done after initializing the SDK.
  {% endhint %}

#### **End Custom UI Trace**

Use the API below to end the trace occurrence that you have already started:

{% code title="Dart" %}

```dart
// End UI Trace
APM.endUITrace();
```

{% endcode %}

{% hint style="info" %}
**Note:** Please note that Custom UI Traces do not interfere with Automatic Screen Grouping; both can run in parallel.
{% endhint %}

#### Enable/Disable Screen Rendering

Luciq collects Screen Rendering performance metrics out of the box. If needed, you can disable it by calling the following API after initializing the SDK.

{% code title="Dart" %}

```dart
// Enable
APM.setScreenRenderingEnabled(true);

// Disable
APM.setScreenRenderingEnabled(false);
```

{% endcode %}
