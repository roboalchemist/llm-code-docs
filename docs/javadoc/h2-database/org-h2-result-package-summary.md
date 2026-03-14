# Package org.h2.result

---

package org.h2.result

Implementation of row and internal result sets.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
BatchResult

Result of a batch execution.

DefaultRow

The default implementation of a row in a table.

FetchedResult

Abstract fetched result.

LazyResult

Lazy execution support for queries.

LocalResult

A local result set contains all row data of a result set.

MergedResult

Merged result.

ResultColumn

A result set column of a remote result.

ResultExternal

This interface is used to extend the LocalResult class, if data does not fit
 in memory.

ResultInterface

The result interface is used by the LocalResult and ResultRemote class.

ResultRemote

The client side part of a result set that is kept on the server.

ResultTarget

A object where rows are written to.

ResultWithGeneratedKeys

Result of update command with optional generated keys.

ResultWithGeneratedKeys.WithKeys

Result of update command with generated keys;

ResultWithPaddedStrings

Result with padded fixed length strings.

Row

Represents a row in a table.

RowFactory

Creates rows.

RowFactory.DefaultRowFactory

Default implementation of row factory.

SearchRow

The base class for rows stored in a table, and for partial rows stored in the
 index.

SimpleResult

Simple in-memory result.

SimpleRowValue

A simple row that contains data for only one column.

SortOrder

A sort order represents an ORDER BY clause in a query.

Sparse

Class Sparse.

UpdatableRow

This class is used for updatable result sets.