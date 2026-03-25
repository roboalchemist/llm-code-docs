# Source: https://maven.apache.org/guides/mini/guide-multiple-modules.html

Title: Guide to Working with Multiple Modules – Maven

URL Source: https://maven.apache.org/guides/mini/guide-multiple-modules.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
Guide to Working with Multiple Modules – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Guide to Working with Multiple Modules [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-multiple-modules.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
    *   [Maven 4](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
        *   [What's new in Maven 4?](https://maven.apache.org/whatsnewinmaven4.html)
        *   [Starting with Maven 4](https://maven.apache.org/guides/mini/guide-migration-to-mvn4.html)
        *   [Maven Mixins](https://maven.apache.org/guides/mini/guide-mixins.html)

    *   [Guides](https://maven.apache.org/guides/mini/index.html)
        *   [Configuring for Reproducible Builds](https://maven.apache.org/guides/mini/guide-reproducible-builds.html)
        *   [Creating Assemblies](https://maven.apache.org/guides/mini/guide-assemblies.html)
        *   [Configuring Archive Plugins](https://maven.apache.org/guides/mini/guide-archive-configuration.html)
        *   [Configuring Maven](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
        *   [Generating Sources](https://maven.apache.org/guides/mini/guide-generating-sources.html)
        *   [Working with Manifests](https://maven.apache.org/guides/mini/guide-manifest.html)
        *   [Maven Classloading](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
        *   [Using Modules (Maven 3)](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
        *   [Using Subprojects (Maven 4)](https://maven.apache.org/guides/mini/guide-multiple-subprojects-4.html)
        *   [Using Release Plugin](https://maven.apache.org/guides/mini/guide-releasing.html)
        *   [Using Ant](https://maven.apache.org/guides/mini/guide-using-ant.html)
        *   [Using Modello](https://maven.apache.org/guides/mini/guide-using-modello.html)
        *   [Using Extensions](https://maven.apache.org/guides/mini/guide-using-extensions.html)
        *   [Building for Different Environments](https://maven.apache.org/guides/mini/guide-building-for-different-environments.html)
        *   [Using Toolchains](https://maven.apache.org/guides/mini/guide-using-toolchains.html)
        *   [Maven CI Friendly Version](https://maven.apache.org/guides/mini/guide-maven-ci-friendly.html)

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
*   [Components](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
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

[](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
Guide to Working with Multiple Modules
======================================

(If you're working with Maven 4, please refer to the [Maven 4 edition of this guide](https://maven.apache.org/guides/mini/guide-multiple-modules-4.html))

As seen in the introduction to the POM, Maven supports [project](https://maven.apache.org/glossary.html#Project) aggregation in addition to project inheritance. This section outlines how Maven processes projects with multiple modules, and how you can work with them more effectively.

[](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
The Reactor
-----------

The mechanism in Maven that handles multi-module projects is referred to as the _reactor_. This part of the Maven core does the following:

*   Collects all the available modules to build
*   Sorts the projects into the correct build order
*   Builds the selected projects in order

[](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
### Reactor Sorting

Because modules within a multi-module build can depend on each other, it is important that the reactor sorts all the projects in a way that guarantees any project is built before it is required.

The following relationships are honoured when sorting projects:

*   a project dependency on another module in the build
*   a plugin declaration where the plugin is another module in the build
*   a plugin dependency on another module in the build
*   a build extension declaration on another module in the build
*   the order declared in the `<modules>` element (if no other rule applies)

Note that only “instantiated” references are used - `dependencyManagement` and `pluginManagement` elements do not cause a change to the reactor sort order.

[](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
### Command Line Options

No special configuration is required to take advantage of the reactor, however it is possible to customize its behavior.

The following command line switches are available:

*   `--resume-from` - resumes a reactor from the specified project (e.g. when it fails in the middle)
*   `--also-make` - build the specified projects, and any of their dependencies in the reactor
*   `--also-make-dependents` - build the specified projects, and any that depend on them
*   `--fail-fast` - the default behavior - whenever a module build fails, stop the overall build immediately
*   `--fail-at-end` - if a particular module build fails, continue the rest of the reactor and report all failed modules at the end instead
*   `--non-recursive` - do not use a reactor build, even if the current project declares modules and just build the project in the current directory

Refer to the Maven command line interface reference for more information on these switches.

[](https://maven.apache.org/guides/mini/guide-multiple-modules.html)
More information
----------------

*   [Chapter 6. A Multi-module Project (Maven by Example)](http://books.sonatype.com/mvnex-book/reference/multimodule.html)

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
