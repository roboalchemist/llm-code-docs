# Source: https://docs.gradle.org/userguide/upgrading_version_7.html

Title: Upgrading from Gradle 7.x to 8.0

URL Source: https://docs.gradle.org/userguide/upgrading_version_7.html

Markdown Content:
This chapter provides the information you need to migrate your Gradle 7.x builds to Gradle 8.0. For migrating from Gradle 6.x, see the [older migration guide](https://docs.gradle.org/current/userguide/upgrading_version_6.html#upgrading_version_6) first.

We recommend the following steps for all users:

1. Try running `gradle help --scan` and view the [deprecations view](https://docs.gradle.com/develocity/get-started/#identifying_deprecated_gradle_functionality) of the generated Build Scan.

![Image 1: Deprecations View in a Build Scan](https://docs.gradle.org/current/userguide/img/deprecations.png)
This is so that you can see any deprecation warnings that apply to your build.

Alternatively, you can run `gradle help --warning-mode=all` to see the deprecations in the console, though it may not report as much detailed information.

1. Update your plugins.

Some plugins will break with this new version of Gradle, for example because they use internal APIs that have been removed or changed. The previous step will help you identify potential problems by issuing deprecation warnings when a plugin does try to use a deprecated part of the API.

1. Run `gradle wrapper --gradle-version 8.0.2` to update the project to 8.0.2.

2. Try to run the project and debug any errors using the [Troubleshooting Guide](https://docs.gradle.org/current/userguide/troubleshooting.html#troubleshooting).

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_8.0)[Upgrading from 7.6 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_8.0)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#warnings_that_are_now_errors)[Warnings that are now errors](https://docs.gradle.org/userguide/upgrading_version_7.html#warnings_that_are_now_errors)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#referencing_tasks_in_an_included_build_with_finalizedby_mustrunafter_or_shouldrunafter)[Referencing tasks in an included build with `finalizedBy`, `mustRunAfter` or `shouldRunAfter`](https://docs.gradle.org/userguide/upgrading_version_7.html#referencing_tasks_in_an_included_build_with_finalizedby_mustrunafter_or_shouldrunafter)

Referencing tasks contained in an included build with any of the following methods now results in an execution time error:

* `finalizedBy`

* `mustRunAfter`

* `shouldRunAfter`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#creating_tar_trees_from_resources_without_backing_files)[Creating TAR trees from resources without backing files](https://docs.gradle.org/userguide/upgrading_version_7.html#creating_tar_trees_from_resources_without_backing_files)

Creating a TAR tree from a resource with no backing file is no longer supported. Instead, convert the resource to a file and use `project.tarTree()` on the file. For more information, see [TAR trees from resources without backing files](https://docs.gradle.org/userguide/upgrading_version_7.html#tar_tree_no_backing_file).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#using_invalid_java_toolchain_specifications)[Using invalid Java toolchain specifications](https://docs.gradle.org/userguide/upgrading_version_7.html#using_invalid_java_toolchain_specifications)

Usage of invalid Java toolchain specifications is no longer supported. Related build errors can be avoided by making sure that language version is set on all toolchain specifications. See [user manual](https://docs.gradle.org/current/userguide/toolchains.html#sec:configuring_toolchain_specifications) for more information.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#using_automatic_toolchain_downloading_without_having_a_repository_configured)[Using automatic toolchain downloading without having a repository configured](https://docs.gradle.org/userguide/upgrading_version_7.html#using_automatic_toolchain_downloading_without_having_a_repository_configured)

Automatic toolchain downloading without explicitly providing repositories to use is no longer supported. See [user manual](https://docs.gradle.org/current/userguide/toolchains.html#sub:download_repositories) for more information.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#changing_test_framework_after_setting_test_framework_options_is_now_an_error)[Changing test framework after setting test framework options is now an error](https://docs.gradle.org/userguide/upgrading_version_7.html#changing_test_framework_after_setting_test_framework_options_is_now_an_error)

When configuring the built-in test task for Java, Groovy, and Scala projects, Gradle no longer allows you to change the test framework used by the `Test` task after configuring options. This was deprecated since it silently discarded configuration in some cases.

The following code example now produces an error:

```
test {
   options {
   }

   useJUnitPlatform()
}
```

Instead, you can:

* set the test framework before configuring options

* migrate to the [JVM Test Suite Plugin](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html#jvm_test_suite_plugin)

```
test {
   // select test framework before configuring options
   useJUnitPlatform()
   options {
   }
}
```

Additionally, setting the test framework multiple times to the _same_ framework now accumulates any options that might be set on the framework. Previously, each time the framework was set, it would cause the framework options to be overwritten.

The following code now results in both the "foo" and "bar" tags to be included for the `test` task:

```
test {
   useJUnitPlatform {
        includeTags("foo")
   }
}
tasks.withType(Test).configureEach {
   // previously, this would overwrite the included tags to only include "bar"
   useJUnitPlatform {
        includeTags("bar")
   }
}
```

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#removed_apis)[Removed APIs](https://docs.gradle.org/userguide/upgrading_version_7.html#removed_apis)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_artifacttransform_api)[Legacy ArtifactTransform API](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_artifacttransform_api)

The legacy `ArtifactTransform` API has been removed. For more information, see [Registering artifact transforms extending `ArtifactTransform`](https://docs.gradle.org/userguide/upgrading_version_7.html#old_artifact_transforms_api).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_incrementaltaskinputs_api)[Legacy IncrementalTaskInputs API](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_incrementaltaskinputs_api)

The legacy `IncrementalTaskInputs` API has been removed. For more information, see [IncrementalTaskInputs type is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#incremental_task_inputs_deprecation). This change also affects Kotlin Gradle Plugin and Android Gradle Plugin. With Gradle 8.0 you should use Kotlin Gradle Plugin 1.6.10 or later and Android Gradle Plugin 7.3.0 with `android.experimental.legacyTransform.forceNonIncremental=true` property or later.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_antlrsourcevirtualdirectory_api)[Legacy AntlrSourceVirtualDirectory API](https://docs.gradle.org/userguide/upgrading_version_7.html#legacy_antlrsourcevirtualdirectory_api)

The legacy `AntlrSourceVirtualDirectory` API has been removed. This change affects the `antlr` plugin. In Gradle 8.0 and above, use the `AntlrSourceDirectorySet` source set extension instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#jvmpluginshelper)[JvmPluginsHelper](https://docs.gradle.org/userguide/upgrading_version_7.html#jvmpluginshelper)

A deprecated `configureDocumentationVariantWithArtifact` method of the `JvmPluginsHelper` class which did not require a `FileResolver` has been removed. This was an internal API, but may have been accessed by plugins. Supply a `FileResolver` to the overloaded version of this method instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#groovydoc_api_cleanup)[Groovydoc API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#groovydoc_api_cleanup)

The deprecated `isIncludePrivate` property of the `Groovydoc` task type has been removed. Use the `access` property along with the `GroovydocAccess#PRIVATE` constant instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#javaapplication_api_cleanup)[JavaApplication API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#javaapplication_api_cleanup)

The deprecated `mainClassName` property of the `JavaApplication` interface has been removed. Use the `mainClass` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#defaultdomainobjectset_api_cleanup)[DefaultDomainObjectSet API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#defaultdomainobjectset_api_cleanup)

The deprecated `DefaultDomainObjectSet(Class)` constructor has been removed. This was an internal API, but may have been used by plugins.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#jacocopluginextension_api_cleanup)[JacocoPluginExtension API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#jacocopluginextension_api_cleanup)

The deprecated `reportsDir` property of the `JacocoPluginExtension` has been removed. Use the `reportsDirectory` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencyinsightreporttask_api_cleanup)[DependencyInsightReportTask API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencyinsightreporttask_api_cleanup)

The deprecated `legacyShowSinglePathToDependnecy` property of the `DependencyInsightReportTask` task type has been removed. Use the `showSinglePathToDependency` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#report_and_testreport_api_cleanup)[Report and TestReport API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#report_and_testreport_api_cleanup)

The deprecated `destination`, and `enabled` properties of the `Report` type have been removed. Use the `outputLocation` and `required` properties instead.

The deprecated `testResultDirs` property of the `TestReport` task type has been removed. Use the `testResults` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#jacocomerge_task_removed)[JacocoMerge Task Removed](https://docs.gradle.org/userguide/upgrading_version_7.html#jacocomerge_task_removed)

The deprecated `JacocoMerge` task type has been removed. The same functionality is also available on the `JacocoReport` task.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#javaexec_api_cleanup)[JavaExec API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#javaexec_api_cleanup)

The deprecated `main` property of the `JavaExec` task type has been removed. Use the `mainClass` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractexectask_api_cleanup)[AbstractExecTask API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractexectask_api_cleanup)

The deprecated `execResult` getter property of the `AbstractExecTask` task type has been removed. Use the `executionResult` getter property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#abstracttesttask_api_cleanup)[AbstractTestTask API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#abstracttesttask_api_cleanup)

The deprecated `binResultsDir` property of the `AbstractTestTask` task type has been removed. Use the `binaryResultsDirectory` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#sourcedirectoryset_api_cleanup)[SourceDirectorySet API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#sourcedirectoryset_api_cleanup)

The deprecated `outputDir` property of the `SourceDirectorySet` type has been removed. Use the `destinationDirectory` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#versioncatalog_api_cleanup)[VersionCatalog API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#versioncatalog_api_cleanup)

The deprecated `findDependency(String)` method and `dependencyAliases` property of the `VersionCatalog` type have been removed. Use the `findLibrary(String)` method and `libraryAliases` property instead.

The deprecated `alias(String)` method of the `VersionCatalogBuilder` type has been removed. Use the `library(String, String, String)` or `plugin(String, String)` methods instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#workerexecutor_api_cleanup)[WorkerExecutor API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#workerexecutor_api_cleanup)

The deprecated `submit(Class, Action)` method of the `WorkerExecutor` interface has been removed. Instead, obtain a `WorkQueue` via the `noIsolation()`, `classLoaderIsolation()`, and `processIsolation()`, methods and use the `submit(Class, Action)` method on the `WorkQueue` instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencysubstitution_api_cleanup)[DependencySubstitution API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencysubstitution_api_cleanup)

The deprecated `with(ComponentSelector)` method of the `DependencySubstitution` type’s inner `Substitution` type’s has been removed. Use the `using(ComponentSelector)` method instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractarchivetask_api_cleanup)[AbstractArchiveTask API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractarchivetask_api_cleanup)

The deprecated `appendix`, `archiveName`, `archivePath`, `baseName`, `classifier`, `destinationDir`, `extension` and `version` properties of the `AbstractArchiveTask` task type have been removed. Use the `archiveAppendix`, `archiveFileName` , `archiveFile`, `archiveBaseName`, `archiveClassifier`, `destinationDirectory`, `archiveExtension` and `archiveVersion` properties instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractcompile_api_deprecations)[AbstractCompile API Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#abstractcompile_api_deprecations)

The previously deprecated `destinationDir` property of the `AbstractCompile` remains deprecated, and will now emit a deprecation warning upon use. It is now scheduled for removal in Gradle 9.0.0. Use the `destinationDirectory` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#resolvedcomponentresult_api_cleanup)[ResolvedComponentResult API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#resolvedcomponentresult_api_cleanup)

The deprecated `getVariant` method of the `ResolvedComponentResult` interface has been removed. Use the `getVariants` method instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#code_quality_plugins_api_cleanup)[Code quality plugins API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#code_quality_plugins_api_cleanup)

The deprecated `antBuilder` property of the `Checkstyle`, `CodeNarc` and `Pmd` task types has been removed. Use the `Project` type’s `ant` property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#usage_api_cleanup)[Usage API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#usage_api_cleanup)

The deprecated public fields `JAVA_API_CLASSES`, `JAVA_API_JARS`, `JAVA_RUNTIME_CLASSES`, `JAVA_RUNTIME_JARS` and `JAVA_RUNTIME_RESOURCES` of the `Usage` type have been removed. The values are available in the **internal**`JavaEcosystemSupport` class for compatibility with previously published modules, but should **not** be used for any new publishing.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#externaldependency_api_cleanup)[ExternalDependency API Cleanup](https://docs.gradle.org/userguide/upgrading_version_7.html#externaldependency_api_cleanup)

The deprecated `setForce(boolean)` method of the `ExternalDependency` interface has been removed. Use the `version(Action)` method to configure strict versions instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#build_scan_method_removed_from_kotlin_dsl)[Build-scan method removed from Kotlin DSL](https://docs.gradle.org/userguide/upgrading_version_7.html#build_scan_method_removed_from_kotlin_dsl)

The deprecated `build-scan` plugin application method has been removed from the Kotlin DSL. Use the `gradle-enterprise` method instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#configuration_extension_methods_removed_from_kotlin_dsl)[Configuration extension methods removed from Kotlin DSL](https://docs.gradle.org/userguide/upgrading_version_7.html#configuration_extension_methods_removed_from_kotlin_dsl)

The Kotlin DSL added specialized extension methods for `NamedDomainObjectProvider<Configuration>` that are available when looking up a configuration by name. These extensions allowed builds to access some properties of a `Configuration` when using an instance of `NamedDomainObjectProvider<Configuration>` directly:

```
configurations.compileClasspath.files // equivalent to configurations.compileClasspath.get().files
configurations.compileClasspath.singleFile // equivalent to configurations.compileClasspath.get().singleFile
```

All of these extensions have been removed from the API, but the methods are still available for plugins compiled against older versions of Gradle.

* NamedDomainObjectProvider<Configuration>.addToAntBuilder

* NamedDomainObjectProvider<Configuration>.all

* NamedDomainObjectProvider<Configuration>.allArtifacts

* NamedDomainObjectProvider<Configuration>.allDependencies

* NamedDomainObjectProvider<Configuration>.allDependencyConstraints

* NamedDomainObjectProvider<Configuration>.artifacts

* NamedDomainObjectProvider<Configuration>.asFileTree

* NamedDomainObjectProvider<Configuration>.asPath

* NamedDomainObjectProvider<Configuration>.attributes

* NamedDomainObjectProvider<Configuration>.buildDependencies

* NamedDomainObjectProvider<Configuration>.contains

* NamedDomainObjectProvider<Configuration>.copy

* NamedDomainObjectProvider<Configuration>.copyRecursive

* NamedDomainObjectProvider<Configuration>.defaultDependencies

* NamedDomainObjectProvider<Configuration>.dependencies

* NamedDomainObjectProvider<Configuration>.dependencyConstraints

* NamedDomainObjectProvider<Configuration>.description

* NamedDomainObjectProvider<Configuration>.exclude

* NamedDomainObjectProvider<Configuration>.excludeRules

* NamedDomainObjectProvider<Configuration>.extendsFrom

* NamedDomainObjectProvider<Configuration>.fileCollection

* NamedDomainObjectProvider<Configuration>.files

* NamedDomainObjectProvider<Configuration>.filter

* NamedDomainObjectProvider<Configuration>.getTaskDependencyFromProjectDependency

* NamedDomainObjectProvider<Configuration>.hierarchy

* NamedDomainObjectProvider<Configuration>.incoming

* NamedDomainObjectProvider<Configuration>.isCanBeConsumed

* NamedDomainObjectProvider<Configuration>.isCanBeResolved

* NamedDomainObjectProvider<Configuration>.isEmpty

* NamedDomainObjectProvider<Configuration>.isTransitive

* NamedDomainObjectProvider<Configuration>.isVisible

* NamedDomainObjectProvider<Configuration>.minus

* NamedDomainObjectProvider<Configuration>.outgoing

* NamedDomainObjectProvider<Configuration>.plus

* NamedDomainObjectProvider<Configuration>.resolutionStrategy

* NamedDomainObjectProvider<Configuration>.resolve

* NamedDomainObjectProvider<Configuration>.resolvedConfiguration

* NamedDomainObjectProvider<Configuration>.setDescription

* NamedDomainObjectProvider<Configuration>.setExtendsFrom

* NamedDomainObjectProvider<Configuration>.setTransitive

* NamedDomainObjectProvider<Configuration>.singleFile

* NamedDomainObjectProvider<Configuration>.state

* NamedDomainObjectProvider<Configuration>.withDependencies

You should prefer to directly reference the methods from `Configuration`.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#javaforkoptions_getjvmargs_and_getalljvmargs_return_immutable_lists)[`JavaForkOptions``getJvmArgs()` and `getAllJvmArgs()` return immutable lists](https://docs.gradle.org/userguide/upgrading_version_7.html#javaforkoptions_getjvmargs_and_getalljvmargs_return_immutable_lists)

The lists of JVM arguments retrieved from the `JavaForkOptions` interface are now immutable.

Previously, modifications of the returned list were silently ignored.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#nullable_annotations_better_reflect_actual_nullability_of_api)[Nullable annotations better reflect actual nullability of API](https://docs.gradle.org/userguide/upgrading_version_7.html#nullable_annotations_better_reflect_actual_nullability_of_api)

In some APIs, nullability was not correctly annotated and APIs that did allow null or returned null were marked as non-null. In Java or Groovy, this mismatch did not cause problems at compile time. In Kotlin, this mismatch made valid code difficult to write because the language would not allow you to pass null.

One particular example was returning `null` from a `Provider#map` or `Provider#flatMap`. In both APIs, Gradle allows you to return null, but in the Kotlin DSL this was considered illegal.

This correction may cause compilation errors in code that expected non-null.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#plugins_tasks_and_extension_classes_are_abstract)[Plugins, tasks and extension classes are abstract](https://docs.gradle.org/userguide/upgrading_version_7.html#plugins_tasks_and_extension_classes_are_abstract)

Most public classes for plugins, tasks and extensions have been made abstract. This was done to make it easier to remove boilerplate from Gradle’s implementation.

Plugins that are affected by this change should make their classes abstract as well. Gradle uses runtime class decoration to implement abstract methods as long as the object is instantiated via `ObjectFactory` or some other automatic mechanism (like [managed properties](https://docs.gradle.org/current/userguide/properties_providers.html#managed_properties)). Those methods should never be directly implemented.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#wrapper_task_configuration)[Wrapper task configuration](https://docs.gradle.org/userguide/upgrading_version_7.html#wrapper_task_configuration)

If `gradle-wrapper.properties` contains the `distributionSha256Sum` property, you must specify a sum. You can specify a sum in the wrapped task configuration or with the `--gradle-distribution-sha256-sum` task option.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_in_the_abstractcodequalityplugin_class)[Changes in the AbstractCodeQualityPlugin class](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_in_the_abstractcodequalityplugin_class)

The deprecated `AbstractCodeQualityPlugin.getJavaPluginConvention()` method was removed in Gradle 8.0. You should use `JavaPluginExtension` instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#remove_implicit_add_opens_for_gradle_workers)[Remove implicit `--add-opens` for Gradle workers](https://docs.gradle.org/userguide/upgrading_version_7.html#remove_implicit_add_opens_for_gradle_workers)

Before Gradle 8.0, Gradle workers on JDK9+ automatically opened JDK modules `java.base/java.util` and `java.base/java.lang` by passing `--add-opens` CLI arguments. This enabled code executed in a Gradle worker to perform deep reflection on JDK internals without warning or failing. Workers no longer use these implicit arguments.

This affects all internal Gradle workers, which are used for a variety of tasks:

* code-quality plugins (Checkstyle, CodeNarc, Pmd)

* ScalaDoc

* AntlrTask

* JVM compiler daemons

* tasks executed using process isolation via the [Worker API](https://docs.gradle.org/current/userguide/worker_api.html)

New warnings and errors may appear in any tools, extensions, or plugins that perform deep reflection into JDK internals with the worker API.

These errors can be resolved by updating the violating code or dependency. Updates may include:

* code-quality tools

* annotation processors

* any Gradle plugins which use the worker API

For some examples of possible error or warning outputs which may arise due to this change, see [Removes implicit `--add-opens` for test workers](https://docs.gradle.org/userguide/upgrading_version_7.html#remove_test_add_opens).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#sourceset_classesdirs_no_longer_depends_upon_the_entire_sourceset_as_a_task_dependency)[SourceSet classesDirs no longer depends upon the entire SourceSet as a task dependency](https://docs.gradle.org/userguide/upgrading_version_7.html#sourceset_classesdirs_no_longer_depends_upon_the_entire_sourceset_as_a_task_dependency)

Prior to Gradle 8.0, the task dependencies for `SourceSetOutput.classesDirs` included tasks that did not produce class files. This meant that a task which depends on `classesDirs` would also depend on `classes`, `processResources`, and any other task dependency added to `SourceSetOutput`. This behavior was potentially an error because the `classesDirs` property did not contain the output for `processResources`. Since 8.0, this implicit dependency is removed. Now, depending on `classesDirs` only executes the tasks which directly produce files in the classes directories.

Consider the following buildscript:

```
plugins {
    id 'java-library'
}
// Task lists all files in the given classFiles FileCollection
tasks.register("listClassFiles", ListClassFiles) {
    classFiles.from(java.sourceSets.main.output.classesDirs)
}
```

Previously, the `listClassFiles` task depended on `compileJava`, `processResources`, and `classes`. Now, only `compileJava` is a task dependency of `listClassFiles`.

If a task in your build relied on the previous behavior, you can instead use the entire `SourceSetOutput` as an input, which contains all classes and resources.

If that is not feasible, you can restore the previous behavior by adding more task dependencies to `classesDirs`:

```
java {
    sourceSets {
        main {
            output.classesDirs.builtBy(output)
        }
    }
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#minimal_supported_kotlin_gradle_plugin_version_changed)[Minimal supported Kotlin Gradle Plugin version changed](https://docs.gradle.org/userguide/upgrading_version_7.html#minimal_supported_kotlin_gradle_plugin_version_changed)

Gradle 7.x supports Kotlin Gradle Plugin 1.3.72 and above. Kotlin Gradle Plugin versions above 1.6.21 are not tested with Gradle 7.x. Gradle 8.x supports Kotlin Gradle Plugin 1.6.10 and above. You can use a lower Kotlin language version by modifying the language version and api version setting in the Kotlin compilation tasks.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#minimal_supported_android_gradle_plugin_version_changed)[Minimal supported Android Gradle Plugin version changed](https://docs.gradle.org/userguide/upgrading_version_7.html#minimal_supported_android_gradle_plugin_version_changed)

Gradle 7.x supports Android Gradle Plugin (AGP) 4.1 and above. AGP versions above 7.3 are not tested with Gradle 7.x. Gradle 8.x supports AGP 8 and above. Gradle 8.x supports AGP 7.3 and above if you configure the following property:

`android.experimental.legacyTransform.forceNonIncremental=true`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#change_to_antbuilder_parent_class)[Change to `AntBuilder` parent class](https://docs.gradle.org/userguide/upgrading_version_7.html#change_to_antbuilder_parent_class)

Previously, `org.gradle.api.AntBuilder` extended the deprecated `groovy.util.AntBuilder` class. It now extends `groovy.ant.AntBuilder`.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#plugindeclaration_is_not_serializable)[`PluginDeclaration` is not serializable](https://docs.gradle.org/userguide/upgrading_version_7.html#plugindeclaration_is_not_serializable)

`org.gradle.plugin.devel.PluginDeclaration` is not serializable anymore. If you need to serialize it, you can convert it into your own, serializable class.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_does_not_use_equals_for_serialized_values_in_up_to_date_checks)[Gradle does not use equals for serialized values in up-to-date checks](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_does_not_use_equals_for_serialized_values_in_up_to_date_checks)

Gradle now does not try to use equals when comparing serialized values in up-to-date checks. For more information see [Relying on equals for up-to-date checks is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#equals_up_to_date_deprecation).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#task_and_transform_validation_warnings_introduced_in_gradle_7_x_are_now_errors)[Task and transform validation warnings introduced in Gradle 7.x are now errors](https://docs.gradle.org/userguide/upgrading_version_7.html#task_and_transform_validation_warnings_introduced_in_gradle_7_x_are_now_errors)

Gradle introduced additional task and artifact transform validation warnings in the Gradle 7.x series. Those warnings are now errors in Gradle 8.0 and will fail the build.

Warnings that became errors:

* An input file collection that can’t be resolved.

* An input or output file or directory that cannot be read. See [Declaring input or output directories which contain unreadable content](https://docs.gradle.org/userguide/upgrading_version_7.html#declare_unreadable_input_output).

* Using a `java.io.File` as the `@InputArtifact` of an artifact transform.

* Using an input with an unknown implementation. See [Cannot use an input with an unknown implementation](https://docs.gradle.org/current/userguide/validation_problems.html#implementation_unknown).

* Missing dependencies between tasks. See [Implicit dependencies between tasks](https://docs.gradle.org/current/userguide/validation_problems.html#implicit_dependency).

* Converting files to a classpath where paths contain file separator.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_does_not_ignore_empty_directories_for_file_trees_with_skipwhenempty)[Gradle does not ignore empty directories for file-trees with `@SkipWhenEmpty`](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_does_not_ignore_empty_directories_for_file_trees_with_skipwhenempty)

Previously Gradle used to detect if an input file collection annotated with `@SkipWhenEmpty` consisted only of file trees and then ignored directories automatically. To ignore directories in Gradle 8.0 and later, the input property needs to be explicitly annotated with `@IgnoreEmptyDirectories`. For more information see [File trees and empty directory handling](https://docs.gradle.org/userguide/upgrading_version_7.html#empty_directories_file_tree).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#format_of_javaversion_has_changed_for_java_9_and_java_10)[Format of `JavaVersion` has changed for Java 9 and Java 10](https://docs.gradle.org/userguide/upgrading_version_7.html#format_of_javaversion_has_changed_for_java_9_and_java_10)

The string format of the `JavaVersion` has changed to match the official Java versioning. Starting from Java 9, the language version must not contain the `1.` prefix. This affects the format of the `sourceCompatiblity` and `targetCompatibility` properties on the `JavaCompile` task and `JavaExtension`. The old format is still supported when resolving the `JavaVersion` from a string.

Gradle 7.6 Gradle 8.0
`1.8``1.8`
`1.9``9`
`1.10``10`
`11``11`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#strict-kotlin-dsl-precompiled-scripts-accessors-by-default)[Precompiled script plugins use strict Kotlin DSL accessor generation by default](https://docs.gradle.org/userguide/upgrading_version_7.html#strict-kotlin-dsl-precompiled-scripts-accessors-by-default)

In precompiled script plugins, type safe Kotlin DSL accessor generation now fails the build if a plugin fails to apply.

Starting in Gradle 7.6, builds could enable this behavior with the `org.gradle.kotlin.dsl.precompiled.accessors.strict` system property. This behavior is now default. The property has been deprecated and its usage should be removed. You can find more information about this property [below](https://docs.gradle.org/userguide/upgrading_version_7.html#strict-kotlin-dsl-precompiled-scripts-accessors).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#init_scripts_are_applied_to_buildsrc_builds)[Init scripts are applied to `buildSrc` builds](https://docs.gradle.org/userguide/upgrading_version_7.html#init_scripts_are_applied_to_buildsrc_builds)

Init scripts specified using `--init-script` are now applied to `buildSrc` builds. In previous releases these were applied to included builds but not `buildSrc builds.

This behavior is now consistent for `buildSrc` and included builds.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_no_longer_runs_the_build_task_for_buildsrc_builds)[Gradle no longer runs the `build` task for `buildSrc` builds](https://docs.gradle.org/userguide/upgrading_version_7.html#gradle_no_longer_runs_the_build_task_for_buildsrc_builds)

When Gradle builds the output of `buildSrc` it runs only the tasks that produce that output, which is typically the `jar` task. In previous releases Gradle would run the `build` task.

This means that the tests of `buildSrc` and its subprojects are not built and executed automatically and must now be explicitly requested.

This behavior is now consistent for `buildSrc` and included builds.

You can run the tests for `buildSrc` in the same way as projects in included builds, for example by running `gradle buildSrc:build`.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#buildfinished_hook_for_buildsrc_runs_after_all_tasks_have_executed)[`buildFinished { }` hook for `buildSrc` runs after all tasks have executed](https://docs.gradle.org/userguide/upgrading_version_7.html#buildfinished_hook_for_buildsrc_runs_after_all_tasks_have_executed)

The `buildFinished {}` hook for `buildSrc` now runs after all tasks have completed. In previous releases this hook would run immediately after the tasks for `buildSrc` completed and before any requested tasks started.

This behavior is now consistent for `buildSrc` and included builds.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_to_paths_of_included_builds)[Changes to paths of included builds](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_to_paths_of_included_builds)

In order to handle conflicts between nested included build names better, Gradle now uses the directory hierarchy of included builds to assign the build path. If you are running tasks from the command line in nested included builds, then you may need to adjust your invocation.

For example, if you have the following hierarchy:

`Kotlin``Groovy`

```
.
├── settings.gradle
└── nested
    ├── settings.gradle
    └── nestedNested
        └── settings.gradle
```

settings.gradle

`includeBuild("nested")`

nested/settings.gradle

`includeBuild("nestedNested")`

Before Gradle 8.0, you ran `gradle :nestedNested:compileJava`. In Gradle 8.0 the invocation changes to `gradle :nested:nestedNested:compileJava`.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#adding_jst_ejb_with_the_eclipse_wtp_plugin_now_removes_the_jst_utility_facet)[Adding `jst.ejb` with the `eclipse wtp` plugin now removes the `jst.utility` facet](https://docs.gradle.org/userguide/upgrading_version_7.html#adding_jst_ejb_with_the_eclipse_wtp_plugin_now_removes_the_jst_utility_facet)

The `eclipse wtp` plugin adds the `jst.utility` facet to java projects. Now, adding the `jst.ejb` facet implicitly removes the `jst.utility` facet:

```
eclipse {
    wtp {
        facet {
            facet name: 'jst.ejb', version: '3.2'
        }
    }
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#simplifying_pmd_custom_rules_configuration)[Simplifying PMD custom rules configuration](https://docs.gradle.org/userguide/upgrading_version_7.html#simplifying_pmd_custom_rules_configuration)

Previously, you had to explicitly configure PMD to ignore default rules with `ruleSets = []`. In the Gradle 8.0, setting `ruleSetConfig` or `ruleSetFiles` to a non-empty value implicitly ignores default rules.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#report_getoutputlocation_return_type_changed_from_provider_to_property)[Report `getOutputLocation` return type changed from Provider to Property](https://docs.gradle.org/userguide/upgrading_version_7.html#report_getoutputlocation_return_type_changed_from_provider_to_property)

The `outputLocation` property of the [Report](https://docs.gradle.org/current/dsl/org.gradle.api.reporting.Report.html#org.gradle.api.reporting.Report) now returns a value of type `Property<? extends FileSystemLocation>`. Previously, `outputLocation` returned a value of type `Provider<? extends FileSystemLocation>`.

This change makes the Report API more internally consistent, and allows for more idiomatic configuration of reporting tasks.

The former, now `@Deprecated` usage:

```
tasks.named('test') {
    reports.junitXml.setDestination(layout.buildDirectory.file('reports/my-report-old').get().asFile) // DEPRECATED
}
```

can be replaced with:

```
tasks.named('test') {
    reports.junitXml.outputLocation = layout.buildDirectory.dir('reports/my-report')
}
```

Many built-in and custom reports, such as those used by JUnit, implement this interface. Plugins compiled against an earlier version of Gradle containing the previous method signature may need to be recompiled to be used with newer versions of Gradle containing the new signature.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#removed_external_plugin_validation_plugin)[Removed external plugin validation plugin](https://docs.gradle.org/userguide/upgrading_version_7.html#removed_external_plugin_validation_plugin)

The incubating plugin `ExternalPluginValidationPlugin` has been removed. Use the [`java-gradle-plugin`](https://docs.gradle.org/current/userguide/java_gradle_plugin.html)'s `validatePlugins` task to validate plugins under development.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#reproducible_archives_can_change_compared_to_past_versions)[Reproducible archives can change compared to past versions](https://docs.gradle.org/userguide/upgrading_version_7.html#reproducible_archives_can_change_compared_to_past_versions)

Gradle changes the compression library used for creating archives from an Ant based one to [Apache Commons Compress™](https://commons.apache.org/proper/commons-compress/). As a consequence archives created from the same content, are unlikely to end up identical byte-by-byte to their older versions, created with the old library.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_language_1_8)[Updated the Kotlin DSL to Kotlin API Level 1.8](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_language_1_8)

Previously, the Kotlin DSL used Kotlin API level 1.4. Starting with Gradle 8.0, the Kotlin DSL uses Kotlin API level 1.8. This change brings all the improvements made to the Kotlin language and standard library since Kotlin 1.4.0.

For information about breaking and nonbreaking changes in this upgrade, see the following links to the Kotlin documentation:

* Kotlin 1.5 [language](https://kotlinlang.org/docs/whatsnew15.html#language-features) / [standard library](https://kotlinlang.org/docs/whatsnew15.html#standard-library)

* Kotlin 1.6 [language](https://kotlinlang.org/docs/whatsnew16.html#language) / [standard library](https://kotlinlang.org/docs/whatsnew16.html#standard-library)

* Kotlin 1.7 [language](https://kotlinlang.org/docs/whatsnew17.html#language) / [standard library](https://kotlinlang.org/docs/whatsnew17.html#standard-library)

* Kotlin 1.8 [language](https://kotlinlang.org/docs/whatsnew18.html#language) / [standard library](https://kotlinlang.org/docs/whatsnew18.html#standard-library)

Note that the Kotlin Gradle Plugin 1.8.0 started using Java toolchains. It is recommended you configure a toolchain instead of defining Java `sourceCompatibility`/`targetCompatibility` in Kotlin projects.

Also note that the Kotlin Gradle Plugin 1.8.0 introduced `compilerOptions` with lazy configuration properties as a replacement for `kotlinOptions` which did not support lazy configuration. It is recommended you configure Kotlin compilation using `compilerOptions` instead of `kotlinOptions`.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_dsl_plugin_toolchains)[`kotlinDslPluginOptions.jvmTarget` is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_dsl_plugin_toolchains)

Previously, you could use `kotlinDslPluginOptions.jvmTarget` to configure which JVM target should be used for compiling code when using the `kotlin-dsl` plugin.

Starting with Gradle 8.0, `kotlinDslPluginOptions.jvmTarget` is deprecated. You should [configure a Java Toolchain](https://docs.gradle.org/current/userguide/kotlin_dsl.html#sec:kotlin-dsl_plugin) instead.

If you already have a Java Toolchain configured and `kotlinDslPluginOptions.jvmTarget` unset then Gradle 8.0 will now use the Java Toolchain as the JVM target instead of the previous default target (1.8).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#java_base_plugin_now_sets_jar_war_and_ear_destination_directory_defaults)[Java Base Plugin now sets Jar, War, and Ear destination directory defaults](https://docs.gradle.org/userguide/upgrading_version_7.html#java_base_plugin_now_sets_jar_war_and_ear_destination_directory_defaults)

Previously, the `base` plugin configured the [destinationDirectory](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.AbstractArchiveTask.html#org.gradle.api.tasks.bundling.AbstractArchiveTask:destinationDirectory) of [Jar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Jar.html), [War](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.War.html), and [Ear](https://docs.gradle.org/current/dsl/org.gradle.plugins.ear.Ear.html) tasks to the directory specified by [BasePluginExtension#getLibsDirectory](https://docs.gradle.org/current/dsl/org.gradle.api.plugins.BasePluginExtension.html#org.gradle.api.plugins.BasePluginExtension:libsDirectory). In Gradle 8.0, `java-base` handles this configuration. No changes are required for projects that already apply the `java-base` plugin directly or indirectly through the `java`, `application`, `java-library`, or other JVM ecosystem plugins.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#upload_task_should_not_be_used)[Upload Task should not be used](https://docs.gradle.org/userguide/upgrading_version_7.html#upload_task_should_not_be_used)

The `Upload` task remains deprecated and is now scheduled for removal in Gradle 9.0.0. Although this type remains, it is no longer functional and will throw an exception upon running. It is preserved solely to avoid breaking plugins. Use the tasks in the `maven-publish` or `ivy-publish` plugins instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#configurations_no_longer_allowed_as_dependencies)[Configurations no longer allowed as Dependencies](https://docs.gradle.org/userguide/upgrading_version_7.html#configurations_no_longer_allowed_as_dependencies)

Adding a Configuration as a dependency in the `dependencies` DSL block, or programmatically using the `DependencyHandler` classes' `doAdd(Configuration, Object, Closure)` method, is no longer allowed and will fail with an exception. To replicate many aspects of this behavior, extend configurations using the `extendsFrom(Configuration)` method on `Configuration` instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecated_for_consumption_configurations_are_now_non_consumable)[Deprecated for consumption configurations are now non-consumable](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecated_for_consumption_configurations_are_now_non_consumable)

The following configurations were never meant to be consumed:

* The `antlr` configuration created by the `AntlrPlugin`

* The `zinc` configuration created by the `ScalaBasePlugin`

* The `providedCompile` and `providedRuntime` configurations created by the `WarPlugin`

These configurations were deprecated for consumption and are now no longer consumable. Attempting to consume them will result in an error.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#identical_consumable_configurations_are_now_an_error)[Identical consumable configurations are now an error](https://docs.gradle.org/userguide/upgrading_version_7.html#identical_consumable_configurations_are_now_an_error)

If a project has multiple consumable configurations that share the same attributes and capabilities declaration, the build will fail when publishing or resolving as a dependency that project. This was [previously deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#unique_attribute_sets).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#toolchain_based_tasks_for_jvm_projects)[Toolchain-based tasks for JVM projects](https://docs.gradle.org/userguide/upgrading_version_7.html#toolchain_based_tasks_for_jvm_projects)

Starting with Gradle 8.0, all core Java tasks that have toolchain support are now using toolchains unconditionally. If `JavaBasePlugin` is applied, the convention value for tool properties on the task is defined by the toolchain configured on the `java` extension. In case no toolchains are explicitly configured, the toolchain corresponding to the JVM running Gradle is used.

Similarly, tasks from the Groovy and Scala plugins also rely on toolchains to determine on which JVM they are executed.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#scala_compilation_target)[Scala compilation target](https://docs.gradle.org/userguide/upgrading_version_7.html#scala_compilation_target)

With the toolchain changes described above, Scala compilation tasks are now always provided with a `target` or `release` parameter. The exact parameter and value depend on toolchain usage, or not, and Scala version.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#pluginbundle_dropped_in_plugin_publish_plugin)[`pluginBundle` dropped in Plugin Publish plugin](https://docs.gradle.org/userguide/upgrading_version_7.html#pluginbundle_dropped_in_plugin_publish_plugin)

Gradle 8 no longer supports the `pluginBundle` extension. Its functionality has been merged into the `gradlePlugin` block. These changes require recent versions of the Plugin Publish plugin ([1.0.+](https://plugins.gradle.org/plugin/com.gradle.plugin-publish/1.1.0)). Documentation on configuring plugin publication can be found both [on the Portal](https://plugins.gradle.org/docs/publish-plugin) and [in the user manual](https://docs.gradle.org/current/userguide/publishing_gradle_plugins.html#configure_the_plugin_publishing_plugin).

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.6)[Upgrading from 7.5 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.6)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#strict-kotlin-dsl-precompiled-scripts-accessors)[Strict Kotlin DSL precompiled script plugins accessors generation](https://docs.gradle.org/userguide/upgrading_version_7.html#strict-kotlin-dsl-precompiled-scripts-accessors)

Type safe Kotlin DSL accessors generation for precompiled script plugins does not fail the build by default if a plugin requested in such precompiled scripts fails to be applied. Because the cause could be environmental and for backwards compatibility reasons, this behaviour hasn’t changed yet.

Back in Gradle 7.1 the `:generatePrecompiledScriptPluginAccessors` task responsible for the accessors generation has been marked as non-cacheable by default. The `org.gradle.kotlin.dsl.precompiled.accessors.strict` system property was introduced in order to offer an opt-in to a stricter mode of operation that fails the build when a plugin application fails, and enable the build cache for that task.

Starting with Gradle 7.6, non-strict accessors generation for Kotlin DSL precompiled script plugins has been deprecated. This will change in Gradle 8.0. Strict accessor generation will become the default. To opt in to the strict behavior, set the 'org.gradle.kotlin.dsl.precompiled.accessors.strict' system property to `true`.

This can be achieved persistently in the `gradle.properties` file in your build root directory:

`systemProp.org.gradle.kotlin.dsl.precompiled.accessors.strict=true`

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_2)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_2)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_1_7_10)[Upgrade to Kotlin 1.7.10](https://docs.gradle.org/userguide/upgrading_version_7.html#kotlin_1_7_10)

The embedded Kotlin has been updated to [Kotlin 1.7.10](https://github.com/JetBrains/kotlin/releases/tag/v1.7.10).

Gradle doesn’t ship with the `kotlin-gradle-plugin` but the upgrade to 1.7.10 can bring the new version. For example when you use the `kotlin-dsl` plugin.

The `kotlin-gradle-plugin` version 1.7.10 changes the type hierarchy of the `KotlinCompile` task type. It doesn’t extend from `AbstractCompile` anymore. If you used to select Kotlin compilation tasks by `AbstractCompile` you need to change that to `KotlinCompile`.

For example, this

`tasks.named<AbstractCompile>("compileKotlin")`

needs to be changed to

`tasks.named<KotlinCompile>("compileKotlin")`

In the same vein, if you used to filter tasks by `AbstractCompile` you won’t obtain the Kotlin compilation tasks anymore:

```
tasks.withType<AbstractCompile>().configureEach {
    // ...
}
```

needs to be changed to

```
tasks.withType<AbstractCompile>().configureEach {
    // ...
}
tasks.withType<KotlinCompile>().configureEach {
    // ...
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#upgrade_to_groovy_3_0_13)[Upgrade to Groovy 3.0.13](https://docs.gradle.org/userguide/upgrading_version_7.html#upgrade_to_groovy_3_0_13)

Since the previous version was 3.0.10, the [3.0.11](https://groovy-lang.org/changelogs/changelog-3.0.11.html) and [3.0.12](https://groovy-lang.org/changelogs/changelog-3.0.12.html) changes are also included.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#upgrade_to_codenarc_3_1_0)[Upgrade to CodeNarc 3.1.0](https://docs.gradle.org/userguide/upgrading_version_7.html#upgrade_to_codenarc_3_1_0)

The default version of CodeNarc has been updated to [3.1.0](https://github.com/CodeNarc/CodeNarc/blob/master/CHANGELOG.md#version-310----jun-2022).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#configuring_a_non_existing_executable_now_fails)[Configuring a non-existing executable now fails](https://docs.gradle.org/userguide/upgrading_version_7.html#configuring_a_non_existing_executable_now_fails)

When configuring an executable explicitly for [`JavaCompile`](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.ForkOptions.html#org.gradle.api.tasks.compile.ForkOptions:executable) or [`Test`](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html#org.gradle.api.tasks.testing.Test:executable) tasks, Gradle will now emit an error if this executable does not exist. In the past, the task would be executed with the default toolchain or JVM running the build.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_to_dependency_declarations_in_test_suites)[Changes to dependency declarations in Test Suites](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_to_dependency_declarations_in_test_suites)

As part of the ongoing effort to evolve Test Suites, dependency declarations in the Test Suites `dependencies` block are [now strongly typed](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html#sec:differences_with_top_level_dependencies). This will help make this incubating API more discoverable and easier to use in an IDE.

In some cases, this requires syntax changes. For example, build scripts that previously added Test Suite dependencies with the following syntax:

```
testing {
  suites {
    register<JvmTestSuite>("integrationTest") {
      dependencies {
        implementation(project)
      }
    }
  }
}
```

will now fail to compile, with a message like:

```
None of the following functions can be called with the arguments supplied:
public operator fun DependencyAdder.invoke(dependencyNotation: CharSequence): Unit defined in org.gradle.kotlin.dsl
public operator fun DependencyAdder.invoke(dependency: Dependency): Unit defined in org.gradle.kotlin.dsl
public operator fun DependencyAdder.invoke(files: FileCollection): Unit defined in org.gradle.kotlin.dsl
public operator fun DependencyAdder.invoke(dependency: Provider<out Dependency>): Unit defined in org.gradle.kotlin.dsl
public operator fun DependencyAdder.invoke(externalModule: ProviderConvertible<out MinimalExternalModuleDependency>): Unit defined in org.gradle.kotlin.dsl
```

To fix this, replace the reference to `project` with a call to `project()`:

```
testing {
  suites {
    register<JvmTestSuite>("integrationTest") {
      dependencies {
        implementation(project())
      }
    }
  }
}
```

Other syntax effected by this change includes:

* You cannot use `Provider<String>` as a dependency declaration.

* You cannot use a `Map` as a dependency declaration for Kotlin or Java.

* You cannot use a bundle as a dependency declaration directly (`implementation(libs.bundles.testing)`). Use `implementation.bundle(libs.bundles.testing)` instead.

For more information, see the updated [declare an additional test suite](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html#sec:declare_an_additional_test_suite) example in the JVM Test Suite Plugin section of the user guide.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#invalid_toolchain_specification_deprecation)[Usage of invalid Java toolchain specifications is now deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#invalid_toolchain_specification_deprecation)

Along with the Java language version, the [Java toolchain](https://docs.gradle.org/current/userguide/toolchains.html#toolchains) DSL allows configuring other criteria such as specific vendors or VM implementations. Starting with Gradle 7.6, toolchain specifications that configure other properties without specifying the language version are considered _invalid_. Invalid specifications are deprecated and will become build errors in Gradle 8.0.

See more details about toolchain configuration in the [user manual](https://docs.gradle.org/current/userguide/toolchains.html#sec:configuring_toolchain_specifications).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#org_gradle_util_reports_deprecations_7)[Deprecated members of the `org.gradle.util` package now report their deprecation](https://docs.gradle.org/userguide/upgrading_version_7.html#org_gradle_util_reports_deprecations_7)

These members will be removed in Gradle 9.0.0.

* `ClosureBackedAction`

* `CollectionUtils`

* `ConfigureUtil`

* `DistributionLocator`

* `GFileUtils`

* `GradleVersion.getBuildTime()`

* `GradleVersion.getNextMajor()`

* `GradleVersion.getRevision()`

* `GradleVersion.isValid()`

* `GUtil`

* `NameMatcher`

* `NameValidator`

* `RelativePathUtil`

* `TextUtil`

* `SingleMessageLogger`

* `VersionNumber`

* `WrapUtil`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#dependency_factory_renamed)[Internal DependencyFactory was renamed](https://docs.gradle.org/userguide/upgrading_version_7.html#dependency_factory_renamed)

The internal `org.gradle.api.internal.artifacts.dsl.dependencies.DependencyFactory` type was renamed to `org.gradle.api.internal.artifacts.dsl.dependencies.DependencyFactoryInternal`. As an internal type, it should not be used, but for compatibility reasons the inner `ClassPathNotation` type is still available. This name for the type is deprecated and will be removed in Gradle 8.0. The public API for this is on `DependencyHandler`, with methods such as `localGroovy()` providing the same functionality.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#replacement_collections_in_org_gradle_plugins_ide_idea_model_ideamodule)[Replacement collections in `org.gradle.plugins.ide.idea.model.IdeaModule`](https://docs.gradle.org/userguide/upgrading_version_7.html#replacement_collections_in_org_gradle_plugins_ide_idea_model_ideamodule)

The `testResourcesDirs` and `testSourcesDirs` fields and their getters and setters have been deprecated. Replace usages with the now stable `getTestSources()` and `getTestResources()` methods and their respective setters. These new methods return and are backed by `ConfigurableFileCollection` instances for improved flexibility of use. Gradle now warns upon usage of these deprecated methods. They will be removed in a future version of Gradle.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#replacement_methods_in_org_gradle_api_tasks_testing_testreport)[Replacement methods in `org.gradle.api.tasks.testing.TestReport`](https://docs.gradle.org/userguide/upgrading_version_7.html#replacement_methods_in_org_gradle_api_tasks_testing_testreport)

The `getDestinationDir()`, `setDestinationDir(File)`, and `getTestResultDirs()` and `setTestResultDirs(Iterable)` methods have been deprecated. Replace usages with the now stable `getDestinationDirectory()` and `getTestResults()` methods and their associated setters. These deprecated elements will be removed in a future version of Gradle.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#referencing_script_configure_method_from_container_configure_closure_deprecated)[Deprecated implicit references to outer scope methods in some configuration blocks](https://docs.gradle.org/userguide/upgrading_version_7.html#referencing_script_configure_method_from_container_configure_closure_deprecated)

Prior to Gradle 7.6, Groovy scripts permitted access to root project configure methods within named container configure methods that throw `MissingMethodException`s. Consider the following snippets for examples of this behavior:

Gradle permits access to the top-level `repositories` block from within the `configurations` block when the provided closure is otherwise an invalid configure closure for a Configuration. In this case, the `repositories` closure executes as if it were called at the script-level, and creates an unconfigured `repositories` Configuration:

```
configurations {
    repositories {
        mavenCentral()
    }
    someConf {
        canBeConsumed = false
        canBeResolved = false
    }
}
```

The behavior also applies to closures which do not immediately execute. In this case, `afterResolve` only executes when the `resolve` task runs. The `distributions` closure is a valid top-level script closure. But it is an invalid configure closure for a Configuration. This example creates the `conf` Configuration immediately. During `resolve` task execution, the `distributions` block executed as if it were declared at the script-level:

```
configurations {
    conf.incoming.afterResolve {
        distributions {
            myDist {
                contents {}
            }
        }
    }
}

task resolve {
    dependsOn configurations.conf
    doFirst {
        configurations.conf.files() // Trigger `afterResolve`
    }
}
```

As of Gradle 7.6, this behavior is deprecated. Starting with Gradle 8.0, this behavior will be removed. Instead, Gradle will throw the underlying `MissingMethodException`. To mitigate this change, consider the following solutions:

```
configurations {
    conf.incoming.afterResolve {
        // Fully qualify the reference.
        project.distributions {
            myDist {
                contents {}
            }
        }
    }
}
```

```
configurations {
    conf
}

// Extract the script-level closure to the script root scope.
configurations.conf.incoming.afterResolve {
    distributions {
        myDist {
            contents {}
        }
    }
}
```

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.5)[Upgrading from 7.4 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.5)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#incremental_task_inputs_deprecation)[IncrementalTaskInputs type is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#incremental_task_inputs_deprecation)

The `IncrementalTaskInputs` type was used to implement _incremental tasks,_ that is to say tasks that can be optimized to run on a subset of changed inputs instead of the whole input. This type had a number of drawbacks. In particular using this type it was not possible to determine what input a change was associated with.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_3)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_3)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#version_catalog_only_accepts_a_single_toml_import_file)[Version catalog only accepts a single TOML import file](https://docs.gradle.org/userguide/upgrading_version_7.html#version_catalog_only_accepts_a_single_toml_import_file)

Only a single file will be accepted when using a `from` import method. This means that notations, which resolve to multiple files (e.g. the [Project.files(java.lang.Object…​)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:files(java.lang.Object[])) method, when more then one file is passed) will result in a build failure.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#classpath_file_generated_by_the_eclipse_plugin_has_changed)[Classpath file generated by the `eclipse` plugin has changed](https://docs.gradle.org/userguide/upgrading_version_7.html#classpath_file_generated_by_the_eclipse_plugin_has_changed)

Project dependencies defined in test configurations get the `test=true` classpath attribute. All source sets and dependencies defined by the JVM Test Suite plugin are also marked as test code by default. You can now customize test source sets and dependencies via the `eclipse` plugin DSL:

```
eclipse {
    classpath {
        testSourceSets = [sourcesSets.test, sourceSets.myTestSourceSet]
        testConfigurations = [configuration.myTestConfiguration]
    }
}
```

Alternatively, you can adjust or remove classpath attributes in the `eclipse.classpath.file.whenMerged { }` block.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#signing_plugin_defaults_to_gpg_instead_of_gpg2_when_using_the_gpg_command)[Signing plugin defaults to `gpg` instead of `gpg2` when using the GPG command](https://docs.gradle.org/userguide/upgrading_version_7.html#signing_plugin_defaults_to_gpg_instead_of_gpg2_when_using_the_gpg_command)

The signature plugin’s default executable [when using the GPG command](https://docs.gradle.org/current/userguide/signing_plugin.html#sec:using_gpg_agent) changed from `gpg2` to `gpg`. The change was motivated as GPG 2.x became stable, and distributions started to migrate by not linking the `gpg2` executable.

In order to set the old default, the executable can be manually defined in `gradle.properties`:

`signing.gnupg.executable=gpg2`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#mustrunafter_constraints_no_longer_violated_by_finalizedby_dependencies)[`mustRunAfter` constraints no longer violated by `finalizedBy` dependencies](https://docs.gradle.org/userguide/upgrading_version_7.html#mustrunafter_constraints_no_longer_violated_by_finalizedby_dependencies)

In previous Gradle versions, `mustRunAfter` constraints between regular tasks and finalizer task dependencies would not be honored.

For a concrete example, consider the following task graph definition:

```
tasks {
    register("dockerTest") {
        dependsOn("dockerUp")     // dependsOn createContainer mustRunAfter removeContainer
        finalizedBy("dockerStop") // dependsOn removeContainer
    }

    register("dockerUp") {
        dependsOn("createContainer")
    }

    register("dockerStop") {
        dependsOn("removeContainer")
    }

    register("createContainer") {
        mustRunAfter("removeContainer")
    }

    register("removeContainer") {
    }
}
```

The relevant constraints are:

* `dockerStop` is a finalizer of `dockerTest` so it must be run after `dockerTest`;

* `removeContainer` is a dependency of `dockerStop` so it must be run before `dockerStop`;

* `createContainer` must run after `removeContainer`;

Prior to Gradle 7.5, `gradle dockerTest` would yield the following order of execution, in violation of the `mustRunAfter` constraint between `:createContainer` and `:removeContainer`:

```
> Task :createContainer UP-TO-DATE
> Task :dockerUp UP-TO-DATE
> Task :dockerTest UP-TO-DATE
> Task :removeContainer UP-TO-DATE
> Task :dockerStop UP-TO-DATE
```

Starting with Gradle 7.5, `mustRunAfter` constraints are fully honored yielding the following order of execution:

```
> Task :removeContainer UP-TO-DATE
> Task :createContainer UP-TO-DATE
> Task :dockerUp UP-TO-DATE
> Task :dockerTest UP-TO-DATE
> Task :dockerStop UP-TO-DATE
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#scala_zinc_version_updated_to_1_6_1)[Scala Zinc version updated to 1.6.1](https://docs.gradle.org/userguide/upgrading_version_7.html#scala_zinc_version_updated_to_1_6_1)

Zinc is the Scala incremental compiler that allows Gradle to always compile the minimal set of files needed by the current file changes. It takes into account which methods are being used and which have changed, which means it’s much more granular than just interfile dependencies.

Zinc version has been updated to the newest available one in order to benefit from all the recent bugfixes. Due to that, if you use `zincVersion` setting it’s advised to remove it and only use the default version, because Gradle will only be able to compile Scala code with Zinc versions set to 1.6.x or higher.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#remove_test_add_opens)[Removes implicit `--add-opens` for test workers](https://docs.gradle.org/userguide/upgrading_version_7.html#remove_test_add_opens)

Prior to Gradle 7.5, JDK modules `java.base/java.util` and `java.base/java.lang` were automatically opened in test workers on JDK9+ by passing `--add-opens` CLI arguments. This meant any tests were able to perform deep reflection on JDK internals without warning or failing. This caused tests to be unreliable by allowing code to pass when it would otherwise fail in a production environment.

These implicit arguments have been removed and are no longer added by default. If your code or any of your dependencies are performing deep reflection into JDK internals during test execution, you may see the following behavior changes:

Before Java 16, new build warnings are shown. These new warnings are printed to stderr and will not fail the build:

```
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by com.google.inject.internal.cglib.core.ReflectUtils$2 (file:/.../testng-5.12.1.jar) to <method>
WARNING: Please consider reporting this to the maintainers of com.google.inject.internal.cglib.core.ReflectUtils$2
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
```

With Java 16 or higher, exceptions are thrown that fail the build:

```
// Thrown by TestNG
java.lang.reflect.InaccessibleObjectException: Unable to make <method> accessible: module java.base does not "opens java.lang" to unnamed module @1e92bd61
 at java.base/java.lang.reflect.AccessibleObject.checkCanSetAccessible(AccessibleObject.java:354)
 at java.base/java.lang.reflect.AccessibleObject.checkCanSetAccessible(AccessibleObject.java:297)
 at java.base/java.lang.reflect.Method.checkCanSetAccessible(Method.java:199)
 at java.base/java.lang.reflect.Method.setAccessible(Method.java:193)
    ...

// Thrown by ProjectBuilder
org.gradle.api.GradleException: Could not inject synthetic classes.
 at org.gradle.initialization.DefaultLegacyTypesSupport.injectEmptyInterfacesIntoClassLoader(DefaultLegacyTypesSupport.java:91)
 at org.gradle.testfixtures.internal.ProjectBuilderImpl.getGlobalServices(ProjectBuilderImpl.java:182)
 at org.gradle.testfixtures.internal.ProjectBuilderImpl.createProject(ProjectBuilderImpl.java:111)
 at org.gradle.testfixtures.ProjectBuilder.build(ProjectBuilder.java:120)
 ...
Caused by: java.lang.RuntimeException: java.lang.IllegalAccessException: module java.base does not open java.lang to unnamed module @1e92bd61
```

In most cases, these errors can be resolved by updating the code or dependency performing the illegal access. If the code-under-test or the newest version of the dependency in question performs illegal access by design, the old behavior can be restored by opening the `java.base/java.lang` and `java.base/java.util` modules manually with `--add-opens`:

```
tasks.withType(Test).configureEach {
    jvmArgs(["--add-opens=java.base/java.lang=ALL-UNNAMED",
             "--add-opens=java.base/java.util=ALL-UNNAMED"]
}
```

If you are developing Gradle plugins, `ProjectBuilder` relies on reflection in the `java.base/java.lang` module. Gradle will automatically add the appropriate `--add-opens` flag to tests when the `java-gradle-plugin` plugin is applied.

If you are using TestNG, versions prior to `5.14.6` perform illegal reflection. Updating to at least `5.14.6` should fix the incompatibility.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#checkstyle_worker_api)[Checkstyle tasks use toolchains and execute in parallel by default](https://docs.gradle.org/userguide/upgrading_version_7.html#checkstyle_worker_api)

The [Checkstyle plugin](https://docs.gradle.org/current/userguide/checkstyle_plugin.html#checkstyle_plugin) now uses the Gradle worker API to run Checkstyle as an external worker process. Multiple Checkstyle tasks may now run in parallel within a project.

Some projects will need to increase the amount of memory available to Checkstyle to avoid out of memory errors. You can [increase the maximum memory for the Checkstyle process](https://docs.gradle.org/current/userguide/checkstyle_plugin.html#sec:checkstyle_customize_memory) by setting the `maxHeapSize` for the Checkstyle task. By default, the process will start with a maximum heap size of 512MB.

We also recommend to update Checkstyle to version 9.3 or later.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#missing_files_specified_with_relative_paths_when_running_checkstyle)[Missing files specified with relative paths when running Checkstyle](https://docs.gradle.org/userguide/upgrading_version_7.html#missing_files_specified_with_relative_paths_when_running_checkstyle)

Gradle 7.5 consistently sets the current working directory for the Checkstyle task to `$GRADLE_USER_HOME/workers`. This may cause problems with custom Checkstyle tasks or Checkstyle configuration files that assume a different directory for relative paths.

Previously, Gradle selected the current working directory based on the directory where you ran Gradle. If you ran Gradle in:

* the root directory of a project: Gradle uses the root directory as the current working directory.

* a nested directory of a project: Gradle uses the root directory of the subproject as the current working directory.

In version 7.5 and above, Gradle consistently sets the current working directory for the Checkstyle task to `$GRADLE_USER_HOME/workers`.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_2)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_2)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#file_collection_to_classpath)[Converting files to a classpath where paths contain file separator](https://docs.gradle.org/userguide/upgrading_version_7.html#file_collection_to_classpath)

Java has the concept of a path separator which is used to separate individual paths in a list of paths, for example in a classpath string. The individual paths must not contain the path separator. Consequently, using `@FileCollection.getAsPath()` for files with paths that contain a path separator has been deprecated, and it will be an error in Gradle 8.0 and later. Using a file collection with paths which contain a path separator may lead to incorrect builds, since Gradle doesn’t find the files as inputs, or even to build failures when the path containing the path separator is illegal on the operating system.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencyinsight_singlepath)[`dependencyInsight``--singlepath` option is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#dependencyinsight_singlepath)

For consistency, this was changed to `--single-path`. The API method has remained the same, this only affects the CLI.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#groovydoc_option_improvements)[Groovydoc `includePrivate` property is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#groovydoc_option_improvements)

There is a new `access` property that allows finer control over what is included in the Groovydoc.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#use_providers_to_run_external_processes)[Provider-based API must be used to run external processes at the configuration time](https://docs.gradle.org/userguide/upgrading_version_7.html#use_providers_to_run_external_processes)

Using `Project.exec`, `Project.javaexec`, and standard Java and Groovy APIs to run external processes at the configuration time is now deprecated when the configuration cache is enabled. It will be an error in Gradle 8.0 and later. Gradle 7.5 introduces configuration cache-compatible ways to execute and obtain output of an external process with the [provider-based APIs](https://docs.gradle.org/current/dsl/org.gradle.api.provider.ProviderFactory.html) or a custom implementation of the [`ValueSource`](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ValueSource.html) interface. The [configuration cache chapter](https://docs.gradle.org/current/userguide/configuration_cache_requirements.html#config_cache:requirements:external_processes) has more details to help with the migration to the new APIs.

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.4)[Upgrading from 7.3 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.4)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_3)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_3)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#adoptopenjdk_download)[AdoptOpenJDK toolchain download](https://docs.gradle.org/userguide/upgrading_version_7.html#adoptopenjdk_download)

Following the move from AdoptOpenJDK to Adoptium, under the Eclipse foundation, it is no longer possible to download an AdoptOpenJDK build from their end point. Instead, an Eclipse Temurin or IBM Semeru build is returned.

Gradle 7.4+ will now emit a deprecation warning when the AdoptOpenJDK vendor is specified in the [toolchain specification](https://docs.gradle.org/current/userguide/toolchains.html#sec:vendors) and it is used by auto provisioning. If you must use AdoptOpenJDK, you should turn off auto-download. If an Eclipse Temurin or IBM Semeru build works for you, specify `JvmVendorSpec.ADOPTIUM` or `JvmVendorSpec.IBM` as the vendor or leave the vendor unspecified.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#empty_directories_file_tree)[File trees and empty directory handling](https://docs.gradle.org/userguide/upgrading_version_7.html#empty_directories_file_tree)

When using `@SkipWhenEmpty` on an input file collection, Gradle skips the task when it determines that the input is empty. If the input file collection consists only of file trees, Gradle ignores directories for the emptiness check. Though when checking for changes to the input file collection, Gradle only ignores directories when the `@IgnoreEmptyDirectories` annotation is present.

Gradle will now ignore directories for both the `@SkipWhenEmpty` check and for determining changes consistently. Until Gradle 8.0, Gradle will detect if an input file collection annotated with `@SkipWhenEmpty` consists only of file trees and then ignore directories automatically. Moreover, Gradle will issue a deprecation warning to advise the user that the behavior will change in Gradle 8.0, and that the input property should be annotated with `@IgnoreEmptyDirectories`. To ignore directories in Gradle 8.0 and later, the input property needs to be annotated with `@IgnoreEmptyDirectories`.

Finally, using `@InputDirectory` implies `@IgnoreEmptyDirectories`, so no changes are necessary when using this annotation. The same is true for `inputs.dir()` when registering an input directory via the runtime API.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#lazypublishartifact_fileresolver)[Using LazyPublishArtifact without a FileResolver is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#lazypublishartifact_fileresolver)

When using a LazyPublishArtifact without a FileResolver, a different file resolution strategy is used, which duplicates some logic in the FileResolver.

To improve consistency, LazyPublishArtifact should be used with a FileResolver, and will require it in the future.

This also affects other internal APIs that use LazyPublishArtifact, which now also have deprecation warnings where needed.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#tar_tree_no_backing_file)[TAR trees from resources without backing files](https://docs.gradle.org/userguide/upgrading_version_7.html#tar_tree_no_backing_file)

It is possible to create TAR trees from arbitrary resources. If the resource is not created via `project.resources`, then it may not have a backing file. Creating a TAR tree from a resource with no backing file has been deprecated. Instead, convert the resource to a file and use `project.tarTree()` on the file. To convert the resource to a file you can use a custom task or use dependency management to download the file via a URL. This way, Gradle is able to apply optimizations like up-to-date checks instead of re-running the logic to create the resource every time.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#unique_attribute_sets)[Unique attribute sets](https://docs.gradle.org/userguide/upgrading_version_7.html#unique_attribute_sets)

The set of [Attribute](https://docs.gradle.org/current/javadoc/org/gradle/api/attributes/Attribute.html)s associated with a _consumable_ configuration within a project, must be unique across all other configurations within that project which share the same set of [Capability](https://docs.gradle.org/current/javadoc/org/gradle/api/capabilities/Capability.html)s.

This will be checked at the end of configuring variant configurations, as they are locked against further mutation.

If the set of attributes is shared across configurations, consider adding an additional attribute to one of the variants for the sole purpose of disambiguation.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#for_use_at_configuration_time_deprecation)[`Provider#forUseAtConfigurationTime()` has been deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#for_use_at_configuration_time_deprecation)

Starting with version 7.4 Gradle will implicitly treat an external value used at configuration time as a configuration cache input.

Clients are also free to use standard Java APIs such as `System#getenv` to read environment variables, `System#getProperty` to read system properties as well as Gradle APIs such as [`Project#property(String)`](https://docs.gradle.org/current/dsl/org.gradle.api.provider.ProviderFactory.html#org.gradle.api.provider.ProviderFactory:systemProperty(java.lang.String)) and [`Project#findProperty(String)`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#findProperty-java.lang.String-) to read Gradle properties at configuration time. The `Provider` based APIs are still the recommended way to connect external values to task inputs for maximum configuration cache reuse.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#task_project)[Calling `Task.getProject()` from a task action](https://docs.gradle.org/userguide/upgrading_version_7.html#task_project)

Calling [Task.getProject()](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#getProject--) from a task action at execution time is now deprecated and will be made an error in Gradle 8.0. This method can be used during configuration time, but it is recommended to avoid doing this.

See the [configuration cache chapter](https://docs.gradle.org/current/userguide/configuration_cache_requirements.html#config_cache:requirements:use_project_during_execution) for details on how to migrate these usages to APIs that are supported by the configuration cache.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#task_dependencies)[Calling `Task.getTaskDependencies()` from a task action](https://docs.gradle.org/userguide/upgrading_version_7.html#task_dependencies)

Calling [Task.getTaskDependencies()](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html#getTaskDependencies--) from a task action at execution time is now deprecated and will be made an error in Gradle 8.0. This method can be used during configuration time, but it is recommended to avoid doing this.

See the [configuration cache chapter](https://docs.gradle.org/current/userguide/configuration_cache_requirements.html#config_cache:requirements:use_project_during_execution) for details on how to migrate these usages to APIs that are supported by the configuration cache.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#undeclared_build_service_usage)[Using a build service from a task without explicitly declaring usage](https://docs.gradle.org/userguide/upgrading_version_7.html#undeclared_build_service_usage)

Gradle needs the information so it can properly honor the build service lifecycle and its usage constraints.

This will become an error in a future Gradle version.

This can be done either by consuming the service via a `@ServiceReference` property (since 8.0) or by invoking `usesService()` on the task (since 6.1).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#version_catalog_deprecations)[VersionCatalog and VersionCatalogBuilder deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#version_catalog_deprecations)

Some methods in [VersionCatalog](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/VersionCatalog.html) and [VersionCatalogBuilder](https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/dsl/VersionCatalogBuilder.html) are now deprecated and scheduled for removal in Gradle 8.0. Specific replacements can be found in the JavaDoc of the affected methods.

These methods were changed to improve the consistency between the `libs.versions.toml` file and the API classes.

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.3)[Upgrading from 7.2 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.3)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_5)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_5)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#application_order_of_plugins_in_the_plugins_block)[Application order of plugins in the `plugins` block](https://docs.gradle.org/userguide/upgrading_version_7.html#application_order_of_plugins_in_the_plugins_block)

The order in which plugins in the `plugins` block were actually applied was inconsistent and depended on how a plugin was added to the class path.

Now the plugins are always applied in the same order they are declared in the `plugins` block which in rare cases might change behavior of existing builds.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#effects_of_exclusion_on_substituted_dependencies_in_dependency_resolution)[Effects of exclusion on substituted dependencies in dependency resolution](https://docs.gradle.org/userguide/upgrading_version_7.html#effects_of_exclusion_on_substituted_dependencies_in_dependency_resolution)

Prior to this version, a dependency substitution target could not be excluded from a dependency graph. This was caused by checking for exclusions prior to performing the substitution. Now Gradle will also check for exclusion on the substitution result.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#toolchain_support_in_scala)[Toolchain support in Scala](https://docs.gradle.org/userguide/upgrading_version_7.html#toolchain_support_in_scala)

When using [toolchains in Scala](https://docs.gradle.org/current/userguide/scala_plugin.html#sec:scala_tasks), the `-target` option of the Scala compiler will now be set automatically. This means that using a version of Java that cannot be targeted by a version of Scala will result in an error. Providing this flag in the compiler options will disable this behaviour and allow to use a higher Java version to compile for a lower bytecode target.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#declare_unreadable_input_output)[Declaring input or output directories which contain unreadable content](https://docs.gradle.org/userguide/upgrading_version_7.html#declare_unreadable_input_output)

For up-to-date checks Gradle relies on tracking the state of the inputs and the outputs of a task. Gradle used to ignore unreadable files in the input or outputs to support certain use-cases, although it cannot track their state. Declaring input or output directories on tasks which contain unreadable content has been deprecated and these use-cases are now supported by declaring the task to be untracked. Use the @[UntrackedTask](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/UntrackedTask.html) annotation or the [Task.doNotTrackState()](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:doNotTrackState(java.lang.String)) method to declare a task as untracked.

When you are using a `Copy` task for copying single files into a directory which contains unreadable files, use the method [Task.doNotTrackState()](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:doNotTrackState(java.lang.String)).

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.2)[Upgrading from 7.1 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.2)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_6)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_6)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#security_changes_to_application_start_scripts_and_gradle_wrapper_scripts)[Security changes to application start scripts and Gradle wrapper scripts](https://docs.gradle.org/userguide/upgrading_version_7.html#security_changes_to_application_start_scripts_and_gradle_wrapper_scripts)

Due to [CVE-2021-32751](https://github.com/gradle/gradle/security/advisories/GHSA-6j2p-252f-7mw8), `gradle`, `gradlew` and start scripts generated by Gradle’s [application plugin](https://docs.gradle.org/current/userguide/application_plugin.html#application_plugin) have been updated to avoid situations where these scripts could be used for arbitrary code execution when an attacker is able to change environment variables.

You can use the latest version of Gradle to generate a `gradlew` script and use it to execute an older version of Gradle.

This should be transparent for most users; however, there may be changes for Gradle builds that rely on the environment variables `JAVA_OPTS` or `GRADLE_OPTS` to pass parameters with complicated quote escaping. Contact us if you suspect something has broken your build and you cannot find a solution.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_4)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_4)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#java_lamdba_action)[Using Java lambdas as task actions](https://docs.gradle.org/userguide/upgrading_version_7.html#java_lamdba_action)

When using a Java lambda to implement a task action, Gradle cannot track the implementation and the task will never be up-to-date or served from the build cache. Since it is easy to add such a task action, using task actions implemented by Java lambdas is now deprecated. See [Validation problems](https://docs.gradle.org/current/userguide/validation_problems.html#implementation_unknown) for more details how to fix the issue.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#equals_up_to_date_deprecation)[Relying on equals for up-to-date checks is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#equals_up_to_date_deprecation)

When a task input is annotated with `@Input` and is not a type Gradle understand directly (like `String`), then Gradle uses the serialized form of the input for up-to-date checks and the build cache key. Historically, Gradle also loads the serialized value from the last execution and then uses `equals()` to compare it to the current value for up-to-date checks. Doing so is error prone, doesn’t work with the build cache and has a performance impact, therefore it has been deprecated. Instead of using `@Input` on a type Gradle doesn’t understand directly, use `@Nested` and annotate the properties of the type accordingly.

[](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.1)[Upgrading from 7.0 and earlier](https://docs.gradle.org/userguide/upgrading_version_7.html#changes_7.1)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_7)[Potential breaking changes](https://docs.gradle.org/userguide/upgrading_version_7.html#potential_breaking_changes_7)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#the_org_gradle_util_package_is_now_a_public_api)[The `org.gradle.util` package is now a public API](https://docs.gradle.org/userguide/upgrading_version_7.html#the_org_gradle_util_package_is_now_a_public_api)

Officially, the `org.gradle.util` package is not part of the public API. But, because this package name doesn’t contain the word `internal`, many Gradle plugins already consider as one. Gradle 7.1 addresses the situation and marks the package as public. The classes that were unintentionally exposed are either deprecated or removed, depending on their external usage.

##### [](https://docs.gradle.org/userguide/upgrading_version_7.html#the_following_classes_have_known_usages_in_external_plugins_and_are_now_deprecated_and_set_for_removal_in_gradle_8_0)[The following classes have known usages in external plugins and are now deprecated and set for removal in Gradle 8.0:](https://docs.gradle.org/userguide/upgrading_version_7.html#the_following_classes_have_known_usages_in_external_plugins_and_are_now_deprecated_and_set_for_removal_in_gradle_8_0)

* `VersionNumber`

* `TextUtil`

* `WrapUtil`

* `RelativePathUtil`

* `DistributionLocator`

* `SingleMessageLogger`

* `ConfigureUtil`

`ConfigureUtil` is being removed without a replacement. Plugins can avoid the need for using `ConfigureUtil`.

##### [](https://docs.gradle.org/userguide/upgrading_version_7.html#the_following_classes_have_only_internal_usages_and_were_moved_from_org_gradle_util_to_the_org_gradle_util_internal_package)[The following classes have only internal usages and were moved from `org.gradle.util` to the `org.gradle.util.internal` package:](https://docs.gradle.org/userguide/upgrading_version_7.html#the_following_classes_have_only_internal_usages_and_were_moved_from_org_gradle_util_to_the_org_gradle_util_internal_package)

* `Resources`

* `RedirectStdOutAndErr`

* `Swapper`

* `StdInSwapper`

* `IncubationLogger`

* `RedirectStdIn`

* `MultithreadedTestRule`

* `DisconnectableInputStream`

* `BulkReadInputStream`

* `MockExecutor`

* `FailsWithMessage`

* `FailsWithMessageExtension`

* `TreeVisitor`

* `AntUtil`

* `JarUtil`

##### [](https://docs.gradle.org/userguide/upgrading_version_7.html#the_last_set_of_classes_have_no_external_or_internal_usages_and_therefore_were_deleted)[The last set of classes have no external or internal usages and therefore were deleted:](https://docs.gradle.org/userguide/upgrading_version_7.html#the_last_set_of_classes_have_no_external_or_internal_usages_and_therefore_were_deleted)

* `DiffUtil`

* `NoopChangeListener`

* `EnumWithClassBody`

* `AlwaysTrue`

* `ReflectionEqualsMatcher`

* `DynamicDelegate`

* `IncubationLogger`

* `NoOpChangeListener`

* `DeferredUtil`

* `ChangeListener`

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#the_return_type_of_source_set_extensions_have_changed)[The return type of source set extensions have changed](https://docs.gradle.org/userguide/upgrading_version_7.html#the_return_type_of_source_set_extensions_have_changed)

The following source sets are contributed via an extension with a custom type:

* `groovy`: [GroovySourceDirectorySet](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.GroovySourceDirectorySet.html)

* `antlr`: [AntlrSourceDirectorySet](https://docs.gradle.org/current/dsl/org.gradle.api.plugins.antlr.AntlrSourceDirectorySet.html)

* `scala`: [ScalaSourceDirectorySet](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.ScalaSourceDirectorySet.html)

The 'idiomatic' DSL declaration is backward compatible:

```
sourceSets {
    main {
        groovy {
            // ...
        }
    }
}
```

However, the return type of the groovy block has changed to the extension type. This means that the following snippet no longer works in Gradle 7.1:

```
sourceSets {
     main {
         GroovySourceSet sourceSet = groovy {
             // ...
         }
     }
 }
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#start_scripts_require_bash_shell)[Start scripts require bash shell](https://docs.gradle.org/userguide/upgrading_version_7.html#start_scripts_require_bash_shell)

The command used to start Gradle, the Gradle wrapper as well as the scripts generated by the `application` plugin now require `bash` shell.

### [](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_5)[Deprecations](https://docs.gradle.org/userguide/upgrading_version_7.html#deprecations_5)

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#convention_mapping)[Using convention mapping with properties with type Provider is deprecated](https://docs.gradle.org/userguide/upgrading_version_7.html#convention_mapping)

Convention mapping is an internal feature that is been replaced by the [Provider API](https://docs.gradle.org/current/userguide/lazy_configuration.html#lazy_configuration). When mixing convention mapping with the Provider API, unexpected behavior can occur. Gradle emits a deprecation warning when a property in a task, extension or other domain object uses convention mapping with the Provider API.

To fix this, the plugin that configures the convention mapping for the task, extension or domain object needs to be changed to use the Provider API only.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#configuring_custom_build_layout_7)[Setting custom build layout](https://docs.gradle.org/userguide/upgrading_version_7.html#configuring_custom_build_layout_7)

Command line options:

* `-c`, `--settings-file` for specifying a custom settings file location

* `-b`, `--build-file` for specifying a custom build file location

have been deprecated.

Setting custom build file using [buildFile](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.GradleBuild.html#org.gradle.api.tasks.GradleBuild:buildFile) property in [GradleBuild](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.GradleBuild.html) task has been deprecated.

Please use the [dir](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.GradleBuild.html#org.gradle.api.tasks.GradleBuild:dir) property instead to specify the root of the nested build.

Please use standard locations for settings and build files:

* settings file in the root of the build

* build file in the root of each subproject

For the use case where custom settings or build files are used to model different behavior (similar to Maven profiles), consider using [system properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_system_properties) with conditional logic. For example, given a piece of code in either settings or build file:

```
if (System.getProperty("profile") == "custom") {
    println("custom profile")
} else {
    println("default profile")
}
```

You can pass the `profile` system property to Gradle using `gradle -Dprofile=custom` to execute the code in the `custom` profile branch.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#dependency_substitutions_with)[Substitution.with replaced with Substitution.using](https://docs.gradle.org/userguide/upgrading_version_7.html#dependency_substitutions_with)

[Dependency substitutions](https://docs.gradle.org/current/userguide/resolution_rules.html#sec:dependency-substitution-rules) using `with` method have been deprecated and are replaced with `using` method that also allows chaining. For example, a dependency substitution rule `substitute(project(':a')).with(project(':b'))` should be replaced with `substitute(project(':a')).using(project(':b'))`. With chaining you can, for example, add a reason for a substitution like this: `substitute(project(':a')).using(project(':b')).because("a reason")`.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#compile_task_wiring)[Deprecated properties in `compile` task](https://docs.gradle.org/userguide/upgrading_version_7.html#compile_task_wiring)

* The [JavaCompile.destinationDir](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.JavaCompile.html#org.gradle.api.tasks.compile.JavaCompile:destinationDir) property has been deprecated. Use the [JavaCompile.destinationDirectory](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.JavaCompile.html#org.gradle.api.tasks.compile.JavaCompile:destinationDirectory) property instead.

* The [GroovyCompile.destinationDir](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.GroovyCompile.html#org.gradle.api.tasks.compile.GroovyCompile:destinationDir) property has been deprecated. Use the [GroovyCompile.destinationDirectory](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.GroovyCompile.html#org.gradle.api.tasks.compile.GroovyCompile:destinationDirectory) property instead.

* The [ScalaCompile.destinationDir](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.scala.ScalaCompile.html#org.gradle.api.tasks.scala.ScalaCompile:destinationDir) property has been deprecated. Use the [ScalaCompile.destinationDirectory](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.scala.ScalaCompile.html#org.gradle.api.tasks.scala.ScalaCompile:destinationDirectory) property instead.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#non_hierarchical_project_structures)[Non-hierarchical project layouts](https://docs.gradle.org/userguide/upgrading_version_7.html#non_hierarchical_project_structures)

Gradle 7.1 deprecated project layouts where subprojects were located outside of the project root. However, based on [community feedback](https://github.com/gradle/gradle/issues/18644) we decided to roll back in Gradle 7.4 and removed the deprecation. As a consequence, the [Settings.includeFlat()](https://docs.gradle.org/current/dsl/org.gradle.api.initialization.Settings.html#org.gradle.api.initialization.Settings:includeFlat(java.lang.String[])) method is deprecated in Gradle 7.1, 7.2, and 7.3 only.

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#upload_task_deprecation)[Deprecated `Upload` task](https://docs.gradle.org/userguide/upgrading_version_7.html#upload_task_deprecation)

Gradle used to have two ways of publishing artifacts. Now, the situation has been cleared and all build should use the `maven-publish` plugin. The last remaining artifact of the old way of publishing is the `Upload` task that has been deprecated and scheduled for removal in Gradle 8.0. Existing clients should migrate to the [`maven-publish` plugin](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#all_convention_deprecation)[Deprecated conventions](https://docs.gradle.org/userguide/upgrading_version_7.html#all_convention_deprecation)

The concept of conventions is outdated and superseded by extensions. To reflect this in the Gradle API, the following elements are now deprecated:

* [org.gradle.api.Project.getConvention()](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#getConvention--)

* `org.gradle.api.internal.HasConvention` (deprecated)

The internal usages of conventions have been also cleaned up (see the deprecated items below).

Plugin authors migrate to extensions if they replicate the changes we’ve done internally. Here are some examples:

* Migrate plugin configuration: [gradle/gradle#16900](https://github.com/gradle/gradle/pull/16900/files#diff-ac53d4f39698b83e30b93855fe6a725ffd96d5ed9df156d4f9dfd32bdc7946e7).

* Migrate custom source sets: [gradle/gradle#17149](https://github.com/gradle/gradle/pull/17149/files#diff-e159587e2f9aec398fa795b1d8b344f1593cb631e15e04893d31cdc9465f9781).

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#plugin_configuration_consumption)[Deprecated consumption of internal plugin configurations](https://docs.gradle.org/userguide/upgrading_version_7.html#plugin_configuration_consumption)

Some core Gradle plugins declare configurations that are used by the plugin itself and are not meant to be published or consumed by another subproject directly. Gradle did not explicitly prohibit this. Gradle 7.1 deprecates consumption of those configurations and this will become an error in Gradle 8.0.

The following plugin configurations have been deprecated for consumption:

| plugin | configurations deprecated for consumption |
| --- | --- |
| `codenarc` | `codenarc` |
| `pmd` | `pmd` |
| `checkstyle` | `checkstyle` |
| `antlr` | `antlr` |
| `jacoco` | `jacocoAnt`, `jacocoAgent` |
| `scala` | `zinc` |
| `war` | `providedCompile`, `providedRuntime` |

If your use case needs to consume any of the above mentioned configurations in another project, please create a separate consumable configuration that extends from the internal ones. For example:

```
plugins {
    id("codenarc")
}
configurations {
    codenarc {
        // because currently this is consumable until Gradle 8.0 and can clash with the configuration below depending on the attributes set
        canBeConsumed = false
    }
    codenarcConsumable {
        extendsFrom(codenarc)
        canBeConsumed = true
        canBeResolved = false
        // the attributes below make this configuration consumable by a `java-library` project using `implementation` configuration
        attributes {
            attribute(Usage.USAGE_ATTRIBUTE, objects.named(Usage, Usage.JAVA_RUNTIME))
            attribute(Category.CATEGORY_ATTRIBUTE, objects.named(Category, Category.LIBRARY))
            attribute(LibraryElements.LIBRARY_ELEMENTS_ATTRIBUTE, objects.named(LibraryElements, LibraryElements.JAR))
            attribute(Bundling.BUNDLING_ATTRIBUTE, objects.named(Bundling, Bundling.EXTERNAL))
            attribute(TargetJvmEnvironment.TARGET_JVM_ENVIRONMENT_ATTRIBUTE, objects.named(TargetJvmEnvironment, TargetJvmEnvironment.STANDARD_JVM));
        }
    }
}
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#custom_source_set_deprecation)[Deprecated custom source set interfaces](https://docs.gradle.org/userguide/upgrading_version_7.html#custom_source_set_deprecation)

The following source set interfaces are now deprecated and scheduled for removal in Gradle 8.0:

* `org.gradle.api.tasks.GroovySourceSet`

* `org.gradle.api.plugins.antlr.AntlrSourceVirtualDirectory` (removed)

* `org.gradle.api.tasks.ScalaSourceSet`

Clients should configure the sources with their plugin-specific configuration:

* `groovy`: [GroovySourceDirectorySet](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/GroovySourceDirectorySet.html)

* `antlr`: [AntlrSourceDirectorySet](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/antlr/AntlrSourceDirectorySet.html)

* `scala`: [ScalaSourceDirectorySet](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/ScalaSourceDirectorySet.html)

For example, here’s how you configure the groovy sources from a plugin:

```
GroovySourceDirectorySet groovySources = sourceSet.getExtensions().getByType(GroovySourceDirectorySet.class);
groovySources.setSrcDirs(Arrays.asList("sources/groovy"));
```

#### [](https://docs.gradle.org/userguide/upgrading_version_7.html#old_artifact_transforms_api)[Registering artifact transforms extending `ArtifactTransform`](https://docs.gradle.org/userguide/upgrading_version_7.html#old_artifact_transforms_api)

When Gradle first introduced artifact transforms, it used the base class `ArtifactTransform` for implementing them. Gradle 5.3 introduced the interface `TransformAction` for implementing artifact transforms, replacing the previous class `ArtifactTransform` and addressing various shortcomings. Using the registration method [DependencyHandler.registerTransform(Action)](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html#org.gradle.api.artifacts.dsl.DependencyHandler:registerTransform(org.gradle.api.Action)) for `ArtifactTransform` has been deprecated. Migrate your artifact transform to use `TransformAction` and use [DependencyHandler.registerTransform(Class, Action)](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html#org.gradle.api.artifacts.dsl.DependencyHandler:registerTransform(java.lang.Class,%20org.gradle.api.Action)) instead. See the [user manual](https://docs.gradle.org/current/userguide/artifact_transforms.html#sec:abm-artifact-transforms) for more information on implementing `TransformAction`.
