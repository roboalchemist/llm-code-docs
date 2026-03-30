# Interface: AssetSource

A source of assets

## Methods[#](#methods)

### findAssets()[#](#findassets)

```
findAssets(queryData): Promise<AssetsQueryResult<AssetResult>>;
```

Find all asset for the given type and the provided query data.

#### Parameters[#](#parameters)

| Parameter | Type |
| --- | --- |
| `queryData` | [`AssetQueryData`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetquerydata/) |

#### Returns[#](#returns)

`Promise`<[`AssetsQueryResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetsqueryresult/)<[`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/)\>>

* * *

### addAsset()?[#](#addasset)

```
optional addAsset(asset): void;
```

Adds the given asset to this source. Throws an error if the asset source does not support adding assets.

#### Parameters[#](#parameters-1)

| Parameter | Type |
| --- | --- |
| `asset` | [`AssetDefinition`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetdefinition/) |

#### Returns[#](#returns-1)

`void`

* * *

### removeAsset()?[#](#removeasset)

```
optional removeAsset(assetId): void;
```

Removes the given asset from this source.

#### Parameters[#](#parameters-2)

| Parameter | Type |
| --- | --- |
| `assetId` | `string` |

#### Returns[#](#returns-2)

`void`

* * *

### getSupportedMimeTypes()?[#](#getsupportedmimetypes)

```
optional getSupportedMimeTypes(): string[];
```

Generates a list of supported mime types for this source.

#### Returns[#](#returns-3)

`string`\[\]

a list of the mime types should be supported by this source

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `id` | `string` | The unique id of the API |
| `fetchAsset?` | (`id`, `params?`) => `Promise`<[`AssetResult`](https://img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetresult/)\> | Fetch an asset by id. |
| `getGroups?` | () => `Promise`<`string`\[\]> | Return every available group |
| `credits?` | `object` | Credits for the source/api |
| `credits.name` | `string` | \- |
| `credits.url?` | `string` | \- |
| `license?` | `object` | General license for all asset from this source |
| `license.name` | `string` | \- |
| `license.url?` | `string` | \- |
| ~`canManageAssets?`~ | `boolean` | Can the source add and remove assets dynamically? If `false` methods like `addAsset` and `removeAsset` will throw an error. **Deprecated** Will be removed in v1.11. Use `canAdd` and `canRemove` in the asset library configuration |
| `applyAsset?` | (`asset`) => `Promise`<`number`\> | Apply the given asset result to the active scene. You can override this with custom behavior. |
| `applyAssetToBlock?` | (`asset`, `block`) => `Promise`<`void`\> | Apply the given asset result to the given block. You can override this with custom behavior. |
| `applyAssetProperty?` | (`asset`, `property`) => `Promise`<`void`\> | Apply a property of the given asset result to the active scene. You can override this with custom behavior. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/interfaces/assetrgbcolor)