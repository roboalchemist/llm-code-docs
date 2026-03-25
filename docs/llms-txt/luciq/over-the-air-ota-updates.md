# Source: https://docs.luciq.ai/react-native/over-the-air-ota-updates.md

# Over-The-Air (OTA) Updates

### Overview

Over-the-air (OTA) updates are a great way to deliver new code to your users without requiring a full app store release. To ensure your bug and crash reports are correctly associated with the right code version, Luciq needs to be made aware of these OTA updates.

### Configuring Your OTA Version

We provide a single, unified API to track your OTA updates, whether you are using EAS Update or CodePush.

#### EAS Update

Luciq provides support for apps using **EAS Update**. This allows you to see a specific EAS Update's build ID in all your reports, helping you track issues with precision.

#### Setup

To track your EAS Update, pass the `overAirVersion` object with the `service` and `version` parameters during SDK initialization.

{% code title="JavaScript" %}

```javascript
import Luciq, { OverAirUpdateServices } from '@luciq/react-native';

// First, initialize the SDK
Luciq.init({
  token: '<YOUR_APP_TOKEN>',
  invocationEvents: [InvocationEvent.shake],
});

// Then, set your OTA version
Luciq.setOverAirVersion({ 
  service: OverAirUpdateServices.expo, 
  version: '<Your-Build-ID>' 
});
```

{% endcode %}

The `service` parameter accepts two enum values:

* `OverAirUpdateServices.expo`: For teams using EAS Update.
* `OverAirUpdateServices.codePush`: For teams using CodePush.

{% hint style="warning" %}

#### Character Limit

The total combined length of your app version and the EAS Update Build ID should not exceed **40 characters**. Any characters beyond this limit will be trimmed.
{% endhint %}

## Uploading Sourcemaps

{% hint style="warning" %}
Uploading sourcemaps should work automatically by adding our Expo plugin `@luciq/react-native` in your `app.json` **for standard Expo builds** (`eas build`).

However, **for EAS Update**, you must use the manual CLI command provided below to upload sourcemaps.
{% endhint %}

{% code title="CLI" %}

```
Usage: luciq upload-eas-updates-sourcemaps [options]

Options:
  -f, --file <path>          The path of eas update folder (default: "dist")
  -t, --token <value>        Your App Token (env: LUCIQ_APP_TOKEN)
  -n, --name <value>         The app version name (env: LUCIQ_APP_VERSION_NAME)
  -c, --code <value>         The app version code (env: LUCIQ_APP_VERSION_CODE)
  --androidUpdateId <value>  The Eas android Update id 
  --iosUpdateId <value>      The Eas ios Update id
```

{% endcode %}

## CodePush (Legacy)

For teams still using the older `codePushVersion` parameter within the `Luciq.init` method, it will continue to be supported.

{% code title="JavaScript" %}

```javascript
// Deprecated but still supported
Luciq.init({
  token: '<User-App-token>',
  codePushVersion: '<Code-push-version>',
  invocationEvents: [<Invocation-events>],
});
```

{% endcode %}

We recommend migrating to the new, unified `setOverAirVersion` API for a more consistent approach.

{% hint style="warning" %}

#### API Precedence

The new API, `setOverAirVersion`, has been created to handle both Expo and CodePush versions.

* It accepts two values: `.expo` or `.codePush` - legacy `.codePush` is still supported.
* If you call both the new `setOverAirVersion` API and use the legacy `codePushVersion` parameter, the SDK will always honor the **most recently called API**. For example, if you set the `codePushVersion` and then call `setOverAirVersion` later, the value from `setOverAirVersion` will be used.
  {% endhint %}
