# Source: https://docs.luciq.ai/references/crash-reporting/enable-or-disable-crash-reporting/disable-oom-crashes.md

# Disable OOM Crashes

By default Out of Memory Crashes are captured by the SDK and sent to your dashboard. However, you can still disable them using the following API.

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
CrashReporting.OOMEnabled = false
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQCrashReporting.OOMEnabled = NO
```

{% endtab %}
{% endtabs %}
