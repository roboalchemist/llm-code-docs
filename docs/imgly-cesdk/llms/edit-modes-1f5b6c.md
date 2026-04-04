# Source: https://img.ly/docs/cesdk/android/concepts/edit-modes-1f5b6c/

---
title: "Editor State"
description: "Control how users interact with content by switching between edit modes like transform, crop, and text."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/edit-modes-1f5b6c/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Editor State](https://img.ly/docs/cesdk/android/concepts/edit-modes-1f5b6c/)

---

```kotlin reference-only
engine.editor.onStateChanged()
	.onEach { println("Editor history has changed") }
	.launchIn(CoroutineScope(Dispatchers.Main))

// Native modes: "Transform", "Crop", "Text"
engine.editor.setEditMode("Crop")
engine.editor.getEditMode() // "Crop"

engine.editor.isInteractionHappening()

// Query information about the text cursor position
engine.editor.getTextCursorPositionInScreenSpaceX()
engine.editor.getTextCursorPositionInScreenSpaceY()
```

The CreativeEditor SDK operates in different states called **Edit Modes**, each designed for a specific type of interaction on the canvas:

- `Transform`: this is the default mode which allow to move, resize and manipulate things on the canvas
- `Text`: Allows to edit the text elements on the canvas
- `Crop`: Allow to Crop media blocks (images, videos, etc...)
- `Trim`: Trim the clips in video mode
- `Playback`: Play the media (mostly video) in video mode

While users typically interact with these modes through the UI (e.g., showing or hiding specific controls based on the active mode), it’s also possible to manage them programmatically via the engine’s API, though this isn’t always required.

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to set and query the editor state in the `editor` API, i.e., what type of content the user is currently able to edit.

## State

The editor state consists of the current edit mode, which informs what type of content the user is currently able to edit. The edit mode can be set to either `Transform`, `Crop`, `Text`, or a custom user-defined one. You can also query the intended mouse cursor and the location of the text cursor while editing text.

Instead of having to constantly query the state in a loop, you can also be notified when the state has changed to then act on these changes in a callback.

```kotlin
fun onStateChanged(): Flow<Unit>
```

Subscribe to changes to the editor state.

- Returns flow of editor state change events.

```kotlin
fun setEditMode(editMode: String)
```

Set the edit mode of the editor.

An edit mode defines what type of content can currently be edited by the user.

Note: The initial edit mode is "Transform".

- `editMode`: "Transform", "Crop", "Text", "Playback", "Trim" or a custom value.

```kotlin
fun getEditMode(): String
```

Get the current edit mode of the editor.

An edit mode defines what type of content can currently be edited by the user.

- Returns "Transform", "Crop", "Text", "Playback", "Trim" or a custom value.

```kotlin
@UnstableEngineApi
fun isInteractionHappening(): Boolean
```

If an user interaction is happening, e.g., a resize edit with a drag handle or a touch gesture.

- Returns true if an interaction is happening.

## Cursor

```kotlin
fun getTextCursorPositionInScreenSpaceX(): Float
```

Get the current text cursor's x position in screen space.

- Returns the text cursor's x position in screen space.

```kotlin
fun getTextCursorPositionInScreenSpaceY(): Float
```

Get the current text cursor's y position in screen space.

- Returns the text cursor's y position in screen space.

## Full Code

Here's the full code:

```kotlin
engine.editor.onStateChanged()
    .onEach { println("Editor history has changed") }
    .launchIn(CoroutineScope(Dispatchers.Main))

// Native modes: "Transform", "Crop", "Text"
engine.editor.setEditMode("Crop")
engine.editor.getEditMode() // "Crop"

engine.editor.isInteractionHappening()

// Query information about the text cursor position
engine.editor.getTextCursorPositionInScreenSpaceX()
engine.editor.getTextCursorPositionInScreenSpaceY()
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
