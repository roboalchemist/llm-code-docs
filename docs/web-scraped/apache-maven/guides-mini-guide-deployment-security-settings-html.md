# Source: https://maven.apache.org/guides/mini/guide-deployment-security-settings.html

Title: Security and Deployment Settings – Maven

URL Source: https://maven.apache.org/guides/mini/guide-deployment-security-settings.html

Markdown Content:
Security and Deployment Settings – Maven
===============

[![Image 1](https://maven.apache.org/images/apache-maven-project.png)](https://www.apache.org/)
===============================================================================================

[![Image 2](https://maven.apache.org/images/maven-logo-black-on-white.png)](https://maven.apache.org/)
======================================================================================================

* * *

*   [Apache](https://www.apache.org/)/
*   [Maven](https://maven.apache.org/index.html)/
*   Security and Deployment Settings [![Image 3: Edit](https://maven.apache.org/images/accessories-text-editor.png)](https://github.com/apache/maven-site/tree/master/content/markdown/guides/mini/guide-deployment-security-settings.md)
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
    *   [Maven Build Fundamentals](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
        *   [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
        *   [Getting Help](https://maven.apache.org/users/getting-help.html)
        *   [Running Maven](https://maven.apache.org/run-maven/index.html)

    *   [Maven Build Config Fundamentals](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
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
    *   [Maven 4](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
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
*   [Components](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
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

[](https://maven.apache.org/guides/mini/guide-deployment-security-settings.html)
Security and Deployment Settings
================================

Repositories to deploy to are defined in a project in the `distributionManagement` section. However, you cannot put your username, password, or other security settings in that project. For that reason, you should add a server definition to your own settings with an id that matches that of the deployment repository in the project.

In addition, some repositories may require authorisation to download from, so the corresponding settings can be specified in a server element in the same way.

Which settings are required will depend on the type of repository you are deploying to. As of the first release, only SCP deployments and file deployments are supported by default, so only the following SCP configuration is needed:

1.   ```xml
<settings>
```
2.   ```xml
.
```
3.   ```xml
.
```
4.   ```xml
<servers>
```
5.   ```xml
<server>
```
6.   ```xml
<id>repo1</id>
```
7.   ```xml
<username>repouser</username>
```
8.   ```xml
<!-- other optional elements:
```
9.   ```xml
<password>my_login_password</password>
```
10.   ```xml
<privateKey>/path/to/identity</privateKey> (default is ~/.ssh/id_dsa)
```
11.   ```xml
<passphrase>my_key_passphrase</passphrase>
```
12.   ```xml
-->
```
13.   ```xml
</server>
```
14.   ```xml
</servers>
```
15.   ```xml
.
```
16.   ```xml
.
```
17.   ```xml
</settings>
```

To encrypt passwords in these sections, refer to [Encryption Settings](https://maven.apache.org/guides/mini/guide-encryption.html).

**Note**: The settings descriptor documentation can be found on the [Maven Local Settings Model Website](https://maven.apache.org/maven-settings/settings.html).

* * *

© 2002–2026 [The Apache Software Foundation](https://www.apache.org/)
