# Source: https://docs.logrocket.com/reference/react-native-expo-adding-the-sdk.md

# Adding The SDK

### Expo Web

For Expo web deployments, the LogRocket Javascript Web SDK must be used. See our [web Quickstart](https://docs.logrocket.com/docs/quickstart) and follow Web SDK guides from there. Note that the Web SDK can only be imported in Web builds of your app.

### Expo Mobile

Our React Native package is available on NPM. New releases of the LogRocket Native SDKs are catalogued on our [Mobile SDK Changelog](https://docs.logrocket.com/docs/mobile-sdk-changelog).

```sh Shell
npx expo install @logrocket/react-native expo-build-properties
```

And then edit your `app.json` (or `app.config.js`) to include our SDK in the plugins list:

```json app.json
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

> 🚧
>
> For Expo SDK version 50 and below you will need to set this additional `expo-build-properties` configuration for Android as well:
>
> ```Text app.json
> {
>   "expo": {
>     "plugins": [
>       // ... your other existing plugins
>       [
>         "expo-build-properties",
>       	{
>           // ... other build-properties plugin settings
>           "android": {
>             // ... other android settings
>             "extraMavenRepos": [
>               "https://storage.googleapis.com/logrocket-maven/"
>             ]
>           }
>         }
>       ]
>     ]
>   }
> }
> ```
>
> ```Text app.config.js
> export default {
>   expo: {
>     plugins: [
>       // ... your other existing plugins
>       [
>         'expo-build-properties',
>         {
>           // ... other build-properties plugin settings
>           android: {
>             // ... other android settings
>             extraMavenRepos: [
>               'https://storage.googleapis.com/logrocket-maven/'
>             ],
>           },
>         },
>       ],
>     ],
>   },
> };
> ```
>
> If you are seeing errors that indicate that the LogRocket package cannot be found in any maven repositories then run `npx expo prebuild --clean --platform android` to clear out the existing native android build artifacts and then try re-building the project.