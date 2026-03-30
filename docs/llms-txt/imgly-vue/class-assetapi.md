# Class: AssetAPI

Manage asset sources and apply assets to scenes.

Asset sources provide assets like images, videos, fonts, and other media that can be applied to design blocks. This API allows registering custom asset sources, querying available assets, and applying them to scenes or specific blocks. It supports both local and remote asset sources, with extensible middleware for custom asset handling.

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`AssetAPI`

## Event Subscriptions[#](#event-subscriptions)

Subscribe to asset source changes and lifecycle events.

### onAssetSourceAdded()[#](#onassetsourceadded)

  

Subscribe to asset source addition events.

```
engine.asset.onAssetSourceAdded((sourceID) => {  console.log(`Added source: ${sourceID}`);});
```

#### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`sourceID`) => `void` | The function called whenever an asset source is added. |

#### Returns[#](#returns)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-1)

`void`

* * *

### onAssetSourceRemoved()[#](#onassetsourceremoved)

  

Subscribe to asset source removal events.

```
engine.asset.onAssetSourceRemoved((sourceID) => {  console.log(`Removed source: ${sourceID}`);});
```

#### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`sourceID`) => `void` | The function called whenever an asset source is removed. |

#### Returns[#](#returns-2)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-3)

`void`

* * *

### onAssetSourceUpdated()[#](#onassetsourceupdated)

  

Subscribe to asset source content change events.

```
engine.asset.onAssetSourceUpdated((sourceID) => {  console.log(`Updated source: ${sourceID}`);});
```

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `callback` | (`sourceID`) => `void` | The function called whenever an asset source’s contents are updated. |

#### Returns[#](#returns-4)

A method to unsubscribe from the event.

```
(): void;
```

##### Returns[#](#returns-5)

`void`

## Asset Source Management[#](#asset-source-management)

Register, remove, and query asset sources for different types of media.

### addSource()[#](#addsource)

  

Add a custom asset source with unique ID.

The asset source provides methods for finding assets, applying them to scenes or blocks, and managing asset lifecycle. All source operations are handled asynchronously.

```
engine.asset.addSource({  id: 'foobar',  async findAssets(queryData) {    return Promise.resolve({      assets: [        {          id: 'logo',          meta: {            uri: 'https://img.ly/static/ubq_samples/imgly_logo.jpg',          }        }      ],      total: 1,      currentPage: queryData.page,      nextPage: undefined    });  },});
```

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `source` | [`AssetSource`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetsource/) | The asset source configuration. |

#### Returns[#](#returns-6)

`void`

#### Signature[#](#signature)

```
addSource(source: AssetSource): void
```

* * *

### addLocalSource()[#](#addlocalsource)

  

Add a local asset source.

Local asset sources allow dynamic asset management through the add/remove methods. You can specify supported MIME types to restrict what assets can be added.

```
engine.asset.addLocalSource('local-source');
```

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique identifier for the asset source. |
| `supportedMimeTypes?` | `string`\[\] | The mime types of assets that are allowed to be added to this local source. |
| `applyAsset?` | (`asset`) => `Promise`<`number`\> | An optional callback that can be used to override the default behavior of applying a given asset result to the active scene. |
| `applyAssetToBlock?` | (`asset`, `block`) => `Promise`<`void`\> | An optional callback that can be used to override the default behavior of applying an asset result to a given block. |

#### Returns[#](#returns-7)

`void`

#### Signature[#](#signature-1)

```
addLocalSource(id: string, supportedMimeTypes?: string[], applyAsset?: (asset: CompleteAssetResult) => Promise<number>, applyAssetToBlock?: (asset: CompleteAssetResult, block: number) => Promise<void>): void
```

* * *

### addLocalAssetSourceFromJSONString()[#](#addlocalassetsourcefromjsonstring)

  

Creates a new local asset source from a JSON string containing asset definitions.

The JSON structure should contain a `version` field, an `id` field specifying the asset source identifier, and an `assets` array with asset definitions. Each asset should have an `id`, localized `label` object, and a `meta` object containing asset-specific properties like `uri`, `thumbUri`, `blockType`, etc.

Optionally, you can provide a `basePath` for resolving relative URLs and additional options including a `matcher` array to filter which assets are loaded based on their IDs. The matcher patterns support wildcard matching using `*`. If multiple patterns are provided, an asset is included if it matches ANY of the patterns.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `contentJSON` | `string` | The JSON string containing the asset definitions. |
| `basePath?` | `string` | An optional base path with which {{base\_url}} strings in the assets should be replaced. If no value is provided, settings.basePath is used. |
| `options?` | { `matcher?`: `string`\[\]; } | Optional configuration: - `matcher`: Array of patterns to filter assets by ID. Supports `*` wildcard. An asset is included if it matches ANY pattern. |
| `options.matcher?` | `string`\[\] | \- |

