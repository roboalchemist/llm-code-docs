# Source: https://maven.apache.org/what-is-maven.html

Title: Introduction – Maven

URL Source: https://maven.apache.org/what-is-maven.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
Introduction – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* Introduction [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/what-is-maven.md)
* | Last Published: 2026-03-13
* |[Get Sources](https://maven.apache.org/scm.html)
* [Downloads](https://maven.apache.org/download.cgi)

* [Welcome](https://maven.apache.org/index.html)
* [License](https://www.apache.org/licenses/)
* About Maven
* [What is Maven?](https://maven.apache.org/what-is-maven.html)
* [Installation](https://maven.apache.org/install.html)
* [Downloads](https://maven.apache.org/download.html)
* [Use](https://maven.apache.org/run.html)
* [Configure](https://maven.apache.org/configure.html)
* [Release Notes](https://maven.apache.org/docs/history.html)
* [Security Reports](https://maven.apache.org/security.html)
* Documentation
* [Maven Plugins](https://maven.apache.org/plugins/index.html)
* [Maven Extensions](https://maven.apache.org/extensions/index.html)
* [Maven Tools](https://maven.apache.org/tools/index.html)
  * [Maven Daemon](https://maven.apache.org/tools/mvnd.html)
  * [Maven Upgrade Tool](https://maven.apache.org/tools/mvnup.html)
  * [Maven Wrapper](https://maven.apache.org/tools/mavenwrapper.html)

* [Index (category)](https://maven.apache.org/guides/index.html)
* [User Manual](https://maven.apache.org/users/index.html)
* [Maven Repositories](https://maven.apache.org/repositories/index.html)
* [Plugin Development](https://maven.apache.org/plugin-developers/index.html)
* [Contribute to Maven](https://maven.apache.org/developers/index.html)
* [Books and Resources](https://maven.apache.org/articles.html)
* Community
* [Community Overview](https://maven.apache.org/community.html)
* [Project Roles](https://maven.apache.org/project-roles.html)
* [How to Contribute](https://maven.apache.org/guides/development/guide-helping.html)
* [Getting Help](https://maven.apache.org/users/getting-help.html)
* [Issue Management](https://maven.apache.org/issue-management.html)
* [Getting Maven Source](https://maven.apache.org/scm.html)
* [The Maven Team](https://maven.apache.org/team.html)
* Project Documentation
* [Project Information](https://maven.apache.org/project-info.html)
* Maven Projects
* [Maven](https://maven.apache.org/ref/current)
* [Archetypes](https://maven.apache.org/archetypes/index.html)
* [Extensions](https://maven.apache.org/extensions/index.html)
* [Parent POMs](https://maven.apache.org/pom/index.html)
* [Plugins](https://maven.apache.org/plugins/index.html)
* [Skins](https://maven.apache.org/skins/index.html)
* [Components](https://maven.apache.org/what-is-maven.html)
  * [Archetype](https://maven.apache.org/archetype/index.html)
  * [Artifact Resolver](https://maven.apache.org/resolver/index.html)
  * [Doxia](https://maven.apache.org/doxia/index.html)
  * [Indexer](https://maven.apache.org/maven-indexer/index.html)
  * [JXR](https://maven.apache.org/jxr/index.html)
  * [Plugin Testing](https://maven.apache.org/plugin-testing/index.html)
  * [Plugin Tools](https://maven.apache.org/plugin-tools/index.html)
  * [Resource Bundles](https://maven.apache.org/apache-resource-bundles/index.html)
  * [SCM](https://maven.apache.org/scm/index.html)
  * [Shared Components](https://maven.apache.org/shared/index.html)
  * [Surefire](https://maven.apache.org/surefire/index.html)
  * [Wagon](https://maven.apache.org/wagon/index.html)

* ASF
* [How Apache Works](https://www.apache.org/foundation/how-it-works.html)
* [Foundation](https://www.apache.org/foundation/)
* [Data Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
* [Sponsoring Apache](https://www.apache.org/foundation/sponsorship.html)
* [Thanks](https://www.apache.org/foundation/thanks.html)

[![Image 4: Built by Maven](https://maven.apache.org/images/logos/maven-feather.png)](https://maven.apache.org/)

[](https://maven.apache.org/what-is-maven.html)
Introduction
============

Maven, a [Yiddish word](https://en.wikipedia.org/wiki/Maven) meaning _accumulator of knowledge_, began as an attempt to simplify the build processes in the Jakarta Turbine project. There were several projects, each with their own Ant build files, that were all slightly different. JARs were checked into CVS. We wanted a standard way to build the projects, a clear definition of what the project consisted of, an easy way to publish project information, and a way to share JARs across several projects.

The result is a tool that can now be used for building and managing any Java-based project. We hope that we have created something that will make the day-to-day work of Java developers easier and generally help them understand any Java-based project.

[](https://maven.apache.org/what-is-maven.html)
Maven's Objectives
------------------

Maven's primary goal is to allow a developer to organize and a build a Java project in the shortest period of time. It does this by:

* Making the build process easy
* Providing a uniform build system
* Providing quality project information
* Encouraging better development practices

[](https://maven.apache.org/what-is-maven.html)

### Making the build process easy

While using Maven doesn't eliminate the need to know about the underlying mechanisms, Maven does shield developers from many details.

[](https://maven.apache.org/what-is-maven.html)

### Providing a uniform build system

Maven builds a project using its project object model (POM) and a set of plugins. Once you familiarize yourself with one Maven project, you know how all Maven projects build. This saves time when navigating many projects.

[](https://maven.apache.org/what-is-maven.html)

### Providing quality project information

Maven provides useful project information that is in part taken from your POM and in part generated from your project's sources. For example, Maven can provide:

* Change log created directly from source control
* Cross referenced sources
* Mailing lists managed by the project
* Dependencies used by the project
* Unit test reports

Third party code analysis products also provide Maven plugins that add their reports to the standard information given by Maven.

[](https://maven.apache.org/what-is-maven.html)

### Providing guidelines for best practices development

Maven aims to gather current principles for best practices development and make it easy to guide a project in that direction.

For example, specification, execution, and reporting of unit tests are part of the normal build cycle using Maven. Current unit testing best practices were used as guidelines:

* Keeping test source code in a separate, but parallel source tree
* Using test case naming conventions to locate and execute tests
* Having test cases setup their environment instead of customizing the build for test preparation

Maven also assists in project workflow such as release and issue management.

Maven also suggests some guidelines on how to layout your project's directory structure. Once you learn the layout, you can easily navigate other projects that use Maven.

While Maven takes an opinionated approach to project layout, some projects may not fit with this structure for historical reasons. While Maven is designed to be flexible to the needs of different projects, it cannot cater to every situation without compromising its objectives.

If your project has an unusual build structure that cannot be reorganized, you may have to forgo some features or the use of Maven altogether.

[](https://maven.apache.org/what-is-maven.html)
Feature summary
---------------

The following are the key features of Maven in a nutshell:

* Simple project setup that follows best practices - get a new project or module started in seconds-
* Consistent usage across all projects - means no ramp up time for new developers coming onto a project-
* Superior dependency management including automatic updating, dependency closures (also known as transitive dependencies)-
* Able to easily work with multiple projects at the same time-
* A [large and growing repository of libraries and metadata](https://maven.apache.org/repository/) to use out of the box, and arrangements in place with the largest Open Source projects for real-time availability of their latest releases-
* Extensible, with the ability to easily [write plugins](https://maven.apache.org/plugin-developers/) in Java or scripting languages-
* Instant access to new features with little or no extra configuration.
* Ant tasks for dependency management and deployment outside of Maven-
* Model based builds: Maven is able to build any number of projects into predefined output types such as a JAR, WAR, or distribution based on metadata about the project, without the need to do any scripting in most cases.
* Coherent site of project information: Using the same metadata as for the build process, Maven is able to generate a website or PDF including any documentation you care to add, and adds to that standard reports about the state of development of the project. Examples of this information can be seen at the bottom of the left-hand navigation of this site under the “_Project Information_” and “_Project Reports_” submenus.
* Release management and distribution publication: Without much additional configuration, Maven will integrate with your source control system (such as Subversion or Git) and manage the release of a project based on a certain tag. It can also publish this to a distribution location for use by other projects. Maven is able to publish individual outputs such as a JAR, an archive including other dependencies and documentation, or as a source distribution.
* Dependency management: Maven encourages the use of a central repository of JARs and other dependencies. Maven comes with a mechanism that your project's clients can use to download any JARs required for building your project from a central JAR repository much like Perl's CPAN. This allows users of Maven to reuse JARs across projects and encourages communication between projects to ensure that backward compatibility issues are dealt with.

[](https://maven.apache.org/what-is-maven.html)
What is Maven Not?
------------------

You might have heard some of the following things about Maven:

* Maven is a site and documentation tool
* Maven extends Ant to let you download dependencies
* Maven is a set of reusable Ant scriptlets

While Maven does these things, as you can read above in the “What is Maven?” section, these are not the only features Maven has, and its objectives are quite different.

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
