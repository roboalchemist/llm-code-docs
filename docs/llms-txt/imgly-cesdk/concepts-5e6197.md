# Source: https://img.ly/docs/cesdk/android/import-media/concepts-5e6197/

---
title: "Concepts"
description: "Understand key asset concepts like sources, formats, metadata, and how assets are integrated into designs."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/concepts-5e6197/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Concepts](https://img.ly/docs/cesdk/android/import-media/concepts-5e6197/)

---

```kotlin reference-only
val engine = Engine(id = "ly.img.engine.example")
engine.start()
engine.bindOffscreen(width = 1080, height = 1920)
val coroutineScope = CoroutineScope(Dispatchers.Main)

val scene = engine.scene.create()
val page = engine.block.create(DesignBlockType.Page)
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(parent = scene, child = page)
engine.block.appendChild(parent = page, child = block)

val source = UnsplashAssetSource()
engine.asset.addSource(source)
val localSourceId = "LocalSourceId"
engine.asset.addLocalSource(localSourceId, supportedMimeTypes = "image/jpeg")
val assetSourceIds = engine.asset.findAllSources() // List [ "ly.img.asset.source.unsplash", "LocalSourceId", ... ]
engine.asset.onAssetSourceAdded()
    .onEach { println("Asset source added: id=$it") }
    .launchIn(coroutineScope)
engine.asset.onAssetSourceRemoved()
    .onEach { println("Asset source removed: id=$it") }
    .launchIn(coroutineScope)
engine.asset.onAssetSourceUpdated()
    .onEach { println("Asset source updated: id=$it") }
    .launchIn(coroutineScope)
val mimeTypes = engine.asset.getSourceSupportedMimeTypes(sourceId = "ly.img.asset.source.unsplash")

val list = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10)
)
val sortByNewest = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.DESCENDING)
)
val sortById = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.ASCENDING, sortKey = "id")
)
val sortByMetaKeyValue = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.ASCENDING, sortKey = "someMetaKey")
)
val search = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "banana", page = 1, perPage = 10)
)

val documentColors = engine.asset.findAssets(
    sourceId = "ly.img.scene.colors",
    query = FindAssetsQuery(query = "", page = 0, perPage = 99999)
)
val colorAsset = documentColors.assets[0]

engine.asset.applyAssetSourceAsset(sourceId = source.sourceId, asset = list.assets[0])
engine.asset.applyAssetSourceAsset(sourceId = source.sourceId, asset = list.assets[0], block = block)
engine.asset.defaultApplyAsset(asset = search.assets[0])
engine.asset.defaultApplyAsset(asset = search.assets[0], block = block)

val assetDefinition = AssetDefinition(
id = "localAssetId",
meta = mapOf(
	"uri" to "https://example.com/localAssetId.jpg",
	"thumbUri" to "https://example.com/thumbnails/localAssetId.jpg",
	"kind" to "image",
	"fillType" to FillType.Image,
	"width" to "1080",
	"height" to "1920"
)
)
engine.asset.addAsset(sourceId = localSourceId, asset = assetDefinition)
engine.asset.removeAsset(sourceId = localSourceId, assetId = assetDefinition.id)

engine.asset.assetSourceContentsChanged(sourceId = source.sourceId)

engine.asset.removeSource(sourceId = source.sourceId)
engine.asset.removeSource(sourceId = localSourceId)

val credits = engine.asset.getCredits(sourceId = source.sourceId)
val license = engine.asset.getLicense(sourceId = source.sourceId)
val groups = engine.asset.getGroups(sourceId = source.sourceId)

engine.stop()

class UnsplashAssetSource : AssetSource(sourceId = "ly.img.asset.source.unsplash") {

  override suspend fun getGroups(): List<String>? = null

  override val credits = AssetCredits(
    name = "Unsplash",
    uri = Uri.parse("https://unsplash.com/")
  )

  override val license = AssetLicense(
    name = "Unsplash license (free)",
    uri = Uri.parse("https://unsplash.com/license")
  )

  override suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult {
    return if (query.query.isNullOrEmpty()) query.getPopularList() else query.getSearchList()
  }

  private suspend fun FindAssetsQuery.getPopularList(): FindAssetsResult {
    val queryParams = listOf(
      "order_by" to "popular",
      "page" to page,
      "perPage" to perPage
    ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
    val assetsArray = getResponseAsString("$BASE_URL/photos?$queryParams").let(::JSONArray)
    return FindAssetsResult(
      assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
      currentPage = page,
      nextPage = page + 1,
      total = 0
    )
  }

  private suspend fun FindAssetsQuery.getSearchList(): FindAssetsResult {
    val queryParams = listOf(
      "query" to query,
      "page" to page,
      "perPage" to perPage
    ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
    val response = getResponseAsString("$BASE_URL/search/photos?$queryParams").let(::JSONObject)
    val assetsArray = response.getJSONArray("results")
    val total = response.getInt("total")
    val totalPages = response.getInt("total_pages")
    return FindAssetsResult(
      assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
      currentPage = page,
      nextPage = if (page == totalPages) -1 else page + 1,
      total = total
    )
  }

  private suspend fun getResponseAsString(url: String) = withContext(Dispatchers.IO) {
    val connection = URL(url).openConnection() as HttpURLConnection
    require(connection.responseCode in 200 until 300) {
      connection.errorStream.bufferedReader().use { it.readText() }
    }
    connection.inputStream.bufferedReader().use { it.readText() }
  }

  private fun JSONObject.toAsset() = Asset(
    id = getString("id"),
    locale = "en",
    label = when {
      has("description") -> getString("description")
      has("alt_description") -> getString("alt_description")
      else -> null
    },
    tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
      (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
    }?.takeIf { it.isNotEmpty() },
    thumbnailUri = getJSONObject("urls").getString("thumb").let { Uri.parse(it) },
    width = getInt("width").toFloat(),
    height = getInt("height").toFloat(),
    meta = mapOf("uri" to getJSONObject("urls").getString("full")),
    context = AssetContext(sourceId = "unsplash", createdByRole = ""),
    credits = AssetCredits(
      name = getJSONObject("user").getString("name"),
      uri = getJSONObject("user")
        .takeIf { it.has("links") }
        ?.getJSONObject("links")
        ?.getString("html")
        ?.let { Uri.parse(it) }
    ),
    utm = AssetUTM(source = "CE.SDK Demo", medium = "referral")
  )

  companion object {
    private const val BASE_URL = "" // INSERT YOUR UNSPLASH PROXY URL HERE
  }
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to manage assets through the `asset` API.

To begin working with assets first you need at least one asset source. As the name might imply asset sources provide the engine with assets. These assets then show up in the editor's asset library. But they can also be independently searched and used to create design blocks. Asset sources can be added dynamically using the `asset` API as we will show in this guide.

## Defining a Custom Asset Source

Asset sources need at least an `id` and a `findAssets` function. You may notice `findAssets` method is `suspend`. This way you can use web requests or other long-running operations inside them and return results asynchronously.

Let's go over these member one by one:

All functions of `AssetApi` refer to an asset source by its unique `id`. That's why it has to be mandatory. Trying to add an asset source with an already registered `id` will fail.

```kotlin highlight-customSourceId
val localSourceId = "LocalSourceId"
```

```kotlin
abstract suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult
```

Searches assets based on the `query`.

- `query`: the object that is used to filter results.

- Returns asset search result.

```kotlin
abstract suspend fun getGroups(): List<String>?
```

Specifies all the available groups in this asset source.

- Returns list of available groups.

```kotlin
open val credits: AssetCredits? = null
```

Returns the credits info of this asset source. By default it is null.

- Returns the credits info.

```kotlin
open val license: AssetLicense? = null
```

Returns the license info of this asset source. By default it is null.

- Returns the license info.

## Registering a New Asset Source

```kotlin
fun addSource(source: AssetSource)
```

Adds a custom asset source. Its ID has to be unique.

- `source`: the asset source.

```kotlin
fun addLocalSource(
    sourceId: String,
    supportedMimeTypes: List<String>,
    applyAsset: (suspend (Asset) -> DesignBlock?)? = null,
    applyAssetToBlock: (suspend (Asset, DesignBlock) -> Unit)? = null,
)
```

Adds a local asset source. Its ID has to be unique.

- `sourceId`: the id of the new local asset source.

- `supportedMimeTypes`: the mime types of assets that are allowed to be added to this local source.

- `applyAsset`: an optional callback that can be used to override the default behavior of applying a given asset result to the active scene.

- `applyAssetToBlock`: an optional callback that can be used to override the default behavior of applying an asset result to a given block.

```kotlin
fun findAllSources(): List<String>
```

Finds all registered asset sources.

- Returns a list with the IDs of all registered asset sources.

```kotlin
fun removeSource(sourceId: String)
```

Removes an asset source with the given ID.

- `sourceId`: the ID to refer to the asset source.

```kotlin
fun onAssetSourceAdded(): Flow<String>
```

Subscribe to asset source addition events.

- Returns flow of asset source addition events.

```kotlin
fun onAssetSourceRemoved(): Flow<String>
```

Subscribe to asset source removal events.

- Returns flow of asset source removal events.

```kotlin
fun onAssetSourceUpdated(): Flow<String>
```

Subscribe to asset source's content update events.

- Returns flow of asset source's content update events.

## Finding and Applying Assets

The `findAssets` function should return paginated asset results for the given `query`. The asset results have a set of mandatory and optional properties. For a listing with an explanation for each property please refer to the [Integrate a Custom Asset Source](https://img.ly/docs/cesdk/android/import-media/from-remote-source/unsplash-8f31f0/) guide. The properties of the `query` and the pagination mechanism are also explained in this guide.

```kotlin
suspend fun findAssets(
    sourceId: String,
    query: FindAssetsQuery,
): FindAssetsResult
```

Finds assets of a given type in a specific asset source.

- `sourceId`: the ID of the asset source.

- `query`: all the options to filter the search results by.

- Returns the search results.

The optional function 'applyAssetSourceAsset' is to define the behavior of what to do when an asset gets applied to the scene. You can use the engine's APIs to do whatever you want with the given asset result. In this case, we always create an image block and add it to the first page we find.

If you don't provide this function the engine's default behavior is to create a block based on the asset.meta\["blockType"] property, add the block to the active page, and sensibly position and size it.

```kotlin
suspend fun applyAssetSourceAsset(
    sourceId: String,
    asset: Asset,
): DesignBlock?
```

Applies an asset to the active scene using custom `AssetSource.applyAsset` function.

- `sourceId`: the sourceId of `AssetSource` which `AssetSource.applyAsset` function is going to be invoked.

- `asset`: the asset to be applied to the active scene. Normally it's a single result of a `findAssets` query.

- Returns the newly created block or null if no new block is created.

```kotlin
suspend fun applyAssetSourceAsset(
    sourceId: String,
    asset: Asset,
    block: DesignBlock,
)
```

Applies an asset to the `block` using custom `AssetSource.applyAsset` function.

- `sourceId`: the sourceId of `AssetSource` which `AssetSource.applyAsset` function is going to be invoked.

- `asset`: the asset that will be applied to the existing block. Normally it's a single result of a `findAssets` query.

- `block`: the block that will be modified by the asset.

```kotlin
suspend fun defaultApplyAsset(asset: Asset): DesignBlock?
```

This is the default implementation of applying asset to the active scene.

This means a design block is instantiated and configured according to the `Asset.meta` properties.

- `asset`: the asset to be applied to the active scene. Normally it's a single result of a `findAssets` query.

- Returns the newly created block or null if no new block is created.

```kotlin
suspend fun defaultApplyAsset(
    asset: Asset,
    block: DesignBlock,
)
```

This is the default implementation of applying `asset` object to an existing `block`.

This means it replaces the `block` content with `asset` content, if compatible.

- `asset`: the asset that will be applied to the existing block. Normally it's a single result of a `findAssets` query.

- `block`: the block that will be modified by the asset.

```kotlin
fun getSourceSupportedMimeTypes(sourceId: String): List<String>
```

Get the asset source's list of supported mime types.

- `sourceId`: the ID of the asset source.

- Returns the list of supported mime types of this asset source.

## Document Asset Sources

A document color asset source is automatically available that allows listing all colors in the document. This asset source is read-only and is updated when `findAssets` is called.

## Add an Asset

```kotlin
fun addAsset(
    sourceId: String,
    asset: AssetDefinition,
)
```

Adds the given `asset` to a local asset source.

- `sourceId`: The local asset source ID that the asset should be added to.

- `asset`: the asset that should be added.

## Remove an Asset

```kotlin
fun removeAsset(
    sourceId: String,
    assetId: String,
)
```

Removes the specified asset from its local asset source.

- `sourceId`: the ID of the local asset source that currently contains the asset.

- `assetId`: the asset id that should be removed.

## Asset Source Content Updates

If the contents of your custom asset source change, you can call the `assetSourceContentsChanged` API to later notify all subscribers of the `onAssetSourceUpdated` API.

```kotlin
fun assetSourceContentsChanged(sourceId: String)
```

Notifies the engine that the contents of an asset source changed.

- `sourceId`: the asset source whose contents changed.

## Groups in Assets

```kotlin
suspend fun getGroups(sourceId: String): List<String>?
```

Queries the asset source's groups for a certain asset type.

- `sourceId`: the ID of the asset source.

- Returns the asset groups.

## Credits and License

```kotlin
fun getCredits(sourceId: String): AssetCredits?
```

Queries the asset source's credits info.

- `sourceId`: the ID of the asset source.

- Returns the asset source's credits info consisting of a name and an optional URL.

```kotlin
fun getLicense(sourceId: String): AssetLicense?
```

Queries the asset source's license info.

- `sourceId`: the ID of the asset source.

- Returns the asset source's license info consisting of a name and an optional URL.

## Full Code

Here's the full code:

```kotlin
val engine = Engine(id = "ly.img.engine.example")
engine.start()
engine.bindOffscreen(width = 100, height = 100)
val coroutineScope = CoroutineScope(Dispatchers.Main)

val scene = engine.scene.create()
val page = engine.block.create(DesignBlockType.Page)
val block = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(parent = scene, child = page)
engine.block.appendChild(parent = page, child = block)

val source = UnsplashAssetSource()
engine.asset.addSource(source)
val localSourceId = "LocalSourceId"
engine.asset.addLocalSource(localSourceId, supportedMimeTypes = "image/jpeg")
val assetSourceIds = engine.asset.findAllSources() // List [ "ly.img.asset.source.unsplash", "LocalSourceId", ... ]
engine.asset.onAssetSourceAdded()
    .onEach { println("Asset source added: id=$it") }
    .launchIn(coroutineScope)
engine.asset.onAssetSourceRemoved()
    .onEach { println("Asset source removed: id=$it") }
    .launchIn(coroutineScope)
engine.asset.onAssetSourceUpdated()
    .onEach { println("Asset source updated: id=$it") }
    .launchIn(coroutineScope)
val mimeTypes = engine.asset.getSourceSupportedMimeTypes(sourceId = "ly.img.asset.source.unsplash")

val list = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10)
)
val sortByNewest = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.DESCENDING)
)
val sortById = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.ASCENDING, sortKey = "id")
)
val sortByMetaKeyValue = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "", page = 1, perPage = 10, sortingOrder = SortingOrder.ASCENDING, sortKey = "someMetaKey")
)
val search = engine.asset.findAssets(
    sourceId = source.sourceId,
    query = FindAssetsQuery(query = "banana", page = 1, perPage = 10)
)

