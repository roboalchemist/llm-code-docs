# Source: https://docs.logrocket.com/reference/expo.md

# Expo

The LogRocket SDK for Expo allows you to capture session replays, network requests and logs from Expo applications.

![](https://files.readme.io/cde28af-Image_2021-04-27_at_5.38.32_PM.png "Image 2021-04-27 at 5.38.32 PM.png")

## Quick Start

### Register with LogRocket

Go to [https://logrocket.com/signup](https://logrocket.com/signup) to create a free trial account. If you already have a LogRocket account, you can use your existing account. All LogRocket accounts include 1,000 free mobile sessions.

### Expo Web

For Expo web deployments, the LogRocket Javascript Web SDK must be used. See our [web Quickstart](https://docs.logrocket.com/docs/quickstart) and follow Web SDK guides from there. Note that the Web SDK can only be imported in Web builds of your app.

### Mobile

#### Adding the SDK

Our React Native package is available on NPM. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```sh Shell
npx expo install @logrocket/react-native expo-build-properties
```

And then edit your `app.json` (or `app.config.js`) to include our SDK in the plugins list:

```json
{
  "expo": {
    // ... your existing configuration
    "plugins": [
      	[
          "expo-build-properties",
          {
            "android": {
              "minSdkVersion": 25
            }
          }
        ],
        "@logrocket/react-native"
      ]
  }
}
```

#### Initializing the SDK

Initializing the SDK is as simple as importing the package and running the initialization method.  A good place to initialize the SDK is in a `useEffect` hook in your top-level Application component.

Replace `<APP_SLUG>` with your LogRocket application slug, located in our [dashboard's quick start guides](https://app.logrocket.com/r/settings/setup).

```typescript
import { useEffect } from 'react';
import * as Updates from 'expo-updates';
import LogRocket from '@logrocket/react-native';

const App = () => {
  useEffect(() => {
    LogRocket.init('<APP_SLUG>', {
      updateId: Updates.isEmbeddedLaunch ? null : Updates.updateId,
      expoChannel: Updates.channel,
    });
  }, []);
};
```

## Local Development Limitations

Expo Go, the local development client for the Expo Framework, does not support mobile Native code additions. Our React Native SDK uses Native code to power the entire system, and cannot run in the Expo Go client.

Our SDK will be fully operational when built with either `npx expo run:` as described in the ["Adding custom native code"](https://docs.expo.io/workflow/customizing/) guide or the EAS Build system, which can be [accomplished locally provided the appropriate tooling is available](https://docs.expo.dev/build-reference/local-builds/).

## Further Reading

For more information on using our SDK in React Native check out [our documentation](https://docs.logrocket.com/docs/react-native).