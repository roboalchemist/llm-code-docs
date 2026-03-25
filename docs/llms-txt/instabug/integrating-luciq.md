# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/integrating-luciq.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/integrating-luciq.md

# Integrate Luciq on Flutter

### Installation

This installation process will install the Luciq SDK that supports [Bug Reporting](https://www.luciq.ai/product/bug-reporting), [Crash Reporting](https://www.luciq.ai/product/crash-reporting) and [App Performance Monitoring](https://www.luciq.ai/product/app-performance-monitoring).

{% stepper %}
{% step %}

#### Add Luciq to pubspec.yaml

Add Luciq to your `pubspec.yaml` file:

{% code title="YAML" %}

```yaml
dependencies:
  luciq_flutter:
```

{% endcode %}
{% endstep %}

{% step %}

#### Install packages

Run the following command to install the package:

{% code title="Shell" %}

```shell
flutter packages get
```

{% endcode %}
{% endstep %}

{% step %}

#### Import Luciq

Import Luciq into your Flutter application:

{% code title="Dart" %}

```dart
import 'package:luciq_flutter/luciq_flutter.dart';
```

{% endcode %}
{% endstep %}

{% step %}

#### Initialize the SDK

Initialize the SDK in `initState()`. This enables the SDK with default behavior and sets invocation on device shake.

{% code title="Dart" %}

```dart
// Make sure to replace APP_TOKEN with your application token.
Luciq.init(
  token: 'APP_TOKEN',
  invocationEvents: [InvocationEvent.shake],
);
```

{% endcode %}

You can find your app token by selecting **SDK Integration** in the **Settings** menu from your [**Luciq dashboard**](https://dashboard.luciq.ai/dashboard/).

![](https://content.gitbook.com/content/XBLFPXoq7NuMGLdJ6oPk/blobs/LAEnjONL0x1uU3TAtXM3/8b9e6ecdb752fca961d275d6df23a2eaba112e57266be9bcd40814051827abed%20flutter%20integration%201.png)
{% endstep %}
{% endstepper %}

### Managing Permissions

{% hint style="warning" %}
Permissions are required. The permissions below are required in order for you to receive attachments (images, videos, audio) from your users through the Luciq SDK.
{% endhint %}

#### iOS

Luciq needs access to the device microphone and photo library to let users add audio, image, and video attachments. Starting from iOS 10, apps that don’t provide a usage description for those two permissions will be rejected when submitted to the App Store.

Add the following keys to your app’s `Info.plist` file with text explaining why those permissions are needed:

* `NSMicrophoneUsageDescription`
* `NSPhotoLibraryUsageDescription`

If your app doesn’t already access the microphone or photo library, recommended usage descriptions:

* " needs access to your microphone so you can attach voice notes."
* " needs access to your photo library so you can attach images."

The permission alert for accessing the microphone/photo library will NOT appear unless users attempt to attach a voice note/photo while using Luciq.

#### Android

Permissions are automatically added to your `AndroidManifest.xml` file. Some are required to fetch information like network and WiFi connection. Others allow users to attach images, videos, and audio recordings. In general, permission requests don't appear unless the user attempts to use a feature requiring a permission.

The only exception is if you set the [invocation event](https://docs.luciq.ai/docs/flutter-invocation) to be a Screenshot. In that case, the storage permission will be requested when your application launches. The screenshot invocation is a special case because there is no native event that tells the SDK that a screenshot has been captured. The only way to know is to monitor the screenshots directory. The SDK is invoked when a screenshot is added to the directory while your application is active.

You can remove any of the permissions if you will not be using the feature associated with it.
