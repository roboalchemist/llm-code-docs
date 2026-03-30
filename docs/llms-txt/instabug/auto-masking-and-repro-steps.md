# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/logs-and-profiling/auto-masking-and-repro-steps.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/logs-and-profiling/auto-masking-and-repro-steps.md

# Auto-masking & Repro Steps

Repro Steps show you all of the interactions a user makes with your app up until a bug or crash is reported, grouped by app view. For each view that a user visits, all of the steps that they commit within those views are captured and displayed as a log, grouped by view.

An example of Repro Steps in the Luciq dashboard.

### Getting Started

To enable Luciq's user steps and privacy features for Flutter, you must wrap your root application widget with the `LuciqWidget`. This is a mandatory step for these features to function correctly.

{% code title="Dart" %}

```dart
import 'package:luciq_flutter/luciq_flutter.dart';

void main() {
  runApp(
    LuciqWidget(
      child: MyApp(),
    ),
  );
}
```

{% endcode %}

### Configuration

The `LuciqWidget` provides several options to configure its behavior at initialization.

{% code title="Dart" %}

```dart
LuciqWidget(
  enablePrivateViews: true,
  enableUserSteps: true,
  automasking: const [
    AutoMasking.labels,
    AutoMasking.textInputs,
    AutoMasking.media
  ],
  child: MyApp(),
),
```

{% endcode %}

* `enablePrivateViews`: A boolean that enables or disables the Private Views feature. It is enabled by default.
* `enableUserSteps`: A boolean that enables or disables the User Steps feature (which is used in ReproSteps). It is enabled by default.
* `automasking`: A list that enables Auto Masking for specific types of views. By default, no auto masking is applied.

### Setting Up Repro Steps

To enable Repro Steps, add `LuciqNavigatorObserver` to the `navigatorObservers` as shown below:

{% code title="Dart" %}

```dart
runApp(MaterialApp(
  navigatorObservers: [LuciqNavigatorObserver()],
));
```

{% endcode %}

### Logged Data

#### Captured Events

**UI Interactions**

For the following gestures, only the gesture is logged and displayed:

* Swipe
* Scroll
* Pinch
* Tap
* Force touch
* Double tap
* Enabling/disabling a switch
* Changing the value of a slider
* Editing a text field

**Lifecycle Events**

Whenever one of the following lifecycle events occurs, it will be captured and shown on the timeline:

* Application is moved to the background
* Application is moved to the foreground
* Application becomes active
* Application becomes inactive
* Memory warning

#### Extra Details

Depending on the event, further details are displayed as part of the log statement.

* **Tap, double tap, and force touch:** the SDK always tries to first capture the text rendered inside the UI that the user is interacting with, then it falls back to capturing the icon only with the buttons and navigation items, then it falls back to the accessibility labels.
* **Switch:** both the accessibility label as well as whether the user enabled or disabled the switch are logged.
* **Slider:** both the accessibility label as well as the value that the user moves the slider to are captured.
* **Text fields:** first, the SDK tries to capture the placeholder, then it falls back to the accessibility label.

#### Examples

Here are some examples of how steps look like:

* `Tapped on the button "Send"`
* `Double tapped on UI that contains "Instructions"`
* `Started editing “Password“`
* `Enabled the switch “Push Notifications“`
* `Moved the slider “Text Size“ to 10%`
* `App went to the background`
* `App became active`
* `Memory warning`

### User Privacy

#### Disclaimer

A disclaimer will be shown at the bottom of the report. It helps your users view all the screenshots taken for the Repro Steps before sending a report and can delete them as well.

<details>

<summary>Repro Steps Disclaimer screenshot</summary>

