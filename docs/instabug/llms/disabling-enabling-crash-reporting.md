# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-crash-reporting/disabling-enabling-crash-reporting.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-crash-reporting/disabling-enabling-crash-reporting.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/setup-crash-reporting/disabling-enabling-crash-reporting.md

# Source: https://docs.instabug.com/android/set-up-luciq-for-android/set-up-crash-reporting/disabling-enabling-crash-reporting.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-crash-reporting/disabling-enabling-crash-reporting.md

# Disabling/Enabling Crash Reporting

&#x20;Luciq [Crash Reporting](https://www.luciq.ai/product/crash-reporting) can be disabled with the following method. This will completely prevent **any** crash report from being sent to your dashboard. By default, crash reporting is enabled if it is available in your current plan.

{% tabs %}
{% tab title="Swift" %}

```swift
CrashReporting.enabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
LCQCrashReporting.enabled = NO;
```

{% endtab %}
{% endtabs %}

{% hint style="info" %} <mark style="color:blue;">Disabling Crash Reporting</mark>

In case you need to disable Crash Reporting, it should be disabled before Luciq is initialized (before `startWithToken:`)
{% endhint %}

#### Disable App Hangs

By default, App Hangs are captured by the SDK and sent to your dashboard. However, you can still disable them using the following API.

{% tabs %}
{% tab title="Swift" %}

```swift
CrashReporting.appHangEnabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
LCQCrashReporting.appHangEnabled = NO
```

{% endtab %}
{% endtabs %}

#### Disable Force Restarts

By default, Force Restarts are captured by the SDK and sent to your dashboard. However, you can still disable them using the following API.

{% tabs %}
{% tab title="Swift" %}

```swift
CrashReporting.forceRestartEnabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
LCQCrashReporting.forceRestartEnabled = NO
```

{% endtab %}
{% endtabs %}

#### Disable OOM Crashes

By default, out-of-memory crashes are captured by the SDK and sent to your dashboard. However, you can still disable them using the following API.

{% tabs %}
{% tab title="Swift" %}

```swift
CrashReporting.OOMEnabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
LCQCrashReporting.OOMEnabled = NO
```

{% endtab %}
{% endtabs %}
