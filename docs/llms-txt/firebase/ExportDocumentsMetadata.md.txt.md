# Source: https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ExportDocumentsMetadata.md.txt

# ExportDocumentsMetadata

Metadata for `https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Operation` results from `https://firebase.google.com/docs/firestore/reference/rest/v1/projects.databases/exportDocuments#google.firestore.admin.v1.FirestoreAdmin.ExportDocuments`.

| JSON representation |
|---|
| ``` { "startTime": string, "endTime": string, "operationState": enum (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/OperationState`), "progressDocuments": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress`) }, "progressBytes": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress`) }, "collectionIds": [ string ], "outputUriPrefix": string, "namespaceIds": [ string ], "snapshotTime": string } ``` |

| Fields ||
|---|---|
| `startTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` The time this operation started. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `endTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` The time this operation completed. Will be unset if operation still in progress. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `operationState` | ``enum (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/OperationState`)`` The state of the export operation. |
| `progressDocuments` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress`)`` The progress, in documents, of this operation. |
| `progressBytes` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/Progress`)`` The progress, in bytes, of this operation. |
| `collectionIds[]` | `string` Which collection IDs are being exported. |
| `outputUriPrefix` | `string` Where the documents are being exported to. |
| `namespaceIds[]` | `string` Which namespace IDs are being exported. |
| `snapshotTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` The timestamp that corresponds to the version of the database that is being exported. If unspecified, there are no guarantees about the consistency of the documents being exported. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |