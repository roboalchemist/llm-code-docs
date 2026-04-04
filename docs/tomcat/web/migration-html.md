# Source: https://tomcat.apache.org/migration.html

Title: Apache Tomcat® - Migration Guide

URL Source: https://tomcat.apache.org/migration.html

Published Time: Wed, 28 Jan 2026 09:27:34 GMT

Markdown Content:
Apache Tomcat® - Migration Guide
===============

[![Image 1: Tomcat Home](https://tomcat.apache.org/res/images/tomcat.png)](http://tomcat.apache.org/)
Apache Tomcat®
==============

[![Image 2: Support Apache](https://www.apache.org/images/SupportApache-small.png)](https://www.apache.org/foundation/contributing.html)[![Image 3: The Apache Software Foundation](https://tomcat.apache.org/res/images/asf_logo_wide.svg)](http://www.apache.org/)

GO

[](https://tomcat.apache.org/migration.html)

Apache Tomcat
-------------

*   [Home](https://tomcat.apache.org/index.html)
*   [Taglibs](https://tomcat.apache.org/taglibs.html)
*   [Maven Plugin](https://tomcat.apache.org/maven-plugin.html)

Download
--------

*   [Which version?](https://tomcat.apache.org/whichversion.html)
*   [Tomcat 11](https://tomcat.apache.org/download-11.cgi)
*   [Tomcat 10](https://tomcat.apache.org/download-10.cgi)
*   [Tomcat 9](https://tomcat.apache.org/download-90.cgi)
*   [Tomcat Migration Tool for Jakarta EE](https://tomcat.apache.org/download-migration.cgi)
*   [Tomcat Connectors](https://tomcat.apache.org/download-connectors.cgi)
*   [Tomcat Native](https://tomcat.apache.org/download-native.cgi)
*   [Taglibs](https://tomcat.apache.org/download-taglibs.cgi)
*   [Archives](https://archive.apache.org/dist/tomcat/)

Documentation
-------------

*   [Tomcat 11.0](https://tomcat.apache.org/tomcat-11.0-doc/index.html)
*   [Tomcat 10.1](https://tomcat.apache.org/tomcat-10.1-doc/index.html)
*   [Tomcat 9.0](https://tomcat.apache.org/tomcat-9.0-doc/index.html)
*   [Upgrading](https://tomcat.apache.org/upgrading.html)
*   [Tomcat Connectors](https://tomcat.apache.org/connectors-doc/index.html)
*   [Tomcat Native 2](https://tomcat.apache.org/native-doc/index.html)
*   [Tomcat Native 1.3](https://tomcat.apache.org/native-1.3-doc/index.html)
*   [Wiki](https://cwiki.apache.org/confluence/display/TOMCAT)
*   [Migration Guide](https://tomcat.apache.org/migration.html)
*   [Presentations](https://tomcat.apache.org/presentations.html)
*   [Specifications](https://cwiki.apache.org/confluence/x/Bi8lBg)

Problems?
---------

*   [Security Reports](https://tomcat.apache.org/security.html)
*   [Find help](https://tomcat.apache.org/findhelp.html)
*   [FAQ](https://cwiki.apache.org/confluence/display/TOMCAT/FAQ)
*   [Mailing Lists](https://tomcat.apache.org/lists.html)
*   [Bug Database](https://tomcat.apache.org/bugreport.html)

Get Involved
------------

*   [Overview](https://tomcat.apache.org/getinvolved.html)
*   [Source code](https://tomcat.apache.org/source.html)
*   [Buildbot](https://tomcat.apache.org/ci.html)
*   [Tools](https://tomcat.apache.org/tools.html)

Media
-----

*   [Twitter](https://twitter.com/theapachetomcat)
*   [YouTube](https://www.youtube.com/c/ApacheTomcatOfficial)
*   [Blog](https://blogs.apache.org/tomcat/)

Misc
----

*   [Who We Are](https://tomcat.apache.org/whoweare.html)
*   [Swag](https://www.redbubble.com/people/comdev/works/30885254-apache-tomcat)
*   [Heritage](https://tomcat.apache.org/heritage.html)
*   [Apache Home](http://www.apache.org/)
*   [Resources](https://tomcat.apache.org/resources.html)
*   [Contact](https://tomcat.apache.org/contact.html)
*   [Legal](https://tomcat.apache.org/legal.html)
*   [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
*   [Support Apache](https://www.apache.org/foundation/contributing.html)
*   [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
*   [Thanks](http://www.apache.org/foundation/thanks.html)
*   [License](http://www.apache.org/licenses/)

Content
-------

### Before upgrading or migrating

When updating from one major Apache Tomcat® version a newer one, please make sure that the JVM that is installed on your system supports at least the required Java version. While it is possible that older versions of Tomcat may not be compatible with newer JVMs, all the currently supported Apache Tomcat versions (9.0.x, 10.1.x and 11.0.x) are known to run correctly on Java 17 JVMs.

When migrating from one major Tomcat version to another (e.g. from Tomcat 9 to Tomcat 10, or from Tomcat 10 to Tomcat 11), you should not copy the configuration files from the old version to the new version. The recommended approach is to start with the default configuration of the new version of Apache Tomcat and to adjust it as necessary.

When migrating from one minor release to another minor release within the same major release (e.g. from Tomcat 9.0.29 to Tomcat 9.0.30) you can retain the configuration files, but you should check to see if any defaults have changed and/or if any new elements have been added and adjust your configuration files accordingly.

### Migration Guides

For upgrading between 11.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-11.0.html#Upgrading_11.0.x) section of the Tomcat 11.0.x Migration Guide.

For migration from 10.1.x to 11.0.x, see the [Tomcat 11.0.x Migration Guide](https://tomcat.apache.org/migration-11.0.html).

For upgrading between 10.1.x versions, see the [upgrading](https://tomcat.apache.org/migration-10.1.html#Upgrading_10.1.x) section of the Tomcat 10.1.x Migration Guide.

For migration from 10.0.x to 10.1.x, see the [Tomcat 10.1.x Migration Guide](https://tomcat.apache.org/migration-10.1.html).

For upgrading between 10.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-10.html#Upgrading_10.0.x) section of the Tomcat 10.0.x Migration Guide.

For migration from 9.0.x to 10.0.x, see the [Tomcat 10.0.x Migration Guide](https://tomcat.apache.org/migration-10.html).

For upgrading between 9.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-9.html#Upgrading_9.0.x) section of the Tomcat 9.0.x Migration Guide.

For migration from 8.0.x / 8.5.x to 9.0.x, see the [Tomcat 9.0.x Migration Guide](https://tomcat.apache.org/migration-9.html).

For upgrading between 8.5.x versions, see the [upgrading](https://tomcat.apache.org/migration-85.html#Upgrading_8.5.x) section of the Tomcat 8.5.x Migration Guide.

For migration from 8.0.x to 8.5.x, see the [Tomcat 8.5.x Migration Guide](https://tomcat.apache.org/migration-85.html).

For upgrading between 8.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-8.html#Upgrading_8.0.x) section of the Tomcat 8.0.x Migration Guide.

For migration from 7.0.x to 8.0.x, see the [Tomcat 8.0.x Migration Guide](https://tomcat.apache.org/migration-8.html).

For upgrading between 7.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-7.html#Upgrading_7.0.x) section of the Tomcat 7.0.x Migration Guide.

For migration from 6.0.x to 7.0.x, see the [Tomcat 7.0.x Migration Guide](https://tomcat.apache.org/migration-7.html).

For upgrading between 6.0.x versions, see the [upgrading](https://tomcat.apache.org/migration-6.html#Upgrading_6.0.x) section of the Tomcat 6.0.x Migration Guide.

For migration from 5.5.x to 6.0.x, see the [Tomcat 6.0.x Migration Guide](https://tomcat.apache.org/migration-6.html).

 Copyright © 1999-2025, The Apache Software Foundation 

 Apache Tomcat, Tomcat, Apache, the Apache Tomcat logo and the Apache logo are either registered trademarks or trademarks of the Apache Software Foundation.
