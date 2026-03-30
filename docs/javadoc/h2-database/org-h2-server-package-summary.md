# Package org.h2.server

---

package org.h2.server

A TCP server.

- 

Related Packages

Package
Description
org.h2

Implementation of the JDBC driver.

org.h2.server.pg

PostgreSQL server implementation of this database.

org.h2.server.web

The H2 Console tool.

- 

Class
Description
Service

Classes implementing this interface usually provide a
 TCP/IP listener such as an FTP server.

ShutdownHandler

A shutdown handler is a listener for shutdown events.

TcpServer

The TCP server implements the native H2 database server protocol.

TcpServerThread

One server thread is opened per client connection.