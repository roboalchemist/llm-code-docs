# Source: https://img.ly/docs/cesdk/ios/export-save-publish/create-thumbnail-749be1/

---
title: "Create Thumbnail"
description: "Generate small preview images for scenes and pages using CE.SDK export options."
platform: ios
url: "https://img.ly/docs/cesdk/ios/export-save-publish/create-thumbnail-749be1/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Export Media Assets](https://img.ly/docs/cesdk/ios/export-save-publish/export-82f968/) > [Create Thumbnail](https://img.ly/docs/cesdk/ios/export-save-publish/create-thumbnail-749be1/)

---

Thumbnails are scaled down previews of your designs. They let you show galleries or document picker previews without loading the full editor. CE.SDK generates thumbnails using the same API you use for final output, just with smaller target dimensions and often lower quality settings.

This guide focuses on **image thumbnails**: small PNG, JPEG or WebP previews for use in grids, lists and document icons. It **doesn’t cover audio waveforms** or arrays of **preview frames** for scrubbers.

## What You’ll Learn

- How to export a scene or page as a small preview image.
- How to control thumbnail dimensions while preserving aspect ratio.
- When to choose PNG, JPEG, or WebP for thumbnails.
- How to tune quality and file size using `ExportOptions`.
- How to batch-generate different thumbnail sizes safely.

## When You’ll Use It

- Showing a “My Designs” or “Recent Files” gallery.
- Rendering previews for templates or drafts.
- Generating document icons or share sheet previews.
- Creating thumbnail sizes for different UI contexts.

## How Thumbnail Export Works

In CE.SDK, `.export` means *rendering bitmap image data from the engine*. When you call `export`, the SDK:

1. Renders the current visual state of a block (for example, a page).
2. Composites all **visible** child blocks (images, text, shapes, effects).
3. Produces raw bitmap image data in the requested format (PNG, JPEG, or WebP).

Exporting **doesn’t** imply writing a file to disk. The result of the export call is an in-memory `Blob` (`Data`) that you can:

- Convert to a `UIImage`, `NSImage`, or SwiftUI `Image`.
- Cache in memory.
- Write to disk if needed.
- Upload elsewhere.

CE.SDK doesn’t provide a separate "thumbnail API". If you build your own UI, you call `engine.block.export(...)` directly whenever you want.

If you use the **prebuilt editor UI** (the default CE.SDK editors), there *is* a convenient hook for the built-in Export/Share button: the editor exposes an `OnExport` callback. The default export:

1. Renders (PDF for design scenes, MP4 for video scenes).
2. Writes the result to a temporary file
3. Opens the system share sheet.

That hook is great for customizing what happens when the user taps Export in the prebuilt UI, but under the hood it still uses the same engine export APIs that you use for thumbnails.

## Export a Scene Thumbnail

You generate thumbnails by exporting a design block. In most cases this should be either:

- The **page block**, which represents the full visible canvas.
- The scene, if your design is single-page.

Exporting the page block is the safest choice when you want a thumbnail that matches what the user sees on screen.

## Control Thumbnail Size and Aspect Ratio

### How `targetWidth` and `targetHeight` behave

When both `targetWidth` and `targetHeight` have values, CE.SDK renders the block large enough to **fill the target box while maintaining its aspect ratio**.

Important implications:

- You don’t need to calculate aspect-fit or aspect-fill yourself.
- The exported image may exceed one of the target dimensions internally to preserve aspect ratio.
- Consider `targetWidth` and `targetHeight` as a *desired bounding box*, not a hard crop.

### Typical Thumbnail Sizes

Common choices include:

- 150 × 150 for dense grids
- 161 × 161 for Instagram Video Feeds
- 55 × 55 or 222 × 150 for Pinterest
- 400 × 300 for list previews
- 800 × 600 for high-quality previews

## Choose the Right Thumbnail Format

CE.SDK supports PNG, JPEG, and WebP for image export. It provides a `MIMEType` enum including `.jpeg`, `.png` and `.webp`.

### PNG

- Preserves transparency
- Lossless quality
- Compression affects speed, not quality
- Best for stickers, cutouts, or UI elements

### JPEG

- Smaller and faster for photographic content
- No transparency
- Control quality via `jpegQuality`

### WebP

