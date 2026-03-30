# Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk

Title: Flutter SDK Installation

URL Source: https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk

Markdown Content:
Install the Clarity SDK in order to track how users interact with your app. The Clarity Flutter SDK is available as a package (`clarity_flutter`) on [pub.dev](https://pub.dev/packages/clarity_flutter).

To add the package, run the following command:

```
flutter pub add clarity_flutter
```

Import the `clarity_flutter` package in your `main.dart` file.

```
import 'package:clarity_flutter/clarity_flutter.dart';
```

There are two ways to initialize Clarity in your Flutter app:

Use the `Clarity.initialize` function to initialize Clarity manually:

```
import 'package:flutter/material.dart';
import 'package:clarity_flutter/clarity_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  void initState() {
    super.initState();
    _initializeClarity();
  }

  void _initializeClarity() {
    final config = ClarityConfig(
      projectId: "your_project_id"
    );
    
    Clarity.initialize(context, config);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Clarity Flutter SDK Example'),
      ),
      body: Center(
        child: Text('Hello, Clarity!'),
      ),
    );
  }
}
```

Alternatively, you can initialize the `ClarityConfig` object and wrap your app with the `ClarityWidget` widget:

```
import 'package:flutter/material.dart';
import 'package:clarity_flutter/clarity_flutter.dart';

void main() {
  final config = ClarityConfig(
    projectId: "your_project_id"
  );

  runApp(ClarityWidget(
    app: MyApp(),
    clarityConfig: config,
  ));
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Clarity Flutter SDK Example'),
        ),
        body: Center(
          child: Text('Hello, Clarity!'),
        ),
      ),
    );
  }
}
```

> **Note:** When using `Clarity.initialize`, make sure to call it with a valid `BuildContext` after the widget is built, typically in the `initState` method of a StatefulWidget.

After integrating Clarity with your application, ensure the following when testing on a device or a simulator:

1.   Your device or simulator should be connected to the internet.
2.   While testing, consider setting the `logLevel`to `Verbose`. This provides detailed logs that can help identify any integration issues.

Allow approximately 2 hours for complete sessions to appear in your Clarity project. However, in-progress sessions can still be viewed in real time. See [Clarity Recordings in Real Time](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-real-time).

```
final config = ClarityConfig(
  projectId: "your_project_id",
  userId: "your_user_id", // DEPRECATED
  logLevel: LogLevel.Info,
);
```

The unique identifier assigned to your Clarity project. You can find it on the **Settings** page of Clarity dashboard. This ID is essential for routing data to the correct Clarity project.

![Image 1: Copy your Clarity project ID.](https://learn.microsoft.com/en-us/clarity/media/sdk-clarity-project-id.png)

The unique identifier associated with the application user. This ID persists across multiple sessions on the same device.

*   **Deprecated:** This field is deprecated and would be removed in a future major version. Use [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setcustomuserid) as an alternative.
*   If `userId` isn't provided, a Clarity generated user ID is used instead.
*   The `userId` should be base-36 string larger than zero and smaller than `1z141z4`.

Note

For greater flexibility in user identification, use the [`setCustomUserId`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setcustomuserid) API. Ensure that the `customUserId` length is between 1 and 255 characters.

The level of logging to show in the device's Logcat while debugging. Defaults to `LogLevel.Info` if not provided (in debug builds).

Possible values are:

*   `LogLevel.Verbose`: Detailed debug information.
*   `LogLevel.Debug`: Debug information.
*   `LogLevel.Info`: Informational messages.
*   `LogLevel.Warn`: Warning messages.
*   `LogLevel.Error`: Error messages.
*   `LogLevel.None`: No logging.

Note

In non-debug (production) builds, `loglevel` is automatically forced to `None` to eliminate any performance overhead.

The Clarity Flutter SDK provides masking widgets to mask sensitive information in your app. These widgets are `ClarityMask` and `ClarityUnmask`.

Note

Clarity supports masking modes that are applied on the entire app. learn more about [masking modes](https://learn.microsoft.com/en-us/clarity/mobile-sdk/clarity-sdk-masking#masking-modes).

Use `ClarityMask` to mask widgets containing sensitive information.

```
import 'package:flutter/material.dart';
import 'package:clarity_flutter/clarity_flutter.dart';

class MaskedWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ClarityMask(
      child: Text('Sensitive Information'),
    );
  }
}
```

Use `ClarityUnmask` to unmask widgets within a masked area.

```
import 'package:flutter/material.dart';
import 'package:clarity_flutter/clarity_flutter.dart';

class UnmaskedWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ClarityUnmask(
      child: Text('Non-sensitive Information'),
    );
  }
}
```

```
bool Clarity.initialize(BuildContext context, ClarityConfig clarityConfig)
```

Initializes Clarity to start capturing the current session data.

**`context` (BuildContext)**: The BuildContext of the widget tree.

**`clarityConfig` (ClarityConfig)**: The configuration for the Clarity session.

Boolean

`true` if the initialization is possible; otherwise `false`.

*   This function should only be called on the UI Isolate.
*   Make sure to call it with a valid `BuildContext` after the widget is built, typically in the `initState` method of a StatefulWidget.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void _initializeClarity() {
  final config = ClarityConfig(
    projectId: "your_project_id"
  );
  
  Clarity.initialize(context, config);
}
```

```
bool Clarity.setCustomUserId(String customUserId)
```

Sets a custom user ID for the current session. This ID can be used to filter sessions on the Clarity dashboard.

`customUserId` String

The custom user ID to associate with the current session. The value must be a nonempty string with a maximum length of 255 characters and can't consist only of whitespace.

Boolean

`true` if the custom user ID was set successfully; otherwise `false`.

*   To ensure that the custom user ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setonsessionstartedcallback).
*   Unlike the `userID`, the `customUserId` value has fewer restrictions.
*   It's recommended **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.
*   This function should only be called on the UI Isolate.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityUserId() {
  Clarity.setCustomUserId('user_id');
}
```

```
bool Clarity.setCustomTag(String key, String value)
```

Sets a custom tag for the current session. This tag can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`value` String

The value for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Boolean

`true` if the custom tag was set successfully; otherwise `false`.

*   To ensure that the custom tag is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setonsessionstartedcallback).
*   This function should only be called on the UI Isolate.
*   It's recommended **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityCustomTag() {
  Clarity.setCustomTag('custom_tag_key', 'custom_tag_value');
}
```

```
bool Clarity.setCustomTags(String key, Iterable<String> values)
```

Sets one or more custom tag values for the current session. These tags can be used to filter sessions on the Clarity dashboard.

`key` String

The key for the custom tag. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

`values` Iterable<String>

The values to associate with the custom tag. The collection must contain at least one nonempty string. Each value must have a maximum length of 255 characters, can't consist only of whitespace, and duplicate entries are ignored.

Boolean

`true` if the tags were set successfully; otherwise `false`.

*   To ensure that the custom tags are associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setonsessionstartedcallback).
*   This function should only be called on the UI Isolate.
*   Duplicate tag values are ignored.
*   It's recommended **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityCustomTags() {
  Clarity.setCustomTags('custom_tag_key', ['value_a', 'value_b']);
}
```

```
bool Clarity.setCustomSessionId(String customSessionId)
```

Sets a custom session ID for the current session.

`customSessionId` String

The custom session ID to associate with the current session. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace.

Boolean

`true` if the custom session ID was set successfully; otherwise `false`.

*   This function should only be called on the UI Isolate.
*   To ensure that the custom session ID is associated with the correct session, it's recommended to call this function within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setonsessionstartedcallback).
*   It's recommended **not** to set any [Personally Identifiable Information (PII)](https://learn.microsoft.com/en-us/clarity/setup-and-installation/glossary-of-terms) values inside this field.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityCustomSessionId() {
  Clarity.setCustomSessionId('custom_session_id');
}
```

```
SessionStartedCallback = void Function(String sessionId)
bool Clarity.setOnSessionStartedCallback(SessionStartedCallback callback)
```

Sets a callback function that's invoked whenever a new Clarity session starts or an existing session is resumed on app startup.

`callback` void Function(String sessionId)

The callback to be invoked whenever a Clarity session starts - the callback receives the new or resumed session ID as a string parameter.

Boolean

`true` if the callback was set successfully; otherwise `false`.

*   If the callback is set after a session has already started, it's invoked immediately.
*   The specified callback is guaranteed to run on the UI isolate.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityOnSessionStartedCallback() {
  Clarity.setOnSessionStartedCallback((String sessionId) {});
}
```

