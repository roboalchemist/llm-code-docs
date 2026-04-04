# Source: https://img.ly/docs/cesdk/mac-catalyst/automation/auto-resize-4c2d58/

---
title: "Auto-Resize Blocks (Fill Parent & Percent Sizing)"
description: "Make blocks automatically fill their parent or resize proportionally using percent-based sizing. Learn when to use absolute vs. percent sizing, and how to build predictable, responsive layouts for automation."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/automation/auto-resize-4c2d58/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Automate Workflows](https://img.ly/docs/cesdk/mac-catalyst/automation-715209/) > [Auto-Resize](https://img.ly/docs/cesdk/mac-catalyst/automation/auto-resize-4c2d58/)

---

Sometimes you don’t want to hard-code widths and heights. You want elements that *just fit*. You need a background that always covers the page, an overlay that scales with its container, or a column that takes up exactly half the parent. CE.SDK supports this through **size modes** and **percent-based sizing**, plus a one-liner convenience API that makes a block **fill its parent**. You set size modes per axis and use `0.0…1.0` values to express percentages; you can then query **computed frame dimensions** once layout stabilizes.

### Why It Matters for Automation

When you generate designs in bulk, you can’t manually correct layout differences for each image. **Percentage-based sizing** and `fillParent()` guarantee that every inserted asset or background automatically scales to the right dimensions, regardless of its original size or aspect ratio. This ensures **reliable layouts** and **predictable exports** in automated pipelines.

## What You’ll Learn

- Make a block **fill its parent** in one line. This is perfect for backgrounds and overlays.
- Use **percent size modes** for responsive, predictable layouts.
- Read **computed** width and height after layout to verify results.
- Switch between **absolute** and **percent** sizing modes at runtime.
- Build a **responsive background** that always fits the page.

## When You’ll Use It

- Full-bleed **background images** that cover the page.
- **Responsive overlays** and watermarks that track the parent’s size.
- **Adaptive layouts** across iPhone, iPad, and Mac (Catalyst).
- **Automation workflows** that replace assets of different sizes without breaking layout consistency.

## Fill the Parent (One-Liner)

The simplest way to auto-resize is to ask the engine to make a block fill its parent:

```swift
// Make 'block' fill its parent container (resizes & positions).
try engine.block.fillParent(block)
```

CE.SDK resizes and positions the block, resets crop values if applicable, and switches content fill mode to `.cover` if needed to avoid invalid crops.

**Good for:** Page backgrounds, edge-to-edge color panels, full-page masks.

## Percent-Based Sizing (Responsive Layouts)

For finer control, switch size modes for width and height to `.percent`, then assign values from `0.0 ... 1.0`:

```swift
// 100% width & height (fill parent)
try engine.block.setWidthMode(block, mode: .percent)
try engine.block.setHeightMode(block, mode: .percent)
try engine.block.setWidth(block, value: 1.0)
try engine.block.setHeight(block, value: 1.0)
```

In percent mode, `1.0` means 100% of the parent. Use:

- `.absolute` for fixed-size elements.
- `.auto` when the content determines its own size.

## Partial Fill Examples

```swift
// 50% width, 100% height (e.g., a left column)
try engine.block.setWidthMode(block, mode: .percent)
try engine.block.setHeightMode(block, mode: .percent)
try engine.block.setWidth(block, value: 0.5)
try engine.block.setHeight(block, value: 1.0)
```

Great for split layouts, sidebars, or variable-width panels.

## Reading Computed Dimensions

After the engine completes a layout pass, you can read **computed** dimensions with the frame accessors:

```swift
let w = try engine.block.getFrameWidth(block)
let h = try engine.block.getFrameHeight(block)
```

These values are available **after** layout updates. If you query immediately after changes, you might see stale values. Yield a tick or wait for engine-driven updates before reading.

> **Note:** In Swift, using `try await Task.yield()` or deferring the read to the next run loop often suffices for demos.

## Switching Between Absolute & Percent

You can toggle sizing modes at runtime to move between fixed and responsive layouts:

```swift
// Fixed (absolute) sizing
try engine.block.setWidthMode(block, mode: .absolute)
try engine.block.setHeightMode(block, mode: .absolute)
try engine.block.setWidth(block, value: 400.0)
try engine.block.setHeight(block, value: 300.0)

// Back to responsive sizing
try engine.block.setWidthMode(block, mode: .percent)
try engine.block.setHeightMode(block, mode: .percent)
try engine.block.setWidth(block, value: 0.75) // 75% width
try engine.block.setHeight(block, value: 1.0)  // 100% height
```

Use **absolute** for fixed-size exports or print layouts, and **percent** for responsive layouts or template-based automation.

## Practical Example: Responsive Background

Here’s a common pattern. Create a background that always fills the page:

```swift
// 1) Create an image block and set its fill (placeholder asset)
let bg = try engine.block.create(.graphic)
let shape = try engine.block.createShape(.rect)
try engine.block.setShape(bg, shape: shape)

let solidColor = try engine.block.createFill(.color)
try engine.block.setFill(bg, fill: solidColor)

let rgbaGreen = Color.rgba(r: 0.5, g: 1, b: 0.5, a: 1)
try engine.block.setColor(solidColor, property: "fill/color/value", color: rgbaGreen)

// 2) Append to the page and send behind other content
try engine.block.appendChild(to: page, child: bg)
try engine.block.sendToBack(bg)

// 3) Either the one-liner:
try engine.block.fillParent(bg)

// 4) Or, percent-based equivalent:
try engine.block.setWidthMode(bg, mode: .percent)
try engine.block.setHeightMode(bg, mode: .percent)
try engine.block.setWidth(bg, value: 1.0)
try engine.block.setHeight(bg, value: 1.0)
```

The percent-based alternative mirrors the behavior of `fillParent` if your content and crop are already valid. The `fillParent` method guarantees coverage and sets a safe fill mode automatically.

## Automation Example: Batch Image Replacement

This automation scenario, generates name tags:

- Each tag has a dedicated container that:
  - Is called hero-frame.
  - Displays the person’s photo.
- The code prepares hero-frame **once** so it always fills its parent.
- It replaces the image fill inside hero-frame during batch generation.
- Layout stays stabless regardless of the photo’s size and aspect.

### Prepare Once

```swift
// One‑time setup when building the template/scene
let heroFrame = try engine.block.create(.graphic)
let rect = try engine.block.createShape(.rect)
try engine.block.setShape(heroFrame, shape: rect)

// Give it a name for easy lookup in later steps / debugging
try engine.block.setString(heroFrame, key: "name", value: "hero-frame")

// Attach an image fill now (can be a placeholder)
var heroFrameImageFill = try engine.block.createFill(.image)
try engine.block.setFill(heroFrame, fill: heroFrameImageFill)

// Place it in the nametag layout once (e.g., inside a card group or page)
try engine.block.appendChild(to: faceGroup, child: heroFrame)

// Make the container auto‑resize to its parent so the photo always fits
try engine.block.fillParent(heroFrame)
```

### Update During the Batch

At a later time, when the batch runs, it:

- Gets a reference to the `heroFrame` block
- Calls a function to update the image fill during each pass.

```swift
func replaceHeroPhotoURL(engine: Engine, hero: DesignBlockID, with url: String) {
  do {
    // Try to get the current fill and swap the image on the same object
    let fill = try engine.block.getFill(hero)
    try engine.block.setString(
      fill,
      property: "fill/image/fileURI",
      value: url
    )
  } catch {
    // If no fill exists yet, create and attach one
    print("No fill found on hero-frame; creating new fill.")
    do {
      let newFill = try engine.block.createFill(.image)
      try engine.block.setString(
        newFill,
        property: "fill/image/fileURI",
        value: url
      )
      try engine.block.setFill(hero, fill: newFill)
    } catch {
      print("Failed to attach new fill: \(error)")
    }
  }
}
```

Because `heroFrame` used `fillParent`, every image conforms to its parent’s size, ensuring layouts remain consistent. This approach is ideal for:

- Product catalogs
- User-generated templates
- Any workflow where image dimensions vary widely.

![Example of batch image replacement for nametags](assets/resize-example-ios-160-0.png)

In the preceding diagram, three input images are of **different sizes**. The engine **crops and resizes** them to fill the placeholder during the batch.

## Platform Notes & Limitations

- **Computed frame values are asynchronous.** Read them after a layout cycle. If you set percent sizing and immediately call `getFrameWidth`, you may get the previous value.
- **Groups vs. children.** Percent sizing relates a child to *its direct parent*. Ensure your block is appended where you expect before reading frames.
- **Fills and crops.** `fillParent` may reset crop values and/or set fill mode to `.cover` to avoid invalid states.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Block doesn’t resize with parent | Width/height modes aren’t set to `.percent` | Set `setWidthMode(.percent)` / `setHeightMode(.percent)` and assign `0…1` values. |
| Computed width/height are `0` or stale | Reading before layout settled | Defer reads; yield a tick before `getFrameWidth/Height`. |
| Only one axis resizes | Only one axis set to `.percent` | Set both axes to `.percent` (or use `fillParent`). |
| Unexpected crop after fill | `fillParent` adjusted crop/fill mode | Use percent sizing manually if you need to preserve a crop. |
| Child ignores parent size | Wrong parent in hierarchy | Verify `appendChild` target and recheck computed frames after update. |

## Next Steps

Explore a code sample of percentage resizing and `.fillParent` on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/engine_guides_autoresize).

You can use auto-resize as you create compositions and make responsive designs. Here are some other guides to explore to deepen your understanding.

- [Resize blocks (manual)](https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform/resize-407242/) — control dimensions interactively.



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
