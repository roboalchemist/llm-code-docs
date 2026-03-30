# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/conversion-issues/db2EWI.md

# SnowConvert AI - IBM DB2 Issues

## SSC-EWI-DB0001

WITH ROW ACCESS POLICY CLAUSE DOES NOT SUPPORT MULTIPLE DECLARATION

### Severity

Low

### Description

This message is shown whenever SnowConvert AI detects multiple security label column options inside the same `CREATE TABLE` clause, the security label is translated to a row access policy clause and Snowflake does not support multiple row access policy declarations. Therefore, if more than one security labels are found they will be commented out with this EWI.

#### Code example

##### Input code

```sql
 CREATE TABLE T1
(
COL1 VARCHAR(10) COLUMN SECURED WITH securityLabel1,
COL2 VARCHAR(10) COLUMN SECURED WITH securityLabel2
);
```

##### Output code

```sql
CREATE TABLE T1
(
COL1 VARCHAR(10),
COL2 VARCHAR(10)
)
WITH ROW ACCESS POLICY securityLabel1 ON (
COL1
)
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0001 - WITH ROW ACCESS POLICY CLAUSE DOES NOT SUPPORT MULTIPLE DECLARATION IN SNOWFLAKE ***/!!!
WITH ROW ACCESS POLICY securityLabel2 ON (
COL2
)
;
```

### Recommendations

* Review your code and ensure that only one security label is inside the `CREATE TABLE` clause
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0003

PERIOD DEFINITION IS NOT SUPPORTED IN SNOWFLAKE.

### Severity

Medium

### Description

DB2 temporal tables do not have a functional equivalent in Snowflake. When an application-period or system-period temporal table declaration is found in the `CREATE TABLE` columns, that column is commented out from the resulting script. The behavior of the SELECT statement will differ from Snowflake because temporal tables are not part of the Snowflake solution and this causes the result to be different if the Select statement is migrated partially, see the example below for more information about this.

#### Select Query

```sql
 SELECT
  ID,
  Start,
  END
FROM
  timetable
FOR system_time as of '2022-05-09-16.20.17.0';
```

##### Result

| ID | START | END |
| --- | --- | --- |
| 1001 | 19:45.3 | 22:39.5 |
| 1002 | 19:45.5 | 22:39.6 |
| 1003 | 19:45.6 | 22:39.8 |
| 1004 | 19:45.7 | 00:00.0 |
| 1005 | 19:45.8 | 00:00.0 |
| 1006 | 19:46.0 | 00:00.0 |
| 7 | 16:21.8 | 00:00.0 |

If the Select statement is migrated partially we get a very different result as shown below.

##### Select Query

```sql
 SELECT
  ID,
  Start,
  END
FROM
  timetable
-- FOR system_time as of '2022-05-09-16.20.17.0';
```

##### Result

|  |  |  |
| --- | --- | --- |
| ID | START | END |
| 2001 | 22:39.5 | 00:00.0 |
| 2002 | 22:39.6 | 00:00.0 |
| 2003 | 22:39.8 | 00:00.0 |
| 1004 | 19:45.7 | 00:00.0 |
| 1005 | 19:45.8 | 00:00.0 |
| 1006 | 19:46.0 | 00:00.0 |
| 7 | 16:21.8 | 00:00.0 |

#### Code example

##### DB2

##### Create table

```sql
CREATE TABLE TestTable (
COL1 DATE,
COL2 DATE,
PERIOD SYSTEM_TIME (COL1, COL2),
PERIOD BUSINESS_TIME (COL1, COL2)
```

##### Select Query

```sql
SELECT
   *
FROM
   Table1
FOR SYSTEM_TIME AS of Value
```

##### Snowflake

##### Create Table

```sql
CREATE TABLE TestTable (
COL1 DATE,
COL2 DATE,
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0003 - PERIOD SPECIFICATION IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
PERIOD SYSTEM_TIME (COL1, COL2),
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0003 - PERIOD SPECIFICATION IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
PERIOD BUSINESS_TIME (COL1, COL2)
)
```

##### Select Query

