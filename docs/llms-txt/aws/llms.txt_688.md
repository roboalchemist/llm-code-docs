# Source: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/llms.txt

# RDS Data API API Reference

> Amazon RDS provides an HTTP endpoint to run SQL statements on an Amazon Aurora DB cluster. To run these statements, you use the RDS Data API (Data API).

- [Welcome](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/Welcome.html)

## [Actions](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Operations.html)

- [BatchExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BatchExecuteStatement.html): Runs a batch SQL statement over an array of data.
- [BeginTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BeginTransaction.html): Starts a SQL transaction.
- [CommitTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_CommitTransaction.html): Ends a SQL transaction started with the BeginTransaction operation and commits the changes.
- [ExecuteSql](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteSql.html): Runs one or more SQL statements.
- [ExecuteStatement](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html): Runs a SQL statement against a database.
- [RollbackTransaction](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_RollbackTransaction.html): Performs a rollback of a transaction.


## [Data Types](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Types.html)

- [ArrayValue](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ArrayValue.html): Contains an array.
- [ColumnMetadata](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ColumnMetadata.html): Contains the metadata for a column.
- [Field](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Field.html): Contains a value.
- [Record](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Record.html): A record returned by a call.
- [ResultFrame](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ResultFrame.html): The result set returned by a SQL statement.
- [ResultSetMetadata](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ResultSetMetadata.html): The metadata of the result set returned by a SQL statement.
- [ResultSetOptions](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ResultSetOptions.html): Options that control how the result set is returned.
- [SqlParameter](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_SqlParameter.html): A parameter used in a SQL statement.
- [SqlStatementResult](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_SqlStatementResult.html): The result of a SQL statement.
- [StructValue](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_StructValue.html): A structure value returned by a call.
- [UpdateResult](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_UpdateResult.html): The response elements represent the results of an update.
- [Value](https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Value.html): Contains the value of a column.