![](https://content.gitbook.com/content/XBLFPXoq7NuMGLdJ6oPk/blobs/cugogftkSWHkm3ojXxrF/c17f12f146208dd87686707af4bcb2ba03296ca5c035904254a406ca30da086c%20flutter%20repro%20steps%202.png)

</details>

### Private Views

You can mark any specific widget that might contain sensitive information as private. Any private view will automatically appear with a black overlay covering it in any screenshot. This feature must be enabled via the `enablePrivateViews` flag in the `LuciqWidget` (enabled by default).

To make a widget private, wrap it with the `LuciqPrivateView` widget.

{% code title="Dart" %}

```dart
LuciqPrivateView(
  child: TextFormField(
    decoration: const InputDecoration(hintText: "Password"),
    obscureText: true,
  ),
),
```

{% endcode %}

For widgets within a scrollable list, such as a `ListView` or `CustomScrollView`, use the `LuciqSliverPrivateView` to ensure privacy for sliver widgets.

{% code title="Dart" %}

```dart
LuciqSliverPrivateView(
  child: SliverFillRemaining(
    child: Text("This private sliver content will be masked"),
  ),
),
```

{% endcode %}

{% hint style="info" %}
Good to Know

* Screen Recordings: Private Views are **not** masked in screen recordings. For Flutter apps on Android, you can use Android's `FLAG_SECURE` to prevent screen capture of sensitive views.
* On iOS they are masked for both screenshots (in ReproSteps) & screen recordings.
* Animated Views: Private Views will be masked in both static and animated states. However, very rapid animations may occasionally not be masked correctly.
  {% endhint %}

### Auto Masking

This feature automatically masks sensitive data when screenshots are captured, protecting your users' privacy by default. To enable Auto Masking, pass a list of `AutoMasking` types to the `automasking` parameter in the `LuciqWidget`.

Example enabling masking for text input fields and text labels:

{% code title="Dart" %}

```dart
void main() {
  runApp(
    LuciqWidget(
      automasking: const [
        AutoMasking.labels,
        AutoMasking.textInputs,
      ],
      child: MyApp(),
    ),
  );
}
```

{% endcode %}

All possible parameters you can pass in the list:

| Parameter                | Description                                     |
| ------------------------ | ----------------------------------------------- |
| `AutoMasking.textInputs` | Masks text input and text area fields           |
| `AutoMasking.labels`     | Masks text labels, including buttons and titles |
| `AutoMasking.media`      | Masks media previews like images                |

To disable Auto Masking, pass an empty list `[]` to the `automasking` parameter.

{% hint style="info" %}
Note

The `LuciqPrivateView` widget takes precedence over Auto-masking. If you need to ensure a specific view is **always** masked, wrapping it in `LuciqPrivateView` is the recommended approach.
{% endhint %}

### Disabling and Enabling

Repro Steps is by default enabled with screenshots for both bug reporting and session replay and enabled without screenshots for crash reporting.

{% code title="Dart" %}

```dart
Luciq.setReproStepsConfig(
  bug: ReproStepsMode.enabled,
  crash: ReproStepsMode.enabledWithNoScreenshots,
  sessionReplay: ReproStepsMode.enabled,
);
```

{% endcode %}

To configure Repro Steps, use the `Luciq.setReproStepsConfig()` method. You can configure the desired mode for bug reports, crash reports, and session replay separately using the `bug`, `crash`, and `sessionReplay` parameters — or configure all of them using the `all` parameter, which overrides `bug`, `crash`, and `sessionReplay`.

{% code title="Dart" %}

```dart
Luciq.setReproStepsConfig(
  all: ReproStepsMode.enabled,
);
```

{% endcode %}

Possible Arguments:

{% code title="Dart" %}

```dart
// Enable Repro Steps with screenshots
ReproStepsMode.enabled

// Enable Repro Steps without screenshots
ReproStepsMode.enabledWithNoScreenshots

// Disable Repro Steps
ReproStepsMode.disabled
```

{% endcode %}

#### Examples

| API                                                                                                                                                                                            | Meaning                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Luciq.setReproStepsConfig(all: ReproStepsMode.enabled)` or `Luciq.setReproStepsConfig(bug: ReproStepsMode.enabled, crash: ReproStepsMode.enabled, sessionReplay: ReproStepsMode.enabled);`    | Enabled with screenshots for Bug Reporting, Crash Reporting, and Session Replay. When the `all` value is present, it overrides the other arguments.                       |
| `Luciq.setReproStepsConfig(crash: ReproStepsMode.enabledWithNoScreenshots)`                                                                                                                    | Enabled with no screenshots for Crash Reporting. (Bug Reporting and Session Replay still retain the default value enabled)                                                |
| `Luciq.setReproStepsConfig(bug: ReproStepsMode.enabled)`                                                                                                                                       | Enabled with screenshot for Bug Reporting. (Crash Reporting and Session Replay still retain their default values of enabled without screenshots and enabled respectively) |
| `Luciq.setReproStepsConfig(all: ReproStepsMode.disabled)` or `Luciq.setReproStepsConfig(bug: ReproStepsMode.disabled, crash: ReproStepsMode.disabled, sessionReplay: ReproStepsMode.disabled)` | Completely disabled for Bug Reporting, Crash Reporting, and Session Replay.                                                                                               |

{% hint style="info" %}
Screenshots are always disabled with Crash Reporting.

For Crash Reporting, screenshots are always disabled as the data is silently collected without any interaction from the user. This decision is part of our ongoing commitment to end-users' privacy.
{% endhint %}
