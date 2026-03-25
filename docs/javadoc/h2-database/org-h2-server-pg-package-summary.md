# Package org.h2.server.pg

---

package org.h2.server.pg

PostgreSQL server implementation of this database.

- 

Related Packages

Package
Description
org.h2.server

A TCP server.

org.h2.server.web

The H2 Console tool.

- 

Classes

Class
Description
PgServer

This class implements a subset of the PostgreSQL protocol as described here:
 https://www.postgresql.org/docs/devel/protocol.html
 The PostgreSQL catalog is described here:
 https://www.postgresql.org/docs/7.4/catalogs.html

PgServerThread

One server thread is opened for each client.