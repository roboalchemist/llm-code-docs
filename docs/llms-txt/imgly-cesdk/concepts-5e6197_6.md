# Source: https://img.ly/docs/cesdk/mac-catalyst/import-media/concepts-5e6197/

---
title: "Concepts"
description: "Understand key asset concepts like sources, formats, metadata, and how assets are integrated into designs."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/import-media/concepts-5e6197/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/mac-catalyst/import-media-4e3703/) > [Concepts](https://img.ly/docs/cesdk/mac-catalyst/import-media/concepts-5e6197/)

---

```swift reference-only
let scene = try engine.scene.create()
let page = try engine.block.create(.page)
let block = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: page)
try engine.block.appendChild(to: page, child: block)

let customSource = CustomAssetSource(engine: engine)

let addedTask = Task {
  for await sourceID in engine.asset.onAssetSourceAdded {
    print("Added source: \(sourceID)")
  }
}
let removedTask = Task {
  for await sourceID in engine.asset.onAssetSourceRemoved {
    print("Removed source: \(sourceID)")
  }
}
let updatedTask = Task {
  for await sourceID in engine.asset.onAssetSourceUpdated {
    print("Updated source: \(sourceID)")
  }
}

try engine.asset.addSource(customSource)

let localSourceID = "local-source"
try engine.asset.addLocalSource(sourceID: localSourceID)

let assetDefinition = AssetDefinition(
  id: "ocean-waves-1",
  meta: [
    "uri": "https://example.com/ocean-waves-1.mp4",
    "thumbUri": "https://example.com/thumbnails/ocean-waves-1.jpg",
    "mimeType": MIMEType.mp4.rawValue,
    "width": "1920",
    "height": "1080",
  ],
  label: [
    "en": "relaxing ocean waves",
  ],
  tags: [
    "en": ["ocean", "waves", "soothing", "slow"],
  ]
)
try engine.asset.addAsset(to: localSourceID, asset: assetDefinition)
try engine.asset.removeAsset(from: localSourceID, assetID: assetDefinition.id)

engine.asset.findAllSources()

let mimeTypes = try engine.asset.getSupportedMIMETypes(sourceID: customSource.id)

let credits = engine.asset.getCredits(sourceID: customSource.id)
let license = engine.asset.getLicense(sourceID: customSource.id)
let groups = try await engine.asset.getGroups(sourceID: customSource.id)

let result = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: "", page: 0, perPage: 10)
)
let asset = result.assets[0]
let sortByNewest = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .descending)
)
let sortById = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .ascending, sortKey: "id")
)
let sortByMetaKeyValue = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .ascending, sortKey: "someMetaKey")
)
let search = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: "banana", page: 0, perPage: 100)
)

let sceneColorsResult = try await engine.asset.findAssets(
  sourceID: "ly.img.scene.colors",
  query: .init(query: nil, page: 0, perPage: 99999)
)
let colorAsset = sceneColorsResult.assets[0]

try await engine.asset.apply(sourceID: customSource.id, assetResult: asset)

try await engine.asset.applyToBlock(sourceID: customSource.id, assetResult: asset, block: block)

try engine.asset.assetSourceContentsChanged(sourceID: customSource.id)

try engine.asset.removeSource(sourceID: customSource.id)
try engine.asset.removeSource(sourceID: localSourceID)

final class CustomAssetSource: NSObject, AssetSource {
  private weak var engine: Engine?

  init(engine: Engine) {
    self.engine = engine
  }

  var id: String { "foobar" }

  func findAssets(queryData: AssetQueryData) async throws -> AssetQueryResult {
    .init(assets: [
      .init(id: "logo",
            meta: [
              "uri": "https://img.ly/static/ubq_samples/imgly_logo.jpg",
              "thumbUri": "https://img.ly/static/ubq_samples/thumbnails/imgly_logo.jpg",
              "blockType": DesignBlockType.graphic.rawValue,
              "fillType": FillType.image.rawValue,
              "width": "320",
              "height": "116",
            ],
            context: .init(sourceID: "foobar")),
    ],
    currentPage: queryData.page,
    total: 1)
  }

  func apply(asset: AssetResult) async throws -> NSNumber? {
    if let id = try await engine?.asset.defaultApplyAsset(assetResult: asset) {
      .init(value: id)
    } else {
      nil
    }
  }

  func applyToBlock(asset: AssetResult, block: DesignBlockID) async throws {
    try await engine?.asset.defaultApplyAssetToBlock(assetResult: asset, block: block)
  }

  var supportedMIMETypes: [String]? { [MIMEType.jpeg.rawValue] }
  var credits: IMGLYEngine.AssetCredits? { nil }
  var license: IMGLYEngine.AssetLicense? { nil }
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to manage assets through the `asset` API.

To begin working with assets first you need at least one asset source. As the name might imply asset sources provide the engine with assets. These assets then show up in the editor's asset library. But they can also be independently searched and used to create design blocks. Asset sources can be added dynamically using the `asset` API as we will show in this guide.

## Defining a Custom Asset Source

Asset sources need at least an `id` and a `findAssets` function. You may notice asset source functions are all `async`. This way you can use web requests or other long-running operations inside them and return results asynchronously.

```swift highlight-defineCustomSource
let customSource = CustomAssetSource(engine: engine)
```

All functions of the `asset` API refer to an asset source by its unique `id`. That's why it has to be mandatory. Trying to add an asset source with an already registered `id` will fail.

```swift highlight-customSourceId
var id: String { "foobar" }
```

## Finding and Applying Assets

The `findAssets` function should return paginated asset results for the given `queryData`. The asset results have a set of mandatory and optional properties. For a listing with an explanation for each property please refer to the [Integrate a Custom Asset Source](https://img.ly/docs/cesdk/mac-catalyst/import-media/from-remote-source/unsplash-8f31f0/) guide. The properties of the `queryData` and the pagination mechanism are also explained in this guide.

```swift
public func findAssets(sourceID: String, query: AssetQueryData) async throws -> AssetQueryResult
```

Finds assets of a given type in a specific asset source.

- `sourceID`: The ID of the asset source.
- `query`: All the options to filter the search results by.
- Returns: The search results.

The optional function 'applyAsset' is to define the behavior of what to do when an asset gets applied to the scene. You can use the engine's APIs to do whatever you want with the given asset result. In this case, we always create an image block and add it to the first page we find.

If you don't provide this function the engine's default behavior is to create a block based on the asset result's `meta.blockType` property, add the block to the active page, and sensibly position and size it.

```swift
public func apply(sourceID: String, assetResult: AssetResult) async throws -> DesignBlockID?
```

Apply an asset result to the active scene.
The default behavior will instantiate a block and configure it according to the asset's properties.

- Note: that this can be overridden by providing an `applyAsset` function when adding the asset source.
- `sourceID`: The ID of the asset source.
- `assetResult`: A single assetResult of a `findAssets` query.

```swift
public func defaultApplyAsset(assetResult: AssetResult) async throws -> DesignBlockID?
```

The default implementation for applying an asset to the scene.
This implementation is used when no `applyAsset` function is provided to `addSource`.

- `assetResult:`: A single assetResult of a `findAssets` query.

```swift
public func applyToBlock(sourceID: String, assetResult: AssetResult, block: DesignBlockID) async throws
```

Apply an asset result to the given block.

- `sourceID`: The ID of the asset source.
- `assetResult`: A single assetResult of a `findAssets` query.
- `block`: The block the asset should be applied to.

```swift
public func defaultApplyAssetToBlock(assetResult: AssetResult, block: DesignBlockID) async throws
```

The default implementation for applying an asset to an existing block.
This implementation is used when no `applyAssetToBlock` function is provided to `addSource`.

- `assetResult`: A single assetResult of a `findAssets` query.
- `block`: The block to apply the asset result to.

```swift
public func getSupportedMIMETypes(sourceID: String) throws -> [String]
```

Queries the list of supported mime types of the specified asset source. An empty result means that all mime types are supported.

- `sourceID:`: The ID of the asset source.

## Registering a New Asset Source

```swift
public func addSource(_ source: AssetSource) throws
```

Adds a custom asset source. Its ID has to be unique.

- `source:`: The asset source.

```swift
public func addLocalSource(sourceID: String, supportedMimeTypes: [String]? = nil, applyAsset: (@Sendable (AssetResult) async throws -> DesignBlockID?)? = nil, applyAssetToBlock: (@Sendable (AssetResult, DesignBlockID) async throws -> Void)? = nil) throws
```

Adds a local asset source. Its ID has to be unique.

- `sourceID`: The asset source.
- `supportedMimeTypes`: The mime types of assets that are allowed to be added to this local source.
- `applyAsset`: An optional callback that can be used to override the default behavior of applying a given asset
  result to the active scene. Returns the newly created block or `nil` if a new block was not created.
- `applyAssetToBlock`: An optional callback that can be used to override the default behavior of applying an asset
  result to a given block.

```swift
public func findAllSources() -> [String]
```

Finds all registered asset sources.

- Returns: A list with the IDs of all registered asset sources.

```swift
public func removeSource(sourceID: String) throws
```

Removes an asset source with the given ID.

- `sourceID:`: The ID to refer to the asset source.

```swift
public var onAssetSourceAdded: AsyncStream<String> { get }
```

Subscribe to changes whenever an asset source is added.

```swift
public var onAssetSourceRemoved: AsyncStream<String> { get }
```

Subscribe to changes whenever an asset source is removed.

```swift
public var onAssetSourceUpdated: AsyncStream<String> { get }
```

Subscribe to changes whenever asset source's content is updated.

## Scene Asset Sources

A scene colors asset source is automatically available that allows listing all colors in the scene. This asset source is read-only and is updated when `findAssets` is called.

## Add an Asset

```swift
public func addAsset(to sourceID: String, asset: AssetDefinition) throws
```

Adds the given asset to an asset source.

- `to`: The asset source ID that the asset should be added to.
- `asset`: The asset to be added to the asset source.

## Remove an Asset

```swift
public func removeAsset(from sourceID: String, assetID: String) throws
```

Removes the specified asset from its asset source.

- `from`: The id of the asset source that currently contains the asset.
- `assetID`: The id of the asset to be removed.

## Asset Source Content Updates

If the contents of your custom asset source change, you can call the `assetSourceUpdated` API to later notify all subscribers of the `onAssetSourceUpdated` API.

```swift
public func assetSourceContentsChanged(sourceID: String) throws
```

Notifies the engine that the contents of an asset source changed.

- `sourceID:`: The ID of the asset source.

## Groups in Assets

```swift
public func getGroups(sourceID: String) async throws -> [String]
```

Queries the asset source's groups for a certain asset type.

- `sourceID:`: The ID of the asset source.
- Returns: The asset groups.

## Credits and License

```swift
public func getCredits(sourceID: String) -> AssetCredits?
```

Queries the asset source's credits info.

- `sourceID:`: The ID of the asset source.
- Returns: The asset source's credits info consisting of a name and an optional URL.

```swift
public func getLicense(sourceID: String) -> AssetLicense?
```

Queries the asset source's license info.

- `sourceID:`: The ID of the asset source.
- Returns: The asset source's license info consisting of a name and an optional URL.

## Full Code

Here's the full code:

```swift
let scene = try engine.scene.create()
let page = try engine.block.create(.page)
let block = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: page)
try engine.block.appendChild(to: page, child: block)

