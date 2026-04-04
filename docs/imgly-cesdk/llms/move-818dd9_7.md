# Source: https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform/move-818dd9/

---
title: "Move"
description: "Position an image relative to its parent using either percentage or units"
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform/move-818dd9/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Create and Edit Images](https://img.ly/docs/cesdk/mac-catalyst/edit-image-c64912/) > [Transform](https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform-9d189b/) > [Move](https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform/move-818dd9/)

---

This guide shows how to move images on the canvas using CE.SDK in your iOS
app. You’ll learn how to reposition single elements, move groups, and
constrain movement behavior within templates. You can move elements
programmatically or by using the built-in IMG.LY UI.

## What you'll learn

- Move images programmatically using Swift
- Use the IMG.LY UI to drag images
- Adjust image position on the canvas
- Move multiple blocks together
- Constrain image movement in templates

## When to use

Use movement to:

- Position content precisely in designs
- Align images with text, backgrounds, or grid layouts
- Enable drag-and-drop or animated movement workflows

***

## Move an image block programmatically

Image position is controlled using the `position/x` and `position/y` properties. They can either use absolute or percentage (relative) values. In addition to setting the properties, there are helper functions.

```swift
try engine.block.setFloat(imageBlock, property: "position/x", value: 150)
try engine.block.setFloat(imageBlock, property: "position/y", value: 100)
```

or

```swift
try engine.block.setPositionX(imageBlock, value: 150)
try engine.block.setPositionY(imageBlock, value: 150)
```

This moves the image to coordinates (150, 100) on the canvas.

```swift
try engine.block.setPositionXMode(imageBlock, mode: .percent)
try engine.block.setPositionYMode(imageBlock, mode: .percent)
try engine.block.setPositionX(imageBlock, value: 0.5)
try engine.block.setPositionY(imageBlock, value: 0.5)
```

This move the image to the center of the canvas, regardless of the dimensions of the canvas. As with setting position, you can update or check the mode using `position/x/mode` and `position/y/mode` properties.

```swift
let xPosition = try engine.block.getPositionX(imageBlock)
let yPosition = try engine.block.getPositionY(imageBlock)
```

***

## Move images with the UI

Users can drag and drop elements directly in the editor canvas.

***

## Move multiple elements together

Group elements before moving to keep them aligned:

```swift
let groupId = try engine.block.group([imageBlockId, textBlockId])
try engine.block.setPositionX(groupId, value: 200)
```

This moves the entire group to 200 from the left edge.

***

## Move relative to current position

To nudge an image instead of setting an absolute position:

```swift
let xPosition = try engine.block.getPositionX(imageBlock)
try engine.block.setPositionX(imageBlock, value: xPosition + 20)
```

This moves the image 20 points to the right.

***

## Lock movement (optional)

When building templates, you might want to lock movement to protect the layout:

```swift
try engine.block.setScopeEnabled(block, key: "layer/move", enabled: false)
```

You can also disable all transformations by locking, this is regardless of working with a template.

```swift
try engine.block.setTransformLocked(block, locked: true)
```

***

## Troubleshooting

| Issue                    | Solution                                              |
| ------------------------ | ----------------------------------------------------- |
| Image not moving         | Ensure it is not constrained or locked                |
| Unexpected position      | Check canvas coordinates and alignment settings       |
| Grouped items misaligned | Confirm all items share the same reference point      |
| Can't move via UI        | Ensure the move feature is enabled in the UI settings |

***



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
