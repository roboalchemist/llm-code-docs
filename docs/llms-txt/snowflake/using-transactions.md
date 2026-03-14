# Source: https://docs.snowflake.com/en/developer-guide/sql-api/using-transactions.md

# Using explicit transactions

To execute SQL statements in an explicit [transaction](../../sql-reference/transactions.md), you must use a
[single HTTP request](submitting-multiple-statements.md) to specify the start, end, and statements in the
transaction. For example:

```sqljson
{
  "statement": "begin transaction; insert into table2 (i) values (1); commit; select i from table1 order by i",
  ...
  "parameters": {
      "MULTI_STATEMENT_COUNT": "4"
  }
  ...
}
```

As is the case when you specify [multiple statements in a request](submitting-multiple-statements.md),
if the request was processed successfully, Snowflake returns a response containing the `statementHandles` field, which is
set to an array of handles for the statements in the request (including the BEGIN TRANSACTION and COMMIT statements).

```none
HTTP/1.1 200 OK
Content-Type: application/json

{
  "resultSetMetaData" : {
    "numRows" : 1,
    "format" : "jsonv2",
    "rowType" : [ {
      "name" : "multiple statement execution",
      "database" : "",
      "schema" : "",
      "table" : "",
      "type" : "text",
      "byteLength" : 16777216,
      "scale" : null,
      "precision" : null,
      "nullable" : false,
      "collation" : null,
      "length" : 16777216
    } ]
  },
  "data" : [ [ "Multiple statements executed successfully." ] ],
  "code" : "090001",
  "statementHandles" : [ "019d6ed0-0502-3101-0000-096d00421082", "019d6ed0-0502-3101-0000-096d00421086", "019d6ed0-0502-3101-0000-096d0042108a", "019d6ed0-0502-3101-0000-096d0042108e" ],
  "statementStatusUrl" : "/api/v2/statements/019d6ed0-0502-3101-0000-096d0042107e?requestId=066920fa-e589-43c6-8cca-9dcb2d4be978",
  "sqlState" : "00000",
  "statementHandle" : "019d6ed0-0502-3101-0000-096d0042107e",
  "message" : "Statement executed successfully.",
  "createdOn" : 1625684162876
}
```

The handles in the `statementHandles` field correspond to the statements in the request. In this example, the statements and
their corresponding handles are:

* BEGIN TRANSACTION (`019d6ed0-0502-3101-0000-096d00421082`)
* INSERT (`019d6ed0-0502-3101-0000-096d00421086`)
* COMMIT (`019d6ed0-0502-3101-0000-096d0042108a`)
* SELECT (`019d6ed0-0502-3101-0000-096d0042108e`)

You can use these handles to [check the status of each statement](submitting-multiple-statements.md).
