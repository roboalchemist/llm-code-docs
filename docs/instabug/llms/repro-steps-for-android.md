# Source: https://docs.instabug.com/android/set-up-luciq-for-android/logs-and-profiling/repro-steps-for-android.md

# Repro Steps for Android

Repro Steps show you all of the interactions a user makes with your app up until a bug or crash is reported, grouped by the app view. For each view that a user visits, all of the steps that they commit are captured and displayed as logs next to the relevant screenshot. Repro steps can be found below the bug details.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FFr7CaMeMTlxi8OJwrF6G%2Fimage.png?alt=media&#x26;token=e9b58a42-c975-4721-8a87-55b424c118b5" alt=""><figcaption></figcaption></figure>

## Logged Data

### Captured Events

#### UI Interactions

For the following gestures, only the gesture is logged and displayed:

* Swipe
* Scroll
* Pinch
* Tap
* Double tap
* Enabling/disabling a switch
* Changing the value of a slider
* Editing a text field.

#### Lifecycle Events

Whenever one of the following lifecycle events occurs, it will be captured and shown on the timeline:

* Application is moved to the background
* Application is moved to the foreground
* Application becomes active
* Application becomes inactive

### Extra Details

Depending on the event, you'll find further details displayed as part of the log statement.

* **Tap and double tap:** the SDK always tries to first capture the text rendered inside the UI that the user is interacting with, then we fall back to capturing the icon only with the buttons and navigation items, then, we fall back to the accessibility labels.
* **Switch:** both the accessibility label as well as whether the user enabled or disabled the switch are logged.
* **Slider:** both the accessibility label as well as the value that the user moves the slider to it are captured.
* **Text fields:** first, the SDK tries to capture the placeholder, then we fall back to the accessibility label.

### Examples

Here are some examples of how steps look like:

* `Tapped on the button "Send"`
* `Double tapped on UI that contains "Instructions"`
* `Started editing “Password“`
* `Enabled the switch “Push Notifications“`
* `Moved the slider “Text Size“ to 10%`
* `App went to the background`
* `App became active`

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2Fz7xWRDrZ4RtBVMwndmIE%2Fimage.png?alt=media&#x26;token=7e8ebca3-4d87-4225-87d9-5c26f38b7964" alt=""><figcaption></figcaption></figure>

## User Privacy

### Disclaimer

A disclaimer will be shown at the bottom of the report. It helps your users view all the screenshots taken for the Repro Steps before sending a report and can delete them as well.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2FBnd8ECGpJPdsinMhPcCM%2Fimage.png?alt=media&#x26;token=d732c69c-629f-44c1-9b9d-6ca819048fe2" alt=""><figcaption></figcaption></figure>

### Private Views

On your side, you can easily mark any view that might contain sensitive info like payment details as private. Any private view will automatically appear with a black overlay covering it in any screenshot.

{% hint style="info" %}

#### Effect of Private Views

When adding a view to the list of private views, here are the list of things it will affect:

