# Source: https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-bug-reporting/proactive-reporting-for-android.md

# Proactive Reporting for Android

### What is Proactive Reporting?

Proactive Reporting is a feature that prompts end users to submit their feedback after our SDK automatically detects a frustrating experience.&#x20;

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FAlvejxWABlkKAhaTcZSW%2FBug%20Reporting%20for%20Android.gif?alt=media&#x26;token=e6e2bc2b-9510-4abf-be21-c571cbb1180a" alt=""><figcaption></figcaption></figure>

***

The frustrating experience our SDK detects to trigger the feedback modal is **Force Restart**.

If you have our **Force Restart** product enabled as part of your plan, users will be prompted to submit their feedback and explain what triggered them to force restart the app.

The details of the feature are as follows:

* You should have **Force Restart** as part of your plan.
* Enable the feature (Using the APIs in the upcoming section).
* Once the SDK captures a Force Restart occurrence, a modal will be triggered to ask your end-users if they want to share their feedback and experience.
* This feedback will reflect on your Bug Reporting page in the dashboard.

If enabled, users will first see a modal asking if they want to report this experience. If their answer is yes, they will see a **Feedback** description model that allows them to enter their email and describe their experience using their own words.

|                                                |                                                |
| ---------------------------------------------- | ---------------------------------------------- |
| ![](https://files.readme.io/66c0542-image.png) | ![](https://files.readme.io/8adf1a8-image.png) |

On the dashboard, your end-user's feedback will be reflected in the Bug Reporting page as a **Frustrating Experience** report type.

Clicking the **Open Occurrence** under the **Force Restart** section will take you to the occurrence where the end-user force closed the app in the Force Restart product.

![](https://files.readme.io/366d473-image.png)

{% hint style="info" %}
The report's details show the data from the session after the user force-closed the app, while the details you’ll see in the Force Restart occurrence are from the session in which they force-closed the app.
{% endhint %}

### Enabling Proactive Reporting

By default, the Proactive Reporting is disabled. You can use the below API to:

* Enable/disable the feature.
* Configure the gap between two pop-ups for the same user.
* Configure the gap between the app launch and the first pop-up.

> 📘 The gap calculation starts when our SDK detects a Force Restart or a Crash occurrence, usually a few milliseconds after the launch.

{% hint style="info" %}
The gap calculation starts when our SDK detects a Force Restart or a Crash occurrence, usually a few milliseconds after the launch.
{% endhint %}

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
val configurations = ProactiveReportingConfigs.Builder() 
                      .isEnabled(true) //Enable/disable
                      .setGapBetweenModals(24) // Time in seconds
                      .setModalDelayAfterDetection(30) // Time in seconds
                      .build() 
BugReporting.setProactiveReportingConfigurations(configurations)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
ProactiveReportingConfigs configs = new ProactiveReportingConfigs.Builder()
                .setGapBetweenModals(24) // Time in seconds
                .setModalDelayAfterDetection(20) // Time in seconds
                .isEnabled(true) //Enable/disable
                .build();

        BugReporting.setProactiveReportingConfigurations(configs);
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Good to know about Proactive Reporting

The feature’s default behavior is as follows:

* Feature is disabled.
* If you don’t configure the gap between pop-ups, the default gap will be 24 hours.
* If you don’t configure the gap between the launch and the first pop-up, the default gap will be 2 seconds.
* If you have Surveys enabled in your plan, please contact the support team to enable this feature for you from our backend. Remember to configure the surveys triggering differently from the proactive reporting modal to avoid overwhelming your users.
* To use this feature, Force Restart (part of Crash Reporting) has to be part of your plan.
* Proactive reports have the same data retention as Force Restart (part of Crash Reporting)
* If you use our Crash Consent feature, the pop-up won’t be displayed in the session in which the crash consent will appear.
