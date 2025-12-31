# Source: https://firebase.google.com/docs/reference/database/cal/rest/Shared.Types/RealtimeDatabaseAuditMetadata.RequestType.md.txt

# RealtimeDatabaseAuditMetadata.RequestType

`RequestType` indicates whether the operation was a REST or REALTIME request.

|                                                        Enums                                                        ||
|----------------------------|-----------------------------------------------------------------------------------------|
| `REQUEST_TYPE_UNSPECIFIED` | Not expected.                                                                           |
| `REALTIME`                 | For realtime requests (`realtime-*`, `concurrent-*`, `ondisconnect-*` in the profiler). |
| `REST`                     | For REST requests (`rest-*` in the profiler).                                           |