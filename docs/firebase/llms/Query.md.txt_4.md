# Source: https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query.md.txt

# Firebase.Firestore.Query Class Reference

# Firebase.Firestore.Query

A query which you can read or listen to.

## Summary

You can also construct refined `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` objects by adding filters, ordering, and other constraints.

[CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference#class_firebase_1_1_firestore_1_1_collection_reference) derives from this class as a "return-all" query against the collection it refers to.

### Inheritance

Direct Known Subclasses:[Firebase.Firestore.CollectionReference](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/collection-reference)

| ### Properties ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a40cb7a28376fe89af21978a341505a1d` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/aggregate-query#class_firebase_1_1_firestore_1_1_aggregate_query` Returns a query that counts the documents in the result set of this query. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ac807490ed0f8f3221830096cacfff5f8` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/firebase-firestore#class_firebase_1_1_firestore_1_1_firebase_firestore` The Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instance associated with this query. |

| ### Public functions ||
|---|---|
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad7118caf3725dae8b07b04ccd64f4758(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot snapshot)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1abce8f8dda85a18fcd251009728d15e39(params object[] fieldValues)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aa7f11902ad530ec49ea31c637f5b3a87(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot snapshot)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends before the provided document (exclusive). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a113a3e07de41c77d291365e17ff94bd3(params object[] fieldValues)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends before the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acca8347de1cf3d0bb089266cd5e4771c(object obj)` | `override bool` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a565737f1d3a336102f2e33fe78dc1f13(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query other)` | `bool` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a344a93a62c40c3bf0e1eceaf244adbe4()` | `override int` |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aac7f5ba93d9b7f6c69fe78769ed49ffe(https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a1e8014969fa0e13d46c8e0684fe0db80 source)` | `Task< https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot >` Asynchronously executes the query and returns all matching documents as a `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a1c9d71597ff1d54f50d9acce371f25cb(int limit)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that only returns the last matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0077ae6ebdf302a5409777aaf7dce12b(int limit)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that only returns the last matching documents up to the specified number. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aff5ae435496d77b14103b885059f8569(Action< https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot > callback)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration` Starts listening to changes to the query results described by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a80185a8630f625c0affae68ddc95f2c0(https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore_1a43cdca9284c02096b03c5ae05de2e288 metadataChanges, Action< https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot > callback)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration` Starts listening to changes to the query results described by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query`. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a5f7045a55509e7806f3754f66f2bbc46(string fieldPath)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a8d84c243588dc42cbda945eb61d4b7fc(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a6b0d9796860a671b596ab7b16b1e33b5(string fieldPath)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field in descending order. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a2accc391ff760b1697e073b38ca9fd93(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field in descending order. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a3d75d0c0fe842821400a1b8173379add(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot snapshot)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts after the provided document (exclusive). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1adaf307a62310f3a7cad493dd0dc1053a(params object[] fieldValues)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts after the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0a8aee0fa2fb84aadd2cdb08b383d7c4(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/document-snapshot#class_firebase_1_1_firestore_1_1_document_snapshot snapshot)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts at the provided document (inclusive). |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a59361562756d52f094b2eb555f635f74(params object[] fieldValues)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts at the provided fields relative to the order of the query. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a2127f33f5a69ebf0a5f2971e85a3b49b(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/filter#class_firebase_1_1_firestore_1_1_filter filter)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) with the additional filter. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a75cff629a5081796e2f99961e6c5f257(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a1225f17511282a807cad4da6a1f4635c(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a709be70065f9072c7031e86cea743abb(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a8f634f9520f635d1b9482122e0d6711c(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a26692b31824797a2aa01c806d8d7ca22(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1adb51e639eb79ff27e59ca092739964c3(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a5be4ed28c393120fe06ea6d9499f43f5(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9bf95814a1c44a5d3afdcd5cf2aa5af1(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a7002e60969bdbfac3596e229e0331d1f(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1af45dc1c64c18e880bb4ce1ea5949473c(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad5a62d72090b53b467c3cb7894e6462e(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a197576c4293d72ce64612db1f38b3bfb(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9470cf702db54423ea571c2e6bd0262f(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1afb224677df7615f864fe708095ba9223(string fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should not equal the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9892d8b549d718ff2b3fe9eb07e22f9c(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, object value)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should not equal the specified value. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acfedad33af02940cbcbff69099c7c42a(https://firebase.google.com/docs/reference/unity/class/firebase/firestore/field-path#class_firebase_1_1_firestore_1_1_field_path fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must not equal any value from the provided list. |
| `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a83e07de5ddf895aa7941601cdf736b93(string fieldPath, IEnumerable< object > values)` | `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must not equal any value from the provided list. |

## Properties

### Count

```c#
AggregateQuery Count
```
Returns a query that counts the documents in the result set of this query.

The returned query, when executed, counts the documents in the result set of this query without actually downloading the documents.

Using the returned query to count the documents is efficient because only the final count, not the documents' data, is downloaded. The returned query can count the documents in cases where the result set is prohibitively large to download entirely (thousands of documents).

<br />

| Details ||
|---|---|
| **Returns** | An aggregate query that counts the documents in the result set of this query. |

### Firestore

```c#
FirebaseFirestore Firestore
```
The Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) instance associated with this query.

## Public functions

### EndAt

```c#
Query EndAt(
  DocumentSnapshot snapshot
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends at the provided document (inclusive).

The end position is relative to the order of the query. The document must contain all of the fields provided in the order-by clauses of the query.

This call replaces any previously specified end position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to end at. | |
| **Returns** | A new query based on the current one, but with the specified end position. |

### EndAt

```c#
Query EndAt(
  params object[] fieldValues
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends at the provided fields relative to the order of the query.

The order of the field values must match the order of the order-by clauses of the query.

This call replaces any previously specified end position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldValues` | The field values. The `fieldValues` array must not be `null` or empty (though elements of the array may be), or have more values than query has orderings. | |
| **Returns** | A new query based on the current one, but with the specified end position. |

### EndBefore

```c#
Query EndBefore(
  DocumentSnapshot snapshot
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends before the provided document (exclusive).

The end position is relative to the order of the query. The document must contain all of the fields provided in the order-by clauses of the query.

This call replaces any previously specified end position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to end before. | |
| **Returns** | A new query based on the current one, but with the specified end position. |

### EndBefore

```c#
Query EndBefore(
  params object[] fieldValues
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that ends before the provided fields relative to the order of the query.

The order of the field values must match the order of the order-by clauses of the query.

This call replaces any previously specified end position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldValues` | The field values. The `fieldValues` array must not be `null` or empty (though elements of the array may be), or have more values than query has orderings. | |
| **Returns** | A new query based on the current one, but with the specified end position. |

### Equals

```c#
override bool Equals(
  object obj
)
```

### Equals

```c#
bool Equals(
  Query other
)
```

### GetHashCode

```c#
override int GetHashCode()
```

### GetSnapshotAsync

```c#
Task< QuerySnapshot > GetSnapshotAsync(
  Source source
)
```
Asynchronously executes the query and returns all matching documents as a `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot`.

By default, `GetSnapshotAsync` attempts to provide up-to-date data when possible by waiting for data from the server, but it may return cached data or fail if you are offline and the server cannot be reached. This behavior can be altered via the `source` parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `source` | indicates whether the results should be fetched from the cache only (`Source.Cache`), the server only (`Source.Server`), or to attempt the server and fall back to the cache (`Source.Default`). | |
| **Returns** | A snapshot of documents matching the query. |

### Limit

```c#
Query Limit(
  int limit
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that only returns the last matching documents up to the specified number.

This call replaces any previously-specified limit in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | The maximum number of items to return. Must be greater than 0. | |
| **Returns** | A new query based on the current one, but with the specified limit applied. |

### LimitToLast

```c#
Query LimitToLast(
  int limit
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that only returns the last matching documents up to the specified number.

You must specify at least one `OrderBy` clause for `LimitToLast` queries, otherwise an exception will be thrown during execution.

This call replaces any previously-specified limit in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `limit` | The maximum number of items to return. Must be greater than 0. | |
| **Returns** | A new query based on the current one, but with the specified limit applied. |

### Listen

```c#
ListenerRegistration Listen(
  Action< QuerySnapshot > callback
)
```
Starts listening to changes to the query results described by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | The callback to invoke each time the query results change. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns** | A [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) which may be used to stop listening gracefully. |

### Listen

```c#
ListenerRegistration Listen(
  MetadataChanges metadataChanges,
  Action< QuerySnapshot > callback
)
```
Starts listening to changes to the query results described by this `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `metadataChanges` | Indicates whether metadata-only changes (i.e. only `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query-snapshot#class_firebase_1_1_firestore_1_1_query_snapshot_1ae3483481c5513bf32acf9a7728850ad2` changed) should trigger snapshot events. | | `callback` | The callback to invoke each time the query results change. Must not be `null`. The callback will be invoked on the main thread. | |
| **Returns** | A [ListenerRegistration](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/listener-registration#class_firebase_1_1_firestore_1_1_listener_registration) which may be used to stop listening gracefully. |

### OrderBy

```c#
Query OrderBy(
  string fieldPath
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field.

Unlike OrderBy in LINQ, this call makes each additional ordering subordinate to the preceding ones. This means that `query.OrderBy("foo").OrderBy("bar")` in Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) is similar to `query.OrderBy(x => x.Foo).ThenBy(x => x.Bar)` in LINQ.

This method cannot be called after a start/end cursor has been specified with [StartAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0a8aee0fa2fb84aadd2cdb08b383d7c4), [StartAfter(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a3d75d0c0fe842821400a1b8173379add), [EndAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad7118caf3725dae8b07b04ccd64f4758) or [EndBefore(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aa7f11902ad530ec49ea31c637f5b3a87) or other overloads.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to order by. Must not be `null` or empty. | |
| **Returns** | A new query based on the current one, but with the additional specified ordering applied. |

### OrderBy

```c#
Query OrderBy(
  FieldPath fieldPath
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field.

Unlike OrderBy in LINQ, this call makes each additional ordering subordinate to the preceding ones. This means that `query.OrderBy("foo").OrderBy("bar")` in Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) is similar to `query.OrderBy(x => x.Foo).ThenBy(x => x.Bar)` in LINQ.

This method cannot be called after a start/end cursor has been specified with [StartAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0a8aee0fa2fb84aadd2cdb08b383d7c4), [StartAfter(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a3d75d0c0fe842821400a1b8173379add), [EndAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad7118caf3725dae8b07b04ccd64f4758) or [EndBefore(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aa7f11902ad530ec49ea31c637f5b3a87) or other overloads.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to order by. Must not be `null`. | |
| **Returns** | A new query based on the current one, but with the additional specified ordering applied. |

### OrderByDescending

```c#
Query OrderByDescending(
  string fieldPath
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field in descending order.

Unlike OrderByDescending in LINQ, this call makes each additional ordering subordinate to the preceding ones. This means that `query.OrderByDescending("foo").OrderByDescending("bar")` in Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) is similar to `query.OrderByDescending(x => x.Foo).ThenByDescending(x => x.Bar)` in LINQ.

This method cannot be called after a start/end cursor has been specified with [StartAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0a8aee0fa2fb84aadd2cdb08b383d7c4), [StartAfter(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a3d75d0c0fe842821400a1b8173379add), [EndAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad7118caf3725dae8b07b04ccd64f4758) or [EndBefore(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aa7f11902ad530ec49ea31c637f5b3a87) or other overloads.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to order by. Must not be `null` or empty. | |
| **Returns** | A new query based on the current one, but with the additional specified ordering applied. |

### OrderByDescending

```c#
Query OrderByDescending(
  FieldPath fieldPath
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that's additionally sorted by the specified field in descending order.

Unlike OrderByDescending in LINQ, this call makes each additional ordering subordinate to the preceding ones. This means that `query.OrderByDescending("foo").OrderByDescending("bar")` in Cloud [Firestore](https://firebase.google.com/docs/reference/unity/namespace/firebase/firestore#namespace_firebase_1_1_firestore) is similar to `query.OrderByDescending(x => x.Foo).ThenByDescending(x => x.Bar)` in LINQ.

This method cannot be called after a start/end cursor has been specified with [StartAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a0a8aee0fa2fb84aadd2cdb08b383d7c4), [StartAfter(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a3d75d0c0fe842821400a1b8173379add), [EndAt(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad7118caf3725dae8b07b04ccd64f4758) or [EndBefore(DocumentSnapshot)](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1aa7f11902ad530ec49ea31c637f5b3a87) or other overloads.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to order by. Must not be `null`. | |
| **Returns** | A new query based on the current one, but with the additional specified ordering applied. |

### StartAfter

```c#
Query StartAfter(
  DocumentSnapshot snapshot
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts after the provided document (exclusive).

The starting position is relative to the order of the query. The document must contain all of the fields provided in the order-by clauses of the query.

This call replaces any previously specified start position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to start after. | |
| **Returns** | A new query based on the current one, but with the specified start position. |

### StartAfter

```c#
Query StartAfter(
  params object[] fieldValues
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts after the provided fields relative to the order of the query.

The order of the field values must match the order of the order-by clauses of the query.

This call replaces any previously specified start position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldValues` | The field values. The `fieldValues` array must not be `null` or empty (though elements of the array may be), or have more values than query has orderings. | |
| **Returns** | A new query based on the current one, but with the specified start position. |

### StartAt

```c#
Query StartAt(
  DocumentSnapshot snapshot
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts at the provided document (inclusive).

The starting position is relative to the order of the query. The document must contain all of the fields provided in order-by clauses of the query.

This call replaces any previously specified start position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `snapshot` | The snapshot of the document to start at. | |
| **Returns** | A new query based on the current one, but with the specified start position. |

### StartAt

```c#
Query StartAt(
  params object[] fieldValues
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` that starts at the provided fields relative to the order of the query.

The order of the field values must match the order of the order-by clauses of the query.

This call replaces any previously specified start position in the query.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldValues` | The field values. The `fieldValues` array must not be `null` or empty (though elements of the array may be), or have more values than query has orderings. | |
| **Returns** | A new query based on the current one, but with the specified start position. |

### Where

```c#
Query Where(
  Filter filter
)
```
Creates and returns a new [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) with the additional filter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `filter` | The new filter to apply to the existing query. | |
| **Returns** | The created [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query). |

### WhereArrayContains

```c#
Query WhereArrayContains(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the fields containing an array to search | | `value` | The value that must be contained in the array. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereArrayContains

```c#
Query WhereArrayContains(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain the provided value.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value that must be contained in the array. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereArrayContainsAny

```c#
Query WhereArrayContainsAny(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7` or `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the fields containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereArrayContainsAny

```c#
Query WhereArrayContainsAny(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field, the value must be an array, and that the array must contain at least one value from the provided list.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7` or `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereEqualTo

```c#
Query WhereEqualTo(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereEqualTo

```c#
Query WhereEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereGreaterThan

```c#
Query WhereGreaterThan(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereGreaterThan

```c#
Query WhereGreaterThan(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereGreaterThanOrEqualTo

```c#
Query WhereGreaterThanOrEqualTo(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereGreaterThanOrEqualTo

```c#
Query WhereGreaterThanOrEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be greater than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereIn

```c#
Query WhereIn(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the fields containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereIn

```c#
Query WhereIn(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must equal one of the values from the provided list.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c` filter and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereLessThan

```c#
Query WhereLessThan(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereLessThan

```c#
Query WhereLessThan(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereLessThanOrEqualTo

```c#
Query WhereLessThanOrEqualTo(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereLessThanOrEqualTo

```c#
Query WhereLessThanOrEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should be less than or equal to the specified value.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereNotEqualTo

```c#
Query WhereNotEqualTo(
  string fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should not equal the specified value.

A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1afb224677df7615f864fe708095ba9223` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acfedad33af02940cbcbff69099c7c42a`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The dot-separated field path to filter on. Must not be `null` or empty. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereNotEqualTo

```c#
Query WhereNotEqualTo(
  FieldPath fieldPath,
  object value
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value should not equal the specified value.

A [Query](https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query) can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1afb224677df7615f864fe708095ba9223` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acfedad33af02940cbcbff69099c7c42a`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The field path to filter on. Must not be `null`. | | `value` | The value to compare in the filter. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereNotIn

```c#
Query WhereNotIn(
  FieldPath fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must not equal any value from the provided list.

One special case is that `WhereNotIn` cannot match null values. To query for documents where a field exists and is null, use `WhereNotEqualTo`, which can handle this special case.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acfedad33af02940cbcbff69099c7c42a` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7`, `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`, `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c`, or `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1afb224677df7615f864fe708095ba9223`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the fields containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |

### WhereNotIn

```c#
Query WhereNotIn(
  string fieldPath,
  IEnumerable< object > values
)
```
Creates and returns a new `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` with the additional filter that documents must contain the specified field and the value must not equal any value from the provided list.

One special case is that `WhereNotIn` cannot match null values. To query for documents where a field exists and is null, use `WhereNotEqualTo`, which can handle this special case.

A `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query` can have only one `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1acfedad33af02940cbcbff69099c7c42a` filter, and it cannot be combined with `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1a9e8d26a0eb2f09315aef43fd0d07c5c7`, `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ad00d5ee3c82f5c8027bff0ec4878b680`, `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1ae2586dfec04d6cd9373cbfd5f9e5ab2c`, or `https://firebase.google.com/docs/reference/unity/class/firebase/firestore/query#class_firebase_1_1_firestore_1_1_query_1afb224677df7615f864fe708095ba9223`.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `fieldPath` | The name of the fields containing an array to search. | | `values` | The list that contains the values to match. | |
| **Returns** | A new query based on the current one, but with the additional filter applied. |