val documentColors = engine.asset.findAssets(
    sourceId = "ly.img.scene.colors",
    query = FindAssetsQuery(query = "", page = 0, perPage = 99999)
)
val colorAsset = documentColors.assets[0]

engine.asset.applyAssetSourceAsset(sourceId = source.sourceId, asset = list.assets[0])
engine.asset.applyAssetSourceAsset(sourceId = source.sourceId, asset = list.assets[0], block = block)
engine.asset.defaultApplyAsset(asset = search.assets[0])
engine.asset.defaultApplyAsset(asset = search.assets[0], block = block)

val assetDefinition = AssetDefinition(
id = "localAssetId",
meta = mapOf(
    "uri" to "https://example.com/localAssetId.jpg",
    "thumbUri" to "https://example.com/thumbnails/localAssetId.jpg",
    "kind" to "image",
    "fillType" to FillType.Image,
    "width" to "1080",
    "height" to "1920"
)
)
engine.asset.addAsset(sourceId = localSourceId, asset = assetDefinition)
engine.asset.removeAsset(sourceId = localSourceId, assetId = assetDefinition.id)

engine.asset.assetSourceContentsChanged(sourceId = source.sourceId)

engine.asset.removeSource(sourceId = source.sourceId)
engine.asset.removeSource(sourceId = localSourceId)

