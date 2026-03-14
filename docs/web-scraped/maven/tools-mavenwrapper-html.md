# Source: https://maven.apache.org/tools/mavenwrapper.html

Title: Maven Wrapper – Maven

URL Source: https://maven.apache.org/tools/mavenwrapper.html

Markdown Content:
Maven Wrapper – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* Maven Wrapper [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/tools/mavenwrapper.md)
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
* [Components](https://maven.apache.org/tools/mavenwrapper.html)
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

[](https://maven.apache.org/tools/mavenwrapper.html)
Maven Wrapper
=============

If you want to ensure that a project is always build with a certain Maven version or JDK you can either define rules using the Maven enforcer plugin. But this leaves the user alone with an error message when the user's environment does not match the requirements. With the Maven Wrapper you not only ensure the correct versions, but also provide the possibility to automatically download them so project is fully encapsulated from the user's environment.

[](https://maven.apache.org/tools/mavenwrapper.html)
One tool - three parts[](https://maven.apache.org/tools/mavenwrapper.html#one-tool-three-parts)
-----------------------------------------------------------------------------------------------

The Maven Wrapper is divided into three parts

* The [Maven Wrapper Plugin](https://maven.apache.org/wrapper/maven-wrapper-plugin/) to set up and run the Maven Wrapper.
* The [Maven Wrapper JAR](https://maven.apache.org/wrapper/maven-wrapper/index.html) which downloads the desired versions.
* The [Maven Wrapper Distribution](https://maven.apache.org/wrapper/maven-wrapper-distribution/index.html) provides everything that has to be installed into a project wanting to use Maven Wrapper.

[](https://maven.apache.org/tools/mavenwrapper.html)
Usage[](https://maven.apache.org/tools/mavenwrapper.html#usage)
---------------------------------------------------------------

To use the Maven Wrapper you first define the desired versions (and maybe URLs) in a `wrapper/maven-wrapper.properties` file inside the `.mvn` folder of your project. The Maven Wrapper plugin picks up this property file and installs everything defined. After that you can build the project using the Wrapper by calling `./mvnw <goals>` (or `mvnw.cmd <goals>` on Windows).

The full detailed information and documentation is available on the [Maven Wrapper documentation](https://maven.apache.org/wrapper/index.html).

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
