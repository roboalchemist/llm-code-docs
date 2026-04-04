# Source: https://img.ly/docs/cesdk/macos/import-media/from-remote-source/unsplash-8f31f0/

---
title: "From A Custom Source"
description: "Browse and import royalty-free images from Unsplash into the editor."
platform: macos
url: "https://img.ly/docs/cesdk/macos/import-media/from-remote-source/unsplash-8f31f0/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/macos/import-media-4e3703/) > [Import From Remote Source](https://img.ly/docs/cesdk/macos/import-media/from-remote-source-b65faf/) > [From a Custom Source](https://img.ly/docs/cesdk/macos/import-media/from-remote-source/unsplash-8f31f0/)

---

```swift file=@cesdk_swift_examples/engine-guides-custom-asset-source/CustomAssetSource.swift reference-only
import Foundation
import IMGLYEngine

@MainActor
func customAssetSource(engine: Engine) async throws {
  let source = UnsplashAssetSource(host: secrets.unsplashHost)
  try engine.asset.addSource(source)

  let list = try await engine.asset.findAssets(
    sourceID: "ly.img.asset.source.unsplash",
    query: .init(query: "", page: 1, perPage: 10),
  )
  let search = try await engine.asset.findAssets(
    sourceID: "ly.img.asset.source.unsplash",
    query: .init(query: "banana", page: 1, perPage: 10),
  )

  try engine.asset.addLocalSource(sourceID: "background-videos")

  let asset = AssetDefinition(id: "ocean-waves-1",
                              meta: [
                                "uri": "https://example.com/ocean-waves-1.mp4",
                                "thumbUri": "https://example.com/thumbnails/ocean-waves-1.jpg",
                                "mimeType": "video/mp4",
                                "width": "1920",
                                "height": "1080",
                              ],
                              label: [
                                "en": "relaxing ocean waves",
                                "es": "olas del mar relajantes",
                              ],
                              tags: [
                                "en": ["ocean", "waves", "soothing", "slow"],
                                "es": ["mar", "olas", "calmante", "lento"],
                              ])
  try engine.asset.addAsset(to: "background-videos", asset: asset)
}
```

```swift file=@cesdk_swift_examples/third-party/UnsplashAssetSource.swift reference-only
import Foundation
import IMGLYEngine

public final class UnsplashAssetSource: NSObject {
  private lazy var decoder: JSONDecoder = {
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    return decoder
  }()

  private let host: String
  private let path: String

  public init(host: String, path: String = "/unsplashProxy") {
    self.host = host
    self.path = path
  }

  private struct Endpoint {
    let path: String
    let query: [URLQueryItem]

    static func search(queryData: AssetQueryData) -> Self {
      Endpoint(
        path: "/search/photos",
        query: [
          .init(name: "query", value: queryData.query),
          .init(name: "page", value: String(queryData.page + 1)),
          .init(name: "per_page", value: String(queryData.perPage)),
          .init(name: "content_filter", value: "high"),
        ],
      )
    }

    static func list(queryData: AssetQueryData) -> Self {
      Endpoint(
        path: "/photos",
        query: [
          .init(name: "order_by", value: "popular"),
          .init(name: "page", value: String(queryData.page + 1)),
          .init(name: "per_page", value: String(queryData.perPage)),
          .init(name: "content_filter", value: "high"),
        ],
      )
    }

    func url(with host: String, path: String) -> URL? {
      var components = URLComponents()
      components.scheme = "https"
      components.host = host
      components.path = path + self.path
      components.queryItems = query
      return components.url
    }
  }
}

extension UnsplashAssetSource: AssetSource {
  public static let id = "ly.img.asset.source.unsplash"

  public var id: String {
    Self.id
  }

  public func findAssets(queryData: AssetQueryData) async throws -> AssetQueryResult {
    let endpoint: Endpoint = queryData.query?
      .isEmpty ?? true ? .list(queryData: queryData) : .search(queryData: queryData)

    let data = try await URLSession.shared.data(from: endpoint.url(with: host, path: path)!).0

    if queryData.query?.isEmpty ?? true {
      let response = try decoder.decode(UnsplashListResponse.self, from: data)
      let nextPage = queryData.page + 1

      return .init(
        assets: response.map(AssetResult.init),
        currentPage: queryData.page,
        nextPage: nextPage,
        total: -1,
      )
    } else {
      let response = try decoder.decode(UnsplashSearchResponse.self, from: data)
      let (results, total, totalPages) = (response.results, response.total ?? 0, response.totalPages ?? 0)
      let nextPage = (queryData.page + 1) == totalPages ? -1 : queryData.page + 1

      return .init(
        assets: results.map(AssetResult.init),
        currentPage: queryData.page,
        nextPage: nextPage,
        total: total,
      )
    }
  }

  public var supportedMIMETypes: [String]? {
    [MIMEType.jpeg.rawValue]
  }

  public var credits: AssetCredits? {
    .init(
      name: "Unsplash",
      url: URL(string: "https://unsplash.com/")!,
    )
  }

  public var license: AssetLicense? {
    .init(
      name: "Unsplash license (free)",
      url: URL(string: "https://unsplash.com/license")!,
    )
  }
}

private extension AssetResult {
  convenience init(image: UnsplashImage) {
    self.init(
      id: image.id,
      locale: "en",
      label: image.description ?? image.altDescription,
      tags: image.tags?.compactMap(\.title),
      meta: [
        "uri": image.urls.full.absoluteString,
        "thumbUri": image.urls.thumb.absoluteString,
        "blockType": DesignBlockType.graphic.rawValue,
        "fillType": FillType.image.rawValue,
        "shapeType": ShapeType.rect.rawValue,
        "kind": "image",
        "width": String(image.width),
        "height": String(image.height),
        "looping": "false",
      ],
      context: .init(sourceID: "unsplash"),
      credits: .init(name: image.user.name!, url: image.user.links?.html),
      utm: .init(source: "CE.SDK Demo", medium: "referral"),
    )
  }
}
```

