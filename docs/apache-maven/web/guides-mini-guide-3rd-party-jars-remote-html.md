# Source: https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html

Title: Guide to deploying 3rd party JARs to remote repository – Maven

URL Source: https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
Guide to deploying 3rd party JARs to remote repository – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Guide to deploying 3rd party JARs to remote repository [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-3rd-party-jars-remote.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
        *   [Plugins Validation](https://maven.apache.org/guides/plugins/validation/index.html)
        *   [Creating a site](https://maven.apache.org/guides/mini/guide-site.html)
        *   [Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html)
        *   [Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)
            *   [Install to Local](https://maven.apache.org/guides/mini/guide-3rd-party-jars-local.html)
            *   [Deploy to Remote](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
            *   [Repository Management](https://maven.apache.org/repository-management.html)
            *   [Using Multiple Repositories](https://maven.apache.org/guides/mini/guide-multiple-repositories.html)
            *   [Large Scale Centralized Deployments](https://maven.apache.org/guides/mini/guide-large-scale-centralized-deployments.html)
            *   [Mirror Settings](https://maven.apache.org/guides/mini/guide-mirror-settings.html)
            *   [Deployment and Security Settings](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
            *   [Encrypting Passwords (Maven 3)](https://maven.apache.org/guides/mini/guide-encryption.html)
            *   [Encrypting Passwords (Maven 4)](https://maven.apache.org/guides/mini/guide-encryption-4.html)
            *   [Using Proxies](https://maven.apache.org/guides/mini/guide-proxies.html)
            *   [Authenticated HTTPS](https://maven.apache.org/guides/mini/guide-repository-ssl.html)
            *   [Resolver Transport](https://maven.apache.org/guides/mini/guide-resolver-transport.html)
            *   [Advanced Wagon HTTP Configuration](https://maven.apache.org/guides/mini/guide-http-settings.html)
            *   [Alternative Wagon Providers](https://maven.apache.org/guides/mini/guide-wagon-providers.html)
            *   [Relocation](https://maven.apache.org/guides/mini/guide-relocation.html)

        *   [Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
        *   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
        *   [Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html)

    *   [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html)
    *   [Maven 4](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
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
*   [Components](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
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

[](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
Guide to deploying 3rd party JARs to remote repository
======================================================

Same concept of the [install:install-file](https://maven.apache.org/guides/mini/guide-3rd-party-jars-local.html) goal of the maven-install-plugin where the 3rd party JAR is installed in the local repository. But this time the JAR will be installed both in the local and remote repository.

To deploy a 3rd party JAR, use the deploy:deploy-file goal under maven-deploy-plugin.

First, the wagon-provider(wagon-ftp, wagon-file, etc..) must be placed to your `${maven.home}/lib`.

Then execute the command:

```
mvn deploy:deploy-file -DgroupId=<group-id> \
  -DartifactId=<artifact-id> \
  -Dversion=<version> \
  -Dpackaging=<type-of-packaging> \
  -Dfile=<path-to-file> \
  -DrepositoryId=<id-to-map-on-server-section-of-settings.xml> \
  -Durl=<url-of-the-repository-to-deploy>
```
[](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
Deploying a 3rd party JAR with a generic POM
--------------------------------------------

By default, deploy:deploy-file generates a generic POM(.pom) to be deployed together with the 3rd party JAR. To disable this feature we should set the `generatePOM` argument to false.

```
-DgeneratePom=false
```
[](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
Deploying a 3rd party JAR with a customized POM
-----------------------------------------------

If a POM already exists for the third party JAR and you want to deploy it together with the JAR, you should use the `pomFile` argument of the deploy-file goal. See sample below.

```
mvn deploy:deploy-file -DpomFile=<path-to-pom> \
  -Dfile=<path-to-file> \
  -DrepositoryId=<id-to-map-on-server-section-of-settings.xml> \
  -Durl=<url-of-the-repository-to-deploy>
```

Note that `groupId`, `artifactId`, `version` and `packaging` arguments are not included here because deploy-file goal will get these information from the given POM.

[](https://maven.apache.org/guides/mini/guide-3rd-party-jars-remote.html)
Deploying Source Jars
---------------------

To deploy a 3rd party source jar, packaging should be set to `java-source`, and generatePom should be set to `false`.

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
