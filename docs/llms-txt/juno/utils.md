# Source: https://juno.build/docs/reference/functions/typescript/utils.md

# Source: https://juno.build/docs/reference/functions/rust/utils.md

# Utils

The following utilities are provided to help you work with document and asset data inside your Satellite. They simplify tasks such as decoding and encoding data, serializing custom types, and interacting with Junoâs core features in a consistent way.

**ð¦ Crate:**

All utilities on this page are provided by the [junobuild-utils](https://docs.rs/junobuild-utils/latest/junobuild_utils/index.html) crate.

To use them, add this to your Cargo.toml:

```
[dependencies]junobuild-utils = "*"
```

Replace `*` with the specific version you want to use, or omit the version to always use the latest version.

---

## decode\_doc\_data

Deserializes raw document data (`&[u8]`) into a typed Rust struct. Use this inside hooks or assertions to get the document contents in a strongly typed way.

```
pub fn decode_doc_data<T: for<'a> Deserialize<'a>>(    data: &[u8],) -> Result<T, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-utils/latest/junobuild_utils/fn.decode_doc_data.html)

---

## encode\_doc\_data

Serializes a Rust struct into a `Vec<u8>` for storing a document into the datastore. Use this when modifying or creating document data inside a hook or assertion.

```
pub fn encode_doc_data<T: Serialize>(data: &T) -> Result<Vec<u8>, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-utils/latest/junobuild_utils/fn.encode_doc_data.html)

---

## encode\_doc\_data\_to\_string

Serializes a Rust struct into a JSON String. Use this if you want to store or inspect document data in a readable format. Commonly used when exposing JSON data on the web, for example by reproducing documents from the datastore into the storage.

```
pub fn encode_doc_data_to_string<T: Serialize>(    data: &T,) -> Result<String, String>
```

ð¦ See full definition on [docs.rs](https://docs.rs/junobuild-utils/latest/junobuild_utils/fn.encode_doc_data_to_string.html)