let customSource = CustomAssetSource(engine: engine)

let addedTask = Task {
  for await sourceID in engine.asset.onAssetSourceAdded {
    print("Added source: \(sourceID)")
  }
}
let removedTask = Task {
  for await sourceID in engine.asset.onAssetSourceRemoved {
    print("Removed source: \(sourceID)")
  }
}
let updatedTask = Task {
  for await sourceID in engine.asset.onAssetSourceUpdated {
    print("Updated source: \(sourceID)")
  }
}

try engine.asset.addSource(customSource)

let localSourceID = "local-source"
try engine.asset.addLocalSource(sourceID: localSourceID)

let assetDefinition = AssetDefinition(
  id: "ocean-waves-1",
  meta: [
    "uri": "https://example.com/ocean-waves-1.mp4",
    "thumbUri": "https://example.com/thumbnails/ocean-waves-1.jpg",
    "mimeType": MIMEType.mp4.rawValue,
    "width": "1920",
    "height": "1080",
  ],
  label: [
    "en": "relaxing ocean waves",
  ],
  tags: [
    "en": ["ocean", "waves", "soothing", "slow"],
  ]
)
try engine.asset.addAsset(to: localSourceID, asset: assetDefinition)
try engine.asset.removeAsset(from: localSourceID, assetID: assetDefinition.id)

