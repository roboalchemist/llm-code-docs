# Source: https://img.ly/docs/cesdk/ios/concepts/edit-modes-1f5b6c/

---
title: "Editor State"
description: "Control how users interact with content by switching between edit modes like transform, crop, and text."
platform: ios
url: "https://img.ly/docs/cesdk/ios/concepts/edit-modes-1f5b6c/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/ios/concepts-c9ff51/) > [Editor State](https://img.ly/docs/cesdk/ios/concepts/edit-modes-1f5b6c/)

---

```swift reference-only
let task = Task {
  for await _ in engine.editor.onStateChanged {
    print("Editor state has changed")
  }
}

// Native modes: 'Transform', 'Crop', 'Text'
engine.editor.setEditMode(.crop)
engine.editor.getEditMode() // 'Crop'

engine.editor.unstable_isInteractionHappening();

// Use this information to alter the displayed cursor
engine.editor.getCursorType()
engine.editor.getCursorRotation()

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

The editor state consists of the current edit mode, which informs what type of content the user is currently able to edit. The edit mode can be set to either `'Transform'`, `'Crop'`, `'Text'`, or a custom user-defined one. You can also query the intended mouse cursor and the location of the text cursor while editing text.

Instead of having to constantly query the state in a loop, you can also be notified when the state has changed to then act on these changes in a callback.

```swift
public var onStateChanged: AsyncStream<Void> { get }
```

Subscribe to changes to the editor state.

```swift
public func setEditMode(_ mode: EditMode)
```

Set the edit mode of the editor.
An edit mode defines what type of content can currently be edited by the user.

- Note: The initial edit mode is "Transform".
- `mode:`: "Transform", "Crop", "Text", "Playback".

```swift
public func getEditMode() -> EditMode
```

Get the current edit mode of the editor.
An edit mode defines what type of content can currently be edited by the user.

- Returns: "Transform", "Crop", "Text", "Playback".

```swift
public func unstable_isInteractionHappening() throws -> Bool
```

If an user interaction is happening, e.g., a resize edit with a drag handle or a touch gesture.

- Returns: true if an interaction is happening.

## Cursor

```swift
public func getCursorType() -> CursorType
```

Get the type of cursor that should be displayed by the application.

- Returns: The cursor type.

```swift
public func getCursorRotation() -> Float
```

Get the rotation with which to render the mouse cursor.

- Returns: The angle in radians.

```swift
public func getTextCursorPositionInScreenSpaceX() -> Float
```

Get the current text cursor's x position in screen space.

- Returns: The text cursor's x position in screen space.

```swift
public func getTextCursorPositionInScreenSpaceY() -> Float
```

Get the current text cursor's y position in screen space.

- Returns: The text cursor's y position in screen space.

## Full Code

Here's the full code:

```swift
let task = Task {
  for await _ in engine.editor.onStateChanged {
    print("Editor state has changed")
  }
}

// Native modes: 'Transform', 'Crop', 'Text'
engine.editor.setEditMode(.crop)
engine.editor.getEditMode() // 'Crop'

engine.editor.unstable_isInteractionHappening();

// Use this information to alter the displayed cursor
engine.editor.getCursorType()
engine.editor.getCursorRotation()

// Query information about the text cursor position
engine.editor.getTextCursorPositionInScreenSpaceX()
engine.editor.getTextCursorPositionInScreenSpaceY()
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
