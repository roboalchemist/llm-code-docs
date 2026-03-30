# Source: https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html

Title: Introduction to the Standard Directory Layout – Maven

URL Source: https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
Introduction to the Standard Directory Layout – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Introduction to the Standard Directory Layout [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/introduction/introduction-to-the-standard-directory-layout.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
    *   [Maven 4](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
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
*   [Components](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
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

[](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
Introduction to the Standard Directory Layout
=============================================

Having a common directory layout allows users familiar with one Maven project to immediately feel at home in another Maven project. The advantages are analogous to adopting a site-wide look-and-feel.

The next section documents the directory layout expected by Maven and the directory layout created by Maven. Try to conform to this structure as much as possible. However, if you can't, these settings can be overridden via the project descriptor.

|  |  |
| --- | --- |
| `src/main/java` | Application/Library sources |
| `src/main/resources` | Application/Library resources |
| `src/main/filters` | Resource filter files |
| `src/main/webapp` | Web application sources |
| `src/test/java` | Test sources |
| `src/test/resources` | Test resources |
| `src/test/filters` | Test resource filter files |
| `src/it` | Integration Tests (primarily for plugins) |
| `src/assembly` | Assembly descriptors |
| `src/site` | Site |
| `LICENSE.txt` | Project's license |
| `NOTICE.txt` | Notices and attributions required by libraries that the project depends on |
| `README.txt` | Project's readme |

At the top level, files descriptive of the project: a `pom.xml` file. In addition, there are textual documents meant for the user to be able to read immediately on receiving the source: `README.txt`, `LICENSE.txt`, etc.

There are just two subdirectories of this structure: `src` and `target`. The only other directories that would be expected here are metadata like `CVS`, `.git` or `.svn`, and any subprojects in a multiproject build (each of which would be laid out as above).

The `target` directory is used to house all output of the build.

The `src` directory contains all of the source material for building the project, its site and so on. It contains a subdirectory for each type: `main` for the main build artifact, `test` for the unit test code and resources, `site` and so on.

Within artifact producing source directories (ie. `main` and `test`), there is one directory for the language `java` (under which the normal package hierarchy exists), and one for `resources` (the structure which is copied to the target classpath given the default resource definition).

If there are other contributing sources to the artifact build, they would be under other subdirectories. For example `src/main/antlr` would contain Antlr grammar definition files.

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
