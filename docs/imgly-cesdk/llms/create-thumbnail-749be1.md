# Source: https://img.ly/docs/cesdk/android/export-save-publish/create-thumbnail-749be1/

---
title: "Create Thumbnail in Android (Kotlin)"
description: "Generate small preview images for scenes and pages using CE.SDK export options in Kotlin."
platform: android
url: "https://img.ly/docs/cesdk/android/export-save-publish/create-thumbnail-749be1/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Export Media Assets](https://img.ly/docs/cesdk/android/export-save-publish/export-82f968/) > [Create Thumbnail](https://img.ly/docs/cesdk/android/export-save-publish/create-thumbnail-749be1/)

---

Thumbnails are scaled down previews of your designs. They let you show galleries or document picker previews without loading the full editor. CE.SDK generates thumbnails using the same API you use for final output, just with smaller target dimensions and often lower quality settings.

This guide focuses on **image thumbnails**: small PNG, JPEG or WebP previews for use in grids, lists and document icons. It **doesn't cover audio waveforms** or arrays of **preview frames** for scrubbers.

## What You'll Learn

- How to export a scene or page as a small preview image.
- How to control thumbnail dimensions while preserving aspect ratio.
- When to choose PNG, JPEG, or WebP for thumbnails.
- How to tune quality and file size using `ExportOptions`.
- How to batch-generate different thumbnail sizes safely.

## When You'll Use It

- Showing a "My Designs" or "Recent Files" gallery.
- Rendering previews for templates or drafts.
- Generating document icons or share sheet previews.
- Creating thumbnail sizes for different UI contexts.

## How Thumbnail Export Works

In CE.SDK, `export` means *rendering bitmap image data from the engine*. When you call `export`, the SDK:

1. Renders the current visual state of a block (for example, a page).
2. Composites all **visible** child blocks (images, text, shapes, effects).
3. Produces raw bitmap image data in the requested format (PNG, JPEG, or WebP).

Exporting **doesn't** imply writing a file to disk. The result of the export call is an in-memory `ByteBuffer` that you can:

- Convert to a `Bitmap`.
- Cache in memory.
- Write to disk if needed.
- Upload elsewhere.

CE.SDK doesn't provide a separate "thumbnail API". If you build your own UI, you call `engine.block.export(...)` directly whenever you want.

If you use the **prebuilt editor UI** (the default CE.SDK editors), there *is* a convenient hook for the built-in Export/Share button: the editor exposes an `DesignEditor` configuration. The default export:

1. Renders (PDF for design scenes, MP4 for video scenes).
2. Writes the result to a temporary file
3. Opens the system share sheet.

That hook is great for customizing what happens when the user taps Export in the prebuilt UI, but under the hood it still uses the same engine export APIs that you use for thumbnails.

## Export a Scene Thumbnail

You generate thumbnails by exporting a design block. In most cases this should be either:

- The **page block**, which represents the full visible canvas.
- The scene, if your design is single-page.

Exporting the page block is the safest choice when you want a thumbnail that matches what the user sees on screen.

```kotlin
import android.content.Context
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.ExportOptions
import ly.img.engine.MimeType
import java.io.File

suspend fun exportSceneThumbnail(
    engine: Engine,
    context: Context,
    scene: Int
): File {
    // Define thumbnail size
    val options = ExportOptions(
        targetWidth = 400,
        targetHeight = 300,
        jpegQuality = 0.8f
    )
    
    // Export the scene as JPEG
    val blob = engine.block.export(
        block = scene,
        mimeType = MimeType.JPEG,
        options = options
    )
    
    // Save to temporary file
    val thumbnailFile = File(context.cacheDir, "thumbnail_${System.currentTimeMillis()}.jpg")
    withContext(Dispatchers.IO) {
        thumbnailFile.outputStream().channel.use { channel ->
            channel.write(blob)
        }
    }
    
    return thumbnailFile
}
```

The preceding code exports a scene at 400×300 resolution with JPEG quality set to 0.8 for efficient file size.

## Control Thumbnail Size and Aspect Ratio

### How `targetWidth` and `targetHeight` behave

When both `targetWidth` and `targetHeight` have values, CE.SDK renders the block large enough to **fill the target box while maintaining its aspect ratio**.

Important implications:

- You don't need to calculate aspect-fit or aspect-fill yourself.
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

CE.SDK supports PNG, JPEG, and WebP for image export. It provides a `MimeType` enum including `JPEG`, `PNG` and `WEBP`.

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

```kotlin
import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.ExportOptions
import ly.img.engine.MimeType
import java.io.File

suspend fun exportJPEGThumbnail(
    engine: Engine,
    context: Context,
    page: Int
): File {
    val options = ExportOptions(
        jpegQuality = 0.8f,
        targetWidth = 400,
        targetHeight = 300
    )
    
    val blob = engine.block.export(
        block = page,
        mimeType = MimeType.JPEG,
        options = options
    )
    
    val file = File(context.cacheDir, "thumbnail.jpg")
    withContext(Dispatchers.IO) {
        file.outputStream().channel.use { channel ->
            channel.write(blob)
        }
    }
    
    return file
}
```

When you need **different thumbnails of different sizes or image formats**, call `export` for each permutation. Pass in the correct mime type and an `ExportOptions` configuration.

