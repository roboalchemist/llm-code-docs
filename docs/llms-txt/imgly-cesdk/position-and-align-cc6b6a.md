# Source: https://img.ly/docs/cesdk/android/insert-media/position-and-align-cc6b6a/

---
title: "Positioning and Alignment"
description: "Precisely position, align, and distribute objects using guides, snapping, and alignment tools."
platform: android
url: "https://img.ly/docs/cesdk/android/insert-media/position-and-align-cc6b6a/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/android/create-composition-db709c/) > [Position and Align](https://img.ly/docs/cesdk/android/insert-media/position-and-align-cc6b6a/)

---

```kotlin reference-only
val x = engine.block.getPositionX(block)
val xMode = engine.block.getPositionXMode(block)
val y = engine.block.getPositionY(block)
val yMode = engine.block.getPositionYMode(block)
engine.block.setPositionX(block, value = 0.25F)
engine.block.setPositionXMode(block, mode = PositionMode.PERCENT)
engine.block.setPositionY(block, value = 0.25)
engine.block.setPositionYMode(block, mode = PositionMode.PERCENT)

val rad = engine.block.getRotation(block)
engine.block.setRotation(block, radians = PI.toFloat())
val isFlipHorizontal = engine.block.isFlipHorizontal(block)
val isFlipVertical = engine.block.isFlipVertical(block)
engine.block.setFlipHorizontal(block, flip = true)
engine.block.setFlipVertical(block, flip = false)

val width = engine.block.getWidth(block)
val widthMode = engine.block.getWidthMode(block)
val height = engine.block.getHeight(block)
val heightMode = engine.block.getHeightMode(block)
engine.block.setWidth(block, value = 0.5F)
engine.block.setWidth(block, value = 2.5F, maintainCrop = true)
engine.block.setWidthMode(block, mode = SizeMode.PERCENT)
engine.block.setHeight(block, value = 0.5F)
engine.block.setHeight(block, value = 2.5F, maintainCrop = true)
engine.block.setHeightMode(block, mode = SizeMode.PERCENT)
val frameX = engine.block.getFrameX(block)
val frameY = engine.block.getFrameY(block)
val frameWidth = engine.block.getFrameWidth(block)
val frameHeight = engine.block.getFrameHeight(block)

engine.block.setAlwaysOnTop(block, false)
val isAlwaysOnTop = engine.block.isAlwaysOnTop(block)
engine.block.setAlwaysOnBottom(block, false)
val isAlwaysOnBottom = engine.block.isAlwaysOnBottom(block)
engine.block.bringToFront(block)
engine.block.sendToBack(block)
engine.block.bringForward(block)
engine.block.sendBackward(block)

val globalX = engine.block.getGlobalBoundingBoxX(block)
val globalY = engine.block.getGlobalBoundingBoxY(block)
val globalWidth = engine.block.getGlobalBoundingBoxWidth(block)
val globalHeight = engine.block.getGlobalBoundingBoxHeight(block)
val screenSpaceRect = engine.block.getScreenSpaceBoundingBoxRect(listOf(block))

engine.block.scale(block, scale = 2F, anchorX = 0.5F, anchorY = 0.5F)

engine.block.fillParent(block)

val pages = engine.scene.getPages()
engine.block.resizeContentAware(pages, width = 100F, height = 100F)

// Create blocks and append to scene
val member1 = engine.block.create(DesignBlockType.Graphic)
val member2 = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(scene, child = member1)
engine.block.appendChild(scene, child = member2)
if (engine.block.isDistributable(listOf(member1, member2))) {
  engine.block.distributeHorizontally(listOf(member1, member2))
  engine.block.distributeVertically(listOf(member1, member2))
}
if (engine.block.isAlignable(listOf(member1, member2))) {
  engine.block.alignHorizontally(listOf(member1, member2), alignment = HorizontalBlockAlignment.LEFT)
  engine.block.alignVertically(listOf(member1, member2), alignment = VerticalBlockAlignment.TOP)
}

val isTransformLocked = engine.block.isTransformLocked(block)
if (!isTransformLocked) {
  engine.block.setTransformLocked(block, locked = true)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes layout through the `block` API.

## Layout of Blocks

> **Note:** **Note on layout and frame size** The frame size is determined during the
> layout phase of the render process inside the engine. This means that calling
> `getFrameSize()` immediately after modifying the scene might return an
> inaccurate result.

The CreativeEngine supports three different modes for positioning blocks. These can be set for each block and both coordinates independently:

- `Absolute`: the position value is interpreted in the scene's current design unit.
- `Percent`: the position value is interpreted as percentage of the block's parent's size, where 1F means 100%.
- `Auto` : the position is automatically determined.

Likewise there are also three different modes for controlling a block's size. Again both dimensions can be set independently:

- `Absolute`: the size value is interpreted in the scene's current design unit.
- `Percent`: the size value is interpreted as percentage of the block's parent's size, where 1F means 100%.
- `Auto` : the block's size is automatically determined by the size of the block's content.

### Positioning

```kotlin
fun getPositionX(block: DesignBlock): Float
```

Query a block's x position.

- `block`: the block to query.

- Returns the value of the x position.

```kotlin
fun getPositionY(block: DesignBlock): Float
```

Query a block's y position.

- `block`: the block to query.

- Returns the value of the y position.

```kotlin
fun getPositionXMode(block: DesignBlock): PositionMode
```

Query a block's mode for its x position.

- `block`: the block to query.

- Returns the current mode for the x position.

```kotlin
fun getPositionYMode(block: DesignBlock): PositionMode
```

Query a block's mode for its y position.

- `block`: the block to query.

- Returns the current mode for the y position.

```kotlin
fun setPositionX(
    block: DesignBlock,
    value: Float,
)
```

Update a block's x position.

The position refers to the block's local space, relative to its parent with the origin at the top left.

Required scope: "layer/move"

- `block`: the block to update.

- `value`: the value of the x position.

```kotlin
fun setPositionY(
    block: DesignBlock,
    value: Float,
)
```

Update a block's y position.

The position refers to the block's local space, relative to its parent with the origin at the top left.

Required scope: "layer/move"

- `block`: the block to update.

- `value`: the value of the y position.

```kotlin
fun setPositionXMode(
    block: DesignBlock,
    mode: PositionMode,
)
```

Set a block's mode for its x position.

The position refers to the block's local space, relative to its parent with the origin at the top left.

Required scope: "layer/move"

- `block`: the block to update.

- `mode`: the x position mode.

```kotlin
fun setPositionYMode(
    block: DesignBlock,
    mode: PositionMode,
)
```

Set a block's mode for its y position.

The position refers to the block's local space, relative to its parent with the origin at the top left.

Required scope: "layer/move"

- `block`: the block to update.

- `mode`: the y position mode.

### Size

```kotlin
fun getWidth(block: DesignBlock): Float
```

Query a block's width.

- `block`: the block to query.

- Returns the value of the block's width.

```kotlin
fun getWidthMode(block: DesignBlock): SizeMode
```

Query a block's mode for its width.

- `block`: the block to query.

- Returns the current mode for the width.

```kotlin
fun getHeight(block: DesignBlock): Float
```

Query a block's height.

- `block`: the block to query.

- Returns the value of the block's height.

```kotlin
fun getHeightMode(block: DesignBlock): SizeMode
```

Query a block's mode for its height.

- `block`: the block to query.

- Returns the current mode for the height.

```kotlin
fun setWidth(
    block: DesignBlock,
    value: Float,
    maintainCrop: Boolean = false,
)
```

Update a block's width and optionally maintain the crop.

If the crop is maintained, the crop values will be automatically adjusted.

The content fill mode `Cover` is only kept if the `features/transformEditsRetainCoverMode` setting is enabled, otherwise it will change to `Crop`.

Required scope: "layer/resize"

- `block`: the block to update.

- `value`: the new width of the block.

- `maintainCrop`: whether or not the crop values, if available, should be automatically adjusted.

```kotlin
fun setWidthMode(
    block: DesignBlock,
    mode: SizeMode,
)
```

Set a block's mode for its width.

Required scope: "layer/resize"

- `block`: the block to update.

- `mode`: the width mode.

```kotlin
fun setHeight(
    block: DesignBlock,
    value: Float,
    maintainCrop: Boolean = false,
)
```

Update a block's height and optionally maintain the crop.

If the crop is maintained, the crop values will be automatically adjusted.

The content fill mode `Cover` is only kept if the `features/transformEditsRetainCoverMode` setting is enabled, otherwise it will change to `Crop`.

Required scope: "layer/resize"

- `block`: the block to update.

- `value`: the new height of the block.

- `maintainCrop`: whether or not the crop values, if available, should be automatically adjusted.

```kotlin
fun setHeightMode(
    block: DesignBlock,
    mode: SizeMode,
)
```

Set a block's mode for its height.

Required scope: "layer/resize"

- `block`: the block to update.

- `mode`: the height mode.

### Rotation

```kotlin
fun getRotation(block: DesignBlock): Float
```

Query a block's rotation in radians.

- `block`: the block to query.

- Returns the block's rotation around its center in radians.

```kotlin
fun setRotation(
    block: DesignBlock,
    radians: Float,
)
```

Update a block's rotation.

Required scope: "layer/rotate"

- `block`: the block to update.

- `radians`: the new rotation in radians. Rotation is applied around the block's center.

### Flipping

```kotlin
fun setFlipHorizontal(
    block: DesignBlock,
    flip: Boolean,
)
```

Update a block's horizontal flip.

Required scope: "layer/flip"

- `block`: the block to update.

- `flip`: if the flip should be enabled.

```kotlin
fun isFlipHorizontal(block: DesignBlock): Boolean
```

Query a block's horizontal flip state.

- `block`: the block to query.

- Returns a boolean indicating for whether the block is flipped in the queried direction.

```kotlin
fun setFlipVertical(
    block: DesignBlock,
    flip: Boolean,
)
```

Update a block's vertical flip.

Required scope: "layer/flip"

- `block`: the block to update.

- `flip`: if the flip should be enabled.

```kotlin
fun isFlipVertical(block: DesignBlock): Boolean
```

Query a block's vertical flip state.

- `block`: the block to query.

- Returns a boolean indicating for whether the block is flipped in the queried direction.

### Scaling

```kotlin
fun scale(
    block: DesignBlock,
    scale: Float,
    @FloatRange(from = 0.0, to = 1.0) anchorX: Float,
    @FloatRange(from = 0.0, to = 1.0) anchorY: Float,
)
```

Scales the block and all of its children proportionally around the specified relative anchor point.

This updates the position, size and style properties (e.g. stroke width) of

the block and its children.

Required scope: "layer/resize"

- `block`: the block that should be scaled.

- `scale`: the scale factor to be applied to the current properties of the block.

- `anchorX`: the relative position along the width of the block around which the

scaling should occur. (0F = left edge, 0.5F = center, 1F = right edge)

- `anchorY`: the relative position along the height of the block around which the

scaling should occur. (0F = top edge, 0.5F = center, 1F = bottom edge)

### Fill a Block's Parent

```kotlin
fun fillParent(block: DesignBlock)
```

Resize and position a block to entirely fill its parent block.

The crop values of the block, except for the flip and crop rotation, are reset if it can be cropped.

If the size of the block's fill is unknown, the content fill mode is changed from `Crop` to `Cover` to prevent invalid crop values.

Required scope: "layer/move"

- "layer/resize"

- `block`: The block that should fill its parent.

### Resize Blocks Content-aware

```kotlin
fun resizeContentAware(
    blocks: List<DesignBlock>,
    width: Float,
    height: Float,
)
```

Resize all blocks to the given size. The content of the blocks is automatically adjusted to fit the

new dimensions.

Required scope: "layer/resize"

- `blocks`: The blocks to resize.

- `width`: The new width of the blocks.

- `height`: The new height of the blocks.

### Even Distribution

```kotlin
fun isDistributable(blocks: List<DesignBlock>): Boolean
```

Confirms that a given set of blocks can be distributed.

- `blocks`: a non-empty array of block ids.

- Returns whether the blocks can be distributed.

```kotlin
fun distributeHorizontally(blocks: List<DesignBlock>)
```

Distribute multiple blocks vertically within their bounding box so that the space between them is even.

Required scope: "layer/move"

- `blocks`: a non-empty array of block ids that should be distributed.

```kotlin
fun distributeVertically(blocks: List<DesignBlock>)
```

Distribute multiple blocks vertically within their bounding box so that the space between them is even.

Required scope: "layer/move"

- `blocks`: a non-empty array of block ids that should be distributed.

### Alignment

```kotlin
fun isAlignable(blocks: List<DesignBlock>): Boolean
```

Confirms that a given set of blocks can be aligned.

- `blocks`: a non-empty array of block ids.

- Returns whether the blocks can be aligned.

```kotlin
fun alignHorizontally(
    blocks: List<DesignBlock>,
    alignment: HorizontalBlockAlignment,
)
```

Align multiple blocks vertically within their bounding box or a single block to its parent.

Required scope: "layer/move"

- `blocks`: a non-empty array of block ids that should be aligned.

- `alignment`: How they should be aligned: left, right, or center

```kotlin
fun alignVertically(
    blocks: List<DesignBlock>,
    alignment: VerticalBlockAlignment,
)
```

Align multiple blocks vertically within their bounding box or a single block to its parent.

Required scope: "layer/move"

- `blocks`: a non-empty array of block ids that should be aligned.

- `alignment`: How they should be aligned: top, bottom, or center

### Computed Dimensions

```kotlin
fun getFrameX(block: DesignBlock): Float
```

Get a block's layout position on the x-axis. The layout position is only available after an

internal update loop, which may not happen immediately.

- `block`: the block to query.

- Returns the layout position.

```kotlin
fun getFrameY(block: DesignBlock): Float
```

Get a block's layout position on the y-axis. The layout position is only available after an

internal update loop, which may not happen immediately.

- `block`: the block to query.

- Returns the layout position.

```kotlin
fun getFrameWidth(block: DesignBlock): Float
```

Get a block's layout width. The layout width is only available after an internal update loop, which may not happen immediately.

- `block`: the block to query.

- Returns the layout width.

```kotlin
fun getFrameHeight(block: DesignBlock): Float
```

Get a block's layout height. The layout height is only available after an internal update loop, which may not happen immediately.

- `block`: the block to query.

- Returns the layout height.

```kotlin
fun getGlobalBoundingBoxX(block: DesignBlock): Float
```

Get the x position of the block's axis-aligned bounding box in the scene's global coordinate space.

The scene's global coordinate space has its origin at the top left.

- `block`: the block to query.

- Returns the x coordinate of the position of the axis-aligned bounding box.

```kotlin
fun getGlobalBoundingBoxY(block: DesignBlock): Float
```

Get the y position of the block's axis-aligned bounding box in the scene's global coordinate space.

The scene's global coordinate space has its origin at the top left.

- `block`: the block to query.

- Returns the y coordinate of the position of the axis-aligned bounding box.

```kotlin
fun getGlobalBoundingBoxWidth(block: DesignBlock): Float
```

Get the width of the block's axis-aligned bounding box in the scene's global coordinate space.

The scene's global coordinate space has its origin at the top left.

- `block`: the block to query.

- Returns the width of the axis-aligned bounding box.

```kotlin
fun getGlobalBoundingBoxHeight(block: DesignBlock): Float
```

Get the height of the block's axis-aligned bounding box in the scene's global coordinate space.

The scene's global coordinate space has its origin at the top left.

- `block`: the block to query.

- Returns the height of the axis-aligned bounding box.

```kotlin
fun getScreenSpaceBoundingBoxRect(blocks: List<DesignBlock>): RectF
```

Get the position and size of the axis-aligned bounding box for the given blocks in screen space.

- `blocks`: the blocks whose bounding box should be calculated.

- Returns the position and size of the bounding box as RectF.

### Layers

```kotlin
fun setAlwaysOnTop(
    block: DesignBlock,
    enabled: Boolean,
)
```

Update the block's always-on-top property. If true, this blocks's global sorting order is automatically

adjusted to be higher than all other siblings

without this property. If more than one block is set to be always-on-top, the child order decides which is on top.

- `block`: the block to update.

- `enabled`: whether the block shall be always-on-top.

```kotlin
fun isAlwaysOnTop(block: DesignBlock): Boolean
```

Query a block's always-on-top property.

- `block`: the block to query.

- Returns true if the block is set to be always-on-top, false otherwise.

```kotlin
fun setAlwaysOnBottom(
    block: DesignBlock,
    enabled: Boolean,
)
```

Update the block's always-on-bottom property. If true, this blocks's global sorting order is automatically

adjusted to be lower than all other siblings

without this property. If more than one block is set to be always-on-bottom, the child order decides which is on the bottom.

- `block`: the block to update.

- `enabled`: whether the block shall be always-on-bottom.

```kotlin
fun isAlwaysOnBottom(block: DesignBlock): Boolean
```

Query a block's always-on-bottom property.

- `block`: the block to query.

- Returns true if the block is set to be always-on-bottom, false otherwise.

```kotlin
fun bringToFront(block: DesignBlock)
```

Updates the sorting order of this block and all of its manually created siblings

so that the given block has the highest sorting order.

If the block is parented to a track, it is first moved up in the hierarchy.

- `block`: the block to be given the highest sorting order among its siblings.

```kotlin
fun sendToBack(block: DesignBlock)
```

Updates the sorting order of this block and all of its manually created siblings

so that the given block has the lowest sorting order.

If the block is parented to a track, it is first moved up in the hierarchy.

- `block`: the block to be given the lowest sorting order among its siblings.

```kotlin
fun bringForward(block: DesignBlock)
```

Updates the sorting order of this block and all of its superjacent siblings

so that the given block has a higher sorting order than the next superjacent sibling.

If the block is parented to a track, it is first moved up in the hierarchy.

Empty tracks and empty groups are passed by.

- `block`: the block to be given a higher sorting than the next superjacent sibling.

```kotlin
fun sendBackward(block: DesignBlock)
```

Updates the sorting order of this block and all of its manually created and subjacent siblings

so that the given block will have a lower sorting order than the next subjacent sibling.

If the block is parented to a track, it is first moved up in the hierarchy.

Empty tracks and empty groups are passed by.

- `block`: the block to be given a lower sorting order than the next subjacent sibling.

### Transform Locking

You can lock the transform of a block to prevent changes to any of its transformations. That is the block's position, rotation, scale, and sizing.

```kotlin
fun isTransformLocked(block: DesignBlock): Boolean
```

Query a block's transform locked state. If `true`, the block's transform can't be changed.

- `block`: the block to query.

- Returns true if block is locked, false otherwise.

```kotlin
fun setTransformLocked(
    block: DesignBlock,
    locked: Boolean,
)
```

Update a block's transform locked state.

- `block`: the block to update.

- `locked`: whether the block's transform should be locked.

## Full Code

Here's the full code:

```kotlin
val x = engine.block.getPositionX(block)
val xMode = engine.block.getPositionXMode(block)
val y = engine.block.getPositionY(block)
val yMode = engine.block.getPositionYMode(block)
engine.block.setPositionX(block, value = 0.25F)
engine.block.setPositionXMode(block, mode = PositionMode.PERCENT)
engine.block.setPositionY(block, value = 0.25)
engine.block.setPositionYMode(block, mode = PositionMode.PERCENT)

