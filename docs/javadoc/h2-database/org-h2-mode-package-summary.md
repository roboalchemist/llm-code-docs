# Package org.h2.mode

---

package org.h2.mode

Utility classes for compatibility with other database, for example MySQL.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
DefaultNullOrdering

Default ordering of NULL values.

FunctionInfo

This class contains information about a built-in function.

FunctionsDB2Derby

Functions for `Mode.ModeEnum.DB2` and
 `Mode.ModeEnum.Derby` compatibility modes.

FunctionsLegacy

This class implements some legacy functions not available in Regular mode.

FunctionsMSSQLServer

Functions for `Mode.ModeEnum.MSSQLServer` compatibility
 mode.

FunctionsMySQL

This class implements some MySQL-specific functions.

FunctionsOracle

Functions for `Mode.ModeEnum.Oracle` compatibility mode.

FunctionsPostgreSQL

Functions for `Mode.ModeEnum.PostgreSQL` compatibility
 mode.

ModeFunction

Base class for mode-specific functions.

OnDuplicateKeyValues

VALUES(column) function for ON DUPLICATE KEY UPDATE clause.

PgCatalogSchema

`pg_catalog` schema.

PgCatalogTable

This class is responsible to build the pg_catalog tables.

Regclass

A ::regclass expression.

ToDateParser

Emulates Oracle's TO_DATE function.

 This class holds and handles the input data form the TO_DATE-method