# Source: https://docs.gradle.org/userguide/gradle_wrapper.html

Title: Gradle Wrapper

URL Source: https://docs.gradle.org/userguide/gradle_wrapper.html

Markdown Content:
The **recommended way to execute any Gradle build** is with the help of the Gradle Wrapper (referred to as "Wrapper").

**The Wrapper is a script** (called `gradlew` or `gradlew.bat`) that invokes a declared version of Gradle, downloading it beforehand if necessary. Instead of running `gradle build` using the installed Gradle, you use the Gradle Wrapper by calling `./gradlew build`.

![Image 1: wrapper workflow](https://docs.gradle.org/current/userguide/img/wrapper-workflow.png)

The Gradle Wrapper isn’t distributed as a standalone download—it’s created using the `gradle wrapper` task.

There are three ways to use the Wrapper:

1. **Adding the Wrapper** - You set up a new Gradle project and [add the Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:adding_wrapper) to it.

2. **Using the Wrapper** - You [run a project with the Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:using_wrapper) that already provides it.

3. **Upgrading the Wrapper** - You [upgrade the Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:upgrading_wrapper) to a new version of Gradle.

When using the Wrapper instead of the installed Gradle, you gain the following benefits:

* Standardizes a project on a given Gradle version for more reliable and robust builds.

* Provisioning the Gradle version for different users is done with a simple Wrapper definition change.

* Provisioning the Gradle version for different execution environments (e.g., IDEs or Continuous Integration servers) is done with a simple Wrapper definition change.

The following sections explain each of these use cases in more detail.

[](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:adding_wrapper)[1. Adding the Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:adding_wrapper)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Gradle Wrapper is **not** something you download.

Generating the Wrapper files requires an installed version of the Gradle runtime on your machine as described in [Installation](https://docs.gradle.org/current/userguide/installation.html#installation). Thankfully, generating the initial Wrapper files is a one-time process.

Every vanilla Gradle build comes with a built-in task called `wrapper`. The task is listed under the group "Build Setup tasks" when [listing the tasks](https://docs.gradle.org/current/userguide/command_line_interface.html#sec:listing_tasks).

Executing the `wrapper` task generates the necessary Wrapper files in the project directory:

`$ gradle wrapper`

```
> Task :wrapper

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

To make the Wrapper files available to other developers and execution environments, you need to check them into version control.

Wrapper files, including the JAR file, are small. Adding the JAR file to version control is expected. Some organizations do not allow projects to submit binary files to version control, and there is no workaround available.

The generated Wrapper properties file, `gradle/wrapper/gradle-wrapper.properties`, stores the information about the Gradle distribution:

* The **server hosting** the Gradle distribution.

* The **type of Gradle distribution**. By default, the `-bin` distribution contains only the runtime but no sample code and documentation.

* The **Gradle version** used for executing the build. By default, the `wrapper` task picks the same Gradle version used to generate the Wrapper files.

* Optionally, a **timeout** in ms used when downloading the Gradle distribution.

* Optionally, a **boolean** to set the **validation of the distribution** URL.

The following is an example of the generated distribution URL in `gradle/wrapper/gradle-wrapper.properties`:

`distributionUrl=https\://services.gradle.org/distributions/gradle-9.4.0-bin.zip`

Use the `-bin` distribution for most builds.

The `-bin` distribution contains only the runtime needed to build and run Gradle. It’s smaller to download and faster to cache on CI systems compared to the `-all` distribution, which also includes Gradle’s full source code and documentation.

All of those aspects are configurable at the time of generating the Wrapper files with the help of the following command line options:

`--gradle-version`
The Gradle version used for downloading and executing the Wrapper. The resulting distribution URL is validated before it is written to the properties file.

For Gradle versions starting with major version 9, the version can be specified using only the major or minor version number. In such cases, the latest normal release matching that major or minor version will be used. For example, `9` resolves to the latest `9.x.y` release, and `9.1` resolves to the latest `9.1.x` release.

The following labels are allowed:

* `latest`

* `release-candidate`

* `release-milestone`

* `release-nightly`

* `nightly`

`--distribution-type`
The Gradle distribution type used for the Wrapper. Available options are `bin` and `all`. The default value is `bin`.

`--gradle-distribution-url`
The full URL pointing to the Gradle distribution ZIP file. This option makes `--gradle-version` and `--distribution-type` obsolete, as the URL already contains this information. This option is valuable if you want to host the Gradle distribution inside your company’s network. The URL is validated before it is written to the properties file.

`--gradle-distribution-sha256-sum`
The SHA256 hash sum used for [verifying the downloaded Gradle distribution](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:verification).

`--network-timeout`
The network timeout to use when downloading the Gradle distribution, in ms. The default value is `10000`.

`--no-validate-url`
Disables the validation of the configured distribution URL.

`--validate-url`
Enables the validation of the configured distribution URL. Enabled by default.

If the distribution URL is configured with `--gradle-version` or `--gradle-distribution-url`, the URL is validated by sending a HEAD request in the case of the `https` scheme or by checking the existence of the file in the case of the `file` scheme.

Let’s assume the following use-case to illustrate the use of the command line options. You would like to generate the Wrapper with version 9.4.0 and use the `-all` distribution to enable your IDE to enable code-completion and being able to navigate to the Gradle source code.

The following command-line execution captures those requirements:

`$ gradle wrapper --gradle-version 9.4.0 --distribution-type all`

```
> Task :wrapper

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

As a result, you can find the desired information (the generated distribution URL) in the Wrapper properties file:

`distributionUrl=https\://services.gradle.org/distributions/gradle-9.4.0-all.zip`

Let’s have a look at the following project layout to illustrate the expected Wrapper files:

`Kotlin``Groovy`

```
.
├── a-subproject
│   └── build.gradle
├── settings.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
└── gradlew.bat
```

A Gradle project typically provides a `settings.gradle(.kts)` file and one `build.gradle(.kts)` file for each subproject. The Wrapper files live alongside in the `gradle` directory and the root directory of the project.

The following list explains their purpose:

`gradle-wrapper.jar`
The Wrapper JAR file containing code for downloading the Gradle distribution.

`gradle-wrapper.properties`
A properties file responsible for configuring the Wrapper runtime behavior e.g. the Gradle version compatible with this version. Note that more generic settings, like [configuring the Wrapper to use a proxy](https://docs.gradle.org/current/userguide/networking.html#sec:accessing_the_web_via_a_proxy), need to go into a [different file](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties).

`gradlew`, `gradlew.bat`
A shell script and a Windows batch script for executing the build with the Wrapper.

You can go ahead and [execute the build with the Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:using_wrapper) without installing the Gradle runtime. If the project you are working on does not contain those Wrapper files, you will need to [generate them](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:adding_wrapper).

[](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:using_wrapper)[2. Using the Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:using_wrapper)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is always recommended to execute a build with the Wrapper to ensure a reliable, controlled, and standardized execution of the build. Using the Wrapper looks like running the build with a Gradle installation. Depending on the operating system you either run `gradlew` or `gradlew.bat` instead of the `gradle` command.

The following console output demonstrates the use of the Wrapper on a Windows machine for a Java-based project:

`$ gradlew.bat build`

```
Downloading https://services.gradle.org/distributions/gradle-5.0-all.zip
.....................................................................................
Unzipping C:\Documents and Settings\Claudia\.gradle\wrapper\dists\gradle-5.0-all\ac27o8rbd0ic8ih41or9l32mv\gradle-5.0-all.zip to C:\Documents and Settings\Claudia\.gradle\wrapper\dists\gradle-5.0-al\ac27o8rbd0ic8ih41or9l32mv
Set executable permissions for: C:\Documents and Settings\Claudia\.gradle\wrapper\dists\gradle-5.0-all\ac27o8rbd0ic8ih41or9l32mv\gradle-5.0\bin\gradle

BUILD SUCCESSFUL in 12s
1 actionable task: 1 executed
```

If the Gradle distribution was not provisioned to `GRADLE_USER_HOME` before, the Wrapper will download it and store it in `GRADLE_USER_HOME`. Any subsequent build invocation will reuse the existing local distribution as long as the distribution URL in the Gradle properties doesn’t change.

The Wrapper shell script and batch file reside in the root directory of a single or multi-project Gradle build. You will need to reference the correct path to those files in case you want to execute the build from a subproject directory e.g. `../../gradlew tasks`.

[](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:upgrading_wrapper)[3. Upgrading the Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:upgrading_wrapper)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Projects typically want to keep up with the times and upgrade their Gradle version to benefit from new features and improvements.

The recommended option is to run the `wrapper` task and provide the target Gradle version as described in [Adding the Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:adding_wrapper). Using the `wrapper` task ensures that any optimizations made to the Wrapper shell script or batch file with that specific Gradle version are applied to the project.

As usual, you should commit the changes to the Wrapper files to version control.

Note that running the wrapper task once will update `gradle-wrapper.properties` only, but leave the wrapper itself in `gradle-wrapper.jar` untouched. This is usually fine as new versions of Gradle can be run even with older wrapper files.

If you want **all** the wrapper files to be completely up-to-date, you will need to run the `wrapper` task a second time.

The following command upgrades the Wrapper to the `latest` version:

`$ ./gradlew wrapper --gradle-version latest   // MacOs, Linux`

`$ gradlew.bat wrapper --gradle-version latest // Windows`

```
BUILD SUCCESSFUL in 4s
1 actionable task: 1 executed
```

The following command upgrades the Wrapper to a specific version:

`$ ./gradlew wrapper --gradle-version 9.4.0 // MacOs, Linux`

`$ gradlew.bat wrapper --gradle-version 9.4.0 // Windows`

```
BUILD SUCCESSFUL in 4s
1 actionable task: 1 executed
```

Once you have upgraded the wrapper, you can check that it’s the version you expected by executing `./gradlew --version`.

Don’t forget to run the `wrapper` task again to download the Gradle distribution binaries (if needed) and update the `gradlew` and `gradlew.bat` files.

Another way to upgrade the Gradle version is by manually changing the `distributionUrl` property in the Wrapper’s `gradle-wrapper.properties` file. The tip above also applies in this case.

Since Gradle 9.0.0, the version _always_ uses the `X.Y.Z` format. Using only the major or minor version is not supported in `gradle-wrapper.properties`.

[](https://docs.gradle.org/userguide/gradle_wrapper.html#customizing_wrapper)[Customizing the Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html#customizing_wrapper)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most users of Gradle are happy with the default runtime behavior of the Wrapper. However, organizational policies, security constraints or personal preferences might require you to dive deeper into customizing the Wrapper.

Thankfully, the built-in `wrapper` task exposes numerous options to bend the runtime behavior to your needs. Most configuration options are exposed by the underlying task type [Wrapper](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.wrapper.Wrapper.html).

Let’s assume you grew tired of defining the `-all` distribution type on the command line every time you upgrade the Wrapper. You can save yourself some keyboard strokes by re-configuring the `wrapper` task.

`Kotlin``Groovy`

build.gradle

```
tasks.named('wrapper') {
    distributionType = Wrapper.DistributionType.ALL
}
```

With the configuration in place, running `./gradlew wrapper --gradle-version 9.4.0` is enough to produce a `distributionUrl` value in the Wrapper properties file that will request the `-all` distribution:

`distributionUrl=https\://services.gradle.org/distributions/gradle-9.4.0-all.zip`

Check out the [API documentation](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/wrapper/Wrapper.html) for a more detailed description of the available configuration options. You can also find various samples for configuring the Wrapper in the Gradle distribution.

### [](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:authenticated_download)[Authenticated Gradle distribution download](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:authenticated_download)

The Gradle `Wrapper` can download Gradle distributions from servers using HTTP Basic Authentication or with a static HTTP Bearer Token. This enables you to host the Gradle distribution on a private protected server.

You can specify a username and password in two different ways depending on your use case: as system properties or directly embedded in the `distributionUrl`. Credentials in system properties take precedence over the ones embedded in `distributionUrl`.

Any Authentication (HTTP Basic / Bearer Token) should only be used with `HTTPS` URLs and not plain `HTTP` ones. With Basic Authentication, the user credentials are sent in clear text. With Bearer Token, the Token itself is sent in clear text.

System properties can be specified in the `.gradle/gradle.properties` file in the user’s home directory or by other [means](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties).

To specify the HTTP Basic Authentication credentials, add the following lines to the system properties file:

```
systemProp.gradle.wrapperUser=username
systemProp.gradle.wrapperPassword=password
```

Embedding credentials in the `distributionUrl` in the `gradle/wrapper/gradle-wrapper.properties` file also works. Please note that this file is to be committed into your source control system.

Shared credentials embedded in `distributionUrl` should only be used in a controlled environment.

To specify the HTTP Basic Authentication credentials in `distributionUrl`, add the following line:

`distributionUrl=https://username:password@somehost/path/to/gradle-distribution.zip`

This can be used in conjunction with a proxy, authenticated or not. See [Accessing the web via a proxy](https://docs.gradle.org/current/userguide/networking.html#sec:accessing_the_web_via_a_proxy) for more information on how to configure the `Wrapper` to use a proxy.

Using `systemProp.gradle.wrapperUser` and `systemProp.gradle.wrapperPassword` may leak your credentials if the build attempts to download the Gradle Wrapper from a server other than your private one.

To safeguard your credentials, prefix these system properties with your private server’s hostname, replacing all dots (`.`) with underscores (`_`).

Hostnames are not case-sensitive thus Gradle converts the hostname in the property name into lowercase. That is, if you wrote `MYCOMPANY.COM` in your wrapper configuration, then you have to use the string `mycompany_com` in the system property key.

For example, if your private server hostname is `your.private-server.com`, use the following system properties:

```
systemProp.gradle.your_private-server_com.wrapperUser=username
systemProp.gradle.your_private-server_com.wrapperPassword=password
```

To authenticate with a static HTTP Bearer Token, add the following line to your Gradle properties file:

`systemProp.gradle.your_private-server_com.wrapperToken=some-api-token`

If a `wrapperToken` is specified, it will take precedence over `wrapperUser` and `wrapperPassword` system properties (and also over user & password values embedded in the URL). It is strongly recommended to include the hostname in the property to prevent the token from being sent to an unintended server by accident.

### [](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:verification)[Verification of downloaded Gradle distributions](https://docs.gradle.org/userguide/gradle_wrapper.html#sec:verification)

The Gradle Wrapper allows for verification of the downloaded Gradle distribution via SHA-256 hash sum comparison. This increases security against targeted attacks by preventing a man-in-the-middle attacker from tampering with the downloaded Gradle distribution.

To enable this feature, download the `.sha256` file associated with the Gradle distribution you want to verify.

#### [](https://docs.gradle.org/userguide/gradle_wrapper.html#configuring_checksum_verification)[Configuring checksum verification](https://docs.gradle.org/userguide/gradle_wrapper.html#configuring_checksum_verification)

Add the downloaded (SHA-256 checksum) hash sum to `gradle-wrapper.properties` using the `distributionSha256Sum` property or use `--gradle-distribution-sha256-sum` on the command-line:

`distributionSha256Sum=371cb9fbebbe9880d147f59bab36d61eee122854ef8c9ee1ecf12b82368bcf10`

Gradle will report a build failure if the configured checksum does not match the checksum found on the server hosting the distribution. Checksum verification is only performed if the configured Wrapper distribution hasn’t been downloaded yet.

The `Wrapper` task fails if `gradle-wrapper.properties` contains `distributionSha256Sum`, but the task configuration does not define a sum. Executing the `Wrapper` task preserves the `distributionSha256Sum` configuration when the Gradle version does not change.

[](https://docs.gradle.org/userguide/gradle_wrapper.html#wrapper_checksum_verification)[Verifying the integrity of the Gradle Wrapper JAR](https://docs.gradle.org/userguide/gradle_wrapper.html#wrapper_checksum_verification)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Wrapper JAR is a binary file that will be executed on the computers of developers and build servers. As with all such files, you should ensure it’s trustworthy before executing it.

Since the Wrapper JAR is usually checked into a project’s version control system, there is the potential for a malicious actor to replace the original JAR with a modified one by submitting a pull request that only upgrades the Gradle version.

To verify the integrity of the Wrapper JAR, Gradle has created a [GitHub Action](https://github.com/marketplace/actions/build-with-gradle#the-wrapper-validation-action) that automatically checks Wrapper JARs in pull requests against a list of known good checksums.

Gradle also publishes the [checksums of all releases](https://gradle.org/release-checksums/) (except for version 3.3 to 4.0.2, which did not generate reproducible JARs), so you can manually verify the integrity of the Wrapper JAR.

### [](https://docs.gradle.org/userguide/gradle_wrapper.html#automatically_verifying_the_gradle_wrapper_jar_on_github)[Automatically verifying the Gradle Wrapper JAR on GitHub](https://docs.gradle.org/userguide/gradle_wrapper.html#automatically_verifying_the_gradle_wrapper_jar_on_github)

The [GitHub Action](https://github.com/marketplace/actions/build-with-gradle#the-wrapper-validation-action) is released separately from Gradle, so please check its documentation for how to apply it to your project.

### [](https://docs.gradle.org/userguide/gradle_wrapper.html#manually_verifying_the_gradle_wrapper_jar)[Manually verifying the Gradle Wrapper JAR](https://docs.gradle.org/userguide/gradle_wrapper.html#manually_verifying_the_gradle_wrapper_jar)

You can manually verify the checksum of the Wrapper JAR to ensure that it has not been tampered with by running the following commands on one of the major operating systems.

Manually verifying the checksum of the Wrapper JAR on Linux:

`$ cd gradle/wrapper`

```
$ curl --location --output gradle-wrapper.jar.sha256 \
       https://services.gradle.org/distributions/gradle-9.4.0-wrapper.jar.sha256
```

`$ echo " gradle-wrapper.jar" >> gradle-wrapper.jar.sha256`

`$ sha256sum --check gradle-wrapper.jar.sha256`

`gradle-wrapper.jar: OK`

Manually verifying the checksum of the Wrapper JAR on macOS:

`$ cd gradle/wrapper`

```
$ curl --location --output gradle-wrapper.jar.sha256 \
       https://services.gradle.org/distributions/gradle-9.4.0-wrapper.jar.sha256
```

`$ echo " gradle-wrapper.jar" >> gradle-wrapper.jar.sha256`

`$ shasum --check gradle-wrapper.jar.sha256`

`gradle-wrapper.jar: OK`

Manually verifying the checksum of the Wrapper JAR on Windows (using PowerShell):

`> $expected = Invoke-RestMethod -Uri https://services.gradle.org/distributions/gradle-9.4.0-wrapper.jar.sha256`

`> $actual = (Get-FileHash gradle\wrapper\gradle-wrapper.jar -Algorithm SHA256).Hash.ToLower()`

`> @{$true = 'OK: Checksum match'; $false = "ERROR: Checksum mismatch!`nExpected: $expected`nActual:   $actual"}[$actual -eq $expected]`

`OK: Checksum match`

### [](https://docs.gradle.org/userguide/gradle_wrapper.html#troubleshooting_a_checksum_mismatch)[Troubleshooting a checksum mismatch](https://docs.gradle.org/userguide/gradle_wrapper.html#troubleshooting_a_checksum_mismatch)

If the checksum does not match the one you expected, chances are the `wrapper` task wasn’t executed with the upgraded Gradle distribution.

You should first check whether the actual checksum matches a different Gradle version.

Here are the commands you can run on the major operating systems to generate the actual checksum of the Wrapper JAR.

Generating the checksum of the Wrapper JAR on Linux:

```
$ sha256sum gradle/wrapper/gradle-wrapper.jar
d81e0f23ade952b35e55333dd5f1821585e887c6d24305aeea2fbc8dad564b95 gradle/wrapper/gradle-wrapper.jar
```

Generating the actual checksum of the Wrapper JAR on macOS:

```
$ shasum --algorithm=256 gradle/wrapper/gradle-wrapper.jar
d81e0f23ade952b35e55333dd5f1821585e887c6d24305aeea2fbc8dad564b95 gradle/wrapper/gradle-wrapper.jar
```

Generating the actual checksum of the Wrapper JAR on Windows (using PowerShell):

```
> (Get-FileHash gradle\wrapper\gradle-wrapper.jar -Algorithm SHA256).Hash.ToLower()
d81e0f23ade952b35e55333dd5f1821585e887c6d24305aeea2fbc8dad564b95
```

Once you know the actual checksum, check whether it’s listed on [https://gradle.org/release-checksums/](https://gradle.org/release-checksums/). If it is listed, you have verified the integrity of the Wrapper JAR. If the version of Gradle that generated the Wrapper JAR doesn’t match the version in `gradle/wrapper/gradle-wrapper.properties`, it’s safe to run the `wrapper` task again to update the Wrapper JAR.

If the checksum is not listed on the page, the Wrapper JAR might be from a milestone, release candidate, or nightly build or may have been generated by Gradle 3.3 to 4.0.2. Try to find out how it was generated but treat it as untrustworthy until proven otherwise. If you think the Wrapper JAR was compromised, please let the Gradle team know by sending an email to [security@gradle.com](mailto:security@gradle.com).