val rad = engine.block.getRotation(block)
engine.block.setRotation(block, radians = PI.toFloat())
val isFlipHorizontal = engine.block.isFlipHorizontal(block)
val isFlipVertical = engine.block.isFlipVertical(block)
engine.block.setFlipHorizontal(block, flip = true)
engine.block.setFlipVertical(block, flip = false)

val width = engine.block.getWidth(block)
val widthMode = engine.block.getWidthMode(block)
val height = engine.block.getHeight(block)
val heightMode = engine.block.getHeightMode(block)
engine.block.setWidth(block, value = 0.5F)
engine.block.setWidth(block, value = 2.5F, maintainCrop = true)
engine.block.setWidthMode(block, mode = SizeMode.PERCENT)
engine.block.setHeight(block, value = 0.5F)
engine.block.setHeight(block, value = 2.5F, maintainCrop = true)
engine.block.setHeightMode(block, mode = SizeMode.PERCENT)
val frameX = engine.block.getFrameX(block)
val frameY = engine.block.getFrameY(block)
val frameWidth = engine.block.getFrameWidth(block)
val frameHeight = engine.block.getFrameHeight(block)

engine.block.setAlwaysOnTop(block, false)
val isAlwaysOnTop = engine.block.isAlwaysOnTop(block)
engine.block.setAlwaysOnBottom(block, false)
val isAlwaysOnBottom = engine.block.isAlwaysOnBottom(block)
engine.block.bringToFront(block)
engine.block.sendToBack(block)
engine.block.bringForward(block)
engine.block.sendBackward(block)