#### Returns[#](#returns-8)

`Promise`<`string`\>

The ID of the newly created asset source (as specified in the JSON’s `id` field).

#### Example[#](#example)

```
// Load all assets from JSONconst json = JSON.stringify({  "version": "2.0.0",  "id": "my.custom.assets",  "assets": [    {      "id": "sample_asset",      "label": { "en": "Sample Asset" },      "meta": {        "uri": "https://example.com/asset.jpg",        "thumbUri": "https://example.com/thumb.jpg",        "blockType": "//ly.img.ubq/image"      }    }  ]});const sourceId = await engine.asset.addLocalAssetSourceFromJSONString(json);console.log('Created asset source:', sourceId); // "my.custom.assets"
// Load with custom base pathconst sourceId2 = await engine.asset.addLocalAssetSourceFromJSONString(  json,  'https://example.com/');
// Load only assets matching one of the patternsconst sourceId3 = await engine.asset.addLocalAssetSourceFromJSONString(  json,  undefined,  { matcher: ['sample_*', '*_asset'] });
// Load with custom base path and matcherconst sourceId4 = await engine.asset.addLocalAssetSourceFromJSONString(  json,  'https://example.com/',  { matcher: ['portrait_*', 'landscape_*'] });
```

#### Signature[#](#signature-2)

```
addLocalAssetSourceFromJSONString(contentJSON: string, basePath?: string, options?: object): Promise<string>
```

* * *

### addLocalAssetSourceFromJSONURI()[#](#addlocalassetsourcefromjsonuri)

  

Creates a new local asset source from a JSON URI.

Loads and parses a JSON file from the specified URI to create an asset source. The JSON structure should contain a `version` field, an `id` field specifying the asset source identifier, and an `assets` array with asset definitions. The created asset source will have the ID specified in the JSON’s `id` field, and all assets defined in the JSON will be added to the source.

Note: The parent directory of the content.json URI will be used as the base path for resolving relative URLs in the asset definitions (e.g., `{{base_url}}` placeholders).

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `contentURI` | `string` | The URI for the JSON file to load and parse. |
| `options?` | { `matcher?`: `string`\[\]; } | Optional configuration: - `matcher`: Array of patterns to filter assets by ID. Supports `*` wildcard. An asset is included if it matches ANY pattern. |
| `options.matcher?` | `string`\[\] | \- |

#### Returns[#](#returns-9)

`Promise`<`string`\>

The ID of the newly created asset source (as specified in the JSON’s `id` field).

#### Example[#](#example-1)

```
// Load all audio assets from IMG.LY's CDNconst sourceId = await engine.asset.addLocalAssetSourceFromJSONURI(  'https://cdn.img.ly/assets/demo/v3/ly.img.audio/content.json');console.log('Loaded asset source:', sourceId); // "ly.img.audio"
// Load only assets matching one of the patternsconst sourceId2 = await engine.asset.addLocalAssetSourceFromJSONURI(  'https://cdn.img.ly/assets/demo/v3/ly.img.image/content.json',  { matcher: ['image-portrait-*', 'image-landscape-*'] });
```

#### Signature[#](#signature-3)

```
addLocalAssetSourceFromJSONURI(contentURI: string, options?: object): Promise<string>
```

* * *

### removeSource()[#](#removesource)

  

Remove a registered asset source.

This permanently removes the asset source and all its associated assets. Any ongoing operations with this source will be cancelled.

```
engine.asset.removeSource('asset-source-id');
```

#### Parameters[#](#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the asset source to remove. |

#### Returns[#](#returns-10)

`void`

#### Signature[#](#signature-4)

```
removeSource(id: string): void
```

* * *

### findAllSources()[#](#findallsources)

  

Get all registered asset source IDs.

```
engine.asset.findAllSources();
```

#### Returns[#](#returns-11)

`string`\[\]

A list with the IDs of all registered asset sources.

#### Signature[#](#signature-5)

```
findAllSources(): string[]
```

## Asset Discovery[#](#asset-discovery)

Search and filter assets from registered sources with advanced query options.

### findAssets()[#](#findassets)

  

Search for assets in a specific source with advanced filtering.

Supports pagination, text search, tag filtering, grouping, and sorting options. Results include asset metadata, thumbnails, and application context.

```
const result = await engine.asset.findAssets('asset-source-id', {  page: 0,  perPage: 100});const asset = result.assets[0];
```