```swift file=@cesdk_swift_examples/third-party/UnsplashResponse.swift reference-only
import Foundation

// MARK: - UnsplashResponse

struct UnsplashSearchResponse: Decodable {
  let total, totalPages: Int?
  let results: [UnsplashImage]
}

typealias UnsplashListResponse = [UnsplashImage]

// MARK: - Result

struct UnsplashImage: Decodable {
  let id: String
  let createdAt, updatedAt: String
  let promotedAt: String?
  let width, height: Int
  let color, blurHash: String?
  let description: String?
  let altDescription: String?
  let urls: Urls
  let likes: Int?
  let likedByUser: Bool?
  let user: User
  let tags: [Tag]?
}

// MARK: - Tag

struct Tag: Decodable {
  let type, title: String?
}

// MARK: - Urls

struct Urls: Decodable {
  let raw, full, regular, small: URL
  let thumb, smallS3: URL
}

// MARK: - User

struct User: Decodable {
  let id: String
  let updatedAt: String

  let username, name, firstName: String?
  let lastName, twitterUsername: String?
  let portfolioURL: String?
  let bio, location: String?
  let links: UserLinks?
  let instagramUsername: String?
  let totalCollections, totalLikes, totalPhotos: Int?
  let acceptedTos, forHire: Bool?
}

// MARK: - UserLinks

struct UserLinks: Decodable {
  let linksSelf, html, photos, likes: URL?
  let portfolio, following, followers: URL?
}
```

In this example, we will show you how to integrate your custom asset sources into [CE.SDK](https://img.ly/products/creative-sdk).

With CE.SDK you can directly add external image providers like Unsplash or your own backend.
A third option we will explore in this guide is using the engine's Asset API directly.
Follow along with this example while we are going to add the Unsplash library.

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/engine-guides-custom-asset-source/CustomAssetSource.swift).

Adding an asset source is done creating an asset source definition and adding it using `func addSource(_ source: AssetSource) throws`.
The asset source needs a unique identifier as part of an object implementing the interface of the source.
All Asset API methods require the asset source's unique identifier.

```swift highlight-unsplash-definition
let source = UnsplashAssetSource(host: secrets.unsplashHost)
try engine.asset.addSource(source)
```

