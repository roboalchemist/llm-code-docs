# Source: https://docs.logrocket.com/reference/expo-capture-custom-fonts.md

# Capture Custom Fonts

Instructions to capture custom font files for display in session replay for Expo apps on Android and iOS.

If you use custom fonts in [Android](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml) or [iOS](https://developer.apple.com/documentation/uikit/text_display_and_fonts/adding_a_custom_font_to_your_app), and notice missing icons or incorrectly sized text in Session Replay, you may want to follow these instructions to upload your fonts on release builds. This will enable custom fonts to display in Session Replay. Custom font replay using the LogRocket Expo plugin requires a minimum SDK version of 1.37.1.

All of the steps below assume that you have already [installed the LogRocket SDK](https://docs.logrocket.com/reference/expo#adding-the-sdk)

See more information about custom fonts in React-Native [here](https://docs.logrocket.com/reference/react-native-capture-custom-fonts)

# Android

## Configure the plugin

In your `app.json` or (`app.config.js`) add the following configuration for the LogRocket plugin:

```Text app.json
{
  "expo": {
    "plugins": [
      // ... your other existing plugins
      [
        "@logrocket/react-native",
      	{
          // ... your other existing LogRocket plugin settings
          "android": {
            "assetCapture": {
              "apiKey": "<PROJECT_API_KEY>",
              "enabledVariants": <ARRAY_OF_BUILD_VARIANTS>,
              "assetDirs": <ARRAY_OF_DIRECTORIES>
            }
          }
        }
      ]
    ]
  }
}
```

```Text app.config.js
export default {
  expo: {
    plugins: [
      // ... your other existing plugins
      [
        '@logrocket/react-native',
        {
          // ... your other existing LogRocket plugin settings
          android: {
            assetCapture: {
              apiKey: "<PROJECT_API_KEY>",
              enabledVariants: <ARRAY_OF_BUILD_VARIANTS>,
              assetDirs: <ARRAY_OF_DIRECTORIES>
            }
          },
        },
      ],
    ],
  },
};
```

* `android.assetCapture.apiKey` - **REQUIRED** - The API key found in `General Settings > Development > API key` within the corresponding LogRocket project
* `android.assetCapture.enabledVariants` - *OPTIONAL* - An array of build variants that should have custom font support enabled. Defaults to `["release"]`
* `android.assetCapture.assetDirs` - *OPTIONAL* - An array of paths to folders that should be checked for font resources to upload. By default LogRocket checks `app/src/main/res/font` and `app/src/main/assets` so those directories don't need to be added to this configuration setting.

## Font resource location

For React Native we capture fonts that have been installed into the Android application at `android/app/src/main/assets/fonts`. In order to ensure font files are installed in that location you need to use the [expo-font config plugin](https://docs.expo.dev/develop/user-interface/fonts/#with-expo-font-config-plugin) instead of the [`useFonts` hook](https://docs.expo.dev/develop/user-interface/fonts/#with-usefonts-hook).

# iOS

## Get the `logrocket-cli` binary

Follow the [steps specified in the iOS custom font capture documentation](https://docs.logrocket.com/reference/ios-capture-custom-fonts#get-logrocket-cli-binary) to download the LogRocket CLI and make it globally available for executation.

## Configure the plugin

In your `app.json` or (`app.config.js`) add the following configuration for the LogRocket plugin:

```Text app.json
{
  "expo": {
    "plugins": [
      // ... your other existing plugins
      [
        "@logrocket/react-native",
      	{
          // ... your other existing LogRocket plugin settings
          "ios": {
            "assetCapture": {
              "apiKey": "<PROJECT_API_KEY>",
              "assetDirectory": "<ASSET_DIRECTORY_PATH>",
              "cliPath": "<CLI_PATH>",
              "enabledBuildConfigs": <ARRAY_OF_BUILD_CONFIGS>
            }
          }
        }
      ]
    ]
  }
}
```

```Text app.config.js
export default {
  expo: {
    plugins: [
      // ... your other existing plugins
      [
        '@logrocket/react-native',
        {
          // ... your other existing LogRocket plugin settings
          android: {
            assetCapture: {
              apiKey: "<PROJECT_API_KEY>",
              assetDirectory: "<ASSET_DIRECTORY_PATH>",
              cliPath: "<CLI_PATH>",
              enabledBuildConfigs: <ARRAY_OF_BUILD_CONFIGS>
            }
          },
        },
      ],
    ],
  },
};
```

* `ios.assetCapture.apiKey` - **REQUIRED** - The API key found in `General Settings > Development > API key` within the corresponding LogRocket project
* `ios.assetCapture.assetDirectory` - **REQUIRED** - The path to the directory in which all custom fonts for the application can be found. If more than one directory contains custom fonts for the application then list all directory paths with a space between each path
* `ios.assetCapture.cliPath` - *OPTIONAL* - Path to where the LogRocket CLI was installed. NOTE: If you didn't [add the CLI to your `PATH` environment variable](https://docs.logrocket.com/reference/ios-capture-custom-fonts#make-cli-available-globally-for-execution) then this setting is **REQUIRED**.
* `ios.assetCapture.enabledBuildConfigs` - *OPTIONAL* - An array of build configurations that should have custom font support enabled. Defaults to `["Release"]`

## Building with EAS

If you are using the Expo Application Service (EAS) to build and deploy your iOS mobile app then you will need to take an additional step to ensure the LogRocket CLI is available to EAS during the build process. To do this include the LogRocket CLI executable in your Expo project (ex. at `/utils/logrocket-cli`) so that it gets included in the project archive that gets uploaded to EAS for the build. Then just make sure to reference the CLI using a path relative to the `ios` folder when defining `cliPath` in the configuration (ex. `../utils/logrocket-cli`).