# Source: https://maven.apache.org/wagon/index.html

Title: Apache Maven Wagon – Introduction

URL Source: https://maven.apache.org/wagon/index.html

Markdown Content:
Apache Maven Wagon – Introduction
===============

[![Image 2: Apache Maven Wagon](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)

[![Image 3](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)

* * *

* [Apache](https://www.apache.org/ "Apache")/
* [Maven](https://maven.apache.org/index.html "Maven")/
* [Apache Maven Wagon](https://maven.apache.org/wagon/index.html "Apache Maven Wagon")/
* Introduction [![Image 4: Edit](https://maven.apache.org/wagon/images/accessories-text-editor.png)](https://github.com/apache/maven-wagon/tree/wagon-3.5.3/src/site/xdoc/index.xml)
* | Last Published: 2022-12-18
* Version: 3.5.3

* Overview
* [Introduction](https://maven.apache.org/wagon/index.html#)
* [JavaDocs](https://maven.apache.org/wagon/apidocs/index.html "JavaDocs")
* [License](http://www.apache.org/licenses/ "License")
* [Download](https://maven.apache.org/wagon/download.html "Download")
* Modules
* [Apache Maven Wagon :: API](https://maven.apache.org/wagon/wagon-provider-api/index.html "Apache Maven Wagon :: API")
* [Apache Maven Wagon :: Providers](https://maven.apache.org/wagon/wagon-providers/index.html "Apache Maven Wagon :: Providers")
* [Apache Maven Wagon :: Provider Test](https://maven.apache.org/wagon/wagon-provider-test/index.html "Apache Maven Wagon :: Provider Test")
* [Apache Maven Wagon :: Test Compatibility Kits](https://maven.apache.org/wagon/wagon-tcks/index.html "Apache Maven Wagon :: Test Compatibility Kits")
* Project Documentation
* [Project Information](https://maven.apache.org/wagon/project-info.html "Project Information")
  * [About](https://maven.apache.org/wagon/index.html#)
  * [Summary](https://maven.apache.org/wagon/summary.html "Summary")
  * [Dependency Information](https://maven.apache.org/wagon/dependency-info.html "Dependency Information")
  * [Project Modules](https://maven.apache.org/wagon/modules.html "Project Modules")
  * [Team](https://maven.apache.org/wagon/team.html "Team")
  * [Source Code Management](https://maven.apache.org/wagon/scm.html "Source Code Management")
  * [Issue Management](https://maven.apache.org/wagon/issue-management.html "Issue Management")
  * [Mailing Lists](https://maven.apache.org/wagon/mailing-lists.html "Mailing Lists")
  * [Dependency Management](https://maven.apache.org/wagon/dependency-management.html "Dependency Management")
  * [Dependency Convergence](https://maven.apache.org/wagon/dependency-convergence.html "Dependency Convergence")
  * [CI Management](https://maven.apache.org/wagon/ci-management.html "CI Management")
  * [Plugin Management](https://maven.apache.org/wagon/plugin-management.html "Plugin Management")
  * [Plugins](https://maven.apache.org/wagon/plugins.html "Plugins")
  * [Distribution Management](https://maven.apache.org/wagon/distribution-management.html "Distribution Management")

* [Project Reports](https://maven.apache.org/wagon/project-reports.html "Project Reports")
* Maven Projects
* [Archetype](https://maven.apache.org/archetype/index.html "Archetype")
* [Artifact Resolver](https://maven.apache.org/resolver/index.html "Artifact Resolver")
* [Doxia](https://maven.apache.org/doxia/index.html "Doxia")
* [JXR](https://maven.apache.org/jxr/index.html "JXR")
* [Maven](https://maven.apache.org/ref/current "Maven")
* [Parent POMs](https://maven.apache.org/pom/index.html "Parent POMs")
* [Plugins](https://maven.apache.org/plugins/index.html "Plugins")
* [Plugin Testing](https://maven.apache.org/plugin-testing/index.html "Plugin Testing")
* [Plugin Tools](https://maven.apache.org/plugin-tools/index.html "Plugin Tools")
* [Resource Bundles](https://maven.apache.org/apache-resource-bundles/index.html "Resource Bundles")
* [SCM](https://maven.apache.org/scm/index.html "SCM")
* [Shared Components](https://maven.apache.org/shared/index.html "Shared Components")
* [Skins](https://maven.apache.org/skins/index.html "Skins")
* [Surefire](https://maven.apache.org/surefire/index.html "Surefire")
* [Wagon](https://maven.apache.org/wagon/index.html#)
* ASF
* [How Apache Works](https://www.apache.org/foundation/how-it-works.html "How Apache Works")
* [Foundation](https://www.apache.org/foundation/ "Foundation")
* [Sponsoring Apache](https://www.apache.org/foundation/sponsorship.html "Sponsoring Apache")
* [Thanks](https://www.apache.org/foundation/thanks.html "Thanks")

* * *

[Follow ASFMavenProject](https://twitter.com/ASFMavenProject)

[![Image 5: Built by Maven](https://maven.apache.org/wagon/images/logos/maven-feather.png)](http://maven.apache.org/ "Built by Maven")

[](https://maven.apache.org/wagon/index.html)Maven Wagon
--------------------------------------------------------

Maven Wagon is a transport abstraction that is used in Maven's artifact and repository handling code.

Wagon defines a [unified API](https://maven.apache.org/wagon/wagon-provider-api/), and it currently has the following providers:

* [File](https://maven.apache.org/wagon/wagon-providers/wagon-file/)
* [HTTP](https://maven.apache.org/wagon/wagon-providers/wagon-http/)
* [HTTP lightweight](https://maven.apache.org/wagon/wagon-providers/wagon-http-lightweight/)
* [FTP](https://maven.apache.org/wagon/wagon-providers/wagon-ftp/)
* [SSH/SCP](https://maven.apache.org/wagon/wagon-providers/wagon-ssh/)
* [WebDAV](https://maven.apache.org/wagon/wagon-providers/wagon-webdav-jackrabbit/)
* [SCM](https://maven.apache.org/wagon/wagon-providers/wagon-scm/) (in progress)

![Image 6: Wagon Dependencies](https://maven.apache.org/wagon/images/wagon-deps.png)

[](https://maven.apache.org/wagon/index.html)Deprecation Notice
---------------------------------------------------------------

The following Wagon providers are deprecated and will be removed in version 4.0.0:

* [HTTP lightweight](https://maven.apache.org/wagon/wagon-providers/wagon-http-lightweight/)
* [FTP](https://maven.apache.org/wagon/wagon-providers/wagon-ftp/)
* [SSH/SCP](https://maven.apache.org/wagon/wagon-providers/wagon-ssh/)
* [WebDAV](https://maven.apache.org/wagon/wagon-providers/wagon-webdav-jackrabbit/)

* * *

Copyright ©2003–2022 [The Apache Software Foundation](https://www.apache.org/). All rights reserved.
