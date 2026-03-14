# Source: https://docs.gradle.org/userguide/custom_tasks.html

Title: Advanced Tasks

URL Source: https://docs.gradle.org/userguide/custom_tasks.html

Markdown Content:
Advanced Tasks
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* [](https://docs.gradle.org/userguide/custom_tasks.html "Theme")
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

* [Beginner Tutorial](https://docs.gradle.org/userguide/custom_tasks.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/custom_tasks.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/custom_tasks.html)
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
* [Upgrading Gradle](https://docs.gradle.org/userguide/custom_tasks.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/custom_tasks.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/custom_tasks.html#running-introduction)
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

* [Writing Build Scripts](https://docs.gradle.org/userguide/custom_tasks.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/custom_tasks.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/custom_tasks.html#gradle-core)
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

* [DSLs and APIs](https://docs.gradle.org/userguide/custom_tasks.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/custom_tasks.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/custom_tasks.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/custom_tasks.html#plugin-development)
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

* [Dependencies](https://docs.gradle.org/userguide/custom_tasks.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/custom_tasks.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/custom_tasks.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/custom_tasks.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/custom_tasks.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/custom_tasks.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/custom_tasks.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/custom_tasks.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/custom_tasks.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/custom_tasks.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/custom_tasks.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/custom_tasks.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/custom_tasks.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/custom_tasks.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/custom_tasks.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/custom_tasks.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/custom_tasks.html#advanced-topics)
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
* [Build Cache](https://docs.gradle.org/userguide/custom_tasks.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/custom_tasks.html#configuration-cache)
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
* [APIs](https://docs.gradle.org/userguide/custom_tasks.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/custom_tasks.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/custom_tasks.html#how-to)
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

Advanced Tasks
==============

version 9.4.0

On this Page

* [Incremental tasks](https://docs.gradle.org/userguide/custom_tasks.html#incremental_tasks)
  * [Implementing an incremental task](https://docs.gradle.org/userguide/custom_tasks.html#sec:implementing_an_incremental_task)
  * [Which inputs are considered out of date?](https://docs.gradle.org/userguide/custom_tasks.html#sec:which_inputs_are_considered_out_of_date)
  * [An incremental task in action](https://docs.gradle.org/userguide/custom_tasks.html#sec:an_incremental_task_in_action)

* [Command Line options](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_and_using_command_line_options)
  * [Step 1. Declare a command-line option](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_task_option)
  * [Step 2. Use an option on the command line](https://docs.gradle.org/userguide/custom_tasks.html#sec:using_task_option_command_line)
  * [Supported data types for options](https://docs.gradle.org/userguide/custom_tasks.html#sec:supported_task_option_data_types)
  * [Documenting available values for an option](https://docs.gradle.org/userguide/custom_tasks.html#sec:documenting_available_task_option_values)
  * [Listing command line options](https://docs.gradle.org/userguide/custom_tasks.html#sec:listing_task_options)
  * [Limitations](https://docs.gradle.org/userguide/custom_tasks.html#limitations)

* [Verification failures](https://docs.gradle.org/userguide/custom_tasks.html#verification_failures)

[](https://docs.gradle.org/userguide/custom_tasks.html#incremental_tasks)[Incremental tasks](https://docs.gradle.org/userguide/custom_tasks.html#incremental_tasks)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Gradle, implementing a task that skips execution when its inputs and outputs are already `UP-TO-DATE` is simple and efficient, thanks to the [Incremental Build](https://docs.gradle.org/userguide/incremental_build.html#incremental_build) feature.

However, there are times when only a few input files have changed since the last execution, and it is best to avoid reprocessing all the unchanged inputs. This situation is common in tasks that transform input files into output files on a one-to-one basis.

To optimize your build process you can use an incremental task. This approach ensures that only out-of-date input files are processed, improving build performance.

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:implementing_an_incremental_task)[Implementing an incremental task](https://docs.gradle.org/userguide/custom_tasks.html#sec:implementing_an_incremental_task)

For a task to process inputs incrementally, that task must contain an _incremental_ task action.

This is a task action method that has a single [InputChanges](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html) parameter. That parameter tells Gradle that the action only wants to process the changed inputs.

In addition, the task needs to declare at least one incremental file input property by using either [`@Incremental`](https://docs.gradle.org/javadoc/org/gradle/work/Incremental.html) or [`@SkipWhenEmpty`](https://docs.gradle.org/javadoc/org/gradle/api/tasks/SkipWhenEmpty.html):

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
public class IncrementalReverseTask : DefaultTask() {

    @get:Incremental
    @get:InputDirectory
    val inputDir: DirectoryProperty = project.objects.directoryProperty()

    @get:OutputDirectory
    val outputDir: DirectoryProperty = project.objects.directoryProperty()

    @get:Input
    val inputProperty: RegularFileProperty = project.objects.fileProperty() // File input property

    @TaskAction
    fun execute(inputs: InputChanges) { // InputChanges parameter
        val msg = if (inputs.isIncremental) "CHANGED inputs are out of date"
                  else "ALL inputs are out of date"
        println(msg)
    }
}
```

build.gradle

```groovy
class IncrementalReverseTask extends DefaultTask {

    @Incremental
    @InputDirectory
    def File inputDir

    @OutputDirectory
    def File outputDir

    @Input
    def inputProperty // File input property

    @TaskAction
    void execute(InputChanges inputs) { // InputChanges parameter
        println inputs.incremental ? "CHANGED inputs are out of date"
                                   : "ALL inputs are out of date"
    }
}
```

To query incremental changes for an input file property, that property must always return the same instance. The easiest way to accomplish this is to use one of the following property types: [`RegularFileProperty`](https://docs.gradle.org/javadoc/org/gradle/api/file/RegularFileProperty.html), [`DirectoryProperty`](https://docs.gradle.org/javadoc/org/gradle/api/file/DirectoryProperty.html) or [`ConfigurableFileCollection`](https://docs.gradle.org/javadoc/org/gradle/api/file/ConfigurableFileCollection.html).

You can learn more about `RegularFileProperty` and `DirectoryProperty` in [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration).

The incremental task action can use [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)) to find out what files have changed for a given file-based input property, be it of type `RegularFileProperty`, `DirectoryProperty` or `ConfigurableFileCollection`.

The method returns an `Iterable` of type [FileChanges](https://docs.gradle.org/javadoc/org/gradle/work/FileChange.html), which in turn can be queried for the following:

* the [affected file](https://docs.gradle.org/javadoc/org/gradle/work/FileChange.html#getFile--)

* the [change type](https://docs.gradle.org/javadoc/org/gradle/work/FileChange.html#getChangeType--) (`ADDED`, `REMOVED` or `MODIFIED`)

* the [normalized path](https://docs.gradle.org/javadoc/org/gradle/work/FileChange.html#getNormalizedPath--) of the changed file

* the [file type](https://docs.gradle.org/javadoc/org/gradle/work/FileChange.html#getFileType--) of the changed file

The following example demonstrates an incremental task that has a directory input. It assumes that the directory contains a collection of text files and copies them to an output directory, reversing the text within each file:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
abstract class IncrementalReverseTask : DefaultTask() {
    @get:Incremental
    @get:PathSensitive(PathSensitivity.NAME_ONLY)
    @get:InputDirectory
    abstract val inputDir: DirectoryProperty

    @get:OutputDirectory
    abstract val outputDir: DirectoryProperty

    @get:Input
    abstract val inputProperty: Property<String>

    @TaskAction
    fun execute(inputChanges: InputChanges) {
        println(
            if (inputChanges.isIncremental) "Executing incrementally"
            else "Executing non-incrementally"
        )

        inputChanges.getFileChanges(inputDir).forEach { change ->
            if (change.fileType == FileType.DIRECTORY) return@forEach

            println("${change.changeType}: ${change.normalizedPath}")
            val targetFile = outputDir.file(change.normalizedPath).get().asFile
            if (change.changeType == ChangeType.REMOVED) {
                targetFile.delete()
            } else {
                targetFile.writeText(change.file.readText().reversed())
            }
        }
    }
}
```

build.gradle

```groovy
abstract class IncrementalReverseTask extends DefaultTask {
    @Incremental
    @PathSensitive(PathSensitivity.NAME_ONLY)
    @InputDirectory
    abstract DirectoryProperty getInputDir()

    @OutputDirectory
    abstract DirectoryProperty getOutputDir()

    @Input
    abstract Property<String> getInputProperty()

    @TaskAction
    void execute(InputChanges inputChanges) {
        println(inputChanges.incremental
            ? 'Executing incrementally'
            : 'Executing non-incrementally'
        )

        inputChanges.getFileChanges(inputDir).each { change ->
            if (change.fileType == FileType.DIRECTORY) return

            println "${change.changeType}: ${change.normalizedPath}"
            def targetFile = outputDir.file(change.normalizedPath).get().asFile
            if (change.changeType == ChangeType.REMOVED) {
                targetFile.delete()
            } else {
                targetFile.text = change.file.text.reverse()
            }
        }
    }
}
```

The type of the `inputDir` property, its annotations, and the `execute()` action use `getFileChanges()` to process the subset of files that have changed since the last build. The action deletes a target file if the corresponding input file has been removed.

If, for some reason, the task is executed non-incrementally (by running with `--rerun-tasks`, for example), all files are reported as `ADDED`, irrespective of the previous state. In this case, Gradle automatically removes the previous outputs, so the incremental task must only process the given files.

For a simple transformer task like the above example, the task action must generate output files for any out-of-date inputs and delete output files for any removed inputs.

A task may only contain a single incremental task action.

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:which_inputs_are_considered_out_of_date)[Which inputs are considered out of date?](https://docs.gradle.org/userguide/custom_tasks.html#sec:which_inputs_are_considered_out_of_date)

When a task has been previously executed, and the only changes since that execution are to incremental input file properties, Gradle can intelligently determine which input files need to be processed, a concept known as incremental execution.

In this scenario, the [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)) method, available in the `org.gradle.work.InputChanges` class, provides details for all input files associated with the given property that have been `ADDED`, `REMOVED` or `MODIFIED`.

However, there are many cases where Gradle cannot determine which input files need to be processed (i.e., non-incremental execution). Examples include:

* There is no history available from a previous execution.

* You are building with a different version of Gradle. Currently, Gradle does not use task history from a different version.

* An [`upToDateWhen`](https://docs.gradle.org/javadoc/org/gradle/api/tasks/TaskOutputs.html#upToDateWhen-groovy.lang.Closure-) criterion added to the task returns `false`.

* An input property has changed since the previous execution.

* A non-incremental input file property has changed since the previous execution.

* One or more output files have changed since the previous execution.

In these cases, Gradle will report all input files as `ADDED`, and the `getFileChanges()` method will return details for all the files that comprise the given input property.

You can check if the task execution is incremental or not with the [`InputChanges.isIncremental()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges.html##org.gradle.work.InputChanges:incremental) method.

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:an_incremental_task_in_action)[An incremental task in action](https://docs.gradle.org/userguide/custom_tasks.html#sec:an_incremental_task_in_action)

Consider an instance of `IncrementalReverseTask` executed against a set of inputs for the first time.

In this case, all inputs will be considered `ADDED`, as shown here:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
tasks.register<IncrementalReverseTask>("incrementalReverse") {
    inputDir = file("inputs")
    outputDir = layout.buildDirectory.dir("outputs")
    inputProperty = project.findProperty("taskInputProperty") as String? ?: "original"
}
```

build.gradle

```groovy
tasks.register('incrementalReverse', IncrementalReverseTask) {
    inputDir = file('inputs')
    outputDir = layout.buildDirectory.dir("outputs")
    inputProperty = project.properties['taskInputProperty'] ?: 'original'
}
```

The build layout:

```text
.
├── build.gradle
└── inputs
    ├── 1.txt
    ├── 2.txt
    └── 3.txt
```

```bash
./gradlew -q incrementalReverse
```

```text
Executing non-incrementally
ADDED: 1.txt
ADDED: 2.txt
ADDED: 3.txt
```

Naturally, when the task is executed again with no changes, then the entire task is `UP-TO-DATE`, and the task action is not executed:

```bash
./gradlew incrementalReverse
```

```text
> Task :incrementalReverse UP-TO-DATE

BUILD SUCCESSFUL in 0s
1 actionable task: 1 up-to-date
```

When an input file is modified in some way or a new input file is added, then re-executing the task results in those files being returned by [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)).

The following example modifies the content of one file and adds another before running the incremental task:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
tasks.register("updateInputs") {
    val inputsDir = layout.projectDirectory.dir("inputs")
    outputs.dir(inputsDir)
    doLast {
        inputsDir.file("1.txt").asFile.writeText("Changed content for existing file 1.")
        inputsDir.file("4.txt").asFile.writeText("Content for new file 4.")
    }
}
```

build.gradle

```groovy
tasks.register('updateInputs') {
    def inputsDir = layout.projectDirectory.dir('inputs')
    outputs.dir(inputsDir)
    doLast {
        inputsDir.file('1.txt').asFile.text = 'Changed content for existing file 1.'
        inputsDir.file('4.txt').asFile.text = 'Content for new file 4.'
    }
}
```

```bash
./gradlew -q updateInputs incrementalReverse
```

```text
Executing incrementally
MODIFIED: 1.txt
ADDED: 4.txt
```

The various mutation tasks (`updateInputs`, `removeInput`, etc) are only present to demonstrate the behavior of incremental tasks. They should not be viewed as the kinds of tasks or task implementations you should have in your own build scripts.

When an existing input file is removed, then re-executing the task results in that file being returned by [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)) as `REMOVED`.

The following example removes one of the existing files before executing the incremental task:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
tasks.register<Delete>("removeInput") {
    delete("inputs/3.txt")
}
```

build.gradle

```groovy
tasks.register('removeInput', Delete) {
    delete 'inputs/3.txt'
}
```

```bash
./gradlew -q removeInput incrementalReverse
```

```text
Executing incrementally
REMOVED: 3.txt
```

Gradle cannot determine which input files are out-of-date when an _output_ file is deleted (or modified). In this case, details for _all_ the input files for the given property are returned by [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)).

The following example removes one of the output files from the build directory. However, all the input files are considered to be `ADDED`:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
tasks.register<Delete>("removeOutput") {
    delete(layout.buildDirectory.file("outputs/1.txt"))
}
```

build.gradle

```groovy
tasks.register('removeOutput', Delete) {
    delete layout.buildDirectory.file("outputs/1.txt")
}
```

```bash
./gradlew -q removeOutput incrementalReverse
```

```text
Executing non-incrementally
ADDED: 1.txt
ADDED: 2.txt
ADDED: 3.txt
```

The last scenario we want to cover concerns what happens when a non-file-based input property is modified. In such cases, Gradle cannot determine how the property impacts the task outputs, so the task is executed non-incrementally. This means that _all_ input files for the given property are returned by [`InputChanges.getFileChanges()`](https://docs.gradle.org/dsl/org.gradle.work.InputChanges.html#org.gradle.work.InputChanges:getFileChanges(org.gradle.api.file.FileCollection)) and they are all treated as `ADDED`.

The following example sets the project property `taskInputProperty` to a new value when running the `incrementalReverse` task. That project property is used to initialize the task’s `inputProperty` property, as you can see in the [first example of this section](https://docs.gradle.org/userguide/custom_tasks.html#ex:incremental_task_definition).

Here is the expected output in this case:

```bash
./gradlew -q -PtaskInputProperty=changed incrementalReverse
```

```text
Executing non-incrementally
ADDED: 1.txt
ADDED: 2.txt
ADDED: 3.txt
```

[](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_and_using_command_line_options)[Command Line options](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_and_using_command_line_options)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes, a user wants to declare the value of an exposed task property on the command line instead of the build script. Passing property values on the command line is particularly helpful if they change more frequently.

The task API supports a mechanism for marking a property to automatically generate a corresponding command line parameter with a specific name at runtime.

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_task_option)[Step 1. Declare a command-line option](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_task_option)

To expose a new command line option for a task property, annotate the corresponding setter method of a property with [Option](https://docs.gradle.org/javadoc/org/gradle/api/tasks/options/Option.html):

```kotlin
@Option(option = "flag", description = "Sets the flag")
```

An option requires a mandatory identifier. You can provide an optional description.

A task can expose as many command line options as properties available in the class.

Options may be declared in superinterfaces of the task class as well. If multiple interfaces declare the same property but with different option flags, they will both work to set the property.

In the example below, the custom task `UrlVerify` verifies whether a URL can be resolved by making an HTTP call and checking the response code. The URL to be verified is configurable through the property `url`. The setter method for the property is annotated with [@Option](https://docs.gradle.org/javadoc/org/gradle/api/tasks/options/Option.html):

UrlVerify.java

```java
import org.gradle.api.tasks.options.Option;

public class UrlVerify extends DefaultTask {
    private String url;

    @Option(option = "url", description = "Configures the URL to be verified.")
    public void setUrl(String url) {
        this.url = url;
    }

    @Input
    public String getUrl() {
        return url;
    }

    @TaskAction
    public void verify() {
        getLogger().quiet("Verifying URL '{}'", url);

        // verify URL by making a HTTP call
    }
}
```

All options declared for a task can be [rendered as console output](https://docs.gradle.org/userguide/custom_tasks.html#sec:listing_task_options) by running the `help` task and the `--task` option.

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:using_task_option_command_line)[Step 2. Use an option on the command line](https://docs.gradle.org/userguide/custom_tasks.html#sec:using_task_option_command_line)

There are a few rules for options on the command line:

* The option uses a double-dash as a prefix, e.g., `--url`. A single dash does not qualify as valid syntax for a task option.

* The option argument follows directly after the task declaration, e.g., `verifyUrl --url=http://www.google.com/`.

* Multiple task options can be declared in any order on the command line following the task name.

Building upon the earlier example, the build script creates a task instance of type `UrlVerify` and provides a value from the command line through the exposed option:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
tasks.register<UrlVerify>("verifyUrl")
```

build.gradle

```groovy
tasks.register('verifyUrl', UrlVerify)
```

```bash
./gradlew -q verifyUrl --url=http://www.google.com/
```

```text
Verifying URL 'http://www.google.com/'
```

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:supported_task_option_data_types)[Supported data types for options](https://docs.gradle.org/userguide/custom_tasks.html#sec:supported_task_option_data_types)

Gradle limits the data types that can be used for declaring command line options.

The use of the command line differs per type:

`boolean`, `Boolean`, `Property<Boolean>`
Describes an option with the value `true` or `false`.

 Passing the option on the command line treats the value as `true`. For example, `--foo` equates to `true`.

 The absence of the option uses the default value of the property. For each boolean option, an opposite option is created automatically. For example, `--no-foo` is created for the provided option `--foo` and `--bar` is created for `--no-bar`. Options whose name starts with `--no` are disabled options and set the option value to `false`. An opposite option is only created if no option with the same name already exists for the task.

`Double`, `Property<Double>`
Describes an option with a double value.

 Passing the option on the command line also requires a value, e.g., `--factor=2.2` or `--factor 2.2`.

`Integer`, `Property<Integer>`
Describes an option with an integer value.

 Passing the option on the command line also requires a value, e.g., `--network-timeout=5000` or `--network-timeout 5000`.

`Long`, `Property<Long>`
Describes an option with a long value.

 Passing the option on the command line also requires a value, e.g., `--threshold=2147483648` or `--threshold 2147483648`.

`String`, `Property<String>`
Describes an option with an arbitrary String value.

 Passing the option on the command line also requires a value, e.g., `--container-id=2x94held` or `--container-id 2x94held`.

`enum`, `Property<enum>`
Describes an option as an enumerated type.

 Passing the option on the command line also requires a value e.g., `--log-level=DEBUG` or `--log-level debug`.

 The value is not case-sensitive.

`List<T>` where `T` is `Double`, `Integer`, `Long`, `String`, `enum`
Describes an option that can take multiple values of a given type.

 The values for the option have to be provided as multiple declarations, e.g., `--image-id=123 --image-id=456`.

 Other notations, such as comma-separated lists or multiple values separated by a space character, are currently not supported.

`ListProperty<T>`, `SetProperty<T>` where `T` is `Double`, `Integer`, `Long`, `String`, `enum`
Describes an option that can take multiple values of a given type.

 The values for the option have to be provided as multiple declarations, e.g., `--image-id=123 --image-id=456`.

 Other notations, such as comma-separated lists or multiple values separated by a space character, are currently not supported.

`DirectoryProperty`, `RegularFileProperty`
Describes an option with a file system element.

 Passing the option on the command line also requires a value representing a path, e.g., `--output-file=file.txt` or `--output-dir outputDir`.

 Relative paths are resolved relative to the project directory of the project that owns this property instance. See [`FileSystemLocationProperty.set()`](https://docs.gradle.org/javadoc/org/gradle/api/file/FileSystemLocationProperty.html#set-java.io.File).

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:documenting_available_task_option_values)[Documenting available values for an option](https://docs.gradle.org/userguide/custom_tasks.html#sec:documenting_available_task_option_values)

Theoretically, an option for a property type `String` or `List<String>` can accept any arbitrary value. Accepted values for such an option can be documented programmatically with the help of the annotation [OptionValues](https://docs.gradle.org/javadoc/org/gradle/api/tasks/options/OptionValues.html):

```text
@OptionValues('file')
```

This annotation may be assigned to any method that returns a `List` of one of the supported data types. You need to specify an option identifier to indicate the relationship between the option and available values.

Passing a value on the command line not supported by the option does not fail the build or throw an exception. You must implement custom logic for such behavior in the task action.

The example below demonstrates the use of multiple options for a single task. The task implementation provides a list of available values for the option `output-type`:

UrlProcess.java

```java
import org.gradle.api.tasks.options.Option;
import org.gradle.api.tasks.options.OptionValues;

public abstract class UrlProcess extends DefaultTask {
    private String url;
    private OutputType outputType;

    @Input
    @Option(option = "http", description = "Configures the http protocol to be allowed.")
    public abstract Property<Boolean> getHttp();

    @Option(option = "url", description = "Configures the URL to send the request to.")
    public void setUrl(String url) {
        if (!getHttp().getOrElse(true) && url.startsWith("http://")) {
            throw new IllegalArgumentException("HTTP is not allowed");
        } else {
            this.url = url;
        }
    }

    @Input
    public String getUrl() {
        return url;
    }

    @Option(option = "output-type", description = "Configures the output type.")
    public void setOutputType(OutputType outputType) {
        this.outputType = outputType;
    }

    @OptionValues("output-type")
    public List<OutputType> getAvailableOutputTypes() {
        return new ArrayList<OutputType>(Arrays.asList(OutputType.values()));
    }

    @Input
    public OutputType getOutputType() {
        return outputType;
    }

    @TaskAction
    public void process() {
        getLogger().quiet("Writing out the URL response from '{}' to '{}'", url, outputType);

        // retrieve content from URL and write to output
    }

    private static enum OutputType {
        CONSOLE, FILE
    }
}
```

### [](https://docs.gradle.org/userguide/custom_tasks.html#sec:listing_task_options)[Listing command line options](https://docs.gradle.org/userguide/custom_tasks.html#sec:listing_task_options)

Command line options using the annotations [Option](https://docs.gradle.org/javadoc/org/gradle/api/tasks/options/Option.html) and [OptionValues](https://docs.gradle.org/javadoc/org/gradle/api/tasks/options/OptionValues.html) are self-documenting.

You will see [declared options](https://docs.gradle.org/userguide/custom_tasks.html#sec:declaring_task_option) and their [available values](https://docs.gradle.org/userguide/custom_tasks.html#sec:documenting_available_task_option_values) reflected in the console output of the `help` task. The output renders options alphabetically, except for boolean disable options, which appear following the enable option:

```bash
./gradlew -q help --task processUrl
```

```text
Detailed task information for processUrl

Path
     :processUrl

Type
     UrlProcess (UrlProcess)

Options
     --http     Configures the http protocol to be allowed.

     --no-http     Disables option --http.

     --output-type     Configures the output type.
                       Available values are:
                            CONSOLE
                            FILE

     --url     Configures the URL to send the request to.

     --rerun     Causes the task to be re-run even if up-to-date.

Description
     -

Group
     -
```

### [](https://docs.gradle.org/userguide/custom_tasks.html#limitations)[Limitations](https://docs.gradle.org/userguide/custom_tasks.html#limitations)

Support for declaring command line options currently comes with a few limitations.

* Command line options can only be declared for custom tasks via annotation. There’s no programmatic equivalent for defining options.

* Options cannot be declared globally, e.g., on a project level or as part of a plugin.

* When assigning an option on the command line, the task exposing the option needs to be spelled out explicitly, e.g., `gradle check --tests abc` does not work even though the `check` task depends on the `test` task.

* If you specify a task option name that conflicts with the name of a built-in Gradle option, use the `--` delimiter before calling your task to reference that option. For more information, see [Disambiguate Task Options from Built-in Options](https://docs.gradle.org/userguide/command_line_interface.html#sec:disambiguate_task_options_from_built_in_options).

[](https://docs.gradle.org/userguide/custom_tasks.html#verification_failures)[Verification failures](https://docs.gradle.org/userguide/custom_tasks.html#verification_failures)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Normally, exceptions thrown during task execution result in a failure that immediately terminates a build. The outcome of the task will be `FAILED`, the result of the build will be `FAILED`, and no further tasks will be executed. When [running with the `--continue` flag](https://docs.gradle.org/userguide/command_line_interface.html#sec:continue_build_on_failure), Gradle will continue to run other requested tasks in the build after encountering a task failure. However, any tasks that depend on a failed task will not be executed.

There is a special type of exception that behaves differently when downstream tasks only rely on the outputs of a failing task. A task can throw a subtype of [VerificationException](https://docs.gradle.org/javadoc/org/gradle/api/tasks/VerificationException.html) to indicate that it has failed in a controlled manner such that its output is still valid for consumers. A task depends on the **outcome** of another task when it directly depends on it using `dependsOn`. When Gradle is run with `--continue`, consumer tasks that depend on a producer task’s output (via a relationship between task inputs and outputs) can still run after the producer fails.

A failed unit test, for instance, will cause a failing outcome for the test task. However, this doesn’t prevent another task from reading and processing the (valid) test results the task produced. Verification failures are used in exactly this manner by the [`Test Report Aggregation Plugin`](https://docs.gradle.org/userguide/test_report_aggregation_plugin.html#test_report_aggregation_plugin).

Verification failures are also useful for tasks that need to report a failure even after producing useful output consumable by other tasks.

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
val process = tasks.register("process") {
    val outputFile = layout.buildDirectory.file("processed.log")
    outputs.files(outputFile) (1)

    doLast {
        val logFile = outputFile.get().asFile
        logFile.appendText("Step 1 Complete.") (2)
        throw VerificationException("Process failed!") (3)
        logFile.appendText("Step 2 Complete.") (4)
    }
}

tasks.register("postProcess") {
    inputs.files(process) (5)

    doLast {
        println("Results: ${inputs.files.singleFile.readText()}") (6)
    }
}
```

build.gradle

```groovy
tasks.register("process") {
    def outputFile = layout.buildDirectory.file("processed.log")
    outputs.files(outputFile) (1)

    doLast {
        def logFile = outputFile.get().asFile
        logFile << "Step 1 Complete." (2)
        throw new VerificationException("Process failed!") (3)
        logFile << "Step 2 Complete." (4)
    }
}

tasks.register("postProcess") {
    inputs.files(tasks.named("process")) (5)

    doLast {
        println("Results: ${inputs.files.singleFile.text}") (6)
    }
}
```

```bash
./gradlew postProcess --continue
```

```text
> Task :process FAILED

> Task :postProcess
Results: Step 1 Complete.
2 actionable tasks: 2 executed

FAILURE: Build failed with an exception.
```

**1****Register Output**: The `process` task writes its output to a log file.
**2****Modify Output**: The task writes to its output file as it executes.
**3****Task Failure**: The task throws a `VerificationException` and fails at this point.
**4****Continue to Modify Output**: This line never runs due to the exception stopping the task.
**5****Consume Output**: The `postProcess` task depends on the output of the `process` task due to using that task’s outputs as its own inputs.
**6****Use Partial Result**: With the `--continue` flag set, Gradle still runs the requested `postProcess` task despite the `process` task’s failure. `postProcess` can read and display the partial (though still valid) result.

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