The most important function to implement is `func findAssets(sourceID: String, query: AssetQueryData) async throws -> AssetQueryResult`.
With this function alone you can define the complete asset source.
It receives the asset query as an argument and returns a promise with the results.

- The argument is the `queryData` and describes the slice of data the engine wants to use.
  This includes a query string and pagination information.
- The result of this query, besides the actual asset data, returns information like the current page, the next page and the total number of assets available for this specific query.

Providing an `async` function gives us great flexibility since we are completely agnostic of how we want to get the assets.
We can use `URLSession`, local storage, cache or import a 3rd party library to return the result.

```swift highlight-unsplash-findAssets
let list = try await engine.asset.findAssets(
  sourceID: "ly.img.asset.source.unsplash",
  query: .init(query: "", page: 1, perPage: 10),
)
```

Let us implement an Unsplash asset source.
Please note that this is just for demonstration purposes only and may not be ideal if you want to integrate Unsplash in your production environment.

We will create a class integrating two Unsplash REST endpoints. The setup part only contains endpoint definition, as well as JSON decoder.
According to their documentation and guidelines, we have to create an access key and use a proxy to query the API, but this is out of scope for this example. Take a look at Unsplash's documentation for further details.

```swift highlight-unsplash-api-creation
public final class UnsplashAssetSource: NSObject {
  private lazy var decoder: JSONDecoder = {
    let decoder = JSONDecoder()
    decoder.keyDecodingStrategy = .convertFromSnakeCase
    return decoder
  }()

  private let host: String
  private let path: String

  public init(host: String, path: String = "/unsplashProxy") {
    self.host = host
    self.path = path
  }

  private struct Endpoint {
    let path: String
    let query: [URLQueryItem]

    static func search(queryData: AssetQueryData) -> Self {
      Endpoint(
        path: "/search/photos",
        query: [
          .init(name: "query", value: queryData.query),
          .init(name: "page", value: String(queryData.page + 1)),
          .init(name: "per_page", value: String(queryData.perPage)),
          .init(name: "content_filter", value: "high"),
        ],
      )
    }

    static func list(queryData: AssetQueryData) -> Self {
      Endpoint(
        path: "/photos",
        query: [
          .init(name: "order_by", value: "popular"),
          .init(name: "page", value: String(queryData.page + 1)),
          .init(name: "per_page", value: String(queryData.perPage)),
          .init(name: "content_filter", value: "high"),
        ],
      )
    }

    func url(with host: String, path: String) -> URL? {
      var components = URLComponents()
      components.scheme = "https"
      components.host = host
      components.path = path + self.path
      components.queryItems = query
      return components.url
    }
  }
}
```

Unsplash has different API endpoints for different use cases.
If we want to search we need to call a different endpoint as if we just want to display images without any search term.

Therefore we need to check if the query data contains a `query` string. If `findAssets` was called with a non-empty `query` we can call the `/search` endpoint. As we can see in the example, we are passing the `queryData` to this method, containing the following fields:

- `queryData.query`: The current search string from the search bar in the asset library.
- `queryData.page`: For Unsplash specifically the requested page number starts with 1.
  We do not query all assets at once but by pages.
  As the user scrolls down more pages will be requested by calls to the `findAssets` method.
- `queryData.perPage`: Determines how many assets we want to have included per page.
  This might change between calls.
  For instance, `perPage` can be called with a small number to display a small preview, but with a higher number e.g. if we want to show more assets in a grid view.

```swift highlight-unsplash-query
let endpoint: Endpoint = queryData.query?
  .isEmpty ?? true ? .list(queryData: queryData) : .search(queryData: queryData)
```

Once we receive the response and check for success we need to map Unsplash's result to what the asset source API needs as a result. The CE.SDK expects an object with the following properties:

- `assets`: An array of assets for the current query. We will take a look at what these have to look like in the next paragraph.
- `total`: The total number of assets available for the current query. If we search for "Cat" with `perPage` set to 30, we will get 30 assets, but `total` likely will be a much higher number.
- `currentPage`: Return the current page that was requested.
- `nextPage`: This is the next page that can be requested after the current one. Should be `undefined` if there is no other page (no more assets). In this case we stop querying for more even if the user has scrolled to the bottom.

