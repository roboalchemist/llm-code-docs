# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input.md

# getLogsInput

Input parameters for querying and filtering audit logs.

### Examples

```graphql
input GetLogsInput {
  logTypes: [LogType!]
  logNames: [LogName!]
  userEmails: [String!]
  limit: Float
  skip: Float
  orderBy: LogOrderBy
  dateRange: LogDateRange
}
```

### Fields

| Field                                                                                                                       | Description                                     | Supported fields                                                                                      |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| logTypes [`[LogType!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-type)           | Filter logs by one or more log types            |                                                                                                       |
| logNames [`[LogName!]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/log-name)           | Filter logs by one or more log names            |                                                                                                       |
| userEmails `[String!]`                                                                                                      | Filter logs by one or more user email addresses |                                                                                                       |
| limit `Float`                                                                                                               | Maximum number of logs to return                |                                                                                                       |
| skip `Float`                                                                                                                | Number of logs to skip (for pagination)         |                                                                                                       |
| orderBy [`LogOrderBy`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/log-order-by)       | Sorting criteria for the logs                   | <p>field <code>String</code><br>direction <a href="../enums/direction"><code>Direction</code></a></p> |
| dateRange [`LogDateRange`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/log-date-range) | Time range to filter logs                       | <p>from <code>DateTime</code><br>to <code>DateTime</code></p>                                         |

### References

#### Queries using this object

* [\<?> getLogs.input](https://docs.ox.security/api-documentation/api-reference/api--audit/queries/get-logs)
* [\<?> getLogsCount.input](https://docs.ox.security/api-documentation/api-reference/api--audit/queries/get-logs-count)
