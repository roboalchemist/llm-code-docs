# Source: https://help.cloudsmith.io/docs/maven-repository.md

# Maven Repository

Cloudsmith provides public & private repositories for Maven

<Image align="center" width="100%" src="https://files.readme.io/ac58b4a-cloudsmith-maven-banner-hd.jpg" />

Maven is a build automation tool primarily associated with the Java programming language. Developed by the Apache Software Foundation and released in 2004 it provides a standardized way to describe how a software project is built.

A Maven Repository or Maven Repo is a registry of packaged files, stored, indexed, and made accessible to projects that depend on them. Each package has a unique name and version allowing for repeatable continuous integration and continuous delivery (or continuous deployment) tasks.

The Maven repository index stores metadata about each package that the Maven tooling looks up at build time, enabling pulling in of dependency projects and extensions.

For more information on Maven, please see:

* [Maven](https://maven.apache.org/): The official website for Apache Maven
* [Maven Central](https://maven.org/): Popular public repository for Maven artifacts

If using Gradle - please see our [Gradle documentation](https://help.cloudsmith.io/docs/gradle-repository)
If using sbt - please see our [sbt documentation](https://help.cloudsmith.io/docs/sbt-repository)

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo/rsa-key pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
      <a target="_blank" href="https://www.youtube.com/watch?v=xT_oXM9g8wE"><img src="https://files.readme.io/3b5b8e1-cloudsmith-youtube-play-maven-small.png"/></a>
    </div>
  </div>
  `}
</HTMLBlock>

In the following examples:

| Identifier       | Description                                                                                                                         |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| OWNER            | Your Cloudsmith account name or organization name (namespace)                                                                       |
| REPOSITORY       | Your Cloudsmith Repository name (also called "slug")                                                                                |
| TOKEN            | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details)                                           |
| USERNAME         | Your Cloudsmith username                                                                                                            |
| PASSWORD         | Your Cloudsmith password                                                                                                            |
| API-KEY          | Your Cloudsmith API Key                                                                                                             |
| PACKAGE\_VERSION | The semantic version number of your package                                                                                         |
| GROUP\_ID        | A unique Maven identifier for your project across all projects and usually takes the form of a reverse domain i.e "com.companyname" |
| ARTIFACT\_ID     | The name of the jar without version i.e "project"                                                                                   |

## Upload a Package

To upload, you need to generate your package first. You can do this with:

```shell
mvn package
```

This generates a Maven package file (`.jar` or similar) like `your-package-1.2.3.jar` that you can upload.

<Callout icon="📘" theme="info">
  You will always need at least the package file and the POM file for uploading.
</Callout>

#### What is a POM?

A POM, the Project Object Model, is the XML file that describes all the aspects of your project that relate to building and packaging the source code into a package file. Typically a jar (java archive). The metadata held within the pom.xml that is typically stored within the jar itself allows Maven to index the package into a Maven Repository for easy distribution.

#### What is a Fat Jar?

A Fat Jar, is also referred to as an Uber Jar, is a Java Archive library that contains all classes, including all the classes of its dependencies. This allows the Jar to be run standalone without requiring any further code available on the Class Path.

The disadvantage of creating an all-in-one jar mean that you have to deploy everything (a potentially large file) each time. If you split the Fat Jar into components you can separately test, version and release code enabling faster deployments and your developers to cherry-pick components for inclusion in other projects.

### Upload via Maven

The endpoint for the native Maven API is:

```
https://maven.cloudsmith.io/OWNER/REPOSITORY/
```

The distribution repositories define where to push your artifacts. In this case it will be a single repository, but you can configure alternatives. Add the following to your project `pom.xml` file:

```xml
<distributionManagement>
  <snapshotRepository>
    <id>NAME</id>
    <url>https://maven.cloudsmith.io/OWNER/REPOSITORY/</url>
  </snapshotRepository>
  <repository>
    <id>NAME</id>
    <url>https://maven.cloudsmith.io/OWNER/REPOSITORY/</url>
  </repository>
</distributionManagement>
```

<Callout icon="📘" theme="info">
  You can configure different repositories for snapshots and releases, and you can replace **NAME** with your own identifier(s) (but make sure they match settings elsewhere).
</Callout>

You then can configure your `~/.m2/settings.xml` file with the API key of the uploading user:

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                      https://maven.apache.org/xsd/settings-1.0.0.xsd">
  <servers>
    <server>
      <id>NAME</id>
      <username>USERNAME</username>
      <password>API-KEY</password>
    </server>
  </servers>
</settings>
```

You can now publish to the native API with:

```
mvn deploy
```

<Callout icon="📘" theme="info">
  You can find out more about Maven publishing in the official [Maven documentation](https://maven.apache.org/plugins/maven-deploy-plugin/usage.html).
</Callout>

### Upload via the Cloudsmith CLI

The command to upload a Maven package via the Cloudsmith CLI is:

```shell
cloudsmith push maven OWNER/REPOSITORY ARTIFACT_ID-PACKAGE_VERSION.jar --pom-file=ARTIFACT_ID-PACKAGE_VERSION.pom
```

Example:

```shell
cloudsmith push maven org/repo validation-api-1.0.0.GA.jar --pom-file=validation-api-1.0.0.GA.pom
```

### Uploading of extra files via the Cloudsmith CLI

Customers can take advantage of the new extra-files option available for the Maven push command in cloudsmith-cli as of version 1.7.0.

Here’s an example of how to use the command. You can either provide a comma-separated list or pass multiple --extra-files parameters.

Using extra-files as a comma-separated list:

```
cloudsmith push maven cloudsmith-test/cli-upload example-maven-project-1.0.0.jar \
  --javadoc-file example-maven-project-1.0.0-javadoc.jar \
  --sources-file example-maven-project-1.0.0-sources.jar \
  --pom-file example-maven-project-1.0.0.pom \
  --version 1.0.0 \
  --group-id com.example \
  --artifact-id maven-cli-push-test \
  --extra-files build-script.sh,random-file.xml
```

Using multiple extra-files parameters:

```
cloudsmith push maven cloudsmith-test/cli-upload example-maven-project-1.0.0.jar \
  --javadoc-file example-maven-project-1.0.0-javadoc.jar \
  --sources-file example-maven-project-1.0.0-sources.jar \
  --pom-file example-maven-project-1.0.0.pom \
  --version 1.0.0 \
  --group-id com.example \
  --artifact-id maven-cli-push-test \
  --extra-files build-script.sh,random-file.xml \
  --extra-files readme.md
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

### Example Project

For examples of what your project should look like for packaging and publishing/uploading, please have a look at our [examples repository](http://github.com/cloudsmith-io/cloudsmith-examples) (on GitHub). We'll supplement these with more detailed guidance later, but otherwise just ask, we're here to help!

***

## Download / Install a Package

### Setup

To enable the retrieval of Cloudsmith hosted packages via Maven, the first step is to add your repository to the [dependencyManagement](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html#Dependency_Management) section of your `pom.xml` file.

To do this add one of the following XML examples to your project `pom.xml` file:

***

#### Public Repositories

```xml
<repositories>
  <repository>
    <id>NAME</id>
    <url>https://dl.cloudsmith.io/public/OWNER/REPOSITORY/maven/</url>
    <releases>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </releases>
    <snapshots>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </snapshots>
  </repository>
</repositories>
```

***

#### Private Repositories

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.

  The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs
</Callout>

```xml Entitlement Token Authentication
<repositories>
  <repository>
    <id>NAME</id>
    <url>https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/maven/</url>
    <releases>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </releases>
    <snapshots>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </snapshots>
  </repository>
</repositories>
```

```xml HTTP Basic Authentication
<repositories>
  <repository>
    <id>NAME</id>
    <url>https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/maven/</url>
    <releases>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </releases>
    <snapshots>
      <enabled>true</enabled>
      <updatePolicy>always</updatePolicy>
    </snapshots>
  </repository>
</repositories>
```

If using HTTP Basic Authentication, you need to provide one following three types of credentials:

* Cloudsmith Username and Password
* Cloudsmith API Key
* An Entitlement Token

When using HTTP Basic Authentication you'll probably want to keep your credentials separately in your `settings.xml` file instead of within the `pom.xml` file. once you have decided which credentials you wish to use, setup your `settings.xml` file as follows:

```xml Username & Password
<settings>
  <servers>
    <server>
      <id>NAME</id>
      <username>USERNAME</username>
      <password>PASSWORD</password>
    </server>
  </servers>
</settings>
```

```xml API Key
<settings>
  <servers>
    <server>
      <id>NAME</id>
      <username>USERNAME</username>
      <password>API-KEY</password>
    </server>
  </servers>
</settings>
```

```xml Entitlement Token
<settings>
  <servers>
    <server>
      <id>NAME</id>
      <username>token</username>
      <password>TOKEN</password>
    </server>
  </servers>
</settings>
```

<Callout icon="📘" theme="info">
  We would highly advise that you encrypt your credentials using something like `mvn encrypt-password`, of which you can refer to the mini [encryption guide](http://maven.apache.org/guides/mini/guide-encryption.html) for more detailed help (external link).

  For more details on authentication in Maven, please refer to the official [Maven documentation](https://maven.apache.org/settings.html) (external link).
</Callout>

***

### Specifying Dependencies

After the repository is added to the `pom.xml` file, and credentials are added to the `settings.xml` file (if using HTTP Basic Authentication), all that is left is to specify the dependency in the dependencies section of the project pom.xml file.

To do this add the following XML to your project `pom.xml` file:

```xml
<dependency>
  <groupId>GROUP_ID</groupId>
  <artifactId>ARTIFACT_ID</artifactId>
  <version>PACKAGE_VERSION</version>
</dependency>
```

***

### Install a Package

To download all the dependencies specified in your `pom.xml` file and build your project you just need to run:

```shell
mvn install
```

## Security Scanning

<br />

<span class="cs-tag cs-tag-dark-green">Supported</span>
Please see our

[Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>
You can configure upstream Maven repositories that you wish to use for packages that are not available in your Cloudsmith repository. In addition, you can also choose to cache any requested packages for future use.

If you’ve configured your Maven upstream for caching, Cloudsmith will cache all files fetched from your upstream, including arbitrary files.

Our supported upstreams for arbitrary file support are:

* Maven Central
* Artifactory
* Gradle
* Nexus
* WSO2/JBOSS
* Google
* Confluent
* Shibbolenth
* Atlassian

Please see our [Upstream Proxying](https://help.cloudsmith.io/docs/proxying) documentation for further instructions.

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span> <span class="cs-tag cs-tag-purple">Index</span> <span class="cs-tag cs-tag-midnight-blue">Packages</span>

## Troubleshooting

Please see the [Troubleshooting Maven](https://help.cloudsmith.io/docs/troubleshooting-maven) page for further help and information.