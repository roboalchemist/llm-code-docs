# Source: https://maven.apache.org/guides/mini/guide-generating-sources.html

Title: Guide to generating sources – Maven

URL Source: https://maven.apache.org/guides/mini/guide-generating-sources.html

Markdown Content:
Guide to generating sources – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Guide to generating sources [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-generating-sources.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-generating-sources.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-generating-sources.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
    *   [Maven 4](https://maven.apache.org/guides/mini/guide-generating-sources.html)
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
*   [Components](https://maven.apache.org/guides/mini/guide-generating-sources.html)
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

[](https://maven.apache.org/guides/mini/guide-generating-sources.html)
Guide to generating sources
===========================

Let's run though a short example. To generate sources you must first have a plugin that participates in the `generate-sources` phase like the [ANTLR4 Maven Plugin](https://www.antlr.org/api/maven-plugin/latest/). You configure its execution in the POM:

1.   ```xml
<project xmlns="http://maven.apache.org/POM/4.0.0">
```
2.   ```xml
...
```
3.   ```xml
<build>
```
4.   ```xml
<plugins>
```
5.   ```xml
<plugin>
```
6.   ```xml
<groupId>org.antlr</groupId>
```
7.   ```xml
<artifactId>antlr4-maven-plugin</artifactId>
```
8.   ```xml
<version>4.5.3</version>
```
9.   ```xml
<executions>
```
10.   ```xml
<execution>
```
11.   ```xml
<id>antlr</id>
```
12.   ```xml
<goals>
```
13.   ```xml
<goal>antlr4</goal>
```
14.   ```xml
</goals>
```
15.   ```xml
</execution>
```
16.   ```xml
</executions>
```
17.   ```xml
</plugin>
```
18.   ```xml
</plugins>
```
19.   ```xml
</build>
```
20.   ```xml
...
```
21.   ```xml
</project>
```

When you type `mvn compile`, Maven walks through the [lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html) and eventually hits the `generate-sources` phase. It sees that a plugin is configured that wants to participate in that phase, and executes the ANTLR4 Maven Plugin with the given configuration. Later, during the compile phase, all the code generated from the grammar files is compiled without further configuration.

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