engine.asset.findAllSources()

let mimeTypes = try engine.asset.getSupportedMIMETypes(sourceID: customSource.id)

let credits = engine.asset.getCredits(sourceID: customSource.id)
let license = engine.asset.getLicense(sourceID: customSource.id)
let groups = try await engine.asset.getGroups(sourceID: customSource.id)

let result = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: "", page: 0, perPage: 10)
)
let asset = result.assets[0]
let sortByNewest = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .descending)
)
let sortById = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .ascending, sortKey: "id")
)
let sortByMetaKeyValue = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: nil, page: 0, perPage: 10, sortingOrder: .ascending, sortKey: "someMetaKey")
)
let search = try await engine.asset.findAssets(
  sourceID: customSource.id,
  query: .init(query: "banana", page: 0, perPage: 100)
)

let sceneColorsResult = try await engine.asset.findAssets(
  sourceID: "ly.img.scene.colors",
  query: .init(query: nil, page: 0, perPage: 99999)
)
let colorAsset = sceneColorsResult.assets[0]

try await engine.asset.apply(sourceID: customSource.id, assetResult: asset)

try await engine.asset.applyToBlock(sourceID: customSource.id, assetResult: asset, block: block)

try engine.asset.assetSourceContentsChanged(sourceID: customSource.id)

