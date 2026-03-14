# Source: https://docs.gradle.org/userguide/part1_gradle_init_project.html

Title: Part 1: Initializing the Project

URL Source: https://docs.gradle.org/userguide/part1_gradle_init_project.html

Markdown Content:
Part 1: Initializing the Project
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* 9.4.0[9.0.0](https://docs.gradle.org/9.0.0) [8.14.4](https://docs.gradle.org/8.14.4) [7.6.6](https://docs.gradle.org/7.6.6) [Latest version](https://docs.gradle.org/current/userguide/) [All versions](https://gradle.org/releases/)  

* [](https://docs.gradle.org/userguide/part1_gradle_init_project.html "Theme")
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

* [Beginner Tutorial](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
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
* [Upgrading Gradle](https://docs.gradle.org/userguide/part1_gradle_init_project.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/part1_gradle_init_project.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/part1_gradle_init_project.html#running-introduction)
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

* [Writing Build Scripts](https://docs.gradle.org/userguide/part1_gradle_init_project.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/part1_gradle_init_project.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/part1_gradle_init_project.html#gradle-core)
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

* [DSLs and APIs](https://docs.gradle.org/userguide/part1_gradle_init_project.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/part1_gradle_init_project.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/part1_gradle_init_project.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/part1_gradle_init_project.html#plugin-development)
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

* [Dependencies](https://docs.gradle.org/userguide/part1_gradle_init_project.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/part1_gradle_init_project.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/part1_gradle_init_project.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/part1_gradle_init_project.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/part1_gradle_init_project.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/part1_gradle_init_project.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/part1_gradle_init_project.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/part1_gradle_init_project.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/part1_gradle_init_project.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/part1_gradle_init_project.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/part1_gradle_init_project.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/part1_gradle_init_project.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/part1_gradle_init_project.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/part1_gradle_init_project.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/part1_gradle_init_project.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/part1_gradle_init_project.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/part1_gradle_init_project.html#advanced-topics)
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
* [Build Cache](https://docs.gradle.org/userguide/part1_gradle_init_project.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/part1_gradle_init_project.html#configuration-cache)
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
* [APIs](https://docs.gradle.org/userguide/part1_gradle_init_project.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/part1_gradle_init_project.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/part1_gradle_init_project.html#how-to)
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

Part 1: Initializing the Project
================================

version 9.4.0

On this Page

* [Step 0. Before you Begin](https://docs.gradle.org/userguide/part1_gradle_init_project.html#part1_begin)
* [Step 1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_1_initializing_the_project)
* [Step 2. Understanding the Directory layout](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_2_understanding_the_directory_layout)
* [Step 3. Review the Gradle Files](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_3_review_the_gradle_files)
* [Step 4. Review the Code](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_4_review_the_code)
* [Step 5. Run the App](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_5_run_the_app)
* [Step 6. Bundle the App](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_bundle_the_app)
* [Step 6. Publish a Build Scan](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_publish_a_build_scan)

Learn the basics of authoring Gradle by first creating a Java app using Gradle init.

**In this section, you will:**

* Initialize a Java project

* Review the directory layout

* Run a Java application

* Produce a Build Scan

* Bundle the application in an archive

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#part1_begin)[Step 0. Before you Begin](https://docs.gradle.org/userguide/part1_gradle_init_project.html#part1_begin)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Make sure you have [Gradle installed](https://docs.gradle.org/userguide/installation.html#installation).

2. Install [IntelliJ IDEA](https://www.jetbrains.com/idea/download/). The Community Edition is a free version of IntelliJ IDEA.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_1_initializing_the_project)[Step 1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_1_initializing_the_project)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Create a new directory called `authoring-tutorial` and `cd` into it:

```bash
mkdir authoring-tutorial
```

```bash
cd authoring-tutorial
```

Run `gradle init` with parameters to generate a Java application:

```option
Kotlin
```

```option
Groovy
```

```kotlin
gradle init --type java-application  --dsl kotlin
```

```groovy
gradle init --type java-application  --dsl groovy
```

Select defaults for any additional prompts.

In this tutorial, all examples are macOS based.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_2_understanding_the_directory_layout)[Step 2. Understanding the Directory layout](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_2_understanding_the_directory_layout)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The **project root directory** contains all source files from your project.

When you are done with Gradle `init`, the directory should look as follows:

```option
Kotlin
```

```option
Groovy
```

```kotlin
.
├── gradle                              (1)
    ├── libs.versions.toml              (2)
│   └── wrapper
├── gradlew                             (3)
├── gradlew.bat                         (3)
├── settings.gradle.kts                 (4)
└── app
    ├── build.gradle.kts                (5)
    └── src
        ├── main
        │   └── java                    (6)
        │       └── demo
        │           └── App.java
        └── test
            └── java                    (7)
                └── demo
                    └── AppTest.java
```

**1**Generated folder for wrapper files
**2**Version catalog for dependencies
**3**Gradle wrapper start scripts
**4**Settings file to define build name and subprojects
**5**Build script for `app` subproject
**6**Default Java source folder for `app` subproject
**7**Default Java test source folder for `app` subproject

```groovy
.
├── gradle                              (1)
    ├── libs.versions.toml              (2)
│   └── wrapper
├── gradlew                             (3)
├── gradlew.bat                         (3)
├── settings.gradle                     (4)
└── app
    ├── build.gradle                    (5)
    └── src
        ├── main
        │   └── java                    (6)
        │       └── demo
        │           └── App.java
        └── test
            └── java                    (7)
                └── demo
                    └── AppTest.java
```

**1**Generated folder for wrapper files
**2**Version catalog for dependencies
**3**Gradle wrapper start scripts
**4**Settings file to define build name and subprojects
**5**Build script for `app` subproject
**6**Default Java source folder for `app` subproject
**7**Default Java test source folder for `app` subproject

The `authoring-tutorial` folder is the **root project directory**. Inside the root project directory are one or more subprojects, build scripts, and the Gradle wrapper.

While the Gradle Wrapper is local to the root project, the Gradle executable is found in the `GRADLE_USER_HOME`.

The `GRADLE_USER_HOME`, which defaults to `USER_HOME/.gradle`, is also where Gradle stores its global configuration properties, initialization scripts, caches, log files and more.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_3_review_the_gradle_files)[Step 3. Review the Gradle Files](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_3_review_the_gradle_files)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `settings.gradle(.kts)` file has two interesting lines:

```option
Kotlin
```

```option
Groovy
```

settings.gradle.kts

```kotlin
rootProject.name = "authoring-tutorial"
include("app")
```

settings.gradle

```groovy
rootProject.name = 'authoring-tutorial'
include('app')
```

* `rootProject.name` assigns a name to the build, overriding the default behavior of naming the build after its directory name.

* `include("app")` defines that the build consists of one subproject called `app` that contains its own source code and build logic.

More subprojects can be added by additional `include()` statements.

Our build contains one subproject called `app` representing the Java application we are building. It is configured in the `app/build.gradle(.kts)` file:

```option
Kotlin
```

```option
Groovy
```

build.gradle.kts

```kotlin
plugins {
    id("application")                                               (1)
}

repositories {
    mavenCentral()                                                  (2)
}

dependencies {
    testImplementation(libs.junit.jupiter)                          (3)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
    implementation(libs.guava)                                      (4)
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)                (5)
    }
}

application {
    mainClass = "org.example.App"                                   (6)
}

tasks.named<Test>("test") {
    useJUnitPlatform()                                              (7)
}
```

**1**Apply the application plugin to add support for building a CLI application in Java.
**2**Use Maven Central for resolving dependencies.
**3**Use JUnit Jupiter for testing (using the version catalog).
**4**This dependency is used by the application (referred using the version catalog).
**5**Define the toolchain version.
**6**Define the main class for the application.
**7**Use JUnit Platform for unit tests.

```groovy
plugins {
    id 'application'                                                (1)
}

repositories {
    mavenCentral()                                                  (2)
}

dependencies {
    testImplementation libs.junit.jupiter                           (3)
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
    implementation libs.guava                                       (4)
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)                (5)
    }
}

application {
    mainClass = 'org.example.App'                                   (6)
}

tasks.named('test') {
    useJUnitPlatform()                                              (7)
}
```

**1**Apply the application plugin to add support for building a CLI application in Java.
**2**Use Maven Central for resolving dependencies.
**3**Use JUnit Jupiter for testing (using the version catalog).
**4**This dependency is used by the application (referred using the version catalog).
**5**Define the toolchain version.
**6**Define the main class for the application.
**7**Use JUnit Platform for unit tests.

The build script in the `app` subproject directory declares the dependencies the `app` code will need to be assembled and tested.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_4_review_the_code)[Step 4. Review the Code](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_4_review_the_code)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The file `app/src/main/java/authoring/tutorial/App.java` contains the main class of the project:

App.java

```java
package authoring.tutorial;

public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting());
    }
}
```

The code prints out a simple "Hello World" greeting to the screen.

A test class is available at `app/src/test/java/authoring/tutorial/AppTest.java`:

AppTest.java

```java
package authoring.tutorial;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test void appHasAGreeting() {
        App classUnderTest = new App();
        assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
    }
}
```

The generated test class has a single _JUnit Jupiter_ test. The test instantiates the `App` class, invokes a method on it, and checks that it returns the expected value.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_5_run_the_app)[Step 5. Run the App](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_5_run_the_app)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Application plugin, which was automatically added by `gradle init`, facilitates creating an executable JVM application:

```option
Kotlin
```

```option
Groovy
```

```kotlin
plugins {
    id("application")
}
```

```groovy
plugins {
    id 'application'
}
```

Applying the Application plugin implicitly applies the Java plugin and adds tasks like `assemble`, `build`, and `run` to our project.

Thanks to the `application` plugin, you can run the application directly from the command line. The `run` task tells Gradle to execute the `main` method in the class assigned to the `mainClass` property.

```bash
./gradlew run
```

```text
> Task :app:run
Hello World!

BUILD SUCCESSFUL in 998ms
2 actionable tasks: 2 executed
```

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_bundle_the_app)[Step 6. Bundle the App](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_bundle_the_app)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `application` plugin packages the application, with all its dependencies, for you. The archive will also contain a script to start the application with a single command.

Run `./gradlew build`:

```bash
./gradlew build
```

```text
> Task :app:compileJava
> Task :app:processResources NO-SOURCE
> Task :app:classes
> Task :app:jar
> Task :app:startScripts
> Task :app:distTar
> Task :app:distZip
> Task :app:assemble
> Task :app:compileTestJava
> Task :app:processTestResources NO-SOURCE
> Task :app:testClasses
> Task :app:test
> Task :app:check
> Task :app:build

BUILD SUCCESSFUL in 5s
```

If you run a full build as shown above, Gradle will have produced the archive in two formats: `app/build/distributions/app.tar` and `app/build/distributions/app.zip`.

[](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_publish_a_build_scan)[Step 6. Publish a Build Scan](https://docs.gradle.org/userguide/part1_gradle_init_project.html#step_6_publish_a_build_scan)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The best way to learn more about what your build is doing behind the scenes is to publish a [Build Scan](https://scans.gradle.com/). To do so, run the `build` task again with the `--scan` flag.

```bash
./gradlew build --scan
```

```text
> Task :app:compileJava UP-TO-DATE
> Task :app:processResources NO-SOURCE
> Task :app:classes UP-TO-DATE
> Task :app:jar UP-TO-DATE
> Task :app:startScripts UP-TO-DATE
> Task :app:distTar UP-TO-DATE
> Task :app:distZip UP-TO-DATE
> Task :app:assemble UP-TO-DATE
> Task :app:compileTestJava UP-TO-DATE
> Task :app:processTestResources NO-SOURCE
> Task :app:testClasses UP-TO-DATE
> Task :app:test UP-TO-DATE
> Task :app:check UP-TO-DATE
> Task :app:build UP-TO-DATE

BUILD SUCCESSFUL in 1s
7 actionable tasks: 7 up-to-date
Resolving local hostname is slow, see https://gradle.com/help/gradle-slow-host-name

Publishing a Build Scan to scans.gradle.com requires accepting the Gradle Terms of Service defined at https://gradle.com/terms-of-service. Do you accept these terms? [yes, no] yes

Gradle Terms of Service accepted.

Publishing Build Scan...
https://gradle.com/s/link
```

Click the link and explore which tasks were executed, which dependencies were downloaded, and many more details:

![Image 2: build scan 3](https://docs.gradle.org/userguide/img/build-scan-3.png)

**Next Step:**[The Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html#part2_build_lifecycle)>>

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
