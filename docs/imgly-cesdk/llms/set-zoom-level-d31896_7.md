# Source: https://img.ly/docs/cesdk/macos/open-the-editor/set-zoom-level-d31896/

---
title: "Set Zoom Level"
description: "Programmatically adjust the zoom level of the canvas to focus on specific areas of the design."
platform: macos
url: "https://img.ly/docs/cesdk/macos/open-the-editor/set-zoom-level-d31896/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/macos/open-the-editor-23a1db/) > [Set Zoom Level](https://img.ly/docs/cesdk/macos/open-the-editor/set-zoom-level-d31896/)

---

```swift reference-only
// Zoom to 100%
try engine.scene.setZoom(1.0)

// Zoom to 50%
try engine.scene.setZoom(0.5 * engine.scene.getZoom())

// Bring entire scene in view with padding of 20px in all directions
try await engine.scene.zoom(to: scene, paddingLeft: 20.0, paddingTop: 20.0, paddingRight: 20.0, paddingBottom: 20.0)
try engine.scene.immediateZoom(to: scene, paddingLeft: 20.0, paddingTop: 20.0, paddingRight: 20.0, paddingBottom: 20.0)

// Follow page with padding of 20px in both directions
let page = try engine.scene.getPages().first!
try engine.scene.enableZoomAutoFit(
  page,
  axis: .both,
  paddingLeft: 20,
  paddingTop: 20,
  paddingRight: 20,
  paddingBottom: 20
)

// Stop following page
try engine.scene.disableZoomAutoFit(page)
// Query if zoom auto-fit is enabled for page
try engine.scene.isZoomAutoFitEnabled(page)

// Keep the scene with padding of 10px within the camera
try engine.scene.unstable_enableCameraPositionClamping(
  [scene],
  paddingLeft: 10,
  paddingTop: 10,
  paddingRight: 10,
  paddingBottom: 10,
  scaledPaddingLeft: 0,
  scaledPaddingTop: 0,
  scaledPaddingRight: 0,
  scaledPaddingBottom: 0
)

try engine.scene.unstable_disableCameraPositionClamping()
// Query if camera position clamping is enabled for the scene
try engine.scene.unstable_isCameraPositionClampingEnabled(scene)

// Allow zooming from 12.5% to 800% relative to the size of a page
try engine.scene.unstable_enableCameraZoomClamping(
  [page],
  minZoomLimit: 0.125,
  maxZoomLimit: 8.0,
  paddingLeft: 0,
  paddingTop: 0,
  paddingRight: 0,
  paddingBottom: 0
)

try engine.scene.unstable_disableCameraZoomClamping()
// Query if camera zoom clamping is enabled for the scene
try engine.scene.unstable_isCameraZoomClampingEnabled(scene)

// Get notified when the zoom level changes
let task = Task {
  for await _ in engine.editor.onZoomLevelChanged {
    let zoomLevel = try engine.scene.getZoom()
    print("Zoom level is now: \(zoomLevel)")
  }
}
task.cancel()
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to control and observe camera zoom via the `scene` API.

## Functions

```swift
public func getZoom() throws -> Float
```

Query a camera zoom level of the active scene.

- Returns: Returns the current zoom level of the scene in unit 1/px, i.e., how large a pixel of the camera
  resolution is shown on the screen. A zoom level of 2.0f results in one pixel in the design to be two pixels on the
  screen.

```swift
public func setZoom(_ level: Float) throws
```

Sets the zoom level of the active scene. A zoom level of 2.0f results in one pixel in the design to be two pixels
on the screen.

- `level:`: The new zoom level with unit 1/px, i.e., how large a pixel of the camera resolution is shown on
  the screen.

```swift
public func zoom(to id: DesignBlockID, paddingLeft: Float = 0, paddingTop: Float = 0, paddingRight: Float = 0, paddingBottom: Float = 0) async throws
```

Sets the zoom and focus to show a block.
Without padding, this results in a tight view on the block.

- `id`: The block that should be focussed on.
- `paddingLeft`: Optional padding in points to the left of the block.
- `paddingTop`: Optional padding in points to the top of the block.
- `paddingRight`: Optional padding in points to the right of the block.
- `paddingBottom`: Optional padding in points to the bottom of the block.

```swift
public func immediateZoom(to id: DesignBlockID, paddingLeft: Float = 0, paddingTop: Float = 0, paddingRight: Float = 0, paddingBottom: Float = 0, forceUpdate: Bool = false) throws
```

Sets the zoom and focus to show a block.
Without padding, this results in a tight view on the block.
Assums layout has been done. You can force the layout with explicit update call
that will update the layout.

- `id`: The block that should be focussed on.
- `paddingLeft`: Optional padding in points to the left of the block.
- `paddingTop`: Optional padding in points to the top of the block.
- `paddingRight`: Optional padding in points to the right of the block.
- `paddingBottom`: Optional padding in points to the bottom of the block.
- `forceUpdate`: Optional flag that will run the system update that will update the layout.

```swift
public func enableZoomAutoFit(_ id: DesignBlockID, axis: ZoomAutoFitAxis, paddingLeft: Float = 0, paddingTop: Float = 0, paddingRight: Float = 0, paddingBottom: Float = 0) throws
```

Continually adjusts the zoom level to fit the width or height of a block's axis-aligned bounding box.
This only shows an effect if the zoom level is not handled/overwritten by the UI.
Without padding, this results in a tight view on the block.

- Note: Calling `setZoom(level:)` or `zoom(to:)` disables the continuous adjustment.
- `id`: The block for which the zoom is adjusted.
- `axis`: The block axis for which the zoom is adjusted.
- `paddingLeft`: Optional padding in points to the left of the block.
- `paddingTop`: Optional padding in points to the top of the block.
- `paddingRight`: Optional padding in points to the right of the block.
- `paddingBottom`: Optional padding in points to the bottom of the block.

```swift
public func disableZoomAutoFit(_ id: DesignBlockID) throws
```

Disables any previously set zoom auto-fit.

- `id:`: The scene or a block in the scene for which to disable zoom auto-fit.

```swift
public func isZoomAutoFitEnabled(_ id: DesignBlockID) throws -> Bool
```

Queries whether zoom auto-fit is enabled.

- `id:`: The scene or a block in the scene for which to query the zoom auto-fit.
- Returns: `true` if the given block has auto-fit set or the scene contains a block for which auto-fit is set,
  `false` otherwise.

```swift
public func unstable_enableCameraPositionClamping(_ ids: [DesignBlockID], paddingLeft: Float = 0, paddingTop: Float = 0, paddingRight: Float = 0, paddingBottom: Float = 0, scaledPaddingLeft: Float = 0, scaledPaddingTop: Float = 0, scaledPaddingRight: Float = 0, scaledPaddingBottom: Float = 0) throws
```

Continually ensures the camera position to be within the width and height of the blocks axis-aligned bounding box.
Without padding, this results in a tight clamp on the blocks. Disables any previously set camera position clamping in the scene and also takes priority over clamp camera commands.

- `ids`: The blocks for which the camera position is adjusted to, usually, the scene or a page.
- `paddingLeft`: Optional padding in points to the left of the block.
- `paddingTop`: Optional padding in points to the top of the block.
- `paddingRight`: Optional padding in points to the right of the block.
- `paddingBottom`: Optional padding in points to the bottom of the block.
- `scaledPaddingLeft`: Optional padding in points to the left of the block that scales with the zoom
  level until five times the initial value.
- `scaledPaddingTop`: Optional padding in points to the left of the block that scales with the zoom
  level until five times the initial value.
- `scaledPaddingRight`: Optional padding in points to the left of the block that scales with the zoom
  level until five times the initial value.
- `scaledPaddingBottom`: Optional padding in points to the left of the block that scales with the zoom
  level until five times the initial value.

```swift
public func unstable_disableCameraPositionClamping() throws
```

Disables any previously set position clamping.

```swift
public func unstable_isCameraPositionClampingEnabled(_ id: DesignBlockID) throws -> Bool
```

Queries whether position clamping is enabled.

- `id:`: The scene or a block in the scene for which to query the position clamping.
- Returns: `true` if the given block has position clamping set or the scene contains a block for which position
  clamping is set, `false` otherwise.

```swift
public func unstable_enableCameraZoomClamping(_ ids: [DesignBlockID], minZoomLimit: Float = -1, maxZoomLimit: Float = -1, paddingLeft: Float = 0, paddingTop: Float = 0, paddingRight: Float = 0, paddingBottom: Float = 0) throws
```

Continually ensures the zoom level of the camera in the active scene to be in the given range.

- `ids`: The blocks for which the camera zoom limits are adjusted to, usually, the scene or a page.
- `minZoomLimit`: The minimum zoom limit in unit `dpx/dot` when zooming out, unlimited when negative.
- `maxZoomLimit`: The maximum zoom limit in unit `dpx/dot` when zooming in, unlimited when negative.
- `paddingLeft`: Optional padding in points to the left of the block. Only applied when the block is not a camera.
- `paddingTop`: Optional padding in points to the top of the block. Only applied when the block is not a camera.
- `paddingRight`: Optional padding in points to the right of the block. Only applied when the block is not a
  camera.
- `paddingBottom`: Optional padding in points to the bottom of the block. Only applied when the block is not a
  camera.

```swift
public func unstable_disableCameraZoomClamping() throws
```

Disables previously set zoom clamping for the block, scene, or camera.

```swift
public func unstable_isCameraZoomClampingEnabled(_ id: DesignBlockID) throws -> Bool
```

Queries whether zoom clamping is enabled.

- `id:`: The scene or a block for which to query the zoom clamping.
- Returns: `true` if the active scene has zoom clamping set, `false` otherwise.

```swift
public var onZoomLevelChanged: AsyncStream<Void> { get }
```

Subscribe to changes to the zoom level.

## Settings

See clamp camera settings in the [editor settings](https://img.ly/docs/cesdk/macos/settings-970c98/).

## Full Code

Here's the full code:

```swift
// Zoom to 100%
try engine.scene.setZoom(1.0)

