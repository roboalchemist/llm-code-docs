# Source: https://docs.gradle.org/userguide/build_lifecycle.html

Title: Build Lifecycle

URL Source: https://docs.gradle.org/userguide/build_lifecycle.html

Markdown Content:
The build lifecycle is the sequence of phases Gradle executes to turn your build scripts into completed work, from initializing the build environment to configuring projects and finally executing tasks.

[](https://docs.gradle.org/userguide/build_lifecycle.html#build_phases)[Build Phases](https://docs.gradle.org/userguide/build_lifecycle.html#build_phases)
----------------------------------------------------------------------------------------------------------------------------------------------------------

A Gradle build has three distinct phases.

![Image 1: author gradle 1](https://docs.gradle.org/current/userguide/img/author-gradle-1.png)

Gradle runs these phases in order:

| Phase 1. Initialization | Phase 2. Configuration | Phase 3. Execution |
| --- | --- | --- |
| - Detects the **settings file** - Creates a [`Settings`](https://docs.gradle.org/current/dsl/org.gradle.api.initialization.Settings.html) instance - Evaluates the **settings file** to determine which projects (and included builds) make up the build - Creates a [`Project`](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html) instance **for every project** | - Evaluates the **build files of every project** participating in the build - Creates a **task graph** for requested tasks | - Schedules and **executes** the selected **tasks** |

![Image 2: build lifecycle example](https://docs.gradle.org/current/userguide/img/build-lifecycle-example.png)

The following example shows which parts of settings and build files correspond to various build phases:

`Kotlin``Groovy`

settings.gradle

```
rootProject.name = 'basic'
println 'This is executed during the initialization phase.'
```

build.gradle

```
println 'This is executed during the configuration phase.'

tasks.register('configured') {
    println 'This is also executed during the configuration phase, because :configured is used in the build.'
}

tasks.register('test') {
    doLast {
        println 'This is executed during the execution phase.'
    }
}

tasks.register('testBoth') {
 doFirst {
   println 'This is executed first during the execution phase.'
 }
 doLast {
   println 'This is executed last during the execution phase.'
 }
 println 'This is executed during the configuration phase as well, because :testBoth is used in the build.'
}
```

The following command executes the `test` and `testBoth` tasks specified above. Because Gradle only configures requested tasks and their dependencies, the `configured` task never configures:

`$ ./gradlew test testBoth`

```
This is executed during the initialization phase.

> Configure project :
This is executed during the configuration phase.
This is executed during the configuration phase as well, because :testBoth is used in the build.

> Task :test
This is executed during the execution phase.

> Task :testBoth
This is executed first during the execution phase.
This is executed last during the execution phase.

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

`$ ./gradlew test testBoth`

```
This is executed during the initialization phase.

> Configure project :
This is executed during the configuration phase.
This is executed during the configuration phase as well, because :testBoth is used in the build.

> Task :test
This is executed during the execution phase.

> Task :testBoth
This is executed first during the execution phase.
This is executed last during the execution phase.

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

### [](https://docs.gradle.org/userguide/build_lifecycle.html#initialization)[Phase 1. Initialization](https://docs.gradle.org/userguide/build_lifecycle.html#initialization)

In the **initialization phase**, Gradle detects the set of projects (root and subprojects) and included builds participating in the build.

Gradle first evaluates the settings file, `settings.gradle(.kts)`, and instantiates a `Settings` object.

Then, Gradle instantiates `Project` object instances for each project included in the build (using `includeBuild()` or `include()` in the settings file).

### [](https://docs.gradle.org/userguide/build_lifecycle.html#configuration)[Phase 2. Configuration](https://docs.gradle.org/userguide/build_lifecycle.html#configuration)

In the **configuration phase**, Gradle adds tasks and other properties to the projects found by the initialization phase.

Gradle constructs the [task graph](https://docs.gradle.org/userguide/build_lifecycle.html#task_graph) by understanding the dependencies between tasks.

### [](https://docs.gradle.org/userguide/build_lifecycle.html#execution)[Phase 3. Execution](https://docs.gradle.org/userguide/build_lifecycle.html#execution)

In the **execution phase**, Gradle runs tasks.

Gradle uses the [task execution graphs](https://docs.gradle.org/userguide/build_lifecycle.html#task_graph) generated by the configuration phase to determine which tasks to execute. Gradle can execute tasks in parallel.

[](https://docs.gradle.org/userguide/build_lifecycle.html#task_graph)[Task Graphs](https://docs.gradle.org/userguide/build_lifecycle.html#task_graph)
-----------------------------------------------------------------------------------------------------------------------------------------------------

As a build author, you write build logic by defining tasks and declaring how they depend on one another. Gradle uses this information to construct a **task graph** during the **configuration phase** that models the relationships between these tasks.

For example, if your project includes tasks such as `build`, `assemble`, and `createDocs`, and you declare that `assemble` depends on `build`, and `createDocs` depends on `assemble`, Gradle constructs a graph with this order: `build` → `assemble` → `createDocs`.

Gradle builds the task graph **before** executing any task(s).

This diagram shows two example task graphs, one abstract and the other concrete, with dependencies between tasks represented as arrows:

![Image 3: task dag examples](https://docs.gradle.org/current/userguide/img/task-dag-examples.png)

[](https://docs.gradle.org/userguide/build_lifecycle.html#lifecycle_api)[Hooks into the Gradle Build Lifecycle](https://docs.gradle.org/userguide/build_lifecycle.html#lifecycle_api)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle exposes several APIs that allow you to listen to or react to key points in the build lifecycle.

Some APIs let you hook into those phases in init scripts, `settings.gradle(.kts)` or `build.gradle(.kts)` to customize or inspect the build as Gradle configures it. These hooks let you:

* react to the structure of the build (root + subprojects),

* configure all projects before their own build scripts are evaluated,

* debug or collect information during configuration.

### [](https://docs.gradle.org/userguide/build_lifecycle.html#gradle_lifecycle_api)[Gradle Lifecycle API](https://docs.gradle.org/userguide/build_lifecycle.html#gradle_lifecycle_api)

The [`Gradle`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html) API accessible via `gradle` and newer [`GradleLifecycle`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/GradleLifecycle.html) API, accessible via `gradle.lifecycle`, can be used to register actions to be executed at certain points in the build lifecycle:

```
buildStarted -> DEPRECATED in Gradle 6
 └─ beforeSettings
     └── settingsEvaluated
          └── projectsLoaded
               ├── beforeProject
               ├── afterProject
               └── projectsEvaluated
                     └── buildFinished -> DEPRECATED in Gradle 7
```

| # | Hook | Phase | Best for |
| --- | --- | --- | --- |
| [1](https://docs.gradle.org/userguide/build_lifecycle.html#before_settings) | [`gradle.beforeSettings`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html#beforeSettings(groovy.lang.Closure)) | Before the `settings.gradle(.kts)` is evaluated. | Early wiring from an init script: global logging/metrics, tweaking `gradle.startParameter`, choosing different settings files, or setting values on the `Settings` object before it’s evaluated. |
| [2](https://docs.gradle.org/userguide/build_lifecycle.html#settings_evaluated) | [`gradle.settingsEvaluated`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html#settingsEvaluated(groovy.lang.Closure)) | After evaluating `settings.gradle(.kts)` | Adjusting repositories, enabling build scans, reading environment variables, or changing build layout. |
| [3](https://docs.gradle.org/userguide/build_lifecycle.html#projects_loaded) | [`gradle.projectsLoaded`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html#projectsLoaded(groovy.lang.Closure)) | After all projects are discovered but before any are configured | Applying configuration to every project (for example, adding a plugin to all subprojects). |
| [4](https://docs.gradle.org/userguide/build_lifecycle.html#before_project) | [`gradle.lifecycle.beforeProject`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/GradleLifecycle.html#beforeProject(org.gradle.api.IsolatedAction)) | Before each project’s `build.gradle(.kts)` is evaluated | Applying defaults, logging project configuration start. |
| [5](https://docs.gradle.org/userguide/build_lifecycle.html#after_project) | [`gradle.lifecycle.afterProject`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/GradleLifecycle.html#afterProject(org.gradle.api.IsolatedAction)) | After each project’s `build.gradle(.kts)` is evaluated | Validating configuration or detecting missing plugins. |
| [6](https://docs.gradle.org/userguide/build_lifecycle.html#projects_evaluated) | [`gradle.projectsEvaluated`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html#projectsEvaluated(org.gradle.api.Action)) | After **all** projects have been evaluated | Performing cross-project validation, configuration summaries, or creating aggregated tasks. |

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#before_settings)[`beforeSettings`](https://docs.gradle.org/userguide/build_lifecycle.html#before_settings)

**Where**: init script.

**When**: By the time `settings.gradle(.kts)` is executing, `beforeSettings` has already fired.

`Kotlin``Groovy`

callbacks.init.gradle

```
// 1. beforeSettings: tweak start parameters / log early info
// before the build settings have been loaded and evaluated.
gradle.beforeSettings {
    println("[beforeSettings] gradleUserHome = ${gradle.gradleUserHomeDir}")

    // Example: default to --parallel if an env var is set
    if (System.getenv("CI") == "true") {
        println("[beforeSettings] Enabling parallel execution on CI")
        gradle.startParameter.parallelProjectExecutionEnabled = true
    } else {
        println("[beforeSettings] Disabling parallel execution, not on CI")
        gradle.startParameter.parallelProjectExecutionEnabled = false
    }

    println("")
}
```

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#settings_evaluated)[`settingsEvaluated`](https://docs.gradle.org/userguide/build_lifecycle.html#settings_evaluated)

**Where**: `settings.gradle(.kts)`.

**When**: After the settings file finishes evaluating.

`Kotlin``Groovy`

callbacks.init.gradle

```
// 2. settingsEvaluated: adjust build layout / repositories / scan config
// when the build settings have been loaded and evaluated.
gradle.settingsEvaluated { settings ->
    println("[settingsEvaluated] rootProject = ${settings.rootProject.name}")

    // Example: enforce a company-wide pluginManagement repo
    settings.pluginManagement.repositories.with {
        println("[settingsEvaluated] Ensuring company plugin repo is configured")
        mavenCentral()
    }

    println("")
}
```

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#projects_loaded)[`projectsLoaded`](https://docs.gradle.org/userguide/build_lifecycle.html#projects_loaded)

**Where**: `settings.gradle(.kts)`.

**When**: All projects have been discovered but not yet configured.

`Kotlin``Groovy`

callbacks.init.gradle

```
// 3. projectsLoaded: we know the full project graph, but nothing configured yet
// to be called when the projects for the build have been created from the settings.
gradle.projectsLoaded {
    println "[projectsLoaded] Projects discovered: " + rootProject.allprojects.collect { it.name }.join(', ')

    // Example: Add a custom property (using the extra properties extension)
    allprojects {
        println("[projectsLoaded] Setting extra property on ${name}")
        extensions.extraProperties["isInitScriptConfigured"] = true
    }
}
```

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#before_project)[`beforeProject`](https://docs.gradle.org/userguide/build_lifecycle.html#before_project)

**Where**: `build.gradle(.kts)` or anywhere you have access to the Gradle instance.

**When**: For each project as its build script is evaluated.

`Kotlin``Groovy`

callbacks.init.gradle

```
// to be called immediately before a project is evaluated.
gradle.lifecycle.beforeProject {
    println("[lifecycle.beforeProject] Started configuring ${path}")
}

// 4. beforeProject: runs before each build.gradle(.kts) is evaluated
// to be called immediately before a project is evaluated.
gradle.beforeProject { project ->
    println("[beforeProject] Started configuring ${project.path}")

    println("[beforeProject] Setup a global build directory for ${project.name}")
    project.layout.buildDirectory.set(
        project.layout.projectDirectory.dir("build")
    )
}
```

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#after_project)[`afterProject`](https://docs.gradle.org/userguide/build_lifecycle.html#after_project)

**Where**: `build.gradle(.kts)` or anywhere you have access to the Gradle instance.

**When**: For each project as its build script is evaluated.

`Kotlin``Groovy`

callbacks.init.gradle

```
// 5. afterProject: runs after each build.gradle(.kts) is evaluated
// to be called immediately after a project is evaluated.
gradle.afterProject { project ->
    println("[afterProject] Finished configuring ${project.path}")

    // Example: apply the Java plugin to all projects that don’t have any plugin yet
    if (project.plugins.hasPlugin("java")) {
        println("[afterProject] ${project.path} already has the java plugin")
    } else {
        println("[afterProject] Applying java plugin to ${project.path}")
        project.apply(plugin: "java")
    }
}

// to be called immediately after a project is evaluated.
gradle.lifecycle.afterProject {
    println("[lifecycle.afterProject] Finished configuring ${path}")
}
```

#### [](https://docs.gradle.org/userguide/build_lifecycle.html#projects_evaluated)[`projectsEvaluated`](https://docs.gradle.org/userguide/build_lifecycle.html#projects_evaluated)

**Where**: `build.gradle(.kts)` or anywhere you have access to the Gradle instance.

**When**: After all projects have been evaluated (i.e., all `build.gradle(.kts)` files are read and configuration is complete), but before task graph is finalized and before execution starts.

`Kotlin``Groovy`

callbacks.init.gradle

```
// 6. projectsEvaluated: all projects are fully configured, safe for cross-project checks
// to be called when all projects for the build have been evaluated.
gradle.projectsEvaluated {
    println("[projectsEvaluated] All projects evaluated")

    // Example: globally configure the java plugin
    allprojects { project ->
        def javaExtension = project.extensions.findByType(JavaPluginExtension)
        if(javaExtension) {
            if (javaExtension.toolchain.languageVersion.orNull != null) {
                println("[projectsEvaluated] ${path} uses Java plugin with toolchain ${javaExtension.toolchain.displayName}")
            } else {
                println("[projectsEvaluated] WARNING: ${path} uses Java plugin but no toolchain is configured, setting Java 17")
                javaExtension.toolchain.languageVersion.set(JavaLanguageVersion.of(17))
            }
        }
    }
}
```

### [](https://docs.gradle.org/userguide/build_lifecycle.html#buildlistener_api)[BuildListener API](https://docs.gradle.org/userguide/build_lifecycle.html#buildlistener_api)

The legacy [`BuildListener`](https://docs.gradle.org/current/javadoc/org/gradle/BuildListener.html) API is also available. This listener interface is supported for backward compatibility, but its callbacks have been gradually deprecated as equivalent events became available through the `Gradle` and `GradleLifecycle` APIs.

```
beforeSettings
    └── settingsEvaluated
        └── projectsLoaded
            └── projectsEvaluated
                └── taskCompletion
                    └── buildFinished -> DEPRECATED in Gradle 7
```

### [](https://docs.gradle.org/userguide/build_lifecycle.html#flow_api)[Flow API](https://docs.gradle.org/userguide/build_lifecycle.html#flow_api)

The [FlowAction API](https://docs.gradle.org/current/userguide/dataflow_actions.html#dataflow_action) replaces ad-hoc listeners with a declarative, dependency-aware graph of “flows” which are actions that react to lifecycle transitions and produce well-defined outcomes.
