# Source: https://tomcat.apache.org/security.html

Title: Apache Tomcat® - Reporting Security Problems

URL Source: https://tomcat.apache.org/security.html

Published Time: Wed, 28 Jan 2026 09:27:34 GMT

Markdown Content:
Apache Tomcat® - Reporting Security Problems
===============

[![Image 1: Tomcat Home](https://tomcat.apache.org/res/images/tomcat.png)](http://tomcat.apache.org/)
Apache Tomcat®
==============

[![Image 2: Support Apache](https://www.apache.org/images/SupportApache-small.png)](https://www.apache.org/foundation/contributing.html)[![Image 3: The Apache Software Foundation](https://tomcat.apache.org/res/images/asf_logo_wide.svg)](http://www.apache.org/)

GO

[](https://tomcat.apache.org/security.html)

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

### Security Updates

Please note that, except in rare circumstances, binary patches are not produced for individual vulnerabilities. To obtain the binary fix for a particular vulnerability you should upgrade to an Apache Tomcat® version where that vulnerability has been fixed.

Source patches, usually in the form of references to commits, may be provided in either in a vulnerability announcement and/or the vulnerability details listed on these pages. These source patches may be used by users wishing to build their own local version of Tomcat with just that security patch rather than upgrade.

Lists of security problems fixed in currently supported versions of Apache Tomcat are available:

*   [Apache Tomcat 11.x Security Vulnerabilities](https://tomcat.apache.org/security-11.html)
*   [Apache Tomcat 10.x Security Vulnerabilities](https://tomcat.apache.org/security-10.html)
*   [Apache Tomcat 9.x Security Vulnerabilities](https://tomcat.apache.org/security-9.html)
*   [Apache Tomcat JK Connectors Security Vulnerabilities](https://tomcat.apache.org/security-jk.html)
*   [Apache Tomcat APR/native Connector Security Vulnerabilities](https://tomcat.apache.org/security-native.html)
*   [Apache Taglibs Security Vulnerabilities](https://tomcat.apache.org/security-taglibs.html)

Lists of security problems fixed in versions of Apache Tomcat that have reached end of life and may be downloaded from the archives are also available:

*   [Apache Tomcat 8.x Security Vulnerabilities](https://tomcat.apache.org/security-8.html)
*   [Apache Tomcat 7.x Security Vulnerabilities](https://tomcat.apache.org/security-7.html)
*   [Apache Tomcat 6.x Security Vulnerabilities](https://tomcat.apache.org/security-6.html)
*   [Apache Tomcat 5.x Security Vulnerabilities](https://tomcat.apache.org/security-5.html)
*   [Apache Tomcat 4.x Security Vulnerabilities](https://tomcat.apache.org/security-4.html)
*   [Apache Tomcat 3.x Security Vulnerabilities](https://tomcat.apache.org/security-3.html)

### Reporting New Security Problems with Tomcat

The ASF takes a very active stance in eliminating security problems and denial of service attacks against Tomcat.

We strongly encourage folks to report such problems to our private security mailing list first, before disclosing them in a public forum.

**Please note that the security mailing list should only be used for reporting undisclosed security vulnerabilities in Tomcat and managing the process of fixing such vulnerabilities. We cannot accept regular bug reports, provide free consulting or answer other queries at this address. All mail sent to this address that does not relate to an undisclosed security problem in the Tomcat source code will be ignored.** The private security mailing address is: [security@tomcat.apache.org](mailto:security@tomcat.apache.org)

The Tomcat [security model](https://tomcat.apache.org/security-model.html) describes what the Tomcat security team will and will not accept as a valid vulnerability report for Tomcat.

Note that all networked servers are subject to denial of service attacks, and we cannot promise magic workarounds to generic problems (such as a client streaming lots of data to your server, or re-requesting the same URL repeatedly). In general our philosophy is to avoid any attacks which can cause the server to consume resources in a non-linear relationship to the size of inputs.

Questions about:

*   how to configure Tomcat securely
*   if a vulnerability applies to your particular application
*   obtaining further information on a published vulnerability
*   availability of patches and/or new releases

should be addressed to the users mailing list. Please see the [mailing lists](https://tomcat.apache.org/lists.html) page for details of how to subscribe.

If you need to report a bug that isn't an undisclosed security vulnerability, please use the [bug reporting page](https://tomcat.apache.org/bugreport.html).

If you are interested in how reported vulnerabilities are handled, the process is documented at ASF-wide pages [[1]](https://apache.org/security/#vulnerability-handling) and [[2]](https://apache.org/security/committers.html#possible).

### Errors and omissions

Please report any errors or omissions to [security@tomcat.apache.org](mailto:security@tomcat.apache.org).

 Copyright © 1999-2025, The Apache Software Foundation 

 Apache Tomcat, Tomcat, Apache, the Apache Tomcat logo and the Apache logo are either registered trademarks or trademarks of the Apache Software Foundation.
