# Source: https://docs.gradle.org/userguide/part5_build_scripts.html

Title: Part 5: Writing a Build Script

URL Source: https://docs.gradle.org/userguide/part5_build_scripts.html

Markdown Content:
Part 5: Writing a Build Script
===============

[](https://docs.gradle.org/ "Gradle Docs")

User Manual

* [](https://docs.gradle.org/userguide/part5_build_scripts.html "Theme")
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

* [Beginner Tutorial](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init.html)
  * [2. Running Tasks](https://docs.gradle.org/userguide/part2_gradle_tasks.html)
  * [3. Understanding Dependencies](https://docs.gradle.org/userguide/part3_gradle_dep_man.html)
  * [4. Applying Plugins](https://docs.gradle.org/userguide/part4_gradle_plugins.html)
  * [5. Exploring Incremental Builds](https://docs.gradle.org/userguide/part5_gradle_inc_builds.html)
  * [6. Enabling the Build Cache](https://docs.gradle.org/userguide/part6_gradle_caching.html)

* [Intermediate Tutorial](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [1. Initializing the Project](https://docs.gradle.org/userguide/part1_gradle_init_project.html)
  * [2. Understanding the Build Lifecycle](https://docs.gradle.org/userguide/part2_build_lifecycle.html)
  * [3. Multi-Project Builds](https://docs.gradle.org/userguide/part3_multi_project_builds.html)
  * [4. Writing the Settings File](https://docs.gradle.org/userguide/part4_settings_file.html)
  * [5. Writing a Build Script](https://docs.gradle.org/userguide/part5_build_scripts.html)
  * [6. Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html)
  * [7. Writing Plugins](https://docs.gradle.org/userguide/part7_writing_plugins.html)

* [Advanced Tutorial](https://docs.gradle.org/userguide/part5_build_scripts.html)
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
* [Upgrading Gradle](https://docs.gradle.org/userguide/part5_build_scripts.html#upgrading-gradle)
  * [Within versions 9.x.y](https://docs.gradle.org/userguide/upgrading_version_9.html)
  * [To version 9.0.0](https://docs.gradle.org/userguide/upgrading_major_version_9.html)
  * [Within versions 8.x](https://docs.gradle.org/userguide/upgrading_version_8.html)
  * [From version 7.x to 8.0](https://docs.gradle.org/userguide/upgrading_version_7.html)
  * [From version 6.x to 7.0](https://docs.gradle.org/userguide/upgrading_version_6.html)
  * [From version 5.x to 6.0](https://docs.gradle.org/userguide/upgrading_version_5.html)
  * [From version 4.x to 5.0](https://docs.gradle.org/userguide/upgrading_version_4.html)

* [Migrating to Gradle](https://docs.gradle.org/userguide/part5_build_scripts.html#migrating-to-gradle)
  * [from Maven](https://docs.gradle.org/userguide/migrating_from_maven.html)
  * [from Ant](https://docs.gradle.org/userguide/migrating_from_ant.html)

* [Compatibility Notes](https://docs.gradle.org/userguide/compatibility.html)
* [Gradle's Feature Lifecycle](https://docs.gradle.org/userguide/feature_lifecycle.html)

### Gradle Fundamentals

* [Learning Gradle Basics](https://docs.gradle.org/userguide/part5_build_scripts.html#running-introduction)
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

* [Writing Build Scripts](https://docs.gradle.org/userguide/part5_build_scripts.html#beyond-the-basics)
  * [1. Anatomy of a Gradle Build](https://docs.gradle.org/userguide/gradle_directories_intermediate.html)
  * [2. Structuring Multi-Project Builds](https://docs.gradle.org/userguide/multi_project_builds_intermediate.html)
  * [3. Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle_intermediate.html)
  * [4. Writing Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html)
  * [5. Gradle Managed Types](https://docs.gradle.org/userguide/gradle_managed_types_intermediate.html)
  * [6. Declaring Dependencies](https://docs.gradle.org/userguide/dependencies_intermediate.html)
  * [7. Creating and Registering Tasks](https://docs.gradle.org/userguide/writing_tasks_intermediate.html)
  * [8. Working with Plugins](https://docs.gradle.org/userguide/plugins_intermediate.html)

* [Creating Plugins](https://docs.gradle.org/userguide/part5_build_scripts.html#deep-dive)
  * [1. Plugin Introduction](https://docs.gradle.org/userguide/plugin_introduction_advanced.html)
  * [2. Pre-Compiled Script Plugins](https://docs.gradle.org/userguide/pre_compiled_script_plugin_advanced.html)
  * [3. Binary Plugins](https://docs.gradle.org/userguide/binary_plugin_advanced.html)
  * [4. Developing Binary Plugins](https://docs.gradle.org/userguide/developing_binary_plugin_advanced.html)
  * [5. Testing Binary Plugins](https://docs.gradle.org/userguide/testing_binary_plugin_advanced.html)
  * [6. Publishing Binary Plugins](https://docs.gradle.org/userguide/publishing_binary_plugin_advanced.html)

### Gradle Reference

* [Runtime and Configuration](https://docs.gradle.org/userguide/part5_build_scripts.html#gradle-core)
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

* [DSLs and APIs](https://docs.gradle.org/userguide/part5_build_scripts.html#dsl-and-apis)
  * [Java API](https://docs.gradle.org/javadoc/index.html?overview-summary.html)
  * [Groovy DSL Primer](https://docs.gradle.org/userguide/groovy_build_script_primer.html)
  * [Groovy DSL](https://docs.gradle.org/dsl/index.html)
  * [Kotlin DSL Primer](https://docs.gradle.org/userguide/kotlin_dsl.html)
  * [Kotlin DSL](https://docs.gradle.org/kotlin-dsl/index.html)
  * [Public APIs](https://docs.gradle.org/userguide/public_apis.html)
  * [Default Script Imports](https://docs.gradle.org/userguide/default_script_imports.html)
  * [Groovy to Kotlin DSL Migration](https://docs.gradle.org/userguide/migrating_from_groovy_to_kotlin_dsl.html)

* [Gradle Managed Types](https://docs.gradle.org/userguide/part5_build_scripts.html#types-and-objects)
  * [Lazy vs Eager Evaluation](https://docs.gradle.org/userguide/lazy_eager_evaluation.html)
  * [Properties and Providers](https://docs.gradle.org/userguide/properties_providers.html)
  * [Collections](https://docs.gradle.org/userguide/collections.html)
  * [Services and Service Injection](https://docs.gradle.org/userguide/service_injection.html)
  * [Dataflow Actions](https://docs.gradle.org/userguide/dataflow_actions.html)
  * [Working with Files](https://docs.gradle.org/userguide/working_with_files.html)

* [Tasks](https://docs.gradle.org/userguide/part5_build_scripts.html#task-development)
  * [Understanding Tasks](https://docs.gradle.org/userguide/more_about_tasks.html)
  * [Controlling Task Execution](https://docs.gradle.org/userguide/controlling_task_execution.html)
  * [Organizing Tasks](https://docs.gradle.org/userguide/organizing_tasks.html)
  * [Implementing Custom Tasks](https://docs.gradle.org/userguide/implementing_custom_tasks.html)
  * [Lazy Configuration](https://docs.gradle.org/userguide/lazy_configuration.html)
  * [Parallel Task Execution](https://docs.gradle.org/userguide/worker_api.html)
  * [Advanced Task Development](https://docs.gradle.org/userguide/custom_tasks.html)
  * [Shared Build Services](https://docs.gradle.org/userguide/build_services.html)

* [Plugins](https://docs.gradle.org/userguide/part5_build_scripts.html#plugin-development)
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

* [Dependencies](https://docs.gradle.org/userguide/part5_build_scripts.html#managing-dependencies)
  * [Getting Started](https://docs.gradle.org/userguide/getting_started_dep_man.html)
  * [Learning the Basics](https://docs.gradle.org/userguide/part5_build_scripts.html#learning-the-basics-dependency-management)
    * [1. Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies.html)
    * [2. Dependency Configurations](https://docs.gradle.org/userguide/dependency_configurations.html)
    * [3. Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories.html)
    * [4. Centralizing Dependencies](https://docs.gradle.org/userguide/centralizing_dependencies.html)
    * [5. Dependency Constraints and Conflict Resolution](https://docs.gradle.org/userguide/dependency_constraints_conflicts.html)

  * [Advanced Concepts](https://docs.gradle.org/userguide/part5_build_scripts.html#understanding_dep_res)
    * [1. Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution.html)
    * [2. Graph Resolution](https://docs.gradle.org/userguide/graph_resolution.html)
    * [3. Variant Selection](https://docs.gradle.org/userguide/variant_aware_resolution.html)
    * [4. Artifact Resolution](https://docs.gradle.org/userguide/artifact_resolution.html)

  * [Declaring Dependencies](https://docs.gradle.org/userguide/part5_build_scripts.html#declaring-dependencies)
    * [Declaring Dependencies](https://docs.gradle.org/userguide/declaring_dependencies_basics.html)
    * [Viewing Dependencies](https://docs.gradle.org/userguide/viewing_debugging_dependencies.html)
    * [Declaring Versions and Ranges](https://docs.gradle.org/userguide/dependency_versions.html)
    * [Declaring Dependency Constraints](https://docs.gradle.org/userguide/dependency_constraints.html)
    * [Creating Dependency Configurations](https://docs.gradle.org/userguide/declaring_configurations.html)
    * [Gradle Distribution-Specific Dependencies](https://docs.gradle.org/userguide/gradle_dependencies.html)

  * [Declaring Repositories](https://docs.gradle.org/userguide/part5_build_scripts.html#declaring-repositories)
    * [Declaring Repositories](https://docs.gradle.org/userguide/declaring_repositories_basics.html)
    * [Centralizing Repository Declarations](https://docs.gradle.org/userguide/centralizing_repositories.html)
    * [Repository Types](https://docs.gradle.org/userguide/supported_repository_types.html)
    * [Metadata Formats](https://docs.gradle.org/userguide/supported_metadata_formats.html)
    * [Supported Protocols](https://docs.gradle.org/userguide/supported_repository_protocols.html)
    * [Filtering Repository Content](https://docs.gradle.org/userguide/filtering_repository_content.html)

  * [Centralizing Dependencies](https://docs.gradle.org/userguide/part5_build_scripts.html#centralizing-dependencies)
    * [Creating Platforms](https://docs.gradle.org/userguide/platforms.html)
    * [Creating Version Catalogs](https://docs.gradle.org/userguide/version_catalogs.html)
    * [Using Catalogs with Platforms](https://docs.gradle.org/userguide/centralizing_catalog_platform.html)

  * [Managing Dependencies](https://docs.gradle.org/userguide/part5_build_scripts.html#dependency-management)
    * [Locking Versions](https://docs.gradle.org/userguide/dependency_locking.html)
    * [Using Resolution Rules](https://docs.gradle.org/userguide/resolution_rules.html)
    * [Modifying Dependency Metadata](https://docs.gradle.org/userguide/component_metadata_rules.html)
    * [Caching Dependencies](https://docs.gradle.org/userguide/dependency_caching.html)

  * [Controlling Dependency Resolution](https://docs.gradle.org/userguide/part5_build_scripts.html#dependency-resolution)
    * [Consistent Dependency Resolution](https://docs.gradle.org/userguide/dependency_resolution_consistency.html)
    * [Resolving Specific Artifacts](https://docs.gradle.org/userguide/resolving_specific_artifacts.html)
    * [Capabilities](https://docs.gradle.org/userguide/component_capabilities.html)
    * [Variants and Attributes](https://docs.gradle.org/userguide/variant_attributes.html)
    * [Artifact Views](https://docs.gradle.org/userguide/artifact_views.html)
    * [Artifact Transforms](https://docs.gradle.org/userguide/artifact_transforms.html)

  * [Publishing Libraries](https://docs.gradle.org/userguide/part5_build_scripts.html#publishing)
    * [Setting up Publishing](https://docs.gradle.org/userguide/publishing_setup.html)
    * [Understanding Gradle Module Metadata](https://docs.gradle.org/userguide/publishing_gradle_module_metadata.html)
    * [Signing Artifacts](https://docs.gradle.org/userguide/publishing_signing.html)
    * [Customizing Publishing](https://docs.gradle.org/userguide/publishing_customization.html)
    * [Maven Publish Plugin](https://docs.gradle.org/userguide/publishing_maven.html)
    * [Ivy Publish Plugin](https://docs.gradle.org/userguide/publishing_ivy.html)

* [Platforms](https://docs.gradle.org/userguide/part5_build_scripts.html#platformst)
  * [JVM Builds](https://docs.gradle.org/userguide/part5_build_scripts.html#jvm)
    * [Building Java & JVM projects](https://docs.gradle.org/userguide/building_java_projects.html)
    * [Testing Java & JVM projects](https://docs.gradle.org/userguide/java_testing.html)
    * [Java Toolchains](https://docs.gradle.org/userguide/part5_build_scripts.html#java-toolchains)
      * [Toolchains for JVM projects](https://docs.gradle.org/userguide/toolchains.html)
      * [Toolchain Resolver Plugins](https://docs.gradle.org/userguide/toolchain_plugins.html)

    * [Managing Dependencies](https://docs.gradle.org/userguide/dependency_management_for_java_projects.html)
    * [JVM Plugins](https://docs.gradle.org/userguide/part5_build_scripts.html#jvm-plugins)
      * [Java Library Plugin](https://docs.gradle.org/userguide/java_library_plugin.html)
      * [Java Application Plugin](https://docs.gradle.org/userguide/application_plugin.html)
      * [Java Platform Plugin](https://docs.gradle.org/userguide/java_platform_plugin.html)
      * [Groovy Plugin](https://docs.gradle.org/userguide/groovy_plugin.html)
      * [Scala Plugin](https://docs.gradle.org/userguide/scala_plugin.html)

  * [C++ Builds](https://docs.gradle.org/userguide/part5_build_scripts.html#cpp)
    * [Building C++ projects](https://docs.gradle.org/userguide/building_cpp_projects.html)
    * [Testing C++ projects](https://docs.gradle.org/userguide/cpp_testing.html)

  * [Swift Builds](https://docs.gradle.org/userguide/part5_build_scripts.html#swift)
    * [Building Swift projects](https://docs.gradle.org/userguide/building_swift_projects.html)
    * [Testing Swift projects](https://docs.gradle.org/userguide/swift_testing.html)

* [Best Practices](https://docs.gradle.org/userguide/part5_build_scripts.html#best-practices)
  * [Introduction](https://docs.gradle.org/userguide/best_practices.html)
  * [Index](https://docs.gradle.org/userguide/best_practices_index.html)
  * [General Best Practices](https://docs.gradle.org/userguide/best_practices_general.html)
  * [Best Practices for Structuring Builds](https://docs.gradle.org/userguide/best_practices_structuring_builds.html)
  * [Best Practices for Dependencies](https://docs.gradle.org/userguide/best_practices_dependencies.html)
  * [Best Practices for Tasks](https://docs.gradle.org/userguide/best_practices_tasks.html)
  * [Best Practices for Performance](https://docs.gradle.org/userguide/best_practices_performance.html)
  * [Best Practices for Security](https://docs.gradle.org/userguide/best_practices_security.html)

* [Other Topics](https://docs.gradle.org/userguide/part5_build_scripts.html#advanced-topics)
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
* [Build Cache](https://docs.gradle.org/userguide/part5_build_scripts.html#build-cache)
  * [Enabling and Configuring](https://docs.gradle.org/userguide/build_cache.html)
  * [Why use the Build Cache?](https://docs.gradle.org/userguide/build_cache_use_cases.html)
  * [Understanding the Impact](https://docs.gradle.org/userguide/build_cache_performance.html)
  * [Learning Basic Concepts](https://docs.gradle.org/userguide/build_cache_concepts.html)
  * [Caching Java Project](https://docs.gradle.org/userguide/caching_java_projects.html)
  * [Caching Android Project](https://docs.gradle.org/userguide/caching_android_projects.html)
  * [Debugging Caching Issues](https://docs.gradle.org/userguide/build_cache_debugging.html)
  * [Troubleshooting](https://docs.gradle.org/userguide/common_caching_problems.html)

* [Configuration Cache](https://docs.gradle.org/userguide/part5_build_scripts.html#configuration-cache)
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
* [APIs](https://docs.gradle.org/userguide/part5_build_scripts.html#third-party-api)
  * [Tooling API](https://docs.gradle.org/userguide/tooling_api.html)
  * [Test Reporting API](https://docs.gradle.org/userguide/test_reporting_api.html)

### How-To-Guides

* [Structuring Builds](https://docs.gradle.org/userguide/part5_build_scripts.html#how-to-guides)
  * [Convert a Single-Project Build to Multi-Project](https://docs.gradle.org/userguide/how_to_convert_single_build_to_multi_build.html)

* [Dependency Management](https://docs.gradle.org/userguide/part5_build_scripts.html#how-to)
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

Part 5: Writing a Build Script
==============================

version 9.4.0

On this Page

* [Step 0. Before you Begin](https://docs.gradle.org/userguide/part5_build_scripts.html#part5_begin)
* [Step 1. The `Project` object](https://docs.gradle.org/userguide/part5_build_scripts.html#step_1_the_project_object)
* [Step 2. The Build script](https://docs.gradle.org/userguide/part5_build_scripts.html#step_2_the_build_script)
* [Step 3. Update the Build scripts](https://docs.gradle.org/userguide/part5_build_scripts.html#step_3_update_the_build_scripts)
* [Step 4. Apply the Plugin](https://docs.gradle.org/userguide/part5_build_scripts.html#step_4_apply_the_plugin)
* [Step 5. View Plugin Task](https://docs.gradle.org/userguide/part5_build_scripts.html#step_5_view_plugin_task)
* [Step 6. View Plugin Tasks](https://docs.gradle.org/userguide/part5_build_scripts.html#step_6_view_plugin_tasks)

Learn the basics of authoring Gradle by developing the Build Script.

**In this section, you will:**

* Understand the Project object

* Update the Build script

* Update the Plugin

* Apply the Plugin

* Run a task from the Plugin

[](https://docs.gradle.org/userguide/part5_build_scripts.html#part5_begin)[Step 0. Before you Begin](https://docs.gradle.org/userguide/part5_build_scripts.html#part5_begin)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. You initialized your Java app in [part 1](https://docs.gradle.org/userguide/part1_gradle_init_project.html#part1_begin).

2. You understand the Gradle Build Lifecycle from [part 2](https://docs.gradle.org/userguide/part2_build_lifecycle.html#part2_begin).

3. You added a subproject and a separate Build in [part3](https://docs.gradle.org/userguide/part3_multi_project_builds.html#part3_begin).

4. You viewed a Settings file in [part 4](https://docs.gradle.org/userguide/part4_settings_file.html#part4_begin).

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_1_the_project_object)[Step 1. The `Project` object](https://docs.gradle.org/userguide/part5_build_scripts.html#step_1_the_project_object)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Build scripts invoke Gradle APIs to configure the build.

During the configuration phase, Gradle finds the build script(s) in the root and subproject directories.

When a build script, `build.gradle(.kts)`, is found, Gradle configures a [Project](https://docs.gradle.org/javadoc/org/gradle/api/Project.html) object.

The purpose of the [Project](https://docs.gradle.org/javadoc/org/gradle/api/Project.html) object is to create a collection of [Task](https://docs.gradle.org/javadoc/org/gradle/api/Task.html) objects, apply plugins, and retrieve dependencies.

You can use any of the methods and properties on the [Project](https://docs.gradle.org/javadoc/org/gradle/api/Project.html) interface directly in your script.

For example:

```option
Kotlin
```

```option
Groovy
```

```kotlin
defaultTasks("some-task")      // Delegates to Project.defaultTasks()
reportsDir = file("reports")   // Delegates to Project.file() and the Java Plugin
```

```groovy
defaultTasks 'some-task'      // Delegates to Project.defaultTasks()
reportsDir = file('reports')  // Delegates to Project.file() and the Java Plugin
```

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_2_the_build_script)[Step 2. The Build script](https://docs.gradle.org/userguide/part5_build_scripts.html#step_2_the_build_script)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s break down the build script for the plugin:

```option
Kotlin
```

```option
Groovy
```

gradle/license-plugin/plugin/build.gradle.kts

```kotlin
plugins {                                                             (1)
    `java-gradle-plugin`                                              (2)
    id("org.jetbrains.kotlin.jvm") version "1.9.0"                    (3)
}

repositories {                                                        (4)
    mavenCentral()                                                    (5)
}

dependencies {                                                        (6)
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit5")     (7)
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

gradlePlugin {                                                        (8)
    val greeting by plugins.creating {                                (9)
        id = "license.greeting"
        implementationClass = "license.LicensePlugin"
    }
}

// Additional lines //
```

**1**Use the `plugins{}` block from [KotlinSettingsScript](https://docs.gradle.org/kotlin-dsl/gradle/org.gradle.kotlin.dsl/-kotlin-settings-script/index.html) in the Kotlin DSL
**2**Apply the Java Gradle plugin development plugin to add support for developing Gradle plugins
**3**Apply the Kotlin JVM plugin to add support for Kotlin
**4**Use [`Project.repositories()`](https://docs.gradle.org/kotlin-dsl/gradle/org.gradle.api/-project/repositories.html) to configure the repositories for this project
**5**Use [Maven Central](https://repo.maven.apache.org/maven2/) for resolving dependencies
**6**Use [`Project.dependencies()`](https://docs.gradle.org/kotlin-dsl/gradle/org.gradle.api/-project/dependencies.html) to configure the dependencies for this project
**7**Use the Kotlin JUnit 5 integration
**8**Use the `gradlePlugin{}` block from [GradlePluginDevelopmentExtension](https://docs.gradle.org/kotlin-dsl/gradle/org.gradle.plugin.devel/-gradle-plugin-development-extension/index.html) in the Kotlin DSL
**9**Define the plugin `id` and `implementationClass`

gradle/license-plugin/plugin/build.gradle

```groovy
plugins {                                                           (1)
    id 'java-gradle-plugin'                                         (2)
    id 'groovy'                                                     (3)
}

repositories {                                                      (4)
    mavenCentral()                                                  (5)
}

dependencies {                                                      (6)
    testImplementation libs.spock.core
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
}

gradlePlugin {                                                      (7)
    plugins {
        greeting {
            id = 'license.greeting'                                 (8)
            implementationClass = 'license.LicensePlugin'
        }
    }
}

// Additional lines //
```

**1**Use the `plugins{}` block from the [PluginDependenciesSpec API](https://docs.gradle.org/dsl/org.gradle.plugin.use.PluginDependenciesSpec.html) in the Groovy DSL
**2**Apply the Java Gradle plugin development plugin to add support for developing Gradle plugins
**3**Apply the Groovy plugin to add support for Groovy
**4**Use [`Project.repositories()`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:repositories) to configure the repositories for this project
**5**Use [Maven Central](https://repo.maven.apache.org/maven2/) for resolving dependencies
**6**Use [`Project.dependencies()`](https://docs.gradle.org/dsl/org.gradle.api.Project.html#org.gradle.api.Project:dependencies) to configure the dependencies for this project
**7**Use the `gradlePlugin{}` block from the [PluginAware API](https://docs.gradle.org/dsl/org.gradle.api.plugins.PluginAware.html) in the Groovy DSL
**8**Define the plugin `id` and `implementationClass`

Plugins, which enhance your build capabilities, are included like this:

```option
Kotlin
```

```option
Groovy
```

```kotlin
plugins {
    id("java")                          // core plugin, no version required
    id("org.some.plugin") version "2.8" // community plugin, version required
}
```

```groovy
plugins {
    id 'java'                          // core plugin, no version required
    id 'org.some.plugin' version '2.8' // community plugin, version required
}
```

The repositories section lets Gradle know where to pull dependencies from:

```option
Kotlin
```

```option
Groovy
```

```kotlin
repositories {
    mavenCentral()  // get dependencies from the Maven central repository
}
```

```groovy
repositories {
    mavenCentral()  // get dependencies from the Maven central repository
}
```

Dependencies are requirements for building your application or library:

```option
Kotlin
```

```option
Groovy
```

```kotlin
dependencies {
    // group: 'org.apache.commons', name: 'commons-lang3', version: '3.13.0'
    implementation("org.apache.commons:commons-lang3:3.13.0")
}
```

```groovy
dependencies {
    // group: 'org.apache.commons', name: 'commons-lang3', version: '3.13.0'
    implementation 'org.apache.commons:commons-lang3:3.13.0'
}
```

In this example, `implementation()` means that the `commons-lang3` library must be added to the Java classpath.

Every dependency declared for a Gradle project must apply to a scope. That is, the dependency is either needed at compile time, runtime, or both. This is called a configuration and the `implementation` configuration is used when the dependency is only needed in the runtime classpath.

Configuration blocks (not to be confused with dependency configurations above) are typically used to configure an applied plugin:

```option
Kotlin
```

```option
Groovy
```

```kotlin
gradlePlugin {  // Define a custom plugin
    val greeting by plugins.creating {  // Define `greeting` plugin using the `plugins.creating` method
        id = "license.greeting" // Create plugin with the specified ID
        implementationClass = "license.LicensePlugin"   // and specified implementation class
    }
}
```

```groovy
gradlePlugin {  // Define a custom plugin
    plugins {
        greeting {  // Define a plugin named greeting
            id = 'license.greeting' // using the id
            implementationClass = 'license.LicensePlugin' // and implementationClass
        }
    }
}
```

When the `java-gradle-plugin` is applied, users must configure the plugin they are developing using the `gradlePlugin{}` configuration block.

Tasks are units of work executed during your build. They can be defined by plugins or inline:

```option
Kotlin
```

```option
Groovy
```

```kotlin
val functionalTest by tasks.registering(Test::class) {
    testClassesDirs = functionalTestSourceSet.output.classesDirs
    classpath = functionalTestSourceSet.runtimeClasspath
    useJUnitPlatform()
}

tasks.named<Test>("test") {
    // Use JUnit Jupiter for unit tests.
    useJUnitPlatform()
}
```

```groovy
tasks.register('functionalTest', Test) {
    testClassesDirs = sourceSets.functionalTest.output.classesDirs
    classpath = sourceSets.functionalTest.runtimeClasspath
    useJUnitPlatform()
}

tasks.named('test') {
    // Use JUnit Jupiter for unit tests.
    useJUnitPlatform()
}
```

In the example generated by Gradle init, we define two tasks:

1. `functionalTest`: This task is registered using `tasks.register()`. It configures the test task for functional tests.

2. `test`: This task is configured using `tasks.named()` for the existing `test` task. It also configures the task to use JUnit Jupiter for unit tests.

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_3_update_the_build_scripts)[Step 3. Update the Build scripts](https://docs.gradle.org/userguide/part5_build_scripts.html#step_3_update_the_build_scripts)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Over the following sections, we will update `LicensePlugin` to a plugin that automatically generates license headers for source code files. Let’s first update the build script with the proper name for our new `license` plugin:

```option
Kotlin
```

```option
Groovy
```

gradle/license-plugin/plugin/build.gradle.kts

```kotlin
gradlePlugin {
    val license by plugins.creating {   // Update name to license
        id = "com.tutorial.license"     // Update id to com.gradle.license
        implementationClass = "license.LicensePlugin"
    }
}
```

gradle/license-plugin/plugin/build.gradle

```groovy
gradlePlugin {
    // Define the plugin
    plugins {
        license {                       // Update name to license
            id = 'com.tutorial.license' // Update id to com.gradle.license
            implementationClass = 'license.LicensePlugin'
        }
    }
}
```

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_4_apply_the_plugin)[Step 4. Apply the Plugin](https://docs.gradle.org/userguide/part5_build_scripts.html#step_4_apply_the_plugin)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s apply our `license` plugin to the `app` subproject:

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
    id("com.tutorial.license")  // Apply the license plugin
}
```

app/build.gradle

```groovy
plugins {
    id 'application'
    id('com.tutorial.license')  // Apply the license plugin
}
```

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_5_view_plugin_task)[Step 5. View Plugin Task](https://docs.gradle.org/userguide/part5_build_scripts.html#step_5_view_plugin_task)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Build init creates a "hello world" plugin when generating a Gradle plugin project. Inside `LicensePlugin` is simply a task that prints a greeting to the console, the task name is `greeting`:

```option
Kotlin
```

```option
Groovy
```

gradle/license-plugin/plugin/src/main/kotlin/license/LicensePlugin.kt

```kotlin
class LicensePlugin: Plugin<Project> {
    override fun apply(project: Project) {                          // Apply plugin
        project.tasks.register("greeting") { task ->                // Register a task
            task.doLast {
                println("Hello from plugin 'com.tutorial.greeting'")  // Hello world printout
            }
        }
    }
}
```

gradle/license-plugin/plugin/src/main/groovy/license/LicensePlugin.groovy

```groovy
class LicensePlugin implements Plugin<Project> {
    void apply(Project project) {
        // Register a task
        project.tasks.register("greeting") {
            doLast {
                println("Hello from plugin 'com.tutorial.greeting'")
            }
        }
    }
}
```

As we can see, the `license` plugin, when applied, exposes a `greeting` task with a simple print statement.

[](https://docs.gradle.org/userguide/part5_build_scripts.html#step_6_view_plugin_tasks)[Step 6. View Plugin Tasks](https://docs.gradle.org/userguide/part5_build_scripts.html#step_6_view_plugin_tasks)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When the `license` plugin is applied to the `app` project, the `greeting` task becomes available:

To view the task in the root directory, run:

```bash
./gradlew tasks --all
```

```text
------------------------------------------------------------
Tasks runnable from root project 'authoring-tutorial'
------------------------------------------------------------
...
Other tasks
-----------
app:greeting
app:task1
app:task2
lib:task3
```

Finally, run the `greeting` task using `./gradlew greeting` or:

```bash
./gradlew :app:greeting
```

```text
> Task :app:greeting
Hello from plugin 'com.tutorial.greeting'
```

**Next Step:**[Writing Tasks](https://docs.gradle.org/userguide/part6_writing_tasks.html#part6_writing_tasks)>>

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