// Zoom to 50%
try engine.scene.setZoom(0.5 * engine.scene.getZoom())

// Bring entire scene in view with padding of 20px in all directions
try await engine.scene.zoom(to: scene, paddingLeft: 20.0, paddingTop: 20.0, paddingRight: 20.0, paddingBottom: 20.0)
try engine.scene.immediateZoom(to: scene, paddingLeft: 20.0, paddingTop: 20.0, paddingRight: 20.0, paddingBottom: 20.0)

// Follow page with padding of 20px in both directions
let page = try engine.scene.getPages().first!
try engine.scene.enableZoomAutoFit(
  page,
  axis: .both,
  paddingLeft: 20,
  paddingTop: 20,
  paddingRight: 20,
  paddingBottom: 20
)

// Stop following page
try engine.scene.disableZoomAutoFit(page)
// Query if zoom auto-fit is enabled for page
try engine.scene.isZoomAutoFitEnabled(page)

// Keep the scene with padding of 10px within the camera
try engine.scene.unstable_enableCameraPositionClamping(
  [scene],
  paddingLeft: 10,
  paddingTop: 10,
  paddingRight: 10,
  paddingBottom: 10,
  scaledPaddingLeft: 0,
  scaledPaddingTop: 0,
  scaledPaddingRight: 0,
  scaledPaddingBottom: 0
)

try engine.scene.unstable_disableCameraPositionClamping()
// Query if camera position clamping is enabled for the scene
try engine.scene.unstable_isCameraPositionClampingEnabled(scene)

// Allow zooming from 12.5% to 800% relative to the size of a page
try engine.scene.unstable_enableCameraZoomClamping(
  [page],
  minZoomLimit: 0.125,
  maxZoomLimit: 8.0,
  paddingLeft: 0,
  paddingTop: 0,
  paddingRight: 0,
  paddingBottom: 0
)

try engine.scene.unstable_disableCameraZoomClamping()
// Query if camera zoom clamping is enabled for the scene
try engine.scene.unstable_isCameraZoomClampingEnabled(scene)

// Get notified when the zoom level changes
let task = Task {
  for await _ in engine.editor.onZoomLevelChanged {
    let zoomLevel = try engine.scene.getZoom()
    print("Zoom level is now: \(zoomLevel)")
  }
}
task.cancel()
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
