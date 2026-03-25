# Package org.h2.jdbcx

---

package org.h2.jdbcx

Implementation of the extended JDBC API (package `javax.sql`).

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

- 

Class
Description
JdbcConnectionPool

A simple standalone JDBC connection pool.

JdbcConnectionPoolBackwardsCompat

Allows us to compile on older platforms, while still implementing the methods
 from the newer JDBC API.

JdbcDataSource

A data source for H2 database connections.

JdbcDataSourceBackwardsCompat

Allows us to compile on older platforms, while still implementing the methods
 from the newer JDBC API.

JdbcDataSourceFactory

This class is used to create new DataSource objects.

JdbcXAConnection

This class provides support for distributed transactions.

JdbcXid

An object of this class represents a transaction id.