# Source: https://docs.convex.dev/api/interfaces/server.StorageActionWriter.md

# Interface: StorageActionWriter

[server](/api/modules/server.md).StorageActionWriter

An interface to read and write files to storage within Convex actions and HTTP actions.

## Hierarchy[​](#hierarchy "Direct link to Hierarchy")

* [`StorageWriter`](/api/interfaces/server.StorageWriter.md)

  ↳ **`StorageActionWriter`**

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

[StorageWriter](/api/interfaces/server.StorageWriter.md).[getUrl](/api/interfaces/server.StorageWriter.md#geturl)

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

[StorageWriter](/api/interfaces/server.StorageWriter.md).[getUrl](/api/interfaces/server.StorageWriter.md#geturl)

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

[StorageWriter](/api/interfaces/server.StorageWriter.md).[getMetadata](/api/interfaces/server.StorageWriter.md#getmetadata)

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

[StorageWriter](/api/interfaces/server.StorageWriter.md).[getMetadata](/api/interfaces/server.StorageWriter.md#getmetadata)

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

#### Inherited from[​](#inherited-from-4 "Direct link to Inherited from")

[StorageWriter](/api/interfaces/server.StorageWriter.md).[generateUploadUrl](/api/interfaces/server.StorageWriter.md#generateuploadurl)

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

#### Inherited from[​](#inherited-from-5 "Direct link to Inherited from")

[StorageWriter](/api/interfaces/server.StorageWriter.md).[delete](/api/interfaces/server.StorageWriter.md#delete)

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

#### Inherited from[​](#inherited-from-6 "Direct link to Inherited from")

[StorageWriter](/api/interfaces/server.StorageWriter.md).[delete](/api/interfaces/server.StorageWriter.md#delete)

#### Defined in[​](#defined-in-6 "Direct link to Defined in")

[server/storage.ts:124](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L124)

***

### get[​](#get "Direct link to get")

▸ **get**(`storageId`): `Promise`<`null` | `Blob`>

Get a Blob containing the file associated with the provided `Id<"_storage">`, or `null` if there is no file.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

| Name        | Type                                                          |
| ----------- | ------------------------------------------------------------- |
| `storageId` | [`GenericId`](/api/modules/values.md#genericid)<`"_storage"`> |

#### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`null` | `Blob`>

#### Defined in[​](#defined-in-7 "Direct link to Defined in")

[server/storage.ts:138](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L138)

▸ **get**<`T`>(`storageId`): `Promise`<`null` | `Blob`>

**`Deprecated`**

Passing a string is deprecated, use `storage.get(Id<"_storage">)` instead.

Get a Blob containing the file associated with the provided [StorageId](/api/modules/server.md#storageid), or `null` if there is no file.

#### Type parameters[​](#type-parameters-3 "Direct link to Type parameters")

| Name | Type             |
| ---- | ---------------- |
| `T`  | extends `string` |

#### Parameters[​](#parameters-7 "Direct link to Parameters")

| Name        | Type                                                 |
| ----------- | ---------------------------------------------------- |
| `storageId` | `T` extends { `__tableName`: `any` } ? `never` : `T` |

#### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`null` | `Blob`>

#### Defined in[​](#defined-in-8 "Direct link to Defined in")

[server/storage.ts:145](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L145)

***

### store[​](#store "Direct link to store")

▸ **store**(`blob`, `options?`): `Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_storage"`>>

Store the file contained in the Blob.

If provided, this will verify the sha256 checksum matches the contents of the file.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

| Name              | Type     |
| ----------------- | -------- |
| `blob`            | `Blob`   |
| `options?`        | `Object` |
| `options.sha256?` | `string` |

#### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<[`GenericId`](/api/modules/values.md#genericid)<`"_storage"`>>

#### Defined in[​](#defined-in-9 "Direct link to Defined in")

[server/storage.ts:153](https://github.com/get-convex/convex-js/blob/main/src/server/storage.ts#L153)
