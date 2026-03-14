# Source: https://docs.gradle.org/userguide/upgrading_version_6.html

Title: Upgrading from Gradle 6.x to 7.0

URL Source: https://docs.gradle.org/userguide/upgrading_version_6.html

Published Time: Wed, 04 Mar 2026 11:20:44 GMT

Markdown Content:
This chapter provides the information you need to migrate your Gradle 6.x builds to Gradle 7.0. For migrating from Gradle 5.x, see the [older migration guide](https://docs.gradle.org/current/userguide/upgrading_version_5.html#upgrading_version_5) first.

We recommend the following steps for all users:

1. Try running `gradle help --scan` and view the [deprecations view](https://docs.gradle.com/develocity/get-started/#identifying_deprecated_gradle_functionality) of the generated Build Scan.

![Image 1: Deprecations View in a Build Scan](https://docs.gradle.org/current/userguide/img/deprecations.png)
This is so that you can see any deprecation warnings that apply to your build.

Alternatively, you can run `gradle help --warning-mode=all` to see the deprecations in the console, though it may not report as much detailed information.

1. Update your plugins.

Some plugins will break with this new version of Gradle, for example because they use internal APIs that have been removed or changed. The previous step will help you identify potential problems by issuing deprecation warnings when a plugin does try to use a deprecated part of the API.

1. Run `gradle wrapper --gradle-version 7.0.2` to update the project to 7.0.2.

2. Try to run the project and debug any errors using the [Troubleshooting Guide](https://docs.gradle.org/current/userguide/troubleshooting.html#troubleshooting).

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_7.0)[Upgrading from 6.9 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_7.0)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_the_ide_integration)[Changes in the IDE integration](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_the_ide_integration)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_the_idea_model)[Changes in the IDEA model](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_the_idea_model)

The `getGeneratedSourceDirectories()` and `getGeneratedTestDirectories()` methods are removed from the `IdeaContentRoot` interface. Clients should replace these invocations with `getSourceDirectories()` and `getTestDirectories()` and use the `isGenerated()` method on the returned instances.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#locking_single)[Dependency locking now defaults to a single file per project](https://docs.gradle.org/userguide/upgrading_version_6.html#locking_single)

The format of the dependency lockfile has been changed and as a consequence there is only one file per project instead of one file per configuration per project. This change only affects _writing_ lock files. Gradle remains capable of _loading_ lock state saved in the older format.

Head over to [the documentation](https://docs.gradle.org/current/userguide/dependency_locking.html#sec:migrate-single-lockfile) to learn how to migrate to the new format. The migration can be performed per configuration and does not have to be done in a single step. Gradle will automatically clean up previous lock files when migrating them over to the new file format.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#gradle_module_metadata_is_now_reproducible_by_default)[Gradle Module Metadata is now reproducible by default](https://docs.gradle.org/userguide/upgrading_version_6.html#gradle_module_metadata_is_now_reproducible_by_default)

The `buildId` field will not be populated by default to ensure that the produced metadata file remains unchanged when no build inputs are changed. Users can still opt in to have this unique identifier part of the produced metadata if they want to, see [the documentation](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html#sub:gmm-reproducible).

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#jcenter_deprecation)[The `jcenter()` convenience method is now deprecated](https://docs.gradle.org/userguide/upgrading_version_6.html#jcenter_deprecation)

JFrog [announced](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter) the sunset of the JCenter repository in February 2021. [Many Gradle builds](https://blog.gradle.org/jcenter-shutdown) rely on JCenter for project dependencies.

No new packages or versions are published to JCenter, but JFrog says they will keep JCenter running in a read-only state indefinitely. We recommend that you consider [using](https://docs.gradle.org/current/userguide/declaring_repositories.html#three-declaring-repositories)`mavenCentral()`, `google()` or a private `maven` repository instead.

Gradle emits a deprecation warning when `jcenter()` is used as a repository and this method is scheduled to be removed in Gradle 8.0.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_to_groovy_and_groovy_dsl)[Changes to Groovy and Groovy DSL](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_to_groovy_and_groovy_dsl)

Due to the update to the next major version of Groovy, you may experience minor issues when upgrading to Gradle 7.0.

The new version of Groovy has a stricter parser that fails to compile code that may have been accepted in previous Groovy versions. If you encounter syntax errors, check the [Groovy issue tracker](https://groovy.apache.org/#reporting-issues) and [Groovy 3 release highlights](https://blogs.apache.org/groovy/entry/groovy-3-highlights).

##### [](https://docs.gradle.org/userguide/upgrading_version_6.html#groovy_modularization)[Groovy modularization](https://docs.gradle.org/userguide/upgrading_version_6.html#groovy_modularization)

Gradle no longer embeds a copy of `groovy-all` that bundles all Groovy modules into a single jar—​only the most important modules are distributed in the Gradle distribution.

The `localGroovy()` dependency will include these Groovy modules:

* `groovy`

* `groovy-ant`

* `groovy-astbuilder`

* `groovy-console`

* `groovy-datetime`

* `groovy-dateutil`

* `groovy-groovydoc`

* `groovy-json`

* `groovy-nio`

* `groovy-sql`

* `groovy-templates`

* `groovy-test`

* `groovy-xml`

But the following Groovy modules are **not** included:

* `groovy-cli-picocli`

* `groovy-docgenerator`

* `groovy-groovysh`

* `groovy-jmx`

* `groovy-jsr223`

* `groovy-macro`

* `groovy-servlet`

* `groovy-swing`

* `groovy-test-junit5`

* `groovy-testng`

You can pull these dependencies into your build like any other external dependency.

##### [](https://docs.gradle.org/userguide/upgrading_version_6.html#building_gradle_plugins_with_groovy_3)[Building Gradle plugins with Groovy 3](https://docs.gradle.org/userguide/upgrading_version_6.html#building_gradle_plugins_with_groovy_3)

Plugins built with Gradle 7.0 will now have Groovy 3 on their classpath when using `gradleApi()` or `localGroovy()`.

If you use [Spock](https://spockframework.org/) to test your plugins, you will need to use Spock 2.x. There are no compatible versions of Spock 1.x and Groovy 3.

```
dependencies {
    // Ensure you use the Groovy 3.x variant
    testImplementation('org.spockframework:spock-core:2.0-groovy-3.0') {
        exclude group: 'org.codehaus.groovy'
    }
}

// Spock 2 is based on JUnit Platform which needs to be enabled explicitly.
tasks.withType(Test).configureEach {
    useJUnitPlatform()
}
```

##### [](https://docs.gradle.org/userguide/upgrading_version_6.html#performance)[Performance](https://docs.gradle.org/userguide/upgrading_version_6.html#performance)

Depending on the number of subprojects and Groovy DSL build scripts, you may notice a performance regression when compiling build scripts for the first time or when changes are made to the build script’s classpath. This is due to the slower performance of the Groovy 3 parser, but the Groovy team is aware of the issue and trying to mitigate the regression.

In general, we are also looking at how we can improve the performance of build script compilation for both Groovy DSL and Kotlin DSL.

##### [](https://docs.gradle.org/userguide/upgrading_version_6.html#encountering_could_not_find_method_x_for_arguments_y_on_defaultdependencyhandler)[Encountering 'Could not find method X for arguments Y on DefaultDependencyHandler'](https://docs.gradle.org/userguide/upgrading_version_6.html#encountering_could_not_find_method_x_for_arguments_y_on_defaultdependencyhandler)

While the following error initially looks like a compile error, it is actually due to the fact that specific `Configuration`s have been removed. Please refer to [Removal of `compile` and `runtime` configurations](https://docs.gradle.org/userguide/upgrading_version_6.html#sec:configuration_removal) for more details.

`Could not find method testCompile() for arguments [DefaultExternalModuleDependency{group='org.junit', name='junit-bom', version='5.7.0', configuration='default'}] on object of type org.gradle.api.internal.artifacts.dsl.dependencies.DefaultDependencyHandler.`

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#sec:configuration_removal)[Removal of `compile` and `runtime` configurations](https://docs.gradle.org/userguide/upgrading_version_6.html#sec:configuration_removal)

Since its inception, Gradle provided the `compile` and `runtime` configurations to declare dependencies. These however did not support a fine grained scoping of dependencies. Hence, better replacements were introduced in Gradle 3.4:

* The `implementation` configuration should be used to declare dependencies which are _implementation details_ of a library: they are not visible to consumers of the library during compilation time.

* The `api` configuration, available only if you apply the `java-library` plugin, should be used to declare dependencies which are part of the API of a library, that need to be exposed to consumers at compilation time.

In Gradle 7, both the `compile` and `runtime` configurations are removed. Therefore, you have to migrate to the `implementation` and `api` configurations above. If you are still using the `java` plugin for a Java library, you will need to apply the `java-library` plugin instead.

Table 1. Common configuration upgrades| Removed Configuration | New Configuration |
| --- | --- |
| `compile` | `api` or `implementation` |
| `runtime` | `runtimeOnly` |
| `testRuntime` | `testRuntimeOnly` |
| `testCompile` | `testImplementation` |
| `<sourceSet>Runtime` | `<sourceSet>RuntimeOnly` |
| `<sourceSet>Compile` | `<sourceSet>Implementation` |

You can find more details about the benefits of the new configurations and which one to use in place of `compile` and `runtime` by reading the [Java Library plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html#java_library_plugin) documentation.

When using the Groovy DSL, you need to watch out for a particular upgrade problem when dealing with the removed configurations.

If you were creating custom configurations that extend one of the removed configurations, Gradle may silently create configurations that do not exist.

This looks something like:

```
configurations {
  // This silently creates a configuration called "runtime"
  myConf extendsFrom runtime
}
```

The result of dependency resolution for your custom configuration may not be the same as Gradle 6.x or before. You may notice missing dependencies or artifacts.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#location_of_temporary_project_files_for_projectbuilder)[Location of temporary project files for `ProjectBuilder`](https://docs.gradle.org/userguide/upgrading_version_6.html#location_of_temporary_project_files_for_projectbuilder)

The `ProjectBuilder` API is used for inspecting Gradle builds in unit tests. This API used to create temporary project files under the system temporary directory as defined by `java.io.tmpdir`.

The API now creates temporary project files under the `Test` task’s temporary directory. This path is usually under the project build directory. This may cause test failures when the test expects particular file paths.

If the test uses `ProjectBuilder.withProjectDir(…​)`, it is unaffected.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#location_of_temporary_files_for_testkit_tests)[Location of temporary files for TestKit tests](https://docs.gradle.org/userguide/upgrading_version_6.html#location_of_temporary_files_for_testkit_tests)

Tests that use the [TestKit](https://docs.gradle.org/current/userguide/test_kit.html#test_kit) API used to create temporary files under the system temporary directory as defined by `java.io.tmpdir`. These files were used to store copies of Gradle distributions or another test-only Gradle User Home.

TestKit tests will now create temporary files under the `Test` task’s temporary directory. This path is usually under the project build directory. This may cause test failures when the test expects particular file paths.

If the test uses `GradleRunner.withTestKitDir(…​)`, it is unaffected.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#file_system_watching_with_testkit_on_windows)[File system watching with TestKit on Windows](https://docs.gradle.org/userguide/upgrading_version_6.html#file_system_watching_with_testkit_on_windows)

The file system watching implementation on Windows adds a lock to the root project directory in order to watch for changes. This may cause errors when you try to delete the root project directory after running a build with TestKit. For example, tests that use TestKit together with JUnit’s `@TempDir` extension, or the `TemporaryFolder` rule can run into this problem. To avoid problems with these file locks, `TestKit` disables file system watching for builds executed on Windows via `GradleRunner`. If you’d like to override the default behavior, you can enable file system watching by passing `--watch-fs` to `GradleRunner.withArguments()`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_the_legacy_maven_plugin)[Removal of the legacy `maven` plugin](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_the_legacy_maven_plugin)

The `maven` plugin has been removed. You should use the `maven-publish` plugin instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_the_uploadarchives_task)[Removal of the `uploadArchives` task](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_the_uploadarchives_task)

The `uploadArchives` task was used in combination with the legacy Ivy or Maven publishing mechanisms. It has been removed in Gradle 7. You should migrate to the `maven-publish` or `ivy-publish` plugin instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_dependency_version_sorting)[Changes in dependency version sorting](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_dependency_version_sorting)

In the context of dependency version sorting, a `-SNAPSHOT` version is now considered to be right before a final release but after any `-RC` version. More special version suffixes are also taken into account. This brings the Gradle algorithm closer to the Maven one for well-known version suffixes.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_play_framework_plugins)[Removal of Play Framework plugins](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_play_framework_plugins)

The deprecated Play plugins have been removed. An external replacement, the [Play Framework plugin](https://gradle.github.io/playframework), is available from the plugin portal.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_deprecated_jvm_plugins)[Removal of deprecated JVM plugins](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_deprecated_jvm_plugins)

These unmaintained alternative JVM plugins have been removed: `java-lang`, `scala-lang`, `junit-test-suite`, `jvm-component`, `jvm-resources`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_experimental_javascript_plugins)[Removal of experimental JavaScript plugins](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_experimental_javascript_plugins)

The following plugins for experimental JavaScript integration are now removed from the distribution: `coffeescript-base`, `envjs`, `javascript-base`, `jshint`, `rhino`.

If you used these plugins despite their experimental nature, you may find suitable replacements in the [Plugin Portal](https://plugins.gradle.org/).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#configuring_the_layout_of_an_ivy_repository)[Configuring the layout of an Ivy repository](https://docs.gradle.org/userguide/upgrading_version_6.html#configuring_the_layout_of_an_ivy_repository)

The `layout` method taking a configuration block has been removed and is replaced by [patternLayout](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.repositories.IvyArtifactRepository.html#org.gradle.api.artifacts.repositories.IvyArtifactRepository:patternLayout(org.gradle.api.Action)).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#executing_a_gradle_build_without_a_settings_file_is_now_an_error)[Executing a Gradle build without a settings file is now an error](https://docs.gradle.org/userguide/upgrading_version_6.html#executing_a_gradle_build_without_a_settings_file_is_now_an_error)

A Gradle build is defined by its `settings.gradle(.kts)` file found in the current or parent directory. Without a settings file, a Gradle build is undefined and Gradle produces an error when attempting to execute tasks.

Exceptions to this are invoking Gradle with the `init` task or using diagnostic command line flags, such as `--version`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#calling_project_afterevaluate_after_project_evaluation_is_now_an_error)[Calling Project.afterEvaluate() after project evaluation is now an error](https://docs.gradle.org/userguide/upgrading_version_6.html#calling_project_afterevaluate_after_project_evaluation_is_now_an_error)

Gradle 6.x warns users about the wrong behavior and ignores the target action in this scenario. Starting from 7.0 the same case will produce an error. Plugins and build scripts should be adjusted to call `afterEvaluate` only at configuration time. If you have such a build failure and the related `afterEvaluate` statement is declared in your build sources then you can simply delete it. If `afterEvaluate` is declared in a plugin then report the issue to the plugin maintainers.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#modifying_file_collections_after_values_finalized_is_now_an_error)[Modifying file collections after values finalized is now an error](https://docs.gradle.org/userguide/upgrading_version_6.html#modifying_file_collections_after_values_finalized_is_now_an_error)

Calling any mutator methods (i.e. `clear()`, `add()`, `remove()`, etc.) on `ConfigurableFileCollection` after the stored value calculated throws an exception. Users and plugin authors should adjust their code such that all configuration on `ConfigurableFileCollection` happens during configuration time, before the values are read.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_projectlayoutconfigurablefiles)[Removal of `ProjectLayout#configurableFiles`](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_projectlayoutconfigurablefiles)

Please use `ObjectFactory#fileCollection()` instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_basepluginconvention_libsdir_and_basepluginconvention_distsdir)[Removal of `BasePluginConvention.libsDir` and `BasePluginConvention.distsDir`](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_basepluginconvention_libsdir_and_basepluginconvention_distsdir)

Please use the `libsDirectory` and `distsDirectory` properties instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_unabletodeletefileexception)[Removal of `UnableToDeleteFileException`](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_unabletodeletefileexception)

Existing usages should be replaced with `RuntimeException`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#properties_removed_in_checkstyle_and_pmd_plugins)[Properties removed in Checkstyle and PMD plugins](https://docs.gradle.org/userguide/upgrading_version_6.html#properties_removed_in_checkstyle_and_pmd_plugins)

* The `configDir` getters and setters have been removed from the Checkstle task and extension. Use the `configDirectory` property instead.

* The `rulePriority` getter and setter have been removed from the Pmd task and extension. Use the `rulesMinimumPriority` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_basename_property_in_distribution_plugin)[Removal of `baseName` property in `distribution` plugin](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_basename_property_in_distribution_plugin)

The `getBaseName()` and `setBaseName()` methods were removed from the `Distribution` class. Clients should replace the usages with the `distributionBaseName` property.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#using_abstracttask)[Using `AbstractTask`](https://docs.gradle.org/userguide/upgrading_version_6.html#using_abstracttask)

Registering a task with the `AbstractTask` type or with a type extending `AbstractTask` was deprecated in Gradle 6.5 and is now an error in Gradle 7.0. You can use [DefaultTask](https://docs.gradle.org/current/javadoc/org/gradle/api/DefaultTask.html) instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_unused_startparameter_apis)[Removal of unused `StartParameter` APIs](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_unused_startparameter_apis)

The following APIs, which were not usable via command line options anymore since Gradle 5.0, are now removed: `StartParameter.useEmptySettings()`, `StartParameter.isUseEmptySettings()`, `StartParameter.setSearchUpwards(boolean)` and `StartParameter.isSearchUpwards()`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_searching_for_settings_files_in_master_directories)[Removal of searching for settings files in 'master' directories](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_searching_for_settings_files_in_master_directories)

Gradle no longer supports discovering the settings file in a directory named `master` in a sibling directory. If your build still uses this deprecated feature, consider refactoring the build to have the root directory match the physical root of the project hierarchy. You can find more information about [how to structure a Gradle build](https://docs.gradle.org/current/userguide/multi_project_builds.html#multi_project_builds) in the user manual. Alternatively, you can still run tasks in builds like this by invoking the build from the `master` directory only using a [fully qualified path to the task](https://docs.gradle.org/current/userguide/multi_project_builds_intermediate.html#sec:executing_tasks_by_fully_qualified_name).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#modularity_infermodulepath_defaults_to_true)[`modularity.inferModulePath` defaults to 'true'](https://docs.gradle.org/userguide/upgrading_version_6.html#modularity_infermodulepath_defaults_to_true)

[Compiling](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_modular), [testing](https://docs.gradle.org/current/userguide/java_testing.html#sec:java_testing_modular) and [executing](https://docs.gradle.org/current/userguide/application_plugin.html#sec:application_modular) now works automatically for any source set that defines a module by containing a `module-info.java` file. Usually, this is the behavior you need. If this is causing issues in cases you manually configure the module path, or use a 3rd party plugin for it, you can still opt out of this by setting `modularity.inferModulePath` to `false` on the java extension or individual tasks.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_componentselectionreason_getdescription)[Removal of `ComponentSelectionReason.getDescription`](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_componentselectionreason_getdescription)

The method `ComponentSelectionReason.getDescription` has been removed. It is replaced by `ComponentSelectionReason.getDescriptions` which returns a list of `ComponentSelectionDescriptor`, each having a `getDescription`.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_domain_object_collection_constructors)[Removal of domain object collection constructors](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_domain_object_collection_constructors)

The following deprecated constructors were removed:

* DefaultNamedDomainObjectList(Class, Instantiator, Namer)

* DefaultNamedDomainObjectSet(Class, Instantiator)

* DefaultPolymorphicDomainObjectContainer(Class, Instantiator)

* FactoryNamedDomainObjectContainer(Class, Instantiator, NamedDomainObjectFactory)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_defaultversionselectorscheme_constructor)[Removal of DefaultVersionSelectorScheme constructor](https://docs.gradle.org/userguide/upgrading_version_6.html#removal_of_defaultversionselectorscheme_constructor)

This internal API was used in plugins, amongst other the [Nebula plugins](https://github.com/nebula-plugins), and was deprecated in the Gradle 5.x timeline and is now removed. Latest plugins version should no longer reference it.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#setting_the_config_loc_config_property_on_the_checkstyle_plugin_is_now_an_error)[Setting the `config_loc` config property on the `checkstyle` plugin is now an error](https://docs.gradle.org/userguide/upgrading_version_6.html#setting_the_config_loc_config_property_on_the_checkstyle_plugin_is_now_an_error)

The `checkstyle` plugin now fails for the following configuration

```
checkstyle {
    configProperties['config_loc'] = file("path/to/checkstyle-config-dir")
}
```

Builds should declare the checkstyle configuration with the `checkstyle` block:

```
checkstyle {
    configDirectory = file("path/to/checkstyle-config-dir")
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#querying_the_mapped_value_of_a_provider_before_the_producer_has_completed_is_now_an_error)[Querying the mapped value of a provider before the producer has completed is now an error](https://docs.gradle.org/userguide/upgrading_version_6.html#querying_the_mapped_value_of_a_provider_before_the_producer_has_completed_is_now_an_error)

Gradle 6.x warns users about the wrong behavior and then returns a possibly incorrect provider value. Starting with 7.0 the same case will produce an error. Plugins and build scripts should be adjusted to query the mapped value of a provider, for example a task output property, after the task has completed.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#task_validation_problems_are_now_errors)[Task validation problems are now errors](https://docs.gradle.org/userguide/upgrading_version_6.html#task_validation_problems_are_now_errors)

Gradle 6.0 started warning about problems with task definitions (such as incorrectly defined inputs or outputs). For Gradle 7.0, those warnings are now errors and will fail the build.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#change_in_behavior_when_theres_a_strict_version_conflict_with_a_local_project)[Change in behavior when there’s a strict version conflict with a local project](https://docs.gradle.org/userguide/upgrading_version_6.html#change_in_behavior_when_theres_a_strict_version_conflict_with_a_local_project)

Previous Gradle releases had an inconsistent behavior in regard to conflict resolution in a particular configuration: - your project declares a strict dependency on a published module (for example, `com.mycompany:some-module:1.2!!`, where `1.2!!` is the short hand notation for a strict dependency on 1.2) - your build actually provides `com.mycompany:some-module` in a higher version

Previous Gradle releases would succeed, selecting the project dependency despite the strict constraint. Starting from Gradle 7, this will trigger a dependency resolution failure.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#missing_dependencies)[Missing dependencies between tasks](https://docs.gradle.org/userguide/upgrading_version_6.html#missing_dependencies)

Having a task which produces an output in a location and another task consuming that location by referring to it as an input without the consumer task depending on the producer task has been deprecated. A fix for this problem is to [add a dependency from the consumer to the producer](https://docs.gradle.org/current/userguide/incremental_build.html#sec:link_output_dir_to_input_files).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#duplicates-strategy)[Duplicates strategy](https://docs.gradle.org/userguide/upgrading_version_6.html#duplicates-strategy)

Gradle 7 now fails when a copy operation (or any operation which uses a `org.gradle.api.file.CopySpec`) encounters a duplicate entry, and that the duplicates strategy isn’t set. Please look at [the CopySpec docs](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html#setDuplicatesStrategy-org.gradle.api.file.DuplicatesStrategy-) for details.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.9)[Upgrading from 6.8 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.9)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

No upgrade notes from 6.8 to 6.9, as 6.9 only contains bug fixes.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.8)[Upgrading from 6.7 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.8)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_2)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_2)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#toolchain_api_is_now_marked_as_nonnull)[Toolchain API is now marked as @NonNull](https://docs.gradle.org/userguide/upgrading_version_6.html#toolchain_api_is_now_marked_as_nonnull)

The API supporting the Java Toolchain feature in `org.gradle.jvm.toolchain` is now marked as `@NonNull`.

This may impact Kotlin consumers where the return types of APIs are no longer nullable.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#updates_to_bundled_gradle_dependencies_2)[Updates to bundled Gradle dependencies](https://docs.gradle.org/userguide/upgrading_version_6.html#updates_to_bundled_gradle_dependencies_2)

* Kotlin has been updated to [Kotlin 1.4.20](https://blog.jetbrains.com/kotlin/2020/08/kotlin-1-4-released-with-a-focus-on-quality-and-performance/). Note that Gradle scripts are still using the Kotlin 1.3 language.

* Apache Ant has been updated to 1.10.9 to fix [CVE-2020-11979](https://github.com/gradle/gradle/security/advisories/GHSA-j45w-qrgf-25vm)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#projects_imported_into_eclipse_now_include_custom_source_set_classpaths)[Projects imported into Eclipse now include custom source set classpaths](https://docs.gradle.org/userguide/upgrading_version_6.html#projects_imported_into_eclipse_now_include_custom_source_set_classpaths)

Previously, projects imported by Eclipse only included dependencies for the main and test source sets. The compile and runtime classpaths of custom source sets were ignored.

Since Gradle 6.8, projects imported into Eclipse include the compile and runtime classpath for every source set defined by the build.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#sourcetask_is_no_longer_sensitive_to_empty_directories)[SourceTask is no longer sensitive to empty directories](https://docs.gradle.org/userguide/upgrading_version_6.html#sourcetask_is_no_longer_sensitive_to_empty_directories)

Previously, empty directories would be taken into account during up-to-date checks and build cache key calculations for the sources declared in `SourceTask`. This meant that a source tree that contained an empty directory and an otherwise identical source tree that did not contain the empty directory would be considered different sources, even if the task would produce the same outputs. In Gradle 6.8, `SourceTask` now ignores empty directories during doing up-to-date checks and build cache key calculations. In the vast majority of cases, this is the desired behavior, but it is possible that a task may extend `SourceTask` but also produce different outputs when empty directories are present in the sources. For tasks where this is a concern, you can expose a separate property without the `@IgnoreEmptyDirectories` annotation in order to capture those changes:

```
@InputFiles
@SkipWhenEmpty
@PathSensitive(PathSensitivity.ABSOLUTE)
public FileTree getSourcesWithEmptyDirectories() {
    return super.getSource()
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_to_publications)[Changes to publications](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_to_publications)

Publishing a component which has a dependency on an enforced platform now triggers a validation error, preventing accidental publishing of bad metadata: enforced platforms use cases should be limited to applications, not things which can be consumed from another library or an application.

If, for some reason, you still want to publish components with dependencies on enforced platforms, you can disable the validation following the [documentation](https://docs.gradle.org/current/userguide/publishing_setup.html#sec:suppressing_validation_errors).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changing_default_excludes_during_the_execution_phase)[Changing default excludes during the execution phase](https://docs.gradle.org/userguide/upgrading_version_6.html#changing_default_excludes_during_the_execution_phase)

Gradle’s file trees apply some default exclude patterns for convenience — the same defaults as Ant in fact. See the [user manual](https://docs.gradle.org/current/userguide/working_with_files.html#sec:file_trees) for more information. Sometimes, Ant’s default excludes prove problematic, for example when you want to include the `.gitignore` in an archive file.

Changing Gradle’s default excludes during the execution phase can lead to correctness problems with up-to-date checks. As a consequence, you are only allowed to change Gradle’s default excludes in the settings script, see the [user manual](https://docs.gradle.org/current/userguide/working_with_files.html#sec:change_default_excludes) for an example.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_2)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_2)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#referencing_tasks_from_included_builds)[Referencing tasks from included builds](https://docs.gradle.org/userguide/upgrading_version_6.html#referencing_tasks_from_included_builds)

Direct references to tasks from included builds in `mustRunAfter`, `shouldRunAfter` and `finalizedBy` task methods have been deprecated. Task ordering using `mustRunAfter` and `shouldRunAfter` as well as finalizers specified by `finalizedBy` should be used for task ordering within a build. If you happen to have cross-build task ordering defined using above mentioned methods, consider restructuring such builds and decoupling them from one another.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#master_subdirectory_root_build)[Searching for settings files in 'master' directories](https://docs.gradle.org/userguide/upgrading_version_6.html#master_subdirectory_root_build)

Gradle will emit a deprecation warning when your build relies on finding the settings file in a directory named `master` in a sibling directory.

If your build uses this feature, consider refactoring the build to have the root directory match the physical root of the project hierarchy.

Alternatively, you can still run tasks in builds like this by invoking the build from the `master` directory only using a [fully qualified path to the task](https://docs.gradle.org/current/userguide/multi_project_builds_intermediate.html#sec:executing_tasks_by_fully_qualified_name).

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#using_NamedDomainObjectContainer_invoke_kotlin_Function1)[Using method `NamedDomainObjectContainer<T>.invoke(kotlin.Function1)`](https://docs.gradle.org/userguide/upgrading_version_6.html#using_NamedDomainObjectContainer_invoke_kotlin_Function1)

Gradle Kotlin DSL extensions have been changed to favor Gradle’s `Action<T>` type over Kotlin function types.

While the change should be transparent to Kotlin clients, Java clients calling Kotlin DSL extensions need to be updated to use the `Action<T>` APIs.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.7)[Upgrading from 6.6 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.7)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_3)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_3)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#buildsrc_can_now_see_included_builds_from_the_root)[buildSrc can now see included builds from the root](https://docs.gradle.org/userguide/upgrading_version_6.html#buildsrc_can_now_see_included_builds_from_the_root)

Previously, `buildSrc` was built in such a way that included builds were ignored from the root build.

Since Gradle 6.7, `buildSrc` can see any included build from the root build. This may cause dependencies to be substituted from an included build in `buildSrc`. This may also change the order in which some builds are executed if an included build is needed by `buildSrc`.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_3)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_3)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changing_default_excludes_during_the_execution_phase_2)[Changing default excludes during the execution phase](https://docs.gradle.org/userguide/upgrading_version_6.html#changing_default_excludes_during_the_execution_phase_2)

Gradle’s file trees apply some default exclude patterns for convenience — the same defaults as Ant in fact. See the [user manual](https://docs.gradle.org/current/userguide/working_with_files.html#sec:file_trees) for more information. Sometimes, Ant’s default excludes prove problematic, for example when you want to include the `.gitignore` in an archive file.

Changing Gradle’s default excludes during the execution phase can lead to correctness problems with up-to-date checks, and is deprecated. You are only allowed to change Gradle’s default excludes in the settings script, see the [user manual](https://docs.gradle.org/current/userguide/working_with_files.html#sec:change_default_excludes) for an example.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#using_a_configuration_directly_as_a_dependency)[Using a Configuration directly as a dependency](https://docs.gradle.org/userguide/upgrading_version_6.html#using_a_configuration_directly_as_a_dependency)

Gradle allowed instances of `Configuration` to be used directly as dependencies:

```
dependencies {
    implementation(configurations.myConfiguration)
}
```

This behavior is now deprecated as it is confusing: one could expect the "dependent configuration" to be resolved first and add the result of resolution as dependencies to the including configuration, which is not the case. The deprecated version can be replaced with the actual behavior, which is configuration inheritance:

`configurations.implementation.extendsFrom(configurations.myConfiguration)`

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.6)[Upgrading from 6.5 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.6)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_4)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_4)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#dependency_substitutions_and_variant_aware_dependency_resolution)[Dependency substitutions and variant aware dependency resolution](https://docs.gradle.org/userguide/upgrading_version_6.html#dependency_substitutions_and_variant_aware_dependency_resolution)

While adding support for expressing [variant support](https://docs.gradle.org/current/userguide/resolution_rules.html#sec:variant-aware-substitutions) in dependency substitutions, a bug fix introduced a behaviour change that some builds may rely upon. Previously a substituted dependency would still use the [attributes](https://docs.gradle.org/current/userguide/variant_attributes.html#variant-attributes) of the original selector instead of the ones from the replacement selector.

With that change, existing substitutions around dependencies with richer selectors, such as for platform dependencies, will no longer work as they did. It becomes mandatory to define the variant aware part in the target selector.

You can be affected by this change if you:

* have dependencies on platforms, like `implementation platform("org:platform:1.0")`

* _or_ if you specify attributes on dependencies,

* _and_ you use [resolution rules](https://docs.gradle.org/current/userguide/resolution_rules.html#using-resolution-rules) on these dependencies.

See the [documentation](https://docs.gradle.org/current/userguide/resolution_rules.html#sec:variant-aware-substitutions) for resolving issues if you are impacted.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_4)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_4)

No deprecations were made in Gradle 6.6.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.5)[Upgrading from 6.4 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.5)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_5)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_5)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#abstract_task_deprecated)[Internal class AbstractTask is deprecated](https://docs.gradle.org/userguide/upgrading_version_6.html#abstract_task_deprecated)

`AbstractTask` is an internal class which is visible on the public API, as a superclass of public type `DefaultTask`. `AbstractTask` will be removed in Gradle 7.0, and the following are deprecated in Gradle 6.5:

* Registering a task whose type is `AbstractTask` or `TaskInternal`. You can remove the task type from the task registration and Gradle will use `DefaultTask` instead.

* Registering a task whose type is a subclass of `AbstractTask` but not a subclass of `DefaultTask`. You can change the task type to extend `DefaultTask` instead.

* Using the class `AbstractTask` from plugin code or build scripts. You can change the code to use `DefaultTask` instead.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.4)[Upgrading from 6.3 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.4)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_6)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_6)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#upgrade:pmd_expects_6)[PMD plugin expects PMD 6.0.0 or higher by default](https://docs.gradle.org/userguide/upgrading_version_6.html#upgrade:pmd_expects_6)

