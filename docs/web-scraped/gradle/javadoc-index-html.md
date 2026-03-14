# Source: https://docs.gradle.org/javadoc/index.html?overview-summary.html

Title: Overview (Gradle API 9.4.0)

URL Source: https://docs.gradle.org/javadoc/index.html?overview-summary.html

Markdown Content:
The top-level package for the Gradle build system.

Gradle's build language API, which is available from your build files.

Classes for declaring and using artifacts and artifact dependencies.

Classes related to requesting and providing capabilities of variants.

Classes that provide meta-data about software components.

Classes used in the artifact DSL.

Classes for declaring and using Ivy modules.

Classes for declaring and using Maven modules.

Classes used for querying the artifacts.

Classes for declaring and using artifact repositories.

Classes that compose the resolution result

Provides classes, interfaces and annotations for registering and implementing artifact transforms.

Types related to artifact type definitions.

Dependency verification related configuration classes

Classes for dealing with configuration and artifact attributes.

Attributes specific to the Java ecosystem.

Attributes specific to Gradle's plugin system.

Classes for configuring cache-related components.

Classes for dealing with capabilities.

Types for declaring and using Software Components.

Classes related to build configuration.

general credentials related classes.

The main interfaces and classes of the distribution plugin.

The distribution plugin itself.

Classes for managing and monitoring build execution.

Classes for working with files.

Gradle Flow API.

Classes for managing and monitoring build initialization.

Types related to the build definition for included builds.

Classes used in the initialization DSL.

Classes for managing cross-project dependency resolution.

Classes for invoking and monitoring gradle builds.

Classes for working with JAR manifests.

Interfaces for configuring the Java Platform Module System (JPMS).

Interfaces for configuring the cli client.

Classes for managing logging in Gradle.

Classes for logging configuration.

Classes that operate on the Gradle model.

The standard [`Plugin`](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html "interface in org.gradle.api") implementations.

A [`Plugin`](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html "interface in org.gradle.api") for generating parsers from Antlr grammars.

Dependency modifiers that can access platform and enforced platforms in `dependencies` blocks.

Plugins which measure and enforce code quality.

A [`Plugin`](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html "interface in org.gradle.api") which compiles and tests Scala sources.

new Problems API

The interfaces for value providers.

Classes that deal with publishing artifacts.

Types that deal with publishing in the Ivy format.

Plugins for Ivy publishing.

Tasks for Ivy publishing.

Types that deal with publishing in the Maven format.

Plugins for publishing in the Maven format.

Tasks for publishing in the Maven format.

Publishing plugin.

Tasks used for publishing to a binary repository.

Classes and API for the reflection and types.

Classes for reporting

Reporting components used by software reports.

Types responsible for generating dependency reports.

Types representing dependent components and rendered for them.

Configuration model reporting tasks.

Plugins for reporting

Interfaces and API for the 'Resources' concept.

Types for defining and using build services.

Classes for defining general purpose criteria.

