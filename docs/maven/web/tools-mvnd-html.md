# Source: https://maven.apache.org/tools/mvnd.html

Title: Maven Daemon – Maven

URL Source: https://maven.apache.org/tools/mvnd.html

Markdown Content:
Maven Daemon – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* Maven Daemon [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/tools/mvnd.md)
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
* [Components](https://maven.apache.org/tools/mvnd.html)
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

[](https://maven.apache.org/tools/mvnd.html)
Maven Daemon
============

The Maven Daemon (mvnd) is a daemon infrastructure for Maven that helps to reduce the build time by:

* Keeping the JVM running between builds
* Managing a pool of Maven processes
* Reusing the JVM and Maven processes across builds

[](https://maven.apache.org/tools/mvnd.html)
Features[](https://maven.apache.org/tools/mvnd.html#features)
-------------------------------------------------------------

* Significantly faster builds compared to regular Maven
* Compatible with existing Maven plugins and extensions
* Daemon process management
* Intelligent memory management
* Native executable available

[](https://maven.apache.org/tools/mvnd.html)
Installation[](https://maven.apache.org/tools/mvnd.html#installation)
---------------------------------------------------------------------

You can download Maven Daemon from our [download page](https://maven.apache.org/download.html#Maven_Daemon).

For more detailed information and documentation, visit the [Maven Daemon GitHub repository](https://github.com/apache/maven-mvnd).

[](https://maven.apache.org/tools/mvnd.html)
Usage[](https://maven.apache.org/tools/mvnd.html#usage)
-------------------------------------------------------

Instead of using the `mvn` command, use `mvnd`:

```bash
mvnd clean verify
```

The daemon will stay alive in the background, ready to process subsequent builds much faster.

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
