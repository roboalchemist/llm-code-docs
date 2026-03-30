# Source: https://img.ly/docs/cesdk/android/open-the-editor/set-zoom-level-d31896/

---
title: "Android Image Zoom Library"
description: "Programmatically adjust the zoom level of the canvas to focus on specific areas of the design."
platform: android
url: "https://img.ly/docs/cesdk/android/open-the-editor/set-zoom-level-d31896/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Open the Editor](https://img.ly/docs/cesdk/android/open-the-editor-23a1db/) > [Set Zoom Level](https://img.ly/docs/cesdk/android/open-the-editor/set-zoom-level-d31896/)

---

```kotlin reference-only
// Zoom to 100%
engine.scene.setZoomLevel(level = 1F)

// Zoom to 50%
engine.scene.setZoomLevel(0.5F * engine.scene.getZoomLevel())

// Bring entire scene in view with padding of 20px in all directions
engine.scene.zoomToBlock(
  block = scene,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)
engine.scene.immediateZoomToBlock(
  block = scene,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)

// Follow page with padding of 20px in both directions
engine.scene.enableZoomAutoFit(
  block = page,
  axis = ZoomAutoFitAxis.BOTH,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)

// Stop following page
engine.scene.disableZoomAutoFit(page)

// Query if zoom auto-fit is enabled for page
engine.scene.isZoomAutoFitEnabled(page)

// Keep the scene with padding of 10px within the camera
engine.scene.enableCameraPositionClamping(
  blocks = listOf(scene),
  paddingLeft = 10F,
  paddingTop = 10F,
  paddingRight = 10F,
  paddingBottom = 10F,
  scaledPaddingLeft = 0F,
  scaledPaddingTop = 0F,
  scaledPaddingRight = 0F,
  scaledPaddingBottom = 0F
)

engine.scene.disableCameraPositionClamping()

// Query if camera position clamping is enabled for the scene
engine.scene.isCameraPositionClampingEnabled(scene)

// Allow zooming from 12.5% to 800% relative to the size of a page
engine.scene.enableCameraZoomClamping(
  listOf(page),
  minZoomLimit = 0.125F,
  maxZoomLimit = 8F,
  paddingLeft = 0F,
  paddingTop = 0F,
  paddingRight = 0F,
  paddingBottom = 0F,
)

engine.scene.disableCameraZoomClamping()

// Query if camera zoom clamping is enabled for the scene
engine.scene.isCameraZoomClampingEnabled(scene)

// Get notified when the zoom level changes
engine.scene.onZoomLevelChanged()
  .onEach {
    val zoomLevel = engine.scene.getZoomLevel()
    println("Zoom level is now: $zoomLevel")
  }
  .launchIn(CoroutineScope(Dispatchers.Main))
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to control and observe camera zoom via the `scene` API.

## Functions

```kotlin
fun getZoomLevel(): Float
```

Get the zoom level of the scene or for a camera in the scene.

Returns the current zoom level of the scene in unit `dpx/dot`.

A zoom level of 2F results in one dot in the design to be two pixels on the screen.

- Returns the zoom level of the scene.

```kotlin
fun setZoomLevel(level: Float)
```

Set the zoom level of the scene, e.g., for headless versions.

This only shows an effect if the zoom level is not handled/overwritten by the UI.

Setting a zoom level of 2F results in one dot in the design to be two pixels on the screen.

- `level`: the zoom level with unit `dpx/dot`.

is shown on the screen.

```kotlin
suspend fun zoomToBlock(
    block: DesignBlock,
    paddingLeft: Float = 0F,
    paddingTop: Float = 0F,
    paddingRight: Float = 0F,
    paddingBottom: Float = 0F,
)
```

Sets the zoom and focus to show a block.

Without padding, this results in a tight view on the block.

It is set asynchronous to ensure that the block dimensions are known.

- `block`: the block that should be focused on.

- `paddingLeft`: optional padding in screen pixels to the left of the block.

- `paddingTop`: optional padding in screen pixels to the top of the block.

- `paddingRight`: optional padding in screen pixels to the right of the block.

- `paddingBottom`: optional padding in screen pixels to the bottom of the block.

```kotlin
fun immediateZoomToBlock(
    block: DesignBlock,
    paddingLeft: Float = 0F,
    paddingTop: Float = 0F,
    paddingRight: Float = 0F,
    paddingBottom: Float = 0F,
    forceUpdate: Boolean = false,
)
```

Sets the zoom and focus to show a block.

This only shows an effect if the zoom level is not handled/overwritten by the UI.

Without padding, this results in a tight view on the block.

It is set immediately and assumes that the block dimensions are known.

The block should not be in pending state and it's layout should be up to date.

- `block`: the block that should be focused on.

- `paddingLeft`: optional padding in screen pixels to the left of the block.

- `paddingTop`: optional padding in screen pixels to the top of the block.

- `paddingRight`: optional padding in screen pixels to the right of the block.

- `paddingBottom`: optional padding in screen pixels to the bottom of the block.

- `forceUpdate`: If true, the implicit update is called.

```kotlin
fun enableZoomAutoFit(
    block: DesignBlock,
    axis: ZoomAutoFitAxis,
    paddingLeft: Float = 0.0F,
    paddingTop: Float = 0.0F,
    paddingRight: Float = 0.0F,
    paddingBottom: Float = 0.0F,
)
```

Continually adjusts the zoom level to fit the width or height of a block's axis-aligned bounding box.

This only shows an effect if the zoom level is not handled/overwritten by the UI.

Without padding, this results in a tight view on the block.

No more than one block per scene can have zoom auto-fit enabled.

Calling `setZoomLevel` or `zoomToBlock` disables the continuous adjustment.

- `block`: the block in the scene for which to enable a zoom auto-fit.

- `axis`: the block axis (or axes) for which the zoom is adjusted.

- `paddingLeft`: optional padding in screen pixels to the left of the block.

- `paddingTop`: optional padding in screen pixels to the top of the block.

- `paddingRight`: optional padding in screen pixels to the right of the block.

- `paddingBottom`: optional padding in screen pixels to the bottom of the block.

```kotlin
fun disableZoomAutoFit(block: DesignBlock)
```

Disables any previously set zoom auto-fit.

- `block`: the scene or a block in the scene for which to disable zoom auto-fit.

```kotlin
fun isZoomAutoFitEnabled(block: DesignBlock): Boolean
```

Queries whether zoom auto-fit is enabled for `block`.

- `block`: the scene or a block in the scene for which to query if zoom auto-fit is set.

- Returns true if the given block has auto-fit set or the scene contains a block for which auto-fit is set, false otherwise.

```kotlin
@UnstableEngineApi
fun enableCameraPositionClamping(
    blocks: List<DesignBlock>,
    paddingLeft: Float = 0.0F,
    paddingTop: Float = 0.0F,
    paddingRight: Float = 0.0F,
    paddingBottom: Float = 0.0F,
    scaledPaddingLeft: Float = 0.0F,
    scaledPaddingTop: Float = 0.0F,
    scaledPaddingRight: Float = 0.0F,
    scaledPaddingBottom: Float = 0.0F,
)
```

Continually ensures the camera position to be within the width and height of the blocks axis-aligned bounding box. Disables any previously set camera position clamping in the scene and also takes priority over clamp camera commands.

Without padding, this results in a tight clamp on the blocks.

- `blocks`: the blocks for which the camera position is adjusted to, usually, the scene or a page.

- `paddingLeft`: optional padding in screen pixels to the left of the block.

- `paddingTop`: optional padding in screen pixels to the top of the block.

- `paddingRight`: optional padding in screen pixels to the right of the block.

- `paddingBottom`: optional padding in screen pixels to the bottom of the block.

- `scaledPaddingLeft`: optional padding in screen pixels to the left of the block that scales with the zoom level until five times the initial value.

- `scaledPaddingTop`: optional padding in screen pixels to the top of the block that scales with the zoom level until five times the initial value.

- `scaledPaddingRight`: optional padding in screen pixels to the right of the block that scales with the zoom level until five times the initial value.

- `scaledPaddingBottom`: optional padding in screen pixels to the bottom of the block that scales with the zoom level until five times the initial value.

```kotlin
@UnstableEngineApi
fun disableCameraPositionClamping()
```

Disables any previously set position clamping for the current scene.

```kotlin
@UnstableEngineApi
fun isCameraPositionClampingEnabled(blockOrScene: DesignBlock): Boolean
```

Queries whether position clamping is enabled for `blockOrScene`.

- `blockOrScene`: the scene or a block in the scene for which to query the position clamping.

- Returns true if the given block has position clamping set or the scene contains a block for which position clamping is set, false

otherwise.

```kotlin
@UnstableEngineApi
fun enableCameraZoomClamping(
    blocks: List<DesignBlock>,
    minZoomLimit: Float = -1.0F,
    maxZoomLimit: Float = -1.0F,
    paddingLeft: Float = 0.0F,
    paddingTop: Float = 0.0F,
    paddingRight: Float = 0.0F,
    paddingBottom: Float = 0.0F,
)
```

Continually ensures the zoom level of the camera in the active scene to be in the given range.

- Note: A zoom level of 2.0 results in one pixel in the design to be two pixels on the screen.

- `blocks`: the blocks for which the camera position is adjusted to, usually, the scene or a page.

- `minZoomLimit`: the minimum zoom level limit when zooming out, unlimited when negative.

- `maxZoomLimit`: the maximum zoom level limit when zooming in, unlimited when negative.

- `paddingLeft`: optional padding in screen pixels to the left of the block. Only applied when the block is not a camera.

- `paddingTop`: optional padding in screen pixels to the top of the block. Only applied when the block is not a camera.

- `paddingRight`: optional padding in screen pixels to the right of the block. Only applied when the block is not a camera.

- `paddingBottom`: optional padding in screen pixels to the bottom of the block. Only applied when the block is not a camera.

```kotlin
@UnstableEngineApi
fun disableCameraZoomClamping()
```

Disables previously set zoom clamping for the current scene.

```kotlin
@UnstableEngineApi
fun isCameraZoomClampingEnabled(blockOrScene: DesignBlock): Boolean
```

Queries whether zoom clamping is enabled.

- `blockOrScene`: the scene or a block in the scene for which to query the zoom clamping.

- Returns true if the given block has zoom clamping set or the scene contains a block for which zoom clamping is set, false otherwise.

```kotlin
fun onZoomLevelChanged(): Flow<Unit>
```

Subscribe to changes to the zoom level.

- Returns flow of zoom change events.

## Settings

See clamp camera settings in the [editor settings](https://img.ly/docs/cesdk/android/settings-970c98/).

## Full Code

Here's the full code:

```kotlin
// Zoom to 100%
engine.scene.setZoomLevel(level = 1F)

