# Source: https://maven.apache.org/guides/mini/guide-releasing.html

Title: Releasing – Maven

URL Source: https://maven.apache.org/guides/mini/guide-releasing.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-releasing.html)[](https://maven.apache.org/guides/mini/guide-releasing.html)
Introduction[](https://maven.apache.org/guides/mini/guide-releasing.html#introduction)
--------------------------------------------------------------------------------------

The main aim of the maven-release plugin is to provide a standard mechanism to release project artifacts outside the immediate development team. The plugin provides basic functionality to create a release and to update the project's SCM accordingly.

To create a release the maven-release plugin is executed through maven in 2 stages:

1.   Preparing the release.
2.   Performing the release.

[](https://maven.apache.org/guides/mini/guide-releasing.html)
Preparing the release[](https://maven.apache.org/guides/mini/guide-releasing.html#preparing-the-release)
--------------------------------------------------------------------------------------------------------

The plugin will record release information into a new revision of the project's _pom.xml_ file as well as applying SCM versioning to the project's resources.

The `release:prepare` goal will:

1.   Verify that there are no uncommitted changes in the workspace.
2.   Prompt the user for the desired tag, release and development version names.
3.   Modify and commit release information into the _pom.xml_ file.
4.   Tag the entire project source tree with the new tag name.

The following example shows how to run the `release:prepare` goal with a Subversion SCM. The commandline example directs the plugin to locate a Subversion SCM on a local file system.

```
mvn release:prepare \
        -Dproject.scm.developerConnection=scm:svn:file:///D:/subversion_data/repos/my_repo/my-app-example/trunk \
        -DtagBase=file:///D:/subversion_data/repos/my_repo/my-app-example/tags
```

When using the `release:prepare` goal, the user must supply maven with information regarding the current location of the project's SCM. In the previous example maven was supplied with the current location of the development trunk and the new location to record tagged instances of the project.

*   **project.scm.developerConnection**

The current location of the development trunk. A valid SCM URL format appropriate to the SCM provider. The “SCM:Provider:” prefix is used to determine the provider being used.

*   **tagbase**

The new location to record a tagged release. A valid SCM URL format appropriate to the SCM provider without the “SCM:Provider:” prefix.

The previous goal parameters can be supplied while executing maven on the commandline, (as shown in the previous example) or they can be defined and maintained within the project's _pom.xml_ file. The location of the current development trunk is defined within the _pom.xml_ file in the following form:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<modelVersion>4.0.0</modelVersion>`
3.   `<groupId>com.mycompany.app</groupId>`
4.   `<artifactId>app</artifactId>`
5.   `<packaging>jar</packaging>`
6.   `<version>1.0-SNAPSHOT</version>`
7.   `<name>Application</name>`
8.   `<url>http://app.mycompany.com</url>`
9.   `...`
10.   `<scm>`
11.   `<developerConnection>scm:svn:file:///D:/subversion_data/repos/my_repo/my-app-example/trunk</developerConnection>`
12.   `</scm>`
13.   `...`
14.   `<build>`
15.   `<plugins>`
16.   `...`
17.   `<plugin>`
18.   `<artifactId>maven-release-plugin</artifactId>`
19.   `<version>2.5.2</version>`
20.   `<configuration>`
21.   `...`
22.   `<tagBase>`
23.   `file:///D:/subversion_data/repos/my_repo/my-app-example/tags`
24.   `</tagBase>`
25.   `...`
26.   `</configuration>`
27.   `</plugin>`
28.   `...`
29.   `</plugins>`
30.   `</build>`
31.   `...`
32.   `</project>`

To define the tagBase parameter within the _pom.xml_ file a tagBase element must be defined within a _plugins/plugin/configuration_ element. The following example shows how this would look within the _pom.xml_ file.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<modelVersion>4.0.0</modelVersion>`
3.   `<groupId>com.mycompany.app</groupId>`
4.   `<artifactId>app</artifactId>`
5.   `<packaging>jar</packaging>`
6.   `<version>1.0-SNAPSHOT</version>`
7.   `<name>Application</name>`
8.   `<url>http://app.mycompany.com</url>`
9.   `...`
10.   `<scm>`
11.   `<developerConnection>scm:svn:file:///D:/subversion_data/repos/my_repo/my-app-example/trunk</developerConnection>`
12.   `</scm>`
13.   `...`
14.   `<build>`
15.   `<plugins>`
16.   `...`
17.   `<plugin>`
18.   `<artifactId>maven-release-plugin</artifactId>`
19.   `<version>2.5.2</version>`
20.   `<configuration>`
21.   `...`
22.   `<tagBase>`
23.   `file:///D:/subversion_data/repos/my_repo/my-app-example/tags`
24.   `</tagBase>`
25.   `...`
26.   `</configuration>`
27.   `</plugin>`
28.   `...`
29.   `</plugins>`
30.   `</build>`
31.   `...`
32.   `</project>`

During the execution of the `release:prepare` goal maven will interact with the user to gather information about the current release. Maven will prompt the user for the following information:

*   **A Desired SCM provider tag name**.

This is a SCM provider specific value, in the case of the Subversion SCM provider this value is equal to the directory name that will appear under the URL provided by the the tagBase parameter.

*   **A Desired project release version**.

This value is placed in the _pom.xml_ that will define the current release. If a development _pom.xml_ holds a version value of 1.0-SNAPSHOT then the release version would be 1.0. This is not enforced and can be a value appropriate to yourself or a company environment.

*   **A New development version**.

This value is the placed in the next revision of the _pom.xml_ file used for continuing development. If the current release represented version 1.0 then an appropriate value could be 2.0-SNAPSHOT. The SNAPSHOT designator is required to prepare and perform future releases. This value is then committed in the next development revision of the _pom.xml_ file.

After maven has been supplied with the required information the maven-release plugin will interact with the project's SCM and define a relese to be extracted and deployed. At the same time the project's development trunk is updated allowing developers to continue with further modifications that will be included within future releases.

[](https://maven.apache.org/guides/mini/guide-releasing.html)
Performing the release[](https://maven.apache.org/guides/mini/guide-releasing.html#performing-the-release)
----------------------------------------------------------------------------------------------------------

The plugin will extract file revisions associated with the current release. Maven will compile, test and package the versioned project source code into an artifact. The final deliverable will then be released into an appropriate maven repository.

The `release:perform` goal will:

1.   Extract file revisions versioned under the new tag name.
2.   Execute the maven build lifecycle on the extracted instance of the project.
3.   Deploy the versioned artifacts to appropriate local and remote repositories.

The following example shows how to run the `release:perform` goal from the commandline.

```
mvn release:perform
```

The `release:perform` goal requires a file called _release.properties_ to be present within the project root directory. The _release.properties_ file is constructed during the execution of the `release:prepare` goal and contains all the information needed to locate and extract the correctly tagged version of the project. Shown below is an example of the contents that can appear within an instance of the _release.properties_ file.

**Note:** The location of the _release.properties_ file is under review and could be moved to the target directory.

```
#Generated by Release Plugin on: Sat Nov 12 11:22:33 GMT 2005
#Sat Nov 12 11:22:33 GMT 2005
maven.username=myusername
checkpoint.transformed-pom-for-release=OK
scm.tag=1.0
scm.url=scm\:svn\:file\:///D\:/subversion_data/repos/my_repo/my-app-example/trunk
scm.tag-base=file\:///D\:/subversion_data/repos/my_repo/my-app-example/tags
checkpoint.transform-pom-for-development=OK
checkpoint.local-modifications-checked=OK
checkpoint.initialized=OK
checkpoint.checked-in-release-version=OK
checkpoint.tagged-release=OK
checkpoint.prepared-release=OK
checkpoint.check-in-development-version=OK
```

The _release.properties_ file is created while preparing the release. By default the file gets deleted after a successful release.

During the execution of the `release:perform` goal, Maven executes the project's entire build lifecycle. The tagged project source code is extracted, compiled, tested, documented, and deployed. An instance of the release artifact is deployed to the machine's local repository. An another instance of the release can be deployed to a remote repository by configuring the _distributionManagement_ element within the _pom.xml_ file.

The following is an example of how a distributionManagement element can be configured within a project _pom.xml_ file.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<modelVersion>4.0.0</modelVersion>`
3.   `<groupId>com.mycompany.app</groupId>`
4.   `<artifactId>app</artifactId>`
5.   `<packaging>jar</packaging>`
6.   `<version>1.0-SNAPSHOT</version>`
7.   `<name>Application</name>`
8.   `<url>http://app.mycompany.com</url>`
9.   `...`
10.   `<distributionManagement>`
11.   `<repository>`
12.   `<id>myRepoId</id>`
13.   `<name>myCompanyReporsitory</name>`
14.   `<url>ftp://repository.mycompany.com/repository</url>`
15.   `</repository>`
16.   `</distributionManagement>`
17.   `...`
18.   `</project>`

If the distributionManagement element is not configured within the _pom.xml_ file then the deployment of the artifact will fail. Maven will report a failure back to the user for the execution of the maven-deploy plugin. Please refer maven documentationa and additional mini guides for the use of the maven-deploy plugin.

The following delvierables are created and deployed to local and remoted repositories after the execution of the `release:perform` goal has finished.

*   _artifact id_-_version_.jar

The binaries for the current release of the project.

*   _artifact id_-_version_-javadoc.jar

The javadoc explaining the current functionality of the classes within the current release.

*   _artifact id_-_version_-source.jar

The source code revisions used to build the current release of the project.

*   _artifact id_-_version_.pom

The contents of the _pom.xml_ file used to create the current release of the project.

[](https://maven.apache.org/guides/mini/guide-releasing.html)
Troubleshooting[](https://maven.apache.org/guides/mini/guide-releasing.html#troubleshooting)
--------------------------------------------------------------------------------------------

[](https://maven.apache.org/guides/mini/guide-releasing.html)
### I get a “The authenticity of host ‘_host_’ can't be established.” error and the build hangs[](https://maven.apache.org/guides/mini/guide-releasing.html#i-get-a-%E2%80%9Cthe-authenticity-of-host-%E2%80%98host%E2%80%99-cant-be-established-%E2%80%9D-e)

This is because your `~user/.ssh/known_hosts` file doesn't have the host listed. You'd normally get a prompt to add the host to the known host list but Maven doesn't propagate that prompt. The solution is to add the host the `known_hosts` file before executing Maven. On Windows, this can be done by installing an OpenSSH client (for example [SSHWindows](http://sshwindows.sourceforge.net/download/)), running `ssh <host`> and accepting to add the host.

[](https://maven.apache.org/guides/mini/guide-releasing.html)
### The site deploy goal hangs[](https://maven.apache.org/guides/mini/guide-releasing.html#the-site-deploy-goal-hangs)

First, this means that you have successfully deployed the artifacts to the remote repo and that it's only the site deployment that is now an issue. Stop your build, cd to **target/checkout**> and run the build again by executing `mvn site:deploy`. You should see a prompt asking you to enter a password. This happens if your key is not in the authorized keys on the server.