val globalX = engine.block.getGlobalBoundingBoxX(block)
val globalY = engine.block.getGlobalBoundingBoxY(block)
val globalWidth = engine.block.getGlobalBoundingBoxWidth(block)
val globalHeight = engine.block.getGlobalBoundingBoxHeight(block)
val screenSpaceRect = engine.block.getScreenSpaceBoundingBoxRect(listOf(block))

engine.block.scale(block, scale = 2F, anchorX = 0.5F, anchorY = 0.5F)

engine.block.fillParent(block)

val pages = engine.scene.getPages()
engine.block.resizeContentAware(pages, width = 100F, height = 100F)

// Create blocks and append to scene
val member1 = engine.block.create(DesignBlockType.Graphic)
val member2 = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(scene, child = member1)
engine.block.appendChild(scene, child = member2)
if (engine.block.isDistributable(listOf(member1, member2))) {
  engine.block.distributeHorizontally(listOf(member1, member2))
  engine.block.distributeVertically(listOf(member1, member2))
}
if (engine.block.isAlignable(listOf(member1, member2))) {
  engine.block.alignHorizontally(listOf(member1, member2), alignment = HorizontalBlockAlignment.LEFT)
  engine.block.alignVertically(listOf(member1, member2), alignment = VerticalBlockAlignment.TOP)
}

val isTransformLocked = engine.block.isTransformLocked(block)
if (!isTransformLocked) {
  engine.block.setTransformLocked(block, locked = true)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
