# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/review-results/reports/object-references-report.md

# SnowConvert AI - Object References Report

> **Note:**
>
> Built-in elements are not considered as part of this report.

## What is an “Object Reference”?

An object reference is the term used to refer to DDL definitions in the source code, that are being referenced by code units. The table below shows which elements could be referenced in each supported language.

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

The object references report can be found in a folder named *“reports”*, in the output folder of your conversion. The name of the file itself starts with *“ObjectReferences”* so it can easily be located.

The format of the file is **.CSV**.

### What information does it contain?

The object references report contains the following information about all the references found while converting:

| Column | Description |
| --- | --- |
| PartitionKey | The unique identifier of the conversion. |
| FileName | The name of the file in which the object is located. |
| Caller_CodeUnit | The type of the code unit referencing an existing element. |
| Caller_CodeUnit_Database | The database of the code unit referencing an existing element. For now, only SQL Server objects can have a database. |
| Caller_CodeUnit_Schema | The schema of the code unit referencing an existing element. |
| Caller_CodeUnit_Name | The name of the code unit referencing an existing element. |
| Caller_CodeUnit_FullName | The fully qualified name of the object referencing an existing element. |
| Referenced_Element_Type | The DDL type of the referenced element. |
| Referenced_Element_Database | The database of the referenced element. For now, only SQL Server objects can have a database. |
| Referenced_Element_Schema | The schema of the referenced element. |
| Referenced_Element_Name | The name of the referenced element. |
| Referenced_Element_FullName | The full qualified name of the referenced element. |
| Line | The line number inside the file where the reference is located. |
| Relation_Type | Shows the type of relation used through the caller code unit and the object reference. |

### Oracle Database Links as object references

To get the information such as database name, schema name, or object name of database link references, we need to know how the database link was defined. Database links contain the most relevant information in the connection string used in its definition. E.g.

#### Database Link with database name

```sql
 CREATE DATABASE LINK remote_hr_db
CONNECT TO hr_user
IDENTIFIED BY hr_password
USING 'RemoteDB';

SELECT * FROM hr.employees@remote_hr_db;
```

Using the example above, the object reference information should look like this:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_Database | Referenced_Element_Schema | Referenced_Element_Name | Referenced_Element_FullName | Line |
| --- | --- | --- | --- | --- | --- | --- |
| SELECT | CREATE DATABASE LINK | RemoteDb | N/A | remote_hr_db | hr.employees@remote_hr_db | 6 |

#### Database Link with database and schema names

```sql
 CREATE DATABASE LINK remote_hr_db1
CONNECT TO hr_user
IDENTIFIED BY hr_password
USING 'RemoteDB.MySchema';

SELECT * FROM employees@remote_hr_db1;
```

Using the example above, the object reference information should look like this:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_Database | Referenced_Element_Schema | Referenced_Element_Name | Referenced_Element_FullName | Line |
| --- | --- | --- | --- | --- | --- | --- |
| SELECT | CREATE DATABASE LINK | RemoteDb | MySchema | remote_hr_db1 | hr.employees@remote_hr_db1 | 6 |

##### Database Link with a connection string

```sql
 CREATE DATABASE LINK remote_hr_db2
CONNECT TO hr_user
IDENTIFIED BY hr_password
USING '(DESCRIPTION=(
          ADDRESS=
          (PROTOCOL=TCP)
          (HOST=10.48.195.17)
          (PORT=1521))
      (CONNECT_DATA=(SID=MyDB)))';

SELECT * FROM employees@remote_hr_db2;
```

Using the example above, the object reference information should look like this:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_Database | Referenced_Element_Schema | Referenced_Element_Name | Referenced_Element_FullName | Line |
| --- | --- | --- | --- | --- | --- | --- |
| SELECT | CREATE DATABASE LINK | MyDB | N/A | remote_hr_db2 | employees@remote_hr_db2 | 6 |

### Relation Type

The relation type represents how a caller code unit is related to an object reference. SnowConvert AI is able to identify the following kinds of relations:

* FOREIGN KEY
* INSERT
* DELETE
* UPDATE
* CALL
* EXECUTE
* SYNONYM
* ALTER
* DROP
* MERGE
* TRUNCATE
* LOCK
* INDEX
* TABLE COLUMN
* GRANT
* REVOKE
* SELECT

  * COLUMN
  * FROM
  * WHERE
  * HAVING
  * GROUP BY
  * JOIN
  * ORDER BY

#### Examples

1. A stored procedure referencing a table through an UPDATE statement:

```sql
 CREATE TABLE TABLE2
(
  COL1 VARCHAR(50) NOT NULL,
  COL2 INT NOT NULL
);

CREATE OR REPLACE PROCEDURE Procedure01 (param1 NUMBER)
IS
BEGIN
    UPDATE TABLE2
    SET COL1 = 'Anderson'
    WHERE COL2 = param1;
END;
```

The report will show something like the following table:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_FullName | Line | Relation_Type |
| --- | --- | --- | --- | --- |
| CREATE PROCEDURE | CREATE TABLE | TABLE2 | 10 | UPDATE |

1. A table referencing another table through a FOREIGN KEY:

```sql
 CREATE TABLE TABLE1
(
  COL1 INT
);

CREATE TABLE TABLE2
(
  COL1 INT,
  CONSTRAINT FK_COL1 FOREIGN KEY (COL1)
    REFERENCES TABLE1(COL1)
);
```

The report will show something like the following table:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_FullName | Line | Relation_Type |
| --- | --- | --- | --- | --- |
| CREATE TABLE | CREATE TABLE | TABLE1 | 10 | FOREIGN KEY |

1. A table referenced by a view in the FROM clause of the SELECT statement:

```sql
 CREATE TABLE TABLE1
(
  COL1 INT
);

CREATE VIEW VIEW1
AS
SELECT * FROM TABLE1;
```

The report will show something like the following table:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_FullName | Line | Relation_Type |
| --- | --- | --- | --- | --- |
| CREATE VIEW | CREATE TABLE | TABLE1 | 8 | SELECT - FROM |

1. A user-defined function (UDF) referenced by a view as a result set column.

```sql
 CREATE FUNCTION FUNCTION1(PARAM1 INT)
RETURN NUMBER
IS
BEGIN
  RETURN(PARAM1 + 1);
END;

CREATE VIEW VIEW1
AS
SELECT FUNCTION1(*) FROM TABLE1;
```

The report will show something like the following table:

| Caller_CodeUnit | Referenced_Element_Type | Referenced_Element_FullName | Line | Relation_Type |
| --- | --- | --- | --- | --- |
| CREATE VIEW | CREATE FUNCTION | FUNCTION1 | 10 | SELECT - COLUMN |