// Zoom to 50%
engine.scene.setZoomLevel(0.5F * engine.scene.getZoomLevel())

// Bring entire scene in view with padding of 20px in all directions
engine.scene.zoomToBlock(
  block = scene,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)
engine.scene.immediateZoomToBlock(
  block = scene,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)

// Follow page with padding of 20px in both directions
engine.scene.enableZoomAutoFit(
  block = page,
  axis = ZoomAutoFitAxis.BOTH,
  paddingLeft = 20F,
  paddingTop = 20F,
  paddingRight = 20F,
  paddingBottom = 20F
)

// Stop following page
engine.scene.disableZoomAutoFit(page)

// Query if zoom auto-fit is enabled for page
engine.scene.isZoomAutoFitEnabled(page)

// Keep the scene with padding of 10px within the camera
engine.scene.enableCameraPositionClamping(
  blocks = listOf(scene),
  paddingLeft = 10F,
  paddingTop = 10F,
  paddingRight = 10F,
  paddingBottom = 10F,
  scaledPaddingLeft = 0F,
  scaledPaddingTop = 0F,
  scaledPaddingRight = 0F,
  scaledPaddingBottom = 0F
)

engine.scene.disableCameraPositionClamping()

// Query if camera position clamping is enabled for the scene
engine.scene.isCameraPositionClampingEnabled(scene)

// Allow zooming from 12.5% to 800% relative to the size of a page
engine.scene.enableCameraZoomClamping(
  listOf(page),
  minZoomLimit = 0.125F,
  maxZoomLimit = 8F,
  paddingLeft = 0F,
  paddingTop = 0F,
  paddingRight = 0F,
  paddingBottom = 0F,
)

engine.scene.disableCameraZoomClamping()

// Query if camera zoom clamping is enabled for the scene
engine.scene.isCameraZoomClampingEnabled(scene)

// Get notified when the zoom level changes
engine.scene.onZoomLevelChanged()
  .onEach {
    val zoomLevel = engine.scene.getZoomLevel()
    println("Zoom level is now: $zoomLevel")
  }
  .launchIn(CoroutineScope(Dispatchers.Main))
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
