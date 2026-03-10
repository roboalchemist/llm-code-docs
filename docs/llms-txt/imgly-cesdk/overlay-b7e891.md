# Source: https://img.ly/docs/cesdk/android/user-interface/appearance/overlay-b7e891/

---
title: "Overlay"
description: "Configure custom overlays for mobile to show dialogs or loading states in response to UI events."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/appearance/overlay-b7e891/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Appearance](https://img.ly/docs/cesdk/android/user-interface/appearance-b155eb/) > [Overlay](https://img.ly/docs/cesdk/android/user-interface/appearance/overlay-b7e891/)

---

In this example, we will show you how to make overlay configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/).

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-android-examples/tree/v$UBQ_VERSION$/editor-guides-configuration-overlay).

## Configuration

When working with [UI events](https://img.ly/docs/cesdk/android/user-interface/events-514b70/), you may want to update the UI that is drawn over the editor (a.k.a `Overlay`) upon receiving events. A great example would be showing a loading indicator when the editor is being loaded or showing a custom dialog asking for export configurations when your customer taps on the `Export` button. This is when overlay configuration comes to help. In this example, we are going to demonstrate how upon capturing show/hide loading events you can render your own loading dialog.

The default `EditorUiState` already contains `showLoading` property that is responsible for drawing an overlaying loading. Although we can use the same property, let's create our own state class in order to demonstrate how the default state can be wrapped and extended. The only requirement of the state class is that it has to be `Parcelable`.

By default, both `onCreate` and `onExport` [callbacks](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) send `ShowLoading` and `HideLoading` UI events. All we have to do is capture these events and override the default behavior. Similar to the [UI events](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) guide, the events are captured and an updated state is returned. Note that instead of updating the `EditorUiState.showLoading` property we update the property of the brand new state: `OverlayCustomState.showCustomLoading`.

As the state is updated, the updated state is received in the `overlay` composable callback to be rendered. Finally, we can render our custom loading dialog and render remaining default overlay components via `EditorDefaults.Overlay` composable function. Note that the callback receives `EditorEventHandler` object too in case your composable component requires UI interaction. In this example, tapping on the confirm button of the loading dialog closes the dialog and the editor.

Note that the overlay is edge-to-edge, therefore it is your responsibility to draw over system bars too.



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