```sql
SELECT
   *
FROM
Table1
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0003 - PERIOD SPECIFICATION IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
FOR SYSTEM_TIME AS of Value
```

### Recommendations

* Snowflake allows the storage of historical table data for up to 90 days, to know more about this see [Understanding & Using Time Travel](https://docs.snowflake.com/en/user-guide/data-time-travel.html).
* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0004

OUTER TABLE REFERENCE NOT APPLICABLE IN SNOWFLAKE

### Severity

Low

### Description

This message is shown when an OUTER table reference is found in a FROM clause inside of a SELECT statement. This clause is used to include from subtables in the intermediate result table of the SELECT statement. Subtables are related to [typed tables](https://www.ibm.com/docs/en/db2/9.7?topic=tables-creating-typed) in the DB2 database, that are created with the [OF clause](https://docs.mobilize.net/snowconvert-limited-access/-MUuBuIkrrZbtDaKcru_/for-ibm-db2/translation-reference/statements/create-table/content-source/of-type) of the CREATE TABLE statement, which is also not supported in Snowflake.

#### Code example

##### Input code

```sql
Select * from OUTER(ATable);
Select * from ONLY(ATable);
```

##### Output code

```sql
Select * from
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0004 - OUTER TABLE REFERENCE IS NOT SUPPORTED IN SNOWFLAKE. ***/!!!
OUTER(ATable) AS AliasName;

Select * from
ATable;
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0005

MANIPULATION OF DATA IN VIEWS IS NOT SUPPORTED

### Severity

Medium

### Description

This message is shown when it is found in a CREATE VIEW a node or clause that is related to the data manipulation of rows in a CREATE VIEW. Note that in DB2 you can insert or update rows directly from a VIEW meanwhile in Snowflake this is not supported, because of this, nodes or clauses related to this functionality are commented and an EWI is added.

#### Code example

##### Input code

```sql
CREATE VIEW TestTableId2 AS Select * from TestTableId1 WITH ROW MOVEMENT;
```

##### Output code

```sql
 CREATE VIEW TestTableId2
 COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "db2",  "convertedOn": "09/02/2025",  "domain": "no-domain-provided" }}'
 AS Select * from
  TestTableId1
 !!!RESOLVE EWI!!! /*** SSC-EWI-DB0005 - MANIPULATION OF DATA IN VIEWS IS NOT SUPPORTED. ***/!!!
 WITH ROW MOVEMENT;
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0006

INTERMEDIATE RESULT TABLE IS NOT SUPPORTED

### Severity

Medium

### Description

This message is shown when a DATA CHANGE TABLE REFERENCE is found in a FROM Clause. A DATA CHANGE TABLE REFERENCE specifies an intermediate table, which consists of the rows that are changed by an UPDATE, DELETE or INSERT statement included in the DATA CHANGE TABLE REFERENCE.

In Snowflake, this is not supported, since it can’t modify the rows and return a result set of table at the same time, hence the Select is commented.

#### Code example

##### DB2 Input code

##### Select statement

```sql
 SELECT
   *
FROM
   OLD Table(UPDATE T1 SET NAME = 'Tony' where ID = 4)
```

##### Update statement

```sql
 UPDATE (SELECT EMPNO, SALARY, COMM,
     AVG(SALARY) OVER (PARTITION BY WORKDEPT),
     AVG(COMM) OVER (PARTITION BY WORKDEPT)
     FROM EMPLOYEE E) AS E(EMPNO, SALARY, COMM, AVGSAL, AVGCOMM)
   SET (SALARY, COMM) = (AVGSAL, AVGCOMM)
   WHERE EMPNO = '000120';

 UPDATE TABLE5
INCLUDE (col1 INT, col2 Varchar(10))
SET Column1 = 1;
```

##### Snowflake Output code

##### Select statement

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0006 - INTERMEDIATE RESULT TABLE IS NOT SUPPORTED. ***/!!!
   OLD Table(UPDATE T1 SET NAME = 'Tony' where ID = 4)
