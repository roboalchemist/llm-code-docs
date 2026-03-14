# Source: https://docs.logrocket.com/reference/initialize-flutter.md

# Initialize SDK

Initialize LogRocket and start recording Flutter sessions

## Adding the SDK

Our Flutter SDK is available on [pub.dev](https://pub.dev/). The Flutter SDK includes the most recent LogRocket Native SDKs as dependencies. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```shell
$ flutter pub add logrocket_flutter
```

### Preparing Android

The LogRocket Android SDK requires a min SDK version of 25. Ensure your app's `minSdk` or `minSdkVersion` are set to at least 25.

In order for our Android Native SDK to be added to the application a small change must be made to the `android/build.gradle` file: find the `repositories` block and add our maven repository. This must be added in the `repositories` section under `allprojects` and NOT in the `buildscript` section.

```Text Groovy
allprojects {
  repositories {
    // Add this declaration to any existing repositories block. Do not remove any existing entries in the block.
    maven { url "https://storage.googleapis.com/logrocket-maven/" }
  }
}
```

### Preparing iOS

Our iOS Native SDK is provided through [CocoaPods](https://cocoapods.org/) and must be added to the iOS project via `pod install`, or using the `pod-install` helper.

First, ensure the `Podfile` in your `ios` directory is using the correct iOS version `platform :ios, '12.0'` (or greater) and then run the following:

```shell
pod install --repo-update
```

## Initializing the SDK

The simplest way to initialize the SDK is with `wrapAndInitialize`. This will wrap the application, in order to automatically capture logs and errors, and then immediately initialize a session when the app starts.

```dart Flutter
import 'package:logrocket_flutter/logrocket_flutter.dart'; 

void main() {
  LogRocket.wrapAndInitialize(
    LogRocketWrapConfiguration(),
    LogRocketInitConfiguration(appID: '<APP_SLUG>'),
    () => runApp(MyApp())
  );
}
```

The `wrap` step and `initalize` steps can be separated, in case you would like to delay the start of session recording to sometime after the app starts. `initalize` only needs to be called once to start a session.

```dart Flutter
import 'package:logrocket_flutter/logrocket_flutter.dart';

void main() {
  LogRocket.wrap(
    LogRocketWrapConfiguration(),
    () {
      runApp(MyApp());
    },
  );
}

// This example initializes inside a widget's `initState()`,
// but `LogRocket.initialize` can be called from elsewhere in the app.
class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    LogRocket.initialize(
      LogRocketInitConfiguration(
        appID: '<APP_SLUG>',
      )
    ).then((bool success) => {
      // success will be `true` if a LogRocket session successfully initialized.
      // success will be `false` if an error occurred during initialization.
    });
    super.initState();
  }
  
  // ...
}
```

If you do not wish to automatically capture logs and uncaught errors in LogRocket, the `wrap` call can be skipped.