#### Parameters[#](#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |
| `query` | [`AssetQueryData`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetquerydata/) | Query options to filter and sort the search results. |

#### Returns[#](#returns-12)

`Promise`<[`AssetsQueryResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetsqueryresult/)<[`CompleteAssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/completeassetresult/)\>>

Promise resolving to paginated search results.

#### Signature[#](#signature-6)

```
findAssets(sourceId: string, query: AssetQueryData): Promise<AssetsQueryResult<CompleteAssetResult>>
```

* * *

### fetchAsset()[#](#fetchasset)

  

Fetch a specific asset by ID from an asset source.

```
const asset = await engine.asset.fetchAsset('asset-source-id', 'asset-id', {  locale: 'en-US'});
```

#### Parameters[#](#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source to search in. |
| `assetId` | `string` | The ID of the asset to fetch. |
| `params?` | `Pick`<[`AssetQueryData`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetquerydata/), `"locale"`\> | Query parameters including locale (optional). |

#### Returns[#](#returns-13)

`Promise`<[`CompleteAssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/completeassetresult/)\>

Promise resolving to the complete asset result, or undefined if not found.

#### Signature[#](#signature-7)

```
fetchAsset(sourceId: string, assetId: string, params?: Pick<AssetQueryData, "locale">): Promise<CompleteAssetResult>
```

## Asset Information[#](#asset-information)

Retrieve metadata, credits, licenses, and supported formats from asset sources.

### getGroups()[#](#getgroups)

  

Get available asset groups from a source.

Groups provide categorization for assets within a source, enabling filtered discovery.

```
const groups = engine.asset.getGroups(customSource.id);
```

#### Parameters[#](#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of the asset source. |

#### Returns[#](#returns-14)

`Promise`<`string`\[\]>

Promise resolving to list of available group names.

#### Signature[#](#signature-8)

```
getGroups(id: string): Promise<string[]>
```

* * *

### getSupportedMimeTypes()[#](#getsupportedmimetypes)

  

Get supported MIME types for an asset source.

Returns the file types that can be added to this source. An empty result means all MIME types are supported.

```
const mimeTypes = engine.asset.getSupportedMimeTypes('asset-source-id');
```

#### Parameters[#](#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |

#### Returns[#](#returns-15)

`string`\[\]

Array of supported MIME type strings.

#### Signature[#](#signature-9)

```
getSupportedMimeTypes(sourceId: string): string[]
```

* * *

### getCredits()[#](#getcredits)

  

Get attribution credits for an asset source.

```
const credits = engine.asset.getCredits('asset-source-id');
```

#### Parameters[#](#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |

#### Returns[#](#returns-16)

`object`

The asset source’s credits info consisting of a name and an optional URL.

| Name | Type |
| --- | --- |
| `name` | `string` |
| `url` | `string` |

#### Signature[#](#signature-10)

```
getCredits(sourceId: string): object
```

* * *

### getLicense()[#](#getlicense)

  

Get license information for an asset source.

```
const license = engine.asset.getLicense('asset-source-id');
```

#### Parameters[#](#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |

#### Returns[#](#returns-17)

`object`

The asset source’s license info consisting of a name and an optional URL.

| Name | Type |
| --- | --- |
| `name` | `string` |
| `url` | `string` |

#### Signature[#](#signature-11)

```
getLicense(sourceId: string): object
```

* * *

### canManageAssets()[#](#canmanageassets)

  

Check if an asset source supports asset management.

Returns true if the source allows adding and removing assets dynamically, via ‘Add File’ and ‘Delete’ button on the UI. This is typically true for local asset sources and false for remote sources.

```
engine.asset.canManageAssets('asset-source-id');
```

#### Parameters[#](#parameters-14)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source to check. |

#### Returns[#](#returns-18)

`boolean`

True if the source supports asset management operations.

#### Signature[#](#signature-12)

```
canManageAssets(sourceId: string): boolean
```

## Asset Application[#](#asset-application)

Apply assets to scenes, blocks, or specific properties with customizable behavior.

### registerApplyMiddleware()[#](#registerapplymiddleware)

  

Register middleware that intercepts asset application to scenes.

The middleware function receives the source ID, asset result, the original apply function, and a context object containing options about how the asset should be applied. It can perform custom logic before, after, or instead of the default asset application.

#### Parameters[#](#parameters-15)

| Parameter | Type | Description |
| --- | --- | --- |
| `middleware` | (`sourceId`, `assetResult`, `apply`, `context`) => `Promise`<`number`\> | The middleware function that is called before applying the asset. |

#### Returns[#](#returns-19)

`VoidFunction`

A function that can be used to remove the middleware.

#### Example[#](#example-2)

```
engine.asset.registerApplyMiddleware(async (sourceId, assetResult, apply, context) => {  // Access context to determine placement intent  console.log('Clip type:', context.clipType); // 'clip', 'overlay', or undefined  console.log('Custom data:', context.myCustomField); // Access custom fields
  // do something before applying the asset  // You still have the choice to call apply or skip it  const blockId = await apply(sourceId, assetResult);  // do something after applying the asset  return blockId;})
```

#### Signature[#](#signature-13)

```
registerApplyMiddleware(middleware: (sourceId: string, assetResult: AssetResult, apply: (sourceId: string, assetResult: AssetResult, options: ApplyAssetOptions) => Promise<number>, context: ApplyAssetOptions) => Promise<number>): VoidFunction
```

* * *

### registerApplyToBlockMiddleware()[#](#registerapplytoblockmiddleware)

  

Register middleware that intercepts asset application to specific blocks.

The middleware function receives the source ID, asset result, target block, and the original apply function. It can perform custom logic before, after, or instead of the default block asset application.

#### Parameters[#](#parameters-16)

| Parameter | Type | Description |
| --- | --- | --- |
| `middleware` | (`sourceId`, `assetResult`, `block`, `applyToBlock`) => `Promise`<`void`\> | The middleware function that is called before applying the asset. |

#### Returns[#](#returns-20)

`VoidFunction`

A function that can be used to remove the middleware.

#### Example[#](#example-3)

```
engine.asset.registerApplyToBlockMiddleware(async (sourceId, assetResult, block, applyToBlock) => {  // do something before applying the asset  // You still have the choice to call applyToBlock or skip it  await applyToBlock(sourceId, assetResult, block);  // do something after applying the asset})
```

#### Signature[#](#signature-14)

```
registerApplyToBlockMiddleware(middleware: (sourceId: string, assetResult: AssetResult, block: number, applyToBlock: (sourceId: string, assetResult: AssetResult, block: number) => Promise<void>) => Promise<void>): VoidFunction
```

* * *

### apply()[#](#apply)

  

Apply an asset to the active scene.

Creates a new block configured according to the asset’s properties and adds it to the scene. The behavior can be customized by providing an `applyAsset` function when registering the asset source, or by passing context options to guide middleware behavior.

#### Parameters[#](#parameters-17)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |
| `assetResult` | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | A single asset result from a `findAssets` query. |
| `options?` | [`ApplyAssetOptions`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/applyassetoptions/) | Optional configuration for asset application. |

#### Returns[#](#returns-21)

`Promise`<`number`\>

Promise resolving to the created block ID, or undefined if no block was created.

#### Examples[#](#examples)

```
// Default behaviorawait engine.asset.apply('asset-source-id', assetResult.assets[0]);
```

```
// Foreground overlay placementawait engine.asset.apply('asset-source-id', assetResult.assets[0], {  clipType: 'overlay'});
```

#### Signature[#](#signature-15)

```
apply(sourceId: string, assetResult: AssetResult, options?: ApplyAssetOptions): Promise<number>
```

* * *

### applyToBlock()[#](#applytoblock)

  

Apply an asset to a specific block.

Modifies the target block’s properties according to the asset’s configuration. The behavior can be customized by providing an `applyAssetToBlock` function when registering the asset source.

```
await engine.asset.applyToBlock('asset-source-id', assetResult.assets[0]);
```

#### Parameters[#](#parameters-18)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |
| `assetResult` | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | A single asset result from a `findAssets` query. |
| `block` | `number` | The block to apply the asset to. |

#### Returns[#](#returns-22)

`Promise`<`void`\>

#### Signature[#](#signature-16)

```
applyToBlock(sourceId: string, assetResult: AssetResult, block: number): Promise<void>
```

* * *

### applyProperty()[#](#applyproperty)

  

Apply a specific asset property to the currently selected element.

Allows applying individual properties (like colors, fonts, or effects) from an asset without creating a new block. The behavior can be customized by providing an `applyAssetProperty` function.

```
const asset = assetResult.assets[0];if (asset.payload && asset.payload.properties) {  for (const property of asset.payload.properties) {    await engine.asset.applyProperty('asset-source-id', asset, property);  }}
```

#### Parameters[#](#parameters-19)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The ID of the asset source. |
| `assetResult` | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | A single asset result from a `findAssets` query. |
| `property` | [`AssetProperty`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/assetproperty/) | The specific asset property to apply. |

#### Returns[#](#returns-23)

`Promise`<`void`\>

#### Signature[#](#signature-17)

```
applyProperty(sourceId: string, assetResult: AssetResult, property: AssetProperty): Promise<void>
```

* * *

### defaultApplyAsset()[#](#defaultapplyasset)

  

Apply an asset using the engine’s default implementation.

The default implementation already handles various different kinds of assets and acts as a good starting point.

```
engine.asset.addSource({  id: 'foobar',  async findAssets(queryData) {    return Promise.resolve({      assets: [        {          id: 'logo',          meta: {            uri: 'https://img.ly/static/ubq_samples/imgly_logo.jpg',          }        }      ],      total: 1,      currentPage: queryData.page,      nextPage: undefined    });  },  async applyAsset(assetResult) {    return engine.asset.defaultApplyAsset(assetResult);  },});
```

#### Parameters[#](#parameters-20)

| Parameter | Type | Description |
| --- | --- | --- |
| `assetResult` | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | A single asset result from a `findAssets` query. |

#### Returns[#](#returns-24)

`Promise`<`number`\>

Promise resolving to the created block ID, or undefined if no block was created.

#### Signature[#](#signature-18)

```
defaultApplyAsset(assetResult: AssetResult): Promise<number>
```

* * *

### defaultApplyAssetToBlock()[#](#defaultapplyassettoblock)

  

Apply an asset to a block using the engine’s default implementation.

The default implementation already handles various different kinds of assets and acts as a good starting point.

```
engine.asset.addSource({  id: 'foobar',  async findAssets(queryData) {    return Promise.resolve({      assets: [        {          id: 'logo',          meta: {            uri: 'https://img.ly/static/ubq_samples/imgly_logo.jpg',          }        }      ],      total: 1,      currentPage: queryData.page,      nextPage: undefined    });  },  async applyAssetToBlock(assetResult, block) {    engine.asset.defaultApplyAssetToBlock(assetResult, block);  },});
```

#### Parameters[#](#parameters-21)

| Parameter | Type | Description |
| --- | --- | --- |
| `assetResult` | [`AssetResult`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetresult/) | A single asset result from a `findAssets` query. |
| `block` | `number` | The block to apply the asset to. |

#### Returns[#](#returns-25)

`Promise`<`void`\>

#### Signature[#](#signature-19)

```
defaultApplyAssetToBlock(assetResult: AssetResult, block: number): Promise<void>
```

## Asset Lifecycle[#](#asset-lifecycle)

Add, remove, and manage assets within local asset sources.

### addAssetToSource()[#](#addassettosource)

  

Add an asset to a local asset source.

Only works with local asset sources that support asset management. The asset will be validated against the source’s supported MIME types.

```
engine.asset.addAssetToSource('local-source', {  id: 'asset-id',  label: {    en: 'My Asset'  },  meta: {    uri: 'https://example.com/asset.jpg',    mimeType: 'image/jpeg'  }});
```

#### Parameters[#](#parameters-22)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The local asset source ID that the asset should be added to. |
| `asset` | [`AssetDefinition`](https://img.ly/docs/cesdk/vue/api/engine/interfaces/assetdefinition/) | The asset definition to add to the source. |

#### Returns[#](#returns-26)

`void`

#### Signature[#](#signature-20)

```
addAssetToSource(sourceId: string, asset: AssetDefinition): void
```

* * *

### removeAssetFromSource()[#](#removeassetfromsource)

  

Remove an asset from a local asset source.

Only works with local asset sources that support asset management. The asset will be permanently deleted from the source.

```
engine.asset.removeAssetFromSource('local-source', 'asset-id');
```

#### Parameters[#](#parameters-23)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceId` | `string` | The id of the local asset source that currently contains the asset. |
| `assetId` | `string` | The id of the asset to be removed. |

#### Returns[#](#returns-27)

`void`

#### Signature[#](#signature-21)

```
removeAssetFromSource(sourceId: string, assetId: string): void
```

* * *

### assetSourceContentsChanged()[#](#assetsourcecontentschanged)

  

Notify the engine that an asset source’s contents have changed.

This triggers refresh of any UI components that display assets from this source and notifies subscribers to the asset source update events.

```
engine.asset.assetSourceContentsChanged('asset-source-id');
```

#### Parameters[#](#parameters-24)

| Parameter | Type | Description |
| --- | --- | --- |
| `sourceID` | `string` | The asset source whose contents changed. |

#### Returns[#](#returns-28)

`void`

#### Signature[#](#signature-22)

```
assetSourceContentsChanged(sourceID: string): void
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/functions/supportswasm)