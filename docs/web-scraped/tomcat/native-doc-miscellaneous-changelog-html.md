# Source: https://tomcat.apache.org/native-doc/miscellaneous/changelog.html

Title: The Apache Tomcat Native Library 2.0

URL Source: https://tomcat.apache.org/native-doc/miscellaneous/changelog.html

Markdown Content:
The Apache Tomcat Native Library 2.0 - Miscellaneous Documentation -
===============

[![Image 3: Tomcat Home](https://tomcat.apache.org/native-doc/images/tomcat.png)](https://tomcat.apache.org/)

[![Image 4: The Apache Software Foundation](https://tomcat.apache.org/native-doc/images/asf-logo.svg)](http://www.apache.org/)

The Apache Tomcat Native Library 2.0 - Miscellaneous Documentation
==================================================================

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

### Preface

This is the Changelog for Apache Tomcat Native 2.0.x. The Tomcat Native 2.0.x branch started from the 1.2.33 tag.

### 2026-03-10 2.0.14

*   ![Image 5: Code: ](https://tomcat.apache.org/native-doc/images/code.gif) Refactor access to ASN1_OCTET_STRING to use setters to fix errors when building against the latest OpenSSL 4.0.x code. (markt) 
*   ![Image 6: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix the handling of OCSP requests with multiple responder URIs. (jfclere) 
*   ![Image 7: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix the handling of `TRY_AGAIN` responses to OCSP requests when soft fail is disabled. (jfclere) 

### 2026-02-11 2.0.13

*   ![Image 8: Code: ](https://tomcat.apache.org/native-doc/images/code.gif) Due to various refactorings, the 2.0.x code no longer compiles with LibreSSL. Without a volunteer to maintain LibreSSL support, the LibreSSL code will be removed no earlier than 30 September 2026. (markt)
*   ![Image 9: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Remove group write permissions from the files in the tar.gz source archive. (markt) 
*   ![Image 10: Code: ](https://tomcat.apache.org/native-doc/images/code.gif) Refactor the SSL_CONF_CTX clean-up to align it with SSL and SSL_CTX clean-up. (markt) 
*   ![Image 11: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix unnecessarily large buffer allocation when filtering out NULL and export ciphers. Pull requests [#35](https://github.com/apache/tomcat-native/pull/35) and [#37](https://github.com/apache/tomcat-native/pull/37) provided by chenjp. (markt) 
*   ![Image 12: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix a potential memory leak if an invalid `OpenSSLConf` is provided. Pull request [#36](https://github.com/apache/tomcat-native/pull/36) provided by chenjp. (markt) 
*   ![Image 13: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Refactor setting of OCSP configuration defaults as they were only applied if the SSL_CONF_CTX was used. While one was always used with Tomcat versions aware of the OCSP configuration options, one was not always used with Tomcat versions unaware of the OCSP configuration options leading to OCSP verification being enabled by default when the expected behaviour was disabled by default. (markt) 
*   ![Image 14: Code: ](https://tomcat.apache.org/native-doc/images/code.gif) Improve performance for the rare case of handling large OCSP responses. (markt) 
*   ![Image 15: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[69939](https://bz.apache.org/bugzilla/show_bug.cgi?id=69939): Fix the cause of a crash with OpenSSL 3.0.x when a certificate PEM file does not contain explicit DH parameters. (markt) 
*   ![Image 16: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Refactor extraction of ECDH curve name from the Certificate to avoid deprecated OpenSSL methods. 
*   ![Image 17: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Refactor the native implementation of `SSL.getTime()` to avoid the Y2038 problem in `SSL_SESSION_get_time()` when running on a version of OpenSSL that includes the new `SSL_SESSION_get_time_ex()` method. (markt) 

### 2026-01-12 2.0.12

*   ![Image 18: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Refactor the addition of TLS 1.3 cipher suite configuration to avoid a regression when running a version of Tomcat that pre-dates this change. (markt) 

### not released 2.0.11

*   ![Image 19: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix a reference to an uninitialized variable. (schultz) 
*   ![Image 20: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Correct file names and update versions in native build instructions. (markt) 
*   ![Image 21: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Remove references to deprecated engine configuration. (markt) 

### not released 2.0.10

*   ![Image 22: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) The Windows binaries are now built with OCSP support enabled by default. (markt) 
*   ![Image 23: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Include a nonce with OCSP requests and check the nonce, if any, in the OCSP response. (markt) 
*   ![Image 24: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Expand verification of OCSP responses. (markt) 
*   ![Image 25: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Add the ability to configure the OCSP checks to soft-fail - i.e. if the responder cannot be contacted or fails to respond in a timely manner the OCSP check will not fail. (markt) 
*   ![Image 26: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Add a configurable timeout to the writing of OCSP requests and reading of OCSP responses. (markt) 
*   ![Image 27: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Add the ability to control the OCSP verification flags. (markt) 
*   ![Image 28: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Configure TLS 1.3 connections from the provided ciphers list as well as connections using TLS 1.2 and earlier. Pull request provided by gastush. (markt) 
*   ![Image 29: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Remove out of date options from make file. (markt) 
*   ![Image 30: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Use automated configuration of DH parameters rather than deprecated callback. (markt) 

### 2025-05-29 2.0.9

*   ![Image 31: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the Windows build environment to use Visual Studio 2022. (markt) 
*   ![Image 32: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.5.0. (markt) 
*   ![Image 33: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of APR to 1.7.6. (markt) 

### 2024-07-24 2.0.8

*   ![Image 34: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix a crash on Windows when `SSLContext.setCACertificate()` is invoked with a `null` value for `caCertificateFile` and a non-`null` value for `caCertificatePath` until properly addressed with https://github.com/openssl/openssl/issues/24416. (michaelo) 
*   ![Image 35: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Use ERR_error_string_n with a definite buffer length as a named constant. (schultz) 
*   ![Image 36: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Ensure local reference capacity is available when creating new arrays and Strings. (schultz) 
*   ![Image 37: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.14. (markt) 

### 2024-02-08 2.0.7

*   ![Image 38: Add: ](https://tomcat.apache.org/native-doc/images/add.gif)[67538](https://bz.apache.org/bugzilla/show_bug.cgi?id=67538): Make use of Ant's `<javaversion />` task to enforce the mininum Java build version. (michaelo) 
*   ![Image 39: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[67615](https://bz.apache.org/bugzilla/show_bug.cgi?id=67615): Windows binary for version 2 has incorrect version suffix compared to the GNU autoconf version. (michaelo) 
*   ![Image 40: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Align default pass phrase prompt with HTTPd on Windows as well. (michaelo) 
*   ![Image 41: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[67616](https://bz.apache.org/bugzilla/show_bug.cgi?id=67616): o.a.tomcat.jni.SSL contains useless check for old OpenSSL version. (michaelo) 
*   ![Image 42: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Drop useless `compile.optimize` option. (michaelo) 
*   ![Image 43: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Align Java source compile configuration with Tomcat. (michaelo) 
*   ![Image 44: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Add Ant version (1.10.2) requirement identical to Tomcat. (michaelo) 
*   ![Image 45: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Remove an unreachable if condition around CRLs in sslcontext.c. (michaelo) 
*   ![Image 46: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[67818](https://bz.apache.org/bugzilla/show_bug.cgi?id=67818): When calling `SSL.setVerify()` or `SSLContext.setVerify()`, the default verify paths are no longer set. Only the explicitly configured trust store, if any, will be used. (michaelo) 
*   ![Image 47: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.13. (markt) 

### 2023-10-02 2.0.6

*   ![Image 48: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[67061](https://bz.apache.org/bugzilla/show_bug.cgi?id=67061): If the insecure optionalNoCA certificate verification mode is used, disable OCSP if enabled else client certificates from unknown certificate authorities will be rejected. (markt) 
*   ![Image 49: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.11. (markt) 

### 2023-08-07 2.0.5

*   ![Image 50: Update: ](https://tomcat.apache.org/native-doc/images/update.gif)[66666](https://bz.apache.org/bugzilla/show_bug.cgi?id=66666): Remove non-reachable functions from ssl.c. (michaelo) 
*   ![Image 51: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Align default pass phrase prompt with HTTPd. (michaelo) 
*   ![Image 52: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Rename configure.in to modern autotools style configure.ac. (rjung) 
*   ![Image 53: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Fix incomplete updates for autotools generated files during "buildconf" execution. (rjung) 
*   ![Image 54: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Improve quoting in tcnative.m4. (rjung) 
*   ![Image 55: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the minimum version of autoconf for releasing to 2.68. (rjung) 
*   ![Image 56: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif)[66669](https://bz.apache.org/bugzilla/show_bug.cgi?id=66669): Fix memory leak in SNI processing. (markt) 
*   ![Image 57: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.10. (markt) 

### not released 2.0.4

*   ![Image 58: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of APR to 1.7.4. (markt) 
*   ![Image 59: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.9. (markt) 

### 2023-02-13 2.0.3

*   ![Image 60: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of APR to 1.7.2. (markt) 
*   ![Image 61: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the recommended minimum version of OpenSSL to 3.0.8. (markt) 

### 2022-11-08 2.0.2

*   ![Image 62: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the minimum supported version of LibreSSL to 3.5.2. Based on pull request [#13](https://github.com/apache/tomcat-native/pull/13) provided by orbea. (markt) 
*   ![Image 63: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix build when building with rlibtool. Pull request [#14](https://github.com/apache/tomcat-native/pull/14) provided by orbea. (markt) 

### 2022-07-12 2.0.1

*   ![Image 64: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update recommended OpenSSL version to 3.0.5 or later. (markt) 

### not released 2.0.0

*   ![Image 65: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the minimum required version of OpenSSL to 3.0.0 and make it a madatory dependency. (markt) 
*   ![Image 66: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the minimum required version of APR to 1.7.0. (markt) 
*   ![Image 67: Design: ](https://tomcat.apache.org/native-doc/images/design.gif) Remove NPN support as NPN was never standardised and browser support was removed in 2019. (markt) 
*   ![Image 68: Add: ](https://tomcat.apache.org/native-doc/images/add.gif) Add support for using OpenSSL when the FIPS provider is configured as the default provider. (markt) 
*   ![Image 69: Design: ](https://tomcat.apache.org/native-doc/images/design.gif) Remove all API methods (and supporting code) that are not used by Tomcat 10.1.x to support the use of OpenSSL as a replacement for JSSE to provide TLS functionality. (markt) 
*   ![Image 70: Docs: ](https://tomcat.apache.org/native-doc/images/docs.gif) Document the TLS rengotiation behaviour. (markt) 
*   ![Image 71: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Update the minimum required Java version to Java 11. (markt) 
*   ![Image 72: Update: ](https://tomcat.apache.org/native-doc/images/update.gif) Remove support for Windows 2000, Windows XP, Windows Server 2003, Windows Vista and Windows Server 2008. The minimum Windows version is now Windows 7 / Windows Server 2008 R2. (markt) 
*   ![Image 73: Docs: ](https://tomcat.apache.org/native-doc/images/docs.gif) Add HOWTO-RELEASE.txt that describes the release process. (markt) 
*   ![Image 74: Fix: ](https://tomcat.apache.org/native-doc/images/fix.gif) Fix the autoconf warnings when creating a release. (markt) 

### Changes in 1.3.x

Please see the [1.3.x changelog](https://tomcat.apache.org/native-1.3-doc/miscellaneous/changelog.html).

### Changes in 1.2.x

Please see the [1.2.x changelog](https://tomcat.apache.org/native-1.2-doc/miscellaneous/changelog.html).

### Changes in 1.1.x

Please see the [1.1.x changelog](https://tomcat.apache.org/native-1.1-doc/miscellaneous/changelog.html).

 Copyright © 2008-2026, The Apache Software Foundation
