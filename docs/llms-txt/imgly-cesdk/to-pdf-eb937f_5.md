# Source: https://img.ly/docs/cesdk/mac-catalyst/conversion/to-pdf-eb937f/

---
title: "Convert Compositions To PDF"
description: "Convert your compositions to PDF for export and print."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/conversion/to-pdf-eb937f/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Conversion](https://img.ly/docs/cesdk/mac-catalyst/conversion-c3fbb3/) > [To PDF](https://img.ly/docs/cesdk/mac-catalyst/conversion/to-pdf-eb937f/)

---

Automate PDF creation entirely in Swift. Load assets, build single- or multi-page scenes, set page size and DPI, and export to PDF. All without presenting the editor UI.

## What You’ll Learn

- Create scenes and pages programmatically.
- Place images and fit/cover them on the page.
- Export a single page or the entire scene to PDF.
- Apply print options: scene DPI, high-compatibility, underlayer (spot color + offset).
- Persist/share the resulting PDF file.

## When to Use It

- Batch generation, server-style workflows on device.
- Custom UIs where you control layout and export.
- Printing to non-white stock requiring an underlayer.
- Create and export (single page vs whole scene)

## Plain PDF Creation

For creating PDFs, the CE.SDK provides an `.export` function in the `block` API. Exporting a `page` creates a single-page PDF. Export a `scene` when you want a multi-page PDF. The `Data` objects that the functions below return are PDFs. Your app can share them, send them to print, or whatever your workflow requires.

```swift
import IMGLYEngine

@MainActor
func exportCurrentPageToPDF(engine: Engine) async throws -> Data {
  let page = try engine.page.get()
  return try await engine.block.export(page, mimeType: .pdf)
}

@MainActor
func exportWholeSceneToPDF(engine: Engine) async throws -> Data {
  let scene = try engine.scene.get()
  return try await engine.block.export(scene, mimeType: .pdf)
}
```

> **Note:** Your app can create `.jpg`, `.png`, and other formats by changing the `mimeType` parameter of the `.export` function. Video and audio exports use other export functions.

## Build a Multi-Page Scene From Images

The function below starts with an array of image URLs. For each URL, the code:

1. Creates a page and adds it to the scene.
2. Creates a rectangular block to hold the image.
3. Loads the contents of each URL as an image fill for a block.
4. Resizes the block to be the same size as the page.
5. Creates a PDF from the entire scene, which contains every page.

```swift
@MainActor
func buildMultiPagePDF(from urls: [URL], engine: Engine) async throws -> Data {
  //Create a scene
  let scene = try engine.scene.create()
  
  for url in urls {
    //Create a page and add it to the scene
    let page = try engine.block.create(.page)
    try engine.block.appendChild(to: scene, child: page)

    //Create a rectangular block to hold the image
    let graphic = try engine.block.create(.graphic)
    let shape = try engine.block.createShape(.rect)
    try engine.block.setShape(graphic, shape: shape)
    try engine.block.appendChild(to: page, child: graphic)

    //Fill the block with the image from the URL
    let fill = try engine.block.createFill(.image)
    try engine.block.setString(fill, property: "fill/image/fileURI", value: url.absoluteString)
    try engine.block.setFill(graphic, fill: fill)

    //Resize the block to fill it’s parent
    try engine.block.fillParent(graphic)
  }
  
  //Convert the scene and all of its children to a pdf.
  return try await engine.block.export(scene, mimeType: .pdf)
}
```

## Page Size & DPI

PDF size follows the page size. By default scenes and pages have a DPI of 300 but don’t have a predefined paper size. Set width and height of the pages **before** export. The helper below defines some common page sizes.

```swift
enum PagePreset { case usLetterPortrait, usLetterLandscape, a4Portrait, a4Landscape, custom(Float, Float) }

@MainActor
func setPageSize(page: DesignBlockID, preset: PagePreset, engine: Engine) throws {
    let (w,h): (Float,Float) = switch preset {
        case .usLetterPortrait: (2550,3300)
        case .usLetterLandscape: (3300,2550)
        case .a4Portrait: (2480,3508)
        case .a4Landscape: (3508,2480)
        case let .custom(W,H): (W,H)
    }
    try engine.block.setWidth(page, value: w)
    try engine.block.setHeight(page, value: h)
}
```

The DPI of the scene:

- Affects the rasterization quality of the PDF (see the next section).
- Doesn’t change the page size when modified.
- Can be set and read using the "scene/dpi" property of a scene.

## High-compatibility & Underlayer (print)

The `.export` function has an optional structure where you can set configuration. This structure is the same for **every** mime type that `.export` supports, not just PDF. For a PDF export these options apply:

- `exportPdfWithHighCompatibility` - Exports the PDF document with a higher compatibility to different PDF viewers. Bitmap images and some effects like gradients are rasterized with the scene’s DPI setting instead of embedding them directly.
- `exportPdfWithUnderlayer` - Export the PDF document with an underlayer. The export generates an underlayer by adding a graphics block behind the existing elements of the shape of the elements. This is useful when printing on non-standard media, like glass.
- `underlayerSpotColorName` - The name of the spot color to use to fill the underlayer.
- `underlayerOffset` - The adjustment in size of the shape of the underlayer.

```swift
@MainActor
func exportWithPrintOptions(engine: Engine) async throws -> Data {
    let scene = try engine.scene.get()
    try engine.block.setFloat(scene, property: "scene/dpi", value: 300)
    engine.editor.setSpotColor(name: "RDG_WHITE", r: 0.8, g: 0.8, b: 0.8)

    let opts = ExportOptions(
        exportPdfWithHighCompatibility: true,
        exportPdfWithUnderlayer: true,
        underlayerSpotColorName: "RDG_WHITE",
        underlayerOffset: -2
    )
    return try await engine.block.export(scene, mimeType: .pdf, options: opts)
}
```

## Save/share

Once the export completes, your app can save the PDF data to the user’s directories or write the it to a temporary URL and present `UIActivityViewController` or `ShareLink`.

## Troubleshooting

**❌ PDF is rasterized / too big**:

Disable `exportPdfWithHighCompatibility` to preserve vectors where possible. If you need compatibility, reduce `"scene/dpi"` (for example, 150 vs 300) to control size.

**❌ Underlayer isn’t visible in the printed result**:

Make sure you **don’t flatten the PDF** in post-processing, the spot color name matches the print shop’s setup exactly, and the underlayer offset is appropriate for your media.

**❌ Colors don’t match the brand**:

Confirm you’re using the correct color model. For brand-critical workflows, coordinate spot color naming with your printer and avoid unnecessary conversions down-stream. Explore more in the [spot color](https://img.ly/docs/cesdk/mac-catalyst/colors-a9b79c/) guide.

**❌ Can’t change PDF page size at export**:

That’s expected. Set page `width`/`height` on your pages before export; the PDF follows the page size. The `targetWidth`/`targetHeight` export options are for some image formats (PNG/JPEG/WEBP), not PDF.

**❌ Multi-page export only gives one page**:

Ensure you export the scene (not just a page) and that your scene actually contains more than one page block.

## Next Steps

Now that you're able to export your creations as PDF, explore some related topics to perfect your workflow:

- [Save](https://img.ly/docs/cesdk/mac-catalyst/export-save-publish/save-c8b124/) Scenes – persist .scene/.zip and restore later to reproduce exports.
- [Asset Sources & Upload](https://img.ly/docs/cesdk/mac-catalyst/import-media-4e3703/) – bring user images/videos in, then export as PDF.
- [Image Crop & Fit](https://img.ly/docs/cesdk/mac-catalyst/edit-image/transform-9d189b/) – control how images fill pages before exporting (cover vs fit).



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
