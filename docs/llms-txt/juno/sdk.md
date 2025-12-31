# Source: https://juno.build/docs/reference/functions/typescript/sdk.md

# Source: https://juno.build/docs/reference/functions/rust/sdk.md

# SDK

The following functions are provided to help you work with document and asset data inside your Satellite. They are part of the tools available when writing serverless functions in Rust and support common tasks such as interacting with the datastore, storage, and custom hook logic.

**ð¦ Crate:**

The SDK is provided by the [junobuild-satellite](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/index.html) crate.

To use them, add this to your Cargo.toml:

```
[dependencies]junobuild-satellite = "*"
```

You have to follow the pace of the Juno release to ensure compatibility. Refer to the [maintenance guide](/docs/build/functions/development/rust.md#maintenance) for instructions.

---

## Datastore

The following functions can be used to manage documents within the Datastore from your serverless functions.

---

### set\_doc\_store

Sets a document in a collectionâs of the datastore. Use this to insert or update document data.

```
pub fn set_doc_store(    caller: UserId,    collection: CollectionKey,    key: Key,    value: SetDoc,) -> Result<DocContext<DocUpsert>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.set_doc_store.html)

---

### get\_doc\_store

Retrieves a document from a collection.

```
pub fn get_doc_store(    caller: UserId,    collection: CollectionKey,    key: Key,) -> Result<Option<Doc>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.get_doc_store.html)

---

### list\_docs\_store

Lists documents in a collection based on filter criteria.

```
pub fn list_docs_store(    caller: Principal,    collection: CollectionKey,    filter: &ListParams,) -> Result<ListResults<Doc>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.list_docs_store.html)

---

### count\_docs\_store

Counts documents in a collection based on filter criteria.

```
pub fn count_docs_store(    caller: Principal,    collection: CollectionKey,    filter: &ListParams,) -> Result<usize, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.count_docs_store.html)

---

### count\_collection\_docs\_store

Counts all documents in a collection.

```
pub fn count_collection_docs_store(    collection: &CollectionKey) -> Result<usize, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.count_collection_docs_store.html)

---

### delete\_doc\_store

Deletes a document from a collection.

```
pub fn delete_doc_store(    caller: UserId,    collection: CollectionKey,    key: Key,    value: DelDoc,) -> Result<DocContext<Option<Doc>>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_doc_store.html)

---

### delete\_docs\_store

Deletes all documents in a collection.

```
pub fn delete_docs_store(    collection: &CollectionKey) -> Result<(), String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_docs_store.html)

---

### delete\_filtered\_docs\_store

Deletes documents matching filter criteria.

```
pub fn delete_filtered_docs_store(    caller: Principal,    collection: CollectionKey,    filter: &ListParams,) -> Result<Vec<DocContext<Option<Doc>>>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_filtered_docs_store.html)

---

## Storage

The following functions can be used to manage assets within the Storage from your serverless functions.

---

### set\_asset\_handler

Sets an asset in the store for the identity encoding (no compression applied).

```
pub fn set_asset_handler(    key: &AssetKey,    content: &Blob,    headers: &[HeaderField],) -> Result<(), String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.set_asset_handler.html)

---

### get\_asset\_store

Retrieves an asset from a collection.

```
pub fn get_asset_store(    caller: Principal,    collection: &CollectionKey,    full_path: FullPath,) -> Result<Option<Asset>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.get_asset_store.html)

---

### list\_assets\_store

Lists assets in a collection, excluding their content.

```
pub fn list_assets_store(    caller: Principal,    collection: &CollectionKey,    filters: &ListParams,) -> Result<ListResults<AssetNoContent>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.list_assets_store.html)

---

### count\_assets\_store

Counts assets in a collection matching the filter criteria.

```
pub fn count_assets_store(    caller: Principal,    collection: &CollectionKey,    filters: &ListParams,) -> Result<usize, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.count_assets_store.html)

---

### count\_collection\_assets\_store

Counts all assets in a collection.

```
pub fn count_collection_assets_store(    collection: &CollectionKey,) -> Result<usize, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.count_collection_assets_store.html)

---

### delete\_asset\_store

Deletes an asset from a collection.

```
pub fn delete_asset_store(    caller: Principal,    collection: &CollectionKey,    full_path: FullPath,) -> Result<Option<Asset>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_asset_store.html)

---

### delete\_assets\_store

Deletes all assets in a collection.

```
pub fn delete_assets_store(    collection: &CollectionKey,) -> Result<(), String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_assets_store.html)

---

### delete\_filtered\_assets\_store

Deletes assets matching filter criteria.

```
pub fn delete_filtered_assets_store(    caller: Principal,    collection: CollectionKey,    filters: &ListParams,) -> Result<Vec<Option<Asset>>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.delete_filtered_assets_store.html)

---

### set\_asset\_token\_store

Set or update an access token for an asset.

```
pub fn set_asset_token_store(    caller: Principal,    collection: &CollectionKey,    full_path: &FullPath,    token: &AssetAccessToken,) -> Result<Option<Asset>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.set_asset_token_store.html)

---

### get\_content\_chunks\_store

Retrieves content chunks of an asset. Particularly useful when stable memory is used.

```
pub fn get_content_chunks_store(    encoding: &AssetEncoding,    chunk_index: usize,    memory: &Memory,) -> Option<Blob>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.get_content_chunks_store.html)

---

## Controllers

The following functions allow you to inspect and assert the controllers of your Satellite.

---

### get\_controllers

Retrieves all controllers of the Satellite.

```
pub fn get_controllers() -> Controllers
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.get_controllers.html)

---

### get\_admin\_controllers

Retrieves only the admin controllers of the Satellite.

```
pub fn get_admin_controllers() -> Controllers
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.get_admin_controllers.html)

---

## Others

The SDK also provides various Satellite-specific functions

---

### random

Generates a random `i32`.

**Caution:**

The generator is seeded once after upgrade of the Satellite. This makes it unsuitable for use cases requiring unpredictable randomness, like lotteries.

```
pub fn random() -> Result<i32, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-satellite/latest/junobuild_satellite/fn.random.html)