# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/review-results/reports/missing-objects-report.md

# SnowConvert AI - Missing Objects Report

## What is a “Missing Object”?

Missing object is the term used to refer to missing DDL definitions inside the source code that are being referenced by code units. The table below shows which elements could be missing objects in each supported language.

| Object | Teradata | Oracle | Transact-SQL | Redshift | BigQuery | Spark | Databricks | Hive | Vertica | PostgreSQL | Greenplum | Netezza | Azure Synapse | IBM DB2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Table | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| View | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Procedure | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Function | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Macro | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Package Function |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| Package Procedure |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| \*Package |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| Join Index | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Index |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| Synonym |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| Database Link |  | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |
| Type | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |
| Materialized View |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| Trigger | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |
| Sequence | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |
| Constraint |  | ✓ | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |

> **Note:**
>
> If an asterisk (‘\*’) is listed in the section above, it means that the object is used to call properties from itself that are not considered DDL statements such as constants, variables, or cursors.

### Where can I find it?

The missing objects report can be found in a folder named *“reports”*, in the output folder of your conversion. The name of the file itself starts with *“MissingObjectReferences”* so it can easily be located.

The format of the file is **.CSV**.

### What information does it contain?

The missing objects report contains the following information about all the missing objects found while converting:

| Column | Description |
| --- | --- |
| PartitionKey | The unique identifier of the conversion. |
| FileName | The name of the file in which the object is located. |
| Caller_CodeUnit | The type of code unit that references a missing element. |
| Caller_CodeUnit_Database | The database where the code unit referencing the missing element is deployed. For now, only SQL Server objects can have a database. |
| Caller_CodeUnit_Schema | The schema where the code unit referencing the missing element is deployed. |
| Caller_CodeUnit_Name | The name of the code unit referencing the missing element. |
| Caller_CodeUnit_FullName | The full qualified name of the code unit referencing the missing element. |
| Referenced_Element_Database | The database where the missing element is deployed. For now, only SQL Server objects can have a database. |
| Referenced_Element_Schema | The schema where the missing element is deployed. |
| Referenced_Element_Name | The name of the missing element. |
| Referenced_Element_FullName | The full qualified name of the missing element. |
| Line | The line number inside the file where the reference is located. |
| Relation_Type | Shows the type of relation used through the caller code unit and the MISSING reference. |

### Known Issues

> **Warning:**
>
> Variables defined in shell files used in script files like .bteq are considered missing objects because their definition is not part of the input files that SnowConvert AI processes. E.g. the `myDB` variable is defined in the shell file but this is a file that is not part of the input for SnowConvert AI. Only the .bteq file will be processed and therefore, line 5 will be marked as a missing reference.

```sh
export myDB=exampleDatabase
bteq < example.bteq
```

```sql
.LABEL EX_SQE

create multiset volatile table DR as
   select * from ${myDB}.myTable;
```

> **Warning:**
>
> Preprocessing an Oracle workload by splitting packages can result in extra missing references if the package’s schema is not specified in the extracted objects.

**Original Code**

```sql
CREATE package Schema1.Package1
IS
  CREATE TABLE Table1 (
    col1 INTEGER
  );

  CREATE PROCEDURE Proc1
    BEGIN
      SELECT * FROM Schema1.Table1;
    END

END
```

Notice that in this case, `Table1` is automatically created within the schema `Schema1`, so the reference in line 9 resolves correctly. However, if a package split process is executed prior to the migration and the resulting files are like these ones:

**Modified Code after a package split process**

```sql
  CREATE TABLE Table1 (
    col1 INTEGER1
  );
```

```sql
CREATE PROCEDURE Proc1
    BEGIN
        SELECT * FROM Schema1.Table1;
    END
```

The reference on line 3 of the file `Schema1_Proc1.sql` will be marked as a missing reference, because `Table1` was not explicitly created within the schema `Schema1`.
