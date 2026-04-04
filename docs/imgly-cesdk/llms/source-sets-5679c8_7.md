# Source: https://img.ly/docs/cesdk/macos/import-media/source-sets-5679c8/

---
title: "Source Sets"
description: "Use multiple versions of an asset to support different resolutions or formats."
platform: macos
url: "https://img.ly/docs/cesdk/macos/import-media/source-sets-5679c8/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/macos/import-media-4e3703/) > [Source Sets](https://img.ly/docs/cesdk/macos/import-media/source-sets-5679c8/)

---

```swift file=@cesdk_swift_examples/engine-guides-source-sets/SourceSets.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func sourceSets(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)
  try await engine.scene.zoom(to: page, paddingLeft: 50, paddingTop: 50, paddingRight: 50, paddingBottom: 50)

  let block = try engine.block.create(DesignBlockType.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setSourceSet(imageFill, property: "fill/image/sourceSet", sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
      width: 512,
      height: 341,
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
      width: 1024,
      height: 683,
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
      width: 2048,
      height: 1366,
    ),
  ])
  try engine.block.setFill(block, fill: imageFill)
  try engine.block.appendChild(to: page, child: block)

  let assetWithSourceSet = AssetDefinition(
    id: "my-image",
    meta: [
      "kind": "image",
      "fillType": "//ly.img.ubq/fill/image",
    ],
    payload: .init(sourceSet: [
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
        width: 512,
        height: 341,
      ),
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
        width: 1024,
        height: 683,
      ),
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
        width: 2048,
        height: 1366,
      ),
    ]),
  )

  try engine.asset.addLocalSource(sourceID: "my-dynamic-images")
  try engine.asset.addAsset(to: "my-dynamic-images", asset: assetWithSourceSet)

  // Could also acquire the asset using `findAssets` on the source
  let assetResult = AssetResult(
    id: assetWithSourceSet.id,
    meta: assetWithSourceSet.meta,
    context: AssetContext(sourceID: "my-dynamic-images"),
  )
  let result = try await engine.asset.defaultApplyAsset(assetResult: assetResult)
  // Lists the entries from above again.
  _ = try engine.block.getSourceSet(
    try engine.block.getFill(result!),
    property: "fill/image/sourceSet",
  )

  let videoFill = try engine.block.createFill(.video)
  try engine.block.setSourceSet(videoFill, property: "fill/video/sourceSet", sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/example-assets/sourceset/1x.mp4")!,
      width: 1920,
      height: 1080,
    ),
  ])

  try await engine.block.addVideoFileURIToSourceSet(
    videoFill,
    property: "fill/video/sourceSet",
    uri: URL(string: "https://img.ly/static/example-assets/sourceset/2x.mp4")!,
  )
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

```swift highlight-setup
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)
  try await engine.scene.zoom(to: page, paddingLeft: 50, paddingTop: 50, paddingRight: 50, paddingBottom: 50)
