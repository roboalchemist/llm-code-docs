# Source: https://firebase.google.com/docs/reference/database/cal/rest/Shared.Types/RealtimeDatabaseAuditMetadata.Precondition.PreconditionType.md.txt

# RealtimeDatabaseAuditMetadata.Precondition.PreconditionType

`PreconditionType` enumerates the possible preconditions a client may send.

|                                              Enums                                              ||
|-------------------------------------|------------------------------------------------------------|
| `PRECONDITION_TYPE_UNSPECIFIED`     | No precondition. Not expected.                             |
| `IF_MATCH`                          | Set for REST transactions if IF_MATCH header is sent.      |
| `IF_NONE_MATCH`                     | Set for REST transactions if IF_NONE_MATCH header is sent. |
| `REALTIME_TRANSACTION_PRECONDITION` | Set for REALTIME transactions and transaction simulations. |