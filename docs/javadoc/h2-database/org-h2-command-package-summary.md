# Package org.h2.command

---

package org.h2.command

This package contains the parser and the base classes for prepared SQL
 statements.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.command.ddl

Contains DDL (data definition language) and related SQL statements.

org.h2.command.dml

Contains DML (data manipulation language) and related SQL statements.

org.h2.command.query

Contains queries.

- 

Class
Description
Command

Represents a SQL statement.

CommandContainer

Represents a single SQL statements.

CommandInterface

Represents a SQL statement.

CommandRemote

Represents the client-side part of a SQL statement.

Parser

The parser is used to convert a SQL statement string to an command object.

ParserBase

The base class for the parser.

Prepared

A prepared statement.

QueryScope

The scope of identifiers for a query with the WITH clause.

Token

Token.

Tokenizer

Tokenizer.