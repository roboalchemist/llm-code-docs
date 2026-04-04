# Source: https://img.ly/docs/cesdk/macos/insert-media/position-and-align-cc6b6a/

---
title: "Positioning and Alignment"
description: "Precisely position, align, and distribute objects using guides, snapping, and alignment tools."
platform: macos
url: "https://img.ly/docs/cesdk/macos/insert-media/position-and-align-cc6b6a/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/macos/create-composition-db709c/) > [Position and Align](https://img.ly/docs/cesdk/macos/insert-media/position-and-align-cc6b6a/)

---

```swift reference-only
let x = try engine.block.getPositionX(block)
let xMode = try engine.block.getPositionXMode(block)
let y = try engine.block.getPositionY(block)
let yMode = try engine.block.getPositionYMode(block)
try engine.block.setPositionX(block, value: 0.25)
try engine.block.setPositionXMode(block, mode: .percent)
try engine.block.setPositionY(block, value: 0.25)
try engine.block.setPositionYMode(block, mode: .percent)

let rad = try engine.block.getRotation(block)
try engine.block.setRotation(block, radians: .pi)
let flipHorizontal = try engine.block.getFlipHorizontal(block)
let flipVertical = try engine.block.getFlipVertical(block)
try engine.block.setFlipHorizontal(block, flip: true)
try engine.block.setFlipVertical(block, flip: false)

let width = try engine.block.getWidth(block)
let widthMode = try engine.block.getWidthMode(block)
let height = try engine.block.getHeight(block)
let heightMode = try engine.block.getHeightMode(block)
try engine.block.setWidth(block, value: 0.5)
try engine.block.setWidth(block, value: 2.5, maintainCrop: true)
try engine.block.setWidthMode(block, mode: .percent)
try engine.block.setHeight(block, value: 0.5)
try engine.block.setHeight(block, value: 2.5, maintainCrop: true)
try engine.block.setHeightMode(block, mode: .percent)
let frameX = try engine.block.getFrameX(block)
let frameY = try engine.block.getFrameY(block)
let frameWidth = try engine.block.getFrameWidth(block)
let frameHeight = try engine.block.getFrameHeight(block)

try engine.block.setAlwaysOnTop(block, enabled: false)
let isAlwaysOnTop = try engine.block.isAlwaysOnTop(block)
try engine.block.setAlwaysOnBottom(block, enabled: false)
let isAlwaysOnBottom = try engine.block.isAlwaysOnBottom(block)
try engine.block.bringToFront(block)
try engine.block.sendToBack(block)
try engine.block.bringForward(block)
try engine.block.sendBackward(block)

let globalX = try engine.block.getGlobalBoundingBoxX(block)
let globalY = try engine.block.getGlobalBoundingBoxY(block)
let globalWidth = try engine.block.getGlobalBoundingBoxWidth(block)
let globalHeight = try engine.block.getGlobalBoundingBoxHeight(block)
let screenSpaceRect = try engine.block.getScreenSpaceBoundingBox(containing: [block])

try engine.block.scale(block, to: 2.0, anchorX: 0.5, anchorY: 0.5)

try engine.block.scale(block, to: 2.0, anchorX: 0.5, anchorY: 0.5)

try engine.block.fillParent(block)

let pages = try engine.scene.getPages()
try engine.block.resizeContentAware(pages, width: 100.0, height: 100.0)

// Create blocks and append to scene
let member1 = try engine.block.create(.graphic)
let member2 = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: member1)
try engine.block.appendChild(to: scene, child: member2)
if try engine.block.isDistributable([member1, member2]) {
  try engine.block.distributeHorizontally([member1, member2])
  try engine.block.distributeVertically([member1, member2])
}
if try engine.block.isAlignable([member1, member2]) {
  try engine.block.alignHorizontally([member1, member2], alignment: .left)
  try engine.block.alignVertically([member1, member2], alignment: .top)
}

let isTransformLocked = try engine.block.isTransformLocked(block)
if !isTransformLocked {
  try engine.block.setTransformLocked(block, locked: true)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify scenes layout through the `block` API.

## Layout of Blocks

> **Note:** **Note on layout and frame size** The frame size is determined during the
> layout phase of the render process inside the engine. This means that calling
> `getFrameSize()` immediately after modifying the scene might return an
> inaccurate result.

The CreativeEngine supports three different modes for positioning blocks. These can be set for each block and both coordinates independently:

- `'Absolute'`: the position value is interpreted in the scene's current design unit.
- `'Percent'`: the position value is interpreted as percentage of the block's parent's size, where 1.0 means 100%.
- `'Auto'` : the position is automatically determined.

Likewise there are also three different modes for controlling a block's size. Again both dimensions can be set independently:

- `'Absolute'`: the size value is interpreted in the scene's current design unit.
- `'Percent'`: the size value is interpreted as percentage of the block's parent's size, where 1.0 means 100%.
- `'Auto'` : the block's size is automatically determined by the size of the block's content.

### Positioning

```swift
public func getPositionX(_ id: DesignBlockID) throws -> Float
```

Query a block's x position.

- `id:`: The block to query.
- Returns: The value of the x position.

```swift
public func getPositionY(_ id: DesignBlockID) throws -> Float
```

Query a block's y position.

- `id:`: The block to query.
- Returns: The value of the y position.

```swift
public func getPositionXMode(_ id: DesignBlockID) throws -> PositionMode
```

Query a block's mode for its x position.

- `id:`: The block to query.
- Returns: The current mode for the x position: absolute, percent or undefined.

```swift
public func getPositionYMode(_ id: DesignBlockID) throws -> PositionMode
```

Query a block's mode for its y position.

- `id:`: The block to query.
- Returns: The current mode for the y position: absolute, percent or undefined.

```swift
public func setPositionX(_ id: DesignBlockID, value: Float) throws
```

Update a block's x position.
The position refers to the block's local space, relative to its parent with the origin at the top left.
Required scope: "layer/move"

- `id`: The block to update.
- `value`: The value of the x position.

```swift
public func setPositionY(_ id: DesignBlockID, value: Float) throws
```

Update a block's y position.
The position refers to the block's local space, relative to its parent with the origin at the top left.
Required scope: "layer/move"

- `id`: The block to update.
- `value`: The value of the y position.

```swift
public func setPositionXMode(_ id: DesignBlockID, mode: PositionMode) throws
```

Set a block's mode for its x position.
Required scope: "layer/move"

- `id`: The block to update.
- `mode`: The x position mode: absolute, percent or undefined.

```swift
public func setPositionYMode(_ id: DesignBlockID, mode: PositionMode) throws
```

Set a block's mode for its y position.
Required scope: "layer/move"

- `id`: The block to update.
- `mode`: The y position mode: absolute, percent or undefined.

### Layers

```swift
public func setAlwaysOnTop(_ id: DesignBlockID, enabled: Bool) throws
```

Set a block to be always-on-top. If true, this blocks's global sorting order is automatically adjusted to
be higher than all other siblings without this property. If more than one block is set to be always-on-top,
the child order decides which is on top.

- `id`: The block to update.
- `enabled`: The new state.

```swift
public func isAlwaysOnTop(_ id: DesignBlockID) throws -> Bool
```

If a block is set to be always-on-top.

- `id`: The block to query.

```swift
public func setAlwaysOnBottom(_ id: DesignBlockID, enabled: Bool) throws
```

Set a block to be always-on-bottom. If true, this blocks's global sorting order is automatically adjusted to
be lower than all other siblings without this property. If more than one block is set to be always-on-bottom,
the child order decides which is on the bottom.

- `id`: The block to update.
- `enabled`: The new state.

```swift
public func isAlwaysOnBottom(_ id: DesignBlockID) throws -> Bool
```

If a block is set to be always-on-bottom.

- `id`: The block to query.

```swift
public func bringToFront(_ id: DesignBlockID) throws
```

Updates the sorting order of this block and all of its manually created siblings so that the given block has
the highest sorting order.
If the block is parented to a track, it is first moved up in the hierarchy.

- `id`: The block to update.

```swift
public func sendToBack(_ id: DesignBlockID) throws
```

Updates the sorting order of this block and all of its manually created siblings so that the given block has
the lowest sorting order.
If the block is parented to a track, it is first moved up in the hierarchy.

- `id`: The block to update.

```swift
public func bringForward(_ id: DesignBlockID) throws
```

Updates the sorting order of this block and all of its superjacent siblings so that the given block has a
higher sorting order than the next superjacent sibling.
If the block is parented to a track, it is first moved up in the hierarchy.
Empty tracks and empty groups are passed by.

- `id`: The block to update.

```swift
public func sendBackward(_ id: DesignBlockID) throws
```

Updates the sorting order of this block and all of its manually created and subjacent siblings so that the
given block will have a lower sorting order than the next subjacent sibling.
If the block is parented to a track, it is first moved up in the hierarchy.
Empty tracks and empty groups are passed by.

- `id`: The block to update.

### Size

```swift
public func getWidth(_ id: DesignBlockID) throws -> Float
```

Query a block's width.

- `id:`: The block to query.
- Returns: The value of the block's width.

```swift
public func getWidthMode(_ id: DesignBlockID) throws -> SizeMode
```

Query a block's mode for its width.

- `id:`: The block to query.
- Returns: The current mode for the width: absolute, percent or auto.

```swift
public func getHeight(_ id: DesignBlockID) throws -> Float
```

Query a block's height.

- `id:`: The block to query.
- Returns: The value of the block's height.

```swift
public func getHeightMode(_ id: DesignBlockID) throws -> SizeMode
```

Query a block's mode for its height.

- `id:`: The block to query.
- Returns: The current mode for the height: absolute, percent or auto.

```swift
public func setWidth(_ id: DesignBlockID, value: Float, maintainCrop: Bool = false) throws
```

Update a block's width and optionally maintain the crop.
If the crop is maintained, the crop values will be automatically adjusted.
The content fill mode `Cover` is only kept if the `features/transformEditsRetainCoverMode` setting is enabled,
otherwise it will change to `Crop`.
Required scope: "layer/resize"

- `id`: The block to update.
- `value`: The new width of the block.
- `maintainCrop`: Whether or not the crop values, if available, should be automatically adjusted.

```swift
public func setWidthMode(_ id: DesignBlockID, mode: SizeMode) throws
```

Set a block's mode for its width.
Required scope: "layer/resize"

- `id`: The block to update.
- `mode`: The width mode.

```swift
public func setHeight(_ id: DesignBlockID, value: Float, maintainCrop: Bool = false) throws
```

Update a block's height and optionally maintain the crop.
If the crop is maintained, the crop values will be automatically adjusted.
The content fill mode `Cover` is only kept if the `features/transformEditsRetainCoverMode` setting is enabled,
otherwise it will change to `Crop`.
Required scope: "layer/resize"

- `id`: The block to update.
- `value`: The new height of the block.
- `maintainCrop`: Whether or not the crop values, if available, should be automatically adjusted.
  features/transformEditsRetainCoverMode is enabled.

```swift
public func setHeightMode(_ id: DesignBlockID, mode: SizeMode) throws
```

Set a block's mode for its height.
Required scope: "layer/resize"

- `id`: The block to update.
- `mode`: The height mode.

### Rotation

```swift
public func getRotation(_ id: DesignBlockID) throws -> Float
```

Query a block's rotation in radians.

- `id:`: The block to query.
- Returns: The block's rotation around its center in radians.

```swift
public func setRotation(_ id: DesignBlockID, radians: Float) throws
```

Update a block's rotation.
Required scope: "layer/rotate"

- `id`: The block to update.
- `radians`: The new rotation in radians. Rotation is applied around the block's center.

### Flipping

```swift
public func setFlipHorizontal(_ id: DesignBlockID, flip: Bool) throws
```

Update a block's horizontal flip.
Required scope: "layer/flip"

- `id`: The block to update.
- `flip`: If the flip should be enabled.

```swift
public func getFlipHorizontal(_ id: DesignBlockID) throws -> Bool
```

Query a block's horizontal flip state.

- `id:`: The block to query.
- Returns: A boolean indicating for whether the block is flipped in the queried direction.

```swift
public func setFlipVertical(_ id: DesignBlockID, flip: Bool) throws
```

Update a block's vertical flip.
Required scope: "layer/flip"

- `id`: The block to update.
- `flip`: If the flip should be enabled.

```swift
public func getFlipVertical(_ id: DesignBlockID) throws -> Bool
```

Query a block's vertical flip state.

- `id:`: The block to query.
- Returns: A boolean indicating for whether the block is flipped in the queried direction.

### Scaling

```swift
public func scale(_ id: DesignBlockID, to scale: Float, anchorX: Float = 0, anchorY: Float = 0) throws
```

Scales the block and all of its children proportionally around the specified
relative anchor point.
This updates the position, size and style properties (e.g. stroke width) of
the block and its children.
Required scope: "layer/resize"

- `id`: The block that should be scaled.
- `scale`: The scale factor to be applied to the current properties of the block.
- `anchorX`: The relative position along the width of the block around which the
  scaling should occur. (0 = left edge, 0.5 = center, 1 = right edge)
- `anchorY`: The relative position along the height of the block around which the
  scaling should occur. (0 = top edge, 0.5 = center, 1 = bottom edge)

### Fill a Block's Parent

```swift
public func fillParent(_ id: DesignBlockID) throws
```

Resize and position a block to entirely fill its parent block.
The crop values of the block, except for the flip and crop rotation, are reset if it can be cropped.
If the size of the block's fill is unknown, the content fill mode is changed from `Crop` to `Cover` to prevent
invalid crop values.
Required scope: "layer/move"

- "layer/resize"
- `id:`: The block that should fill its parent.

### Resize Blocks Content-aware

```swift
public func resizeContentAware(_ ids: [DesignBlockID], width: Float, height: Float) throws
```

Resize all blocks to the given size. The content of the blocks is automatically adjusted to fit the new
dimensions.
Required scope: "layer/resize"

- `ids`: The blocks to resize.
- `width`: The new width of the blocks.
- `height`: The new height of the blocks.
- Returns: An error if the blocks could not be resized.

### Even Distribution

```swift
public func isDistributable(_ ids: [DesignBlockID]) throws -> Bool
```

Confirms that a given set of blocks can be distributed.

- `ids:`: A non-empty array of block ids.
- Returns: Whether the blocks can be distributed.

```swift
public func distributeHorizontally(_ ids: [DesignBlockID]) throws
```

Distribute multiple blocks horizontally within their bounding box so that the space between them is even.
Required scope: "layer/move"

- `ids:`: A non-empty array of block ids.

```swift
public func distributeVertically(_ ids: [DesignBlockID]) throws
```

Distribute multiple blocks vertically within their bounding box so that the space between them is even.
Required scope: "layer/move"

- `ids:`: A non-empty array of block ids.

### Alignment

```swift
public func isAlignable(_ ids: [DesignBlockID]) throws -> Bool
```

Confirms that a given set of blocks can be aligned.

- `ids:`: A non-empty array of block ids.
- Returns: Whether the blocks can be aligned.

```swift
public func alignHorizontally(_ ids: [DesignBlockID], alignment: HorizontalBlockAlignment) throws
```

Align multiple blocks horizontally within their bounding box or a single block to its parent.
Required scope: "layer/move"

- `ids:`: A non-empty array of block ids.
- `alignment:`: How they should be aligned: left, right, or center

```swift
public func alignVertically(_ ids: [DesignBlockID], alignment: VerticalBlockAlignment) throws
```

Align multiple blocks vertically within their bounding box or a single block to its parent.
Required scope: "layer/move"

- `ids:`: A non-empty array of block ids.
- `alignment:`: How they should be aligned: top, bottom, or center

### Computed Dimensions

```swift
public func getFrameX(_ id: DesignBlockID) throws -> Float
```

Get a block's layout position on the x-axis. The layout position is only available after an
internal update loop, which may not happen immediately.

- `id:`: The block to query.
- Returns: The layout position on the x-axis.

```swift
public func getFrameY(_ id: DesignBlockID) throws -> Float
```

Get a block's layout position on the y-axis. The layout position is only available after an
internal update loop, which may not happen immediately.

- `id:`: The block to query.
- Returns: The layout position on the y-axis.

```swift
public func getFrameWidth(_ id: DesignBlockID) throws -> Float
```

Get a block's layout width. The layout width is only available after an
internal update loop, which may not happen immediately.

- `id:`: The block to query.
- Returns: The layout width.

```swift
public func getFrameHeight(_ id: DesignBlockID) throws -> Float
```

Get a block's layout height. The layout height is only available after an
internal update loop, which may not happen immediately.

- `id:`: The block to query.
- Returns: The layout height.

```swift
public func getGlobalBoundingBoxX(_ id: DesignBlockID) throws -> Float
```

Get the x position of the block's axis-aligned bounding box in the scene's global coordinate space.
The scene's global coordinate space has its origin at the top left.

- `id:`: The block whose bounding box should be calculated.
- Returns: The x coordinate of the position of the axis-aligned bounding box.

```swift
public func getGlobalBoundingBoxY(_ id: DesignBlockID) throws -> Float
```

Get the y position of the block's axis-aligned bounding box in the scene's global coordinate space.
The scene's global coordinate space has its origin at the top left.

- `id:The`: block whose bounding box should be calculated.
- Returns: The y coordinate of the position of the axis-aligned bounding box.

```swift
public func getGlobalBoundingBoxWidth(_ id: DesignBlockID) throws -> Float
```

Get the width of the block's axis-aligned bounding box in the scene's global coordinate space.
The scene's global coordinate space has its origin at the top left.

- `id:`: The block whose bounding box should be calculated.
- Returns: The width of the axis-aligned bounding box.

```swift
public func getGlobalBoundingBoxHeight(_ id: DesignBlockID) throws -> Float
```

Get the height of the block's axis-aligned bounding box in the scene's global coordinate space.
The scene's global coordinate space has its origin at the top left.

- `id:`: The block whose bounding box should be calculated.
- Returns: The height of the axis-aligned bounding box.

```swift
public func getScreenSpaceBoundingBox(containing blocks: [DesignBlockID]) throws -> CGRect
```

Get the position and size of the axis-aligned bounding box for the given blocks in screen space.

- `blocks:`: The blocks whose bounding box should be calculated.
- Returns: The position and size of the bounding box as `CGRect` (in points).

### Transform Locking

You can lock the transform of a block to prevent changes to any of its transformations. That is the block's position, rotation, scale, and sizing.

```swift
public func isTransformLocked(_ id: DesignBlockID) throws -> Bool
```

Query a block's transform locked state. If `true`, the block's transform can't be changed.

- `id:`: The block to query.
- Returns: `True` if transform locked, `false` otherwise.

```swift
public func setTransformLocked(_ id: DesignBlockID, locked: Bool) throws
```

Update a block's transform locked state.

- `id`: The block to update.
- `locked`: Whether the block's transform should be locked.

## Full Code

Here's the full code:

```swift
let x = try engine.block.getPositionX(block)
let xMode = try engine.block.getPositionXMode(block)
let y = try engine.block.getPositionY(block)
let yMode = try engine.block.getPositionYMode(block)
try engine.block.setPositionX(block, value: 0.25)
try engine.block.setPositionXMode(block, mode: .percent)
try engine.block.setPositionY(block, value: 0.25)
try engine.block.setPositionYMode(block, mode: .percent)