Gradle 6.4 enabled incremental analysis by default. Incremental analysis is only available in PMD 6.0.0 or higher. If you want to use an older PMD version, you need to disable incremental analysis:

```
pmd {
    incrementalAnalysis = false
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_dependency_locking)[Changes in dependency locking](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_in_dependency_locking)

With Gradle 6.4, the incubating API for [dependency locking `LockMode`](https://docs.gradle.org/current/userguide/dependency_locking.html#sec:fine-tuning-dependency-locking-behaviour-with-lock-mode) has changed. The value is now set via a `Property<LockMode>` instead of a direct setter. This means that the notation to set the value has to be updated for the Kotlin DSL:

```
dependencyLocking {
    lockMode.set(LockMode.STRICT)
}
```

Users of the Groovy DSL should not be impacted as the notation `lockMode = LockMode.STRICT` remains valid.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#java_versions_in_published_metadata)[Java versions in published metadata](https://docs.gradle.org/userguide/upgrading_version_6.html#java_versions_in_published_metadata)

If a Java library is published with Gradle Module Metadata, the information which Java version it supports is encoded in the `org.gradle.jvm.version` attribute. By default, this attribute was set to what you configured in `java.targetCompatibility`. If that was not configured, it was set to the current Java version running Gradle. Changing the version of a particular compile task, e.g. `javaCompile.targetCompatibility` had no effect on that attribute, leading to wrong information if the attribute was not adjusted manually. This is now fixed and the attribute defaults to the setting of the compile task that is associated with the sources from which the published jar is built.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#ivy_repositories_with_custom_layouts)[Ivy repositories with custom layouts](https://docs.gradle.org/userguide/upgrading_version_6.html#ivy_repositories_with_custom_layouts)

Gradle versions from 6.0 to 6.3.x included could generate bad Gradle Module Metadata when publishing on an Ivy repository which had a custom repository layout. Starting from 6.4, Gradle will no longer publish Gradle Module Metadata if it detects that you are using a custom repository layout.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#new_properties_may_shadow_variables_in_build_scripts)[New properties may shadow variables in build scripts](https://docs.gradle.org/userguide/upgrading_version_6.html#new_properties_may_shadow_variables_in_build_scripts)

This release introduces some new properties — `mainClass`, `mainModule`, `modularity` — in different places. Since these are very generic names, there is a chance that you use one of them in your build scripts as variable name. A new property might then shadow one of your variables in an undesired way, leading to a build failure where the property is accessed instead of the local variable with the same name. You can fix it by renaming the corresponding variable in the build script.

Affected is configuration code inside the `application {}` and `java {}` configuration blocks, inside a java execution setup with `project.javaexec {}`, and inside various task configurations (`JavaExec`, `CreateStartScripts`, `JavaCompile`, `Test`, `Javadoc`).

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_6)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_6)

There were no deprecations between Gradle 6.3 and 6.4.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.3)[Upgrading from 6.2 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.3)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_7)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_7)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#fewer_dependencies_available_in_idea)[Fewer dependencies available in IDEA](https://docs.gradle.org/userguide/upgrading_version_6.html#fewer_dependencies_available_in_idea)

Gradle no longer includes the annotation processor classpath as provided dependencies in IDEA. The dependencies IDEA sees at compile time are the same as what Gradle sees after resolving the compile classpath (configuration named `compileClasspath`). This prevents the leakage of annotation processor dependencies into the project’s code.

Before Gradle introduced [incremental annotation processing support](https://docs.gradle.org/current/userguide/java_plugin.html#sec:incremental_annotation_processing), IDEA required all annotation processors to be on the compilation classpath to be able to run annotation processing when compiling in IDEA. This is no longer necessary because Gradle has a separate [annotation processor classpath](https://docs.gradle.org/current/userguide/java_plugin.html#tab:configurations). The dependencies for annotation processors are not added to an IDEA module’s classpath when a Gradle project with annotation processors is imported.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#rich_console_support_removed_for_some_32_bit_operating_systems)[Rich console support removed for some 32-bit operating systems](https://docs.gradle.org/userguide/upgrading_version_6.html#rich_console_support_removed_for_some_32_bit_operating_systems)

Gradle 6.3 does not support the [rich console](https://docs.gradle.org/current/userguide/command_line_interface.html#sec:rich_console) for 32-bit Unix systems and for old FreeBSD versions (older than FreeBSD 10). Microsoft Windows 32-bit is unaffected.

Gradle will continue building projects on 32-bit systems but will no longer show the rich console.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_7)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_7)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#using_default_and_archives_configurations)[Using default and archives configurations](https://docs.gradle.org/userguide/upgrading_version_6.html#using_default_and_archives_configurations)

Almost every Gradle project has the _default_ and _archives_ configurations which are added by the _base_ plugin. These configurations are no longer used in modern Gradle builds that use [variant aware dependency management](https://docs.gradle.org/current/userguide/variant_aware_resolution.html#sec:understanding-variant-selection) and the [new publishing plugins](https://docs.gradle.org/current/userguide/publishing_setup.html#publishing_components).

While the configurations will stay in Gradle for backwards compatibility for now, using them to declare dependencies or to resolve dependencies is now deprecated.

Resolving these configurations was never an intended use case and only possible because in earlier Gradle versions _every_ configuration was resolvable. For declaring dependencies, please use the configurations provided by the plugins you use, for example by the [Java Library plugin](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph).

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.2)[Upgrading from 6.1 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.2)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_8)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_8)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#compile_and_runtime_classpath_now_request_library_variants_by_default)[Compile and runtime classpath now request library variants by default](https://docs.gradle.org/userguide/upgrading_version_6.html#compile_and_runtime_classpath_now_request_library_variants_by_default)

A classpath in a JVM project now explicitly requests the `org.gradle.category=library` attribute. This leads to clearer error messages if a certain library cannot be used. For example, when the library does not support the required Java version. The practical effect is that now all [platform dependencies](https://docs.gradle.org/current/userguide/java_platform_plugin.html#sec:java_platform_consumption) have to be declared as such. Before, platform dependencies also worked, accidentally, when the `platform()` keyword was omitted for local platforms or platforms published with Gradle Module Metadata.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#properties_from_project_root_gradle_properties_leaking_into_buildsrc_and_included_builds)[Properties from project root `gradle.properties` leaking into `buildSrc` and included builds](https://docs.gradle.org/userguide/upgrading_version_6.html#properties_from_project_root_gradle_properties_leaking_into_buildsrc_and_included_builds)

There was a regression in Gradle 6.2 and Gradle 6.2.1 that caused Gradle properties set in the project root `gradle.properties` file to leak into the `buildSrc` build and any builds included by the root.

This could cause your build to start failing if the `buildSrc` build or an included build suddenly found an unexpected or incompatible value for a property coming from the project root `gradle.properties` file.

The regression has been fixed in Gradle 6.2.2.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_8)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_8)

There were no deprecations between Gradle 6.1 and 6.2.

[](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.1)[Upgrading from 6.0 and earlier](https://docs.gradle.org/userguide/upgrading_version_6.html#changes_6.1)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_9)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_6.html#deprecations_9)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#querying_a_mapped_output_property_of_a_task_before_the_task_has_completed)[Querying a mapped output property of a task before the task has completed](https://docs.gradle.org/userguide/upgrading_version_6.html#querying_a_mapped_output_property_of_a_task_before_the_task_has_completed)

Querying the value of a mapped output property before the task has completed can cause strange build failures because it indicates stale or non-existent outputs may be used by mistake. This behavior is deprecated and will emit a deprecation warning. This will become an error in Gradle 7.0.

The following example demonstrates this problem where the Producer’s output file is parsed before the Producer executes:

```
class Consumer extends DefaultTask {
    @Input
    final Property<Integer> threadPoolSize = ...
}

