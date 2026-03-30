# Source: https://img.ly/docs/cesdk/react-native/get-started/react-native/existing-project-b9012y/

---
title: "Existing Project Setup"
description: "Setting up CE.SDK in an existing React Native CLI project for both Android and iOS platforms"
platform: react-native
url: "https://img.ly/docs/cesdk/react-native/get-started/react-native/existing-project-b9012y/"
---

> This is one page of the CE.SDK React Native documentation. For a complete overview, see the [React Native Documentation Index](https://img.ly/docs/cesdk/react-native.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/react-native/llms-full.txt).

**Navigation:** [Get Started](https://img.ly/docs/cesdk/react-native/get-started/overview-e18f40/) > [Quickstart React Native](https://img.ly/docs/cesdk/react-native/get-started/react-native/new-project-a5678y/)

---

## Introduction

This guide provides step-by-step instructions for integrating the `@imgly/editor-react-native` module into your existing mobile React Native project. By the end of this guide, you will have a powerful creative editor running in your own React Native application.

> **Note:** Customizing the CreativeEditor SDK for React Native is handled exclusively through native code (Swift/Kotlin), as outlined in our [configuration overview section](https://img.ly/docs/cesdk/react-native/user-interface/customization-72b2f8/).

## Pre-requisites

Before you begin, make sure the following requirements are met:

- A properly configured React Native development environment
- Platform-specific development setup for your target (Android and/or iOS)
- Git CLI installed
- A valid IMG.LY license key - [Get one here](https://img.ly/pricing), pass `null` to run in evaluation mode with watermark.

## Minimum Requirements

- React Native: 0.73
- iOS: 16
- Swift: 6.2 (Xcode 26.0.1)
- Android: 7.0 (Android SDK 24)

## Add Dependency

First, install the `@imgly/editor-react-native` module by running the following command:

```sh
npm install @imgly/editor-react-native
```

## iOS Configuration

If your application is targeting iOS, you will need to make the following changes:

#### Minimum iOS version

Ensure that your app is targeting at least iOS 16. You can do this in the `ios/Podfile` file, by editing this line:

```ruby
platform :ios, '16.0'
```

#### Install Dependencies

Run the following commands to navigate to the `ios/` directory and install the CocoaPods dependencies:

#### Run iOS App

To build and install the app, launch/connect your iOS simulator/device and run:

```sh
npm run ios
```

## Android Configuration

If your application is targeting Android, you will need to make the following changes:

#### Minimum Android SDK

Ensure that the minimum android SDK is set to at least 24. You can do this in the `android/build.gradle` file.

```groovy
minSdkVersion = 24
```

#### IMG.LY Maven Coordinates

You will also need to add the maven coordinates for the IMG.LY repo. This can also be done in the same `android/build.gradle` file.

```groovy
allprojects {
    repositories {
        maven {
            name "IMG.LY Artifactory"
            url "https://artifactory.img.ly/artifactory/maven"
            mavenContent {
                includeGroup("ly.img")
            }
        }
    }
}
```

#### Compose Plugin

Finally, if your version of Kotlin is `2.0.0` or above, you will also need to add the compose plugin dependency in the `dependencies` block of the `android/build.gradle` file. The plugin version you use should be the same as the kotlin version.

```groovy
classpath("org.jetbrains.kotlin.plugin.compose:org.jetbrains.kotlin.plugin.compose.gradle.plugin:$kotlinVersion")
```

#### Run Android App

To build and install the app, launch/connect your android emulator/device and run:

```sh
npm run android
```

## Using the Creative Editor

To finally make use of the editor, call the `IMGLYEditor.openEditor` function with suitable `EditorSettings` and optionally your desired `EditorPreset` passed in:

```typescript
import IMGLYEditor, {
  EditorPreset,
  EditorSettingsModel,
  SourceType,
} from '@imgly/editor-react-native';

export const design_editor_solution = async (): Promise<void> => {
  const settings = new EditorSettingsModel({
    license: 'YOUR_LICENSE_KEY', // pass null for evaluation mode with watermark
    userId: 'UNIQUE_USER_ID',
  });
  const result = await IMGLYEditor?.openEditor(
    settings,
    {
      source: 'test_image.png',
      type: SourceType.IMAGE,
    },
    EditorPreset.DESIGN,
  );
};
```

Within a new file, define an asynchronous function named `design_editor_solution` where you will initialize the `EditorSettingsModel`. After providing your valid license key and an optional unique user ID, pass the configured settings to `IMGLYEditor.openEditor()`. At this point, you can also specify an optional `EditorPreset` to open one of our predefined editor variants.

Optionally provide a `Source` object containing an existing image, video, or scene alongside its corresponding `SourceType` to open the editor with that content; otherwise pass `undefined` and the editor will start blank.

Now, you can launch the editor by calling `design_editor_solution()` from wherever you want to open it from.

## Next Steps

- Explore the available presets tailored to different editor solutions.
- Set up a native interface to customize the editor according to your specific requirements.

## Common Errors

#### Dependency not found

```
Couldn't find any versions for "@imgly/editor-react-native" that matches "^x.xx.x"
```

**Solution** -> Ensure you are using an existing version of the IMG.LY editor.

#### CocoaPods versions not found

```
[!] CocoaPods could not find compatible versions for pod "IMGLYUI":

  In Podfile:

    IMGLYEditorModule (from `../node_modules/@imgly/editor-react-native`) was resolved to 1.51.0, which depends on
```

**Solution**

```
(cd ios && pod repo update)
```

#### Unintegrated swift pods

```
[!] The following Swift pods cannot yet be integrated as static libraries:
The Swift pod `IMGLYEditorModule` depends upon `IMGLYUI`, which does not define modules.
```

**Solution**

```
use_frameworks! :linkage => :static
```



---

## More Resources

- **[React Native Documentation Index](https://img.ly/docs/cesdk/react-native.md)** - Browse all React Native documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/react-native/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/react-native/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
