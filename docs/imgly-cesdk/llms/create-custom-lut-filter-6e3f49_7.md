# Source: https://img.ly/docs/cesdk/macos/filters-and-effects/create-custom-lut-filter-6e3f49/

---
title: "Create a Custom LUT Filter"
description: "Create and apply custom LUT filters to achieve consistent, brand-aligned visual styles."
platform: macos
url: "https://img.ly/docs/cesdk/macos/filters-and-effects/create-custom-lut-filter-6e3f49/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Filters and Effects](https://img.ly/docs/cesdk/macos/filters-and-effects-6f88ac/) > [Apply Custom LUT Filter](https://img.ly/docs/cesdk/macos/filters-and-effects/create-custom-lut-filter-6e3f49/)

---

```swift file=@cesdk_swift_examples/engine-guides-custom-lut-filter/CustomLUTFilter.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func customLutFilter(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 100)
  try engine.block.setHeight(page, value: 100)
  try engine.block.appendChild(to: scene, child: page)
  try await engine.scene.zoom(to: scene, paddingLeft: 40.0, paddingTop: 40.0, paddingRight: 40.0, paddingBottom: 40.0)

  let rect = try engine.block.create(.graphic)
  try engine.block.setShape(rect, shape: engine.block.createShape(.rect))
  try engine.block.setWidth(rect, value: 100)
  try engine.block.setHeight(rect, value: 100)
  try engine.block.appendChild(to: page, child: rect)

  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg",
  )

  let lutFilter = try engine.block.createEffect(.lutFilter)
  try engine.block.setBool(lutFilter, property: "effect/enabled", value: true)
  try engine.block.setFloat(lutFilter, property: "effect/lut_filter/intensity", value: 0.9)
  try engine.block.setString(
    lutFilter,
    property: "effect/lut_filter/lutFileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png",
  )
  try engine.block.setInt(lutFilter, property: "effect/lut_filter/verticalTileCount", value: 5)
  try engine.block.setInt(lutFilter, property: "effect/lut_filter/horizontalTileCount", value: 5)

  try engine.block.appendEffect(rect, effectID: lutFilter)
  try engine.block.setFill(rect, fill: imageFill)
}
```

We use a technology called Lookup Tables (LUTs) in order to add new filters to our SDK.
The main idea is that colors respond to operations that are carried out during the filtering process. We 'record' that very response by applying the filter to the identity image shown below.

<img src="content-assets/6e3f49/identity.png" alt="Identity LUT" />

The resulting image can be used within our SDK and the recorded changes can then be applied to any image by looking up the transformed colors in the modified LUT.

If you want to create a new filter, you'll need to [download](content-assets/6e3f49/imgly_lut_ad1920_5_5_128.png) the identity LUT shown above, load it into an image editing software of your
choice, apply your operations, save it and add it to your app.

> **WARNING:** As any compression artifacts in the edited LUT could lead to distorted results when applying the filter, you need to save your LUT as a PNG file.

## Using Custom Filters

In this example, we will use a hosted CDN LUT filter file.
First we will load one of our demo scenes and change the first image to use LUT filter we will provide.
We will also configure the necessary setting based on the file.

LUT file we will use:

<img src="content-assets/6e3f49/imgly_lut_ad1920_5_5_128.png" alt="Color grading LUT showcasing a grid of color variations used for applying a specific visual style to images." />

## Load Scene

After the setup, we create a new scene. Within this scene, we create a page, set its dimensions, and append it to the scene. Lastly, we adjust the zoom level to properly fit the page into the view.

```javascript highlight-load-scene
let page = try engine.block.create(.page)
try engine.block.setWidth(page, value: 100)
try engine.block.setHeight(page, value: 100)
try engine.block.appendChild(to: scene, child: page)
try await engine.scene.zoom(to: scene, paddingLeft: 40.0, paddingTop: 40.0, paddingRight: 40.0, paddingBottom: 40.0)
```

## Create Rectangle

