# Source: https://tomcat.apache.org/bugreport.html

Title: Apache Tomcat® - Reporting Bugs

URL Source: https://tomcat.apache.org/bugreport.html

Markdown Content:
### Table of Contents

*   [Before you report a bug](https://tomcat.apache.org/bugreport.html#Before_you_report_a_bug)
    1.   [Bugzilla is not a support forum](https://tomcat.apache.org/bugreport.html#Bugzilla_is_not_a_support_forum)

*   [Resources to help resolve Apache Tomcat problems](https://tomcat.apache.org/bugreport.html#Resources_to_help_resolve_Apache_Tomcat_problems)
    1.   [Problem troubleshooting](https://tomcat.apache.org/bugreport.html#Problem_troubleshooting)
    2.   [Apache Tomcat discussion lists](https://tomcat.apache.org/bugreport.html#Apache_Tomcat_discussion_lists)
    3.   [Known issues](https://tomcat.apache.org/bugreport.html#Known_issues)
    4.   [Recent version](https://tomcat.apache.org/bugreport.html#Recent_version)

*   [Looking for known issues](https://tomcat.apache.org/bugreport.html#Looking_for_known_issues)
    1.   [Search the bug database](https://tomcat.apache.org/bugreport.html#Search_the_bug_database)
    2.   [Changelog](https://tomcat.apache.org/bugreport.html#Changelog)
    3.   [Third party components](https://tomcat.apache.org/bugreport.html#Third_party_components)

*   [Reporting Apache Tomcat bugs](https://tomcat.apache.org/bugreport.html#Reporting_Apache_Tomcat_bugs)
    1.   [How to write a bug report](https://tomcat.apache.org/bugreport.html#How_to_write_a_bug_report)
    2.   [How to submit patches and enhancement requests](https://tomcat.apache.org/bugreport.html#How_to_submit_patches_and_enhancement_requests)
    3.   [Security Issues](https://tomcat.apache.org/bugreport.html#Security_Issues)

### Before you report a bug

The Apache Tomcat® community consists of those who use Apache Tomcat, help answer questions on discussions lists, contribute documentation and patches, and those who develop and maintain the code for Apache Tomcat. Almost all those who assist on a day to day basis resolving bug reports do this for a wide variety of reasons, and almost all of them do this on their own time.

Many bugs reported end up not being a bug in the Apache Tomcat code, but are due to misconfiguration, problems caused by installed applications, the operating system, etc.

**Before reporting a bug please make every effort to resolve the problem yourself.**

If you need help, ask on the **users**[mailing list](https://tomcat.apache.org/lists.html#tomcat-users).

The remainder of this document points you toward resources you can use to resolve the problem you are having.

#### Bugzilla is not a support forum

Bugzilla is a tool to track bug reports and feature requests. It is used to **organize** work on Apache Tomcat projects, so that such issues are not forgotten and to document how they were resolved.

Bugzilla **is not** a place to ask questions on how to configure your own system, or how to interpret some error message or behaviour that you do not understand. If you have questions, please ask on the **users**[mailing list](https://tomcat.apache.org/lists.html#tomcat-users).

When you have gathered enough information to diagnose your problem, and it is indeed a bug that can be fixed in Apache Tomcat, feel free to create or reopen your Bugzilla issue for it. You can find a link to your discussion in the [mailing list archives](https://tomcat.apache.org/lists.html) and include it in your bug report.

### Resources to help resolve Apache Tomcat problems

Here are some resources you can use to help you resolve the problem you are having before reporting a bug.

#### Problem troubleshooting

*   **Documentation** – Review the documentation for the version of Apache Tomcat that you are using. The problem that you are facing may already be addressed in the docs. Note, that documentation is searchable.
*   **Logs** – The logs which Apache Tomcat generates can be a valuable resource when trying to diagnose a problem. Please review them. You may want to enable debug output in your Apache Tomcat configuration so that you have more information to help diagnose the problem. You may want to configure an Access Log (a valve) to log what requests reached Tomcat and what was Tomcat's response to them. 
*   **Wiki** – Search the [Wiki](https://cwiki.apache.org/confluence/display/TOMCAT). That is unofficial documentation to which everyone can contribute. 
*   **FAQ's** – Search the [Tomcat Frequently Asked Questions](https://cwiki.apache.org/confluence/display/TOMCAT/FAQ) that is part of the Wiki.

#### Apache Tomcat discussion lists

It is very likely you are not the first to run into a problem. Others may have already found a solution. The mailing list archives may contain discussions which will help you resolve the problem.

See the [mailing lists](https://tomcat.apache.org/lists.html) page for the further information on the lists.

See also the [Find help](https://tomcat.apache.org/findhelp.html) page.

#### Known issues

Please search the bug database to see if the bug you are seeing has already been reported. Please look at the changelog page for the bugs that have already been fixed. The changelogs for not-yet-released versions of Tomcat are also available. More details are below.

#### Recent version

Try to reproduce your problem with the latest released version of Apache Tomcat.

### Looking for known issues

#### Search the bug database

Please search the bug database to see if the bug you are seeing has already been reported.

*   The bug may have already been fixed and is available in a later version or nightly build.
*   Someone else may have reported the bug, you could add supporting information to help reproduce and resolve the bug.

The search page is [here](https://bz.apache.org/bugzilla/query.cgi). There is also [advanced](https://bz.apache.org/bugzilla/query.cgi?format=advanced) search page.

Here are some search tips.

1.   Search for closed bugs as well as for the open ones.

On the advanced search page you can clear the "Status" field to avoid filtering by status.

2.   Search across different versions of Tomcat.

In the bug database Tomcat is represented by several "products". The same problem should be reported only once, but the fix may be applied to different Tomcat versions. While doing so, the bug report is moved between different products. A bug that is originally reported against Tomcat 9 is moved to Tomcat 8 and maybe later to Tomcat 7. So it makes sense to search all the versions at once.

Here is a quick list of supported products:

    *   **Tomcat 11**, **Tomcat 10** and **Tomcat 9** – Tomcat 11.0.x, 10.1.x and 9.0.x
    *   **Tomcat Connectors** – Integration of Tomcat with other Web servers
    *   **Tomcat Native** – APR based native HTTP and AJP connectors for Tomcat
    *   **Tomcat Modules** – Additional Tomcat components
    *   **Taglibs** – Apache [Taglibs](https://tomcat.apache.org/taglibs/) subproject

3.   Search not only Summary field, but also the Comment one

On the advanced search page open "Detailed Bug Information", then type your query into the "Comment" field.

4.   You can limit results to the issues that were changed recently.

On the advanced search page open "Search by Change History", then type "`-2m`" into the first field in the pair of "between" fields to limit results to the issues changed in the last 2 months.

5.   Some bugs do not belong to Tomcat.

Tomcat bundles libraries from several other projects. You can see RELEASE-NOTES and NOTICE files in your distribution for details. More details are in a separate section below.

#### Changelog

If you are looking for the recently fixed issues there are several places to look at.

*   Changelog files for released versions

These are published on the Tomcat website.

*   Changelog files for _not-yet-released_ versions

These are available in the source code.

They are in XML format with style sheets attached. Thus modern web browsers can display them nicely.

The files are also available in nightly documentation builds. See [Buildbot](https://tomcat.apache.org/ci.html) page for details.

Links:

| **Product** | **Changelog (released)** | **Changelog (unreleased)** |
| --- | --- | --- |
| Tomcat 11.0 (main) | [changelog.html](https://tomcat.apache.org/tomcat-11.0-doc/changelog.html) | [changelog.html - CI](https://nightlies.apache.org/tomcat/tomcat-11.0.x/docs/changelog.html) |
| Tomcat 10.1 | [changelog.html](https://tomcat.apache.org/tomcat-10.1-doc/changelog.html) | [changelog.html - CI](https://nightlies.apache.org/tomcat/tomcat-10.1.x/docs/changelog.html) |
| Tomcat 9.0 | [changelog.html](https://tomcat.apache.org/tomcat-9.0-doc/changelog.html) | [changelog.html - CI](https://nightlies.apache.org/tomcat/tomcat-9.0.x/docs/changelog.html) |
| Tomcat Connectors | [changelog.html](https://tomcat.apache.org/connectors-doc/miscellaneous/changelog.html) | [changelog.xml](https://github.com/apache/tomcat-connectors/blob/main/xdocs/miscellaneous/changelog.xml) |
| Tomcat Native 2.0 | [changelog.html](https://tomcat.apache.org/native-doc/miscellaneous/changelog.html) | [changelog.xml](https://github.com/apache/tomcat-native/blob/main/xdocs/miscellaneous/changelog.xml) |
| Tomcat Native 1.2 | [changelog.html](https://tomcat.apache.org/native-1.2-doc/miscellaneous/changelog.html) | [changelog.xml](https://github.com/apache/tomcat-native/blob/1.2.x/xdocs/miscellaneous/changelog.xml) |

#### Third party components

Tomcat bundles libraries from several other projects. See RELEASE-NOTES and NOTICE files in your distribution for details. The versions of the components that were used to build Tomcat are defined in the `build.properties.default` file in the source distribution.

Notable components are:

*   Tomcat service launcher – `commons-daemon-*`, `tomcatN.exe`, `tomcatNw.exe`

The service launcher is provided by [Apache Commons Daemon](http://commons.apache.org/daemon/) project.

Using the terminology from that project, the *nixes launcher is called `jsvc` and the Windows launcher is called `procrun`. The `tomcatN.exe` and `tomcatNw.exe` programs in Tomcat distributions are just renamed `prunsrv.exe` and `prunmgr.exe` from Apache Commons Daemon binaries distribution.

*   DBCP Database Pool implementation – `tomcat-dbcp.jar`.

This pool implementation is provided by [Apache Commons Pool](http://commons.apache.org/pool/) and [Apache Commons DBCP](http://commons.apache.org/dbcp/) projects.

The classes from these two projects are renamed into a different package, to avoid conflicts if the same libraries are used by web applications, recompiled and packed into a single JAR file.

*   JDBC Database Pool implementation – `tomcat-jdbc.jar`.

This pool implementation is available with Tomcat 7 and later and it comes from **jdbc-pool** project that is part of **Tomcat Modules**. This library is developed alongside the main Tomcat.

*   Tomcat [Maven plugin](http://tomcat.apache.org/maven-plugin.html) subproject tracks its issues in [JIRA database](https://bz.apache.org/jira/browse/MTOMCAT).

### Reporting Apache Tomcat bugs

Please make sure the problem is a bug in Apache Tomcat and not a bug in your web application.

Note, that [security-related](https://tomcat.apache.org/security.html) issues should **not** be reported through Bugzilla.

#### How to write a bug report

Please provide as much information as possible. It is very hard to fix a bug if the person looking into the problem cannot reproduce it. See also [Bug Writing Guidelines](https://bz.apache.org/bugzilla/page.cgi?id=bug-writing.html).

Bug submission starts [here](https://bz.apache.org/bugzilla/enter_bug.cgi). You have to include the following information in your bug report:

*   **Product**. Here is a list of supported products:

    *   **Tomcat 11** – Tomcat 11.1.x and tomcat.apache.org web site
    *   **Tomcat 10** – Tomcat 10.1.x
    *   **Tomcat 9** – Tomcat 9.0.x
    *   **Tomcat Connectors** – Integration of Tomcat with other Web servers. The **mod_jk** module for [Apache HTTPD](http://httpd.apache.org/) and other web servers.
    *   **Tomcat Native** – HTTP and AJP connectors for Tomcat using native code and linked with Apache APR and OpenSSL libraries
    *   **Tomcat Modules** – Additional Tomcat components, such as **jdbc-pool**
    *   **Taglibs** – Apache [Taglibs](https://tomcat.apache.org/taglibs/) subproject

*   **Version** – Apache Tomcat version.

Please not only select it from the list, but also mention it in your text. The bug description can be updated, so it is important to mention the version in the text as well.

*   **Component** – The component which has the bug.

If you do not know, just guess.

*   **Platform** and **OS** – Hardware platform and operating system Tomcat is running on.

*   **Severity** – This is `normal` for usual bug reports and `enhancement` for enhancement requests.

If you tend to mark it as `critical`, you are probably doing it wrong. It is likely that the issue is already known and fixed, or it is not an issue at all.

*   Configuration details

Please mention these in your text:

    *   Java version – Vendor and version of your Java Runtime Environment used to run Tomcat.
    *   If Tomcat is used behind [Apache HTTPD](http://httpd.apache.org/) or other web server – its version and how it is configured.
    *   Tomcat Connector that is being used. There are several implementations of Connectors in Tomcat. Which one is being used is shown in the logs during Tomcat startup. 

*   Attachments

Attach configuration files and Tomcat log files if they would help to track down the bug.

*   Reproducer

Please describe how to reproduce your problem on a clean Tomcat installation. If you can please provide a **simple** sample web application that demonstrates the issue.

#### How to submit patches and enhancement requests

Enhancement requests for Tomcat are submitted using the same procedure as bug reports, but in the **Severity** field you will select the value "`enhancement`".

For components available via GitHub you may provide a proposed patch as a pull request. Alternatively, you can attach your proposed patch to a Bugzilla issue. When providing a patch, please mention to which version of the source code it applies. Any patches are welcome, but we prefer the ones that use the [Unified Diff](http://en.wikipedia.org/wiki/Diff#Unified_format) format. Those can be generated using `diff -u` command or `svn diff` or `git diff` command.

To patch and build Apache Tomcat see the following references:

*   [Repository access](https://tomcat.apache.org/source.html) for Apache Tomcat
*   Read BUILDING.txt in the source distribution

To prepare a documentation patch:

Read section on building the documentation in BUILDING.txt file in the source distribution. Usually the documentation for a version of Tomcat is located in `webapps/docs/` directory in the source code and can be built with `ant build-docs` command.

To build documentation it should be sufficient to have a Java runtime and a copy of [Apache Ant](http://ant.apache.org/). Compiling Tomcat code should be unnecessary.

Generic references:

*   Apache Software Foundation guildelines:

    *   General [Apache guidance for Subversion](http://www.apache.org/dev/version-control.html#anon-svn)
    *   Sending in Patches chapter of [Contributors Tech Guide](http://www.apache.org/dev/contributors.html#patches)

*   General Subversion documentation:

    *   The [Subversion Book](http://svnbook.red-bean.com/index.en.html)

#### Security Issues

Security-related bugs are of special concern. If you have a verified security bug to report please neither post it to public email lists nor submit a bug report. See [Security Reports](https://tomcat.apache.org/security.html) page on how to report them.