class Producer extends DefaultTask {
    @OutputFile
    final RegularFileProperty outputFile = ...
}

// threadPoolSize is read from the producer's outputFile
consumer.threadPoolSize = producer.outputFile.map { it.text.toInteger() }

// Emits deprecation warning
println("thread pool size = " + consumer.threadPoolSize.get())
```

Querying the value of `consumer.threadPoolSize` will produce a deprecation warning if done prior to `producer` completing, as the output file has not yet been generated.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#discontinued_methods)[Discontinued methods](https://docs.gradle.org/userguide/upgrading_version_6.html#discontinued_methods)

The following methods have been discontinued and should no longer be used. They will be removed in Gradle 7.0.

* `BasePluginConvention.setProject(ProjectInternal)`

* `BasePluginConvention.getProject()`

* `StartParameter.useEmptySettings()`

* `StartParameter.isUseEmptySettings()`

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#upgrading_jvm_plugins)[Alternative JVM plugins (a.k.a "Software Model")](https://docs.gradle.org/userguide/upgrading_version_6.html#upgrading_jvm_plugins)

A set of alternative plugins for Java and Scala development were introduced in Gradle 2.x as an experiment based on the "software model". These plugins are now deprecated and will eventually be removed. If you are still using one of these old plugins (`java-lang`, `scala-lang`, `jvm-component`, `jvm-resources`, `junit-test-suite`) please consult the documentation on [Building Java & JVM projects](https://docs.gradle.org/current/userguide/building_java_projects.html#building_java_projects) to determine which of the stable JVM plugins are appropriate for your project.

### [](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_9)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_6.html#potential_breaking_changes_9)

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#projectlayout_is_no_longer_available_to_worker_actions_as_a_service)[`ProjectLayout` is no longer available to worker actions as a service](https://docs.gradle.org/userguide/upgrading_version_6.html#projectlayout_is_no_longer_available_to_worker_actions_as_a_service)

In Gradle 6.0, the `ProjectLayout` service was made available to worker actions via service injection. This service allowed for mutable state to leak into a worker action and introduced a way for dependencies to go undeclared in the worker action.

`ProjectLayout` has been removed from the available services. Worker actions that were using `ProjectLayout` should switch to injecting the `projectDirectory` or `buildDirectory` as a parameter instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_6.html#publishing_spring_boot_applications)[Publishing Spring Boot applications](https://docs.gradle.org/userguide/upgrading_version_6.html#publishing_spring_boot_applications)

Starting from Gradle 6.2, Gradle performs a sanity check before uploading, to make sure you don’t upload stale files (files produced by another build). This introduces a problem with Spring Boot applications which are uploaded using the `components.java` component:

`Artifact my-application-0.0.1-SNAPSHOT.jar wasn't produced by this build.`

This is caused by the fact that the main `jar` task is disabled by the Spring Boot application, and the component expects it to be present. Because the `bootJar` task uses the _same file_ as the main `jar` task by default, previous releases of Gradle would either:

* publish a stale `bootJar` artifact

* or fail if the `bootJar` task hasn’t been called previously

A workaround is to tell Gradle what to upload. If you want to upload the `bootJar`, then you need to configure the outgoing configurations to do this:

```
configurations {
   [apiElements, runtimeElements].each {
       it.outgoing.artifacts.removeIf { it.buildDependencies.getDependencies(null).contains(jar) }
       it.outgoing.artifact(bootJar)
   }
}
```

Alternatively, you might want to re-enable the `jar` task, and add the `bootJar` with a different classifier.

```
jar {
   enabled = true
}

bootJar {
   classifier = 'application'
}
```
