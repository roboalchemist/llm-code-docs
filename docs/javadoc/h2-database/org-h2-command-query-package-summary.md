# Package org.h2.command.query

---

package org.h2.command.query

Contains queries.

- 

Related Packages

Package
Description
org.h2.command

This package contains the parser and the base classes for prepared SQL
 statements.

org.h2.command.ddl

Contains DDL (data definition language) and related SQL statements.

org.h2.command.dml

Contains DML (data manipulation language) and related SQL statements.

- 

Class
Description
AllColumnsForPlan

This information is expensive to compute for large queries, so do so
 on-demand.

ForUpdate

FOR UPDATE clause.

ForUpdate.Type

Type of FOR UPDATE clause.

Query

Represents a SELECT statement (simple, or union).

QueryOrderBy

Describes one element of the ORDER BY clause of a query.

Select

This class represents a simple SELECT statement.

SelectGroups

Grouped data for aggregates.

SelectListColumnResolver

This class represents a column resolver for the column list of a SELECT
 statement.

SelectUnion

Represents a union SELECT statement.

SelectUnion.UnionType
 
TableValueConstructor

Table value constructor.