try engine.asset.removeSource(sourceID: customSource.id)
try engine.asset.removeSource(sourceID: localSourceID)

final class CustomAssetSource: NSObject, AssetSource {
  private weak var engine: Engine?

  init(engine: Engine) {
    self.engine = engine
  }

  var id: String { "foobar" }

  func findAssets(queryData: AssetQueryData) async throws -> AssetQueryResult {
    .init(assets: [
      .init(id: "logo",
            meta: [
              "uri": "https://img.ly/static/ubq_samples/imgly_logo.jpg",
              "thumbUri": "https://img.ly/static/ubq_samples/thumbnails/imgly_logo.jpg",
              "blockType": DesignBlockType.graphic.rawValue,
              "fillType": FillType.image.rawValue,
              "width": "320",
              "height": "116",
            ],
            context: .init(sourceID: "foobar")),
    ],
    currentPage: queryData.page,
    total: 1)
  }

  func apply(asset: AssetResult) async throws -> NSNumber? {
    if let id = try await engine?.asset.defaultApplyAsset(assetResult: asset) {
      .init(value: id)
    } else {
      nil
    }
  }

  func applyToBlock(asset: AssetResult, block: DesignBlockID) async throws {
    try await engine?.asset.defaultApplyAssetToBlock(assetResult: asset, block: block)
  }

  var supportedMIMETypes: [String]? { [MIMEType.jpeg.rawValue] }
  var credits: IMGLYEngine.AssetCredits? { nil }
  var license: IMGLYEngine.AssetLicense? { nil }
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