val credits = engine.asset.getCredits(sourceId = source.sourceId)
val license = engine.asset.getLicense(sourceId = source.sourceId)
val groups = engine.asset.getGroups(sourceId = source.sourceId)

engine.stop()

class UnsplashAssetSource : AssetSource(sourceId = "ly.img.asset.source.unsplash") {

  override suspend fun getGroups(): List<String>? = null

  override val credits = AssetCredits(
    name = "Unsplash",
    uri = Uri.parse("https://unsplash.com/")
  )

  override val license = AssetLicense(
    name = "Unsplash license (free)",
    uri = Uri.parse("https://unsplash.com/license")
  )

  override suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult {
    return if (query.query.isNullOrEmpty()) query.getPopularList() else query.getSearchList()
  }

  private suspend fun FindAssetsQuery.getPopularList(): FindAssetsResult {
    val queryParams = listOf(
      "order_by" to "popular",
      "page" to page,
      "perPage" to perPage
    ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
    val assetsArray = getResponseAsString("$BASE_URL/photos?$queryParams").let(::JSONArray)
    return FindAssetsResult(
      assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
      currentPage = page,
      nextPage = page + 1,
      total = 0
    )
  }

  private suspend fun FindAssetsQuery.getSearchList(): FindAssetsResult {
    val queryParams = listOf(
      "query" to query,
      "page" to page,
      "perPage" to perPage
    ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
    val response = getResponseAsString("$BASE_URL/search/photos?$queryParams").let(::JSONObject)
    val assetsArray = response.getJSONArray("results")
    val total = response.getInt("total")
    val totalPages = response.getInt("total_pages")
    return FindAssetsResult(
      assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
      currentPage = page,
      nextPage = if (page == totalPages) -1 else page + 1,
      total = total
    )
  }

  private suspend fun getResponseAsString(url: String) = withContext(Dispatchers.IO) {
    val connection = URL(url).openConnection() as HttpURLConnection
    require(connection.responseCode in 200 until 300) {
      connection.errorStream.bufferedReader().use { it.readText() }
    }
    connection.inputStream.bufferedReader().use { it.readText() }
  }

  private fun JSONObject.toAsset() = Asset(
    id = getString("id"),
    locale = "en",
    label = when {
      has("description") -> getString("description")
      has("alt_description") -> getString("alt_description")
      else -> null
    },
    tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
      (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
    }?.takeIf { it.isNotEmpty() },
    thumbnailUri = getJSONObject("urls").getString("thumb").let { Uri.parse(it) },
    width = getInt("width").toFloat(),
    height = getInt("height").toFloat(),
    meta = mapOf("uri" to getJSONObject("urls").getString("full")),
    context = AssetContext(sourceId = "unsplash", createdByRole = ""),
    credits = AssetCredits(
      name = getJSONObject("user").getString("name"),
      uri = getJSONObject("user")
        .takeIf { it.has("links") }
        ?.getJSONObject("links")
        ?.getString("html")
        ?.let { Uri.parse(it) }
    ),
    utm = AssetUTM(source = "CE.SDK Demo", medium = "referral")
  )

  companion object {
    private const val BASE_URL = "" // INSERT YOUR UNSPLASH PROXY URL HERE
  }
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