```swift highlight-unsplash-result-mapping
    if queryData.query?.isEmpty ?? true {
      let response = try decoder.decode(UnsplashListResponse.self, from: data)
      let nextPage = queryData.page + 1

      return .init(
        assets: response.map(AssetResult.init),
        currentPage: queryData.page,
        nextPage: nextPage,
        total: -1,
      )
    } else {
      let response = try decoder.decode(UnsplashSearchResponse.self, from: data)
      let (results, total, totalPages) = (response.results, response.total ?? 0, response.totalPages ?? 0)
      let nextPage = (queryData.page + 1) == totalPages ? -1 : queryData.page + 1

      return .init(
        assets: results.map(AssetResult.init),
        currentPage: queryData.page,
        nextPage: nextPage,
        total: total,
      )
    }
```

Every image we get as a result of Unsplash needs to be translated into an object that is expected by the asset source API.
We will describe every mandatory and optional property in the following paragraphs.

```swift highlight-translateToAssetResult
convenience init(image: UnsplashImage) {
  self.init(
    id: image.id,
    locale: "en",
    label: image.description ?? image.altDescription,
    tags: image.tags?.compactMap(\.title),
    meta: [
      "uri": image.urls.full.absoluteString,
      "thumbUri": image.urls.thumb.absoluteString,
      "blockType": DesignBlockType.graphic.rawValue,
      "fillType": FillType.image.rawValue,
      "shapeType": ShapeType.rect.rawValue,
      "kind": "image",
      "width": String(image.width),
      "height": String(image.height),
      "looping": "false",
    ],
    context: .init(sourceID: "unsplash"),
    credits: .init(name: image.user.name!, url: image.user.links?.html),
    utm: .init(source: "CE.SDK Demo", medium: "referral"),
  )
}
```

`id`: The id of the asset (mandatory).
This has to be unique for this source configuration.

```swift highlight-result-id
id: image.id,
```

`locale` (optional): The language locale for this asset is used in `label` and `tags`.

```swift highlight-result-locale
locale: "en",
```

`label` (optional): The label of this asset.
It could be displayed in the tooltip as well as in the credits of the asset.

```swift highlight-result-label
label: image.description ?? image.altDescription,
```

`tags` (optional): The tags of this asset.
It could be displayed in the credits of the asset.

```swift highlight-result-tags
tags: image.tags?.compactMap(\.title),
```

`meta`: The meta object stores asset properties that depend on the specific asset type.

```swift highlight-result-meta
meta: [
  "uri": image.urls.full.absoluteString,
  "thumbUri": image.urls.thumb.absoluteString,
  "blockType": DesignBlockType.graphic.rawValue,
  "fillType": FillType.image.rawValue,
  "shapeType": ShapeType.rect.rawValue,
  "kind": "image",
  "width": String(image.width),
  "height": String(image.height),
  "looping": "false",
],
```

`uri`: For an image asset this is the URL to the image file that will be used to add the image to the scene.

Note that we have to use the Unsplash API to obtain a usable URL at first.

```swift highlight-result-uri
"uri": image.urls.full.absoluteString,
```

`thumbUri`: The URI of the asset's thumbnail.
It could be used in an asset library.

```swift highlight-result-thumbUri
"thumbUri": image.urls.thumb.absoluteString,
```

`blockType`: The type id of the design block that should be created when this asset is applied to the scene.

If omitted, CE.SDK will try to infer the block type from an optionally provided `mimeType` property (e.g. `image/jpeg`) or by loading the asset data behind `uri` and parsing the mime type from that. However, this will cause a delay before the asset can be added to the scene, which is why it is always recommended to specify the `blockType` upfront.

```swift highlight-result-blockType
"blockType": DesignBlockType.graphic.rawValue,
```

`fillType`: The type id of the fill that should be attached to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to a solid color fill `//ly.img.ubq/fill/color`.

```swift highlight-result-fillType
"fillType": FillType.image.rawValue,
```

`shapeType`: The type id of the shape that should be attached to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to a rect shape `//ly.img.ubq/shape/rect`.

```swift highlight-result-shapeType
"shapeType": ShapeType.rect.rawValue,
```

