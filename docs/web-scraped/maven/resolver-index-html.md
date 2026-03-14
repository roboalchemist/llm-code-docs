# Source: https://maven.apache.org/resolver/index.html

Title: Introduction – Artifact Resolver

URL Source: https://maven.apache.org/resolver/index.html

Markdown Content:
Introduction – Artifact Resolver
===============

[![Image 2](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 3](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

* [Apache](https://www.apache.org/)/
* [Maven](https://maven.apache.org/index.html)/
* [Artifact Resolver](https://maven.apache.org/resolver/index.html)/
* Introduction [![Image 4: Edit](https://maven.apache.org/resolver/images/accessories-text-editor.png)](https://github.com/apache/maven-resolver/tree/maven-resolver-2.0.16/src/site/xdoc/index.xml)
* | Last Published: 2026-02-20
* Version: 2.0.16

* Overview
* [Introduction](https://maven.apache.org/resolver/index.html)
* [What Is Resolver?](https://maven.apache.org/resolver/what-is-resolver.html)
* [Checksums](https://maven.apache.org/resolver/about-checksums.html)
* [Expected Checksums](https://maven.apache.org/resolver/expected-checksums.html)
* [Local Repository](https://maven.apache.org/resolver/local-repository.html)
* [Remote Repository Filtering](https://maven.apache.org/resolver/remote-repository-filtering.html)
* [Third-party Integrations](https://maven.apache.org/resolver/third-party-integrations.html)
* [Repository Key Function](https://maven.apache.org/resolver/repository-key-function.html)
* [Download](https://maven.apache.org/resolver/download.html)
* Guides
* [API Compatibility](https://maven.apache.org/resolver/api-compatibility.html)
* [Upgrading Resolver](https://maven.apache.org/resolver/upgrading-resolver.html)
* [Using Resolver in Maven Plugins](https://maven.apache.org/resolver/using-resolver-in-maven-plugins.html)
* [Transitive Dependency Resolution](https://maven.apache.org/resolver/transitive-dependency-resolution.html)
* [Dependency Graph](https://maven.apache.org/resolver/dependency-graph.html)
* [Creating a RepositorySystemSession](https://maven.apache.org/resolver/creating-a-repository-system-session.html)
* [Resolving Dependencies](https://maven.apache.org/resolver/resolving-dependencies.html)
* [Common Misconceptions](https://maven.apache.org/resolver/common-misconceptions.html)
* [Artifact Deployment](https://maven.apache.org/resolver/deployment.html)
* [How Resolver Works](https://maven.apache.org/resolver/how-resolver-works.html)
* [Transporter Known Issues](https://maven.apache.org/resolver/transporter-known-issues.html)
* Reference
* [Configuration](https://maven.apache.org/resolver/configuration.html)
* [JavaDocs](https://maven.apache.org/resolver/apidocs/index.html)
* [Source Xref](https://maven.apache.org/resolver/xref/index.html)
* [License](https://www.apache.org/licenses/)
* See Also
* [Maven Artifact Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/)
* Modules
* [Maven Artifact Resolver API](https://maven.apache.org/resolver/maven-resolver-api/index.html)
* [Maven Artifact Resolver SPI](https://maven.apache.org/resolver/maven-resolver-spi/index.html)
* [Maven Artifact Resolver Utilities](https://maven.apache.org/resolver/maven-resolver-util/index.html)
* [Maven Artifact Resolver Named Locks](https://maven.apache.org/resolver/maven-resolver-named-locks/index.html)
* [Maven Artifact Resolver Named Locks using Hazelcast (deprecated)](https://maven.apache.org/resolver/maven-resolver-named-locks-hazelcast/index.html)
* [Maven Artifact Resolver Named Locks using IPC](https://maven.apache.org/resolver/maven-resolver-named-locks-ipc/index.html)
* [Maven Artifact Resolver Named Locks using Redisson](https://maven.apache.org/resolver/maven-resolver-named-locks-redisson/index.html)
* [Maven Artifact Resolver Implementation](https://maven.apache.org/resolver/maven-resolver-impl/index.html)
* [Maven Artifact Resolver Test Utilities](https://maven.apache.org/resolver/maven-resolver-test-util/index.html)
* [Maven Artifact Resolver Test Utilities HTTP](https://maven.apache.org/resolver/maven-resolver-test-http/index.html)
* [Maven Artifact Resolver Connector Basic](https://maven.apache.org/resolver/maven-resolver-connector-basic/index.html)
* [Maven Artifact Resolver Transport Classpath](https://maven.apache.org/resolver/maven-resolver-transport-classpath/index.html)
* [Maven Artifact Resolver Transport File](https://maven.apache.org/resolver/maven-resolver-transport-file/index.html)
* [Maven Artifact Resolver Transport Jetty](https://maven.apache.org/resolver/maven-resolver-transport-jetty/index.html)
* [Maven Artifact Resolver Transport JDK Parent](https://maven.apache.org/resolver/maven-resolver-transport-jdk-parent/index.html)
* [Maven Artifact Resolver Transport Apache](https://maven.apache.org/resolver/maven-resolver-transport-apache/index.html)
* [Maven Artifact Resolver Transport Wagon](https://maven.apache.org/resolver/maven-resolver-transport-wagon/index.html)
* [Maven Artifact Resolver Transport S3 MinIO](https://maven.apache.org/resolver/maven-resolver-transport-minio/index.html)
* [Maven Artifact Resolver GnuPG Signer Generator](https://maven.apache.org/resolver/maven-resolver-generator-gnupg/index.html)
* [Maven Artifact Resolver Sigstore Signer Generator](https://maven.apache.org/resolver/maven-resolver-generator-sigstore/index.html)
* [Maven Artifact Resolver Instance Supplier Maven3](https://maven.apache.org/resolver/maven-resolver-supplier-mvn3/index.html)
* [Maven Artifact Resolver Instance Supplier Maven4](https://maven.apache.org/resolver/maven-resolver-supplier-mvn4/index.html)
* [Maven Artifact Resolver Demos](https://maven.apache.org/resolver/maven-resolver-demos/index.html)
* [Maven Artifact Resolver Tools](https://maven.apache.org/resolver/maven-resolver-tools/index.html)
* Project Documentation
* [Project Information](https://maven.apache.org/resolver/project-info.html)
  * [About](https://maven.apache.org/resolver/index.html)
  * [Summary](https://maven.apache.org/resolver/summary.html)
  * [Maven Coordinates](https://maven.apache.org/resolver/dependency-info.html)
  * [Project Modules](https://maven.apache.org/resolver/modules.html)
  * [Team](https://maven.apache.org/resolver/team.html)
  * [Source Code Management](https://maven.apache.org/resolver/scm.html)
  * [Issue Management](https://maven.apache.org/resolver/issue-management.html)
  * [Mailing Lists](https://maven.apache.org/resolver/mailing-lists.html)
  * [Dependency Management](https://maven.apache.org/resolver/dependency-management.html)
  * [Dependency Convergence](https://maven.apache.org/resolver/dependency-convergence.html)
  * [CI Management](https://maven.apache.org/resolver/ci-management.html)
  * [Plugin Management](https://maven.apache.org/resolver/plugin-management.html)
  * [Plugins](https://maven.apache.org/resolver/plugins.html)
  * [Distribution Management](https://maven.apache.org/resolver/distribution-management.html)

* [Project Reports](https://maven.apache.org/resolver/project-reports.html)
* Maven Projects
* [Maven](https://maven.apache.org/ref/current)
* [Archetypes](https://maven.apache.org/archetypes/index.html)
* [Extensions](https://maven.apache.org/extensions/index.html)
* [Parent POMs](https://maven.apache.org/pom/index.html)
* [Plugins](https://maven.apache.org/plugins/index.html)
* [Skins](https://maven.apache.org/skins/index.html)
* [Components](https://maven.apache.org/resolver/index.html)
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

[![Image 5: Built by Maven](https://maven.apache.org/resolver/images/logos/maven-feather.png)](https://maven.apache.org/)

[](https://maven.apache.org/resolver/index.html)
Apache Maven Artifact Resolver
==============================

Apache Maven Artifact Resolver is a library for working with artifact repositories and dependency resolution.

Maven Artifact Resolver deals with the specification of local repository, remote repository, developer workspaces, artifact transports, and artifact resolution. It is expected to be extended by a concrete repository implementation, such as [Maven Artifact Resolver Provider](https://maven.apache.org/ref/current/maven-resolver-provider/) for Maven repositories or any other provider for other repository formats.

![Image 6](https://maven.apache.org/resolver/images/maven-resolver-deps.png)

[](https://maven.apache.org/resolver/index.html)
See Also[](https://maven.apache.org/resolver/index.html#see-also)
-----------------------------------------------------------------

* [Maven Artifact Resolver Ant Tasks](https://maven.apache.org/resolver-ant-tasks/)

* * *

© 2010–2026 [The Apache Software Foundation](https://www.apache.org/)