* Views will be blacked out in screenshots
* Views will be blacked out in repro steps
* Views will be blacked out in the View Hierarchy. Text views will be replaced with \*\*\*\*
* Videos will not be blacked out due to limitations regarding media projection
* To black out screens in videos/screen recording, you can use Android’s [FLAG SECURE](https://developer.android.com/reference/android/view/WindowManager.LayoutParams#FLAG_SECURE)
  {% endhint %}

#### Adding Private Views

To make a view private, you use the following method:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Should be added in the activity with the view, takes any number of views
Luciq.addPrivateViews(view1, view2, view3)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Should be added in the activity with the view, takes any number of views
Luciq.addPrivateViews(view1, view2, view3);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Removing Private Views

If you'd like to remove a view from the list of private views, use the following method:

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Should be added in the activity with the view, takes any number of views
Luciq.removePrivateViews(view1, view2, view3)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Should be added in the activity with the view, takes any number of views
Luciq.removePrivateViews(view1, view2, view3);
```

{% endcode %}
{% endtab %}
{% endtabs %}

## Auto Masking

{% hint style="info" %}

#### Good To Know

* This feature requires a minimum Android SDK version of 11.13.0
* Auto Masking is supported only in screenshots (Repro Steps), not screen recordings.
* Starting from SDK version **19.2.0**, the default value is `WEBVIEWS`. WebViews are masked by default in screenshots to protect potentially sensitive content.
  {% endhint %}

{% hint style="warning" %}

#### Jetpack Compose

Auto Masking is available in Jetpack Compose starting from SDK version 13.4.0
{% endhint %}

This feature automatically masks sensitive data when screenshots are captured while protecting the user's privacy by default. This affects Bugs Reporting, Crash Reporting and Session Replay.

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2Fjv1bNw2rQF4aN0xugx5e%2Fimage.png?alt=media&#x26;token=d748e993-9c3a-4be4-a01a-58227b05beaf" alt=""><figcaption><p><br><em>Example of Masked Text Inputs, Labels, and Media.</em></p></figcaption></figure>

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//build time
Luciq.Builder(this, "{LUCIQ_TOKEN}")
        .setAutoMaskScreenshotsTypes()
        .build()

//runtime
Luciq.setAutoMaskScreenshotsTypes()
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//build time
new Luciq.Builder(this, "{LUCIQ_TOKEN}")
     .setAutoMaskScreenshotsTypes()
     .build();

//runtime
Luciq.setAutoMaskScreenshotsTypes();
```

{% endcode %}
{% endtab %}
{% endtabs %}

Here are all the possible parameters.

{% tabs %}
{% tab title="JavaScript" %}

```
//No Masking Applied
MaskingType.MASK_NOTHING

//Masks text labels, including buttons and titles
MaskingType.LABELS

//Masks images and video
MaskingType.MEDIA

//Masks Text Input
MaskingType.TEXT_INPUTS
```

{% endtab %}
{% endtabs %}

<figure><img src="https://2056309239-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzyyZGn3dXyNyX4fbdQmV%2Fuploads%2F0QM0Ram04Hr5s9BOPMEN%2Fimage.png?alt=media&#x26;token=dc0a1d51-b03c-4bc5-8b3b-0c7b3d86b61c" alt=""><figcaption><p><br>Preview of different masking levels.</p></figcaption></figure>

#### Examples

<table data-full-width="true"><thead><tr><th width="422.49609375">API</th><th>Meaning</th></tr></thead><tbody><tr><td>Java: Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS)<br><br>Kotlin: Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS)</td><td>Mask Text Inputs only.</td></tr><tr><td>Java: Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS)<br><br>Kotlin: Luciq.setAutoMaskScreenshotsTypes(MaskingType.TEXT_INPUTS, MaskingType.LABELS)</td><td>Mask Text Inputs and Labels.</td></tr><tr><td>Java: Luciq.setAutoMaskScreenshotsTypes(MaskingType.MASK_NOTHING)<br><br>Kotlin: Luciq.setAutoMaskScreenshotsTypes(MaskingType.MASK_NOTHING)</td><td>Disable auto masking.</td></tr></tbody></table>

