# Source: https://docs.luciq.ai/kmp/setup-luciq-for-kmp/setup-session-replay.md

# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-session-replay.md

# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/setup-session-replay.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-session-replay.md

# Setup Session Replay

If you're already using Luciq, but Session Replay isn't included in your current plan, please reach out to us at <contactus@luciq.ai> We would love to enable a custom trial for you and help you set it up.

{% hint style="warning" %}

### Min Required SDK Version

Session Replay is supported starting iOS SDK version 12.0.
{% endhint %}

#### **Session Replay Footprint**

We're taking several measures to make sure Luciq Session Replay is resource-friendly. To minimize its impact on the device's battery and data consumption:

* The SDK collects your performance data and sends it in batches, at most, once every 6 hours.
* The SDK doesn't perform any network operations while the app is in the background.
  * This means data collected is sent to the server at the beginning of a session if the last server communication took place more than 6 hours ago.

{% hint style="info" %}

### Data Retention

Data retention period is customizable on the [Enterprise plan](https://luciq.ai/pricing).
{% endhint %}

### Enabling/Disabling Session Replay

Luciq's Session Replay can be disabled with the following method. This will completely prevent any session replay data from being sent to your dashboard.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
SessionReplay.enabled = true //Enabled
SessionReplay.enabled = false //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSessionReplay.networkLogsEnabled = YES; //Enabled
LCQSessionReplay.networkLogsEnabled = NO; //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Logs

All logs are enabled by default, but can be manually disabled/enabled using the below APIs. More details about each log type can be found [here](https://docs.instabug.com/docs/ios-logging).

#### Network

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
SessionReplay.networkLogsEnabled = true //Enabled
SessionReplay.networkLogsEnabled = false //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSessionReplay.networkLogsEnabled = YES; //Enabled
LCQSessionReplay.networkLogsEnabled = NO; //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Luciq Logs

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
SessionReplay.IBGLogsEnabled = true //Enabled
SessionReplay.IBGLogsEnabled = false //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSessionReplay.IBGLogsEnabled = YES; //Enabled
LCQSessionReplay.IBGLogsEnabled = NO; //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### User Steps

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
SessionReplay.userStepsEnabled = true //Enabled
SessionReplay.userStepsEnabled = false //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQSessionReplay.userStepsEnabled = YES; //Enabled
LCQSessionReplay.userStepsEnabled = NO; //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Screenshots

{% hint style="info" %}
Screenshots are enabled by default; however, you can change the level of masking using the [Auto Masking](https://docs.instabug.com/docs/ios-repro-steps#auto-masking) feature.
{% endhint %}

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
Luciq.setReproStepsFor(.all, with: .enable)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[Luciq setReproStepsFor:LCQIssueTypeAll withMode:LCQUserStepsModeEnable];
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Limits

* Each session contains up to 2MB of compressed logs and 2MB of compressed screenshots.
* Luciq saves sessions up to 50MB worth of data. (for multiple sessions)
* Data is sent through requests with a maximum of 1MB per request.

### Privacy options

#### Auto-Masking

Enable auto-masking with different levels like masking all text, masking images, or masking everything. You can find more details about auto-masking [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/repro-steps).

#### Private Views

Set certain screens as private and any private view will automatically appear with a black overlay covering it in any screenshot. You can find more details about private views [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/private-views).

#### Network Logs Masking

To obfuscate parts of a network request prior to sending it to the dashboard, you can follow the below steps found [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/network-masking).
