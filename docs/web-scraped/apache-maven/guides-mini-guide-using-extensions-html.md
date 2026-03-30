# Source: https://maven.apache.org/guides/mini/guide-using-extensions.html

Title: Using Extensions – Maven

URL Source: https://maven.apache.org/guides/mini/guide-using-extensions.html

Markdown Content:
Using Extensions – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Using Extensions [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-using-extensions.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-using-extensions.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-using-extensions.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
    *   [Maven 4](https://maven.apache.org/guides/mini/guide-using-extensions.html)
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
*   [Components](https://maven.apache.org/guides/mini/guide-using-extensions.html)
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

[](https://maven.apache.org/guides/mini/guide-using-extensions.html)
Using Extensions
================

Extensions are a way to add classes to either the [Core Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Core_Classloader) (Core Extensions) or the [Project Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Project_Classloaders) (Build Extensions). This is necessary for adjusting Maven in a way that affects more than just one plug-in.

The mechanism allows extensions to either replace default [Sisu components](https://www.eclipse.org/sisu/) with custom ones or add new components which are used at run time. In addition one could also expose additional packages from the Core Classloader.

Extensions are typically used to enable [Wagon providers](https://maven.apache.org/wagon/wagon-providers/), used for the transport of artifact between repositories, and plug-ins which [provide lifecycle enhancements](https://maven.apache.org/examples/maven-3-lifecycle-extensions.html).

[](https://maven.apache.org/guides/mini/guide-using-extensions.html)
Loading Extensions[](https://maven.apache.org/guides/mini/guide-using-extensions.html#loading-extensions)
---------------------------------------------------------------------------------------------------------

There are different means of loading extensions depending on the type. There are _core extensions_ which are loaded **early** and build extensions which are loaded **late**. Some extensions require early loading as they fundamentally change Maven behaviour. An extension's documentation should indicate whether it provides a core or a build extension.

[](https://maven.apache.org/guides/mini/guide-using-extensions.html)
### Core Extension[](https://maven.apache.org/guides/mini/guide-using-extensions.html#core-extension)

*   Registered via extension jar in `${maven.home}/lib/ext`
*   Registered via CLI argument `mvn -Dmaven.ext.class.path=extension.jar`
*   Registered via [`.mvn/extensions.xml` file](https://maven.apache.org/configure.html#mvn-extensions-xml-file)

[](https://maven.apache.org/guides/mini/guide-using-extensions.html)
### Build Extension[](https://maven.apache.org/guides/mini/guide-using-extensions.html#build-extension)

*   Registered via [`project->build->plugins->plugin`](https://maven.apache.org/pom.html#Plugins) with element `extensions` being set to `true`. This is useful for regular plug-ins carrying some extensions.

Example:

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
<groupId>org.apache.felix</groupId>
```
    7.   ```xml
<artifactId>maven-bundle-plugin</artifactId>
```
    8.   ```xml
<extensions>true</extensions>
```
    9.   ```xml
<configuration>
```
    10.   ```xml
...
```
    11.   ```xml
</configuration>
```
    12.   ```xml
</plugin>
```
    13.   ```xml
</plugins>
```
    14.   ```xml
</build>
```
    15.   ```xml
...
```
    16.   ```xml
</project>
```

*   Registered as build extension in [`project->build->extensions->extension`](https://maven.apache.org/pom.html#Extensions)

Example:

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
<extensions>
```
    5.   ```xml
<extension>
```
    6.   ```xml
<groupId>org.apache.maven.wagon</groupId>
```
    7.   ```xml
<artifactId>wagon-ftp</artifactId>
```
    8.   ```xml
<version>2.10</version>
```
    9.   ```xml
</extension>
```
    10.   ```xml
</extensions>
```
    11.   ```xml
</build>
```
    12.   ```xml
...
```
    13.   ```xml
</project>
```

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
