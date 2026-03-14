# Source: https://tomcat.apache.org/tomcat-9.0-doc/index.html

Title: Apache Tomcat 9 (9.0.115) - Documentation Index

URL Source: https://tomcat.apache.org/tomcat-9.0-doc/index.html

Markdown Content:
### Introduction

This is the top-level entry point of the documentation bundle for the **Apache Tomcat** Servlet/JSP container. Apache Tomcat version 9.0 implements the Servlet 4.0 and JavaServer Pages 2.3 [specifications](https://cwiki.apache.org/confluence/display/TOMCAT/Specifications) from the [Java Community Process](https://www.jcp.org/), and includes many additional features that make it a useful platform for developing and deploying web applications and web services.

Select one of the links from the navigation menu (to the left) to drill down to the more detailed documentation that is available. Each available manual is described in more detail below.

### Apache Tomcat User Guide

The following documents will assist you in downloading and installing Apache Tomcat, and using many of the Apache Tomcat features.

1.   [**Introduction**](https://tomcat.apache.org/tomcat-9.0-doc/introduction.html) - A brief, high level, overview of Apache Tomcat.
2.   [**Setup**](https://tomcat.apache.org/tomcat-9.0-doc/setup.html) - How to install and run Apache Tomcat on a variety of platforms.
3.   [**First web application**](https://tomcat.apache.org/tomcat-9.0-doc/appdev/index.html) - An introduction to the concepts of a _web application_ as defined in the Servlet Specification. Covers basic organization of your web application source tree, the structure of a web application archive, and an introduction to the web application deployment descriptor (`/WEB-INF/web.xml`).
4.   [**Deployer**](https://tomcat.apache.org/tomcat-9.0-doc/deployer-howto.html) - Operating the Apache Tomcat Deployer to deploy, precompile, and validate web applications.
5.   [**Manager**](https://tomcat.apache.org/tomcat-9.0-doc/manager-howto.html) - Operating the **Manager** web app to deploy, undeploy, and redeploy applications while Apache Tomcat is running.
6.   [**Host Manager**](https://tomcat.apache.org/tomcat-9.0-doc/host-manager-howto.html) - Operating the **Host Manager** web app to add and remove virtual hosts while Apache Tomcat is running.
7.   [**Realms and Access Control**](https://tomcat.apache.org/tomcat-9.0-doc/realm-howto.html) - Description of how to configure _Realms_ (databases of users, passwords, and their associated roles) for use in web applications that utilize _Container Managed Security_.
8.   [**Security Manager**](https://tomcat.apache.org/tomcat-9.0-doc/security-manager-howto.html) - Configuring and using a Java Security Manager to support fine-grained control over the behavior of your web applications. 
9.   [**JNDI Resources**](https://tomcat.apache.org/tomcat-9.0-doc/jndi-resources-howto.html) - Configuring standard and custom resources in the JNDI naming context that is provided to each web application.
10.   [**JDBC DataSource**](https://tomcat.apache.org/tomcat-9.0-doc/jndi-datasource-examples-howto.html) - Configuring a JNDI DataSource with a DB connection pool. Examples for many popular databases.
11.   [**Classloading**](https://tomcat.apache.org/tomcat-9.0-doc/class-loader-howto.html) - Information about class loading in Apache Tomcat, including where to place your application classes so that they are visible.
12.   [**JSPs**](https://tomcat.apache.org/tomcat-9.0-doc/jasper-howto.html) - Information about Jasper configuration, as well as the JSP compiler usage.
13.   [**SSL/TLS**](https://tomcat.apache.org/tomcat-9.0-doc/ssl-howto.html) - Installing and configuring SSL/TLS support so that your Apache Tomcat will serve requests using the `https` protocol.
14.   [**SSI**](https://tomcat.apache.org/tomcat-9.0-doc/ssi-howto.html) - Using Server Side Includes in Apache Tomcat.
15.   [**CGI**](https://tomcat.apache.org/tomcat-9.0-doc/cgi-howto.html) - Using CGIs with Apache Tomcat.
16.   [**Proxy Support**](https://tomcat.apache.org/tomcat-9.0-doc/proxy-howto.html) - Configuring Apache Tomcat to run behind a proxy server (or a web server functioning as a proxy server).
17.   [**MBeans Descriptors**](https://tomcat.apache.org/tomcat-9.0-doc/mbeans-descriptors-howto.html) - Configuring MBean descriptors files for custom components.
18.   [**Default Servlet**](https://tomcat.apache.org/tomcat-9.0-doc/default-servlet.html) - Configuring the default servlet and customizing directory listings.
19.   [**Apache Tomcat Clustering**](https://tomcat.apache.org/tomcat-9.0-doc/cluster-howto.html) - Enable session replication in a Apache Tomcat environment.
20.   [**Balancer**](https://tomcat.apache.org/tomcat-9.0-doc/balancer-howto.html) - Configuring, using, and extending the load balancer application.
21.   [**Connectors**](https://tomcat.apache.org/tomcat-9.0-doc/connectors.html) - Connectors available in Apache Tomcat, and native web server integration.
22.   [**Monitoring and Management**](https://tomcat.apache.org/tomcat-9.0-doc/monitoring.html) - Enabling JMX Remote support, and using tools to monitor and manage Apache Tomcat.
23.   [**Logging**](https://tomcat.apache.org/tomcat-9.0-doc/logging.html) - Configuring logging in Apache Tomcat.
24.   [**Apache Portable Runtime**](https://tomcat.apache.org/tomcat-9.0-doc/apr.html) - Using APR to provide superior performance, scalability and better integration with native server technologies.
25.   [**Virtual Hosting**](https://tomcat.apache.org/tomcat-9.0-doc/virtual-hosting-howto.html) - Configuring virtual hosting in Apache Tomcat.
26.   [**Advanced IO**](https://tomcat.apache.org/tomcat-9.0-doc/aio.html) - Extensions available over regular, blocking IO.
27.   [**Using Tomcat libraries with Maven**](https://tomcat.apache.org/tomcat-9.0-doc/maven-jars.html) - Obtaining Tomcat jars through Maven.
28.   [**Security Considerations**](https://tomcat.apache.org/tomcat-9.0-doc/security-howto.html) - Options to consider when securing an Apache Tomcat installation.
29.   [**Windows Service**](https://tomcat.apache.org/tomcat-9.0-doc/windows-service-howto.html) - Running Tomcat as a service on Microsoft Windows.
30.   [**Windows Authentication**](https://tomcat.apache.org/tomcat-9.0-doc/windows-auth-howto.html) - Configuring Tomcat to use integrated Windows authentication.
31.   [**High Concurrency JDBC Pool**](https://tomcat.apache.org/tomcat-9.0-doc/jdbc-pool.html) - Configuring Tomcat to use an alternative JDBC pool.
32.   [**WebSocket support**](https://tomcat.apache.org/tomcat-9.0-doc/web-socket-howto.html) - Developing WebSocket applications for Apache Tomcat.
33.   [**URL rewrite**](https://tomcat.apache.org/tomcat-9.0-doc/rewrite.html) - Using the regexp based rewrite valve for conditional URL and host rewrite.
34.   [**CDI and JAX-RS support**](https://tomcat.apache.org/tomcat-9.0-doc/cdi.html) - Configuring CDI,JAX-RS and Eclipse Microprofile support.
35.   [**AOT compilation support**](https://tomcat.apache.org/tomcat-9.0-doc/graal.html) - Ahead of Time compilation support with GraalVM/Native Image.

### Reference

The following documents are aimed at _System Administrators_ who are responsible for installing, configuring, and operating an Apache Tomcat server.

*   [**Release notes**](https://tomcat.apache.org/tomcat-9.0-doc/RELEASE-NOTES.txt) - Known issues in this Apache Tomcat release. 
*   [**Apache Tomcat Server Configuration Reference**](https://tomcat.apache.org/tomcat-9.0-doc/config/index.html) - Reference manual that documents all available elements and attributes that may be placed into the Apache Tomcat `conf/server.xml` file. 
*   [**JK Documentation**](https://tomcat.apache.org/connectors-doc/index.html) - Complete documentation and HOWTOs on the JK native webserver connector, used to interface Apache Tomcat with servers like Apache HTTPd, IIS and others.
*   Servlet 4.0 [**Specification**](https://jcp.org/aboutJava/communityprocess/final/jsr369/index.html) and [**Javadoc**](https://javaee.github.io/javaee-spec/javadocs/javax/servlet/package-summary.html)
*   JSP 2.3 [**Specification**](https://jcp.org/aboutJava/communityprocess/mrel/jsr245/index2.html) and [**Javadoc**](http://docs.oracle.com/javaee/7/api/javax/servlet/jsp/package-summary.html)
*   EL 3.0 [**Specification**](https://jcp.org/aboutJava/communityprocess/final/jsr341/index.html) and [**Javadoc**](http://docs.oracle.com/javaee/7/api/javax/el/package-summary.html)
*   WebSocket 1.1 [**Specification**](https://jcp.org/aboutJava/communityprocess/mrel/jsr356/index.html) and [**Javadoc**](http://docs.oracle.com/javaee/7/api/javax/websocket/package-summary.html)
*   JASPIC 1.1 [**Specification**](https://jcp.org/aboutJava/communityprocess/mrel/jsr196/index.html) and [**Javadoc**](http://docs.oracle.com/javaee/7/api/javax/security/auth/message/package-summary.html)

### Apache Tomcat Developers

The following documents are for Java developers who wish to contribute to the development of the _Apache Tomcat_ project.

*   [**Building from Source**](https://tomcat.apache.org/tomcat-9.0-doc/building.html) - Details the steps necessary to download Apache Tomcat source code (and the other packages that it depends on), and build a binary distribution from those sources. 
*   [**Changelog**](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html) - Details the changes made to Apache Tomcat. 
*   [**Status**](https://wiki.apache.org/tomcat/TomcatVersions) - Apache Tomcat development status. 
*   [**Developers**](https://tomcat.apache.org/tomcat-9.0-doc/developers.html) - List of active Apache Tomcat contributors. 
*   [**Javadocs**](https://tomcat.apache.org/tomcat-9.0-doc/api/index.html) - Javadoc API documentation for Apache Tomcat's internals.
*   [**Apache Tomcat Architecture**](https://tomcat.apache.org/tomcat-9.0-doc/architecture/index.html) - Documentation of the Apache Tomcat Server Architecture.
