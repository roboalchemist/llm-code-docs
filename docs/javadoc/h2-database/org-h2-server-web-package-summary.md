# Package org.h2.server.web

---

package org.h2.server.web

The H2 Console tool.

- 

Related Packages

Package
Description
org.h2.server

A TCP server.

org.h2.server.pg

PostgreSQL server implementation of this database.

- 

Classes

Class
Description
ConnectionInfo

The connection info object is a wrapper for database connection information
 such as the database URL, user name and password.

DbStarter

This class can be used to start the H2 TCP server (or other H2 servers, for
 example the PG server) inside a web application container such as Tomcat or
 Jetty.

JakartaDbStarter

This class can be used to start the H2 TCP server (or other H2 servers, for
 example the PG server) inside a Jakarta web application container such as
 Tomcat or Jetty.

JakartaWebServlet

This servlet lets the H2 Console be used in a Jakarta servlet container
 such as Tomcat or Jetty.

PageParser

A page parser can parse an HTML page and replace the tags there.

WebApp

For each connection to a session, an object of this class is created.

WebServer

The web server is a simple standalone HTTP server that implements the H2
 Console application.

WebServlet

This servlet lets the H2 Console be used in a standard servlet container
 such as Tomcat or Jetty.