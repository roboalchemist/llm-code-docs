# Source: https://docs.logrocket.com/reference/react-native.md

# Initialize SDK

Initialize LogRocket and start recording sessions

Call `init()` with your appID to configure and start LogRocket. You can find your appID on [https://app.logrocket.com](https://app.logrocket.com) under Settings > Project Setup.

##

### Adding the SDK

Our React Native package is available on NPM. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```sh
npm install --save @logrocket/react-native
```

> 📘
>
> When installing the LogRocket React Native package in a project you may see warnings about there being unmet peer dependencies due to the `expo` and/or `expo-build-properties` packages not being provided. These warnings can be disregarded if Expo isn't being used for this project.

### Preparing Android

In order for our Android Native SDK to be added to the application a small change must be made to the `android/build.gradle` file: find the `repositories` block under and add our maven repository. This must be added in the `repositories` section under `allprojects` and NOT in the `buildscript` section.

```gradle
allprojects {
  repositories {
    // Add this declaration to any existing repositories block. Do not remove any existing entries in the block.
    maven { url "https://storage.googleapis.com/logrocket-maven/" }
  }
}
```

### Preparing iOS

Our iOS Native SDK is provided through [CocoaPods](https://cocoapods.org) and must be added to the iOS project via `pod install`, or using the `pod-install` helper.

First update your `Podfile` to use the correct iOS version with `platform :ios, '12.0'` (or greater) and then run the following:

```sh
npx pod-install
```

### Initializing the SDK

Initializing the SDK is as simple as importing the package and running the initialization method.  A good place to initialize the SDK is in a `useEffect` hook in your top-level Application component.

Replace `<APP_SLUG>` with your LogRocket application slug, located in our [dashboard's quick start guides](https://app.logrocket.com/r/settings/setup).

```typescript
import React, { useEffect } from 'react';
import LogRocket from '@logrocket/react-native';

const App = () => {
  useEffect(() => {
    LogRocket.init('<APP_SLUG>');
  }, []);
  // Your application entry
};
```

> 📘 React Native New Architecture
>
> The LogRocket React Native SDK supports React Native's New Architecture (the default as of React Native 0.76) as of version 1.46.4. For apps that use the LogRocket React Native SDK's view redaction features and are transitioning to the New Architecture, we recommend reviewing the [redaction documentation](https://docs.logrocket.com/reference/react-native-redaction-tags) for important changes that may be necessary as part of your transition.