- Efficient compression
- Supports lossless and lossy modes
- Requires WebP support everywhere you display thumbnails

Switching formats only requires changing the `mimeType` and relevant quality option.

```swift
let jpegBlob = try await engine.block.export(
  handle: page,
  mimeType: .jpeg,
  options: ExportOptions(
    jpegQuality: 0.8,
    targetWidth: 400,
    targetHeight: 300
  )
)
```

When you need **different thumbnails of different sizes or image formats**, call `export` for each permutation. Pass in the correct mime type and an `ExportOptions` configuration.

```swift
let smallBlob = try await engine.block.export(
  handle: page,
  mimeType: .jpeg,
  options: ExportOptions(jpegQuality: 0.8,
                         targetWidth: 22,
                         targetHeight: 22
  )
)

let mediumBlob = try await engine.block.export(
  handle: page,
  mimeType: .jpeg,
  options: ExportOptions(jpegQuality: 0.8,
                         targetWidth: 150,
                         targetHeight: 150
  )
)
```

> **Note:** ## Caching ThumbnailsThumbnail export is expensive compared to image display.Even a basic in-memory cache (for example, `NSCache`) can dramatically improve scrolling performance in galleries and `List` views.

## Tune Quality and File Size with `ExportOptions`

`ExportOptions` lets you balance visual quality, file size, and export speed.

Key fields for thumbnails:

- `pngCompressionLevel` (0–9, default 5)
- `jpegQuality` (0–1, default 0.9)
- `webpQuality` (0–1, default 1.0)
- `targetWidth` / `targetHeight`

CE.SDK applies only the options relevant to the chosen MIME type. Others are ignored.

## Headless and Background Thumbnail Generation

CE.SDK offers two common ways to export without blocking your UI:

### Use Your Existing Engine

For occasional thumbnail creation (for example, when a user saves a draft), it’s often fine to export from the same `Engine` instance that powers the editor.

### Use a Separate Headless Engine Instance

For batch thumbnail generation (for example, populating a large gallery), you can create a separate `Engine` instance, load the same scene data into it, and export thumbnails there.

> **Note:** When you’re using the **prebuilt editor UI** in iOS, you can also customize what happens when the user taps the Export button via the editor’s `OnExport` callback. The default callback writes the exported data to a temporary file and triggers the share sheet. You could generate thumbnails here and control the export instead.

## Thumbnails from Video Blocks (Single Frame)

Although this guide focuses on static image thumbnails, it’s worth calling out an important edge case that often surprises developers:

If you export a **paused video fill block**, the result is a **single image thumbnail**, just like exporting a graphic or page.

This is *not* the same as generating a stream of video thumbnails or scrubbing previews.

### How This Works

- Video blocks render their current frame when exported.
- You can control *which* frame becomes the thumbnail by setting the playhead time before calling `export`.

Conceptually:

1. Seek the video to the desired time.
2. Pause playback.
3. Export the block using the thumbnail export flow shown earlier.

This produces a single static image suitable for:

- Gallery previews
- Document icons
- Poster-frame–style thumbnails

## Troubleshooting

| Symptom | Likely Cause | Solution |
|---|---|---|
| Thumbnail only shows part of the design | Exported a child block instead of the page | Export the page block to capture the full visible canvas |
| Thumbnail size looks wrong | Missing or zero target dimension | Set both `targetWidth` and `targetHeight` |
| Export is slow | Large target size or high PNG compression | Reduce dimensions or compression level |
| File size too large | Quality settings too high | Lower JPEG/WebP quality or size |
| Thumbnail looks blurry | Target size too small | Increase target dimensions |
| Export fails | Scene not loaded | Ensure `engine.scene.get()` returns a valid scene |

## Next Steps

- To learn more about exporting images and controlling output quality, see [Export designs to image formats](https://img.ly/docs/cesdk/ios/export-save-publish/export/overview-9ed3a8/).
- Reduce file size or tune quality for thumbnails and previews, with [Compress exported images](https://img.ly/docs/cesdk/ios/export-save-publish/export/compress-29105e/).
- If you need to generate thumbnails at scale or as part of automated workflows, take a look at [Batch processing designs](https://img.ly/docs/cesdk/ios/automation/batch-processing-ab2d18/).



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