```

##### Update statement

```sql
UPDATE
       !!!RESOLVE EWI!!! /*** SSC-EWI-DB0006 - INTERMEDIATE RESULT TABLE IS NOT SUPPORTED. ***/!!!
 (SELECT EMPNO, SALARY, COMM,
       AVG(SALARY) OVER (PARTITION BY WORKDEPT),
       AVG(COMM) OVER (PARTITION BY WORKDEPT)
       FROM EMPLOYEE E) AS E(EMPNO, SALARY, COMM, AVGSAL, AVGCOMM)
       SET
       SALARY = AVGSAL,
       COMM = AVGCOMM
WHERE EMPNO = '000120';

UPDATE TABLE5
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0006 - INTERMEDIATE RESULT TABLE IS NOT SUPPORTED. ***/!!!
INCLUDE (col1 INT, col2 Varchar(10))
SET Column1 = 1;
```

#### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0007

QUERY AS INSERT TARGET NAME IS NOT SUPPORTED.

### Severity

Medium

### Description

Unlike DB2, Snowflake does not allow using SELECT query results as the target of an INSERT statement, requiring instead that data be inserted directly into tables or materialized views.

#### Code example

##### DB2

##### Query

```sql
 INSERT INTO
   (SELECT * FROM SOMEOTHERTABLE)
VALUES
   (DEFAULT);
```

##### Snowflake

##### Query

```sql
 INSERT INTO
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0007 - QUERY AS INSERT TARGET NAME IS NOT SUPPORTED ***/!!!
   (SELECT * FROM SOMEOTHERTABLE)
VALUES
   (DEFAULT);
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0008

DELETE FROM SELECT STATEMENT IS NOT SUPPORTED.

### Severity

Medium

### Description

Snowflake does not support the use of select queries in the From clause of a Delete statement. If the Delete statement is migrated partially we get an incomplete statement as the From clause will be empty.

#### Code example

##### DB2

##### Select Query

```sql
 DELETE FROM (
SELECT * FROM table1
)
```

##### Snowflake

##### Select Query

```sql
DELETE FROM
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0008 - DELETE FROM SELECT STATEMENT IS NOT SUPPORTED. ***/!!!
 (
SELECT * FROM table1
)
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0009

POSITIONED STATEMENT IS NOT SUPPORTED.

### Severity

Medium

### Description

Snowflake does not support the use of cursors as part of the Delete statement and Update statement. If the statement is migrated partially, we will get rid of the where clause in which the cursor is forming part, making it dangerous to delete or update the whole table.

#### Code example

##### DB2

##### Delete statement

```sql
 DELETE FROM table1
WHERE CURRENT OF cursor1
```

##### Update statement

```sql
 UPDATE table1
     SET col1 = 1
     WHERE CURRENT OF cursor1
```

##### Snowflake

##### Delete statement

```sql
DELETE FROM
table1
WHERE
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0009 - POSITIONED CURRENT OF IS NOT SUPPORTED. ***/!!! CURRENT OF cursor1
```

##### Update statement

```sql
UPDATE TABLE1
SET Column1 = 1
WHERE
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0009 - POSITIONED CURRENT OF IS NOT SUPPORTED. ***/!!!
 CURRENT OF cursor1;
```

### Recommendations

* For additional support, contact SnowConvert support at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com).

## SSC-EWI-DB0010

ATTRIBUTE NAME IS NOT SUPPORTED IN SNOWFLAKE

### Severity

Medium

### Description

This message is displayed when specifying the attribute of a structured type that is being set (called an attribute assignment). A structured type can be a subtype that allows attributes to be inherited from a supertype.

Snowflake does not support these types of structures.

For more information, see the [DB2 CREATE TYPE (structured) documentation](https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-type-structured).

#### Code Example

##### DB2

```sql
 UPDATE CIRCLES
     SET C..CENTER..X = C..CENTER..Y,
       C..CENTER..Y = C..CENTER..X
     WHERE ID = 999;
