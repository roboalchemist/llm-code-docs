# Source: https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html

Title: Pre-compiled Script Plugins

URL Source: https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html

Published Time: Wed, 04 Mar 2026 11:20:45 GMT

Markdown Content:
Pre-compiled Script Plugins
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* [](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html "Theme")
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

* [Beginner Tutorial](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html)
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
* [Upgrading Gradle](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#running-introduction)
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

* [Writing Build Scripts](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#gradle-core)
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

* [DSLs and APIs](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#plugin-development)
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

* [Dependencies](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#advanced-topics)
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
* [Build Cache](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#configuration-cache)
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
* [APIs](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#how-to)
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

Pre-compiled Script Plugins
===========================

version 9.4.0

On this Page

* [Setting the plugin ID](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:the_plugin_id)
* [Making a plugin configurable using extensions](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:getting_input_from_the_build)
* [Adding default configuration as conventions](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:plugin_conventions)
* [Mapping extension properties to task properties](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:mapping_extension_properties_to_task_properties)
* [Applying external plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:applying_external_plugins)
* [Example of a precompiled script plugin in the `Project` scope](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#project_pre_compiled_plugins)
* [Example of a precompiled script plugin in the `Settings` scope](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#settings_pre_compiled_plugins)

A **precompiled script plugin** is a `.gradle.kts` (Kotlin DSL) or `.gradle` (Groovy DSL) script stored in a plugin source set (e.g. `buildSrc` or an included build like `build-logic`). Gradle automatically compiles it into a proper plugin class, packages it like a normal plugin, and assigns the plugin ID based on the file name.

For example, you place a script in `build-logic/src/main/kotlin/java-library-conventions.gradle.kts`:

```text
some-project/
├─ settings.gradle.kts
├─ build-logic/
│  ├─ build.gradle.kts
│  └─ src/
│     └─ main/
│        └─ kotlin/
│           └─ java-library-conventions.gradle.kts  (1)
└─ app/
   ├─ build.gradle.kts                              (2)
   └─ src/
```

**1**Pre-compiled script plugin
**2**Build file applies the plugin

Gradle automatically compiles that script into a plugin. The plugin ID is derived from the file name: `java-library-conventions.gradle.kts`.

You can now apply it in any build like a regular plugin. In the build file of the `app` project:

app/build.gradle.kts

```kotlin
plugins {
    // Apply by ID derived from the file name:
    id("java-library-conventions")
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:the_plugin_id)[Setting the plugin ID](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:the_plugin_id)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The plugin ID for a precompiled script is derived from its file name and optional package declaration.

For example, a script named `code-quality.gradle(.kts)` located in `src/main/groovy` (or `src/main/kotlin`) without a package declaration would be exposed as the `code-quality` plugin:

```option
Kotlin
```

```option
Groovy
```

buildSrc/build.gradle.kts

```kotlin
plugins {
    `kotlin-dsl`
}
```

app/build.gradle.kts

```kotlin
plugins {
    id("code-quality")
}
```

buildSrc/build.gradle

```groovy
plugins {
    id 'groovy-gradle-plugin'
}
```

app/build.gradle

```groovy
plugins {
    id 'code-quality'
}
```

On the other hand, a script named `code-quality.gradle.kts` located in `src/main/kotlin/my` with the package declaration `my` would be exposed as the `my.code-quality` plugin:

buildSrc/build.gradle.kts

```kotlin
plugins {
    `kotlin-dsl`
}
```

app/build.gradle.kts

```kotlin
plugins {
    id("my.code-quality")
}
```

When creating precompiled script plugins intended for settings or init scripts, the filename suffix determines where Gradle applies them:

* `.settings.gradle` or `.settings.gradle.kts` → interpreted as `Plugin<Settings>`

* `.init.gradle` or `.init.gradle.kts` → interpreted as `Plugin<Gradle>`

* `.gradle` or `.gradle.kts` → interpreted as the default `Plugin<Project>`

Groovy pre-compiled script plugins cannot have packages.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:getting_input_from_the_build)[Making a plugin configurable using extensions](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:getting_input_from_the_build)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Extension objects** are commonly used in plugins to expose configuration options and additional functionality to build scripts.

When you apply a plugin that defines an extension, you can access the extension object and configure its properties or call its methods to customize the behavior of the plugin or tasks provided by the plugin.

A [Project](https://docs.gradle.org/dsl/org.gradle.api.Project.html) has an associated [ExtensionContainer](https://docs.gradle.org/javadoc/org/gradle/api/plugins/ExtensionContainer.html) object that contains all the settings and properties for the plugins that have been applied to the project. You can provide configuration for your plugin by adding an extension object to this container.

Let’s update our `greetings` example:

[![Image 6: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/greeting)

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/greetings.gradle.kts

```kotlin
// Create extension object
interface GreetingPluginExtension {
    val message: Property<String>
}

// Add the 'greeting' extension object to project
val extension = project.extensions.create<GreetingPluginExtension>("greeting")
```

buildSrc/src/main/groovy/greetings.gradle

```groovy
// Create extension object
interface GreetingPluginExtension {
    Property<String> getMessage()
}

// Add the 'greeting' extension object to project
def extension = project.extensions.create("greeting", GreetingPluginExtension)
```

You can set the value of the `message` property directly with `extension.message.set("Hi from Gradle,")`.

However, the `GreetingPluginExtension` object becomes available as a project property with the same name as the extension object. You can now access `message` like so:

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/greetings.gradle.kts

```kotlin
// Where the<GreetingPluginExtension>() is equivalent to project.extensions.getByType(GreetingPluginExtension::class.java)
the<GreetingPluginExtension>().message.set("Hi from Gradle")
```

buildSrc/src/main/groovy/greetings.gradle

```groovy
extensions.findByType(GreetingPluginExtension).message.set("Hi from Gradle")
```

If you apply the `greetings` plugin, you can set the convention in your build script:

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
    id("greetings")
}

greeting {
    message = "Hello from Gradle"
}
```

app/build.gradle

```groovy
plugins {
    id 'application'
    id('greetings')
}

configure(greeting) {
    message = "Hello from Gradle"
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:plugin_conventions)[Adding default configuration as conventions](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:plugin_conventions)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In plugins, you can define default values, also known as **conventions**, using the `project` object.

Convention properties are properties that are initialized with default values but can be overridden:

[![Image 7: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/greeting)

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/greetings.gradle.kts

```kotlin
// Create extension object
interface GreetingPluginExtension {
    val message: Property<String>
}

// Add the 'greeting' extension object to project
val extension = project.extensions.create<GreetingPluginExtension>("greeting")

// Set a default value for 'message'
extension.message.convention("Hello from Gradle")
```

buildSrc/src/main/groovy/greetings.gradle

```groovy
// Create extension object
interface GreetingPluginExtension {
    Property<String> getMessage()
}

// Add the 'greeting' extension object to project
def extension = project.extensions.create("greeting", GreetingPluginExtension)

// Set a default value for 'message'
extension.message.convention("Hello from Gradle")
```

`extension.message.convention(…​)` sets a convention for the `message` property of the extension. This convention specifies that the value of `message` should default to `"Hello from Gradle"`.

If the `message` property is not explicitly set, its value will be automatically set to `"Hello from Gradle"`.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:mapping_extension_properties_to_task_properties)[Mapping extension properties to task properties](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:mapping_extension_properties_to_task_properties)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using an extension and mapping it to a custom task’s input/output properties is common in plugins.

In this example, the message property of the `GreetingPluginExtension` is mapped to the message property of the `GreetingTask` as an input:

[![Image 8: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/greeting)

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/greetings.gradle.kts

```kotlin
// Create extension object
interface GreetingPluginExtension {
    val message: Property<String>
}

// Add the 'greeting' extension object to project
val extension = project.extensions.create<GreetingPluginExtension>("greeting")

// Set a default value for 'message'
extension.message.convention("Hello from Gradle")

// Create a greeting task
abstract class GreetingTask : DefaultTask() {
    @Input
    val message = project.objects.property<String>()

    @TaskAction
    fun greet() {
        println("Message: ${message.get()}")
    }
}

// Register the task and set the convention
tasks.register<GreetingTask>("hello") {
    message.convention(extension.message)
}
```

buildSrc/src/main/groovy/greetings.gradle

```groovy
// Create extension object
interface GreetingPluginExtension {
    Property<String> getMessage()
}

// Add the 'greeting' extension object to project
def extension = project.extensions.create("greeting", GreetingPluginExtension)

// Set a default value for 'message'
extension.message.convention("Hello from Gradle")

// Create a greeting task
abstract class GreetingTask extends DefaultTask {
    @Input
    abstract Property<String> getMessage()

    @TaskAction
    void greet() {
        println("Message: ${message.get()}")
    }
}

// Register the task and set the convention
tasks.register("hello", GreetingTask) {
    message.convention(extension.message)
}
```

```bash
./gradlew -q hello
```

```text
Message: Hello from Gradle
```

This means that changes to the extension’s `message` property will trigger the task to be considered out-of-date, ensuring that the task is re-executed with the new message.

You can find out more about types that you can use in task implementations and extensions in [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration).

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:applying_external_plugins)[Applying external plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:applying_external_plugins)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to apply an external plugin in a precompiled script plugin, it has to be added to the plugin project’s implementation classpath in the plugin’s build file:

[![Image 9: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/precompiledScriptPlugins-externalPlugins)

```option
Kotlin
```

```option
Groovy
```

buildSrc/build.gradle.kts

```kotlin
plugins {
    `kotlin-dsl`
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("com.bmuschko:gradle-docker-plugin:6.4.0")
}
```

buildSrc/build.gradle

```groovy
plugins {
    id 'groovy-gradle-plugin'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.bmuschko:gradle-docker-plugin:6.4.0'
}
```

It can then be applied in the precompiled script plugin:

```option
Kotlin
```

```option
Groovy
```

buildSrc/src/main/kotlin/my-plugin.gradle.kts

```kotlin
plugins {
    id("com.bmuschko.docker-remote-api")
}
```

buildSrc/src/main/groovy/my-plugin.gradle

```groovy
plugins {
    id 'com.bmuschko.docker-remote-api'
}
```

The plugin version in this case is defined in the dependency declaration.

The `version "…​"` and `apply false` syntax are not supported in precompiled script plugins. The version for the plugin is determined by the version declared in the plugin’s build file. If a plugin needs to be on the classpath but not applied, it can be left out of the `plugins {}` block and only added as a dependency in the plugin’s build file.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#project_pre_compiled_plugins)[Example of a precompiled script plugin in the `Project` scope](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#project_pre_compiled_plugins)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can see an example [here](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html#example_precompiled_script_plugin).

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#settings_pre_compiled_plugins)[Example of a precompiled script plugin in the `Settings` scope](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#settings_pre_compiled_plugins)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Precompiled script plugins can also target the [`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html) scope. The following example defines a simple plugin in a separate build called `settings-plugin`.

Configure plugin management for the plugin build:

[![Image 10: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/precompiledScriptPlugins-settings)

```option
Kotlin
```

```option
Groovy
```

settings-plugin/settings.gradle.kts

```kotlin
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

settings-plugin/settings.gradle

```groovy
pluginManagement {
    repositories {
        gradlePluginPortal()
        mavenCentral()
    }
}
```

Set up the build to support precompiled script plugins:

```option
Kotlin
```

```option
Groovy
```

settings-plugin/build.gradle.kts

```kotlin
plugins {
    `kotlin-dsl`
}

repositories {
    mavenCentral()
    gradlePluginPortal()
}

dependencies {
    implementation("com.gradle:develocity-gradle-plugin:4.1")
}
```

settings-plugin/build.gradle

```groovy
plugins {
    id('groovy-gradle-plugin')
}

repositories {
    mavenCentral()
    gradlePluginPortal()
}

dependencies {
    implementation('com.gradle:develocity-gradle-plugin:4.1')
}
```

Notice that we used the practice described in [Applying external plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_precompiled.html#sec:applying_external_plugins).

Write the precompiled script plugin itself:

```option
Kotlin
```

```option
Groovy
```

settings-plugin/src/main/kotlin/my-plugin.settings.gradle.kts

```kotlin
plugins {
    id("com.gradle.develocity")
}
```

settings-plugin/src/main/groovy/my-plugin.settings.gradle

```groovy
plugins {
    id('com.gradle.develocity')
}
```

Because the file name ends with `.settings.gradle.kts`, Gradle compiles it into a plugin with a `Settings` scope. The plugin ID is `my-plugin`. You can use it as follows in a consumer project (root settings file of the consuming project):

```option
Kotlin
```

```option
Groovy
```

settings.gradle.kts

```kotlin
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
    includeBuild("./settings-plugin")
}

plugins {
    id("my-plugin")
}
```

settings.gradle

```groovy
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
    }
    includeBuild('./settings-plugin')
}

plugins {
    id('my-plugin')
}
```

Because the plugin was precompiled as a [`Settings`](https://docs.gradle.org/dsl/org.gradle.api.initialization.Settings.html) plugin (the `.settings.gradle(.kts)` suffix), you apply it in the settings file’s `plugins {}` block, not in a project `build.gradle(.kts)` file.

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
