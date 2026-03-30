# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/integrate-luciq-on-react-native/integrate-luciq-with-expo.md

# Integrate Luciq with Expo

### Overview

Luciq supports modern Expo development. The recommended way to install Luciq is by using our **Expo Plugin**, which automatically handles native project configuration and automates the sourcemap uploading process for your standard builds.

{% hint style="info" %}
The Luciq SDK is not supported in the Expo Go app. You will need to create a development build or use a simulator/physical device.
{% endhint %}

### Recommended Setup: Using the Expo Plugin

This is the simplest and most robust way to integrate Luciq into an Expo project.

{% stepper %}
{% step %}

#### Install the SDK

In your project directory, install the Luciq SDK.

{% tabs %}
{% tab title="npm" %}
{% code title="Install (npm)" %}

```
npm install @luciq/react-native
```

{% endcode %}
{% endtab %}

{% tab title="yarn" %}
{% code title="Install (yarn)" %}

```
yarn add @luciq/react-native
```

{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}

#### Configure the Expo Plugin

Add the `@luciq/react-native` plugin to the `plugins` array in your `app.json` file.

{% code title="app.json" %}

```json
{
  "expo": {
    "plugins": [
      [
        "@luciq/react-native",
        {
          "addScreenRecordingBugReportingPermission": true //check note below
        }
      ]
    ]
  }
}
```

{% endcode %}

The `addScreenRecordingBugReportingPermission` is an optional helper that automatically adds the required microphone and photo library permissions on iOS and the foreground service permission on Android for the screen recording feature.
{% endstep %}

{% step %}

#### Rebuild Your App

After adding the plugin, rebuild your app's native directories for the changes to take effect.

{% code title="Rebuild (local)" %}

```
npx expo prebuild
```

{% endcode %}

{% hint style="info" %}
This command is for local development. If you are using EAS Build, this step is handled automatically for you during the build process.

This command will modify your `ios` and `android` directories to include the necessary Luciq configurations.
{% endhint %}
{% endstep %}
{% endstepper %}

### Automatic Sourcemap Uploads

A key benefit of using the Expo Plugin is that it **automatically handles sourcemap uploads** for all your standard Expo builds (`eas build`). By adding the plugin to your `app.json`, it will detect your builds and upload the correct sourcemaps to Luciq with no additional configuration required.

{% hint style="info" %}
This automatic process applies to standard builds only. For **Expo Updates (OTA)**, you must manually upload sourcemaps using our CLI. See our [Over-the-Air (OTA) Updates Guide](https://docs.luciq.ai/react-native/setup-luciq-for-react-native/integrate-luciq-on-react-native/broken-reference) for more details.
{% endhint %}

### Using Luciq

To start using Luciq, import and initialize the SDK in your app’s main file (e.g. `App.js`).

{% code title="App.js" %}

```javascript
import Luciq, { InvocationEvent } from '@luciq/react-native';

Luciq.init({
  token: 'APP_TOKEN',
  invocationEvents: [InvocationEvent.shake],
});
```

{% endcode %}

You can find your app token by selecting **SDK Integration** in the **Settings** menu from your Luciq dashboard.

### Legacy: Using a Custom Development Client

For older managed workflows that do not use the Expo plugin system, you will need to use Expo’s custom development client.

{% stepper %}
{% step %}
Run the dev client package install:

{% code title="Install expo-dev-client" %}

```
npx expo install expo-dev-client
```

{% endcode %}
{% endstep %}

{% step %}
Modify your `package.json` scripts to use the `--dev-client` flag for the start command.

{% code title="package.json (scripts)" %}

```json
"scripts": {
  "start": "expo start --dev-client",
  "android": "expo run:android",
  "ios": "expo run:ios"
}
```

{% endcode %}
{% endstep %}

{% step %}
Proceed with the Luciq SDK installation and initialization as described above.
{% endstep %}
{% endstepper %}
