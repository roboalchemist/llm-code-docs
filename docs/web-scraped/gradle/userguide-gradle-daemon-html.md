# Source: https://docs.gradle.org/userguide/gradle_daemon.html

Title: Gradle Daemon

URL Source: https://docs.gradle.org/userguide/gradle_daemon.html

Markdown Content:
The Gradle Daemon is a long-lived, persistent process that runs in the background and hosts Gradle’s execution engine. It dramatically reduces build times using caching, runtime optimizations, and eliminating JVM startup overhead.

[](https://docs.gradle.org/userguide/gradle_daemon.html#the_gradle_client_vs_the_gradle_daemon)[The Gradle Client vs. the Gradle Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#the_gradle_client_vs_the_gradle_daemon)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To run any Gradle command, your system starts two separate Java Virtual Machine (JVM) processes, which can use different Java versions.

Understanding their distinct roles and how their respective JVM versions are determined is key to effective build configuration and debugging:

| Process | Role | JVM Version Source |
| --- | --- | --- |
| **Gradle Client JVM** | Process that starts when you run `gradle` or `./gradlew` and stays alive for the **entire build invocation**. It connects to (or starts) a Daemon, sends the build request, and streams output back to the console. | Uses the JVM that launches the wrapper script (e.g. `JAVA_HOME`, `java` on `PATH`, or your IDE). |
| **Gradle Daemon JVM** | Long-lived process that executes the build and caches state between runs. | Uses the JVM set by: - `org.gradle.java.home` (properties) - [Tooling API](https://docs.gradle.org/current/userguide/tooling_api.html#tooling_api) requests (e.g., IDE) - [Daemon JVM toolchains](https://docs.gradle.org/userguide/gradle_daemon.html#sec:configuring_daemon_jvm) By default, the Gradle Client will look for compatible daemons* or start a new one if none are available. |

*Gradle reuses an existing daemon only if its Java home/version and JVM args (e.g., `org.gradle.jvmargs`, `GRADLE_OPTS`) are identical. Changing JVM args (like increasing memory) will spawn a new daemon. In the rare case where the daemon has been disabled (`--no-daemon` or `-Dorg.gradle.daemon=false`) and the Client process is compatible, the Gradle Daemon uses the JVM that launched the Gradle Client.

[](https://docs.gradle.org/userguide/gradle_daemon.html#understanding_daemon)[Understanding the Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#understanding_daemon)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A daemon is a computer program that runs as a background process rather than being under the direct control of an interactive user.

Gradle runs on the Java Virtual Machine (JVM) and uses several supporting libraries with non-trivial initialization time. Startups can be slow. The **Gradle Daemon** solves this problem.

The Gradle Daemon is a long-lived background process that reduces the time it takes to run a build.

The Gradle Daemon reduces build times by:

* Caching project information across builds

* Running in the background so every Gradle build doesn’t have to wait for JVM startup

* Benefiting from continuous runtime optimization in the JVM

* [Watching the file system](https://docs.gradle.org/current/userguide/file_system_watching.html#sec:daemon_watch_fs) to calculate exactly what needs to be rebuilt before you run a build

The Gradle Client sends the Gradle Daemon build information such as command line arguments, project directories, and environment variables so that it can run the build. The Daemon is responsible for resolving dependencies, executing build scripts, creating and running tasks; when it is done, it sends the client the output. Communication between the client and the Daemon happens via a local socket connection.

Daemons use the JVM’s default minimum heap size.

If the requested build environment does not specify a maximum heap size, the Daemon uses up to 512MB of heap. 512MB is adequate for most builds. Larger builds with hundreds of subprojects, configuration, and source code may benefit from a larger heap size.

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:status)[Check Daemon status](https://docs.gradle.org/userguide/gradle_daemon.html#sec:status)
---------------------------------------------------------------------------------------------------------------------------------------------------------

To get a list of running Daemons and their statuses, use the `--status` command:

`$ gradle --status`

```
PID STATUS   INFO
 28486 IDLE     7.5
 34247 BUSY     7.5
```

Currently, a given Gradle version can only connect to Daemons of the same version. This means the status output only shows Daemons spawned running the same version of Gradle as the current project.

[](https://docs.gradle.org/userguide/gradle_daemon.html#find_all_daemons)[Find Daemons](https://docs.gradle.org/userguide/gradle_daemon.html#find_all_daemons)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have installed the Java Development Kit (JDK), you can view live daemons with the `jps` command.

`$ jps`

```
33920 Jps
27171 GradleDaemon
22792
```

Live Daemons appear under the name `GradleDaemon`. Because this command uses the JDK, you can view Daemons running any version of Gradle.

[](https://docs.gradle.org/userguide/gradle_daemon.html#enable_deamon)[Enable Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#enable_deamon)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle enables the Daemon by default since Gradle 3.0. If your project doesn’t use the Daemon, you can enable it for a single build with the `--daemon` flag when you run a build:

`$ gradle <task> --daemon`

This flag overrides any settings that disable the Daemon in your project or user `gradle.properties` files.

To enable the Daemon by default in older Gradle versions, add the following setting to the `gradle.properties` file in the [project root](https://docs.gradle.org/current/userguide/directory_layout.html#dir:project_root) or your Gradle User Home ([`GRADLE_USER_HOME`](https://docs.gradle.org/current/userguide/directory_layout.html#dir:gradle_user_home)):

gradle.properties

`org.gradle.daemon=true`

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:disabling_the_daemon)[Disable Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#sec:disabling_the_daemon)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can disable the Daemon in multiple ways but there are important considerations:

Single-use Daemon
If the JVM args of the client process don’t match what the build requires, a single-used Daemon (disposable JVM) is created. This means the Daemon is required for the build, so it is created, used, and then stopped at the end of the build.

No Daemon
If the `JAVA_OPTS` and `GRADLE_OPTS` match `org.gradle.jvmargs`, the Daemon will not be used at all since the build happens in the client JVM.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_build)[Disable for a build](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_build)

To disable the Daemon for a single build, pass the `--no-daemon` flag when you run a build:

`$ gradle <task> --no-daemon`

This flag overrides any settings that enable the Daemon in your project including the `gradle.properties` files.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_project)[Disable for a project](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_project)

To disable the Daemon for all builds of a project, add `org.gradle.daemon=false` to the `gradle.properties` file in the [project root](https://docs.gradle.org/current/userguide/directory_layout.html#dir:project_root).

### [](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_user)[Disable for a user](https://docs.gradle.org/userguide/gradle_daemon.html#disable_for_a_user)

On Windows, this command disables the Daemon for the current user:

`(if not exist "%USERPROFILE%/.gradle" mkdir "%USERPROFILE%/.gradle") && (echo. >> "%USERPROFILE%/.gradle/gradle.properties" && echo org.gradle.daemon=false >> "%USERPROFILE%/.gradle/gradle.properties")`

On UNIX-like operating systems, the following Bash shell command disables the Daemon for the current user:

`mkdir -p ~/.gradle && echo "org.gradle.daemon=false" >> ~/.gradle/gradle.properties`

### [](https://docs.gradle.org/userguide/gradle_daemon.html#disable_globally)[Disable globally](https://docs.gradle.org/userguide/gradle_daemon.html#disable_globally)

There are two recommended ways to disable the Daemon globally across an environment:

* add `org.gradle.daemon=false` to the `$GRADLE_USER_HOME`/gradle.properties` file

* add the flag `-Dorg.gradle.daemon=false` to the `GRADLE_OPTS` environment variable

Don’t forget to make sure your JVM arguments and `GRADLE_OPTS` / `JAVA_OPTS` match if you want to completely disable the Daemon and not simply invoke a single-use one.

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:stopping_an_existing_daemon)[Stop Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#sec:stopping_an_existing_daemon)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It can be helpful to stop the Daemon when troubleshooting or debugging a failure.

Daemons automatically stop given any of the following conditions:

* Available system memory is low

* Daemon has been idle for 3 hours

To stop running Daemon processes, use the following command:

`$ gradle --stop`

This terminates all Daemon processes started with the same version of Gradle used to execute the command.

You can also kill Daemons manually with your operating system. To find the PIDs for all Daemons regardless of Gradle version, see [Find Daemons](https://docs.gradle.org/userguide/gradle_daemon.html#find_all_daemons).

[](https://docs.gradle.org/userguide/gradle_daemon.html#troubleshooting_the_daemon)[Troubleshooting the Daemon](https://docs.gradle.org/userguide/gradle_daemon.html#troubleshooting_the_daemon)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Gradle Daemon is a long-lived background process, as such, it can sometimes encounter issues.

If builds start behaving unexpectedly, try stopping and restarting the Daemon:

`$ gradle --stop`

If you see a warning like: `Multiple Gradle daemons might be spawned because the Gradle JDK and JAVA_HOME locations are different`.

Gradle is telling you that it’s using more than one Java version across your environment. This can lead to multiple daemons being started, increasing memory usage unnecessarily.

To resolve this, make sure your Java versions match across:

1. Your environment (`JAVA_HOME`)

2. Your build script (if using toolchains)

3. Your IDE’s configured JDK

To check `JAVA_HOME`, run this in your terminal:

`echo $JAVA_HOME`

Your project may be using a specific toolchain in your `build.gradle(.kts)` file. Check for similar code:

```
java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)
    }
}
```

If your build uses a toolchain, ensure it matches the `JAVA_HOME` value, or at least know they differ intentionally. You should also check your IDE settings to make sure they match as well.

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_logs)[Daemon Logs](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_logs)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The Gradle Daemon writes detailed log files to help diagnose build issues and understand daemon behavior.

These logs are stored in the [Gradle User Home](https://docs.gradle.org/current/userguide/directory_layout.html#dir:gradle_user_home) directory under `daemon/<gradle-version>/`:

```
~/.gradle/daemon/9.4.0/
├── daemon-<pid>.out.log
├── daemon-<pid>.out.log
└── registry.bin
```

Each daemon process creates its own log file named `daemon-<pid>.out.log`, where `<pid>` is the process ID of that daemon instance.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_log_cleanup)[Automatic Log Cleanup](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_log_cleanup)

Gradle automatically cleans up old daemon logs to prevent the daemon directory from growing indefinitely.

By default, daemon logs older than 14 days are deleted during build execution as part of Gradle’s periodic cache cleanup. This cleanup runs alongside other [cache cleanup operations](https://docs.gradle.org/current/userguide/directory_layout.html#dir:gradle_user_home:cache_cleanup).

The cleanup is triggered during builds:

* In the background between builds when using the daemon (default behavior)

* In the foreground after the build when using `--no-daemon`

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:configuring_daemon_jvm)[Daemon JVM Toolchains](https://docs.gradle.org/userguide/gradle_daemon.html#sec:configuring_daemon_jvm)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, the Gradle Daemon runs with the same JVM installation that started the build. Gradle defaults to the current shell path and `JAVA_HOME` environment variable to locate a usable JVM.

Alternatively, a different JVM installation can be specified for the build using the [`org.gradle.java.home` Gradle property](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties) or programmatically through the Tooling API.

Building on the [toolchain feature](https://docs.gradle.org/current/userguide/toolchains.html#toolchains), you can now use declarative criteria to specify the JVM requirements for the build.

If the Daemon JVM criteria configuration is provided, it takes precedence over `JAVA_HOME` and `org.gradle.java.home`.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_jvm_criteria)[Daemon JVM criteria](https://docs.gradle.org/userguide/gradle_daemon.html#sec:daemon_jvm_criteria)

The _Daemon JVM criteria_ is controlled by the `updateDaemonJvm` task, similar to how the [wrapper task](https://docs.gradle.org/current/userguide/gradle_wrapper.html#customizing_wrapper) updates the wrapper properties file.

When the task runs, it creates or updates the criteria in the `gradle/gradle-daemon-jvm.properties` file.

To configure the generation, you can use command line options:

`$ ./gradlew updateDaemonJvm --jvm-version=17`

Or configure the task in the build script of the root project:

[![Image 1: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/daemon-jvm/customized-task)

`Kotlin``Groovy`

build.gradle

```
tasks.named("updateDaemonJvm") {
    languageVersion = JavaLanguageVersion.of(17)
}
```

And then run the task:

`$ ./gradlew updateDaemonJvm`

Both of these actions will produce a file like the following one:

gradle/gradle-daemon-jvm.properties

```
#This file is generated by updateDaemonJvm
toolchainUrl.FREE_BSD.AARCH64=https\://example.com/...
toolchainUrl.FREE_BSD.X86_64=https\://example.com/...
toolchainUrl.LINUX.AARCH64=https\://example.com/...
toolchainUrl.LINUX.X86_64=https\://example.com/...
toolchainUrl.MAC_OS.AARCH64=https\://example.com/...
toolchainUrl.MAC_OS.X86_64=https\://example.com/...
toolchainUrl.UNIX.AARCH64=https\://example.com/...
toolchainUrl.UNIX.X86_64=https\://example.com/...
toolchainUrl.WINDOWS.X86_64=https\://example.com/...
toolchainVersion=17
```

If you run the `updateDaemonJvm` task without any arguments, and the properties file does not exist, then the version of the current JVM used by the Daemon will be used.

On the next execution of the build, the Gradle client will use this file to locate a compatible JVM installation and start the Daemon with it.

Similar to the wrapper, the generated `gradle-daemon-jvm.properties` file should be checked into version control. This ensures that any developer or CI server running the build will use the same JVM version.

#### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:specifying_a_jvm_vendor)[Specifying a JVM vendor](https://docs.gradle.org/userguide/gradle_daemon.html#sec:specifying_a_jvm_vendor)

The JVM vendor, like the JVM version, can be used as a criteria to select a compatible JVM installation for the build. If no vendor is specified, Gradle considers all vendors compatible.

By default, running `updateDaemonJvm` to create the `gradle-daemon-jvm.properties` file will not generate a JVM vendor criteria. To specify a vendor, either configure it in the build script, using [the same syntax as the Java toolchain spec](https://docs.gradle.org/current/userguide/toolchains.html#sec:vendors), or pass it on the command line:

`$ ./gradlew updateDaemonJvm --jvm-version=17 --jvm-vendor=adoptium`

List of recognized vendors:

| Known Vendors | Acceptable Strings | `toolchainVendor` Value |
| --- | --- | --- |
| Adoptium / Eclipse Temurin | `adoptium`, `temurin`, `eclipse foundation` | ADOPTIUM |
| AdoptOpenJDK | `adoptopenjdk`, `aoj` | ADOPTOPENJDK |
| Amazon Corretto | `amazon`, `corretto` | AMAZON |
| Apple | `apple` | APPLE |
| Azul Zulu | `azul`, `zulu` | AZUL |
| BellSoft | `bellsoft`, `liberica` | BELLSOFT |
| GraalVM | `graalvm`, `graal vm` | GRAAL_VM |
| Hewlett Packard | `hp`, `hewlett` | HEWLETT_PACKARD |
| IBM | `ibm`, `semeru`, `international business machines corporation` | IBM |
| JetBrains | `jetbrains`, `jbr` | JETBRAINS |
| Microsoft | `microsoft` | MICROSOFT |
| Oracle | `oracle` | ORACLE |
| SAP | `sap` | SAP |
| Tencent | `tencent`, `kona` | TENCENT |

Some vendors will be recognized from more than one set of characters. All vendor strings are case-insensitive. You can view the list of recognized vendors by running `./gradlew help --task updateDaemonJvm`.

If the specified vendor is not one of the recognized equivalents, Gradle will match it exactly. For example, "MyCustomJVM" would require an exact match of the vendor name.

#### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:native_image)[Requesting a native-image capable JDK](https://docs.gradle.org/userguide/gradle_daemon.html#sec:native_image)

Both the CLI options and the task configuration allow to request a JDK that is `native-image` capable.

`$ ./gradlew updateDaemonJvm --jvm-version=17 --native-image-capable`

### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:detect_provision)[Auto-detection and auto-provisioning](https://docs.gradle.org/userguide/gradle_daemon.html#sec:detect_provision)

With _auto-provisioning_, the logic is simpler, as Gradle can only look up a download URL matching the platform inside the `gradle-daemon-jvm.properties` file. The URL is then used to download a JDK if none can be found locally.

The properties used for disabling _auto-detection_ and _auto-provisioning_ affect the Daemon toolchain resolution logic:

```
org.gradle.java.installations.auto-detect=false
org.gradle.java.installations.auto-download=false
```

### [](https://docs.gradle.org/userguide/gradle_daemon.html#sec:configure_provision)[Configuring provisioning URLs](https://docs.gradle.org/userguide/gradle_daemon.html#sec:configure_provision)

There are currently no CLI options for configuring this.

By default, the `updateDaemonJvm` task attempts to generate download URLs for JDKs on various platforms (OS and architecture) that match the specified criteria. Gradle needs to consider more than the current running platform as the build could be run on different platforms.

Gradle sets, by convention, build platforms based on architectures `X86_64` and `AARCH64` for the following operating systems:

* [FreeBSD](https://www.freebsd.org/)

* [Linux](https://www.linux.org/pages/download/)

* [macOS](https://www.apple.com/macos)

* [Solaris](https://www.oracle.com/solaris)

* [UNIX](https://en.wikipedia.org/wiki/List_of_Unix_systems)

* [Windows](https://www.microsoft.com/en-us/windows)

These platforms can be configured through the `toolchainPlatforms` property of the `UpdateDaemonJvm` task.

[![Image 2: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/daemon-jvm/customized-task)

`Kotlin``Groovy`

build.gradle

```
tasks.named("updateDaemonJvm") {
    def myPlatforms = [
        BuildPlatformFactory.of(
            org.gradle.platform.Architecture.AARCH64,
            org.gradle.platform.OperatingSystem.MAC_OS
        )
    ]
    toolchainPlatforms.set(myPlatforms)
}
```

Gradle resolves JDK download URLs for these platforms by using the [configured toolchain download repositories](https://docs.gradle.org/current/userguide/toolchains.html#sub:download_repositories). If no such repositories are configured and the `toolchainPlatforms` property has at least one value, the `updateDaemonJvm` task will fail.

Alternatively, users can directly configure the JDK URLs for specific platforms using the `toolchainDownloadUrls` property. This property is a `Map<BuildPlatform, URI>` and can be configured as shown in the following example:

`Kotlin``Groovy`

build.gradle

```
tasks.named("updateDaemonJvm") {
    toolchainDownloadUrls = [(BuildPlatformFactory.of(org.gradle.platform.Architecture.AARCH64, org.gradle.platform.OperatingSystem.MAC_OS)) : uri("https://server?platform=MAC_OS.AARCH64"),
                             (BuildPlatformFactory.of(org.gradle.platform.Architecture.AARCH64, org.gradle.platform.OperatingSystem.WINDOWS)) : uri("https://server?platform=WINDOWS.AARCH64")]
}
```

Running `./gradlew updateDaemonJvm` produces the following:

```
#This file is generated by updateDaemonJvm
toolchainUrl.MAC_OS.AARCH64=https\://server?platform\=MAC_OS.AARCH64
toolchainUrl.WINDOWS.AARCH64=https\://server?platform\=WINDOWS.AARCH64
toolchainVersion=17
```

If you want to disable the generation of URLs by the `updateDaemonJvm` task:

`Kotlin``Groovy`

build.gradle

```
tasks.named("updateDaemonJvm") {
    toolchainPlatforms = []
}
```

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:tools_and_ides)[Tools & IDEs](https://docs.gradle.org/userguide/gradle_daemon.html#sec:tools_and_ides)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Gradle Tooling API](https://docs.gradle.org/current/userguide/tooling_api.html#embedding) used by IDEs and other tools to integrate with Gradle _always_ uses the Gradle Daemon to execute builds. If you execute Gradle builds from within your IDE, you already use the Gradle Daemon. There is no need to enable it for your environment.

[](https://docs.gradle.org/userguide/gradle_daemon.html#continuous_integration)[Continuous Integration](https://docs.gradle.org/userguide/gradle_daemon.html#continuous_integration)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We recommend using the Daemon for developer machines and Continuous Integration (CI) servers.

[](https://docs.gradle.org/userguide/gradle_daemon.html#deamon_compatibility)[Compatibility](https://docs.gradle.org/userguide/gradle_daemon.html#deamon_compatibility)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle starts a new Daemon if no idle or compatible Daemons exist.

The following values determine compatibility:

* **Requested build environment**, including the following:

  * Java version

  * JVM attributes

  * JVM properties

* Gradle version

Compatibility is based on exact matches of these values. For example:

* If a Daemon is available with a Java 8 runtime, but the requested build environment calls for Java 10, then the Daemon is not compatible.

* If a Daemon is available running Gradle 7.0, but the current build uses Gradle 7.4, then the Daemon is not compatible.

Certain properties of a Java runtime are _immutable_: they cannot be changed once the JVM has started. The following JVM system properties are immutable:

* `file.encoding`

* `user.language`

* `user.country`

* `user.variant`

* `java.io.tmpdir`

* `javax.net.ssl.keyStore`

* `javax.net.ssl.keyStorePassword`

* `javax.net.ssl.keyStoreType`

* `javax.net.ssl.trustStore`

* `javax.net.ssl.trustStorePassword`

* `javax.net.ssl.trustStoreType`

* `com.sun.management.jmxremote`

The following JVM attributes controlled by startup arguments are also immutable:

* The maximum heap size (the `-Xmx` JVM argument)

* The minimum heap size (the `-Xms` JVM argument)

* The boot classpath (the `-Xbootclasspath` argument)

* The "assertion" status (the `-ea` argument)

If the requested build environment requirements for any of these properties and attributes differ from the Daemon’s JVM requirements, the Daemon is not compatible.

[](https://docs.gradle.org/userguide/gradle_daemon.html#sec:why_the_daemon)[Performance Impact](https://docs.gradle.org/userguide/gradle_daemon.html#sec:why_the_daemon)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Daemon can reduce build times by 15-75% when you build the same project repeatedly.

In between builds, the Daemon waits idly for the next build. As a result, your machine only loads Gradle into memory once for multiple builds instead of once per build. This is a significant performance optimization.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#runtime_code_optimizations)[Runtime Code Optimizations](https://docs.gradle.org/userguide/gradle_daemon.html#runtime_code_optimizations)

The JVM gains significant performance from **runtime code optimization**: optimizations applied to code while it runs.

JVM implementations like OpenJDK’s Hotspot progressively optimize code during execution. Consequently, subsequent builds can be faster purely due to this optimization process.

With the Daemon, perceived build times can drop dramatically between a project’s 1 st and 10 th builds.

### [](https://docs.gradle.org/userguide/gradle_daemon.html#memory_caching)[Memory Caching](https://docs.gradle.org/userguide/gradle_daemon.html#memory_caching)

The Daemon enables in-memory caching across builds. This includes classes for plugins and build scripts.

Similarly, the Daemon maintains in-memory caches of build data, such as the hashes of task inputs and outputs for incremental builds.

[](https://docs.gradle.org/userguide/gradle_daemon.html#performance_monitoring)[Performance Monitoring](https://docs.gradle.org/userguide/gradle_daemon.html#performance_monitoring)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle actively monitors heap usage to detect memory leaks in the Daemon.

When a memory leak exhausts available heap space, the Daemon:

1. Finishes the currently running build.

2. Restarts before running the next build.

Gradle enables this monitoring by default.

To disable this monitoring, set the `org.gradle.daemon.performance.enable-monitoring` Daemon option to `false`.

You can do this on the command line with the following command:

`$ gradle <task> -Dorg.gradle.daemon.performance.enable-monitoring=false`

Or you can configure the property in the `gradle.properties` file in the [project root](https://docs.gradle.org/current/userguide/directory_layout.html#dir:project_root) or your [GRADLE_USER_HOME](https://docs.gradle.org/current/userguide/directory_layout.html#dir:gradle_user_home) (Gradle User Home):

gradle.properties

`org.gradle.daemon.performance.enable-monitoring=false`
