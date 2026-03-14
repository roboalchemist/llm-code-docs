# Source: https://docs.gradle.org/userguide/plugins.html

Title: Introduction to Plugins

URL Source: https://docs.gradle.org/userguide/plugins.html

Markdown Content:
Introduction to Plugins
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* [](https://docs.gradle.org/userguide/plugins.html "Theme")
* Build Tool [Releases](https://gradle.org/releases) [Features](https://gradle.org/features) [9.0.0 Highlights](https://gradle.org/whats-new/gradle-9) [8.0.0 Highlights](https://gradle.org/whats-new/gradle-8) [Gradle vs Maven](https://gradle.org/maven-and-gradle)  
* Learn [User Manual](https://docs.gradle.org/) [DPE University](https://dpeuniversity.gradle.com/) [YouTube Channel](https://www.youtube.com/channel/UCvClhveoEjokKIuBAsSjEwQ) [Events and Webinars](https://gradle.com/training/)  
* Support [Community Slack](https://gradle.org/slack-invite) [Community Forums](https://discuss.gradle.org/) [Professional Services](https://gradle.org/services)  
* News [Newsletter](https://newsletter.gradle.org/) [Blog](https://blog.gradle.org/)  
* Gradle Technologies [Develocity®](https://gradle.com/develocity/) [Build Scan®](https://scans.gradle.com/) [DPE.org](https://dpe.org/) [Careers](https://gradle.com/careers)  
* About [Contact Us](https://gradle.org/contact) [Gradle Fellowship](https://gradle.org/fellowship)  
* [](https://github.com/gradle/gradle "Gradle on GitHub")

Search

### [Gradle User Manual](https://docs.gradle.org/userguide/userguide.html)

* [Getting Started](https://docs.gradle.org/userguide/getting_started.html)

### Gradle Tutorials

* [Beginner Tutorial](https://docs.gradle.org/userguide/plugins.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/plugins.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/plugins.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_plugin.html)
  * [2. Adding an Extension](https://docs.gradle.org/userguide/part2_add_extension.html)
  * [3. Creating a Custom Task](https://docs.gradle.org/userguide/part3_create_custom_task.html)
  * [4. Writing a Unit Test](https://docs.gradle.org/userguide/part4_unit_test.html)
  * [5. Adding a DataFlow Action](https://docs.gradle.org/userguide/part5_add_dataflow_action.html)
  * [6. Writing a Functional Test](https://docs.gradle.org/userguide/part6_functional_test.html)
  * [7. Using a Consumer Project](https://docs.gradle.org/userguide/part7_use_consumer_project.html)
  * [8. Publish the Plugin](https://docs.gradle.org/userguide/part8_publish_locally.html)

### Gradle Releases

* [All Releases](https://gradle.org/releases/)
* [Release Notes](https://docs.gradle.org/release-notes.html)
* [Installing Gradle](https://docs.gradle.org/userguide/installation.html)
* [Upgrading Gradle](https://docs.gradle.org/userguide/plugins.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/plugins.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/plugins.html#running-introduction)
  * [1. Core Concepts](https://docs.gradle.org/userguide/gradle_basics.html)
  * [2. Wrapper Basics](https://docs.gradle.org/userguide/gradle_wrapper_basics.html)
  * [3. CLI Basics](https://docs.gradle.org/userguide/command_line_interface_basics.html)
  * [4. Settings File Basics](https://docs.gradle.org/userguide/settings_file_basics.html)
  * [5. Build File Basics](https://docs.gradle.org/userguide/build_file_basics.html)
  * [6. Dependencies Basics](https://docs.gradle.org/userguide/dependency_management_basics.html)
  * [7. Tasks Basics](https://docs.gradle.org/userguide/task_basics.html)
  * [8. Caching Basics](https://docs.gradle.org/userguide/gradle_optimizations.html)
  * [9. Plugins Basics](https://docs.gradle.org/userguide/plugin_basics.html)
  * [10. Build Scan Basics](https://docs.gradle.org/userguide/build_scans.html)

* [Writing Build Scripts](https://docs.gradle.org/userguide/plugins.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/plugins.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/plugins.html#gradle-core)
  * [Command-Line Interface](https://docs.gradle.org/userguide/command_line_interface.html)
  * [Logging and Output](https://docs.gradle.org/userguide/logging.html)
  * [Gradle Wrapper](https://docs.gradle.org/userguide/gradle_wrapper.html)
  * [Gradle Daemon](https://docs.gradle.org/userguide/gradle_daemon.html)
  * [Gradle Directories](https://docs.gradle.org/userguide/directory_layout.html)
  * [Build Configuration](https://docs.gradle.org/userguide/build_environment.html)
  * [Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle.html)
  * [Build Scan](https://docs.gradle.org/userguide/inspect.html)
  * [Continuous Builds](https://docs.gradle.org/userguide/continuous_builds.html)
  * [File System Watching](https://docs.gradle.org/userguide/file_system_watching.html)

* [DSLs and APIs](https://docs.gradle.org/userguide/plugins.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/plugins.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/plugins.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/plugins.html#plugin-development)
  * [Introduction to Plugins](https://docs.gradle.org/userguide/plugins.html)
  * [Precompiled Script Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html)
  * [Convention Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_convention.html)
  * [Binary Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html)
  * [Testing Plugins](https://docs.gradle.org/userguide/testing_gradle_plugins.html)
  * [Preparing to Publish](https://docs.gradle.org/userguide/preparing_to_publish.html)
  * [Publishing Plugins](https://docs.gradle.org/userguide/publishing_gradle_plugins.html)
  * [Reporting Plugin Problems](https://docs.gradle.org/userguide/reporting_problems.html)
  * [Initialization Scripts & Init Plugins](https://docs.gradle.org/userguide/init_scripts.html)
  * [Testing with TestKit](https://docs.gradle.org/userguide/test_kit.html)
  * [Core Plugins](https://docs.gradle.org/userguide/plugin_reference.html)

* [Dependencies](https://docs.gradle.org/userguide/plugins.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/plugins.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/plugins.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/plugins.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/plugins.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/plugins.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/plugins.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/plugins.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/plugins.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/plugins.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/plugins.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/plugins.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/plugins.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/plugins.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/plugins.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/plugins.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/plugins.html#advanced-topics)
  * [Using Ant from Gradle](https://docs.gradle.org/userguide/ant.html)

### Structuring Gradle Builds

* [Organizing Projects](https://docs.gradle.org/userguide/organizing_gradle_projects.html)
* [Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds.html)
* [Sharing Build Logic](https://docs.gradle.org/userguide/sharing_build_logic_between_subprojects.html)
* [Composite Builds](https://docs.gradle.org/userguide/composite_builds.html)
* [Configuration on Demand](https://docs.gradle.org/userguide/configuration_on_demand.html)
* [Isolated Projects](https://docs.gradle.org/userguide/isolated_projects.html)

### Optimizing Gradle Builds

* [Improving Performance](https://docs.gradle.org/userguide/performance.html)
* [Build Cache](https://docs.gradle.org/userguide/plugins.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/plugins.html#configuration-cache)
  * [How it Works](https://docs.gradle.org/userguide/configuration_cache.html)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/configuration_cache_enabling.html)
  * [Requirements for your Build Logic](https://docs.gradle.org/userguide/configuration_cache_requirements.html)
  * [Debugging and Troubleshooting](https://docs.gradle.org/userguide/configuration_cache_debugging.html)
  * [Status](https://docs.gradle.org/userguide/configuration_cache_status.html)

### Securing Gradle Builds

* [Supply Chain Security](https://docs.gradle.org/userguide/security.html)
* [Verifying Dependencies](https://docs.gradle.org/userguide/dependency_verification.html)

### IDE & Tool Integration

* [Third-party Tools](https://docs.gradle.org/userguide/third_party_integration.html)
* [APIs](https://docs.gradle.org/userguide/plugins.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/plugins.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/plugins.html#how-to)
  * [How to Downgrade Transitive Dependencies](https://docs.gradle.org/userguide/how_to_downgrade_transitive_dependencies.html)
  * [How to Upgrade Transitive Dependencies](https://docs.gradle.org/userguide/how_to_upgrade_transitive_dependencies.html)
  * [How to Exclude Transitive Dependencies](https://docs.gradle.org/userguide/how_to_exclude_transitive_dependencies.html)
  * [How to Prevent Accidental or Eager Dependency Upgrades](https://docs.gradle.org/userguide/how_to_prevent_accidental_dependency_upgrades.html)
  * [How to Align Dependency Versions](https://docs.gradle.org/userguide/how_to_align_dependency_versions.html)
  * [How to Share Outputs Between Projects](https://docs.gradle.org/userguide/how_to_share_outputs_between_projects.html)
  * [How to Resolve Specific Artifacts from a Module Dependency](https://docs.gradle.org/userguide/how_to_resolve_specific_artifacts.html)
  * [How to Use a Local Fork of a Module Dependency](https://docs.gradle.org/userguide/how_to_use_local_forks.html)
  * [How to Fix Version Catalog Problems](https://docs.gradle.org/userguide/how_to_fix_version_catalog_problems.html)
  * [How to Create Feature Variants of a Library](https://docs.gradle.org/userguide/how_to_create_feature_variants_of_a_library.html)

### More Resources

* [Samples](https://docs.gradle.org/samples/index.html)
* [Glossary](https://docs.gradle.org/userguide/glossary.html)
* [Single Page Version](https://docs.gradle.org/userguide/userguide_single.html)

Introduction to Plugins
=======================

version 9.4.0

On this Page

* [Sources for Plugins](https://docs.gradle.org/userguide/plugins.html#sources_for_plugins)
  * [Core Plugins](https://docs.gradle.org/userguide/plugins.html#core_plugins)
  * [Community Plugins](https://docs.gradle.org/userguide/plugins.html#community_plugins)
  * [Local or Custom Plugins](https://docs.gradle.org/userguide/plugins.html#local_or_custom_plugins)

* [Types of Plugins](https://docs.gradle.org/userguide/plugins.html#types_of_plugins)
  * [Script plugins](https://docs.gradle.org/userguide/plugins.html#sec:build_script_plugins)
  * [Precompiled script plugins](https://docs.gradle.org/userguide/plugins.html#sec:precompile_script_plugin)
  * [Convention plugins](https://docs.gradle.org/userguide/plugins.html#sec:convention_plugins)
  * [Binary plugins](https://docs.gradle.org/userguide/plugins.html#sec:custom_plugins_standalone_project)

* [Scope of Plugins](https://docs.gradle.org/userguide/plugins.html#project_vs_settings_vs_init_plugins)

Gradle comes with a set of powerful core systems such as dependency management, task execution, and project configuration. But everything else it can do is supplied by plugins.

Plugins encapsulate logic for specific tasks or integrations, such as compiling code, running tests, or deploying artifacts. By applying plugins, users can easily add new features to their build process without having to write complex code from scratch.

This plugin-based approach allows Gradle to be lightweight and modular. It also promotes code reuse and maintainability, as plugins can be shared across projects or within an organization.

Before reading this chapter, it’s recommended that you first complete the [Advanced Tutorial and Reading](https://docs.gradle.org/userguide/plugin_introduction_advanced.html#plugin_introduction_advanced).

[](https://docs.gradle.org/userguide/plugins.html#sources_for_plugins)[Sources for Plugins](https://docs.gradle.org/userguide/plugins.html#sources_for_plugins)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Plugins can be sourced from Gradle or the Gradle community. But when users want to organize their build logic or need specific build capabilities not provided by existing plugins, they can develop their own.

As such, we distinguish between three different sources for Gradle plugins:

1. **Core Plugins** - plugins that come from Gradle itself.

2. **Community Plugins** - plugins that come from the [Gradle Plugin Portal](https://plugins.gradle.org/) or a public repository.

3. **Local or Custom Plugins** - plugins that you develop yourself.

### [](https://docs.gradle.org/userguide/plugins.html#core_plugins)[Core Plugins](https://docs.gradle.org/userguide/plugins.html#core_plugins)

The term **core plugin** refers to a plugin that is part of the Gradle distribution such as the [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html#java_library_plugin). They are always available.

### [](https://docs.gradle.org/userguide/plugins.html#community_plugins)[Community Plugins](https://docs.gradle.org/userguide/plugins.html#community_plugins)

The term **community plugin** refers to a plugin published to the Gradle Plugin Portal (or another public repository) such as the [Spotless Plugin](https://plugins.gradle.org/plugin/com.diffplug.gradle.spotless).

### [](https://docs.gradle.org/userguide/plugins.html#local_or_custom_plugins)[Local or Custom Plugins](https://docs.gradle.org/userguide/plugins.html#local_or_custom_plugins)

The term **local plugin** or **custom plugin** refers to a plugin you write yourself for your own build.

[](https://docs.gradle.org/userguide/plugins.html#types_of_plugins)[Types of Plugins](https://docs.gradle.org/userguide/plugins.html#types_of_plugins)
------------------------------------------------------------------------------------------------------------------------------------------------------

There are three types of **plugins** you can develop:

| # | Type | Location: | Most likely: | Benefit: |
| --- | --- | --- | --- | --- |
| [1](https://docs.gradle.org/userguide/plugins.html#sec:build_script_plugins) | [Script plugins](https://docs.gradle.org/userguide/plugins.html#sec:build_script_plugins) | A `.gradle(.kts)` script file | A local plugin | The plugin is automatically compiled and included in the classpath of the build script. |
| [2](https://docs.gradle.org/userguide/plugins.html#sec:precompile_script_plugin) | [Precompiled script plugins](https://docs.gradle.org/userguide/plugins.html#sec:precompile_script_plugin) | [`buildSrc`](https://docs.gradle.org/userguide/sharing_build_logic_between_subprojects.html#sec:using_buildsrc) folder or [composite](https://docs.gradle.org/userguide/composite_builds.html#composite_builds) build | A convention plugin | The plugin is automatically compiled, tested, and available on the classpath of the build script. The plugin is visible to every build script used by the build. |
| [3](https://docs.gradle.org/userguide/plugins.html#sec:custom_plugins_standalone_project) | [Binary plugins](https://docs.gradle.org/userguide/plugins.html#sec:custom_plugins_standalone_project) | Standalone project | A shared plugin | The plugin JAR is produced and can be published. The plugin can be used in multiple builds and shared with others. |

### [](https://docs.gradle.org/userguide/plugins.html#sec:build_script_plugins)[Script plugins](https://docs.gradle.org/userguide/plugins.html#sec:build_script_plugins)

A **script plugin** is a plugin written directly in a build file (`.gradle` or `.gradle.kts`). They are usually small, local utilities for one project and not intended for reuse.

Script plugins are useful for quick experiments but **not recommended** for production builds. They often evolve into proper plugins placed in `buildSrc` or published as standalone plugins.

The simplest plugin is a class that implements [`Plugin<Project>`](https://docs.gradle.org/javadoc/org/gradle/api/Plugin.html) and configures the project when applied:

[![Image 5: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/customPlugins/customPlugin)

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
class GreetingPlugin : Plugin<Project> {
    override fun apply(project: Project) {
        project.task("hello") {
            doLast {
                println("Hello from the GreetingPlugin")
            }
        }
    }
}

// Apply the plugin
apply<GreetingPlugin>()
```

build.gradle

```groovy
class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        project.task('hello') {
            doLast {
                println 'Hello from the GreetingPlugin'
            }
        }
    }
}

// Apply the plugin
apply plugin: GreetingPlugin
```

```bash
./gradlew -q hello
```

```text
Hello from the GreetingPlugin
```

You can also put such a plugin in a separate script file and apply it with `apply(from = "other.gradle.kts")` or `apply from: 'other.gradle'`:

```option
Kotlin
```

```option
Groovy
```

other.gradle.kts

```kotlin
class GreetingScriptPlugin : Plugin<Project> {
    override fun apply(project: Project) {
        project.task("hi") {
            doLast {
                println("Hi from the GreetingScriptPlugin")
            }
        }
    }
}

// Apply the plugin
apply<GreetingScriptPlugin>()
```

other.gradle

```groovy
class GreetingScriptPlugin implements Plugin<Project> {
    void apply(Project project) {
        project.task('hi') {
            doLast {
                println 'Hi from the GreetingScriptPlugin'
            }
        }
    }
}

// Apply the plugin
apply plugin: GreetingScriptPlugin
```

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
apply(from = "other.gradle.kts")
```

build.gradle

```groovy
apply from: 'other.gradle'
```

```bash
./gradlew -q hi
```

```text
Hi from the GreetingScriptPlugin
```

**Script plugins should be avoided.** Script plugins are convenient for local, throwaway logic but make builds harder to maintain.

### [](https://docs.gradle.org/userguide/plugins.html#sec:precompile_script_plugin)[Precompiled script plugins](https://docs.gradle.org/userguide/plugins.html#sec:precompile_script_plugin)

**Precompiled script plugins** are compiled into class files and packaged into a JAR before they are executed. These plugins use the Gradle DSLs instead of pure Java, Kotlin, or Groovy.

To create a precompiled script plugin, you can:

1. Use [Gradle’s Kotlin DSL](https://docs.gradle.org/userguide/kotlin_dsl.html#kotdsl:kotlin_dsl) - The plugin is a `.gradle.kts` file, and applies `id("kotlin-dsl")`.

2. Use [Gradle’s Groovy DSL](https://docs.gradle.org/userguide/groovy_build_script_primer.html#groovy_build_script_primer) - The plugin is a `.gradle` file, and apply `id("groovy-gradle-plugin")`.

To apply a precompiled script plugin, you need to know its ID. The ID is derived from the plugin script’s filename and its (optional) package declaration.

For example, the script `src/main/kotlin/some-java-library.gradle.kts` has a plugin ID of `some-java-library` (assuming it has no package declaration). Likewise, `src/main/kotlin/my/some-java-library.gradle(.kts)` has a plugin ID of `my.some-java-library` as long as it has a package declaration of `my`.

Precompiled script plugin names have two important limitations:

* They cannot start with `org.gradle`.

* They cannot have the same name as a [core plugin](https://docs.gradle.org/userguide/plugin_reference.html#plugin_reference).

When the plugin is applied to a project, Gradle creates an instance of the plugin class and calls the instance’s [`Plugin.apply()`](https://docs.gradle.org/javadoc/org/gradle/api/Plugin.html#apply-T-) method.

Let’s rewrite the `GreetingPlugin` script plugin as a precompiled script plugin. The script plugin is moved to its own file in `buildSrc`:

[![Image 6: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/greetingPlugin)

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/GreetingPlugin.gradle.kts

```kotlin
tasks.register("hello") {
    doLast {
        println("Hello from the convention GreetingPlugin")
    }
}
```

buildSrc/src/main/groovy/GreetingPlugin.gradle

```groovy
tasks.register("hello") {
    doLast {
        println("Hello from the convention GreetingPlugin")
    }
}
```

The `GreetingPlugin` can now be applied in other subprojects' builds by using its ID:

```option
Kotlin
```

```option
Groovy
```

app/build.gradle.kts

```kotlin
plugins {
    application
    id("GreetingPlugin")
}
```

app/build.gradle

```groovy
plugins {
    id 'application'
    id('GreetingPlugin')
}
```

```bash
./gradlew -q hello
```

```text
Hello from the convention GreetingPlugin
```

### [](https://docs.gradle.org/userguide/plugins.html#sec:convention_plugins)[Convention plugins](https://docs.gradle.org/userguide/plugins.html#sec:convention_plugins)

A **convention plugin** is typically a precompiled script plugin that configures existing core and community plugins with your own conventions (i.e. default values) such as setting the Java version by using `java.toolchain.languageVersion = JavaLanguageVersion.of(17)`.

Convention plugins are also used to enforce project standards and help streamline the build process. They can apply and configure plugins, create new tasks and extensions, set dependencies, and much more.

Let’s take an example build with three subprojects: one for `data-model`, one for `database-logic` and one for `app` code. The project has the following structure:

```text
.
├── buildSrc
│   ├── src
│   │   └──...
│   └── build.gradle.kts
├── data-model
│   ├── src
│   │   └──...
│   └── build.gradle.kts
├── database-logic
│   ├── src
│   │   └──...
│   └── build.gradle.kts
├── app
│   ├── src
│   │   └──...
│   └── build.gradle.kts
└── settings.gradle.kts
```

The build file of the `database-logic` subproject is as follows:

[![Image 7: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/pluginProject)

```option
Kotlin
```

```option
Groovy
```

database-logic/build.gradle.kts

```kotlin
plugins {
    id("java-library")
    id("org.jetbrains.kotlin.jvm") version "2.3.0"
}

repositories {
    mavenCentral()
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(11))
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(11)
}

// More build logic
```

database-logic/build.gradle

```groovy
plugins {
    id 'java-library'
    id 'org.jetbrains.kotlin.jvm' version '2.3.0'
}

repositories {
    mavenCentral()
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(11))
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain {
        languageVersion.set(JavaLanguageVersion.of(11))
    }
}

// More build logic
```

We apply the `java-library` plugin and add the `org.jetbrains.kotlin.jvm` plugin for Kotlin support. We also configure Kotlin, Java, tests and more.

Our build file is beginning to grow.

The more plugins we apply and the more plugins we configure, the larger it gets. There’s also repetition in the build files of the `app` and `data-model` subprojects, especially when configuring common extensions like setting the Java version and Kotlin support.

To address this, we use **convention plugins**. This allows us to avoid repeating configuration in each build file and keeps our build scripts more concise and maintainable. In convention plugins, we can encapsulate arbitrary build configuration or custom build logic.

To develop a convention plugin, you can use the protected [`buildSrc`](https://docs.gradle.org/userguide/sharing_build_logic_between_subprojects.html#sec:using_buildsrc) folder, which represents a completely separate Gradle build. `buildSrc` has its own settings file to define where dependencies of this build are located.

We add a Kotlin script called `my-java-library.gradle.kts` inside the `buildSrc/src/main/kotlin` directory. Or conversely, a Groovy script called `my-java-library.gradle` inside the `buildSrc/src/main/groovy` directory. We put all the plugin application and configuration from the `database-logic` build file into it:

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/my-java-library.gradle.kts

```kotlin
plugins {
    id("java-library")
    id("org.jetbrains.kotlin.jvm")
}

repositories {
    mavenCentral()
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(11))
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(11)
}
```

buildSrc/src/main/groovy/my-java-library.gradle

```groovy
plugins {
    id 'java-library'
    id 'org.jetbrains.kotlin.jvm'
}

repositories {
    mavenCentral()
}

java {
    toolchain.languageVersion.set(JavaLanguageVersion.of(11))
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain {
        languageVersion.set(JavaLanguageVersion.of(11))
    }
}
```

The name of the file `my-java-library` is the ID of our plugin, which we can now reference in all of our subprojects.

Why is the version of `id 'org.jetbrains.kotlin.jvm'` missing? See [Applying External Plugins to Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:applying_external_plugins).

The `database-logic` build file becomes much simpler by removing all the redundant build logic and applying our convention `my-java-library` plugin instead:

```option
Kotlin
```

```option
Groovy
```

database-logic/build.gradle.kts

```kotlin
plugins {
    id("my-java-library")
}
```

database-logic/build.gradle

```groovy
plugins {
    id('my-java-library')
}
```

This convention plugin enables us to easily share common configurations across all our build files. Any modifications can be made in one place, simplifying maintenance.

### [](https://docs.gradle.org/userguide/plugins.html#sec:custom_plugins_standalone_project)[Binary plugins](https://docs.gradle.org/userguide/plugins.html#sec:custom_plugins_standalone_project)

**Binary plugins** in Gradle are plugins that are built as standalone JAR files and applied to a project using the `plugins {}` block in the build script.

Let’s move our `GreetingPlugin` to a standalone project so that we can publish it and share it with others. The plugin is essentially moved from the `buildSrc` folder to its own build called `greeting-plugin`.

You can publish the plugin from `buildSrc`, but this is not recommended practice. Plugins that are ready for publication should be in their own build.

`greeting-plugin` is simply a Java project that produces a JAR containing the plugin classes.

The easiest way to package and publish a plugin to a repository is to use the [Gradle Plugin Development Plugin](https://docs.gradle.org/userguide/java_gradle_plugin.html#java_gradle_plugin). This plugin provides the necessary tasks and configurations (including the plugin metadata) to compile your script into a plugin that can be applied in other builds.

Here is a simple build script for the `greeting-plugin` project using the Gradle Plugin Development Plugin:

[![Image 8: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/customPlugin)

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
plugins {
    `java-gradle-plugin`
}

gradlePlugin {
    plugins {
        create("simplePlugin") {
            id = "org.example.greeting"
            implementationClass = "org.example.GreetingPlugin"
        }
    }
}
```

build.gradle

```groovy
plugins {
    id 'java-gradle-plugin'
}

gradlePlugin {
    plugins {
        simplePlugin {
            id = 'org.example.greeting'
            implementationClass = 'org.example.GreetingPlugin'
        }
    }
}
```

For more on publishing plugins, see [Publishing Plugins](https://docs.gradle.org/userguide/publishing_gradle_plugins.html#plugin-publishing-plugin).

[](https://docs.gradle.org/userguide/plugins.html#project_vs_settings_vs_init_plugins)[Scope of Plugins](https://docs.gradle.org/userguide/plugins.html#project_vs_settings_vs_init_plugins)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In earlier examples, `GreetingScriptPlugin` was defined against a [`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html) parameter:

```kotlin
class GreetingScriptPlugin : Plugin<Project> { }
```

Gradle plugins can in fact target three different scopes: [`Project`](https://docs.gradle.org/dsl/org.gradle.api.Project.html), [`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html), and [`Gradle`](https://docs.gradle.org/dsl/org.gradle.api.invocation.Gradle.html). Each scope controls different aspects of the build lifecycle and represents an interface.

| Interface | Scope | Description |
| --- | --- | --- |
| **Project** | Applied to an individual project. | Used to define build logic, register tasks, and configure project-specific settings. |
| **Settings** | Applied to the build as a whole. | Used to include subprojects, configure plugin management, or define buildscript repositories. |
| **Gradle** (init) | Applied globally. | Affects all builds on a machine. Commonly used to configure enterprise build tooling, inject repositories, or enforce conventions across builds. |

When writing **precompiled script plugins**, Gradle determines the intended plugin target (`Project`, `Settings`, or `Gradle`) based on the file name of the plugin source file:

| Plugin | Filename Suffix | Applies To | Scope |
| --- | --- | --- | --- |
| Project plugin | `.gradle`, `.gradle.kts` | `Plugin<Project>` object | Project scope |
| Settings plugin | `.settings.gradle`, `.settings.gradle.kts` | `Plugin<Settings>` object | Build scope |
| Init plugin | `.init.gradle`, `.init.gradle.kts` | `Plugin<Gradle>` object | Global scope |

For example, a file named `myplugin.gradle.kts` will always be treated as a Project plugin—even if it’s applied from a `settings.gradle.kts` file. To create a plugin for the settings context, it must be named something like `myplugin.settings.gradle.kts`.

We'd like to collect non-essential cookies for analytics and marketing which involves cookies managed by third parties. You can read more about how we use cookies in our [Privacy Policy](https://gradle.com/legal/privacy//) . By clicking “Accept,” below you agree to our website's cookie use as described in our Privacy Policy and our collection of non-essential cookies.

Reject Accept

**Docs**

* [Release Notes](https://docs.gradle.org/current/release-notes.html)
* [Groovy DSL](https://docs.gradle.org/current/dsl/)
* [Kotlin DSL](https://docs.gradle.org/current/kotlin-dsl/)
* [Javadoc](https://docs.gradle.org/current/javadoc/)

**News**

* [Blog](https://blog.gradle.org/)
* [Newsletter](https://newsletter.gradle.org/)
* [Twitter](https://twitter.com/gradle)
* [Status](https://status.gradle.com/)

**Products**

* [Develocity](https://gradle.com/develocity/)
* [Build Scan®](https://gradle.com/develocity/product/build-scan/)
* [Build Cache](https://gradle.com/build-cache/)
* [Services](https://gradle.org/services/)

**Get Help**

* [Forums](https://discuss.gradle.org/c/help-discuss)
* [GitHub](https://github.com/gradle/)
* [Events](https://gradle.org/training/)
* [DPE University](https://dpeuniversity.gradle.com/)

##### Stay `UP-TO-DATE` on new features and news

By entering your email, you agree to our [Terms](https://gradle.com/legal/terms-of-service/) and [Privacy Policy](https://gradle.com/legal/privacy/).

 © 2025 Gradle, Inc. Gradle®, Develocity®, Build Scan®, and the Gradlephant logo are registered trademarks of Gradle, Inc.

[](https://gradle.com/)

[Privacy](https://gradle.com/legal/privacy/) | [Terms of Service](https://gradle.com/legal/terms-of-service/)
