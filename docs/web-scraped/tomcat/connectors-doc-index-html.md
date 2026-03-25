# Source: https://tomcat.apache.org/connectors-doc/index.html

Title: The Apache Tomcat Connectors: mod_jk, ISAPI redirector, NSAPI redirector (1.2.50)

URL Source: https://tomcat.apache.org/connectors-doc/index.html

Markdown Content:
The **Apache Tomcat Connectors** project is part of the Tomcat project and provides web server plugins to connect web servers with Tomcat and other backends.

The supported web servers are:

*   the Apache HTTP Server with a plugin (module) named **mod_jk**.
*   Microsoft IIS with a plugin (extension) named **ISAPI redirector** (or simply redirector).

In all cases the plugin uses a special protocol named **Apache JServ Protocol** or simply **AJP** to connect to the backend. Backends known to support AJP are Apache Tomcat, Jetty and JBoss. Although there exist 3 versions of the protocol, **ajp12**, **ajp13**, **ajp14**, most installations only use ajp13. The older ajp12 does not use persistent connections and is obsolete, the newer version ajp14 is still experimental. Sometimes ajp13 is called AJP 1.3 or AJPv13, but we will mostly use the name ajp13.

Most features of the plugins are the same for all web servers. Some details vary on a per web server basis. The documentation and the configuration is split into common parts and web server specific parts.

down to the more detailed documentation that is available. Each available manual is described in more detail below.

*   [**JK-1.2.50 released**](https://tomcat.apache.org/connectors-doc/news/20240101.html)
The Apache Tomcat team is proud to announce the immediate availability of Tomcat Connectors 1.2.50 Stable. This release contains improvements and bug fixes for issues found in previous releases.

Download the [JK 1.2.50 release](https://tomcat.apache.org/download-connectors.cgi).

*   Download [previous releases](https://archive.apache.org/dist/tomcat/tomcat-connectors/) from the archives.

*   [**workers.properties**](https://tomcat.apache.org/connectors-doc/reference/workers.html)
A Tomcat worker is a Tomcat instance that is waiting to execute servlets on behalf of some web server. For example, we can have a web server such as Apache forwarding servlet requests to a Tomcat process (the worker) running behind it.

This page contains detailed description of all workers.properties directives.

*   [**uriworkermap.properties**](https://tomcat.apache.org/connectors-doc/reference/uriworkermap.html)
The forwarding of requests from the web server to tomcat gets configured by defining mapping rules. The so-called **uriworkermap** file is a mechanism of defining those rules.

*   [**Status Worker**](https://tomcat.apache.org/connectors-doc/reference/status.html)
The status worker is a builtin management worker. It displays state information and can also be used to dynamically reconfigure JK.

*   [**Apache HTTP Server (mod_jk)**](https://tomcat.apache.org/connectors-doc/reference/apache.html)
This page contains detailed description of all directives of mod_jk for the Apache HTTP Server.

*   [**Microsoft IIS (ISAPI redirector)**](https://tomcat.apache.org/connectors-doc/reference/iis.html)
This page contains detailed description of all directives of the ISAPI redirector for Microsoft IIS.

*   [**Quick Start**](https://tomcat.apache.org/connectors-doc/common_howto/quick.html)
This page describes the configuration files used by JK on the web server side for the 'impatient'.

*   [**All about workers**](https://tomcat.apache.org/connectors-doc/common_howto/workers.html)
This page contains an overview about the various aspects of defining and using workers.

*   [**Timeouts**](https://tomcat.apache.org/connectors-doc/common_howto/timeouts.html)
This page describes the possible timeout settings you can use.

*   [**Load Balancing**](https://tomcat.apache.org/connectors-doc/common_howto/loadbalancers.html)
This page contains an introduction on load balancing with JK.

*   [**Reverse Proxy**](https://tomcat.apache.org/connectors-doc/common_howto/proxy.html)
This page contains an introduction to reverse proxies, how JK handles this situation and how you can influence the JK proxying behaviour.

These pages contain detailed descriptions of how to build and install JK for the various web servers.

*   [**Apache HTTP Server (mod_jk)**](https://tomcat.apache.org/connectors-doc/webserver_howto/apache.html)
*   [**Microsoft IIS (ISAPI redirector)**](https://tomcat.apache.org/connectors-doc/webserver_howto/iis.html)

*   [**AJPv13**](https://tomcat.apache.org/connectors-doc/ajp/ajpv13a.html)
This page describes the Apache JServ Protocol version 1.3 (hereafter **ajp13**).

*   [**AJPv13 Extension Proposal**](https://tomcat.apache.org/connectors-doc/ajp/ajpv13ext.html)
This page describes an extension proposal for ajp13.

*   [**Frequently asked questions**](https://tomcat.apache.org/connectors-doc/miscellaneous/faq.html)
*   [**Changelog**](https://tomcat.apache.org/connectors-doc/miscellaneous/changelog.html)
This page contains the detailed list of all changes made in each version of JK.

*   [**Current Tomcat Connectors bugs**](http://issues.apache.org/bugzilla/buglist.cgi?query_format=advanced&short_desc_type=allwordssubstr&short_desc=&product=Tomcat+Connectors&long_desc_type=substring&long_desc=&bug_file_loc_type=allwordssubstr&bug_file_loc=&keywords_type=allwords&keywords=&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&emailassigned_to1=1&emailtype1=substring&email1=&emailassigned_to2=1&emailreporter2=1&emailcc2=1&emailtype2=substring&email2=&bugidtype=include&bug_id=&votes=&chfieldfrom=&chfieldto=Now&chfieldvalue=&cmdtype=doit&order=Reuse+same+sort+as+last+time&field0-0-0=noop&type0-0-0=noop&value0-0-0=)
This is the Bugzilla Bug List related to Tomcat Connectors.

*   [**Contribute documentation**](https://tomcat.apache.org/connectors-doc/miscellaneous/doccontrib.html)
This page describes, how to contribute to the JK documentation.

*   [**JK Status Ant Tasks**](https://tomcat.apache.org/connectors-doc/miscellaneous/jkstatustasks.html)
This page describes ant tasks to automate JK management via the status worker.

*   [**Reporting Tools**](https://tomcat.apache.org/connectors-doc/miscellaneous/reporttools.html)
This page contains information, on some report analysis scripts contained in the JK distribution.