`kind`: The kind that should be set to the block when this asset is applied to the scene.

If omitted, CE.SDK will default to an empty string.

```swift highlight-result-kind
"kind": "image",
```

`width`: The original width of the image.

`height`: The original height of the image.

```swift highlight-result-size
"width": String(image.width),
"height": String(image.height),
```

`looping`: Determines whether the asset allows looping (applicable only to Video and GIF). When set to `true`, the asset can extend beyond its original length by looping for the specified duration.

```swift highlight-result-looping
"looping": "false",
```

`context`: Adds contextual information to the asset.
Right now, this only includes the source id of the source configuration.

```swift highlight-result-context
context: .init(sourceID: "unsplash"),
```

`credits` (optional): Some image providers require to display credits to the asset's artist.
If set, it has to be an object with the artist's `name` and a `url` to the artist page.

```swift highlight-result-credits
credits: .init(name: image.user.name!, url: image.user.links?.html),
```

`utm` (optional): Some image providers require to add UTM parameters to all links to the source or the artist.
If set, it contains a string to the `source` (added as `utm_source`) and the `medium` (added as `utm_medium`)

```swift highlight-result-utm
utm: .init(source: "CE.SDK Demo", medium: "referral"),
```

After translating the asset to match the interface from the asset source API, the array of assets for the current page can be returned.

Going further with our Unsplash integration we need to handle the case when no query was provided.
Unsplash requires us to call a different API endpoint (`/photos`) with slightly different parameters but the basics are the same.
We need to check for success, calculate `total` and `nextPage` and translate the assets.

```swift highlight-unsplash-list
let search = try await engine.asset.findAssets(
  sourceID: "ly.img.asset.source.unsplash",
  query: .init(query: "banana", page: 1, perPage: 10),
)
```

We have already seen that an asset can define credits for the artist.
Depending on the image provider you might need to add credits and the license for the source.
In case of Unsplash, this includes a link as well as the license of all assets from this source.

```swift highlight-unsplash-credits-license
  public var credits: AssetCredits? {
    .init(
      name: "Unsplash",
      url: URL(string: "https://unsplash.com/")!,
    )
  }

  public var license: AssetLicense? {
    .init(
      name: "Unsplash license (free)",
      url: URL(string: "https://unsplash.com/license")!,
    )
  }
```

## Local Asset Sources

In many cases, you already have various finite sets of assets that you want to make available via asset sources.
In order to save you the effort of having to implement custom asset query callbacks for each of these asset sources,
CE.SDK also allows you to create "local" asset sources, which are managed by the engine and provide search and
pagination functionalities.

In order to add such a local asset source, simply call the `addLocalSource` API and choose a unique id with which you
can later access the asset source.

```swift highlight-add-local-source
try engine.asset.addLocalSource(sourceID: "background-videos")
```

The `addAsset(to: String, asset: AssetDefinition)` API allows you to add new asset instances to your local asset source. The local asset source then
keeps track of these assets and returns matching items as the result of asset queries. Asset queries return the
assets in the same order in which they were inserted into the local asset source.

Note that the `AssetDefinition` type that we pass to the `addAsset` API is slightly different than
the `AssetResult` type which is returned by asset queries. The `AssetDefinition` for example contains all localizations
of the labels and tags of the same asset whereas the `AssetResult` is specific to the locale property of the query.

```swift highlight-add-asset-to-source
let asset = AssetDefinition(id: "ocean-waves-1",
                            meta: [
                              "uri": "https://example.com/ocean-waves-1.mp4",
                              "thumbUri": "https://example.com/thumbnails/ocean-waves-1.jpg",
                              "mimeType": "video/mp4",
                              "width": "1920",
                              "height": "1080",
                            ],
                            label: [
                              "en": "relaxing ocean waves",
                              "es": "olas del mar relajantes",
                            ],
                            tags: [
                              "en": ["ocean", "waves", "soothing", "slow"],
                              "es": ["mar", "olas", "calmante", "lento"],
                            ])
try engine.asset.addAsset(to: "background-videos", asset: asset)
```

## Full Code

Explore a full code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/engine-guides-custom-asset-source/CustomAssetSource.swift).



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
