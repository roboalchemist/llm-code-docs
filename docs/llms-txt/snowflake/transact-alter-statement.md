# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/transact/transact-alter-statement.md

# SnowConvert AI - SQL Server-Azure Synapse - ALTER

Translation reference for all the DDL statements that are preceded by the `ALTER` keyword.

## TABLE

### Description

Modifies a table definition by altering, adding, or dropping columns and constraints. ALTER TABLE also reassigns and rebuilds partitions, or disables and enables constraints and triggers. (<https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql>)

## CHECK CONSTRAINT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

When the constraint that was being added in the SQL Server code is not supported at all in Snowflake, SnowConvert AI comments out the Check constraint statement, since it’s no longer valid.

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE
    [Person].[EmailAddress] CHECK CONSTRAINT [FK_EmailAddress_Person_BusinessEntityID]
GO
```

#### Snowflake

```sql
!!!RESOLVE EWI!!! /*** SSC-EWI-0035 - CHECK STATEMENT NOT SUPPORTED ***/!!!
ALTER TABLE IF EXISTS Person.EmailAddress CHECK CONSTRAINT FK_EmailAddress_Person_BusinessEntityID;
```

### Known Issues

* 1. The invalid CHECK CONSTRAINT is commented out leaving an invalid ALTER TABLE statement.

### Related EWIs

* [SSC-EWI-0035](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Check statement not supported.

## ADD

### Description

> **Note:**
>
> In SQL Server, the ADD clause permits multiple actions per ADD, whereas Snowflake only allows a sequence of ADD column actions. Consequently, SnowConvert AI divides the ALTER TABLE ADD clause into individual ALTER TABLE statements.

There is a subset of functionalities provided by the ADD keyword, allowing the addition of different elements to the target table. These include:

* Column definition
* Computed column definition
* Table constraint
* Column set definition

## TABLE CONSTRAINT

Applies to

* SQL Server

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Specifies the properties of a PRIMARY KEY, FOREIGN KEY, UNIQUE, or CHECK constraint that is part of a new column definition added to a table by using [ALTER TABLE](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql?view=sql-server-ver16). (<https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-column-constraint-transact-sql>)

Translation for column constraints is relatively straightforward. There are several parts of the syntax that are not required or not supported in Snowflake.

These parts include:

* `CLUSTERED | NONCLUSTERED`
* `WITH FILLFACTOR = fillfactor`
* `WITH ( index_option [, ...n ] )`
* `ON { partition_scheme_name ( partition_column_name ) | filegroup | "default" }`
* `NOT FOR REPLICATION`
* `CHECK [ NOT FOR REPLICATION ]`

#### Syntax in SQL Server

```sql
 [ CONSTRAINT constraint_name ]
{
    { PRIMARY KEY | UNIQUE }
        [ CLUSTERED | NONCLUSTERED ]
        (column [ ASC | DESC ] [ ,...n ] )
        [ WITH FILLFACTOR = fillfactor
        [ WITH ( <index_option>[ , ...n ] ) ]
        [ ON { partition_scheme_name ( partition_column_name ... )  | filegroup | "default" } ]
    | FOREIGN KEY
        ( column [ ,...n ] )
        REFERENCES referenced_table_name [ ( ref_column [ ,...n ] ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ NOT FOR REPLICATION ]
    | CONNECTION
        ( { node_table TO node_table }
          [ , {node_table TO node_table }]
          [ , ...n ]
        )
        [ ON DELETE { NO ACTION | CASCADE } ]
    | DEFAULT constant_expression FOR column [ WITH VALUES ]
    | CHECK [ NOT FOR REPLICATION ] ( logical_expression )
}
```

#### Syntax in [**Snowflake**](https://docs.snowflake.com/en/sql-reference/sql/create-table-constraint.html#inline-unique-primary-foreign-key)

```sql
 inlineUniquePK ::=
  [ CONSTRAINT <constraint_name> ]
  { UNIQUE | PRIMARY KEY }
  [ [ NOT ] ENFORCED ]
  [ [ NOT ] DEFERRABLE ]
  [ INITIALLY { DEFERRED | IMMEDIATE } ]
  [ ENABLE | DISABLE ]
  [ VALIDATE | NOVALIDATE ]
  [ RELY | NORELY ]

 [ CONSTRAINT <constraint_name> ]
  { UNIQUE | PRIMARY KEY }
  [ [ NOT ] ENFORCED ]
  [ [ NOT ] DEFERRABLE ]
  [ INITIALLY { DEFERRED | IMMEDIATE } ]
  [ ENABLE | DISABLE ]
  [ VALIDATE | NOVALIDATE ]
  [ RELY | NORELY ]
```

### Sample Source Patterns

#### Multiple ALTER TABLE instances

##### SQL Server

```sql
 -- PRIMARY KEY
ALTER TABLE
    [Person]
ADD
    CONSTRAINT [PK_EmailAddress_BusinessEntityID_EmailAddressID] PRIMARY KEY CLUSTERED (
        [BusinessEntityID] ASC,
        [EmailAddressID] ASC
    ) ON [PRIMARY]
GO

-- FOREING KEY TO ANOTHER TABLE
ALTER TABLE
    [Person].[EmailAddress] WITH CHECK
ADD
    CONSTRAINT [FK_EmailAddress_Person_BusinessEntityID] FOREIGN KEY([BusinessEntityID]) REFERENCES [Person].[Person] ([BusinessEntityID]) ON DELETE CASCADE
GO
```

##### Snowflake

```sql
 -- PRIMARY KEY
ALTER TABLE Person
ADD
    CONSTRAINT PK_EmailAddress_BusinessEntityID_EmailAddressID PRIMARY KEY (BusinessEntityID, EmailAddressID);

-- FOREING KEY TO ANOTHER TABLE
ALTER TABLE Person.EmailAddress
!!!RESOLVE EWI!!! /*** SSC-EWI-0035 - CHECK STATEMENT NOT SUPPORTED ***/!!!
WITH CHECK
ADD
    CONSTRAINT FK_EmailAddress_Person_BusinessEntityID FOREIGN KEY(BusinessEntityID) REFERENCES Person.Person (BusinessEntityID) ON DELETE CASCADE ;
```

#### DEFAULT within constraints

##### SQL Server

```sql
CREATE TABLE Table1
(
   COL_VARCHAR VARCHAR,
   COL_INT INT,
   COL_DATE DATE
);

ALTER TABLE
    Table1
ADD
    CONSTRAINT [DF_Table1_COL_INT] DEFAULT ((0)) FOR [COL_INT]
GO

ALTER TABLE
    Table1
ADD
    COL_NEWCOLUMN VARCHAR,
    CONSTRAINT [DF_Table1_COL_VARCHAR] DEFAULT ('NOT DEFINED') FOR [COL_VARCHAR]
GO

ALTER TABLE
    Table1
ADD
    CONSTRAINT [DF_Table1_COL_DATE] DEFAULT (getdate()) FOR [COL_DATE]
GO
```

##### Snowflake

```sql
CREATE OR REPLACE TABLE Table1 (
   COL_VARCHAR VARCHAR DEFAULT ('NOT DEFINED'),
   COL_INT INT DEFAULT ((0)),
   COL_DATE DATE DEFAULT (CURRENT_TIMESTAMP() :: TIMESTAMP)
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE Table1
--ADD
--    CONSTRAINT DF_Table1_COL_INT DEFAULT ((0)) FOR COL_INT
                                                          ;

ALTER TABLE Table1
ADD COL_NEWCOLUMN VARCHAR;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE Table1
--ADD
--CONSTRAINT DF_Table1_COL_VARCHAR DEFAULT ('NOT DEFINED') FOR COL_VARCHAR
                                                                        ;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE Table1
--ADD
--    CONSTRAINT DF_Table1_COL_DATE DEFAULT (CURRENT_TIMESTAMP() :: TIMESTAMP) FOR COL_DATE
                                                                                         ;
```

### Known Issues

**1. DEFAULT is only supported within** `CREATE TABLE` and `ALTER TABLE ... ADD COLUMN`

SQL Server supports defining a `DEFAULT` property within a constraint, while Snowflake only allows that when adding the column through `CREATE TABLE` or `ALTER TABLE ... ADD COLUMN`. `DEFAULT` properties within the `ADD CONSTRAINT` syntax are not supported and will be translated to ALTER TABLE ALTER COLUMN.

### Related EWIs

1. [SSC-EWI-0035](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Check statement not supported.
2. [SSC-EWI-0040](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Statement Not Supported.
3. [SSC-FDM-TS0020](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): Default constraint was commented out and may have been added to a table definition.

## CHECK

Applies to

* SQL Server

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

When CHECK clause is in the ALTER statement, SnowConvert AI will comment out the entire statement, since it is not supported.

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE dbo.doc_exd
ADD CONSTRAINT exd_check CHECK NOT FOR REPLICATION (column_a > 1);
```

#### Snowflake

```sql
!!!RESOLVE EWI!!! /*** SSC-EWI-0035 - CHECK STATEMENT NOT SUPPORTED ***/!!!
ALTER TABLE dbo.doc_exd
ADD CONSTRAINT exd_check CHECK NOT FOR REPLICATION (column_a > 1);
```

### Known Issues

**1.** **ALTER TABLE CHECK clause is not supported in Snowflake.**

The entire ALTER TABLE CHECK clause is commented out, since it is not supported in Snowflake.

### Related EWIs

* [SSC-EWI-0035](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Check statement not supported.

## CONNECTION

Applies to

* SQL Server

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

When CONNECTION clause is in the ALTER statement, SnowConvert AI will comment out the entire statement, since it is not supported.

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE bought
ADD COL2 VARCHAR(32), CONSTRAINT EC_BOUGHT1 CONNECTION (Customer TO Product, Supplier TO Product)
ON DELETE NO ACTION;
```

#### Snowflake

```sql
ALTER TABLE bought
ADD COL2 VARCHAR(32);

!!!RESOLVE EWI!!! /*** SSC-EWI-0109 - ALTER TABLE SYNTAX NOT APPLICABLE IN SNOWFLAKE ***/!!!
ALTER TABLE bought
ADD
CONSTRAINT EC_BOUGHT1 CONNECTION (Customer TO Product, Supplier TO Product)
ON DELETE NO ACTION;
```

### Known Issues

**1.** **ALTER TABLE CONNECTION clause is not supported in Snowflake.**

The entire ALTER TABLE CONNECTION clause is commented out, since it is not supported in Snowflake.

### Related EWIs

* [SSC-EWI-0109](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Alter Table syntax is not applicable in Snowflake.

## DEFAULT

Applies to

* SQL Server

### Description

When DEFAULT clause is in the ALTER statement, SnowConvert AI will comment out the entire statement, since it is not supported.

The only functional scenario happens when the table definition is on the same file, in this way the default is added in the column definition.

### Sample Source Patterns

#### SQL Server

```sql
CREATE TABLE table1
(
  col1 integer not null,
  col2 varchar collate Latin1_General_CS,
  col3 date not null
)

ALTER TABLE table1
ADD CONSTRAINT col1_constraint DEFAULT 50 FOR col1;

ALTER TABLE table1
ADD CONSTRAINT col2_constraint DEFAULT 'hello world' FOR col2;

ALTER TABLE table1
ADD CONSTRAINT col3_constraint DEFAULT getdate() FOR col3;
```

#### Snowflake

```sql
CREATE OR REPLACE TABLE table1 (
  col1 INTEGER not null DEFAULT 50,
  col2 VARCHAR COLLATE 'EN-CS' DEFAULT 'hello world',
  col3 DATE not null DEFAULT CURRENT_TIMESTAMP() :: TIMESTAMP
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE table1
--ADD CONSTRAINT col1_constraint DEFAULT 50 FOR col1
                                                  ;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE table1
--ADD CONSTRAINT col2_constraint DEFAULT 'hello world' FOR col2
                                                             ;

----** SSC-FDM-TS0020 - DEFAULT CONSTRAINT MAY HAVE BEEN ADDED TO TABLE DEFINITION **

--ALTER TABLE table1
--ADD CONSTRAINT col3_constraint DEFAULT CURRENT_TIMESTAMP() :: TIMESTAMP FOR col3
                                                                                ;
```

### Known Issues

**1. ALTER TABLE DEFAULT clause is not supported in Snowflake.**

The entire ALTER TABLE DEFAULT clause is commented out, since it is not supported in Snowflake.

### Related EWIs

1. [SSC-FDM-TS0020](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): Default constraint was commented out and may have been added to a table definition.

## FOREIGN KEY

Applies to

* SQL Server

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

Snowflake supports the grammar for Referential Integrity Constraints, and their properties to facilitate the migration from other databases.

#### SQL Server

```sql
FOREIGN KEY
        ( column [ ,...n ] )
        REFERENCES referenced_table_name [ ( ref_column [ ,...n ] ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ NOT FOR REPLICATION ]
```

#### Snowflake

```sql
  [ FOREIGN KEY ]
  REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
  [ MATCH { FULL | SIMPLE | PARTIAL } ]
  [ ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
       [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ] ]
  [ [ NOT ] ENFORCED ]
  [ [ NOT ] DEFERRABLE ]
  [ INITIALLY { DEFERRED | IMMEDIATE } ]
  [ ENABLE | DISABLE ]
  [ VALIDATE | NOVALIDATE ]
  [ RELY | NORELY ]
```

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE [Tests].[dbo].[Employee]
ADD CONSTRAINT FK_Department FOREIGN KEY(DepartmentID) REFERENCES Department(DepartmentID)
ON UPDATE CASCADE
ON DELETE NO ACTION
NOT FOR REPLICATION;
```

#### Snowflake

```sql
ALTER TABLE Tests.dbo.Employee
ADD CONSTRAINT FK_Department FOREIGN KEY(DepartmentID) REFERENCES Department (DepartmentID)
ON UPDATE CASCADE
ON DELETE NO ACTION;
```

> **Note:**
>
> Constraints are not enforced in Snowflake, excepting NOT NULL.
>
> Primary and Foreign Key are only used for documentation purposes more than design constraints.

## ON PARTITION

Applies to

* SQL Server

> **Note:**
>
> Non-relevant statement.

> **Warning:**
>
> Notice that this statement is removed from the migration because it is a non-relevant syntax. It means that it is not required in Snowflake.

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

In Transact SQL Server, the `on partition` statement is used inside `alter` statements and is used to divide the data across the database. For more information, see the [SQL Server partitioned tables and indexes documentation](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver16).

### Sample Source Patterns

#### On Partition

Notice that in this example the `ON PARTITION` has been removed. This is because Snowflake provides an integrated partitioning methodology. Thus, the syntax is not relevant.

##### SQL SERVER

```sql
ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE
ON partition_scheme_name (partition_column_name);
```

##### Snowflake

```sql
ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE;
```

## PRIMARY KEY

Applies to

* SQL Server

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

SQL Server primary key has many clauses that are not applicable for Snowflake. So, most of the statement will be commented out.

#### Syntax in SQL Server

```sql
{ PRIMARY KEY | UNIQUE }
[ CLUSTERED | NONCLUSTERED ]
(column [ ASC | DESC ] [ ,...n ] )
[ WITH FILLFACTOR = fillfactor
[ WITH ( <index_option>[ , ...n ] ) ]
[ ON { partition_scheme_name ( partition_column_name ... )  | filegroup | "default" } ]
```

#### Syntax in Snowflake

```sql
[ CONSTRAINT <constraint_name> ]
{ UNIQUE | PRIMARY KEY } ( <col_name> [ , <col_name> , ... ] )
[ [ NOT ] ENFORCED ]
[ [ NOT ] DEFERRABLE ]
[ INITIALLY { DEFERRED | IMMEDIATE } ]
[ ENABLE | DISABLE ]
[ VALIDATE | NOVALIDATE ]
[ RELY | NORELY ]
```

### Sample Source Patterns

> **Warning:**
>
> Notice that `WITH FILLFACTOR` statement has been removed from the translation because it is not relevant in Snowflake syntax.

#### SQL Server

```sql
ALTER TABLE Production.TransactionHistoryArchive
   ADD CONSTRAINT PK_TransactionHistoryArchive_TransactionID PRIMARY KEY
   CLUSTERED (TransactionID)
   WITH (FILLFACTOR = 75, ONLINE = ON, PAD_INDEX = ON)
   ON "DEFAULTLOCATION";
```

#### Snowflake

```sql
ALTER TABLE Production.TransactionHistoryArchive
   ADD CONSTRAINT PK_TransactionHistoryArchive_TransactionID PRIMARY KEY (TransactionID);
```

## COLUMN DEFINITION

ALTER TABLE ADD column_name

Applies to

* SQL Server
* Azure Synapse Analytics

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

### Description

Specifies the properties of a column that are added to a table by using [ALTER TABLE](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql?view=sql-server-ver16).

Adding a [column definition](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-column-definition-transact-sql?view=sql-server-ver16) in Snowflake does have some differences compared to SQL Server.

For instance, several parts of the SQL Server grammar are not required or entirely not supported by Snowflake. These include:

* FILESTREAM
* [ROWGUIDCOL](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-table-column-definition-transact-sql?view=sql-server-ver16)
* ENCRYPTED WITH …
* SPARSE

Additionally, a couple other parts are partially supported, and require additional work to be implemented to properly emulate the original functionality. Specifically, we’re talking about the `MASKED WITH` property, which will be covered in the patterns section of this page.

#### SQL Server

```sql
column_name <data_type>
[ FILESTREAM ]
[ COLLATE collation_name ]
[ NULL | NOT NULL ]
[
    [ CONSTRAINT constraint_name ] DEFAULT constant_expression [ WITH VALUES ]
    | IDENTITY [ ( seed , increment ) ] [ NOT FOR REPLICATION ]
]
[ ROWGUIDCOL ]
[ SPARSE ]
[ ENCRYPTED WITH
  ( COLUMN_ENCRYPTION_KEY = key_name ,
      ENCRYPTION_TYPE = { DETERMINISTIC | RANDOMIZED } ,
      ALGORITHM =  'AEAD_AES_256_CBC_HMAC_SHA_256'
  ) ]
[ MASKED WITH ( FUNCTION = ' mask_function ') ]
[ <column_constraint> [ ...n ] ]
```

#### Snowflake

```sql
ADD [ COLUMN ] <col_name> <col_type>
        [ { DEFAULT <expr> | { AUTOINCREMENT | IDENTITY } [ { ( <start_num> , <step_num> ) | START <num> INCREMENT <num> } ] } ]
                            /* AUTOINCREMENT (or IDENTITY) supported only for columns with numeric data types (NUMBER, INT, FLOAT, etc.). */
                            /* Also, if the table is not empty (i.e. rows exist in the table), only DEFAULT can be altered.               */
        [ inlineConstraint ]
        [ [ WITH ] MASKING POLICY <policy_name> [ USING ( <col1_name> , cond_col_1 , ... ) ] ]
```

### Sample Source Patterns

#### Basic pattern

This pattern showcases the removal of elements from the original ALTER TABLE.

##### SQL Server

```sql
ALTER TABLE table_name
ADD column_name INTEGER;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD column_name INTEGER;
```

#### COLLATE

Collation allows you to specify broader rules when talking about string comparison.

##### SQL Server

```sql
ALTER TABLE table_name
ADD COLUMN new_column_name VARCHAR
COLLATE Latin1_General_CI_AS;
```

Since the collation rule nomenclature varies from SQL Server to Snowflake, it is necessary to make adjustments.

##### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD COLUMN new_column_name VARCHAR COLLATE 'EN-CI-AS' /*** SSC-PRF-0002 - CASE INSENSITIVE COLUMNS CAN DECREASE THE PERFORMANCE OF QUERIES ***/;
```

#### MASKED WITH

This pattern showcases the translation for MASKED WITH property. CREATE OR REPLACE MASKING POLICY is inserted somewhere before the first usage, and then referenced by a SET MASKING POLICY clause.

The name of the new MASKING POLICY will be the concatenation of the name and arguments of the original MASKED WITH FUNCTION, as seen below:

##### SQL Server

```sql
ALTER TABLE table_name
ALTER COLUMN column_name
ADD MASKED WITH ( FUNCTION = ' random(1, 999) ' );
```

##### Snowflake

```sql
--** SSC-FDM-TS0022 - MASKING ROLE MUST BE DEFINED PREVIOUSLY BY THE USER **
CREATE OR REPLACE MASKING POLICY "random_1_999" AS
(val SMALLINT)
RETURNS SMALLINT ->
CASE
WHEN current_role() IN ('YOUR_DEFINED_ROLE_HERE')
THEN val
ELSE UNIFORM(1, 999, RANDOM()) :: SMALLINT
END;

ALTER TABLE IF EXISTS table_name MODIFY COLUMN column_name/*** SSC-FDM-TS0021 - A MASKING POLICY WAS CREATED AS SUBSTITUTE FOR MASKED WITH ***/  SET MASKING POLICY "random_1_999";
```

#### DEFAULT

This pattern showcases some of the basic translation scenarios for DEFAULT property.

##### SQL Server

```sql
ALTER TABLE table_name
ADD intcol INTEGER DEFAULT 0;

ALTER TABLE table_name
ADD varcharcol VARCHAR(20) DEFAULT '';

ALTER TABLE table_name
ADD datecol DATE DEFAULT CURRENT_TIMESTAMP;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD intcol INTEGER DEFAULT 0;

ALTER TABLE IF EXISTS table_name
ADD varcharcol VARCHAR(20) DEFAULT '';

ALTER TABLE IF EXISTS table_name
ADD datecol DATE
                 !!!RESOLVE EWI!!! /*** SSC-EWI-TS0078 - DEFAULT OPTION NOT ALLOWED IN SNOWFLAKE ***/!!!
                 DEFAULT CURRENT_TIMESTAMP;
```

#### ENCRYPTED WITH

This pattern showcases the translation for ENCRYPTED WITH property, which is commented out in the output code.

##### SQL Server

```sql
ALTER TABLE table_name
ADD encryptedcol VARCHAR(20)
ENCRYPTED WITH
  ( COLUMN_ENCRYPTION_KEY = key_name ,
      ENCRYPTION_TYPE = RANDOMIZED ,
      ALGORITHM =  'AEAD_AES_256_CBC_HMAC_SHA_256'
  );
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD encryptedcol VARCHAR(20)
----** SSC-FDM-TS0009 - ENCRYPTED WITH NOT SUPPORTED IN SNOWFLAKE **
--ENCRYPTED WITH
--  ( COLUMN_ENCRYPTION_KEY = key_name ,
--      ENCRYPTION_TYPE = RANDOMIZED ,
--      ALGORITHM =  'AEAD_AES_256_CBC_HMAC_SHA_256'
--  )
   ;
```

#### NOT NULL

The SQL Server NOT NULL clause has the same pattern and functionality as the Snowflake NOT NULL clause

##### SQL Server

```sql
ALTER TABLE table2 ADD
column_test INTEGER NOT NULL,
column_test2 INTEGER NULL,
column_test3 INTEGER;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table2 ADD column_test INTEGER NOT NULL;

ALTER TABLE IF EXISTS table2 ADD column_test2 INTEGER NULL;

ALTER TABLE IF EXISTS table2 ADD column_test3 INTEGER;
```

#### IDENTITY

This pattern showcases the translation for IDENTITY. The `NOT FOR REPLICATION` portion is removed in Snowflake.

##### SQL Server

```sql
ALTER TABLE table3 ADD
column_test INTEGER IDENTITY(1, 100) NOT FOR REPLICATION;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table3 ADD column_test INTEGER IDENTITY(1, 100) ORDER;
```

### Unsupported clauses

#### FILESTREAM

The original behavior of `FILESTREAM` is not replicable in Snowflake, and merits commenting out the entire `ALTER TABLE` statement.

##### SQL Server

```sql
ALTER TABLE table2
ADD column1 varbinary(max)
FILESTREAM;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table2
ADD column1 VARBINARY
!!!RESOLVE EWI!!! /*** SSC-EWI-0040 - THE 'FILESTREAM COLUMN OPTION' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
FILESTREAM;
```

#### SPARSE

In SQL Server, [SPARSE](https://docs.microsoft.com/en-us/sql/relational-databases/tables/use-sparse-columns) is used to define columns that are optimized for NULL storage. However, when we’re using Snowflake, we are not required to use this clause.

Snowflake performs [optimizations over tables](https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions.html#benefits-of-micro-partitioning) automatically, which mitigates the need for manual user-made optimizations.

##### SQL Server

```sql
-- ADD COLUMN DEFINITION form
ALTER TABLE table3
ADD column1 int NULL SPARSE;

----------------------------------------
/* It also applies to the other forms */
----------------------------------------

-- CREATE TABLE form
CREATE TABLE table3
(
    column1 INT SPARSE NULL
);

-- ALTER COLUMN form
ALTER TABLE table3
ALTER COLUMN column1 INT NULL SPARSE;
```

##### Snowflake

```sql
-- ADD COLUMN DEFINITION form
ALTER TABLE IF EXISTS table3
ALTER COLUMN column1
                     !!!RESOLVE EWI!!! /*** SSC-EWI-TS0061 - ALTER COLUMN COMMENTED OUT BECAUSE SPARSE COLUMN IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
                     INT NULL SPARSE;

----------------------------------------
/* It also applies to the other forms */
----------------------------------------

-- CREATE TABLE form
CREATE OR REPLACE TABLE table3
(
    column1 INT
                !!!RESOLVE EWI!!! /*** SSC-EWI-0040 - THE 'SPARSE COLUMN OPTION' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
                SPARSE NULL
)
COMMENT = '{"origin":"sf_sc","name":"snowconvert","version":{"major":1, "minor":0},"attributes":{"component":"transact"}}'
;

-- ALTER COLUMN form
ALTER TABLE IF EXISTS table3
ALTER COLUMN column1
                     !!!RESOLVE EWI!!! /*** SSC-EWI-TS0061 - ALTER COLUMN COMMENTED OUT BECAUSE SPARSE COLUMN IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
                     INT NULL SPARSE;
```

#### ROWGUIDCOL

##### SQL Server

```sql
ALTER TABLE table_name
ADD column_name UNIQUEIDENTIFIER
ROWGUIDCOL;
```

##### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD column_name VARCHAR
!!!RESOLVE EWI!!! /*** SSC-EWI-0040 - THE 'ROWGUIDCOL COLUMN OPTION' CLAUSE IS NOT SUPPORTED IN SNOWFLAKE ***/!!!
ROWGUIDCOL;
```

### Known Issues

**1. Roles and users have to be previously set up for masking policies**

Snowflake’s Masking Policies can be applied to columns only after the policies were created. This requires the user to create the policies and assign them to roles, and these roles to users, to work properly. Masking Policies can behave differently depending on which user is querying.

> **Warning:**
>
> SnowConvert AI does not perform this setup automatically.

**2. Masking policies require a Snowflake Enterprise account or higher.**

The Snowflake documentation states that masking policies are available on Enterprise or higher rank accounts.

> **Note:**
>
> For further details visit [CREATE MASKING POLICY — Snowflake Documentation](https://docs.snowflake.com/en/sql-reference/sql/create-masking-policy.html#create-masking-policy).

**3. DEFAULT only supports constant values**

SQL Server’s DEFAULT property is partially supported by Snowflake, as long as its associated value is a constant.

**4.** **FILESTREAM clause is not supported in Snowflake.**

The entire FILESTSTREAM clause is commented out, since it is not supported in Snowflake.

**5.** **SPARSE clause is not supported in Snowflake.**

The entire SPARSE clause is commented out, since it is not supported in Snowflake. When it is added within an ALTER COLUMN statement, and it’s the only modification being made to the column, the entire statement is removed since it’s no longer adding anything.

### Related EWIs

1. [SSC-EWI-0040](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Statement Not Supported.
2. [SSC-EWI-TS0061](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/sqlServerEWI.md): ALTER COLUMN not supported.
3. [SSC-EWI-TS0078](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/sqlServerEWI.md): Default value not allowed in Snowflake.
4. [SSC-FDM-TS0009](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): Encrypted with not supported in Snowflake.
5. [SSC-FDM-TS0021](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): A MASKING POLICY was created as a substitute for MASKED WITH.
6. [SSC-FDM-TS0022](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/sqlServerFDM.md): The user must previously define the masking role.
7. [SSC-PRF-0002](../../general/technical-documentation/issues-and-troubleshooting/performance-review/generalPRF.md): Case-insensitive columns can decrease the performance of queries.

## COLUMN CONSTRAINT

ALTER TABLE ADD COLUMN … COLUMN CONSTRAINT

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

Specifies the properties of a PRIMARY KEY, FOREIGN KEY or CHECK that is part of a new [column constraint](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-column-constraint-transact-sql?view=sql-server-ver16) added to a table by using [Alter Table.](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql?view=sql-server-ver16)

#### SQL Server

```sql
[ CONSTRAINT constraint_name ]
{
    [ NULL | NOT NULL ]
    { PRIMARY KEY | UNIQUE }
        [ CLUSTERED | NONCLUSTERED ]
        [ WITH FILLFACTOR = fillfactor ]
        [ WITH ( index_option [, ...n ] ) ]
        [ ON { partition_scheme_name (partition_column_name)
            | filegroup | "default" } ]
    | [ FOREIGN KEY ]
        REFERENCES [ schema_name . ] referenced_table_name
            [ ( ref_column ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ NOT FOR REPLICATION ]
    | CHECK [ NOT FOR REPLICATION ] ( logical_expression )
}
```

#### Snowflake

```sql
CREATE TABLE <name> ( <col1_name> <col1_type>    [ NOT NULL ] { inlineUniquePK | inlineFK }
                     [ , <col2_name> <col2_type> [ NOT NULL ] { inlineUniquePK | inlineFK } ]
                     [ , ... ] )

ALTER TABLE <name> ADD COLUMN <col_name> <col_type> [ NOT NULL ] { inlineUniquePK | inlineFK }
```

Where:

```sql
inlineUniquePK ::=
  [ CONSTRAINT <constraint_name> ]
  { UNIQUE | PRIMARY KEY }
  [ [ NOT ] ENFORCED ]
  [ [ NOT ] DEFERRABLE ]
  [ INITIALLY { DEFERRED | IMMEDIATE } ]
  [ ENABLE | DISABLE ]
  [ VALIDATE | NOVALIDATE ]
  [ RELY | NORELY ]
```

```sql
inlineFK :=
  [ CONSTRAINT <constraint_name> ]
  [ FOREIGN KEY ]
  REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
  [ MATCH { FULL | SIMPLE | PARTIAL } ]
  [ ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
       [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ] ]
  [ [ NOT ] ENFORCED ]
  [ [ NOT ] DEFERRABLE ]
  [ INITIALLY { DEFERRED | IMMEDIATE } ]
  [ ENABLE | DISABLE ]
  [ VALIDATE | NOVALIDATE ]
  [ RELY | NORELY ]
```

## CHECK

Applies to

* SQL Server

### Description

> **Note:**
>
> Some parts in the output code are omitted for clarity reasons.

When CHECK clause is in the ALTER statement, SnowConvert AI will comment out the entire statement, since it is not supported.

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE table_name
ADD column_name VARCHAR(255)
CONSTRAINT constraint_name
CHECK NOT FOR REPLICATION (column_name > 1);
```

#### Snowflake

```sql
ALTER TABLE IF EXISTS table_name
ADD column_name VARCHAR(255)
!!!RESOLVE EWI!!! /*** SSC-EWI-0035 - CHECK STATEMENT NOT SUPPORTED ***/!!!
CONSTRAINT constraint_name
CHECK NOT FOR REPLICATION (column_name > 1);
```

### Known Issues

**1.** **ALTER TABLE CHECK clause is not supported in Snowflake.**

The entire ALTER TABLE CHECK clause is commented out, since it is not supported in Snowflake.

### Related EWIs

* [SSC-EWI-0035](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Check statement not supported.

## FOREIGN KEY

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

The syntax for the Foreign Key is fully supported by Snowflake, except for the `[ NOT FOR REPLICATION ]` and the `WITH CHECK` clauses.

#### SQL Server

Review the following [SQL Server documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-table-transact-sql?view=sql-server-ver16#syntax-for-memory-optimized-tables) for more information.

```sql
[ FOREIGN KEY ]
REFERENCES [ schema_name . ] referenced_table_name
[ ( ref_column ) ]
[ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
[ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
[ NOT FOR REPLICATION ]
```

#### Snowflake

```sql
[ FOREIGN KEY ]
REFERENCES <ref_table_name> [ ( <ref_col_name> ) ]
[ MATCH { FULL | SIMPLE | PARTIAL } ]
[ ON [ UPDATE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ]
     [ DELETE { CASCADE | SET NULL | SET DEFAULT | RESTRICT | NO ACTION } ] ]
[ [ NOT ] ENFORCED ]
[ [ NOT ] DEFERRABLE ]
[ INITIALLY { DEFERRED | IMMEDIATE } ]
[ ENABLE | DISABLE ]
[ VALIDATE | NOVALIDATE ]
[ RELY | NORELY ]
```

### Sample Source Patterns

#### General case

##### SQL Server

```sql
ALTER TABLE dbo.student
ADD CONSTRAINT Fk_empid FOREIGN KEY(emp_id)
REFERENCES dbo.emp(id);

ALTER TABLE dbo.student
ADD CONSTRAINT Fk_empid FOREIGN KEY(emp_id)
REFERENCES dbo.emp(id)
NOT FOR REPLICATION;
```

##### Snowflake

```sql
ALTER TABLE dbo.student
ADD CONSTRAINT Fk_empid FOREIGN KEY(emp_id)
REFERENCES dbo.emp (id);

ALTER TABLE dbo.student
ADD CONSTRAINT Fk_empid FOREIGN KEY(emp_id)
REFERENCES dbo.emp (id);
```

#### WITH CHECK / NO CHECK case

Notice that Snowflake logic does not support the CHECK clause in the creation of foreign keys. The `WITH CHECK` statement is marked as not supported. Besides, the `WITH NO CHECK` clause is removed because it is the default behavior in Snowflake and the equivalence is the same.

Please, review the following examples to have a better understanding of the translation.

##### SQL Server

```sql
ALTER TABLE testTable
WITH CHECK ADD CONSTRAINT testFK1 FOREIGN KEY (table_id)
REFERENCES otherTable (Othertable_id);

ALTER TABLE testTable
WITH NOCHECK ADD CONSTRAINT testFK2 FOREIGN KEY (table_id)
REFERENCES otherTable (Othertable_id);
```

##### Snowflake

```sql
ALTER TABLE testTable
----** SSC-FDM-0014 - CHECK STATEMENT NOT SUPPORTED **
--WITH CHECK
           ADD CONSTRAINT testFK1 FOREIGN KEY (table_id)
REFERENCES otherTable (Othertable_id);

ALTER TABLE testTable
ADD CONSTRAINT testFK2 FOREIGN KEY (table_id)
REFERENCES otherTable (Othertable_id);
```

### Known Issues

**1.** **NOT FOR REPLICATION clause.**

Snowflake has a different approach to the replication cases. Please, review the following [documentation](https://docs.snowflake.com/en/user-guide/account-replication-considerations).

**2. WITH CHECK clause.**

Snowflake does not support the `WITH CHECK` statement. Review the following [documentation](https://docs.snowflake.com/en/sql-reference/constraints-overview) for more information.

## PRIMARY KEY / UNIQUE

Applies to

* SQL Server
* Azure Synapse Analytics

### Description

All of the optional clauses of the PRIMARY KEY / UNIQUE constraint are removed in Snowflake.

**Syntax in SQL Server**

```sql
{ PRIMARY KEY | UNIQUE }
    [ CLUSTERED | NONCLUSTERED ]
    [ WITH FILLFACTOR = fillfactor ]
    [ WITH ( index_option [, ...n ] ) ]
    [ ON { partition_scheme_name (partition_column_name)
        | filegroup | "default" } ]
```

### Sample Source Patterns

#### SQL Server

```sql
ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name PRIMARY KEY
NONCLUSTERED;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE
WITH FILLFACTOR = 80;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name PRIMARY KEY
WITH (PAD_INDEX = off);

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE
ON partition_scheme_name (partition_column_name);
```

#### Snowflake

```sql
ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name PRIMARY KEY;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name PRIMARY KEY;

ALTER TABLE table_name
ADD column_name INTEGER
CONSTRAINT constraint_name UNIQUE;
```
