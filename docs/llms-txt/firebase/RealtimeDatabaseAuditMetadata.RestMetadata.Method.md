# Source: https://firebase.google.com/docs/reference/database/cal/rest/Shared.Types/RealtimeDatabaseAuditMetadata.RestMetadata.Method.md.txt

# RealtimeDatabaseAuditMetadata.RestMetadata.Method

`Method` enumerates possible HTTP methods RTDB supports.

|                                          Enums                                          ||
|----------------------|-------------------------------------------------------------------|
| `METHOD_UNSPECIFIED` | Set for unexpected methods.                                       |
| `GET`                | Set for data read operations.                                     |
| `POST`               | Set for data write operations.                                    |
| `PUT`                | Set for data push operations.                                     |
| `DELETE`             | Set for remove operations (but not updates that remove subpaths). |
| `OPTIONS`            | Sent by browser to determine what methods are allowed.            |
| `PATCH`              | Set for data update operations.                                   |