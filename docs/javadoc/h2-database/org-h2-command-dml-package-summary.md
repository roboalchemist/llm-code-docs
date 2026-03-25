# Package org.h2.command.dml

---

package org.h2.command.dml

Contains DML (data manipulation language) and related SQL statements.

- 

Related Packages

Package
Description
org.h2.command

This package contains the parser and the base classes for prepared SQL
 statements.

org.h2.command.ddl

Contains DDL (data definition language) and related SQL statements.

org.h2.command.query

Contains queries.

- 

Classes

Class
Description
AlterTableSet

This class represents the statement
 ALTER TABLE SET

BackupCommand

This class represents the statement
 BACKUP

Call

This class represents the statement
 CALL.

CommandWithValues

Command that supports VALUES clause.

DataChangeStatement

Data change statement.

Delete

This class represents the statement
 DELETE

ExecuteImmediate

This class represents the statement
 EXECUTE IMMEDIATE.

ExecuteProcedure

This class represents the statement
 EXECUTE

Explain

This class represents the statement
 EXPLAIN

Help

This class represents the statement CALL.

Insert

This class represents the statement
 INSERT

Merge

This class represents the statement
 MERGE
 or the MySQL compatibility statement
 REPLACE

MergeUsing

This class represents the statement syntax
 MERGE INTO table alias USING...

NoOperation

Represents an empty statement or a statement that has no effect.

RunScriptCommand

This class represents the statement
 RUNSCRIPT

ScriptCommand

This class represents the statement
 SCRIPT

Set

This class represents the statement
 SET

SetClauseList

Set clause list.

SetSessionCharacteristics

This class represents the statement SET SESSION CHARACTERISTICS

SetTypes

The list of setting for a SET statement.

TransactionCommand

Represents a transactional statement.

Update

This class represents the statement
 UPDATE