```

##### Snowflake

```sql
UPDATE CIRCLES
     SET
          !!!RESOLVE EWI!!! /*** SSC-EWI-DB0010 - ATTRIBUTE NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!! C..CENTER..X =
          !!!RESOLVE EWI!!! /*** SSC-EWI-DB0010 - ATTRIBUTE NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!! C..CENTER..Y,
          !!!RESOLVE EWI!!! /*** SSC-EWI-DB0010 - ATTRIBUTE NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
       C..CENTER..Y =
                      !!!RESOLVE EWI!!! /*** SSC-EWI-DB0010 - ATTRIBUTE NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!! C..CENTER..X
     WHERE ID = 999
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0011

ASSIGNMENT CLAUSE TYPE IS NOT SUPPORTED IN SNOWFLAKE

### Severity

Medium

### Description

This message is displayed when the assignment clause contains an expression not supported by Snowflake

### Cases

#### Update Statement

When an assignment clause presents a multi-column assignment of a row selection, an example of this can be found in the Code example section.

#### Code Example

##### DB2

```sql
 UPDATE EMPLOYEE EU
    SET (EU.COM, EU.SALARY) = (SELECT ES.SALARY FROM EMPLOYEE ES WHERE ES.WORKDEPT = EU.WORKDEPT)
    WHERE EU.EMPNO = '000120';
```

##### Snowflake

```sql
UPDATE EMPLOYEE EU
    SET
        !!!RESOLVE EWI!!! /*** SSC-EWI-DB0011 - ASSIGNMENT CLAUSE TYPE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
 (EU.COM, EU.SALARY) = (SELECT ES.SALARY FROM
         EMPLOYEE ES WHERE ES.WORKDEPT = EU.WORKDEPT)
    WHERE EU.EMPNO = '000120';
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0012

INVALID NAME AS INSERTION TARGET, USE OF VIEW NAME IS NOT SUPPORTED IN SNOWFLAKE

### Severity

Medium

### Description

Snowflake does not support the use of view name in the insert target name statement.

#### Code Example

##### DB2

```sql
 CREATE VIEW VIEW1 AS SELECT * FROM T;
INSERT INTO VIEW1 (COL1, COL2) VALUES (NULL, DEFAULT);
```

##### Snowflake

```sql
 CREATE VIEW PUBLIC.VIEW1
AS SELECT * FROM
PUBLIC.T;

!!!RESOLVE EWI!!! /*** SSC-EWI-DB0012 - INVALID NAME AS INSERTION TARGET, USE OF VIEW NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
INSERT INTO VIEW1 (COL1, COL2) VALUES (NULL,DEFAULT);
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0013

INVALID NAME AS DELETE TARGET, USE OF VIEW NAME IS NOT SUPPORTED IN SNOWFLAKE

### Severity

Medium

### Description

Snowflake does not support the use of view name in the delete target name statement. For this reason, the result query could not be valid

#### Code Example

##### DB2

```sql
 CREATE VIEW VIEW1 AS SELECT * FROM T;
DELETE FROM VIEW1
```

##### Snowflake

```sql
 CREATE VIEW PUBLIC.VIEW1
AS SELECT * FROM
PUBLIC.T;

DELETE FROM
!!!RESOLVE EWI!!! /*** SSC-EWI-DB0013 - INVALID NAME AS DELETE TARGET, USE OF VIEW NAME IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
 VIEW1
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)

## SSC-EWI-DB0014

THE USE OF EXTERNAL TABLE REFERENCES IS NOT SUPPORTED IN SNOWFLAKE

### Severity

Medium

### Description

Snowflake does not support the use of external tables in the Select statement. For this reason, the result query could not be valid

#### Code Example

##### DB2

```sql
 SELECT
   *
FROM
   EXTERNAL SOMENAME AS T1 LIKE TABLE2 USING(COMPRESS NO)
```

##### Snowflake

```sql
SELECT
   *
FROM
   !!!RESOLVE EWI!!! /*** SSC-EWI-DB0014 - THE USE OF EXTERNAL TABLE REFERENCES IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
   EXTERNAL SOMENAME AS T1 LIKE TABLE2 USING(COMPRESS NO)
```

### Recommendations

* If you need more support, you can email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
