# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/logs-and-profiling/repro-steps.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings/repro-steps.md

# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/logs-and-profiling/repro-steps.md

# Repro Steps

Repro Steps show you all of the interactions a user makes with your app up until a bug or crash is reported, grouped by the app view. For each view that a user visits, all of the steps that they commit are captured and displayed as logs next to the relevant screenshot. Repro steps can be found below the bug details.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2Ffy4Ly6zeHFNUHztHLQhy%2Fimage.png?alt=media&#x26;token=9ec3e043-36d8-4733-b836-e5a1f54351d8" alt=""><figcaption></figcaption></figure>

### Disabling and Enabling Repro steps

Repro Steps is by default enabled with screenshots for both bug reporting and session replay and enabled without screenshots for crash reporting.

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

You can change the value of the Issue Type.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
//Bug Reporting and Crash Reporting
.all
//Bug Reporting Only
.bug
//Crash Reporting Only
.crash
//Session Replay Only
.sessionReplay
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
//Bug Reporting and Crash Reporting
LCQIssueTypeAll
//Bug Reporting Only
LCQIssueTypeBug
//Crash Reporting Only
LCQIssueTypeCrash
//Session Replay Only
LCQIssueTypeSessionReplay
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can change the value of the User Steps Mode.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
//Enable with Screenshots
.enable
//Enable with NO Screenshots
.enabledWithNoScreenshots
//Disable
.disable
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
//Enable with Screenshots
LCQUserStepsModeEnable
//Enable with NO Screenshots
LCQUserStepsModeEnabledWithNoScreenshots
//Disable
LCQUserStepsModeDisable
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Examples

<table><thead><tr><th width="453.125">API</th><th>Meaning</th></tr></thead><tbody><tr><td>Swift: <code>Luciq.setReproStepsFor(.all, with: .enable)</code><br><br>ObjC:<code>[Lucuq setReproStepsFor:LCQIssueTypeAll withMode:LCQUserStepsModeEnable];</code></td><td>Enable with Screenshots for both Bug Reporting and Crash Reporting.</td></tr><tr><td>Swift: <code>Luciq.setReproStepsFor(.crash, with: .enabledWithNoScreenshots)</code><br><br>ObjC: <code>[Luciq setReproStepsFor:LCQIssueTypeCrash withMode:LCQUserStepsModeEnabledWithNoScreenshots];</code></td><td>Enable with No Screenshots for Crash Reporting.</td></tr><tr><td>Swift: <code>Luciq.setReproStepsFor(.bug, with: .enable)</code><br><br>ObjC: <code>[Luciq setReproStepsFor:LCQIssueTypeBug withMode:LCQUserStepsModeEnable];</code></td><td>Enable with Screenshots for Bug Reporting.</td></tr><tr><td>Swift: <code>Luciq.setReproStepsFor(.all, with: .disable)</code><br><br>ObjC: <code>[Luciq setReproStepsFor:LCQIssueTypeAll withMode:LCQUserStepsModeDisable];</code></td><td>Completely disable for both Bug Reporting and Crash Reporting.</td></tr></tbody></table>

To be able to capture Repro Steps, we need to do method swizzling. We take an approach to swizzling that is absolutely safe and does not impact your app negatively in any way.

{% hint style="info" %}

### Screenshots are by default disabled for Crash Reporting.

For Crash Reporting, screenshots are by default disabled; however, if you are looking to enable screenshots in Crash Reporting, make sure to use the [Auto Masking API](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings). This API will automatically help you mask sensitive data in screenshots to protect the [end-users' privacy](https://docs.luciq.ai/ios/setup-luciq-for-ios/custom-settings/privacy-settings).
{% endhint %}
