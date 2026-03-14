# Source: https://maven.apache.org/repository/index.html

Title: Maven Central Repository – Maven

URL Source: https://maven.apache.org/repository/index.html

Markdown Content:
Maven Central Repository – Maven
===============

[![Image 3](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 4](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* Maven Central Repository [![Image 5: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/repository/index.md)
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
  * [Maven Central Repository](https://maven.apache.org/repository/index.html)
    * [Maintaining your Metadata](https://maven.apache.org/project-faq.html)
    * [Guide to Uploading Artifacts](https://maven.apache.org/repository/guide-central-repository-upload.html)
    * [Fixing Metadata](https://maven.apache.org/repository/central-metadata.html)
    * [Central Index](https://maven.apache.org/repository/central-index.html)
    * [Repository Layout](https://maven.apache.org/repository/layout.html)

  * [Maven Artifacts](https://maven.apache.org/repositories/artifacts.html)
  * [Maven Metadata](https://maven.apache.org/repositories/metadata.html)
  * [Maven Layout](https://maven.apache.org/repositories/layout.html)
  * [Maven Local Repository](https://maven.apache.org/repositories/local.html)
  * [Maven Remote Repositories](https://maven.apache.org/repositories/remote.html)

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
* [Components](https://maven.apache.org/repository/index.html)
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

[![Image 6: Built by Maven](https://maven.apache.org/images/logos/maven-feather.png)](https://maven.apache.org/)

[](https://maven.apache.org/repository/index.html)
Maven Central Repository
========================

This documentation is for those that need to use or contribute to the Maven `central` repository. This includes those that need dependencies for their own build or projects that wish to have their releases added to the Maven `central` repository, even if they don't use Maven as their build tool.

![Image 7: Warning](https://maven.apache.org/images/icon_warning_sml.gif) Be aware of those announcements:

* [**Discontinuing support for TLSv1.1** and below as of **June 15th 2018**](https://central.sonatype.org/faq/tls-info/)
* [**Discontinuing support for HTTP** as of **January 15th 2020**](https://central.sonatype.org/news/20190715_http_deprecation_update)

[](https://maven.apache.org/repository/index.html)
Content[](https://maven.apache.org/repository/index.html#content)
-----------------------------------------------------------------

* [Maintaining your Metadata](https://maven.apache.org/project-faq.html) - Information for third-party projects
* [Guide to uploading artifacts](https://maven.apache.org/repository/guide-central-repository-upload.html) - How to get things uploaded to the central repository
* [Fixing Central Metadata](https://maven.apache.org/repository/central-metadata.html) - How to fix issues in content already uploaded

![Image 8](https://maven.apache.org/repository/maven-central-repository.png)

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
