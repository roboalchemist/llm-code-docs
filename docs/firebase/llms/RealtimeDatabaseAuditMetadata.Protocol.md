# Source: https://firebase.google.com/docs/reference/database/cal/rest/Shared.Types/RealtimeDatabaseAuditMetadata.Protocol.md.txt

# RealtimeDatabaseAuditMetadata.Protocol

`Protocol` indicates which communication protocol the client used to start the audited operation.

|                                               Enums                                                ||
|------------------------|----------------------------------------------------------------------------|
| `PROTOCOL_UNSPECIFIED` | Not expected.                                                              |
| `WEBSOCKETS`           | Set for realtime wire protocol requests made over a websockets connection. |
| `LONG_POLLING`         | Set for realtime wire protocol request made using long-polling.            |
| `EVENT_STREAMING`      | Set for streaming queries made using REST with server-sent events.         |
| `REST_HTTP`            | Set for normal REST data requests `rest-{read, write, etc.}`.              |