```

## Using a Source Set for an existing Block

To make use of a source set for an existing image fill, we use the `setSourceSet` API. This defines a set of sources and specifies height and width for each of these sources. The engine then chooses the appropriate source during drawing. You may query an existing source set using `getSourceSet`. You can add sources to an existing source set with `addImageFileURIToSourceSet`.

```swift highlight-set-source-set
let block = try engine.block.create(DesignBlockType.graphic)
try engine.block.setShape(block, shape: engine.block.createShape(.rect))
let imageFill = try engine.block.createFill(.image)
try engine.block.setSourceSet(imageFill, property: "fill/image/sourceSet", sourceSet: [
  .init(
    uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
    width: 512,
    height: 341,
  ),
  .init(
    uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
    width: 1024,
    height: 683,
  ),
  .init(
    uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
    width: 2048,
    height: 1366,
  ),
])
try engine.block.setFill(block, fill: imageFill)
try engine.block.appendChild(to: page, child: block)
```

## Using a Source Set in an Asset

For assets, source sets can be defined in the `payload.sourceSet` field. This is directly translated to the `sourceSet` property when applying the asset. The resulting block is configured in the same way as the one described above. The code demonstrates how to add an asset that defines a source set to a local source and how `applyAsset` handles a populated `payload.sourceSet`.

```swift highlight-asset-definition
let assetWithSourceSet = AssetDefinition(
  id: "my-image",
  meta: [
    "kind": "image",
    "fillType": "//ly.img.ubq/fill/image",
  ],
  payload: .init(sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
      width: 512,
      height: 341,
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
      width: 1024,
      height: 683,
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
      width: 2048,
      height: 1366,
    ),
  ]),
)
```

## Video Source Sets

Source sets can also be used for video fills. This is done by setting the `sourceSet` property of the video fill. The engine will then use the source with the closest size exceeding the drawing size.

Thumbnails will use the smallest source if `features/matchThumbnailSourceToFill` is disabled, which is the default.

For low end devices or scenes with large videos, you can force the preview to always use the smallest source when editing by enabling `features/forceLowQualityVideoPreview`. On export, the highest quality source is used in any case.

```swift highlight-video-source-sets
  let videoFill = try engine.block.createFill(.video)
  try engine.block.setSourceSet(videoFill, property: "fill/video/sourceSet", sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/example-assets/sourceset/1x.mp4")!,
      width: 1920,
      height: 1080,
    ),
  ])

  try await engine.block.addVideoFileURIToSourceSet(
    videoFill,
    property: "fill/video/sourceSet",
    uri: URL(string: "https://img.ly/static/example-assets/sourceset/2x.mp4")!,
  )
```

## Full Code

Here's the full code:

```swift
import Foundation
import IMGLYEngine

@MainActor
func sourceSets(engine: Engine) async throws {
  let scene = try engine.scene.create()

  let page = try engine.block.create(.page)
  try engine.block.setWidth(page, value: 800)
  try engine.block.setHeight(page, value: 600)
  try engine.block.appendChild(to: scene, child: page)
  try await engine.scene.zoom(to: page, paddingLeft: 50, paddingTop: 50, paddingRight: 50, paddingBottom: 50)

  let block = try engine.block.create(DesignBlockType.graphic)
  try engine.block.setShape(block, shape: engine.block.createShape(.rect))
  let imageFill = try engine.block.createFill(.image)
  try engine.block.setSourceSet(imageFill, property: "fill/image/sourceSet", sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
      width: 512,
      height: 341
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
      width: 1024,
      height: 683
    ),
    .init(
      uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
      width: 2048,
      height: 1366
    ),
  ])
  try engine.block.setFill(block, fill: imageFill)
  try engine.block.appendChild(to: page, child: block)

  let assetWithSourceSet = AssetDefinition(
    id: "my-image",
    meta: [
      "kind": "image",
      "fillType": "//ly.img.ubq/fill/image",
    ],
    payload: .init(sourceSet: [
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_512x341.jpg")!,
        width: 512,
        height: 341
      ),
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_1024x683.jpg")!,
        width: 1024,
        height: 683
      ),
      .init(
        uri: URL(string: "https://img.ly/static/ubq_samples/sample_1_2048x1366.jpg")!,
        width: 2048,
        height: 1366
      ),
    ])
  )

  try engine.asset.addLocalSource(sourceID: "my-dynamic-images")
  try engine.asset.addAsset(to: "my-dynamic-images", asset: assetWithSourceSet)

  // Could also acquire the asset using `findAssets` on the source
  let assetResult = AssetResult(
    id: assetWithSourceSet.id,
    meta: assetWithSourceSet.meta,
    context: AssetContext(sourceID: "my-dynamic-images")
  )
  let result = try await engine.asset.defaultApplyAsset(assetResult: assetResult)
  // Lists the entries from above again.
  _ = try engine.block.getSourceSet(
    try engine.block.getFill(result!),
    property: "fill/image/sourceSet"
  )

  let videoFill = try engine.block.createFill(.video)
  try engine.block.setSourceSet(videoFill, property: "fill/video/sourceSet", sourceSet: [
    .init(
      uri: URL(string: "https://img.ly/static/example-assets/sourceset/1x.mp4")!,
      width: 1920,
      height: 1080
    ),
  ])

  try await engine.block.addVideoFileURIToSourceSet(
    videoFill,
    property: "fill/video/sourceSet",
    uri: URL(string: "https://img.ly/static/example-assets/sourceset/2x.mp4")!
  )
}
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
