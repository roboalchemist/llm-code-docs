# Source: https://maven.apache.org/guides/mini/guide-configuring-maven.html

Title: Configuring Maven – Maven

URL Source: https://maven.apache.org/guides/mini/guide-configuring-maven.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Maven configuration occurs at 3 levels:

*   _Project_ - most static configuration occurs in `pom.xml`
*   _Installation_ - this is configuration added once for a Maven installation
*   _User_ - this is configuration specific to a particular user

The separation is quite clear - the project defines information that applies to the project, no matter who is building it, while the others both define settings for the current environment.

**Note:** the installation and user configuration cannot be used to add shared project information - for example, setting `<organization>` or `<distributionManagement>` company-wide.

For this, you should have your projects inherit from a company-wide parent `pom.xml`.

You can specify your user configuration in `${user.home}/.m2/settings.xml`. A [full reference](https://maven.apache.org/maven-settings/settings.html) to the configuration file is available. This section will show how to make some common configurations. Note that the file is not required - defaults will be used if it is not found.

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Configuring your Local Repository[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#configuring-your-local-repository)
----------------------------------------------------------------------------------------------------------------------------------------

The location of your local repository can be changed in your user configuration. The default value is `${user.home}/.m2/repository/`.

1.   `<settings>`
2.   `...`
3.   `<localRepository>/path/to/local/repo/</localRepository>`
4.   `...`
5.   `</settings>`

**Note:** The local repository must be an absolute path.

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Configuring a Proxy[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#configuring-a-proxy)
------------------------------------------------------------------------------------------------------------

Proxy configuration can also be specified in the settings file.

For more information, see the [Guide to using a Proxy](https://maven.apache.org/guides/mini/guide-proxies.html).

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Configuring Parallel Artifact Resolution[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#configuring-parallel-artifact-resolution)
------------------------------------------------------------------------------------------------------------------------------------------------------

By default, Maven will download up to five artifacts (from different groups) at once. To change the size of the thread pool, start Maven using `-Dmaven.artifact.threads`. For example, to only download one artifact at a time:

```
mvn -Dmaven.artifact.threads=1 verify
```

You may wish to set this option permanently, in which case you can use the `MAVEN_OPTS` environment variable. For example:

```
export MAVEN_OPTS=-Dmaven.artifact.threads=3
```
[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Security and Deployment Settings[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#security-and-deployment-settings)
--------------------------------------------------------------------------------------------------------------------------------------

Repositories to deploy to are defined in a project in the `<distributionManagement>` section. However, you cannot put your username, password, or other security settings in that project. For that reason, you should add a server definition to your own settings with an `id` that matches that of the deployment repository in the project.

In addition, some repositories may require authorization to download from, so the corresponding settings can be specified in a `server` element in the same way.

Which settings are required will depend on the type of repository you are deploying to. As of the first release, only SCP deployments and file deployments are supported by default, so only the following SCP configuration is needed:

1.   `<settings>`
2.   `...`
3.   `<servers>`
4.   `<server>`
5.   `<id>repo1</id>`
6.   `<username>repouser</username>`
7.   `<!-- other optional elements:`
8.   `<password>my_login_password</password>`
9.   `<privateKey>/path/to/identity</privateKey> (default is ~/.ssh/id_dsa)`
10.   `<passphrase>my_key_passphrase</passphrase>`
11.   `-->`
12.   `</server>`
13.   `...`
14.   `</servers>`
15.   `...`
16.   `</settings>`

To encrypt passwords in these sections, refer to [Encryption Settings](https://maven.apache.org/guides/mini/guide-encryption.html).

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Using Mirrors for Repositories[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#using-mirrors-for-repositories)
----------------------------------------------------------------------------------------------------------------------------------

Repositories can be declared inside a project, which means that if you have your own custom repositories, those sharing your project easily get the right settings out of the box. However, you may want to use an alternative mirror for a particular repository without changing the project files. Refer to [Guide to Mirror Settings](https://maven.apache.org/guides/mini/guide-mirror-settings.html) for more details.

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Profiles[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#profiles)
--------------------------------------------------------------------------------------

Repository configuration can also be put into a profile. You can have multiple profiles, with one set to active so that you can easily switch environments. Read more about profiles in [Introduction to Build Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html).

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
Optional configuration[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#optional-configuration)
------------------------------------------------------------------------------------------------------------------

Maven will work for most tasks with the above configuration, however if you have any environmental specific configuration outside of individual projects then you will need to configure settings. The following sections refer to what is available.

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
### Settings[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#settings)

Maven has a settings file located in the Maven installation and/or user home directory that configure environmental specifics such as:

*   HTTP proxy server
*   repository manager location
*   server authentication and passwords
*   other configuration properties

For information on this file, see the [Settings reference](https://maven.apache.org/settings.html)

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
### Security[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#security)

You can encrypt passwords in your settings file. However, you must first configure a master password. For more information on both server passwords and the master password, see the [Guide to Password Encryption](https://maven.apache.org/guides/mini/guide-encryption.html).

[](https://maven.apache.org/guides/mini/guide-configuring-maven.html)
### Toolchains[](https://maven.apache.org/guides/mini/guide-configuring-maven.html#toolchains)

You can build a project using a specific version of JDK independent from the one Maven is running with. For more information, see the [Guide to Using Toolchains](https://maven.apache.org/guides/mini/guide-using-toolchains.html).
