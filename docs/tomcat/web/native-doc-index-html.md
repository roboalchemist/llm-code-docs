# Source: https://tomcat.apache.org/native-doc/index.html

Title: The Apache Tomcat Native Library 2.0

URL Source: https://tomcat.apache.org/native-doc/index.html

Markdown Content:
The Apache Tomcat Native Library 2.0 - Documentation Index
===============

[![Image 1: Tomcat Home](https://tomcat.apache.org/native-doc/images/tomcat.png)](https://tomcat.apache.org/)

[![Image 2: The Apache Software Foundation](https://tomcat.apache.org/native-doc/images/asf-logo.svg)](http://www.apache.org/)

The Apache Tomcat Native Library 2.0
====================================

**Links**
---------

*   [Docs Home](https://tomcat.apache.org/native-doc/index.html)

**Miscellaneous Documentation**
-------------------------------

*   [Changelog](https://tomcat.apache.org/native-doc/miscellaneous/changelog.html)
*   [TLS renegotiation](https://tomcat.apache.org/native-doc/miscellaneous/tls-renegotiation.html)

**News**
--------

*   [2026](https://tomcat.apache.org/native-doc/news/2026.html)
*   [2025](https://tomcat.apache.org/native-doc/news/2025.html)
*   [2024](https://tomcat.apache.org/native-doc/news/2024.html)
*   [2023](https://tomcat.apache.org/native-doc/news/2023.html)
*   [2022](https://tomcat.apache.org/native-doc/news/2022.html)

Documentation Index
-------------------

### Introduction

The Apache Tomcat Native Library is an optional component for use with Apache Tomcat that allows Tomcat to use OpenSSL as a replacement for JSSE to support TLS connections.

### Headlines

*   [10 March 2026 - **Tomcat-Native-2.0.14 released**](https://tomcat.apache.org/native-doc/news/2026.html#20260310)
The Apache Tomcat team is proud to announce the immediate availability of Tomcat Native 2.0.14 Stable.

The sources and the binaries for selected platforms are available from the [Download page](https://tomcat.apache.org/download-native.cgi).

Please see the [Changelog](https://tomcat.apache.org/native-doc/miscellaneous/changelog.html) for a full list of changes.

### Building

#### Requirements

To build TC-Native, the following components must be installed:

*   APR library
*   OpenSSL libraries
*   Java SE Development Kit (JDK)

For Debian-based Linux distributions, these dependencies can be installed using the following command:

`apt-get install libapr1-dev libssl-dev openjdk-11-jdk`

For RPM-based Linux distributions, these dependencies can be installed using the following command:

`yum install apr-devel openssl-devel java-11-openjdk-devel`

#### UNIX

On all POSIX-like systems (Linux, Solaris, HP-UX, AIX etc...), the well-known configure and make are used to build TC-Native.

 To see a description of all configuration parameters, run the following command in the `native` directory of the source distribution:

`./configure --help`

To create the includes and makefiles necessary for building TC-Native, use the following command:

```
./configure --with-apr=$HOME/APR \
            --with-java-home=$JAVA_HOME \
            --with-ssl=$HOME/OPENSSL \
            --prefix=$CATALINA_HOME
```

Where:

`$HOME/APR` is the path to the APR installation, such as /usr/bin/apr-1-config.

`$JAVA_HOME` is the path to a JDK installation, for example, /home/jfclere/JAVA/jdk11. Any JDK version should work, but it is advisable to use the same JVM version as the one you use with Tomcat.

`$HOME/OPENSSL` is the path where OpenSSL is installed.

`$CATALINA_HOME` is the path where the produced libraries will be installed, such as $HOME/apache-tomcat-10.1.0

 The configure script can automatically detect most standard APR and OpenSSL installations. Therefore, an equivalent command is usually sufficient:

`./configure --with-java-home=$JAVA_HOME --prefix=$CATALINA_HOME`

To build and install the libraries, run:

`make && make install`

The libraries will be installed in `$CATALINA_HOME/lib`.

#### Windows

Detailed building instructions including the steps to create a standard release distribution are provided on the [Wiki](https://cwiki.apache.org/confluence/display/TOMCAT/Building+the+Tomcat+Native+Connector+binaries+for+Windows).

### Install and tests

#### Configuring Tomcat

Apache Tomcat comes with the `AprLifecycleListener` enabled by default. However, it is recommended to check `conf/server.xml` file to ensure that the following configuration is present and uncommented:

`<Listener className="org.apache.catalina.core.AprLifecycleListener" />`

For detailed configuration instructions, please refer to the Apache Tomcat documentation (See [Tomcat 11.0.x](https://tomcat.apache.org/tomcat-11.0-doc/config/listeners.html#APR_Lifecycle_Listener_-_org.apache.catalina.core.AprLifecycleListener), [Tomcat 10.1.x](https://tomcat.apache.org/tomcat-10.1-doc/config/listeners.html#APR_Lifecycle_Listener_-_org.apache.catalina.core.AprLifecycleListener) and [Tomcat 9.0.x](https://tomcat.apache.org/tomcat-9.0-doc/config/listeners.html#APR_Lifecycle_Listener_-_org.apache.catalina.core.AprLifecycleListener)).

#### UNIX

To ensure the TC-Native libraries are correctly loaded, follow these steps:

*   Edit the `$CATALINA_HOME/bin/setenv.sh` file. For detailed instructions, please refer to the `RUNNING.txt` file of your Apache Tomcat distribution.
*   Check that TC-Native libraries exist in `$CATALINA_HOME/lib` and add the path to the TC-Native libraries to the LD_LIBRARY_PATH:

`LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CATALINA_HOME/libexport LD_LIBRARY_PATH` 
*   Start Tomcat and look for messages similar to the following in the logs:

`21-Jun-2024 11:06:23.274 INFO [main] org.apache.catalina.core.AprLifecycleListener.lifecycleEvent Loaded Apache Tomcat Native library [2.0.7] using APR version [1.7.3].21-Jun-2024 11:06:23.298 INFO [main] org.apache.catalina.core.AprLifecycleListener.initializeSSL OpenSSL successfully initialized [OpenSSL 3.2.1 30 Jan 2024]` 

For detailed configuration of connectors, refer to the Apache Tomcat documentation (See [Tomcat 11.0.x](https://tomcat.apache.org/tomcat-11.0-doc/config/http.html), [Tomcat 10.1.x](https://tomcat.apache.org/tomcat-10.1-doc/config/http.html) and [Tomcat 9.0.x](https://tomcat.apache.org/tomcat-9.0-doc/config/http.html)).

#### Windows

To ensure the TC-Native libraries are correctly loaded, follow these steps:

*   Edit the `$CATALINA_HOME/bin/setenv.sh` file. For detailed instructions, please refer to the `RUNNING.txt` file of your Apache Tomcat distribution.
*   Ensure that the `tcnative-2.dll` file matches CPU architecture of JVM that you use to run Tomcat (x86 or x64) and is located in the `$CATALINA_HOME/bin` directory.

 Alternatively, you can add the path to the TC-Native libraries to the PATH environment variable:

`set PATH=%PATH%;C:\your\path\to\tc-native-dll` 
*   Start Tomcat and look for messages similar to the following in the logs:

`21-Jun-2024 11:06:23.274 INFO [main] org.apache.catalina.core.AprLifecycleListener.lifecycleEvent Loaded Apache Tomcat Native library [2.0.7] using APR version [1.7.3].21-Jun-2024 11:06:23.298 INFO [main] org.apache.catalina.core.AprLifecycleListener.initializeSSL OpenSSL successfully initialized [OpenSSL 3.2.1 30 Jan 2024]` 

 Copyright © 2008-2026, The Apache Software Foundation
