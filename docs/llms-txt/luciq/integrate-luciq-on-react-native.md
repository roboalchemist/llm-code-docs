# Source: https://docs.luciq.ai/react-native/setup-luciq-for-react-native/integrate-luciq-on-react-native.md

# Integrate Luciq on React Native

This page covers how to install the Luciq SDK in your React Native application.

{% hint style="info" %}
Our React Native SDK support starts from React Native 0.60.x and up to the latest version. We always try to keep our SDK compatible with the latest React Native version while trying to maintain backward-compatibility whenever possible.
{% endhint %}

### Installation

This installation process will install the Luciq SDK that supports Bug reporting, Crash reporting, and Application performance moniroting.

If you are upgrading from versions prior to v11.0, check our migration guide: /docs/react-native-migration-guide

{% stepper %}
{% step %}

### Add the SDK package

Choose your package manager:

{% tabs %}
{% tab title="npm" %}
{% code title="Install with npm" %}

```bash
npm install @luciq/react-native
```

{% endcode %}
{% endtab %}

{% tab title="yarn" %}
{% code title="Install with yarn" %}

```bash
yarn add @luciq/react-native
```

{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}

### iOS — install CocoaPods dependencies

Run the following in your project root:

{% code title="Install CocoaPods (iOS)" %}

```bash
cd ios && pod install && cd ..
```

{% endcode %}
{% endstep %}
{% endstepper %}

### Using Luciq

Import and initialize the SDK in your `index.js` (or main entry) file. The default behavior shows Luciq when the device is shaken; you can customize this via the SDK APIs.

{% code title="index.js" %}

```javascript
import Luciq, { InvocationEvent } from '@luciq/react-native';

Luciq.init({
  token: 'APP_TOKEN',
  invocationEvents: [InvocationEvent.shake],
});
```

{% endcode %}

You can find your app token by selecting **SDK Integration** in the **Settings** menu from your [Luciq dashboard](https://dashboard.luciq.ai/dashboard/).

![](https://content.gitbook.com/content/6lIBifTCHAMDxXnztiBK/blobs/sEQDB1kgIDVkN5vAMOxK/4ae8f0363cec2cd63e5258fc8df995c5ce2183781286438b7bd44fd7e8be7f80%20react%20native%20integration%201.png)

### Managing Permissions

Luciq needs access to the device microphone and photo library to allow users to add audio, image, and video attachments. Starting from iOS 10, apps that don’t provide usage descriptions for these permissions will be rejected by the App Store.

Add the following keys to your app’s `info.plist` with a user-facing explanation:

* NSMicrophoneUsageDescription
* NSPhotoLibraryUsageDescription

Example wording if your app doesn't already access these resources:

* " needs access to your microphone so you can attach voice notes."
* " needs access to your photo library so you can attach images."

{% hint style="info" %}
The permission alert for accessing the microphone/photo library will NOT appear unless users attempt to attach a voice note or photo while using Luciq.
{% endhint %}

{% hint style="warning" %}
Permissions Are Required

The above permissions are required in order for you to receive attachments from your users through the Luciq SDK.
{% endhint %}