```
String? Clarity.getCurrentSessionUrl()
```

Gets the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `null`.

String

A string representing the URL of the current Clarity session recording on the Clarity dashboard if a session has already started; otherwise `null`.

*   Initially, this function might return `null` until a Clarity session begins.
*   To ensure a valid session URL, use this method within the callbacks of [`setOnSessionStartedCallback`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#setonsessionstartedcallback).
*   This function should only be called on the UI Isolate.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void getClaritySessionUrl() {
  String? claritySessionUrl = Clarity.getCurrentSessionUrl();
}
```

```
bool Clarity.sendCustomEvent(String value)
```

Sends a custom event to the current Clarity session. These custom events can be used to track specific user interactions or actions that Clarity's built-in event tracking doesn't automatically capture.

`value` String

The name of the custom event. The value must be a nonempty string, with a maximum length of 254 characters, and can't consist only of whitespace.

Boolean

`true` if the custom event was sent successfully; otherwise `false`.

*   This API can be called multiple times per page to track various user actions.
*   Each custom event is logged individually and can be filtered, viewed and analyzed in the Clarity dashboard.
*   This function should only be called on the UI Isolate.
*   It's recommended **not** to set any PII values inside this field.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void sendClarityCustomEvent() {
  Clarity.sendCustomEvent('custom_event');
}
```

```
bool Clarity.setCurrentScreenName(String? screenName)
```

This function allows you to provide a custom screen name that replaces the default screen name.

`screenName` String

The desired screen name. The value must be a nonempty string, with a maximum length of 255 characters, and can't consist only of whitespace. Set to `null` to reset.

Boolean

`true` if the specified screen name was set successfully; otherwise `false`.

*   Clarity starts a new page whenever the screen name changes.
*   This function should only be called on the UI Isolate.
*   To cover all route changes, it is recommended to call this function inside a `RouteObserver`.
*   The custom screen name is set globally and persists across all subsequent activities until explicitly reset.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void setClarityScreenName() {
  Clarity.setCurrentScreenName('screen_name');
}
```

```
SessionStartedCallback = void Function(String sessionId)
bool Clarity.startNewSession(SessionStartedCallback callback)
```

Starts a new Clarity session and ends the current session if one is active.

`callback` void Function(String sessionId)

Invoked when the new session starts. Receives the newly created session ID.

Boolean

`true` if a new session was started successfully; otherwise `false`.

*   This function should only be called on the UI Isolate.
*   The specified callback is guaranteed to run on the UI isolate.
*   Use this API to segment recordings into separate sessions (for example, when a user signs out and a different user signs in).

```
import 'package:clarity_flutter/clarity_flutter.dart';

void restartClaritySession() {
  Clarity.startNewSession((String newSessionId) {
    // Handle the new session ID here.
  });
}
```

```
bool Clarity.pause()
```

Pauses the Clarity session capturing until the [`resume`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#resume) function is called.

Boolean

`true` if Clarity was successfully paused; otherwise `false`.

*   This function should only be called on the UI Isolate.
*   Calling `pause` stops the capture of events and data until [`resume`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#resume) is called.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void pauseClarity() {
  Clarity.pause();
}
```

```
bool Clarity.resume()
```

Resumes the Clarity session capturing only if it was previously paused using the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#pause) function.

Boolean

`true` if Clarity was successfully resumed; otherwise `false`.

*   This function should only be called on the UI Isolate.
*   If the session is not paused, calling `resume` has no effect.

```
import 'package:clarity_flutter/clarity_flutter.dart';

void resumeClarity() {
  Clarity.resume();
}
```

```
bool Clarity.isPaused()
```

Checks if the Clarity session is currently paused.

Boolean

`true` if Clarity session capturing is currently in the paused state based on an earlier call to the [`pause`](https://learn.microsoft.com/en-us/clarity/mobile-sdk/flutter-sdk#pause) function; otherwise `false`.

*   This function should only be called on the UI Isolate.

```
import 'package:clarity_flutter/clarity_flutter.dart';

bool isClarityPaused() {
  return Clarity.isPaused();
}
```

*   Uploading session data while the user is offline is currently not supported on the Flutter SDK. Only session data captured while the user is online is sent.
*   Currently, native view capturing (including web views) is not supported. You can find these views covered in recordings.
*   Font support is limited at the moment. You can find font differences in the recordings.

For any queries, contact [Clarity Apps support](mailto:clarity-apps-support@microsoft.com).

For more answers, refer to [FAQ](https://learn.microsoft.com/en-us/clarity/faq#clarity-for-mobile-apps).
