# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/ImportDocumentsMetadata.md.txt

# ImportDocumentsMetadata

Metadata for databases.importDocuments operations.

| JSON representation ||
|---|---|
| ``` { "startTime": string, "endTime": string, "operationState": enum(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/OperationState`), "progressDocuments": { object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress`) }, "progressBytes": { object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress`) }, "collectionIds": [ string ], "inputUriPrefix": string } ``` |

| Fields ||
|---|---|
| `startTime` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp` format)`` The time that work began on the operation. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`. <br /> |
| `endTime` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp` format)`` The time the operation ended, either successfully or otherwise. Unset if the operation is still active. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`. <br /> |
| `operationState` | ``enum(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/OperationState`)`` The state of the import operation. |
| `progressDocuments` | ``object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress`)`` An estimate of the number of documents processed. |
| `progressBytes` | ``object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress`)`` An estimate of the number of bytes processed. |
| `collectionIds[]` | `string` Which collection ids are being imported. |
| `inputUriPrefix` | `string` The location of the documents being imported. |