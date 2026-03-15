# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-session-replay.md

# Set up Session Replay

If you're already using Luciq, but [Session Replay](https://www.luciq.ai/product/session-replay) isn't included in your current plan, please reach out to us at <contactus@luciq.ai>, We would love to enable a custom trial for you and help you set it up.

{% hint style="warning" %}

### Min Required SDK Version

Session Replay is supported starting Android SDK version 12.0.
{% endhint %}

**Session Replay Footprint**

We're taking several measures to make sure Luciq Session Replay is resource-friendly. To minimize its impact on the device's battery and data consumption:

* The SDK collects your performance data and sends it in batches, at most, once every 6 hours.
* The SDK doesn't perform any network operations while the app is in the background.
  * This means data collected is sent to the server at the beginning of a session if the last server communication took place more than 6 hours ago.

### Enabling/Disabling Session Replay

Luciq's Session Replay can be disabled with the following method. This will completely prevent any session replay data from being sent to your dashboard. By default, Session Replay is enabled if it is available in your subscription plan.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
SessionReplay.setEnabled(true) //Enabled
SessionReplay.setEnabled(false) //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
SessionReplay.setEnabled(true); //Enabled
SessionReplay.setEnabled(false); //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Logs

All logs are enabled by default, but can be manually disabled/enabled using the below APIs.

### Network

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
SessionReplay.setNetworkLogsEnabled(true) //Enabled
SessionReplay.setNetworkLogsEnabled(false) //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
SessionReplay.setNetworkLogsEnabled(true); //Enabled
SessionReplay.setNetworkLogsEnabled(false); //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Luciq Logs

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
SessionReplay.setLuciqLogsEnabled()(true) //Enabled
SessionReplay.setLuciqLogsEnabled()(false) //Enabled
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
SessionReplay.setLCQLogsEnabled(true); //Enabled
SessionReplay.setLCQLogsEnabled(false); //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

### User Steps

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
SessionReplay.setUserStepsEnabled(true) //Enabled
SessionReplay.setUserStepsEnabled(false) //Disabled
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
SessionReplay.setUserStepsEnabled(true); //Enabled
SessionReplay.setUserStepsEnabled(false); //Disabled
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Screenshots

{% hint style="info" %}
Screenshots are enabled by default; however, you can change the level of masking using the Auto Masking feature.
{% endhint %}

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
val reproConfig = ReproConfigurations.Builder()
        .setIssueMode(IssueType.SessionReplay, {ReproMode})
        .build()
// For Screenshots replace {ReproMode} with ReproMode.EnableWithScreenshots
// For metadata only replace {ReproMode} with ReproMode.EnableWithNoScreenshots
// For disabling screenshots & metadata replace {ReproMode} with ReproMode.Disable

// Setting config on Builder
Luciq.Builder(this, {Application_token})
        .setReproConfigurations(reproConfig)
        .build()

// Setting config RT
Luciq.setReproConfigurations(reproConfig)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
ReproConfigurations reproConfig = new ReproConfigurations.Builder()
         .setIssueMode(IssueType.SessionReplay, {ReproMode})
         .build();
// For Screenshots replace {ReproMode} with ReproMode.EnableWithScreenshots
// For metadata only replace {ReproMode} with ReproMode.EnableWithNoScreenshots
// For disabling screenshots & metadata replace {ReproMode} with ReproMode.Disable

// Setting config on Builder
new Luciq.Builder(this, {Application_token})
         .setReproConfigurations(reproConfig)
         .build();

// Setting config RT
Luciq.setReproConfigurations(reproConfig);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Limits

* Each session contains up to 2MB of compressed logs and 2MB of compressed screenshots.
* Luciq saves sessions up to 50MB worth of data. (for multiple sessions)

### Privacy options

#### Automasking

Enable [auto-masking](https://about/docs/android-repro-steps#auto-masking) with different levels like masking all text, masking images, or masking everything. You can find more details about auto-masking [here](https://about/docs/android-repro-steps#auto-masking).

#### Private views

Set certain screens as private and any private view will automatically appear with a black overlay covering it in any screenshot. You can find more details about private views [here](https://about/docs/android-repro-steps#private-views).

#### Network logs masking

To obfuscate parts of a network request prior to sending it to the dashboard, you can follow the below steps found [here](https://about/docs/android-logging#modifying-requests).
