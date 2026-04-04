# Source: https://docs.convex.dev/api/interfaces/server.StorageWriter.md

# Interface: StorageWriter

[server](/api/modules/server.md).StorageWriter

An interface to write files to storage within Convex mutation functions.

## Hierarchy[​](#hierarchy "Direct link to Hierarchy")

* [`StorageReader`](/api/interfaces/server.StorageReader.md)

  ↳ **`StorageWriter`**

  ↳↳ [`StorageActionWriter`](/api/interfaces/server.StorageActionWriter.md)

## Methods[​](#methods "Direct link to Methods")

### getUrl[​](#geturl "Direct link to getUrl")

▸ **getUrl**(`storageId`): `Promise`<`null` | `string`>

Get the URL for a file in storage by its `Id<"_storage">`.

The GET response includes a standard HTTP Digest header with a sha256 checksum.

#### Parameters[​](#parameters "Direct link to Parameters")

| Name        | Type                                                          | Description                                                    |
| ----------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| `storageId` | [`GenericId`](/api/modules/values.md#genericid)<`"_storage"`> | The `Id<"_storage">` of the file to fetch from Convex storage. |

#### Returns[​](#returns "Direct link to Returns")

`Promise`<`null` | `string`>

* A url which fetches the file via an HTTP GET, or `null` if it no longer exists.

#### Inherited from[​](#inherited-from "Direct link to Inherited from")

[StorageReader](/api/interfaces/server.StorageReader.md).[getUrl](/api/interfaces/server.StorageReader.md#geturl)

#### Defined in[​](#defined-in "Direct link to Defined in")

[server/storage.ts:51](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L51)

▸ **getUrl**<`T`>(`storageId`): `Promise`<`null` | `string`>

**`Deprecated`**

Passing a string is deprecated, use `storage.getUrl(Id<"_storage">)` instead.

Get the URL for a file in storage by its [StorageId](/api/modules/server.md#storageid).

The GET response includes a standard HTTP Digest header with a sha256 checksum.

#### Type parameters[​](#type-parameters "Direct link to Type parameters")

| Name | Type             |
| ---- | ---------------- |
| `T`  | extends `string` |

#### Parameters[​](#parameters-1 "Direct link to Parameters")

| Name        | Type                                                 | Description                                                                                 |
| ----------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `storageId` | `T` extends { `__tableName`: `any` } ? `never` : `T` | The [StorageId](/api/modules/server.md#storageid) of the file to fetch from Convex storage. |

#### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`null` | `string`>

* A url which fetches the file via an HTTP GET, or `null` if it no longer exists.

#### Inherited from[​](#inherited-from-1 "Direct link to Inherited from")

[StorageReader](/api/interfaces/server.StorageReader.md).[getUrl](/api/interfaces/server.StorageReader.md#geturl)

#### Defined in[​](#defined-in-1 "Direct link to Defined in")

[server/storage.ts:63](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L63)

***

### getMetadata[​](#getmetadata "Direct link to getMetadata")

▸ **getMetadata**(`storageId`): `Promise`<`null` | [`FileMetadata`](/api/modules/server.md#filemetadata)>

**`Deprecated`**

This function is deprecated, use `db.system.get(Id<"_storage">)` instead.

Get metadata for a file.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Name        | Type                                                          | Description                       |
| ----------- | ------------------------------------------------------------- | --------------------------------- |
| `storageId` | [`GenericId`](/api/modules/values.md#genericid)<`"_storage"`> | The `Id<"_storage">` of the file. |

#### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`null` | [`FileMetadata`](/api/modules/server.md#filemetadata)>

* A [FileMetadata](/api/modules/server.md#filemetadata) object if found or `null` if not found.

#### Inherited from[​](#inherited-from-2 "Direct link to Inherited from")

[StorageReader](/api/interfaces/server.StorageReader.md).[getMetadata](/api/interfaces/server.StorageReader.md#getmetadata)

#### Defined in[​](#defined-in-2 "Direct link to Defined in")

[server/storage.ts:75](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L75)

▸ **getMetadata**<`T`>(`storageId`): `Promise`<`null` | [`FileMetadata`](/api/modules/server.md#filemetadata)>

**`Deprecated`**

This function is deprecated, use `db.system.get(Id<"_storage">)` instead.

Get metadata for a file.

#### Type parameters[​](#type-parameters-1 "Direct link to Type parameters")

| Name | Type             |
| ---- | ---------------- |
| `T`  | extends `string` |

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Name        | Type                                                 | Description                                                    |
| ----------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `storageId` | `T` extends { `__tableName`: `any` } ? `never` : `T` | The [StorageId](/api/modules/server.md#storageid) of the file. |

#### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`null` | [`FileMetadata`](/api/modules/server.md#filemetadata)>

* A [FileMetadata](/api/modules/server.md#filemetadata) object if found or `null` if not found.

#### Inherited from[​](#inherited-from-3 "Direct link to Inherited from")

[StorageReader](/api/interfaces/server.StorageReader.md).[getMetadata](/api/interfaces/server.StorageReader.md#getmetadata)

#### Defined in[​](#defined-in-3 "Direct link to Defined in")

[server/storage.ts:85](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L85)

***

### generateUploadUrl[​](#generateuploadurl "Direct link to generateUploadUrl")

▸ **generateUploadUrl**(): `Promise`<`string`>

Fetch a short-lived URL for uploading a file into storage.

Upon a POST request to this URL, the endpoint will return a JSON object containing a newly allocated `Id<"_storage">`.

The POST URL accepts an optional standard HTTP Digest header with a sha256 checksum.

#### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`string`>

* A url that allows file upload via an HTTP POST.

#### Defined in[​](#defined-in-4 "Direct link to Defined in")

[server/storage.ts:105](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L105)

***

### delete[​](#delete "Direct link to delete")

▸ **delete**(`storageId`): `Promise`<`void`>

Delete a file from Convex storage.

Once a file is deleted, any URLs previously generated by [getUrl](/api/interfaces/server.StorageReader.md#geturl) will return 404s.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Name        | Type                                                          | Description                                                     |
| ----------- | ------------------------------------------------------------- | --------------------------------------------------------------- |
| `storageId` | [`GenericId`](/api/modules/values.md#genericid)<`"_storage"`> | The `Id<"_storage">` of the file to delete from Convex storage. |

#### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-5 "Direct link to Defined in")

[server/storage.ts:113](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L113)

▸ **delete**<`T`>(`storageId`): `Promise`<`void`>

**`Deprecated`**

Passing a string is deprecated, use `storage.delete(Id<"_storage">)` instead.

Delete a file from Convex storage.

Once a file is deleted, any URLs previously generated by [getUrl](/api/interfaces/server.StorageReader.md#geturl) will return 404s.

#### Type parameters[​](#type-parameters-2 "Direct link to Type parameters")

| Name | Type             |
| ---- | ---------------- |
| `T`  | extends `string` |

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Name        | Type                                                 | Description                                                                                  |
| ----------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `storageId` | `T` extends { `__tableName`: `any` } ? `never` : `T` | The [StorageId](/api/modules/server.md#storageid) of the file to delete from Convex storage. |

#### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`void`>

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/storage.ts:124](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L124)
