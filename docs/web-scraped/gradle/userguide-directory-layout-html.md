# Source: https://docs.gradle.org/userguide/directory_layout.html

Title: Gradle-managed Directories

URL Source: https://docs.gradle.org/userguide/directory_layout.html

Markdown Content:
Gradle uses two main directories to perform and manage its work:

* [1. Gradle User Home directory](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home)

* [2. Project Root directory](https://docs.gradle.org/userguide/directory_layout.html#dir:project_root)

![Image 1: author gradle 2](https://docs.gradle.org/current/userguide/img/author-gradle-2.png)

[](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home)[1. Gradle User Home directory](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

By default, the Gradle User Home (`~/.gradle` or `C:\Users\<USERNAME>\.gradle`) stores global configuration properties, initialization scripts, caches, and log files.

It can be set with the environment variable `GRADLE_USER_HOME`.

Not to be confused with the `GRADLE_HOME`, the optional installation directory for Gradle.

It is roughly structured as follows:

```
├── caches              (1)
│   ├── 4.8         (2)
│   ├── 9.2.0             (2)
│   ├── ⋮
│   ├── jars-3      (3)
│   └── modules-2       (3)
├── daemon          (4)
│   ├── ⋮
│   ├── 4.8
│   └── 9.2.0
├── init.d              (5)
│   └── my-setup.gradle
├── jdks                (6)
│   ├── ⋮
│   └── jdk-14.0.2+12
├── wrapper
│   └── dists           (7)
│       ├── ⋮
│       ├── gradle-4.8-bin
│       ├── gradle-9.2.0-all
│       └── gradle-9.2.0-bin
└── gradle.properties   (8)
```

**1**Global cache directory (for everything that is not project-specific).
**2**Version-specific caches (e.g., to support incremental builds).
**3**Shared caches (e.g., for artifacts of dependencies).
**4**Registry and logs of the [Gradle Daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html#gradle_daemon).
**5**Global [initialization scripts](https://docs.gradle.org/current/userguide/init_scripts.html#init_scripts).
**6**JDKs downloaded by the [toolchain support](https://docs.gradle.org/current/userguide/toolchains.html#sec:provisioning).
**7**Distributions downloaded by the [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html#gradle_wrapper).
**8**Global [Gradle configuration properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties).

### [](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:cache_cleanup)[Cleanup of caches and distributions](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:cache_cleanup)

Gradle automatically cleans its user home directory.

By default, the cleanup runs in the background when the Gradle daemon is stopped or shut down.

If using `--no-daemon`, it runs in the foreground after the build session.

The following cleanup strategies are applied periodically (by default, once every 24 hours):

* Version-specific caches in all `caches/<GRADLE_VERSION>/` directories are checked for whether they are still in use.

If not, directories for release versions are deleted after 30 days of inactivity, and snapshot versions after 7 days.

* Shared caches in `caches/` (e.g., `jars-*`) are checked for whether they are still in use.

If no Gradle version still uses them, they are deleted.

* Files in shared caches used by the current Gradle version in `caches/` (e.g., `jars-3` or `modules-2`) are checked for when they were last accessed.

Depending on whether the file can be recreated locally or downloaded from a remote repository, it will be deleted after 7 or 30 days, respectively.

* Gradle distributions in `wrapper/dists/` are checked for whether they are still in use, i.e., whether there’s a corresponding version-specific cache directory.

Unused distributions are deleted.

* Daemon log files in `daemon/<GRADLE_VERSION>/` directories are checked for their last modification time.

Log files older than 14 days are automatically deleted to prevent the daemon directory from growing indefinitely.

#### [](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:configure_cache_cleanup)[Configuring cleanup of caches and distributions](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:configure_cache_cleanup)

The retention periods of the various caches can be configured.

Caches are classified into six categories:

1. **Released wrapper distributions:** Distributions and related version-specific caches corresponding to released versions (e.g., `4.6.2` or `8.0`).

Default retention for unused versions is 30 days.

1. **Snapshot wrapper distributions:** Distributions and related version-specific caches corresponding to snapshot versions (e.g. `7.6-20221130141522+0000`).

Default retention for unused versions is 7 days.

1. **Downloaded resources:** Shared caches downloaded from a remote repository (e.g., cached dependencies).

Default retention for unused resources is 30 days.

1. **Created resources:** Shared caches that Gradle creates during a build (e.g., artifact transforms).

Default retention for unused resources is 7 days.

1. **Build cache:** The local build cache (e.g., build-cache-1).

Default retention for unused build cache entries is 7 days.

1. **Daemon logs:** Log files from Gradle Daemon processes in `daemon/<GRADLE_VERSION>/` directories.

Default retention for daemon logs is 14 days.

The retention period for each category can be configured independently via an [init script](https://docs.gradle.org/current/userguide/init_scripts.html#init_scripts) in the Gradle User Home:

`Kotlin``Groovy`

gradleUserHome/init.d/cache-settings.init.gradle

```
beforeSettings { settings ->
    settings.caches {
        releasedWrappers.removeUnusedEntriesAfterDays = 45
        snapshotWrappers.removeUnusedEntriesAfterDays = 10
        downloadedResources.removeUnusedEntriesAfterDays = 45
        createdResources.removeUnusedEntriesAfterDays = 10
        buildCache.removeUnusedEntriesAfterDays = 5
        daemonLogs.removeUnusedEntriesAfterDays = 14
    }
}
```

The frequency at which cache cleanup is invoked is also configurable.

There are three possible settings:

1. **DEFAULT:** Cleanup is performed periodically in the background (currently once every 24 hours).

2. **DISABLED:** Never cleanup Gradle User Home.

This is useful in cases where Gradle User Home is ephemeral or delaying cleanup is desirable until an explicit point.

1. **ALWAYS:** Cleanup is performed at the end of each build session.

This is useful in cases where it’s desirable to ensure that cleanup has occurred before proceeding.

However, this performs cache cleanup during the build (rather than in the background), which can be expensive, so this option should only be used when necessary.

To disable cache cleanup:

`Kotlin``Groovy`

gradleUserHome/init.d/cache-settings.init.gradle

```
beforeSettings { settings ->
    settings.caches {
        cleanup = Cleanup.DISABLED
    }
}
```

Cache cleanup settings can only be configured via init scripts and should be placed under the `init.d` directory in Gradle User Home. This effectively couples the configuration of cache cleanup to the Gradle User Home those settings apply to and limits the possibility of different conflicting settings from different projects being applied to the same directory.

#### [](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:multi_version_cache_cleanup)[Multiple versions of Gradle sharing a Gradle User Home](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:multi_version_cache_cleanup)

It is common to share a single Gradle User Home between multiple versions of Gradle.

As stated above, caches in Gradle User Home are version-specific. Different versions of Gradle will perform maintenance on only the version-specific caches associated with each version.

On the other hand, some caches are shared between versions (e.g., the dependency artifact cache or the artifact transform cache).

Beginning with Gradle version 8.0, the cache cleanup settings can be configured to custom retention periods. However, older versions have fixed retention periods (7 or 30 days, depending on the cache). These shared caches could be accessed by versions of Gradle with different settings to retain cache artifacts.

This means that:

* If the retention period is _not_ customized, all versions that perform cleanup will have the same retention periods. There will be no effect due to sharing a Gradle User Home with multiple versions.

* If the retention period is customized for Gradle versions greater than or equal to version 8.0 to use retention periods _shorter_ than the previously fixed periods, there will also be no effect.

The versions of Gradle aware of these settings will cleanup artifacts earlier than the previously fixed retention periods, and older versions will effectively not participate in the cleanup of shared caches.

* If the retention period is customized for Gradle versions greater than or equal to version 8.0 to use retention periods _longer_ than the previously fixed periods, the older versions of Gradle may clean the shared caches earlier than what is configured.

In this case, if it is desirable to maintain these shared cache entries for newer versions for longer retention periods, they will not be able to share a Gradle User Home with older versions. They will need to use a separate directory.

Another consideration when sharing the Gradle User Home with versions of Gradle before version 8.0 is that the DSL elements to configure the cache retention settings are unavailable in earlier versions, so this must be accounted for in any init script shared between versions. This can easily be handled by conditionally applying a version-compliant script.

The version-compliant script should reside somewhere other than the `init.d` directory (such as a sub-directory), so it is not automatically applied.

To configure cache cleanup in a version-safe manner:

`Kotlin``Groovy`

gradleUserHome/init.d/cache-settings.init.gradle

```
if (GradleVersion.current() >= GradleVersion.version('8.0')) {
    apply from: "gradle8/cache-settings.init.gradle"
}
```

Version-compliant cache configuration script:

`Kotlin``Groovy`

gradleUserHome/init.d/gradle8/cache-settings.init.gradle

```
beforeSettings { settings ->
    settings.caches {
        releasedWrappers.removeUnusedEntriesAfterDays = 45
        snapshotWrappers.removeUnusedEntriesAfterDays = 10
        downloadedResources.removeUnusedEntriesAfterDays = 45
        createdResources.removeUnusedEntriesAfterDays = 10
        buildCache.removeUnusedEntriesAfterDays = 5
    }
}
```

### [](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:cache_marking)[Cache marking](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:cache_marking)

Beginning with Gradle version 8.1, Gradle supports marking caches with a `CACHEDIR.TAG` file.

It follows the format described in [the Cache Directory Tagging Specification](https://bford.info/cachedir/). The purpose of this file is to allow tools to identify the directories that do not need to be searched or backed up.

By default, the directories `caches`, `wrapper/dists`, `daemon`, and `jdks` in the Gradle User Home are marked with this file.

#### [](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:configure_cache_marking)[Configuring cache marking](https://docs.gradle.org/userguide/directory_layout.html#dir:gradle_user_home:configure_cache_marking)

The cache marking feature can be configured via an init script in the Gradle User Home:

`Kotlin``Groovy`

gradleUserHome/init.d/cache-settings.init.gradle

```
beforeSettings { settings ->
    settings.caches {
        // Disable cache marking for all caches
        markingStrategy = MarkingStrategy.NONE
    }
}
```

Cache marking settings can only be configured via init scripts and should be placed under the `init.d` directory in Gradle User Home. This effectively couples the configuration of cache marking to the Gradle User Home to which those settings apply and limits the possibility of different conflicting settings from different projects being applied to the same directory.

[](https://docs.gradle.org/userguide/directory_layout.html#dir:project_root)[2. Project Root directory](https://docs.gradle.org/userguide/directory_layout.html#dir:project_root)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The project root directory contains all source files from your project.

It also contains files and directories Gradle generates, such as `.gradle` and `build`.

While the former are usually checked into source control, the latter are transient files Gradle uses to support features like incremental builds.

The anatomy of a typical project root directory looks as follows:

```
├── .gradle                 (1)
│   ├── 4.8             (2)
│   ├── 4.9                 (2)
│   └── ⋮
├── build               (3)
├── gradle
│   └── wrapper             (4)
├── gradle.properties   (5)
├── gradlew                 (6)
├── gradlew.bat         (6)
├── settings.gradle.kts     (7)
├── subproject-one      (8)
|   └── build.gradle.kts    (9)
├── subproject-two      (8)
|   └── build.gradle.kts    (9)
└── ⋮
```

**1**Project-specific cache directory generated by Gradle.
**2**Version-specific caches (e.g., to support incremental builds).
**3**The build directory of this project into which Gradle generates all build artifacts.
**4**Contains the JAR file and configuration of the [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html#gradle_wrapper).
**5**Project-specific [Gradle configuration properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties).
**6**Scripts for executing builds using the [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html#gradle_wrapper).
**7**The project’s [settings file](https://docs.gradle.org/current/userguide/settings_file_basics.html#sec:settings_file_script) where the list of subprojects is defined.
**8**Usually, a project is organized into one or multiple subprojects.
**9**Each subproject has its own Gradle build script.

### [](https://docs.gradle.org/userguide/directory_layout.html#dir:project_root:cache_cleanup)[Project cache cleanup](https://docs.gradle.org/userguide/directory_layout.html#dir:project_root:cache_cleanup)

From version 4.10 onwards, Gradle automatically cleans the project-specific cache directory.

After building the project, version-specific cache directories in `.gradle/9.4.0/` are checked periodically (at most, every 24 hours) to determine whether they are still in use. They are deleted if they haven’t been used for 7 days.