let rad = try engine.block.getRotation(block)
try engine.block.setRotation(block, radians: .pi)
let flipHorizontal = try engine.block.getFlipHorizontal(block)
let flipVertical = try engine.block.getFlipVertical(block)
try engine.block.setFlipHorizontal(block, flip: true)
try engine.block.setFlipVertical(block, flip: false)

let width = try engine.block.getWidth(block)
let widthMode = try engine.block.getWidthMode(block)
let height = try engine.block.getHeight(block)
let heightMode = try engine.block.getHeightMode(block)
try engine.block.setWidth(block, value: 0.5)
try engine.block.setWidth(block, value: 2.5, maintainCrop: true)
try engine.block.setWidthMode(block, mode: .percent)
try engine.block.setHeight(block, value: 0.5)
try engine.block.setHeight(block, value: 2.5, maintainCrop: true)
try engine.block.setHeightMode(block, mode: .percent)
let frameX = try engine.block.getFrameX(block)
let frameY = try engine.block.getFrameY(block)
let frameWidth = try engine.block.getFrameWidth(block)
let frameHeight = try engine.block.getFrameHeight(block)

try engine.block.setAlwaysOnTop(block, enabled: false)
let isAlwaysOnTop = try engine.block.isAlwaysOnTop(block)
try engine.block.setAlwaysOnBottom(block, enabled: false)
let isAlwaysOnBottom = try engine.block.isAlwaysOnBottom(block)
try engine.block.bringToFront(block)
try engine.block.sendToBack(block)
try engine.block.bringForward(block)
try engine.block.sendBackward(block)

