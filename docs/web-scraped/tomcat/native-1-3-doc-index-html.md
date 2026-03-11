# Source: https://tomcat.apache.org/native-1.3-doc/index.html

Title: The Apache Tomcat Native Library 1.3

URL Source: https://tomcat.apache.org/native-1.3-doc/index.html

Markdown Content:
Documentation Index
-------------------

### Introduction

The Apache Tomcat Native Library is an optional component for use with Apache Tomcat that allows Tomcat to use certain native resources for performance, compatibility, etc.

Specifically, the Apache Tomcat Native Library gives Tomcat access to the Apache Portable Runtime (APR) library's network connection (socket) implementation and random-number generator. See the Apache Tomcat documentation for more information on how to configure Tomcat to use the APR connector.

Features of the APR connector:

*   Non-blocking I/O for Keep-Alive requests (between requests)
*   Uses OpenSSL for TLS/SSL capabilities (if supported by linked APR library)
*   FIPS 140-2 support for TLS/SSL (if supported by linked OpenSSL library)
*   Support for IPv4, IPv6 and Unix Domain Sockets

### Headlines

*   [10 March 2026 - **Tomcat-Native-1.3.7 released**](https://tomcat.apache.org/native-1.3-doc/news/2026.html#20260310)
The Apache Tomcat team is proud to announce the immediate availability of Tomcat Native 1.3.7 Stable.

The sources and the binaries for selected platforms are available from the [Download page](https://tomcat.apache.org/download-native.cgi).

Please see the [Changelog](https://tomcat.apache.org/native-1.3-doc/miscellaneous/changelog.html) for a full list of changes.

Note: End of support for Tomcat Native 1.3.x has been announced as 31 March 2027.

### Building

#### Requirements

Build tc-native requires three components to be installed:

*   APR library
*   OpenSSL libraries
*   Java SE Development Kit (JDK)

In debian based Linux those dependencies could be installed by something like:

`apt-get install libapr1.0-dev libssl-dev`

In rpm based Linux those dependencies could be installed by something like:

`yum install apr-devel openssl-devel`

#### UNIX

On all the POSIX systems (Linux, Solaris, HP-UX, AIX etc...) a well-known configure and make is used to build tc-native.

 In the jni/native runs:

`./configure --help`

to read the description of all the parameters.

```
./configure --with-apr=$HOME/APR \
            --with-java-home=$JAVA_HOME \
            --with-ssl=$HOME/OPENSSL \
            --prefix=$CATALINA_HOME
```

to create the includes and makefiles to be able to build tc-native.

 Where:

`$HOME/APR` is something like /usr/bin/apr-1-config or the path where apr is installed.

`$JAVA_HOME` is something /home/jfclere/JAVA/jdk1.7.0_80 path to a JDK installation. Any JDK should work but it is advisable to use the same JVM version the JVM you use with Tomcat.

`$HOME/OPENSSL` is the path where OpenSSL is installed.

`$CATALINA_HOME` is the path where the produced libraries will be installed. Something like $HOME/apache-tomcat-8.0.47/

The configure is able to guess most of OpenSSL standard installations. So most of the time the following will be enough:

```
./configure --with-apr=/usr/bin/apr-1-config \
            --with-java-home=/home/jfclere/JAVA/jdk1.7.0_80/ \
            --with-ssl=yes \
            --prefix=$CATALINA_HOME
```

To build the libraries and install them:

`make && make install`

The libraries will be found in $CATALINA_HOME/lib

#### Windows

Download the Windows sources of tc-native and extract them.

Obtain the Windows sources for [APR](http://apr.apache.org/download.cgi) and [OpenSSL](https://www.openssl.org/source/). Apply the patches from native/srclib and build APR and OpenSSL for your platform (X86 or X64).

Build with

`nmake -f NMAKEMakefile WITH_APR=... WITH_OPENSSL=... APR_DECLARE_STATIC=1`

More detailed instructions including the steps to create a standard release distribution are provided on the [Wiki](https://cwiki.apache.org/confluence/display/TOMCAT/Building+the+Tomcat+Native+Connector+binaries+for+Windows).

### Install and tests

#### Configuring Tomcat

Apache Tomcat comes with the `AprLifecycleListener` enabled by default. Still, you should check your `conf/server.xml` to ensure that something like the following is present, and uncommented:

`<Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" />`

Please see the Apache Tomcat documentation for configuration specifics.

When using Unix Domain Sockets a cleanup is registered to delete the socket on destruction of the socket, or shutdown of the application. Should the application terminate abnormally, the socket deletion will need to be handled by the caller or by the administrator.

#### UNIX

Edit $CATALINA_HOME/bin/setenv.sh (creating the file if necessary) and add the path to the tc-native libraries to LD_LIBRARY_PATH. Something like:

```
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CATALINA_HOME/lib
export LD_LIBRARY_PATH
```

Start tomcat and check for the messages like this ones:

```
Nov 29, 2020 12:27:41 PM org.apache.catalina.core.AprLifecycleListener init
INFO: Loaded APR based Apache Tomcat Native library 1.x.y.
Nov 29, 2020 12:27:41 PM org.apache.catalina.core.AprLifecycleListener init
INFO: APR capabilities: IPv6 [true], sendfile [true], accept filters [false], random [true], UDS [true].
Nov 29, 2020 12:27:41 PM org.apache.coyote.http11.Http11AprProtocol init
INFO: Initializing Coyote HTTP/1.1 on http-8080
```

Refer to the tomcat documentation to configure the connectors (See [Tomcat 11.0.x](http://tomcat.apache.org/tomcat-11.0-doc/apr.html), [Tomcat 10.1.x](http://tomcat.apache.org/tomcat-10.1-doc/apr.html) and [Tomcat 9.0.x](http://tomcat.apache.org/tomcat-9.0-doc/apr.html))

#### Windows

Edit $CATALINA_BASE\bin\setenv.bat (creating the file if necessary) and add the path to the tc-native libraries, apr and OpenSSL to PATH. For example:

`set PATH=%PATH;C:\cygwin\home\support\tomcat-native-current-win32-src\jni\native\Debug;C:\cygwin\home\support\tomcat-native-current-win32-src\jni\apr\Debug;C:\OpenSSL\lib\VC`

Start tomcat and check for the messages like this ones:

```
Nov 29, 2020 2:48:17 PM org.apache.catalina.core.AprLifecycleListener init
INFO: Loaded APR based Apache Tomcat Native library 1.x.y.
Nov 29, 2020 2:48:17 PM org.apache.catalina.core.AprLifecycleListener init
INFO: APR capabilities: IPv6 [false], sendfile [true], accept filters [false], random [true], UDS [false].
Nov 29, 2020 2:48:18 PM org.apache.coyote.http11.Http11AprProtocol init
INFO: Initializing Coyote HTTP/1.1 on http-8080
```