Next, we create a rectangle with defined dimensions and append it to the page. We will apply our LUT filter to this rectangle.

```javascript highlight-create-rect
let rect = try engine.block.create(.graphic)
try engine.block.setShape(rect, shape: engine.block.createShape(.rect))
try engine.block.setWidth(rect, value: 100)
try engine.block.setHeight(rect, value: 100)
try engine.block.appendChild(to: page, child: rect)
```

## Load Image

After creating the rectangle, we create an image fill with a specified URL. This will load the image as a fill for the rectangle to which we will apply the LUT filter.

```javascript highlight-create-image-fill
let imageFill = try engine.block.createFill(.image)
try engine.block.setString(
  imageFill,
  property: "fill/image/imageFileURI",
  value: "https://img.ly/static/ubq_samples/sample_1.jpg",
)
```

## Create LUT Filter

Now, we create a Look-Up Table (LUT) filter effect. We enable the filter, set its intensity, and provide a URL for the LUT file. We also define the tile count for the filter. The LUT filter effect is then applied to the rectangle and image should appear
black and white.

```javascript highlight-create-lut-filter
let lutFilter = try engine.block.createEffect(.lutFilter)
try engine.block.setBool(lutFilter, property: "effect/enabled", value: true)
try engine.block.setFloat(lutFilter, property: "effect/lut_filter/intensity", value: 0.9)
try engine.block.setString(
  lutFilter,
  property: "effect/lut_filter/lutFileURI",
  // swiftlint:disable:next line_length
  value: "https://cdn.img.ly/packages/imgly/cesdk-js/1.70.0/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png",
)
try engine.block.setInt(lutFilter, property: "effect/lut_filter/verticalTileCount", value: 5)
try engine.block.setInt(lutFilter, property: "effect/lut_filter/horizontalTileCount", value: 5)
```

## Apply LUT Filter

Finally, we apply the LUT filter effect to the rectangle, and set the image fill to the rectangle.
Before setting an image fill, we destroy the default rectangle fill.

```javascript highlight-apply-lut-filter
try engine.block.appendEffect(rect, effectID: lutFilter)
try engine.block.setFill(rect, fill: imageFill)
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func customLutFilter(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 100)
  try engine.block.setHeight(page, value: 100)
  try engine.block.appendChild(to: scene, child: page)
  try await engine.scene.zoom(to: scene, paddingLeft: 40.0, paddingTop: 40.0, paddingRight: 40.0, paddingBottom: 40.0)

  let rect = try engine.block.create(.graphic)
  try engine.block.setShape(rect, shape: engine.block.createShape(.rect))
  try engine.block.setWidth(rect, value: 100)
  try engine.block.setHeight(rect, value: 100)
  try engine.block.appendChild(to: page, child: rect)

  let imageFill = try engine.block.createFill(.image)
  try engine.block.setString(
    imageFill,
    property: "fill/image/imageFileURI",
    value: "https://img.ly/static/ubq_samples/sample_1.jpg"
  )

  let lutFilter = try engine.block.createEffect(.lutFilter)
  try engine.block.setBool(lutFilter, property: "effect/enabled", value: true)
  try engine.block.setFloat(lutFilter, property: "effect/lut_filter/intensity", value: 0.9)
  try engine.block.setString(
    lutFilter,
    property: "effect/lut_filter/lutFileURI",
    // swiftlint:disable:next line_length
    value: "https://cdn.img.ly/packages/imgly/cesdk-js/$UBQ_VERSION$/assets/extensions/ly.img.cesdk.filters.lut/LUTs/imgly_lut_ad1920_5_5_128.png"
  )
  try engine.block.setInt(lutFilter, property: "effect/lut_filter/verticalTileCount", value: 5)
  try engine.block.setInt(lutFilter, property: "effect/lut_filter/horizontalTileCount", value: 5)

  try engine.block.appendEffect(rect, effectID: lutFilter)
  try engine.block.setFill(rect, fill: imageFill)
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
