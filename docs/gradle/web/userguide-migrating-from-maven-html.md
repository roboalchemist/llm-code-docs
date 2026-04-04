# Source: https://docs.gradle.org/userguide/migrating_from_maven.html

Title: Migrating Builds From Apache Maven

URL Source: https://docs.gradle.org/userguide/migrating_from_maven.html

Markdown Content:
[Apache Maven](https://maven.apache.org/) is a build tool for Java and other JVM-based projects. It is typical to migrate an existing Maven build to Gradle.

This guide will help with such a migration by explaining the differences and similarities between the two tools and providing steps that you can follow to ease the process.

Converting a build can be scary, but you don’t have to do it alone. You can search our [documentation](https://docs.gradle.org/), post on our [community forums](https://discuss.gradle.org/), or reach out on our [Slack channel](https://gradle.org/slack-invite) if you get stuck.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:making_a_case)[Making a case for migration](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:making_a_case)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The primary differences between Gradle and Maven are flexibility, performance, user experience, and dependency management.

Since Gradle 3.0, Gradle has invested heavily in making Gradle builds much faster, with features such as [build caching](https://blog.gradle.org/introducing-gradle-build-cache), [compile avoidance](https://blog.gradle.org/incremental-compiler-avoidance), and an improved incremental Java compiler. Gradle is now 2-10x faster than Maven for the vast majority of projects, even without using a build cache. In-depth performance comparison and business cases for switching from Maven to Gradle can be found [here](https://gradle.org/gradle-vs-maven-performance/).

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:general_guidelines)[General guidelines](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:general_guidelines)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle and Maven have fundamentally different views on how to build a project. Gradle provides a flexible and extensible build model that delegates the actual work to the execution of a graph of tasks. Maven uses a model of fixed, linear phases to which you can attach goals (the things that do the work). This may make migrating between the two seem intimidating, but migrations can be surprisingly easy because Gradle follows many of the same conventions as Maven — such as the [standard project structure](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_project_layout) — and its dependency management works in a similar way.

Here we lay out a series of steps for you to follow that will help facilitate the migration of any Maven build to Gradle:

Keep the old Maven build and new Gradle build side by side. You know the Maven build works, so you should keep it until you are confident that the Gradle build produces all the same artifacts. This also means that users can try the Gradle build without creating a new copy of the source tree.

1. [Create a Build Scan for the Maven build](https://scans.gradle.com/).

A Build Scan will make it easier to visualize what’s happening in your existing Maven build. For Maven builds, you will be able to see the project structure, what plugins are being used, a timeline of the build steps, and more. Keep this handy so you can compare it to the Build Scan while converting the project.

1. Develop a mechanism to verify that the two builds produce the same artifacts.

This is a vitally important step to ensure that your deployments and tests don’t break. Even small changes, such as the contents of a manifest file in a JAR, can cause problems. If your Gradle build produces the same output as the Maven build, this will give you confidence in switching over and make it easier to implement the changes that will provide the greatest benefits.

This doesn’t mean that you need to verify every artifact at every stage, although doing so can help you quickly identify the source of a problem. You should focus on the critical output such as final reports and the artifacts that are published or deployed.

You will need to factor in some inherent differences in the build output that Gradle produces compared to Maven. Generated POMs will contain only the information needed for consumption and they will use `<compile>` and `<runtime>` scopes correctly for that scenario. You might also see differences in the order of files in archives and of files on classpaths. Most differences will be minor, but it’s worth identifying them and verifying that they are acceptable.

1. [Run an automatic conversion](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:automatic_conversion).

This will create all the Gradle build files you need, even for [multi-module builds](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:multimodule_builds). For simpler Maven projects, the Gradle build will be ready to run!

1. [Create a Build Scan for the Gradle build](https://scans.gradle.com/).

A Build Scan will make it easier to visualize what’s happening in the build. For Gradle builds, you’ll be able to see the project structure, the dependencies (regular and inter-project ones), what plugins are being used and the console output of the build.

Your build may fail at this point, but that’s ok; the scan will still run. Compare the Build Scan for the Gradle build to the one for the Maven build and continue down this list to troubleshoot the failures.

We recommend that you regularly generate a Build Scan during the migration to help you identify and troubleshoot problems. If you want, you can also use a Build Scan to identify opportunities to [improve the performance of the build](https://docs.gradle.org/current/userguide/performance.html#performance_gradle).

1. [Verify your dependencies and fix any problems](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:migrating_deps).

2. [Configure integration and functional tests](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:integration_tests).

Many tests can simply be migrated by configuring an extra source set. If you are using a third-party library, such as [FitNesse](https://fitnesse.org/FitNesse/UserGuide.html), look to see whether there is a suitable community plugin available on the [Gradle Plugin Portal](https://plugins.gradle.org/).

1. Replace Maven plugins with Gradle equivalents.

In the case of [popular plugins](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:common_plugins), Gradle often has an equivalent plugin that you can use. You might also find that you can [replace a plugin with built-in Gradle functionality](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:unnecessary_plugins). As a last resort, you may need to reimplement a Maven plugin [via your own custom plugins and task types](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:custom_plugins).

The rest of this chapter looks in more detail at specific aspects of migrating a build from Maven to Gradle.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:build_lifecycle)[Understanding the build lifecycle](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:build_lifecycle)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven builds are based around the concept of [_build lifecycles_](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html) that consist of a set of fixed phases. This can be a challenge for users migrating to Gradle because the build lifecycle is [a new concept](https://docs.gradle.org/current/userguide/build_lifecycle_intermediate.html#build_lifecycle). Although it’s important to understand how Gradle builds fit into the structure of **initialization**, **configuration**, and **execution** phases, Gradle provides a helper feature that can mimic Maven’s phases: [_lifecycle tasks_](https://docs.gradle.org/current/userguide/organizing_tasks.html#sec:lifecycle_tasks).

This feature allow you to define your own "lifecycles" by creating no-action tasks that simply depend on the tasks you’re interested in. And to make the transition to Gradle easier for Maven users, the [Base Plugin](https://docs.gradle.org/current/userguide/base_plugin.html#sec:base_tasks) — applied by all the JVM language plugins like the [Java Library Plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html#java_library_plugin) — provides a set of lifecycle tasks that correspond to the main Maven phases.

Here is a list of some of the main Maven phases and the Gradle tasks that they map to:

`clean`
Use the `clean` task provided by the Base Plugin.

`compile`
Use the `classes` task provided by the [Java Plugin](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_tasks) and other JVM language plugins. This compiles all classes for all source files of all languages and also performs [resource filtering](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:filtering_resources) via the `processResources` task.

`test`
Use the `test` task provided by the Java Plugin. It runs the unit tests, and more specifically, the tests that make up the [`test` source set](https://docs.gradle.org/current/userguide/java_plugin.html#source_sets).

`package`
Use the `assemble` task provided by the Base Plugin. This builds whatever is the appropriate package for the project; for example, a JAR for Java libraries or a WAR for traditional Java webapps.

`verify`
Use the `check` task provided by the Base Plugin. This runs all verification tasks that are attached to it, which typically includes the unit tests, any static analysis tasks — such as [Checkstyle](https://docs.gradle.org/current/userguide/checkstyle_plugin.html#checkstyle_plugin) — and others. If you want to include integration tests, you will have to [configure these manually](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:integration_tests).

`install`
Use the `publishToMavenLocal` task provided by the [Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:tasks).

Note that Gradle builds don’t require you to "install" artifacts as you have access to more appropriate features like [inter-project dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies_basics.html#sec:project-dependencies) and [composite builds](https://docs.gradle.org/current/userguide/composite_builds.html#composite_builds). You should only use `publishToMavenLocal` for interoperating with Maven builds.

Gradle also allows you to resolve dependencies against the local Maven cache, as described in the [Declaring repositories](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:declaring_repos) section.

`deploy`
Use the `publish` task provided by the [Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:tasks) — making sure you switch from the older Maven Plugin (ID: `maven`) if your build is using that one. This will publish your package to all configured publication repositories. There are also tasks that allow you to publish to a single repository even when multiple ones are defined.

Note that the Maven Publish Plugin does not publish **source and Javadoc JARs**_by default_, but this can easily be activated as explained in [the guide for building java projects](https://docs.gradle.org/current/userguide/building_java_projects.html#sec:java_packaging).

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:automatic_conversion)[Performing an automatic conversion](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:automatic_conversion)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle’s [`init` task](https://docs.gradle.org/current/userguide/build_init_plugin.html#build_init_plugin) is typically used to create a new skeleton project, but you can also use it to convert an existing Maven build to Gradle automatically. Once Gradle is [installed on your system](https://docs.gradle.org/current/userguide/installation.html#installation), all you have to do is run the command

> gradle init

from the root project directory. This consists of parsing the existing POMs and generating the corresponding Gradle build scripts. Gradle will also create a settings script if you’re migrating a [multi-project build](https://docs.gradle.org/current/userguide/multi_project_builds.html#multi_project_builds).

You’ll find that the new Gradle build includes the following:

* All the custom repositories that are specified in the POM

* Your external and inter-project dependencies

* The appropriate plugins to build the project (limited to one or more of the [Maven Publish](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven), [Java](https://docs.gradle.org/current/userguide/java_plugin.html#java_plugin) and [War](https://docs.gradle.org/current/userguide/war_plugin.html#war_plugin) Plugins)

One thing to keep in mind is that assemblies are not automatically converted. This additional conversion will required some manual work. Options include:

* Using the [Distribution Plugin](https://docs.gradle.org/current/userguide/distribution_plugin.html#distribution_plugin)

* Using the [Java Library Distribution Plugin](https://docs.gradle.org/current/userguide/java_library_distribution_plugin.html#java_library_distribution_plugin)

* Using the [Application Plugin](https://docs.gradle.org/current/userguide/application_plugin.html#application_plugin)

* [Creating custom archive tasks](https://docs.gradle.org/current/userguide/working_with_files.html#sec:creating_archives_example)

* Using a suitable community plugin from the [Gradle Plugin Portal](https://plugins.gradle.org/)

If your Maven build does not have many plugins or custom steps, you can simply run

> gradle build

once the migration has completed. This will run the tests and produce the required artifacts automatically.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:migrating_deps)[Migrating dependencies](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:migrating_deps)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle’s dependency management system is more flexible than Maven’s, but it still supports the same concepts of repositories, declared dependencies, scopes ([dependency configurations](https://docs.gradle.org/current/userguide/dependency_configurations.html#sub:what-are-dependency-configurations) in Gradle), and transitive dependencies. In fact, Gradle works with Maven-compatible repositories which makes it easy to migrate your dependencies.

One notable difference between the two tools is in how they manage version conflicts. Maven uses a "closest" match algorithm, whereas Gradle picks the newest. Don’t worry though, you have a lot of control over which versions are selected, as documented in [Managing Transitive Dependencies](https://docs.gradle.org/current/userguide/dependency_constraints.html#dependency-constraints).

Over the following sections, we will show you how to migrate the most common elements of a Maven build’s dependency management information.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:declaring_deps)[Declaring dependencies](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:declaring_deps)

Gradle uses the same dependency identifier components as Maven: group ID, artifact ID and version. It also supports classifiers. All you need to do is substitute the identifier information for a dependency into Gradle’s syntax, which is described in the [Declaring Dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies.html#one-declaring-dependencies) chapter.

For example, consider this Maven-style dependency on Log4J:

```
<dependencies>
    <dependency>
        <groupId>log4j</groupId>
        <artifactId>log4j</artifactId>
        <version>1.2.12</version>
    </dependency>
</dependencies>
```

This dependency would look like the following in a Gradle build script:

Example 1. [Declaring a simple compile-time dependency](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-declaring-a-simple-compile-time-dependency)

`Kotlin``Groovy`

build.gradle

```
dependencies {
    implementation 'log4j:log4j:1.2.12'  (1)
}
```

**1**Attaches version 1.2.12 of Log4J to the `implementation` configuration (scope)

The string identifier takes the Maven values of `groupId`, `artifactId` and `version`, although Gradle refers to them as `group`, `module` and `version`.

The above example raises an obvious question: what is that `implementation` configuration? It’s one of the standard dependency configurations provided by the [Java Plugin](https://docs.gradle.org/current/userguide/java_plugin.html#tab:configurations) and is often used as a substitute for Maven’s default `compile` scope.

Several of the differences between Maven’s scopes and Gradle’s standard configurations come down to Gradle distinguishing between the dependencies required to build a module and the dependencies required to build a module that depends on it. Maven makes no such distinction, so published POMs typically include dependencies that consumers of a library don’t actually need.

Here are the main Maven dependency scopes and how you should deal with their migration:

`compile`
Gradle has two configurations that can be used in place of the `compile` scope: `implementation` and `api`. The former is available to any project that applies the Java Plugin, while `api` is only available to projects that specifically apply the [Java Library Plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html#java_library_plugin).

In most cases you should simply use the `implementation` configuration, particularly if you’re building an application or webapp. But if you’re building a library, you can learn about which dependencies should be declared using `api` in the section on [Building Java libraries](https://docs.gradle.org/current/userguide/building_java_projects.html#sec:building_java_libraries). Even more information on the differences between `api` and `implementation` is provided in the Java Library Plugin chapter linked above.

`runtime`
Use the `runtimeOnly` configuration.

`test`
Gradle distinguishes between those dependencies that are required to _compile_ a project’s tests and those that are only needed to _run_ them.

Dependencies required for test compilation should be declared against the `testImplementation` configuration. Those that are only required for running the tests should use `testRuntimeOnly`.

`provided`
Use the `compileOnly` configuration.

Note that the [War Plugin](https://docs.gradle.org/current/userguide/war_plugin.html#sec:war_dependency_management) adds `providedCompile` and `providedRuntime` dependency configurations. These behave slightly differently from `compileOnly` and simply ensure that those dependencies aren’t packaged in the WAR file. However, the dependencies are included on runtime and test runtime classpaths, so use these configurations if that’s the behavior you need.

`import`
The `import` scope is mostly used within `<dependencyManagement>` blocks and applies solely to POM-only publications. Read the section on [Using bills of materials](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:using_boms) to learn more about how to replicate this behavior.

You can also specify a regular dependency on a POM-only publication. In this case, the dependencies declared in that POM are treated as normal transitive dependencies of the build.

For example, imagine you want to use the `groovy-all` POM for your tests. It’s a POM-only publication that has its own dependencies listed inside a `<dependencies>` block. The appropriate configuration in the Gradle build looks like this:

Example 2. [Consuming a POM-only dependency](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-consuming-a-pom-only-dependency)

`Kotlin``Groovy`

build.gradle

```
dependencies {
    testImplementation 'org.codehaus.groovy:groovy-all:2.5.4'
}
```

The result of this will be that all `compile` and `runtime` scope dependencies in the `groovy-all` POM get added to the test runtime classpath, while only the `compile` scope dependencies get added to the test compilation classpath. Dependencies with other scopes will be ignored.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:declaring_repos)[Declaring repositories](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:declaring_repos)

Gradle allows you to retrieve declared dependencies from any Maven-compatible or Ivy-compatible repository. Unlike Maven, it has no default repository and so you have to declare at least one. In order to have the same behavior as your Maven build, just configure [Maven Central](https://docs.gradle.org/current/userguide/declaring_repositories_basics.html#sec:maven-central) in your Gradle build, like this:

Example 3. [Configuring the build to use Maven Central](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-configuring-the-build-to-use-maven-central)

`Kotlin``Groovy`

build.gradle

```
repositories {
    mavenCentral()
}
```

You can also use the `repositories {}` block to configure custom repositories, as described in the [Repository Types](https://docs.gradle.org/current/userguide/supported_repository_types.html#sec:maven-repo) chapter.

Lastly, Gradle allows you to resolve dependencies against the [local Maven cache/repository](https://docs.gradle.org/current/userguide/supported_repository_types.html#sec:maven-local). This helps Gradle builds interoperate with Maven builds, but it shouldn’t be a technique that you use if you don’t need that interoperability. If you want to share published artifacts via the filesystem, consider configuring a [custom Maven repository](https://docs.gradle.org/current/userguide/supported_repository_types.html#sec:maven-repo) with a `file://` URL.

You might also be interested in learning about Gradle’s own [dependency cache](https://docs.gradle.org/current/userguide/dependency_caching.html#sec:dependency-cache), which behaves more reliably than Maven’s and can be used safely by multiple concurrent Gradle processes.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:controlling_dep_versions)[Controlling dependency versions](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:controlling_dep_versions)

The existence of transitive dependencies means that you can very easily end up with multiple versions of the same dependency in your dependency graph. By default, Gradle will pick the newest version of a dependency in the graph, but that’s not always the right solution. That’s why it provides several mechanisms for controlling which version of a given dependency is resolved.

On a per-project basis, you can use:

* [Dependency constraints](https://docs.gradle.org/current/userguide/dependency_constraints.html#sec:adding-constraints-transitive-deps)

* [Bills of materials](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:using_boms) (Maven BOMs)

* [Overriding transitive versions](https://docs.gradle.org/current/userguide/dependency_versions.html#sec:enforcing-dependency-version)

If you want to ensure consistency of versions across all projects in a multi-project build, similar to how the `<dependencyManagement>` block in Maven works, you can use the [Java Platform Plugin](https://docs.gradle.org/current/userguide/java_platform_plugin.html#java_platform_plugin). This allows you declare a set of dependency constraints that can be applied to multiple projects. You can even publish the platform as a Maven BOM or using Gradle’s metadata format. See the plugin page for more information on how to do that, and in particular the section on [Consuming platforms](https://docs.gradle.org/current/userguide/java_platform_plugin.html#sec:java_platform_consumption) to see how you can apply a platform to other projects in the same build.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:excluding_deps)[Excluding transitive dependencies](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:excluding_deps)

Maven builds use exclusions to keep unwanted dependencies — or unwanted _versions_ of dependencies — out of the dependency graph. You can do the same thing with Gradle, but that’s not necessarily the _right_ thing to do. Gradle provides other options that may be more appropriate for a given situation, so you really need to understand _why_ an exclusion is in place to migrate it properly.

If you want to exclude a dependency for reasons unrelated to versions, then check out the section on [excluding transitive dependencies](https://docs.gradle.org/current/userguide/dependency_constraints.html#sec:adding-constraints-transitive-deps). It shows you how to attach an exclusion either to an entire configuration (often the most appropriate solution) or to a dependency. You can even easily apply an exclusion to all configurations.

If you’re more interested in controlling which version of a dependency is actually resolved, see the previous section.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:optional_deps)[Handling optional dependencies](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:optional_deps)

You are likely to encounter two situations regarding optional dependencies:

* Some of your transitive dependencies are declared as optional

* You want to declare some of your direct dependencies as optional in your project’s published POM

For the first scenario, Gradle behaves the same way as Maven and simply ignores any transitive dependencies that are declared as optional. They are not resolved and have no impact on the versions selected if the same dependencies appear elsewhere in the dependency graph as non-optional.

As for publishing dependencies as optional, Gradle provides a richer model called [feature variants](https://docs.gradle.org/current/userguide/how_to_create_feature_variants_of_a_library.html#feature_variants), which will let you declare the "optional features" your library provides.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:using_boms)[Using bills of materials (BOMs)](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:using_boms)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven allows you to share dependency constraints by defining dependencies inside a `<dependencyManagement>` section of a POM file that has a packaging type of `pom`. This special type of POM (a BOM) can then be imported into other POMs so that you have consistent library versions across your projects.

Gradle can use such BOMs for the same purpose, using a special dependency syntax based on [platform()](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html#org.gradle.api.artifacts.dsl.DependencyHandler:platform(java.lang.Object)) and [enforcedPlatform()](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html#org.gradle.api.artifacts.dsl.DependencyHandler:enforcedPlatform(java.lang.Object)) methods. You simply declare the dependency in the normal way, but wrap the dependency identifier in the appropriate method, as shown in this example that "imports" the Spring Boot Dependencies BOM:

Example 4. [Importing a BOM in a Gradle build](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-importing-a-bom-in-a-gradle-build)

`Kotlin``Groovy`

build.gradle

```
dependencies {
    implementation platform('org.springframework.boot:spring-boot-dependencies:1.5.8.RELEASE') (1)

    implementation 'com.google.code.gson:gson' (2)
    implementation 'dom4j:dom4j'
}
```

**1**Applies the Spring Boot Dependencies BOM
**2**Adds a dependency whose version is defined by that BOM

You can use this feature to apply the `<dependencyManagement>` information from any dependency’s POM to the Gradle build, even those that don’t have a packaging type of `pom`. Both `platform()` and `enforcedPlatform()` will ignore any dependencies declared in the `<dependencies>` block.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:multimodule_builds)[Migrating multi-module builds (project aggregation)](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:multimodule_builds)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven’s multi-module builds map nicely to Gradle’s [multi-project builds](https://docs.gradle.org/current/userguide/multi_project_builds.html#multi_project_builds). Try the corresponding [sample](https://docs.gradle.org/current/samples/sample_structuring_software_projects.html) to see how a basic multi-project Gradle build is set up.

To migrate a multi-module Maven build, simply follow these steps:

1. Create a settings script that matches the `<modules>` block of the root POM.

For example, this `<modules>` block:

```
<modules>
    <module>simple-weather</module>
    <module>simple-webapp</module>
</modules>
```

can be migrated by adding the following line to the settings script:

Example 5. [Declaring which projects are part of the build](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-declaring-which-projects-are-part-of-the-build)

`Kotlin``Groovy`

settings.gradle

```
rootProject.name = 'simple-multi-module'  (1)

include 'simple-weather', 'simple-webapp'  (2)
```    **1**Sets the name of the overall project
**2**Configures two subprojects as part of this build `$ ./gradlew projects` 

Projects:
------------------------------------------------------------
Root project 'simple-multi-module'
------------------------------------------------------------
Location: /home/user/gradle/samples
Project hierarchy:
Root project 'simple-multi-module'
+--- Project ':simple-weather'
\--- Project ':simple-webapp'
Project locations:
project ':simple-weather' - /simple-weather
project ':simple-webapp' - /simple-webapp
To see a list of the tasks of a project, run gradle <project-path>:tasks
For example, try running gradle :simple-weather:tasks

1.   Replace cross-module dependencies with [project dependencies](https://docs.gradle.org/current/userguide/declaring_dependencies_basics.html#sec:project-dependencies).

2.   Replicate project inheritance with [convention plugins](https://docs.gradle.org/current/userguide/sharing_build_logic_between_subprojects.html#sec:sharing_logic_via_convention_plugins).

This basically involves creating a root project build script that injects shared configuration into the appropriate subprojects.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:sub:sharing-versions)[Sharing versions across projects](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:sub:sharing-versions)

If you want to replicate the Maven pattern of having dependency versions declared in the `dependencyManagement` section of the root POM file, the best approach is to leverage the `java-platform` plugin. You will need to add a dedicated project for this and consume it in the regular projects of your build. See [the documentation](https://docs.gradle.org/current/userguide/java_platform_plugin.html#java_platform_plugin) for more details on this pattern.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:profiles_and_properties)[Migrating Maven profiles and properties](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:profiles_and_properties)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven allows you parameterize builds using properties of various sorts. Some are read-only properties of the project model, others are user-defined in the POM. It even allows you to treat system properties as project properties.

Gradle has a similar system of project properties, although it differentiates between those and system properties. You can, for example, define properties in:

*   the build script

*   a `gradle.properties` file in the root project directory

*   a `gradle.properties` file in the `$HOME/.gradle` directory

Those aren’t the only options, so if you are interested in finding out more about how and where you can define properties, check out the [Build Environment](https://docs.gradle.org/current/userguide/build_environment.html#build_environment) chapter.

One important piece of behavior you need to be aware of is what happens when the same property is defined in both the build script and one of the external properties files: the build script value takes precedence. Always. Fortunately, you can mimic the concept of profiles to provide overridable default values.

Which brings us to Maven profiles. These are a way to enable and disable different configurations based on environment, target platform, or any other similar factor. Logically, they are nothing more than limited `if` statements. And since Gradle has much more powerful ways to declare conditions, it does not need to have formal support for profiles (except in the POMs of dependencies). You can easily get the same behavior by combining conditions with secondary build scripts, as you’ll see.

Let’s say you have different deployment settings depending on the environment: local development (the default), a test environment, and production. To add profile-like behavior, you first create build scripts for each environment in the project root: `profile-default.gradle`, `profile-test.gradle`, and `profile-prod.gradle`. You can then conditionally apply one of those profile scripts based on a [project property](https://docs.gradle.org/current/userguide/build_environment.html#sec:project_properties) of your own choice.

The following example demonstrates the basic technique using a project property called `buildProfile` and profile scripts that simply initialize an [extra project property](https://docs.gradle.org/current/userguide/writing_build_scripts_intermediate.html#sec:extra_properties) called `message`:

Example 6. [Mimicking the behavior of Maven profiles in Gradle](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-mimicking-the-behavior-of-maven-profiles-in-gradle)

`Kotlin``Groovy`

build.gradle

```

if (!hasProperty('buildProfile')) ext.buildProfile = 'default'  (1)

apply from: "profile-${buildProfile}.gradle"  (2)

tasks.register('greeting') {
    // Store the message into a variable, because referencing extras from the task action
    // is not compatible with the configuration cache.
    def message = project.message
    doLast {
        println message  (3)
    }
}

```

profile-default.gradle

`ext.message = 'foobar'  (4)`

profile-test.gradle

`ext.message = 'testing 1 2 3'  (4)`

profile-prod.gradle

`ext.message = 'Hello, world!'  (4)`

**1**Checks for the existence of (Groovy) or binds (Kotlin) the `buildProfile` project property
**2**Applies the appropriate profile script, using the value of `buildProfile` in the script filename
**3**Prints out the value of the `message` extra project property
**4**Initializes the `message` extra project property, whose value can then be used in the main build script

With this setup in place, you can activate one of the profiles by passing a value for the project property you’re using — `buildProfile` in this case:

`$ ./gradlew gradle greeting`

`foobar`

`$ ./gradlew -PbuildProfile=test greeting`

`testing 1 2 3`

You’re not limited to checking project properties. You could also check environment variables, the JDK version, the OS the build is running on, or anything else you can imagine.

One thing to bear in mind is that high level condition statements make builds harder to understand and maintain, similar to the way they complicate object-oriented code. The same applies to profiles. Gradle offers you many better ways to avoid the extensive use of profiles that Maven often requires, for example by configuring multiple tasks that are variants of one another. See the `publishPubNamePublicationToRepoNameRepository` tasks created by the [Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:tasks).

For a lengthier discussion on working with Maven profiles in Gradle, look no further than [this blog post](https://blog.gradle.org/maven-pom-profiles).

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:filtering_resources)[Filtering resources](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:filtering_resources)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven has a phase called `process-resources` that has the goal `resources:resources` bound to it by default. This gives the build author an opportunity to perform variable substitution on various files, such as web resources, packaged properties files, etc.

The Java plugin for Gradle provides a `processResources` task to do the same thing. This is a [ProcessResources](https://docs.gradle.org/current/dsl/org.gradle.language.jvm.tasks.ProcessResources.html) task that copies files from the configured resources directory — `src/main/resources` by default — to an output directory. And as with any `ProcessResources` or `Copy` task, you can configure it to perform [file filtering](https://docs.gradle.org/current/userguide/working_with_files.html#filtering_files), [renaming](https://docs.gradle.org/current/userguide/working_with_files.html#sec:renaming_files), and [content filtering](https://docs.gradle.org/current/userguide/working_with_files.html#sec:filtering_files).

As an example, here’s a configuration that treats the source files as [Groovy `SimpleTemplateEngine`](https://docs.groovy-lang.org/docs/next/html/documentation/template-engines.html#_simpletemplateengine) templates, providing `version` and `buildNumber` properties to those templates:

`Kotlin``Groovy`

build.gradle

```

processResources {
    expand(version: version, buildNumber: currentBuildNumber)
}

```

See the API docs for [CopySpec](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html) to see all the options available to you.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:integration_tests)[Configuring integration tests](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:integration_tests)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many Maven builds incorporate integration tests of some sort, which Maven supports through an extra set of phases: `pre-integration-test`, `integration-test`, `post-integration-test`, and `verify`. It also uses the Failsafe plugin in place of Surefire so that failed integration tests don’t automatically fail the build (because you may need to clean up resources, such as a running application server).

This behavior is easy to replicate in Gradle with source sets, as explained in our chapter on [Testing in Java & JVM projects](https://docs.gradle.org/current/userguide/java_testing.html#sec:configuring_java_integration_tests). You can then configure a clean-up task, such as one that shuts down a test server for example, to always run after the integration tests regardless of whether they succeed or fail using [Task.finalizedBy()](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:finalizedBy(java.lang.Object[])).

If you really don’t want your integration tests to fail the build, then you can use the [Test.ignoreFailures](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html#org.gradle.api.tasks.testing.Test:ignoreFailures) setting described in the [Test execution](https://docs.gradle.org/current/userguide/java_testing.html#sec:test_execution) section of the Java testing chapter.

Source sets also give you a lot of flexibility on where you place the source files for your integration tests. You can easily keep them in the same directory as the unit tests or, more preferably, in a separate source directory like `src/integTest/java`. To support other types of tests, simple add more source sets and [Test](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) tasks.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:common_plugins)[Migrating common plugins](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:common_plugins)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Maven and Gradle share a common approach of extending the build through plugins. Although the plugin systems are very different beneath the surface, they share many feature-based plugins, such as:

*   Shade/Shadow

*   Jetty

*   Checkstyle

*   JaCoCo

*   AntRun (see further down)

Why does this matter? Because many plugins rely on standard Java conventions, migration is just a matter of replicating the configuration of the Maven plugin in Gradle. As an example, here’s a simple Maven Checkstyle plugin configuration:

```

...
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-checkstyle-plugin</artifactId>
  <version>2.17</version>
  <executions>
    <execution>
      <id>validate</id>
      <phase>validate</phase>
      <configuration>
        <configLocation>checkstyle.xml</configLocation>
        <encoding>UTF-8</encoding>
        <consoleOutput>true</consoleOutput>
        <failsOnError>true</failsOnError>
        <linkXRef>false</linkXRef>
      </configuration>
      <goals>
        <goal>check</goal>
      </goals>
    </execution>
  </executions>
</plugin>
...

```

Everything outside of the configuration block can safely be ignored when migrating to Gradle. In this case, the corresponding Gradle configuration is as follows:

Example 8. [Configuring the Gradle Checkstyle Plugin](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-configuring-the-gradle-checkstyle-plugin)

`Kotlin``Groovy`

build.gradle

```

checkstyle {
    config = resources.text.fromFile('checkstyle.xml', 'UTF-8')
    showViolations = true
    ignoreFailures = false
}

```

The Checkstyle tasks are automatically added as dependencies of the `check` task, which also includes `test`. If you want to ensure that Checkstyle runs before the tests, then just specify an ordering with the [mustRunAfter(…​)](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:mustRunAfter(java.lang.Object[])) method:

Example 9. [Controlling when the `checkstyle` task runs](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-controlling-when-the-checkstyle-task-runs)

`Kotlin``Groovy`

build.gradle

`test.mustRunAfter checkstyleMain, checkstyleTest`

As you can see, the Gradle configuration is often much shorter than the Maven equivalent. You also have a much more flexible execution model since you are no longer constrained by Maven’s fixed phases.

While migrating a project from Maven, don’t forget about source sets. These often provide a more elegant solution for handling integration tests or generated sources than Maven can provide, so you should factor them into your migration plans.

### [](https://docs.gradle.org/userguide/migrating_from_maven.html#ant_goals)[Ant goals](https://docs.gradle.org/userguide/migrating_from_maven.html#ant_goals)

Many Maven builds rely on the AntRun plugin to customize the build without the overhead of implementing a custom Maven plugin. Gradle has no equivalent plugin because Ant is a first-class citizen in Gradle builds, via the `ant` object. For example, you can use Ant’s Echo task like this:

Example 10. [Invoking Ant tasks](https://docs.gradle.org/userguide/migrating_from_maven.html#ex-invoking-ant-tasks)

`Kotlin``Groovy`

build.gradle

```

tasks.register('sayHello') {
    doLast {
        ant.echo message: 'Hello!'
    }
}

```

Even Ant properties and filesets are supported natively. To learn more, see [Using Ant from Gradle](https://docs.gradle.org/current/userguide/ant.html#ant).

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:unnecessary_plugins)[Understanding which plugins you don’t need](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:unnecessary_plugins)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It’s worth remembering that Gradle builds are typically easier to extend and customize than Maven ones. In this context, that means you may not need a Gradle plugin to replace a Maven one. For example, the Maven Enforcer plugin allows you to control dependency versions and environmental factors, but these things can easily be configured in a normal Gradle build script.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:custom_plugins)[Dealing with uncommon and custom plugins](https://docs.gradle.org/userguide/migrating_from_maven.html#migmvn:custom_plugins)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You may come across Maven plugins that have no counterpart in Gradle, particularly if you or someone in your organisation has written a custom plugin. Such cases rely on you understanding how Gradle (and potentially Maven) works, because you will usually have to write your own plugin.

For the purposes of migration, there are two key types of Maven plugins:

*   Those that use the Maven project object.

*   Those that don’t.

Why is this important? Because if you use one of the latter, you can trivially reimplement it as a [custom Gradle task type](https://docs.gradle.org/current/userguide/custom_tasks.html#custom_tasks). Simply define task inputs and outputs that correspond to the mojo parameters and convert the execution logic into a task action.

If a plugin depends on the Maven project, then you will have to rewrite it. Don’t start by considering how the Maven plugin works, but look at what problem it is trying to solve. Then try to work out how to solve that problem in Gradle. You will probably find that the two build models are different enough that "transcribing" Maven plugin code into a Gradle plugin just won’t be effective. On the plus side, the plugin is likely to be much easier to write than the original Maven one because Gradle has a much richer build model and API.

If you do need to implement custom logic, either via build scripts or plugins, check out the [Guides related to plugin development](https://gradle.org/guides/?q=Plugin%20Development). Also be sure to familiarize yourself with Gradle’s [Groovy DSL Reference](https://docs.gradle.org/current/dsl/), which provides comprehensive documentation on the API that you’ll be working with. It details the standard configuration blocks (and the objects that back them), the core types in the system (`Project`, `Task`, etc.), and the standard set of task types. The main entry point is the [Project](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html) interface as that’s the top-level object that backs the build scripts.

[](https://docs.gradle.org/userguide/migrating_from_maven.html#further_reading)[Further reading](https://docs.gradle.org/userguide/migrating_from_maven.html#further_reading)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This chapter has covered the major topics that are specific to migrating Maven builds to Gradle. All that remain are a few other areas that may be useful during or after a migration:

*   Learn how to configure Gradle’s [build environment](https://docs.gradle.org/current/userguide/build_environment.html#build_environment), including the JVM settings used to run it

*   Learn how to [structure your builds effectively](https://docs.gradle.org/current/userguide/organizing_gradle_projects.html#organizing_gradle_projects)

*   [Configure Gradle’s logging](https://docs.gradle.org/current/userguide/logging.html#logging) and use it from your builds

As a final note, this guide has only touched on a few of Gradle’s features and we encourage you to learn about the rest from the other chapters of the user manual and from our [step-by-step samples](https://docs.gradle.org/current/samples/index.html).