{% hint style="info" %}
The[ Private Views API](#private-views) takes precedence over Auto Masking.
{% endhint %}

## Disabling and Enabling

Repro Steps is by default enabled with screenshots for both bug reporting and session replay and enabled without screenshots for crash reporting.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
val configurations = ReproConfigurations.Builder()
  .setIssueMode(IssueType.All, ReproMode.EnableWithScreenshots)
  .build()

Luciq.setReproConfigurations(configurations)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
ReproConfigurations configurations = new ReproConfigurations.Builder()
                .setIssueMode(IssueType, ReproMode)
                .build();
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can change the value of the Issue Type.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Bug Reporting, Crash Reporting and Session Replay
IssueType.All
//Bug Reporting Only
IssueType.Bug
//Crash Reporting Only
IssueType.Crash
//Session Replay Only
IssueType.SessionReplay
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Bug Reporting, Crash Reporting and Session Replay
IssueType.All
//Bug Reporting Only
IssueType.Bug
//Crash Reporting Only
IssueType.Crash
//Session Replay Only
IssueType.SessionReplay
```

{% endcode %}
{% endtab %}
{% endtabs %}

You can change the value of ReproMode.

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//Enable with Screenshots
ReproMode.EnableWithScreenshots
//Enable with NO Screenshots
ReproMode.EnableWithNoScreenshots
//Disable
ReproMode.Disable
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//Enable with Screenshots
ReproMode.EnableWithScreenshots
//Enable with NO Screenshots
ReproMode.EnableWithNoScreenshots
//Disable
ReproMode.Disable
```

{% endcode %}
{% endtab %}
{% endtabs %}

Then configure the SDK

{% tabs %}
{% tab title="Kotlin" %}
{% code overflow="wrap" %}

```kotlin
//build time
Luciq.Builder(this, "{LUCIQ_TOKEN}")
    .setReproConfigurations(configurations)
    .build()

//runtime
Luciq.setReproConfigurations(configurations)
```

{% endcode %}
{% endtab %}

{% tab title="Java" %}
{% code overflow="wrap" %}

```java
//build time
new Luciq.Builder(this, "{LUCIQ_TOKEN}")
                .setReproConfigurations(configurations)
                .build();
//runtime 
Luciq.setReproConfigurations(configurations);
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Examples

<table data-full-width="true"><thead><tr><th width="490.88671875">API</th><th>Meaning</th></tr></thead><tbody><tr><td><strong>Java:</strong> ReproConfigurations configurations = new ReproConfigurations.Builder()<br>.setIssueMode(IssueType.All, ReproMode.EnableWithScreenshots)<br>.build();<br><br>Luciq.setReproConfigurations(configurations);<br><br><strong>Kotlin:</strong> val configurations = ReproConfigurations.Builder()<br>.setIssueMode(IssueType.All, ReproMode.EnableWithScreenshots)<br>.build()<br><br>Luciq.setReproConfigurations(configurations)</td><td>Enable with Screenshots for both Bug Reporting and Crash Reporting.</td></tr><tr><td><strong>Java:</strong> ReproConfigurations configurations = new ReproConfigurations.Builder()<br>.setIssueMode(IssueType.Crash, ReproMode.EnableWithNoScreenshots)<br>.build();<br><br>Luciq.setReproConfigurations(configurations);<br><br><strong>Kotlin:</strong> val configurations = ReproConfigurations.Builder()<br>.setIssueMode(IssueType.Crash, ReproMode.EnableWithNoScreenshots)<br>.build()<br><br>Luciq.setReproConfigurations(configurations)</td><td>Enable with No Screenshots for Crash Reporting.</td></tr><tr><td><strong>Java:</strong> ReproConfigurations configurations = new ReproConfigurations.Builder()<br>.setIssueMode(IssueType.Bug, ReproMode.EnableWithScreenshots)<br>.build();<br><br>Luciq.setReproConfigurations(configurations);<br><br><strong>Kotlin:</strong> val configurations = ReproConfigurations.Builder()<br>.setIssueMode(IssueType.Bug, ReproMode.EnableWithScreenshots)<br>.build()<br><br>Luciq.setReproConfigurations(configurations)</td><td>Enable with Screenshots for Bug Reporting.</td></tr><tr><td><strong>Java:</strong> ReproConfigurations configurations = new ReproConfigurations.Builder()<br>.setIssueMode(IssueType.All, ReproMode.Disable)<br>.build();<br><br>Luciq.setReproConfigurations(configurations);<br><br><strong>Kotlin:</strong> val configurations = ReproConfigurations.Builder()<br>.setIssueMode(IssueType.All, ReproMode.Disable)<br>.build()<br><br>Luciq.setReproConfigurations(configurations)</td><td>Completely disable for both Bug Reporting and Crash Reporting.</td></tr></tbody></table>

{% hint style="success" %}

#### Screenshots are by default disabled for Crash Reporting.

For Crash Reporting, screenshots are by default disabled; however, if you are looking to enable screenshots in Crash Reporting, make sure to use the Auto Masking API. This API will automatically help you mask sensitive data in screenshots to protect the end-users' privacy.
{% endhint %}

## Handling Screenshots and Mitigating Overhead

If screenshots are enabled, we capture a screenshot whenever a screen is changed, then attach this info to Crash Reporting and Session Replay. However, we have mitigation methods to avoid causing performance overhead on the device. If this happens, we pause the screenshot-capturing process when we detect that the device has **any of the following states**, and continue capturing screenshots after the device returns to normal:

1. High CPU throughput
2. High RAM utilization
3. Low-disk storage
