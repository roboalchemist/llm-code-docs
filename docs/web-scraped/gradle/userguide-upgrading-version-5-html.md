# Source: https://docs.gradle.org/userguide/upgrading_version_5.html

Title: Upgrading from Gradle 5.x to 6.0

URL Source: https://docs.gradle.org/userguide/upgrading_version_5.html

Markdown Content:

### [](https://docs.gradle.org/userguide/upgrading_version_5.html#deprecations)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_5.html#deprecations)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#dependencies_should_no_longer_be_declared_using_the_compile_and_runtime_configurations)[Dependencies should no longer be declared using the `compile` and `runtime` configurations](https://docs.gradle.org/userguide/upgrading_version_5.html#dependencies_should_no_longer_be_declared_using_the_compile_and_runtime_configurations)

The usage of the `compile` and `runtime` configurations in the Java ecosystem plugins has been discouraged since [Gradle 3.4](https://docs.gradle.org/3.4/release-notes.html#the-java-library-plugin).

These configurations are used for compiling and running code from the `main` source set. Other sources sets create similar configurations (e.g. `testCompile` and `testRuntime` for the `test` source set), should not be used either. The `implementation`, `api`, `compileOnly` and `runtimeOnly` configurations should be used to declare dependencies and the `compileClasspath` and `runtimeClasspath` configurations to resolve dependencies. See [the relationship of these configurations](https://docs.gradle.org/current/userguide/java_library_plugin.html#sec:java_library_configurations_graph).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#legacy_publication_system_is_deprecated_and_replaced_with_the_publish_plugins)[Legacy publication system is deprecated and replaced with the `*-publish` plugins](https://docs.gradle.org/userguide/upgrading_version_5.html#legacy_publication_system_is_deprecated_and_replaced_with_the_publish_plugins)

The `uploadArchives` task and the `maven` plugin are deprecated.

The publishing system is also the only way to ensure the publication of [Gradle Module Metadata](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html#sec:understanding-gradle-module-md).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#problems_with_tasks_emit_deprecation_warnings)[Problems with tasks emit deprecation warnings](https://docs.gradle.org/userguide/upgrading_version_5.html#problems_with_tasks_emit_deprecation_warnings)

When Gradle detects problems with task definitions (such as incorrectly defined inputs or outputs) it will show the following message on the console:

```
Deprecated Gradle features were used in this build, making it incompatible with Gradle 7.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/6.0/userguide/command_line_interface.html#sec:command_line_warnings
```

The deprecation warnings show up in a [Build Scan](https://scans.gradle.com/s/txrptciitl2ha/deprecations) for every build, regardless of the command-line switches used.

When the build is executed with `--warning-mode all`, the individual warnings will be shown:

```
> Task :myTask
Property 'inputDirectory' is declared without normalization specified. Properties of cacheable work must declare their normalization via @PathSensitive, @Classpath or @CompileClasspath. Defaulting to PathSensitivity.ABSOLUTE. This behavior is scheduled to be removed in Gradle 7.0.
Property 'outputFile' is not annotated with an input or output annotation. This behavior is scheduled to be removed in Gradle 7.0.
```

If you own the code of the tasks in question, you can fix them by [following the suggestions](https://docs.gradle.org/current/userguide/incremental_build.html#sec:task_input_validation). You can also use `--stacktrace` to see where in the code each warning originates from.

Otherwise, you’ll need to report the problems to the maintainer of the relevant task or plugin.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#forced_dependencies)[Forced dependencies](https://docs.gradle.org/userguide/upgrading_version_5.html#forced_dependencies)

Forcing dependency versions using `force = true` on a first-level dependency has been deprecated.

Force has both a semantic and ordering issue which can be avoided by using a [strict version constraint](https://docs.gradle.org/current/userguide/dependency_versions.html#sec:rich-version-constraints).

In Gradle 5.0, we removed the `--no-search-upward` CLI parameter.

The related APIs in `StartParameter` (like `isSearchUpwards()`) are now deprecated.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#apis_buildlistener_buildstarted_and_gradle_buildstarted_have_been_deprecated)[APIs `BuildListener.buildStarted` and `Gradle.buildStarted` have been deprecated](https://docs.gradle.org/userguide/upgrading_version_5.html#apis_buildlistener_buildstarted_and_gradle_buildstarted_have_been_deprecated)

These methods currently do not work as expected since the callbacks will never be called after the build has started.

The methods are being deprecated to avoid confusion.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#implicit_duplicate_strategy_for_copy_or_archive_tasks_has_been_deprecated)[Implicit duplicate strategy for `Copy` or archive tasks has been deprecated](https://docs.gradle.org/userguide/upgrading_version_5.html#implicit_duplicate_strategy_for_copy_or_archive_tasks_has_been_deprecated)

To prevent this from happening accidentally, encountering duplicates while creating an archive now produces a deprecation message and will fail the build starting with Gradle 7.0.

`Copy` tasks also happily copy multiple sources with the same relative path to the destination directory. This behavior has also been deprecated.

If you want to allow duplicates, you can specify that explicitly:

```
task archive(type: Zip) {
    duplicatesStrategy = DuplicatesStrategy.INCLUDE // allow duplicates
    ...
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#executing_gradle_without_a_settings_file_has_been_deprecated)[Executing Gradle without a settings file has been deprecated](https://docs.gradle.org/userguide/upgrading_version_5.html#executing_gradle_without_a_settings_file_has_been_deprecated)

A Gradle build is defined by a `settings.gradle[.kts]` file in the current or parent directory. Without a settings file, a Gradle build is undefined and will emit a deprecation warning.

In Gradle 7.0, Gradle will only allow you to invoke the `init` task or diagnostic command line flags, such as `--version`, with undefined builds.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#calling_project_afterevaluate_on_an_evaluated_project_has_been_deprecated)[Calling `Project.afterEvaluate` on an evaluated project has been deprecated](https://docs.gradle.org/userguide/upgrading_version_5.html#calling_project_afterevaluate_on_an_evaluated_project_has_been_deprecated)

Once a project is evaluated, Gradle ignores all configuration passed to `Project#afterEvaluate` and emits a deprecation warning. This scenario will become an error in Gradle 7.0.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#deprecated_plugins)[Deprecated plugins](https://docs.gradle.org/userguide/upgrading_version_5.html#deprecated_plugins)

The following bundled plugins were never announced and will be removed in the next major release of Gradle:

* `org.gradle.coffeescript-base`

* `org.gradle.envjs`

* `org.gradle.javascript-base`

* `org.gradle.jshint`

* `org.gradle.rhino`

Some of these plugins may have replacements on the [Plugin Portal](https://plugins.gradle.org/).

### [](https://docs.gradle.org/userguide/upgrading_version_5.html#potential_breaking_changes)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_5.html#potential_breaking_changes)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#android_gradle_plugin_3_3_and_earlier_is_no_longer_supported)[Android Gradle Plugin 3.3 and earlier is no longer supported](https://docs.gradle.org/userguide/upgrading_version_5.html#android_gradle_plugin_3_3_and_earlier_is_no_longer_supported)

Gradle 6.0 supports Android Gradle Plugin versions 3.4 and later.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_build_and_task_names_in_composite_builds)[Changes to build and task names in composite builds](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_build_and_task_names_in_composite_builds)

Previously, Gradle used the name of the root project as the build name for an included build. Now, the name of the build’s root directory is used and the root project name is not considered if different. A different name for the build can be specified if the build is being included via a settings file.

```
includeBuild("some-other-build") {
    name = "another-name"
}
```

The previous behavior was problematic as it caused different names to be used at different times during the build.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#buildsrc_is_now_reserved_as_a_project_and_subproject_build_name)[buildSrc is now reserved as a project and subproject build name](https://docs.gradle.org/userguide/upgrading_version_5.html#buildsrc_is_now_reserved_as_a_project_and_subproject_build_name)

Previously, Gradle did not prevent using the name "buildSrc" for a subproject of a multi-project build or as the name of an included build. Now, this is not allowed. The name "buildSrc" is now reserved for the conventional buildSrc project that builds extra build logic.

Typical use of buildSrc is unaffected by this change. You will only be affected if your settings file specifies `include("buildSrc")` or `includeBuild("buildSrc")`.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#scala_zinc_compiler)[Scala Zinc compiler](https://docs.gradle.org/userguide/upgrading_version_5.html#scala_zinc_compiler)

The Zinc compiler has been upgraded to version 1.3.0. Gradle no longer supports building for Scala 2.9.

The minimum Zinc compiler supported by Gradle is 1.2.0 and the maximum tested version is 1.3.0.

To make it easier to select the version of the Zinc compiler, you can now configure a `zincVersion` property:

```
scala {
    zincVersion = "1.2.1"
}
```

Please remove any explicit dependencies you’ve added to the `zinc` configuration and use this property instead. If you try to use the `com.typesafe.zinc:zinc` dependency, Gradle will switch to the new Zinc implementation.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_build_cache)[Changes to Build Cache](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_build_cache)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#local_build_cache_is_always_a_directory_cache)[Local build cache is always a directory cache](https://docs.gradle.org/userguide/upgrading_version_5.html#local_build_cache_is_always_a_directory_cache)

In the past, it was possible to use any build cache implementation as the `local` cache. This is no longer allowed as the local cache must always be a `DirectoryBuildCache`.

Calls to `BuildCacheConfiguration.local(Class)` with anything other than `DirectoryBuildCache` as the type will fail the build. Calling these methods with the `DirectoryBuildCache` type will produce a deprecation warning.

Use `getLocal()` and `local(Action)` instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#failing_to_pack_or_unpack_cached_results_will_now_fail_the_build)[Failing to pack or unpack cached results will now fail the build](https://docs.gradle.org/userguide/upgrading_version_5.html#failing_to_pack_or_unpack_cached_results_will_now_fail_the_build)

In the past, when Gradle encountered a problem while packing the results of a cached task, Gradle would ignore the problem and continue running the build.

When encountering a corrupt cached artifact, Gradle would remove whatever was already unpacked and re-execute the task to make sure the build had a chance to succeed.

While this behavior was intended to make a build successful, this had the adverse effect of hiding problems and led to reduced cache performance.

In Gradle 6.0, both pack and unpack errors will cause the build to fail, so that these problems will be surfaced more easily.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#buildsrc_projects_automatically_use_build_cache_configuration)[buildSrc projects automatically use build cache configuration](https://docs.gradle.org/userguide/upgrading_version_5.html#buildsrc_projects_automatically_use_build_cache_configuration)

Previously, in order to use the build cache for the buildSrc build you needed to duplicate your build cache config in the buildSrc build. Now, it automatically uses the build cache configuration defined by the top level settings script.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_dependency_management)[Changes to Dependency Management](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_dependency_management)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#gradle_module_metadata_is_always_published)[Gradle Module Metadata is always published](https://docs.gradle.org/userguide/upgrading_version_5.html#gradle_module_metadata_is_always_published)

Officially introduced in Gradle 5.3, [Gradle Module Metadata](https://blog.gradle.org/gradle-metadata-1.0) was created to solve many of the problems that have plagued dependency management for years, in particular, but not exclusively, in the Java ecosystem.

With Gradle 6.0, Gradle Module Metadata is enabled by default.

This means, if you are publishing libraries with Gradle and using the [maven-publish](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven) or [ivy-publish](https://docs.gradle.org/current/userguide/publishing_ivy.html#publishing_ivy) plugin, the Gradle Module Metadata file is always published **in addition** to traditional metadata.

The traditional metadata file will contain a marker so that Gradle knows that there is additional metadata to consume.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#maven_or_ivy_repositories_are_no_longer_queried_for_artifacts_without_metadata_by_default)[Maven or Ivy repositories are no longer queried for artifacts without metadata by default](https://docs.gradle.org/userguide/upgrading_version_5.html#maven_or_ivy_repositories_are_no_longer_queried_for_artifacts_without_metadata_by_default)

If Gradle fails to locate the metadata file (`.pom` or `ivy.xml`) of a module in a repository defined in the `repositories { }` section, it now assumes that the module does not exist in that repository.

For dynamic versions, the `maven-metadata.xml` for the corresponding module needs to be present in a Maven repository.

Previously, Gradle would also look for a default artifact (`.jar`). This behavior often caused a large number of unnecessary requests when using multiple repositories that slowed builds down.

You can opt into the old behavior for selected repositories by adding the `artifact()`[metadata source](https://docs.gradle.org/current/userguide/supported_metadata_formats.html#sec:supported-metadata-sources).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changing_the_pom_packaging_property_no_longer_changes_the_artifact_extension)[Changing the pom `packaging` property no longer changes the artifact extension](https://docs.gradle.org/userguide/upgrading_version_5.html#changing_the_pom_packaging_property_no_longer_changes_the_artifact_extension)

Previously, if the pom packaging was not _jar_, _ejb_, _bundle_ or _maven-plugin_, the extension of the main artifact published to a Maven repository was changed during publishing to match the pom packaging.

This behavior led to broken Gradle Module Metadata and was difficult to understand due to handling of different packaging types.

Build authors can change the artifact name when the artifact is created to obtain the same result as before — e.g. by setting `jar.archiveExtension.set(pomPackaging)` explicitly.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#an_ivy_xml_published_for_java_libraries_contains_more_information)[An `ivy.xml` published for Java libraries contains more information](https://docs.gradle.org/userguide/upgrading_version_5.html#an_ivy_xml_published_for_java_libraries_contains_more_information)

A number of fixes were made to produce more correct `ivy.xml` metadata in the `ivy-publish` plugin.

As a consequence, the internal structure of the `ivy.xml` file has changed. The `runtime` configuration now contains more information, which corresponds to the _runtimeElements_ variant of a Java library. The `default` configuration should yield the same result as before.

In general, users are advised to migrate from `ivy.xml` to the new Gradle Module Metadata format.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_plugins_and_build_scripts)[Changes to Plugins and Build scripts](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_plugins_and_build_scripts)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#classes_from_buildsrc_are_no_longer_visible_to_settings_scripts)[Classes from `buildSrc` are no longer visible to settings scripts](https://docs.gradle.org/userguide/upgrading_version_5.html#classes_from_buildsrc_are_no_longer_visible_to_settings_scripts)

Previously, the buildSrc project was built before applying the project’s settings script and its classes were visible within the script. Now, buildSrc is built after the settings script and its classes are not visible to it. The buildSrc classes remain visible to project build scripts and script plugins.

Custom logic can be used from a settings script by declaring external dependencies.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_pluginmanagement_block_in_settings_scripts_is_now_isolated)[The `pluginManagement` block in settings scripts is now isolated](https://docs.gradle.org/userguide/upgrading_version_5.html#the_pluginmanagement_block_in_settings_scripts_is_now_isolated)

Previously, any `pluginManagement {}` blocks inside a settings script were executed during the normal execution of the script.

Now, they are executed earlier in a similar manner to `buildscript {}` or `plugins {}`. This means that code inside such a block cannot reference anything declared elsewhere in the script.

This change has been made so that `pluginManagement` configuration can also be applied when resolving plugins for the settings script itself.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#plugins_and_classes_loaded_in_settings_scripts_are_visible_to_project_scripts_and_buildsrc)[Plugins and classes loaded in settings scripts are visible to project scripts and `buildSrc`](https://docs.gradle.org/userguide/upgrading_version_5.html#plugins_and_classes_loaded_in_settings_scripts_are_visible_to_project_scripts_and_buildsrc)

Previously, any classes added to the a settings script by using `buildscript {}` were not visible outside of the script. Now, they are visible to all of the project build scripts.

They are also visible to the `buildSrc` build script and its settings script.

This change has been made so that plugins applied to the settings script can contribute logic to the entire build.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#plugin_validation_changes)[Plugin validation changes](https://docs.gradle.org/userguide/upgrading_version_5.html#plugin_validation_changes)

* The `validateTaskProperties` task is now deprecated, use `validatePlugins` instead. The new name better reflects the fact that it also validates artifact transform parameters and other non-property definitions.

* The `ValidateTaskProperties` type is replaced by `ValidatePlugins`.

* The `setClasses()` method is now removed. Use `getClasses().setFrom()` instead.

* The `setClasspath()` method is also removed. use `getClasspath().setFrom()` instead.

* The [failOnWarning](https://docs.gradle.org/current/javadoc/org/gradle/plugin/devel/tasks/ValidatePlugins.html#getFailOnWarning--) option is now enabled by default.

* The following task validation errors now fail the build at runtime and are promoted to errors for [ValidatePlugins](https://docs.gradle.org/current/javadoc/org/gradle/plugin/devel/tasks/ValidatePlugins.html):

  * A task property is annotated with a property annotation not allowed for tasks, like `@InputArtifact`.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_kotlin_dsl)[Changes to Kotlin DSL](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_kotlin_dsl)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#using_the_embedded_kotlin_plugin_now_requires_a_repository)[Using the `embedded-kotlin` plugin now requires a repository](https://docs.gradle.org/userguide/upgrading_version_5.html#using_the_embedded_kotlin_plugin_now_requires_a_repository)

Just like when using the `kotlin-dsl` plugin, it is now required to declare a repository where Kotlin dependencies can be found if you apply the `embedded-kotlin` plugin.

```
plugins {
    `embedded-kotlin`
}

repositories {
    mavenCentral()
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#kotlin_dsl_ide_support_now_requires_kotlin_intellij_plugin_1_3_50)[Kotlin DSL IDE support now requires Kotlin IntelliJ Plugin >= 1.3.50](https://docs.gradle.org/userguide/upgrading_version_5.html#kotlin_dsl_ide_support_now_requires_kotlin_intellij_plugin_1_3_50)

With Kotlin IntelliJ plugin versions prior to 1.3.50, Kotlin DSL scripts will be wrongly highlighted when the _Gradle JVM_ is set to a version different from the one in _Project SDK_. Simply upgrade your IDE plugin to a version >= 1.3.50 to restore the correct Kotlin DSL script highlighting behavior.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#kotlin_dsl_script_base_types_no_longer_extend_project_settings_or_gradle)[Kotlin DSL script base types no longer extend `Project`, `Settings` or `Gradle`](https://docs.gradle.org/userguide/upgrading_version_5.html#kotlin_dsl_script_base_types_no_longer_extend_project_settings_or_gradle)

In previous versions, Kotlin DSL scripts were compiled to classes that implemented one of the three core Gradle configuration interfaces in order to implicitly expose their APIs to scripts. `org.gradle.api.Project` for project scripts, `org.gradle.api.initialization.Settings` for settings scripts and `org.gradle.api.invocation.Gradle` for init scripts.

Having the script instance implement the core Gradle interface of the model object it was supposed to configure was convenient because it made the model object API immediately available to the body of the script but it was also a lie that could cause all sorts of trouble whenever the script itself was used in place of the model object, a project script **was not** a proper `Project` instance just because it implemented the core `Project` interface and the same was true for settings and init scripts.

In 6.0 all Kotlin DSL scripts are compiled to classes that implement the newly introduced `org.gradle.kotlin.dsl.KotlinScript` interface and the corresponding model objects are now available as _implicit receivers_ in the body of the scripts. In other words, a project script behaves as if the body of the script is enclosed within a `with(project) { …​ }` block, a settings script as if the body of the script is enclosed within a `with(settings) { …​ }` block and an init script as if the body of the script is enclosed within a `with(gradle) { …​ }` block. This implies the corresponding model object is also available as a property in the body of the script, the `project` property for project scripts, the `settings` property for settings scripts and the `gradle` property for init scripts.

As part of the change, the `SettingsScriptApi` interface is no longer implemented by settings scripts and the `InitScriptApi` interface is no longer implemented by init scripts. They should be replaced with the corresponding model object interfaces, `Settings` and `Gradle`.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#miscellaneous)[Miscellaneous](https://docs.gradle.org/userguide/upgrading_version_5.html#miscellaneous)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#javadoc_and_groovydoc_dont_include_timestamps_by_default)[Javadoc and Groovydoc don’t include timestamps by default](https://docs.gradle.org/userguide/upgrading_version_5.html#javadoc_and_groovydoc_dont_include_timestamps_by_default)

Timestamps in the generated documentation have very limited practical use, however they make it impossible to have repeatable documentation builds. Therefore, the `Javadoc` and `Groovydoc` tasks are now configured to not include timestamps by default any more.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#user_provided_config_loc_properties_are_ignored_by_checkstyle)[User provided 'config_loc' properties are ignored by Checkstyle](https://docs.gradle.org/userguide/upgrading_version_5.html#user_provided_config_loc_properties_are_ignored_by_checkstyle)

Gradle always uses `configDirectory` as the value for 'config_loc' when running Checkstyle.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#new_tooling_api_progress_event)[New Tooling API progress event](https://docs.gradle.org/userguide/upgrading_version_5.html#new_tooling_api_progress_event)

In Gradle 6.0, we introduced a new progress event ([org.gradle.tooling.events.test.TestOutputEvent](https://docs.gradle.org/current/javadoc/org/gradle/tooling/events/test/TestOutputEvent.html)) to expose the output of test execution. This new event breaks the convention of having a `StartEvent`-`FinishEvent` pair to express progress. `TaskOutputEvent` is a simple `ProgressEvent`.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_the_task_container_behavior)[Changes to the task container behavior](https://docs.gradle.org/userguide/upgrading_version_5.html#changes_to_the_task_container_behavior)

The following deprecated methods on the task container now result in errors:

* `TaskContainer.add()`

* `TaskContainer.addAll()`

* `TaskContainer.remove()`

* `TaskContainer.removeAll()`

* `TaskContainer.retainAll()`

* `TaskContainer.clear()`

* `TaskContainer.iterator().remove()`

Additionally, the following deprecated functionality now results in an error:

* Replacing a task that has already been realized.

* Replacing a registered (unrealized) task with an incompatible type. A compatible type is the same type or a sub-type of the registered type.

* Replacing a task that has never been registered.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#replaced_and_removed_apis)[Replaced and Removed APIs](https://docs.gradle.org/userguide/upgrading_version_5.html#replaced_and_removed_apis)

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#methods_on_defaulttask_and_projectlayout_replaced_with_objectfactory)[Methods on `DefaultTask` and `ProjectLayout` replaced with `ObjectFactory`](https://docs.gradle.org/userguide/upgrading_version_5.html#methods_on_defaulttask_and_projectlayout_replaced_with_objectfactory)

Use `ObjectFactory.fileProperty()` instead of the following methods that are now removed:

* `DefaultTask.newInputFile()`

* `DefaultTask.newOutputFile()`

* `ProjectLayout.fileProperty()`

Use `ObjectFactory.directoryProperty()` instead of the following methods that are now removed:

* `DefaultTask.newInputDirectory()`

* `DefaultTask.newOutputDirectory()`

* `ProjectLayout.directoryProperty()`

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#annotation_nullable_has_been_removed)[Annotation `@Nullable` has been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#annotation_nullable_has_been_removed)

The `org.gradle.api.Nullable` annotation type has been removed. Use `javax.annotation.Nullable` from JSR-305 instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_jdepend_plugin_has_been_removed)[The JDepend plugin has been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#the_jdepend_plugin_has_been_removed)

The deprecated JDepend plugin has been removed. There are a number of community-provided plugins for code and architecture analysis available on the [Gradle Plugin Portal](https://plugins.gradle.org/).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_osgi_plugin_has_been_removed)[The OSGI plugin has been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#the_osgi_plugin_has_been_removed)

The deprecated OSGI plugin has been removed. There are a number of community-provided OSGI plugins available on the [Gradle Plugin Portal](https://plugins.gradle.org/search?term=osgi).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_announce_and_build_announcements_plugins_have_been_removed)[The announce and build-announcements plugins have been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#the_announce_and_build_announcements_plugins_have_been_removed)

The deprecated announce and build-announcements plugins have been removed. There are a number of community-provided plugins for sending out notifications available on the [Gradle Plugin Portal](https://plugins.gradle.org/).

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_compare_gradle_builds_plugin_has_been_removed)[The Compare Gradle Builds plugin has been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#the_compare_gradle_builds_plugin_has_been_removed)

The deprecated Compare Gradle Builds plugin has been removed. Please use a [Build Scan](https://scans.gradle.com/) for build analysis and comparison.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#the_play_plugins_have_been_removed)[The Play plugins have been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#the_play_plugins_have_been_removed)

The deprecated Play plugin has been removed. An external replacement, the [Play Framework plugin](https://gradle.github.io/playframework), is available from the plugin portal.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#method_abstractcompile_compile_method_has_been_removed)[Method `AbstractCompile.compile()` method has been removed](https://docs.gradle.org/userguide/upgrading_version_5.html#method_abstractcompile_compile_method_has_been_removed)

The abstract method `compile()` is no longer declared by `AbstractCompile`.

Tasks extending `AbstractCompile` can implement their own `@TaskAction` method with the name of their choosing.

They are also free to add a method annotated with `@TaskAction` using an `InputChanges` parameter without having to implement a parameter-less one as well.

#### [](https://docs.gradle.org/userguide/upgrading_version_5.html#other_deprecated_behaviors_and_apis)[Other Deprecated Behaviors and APIs](https://docs.gradle.org/userguide/upgrading_version_5.html#other_deprecated_behaviors_and_apis)

* The `org.gradle.util.internal.GUtil.savePropertiesNoDateComment` has been removed. There is no public replacement for this internal method.

* The deprecated class `org.gradle.api.tasks.compile.CompilerArgumentProvider` has been removed. Use [org.gradle.process.CommandLineArgumentProvider](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html) instead.

* The deprecated class `org.gradle.api.ConventionProperty` has been removed. Use [Providers](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) instead of convention properties.

* The deprecated class `org.gradle.reporting.DurationFormatter` has been removed.

* The bridge method `org.gradle.api.tasks.TaskInputs.property(String name, @Nullable Object value)` returning `TaskInputs` has been removed. A plugin using the method must be compiled with Gradle 4.3 to work on Gradle 6.0.

* The following setters have been removed from `JacocoReportBase`:

  * [executionData](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html#org.gradle.testing.jacoco.tasks.JacocoReport:executionData) - use `getExecutionData().setFrom()` instead.

  * [sourceDirectories](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html#org.gradle.testing.jacoco.tasks.JacocoReport:sourceDirectories) - use `getSourceDirectories().setFrom()` instead.

  * [classDirectories](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html#org.gradle.testing.jacoco.tasks.JacocoReport:classDirectories) - use `getClassDirectories().setFrom()` instead.

  * [additionalClassDirs](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html#org.gradle.testing.jacoco.tasks.JacocoReport:additionalClassDirs) - use `getAdditionalClassDirs().setFrom()` instead.

  * [additionalSourceDirs](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.tasks.JacocoReport.html#org.gradle.testing.jacoco.tasks.JacocoReport:additionalSourceDirs) - use `getAdditionalSourceDirs().setFrom()` instead.

* The `append` property on `JacocoTaskExtension` has been removed. `append` is now always configured to be true for the Jacoco agent.

* The `configureDefaultOutputPathForJacocoMerge` method on `JacocoPlugin` has been removed. The method was never meant to be public.

* File paths in [deployment descriptor file name](https://docs.gradle.org/current/javadoc/org/gradle/plugins/ear/descriptor/DeploymentDescriptor.html#getFileName--) for the ear plugin are not allowed any more. Use a simple name, like `application.xml`, instead.

* The `org.gradle.testfixtures.ProjectBuilder` constructor has been removed. Please use `ProjectBuilder.builder()` instead.

* When [incremental Groovy compilation](https://docs.gradle.org/current/userguide/groovy_plugin.html#sec:incremental_groovy_compilation) is enabled, a wrong configuration of the source roots or enabling Java annotation for Groovy now fails the build. Disable incremental Groovy compilation when you want to compile in those cases.

* `ComponentSelectionRule` no longer can inject the metadata or ivy descriptor. Use the methods on the [`ComponentSelection` parameter](https://docs.gradle.org/current/userguide/resolution_rules.html#sec:component-selection-rules) instead.

* Declaring an [incremental task](https://docs.gradle.org/current/userguide/custom_tasks.html#incremental_tasks) without declaring outputs is now an error. Declare file outputs or use [TaskOutputs.upToDateWhen()](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskOutputs.html#upToDateWhen-groovy.lang.Closure-) instead.

* The `getEffectiveAnnotationProcessorPath()` method is removed from the `JavaCompile` and `ScalaCompile` tasks.

* Changing the value of a task property with type `Property<T>` after the task has started execution now results in an error.

* The `isLegacyLayout()` method is removed from `SourceSetOutput`.

* The map returned by `TaskInputs.getProperties()` is now unmodifiable. Trying to modify it will result in an `UnsupportedOperationException` being thrown.

* There are slight changes in the incubating [capabilities resolution](https://docs.gradle.org/current/userguide/component_capabilities.html#sec:selecting-between-candidates) API, which has been introduced in 5.6, to also allow variant selection based on variant name
