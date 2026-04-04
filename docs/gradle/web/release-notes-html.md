# Source: https://docs.gradle.org/release-notes.html

Title: Gradle 9.4.0 Release Notes

URL Source: https://docs.gradle.org/release-notes.html

Markdown Content:
We are excited to announce Gradle 9.4.0 (released [2026-03-04](https://gradle.org/releases/)).

Gradle now supports [Java 26](https://docs.gradle.org/release-notes.html#support-for-java-26).

This release significantly improves [test reporting and execution](https://docs.gradle.org/release-notes.html#test-reporting-and-execution) by introducing support for non-class-based tests, enabling direct execution of Cucumber features and custom test engines, and capturing richer test metadata directly into HTML reports.

There are notable [command-line interface and problem reporting](https://docs.gradle.org/release-notes.html#cli-logging-and-problem-reporting) refinements, including high-resolution progress bars with native terminal integration, a more intuitive Problems HTML report, and expanded output formats for the PMD plugin.

This version also enhances [build authoring](https://docs.gradle.org/release-notes.html#build-authoring) with simplified APIs, improves [Configuration Cache](https://docs.gradle.org/release-notes.html#configuration-cache) debugging with clearer attribution for closures and lambdas, and adds [security improvements](https://docs.gradle.org/release-notes.html#security-and-infrastructure), including Bearer token authentication for the Gradle Wrapper and automatic cleanup of daemon logs. We've refined [plugin authoring](https://docs.gradle.org/release-notes.html#core-plugin-and-plugin-authoring) by adding default plugin IDs and stricter validation for published plugins.

Finally, [tooling integration](https://docs.gradle.org/release-notes.html#tooling-and-ide-integration) improvements provide new Tooling API models plus granular control over Tooling API parallelism.

We would like to thank the following community members for their contributions to this release of Gradle: [akankshaa-00](https://github.com/akankshaa-00), [Attila Kelemen](https://github.com/kelemen), [Björn Kautler](https://github.com/Vampire), [dblood](https://github.com/dblood), [Dennis Rieks](https://github.com/drieks), [duvvuvenkataramana](https://github.com/duvvuvenkataramana), [John Burns](https://github.com/wakingrufus), [Julian](https://github.com/Julianw03), [kevinstembridge](https://github.com/kevinstembridge), [Niels Doucet](https://github.com/NielsDoucet), [Philip Wedemann](https://github.com/hfhbd), [ploober](https://github.com/ploober), [Richard Hernandez](https://github.com/rhernandez35), [Roberto Perez Alcolea](https://github.com/rpalcolea), [Sebastian Lövdahl](https://github.com/slovdahl), [stephan2405](https://github.com/stephan2405), [Stephane Landelle](https://github.com/slandelle), [Ujwal Suresh Vanjare](https://github.com/usv240), [Victor Merkulov](https://github.com/urdak), [Vincent Potuček](https://github.com/Pankraz76), [Vladimir Sitnikov](https://github.com/vlsi).

Be sure to check out the [public roadmap](https://roadmap.gradle.org/) for insight into what's planned for future releases.

Table Of Contents
-----------------

* [Upgrade instructions](https://docs.gradle.org/release-notes.html#upgrade-instructions)
* [New features and usability improvements](https://docs.gradle.org/release-notes.html#new-features-and-usability-improvements)
* [Support for Java 26](https://docs.gradle.org/release-notes.html#support-for-java-26)
* [Test reporting and execution](https://docs.gradle.org/release-notes.html#test-reporting-and-execution)
* [CLI, logging, and problem reporting](https://docs.gradle.org/release-notes.html#cli-logging-and-problem-reporting)
* [Security and infrastructure](https://docs.gradle.org/release-notes.html#security-and-infrastructure)
* [Build authoring](https://docs.gradle.org/release-notes.html#build-authoring)
* [Configuration Cache](https://docs.gradle.org/release-notes.html#configuration-cache)
* [Core plugin and plugin authoring](https://docs.gradle.org/release-notes.html#core-plugin-and-plugin-authoring)
* [Tooling and IDE integration](https://docs.gradle.org/release-notes.html#tooling-and-ide-integration)
* [Promoted features](https://docs.gradle.org/release-notes.html#promoted-features)
* [Task graph is now stable](https://docs.gradle.org/release-notes.html#task-graph-is-now-stable)
* [Documentation and training](https://docs.gradle.org/release-notes.html#documentation-and-training)
* [Documentation](https://docs.gradle.org/release-notes.html#documentation)
* [Training](https://docs.gradle.org/release-notes.html#training)
* [Fixed issues](https://docs.gradle.org/release-notes.html#fixed-issues)
* [Known issues](https://docs.gradle.org/release-notes.html#known-issues)
* [External contributions](https://docs.gradle.org/release-notes.html#external-contributions)
* [Reporting problems](https://docs.gradle.org/release-notes.html#reporting-problems)

[Upgrade instructions](https://docs.gradle.org/release-notes.html#upgrade-instructions)
---------------------------------------------------------------------------------------

Switch your build to use Gradle 9.4.0 by updating the [wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html) in your project:

```
./gradlew wrapper --gradle-version=9.4.0 && ./gradlew wrapper
```

See the [Gradle 9.x upgrade guide](https://docs.gradle.org/current/userguide/upgrading_version_9.html#changes_9.4.0) to learn about deprecations, breaking changes, and other considerations when upgrading to Gradle 9.4.0.

For Java, Groovy, Kotlin, and Android compatibility, see the [full compatibility notes](https://docs.gradle.org/current/userguide/compatibility.html).

[New features and usability improvements](https://docs.gradle.org/release-notes.html#new-features-and-usability-improvements)
-----------------------------------------------------------------------------------------------------------------------------

### [Support for Java 26](https://docs.gradle.org/release-notes.html#support-for-java-26)

With this release, Gradle supports [Java 26](https://openjdk.org/projects/jdk/26/). This means you can now use Java 26 for the [daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html) in addition to [toolchains](https://docs.gradle.org/current/userguide/toolchains.html). Third-party tool compatibility with Java 26 may still be limited.

See the [compatibility documentation](https://docs.gradle.org/current/userguide/compatibility.html#java_runtime) for more details.

### [Test reporting and execution](https://docs.gradle.org/release-notes.html#test-reporting-and-execution)

Gradle provides a [set of features and abstractions](https://docs.gradle.org/current/userguide/java_testing.html) for testing JVM code, along with test reports to display results.

#### [Non-class-based testing](https://docs.gradle.org/release-notes.html#non-class-based-testing)

When testing using [JUnit Platform](https://junit.org/), Gradle can now discover and execute tests that are not defined in classes.

JUnit Platform [`TestEngine`s](https://docs.junit.org/current/advanced-topics/engines.html) can discover and execute tests in arbitrary formats, extending testing beyond the confines of JVM classes. In this release, tests can be defined in any format supported by the configured `TestEngine`. Gradle no longer requires a test class to be present to “unlock” test execution.

For example, this library project structure doesn't use typical class-based testing, but instead uses XML test definitions understood by a custom `TestEngine`:

```
my-lib/
├── src/
│   ├── main/
│   │   └── java/
│   └── test/
│       └── definitions/
│           ├── some-tests.xml
│           ├── some-other-tests.xml
│           └── sub/
│               └── even-more-tests.xml
└── build.gradle.kts
```

```
testing.suites.named("test", JvmTestSuite::class) {
    useJUnitJupiter()

    dependencies {
        implementation("...") // Library containing custom TestEngine
    }

    targets.all {
        testTask.configure {
            testDefinitionDirs.from("src/test/definitions") // Conventional non-class-based test definitions location
        }
    }
}
```

This feature works both with and without using [JvmTestSuites](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html).

We recommend storing non-class test definitions in the conventional location `src/<TEST_TASK_NAME>/definitions` to keep builds using this feature structured similarly; however, any location can be used.

For more information, see the section on [Non-Class-Based Testing](https://docs.gradle.org/current/userguide/java_testing.html#sec:non-class-based-testing) in the User Manual.

##### [Improved Cucumber support](https://docs.gradle.org/release-notes.html#improved-cucumber-support)

`TestEngine`s such as [Cucumber](https://cucumber.io/) previously required workarounds when testing with Gradle, such as creating an empty `@Suite` class, or using a JUnit extension like `@RunWith(Cucumber.class)` to satisfy Gradle's class-based test discovery requirement.

These non-class-based tests can now be run directly without workarounds:

```
testing.suites.named("test", JvmTestSuite::class) {
    useJUnitJupiter()

    dependencies {
        implementation("io.cucumber:cucumber-java:7.15.0")
        runtimeOnly("io.cucumber:cucumber-junit-platform-engine:7.15.0")
    }

    targets.all {
        testTask.configure {
            testDefinitionDirs.from("src/test/resources")  // Conventional Cucumber *.feature files location
        }
    }
}
```

#### [Additional test data capture](https://docs.gradle.org/release-notes.html#additional-test-data-capture)

During test execution, JUnit Platform tests can emit additional data such as file attachments or arbitrary key–value pairs using the [TestReporter API](https://docs.junit.org/current/api/org.junit.jupiter.api/org/junit/jupiter/api/TestReporter.html).

This data can include metadata about the tests or their environment, or files used or generated during testing, such as screenshots.

For example:

```
@Test
void someTestMethod(TestReporter testReporter) {
    testReporter.publishEntry("myKey", "myValue");
    testReporter.publishFile("screenshot1.svg", MediaType.create("image", "svg+xml"), file -> {});
    // Test logic continues...
}
```

Gradle now captures this metadata and integrates it directly into both the HTML test report and the [XML test results](https://docs.gradle.org/current/userguide/java_testing.html#test_reporting).

When a test publishes data, the HTML report now features two additional tabs alongside the standard `stdout` and `stderr`:

* **Data**: Displays custom key–value entries.
* **Attachments**: Provides links to any published file attachments.

To ensure compatibility with CI/CD pipelines, this data is represented in the XML output as follows:

* `ReportEntry` values are mapped to `<properties/>`.
* `FileEntry` values are formatted as `[[ATTACHMENT|/path/to/file]]`, following established conventions used by Jenkins, Azure Pipelines, and GitLab.

This capture mechanism is comprehensive; it supports both class-based and non-class-based tests and includes data published during test construction as well as setup and teardown phases.

This is especially useful for capturing failure screenshots in UI tests. For file attachments, some known media types, such as images and videos, are rendered directly in the HTML reports. Other file types are presented as links. This can make it easier to diagnose issues without reproducing them locally:

![Image 1: test-report-metadata.png](https://docs.gradle.org/current/release-notes-assets/test-report-metadata.png)

#### [Test metadata logging](https://docs.gradle.org/release-notes.html#test-metadata-logging)

Test data capture events, as detailed in the previous section, can be observed by Gradle through a new [listener](https://docs.gradle.org/current/userguide/build_lifecycle.html#buildlistener_api) dedicated to test metadata events during execution, allowing for more sophisticated tracking of test behavior.

Similar to the existing [`TestOutputListener`](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/TestOutputListener.html), you can now register a [`TestMetadataListener`](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/testing/TestMetadataListener.html) to receive structured metadata events emitted by the test framework. This is done via the new [`Test#addTestMetadataListener(TestMetadataListener)`](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html#addTestMetadataListener(TestMetadataListener)) method:

```
class LoggingListener(val logger: Logger) : TestMetadataListener {
    override fun onMetadata(descriptor: TestDescriptor , event: TestMetadataEvent) {
        logger.lifecycle("Got metadata event: " + event.toString())
    }
}

tasks.named<Test>("test").configure {
    addTestMetadataListener(LoggingListener())
}
```

This addition enables fuller support for advanced JUnit Platform features. It allows tests to communicate structured information back to the build process, providing a cleaner and more reliable alternative to parsing standard output or error streams. For example, you can use the listener to automatically copy the failure screenshots (from the previous section) to a dedicated CI artifacts directory, upload them to cloud storage for team access, or compress and archive them with timestamp-based naming.

### [CLI, logging, and problem reporting](https://docs.gradle.org/release-notes.html#cli-logging-and-problem-reporting)

Gradle provides an intuitive [command-line interface](https://docs.gradle.org/current/userguide/command_line_interface.html), detailed [logs](https://docs.gradle.org/current/userguide/logging.html), and a structured [problems report](https://docs.gradle.org/current/userguide/reporting_problems.html#sec:generated_html_report) that helps developers quickly identify and resolve build issues.

#### [Enhanced terminal progress bars](https://docs.gradle.org/release-notes.html#enhanced-terminal-progress-bars)

Gradle’s [command-line interface](https://docs.gradle.org/current/userguide/command_line_interface.html) has been updated with progress bars that offer enhanced compatibility for modern terminals:

* **Ligature-Safe Rendering:** Progress bars no longer interfere with ligature fonts, ensuring a clean visual experience.
* **Unicode Support:** High-resolution Unicode characters are now used for rendering whenever the terminal supports them.
* **Native Terminal Integration:** Added support for OSC 9;4 escape sequences. This allows native progress bar display in terminals like [Ghostty](https://ghostty.org/) and [iTerm2 >3.6.6](https://iterm2.com/).

The progress bars are displayed on terminals that support them:

![Image 2: gradle-progress-bar-new.gif](https://docs.gradle.org/current/release-notes-assets/gradle-progress-bar-new.gif)

#### [Problems HTML report refinements](https://docs.gradle.org/release-notes.html#problems-html-report-refinements)

The incubating [Problems HTML report](https://docs.gradle.org/current/userguide/reporting_problems.html#sec:generated_html_report) has been refined to provide a more intuitive and efficient user experience.

To help you find relevant information faster, the report's structure and readability have been optimized:

* **Clearer Summaries:** The summary clearly displays the number of problems that lack a specific location or were skipped for performance reasons.
* **Smart Hierarchy:** Each tab loads with collapsed trees for a cleaner initial view, while specific location and solution nodes are expanded by default to reduce the number of clicks needed to see actionable data.
* **Logical Sorting:** All entries are sorted alphabetically and by location.
* **Improved Formatting:** Problem details use a monospaced font, ensuring that multi-line messages and stack traces maintain their intended alignment.
* **Reduced Noise:** Duplicate information has been removed across the report, and the overall file size has been reduced for faster loading.

![Image 3: new-problems-report.png](https://docs.gradle.org/current/release-notes-assets/new-problems-report.png)

You can now influence whether a link to the report is printed at the end of a build via the `org.gradle.warning.mode` property. If set to `none`, the report is still generated in the background, but the link is omitted from the build output to keep your console clean.

#### [Support for CSV, Code Climate, and SARIF reports in the PMD plugin](https://docs.gradle.org/release-notes.html#support-for-csv-code-climate-and-sarif-reports-in-the-pmd-plugin)

The [PMD plugin](https://docs.gradle.org/current/userguide/pmd_plugin.html), which performs quality checks on your Java source files, has expanded its reporting capabilities.

In addition to standard XML and HTML, the plugin now supports generating reports in CSV, Code Climate, and SARIF formats. This allows for easier ingestion of PMD results by static analysis platforms and CI/CD security dashboards.

These formats are not enabled by default. To use them, configure the specific `Pmd` task (such as `pmdMain`) rather than the general `pmd` extension:

```
// Note that report configuration must be done on the `Pmd` task (here `pmdMain`), not the `pmd` extension.
tasks.pmdMain {
    reports {
        csv.required = true
        // Optional, defaults to "<project dir>/build/reports/pmd/main.csv"
        csv.outputLocation = layout.buildDirectory.file("reports/my-custom-pmd-report.csv")

        codeClimate.required = true
        // Optional, defaults to "<project dir>/build/reports/pmd/main.codeclimate.json"
        codeClimate.outputLocation = layout.buildDirectory.file("reports/my-custom-codeclimate-pmd-report.json")

        sarif.required = true
        // Optional, defaults to "<project dir>/build/reports/pmd/main.sarif.json"
        sarif.outputLocation = layout.buildDirectory.file("reports/my-custom-sarif-pmd-report.json")
    }
}
```

For more information on configuring static analysis, see the [PMD plugin documentation](https://docs.gradle.org/current/userguide/pmd_plugin.html#sec:pmd_configuration).

### [Security and infrastructure](https://docs.gradle.org/release-notes.html#security-and-infrastructure)

Gradle provides robust [security features and underlying infrastructure](https://docs.gradle.org/current/userguide/security.html) to ensure that builds are secure, reproducible, and easy to maintain.

#### [Bearer token authentication for wrapper download](https://docs.gradle.org/release-notes.html#bearer-token-authentication-for-wrapper-download)

The [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html) now supports Bearer token authentication for downloading Gradle distributions from authenticated backends. This provides a modern, secure alternative to Basic authentication (username and password), which was the only method supported in previous versions:

* **Authentication Priority:** Bearer tokens can be specified via system properties and take precedence over Basic authentication if both are configured.
* **Per-Host Configuration:** To prevent credential leakage, both Basic and Bearer authentication can now be configured on a per-host basis. This ensures your credentials are only sent to the specific hosts you authorize, rather than being broadcast globally.

While these authentication methods are supported over both HTTP and HTTPS, using a secure HTTPS backend is strongly preferred.

For more details on setup, see the [Wrapper documentation](https://docs.gradle.org/current/userguide/gradle_wrapper.html#sec:authenticated_download).

#### [Daemon logging improvements](https://docs.gradle.org/release-notes.html#daemon-logging-improvements)

The [Gradle Daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html) is a long-lived, persistent process that runs in the background and hosts Gradle’s execution engine. It dramatically reduces build times using caching, runtime optimizations, and eliminating JVM startup overhead.

Gradle Daemon logs older than 14 days are now automatically cleaned up when the daemon shuts down, eliminating the need for manual cleanup.

See the [Daemon documentation](https://docs.gradle.org/current/userguide/gradle_daemon.html#sec:daemon_log_cleanup) for more details.

Gradle provides [rich APIs](https://docs.gradle.org/current/userguide/getting_started_dev.html) for build engineers and plugin authors, enabling the creation of custom, reusable build logic and better maintainability.

#### [`Configuration.extendsFrom` accepts `Provider`s](https://docs.gradle.org/release-notes.html#configurationextendsfrom-accepts-providers)

It is now possible to pass a `Provider<Configuration>` directly when calling [`extendsFrom()`](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html#extendsFrom(org.gradle.api.artifacts.Configuration...)) on a [`Configuration`](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/Configuration.html)).

By accepting a `Provider`, Gradle can now establish the relationship without requiring the parent to be realized immediately:

```
configurations {
    // dependencyScope creates a Provider<Configuration>
    val parent = dependencyScope("parent")
    val child = resolvable("child") {
        // No .get() required; the relationship is established lazily
        extendsFrom(parent) // previously required 'parent.get()' 
    }
}
```

### [Configuration Cache](https://docs.gradle.org/release-notes.html#configuration-cache)

Gradle provides a [Configuration Cache](https://docs.gradle.org/current/userguide/configuration_cache.html) that improves build time by caching the result of the configuration phase and reusing it for subsequent builds.

#### [Improved hit rates for changes in `gradle.properties` files](https://docs.gradle.org/release-notes.html#improved-hit-rates-for-changes-in-gradleproperties-files)

Previously, changing any `gradle.properties` file resulted in invalidating the [Configuration Cache](https://docs.gradle.org/current/userguide/configuration_cache.html), even if no [project properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:project_properties) were changed, or any changed properties weren't used during the configuration phase.

Consider the following Kotlin DSL example:

```
tasks.register("printValue") {
    val value = providers.gradleProperty("value").orElse("N/A")
    doLast {
        println("value: ${value.get()}")
    }
}
```

When running the `printValue` task with the Configuration Cache enabled, Gradle caches the work graph:

```
$ ./gradlew --configuration-cache printValue

Calculating task graph as no cached configuration is available for tasks: printValue

> Task :printValue
value: N/A

...
Configuration cache entry stored.
```

Previous versions of Gradle were unable to reuse this cache entry when re-executing the `printValue` task after changing anything in `gradle.properties`:

```
$ echo "value=1" >> gradle.properties
$ ./gradlew --configuration-cache printValue

Calculating task graph as configuration cache cannot be reused because file 'gradle.properties' has changed.

> Task :printValue
value: 1

...
Configuration cache entry stored.
```

In this release, Gradle now detects that only the `value` property was changed, and that this property was never used during the configuration phase. This allows Gradle to reuse the configuration cache entry and start executing tasks faster

```
$ echo "value=1" >> gradle.properties
$ ./gradlew --configuration-cache printValue

Reusing configuration cache.

> Task :printValue
value: 1

...
Configuration cache entry reused.
```

#### [Clearer attribution for closures and lambdas](https://docs.gradle.org/release-notes.html#clearer-attribution-for-closures-and-lambdas)

Identifying the source of [Configuration Cache violations](https://docs.gradle.org/current/userguide/configuration_cache_debugging.html) can be challenging when a task contains multiple lambdas or closures. Common examples include task actions like `doFirst`/`doLast`, or task predicates such as `onlyIf`, `upToDateWhen`, and `cacheIf`/`doNotCacheIf`.

Previously, if one of these closures captured an unsupported type (such as a reference to the enclosing script), the [problem report](https://docs.gradle.org/current/userguide/configuration_cache_debugging.html#config_cache:troubleshooting) was often ambiguous:

```
fun myFalse() = false

fun noOp() { } 

tasks.register("myTask") {
    outputs.cacheIf { myFalse() }
    outputs.doNotCacheIf("reason") { myFalse() }
    outputs.upToDateWhen { myFalse() }
    onlyIf { myFalse() }
    doLast { noOp() }
}
```

In earlier versions, the report would reference a cryptic generated class name, leaving you to guess which specific block was the culprit:

![Image 4: before-action-attribution-in-cc-report.png](https://docs.gradle.org/current/release-notes-assets/before-action-attribution-in-cc-report.png)

Starting with this release, the [Configuration Cache report](https://docs.gradle.org/current/userguide/configuration_cache_debugging.html#config_cache:troubleshooting) now explicitly identifies the type of action or spec associated with each lambda. This provides the necessary context to pinpoint and fix the violation immediately:

![Image 5: action-attribution-in-cc-report.png](https://docs.gradle.org/current/release-notes-assets/action-attribution-in-cc-report.png)

### [Core plugin and plugin authoring](https://docs.gradle.org/release-notes.html#core-plugin-and-plugin-authoring)

Gradle provides a comprehensive plugin system, including built-in [Core Plugins](https://docs.gradle.org/current/userguide/plugin_reference.html) for standard tasks and powerful APIs for creating custom plugins.

#### [Default plugin IDs](https://docs.gradle.org/release-notes.html#default-plugin-ids)

This release reduces the boilerplate required for plugin authors when using the [`java-gradle-plugin` plugin](https://docs.gradle.org/current/userguide/java_gradle_plugin.html#sec:gradle_plugin_dev_usage) by introducing a sensible default for plugin IDs.

Previously, you had to explicitly provide a string for both the registration name and the `id` property. Now, the plugin ID is automatically set to the registration name by default:

```
gradlePlugin {
    plugins {
        register("my.plugin-id") {
            // id is automatically inferred as "my.plugin-id"
            implementationClass = "my.PluginClass"
        }
    }
}
```

This change makes your build scripts cleaner and less repetitive, especially in projects that define multiple plugins. If you still need a custom ID that differs from the registration name, the `id` property remains available for manual overrides.

For more details, check out the [Java Gradle Plugin documentation](https://docs.gradle.org/current/userguide/java_gradle_plugin.html).

#### [Stricter validation for published plugins](https://docs.gradle.org/release-notes.html#stricter-validation-for-published-plugins)

To ensure high quality and compatibility across the [plugin ecosystem](https://docs.gradle.org/current/userguide/plugins.html), Gradle now automatically enables [stricter validation](https://docs.gradle.org/current/userguide/preparing_to_publish.html#validating) for projects that use the `com.gradle.plugin-publish`, `ivy-publish`, or `maven-publish` plugins.

This validation catches common issues, such as missing task input annotations or improper property definitions, before a plugin is distributed.

To avoid breaking your internal builds, this automatic enforcement does not apply to local plugins (e.g., those in `buildSrc` or included builds).

While only enabled by default for publishing, we recommend opting into stricter validation for all plugin projects to ensure they are robust and future-proof. You can enable it manually in your build script:

```
tasks.validatePlugins {
    enableStricterValidation = true
}
```

### [Tooling and IDE integration](https://docs.gradle.org/release-notes.html#tooling-and-ide-integration)

Gradle provides [Tooling APIs](https://docs.gradle.org/current/userguide/third_party_integration.html) that facilitate deep integration with modern IDEs and CI/CD pipelines.

#### [New property for Tooling API parallelism control](https://docs.gradle.org/release-notes.html#new-property-for-tooling-api-parallelism-control)

Gradle now provides granular control over how [Tooling API](https://docs.gradle.org/current/userguide/tooling_api.html) clients interact with your build in parallel using a new `org.gradle.tooling.parallel`[property](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_configuration_properties).

Previously, parallelism for Tooling API actions was tied directly to the `org.gradle.parallel` property. This meant that if you wanted to enable parallel task execution, you were forced to also enable parallel IDE actions, and vice versa.

The new property decouples these two behaviors. This is particularly relevant for the IDE Sync scenarios, where IDEs can take advantage of the parallelism to improve performance (independently of your task execution strategy):

```
# gradle.properties

// Controls parallelism for Tooling API clients (e.g., IDE Sync)
org.gradle.tooling.parallel=true

// Controls parallelism for task execution (e.g., build/test)
org.gradle.parallel=false
```

When `org.gradle.tooling.parallel` is not specified, it defaults to the value of `org.gradle.parallel`, preserving existing behavior and performance characteristics. For more information, see the [Tooling API parallelism configuration](https://docs.gradle.org/current/userguide/performance.html#sec:configure_tooling_api_actions_parallelism) section of the user guide.

#### [Tooling integration improvements](https://docs.gradle.org/release-notes.html#tooling-integration-improvements)

This release adds a few enhancements to the built-in [Tooling API](https://docs.gradle.org/current/userguide/tooling_api.html) models:

* **Instant Version Info:** Clients can now access the exact output of `gradle --version` without starting a daemon, via the new [`BuildEnvironment.getVersionInfo()`](https://docs.gradle.org/current/javadoc/org/gradle/tooling/model/build/BuildEnvironment.html#getVersionInfo()) property.
* **Built-in Help Model:** A new [`Help`](https://docs.gradle.org/current/javadoc/org/gradle/tooling/model/build/Help.html) model exposes the output of the `gradle --help` command-line build invocation.

The following example demonstrates how to retrieve version and help information using a [`ProjectConnection`](https://docs.gradle.org/current/javadoc/org/gradle/tooling/ProjectConnection.html):

```
import org.gradle.tooling.GradleConnector;
import org.gradle.tooling.ProjectConnection;
import org.gradle.tooling.model.build.BuildEnvironment;
import org.gradle.tooling.model.build.Help;

import java.io.File;

void main() {
    var projectDir = new File("/path/to/project");
    try (var conn = GradleConnector.newConnector().forProjectDirectory(projectDir).connect()) {
        System.out.println("--version:\n + " + conn.getModel(BuildEnvironment.class).getVersionInfo());
        System.out.println("--help:\n" + conn.getModel(Help.class).getRenderedText());
    }
}
```

[Promoted features](https://docs.gradle.org/release-notes.html#promoted-features)
---------------------------------------------------------------------------------

Promoted features are features that were incubating in previous versions of Gradle but are now supported and subject to backward compatibility. See the User Manual section on the "[Feature Lifecycle](https://docs.gradle.org/current/userguide/feature_lifecycle.html)" for more information.

The following are the features that have been promoted in this Gradle release.

* [`getSettingsDirectory()`](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ProjectLayout.html#getSettingsDirectory()) in `ProjectLayout`

### [Task graph is now stable](https://docs.gradle.org/release-notes.html#task-graph-is-now-stable)

The [task graph](https://docs.gradle.org/current/userguide/command_line_interface.html#sec:command_line_execution_options), introduced as an incubating feature in Gradle 9.1.0, is now stable. It is no longer marked as experimental.

[Documentation and training](https://docs.gradle.org/release-notes.html#documentation-and-training)
---------------------------------------------------------------------------------------------------

### [Documentation](https://docs.gradle.org/release-notes.html#documentation)

#### [User Manual](https://docs.gradle.org/release-notes.html#user-manual)

A brand-new section of the User Manual has been started, called [Securing Your Gradle Builds](https://docs.gradle.org/current/userguide/security.html).

#### [Best Practices](https://docs.gradle.org/release-notes.html#best-practices)

The following best practices have been added in this Gradle release:

* [Prefer the -bin Gradle Distribution](https://docs.gradle.org/current/userguide/best_practices_performance.html#prefer_bin_distribution)

### [Training](https://docs.gradle.org/release-notes.html#training)

The following course is now available:

* [Authoring Gradle Plugins](https://dpeuniversity.gradle.com/app/courses/7603d9fb-620d-4d60-8e79-ee94433dc2b1)

[Fixed issues](https://docs.gradle.org/release-notes.html#fixed-issues)
-----------------------------------------------------------------------

89 issues have been fixed in Gradle 9.4.0.

* [[#36544](https://github.com/gradle/gradle/issues/36544)] - Excluded tests in a suite are no longer being run
* [[#36483](https://github.com/gradle/gradle/issues/36483)] - Symbolic links are completely broken with Gradle 9.2.0+
* [[#36457](https://github.com/gradle/gradle/issues/36457)] - TestKit test fails with test distribution
* [[#36364](https://github.com/gradle/gradle/issues/36364)] - Host specific wrapper credential property names are case-sensitive
* [[#36351](https://github.com/gradle/gradle/issues/36351)] - Expose nullable JavaBean properties from definitions in DCL
* [[#36343](https://github.com/gradle/gradle/issues/36343)] - Build scripts should report a warning when multiple candidates are present
* [[#36319](https://github.com/gradle/gradle/issues/36319)] - Progress bar garbled in Git Bash for Windows 2.47 or later, or with experimental pseudo consoles support enabled
* [[#36266](https://github.com/gradle/gradle/issues/36266)] - Test failure: WorkerExecutorErrorHandlingIntegrationTest
* [[#36225](https://github.com/gradle/gradle/issues/36225)] - WriteProperties.setProperties() does not clear deferedProperties
* [[#36200](https://github.com/gradle/gradle/issues/36200)] - DCL: org.gradle.kotlin.dsl.dcl=true - KTS configuring functions for nested models are missing
* [[#36189](https://github.com/gradle/gradle/issues/36189)] - Wrapper: system property priority order is incorrect
* [[#36180](https://github.com/gradle/gradle/issues/36180)] - CC report summary shows misleading information regarding unique vs considered problems
* [[#36150](https://github.com/gradle/gradle/issues/36150)] - Broken support for junit dynamic test source URI schemes
* [[#36068](https://github.com/gradle/gradle/issues/36068)] - CC entry for sanityCheck should not depend on accepted-public-api-changes.json content
* [[#36046](https://github.com/gradle/gradle/issues/36046)] - Configuration cache report threshold for unique problems is triggered by non-unique problems
* [[#35999](https://github.com/gradle/gradle/issues/35999)] - Investigate Spek2 behavior in Gradle 9.4
* [[#35998](https://github.com/gradle/gradle/issues/35998)] - Configuration Cache miss when changing -P command line properties (Regression in 9.2)
* [[#35974](https://github.com/gradle/gradle/issues/35974)] - JUnit 6 support
* [[#35923](https://github.com/gradle/gradle/issues/35923)] - ServiceRegistry service registration is not thread-safe
* [[#35883](https://github.com/gradle/gradle/issues/35883)] - Provide an option to suppress '[Incubating] Problems report is available at' message
* [[#35875](https://github.com/gradle/gradle/issues/35875)] - Missing space in message when running Gradle outside of a Gradle project
* [[#35869](https://github.com/gradle/gradle/issues/35869)] - DCL: bindProjectFeature does not support BuildModel.NONE for the Feature Definition
* [[#35840](https://github.com/gradle/gradle/issues/35840)] - Settings scripts should report a warning when multiple candidates are present
* [[#35839](https://github.com/gradle/gradle/issues/35839)] - Numbers displayed in the Problems report tabs are non-sensical
* [[#35803](https://github.com/gradle/gradle/issues/35803)] - Refine daemon logs cleanup to provide progress, build ops and configurability
* [[#35766](https://github.com/gradle/gradle/issues/35766)] - Use of `AvailableJavaHomes` causes NPEs when environment is not ready
* [[#35740](https://github.com/gradle/gradle/issues/35740)] - Gradle currently trigger vulnerability scan tools because of the version of its commons-lang3 dependency
* [[#35722](https://github.com/gradle/gradle/issues/35722)] - Tests of Gradle fail on Windows due to incorrect URL to path conversion
* [[#35721](https://github.com/gradle/gradle/issues/35721)] - Provide better attribution for task-captured closures in the configuration cache report
* [[#35705](https://github.com/gradle/gradle/issues/35705)] - Make resilient sync work when running tasks before querying models via Tooling API
* [[#35698](https://github.com/gradle/gradle/issues/35698)] - Problems API annotation is unclear
* [[#35697](https://github.com/gradle/gradle/issues/35697)] - Documented Problems API CLI output is wrong
* [[#35649](https://github.com/gradle/gradle/issues/35649)] - Default plugin id to the name of registration container
* [[#35584](https://github.com/gradle/gradle/issues/35584)] - Add IP Gradleception tests to synthetically schedule all tasks
* [[#35572](https://github.com/gradle/gradle/issues/35572)] - Kotlin DSL fails with a compilation error in 9.2.0 if unicode symbols are present in gradle user home
* [[#35553](https://github.com/gradle/gradle/issues/35553)] - Pass a query type of org.gradle.tooling.BuildController calls to internal BuildToolingModelController
* [[#35551](https://github.com/gradle/gradle/issues/35551)] - Make `BuildController.fetch` automatically work in resilient mode
* [[#35537](https://github.com/gradle/gradle/issues/35537)] - Ligature-safe progress bar with Unicode blocks and ASCII fallback (avoid ===, --> sequences)
* [[#35520](https://github.com/gradle/gradle/issues/35520)] - Eclipse does not respect order of dependencies in build path
* [[#35518](https://github.com/gradle/gradle/issues/35518)] - Throwables thrown from OperationCompletionListeners are silently ignored
* [[#35497](https://github.com/gradle/gradle/issues/35497)] - Enable all available plugin development checks for published plugins
* [[#35494](https://github.com/gradle/gradle/issues/35494)] - CodeNarc / Groovy plugin `CustomCompilerPhaseSourceDecorator` regression
* [[#35480](https://github.com/gradle/gradle/issues/35480)] - Support for non-class-based test events in the Tooling API
* [[#35434](https://github.com/gradle/gradle/issues/35434)] - Polish `ResilientKotlinDslScriptsModelBuilderCrossVersionSpec`, solve remaining TODOs
* [[#35423](https://github.com/gradle/gradle/issues/35423)] - Smoke and performance tests using Santa Tracker don't work with the upcoming AGP 9.0
* [[#35418](https://github.com/gradle/gradle/issues/35418)] - Improve error handling on configuration failures for resilient Tooling API models
* [[#35406](https://github.com/gradle/gradle/issues/35406)] - Support running on Java 26
* [[#35405](https://github.com/gradle/gradle/issues/35405)] - Support compiling and testing on Java 26
* [[#35385](https://github.com/gradle/gradle/issues/35385)] - Thread-unsafe code in DefaultServiceRegistry$OwnServices leads to CME
* [[#35211](https://github.com/gradle/gradle/issues/35211)] - Support third-party model builders to run after configuration failures, but only for successful builds
* [[#35204](https://github.com/gradle/gradle/issues/35204)] - Getting warning about Kotlin being incompatible with JDK 25 with Gradle 9.1.0, JDK 25, and Kotlin DSL
* [[#35029](https://github.com/gradle/gradle/issues/35029)] - About `gradle.properties` in subprojects and the new "best practice"
* [[#35005](https://github.com/gradle/gradle/issues/35005)] - Retire/Remove `SoftwareType` annotation and functionality
* [[#34916](https://github.com/gradle/gradle/issues/34916)] - Kotlin DSL build script is not recompiled if its name changed
* [[#34705](https://github.com/gradle/gradle/issues/34705)] - Unify locking logic in AssignImmutableWorkspaceStep
* [[#34585](https://github.com/gradle/gradle/issues/34585)] - Docker: Could not move inconsistent immutable workspace
* [[#34539](https://github.com/gradle/gradle/issues/34539)] - JavaGradlePluginPlugin adds gradleApi() to wrong configuration
* [[#34525](https://github.com/gradle/gradle/issues/34525)] - De-incubate Task graph printing mode
* [[#34374](https://github.com/gradle/gradle/issues/34374)] - Missing removeUnusedEntriesAfterDays() documentation for 9.0.0
* [[#34147](https://github.com/gradle/gradle/issues/34147)] - Warn about multiple script files for a project
* [[#32945](https://github.com/gradle/gradle/issues/32945)] - Fix exclude simplification logic
* [[#32928](https://github.com/gradle/gradle/issues/32928)] - ProjectBuilder does not set layout.settingsDirectory
* [[#31966](https://github.com/gradle/gradle/issues/31966)] - Gradle init exception.Migrating to gradle from maven. lost all exclusions.
* [[#31888](https://github.com/gradle/gradle/issues/31888)] - `mavenContent.snapshotsOnly()` does not seem to work with unique SNAPSHOT versions
* [[#31671](https://github.com/gradle/gradle/issues/31671)] - Make the Configuration Cache report smaller for Isolated Projects
* [[#31243](https://github.com/gradle/gradle/issues/31243)] - Internal options are not customizable for sync
* [[#30990](https://github.com/gradle/gradle/issues/30990)] - Eliminate potential deadlocks when writing CC fingerprint
* [[#29678](https://github.com/gradle/gradle/issues/29678)] - Expose Gradle services like ProviderFactory to init scripts
* [[#28974](https://github.com/gradle/gradle/issues/28974)] - Transforms cache problems "Could not read workspace metadata"
* [[#26732](https://github.com/gradle/gradle/issues/26732)] - Configuration.extendsFrom: Support Provider<Configuration>
* [[#25345](https://github.com/gradle/gradle/issues/25345)] - No longer possible to specify a executable which is not part of a Java toolchain for a JavaExec task
* [[#24693](https://github.com/gradle/gradle/issues/24693)] - Detection of environment variables accessed taking 4% of build activity in some builds
* [[#22610](https://github.com/gradle/gradle/issues/22610)] - Support CSV, Code Climate, and SARIF reports for the PMD plugin
* [[#22428](https://github.com/gradle/gradle/issues/22428)] - Can't use `kotlin-dsl` inside a precompiled script plugin that is applied to other precompiled script plugins
* [[#21695](https://github.com/gradle/gradle/issues/21695)] - Gradle debugging suspending on startup should inform that it is waiting for debugger to attach
* [[#19788](https://github.com/gradle/gradle/issues/19788)] - ResolvedVariantResult getResolvedVariant() is sometimes null
* [[#18875](https://github.com/gradle/gradle/issues/18875)] - gradle init ignoring <exclusions> in dependency definition of maven pom.xml
* [[#4773](https://github.com/gradle/gradle/issues/4773)] - JUnit 5: Allow resource-based testing
* [[#4605](https://github.com/gradle/gradle/issues/4605)] - Support JUnit platform reporting entries
* [[#2688](https://github.com/gradle/gradle/issues/2688)] - Gradle logging hygiene
* [[#36841](https://github.com/gradle/gradle/issues/36841)] - [Gradle 9.4.0-rc-1] No Provider<Configuration> based override for nested `extendsFrom`
* [[#36808](https://github.com/gradle/gradle/issues/36808)] - IllegalStateException: Expected exactly one run for grouping node when Develocity Test Distribution reschedules tests after remote executor disconnections
* [[#36797](https://github.com/gradle/gradle/issues/36797)] - Intellij sync fails with `Could not find gradle:gradle:9.4.0-rc-1` for offline distribution URLs
* [[#36790](https://github.com/gradle/gradle/issues/36790)] - Build failing due to "Please remove path-based exclude patterns when running only class-based tests" after 9.4.0-rc-1 update
* [[#36751](https://github.com/gradle/gradle/issues/36751)] - `SerializableTestResultStore` flaky crash in `OutputRanges` when running Kotlin/Wasm tests
* [[#36726](https://github.com/gradle/gradle/issues/36726)] - SourceDistributionProvider doesn't derive url from distributionUrl for included builds
* [[#36719](https://github.com/gradle/gradle/issues/36719)] - Unexpected Problem id required for deprecation logger
* [[#36681](https://github.com/gradle/gradle/issues/36681)] - Unicode progress bar in 9.4.0 does not work on Mac and Linux
* [[#20969](https://github.com/gradle/gradle/issues/20969)] - Project properties not used at configuration time can still invalidate configuration cache

[Known issues](https://docs.gradle.org/release-notes.html#known-issues)
-----------------------------------------------------------------------

Known issues are problems that were discovered post-release that are directly related to changes made in this release.

3 issues are known to affect Gradle 9.4.0.

* [[#37045](https://github.com/gradle/gradle/issues/37045)] - projects task fails due to "Incorrect lifecycle state" error
* [[#36961](https://github.com/gradle/gradle/issues/36961)] - 9.4.0: Unable to find a variant with the requested capability: coordinates 'org.jetbrains.kotlin:kotlin-gradle-plugin-api-gradle813'
* [[#35969](https://github.com/gradle/gradle/issues/35969)] - Possible false positive deprecation warning for "Declaring a dependency on an unpublished project has been deprecated" in 9.3.0-rc-1

[External contributions](https://docs.gradle.org/release-notes.html#external-contributions)
-------------------------------------------------------------------------------------------

We love getting contributions from the Gradle community. For information on contributing, please see [gradle.org/contribute](https://gradle.org/contribute).

[Reporting problems](https://docs.gradle.org/release-notes.html#reporting-problems)
-----------------------------------------------------------------------------------

If you find a problem with this release, please file a bug on [GitHub Issues](https://github.com/gradle/gradle/issues) adhering to our issue guidelines. If you're not sure if you're encountering a bug, please use the [forum](https://discuss.gradle.org/c/help-discuss).

We hope you will build happiness with Gradle, and we look forward to your feedback via [Twitter](https://twitter.com/gradle) or on [GitHub](https://github.com/gradle).
