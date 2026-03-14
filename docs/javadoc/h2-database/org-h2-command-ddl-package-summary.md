# Package org.h2.command.ddl

---

package org.h2.command.ddl

Contains DDL (data definition language) and related SQL statements.

- 

Related Packages

Package
Description
org.h2.command

This package contains the parser and the base classes for prepared SQL
 statements.

org.h2.command.dml

Contains DML (data manipulation language) and related SQL statements.

org.h2.command.query

Contains queries.

- 

Classes

Class
Description
AlterDomain

The base class for ALTER DOMAIN commands.

AlterDomainAddConstraint

This class represents the statement ALTER DOMAIN ADD CONSTRAINT

AlterDomainDropConstraint

This class represents the statement ALTER DOMAIN DROP CONSTRAINT

AlterDomainExpressions

This class represents the statements
 ALTER DOMAIN SET DEFAULT
 ALTER DOMAIN DROP DEFAULT
 ALTER DOMAIN SET ON UPDATE
 ALTER DOMAIN DROP ON UPDATE

AlterDomainRename

This class represents the statement
 ALTER DOMAIN RENAME

AlterDomainRenameConstraint

This class represents the statement
 ALTER DOMAIN RENAME CONSTRAINT

AlterIndexRename

This class represents the statement
 ALTER INDEX RENAME

AlterSchemaRename

This class represents the statement
 ALTER SCHEMA RENAME

AlterSequence

This class represents the statement ALTER SEQUENCE.

AlterTable

The base class for ALTER TABLE commands.

AlterTableAddConstraint

This class represents the statement
 ALTER TABLE ADD CONSTRAINT

AlterTableAlterColumn

This class represents the statements
 ALTER TABLE ADD,
 ALTER TABLE ADD IF NOT EXISTS,
 ALTER TABLE ALTER COLUMN,
 ALTER TABLE ALTER COLUMN SELECTIVITY,
 ALTER TABLE ALTER COLUMN SET DEFAULT,
 ALTER TABLE ALTER COLUMN DROP DEFAULT,
 ALTER TABLE ALTER COLUMN DROP EXPRESSION,
 ALTER TABLE ALTER COLUMN SET NULL,
 ALTER TABLE ALTER COLUMN DROP NULL,
 ALTER TABLE ALTER COLUMN SET VISIBLE,
 ALTER TABLE ALTER COLUMN SET INVISIBLE,
 ALTER TABLE DROP COLUMN

AlterTableDropConstraint

This class represents the statement
 ALTER TABLE DROP CONSTRAINT

AlterTableRename

This class represents the statement
 ALTER TABLE RENAME

AlterTableRenameColumn

This class represents the statement
 ALTER TABLE ALTER COLUMN RENAME

AlterTableRenameConstraint

This class represents the statement
 ALTER TABLE RENAME CONSTRAINT

AlterType

This class represents the statements ALTER TYPE

AlterUser

This class represents the statements
 ALTER USER ADMIN,
 ALTER USER RENAME,
 ALTER USER SET PASSWORD

AlterView

This class represents the statement
 ALTER VIEW

Analyze

This class represents the statements
 ANALYZE and ANALYZE TABLE

CommandWithColumns
 
CreateAggregate

This class represents the statement
 CREATE AGGREGATE

CreateConstant

This class represents the statement
 CREATE CONSTANT

CreateDomain

This class represents the statement
 CREATE DOMAIN

CreateFunctionAlias

This class represents the statement
 CREATE ALIAS

CreateIndex

This class represents the statement
 CREATE INDEX

CreateLinkedTable

This class represents the statement
 CREATE LINKED TABLE

CreateMaterializedView

This class represents the statement CREATE MATERIALIZED VIEW

CreateRole

This class represents the statement
 CREATE ROLE

CreateSchema

This class represents the statement
 CREATE SCHEMA

CreateSequence

This class represents the statement CREATE SEQUENCE.

CreateSynonym

This class represents the statement
 CREATE SYNONYM

CreateSynonymData

The data required to create a synonym.

CreateTable

This class represents the statement
 CREATE TABLE

CreateTableData

The data required to create a table.

CreateTrigger

This class represents the statement
 CREATE TRIGGER

CreateUser

This class represents the statement
 CREATE USER

CreateView

This class represents the statement
 CREATE VIEW

DeallocateProcedure

This class represents the statement
 DEALLOCATE

DefineCommand

This class represents a non-transaction statement, for example a CREATE or
 DROP.

DropAggregate

This class represents the statement
 DROP AGGREGATE

DropConstant

This class represents the statement
 DROP CONSTANT

DropDatabase

This class represents the statement
 DROP ALL OBJECTS

DropDomain

This class represents the statement DROP DOMAIN

DropFunctionAlias

This class represents the statement
 DROP ALIAS

DropIndex

This class represents the statement
 DROP INDEX

DropMaterializedView

This class represents the statement DROP MATERIALIZED VIEW

DropRole

This class represents the statement
 DROP ROLE

DropSchema

This class represents the statement
 DROP SCHEMA

DropSequence

This class represents the statement
 DROP SEQUENCE

DropSynonym

This class represents the statement
 DROP SYNONYM

DropTable

This class represents the statement
 DROP TABLE

DropTrigger

This class represents the statement
 DROP TRIGGER

DropUser

This class represents the statement
 DROP USER

DropView

This class represents the statement
 DROP VIEW

GrantRevoke

This class represents the statements
 GRANT RIGHT,
 GRANT ROLE,
 REVOKE RIGHT,
 REVOKE ROLE

PrepareProcedure

This class represents the statement
 PREPARE

RefreshMaterializedView

This class represents the statement REFRESH MATERIALIZED VIEW

SchemaCommand

This class represents a non-transaction statement that involves a schema.

SequenceOptions

Sequence options.

SetComment

This class represents the statement
 COMMENT

TruncateTable

This class represents the statement
 TRUNCATE TABLE