The standard [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

The Ant integration [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

Tasks for creating and running java applications.

The archive bundling [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

The compilation [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

The diagnostic [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

Diagnostic tasks which report information about configurations.

API classes for implementing incremental tasks.

The documentation generation [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

Annotations for exposing task properties as command line options.

The unit testing [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html "interface in org.gradle.api") implementations.

JUnit specific testing classes.

Types related to logging of test related information to the console.

Defines different test sources that can be associated to tests.

TestNG specific testing classes.

Utility classes used by the standard task implementations.

APIs to influence how toolchains are resolved.

Classes related to transport authentication protocols.

Classes related to transport authentication protocols for S3.

Classes related to transport authentication protocols for HTTP.

Types for receiving build events.

Public types for updating the Gradle Daemon JVM criteria.

Build init plugins and tasks.

Build init plugins.

Provides the API that plugins can use to contribute additional types of builds to the `init` task.

Build init plugins.

Classes for build caches and for types to extend build cache functionality.

Classes for configuring build caches.

Classes for HTTP build cache service.

Classes for local build cache services.

Classes related to Gradle parallelism and concurrency.

Classes to run Javadoc.

Model classes for visual studio.

Plugins for Visual Studio integration.

Task classes for visual studio.

Model classes for XCode.

Plugins for XCode integration.

Task classes for XCode.

Component types for Ivy modules.

Types for support of JVM runtime.

Classes that enable JVM application script generation.

Tasks for the JVM application plugin.

Tasks that add support for JVM runtime.

Defines tools and configuration options that can build things that run on the JVM.

Model classes for managing language sources.

Model classes for building from Assembler language sources.

Plugins for building from Assembler language sources.

Tasks for assembling Assembler sources for a native runtime.

General purpose types for language support.

Classes representing artifacts relevant to languages in general.

General purpose types for related to compiling.

Base plugins for language support.

General purpose types for language sources support.

Model classes for building from C language sources.

Plugins for building from C language sources.

Tasks for compiling C sources for a native runtime.

Model classes for building from C++ language sources.

Plugins for building from C++ language sources.

Tasks for compiling C++ sources for a native runtime.

Classes representing artifacts relevant to the Java language.

Tasks for support for JVM languages.

Model classes for managing language sources.

Base classes for native language compile tasks.

Model classes for building from Objective-C language sources.

Plugins for building from Objective-C language sources.

Tasks for compiling Objective-C sources for a native runtime.

Model classes for building from Objective-C++ language sources.

Plugins for building from Objective-C++ language sources.

Tasks for compiling Objective-C++ sources for a native runtime.

Base plugins for the native languages.

Model classes for building from Windows Resource scripts.

Plugins for building from Windows Resource scripts.

Tasks for compiling Windows resources for a native runtime.

Tasks that add support for Scala language.

Model classes for building from Swift language sources.

Plugins for building from Swift language sources.

Tasks for compiling Swift sources for a native runtime.

Component types for Maven modules.

Classes that operate upon the Gradle model.

Classes that model aspects of native component projects.

Classes that allow defining a native binary platform.

Plugins for building native component projects.

Tasks for building native component projects.

API classes for testing native binaries.

API classes for C++ test integration.

Plugins for C++ test integration.

API classes for cunit integration.

Plugins for cunit testing.

Tasks for cunit integration.

API classes for Google Test integration.

Plugins for Google Test testing.

Plugin classes for generic support for testing native binaries.

Tasks for test execution.

Model classes for the XCTest plugins.

Plugins for XCTest testing.

Tasks for XCTest execution.

Classes that allow C++ tool chains to be configured.

Built-in tool chain support.

Interfaces and API for input normalization.

Types to define build environment.

General purpose types for runtime support.

General purpose types for binary support.

General purpose types for library support.

Base plugins for software model support.

Classes for assisting with plugin development.

Plugins for assisting with plugin development.

Tasks for assisting with plugin development.

APIs to influence how plugins are resolved.

Classes for managing plugin resolution and use.

Support for generating EAR archives in a Gradle build

Classes for working with EAR deployment descriptors.

General purpose IDE types.

General ide plugin api.

A [`Plugin`](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html "interface in org.gradle.api") for generating Eclipse files.

Classes for the model used by the eclipse plugins.

A [`Plugin`](https://docs.gradle.org/current/javadoc/org/gradle/api/Plugin.html "interface in org.gradle.api") for generating IDEA files.

The signing plugin.

The signing plugin signatory types.

PGP signing support.

The signing plugin signature types.

PGP signing support.

Classes for executing system and Java processes.

Model classes that describe a Swift Package Manager package.

Plugins that produce Swift Package Manager manifests from the Gradle model.

Tasks that produce Swift Package Manager manifests from the Gradle model.

Classes and interfaces for testing custom task and plugin implementations.

General purpose types for test suite support.

Plugin classes for generic support for testing.

Plugins to work with the JaCoCo code coverage library.

Tasks to work with the JaCoCo code coverage library.

Implementations for Jacoco code coverage rules.

Support for executing contrived Gradle builds for the purpose of testing build logic.

The main interfaces and classes of the Gradle tooling API.

The interfaces and classes related to registering for event notifications and listening to dispatched events.

Project configuration specific interfaces and classes related to event notifications.

File download specific interfaces and classes related to event notifications.

Build lifecycle interfaces and classes related to event notifications.

Problem specific interfaces and classes related to event notifications.

Task execution specific interfaces and classes related to event notifications.

Task execution result interfaces specific to Java projects.

Test execution specific interfaces and classes related to event notifications.

Defines Tooling API client types for different test sources that can be associated to tests.

Artifact transform execution specific interfaces and classes related to event notifications.

Work item execution specific interfaces and classes related to event notifications.

Exceptions thrown when using the tooling API.

The general-purpose tooling model types, provided by the tooling API.

Tooling models for the build environment, which includes information such as Gradle or Java versions.

Types that represent the tooling model for C++ projects.

Generic DSL related tooling models.

Eclipse-centric tooling models.

The tooling models for Gradle builds and projects.

IntelliJ IDEA centric tooling models.

Java-specific details for tooling models.

Kotlin DSL related tooling models.

Interfaces and classes that allow tooling models to be made available to the tooling API client.

Contains Gradle utility classes.

Packages for version control systems.

The API for dealing with Version Control Systems in Gradle.

Classes used for implementing units of work.

Workers allow running pieces of work in the background, either in-process in isolated classloaders or out-of-process in reusable daemons.
