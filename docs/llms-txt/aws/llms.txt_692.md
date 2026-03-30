# Source: https://docs.aws.amazon.com/redshift-data/latest/APIReference/llms.txt

# Amazon Redshift Data API API Reference

> You can use the Amazon Redshift Data API to run queries on Amazon Redshift tables. You can run SQL statements, which are committed if the statement succeeds.

- [Welcome](https://docs.aws.amazon.com/redshift-data/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/redshift-data/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/redshift-data/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_Operations.html)

- [BatchExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_BatchExecuteStatement.html): Runs one or more SQL statements, which can be data manipulation language (DML) or data definition language (DDL).
- [CancelStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_CancelStatement.html): Cancels a running query.
- [DescribeStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeStatement.html): Describes the details about a specific instance when a query was run by the Amazon Redshift Data API.
- [DescribeTable](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeTable.html): Describes the detailed information about a table from metadata in the cluster.
- [ExecuteStatement](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ExecuteStatement.html): Runs an SQL statement, which can be data manipulation language (DML) or data definition language (DDL).
- [GetStatementResult](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_GetStatementResult.html): Fetches the temporarily cached result of an SQL statement in JSON format.
- [GetStatementResultV2](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_GetStatementResultV2.html): Fetches the temporarily cached result of an SQL statement in CSV format.
- [ListDatabases](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListDatabases.html): List the databases in a cluster.
- [ListSchemas](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListSchemas.html): Lists the schemas in a database.
- [ListStatements](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListStatements.html): List of SQL statements.
- [ListTables](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListTables.html): List the tables in a database.


## [Data Types](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_Types.html)

- [ColumnMetadata](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ColumnMetadata.html): The properties (metadata) of a column.
- [Field](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_Field.html): A data value in a column.
- [QueryRecords](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_QueryRecords.html): The results of the SQL statement.
- [SqlParameter](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_SqlParameter.html): A parameter used in a SQL statement.
- [StatementData](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_StatementData.html): The SQL statement to run.
- [SubStatementData](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_SubStatementData.html): Information about an SQL statement.
- [TableMember](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_TableMember.html): The properties of a table.
