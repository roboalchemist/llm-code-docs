# Source: https://maven.apache.org/ref/current

Title: Introduction – Apache Maven

URL Source: https://maven.apache.org/ref/current

Markdown Content:
Introduction – Apache Maven
===============

[![Image 1: Apache Maven](https://maven.apache.org/images/apache-maven-project.png)](https://maven.apache.org/)
===============================================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* [Ref](https://maven.apache.org/)/
* [Maven 3.9.14](https://maven.apache.org/ref/)/
* Introduction [![Image 3: Edit](https://maven.apache.org/ref/images/accessories-text-editor.png)](https://github.com/apache/maven/tree/maven-3.9.14/src/site/xdoc/index.xml)
* | Last Published: 2026-03-09
* Version: 3.9.14

* Overview
* [Introduction](https://maven.apache.org/ref/current)
* [Javadocs](https://maven.apache.org/ref/apidocs/index.html)
* [Source Xref](https://maven.apache.org/ref/xref/index.html)
* [License](http://www.apache.org/licenses/)
* [Download](https://maven.apache.org/ref/download.html)
* Descriptors Reference
* [POM](https://maven.apache.org/ref/maven-model/maven.html)
* [Settings](https://maven.apache.org/ref/maven-settings/settings.html)
* [Toolchains](https://maven.apache.org/ref/maven-core/toolchains.html)
* Reference
* [Lifecycles](https://maven.apache.org/ref/maven-core/lifecycles.html)
* [Plugin Bindings to Default Lifecycle](https://maven.apache.org/ref/maven-core/default-bindings.html)
* [Artifact Handlers](https://maven.apache.org/ref/maven-core/artifact-handlers.html)
* [CLI options](https://maven.apache.org/ref/maven-embedder/cli.html)
* [Super POM](https://maven.apache.org/ref/maven-model-builder/super-pom.html)
* Development
* [Maven Developer Centre](https://maven.apache.org/developers/index.html)
* [Maven Core ITs](https://maven.apache.org/core-its/index.html)
* Modules
* [Maven Plugin API](https://maven.apache.org/ref/maven-plugin-api/index.html)
* [Maven Builder Support](https://maven.apache.org/ref/maven-builder-support/index.html)
* [Maven Model](https://maven.apache.org/ref/maven-model/index.html)
* [Maven Model Builder](https://maven.apache.org/ref/maven-model-builder/index.html)
* [Maven Core](https://maven.apache.org/ref/maven-core/index.html)
* [Maven Settings](https://maven.apache.org/ref/maven-settings/index.html)
* [Maven Settings Builder](https://maven.apache.org/ref/maven-settings-builder/index.html)
* [Maven Artifact](https://maven.apache.org/ref/maven-artifact/index.html)
* [Maven Artifact Resolver Provider](https://maven.apache.org/ref/maven-resolver-provider/index.html)
* [Maven Repository Metadata Model](https://maven.apache.org/ref/maven-repository-metadata/index.html)
* [Maven SLF4J Simple Provider](https://maven.apache.org/ref/maven-slf4j-provider/index.html)
* [Maven Embedder](https://maven.apache.org/ref/maven-embedder/index.html)
* [Maven Compat](https://maven.apache.org/ref/maven-compat/index.html)
* [Apache Maven Distribution](https://maven.apache.org/ref/apache-maven/index.html)
* Project Documentation
* [Project Information](https://maven.apache.org/ref/project-info.html)
  * [About](https://maven.apache.org/ref/current)
  * [Summary](https://maven.apache.org/ref/summary.html)
  * [Maven Coordinates](https://maven.apache.org/ref/dependency-info.html)
  * [Project Modules](https://maven.apache.org/ref/modules.html)
  * [Team](https://maven.apache.org/ref/team.html)
  * [Source Code Management](https://maven.apache.org/ref/scm.html)
  * [Issue Management](https://maven.apache.org/ref/issue-management.html)
  * [Mailing Lists](https://maven.apache.org/ref/mailing-lists.html)
  * [Dependency Management](https://maven.apache.org/ref/dependency-management.html)
  * [Dependency Convergence](https://maven.apache.org/ref/dependency-convergence.html)
  * [CI Management](https://maven.apache.org/ref/ci-management.html)
  * [Plugin Management](https://maven.apache.org/ref/plugin-management.html)
  * [Plugins](https://maven.apache.org/ref/plugins.html)
  * [Distribution Management](https://maven.apache.org/ref/distribution-management.html)

* [Project Reports](https://maven.apache.org/ref/project-reports.html)
* Maven Projects
* [Maven](https://maven.apache.org/current)
* [Archetypes](https://maven.apache.org/archetypes/index.html)
* [Extensions](https://maven.apache.org/extensions/index.html)
* [Parent POMs](https://maven.apache.org/pom/index.html)
* [Plugins](https://maven.apache.org/plugins/index.html)
* [Skins](https://maven.apache.org/skins/index.html)
* [Components](https://maven.apache.org/ref/current)
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

[![Image 4: Built by Maven](https://maven.apache.org/ref/images/logos/maven-feather.png)](https://maven.apache.org/)

[](https://maven.apache.org/ref/current)
Apache Maven 3.x
================

Maven is a project development management and comprehension tool. Based on the concept of a project object model: builds, dependency management, documentation creation, site publication, and distribution publication are all controlled from [the `pom.xml` declarative file](https://maven.apache.org/ref/maven-model/maven.html). Maven can be extended by [plugins](https://maven.apache.org/plugins/) to utilise a number of other development tools for reporting or the build process.

* * *

© 2001–2026 [The Apache Software Foundation](https://www.apache.org/)