```kotlin
import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.ExportOptions
import ly.img.engine.MimeType
import java.io.File

suspend fun exportMultipleThumbnails(
    engine: Engine,
    context: Context,
    page: Int
): Map<String, File> {
    val results = mutableMapOf<String, File>()
    
    // Small thumbnail (22x22)
    val smallOptions = ExportOptions(
        jpegQuality = 0.8f,
        targetWidth = 22,
        targetHeight = 22
    )
    val smallBlob = engine.block.export(page, MimeType.JPEG, smallOptions)
    val smallFile = File(context.cacheDir, "thumbnail_small.jpg")
    withContext(Dispatchers.IO) {
        smallFile.outputStream().channel.use { it.write(smallBlob) }
    }
    results["small"] = smallFile
    
    // Medium thumbnail (150x150)
    val mediumOptions = ExportOptions(
        jpegQuality = 0.8f,
        targetWidth = 150,
        targetHeight = 150
    )
    val mediumBlob = engine.block.export(page, MimeType.JPEG, mediumOptions)
    val mediumFile = File(context.cacheDir, "thumbnail_medium.jpg")
    withContext(Dispatchers.IO) {
        mediumFile.outputStream().channel.use { it.write(mediumBlob) }
    }
    results["medium"] = mediumFile
    
    return results
}
```

> **Note:** ## Caching ThumbnailsThumbnail export is expensive compared to image display.Even a basic in-memory cache (for example, `LruCache`) can dramatically improve scrolling performance in galleries and `RecyclerView` lists.

## Tune Quality and File Size with `ExportOptions`

`ExportOptions` lets you balance visual quality, file size, and export speed.

Key fields for thumbnails:

- `pngCompressionLevel` (0–9, default 5)
- `jpegQuality` (0.0–1.0, default 0.9)
- `webpQuality` (0.0–1.0, default 1.0)
- `targetWidth` / `targetHeight`

CE.SDK applies only the options relevant to the chosen MIME type. Others are ignored.

```kotlin
import ly.img.engine.ExportOptions
import ly.img.engine.MimeType

// PNG with maximum compression (slower, smaller file)
val pngOptions = ExportOptions(
    pngCompressionLevel = 9,
    targetWidth = 400,
    targetHeight = 300
)
val pngBlob = engine.block.export(page, MimeType.PNG, pngOptions)

// JPEG with lower quality (faster, much smaller file)
val jpegOptions = ExportOptions(
    jpegQuality = 0.6f,
    targetWidth = 400,
    targetHeight = 300
)
val jpegBlob = engine.block.export(page, MimeType.JPEG, jpegOptions)

// WebP with lossless mode
val webpOptions = ExportOptions(
    webpQuality = 1.0f,
    targetWidth = 400,
    targetHeight = 300
)
val webpBlob = engine.block.export(page, MimeType.WEBP, webpOptions)
```

## Headless and Background Thumbnail Generation

CE.SDK offers two common ways to export without blocking your UI:

### Use Your Existing Engine

For occasional thumbnail creation (for example, when a user saves a draft), it's often fine to export from the same `Engine` instance that powers the editor.

### Use a Separate Headless Engine Instance

For batch thumbnail generation (for example, populating a large gallery), you can create a separate `Engine` instance, load the same scene data into it, and export thumbnails there.

```kotlin
import android.content.Context
import android.net.Uri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import ly.img.engine.Engine
import ly.img.engine.ExportOptions
import ly.img.engine.MimeType
import java.io.File

suspend fun generateThumbnailsHeadless(
    context: Context,
    license: String,
    userId: String,
    sceneUris: List<Uri>
): List<File> {
    val thumbnails = mutableListOf<File>()
    
    // Create a headless engine instance
    val engine = Engine.getInstance(id = "ly.img.engine.thumbnail")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)
    
    try {
        for (sceneUri in sceneUris) {
            // Load scene
            val scene = engine.scene.load(sceneUri = sceneUri)
            
            // Export thumbnail
            val options = ExportOptions(
                jpegQuality = 0.8f,
                targetWidth = 400,
                targetHeight = 300
            )
            val blob = engine.block.export(scene, MimeType.JPEG, options)
            
            // Save to file
            val file = File(context.cacheDir, "thumb_${System.currentTimeMillis()}.jpg")
            withContext(Dispatchers.IO) {
                file.outputStream().channel.use { it.write(blob) }
            }
            thumbnails.add(file)
        }
    } finally {
        engine.stop()
    }
    
    return thumbnails
}
```

> **Note:** When you're using the **prebuilt editor UI** in Android, you can also customize what happens when the user taps the Export button via the editor's export configuration. The default callback writes the exported data to a temporary file and triggers the share sheet. You could generate thumbnails here and control the export instead.

## Thumbnails from Video Blocks (Single Frame)

Although this guide focuses on static image thumbnails, it's worth calling out an important edge case that often surprises developers:

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

- To learn more about exporting images and controlling output quality, see [Export designs to image formats](https://img.ly/docs/cesdk/android/export-save-publish/export/overview-9ed3a8/).
- Reduce file size or tune quality for thumbnails and previews, with [Compress exported images](https://img.ly/docs/cesdk/android/export-save-publish/export/compress-29105e/).
- If you need to generate thumbnails at scale or as part of automated workflows, take a look at [Batch processing designs](https://img.ly/docs/cesdk/android/automation/batch-processing-ab2d18/).



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
