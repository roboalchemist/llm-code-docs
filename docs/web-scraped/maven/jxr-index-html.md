# Source: https://maven.apache.org/jxr/index.html

Title: JXR – Introduction

URL Source: https://maven.apache.org/jxr/index.html

Markdown Content:
JXR – Introduction
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)

* * *

* [Apache](https://www.apache.org/ "Apache")/
* [Maven](https://maven.apache.org/index.html "Maven")/
* [JXR](https://maven.apache.org/jxr/index.html "JXR")/
* Introduction [![Image 3: Edit](https://maven.apache.org/jxr/images/accessories-text-editor.png)](https://github.com/apache/maven-jxr/tree/jxr-3.6.0/src/site/apt/index.apt)
* | Last Published: 2024-10-22
* Version: 3.6.0

* Overview
* [Introduction](https://maven.apache.org/jxr/index.html)
* [Maven JXR Plugin](https://maven.apache.org/jxr/maven-jxr-plugin/ "Maven JXR Plugin")
* [FAQ](https://maven.apache.org/jxr/faq.html "FAQ")
* [License](http://www.apache.org/licenses/ "License")
* [Download](https://maven.apache.org/jxr/download.html "Download")
* Examples
* [Using Maven JXR in Java](https://maven.apache.org/jxr/examples/java.html "Using Maven JXR in Java")
* Modules
* [Maven JXR](https://maven.apache.org/jxr/maven-jxr/index.html "Maven JXR")
* [Maven JXR Plugin](https://maven.apache.org/jxr/maven-jxr-plugin/index.html "Maven JXR Plugin")
* Project Documentation
* [Project Information](https://maven.apache.org/jxr/project-info.html "Project Information")
  * [About](https://maven.apache.org/jxr/index.html)
  * [Summary](https://maven.apache.org/jxr/summary.html "Summary")
  * [Maven Coordinates](https://maven.apache.org/jxr/dependency-info.html "Maven Coordinates")
  * [Project Modules](https://maven.apache.org/jxr/modules.html "Project Modules")
  * [Team](https://maven.apache.org/jxr/team.html "Team")
  * [Source Code Management](https://maven.apache.org/jxr/scm.html "Source Code Management")
  * [Issue Management](https://maven.apache.org/jxr/issue-management.html "Issue Management")
  * [Mailing Lists](https://maven.apache.org/jxr/mailing-lists.html "Mailing Lists")
  * [Dependency Management](https://maven.apache.org/jxr/dependency-management.html "Dependency Management")
  * [Dependency Convergence](https://maven.apache.org/jxr/dependency-convergence.html "Dependency Convergence")
  * [CI Management](https://maven.apache.org/jxr/ci-management.html "CI Management")
  * [Plugin Management](https://maven.apache.org/jxr/plugin-management.html "Plugin Management")
  * [Plugins](https://maven.apache.org/jxr/plugins.html "Plugins")
  * [Distribution Management](https://maven.apache.org/jxr/distribution-management.html "Distribution Management")

* [Project Reports](https://maven.apache.org/jxr/project-reports.html "Project Reports")
* Maven Projects
* [Maven](https://maven.apache.org/ref/current "Maven")
* [Archetypes](https://maven.apache.org/archetypes/index.html "Archetypes")
* [Extensions](https://maven.apache.org/extensions/index.html "Extensions")
* [Parent POMs](https://maven.apache.org/pom/index.html "Parent POMs")
* [Plugins](https://maven.apache.org/plugins/index.html "Plugins")
* [Skins](https://maven.apache.org/skins/index.html "Skins")
* [Components](https://maven.apache.org/jxr/index.html "Components")
  * [Archetype](https://maven.apache.org/archetype/index.html "Archetype")
  * [Artifact Resolver](https://maven.apache.org/resolver/index.html "Artifact Resolver")
  * [Doxia](https://maven.apache.org/doxia/index.html "Doxia")
  * [Indexer](https://maven.apache.org/maven-indexer/index.html "Indexer")
  * [JXR](https://maven.apache.org/jxr/index.html)
  * [Plugin Testing](https://maven.apache.org/plugin-testing/index.html "Plugin Testing")
  * [Plugin Tools](https://maven.apache.org/plugin-tools/index.html "Plugin Tools")
  * [Resource Bundles](https://maven.apache.org/apache-resource-bundles/index.html "Resource Bundles")
  * [SCM](https://maven.apache.org/scm/index.html "SCM")
  * [Shared Components](https://maven.apache.org/shared/index.html "Shared Components")
  * [Surefire](https://maven.apache.org/surefire/index.html "Surefire")
  * [Wagon](https://maven.apache.org/wagon/index.html "Wagon")

* ASF
* [How Apache Works](https://www.apache.org/foundation/how-it-works.html "How Apache Works")
* [Foundation](https://www.apache.org/foundation/ "Foundation")
* [Data Privacy](https://privacy.apache.org/policies/privacy-policy-public.html "Data Privacy")
* [Sponsoring Apache](https://www.apache.org/foundation/sponsorship.html "Sponsoring Apache")
* [Thanks](https://www.apache.org/foundation/thanks.html "Thanks")

[![Image 4: Built by Maven](https://maven.apache.org/jxr/images/logos/maven-feather.png)](http://maven.apache.org/ "Built by Maven")

[](https://maven.apache.org/jxr/index.html)Maven JXR[](https://maven.apache.org/jxr/index.html#maven-jxr)
---------------------------------------------------------------------------------------------------------

Maven JXR project (formally Java Cross Reference) is a library to analyze a set of Java source files and produces documentation in HTML format _à la Javadoc_.

Take a look at this [JXR report](https://maven.apache.org/jxr/xref/index.html) to see an example.

### [](https://maven.apache.org/jxr/index.html)Main Features[](https://maven.apache.org/jxr/index.html#main-features)

* Supports JDK 1.4+
* Complementary tool for Javadoc
* Easy configuration for color, style or template
* Fully integrated with [Maven](https://maven.apache.org/jxr/maven-jxr-plugin/)

### [](https://maven.apache.org/jxr/index.html)Brief History[](https://maven.apache.org/jxr/index.html#brief-history)

The original JXR code was merged in 2004 with the Javasrc project from the defunct [Jakarta Alexandria](http://jakarta.apache.org/alexandria) project. The code was first maintained within the Maven 1 JXR plugin. In September 2005, it was voted to fork the base and create a separate library.

### [](https://maven.apache.org/jxr/index.html)Examples[](https://maven.apache.org/jxr/index.html#examples)

The following example shows how to use Maven JXR in more advanced use cases:

* [Using Maven JXR in Java](https://maven.apache.org/jxr/examples/java.html)

* * *

© 2002–2024 [The Apache Software Foundation](https://www.apache.org/)
