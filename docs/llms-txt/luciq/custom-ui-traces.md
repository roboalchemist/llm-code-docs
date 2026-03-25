# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-rendering/custom-ui-traces.md

# Custom UI Traces

#### Customizing Screen Grouping

By default, screens are grouped by Activity. However, you can adjust how Frozen and Slow Frames are grouped by configuring **Custom UI Traces**. These act as their own screen, and any frozen/slow frames that occur when a custom UI trace is active will be aggregated in a new group under that custom UI trace.

* You can run only **one** custom UI trace at a given time; a trace must be ended before a new one can be started.
* The SDK will end any occurrence that wasn't explicitly ended via the end API.

**Start Custom UI Trace**

You can use the API below to mark the start of a UI trace. It takes as input a trace name that we use to aggregate the data of relevant occurrences together on your dashboard.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// Start UI Trace
APM.startUITrace(withName: "name")
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// Start UI Trace
[LCQAPM startUITraceWithName:@"name"];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

### **Rules around creating UI Traces:**

* Trace **name** can be up to **150 characters**. Any extra characters are truncated.
* Trace name can't be nil or an empty string.
* Avoid adding any of these special characters `[, (, ), =, {, }, <, >, /, , ]` (commas not included) as they will be replaced with `_`.
* Starting a new trace has to be done after initializing the SDK.
  {% endhint %}

**End Custom UI Trace**

Use the API below to end the trace occurrence that you have already started:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// End UI Trace
APM.endUITrace()
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// End UI Trace
[LCQAPM endUITrace];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note:** Please note that Custom UI Traces do not interfere with Automatic Screen Grouping; both can run in parallel.
{% endhint %}
