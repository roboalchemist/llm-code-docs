# Source: https://img.ly/docs/cesdk/android/import-media/from-remote-source/unsplash-8f31f0/

---
title: "From A Custom Source"
description: "Browse and import royalty-free images from Unsplash into the editor."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/from-remote-source/unsplash-8f31f0/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Import From Remote Source](https://img.ly/docs/cesdk/android/import-media/from-remote-source-b65faf/) > [From a Custom Source](https://img.ly/docs/cesdk/android/import-media/from-remote-source/unsplash-8f31f0/)

---

```kotlin file=@cesdk_android_examples/engine-guides-custom-asset-source/UnsplashAssetSource.kt reference-only
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Asset
import ly.img.engine.AssetColor
import ly.img.engine.AssetContext
import ly.img.engine.AssetCredits
import ly.img.engine.AssetDefinition
import ly.img.engine.AssetLicense
import ly.img.engine.AssetPayload
import ly.img.engine.AssetSource
import ly.img.engine.AssetUTM
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.FindAssetsQuery
import ly.img.engine.FindAssetsResult
import ly.img.engine.ShapeType
import org.json.JSONArray
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

fun customAssetSource(
    license: String?, // pass null or empty for evaluation mode with watermark
    userId: String,
    unsplashBaseUrl: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 1080, height = 1920)

    val source = UnsplashAssetSource(unsplashBaseUrl) // INSERT YOUR UNSPLASH PROXY URL HERE
    engine.asset.addSource(source)

    val list = runCatching {
        engine.asset.findAssets(
            sourceId = "ly.img.asset.source.unsplash",
            query = FindAssetsQuery(query = "", page = 1, perPage = 10),
        )
    }.getOrElse { it.printStackTrace() }

    val search = runCatching {
        engine.asset.findAssets(
            sourceId = "ly.img.asset.source.unsplash",
            query = FindAssetsQuery(query = "banana", page = 1, perPage = 10),
        )
    }.getOrElse { it.printStackTrace() }

    engine.asset.addLocalSource(
        sourceId = "background-videos",
        supportedMimeTypes = listOf("video/mp4"),
    )
    val asset = AssetDefinition(
        id = "ocean-waves-1",
        label = mapOf(
            "en" to "relaxing ocean waves",
            "es" to "olas del mar relajantes",
        ),
        tags = mapOf(
            "en" to listOf("ocean", "waves", "soothing", "slow"),
            "es" to listOf("mar", "olas", "calmante", "lento"),
        ),
        meta = mapOf(
            "uri" to "https://example.com/ocean-waves-1.mp4",
            "thumbUri" to "https://example.com/thumbnails/ocean-waves-1.jpg",
            "mimeType" to "video/mp4",
            "width" to "1920",
            "height" to "1080",
        ),
        payload = AssetPayload(color = AssetColor.RGB(r = 0F, g = 0F, b = 1F)),
    )
    engine.asset.addAsset(sourceId = "background-videos", asset = asset)

    engine.stop()
}

class UnsplashAssetSource(
    private val baseUrl: String,
) : AssetSource(sourceId = "ly.img.asset.source.unsplash") {

    override suspend fun getGroups(): List<String>? = null

    override val supportedMimeTypes = listOf("image/jpeg")

    override val credits = AssetCredits(
        name = "Unsplash",
        uri = Uri.parse("https://unsplash.com/"),
    )

    override val license = AssetLicense(
        name = "Unsplash license (free)",
        uri = Uri.parse("https://unsplash.com/license"),
    )

    override suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult = withContext(Dispatchers.IO) {
        if (query.query.isNullOrEmpty()) query.getPopularList() else query.getSearchList()
    }

    private suspend fun FindAssetsQuery.getPopularList(): FindAssetsResult {
        val queryParams = listOf(
            "order_by" to "popular",
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val assetsArray = getResponseAsString("$baseUrl/photos?$queryParams").let(::JSONArray)
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = page + 1,
            total = Int.MAX_VALUE,
        )
    }

    private suspend fun FindAssetsQuery.getSearchList(): FindAssetsResult {
        val queryParams = listOf(
            "query" to query,
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val response = getResponseAsString("$baseUrl/search/photos?$queryParams").let(::JSONObject)
        val assetsArray = response.getJSONArray("results")
        val total = response.getInt("total")
        val totalPages = response.getInt("total_pages")
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = if (page == totalPages) -1 else page + 1,
            total = total,
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
            !isNull("description") -> getString("description")
            !isNull("alt_description") -> getString("alt_description")
            else -> null
        },
        tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
            (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
        }?.takeIf { it.isNotEmpty() },
        meta = mapOf(
            "uri" to getJSONObject("urls").getString("full"),
            "thumbUri" to getJSONObject("urls").getString("thumb"),
            "blockType" to DesignBlockType.Graphic.key,
            "fillType" to FillType.Image.key,
            "shapeType" to ShapeType.Rect.key,
            "kind" to "image",
            "width" to getInt("width").toString(),
            "height" to getInt("height").toString(),
        ),
        context = AssetContext(sourceId = "unsplash"),
        credits = AssetCredits(
            name = getJSONObject("user").getString("name"),
            uri = getJSONObject("user")
                .takeIf { it.has("links") }
                ?.getJSONObject("links")
                ?.getString("html")
                ?.let { Uri.parse(it) },
        ),
        utm = AssetUTM(source = "CE.SDK Demo", medium = "referral"),
    )
}
```

In this example, we will show you how to integrate your custom asset sources into [CE.SDK](https://img.ly/products/creative-sdk).

With CE.SDK you can directly add external image providers like Unsplash or your own backend.
A third option we will explore in this guide is using the engine's Asset API directly.
Follow along with this example while we are going to add the Unsplash library.

Adding an asset source is done creating an asset source definition and adding it using `fun addSource(source: AssetSource)`.
The asset source needs a unique identifier as part of an object implementing the interface of the source.
All Asset API methods require the asset source's unique identifier.

```kotlin highlight-unsplash-definition
val source = UnsplashAssetSource(unsplashBaseUrl) // INSERT YOUR UNSPLASH PROXY URL HERE
engine.asset.addSource(source)
```

The most important function to implement is `suspend fun findAssets(sourceId: String, query: FindAssetsQuery): FindAssetsResult`.
With this function alone you can define the complete asset source.
It receives the asset query as an argument and returns results asynchronously.

- The argument is the `query` and describes the slice of data the engine wants to use.
  This includes a query string and pagination information.
- The result of this query, besides the actual asset data, returns information like the current page, the next page and the total number of assets available for this specific query.

Providing a `suspend` function gives us great flexibility since we are completely agnostic of how we want to get the assets.
We can use `HttpURLConnection`, local storage, cache or import a 3rd party library to return the result.

```kotlin highlight-unsplash-findAssets
val list = runCatching {
    engine.asset.findAssets(
        sourceId = "ly.img.asset.source.unsplash",
        query = FindAssetsQuery(query = "", page = 1, perPage = 10),
    )
}.getOrElse { it.printStackTrace() }
```

Let us implement an Unsplash asset source.
Please note that this is just for demonstration purposes only and may not be ideal if you want to integrate Unsplash in your production environment.

We will create a class implementing abstract class `AssetSource`. A unique `sourceId = "ly.img.asset.source.unsplash"` is passed via the constructor.
There are multiple abstract methods that we need to implement, however, `findAssets` is the most important one.

```kotlin highlight-unsplash-source-creation
class UnsplashAssetSource(
    private val baseUrl: String,
) : AssetSource(sourceId = "ly.img.asset.source.unsplash") {
```

`findAssets` is the function that receives `query` object from the engine and is supposed to return the corresponding results.
Unsplash has different API endpoints for different use cases. If we want to search we need to call a different endpoint as if we just want to display images without any search term.
Therefore we need to check if the query data contains a `query` string. If `findAssets` was called with a non-empty `query` we call the `/search` endpoint via `getSearchList` function, otherwise we call `getPopularList`. As we can see in the example, we are passing the `query` object to `findAssets` method, containing the following fields:

- `query.query`: The current search string from the search bar in the asset library.
- `query.page`: For Unsplash specifically the requested page number starts with 1.
  We do not query all assets at once but by pages.
  As the user scrolls down more pages will be requested by calls to the `findAssets` method.
- `query.perPage`: Determines how many assets we want to have included per page.
  This might change between calls.
  For instance, `perPage` can be called with a small number to display a small preview, but with a higher number e.g. if we want to show more assets in a grid view.

```kotlin highlight-unsplash-query
    override suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult = withContext(Dispatchers.IO) {
        if (query.query.isNullOrEmpty()) query.getPopularList() else query.getSearchList()
    }

    private suspend fun FindAssetsQuery.getPopularList(): FindAssetsResult {
        val queryParams = listOf(
            "order_by" to "popular",
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val assetsArray = getResponseAsString("$baseUrl/photos?$queryParams").let(::JSONArray)
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = page + 1,
            total = Int.MAX_VALUE,
        )
    }

    private suspend fun FindAssetsQuery.getSearchList(): FindAssetsResult {
        val queryParams = listOf(
            "query" to query,
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val response = getResponseAsString("$baseUrl/search/photos?$queryParams").let(::JSONObject)
        val assetsArray = response.getJSONArray("results")
        val total = response.getInt("total")
        val totalPages = response.getInt("total_pages")
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = if (page == totalPages) -1 else page + 1,
            total = total,
        )
    }
```

Once we receive the response and check for success we need to map Unsplash's result to what the asset source API needs as a result. The CE.SDK expects an object with the following properties:

- `assets`: An array of assets for the current query. We will take a look at what these have to look like in the next paragraph.
- `currentPage`: Return the current page that was requested.
- `nextPage`: This is the next page that can be requested after the current one. Should be `-1` if there is no other page (no more assets). In this case we stop querying for more even if the user has scrolled to the bottom.
- `total`: The total number of assets available for the current query. If we search for "Cat" with `perPage` set to 30, we will get 30 assets, but `total` likely will be a much higher number.

```kotlin highlight-unsplash-result-mapping
val response = getResponseAsString("$baseUrl/search/photos?$queryParams").let(::JSONObject)
val assetsArray = response.getJSONArray("results")
val total = response.getInt("total")
val totalPages = response.getInt("total_pages")
return FindAssetsResult(
    assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
    currentPage = page,
    nextPage = if (page == totalPages) -1 else page + 1,
    total = total,
)
```

Every image we get as a result of Unsplash needs to be translated into an object that is expected by the asset source API.
We will describe every mandatory and optional property in the following paragraphs.

```kotlin highlight-translateToAssetResult
private fun JSONObject.toAsset() = Asset(
    id = getString("id"),
    locale = "en",
    label = when {
        !isNull("description") -> getString("description")
        !isNull("alt_description") -> getString("alt_description")
        else -> null
    },
    tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
        (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
    }?.takeIf { it.isNotEmpty() },
    meta = mapOf(
        "uri" to getJSONObject("urls").getString("full"),
        "thumbUri" to getJSONObject("urls").getString("thumb"),
        "blockType" to DesignBlockType.Graphic.key,
        "fillType" to FillType.Image.key,
        "shapeType" to ShapeType.Rect.key,
        "kind" to "image",
        "width" to getInt("width").toString(),
        "height" to getInt("height").toString(),
    ),
    context = AssetContext(sourceId = "unsplash"),
    credits = AssetCredits(
        name = getJSONObject("user").getString("name"),
        uri = getJSONObject("user")
            .takeIf { it.has("links") }
            ?.getJSONObject("links")
            ?.getString("html")
            ?.let { Uri.parse(it) },
    ),
    utm = AssetUTM(source = "CE.SDK Demo", medium = "referral"),
)
```

`id`: The id of the asset (mandatory).
This has to be unique for this source configuration.

```kotlin highlight-result-id
id = getString("id"),
```

`locale` (optional): The language locale for this asset is used in `label` and `tags`.

```kotlin highlight-result-locale
locale = "en",
```

`label` (optional): The label of this asset.
It could be displayed in the tooltip as well as in the credits of the asset.

```kotlin highlight-result-label
label = when {
    !isNull("description") -> getString("description")
    !isNull("alt_description") -> getString("alt_description")
    else -> null
},
```

`tags` (optional): The tags of this asset.
It could be displayed in the credits of the asset.

```kotlin highlight-result-tags
tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
    (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
}?.takeIf { it.isNotEmpty() },
```

`meta`: The meta object stores asset properties that depend on the specific asset type.

```kotlin highlight-result-meta
meta = mapOf(
    "uri" to getJSONObject("urls").getString("full"),
    "thumbUri" to getJSONObject("urls").getString("thumb"),
    "blockType" to DesignBlockType.Graphic.key,
    "fillType" to FillType.Image.key,
    "shapeType" to ShapeType.Rect.key,
    "kind" to "image",
    "width" to getInt("width").toString(),
    "height" to getInt("height").toString(),
),
```

`uri`: For an image asset this is the URL to the image file that will be used to add the image to the scene.

Note that we have to use the Unsplash API to obtain a usable URL at first.

```kotlin highlight-result-uri
"uri" to getJSONObject("urls").getString("full"),
```

`thumbUri`: The URI of the asset's thumbnail.
It could be used in an asset library.

```kotlin highlight-result-thumbUri
"thumbUri" to getJSONObject("urls").getString("thumb"),
```

`blockType`: The type id of the design block that should be created when this asset is applied to the scene.

If omitted, CE.SDK will try to infer the block type from an optionally provided `mimeType` property (e.g. `image/jpeg`) or by loading the asset data behind `uri` and parsing the mime type from that. However, this will cause a delay before the asset can be added to the scene, which is why it is always recommended to specify the `blockType` upfront.

```kotlin highlight-result-blockType
"blockType" to DesignBlockType.Graphic.key,
```

`fillType`: The type id of the fill that should be attached to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to a solid color fill `//ly.img.ubq/fill/color`.

```kotlin highlight-result-fillType
"fillType" to FillType.Image.key,
```

`shapeType`: The type id of the shape that should be attached to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to a rect shape `//ly.img.ubq/shape/rect`.

```kotlin highlight-result-shapeType
"shapeType" to ShapeType.Rect.key,
```

`kind`: The kind that should be set to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to an empty string.

```kotlin highlight-result-kind
"kind" to "image",
```

`width`: The original width of the image.

`height`: The original height of the image.

```kotlin highlight-result-size
"width" to getInt("width").toString(),
"height" to getInt("height").toString(),
```

`looping`: Determines whether the asset allows looping (applicable only to Video and GIF). When set to `true`, the asset can extend beyond its original length by looping for the specified duration.

`context`: Adds contextual information to the asset.
Right now, this only includes the source id of the source configuration.

```kotlin highlight-result-context
context = AssetContext(sourceId = "unsplash"),
```

`credits` (optional): Some image providers require to display credits to the asset's artist.
If set, it has to be an object with the artist's `name` and a `url` to the artist page.

```kotlin highlight-result-credits
credits = AssetCredits(
    name = getJSONObject("user").getString("name"),
    uri = getJSONObject("user")
        .takeIf { it.has("links") }
        ?.getJSONObject("links")
        ?.getString("html")
        ?.let { Uri.parse(it) },
),
```

`utm` (optional): Some image providers require to add UTM parameters to all links to the source or the artist.
If set, it contains a string to the `source` (added as `utm_source`) and the `medium` (added as `utm_medium`)

```kotlin highlight-result-utm
utm = AssetUTM(source = "CE.SDK Demo", medium = "referral"),
```

After translating the asset to match the interface from the asset source API, the array of assets for the current page can be returned.

Going further with our Unsplash integration we need to handle the case when no query was provided.
Unsplash requires us to call a different API endpoint (`/photos`) with slightly different parameters but the basics are the same.
We need to check for success, calculate `total` and `nextPage` and translate the assets.

```kotlin highlight-unsplash-list
val search = runCatching {
    engine.asset.findAssets(
        sourceId = "ly.img.asset.source.unsplash",
        query = FindAssetsQuery(query = "banana", page = 1, perPage = 10),
    )
}.getOrElse { it.printStackTrace() }
```

In addition to `findAssets`, there are couple more methods that need to be implemented.
We have already seen that an asset can define credits for the artist.
Depending on the image provider you might need to add credits and the license for the source.
In case of Unsplash, this includes a link as well as the license of all assets from this source.

```kotlin highlight-unsplash-credits-license
    override val credits = AssetCredits(
        name = "Unsplash",
        uri = Uri.parse("https://unsplash.com/"),
    )

    override val license = AssetLicense(
        name = "Unsplash license (free)",
        uri = Uri.parse("https://unsplash.com/license"),
    )
```

## Local Asset Sources

In many cases, you already have various finite sets of assets that you want to make available via asset sources.
In order to save you the effort of having to implement custom asset query callbacks for each of these asset sources,
CE.SDK also allows you to create "local" asset sources, which are managed by the engine and provide search and
pagination functionalities.

In order to add such a local asset source, simply call the `addLocalSource` API and choose a unique id with which you
can later access the asset source.

```kotlin highlight-add-local-source
engine.asset.addLocalSource(
    sourceId = "background-videos",
    supportedMimeTypes = listOf("video/mp4"),
)
```

The `fun addAsset(sourceId: String, asset: AssetDefinition)` API allows you to add new asset instances to your local asset source. The local asset source then
keeps track of these assets and returns matching items as the result of asset queries. Asset queries return the
assets in the same order in which they were inserted into the local asset source.

Note that the `AssetDefinition` type that we pass to the `addAsset` API is slightly different than
the `Asset` type which is returned by asset queries. The `AssetDefinition` for example contains all localizations
of the labels and tags of the same asset whereas the `Asset` is specific to the locale property of the query.

```kotlin highlight-add-asset-to-source
val asset = AssetDefinition(
    id = "ocean-waves-1",
    label = mapOf(
        "en" to "relaxing ocean waves",
        "es" to "olas del mar relajantes",
    ),
    tags = mapOf(
        "en" to listOf("ocean", "waves", "soothing", "slow"),
        "es" to listOf("mar", "olas", "calmante", "lento"),
    ),
    meta = mapOf(
        "uri" to "https://example.com/ocean-waves-1.mp4",
        "thumbUri" to "https://example.com/thumbnails/ocean-waves-1.jpg",
        "mimeType" to "video/mp4",
        "width" to "1920",
        "height" to "1080",
    ),
    payload = AssetPayload(color = AssetColor.RGB(r = 0F, g = 0F, b = 1F)),
)
engine.asset.addAsset(sourceId = "background-videos", asset = asset)
```

## Full Code

Here's the full code:

```kotlin
import android.net.Uri
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import ly.img.engine.Asset
import ly.img.engine.AssetColor
import ly.img.engine.AssetContext
import ly.img.engine.AssetCredits
import ly.img.engine.AssetDefinition
import ly.img.engine.AssetLicense
import ly.img.engine.AssetPayload
import ly.img.engine.AssetSource
import ly.img.engine.AssetUTM
import ly.img.engine.DesignBlockType
import ly.img.engine.Engine
import ly.img.engine.FillType
import ly.img.engine.FindAssetsQuery
import ly.img.engine.FindAssetsResult
import ly.img.engine.ShapeType
import org.json.JSONArray
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

fun customAssetSource(
    license: String,
    userId: String,
    unsplashBaseUrl: String,
) = CoroutineScope(
    Dispatchers.Main,
).launch {
    val engine = Engine.getInstance(id = "ly.img.engine.example")
    engine.start(license = license, userId = userId)
    engine.bindOffscreen(width = 100, height = 100)

    val source = UnsplashAssetSource(unsplashBaseUrl) // INSERT YOUR UNSPLASH PROXY URL HERE
    engine.asset.addSource(source)

    val list = runCatching {
        engine.asset.findAssets(
            sourceId = "ly.img.asset.source.unsplash",
            query = FindAssetsQuery(query = "", page = 1, perPage = 10),
        )
    }.getOrElse { it.printStackTrace() }

    val search = runCatching {
        engine.asset.findAssets(
            sourceId = "ly.img.asset.source.unsplash",
            query = FindAssetsQuery(query = "banana", page = 1, perPage = 10),
        )
    }.getOrElse { it.printStackTrace() }

    engine.asset.addLocalSource(
        sourceId = "background-videos",
        supportedMimeTypes = listOf("video/mp4"),
    )
    val asset = AssetDefinition(
        id = "ocean-waves-1",
        label = mapOf(
            "en" to "relaxing ocean waves",
            "es" to "olas del mar relajantes",
        ),
        tags = mapOf(
            "en" to listOf("ocean", "waves", "soothing", "slow"),
            "es" to listOf("mar", "olas", "calmante", "lento"),
        ),
        meta = mapOf(
            "uri" to "https://example.com/ocean-waves-1.mp4",
            "thumbUri" to "https://example.com/thumbnails/ocean-waves-1.jpg",
            "mimeType" to "video/mp4",
            "width" to "1920",
            "height" to "1080",
        ),
        payload = AssetPayload(color = AssetColor.RGB(r = 0F, g = 0F, b = 1F)),
    )
    engine.asset.addAsset(sourceId = "background-videos", asset = asset)

    engine.stop()
}

class UnsplashAssetSource(
    private val baseUrl: String,
) : AssetSource(sourceId = "ly.img.asset.source.unsplash") {

    override suspend fun getGroups(): List<String>? = null

    override val supportedMimeTypes = listOf("image/jpeg")

    override val credits = AssetCredits(
        name = "Unsplash",
        uri = Uri.parse("https://unsplash.com/"),
    )

    override val license = AssetLicense(
        name = "Unsplash license (free)",
        uri = Uri.parse("https://unsplash.com/license"),
    )

    override suspend fun findAssets(query: FindAssetsQuery): FindAssetsResult = withContext(Dispatchers.IO) {
        if (query.query.isNullOrEmpty()) query.getPopularList() else query.getSearchList()
    }

    private suspend fun FindAssetsQuery.getPopularList(): FindAssetsResult {
        val queryParams = listOf(
            "order_by" to "popular",
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val assetsArray = getResponseAsString("$baseUrl/photos?$queryParams").let(::JSONArray)
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = page + 1,
            total = Int.MAX_VALUE,
        )
    }

    private suspend fun FindAssetsQuery.getSearchList(): FindAssetsResult {
        val queryParams = listOf(
            "query" to query,
            "page" to page + 1,
            "per_page" to perPage,
        ).joinToString(separator = "&") { (key, value) -> "$key=$value" }
        val response = getResponseAsString("$baseUrl/search/photos?$queryParams").let(::JSONObject)
        val assetsArray = response.getJSONArray("results")
        val total = response.getInt("total")
        val totalPages = response.getInt("total_pages")
        return FindAssetsResult(
            assets = (0 until assetsArray.length()).map { assetsArray.getJSONObject(it).toAsset() },
            currentPage = page,
            nextPage = if (page == totalPages) -1 else page + 1,
            total = total,
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
            !isNull("description") -> getString("description")
            !isNull("alt_description") -> getString("alt_description")
            else -> null
        },
        tags = takeIf { has("tags") }?.let { getJSONArray("tags") }?.let {
            (0 until it.length()).map { index -> it.getJSONObject(index).getString("title") }
        }?.takeIf { it.isNotEmpty() },
        meta = mapOf(
            "uri" to getJSONObject("urls").getString("full"),
            "thumbUri" to getJSONObject("urls").getString("thumb"),
            "blockType" to DesignBlockType.Graphic.key,
            "fillType" to FillType.Image.key,
            "shapeType" to ShapeType.Rect.key,
            "kind" to "image",
            "width" to getInt("width").toString(),
            "height" to getInt("height").toString(),
        ),
        context = AssetContext(sourceId = "unsplash"),
        credits = AssetCredits(
            name = getJSONObject("user").getString("name"),
            uri = getJSONObject("user")
                .takeIf { it.has("links") }
                ?.getJSONObject("links")
                ?.getString("html")
                ?.let { Uri.parse(it) },
        ),
        utm = AssetUTM(source = "CE.SDK Demo", medium = "referral"),
    )
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
