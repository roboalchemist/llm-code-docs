# Source: https://img.ly/docs/cesdk/android/import-media/source-sets-5679c8/

---
title: "Source Sets"
description: "Use multiple versions of an asset to support different resolutions or formats."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/source-sets-5679c8/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Source Sets](https://img.ly/docs/cesdk/android/import-media/source-sets-5679c8/)

---

```kotlin file=@cesdk_android_examples/engine-guides-source-sets/SourceSets.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Asset
import ly.img.engine.AssetContext
import ly.img.engine.AssetDefinition
import ly.img.engine.AssetPayload
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.Source

fun sourceSets(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)
    engine.scene.zoomToBlock(
        block = page,
        paddingLeft = 50F,
        paddingTop = 50F,
        paddingRight = 50F,
        paddingBottom = 50F,
    )

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, engine.block.createShape(ShapeType.Rect))
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setSourceSet(
        block = imageFill,
        property = "fill/image/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
                width = 512,
                height = 341,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
                width = 1024,
                height = 683,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
                width = 2048,
                height = 1366,
            ),
        ),
    )
    engine.block.setFill(block = block, fill = imageFill)
    engine.block.appendChild(parent = page, child = block)

    val assetWithSourceSet = AssetDefinition(
        id = "my-image",
        meta = mapOf(
            "kind" to "image",
            "fillType" to "//ly.img.ubq/fill/image",
        ),
        payload = AssetPayload(
            sourceSet = listOf(
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
                    width = 512,
                    height = 341,
                ),
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
                    width = 1024,
                    height = 683,
                ),
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
                    width = 2048,
                    height = 1366,
                ),
            ),
        ),
    )

    engine.asset.addLocalSource(
        sourceId = "my-dynamic-images",
        supportedMimeTypes = listOf("image/jpeg"),
    )
    engine.asset.addAsset(sourceId = "my-dynamic-images", asset = assetWithSourceSet)

    // Could also acquire the asset using `findAssets` on the source
    val asset = Asset(
        id = assetWithSourceSet.id,
        meta = assetWithSourceSet.meta?.toMap(),
        context = AssetContext(sourceId = "my-dynamic-images"),
    )
    val result = engine.asset.defaultApplyAsset(asset)

    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/example-assets/sourceset/1x.mp4"),
                width = 720,
                height = 1280,
            ),
        ),
    )

    engine.block.addVideoFileUriToSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        uri = "https://img.ly/static/example-assets/sourceset/2x.mp4",
    )

    engine.stop()
}
```

Source sets allow specifying an entire set of sources, each with a different size, that should be used for drawing a block. The appropriate source is then dynamically chosen based on the current drawing size. This allows using the same scene to render a preview on a mobile screen using a small image file and a high-resolution file for print in the backend.

This guide will show you how to specify source sets both for existing blocks and when defining assets.

### Drawing

When an image needs to be drawn, the current drawing size in screen pixels is calculated and the engine looks up the most appropriate source file to draw at that resolution.

1. If a source set is set, the source with the closest size exceeding the drawing size is used
2. If no source set is set, the full resolution image is downscaled to a maximum edge length of 4096 (configurable via `maxImageSize` setting) and drawn to the target area

This also gives more control about up- and downsampling to you, as all intermediate resolutions can be generated using tooling of your choice.

**Source sets are also used during export of your designs and will resolve to the best matching asset for the export resolution.**

## Setup the scene

We first create a new scene with a new page.

```kotlin highlight-setup
    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)
    engine.scene.zoomToBlock(
        block = page,
        paddingLeft = 50F,
        paddingTop = 50F,
        paddingRight = 50F,
        paddingBottom = 50F,
    )
```

## Using a Source Set for an existing Block

To make use of a source set for an existing image fill, we use the `setSourceSet` API. This defines a set of sources and specifies height and width for each of these sources. The engine then chooses the appropriate source during drawing. You may query an existing source set using `getSourceSet`. You can add sources to an existing source set with `addImageFileURIToSourceSet`.

```kotlin highlight-set-source-set
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.setShape(block, engine.block.createShape(ShapeType.Rect))
val imageFill = engine.block.createFill(FillType.Image)
engine.block.setSourceSet(
    block = imageFill,
    property = "fill/image/sourceSet",
    sourceSet = listOf(
        Source(
            uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
            width = 512,
            height = 341,
        ),
        Source(
            uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
            width = 1024,
            height = 683,
        ),
        Source(
            uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
            width = 2048,
            height = 1366,
        ),
    ),
)
engine.block.setFill(block = block, fill = imageFill)
engine.block.appendChild(parent = page, child = block)
```

## Using a Source Set in an Asset

For assets, source sets can be defined in the `payload.sourceSet` field. This is directly translated to the `sourceSet` property when applying the asset. The resulting block is configured in the same way as the one described above. The code demonstrates how to add an asset that defines a source set to a local source and how `applyAsset` handles a populated `payload.sourceSet`.

```kotlin highlight-asset-definition
val assetWithSourceSet = AssetDefinition(
    id = "my-image",
    meta = mapOf(
        "kind" to "image",
        "fillType" to "//ly.img.ubq/fill/image",
    ),
    payload = AssetPayload(
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
                width = 512,
                height = 341,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
                width = 1024,
                height = 683,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
                width = 2048,
                height = 1366,
            ),
        ),
    ),
)
```

## Video Source Sets

Source sets can also be used for video fills. This is done by setting the `sourceSet` property of the video fill. The engine will then use the source with the closest size exceeding the drawing size.

Thumbnails will use the smallest source if `features/matchThumbnailSourceToFill` is disabled, which is the default.

For low end devices or scenes with large videos, you can force the preview to always use the smallest source when editing by enabling `features/forceLowQualityVideoPreview`. On export, the highest quality source is used in any case.

```kotlin highlight-video-source-sets
    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/example-assets/sourceset/1x.mp4"),
                width = 720,
                height = 1280,
            ),
        ),
    )

    engine.block.addVideoFileUriToSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        uri = "https://img.ly/static/example-assets/sourceset/2x.mp4",
    )
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import ly.img.engine.Asset
import ly.img.engine.AssetContext
import ly.img.engine.AssetDefinition
import ly.img.engine.AssetPayload
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.ShapeType
import ly.img.engine.Source

fun sourceSets(
    license: String,
    userId: String,
) = CoroutineScope(Dispatchers.Main).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val scene = engine.scene.create()

    val page = engine.block.create(DesignBlockType.Page)
    engine.block.setWidth(page, value = 800F)
    engine.block.setHeight(page, value = 600F)
    engine.block.appendChild(parent = scene, child = page)
    engine.scene.zoomToBlock(
        block = page,
        paddingLeft = 50F,
        paddingTop = 50F,
        paddingRight = 50F,
        paddingBottom = 50F,
    )

    val block = engine.block.create(DesignBlockType.Graphic)
    engine.block.setShape(block, engine.block.createShape(ShapeType.Rect))
    val imageFill = engine.block.createFill(FillType.Image)
    engine.block.setSourceSet(
        block = imageFill,
        property = "fill/image/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
                width = 512,
                height = 341,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
                width = 1024,
                height = 683,
            ),
            Source(
                uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
                width = 2048,
                height = 1366,
            ),
        ),
    )
    engine.block.setFill(block = block, fill = imageFill)
    engine.block.appendChild(parent = page, child = block)

    val assetWithSourceSet = AssetDefinition(
        id = "my-image",
        meta = mapOf(
            "kind" to "image",
            "fillType" to "//ly.img.ubq/fill/image",
        ),
        payload = AssetPayload(
            sourceSet = listOf(
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_512x341.jpg"),
                    width = 512,
                    height = 341,
                ),
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_1024x683.jpg"),
                    width = 1024,
                    height = 683,
                ),
                Source(
                    uri = Uri.parse("https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg"),
                    width = 2048,
                    height = 1366,
                ),
            ),
        ),
    )

    engine.asset.addLocalSource(
        sourceId = "my-dynamic-images",
        supportedMimeTypes = listOf("image/jpeg"),
    )
    engine.asset.addAsset(sourceId = "my-dynamic-images", asset = assetWithSourceSet)

    // Could also acquire the asset using `findAssets` on the source
    val asset = Asset(
        id = assetWithSourceSet.id,
        meta = assetWithSourceSet.meta?.toMap(),
        context = AssetContext(sourceId = "my-dynamic-images"),
    )
    val result = engine.asset.defaultApplyAsset(asset)

    val videoFill = engine.block.createFill(FillType.Video)
    engine.block.setSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        sourceSet = listOf(
            Source(
                uri = Uri.parse("https://img.ly/static/example-assets/sourceset/1x.mp4"),
                width = 720,
                height = 1280,
            ),
        ),
    )

    engine.block.addVideoFileUriToSourceSet(
        block = videoFill,
        property = "fill/video/sourceSet",
        uri = "https://img.ly/static/example-assets/sourceset/2x.mp4",
    )

    engine.stop()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
