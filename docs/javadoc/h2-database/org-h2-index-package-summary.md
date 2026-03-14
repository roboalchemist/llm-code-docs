# Package org.h2.index

---

package org.h2.index

Various table index implementations, as well as cursors to navigate in an
 index.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
Cursor

A cursor is a helper object to iterate through an index.

DualIndex

An index for the DUAL table.

Index

An index.

IndexCondition

An index condition object is made for each condition that can potentially use
 an index.

IndexCursor

The filter used to walk through an index.

IndexSort

Index-sorting information.

IndexType

Represents information about the properties of an index

LinkedCursor

The cursor implementation for the linked index.

LinkedIndex

A linked index is a index for a linked (remote) table.

MetaCursor

An index for a meta data table.

MetaIndex

The index implementation for meta data tables.

QueryExpressionCursor

The cursor implementation of a query expression index.

QueryExpressionIndex

This object represents a virtual index for a query expression.

RangeIndex

An index for the SYSTEM_RANGE table.

RecursiveIndex

A recursive index.

RegularQueryExpressionIndex

A regular query expression index.

SingleRowCursor

A cursor with at most one row.

SpatialIndex

A spatial index.

VirtualConstructedTableIndex

An index for a virtual table that returns a result set.

VirtualTableIndex

An base class for indexes of virtual tables.