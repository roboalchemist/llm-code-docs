# Source: https://tomcat.apache.org/native-1.3-doc/miscellaneous/changelog.html

Title: The Apache Tomcat Native Library 1.3

URL Source: https://tomcat.apache.org/native-1.3-doc/miscellaneous/changelog.html

Markdown Content:
The Apache Tomcat Native Library 1.3 - Miscellaneous Documentation -
===============

[![Image 3: Tomcat Home](https://tomcat.apache.org/native-1.3-doc/images/tomcat.png)](https://tomcat.apache.org/)

[![Image 4: The Apache Software Foundation](https://tomcat.apache.org/native-1.3-doc/images/asf-logo.svg)](http://www.apache.org/)

The Apache Tomcat Native Library 1.3 - Miscellaneous Documentation
==================================================================

**Links**
---------

*   [Docs Home](https://tomcat.apache.org/native-1.3-doc/index.html)

**Miscellaneous Documentation**
-------------------------------

*   [Changelog](https://tomcat.apache.org/native-1.3-doc/miscellaneous/changelog.html)
*   [TLS renegotiation](https://tomcat.apache.org/native-1.3-doc/miscellaneous/tls-renegotiation.html)

**News**
--------

*   [2026](https://tomcat.apache.org/native-1.3-doc/news/2026.html)
*   [2024](https://tomcat.apache.org/native-1.3-doc/news/2024.html)

### Preface

This is the Changelog for Tomcat Native 1.3.x. The Tomcat Native 1.3.x branch started from the 1.2.39 tag.

### 2026-03-10 1.3.7

*   ![Image 5: Code: ](https://tomcat.apache.org/native-1.3-doc/images/code.gif) Refactor access to ASN1_OCTET_STRING to use setters to fix errors when building against the latest OpenSSL 4.0.x code. (markt) 
*   ![Image 6: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix the handling of OCSP requests with multiple responder URIs. (jfclere) 
*   ![Image 7: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix the handling of `TRY_AGAIN` responses to OCSP requests when soft fail is disabled. (jfclere) 

### 2026-02-11 1.3.6

*   ![Image 8: Code: ](https://tomcat.apache.org/native-1.3-doc/images/code.gif) Refactor the SSL_CONF_CTX clean-up to align it with SSL and SSL_CTX clean-up. (markt) 
*   ![Image 9: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix unnecessarily large buffer allocation when filtering out NULL and export ciphers. Pull requests [#35](https://github.com/apache/tomcat-native/pull/35) and [#37](https://github.com/apache/tomcat-native/pull/37) provided by chenjp. (markt) 
*   ![Image 10: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix a potential memory leak if an invalid `OpenSSLConf` is provided. Pull request [#36](https://github.com/apache/tomcat-native/pull/36) provided by chenjp. (markt) 
*   ![Image 11: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Refactor setting of OCSP configuration defaults as they were only applied if the SSL_CONF_CTX was used. While one was always used with Tomcat versions aware of the OCSP configuration options, one was not always used with Tomcat versions unaware of the OCSP configuration options leading to OCSP verification being enabled by default when the expected behaviour was disabled by default. (markt) 
*   ![Image 12: Code: ](https://tomcat.apache.org/native-1.3-doc/images/code.gif) Improve performance for the rare case of handling large OCSP responses. (markt) 

### 2026-01-19 1.3.5

*   ![Image 13: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Remove group write permissions from the files in the tar.gz source archive. (markt) 
*   ![Image 14: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Clear an additional error in OCSP processing that was preventing OCSP soft fail working with Tomcat's APR/native connector. (markt) 

### 2026-01-12 1.3.4

*   ![Image 15: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Correct logic error that prevented the configuration of TLS 1.3 cipher suites. (markt) 

### not released 1.3.3

*   ![Image 16: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Refactor the addition of TLS 1.3 cipher suite configuration to avoid a regression when running a version of Tomcat that pre-dates this change. (markt) 

### not released 1.3.2

*   ![Image 17: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Rename configure.in to modern autotools style configure.ac. (rjung) 
*   ![Image 18: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Fix incomplete updates for autotools generated files during "buildconf" execution. (rjung) 
*   ![Image 19: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Improve quoting in tcnative.m4. (rjung) 
*   ![Image 20: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Update the minimum version of autoconf for releasing to 2.68. (rjung) 
*   ![Image 21: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix the autoconf warnings when creating a release. (markt) 
*   ![Image 22: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) The Windows binaries are now built with OCSP support enabled by default. (markt) 
*   ![Image 23: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Include a nonce with OCSP requests and check the nonce, if any, in the OCSP response. (markt) 
*   ![Image 24: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Expand verification of OCSP responses. (markt) 
*   ![Image 25: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Add the ability to configure the OCSP checks to soft-fail - i.e. if the responder cannot be contacted or fails to respond in a timely manner the OCSP check will not fail. (markt) 
*   ![Image 26: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Add a configurable timeout to the writing of OCSP requests and reading of OCSP responses. (markt) 
*   ![Image 27: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Add the ability to control the OCSP verification flags. (markt) 
*   ![Image 28: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Configure TLS 1.3 connections from the provided ciphers list as well as connections using TLS 1.2 and earlier. Pull request provided by gastush. (markt) 
*   ![Image 29: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Update the Windows build environment to use Visual Studio 2022. (markt) 

### 2024-07-24 1.3.1

*   ![Image 30: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix a crash on Windows when `SSLContext.setCACertificate()` is invoked with a `null` value for `caCertificateFile` and a non-`null` value for `caCertificatePath` until properly addressed with https://github.com/openssl/openssl/issues/24416. (michaelo) 
*   ![Image 31: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Use ERR_error_string_n with a definite buffer length as a named constant. (schultz) 
*   ![Image 32: Add: ](https://tomcat.apache.org/native-1.3-doc/images/add.gif) Ensure local reference capacity is available when creating new arrays and Strings. (schultz) 
*   ![Image 33: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.14. (markt) 

### 2024-02-12 1.3.0

*   ![Image 34: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Drop useless `compile.optimize` option. (michaelo) 
*   ![Image 35: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Align Java source compile configuration with Tomcat. (michaelo) 
*   ![Image 36: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif) Fix version set in DLL header on Windows. (michaelo) 
*   ![Image 37: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Remove an unreachable if condition around CRLs in sslcontext.c. (michaelo) 
*   ![Image 38: Fix: ](https://tomcat.apache.org/native-1.3-doc/images/fix.gif)[67818](https://bz.apache.org/bugzilla/show_bug.cgi?id=67818): When calling `SSL.setVerify()` or `SSLContext.setVerify()`, the default verify paths are no longer set. Only the explicitly configured trust store, if any, will be used. (michaelo) 
*   ![Image 39: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Update the minimum supported version of LibreSSL to 3.5.2. (markt) 
*   ![Image 40: Design: ](https://tomcat.apache.org/native-1.3-doc/images/design.gif) Remove NPN support as NPN was never standardised and browser support was removed in 2019. (markt) 
*   ![Image 41: Update: ](https://tomcat.apache.org/native-1.3-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.13. (markt) 

### Changes in 1.2.x

Please see the [1.2.x changelog](https://tomcat.apache.org/native-1.2-doc/miscellaneous/changelog.html).

### Changes in 1.1.x

Please see the [1.1.x changelog](https://tomcat.apache.org/native-1.1-doc/miscellaneous/changelog.html).

 Copyright © 2008-2026, The Apache Software Foundation
