# Source: https://docs.logrocket.com/reference/configure-reactnative-sdk.md

# Configure React Native SDK

Getting started is easy:

1. **Connect your app**\
   Visit [https://app.logrocket.com](https://app.logrocket.com) to create an app ID - this links your app to your LogRocket workspace

2. **Add the SDK**\
   [Initialize the SDK](https://docs.logrocket.com/reference/react-native) in your application to start recording sessions. You only need to initialize the SDK once using our React Native SDK. There’s no need to separately initialize the iOS or Android native SDKs. If you use Expo, follow [these initialization steps for Expo](https://docs.logrocket.com/reference/react-native-expo-adding-the-sdk#/)

3. **Protect sensitive data**\
   Sanitize your data before sending it to LogRocket. Control exactly what LogRocket records - easily exclude [UI elements](https://docs.logrocket.com/reference/react-native-redaction-tags), [text](https://docs.logrocket.com/reference/react-native-automatically-sanitize-text), or [network data ](https://docs.logrocket.com/reference/react-native-network) that shouldn't appear in session replays

Get the most out of LogRocket - follow the steps below to unlock deeper insights:

1. **Identify Users**\
   [Associate sessions with known users](https://docs.logrocket.com/reference/react-native-identify) for easier search and enhanced analytics

2. **See full stack traces**\
   [Upload](https://docs.logrocket.com/reference/stack-traces-react-native) mapping files for full stack trace visibility - no more guessing which line failed

3. **Capture WebViews**\
   If you use WebViews in your app, [initialize LogRocket on WebViews](https://docs.logrocket.com/reference/webviews-on-react-native) to ensure every page view appears in session replay

4. **Tag key pages**\
   By default, LogRocket captures View Controller (iOS) and Activity (Android) events for navigation tracking - but these don't always reflect every screen you'd consider a "page". Add [custom page tags](https://docs.logrocket.com/reference/capture-custom-pages-reactnative) to make your analytics more meaningful, highlight real user journeys, and pinpoint where users drop off

5. **Upload custom fonts**\
   If you use custom fonts or icons, upload custom fonts so you can see exactly what your users see. Follow instructions here if you use [Expo](https://docs.logrocket.com/reference/expo-capture-custom-fonts#/), or follow the setup instructions for both [iOS](https://docs.logrocket.com/reference/ios-capture-custom-fonts) and [Android](https://docs.logrocket.com/reference/android-capture-custom-fonts) to configure custom fonts on each platform.

6. **Track custom events**\
   While LogRocket automatically captures standard events like clicks and navigation, you can [define custom events](https://docs.logrocket.com/reference/react-native-custom-events#/) to capture anything unique to your app

7. **Manually log errors**
   Add manual logging for [error messages](https://docs.logrocket.com/reference/capture-error-messages-2#/) and [exceptions](https://docs.logrocket.com/reference/capture-exceptions#/) to capture additional debugging details and make issues easier to diagnose

Not seeing what you're looking for? Check out the rest of our React Native documentation for even more granular controls.

> 📘 React Native New Architecture
>
> The LogRocket React Native SDK supports React Native's New Architecture (the default as of React Native 0.76) as of version 1.46.4. For apps that use the LogRocket React Native SDK's view redaction features and are transitioning to the New Architecture, we recommend reviewing the [redaction documentation](https://docs.logrocket.com/reference/react-native-redaction-tags) for important changes that may be necessary as part of your transition.