let globalX = try engine.block.getGlobalBoundingBoxX(block)
let globalY = try engine.block.getGlobalBoundingBoxY(block)
let globalWidth = try engine.block.getGlobalBoundingBoxWidth(block)
let globalHeight = try engine.block.getGlobalBoundingBoxHeight(block)
let screenSpaceRect = try engine.block.getScreenSpaceBoundingBox(containing: [block])

try engine.block.scale(block, to: 2.0, anchorX: 0.5, anchorY: 0.5)

try engine.block.scale(block, to: 2.0, anchorX: 0.5, anchorY: 0.5)

try engine.block.fillParent(block)

let pages = try engine.scene.getPages()
try engine.block.resizeContentAware(pages, width: 100.0, height: 100.0)

// Create blocks and append to scene
let member1 = try engine.block.create(.graphic)
let member2 = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: member1)
try engine.block.appendChild(to: scene, child: member2)
if try engine.block.isDistributable([member1, member2]) {
  try engine.block.distributeHorizontally([member1, member2])
  try engine.block.distributeVertically([member1, member2])
}
if try engine.block.isAlignable([member1, member2]) {
  try engine.block.alignHorizontally([member1, member2], alignment: .left)
  try engine.block.alignVertically([member1, member2], alignment: .top)
}

let isTransformLocked = try engine.block.isTransformLocked(block)
if !isTransformLocked {
  try engine.block.setTransformLocked(block, locked: true)
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
