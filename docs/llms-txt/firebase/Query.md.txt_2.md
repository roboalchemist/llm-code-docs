# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query.md.txt

# firebase::firestore::Query Class Reference

# firebase::firestore::Query


`#include <query.h>`

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) which you can read or listen to.

## Summary

You can also construct refined [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) objects by adding filters and ordering.

You cannot construct a valid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) directly; use [CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference#classfirebase_1_1firestore_1_1_collection_reference) methods that return a [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) instead.


> [!NOTE]
> **Note:** [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) classes are not meant to be subclassed except for use in test mocks. Subclassing is not supported in production code and new SDK releases may break code that does so.

<br />

### Inheritance

Direct Known Subclasses:[firebase::firestore::CollectionReference](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/collection-reference)

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a4f60a0201265ead1826025e27f759ef6()` Creates an invalid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that has to be reassigned before it can be used. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a5ec9f17aec1c45cc2fd44e6f2fe89ea4(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query & other)` Copy constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1acf8a6439390db42df8a1b425074107a3(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query && other)` Move constructor. ||
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a9558d0713e2d367a9d6a291d3bfdf03b()` ||

| ### Public types ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae07a7722ee6cede6acbb4c2ef8d8f11a` | enumAn enum for the direction of a sort. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae0b372205de96efe45992d48d6f8aaef(std::function< void(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot &, https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5, const std::string &)> callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` Starts listening to the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) events referenced by this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a985be080cd45fb2300497c3a5061dad7(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a9f0a586c44417cd24932561719c97f54 metadata_changes, std::function< void(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot &, https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1acbed0dcd73b55ce5a9d9c3d07bb9cac5, const std::string &)> callback)` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/listener-registration#classfirebase_1_1firestore_1_1_listener_registration` Starts listening to the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) events referenced by this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1af391a3c06f687dd978a97aa7ee3e23f9() const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/aggregate-query#classfirebase_1_1firestore_1_1_aggregate_query` Returns a query that counts the documents in the result set of this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a566ef03e26022f2d6131eb112f02d955(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & snapshot) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f2b5fd0dd939896bb1211d9efebec87(const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ab38fcf1615b20a7a3ab3424870601689(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & snapshot) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends before the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a320c929f99cbb81b735fecbf9cf644eb(const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends before the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a3bf794938d8680d31b799c3f58664375(https://firebase.google.com/docs/reference/cpp/namespace/firebase/firestore#namespacefirebase_1_1firestore_1a706b13a274f8586c90167ba6073e5c66 source) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot >` Executes the query and returns the results as a [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae340518fda964ee5898afa0be9bd1cae(int32_t limit) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that only returns the first matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a56d44ffb65efe77dfff497ec0aaf0c4b(int32_t limit) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that only returns the last matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a4ac550dfc5485cfafab4f86dc50fbe94(const std::string & field, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae07a7722ee6cede6acbb4c2ef8d8f11a direction) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a1733a291039b1ba99875ccb827872c35(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae07a7722ee6cede6acbb4c2ef8d8f11a direction) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a846fee776a1479a85fb54bf176866e9c(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & snapshot) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts after the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a1a91f3e63ae5d2c75e6ce37d79b64488(const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts after the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ab297a2163a03289010db3a1b253eea94(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot & snapshot) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a69fcca2dbfe16d4e54ddda0fd026d511(const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a6e7eda11baf412c31c7109d2b8ab1677(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/filter#classfirebase_1_1firestore_1_1_filter & filter) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a75fa175e136c3a594c271abdc3323460(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c(const std::string & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a956196800239c1108101e835f1f60e22(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1aa5a48c8e3bcfbeee9645d8c303f6dc94(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a316309c749ce5210812b6d48eadcca2a(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1aaea1f3e43ffeb6137b5aa97590e36cd6(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a94906cf085ca72fd3efa3833d5fac397(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1acc6e241bf240af07f0799f3cefaf7670(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1adeed02601776ba5337432604719bb0bb(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229(const std::string & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a0950c6a7827f26801c2fc28fd21ae009(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f6e1ffa44f48da91d0aea489bd5b0a0(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae853eea2347c36964a50989f184ba602(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae5ed1812b1af8cd9cc1a5cf673fea088(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a0f9ef56428526f05242615770fc76860(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a43a82fd0c5ffbb0d4dda6f82e61fef32(const std::string & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value does not equal the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a44e5a9c4d6c14bc0e04dd3449b9cf89d(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value & value) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value does not equal the specified value. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f015a1811acabd22b34630c71317de5(const std::string & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must not equal any of the values from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a530231a0a0f7b6bd440d6163665aa09c(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-path#classfirebase_1_1firestore_1_1_field_path & field, const std::vector< https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value > & values) const ` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must not equal any of the values from the provided list. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a44ff1bcbfa399eb1f1acf8e581bc19d9() const ` | `virtual const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a781f1b109e27d1dfa45bc9dcf6bbc27f()` | `virtual https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore *` Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this query. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a126b51635a823dba82f716e47154d8bd() const ` | `bool` Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is valid, false if it is not valid. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a8a6e50bc1f6608d59192a51b12718802(const https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query & other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query &` Copy assignment operator. |
| `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a497389d2389140e9ff194f31aefffa61(https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query && other)` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query &` Move assignment operator. |

## Public types

### Direction

```c++
 Direction
```
An enum for the direction of a sort.

## Public functions

### AddSnapshotListener

```c++
virtual ListenerRegistration AddSnapshotListener(
  std::function< void(const QuerySnapshot &, Error, const std::string &)> callback
)
```
Starts listening to the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) events referenced by this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | The std::function to call. When this function is called, snapshot value is valid if and only if error is Error::kErrorOk. The std::string is an error message; the value may be empty if an error message is not available. | |
| **Returns** | A registration object that can be used to remove the listener. |

### AddSnapshotListener

```c++
virtual ListenerRegistration AddSnapshotListener(
  MetadataChanges metadata_changes,
  std::function< void(const QuerySnapshot &, Error, const std::string &)> callback
)
```
Starts listening to the [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot) events referenced by this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `metadata_changes` | Indicates whether metadata-only changes (that is, only [DocumentSnapshot::metadata()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/document-snapshot#classfirebase_1_1firestore_1_1_document_snapshot_1a6e8881817cf1fdd48fe5603c74fe9aae) changed) should trigger snapshot events. | | `callback` | The std::function to call. When this function is called, snapshot value is valid if and only if error is Error::kErrorOk. The std::string is an error message; the value may be empty if an error message is not available. | |
| **Returns** | A registration object that can be used to remove the listener. |

### Count

```c++
virtual AggregateQuery Count() const 
```
Returns a query that counts the documents in the result set of this query.

The returned query, when executed, counts the documents in the result set of this query without actually downloading the documents.

Using the returned query to count the documents is efficient because only the final count, not the documents' data, is downloaded. The returned query can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

<br />

| Details ||
|---|---|
| **Returns** | An aggregate query that counts the documents in the result set of this query. |

### EndAt

```c++
virtual Query EndAt(
  const DocumentSnapshot & snapshot
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends at the provided document (inclusive).

The end position is relative to the order of the query. The document must contain all of the fields provided in the order by of this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to end at. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### EndAt

```c++
virtual Query EndAt(
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends at the provided fields relative to the order of the query.

The order of the field values must match the order of the order by clauses of the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | The field values to end this query at, in order of the query's order by. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### EndBefore

```c++
virtual Query EndBefore(
  const DocumentSnapshot & snapshot
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends before the provided document (inclusive).

The end position is relative to the order of the query. The document must contain all of the fields provided in the order by of this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to end before. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### EndBefore

```c++
virtual Query EndBefore(
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that ends before the provided fields relative to the order of the query.

The order of the field values must match the order of the order by clauses of the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | The field values to end this query before, in order of the query's order by. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### Get

```c++
virtual Future< QuerySnapshot > Get(
  Source source
) const 
```
Executes the query and returns the results as a [QuerySnapshot](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query-snapshot#classfirebase_1_1firestore_1_1_query_snapshot).

By default, [Get()](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a3bf794938d8680d31b799c3f58664375) attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the Source parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `source` | A value to configure the get behavior (optional). | |
| **Returns** | A [Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future) that will be resolved with the results of the [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### Limit

```c++
virtual Query Limit(
  int32_t limit
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that only returns the first matching documents up to the specified number.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | A non-negative integer to specify the maximum number of items to return. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### LimitToLast

```c++
virtual Query LimitToLast(
  int32_t limit
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that only returns the last matching documents up to the specified number.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | A non-negative integer to specify the maximum number of items to return. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### OrderBy

```c++
virtual Query OrderBy(
  const std::string & field,
  Direction direction
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that's additionally sorted by the specified field.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The field to sort by. | | `direction` | The direction to sort (optional). If not specified, order will be ascending. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### OrderBy

```c++
virtual Query OrderBy(
  const FieldPath & field,
  Direction direction
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that's additionally sorted by the specified field.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The field to sort by. | | `direction` | The direction to sort (optional). If not specified, order will be ascending. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### Query

```c++
 Query()
```
Creates an invalid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that has to be reassigned before it can be used.

Calling any member function on an invalid [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) will be a no-op. If the function returns a value, it will return a zero, empty, or invalid value, depending on the type of the value.

### Query

```c++
 Query(
  const Query & other
)
```
Copy constructor.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is immutable and can be efficiently copied.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` to copy from. | |

### Query

```c++
 Query(
  Query && other
)
```
Move constructor.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` to move data from. | |

### StartAfter

```c++
virtual Query StartAfter(
  const DocumentSnapshot & snapshot
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts after the provided document (inclusive).

The starting position is relative to the order of the query. The document must contain all of the fields provided in the order by of this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to start after. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### StartAfter

```c++
virtual Query StartAfter(
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts after the provided fields relative to the order of the query.

The order of the field values must match the order of the order by clauses of the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | The field values to start this query after, in order of the query's order by. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### StartAt

```c++
virtual Query StartAt(
  const DocumentSnapshot & snapshot
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts at the provided document (inclusive).

The starting position is relative to the order of the query. The document must contain all of the fields provided in the order by of this query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to start at. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### StartAt

```c++
virtual Query StartAt(
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) that starts at the provided fields relative to the order of the query.

The order of the field values must match the order of the order by clauses of the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `values` | The field values to start this query at, in order of the query's order by. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### Where

```c++
virtual Query Where(
  const Filter & filter
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `filter` | The new filter to apply to the existing query. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereArrayContains

```c++
virtual Query WhereArrayContains(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192` filter and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c` or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field containing an array to search. | | `value` | The value that must be contained in the array. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereArrayContains

```c++
virtual Query WhereArrayContains(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192` filter and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c` or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field containing an array to search. | | `value` | The value that must be contained in the array. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereArrayContainsAny

```c++
virtual Query WhereArrayContainsAny(
  const std::string & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c` filter and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192` or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereArrayContainsAny

```c++
virtual Query WhereArrayContainsAny(
  const FieldPath & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c` filter and it cannot be combined with`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192` or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereEqualTo

```c++
virtual Query WhereEqualTo(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereEqualTo

```c++
virtual Query WhereEqualTo(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereGreaterThan

```c++
virtual Query WhereGreaterThan(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereGreaterThan

```c++
virtual Query WhereGreaterThan(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereGreaterThanOrEqualTo

```c++
virtual Query WhereGreaterThanOrEqualTo(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereGreaterThanOrEqualTo

```c++
virtual Query WhereGreaterThanOrEqualTo(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereIn

```c++
virtual Query WhereIn(
  const std::string & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229` filter and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereIn

```c++
virtual Query WhereIn(
  const FieldPath & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229` filter and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereLessThan

```c++
virtual Query WhereLessThan(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereLessThan

```c++
virtual Query WhereLessThan(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereLessThanOrEqualTo

```c++
virtual Query WhereLessThanOrEqualTo(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereLessThanOrEqualTo

```c++
virtual Query WhereLessThanOrEqualTo(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereNotEqualTo

```c++
virtual Query WhereNotEqualTo(
  const std::string & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value does not equal the specified value.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a43a82fd0c5ffbb0d4dda6f82e61fef32` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f015a1811acabd22b34630c71317de5`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereNotEqualTo

```c++
virtual Query WhereNotEqualTo(
  const FieldPath & field,
  const FieldValue & value
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value does not equal the specified value.

A [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a43a82fd0c5ffbb0d4dda6f82e61fef32` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f015a1811acabd22b34630c71317de5`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `value` | The value for comparison. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereNotIn

```c++
virtual Query WhereNotIn(
  const std::string & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must not equal any of the values from the provided list.

One special case is that `WhereNotIn` cannot match `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2f53ca0c77dfabd8ed8bd313721f960c` values. To query for documents where a field exists and is `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2f53ca0c77dfabd8ed8bd313721f960c`, use `WhereNotEqualTo`, which can handle this special case.

A `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f015a1811acabd22b34630c71317de5` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192`, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c`, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`, or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a43a82fd0c5ffbb0d4dda6f82e61fef32`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The name of the field to compare. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### WhereNotIn

```c++
virtual Query WhereNotIn(
  const FieldPath & field,
  const std::vector< FieldValue > & values
) const 
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) with the additional filter that documents must contain the specified field and the value must not equal any of the values from the provided list.

One special case is that `WhereNotIn` cannot match `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2f53ca0c77dfabd8ed8bd313721f960c` values. To query for documents where a field exists and is `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/field-value#classfirebase_1_1firestore_1_1_field_value_1a2f53ca0c77dfabd8ed8bd313721f960c`, use `WhereNotEqualTo`, which can handle this special case.

A `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a7f015a1811acabd22b34630c71317de5` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ad479af40687aa50d7284c4ca9d69d192`, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a10c75538631558602e930a9e6e411a8c`, `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1ae9cf4fbc650753fa844ee43d3f9ca229`, or `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query_1a43a82fd0c5ffbb0d4dda6f82e61fef32`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `field` | The path of the field to compare. | | `values` | The list that contains the values to match. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query). |

### firestore

```c++
virtual const Firestore * firestore() const 
```
Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this query.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance that this [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) refers to. |

### firestore

```c++
virtual Firestore * firestore()
```
Returns the [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance associated with this query.

The pointer will remain valid indefinitely.

<br />

| Details ||
|---|---|
| **Returns** | Firebase [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance that this [Query](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query) refers to. |

### is_valid

```c++
bool is_valid() const 
```
Returns true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is valid, false if it is not valid.

An invalid `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` could be the result of:

- Creating a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` using the default constructor.
- Moving from the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`.
- Deleting your [Firestore](https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/firestore#classfirebase_1_1firestore_1_1_firestore) instance, which will invalidate all the `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` instances associated with it.

<br />

<br />

| Details ||
|---|---|
| **Returns** | true if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is valid, false if this `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is invalid. |

### operator=

```c++
Query & operator=(
  const Query & other
)
```
Copy assignment operator.

`https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is immutable and can be efficiently copied.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` to copy from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`. |

### operator=

```c++
Query & operator=(
  Query && other
)
```
Move assignment operator.

Moving is more efficient than copying for a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`. After being moved from, a `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` is equivalent to its default-constructed state.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `other` | `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query` to move data from. | |
| **Returns** | Reference to the destination `https://firebase.google.com/docs/reference/cpp/class/firebase/firestore/query#classfirebase_1_1firestore_1_1_query`. |

### \~Query

```c++
virtual  ~Query()
```