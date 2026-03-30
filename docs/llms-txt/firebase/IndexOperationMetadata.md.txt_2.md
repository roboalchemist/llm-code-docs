# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/IndexOperationMetadata.md.txt

# IndexOperationMetadata

Metadata for index operations. This metadata populates the metadata field of `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Operation`.

| JSON representation ||
|---|---|
| ``` { "startTime": string, "endTime": string, "index": string, "operationType": enum(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/OperationType`), "cancelled": boolean, "documentProgress": { object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/IndexOperationMetadata#Progress`) } } ``` |

| Fields ||
|---|---|
| `startTime` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp` format)`` The time that work began on the operation. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`. <br /> |
| `endTime` | ``string (`https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp` format)`` The time the operation ended, either successfully or otherwise. Unset if the operation is still active. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`. <br /> |
| `index` | `string` The index resource that this operation is acting on. For example: `projects/{projectId}/databases/{databaseId}/indexes/{index_id}` |
| `operationType` | ``enum(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/OperationType`)`` The type of index operation. |
| `cancelled` | `boolean` True if the `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Operation` was cancelled. If the cancellation is in progress, cancelled will be true but `https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Operation#FIELDS.done` will be false. |
| `documentProgress` | ``object(`https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress`)`` Progress of the existing operation, measured in number of documents. |

## Progress

Measures the progress of a particular metric.

| JSON representation ||
|---|---|
| ``` { "workCompleted": string, "workEstimated": string } ``` |

| Fields ||
|---|---|
| `workCompleted` | `string (https://developers.google.com/discovery/v1/type-format format)` An estimate of how much work has been completed. Note that this may be greater than `workEstimated`. |
| `workEstimated` | `string (https://developers.google.com/discovery/v1/type-format format)` An estimate of how much work needs to be performed. Zero if the work estimate is unavailable. May change as work progresses. |