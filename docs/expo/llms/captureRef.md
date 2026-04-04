# Source: https://docs.expo.dev/versions/latest/sdk/captureRef

---
title: react-native-view-shot
description: A library that allows you to capture a React Native view and save it as an image.
sourceCodeUrl: 'https://github.com/gre/react-native-view-shot'
packageName: react-native-view-shot
platforms: ['android', 'ios', 'expo-go']
inExpoGo: true
---

# react-native-view-shot

A library that allows you to capture a React Native view and save it as an image.
Android, iOS, Included in Expo Go

Given a view, `captureRef` will essentially screenshot that view and return an image for you. This is very useful for things like signature pads, where the user draws something, and then you want to save an image from it.

If you're interested in taking snapshots from the GLView, we recommend you use [GLView's takeSnapshotAsync](/versions/latest/sdk/gl-view#takesnapshotasyncoptions) instead.

## Installation

```sh
npx expo install react-native-view-shot
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project. Then, follow the [installation instructions](https://github.com/gre/react-native-view-shot) provided in the library's README or documentation.

## Note on pixel values

Remember to take the device `PixelRatio` into account. When you work with pixel values in a UI, most of the time those units are "logical pixels" or "device-independent pixels". With images like PNG files, you often work with "physical pixels". You can get the `PixelRatio` of the device using the React Native API: `PixelRatio.get()`

For example, to save a 'FullHD' picture of `1080x1080`, you would do something like this:

```js
const targetPixelCount = 1080; // If you want full HD pictures
const pixelRatio = PixelRatio.get(); // The pixel ratio of the device
// pixels * pixelRatio = targetPixelCount, so pixels = targetPixelCount / pixelRatio
const pixels = targetPixelCount / pixelRatio;

const result = await captureRef(this.imageContainer, {
  result: 'tmpfile',
  height: pixels,
  width: pixels,
  quality: 1,
  format: 'png',
});
```

## Learn more

[Visit official documentation](https://github.com/gre/react-native-view-shot) — Get full information on API and its usage.
