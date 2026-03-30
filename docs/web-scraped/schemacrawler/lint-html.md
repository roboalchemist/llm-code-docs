# Source: https://www.schemacrawler.com/lint.html

Title: SchemaCrawler

URL Source: https://www.schemacrawler.com/lint.html

Markdown Content:
[](https://www.schemacrawler.com/lint.html#lint-checks)Lint Checks
------------------------------------------------------------------

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintercatalogsql)Linter: _schemacrawler.tools.linter.LinterCatalogSql_

Allows you to run SQL against the database. The SQL statement must return exactly one column and one row of data in the results. If one row is returned, it means that the lint has detected a problem. However, if no rows of data are returned, it means that there are no issues. Example configuration:

```
- id: schemacrawler.tools.linter.LinterCatalogSql
  config:
    message: message for SQL catalog lint
    sql: SELECT TOP 1 1 FROM INFORMATION_SCHEMA.TABLES
```

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintercolumntypes)Linter: _schemacrawler.tools.linter.LinterColumnTypes_

Looks for columns in different tables, that have the same name but have different data types.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinterforeignkeymismatch)Linter: _schemacrawler.tools.linter.LinterForeignKeyMismatch_

Checks tables where the foreign key column data type is different from the referenced primary key column data type.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinterforeignkeyselfreference)Linter: _schemacrawler.tools.linter.LinterForeignKeySelfReference_

Checks tables where the foreign key self-references the primary key. This means that a record in the table references itself, and cannot be deleted.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinterforeignkeywithnoindexes)Linter: _schemacrawler.tools.linter.LinterForeignKeyWithNoIndexes_

Checks for tables where foreign keys have no indexes. This may cause inefficient lookups.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinternullcolumnsinindex)Linter: _schemacrawler.tools.linter.LinterNullColumnsInIndex_

Checks for tables that have nullable columns in a unique index.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinternullintendedcolumns)Linter: _schemacrawler.tools.linter.LinterNullIntendedColumns_

Checks for tables where the default value is ‘NULL’ instead of NULL, since this may indicate a error when creating a table.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlinterredundantindexes)Linter: _schemacrawler.tools.linter.LinterRedundantIndexes_

Checks for tables with redundant indexes. A redundant index is one where the sequence of columns is the same as the first few columns of another index. For example, the index `INDEX_B(COL1)` is not needed when you have another index, `INDEX_A(COL1, COL2)``.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertableallnullablecolumns)Linter: _schemacrawler.tools.linter.LinterTableAllNullableColumns_

Tables that have all columns besides the primary key that are nullable, may contain no useful data, and could indicate a schema design smell.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablecycles)Linter: _schemacrawler.tools.linter.LinterTableCycles_

Checks for cyclical relationships between tables, which could cause issues with deletes and inserts.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertableempty)Linter: _schemacrawler.tools.linter.LinterTableEmpty_

Checks for empty tables with no data.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablesql)Linter: _schemacrawler.tools.linter.LinterTableSql_

Allows you to run SQL against the database. The SQL statement must return exactly one column and one row of data in the results. If one row is returned, it means that the lint has detected a problem. However, if no rows of data are returned, it means that there are no issues. Notice the use of `${table}` to indicate the name of the table the lint is running against. Example configuration:

```
- id: schemacrawler.tools.linter.LinterTableSql
  table-exclusion-pattern: .*BOOKS
  config:
    message: message for custom SQL lint
    sql: SELECT TOP 1 1 FROM ${table}
```

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithbadlynamedcolumns)Linter: _schemacrawler.tools.linter.LinterTableWithBadlyNamedColumns_

Checks for columns that should not be named according to certain patterns. For example, you may have a policy that no column can be named `ID`, because you want columns with complete names, such as `ORDER_ID`. If you want to detect columns named `ID`, you could use configuration as shown in the example below. Example configuration:

```
- id: schemacrawler.tools.linter.LinterTableWithBadlyNamedColumns
  config:
    bad-column-names: .*\.ID
```

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithincrementingcolumns)Linter: _schemacrawler.tools.linter.LinterTableWithIncrementingColumns_

Checks for tables with incrementing column names, for example, a table with column names like `CONTACT1`, `CONTACT2` and so on can indicate de-normalization. Additionally, SchemaCrawler Lint will check that the data-types of all incrementing columns are the same, and that no numbers are skipped.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithnoindexes)Linter: _schemacrawler.tools.linter.LinterTableWithNoIndexes_

Checks for tables with no indexes.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithnoprimarykey)Linter: _schemacrawler.tools.linter.LinterTableWithNoPrimaryKey_

Checks for tables with no primary keys. Tables that purely model relationships, without any attributes are ignored.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithnoremarks)Linter: _schemacrawler.tools.linter.LinterTableWithNoRemarks_

Checks for tables and columns with no remarks.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithnosurrogateprimarykey)Linter: _schemacrawler.tools.linter.LinterTableWithNoSurrogatePrimaryKey_

Checks for tables that have more than one column as a primary key, and recommends that a surrogate key column be used as a primary key instead.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithprimarykeynotfirst)Linter: _schemacrawler.tools.linter.LinterTableWithPrimaryKeyNotFirst_

Checks for tables where the primary key columns are not first, since this is the convention.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithquotednames)Linter: _schemacrawler.tools.linter.LinterTableWithQuotedNames_

Checks for tables that have spaces in table or column names, or names that are reserved words in the ANSI SQL standard.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertablewithsinglecolumn)Linter: _schemacrawler.tools.linter.LinterTableWithSingleColumn_

Checks for tables with no columns at all, or just a single column, since that could indicate a schema design smell.

### [](https://www.schemacrawler.com/lint.html#linter-schemacrawlertoolslinterlintertoomanylobs)Linter: _schemacrawler.tools.linter.LinterTooManyLobs_

Checks for tables that have too many large objects (CLOBs or BLOBs), since these could result in additional reads when returning query results. By default, this is more than one such column. Example configuration:

```
- id: schemacrawler.tools.linter.LinterTooManyLobs
  config:
    max-large-objects: 3
```
