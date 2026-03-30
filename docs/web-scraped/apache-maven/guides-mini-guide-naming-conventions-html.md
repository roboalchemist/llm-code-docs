# Source: https://maven.apache.org/guides/mini/guide-naming-conventions.html

Title: Naming conventions of Maven coordinates (groupId, artifactId, and version) – Maven

URL Source: https://maven.apache.org/guides/mini/guide-naming-conventions.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
Naming conventions of Maven coordinates (groupId, artifactId, and version) – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Naming conventions of Maven coordinates (groupId, artifactId, and version) [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-naming-conventions.md)
*   | Last Published: 2026-03-13
*   |[Get Sources](https://maven.apache.org/scm.html)
*   [Downloads](https://maven.apache.org/download.cgi)

*   [Welcome](https://maven.apache.org/index.html)
*   [License](https://www.apache.org/licenses/)
*   About Maven
*   [What is Maven?](https://maven.apache.org/what-is-maven.html)
*   [Installation](https://maven.apache.org/install.html)
*   [Downloads](https://maven.apache.org/download.html)
*   [Use](https://maven.apache.org/run.html)
*   [Configure](https://maven.apache.org/configure.html)
*   [Release Notes](https://maven.apache.org/docs/history.html)
*   [Security Reports](https://maven.apache.org/security.html)
*   Documentation
*   [Maven Plugins](https://maven.apache.org/plugins/index.html)
*   [Maven Extensions](https://maven.apache.org/extensions/index.html)
*   [Maven Tools](https://maven.apache.org/tools/index.html)
    *   [Maven Daemon](https://maven.apache.org/tools/mvnd.html)
    *   [Maven Upgrade Tool](https://maven.apache.org/tools/mvnup.html)
    *   [Maven Wrapper](https://maven.apache.org/tools/mavenwrapper.html)

*   [Index (category)](https://maven.apache.org/guides/index.html)
*   [User Manual](https://maven.apache.org/users/index.html)
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
        *   [Naming Conventions](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
        *   [The Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
        *   [The POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html)
        *   [Configuring Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
        *   [POM 4.0.0 Reference](https://maven.apache.org/pom.html)
        *   [Settings Reference](https://maven.apache.org/settings.html)

    *   [Maven 4](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
        *   [What's new in Maven 4?](https://maven.apache.org/whatsnewinmaven4.html)
        *   [Starting with Maven 4](https://maven.apache.org/guides/mini/guide-migration-to-mvn4.html)
        *   [Maven Mixins](https://maven.apache.org/guides/mini/guide-mixins.html)

    *   [Guides](https://maven.apache.org/guides/mini/index.html)
    *   [FAQ](https://maven.apache.org/general.html)

*   [Maven Repositories](https://maven.apache.org/repositories/index.html)
*   [Plugin Development](https://maven.apache.org/plugin-developers/index.html)
*   [Contribute to Maven](https://maven.apache.org/developers/index.html)
*   [Books and Resources](https://maven.apache.org/articles.html)
*   Community
*   [Community Overview](https://maven.apache.org/community.html)
*   [Project Roles](https://maven.apache.org/project-roles.html)
*   [How to Contribute](https://maven.apache.org/guides/development/guide-helping.html)
*   [Getting Help](https://maven.apache.org/users/getting-help.html)
*   [Issue Management](https://maven.apache.org/issue-management.html)
*   [Getting Maven Source](https://maven.apache.org/scm.html)
*   [The Maven Team](https://maven.apache.org/team.html)
*   Project Documentation
*   [Project Information](https://maven.apache.org/project-info.html)
*   Maven Projects
*   [Maven](https://maven.apache.org/ref/current)
*   [Archetypes](https://maven.apache.org/archetypes/index.html)
*   [Extensions](https://maven.apache.org/extensions/index.html)
*   [Parent POMs](https://maven.apache.org/pom/index.html)
*   [Plugins](https://maven.apache.org/plugins/index.html)
*   [Skins](https://maven.apache.org/skins/index.html)
*   [Components](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
    *   [Archetype](https://maven.apache.org/archetype/index.html)
    *   [Artifact Resolver](https://maven.apache.org/resolver/index.html)
    *   [Doxia](https://maven.apache.org/doxia/index.html)
    *   [Indexer](https://maven.apache.org/maven-indexer/index.html)
    *   [JXR](https://maven.apache.org/jxr/index.html)
    *   [Plugin Testing](https://maven.apache.org/plugin-testing/index.html)
    *   [Plugin Tools](https://maven.apache.org/plugin-tools/index.html)
    *   [Resource Bundles](https://maven.apache.org/apache-resource-bundles/index.html)
    *   [SCM](https://maven.apache.org/scm/index.html)
    *   [Shared Components](https://maven.apache.org/shared/index.html)
    *   [Surefire](https://maven.apache.org/surefire/index.html)
    *   [Wagon](https://maven.apache.org/wagon/index.html)

*   ASF
*   [How Apache Works](https://www.apache.org/foundation/how-it-works.html)
*   [Foundation](https://www.apache.org/foundation/)
*   [Data Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
*   [Sponsoring Apache](https://www.apache.org/foundation/sponsorship.html)
*   [Thanks](https://www.apache.org/foundation/thanks.html)

[![Image 4: Built by Maven](https://maven.apache.org/images/logos/maven-feather.png)](https://maven.apache.org/)

[](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
Naming convention of Maven coordinates
======================================

So that Maven can identify and utilise any artifact (e.g. a `.jar` file), every artifact must be identifiable through a unique combination of three identifiers. This combination is called the “[Maven coordinates](https://maven.apache.org/pom.html#Maven_Coordinates)”. Maven coordinates consist of a project group identifier named `groupId`, an artifact identifier named `artifactId`, and the version identifier named `version`.

This document defines the naming conventions of Maven coordinates.

You should follow this convention whenever you create a new artifact.

[](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
Project group identifier
------------------------

When projects of the same organization are topically related, we say they belong to the same “project group”. The `groupId` uniquely identifies a project group across all other groups. Each `groupId` should follow [Java's package name rules](https://docs.oracle.com/javase/specs/jls/se21/html/jls-6.html#d5e8762). This means it starts with a reversed domain name you control.

Examples

```
org.apache.maven
org.apache.commons
com.google.guava
```

There are many legacy projects that do not follow this convention and instead use single word group IDs. However, it will be difficult to get a new single word group ID approved for inclusion in the Maven Central repository.

You can create as many subgroups as you want. A good way to determine the granularity of the `groupId` is to look at the project group's structure. If there are multiple projects of the same topic or type, e.g. plugins, those may be grouped in a subgroup. Each subgroup should append a new identifier to the parent's `groupId`.

Example

```
// Parent project group
org.apache.maven

// Subgroups
org.apache.maven.plugins
org.apache.maven.reporting
```
[](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
Artifact identifier
-------------------

The `artifactId` is the name of the artifact. The identifiers should only consist of _lowercase_ letters, digits, and hyphens.

Examples

```
commons-math
maven-clean-plugin
```
[](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
Version identifier
------------------

We recommend that the `version` follow the rules of [Semantic Versioning 1.0.0](https://semver.org/spec/v1.0.0.html). It should start with the major version, followed by the minor version and the patch version. All three are numeric, separated by a dot.

Examples

```
1.0.0
2.3.2
3.5.42
```

You can add labels for pre-releases or build metadata after the patch version. Avoid using dates in those labels, because they are usually associated with unstable versions.

Examples

```
// Pre-releases
1.0.0-beta
1.0.0-M1
1.0.0-rc2

// Build metadata
1.2.3+dfc0c87
2.3.4+15433
```
[](https://maven.apache.org/guides/mini/guide-naming-conventions.html)
### Unstable versions (SNAPSHOT)

`SNAPSHOT`s are artifacts built in between releases. They may be built from a particular commit or from code that isn't even committed to the source repository. They are a snapshot of the project at a particular point in time, generally used for testing. Unlike release versions, snapshot artifacts can and do change over time.

Usually the snapshot has the version of the next anticipated release followed by `-SNAPSHOT`, e.g. `1.0.1-SNAPSHOT`.

Maven treats artifacts with such versions in a special way during deployment and stores them in the `snapshotRepository` if one is defined in the [POM file](https://maven.apache.org/pom.html#Repository).

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
