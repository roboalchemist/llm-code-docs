# Source: https://docs.luciq.ai/flutter/setup-luciq-for-flutter/setup-crash-reporting/crash-free-sessions.md

# Crash-Free Sessions

### Overview

In Flutter, unhandled exceptions can be thrown from two sides:

* Native Side
* Dart/Flutter Side

### User Exceptions

#### Native Exceptions

When a native exception occurs:

* The app crashes.
* The user needs to reopen the app.
* A crash report is sent to the Luciq dashboard.

#### Flutter Exceptions

When a Flutter exception occurs:

* The app does not crash; the user can continue their flow.
* The user may reach a point where the app becomes unresponsive (e.g., a button stops working).
* A crash report is sent to the Luciq dashboard.

### Crash-Free Sessions Calculation

Crash-Free sessions are calculated as follows:

* **Crash Rate** = (Total number of crash occurrences) / (Total number of sessions)
* **Crash-Free Sessions** = 100% - Crash Rate

**Common Issue: Low Crash-Free Session Rate on Flutter**

A low crash-free session rate can occur because:

* A single session might have multiple Flutter crashes.
* Flutter crashes do not terminate the session, leading to multiple crash reports within the same session.

### User Frustration

Users may become frustrated when the app doesn't respond rather than crashing. To mitigate this, consider the following options:

{% stepper %}
{% step %}

#### Terminate the App (Force a Crash)

* Use exit(0) to forcefully close the app.
  {% endstep %}

{% step %}

#### Display a Recoverable Error Alert

* Show an alert message, such as "A problem happened here," to inform the user of the issue.
  {% endstep %}
  {% endstepper %}

### Configuring Flutter Exceptions

Flutter exceptions can be customized to be reported as fatal, non-fatal, or completely ignored.

#### Flutter Crashes as Fatal Crashes

This is done by passing `CrashReporting.reportCrash` to `runZonedGuarded` as shown below:

{% code title="Dart" %}

```dart
void main() {
  runZonedGuarded(() {
    // ...
    // Notice we're using CrashReporting.reportCrash here which reports errors as fatal crashes.
  }, CrashReporting.reportCrash);
}
```

{% endcode %}

#### Flutter Crashes as Non-Fatals

This is done by passing `CrashReporting.reportHandledCrash` to `runZonedGuarded` as shown below:

{% code title="Dart" %}

```dart
void main() {
  runZonedGuarded(() {
    // ...
    // Notice we're using CrashReporting.reportHandledCrash here which reports errors as non-fatal crashes.
  }, CrashReporting.reportHandledCrash);
}
```

{% endcode %}

#### Ignoring Flutter Crashes

This is done by passing a function to `runZonedGuarded` that doesn’t call `CrashReporting.reportCrash` or `CrashReporting.reportHandledCrash` internally as shown below:

{% code title="Dart" %}

```dart
void main() {
  runZonedGuarded(() {
    // ...
    // We're passing a custom callback here to handle errors without reporting them to Luciq.
  }, (Object error, StackTrace stackTrace) {
    // Do whatever is needed with the error
    print(error);
    print(stackTrace);
  });
}
```

{% endcode %}

### Summary of Exception Handling

#### Native Exceptions

* **User Experience**: App crashes, user reopens the app.
* **Reporting**: Native Stacktrace is collected and sent to Luciq.
* **Impact**: One session can contain only one crash.

#### Dart/Flutter Exceptions

* **User Experience**: App does not crash but becomes unresponsive.
* **Reporting**: Dart Stacktrace is collected and sent to Luciq.
* **Impact**: One session can contain multiple crashes.

For more details on managing exceptions and improving crash-free sessions, refer to the Luciq documentation.
