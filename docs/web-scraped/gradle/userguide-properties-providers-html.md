# Source: https://docs.gradle.org/userguide/properties_providers.html

Title: Properties and Providers

URL Source: https://docs.gradle.org/userguide/properties_providers.html

Markdown Content:
Properties and Providers
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* [](https://docs.gradle.org/userguide/properties_providers.html "Theme")
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

* [Beginner Tutorial](https://docs.gradle.org/userguide/properties_providers.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/properties_providers.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/properties_providers.html)
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
* [Upgrading Gradle](https://docs.gradle.org/userguide/properties_providers.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/properties_providers.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/properties_providers.html#running-introduction)
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

* [Writing Build Scripts](https://docs.gradle.org/userguide/properties_providers.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/properties_providers.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/properties_providers.html#gradle-core)
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

* [DSLs and APIs](https://docs.gradle.org/userguide/properties_providers.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/properties_providers.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/properties_providers.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/properties_providers.html#plugin-development)
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

* [Dependencies](https://docs.gradle.org/userguide/properties_providers.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/properties_providers.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/properties_providers.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/properties_providers.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/properties_providers.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/properties_providers.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/properties_providers.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/properties_providers.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/properties_providers.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/properties_providers.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/properties_providers.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/properties_providers.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/properties_providers.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/properties_providers.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/properties_providers.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/properties_providers.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/properties_providers.html#advanced-topics)
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
* [Build Cache](https://docs.gradle.org/userguide/properties_providers.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/properties_providers.html#configuration-cache)
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
* [APIs](https://docs.gradle.org/userguide/properties_providers.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/properties_providers.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/properties_providers.html#how-to)
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

Properties and Providers
========================

version 9.4.0

On this Page

* [Understanding Properties](https://docs.gradle.org/userguide/properties_providers.html#understanding_properties)
* [Understanding Providers](https://docs.gradle.org/userguide/properties_providers.html#understanding_providers)
* [Chaining Providers](https://docs.gradle.org/userguide/properties_providers.html#chaining_providers)
* [Using Gradle Managed Properties](https://docs.gradle.org/userguide/properties_providers.html#managed_properties)
  * [Mutable Managed Properties](https://docs.gradle.org/userguide/properties_providers.html#mutable_managed_properties)
  * [Read-only Managed Properties (Providers)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_properties)
  * [Read-only Managed Nested Properties (Nested Providers)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_nested_properties)
  * [Read-only Managed "name" Property (Provider)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_name_property)

* [Using Gradle Managed Types](https://docs.gradle.org/userguide/properties_providers.html#managed_types)
* [Using Java Bean Properties](https://docs.gradle.org/userguide/properties_providers.html#using_java_bean_properties)

Gradle provides properties that are important for [lazy configuration](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration). When implementing a custom task or plugin, it’s imperative that you use these lazy properties.

Gradle represents lazy properties with two interfaces:

1. [Property](https://docs.gradle.org/javadoc/org/gradle/api/provider/Property.html) - Represents a value that can be queried and changed.

2. [Provider](https://docs.gradle.org/javadoc/org/gradle/api/provider/Provider.html) - Represents a value that can only be queried and cannot be changed.

Properties and providers manage _values and configurations_ in a build script.

In this example, `configuration` is a `Property<String>` that is set to the `configurationProvider``Provider<String>`. The `configurationProvider` lazily provides the value `"Hello, Gradle!"`:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
abstract class MyIntroTask : DefaultTask() {
    @get:Input
    abstract val configuration: Property<String>

    @TaskAction
    fun printConfiguration() {
        println("Configuration value: ${configuration.get()}")
    }
}

val configurationProvider: Provider<String> = project.provider { "Hello, Gradle!" }

tasks.register("myIntroTask", MyIntroTask::class) {
    configuration = configurationProvider
}
```

build.gradle

```groovy
abstract class MyIntroTask extends DefaultTask {
    @Input
    abstract Property<String> getConfiguration()

    @TaskAction
    void printConfiguration() {
        println "Configuration value: ${configuration.get()}"
    }
}

Provider<String> configurationProvider = project.provider { "Hello, Gradle!" }

tasks.register("myIntroTask", MyIntroTask) {
    configuration = configurationProvider
}
```

[](https://docs.gradle.org/userguide/properties_providers.html#understanding_properties)[Understanding Properties](https://docs.gradle.org/userguide/properties_providers.html#understanding_properties)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Properties in Gradle are variables that hold values. They can be defined and accessed within the build script to store information like file paths, version numbers, or custom values.

Properties can be set and retrieved using the `project` object:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
// Setting a property
val simpleMessageProperty: Property<String> = project.objects.property(String::class)
simpleMessageProperty.set("Hello, World from a Property!")
// Accessing a property
println(simpleMessageProperty.get())
```

build.gradle

```groovy
// Setting a property
def simpleMessageProperty = project.objects.property(String)
simpleMessageProperty.set("Hello, World from a Property!")
// Accessing a property
println(simpleMessageProperty.get())
```

Properties:

* Properties with these types are configurable.

* `Property` extends the `Provider` interface.

* The method [Property.set(T)](https://docs.gradle.org/javadoc/org/gradle/api/provider/Property.html#set-T-) specifies a value for the property, overwriting whatever value may have been present.

* The method [Property.set(Provider)](https://docs.gradle.org/javadoc/org/gradle/api/provider/Property.html#set-org.gradle.api.provider.Provider-) specifies a `Provider` for the value for the property, overwriting whatever value may have been present. This allows you to wire together `Provider` and `Property` instances before the values are configured.

* A `Property` can be created by the factory method [ObjectFactory.property(Class)](https://docs.gradle.org/javadoc/org/gradle/api/model/ObjectFactory.html#property-java.lang.Class-).

[](https://docs.gradle.org/userguide/properties_providers.html#understanding_providers)[Understanding Providers](https://docs.gradle.org/userguide/properties_providers.html#understanding_providers)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Providers are objects that represent a value that may not be immediately available. Providers are useful for lazy evaluation and can be used to model values that may change over time or depend on other tasks or inputs:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
// Setting a provider
val simpleMessageProvider: Provider<String> = project.providers.provider { "Hello, World from a Provider!" }
// Accessing a provider
println(simpleMessageProvider.get())
```

build.gradle

```groovy
// Setting a provider
def simpleMessageProvider = project.providers.provider { "Hello, World from a Provider!" }
// Accessing a provider
println(simpleMessageProvider.get())
```

Providers:

* Properties with these types are read-only.

* The method [Provider.get()](https://docs.gradle.org/javadoc/org/gradle/api/provider/Provider.html#get--) returns the current value of the property.

* A `Provider` can be created from another `Provider` using [Provider.map(Transformer)](https://docs.gradle.org/javadoc/org/gradle/api/provider/Provider.html#map-org.gradle.api.Transformer-).

* Many other types extend `Provider` and can be used wherever a `Provider` is required.

[](https://docs.gradle.org/userguide/properties_providers.html#chaining_providers)[Chaining Providers](https://docs.gradle.org/userguide/properties_providers.html#chaining_providers)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chaining `Providers` preserves laziness and is essential to use when writing build logic.

These methods allow you to transform, combine, or provide fallback values without triggering eager evaluation:

| Method | Purpose |
| --- | --- |
| `map()` | Transforms the value using a function, producing a new `Provider`. |
| `flatMap()` | Transforms the value into another `Provider`, and flattens the result. |
| `zip()` | Combines multiple `Providers` into one, applying a function to their values. |
| `orElse()` | Supplies a fallback `Provider` if the original is missing or undefined. |

Using `map()` is a common example:

build.gradle.kts

```kotlin
val majorVersion: Provider<String> = versionProvider.map { it.split(".")[0] }
```

You can see the following example for a detailed breakdown at `Provider` chaining using `map()`:

build.gradle

```groovy
tasks.register("printFloatFromFile") {
    // Type: RegularFile
    def myFile = layout.projectDirectory.file("someNumber.txt")

    // Type: Provider<Float>
    def floatProvider = project.providers
        // Type: Provider<FileContents>
        .fileContents(myFile)
        // Type: Provider<String>
        .asText
        // Type: Provider<Float>
        .map {
            // Type: Float
            it.toFloat()
        }

    doLast {
        // Type: Provider<Float>
        println ">>> Float value from file: $floatProvider"
        // Type: Float
        println ">>> Float value from file: ${floatProvider.get()}"
    }
}
```

[](https://docs.gradle.org/userguide/properties_providers.html#managed_properties)[Using Gradle Managed Properties](https://docs.gradle.org/userguide/properties_providers.html#managed_properties)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle’s managed properties allow you to declare properties as getters (Java, Groovy) or properties (Kotlin).

Gradle then automatically provides the implementation for these properties, managing their state.

A property may be _mutable_, meaning that it is of type `Property`, which has both a `get()` and a `set()` method:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
abstract class MyPropertyTask : DefaultTask() {
    @get:Input
    abstract val messageProperty: Property<String> // message property

    @TaskAction
    fun printMessage() {
        println(messageProperty.get())
    }
}

tasks.register<MyPropertyTask>("myPropertyTask") {
    messageProperty.convention("Hello, Gradle!")
}
```

build.gradle

```groovy
abstract class MyPropertyTask extends DefaultTask {
    @Input
    abstract Property<String> getMessageProperty()

    @TaskAction
    void printMessage() {
        println(messageProperty.get())
    }
}

tasks.register('myPropertyTask', MyPropertyTask) {
    messageProperty.convention("Hello, Gradle!")
}
```

Or _read-only_, meaning that it is of type `Provider`, which only has a `get()` method:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
abstract class MyProviderTask : DefaultTask() {
    val messageProvider: Provider<String> = project.providers.provider { "Hello, Gradle!" } // message provider

    @TaskAction
    fun printMessage() {
        println(messageProvider.get())
    }
}

tasks.register<MyProviderTask>("MyProviderTask") {

}
```

build.gradle

```groovy
abstract class MyProviderTask extends DefaultTask {
    final Provider<String> messageProvider = project.providers.provider { "Hello, Gradle!" }

    @TaskAction
    void printMessage() {
        println(messageProvider.get())
    }
}

tasks.register('MyProviderTask', MyProviderTask)
```

### [](https://docs.gradle.org/userguide/properties_providers.html#mutable_managed_properties)[Mutable Managed Properties](https://docs.gradle.org/userguide/properties_providers.html#mutable_managed_properties)

A mutable managed property is declared using a getter method of type `Property<T>`, where `T` can be any serializable type or a [fully managed Gradle type](https://docs.gradle.org/userguide/properties_providers.html#managed_types). The property must not have any setter methods.

Here is an example of a task type with an `uri` property of type `URI`:

Download.java

```java
public abstract class Download extends DefaultTask {
    @Input
    public abstract Property<URI> getUri(); // abstract getter of type Property<T>

    @TaskAction
    void run() {
        System.out.println("Downloading " + getUri().get()); // Use the `uri` property
    }
}
```

Note that for a property to be considered a mutable managed property, the property’s getter methods must have `public` or `protected` visibility. It is recommended to also make the property `abstract`, so Gradle can manage the initialization of the property.

The property type must be one of the following:

| Property Type | Note |
| --- | --- |
| `Property<T>` | Where `T` is typically `Double`, `Integer`, `Long`, `String`, or `Bool` |
| `RegularFileProperty` | Configurable regular file location, whose value is mutable |
| `DirectoryProperty` | Configurable directory location, whose value is mutable |
| `ListProperty<T>` | List of elements of type `T` |
| `SetProperty<T>` | Set of elements of type `T` |
| `MapProperty<K, V>` | Map of `K` type keys with `V` type values |
| `ConfigurableFileCollection` | A mutable `FileCollection` which represents a collection of file system locations |
| `ConfigurableFileTree` | A mutable `FileTree` which represents a hierarchy of files |

### [](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_properties)[Read-only Managed Properties (Providers)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_properties)

You can declare a read-only managed property, also known as a provider, using a getter method of type `Provider<T>`. The method implementation needs to derive the value. It can, for example, derive the value from other properties.

Here is an example of a task type with a `uri` provider that is derived from a `location` property:

Download.java

```java
public abstract class Download extends DefaultTask {
    @Input
    public abstract Property<String> getLocation();

    @Internal
    public Provider<URI> getUri() {
        return getLocation().map(l -> URI.create("https://" + l));
    }

    @TaskAction
    void run() {
        System.out.println("Downloading " + getUri().get());  // Use the `uri` provider (read-only property)
    }
}
```

### [](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_nested_properties)[Read-only Managed Nested Properties (Nested Providers)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_nested_properties)

You can declare a read-only managed nested property by adding an abstract getter method for the property to a type annotated with [`@Nested`](https://docs.gradle.org/javadoc/org/gradle/api/tasks/Nested.html). The property should not have any setter methods. Gradle provides the implementation for the getter method and creates a value for the property.

This pattern is useful when a custom type has a nested complex type which has the same lifecycle. If the lifecycle is different, consider using `Property<NestedType>` instead.

Here is an example of a task type with a `resource` property. The `Resource` type is also a custom Gradle type and defines some managed properties:

Download.java

```java
public abstract class Download extends DefaultTask {
    @Nested
    public abstract Resource getResource(); // Use an abstract getter method annotated with @Nested

    @TaskAction
    void run() {
        // Use the `resource` property
        System.out.println("Downloading https://" + getResource().getHostName().get() + "/" + getResource().getPath().get());
    }
}

public interface Resource {
    @Input
    Property<String> getHostName();
    @Input
    Property<String> getPath();
}
```

### [](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_name_property)[Read-only Managed "name" Property (Provider)](https://docs.gradle.org/userguide/properties_providers.html#read_only_managed_name_property)

If the type contains an abstract property called "name" of type `String`, Gradle provides an implementation for the getter method, and extends each constructor with a "name" parameter, which comes before all other constructor parameters.

If the type is an interface, Gradle will provide a constructor with a single "name" parameter and `@Inject` semantics.

You can have your type implement or extend the [Named](https://docs.gradle.org/javadoc/org/gradle/api/Named.html) interface, which defines such a read-only "name" property:

```groovy
import org.gradle.api.Named

interface MyType : Named {
    // Other properties and methods...
}

class MyTypeImpl(override val name: String) : MyType {
    // Implement other properties and methods...
}

// Usage
val instance = MyTypeImpl("myName")
println(instance.name) // Prints: myName
```

[](https://docs.gradle.org/userguide/properties_providers.html#managed_types)[Using Gradle Managed Types](https://docs.gradle.org/userguide/properties_providers.html#managed_types)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A managed type as an abstract class or interface with no fields and whose properties are all managed. These types have their state entirely managed by Gradle.

For example, this managed type is defined as an interface:

Resource.java

```java
public interface Resource {
    @Input
    Property<String> getHostName();
    @Input
    Property<String> getPath();
}
```

A _named managed type_ is a managed type that additionally has an abstract property "name" of type `String`. Named managed types are especially useful as the element type of [NamedDomainObjectContainer](https://docs.gradle.org/javadoc/org/gradle/api/NamedDomainObjectContainer.html):

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
interface MyNamedType : Named {
    
}

abstract class MyPluginExtension {
    abstract val myNamedContainer: NamedDomainObjectContainer<MyNamedType>

    fun myNamedContainer(configurationAction: Action<in NamedDomainObjectContainer<MyNamedType>>) = configurationAction.execute(myNamedContainer)
}

val pluginExtension = extensions.create<MyPluginExtension>("pluginExtension")

pluginExtension.apply {
    myNamedContainer {
        val myName by registering
    }
}
```

build.gradle

```groovy
interface MyNamedType extends Named {

}

abstract class MyPluginExtension {
    abstract NamedDomainObjectContainer<MyNamedType> getMyNamedContainer()

    void myNamedContainer(Action<? super NamedDomainObjectContainer<MyNamedType>> action) {
        action.execute(getMyNamedContainer())
    }
}

extensions.create("pluginExtension", MyPluginExtension)

pluginExtension {
    myNamedContainer {
        myName
    }
}
```

[](https://docs.gradle.org/userguide/properties_providers.html#using_java_bean_properties)[Using Java Bean Properties](https://docs.gradle.org/userguide/properties_providers.html#using_java_bean_properties)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may see properties implemented in the Java bean property style. That is, they do not use a `Property<T>` or `Provider<T>` types but are instead implemented with concrete setter and getter methods (or corresponding conveniences in Groovy or Kotlin).

This style of property definition is legacy in Gradle and is discouraged:

```java
public class MyTask extends DefaultTask {
    private String someProperty;

    public String getSomeProperty() {
        return someProperty;
    }

    public void setSomeProperty(String someProperty) {
        this.someProperty = someProperty;
    }

    @TaskAction
    public void myAction() {
        System.out.println("SomeProperty: " + someProperty);
    }
}
```

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

![Image 1](https://cdn.usefathom.com/?h=https%3A%2F%2Fdocs.gradle.org&p=%2Fcurrent%2Fuserguide%2Fproperties_providers.html&r=&sid=ULMNNWXO&qs=%7B%7D&cid=64207461)
