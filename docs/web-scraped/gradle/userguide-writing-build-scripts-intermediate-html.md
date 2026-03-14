# Source: https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html

Title: Writing Build Scripts

URL Source: https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html

Markdown Content:
The initialization phase in the Gradle Build lifecycle finds the settings file.

![Image 1: gradle basic 11](https://docs.gradle.org/current/userguide/img/gradle-basic-11.png)

When Gradle evaluates the settings file, it creates a single [`Settings`](https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/Settings.html) instance.

Then, for each project declared in the settings file, Gradle creates a corresponding [`Project`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html) instance.

Gradle then locates the associated build script (e.g., `build.gradle(.kts)`) and uses it during the configuration phase to configure each `Project` object.

[](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#anatomy_of_a_build_script)[Anatomy of a Build Script](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#anatomy_of_a_build_script)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle build scripts are written in either [Groovy DSL](https://docs.gradle.org/current/userguide/groovy_build_script_primer.html#groovy_build_script_primer) or [Kotlin DSL](https://docs.gradle.org/current/userguide/kotlin_dsl.html#kotdsl:kotlin_dsl) (domain-specific language). The build script is either a `*.gradle` file in Groovy or a `*.gradle.kts` file in Kotlin.

As a build script executes, it configures either a [`Settings`](https://docs.gradle.org/current/javadoc/org/gradle/api/initialization/Settings.html) object or [`Project`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html) object and its children.

![Image 2: Build](https://docs.gradle.org/current/userguide/img/author-gradle-3.png)

![Image 3: Build](https://docs.gradle.org/current/userguide/img/author-gradle-4.png)

There is a third type of build script that also configures a [`Gradle`](https://docs.gradle.org/current/javadoc/org/gradle/api/invocation/Gradle.html) object, but it is not covered in the intermediate concepts.

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#script_structure)[Script Structure](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#script_structure)

A Gradle script consists of two main types of elements:

1. **Statements:** Top-level expressions that execute immediately during the initialization (for settings scripts) or configuration (for build scripts) phase.

2. **Blocks:** Nested sections (Groovy _closures_ or Kotlin _lambdas_) passed to configuration methods. These blocks apply settings to Gradle objects like `project`, `pluginManagement`, `dependencyResolutionManagement`, `repositories`, or `dependencies`.

Examples of common blocks include:

`Kotlin``Groovy`

api/build.gradle

```
plugins {
    id 'java'
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation "junit:junit:4.13"
    implementation project(':shared')
}
```

In this case, we are looking at a build script. Therefore, each block corresponds to a method on the [`Project`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html) object, also referred to as the Project API, and is evaluated with a **delegate** or **receiver** (more on that below).

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#closures_and_lambdas)[Closures and Lambdas](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#closures_and_lambdas)

Gradle scripts are based on dynamic _closures_ in Groovy or static _lambdas_ in Kotlin:

* In Groovy, blocks are _closures_, and Gradle dynamically **delegates** method/property calls to a target object.

* In Kotlin, blocks are _lambdas_ with **receivers**, and Gradle statically types the `this` object inside the block.

This delegation allows concise configuration:

```
repositories {
    mavenCentral()
}
```

```
repositories {
    mavenCentral()
}
```

Inside the block, `mavenCentral()` is a method on that **receiver**, so no qualifier is needed.

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#delegates_and_receivers)[Delegates and Receivers](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#delegates_and_receivers)

Every configuration block executes in the context of an object:

* In Groovy, this is the block’s **delegate**.

* In Kotlin, this is the block’s **receiver**.

```
dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib")
}
```

This behavior allows intuitive configuration but can sometimes obscure where a method is coming from. For clarity, you can use explicit references like `project.dependencies.implementation(…​)`.

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#sec:declaring_variables)[Variables](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#sec:declaring_variables)

Build scripts support two types of variables:

1. Local Variables

2. Extra Properties

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#sec:local_variables)[Local Variables](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#sec:local_variables)

Declare local variables with the `val` keyword. Local variables are only visible in the scope where they have been declared. They are a feature of the underlying Kotlin language.

Declare local variables with the `def` keyword. Local variables are only visible in the scope where they have been declared. They are a feature of the underlying Groovy language.

`Kotlin``Groovy`

build.gradle

```
def dest = 'dest'

tasks.register('copy', Copy) {
    from 'source'
    into dest
}
```

Gradle provides extra properties for storing user-defined data on [enhanced objects](https://docs.gradle.org/current/userguide/properties_providers.html#properties_and_providers) such as `project`.

Extra properties are accessible via:

* `extra` property in Kotlin.

* `ext` property in Groovy.

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'java-library'
}

ext {
    springVersion = "3.1.0.RELEASE"
    emailNotification = "build@master.org"
}

sourceSets.all { ext.purpose = null }

sourceSets {
    main {
        purpose = "production"
    }
    test {
        purpose = "test"
    }
    plugin {
        purpose = "production"
    }
}

tasks.register('printProperties') {
    def springVersion = springVersion
    def emailNotification = emailNotification
    def productionSourceSets = provider {
        sourceSets.matching { it.purpose == "production" }.collect { it.name }
    }
    doLast {
        println springVersion
        println emailNotification
        productionSourceSets.get().each { println it }
    }
}
```

`$ gradle -q printProperties`

```
3.1.0.RELEASE
build@master.org
main
plugin
```

Gradle uses special syntax for defining extra properties to ensure fail-fast behavior. This means Gradle will immediately detect if you try to set a property that hasn’t been declared, helping you catch mistakes early.

Extra properties are attached to the object that owns them (such as `project`). Unlike local variables, extra properties have a wider scope, you can access them anywhere the owning object is visible, including from subprojects accessing their parent project’s properties.

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#line_by_line_execution)[Line-by-Line Execution](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#line_by_line_execution)

Gradle executes build scripts top to bottom during the configuration phase. That means:

1. Code is evaluated immediately in order.

2. Statements outside of configuration blocks execute eagerly.

3. Properties and logic should be deferred using `Provider` or lazy APIs when possible (more on this in the next section).

This top-down execution model means the order of declarations can affect behavior, especially when using variables or configuring tasks.

### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#example_breakdown)[Example Breakdown](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#example_breakdown)

Now, let’s take a look at an example and break it down:

`Kotlin``Groovy`

build.gradle

```
plugins {   (1)
    id 'application'
}

repositories {  (2)
    mavenCentral()
}

dependencies {  (3)
    testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.9.3'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
    implementation 'com.google.guava:guava:32.1.1-jre'
}

application {   (4)
    mainClass = 'com.example.Main'
}

tasks.named('test', Test) { (5)
    useJUnitPlatform()
}

tasks.named('javadoc', Javadoc).configure {
    exclude 'app/Internal*.java'
    exclude 'app/internal/*'
}

tasks.register('zip-reports', Zip) {
    from 'Reports/'
    include '*'
    archiveFileName = 'Reports.zip'
    destinationDirectory = file('/dir')
}
```

**1**Apply plugins to the build.
**2**Define the locations where dependencies can be found.
**3**Add dependencies.
**4**Set properties.
**5**Register and configure tasks.

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#1_apply_plugins_to_the_build)[1. Apply plugins to the build](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#1_apply_plugins_to_the_build)

Plugins are used to extend Gradle. They are also used to modularize and reuse project configurations.

Plugins can be applied using the `PluginDependenciesSpec` plugins script block.

The plugins block is preferred:

`Kotlin``Groovy`

build.gradle

```
plugins {   (1)
    id 'application'
}
```

In the example, the `application` plugin, which is included with Gradle, has been applied, describing our project as a Java application.

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#2_define_the_locations_where_dependencies_can_be_found)[2. Define the locations where dependencies can be found](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#2_define_the_locations_where_dependencies_can_be_found)

A project generally has a number of dependencies it needs to do its work. Dependencies include plugins, libraries, or components that Gradle must download for the build to succeed.

The build script lets Gradle know where to look for the binaries of the dependencies. More than one location can be provided:

`Kotlin``Groovy`

build.gradle

```
repositories {  (2)
    mavenCentral()
}
```

In the example, the `guava` library and the JetBrains Kotlin plugin (`org.jetbrains.kotlin.jvm`) will be downloaded from the [Maven Central Repository](https://repo.maven.apache.org/maven2/).

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#3_add_dependencies)[3. Add dependencies](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#3_add_dependencies)

A project generally has a number of dependencies it needs to do its work. These dependencies are often libraries of precompiled classes that are imported in the project’s source code.

Dependencies are managed via [configurations](https://docs.gradle.org/current/userguide/glossary.html#sub:terminology_configuration) and are retrieved from repositories.

Use the `DependencyHandler` returned by `Project.getDependencies()` method to manage the dependencies. Use the `RepositoryHandler` returned by `Project.getRepositories()` method to manage the repositories.

`Kotlin``Groovy`

build.gradle

```
dependencies {  (3)
    testImplementation 'org.junit.jupiter:junit-jupiter-engine:5.9.3'
    testRuntimeOnly 'org.junit.platform:junit-platform-launcher'
    implementation 'com.google.guava:guava:32.1.1-jre'
}
```

In the example, the application code uses Google’s `guava` libraries. Guava provides utility methods for collections, caching, primitives support, concurrency, common annotations, string processing, I/O, and validations.

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#4_set_properties)[4. Set properties](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#4_set_properties)

A plugin can add properties and methods to a project using extensions.

The [`Project`](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html) object has an associated [`ExtensionContainer`](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html) object that contains all the settings and properties for the plugins that have been applied to the project.

In the example, the `application` plugin added an `application` property, which is used to detail the main class of our Java application:

`Kotlin``Groovy`

build.gradle

```
application {   (4)
    mainClass = 'com.example.Main'
}
```

#### [](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#5_register_and_configure_tasks)[5. Register and configure tasks](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#5_register_and_configure_tasks)

Tasks perform some basic piece of work, such as compiling classes, or running unit tests, or zipping up a WAR file.

While tasks are typically defined in plugins, you may need to register or configure tasks in build scripts.

**Registering** a task adds the task to your project.

`Kotlin``Groovy`

build.gradle

```
tasks.register('zip-reports', Zip) {
    from 'Reports/'
    include '*'
    archiveFileName = 'Reports.zip'
    destinationDirectory = file('/dir')
}
```

`tasks.create<Zip>("zip-reports") { }`

You can locate a task to configure it using the `TaskCollection.named(java.lang.String)` method:

`Kotlin``Groovy`

build.gradle

```
tasks.named('test', Test) { (5)
    useJUnitPlatform()
}
```

The example below configures the [`Javadoc`](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.javadoc.Javadoc.html) task to automatically generate HTML documentation from Java code:

`Kotlin``Groovy`

build.gradle

```
tasks.named('javadoc', Javadoc).configure {
    exclude 'app/Internal*.java'
    exclude 'app/internal/*'
}
```

[](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#accessing_project_properties_in_build_scripts)[Accessing Project Properties in Build Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#accessing_project_properties_in_build_scripts)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In a Gradle build script, you can refer to project-level properties like `name`, `version`, or `group` without needing to qualify them with `project`:

`Kotlin``Groovy`

build.gradle

```
println name
println project.name
```

`$ gradle -q check`

```
project-api
project-api
```

This works because of how Gradle evaluates build scripts:

* In **Groovy**, Gradle dynamically delegates unqualified references like `name` to the `Project` object.

* In **Kotlin**, the build script is compiled as an extension of the `Project` type, so you can directly access its properties.

While you can always use `project.name` to be explicit, using the shorthand `name` is common and safe in most situations.

[](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#accessing_settings_properties_in_settings_scripts)[Accessing Settings Properties in Settings Scripts](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#accessing_settings_properties_in_settings_scripts)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Just like build scripts operate within a `Project` context, settings scripts (`settings.gradle(.kts)`) operate within a `Settings` context.

This means you can refer to properties and methods available on the `Settings` object, often without qualification.

For example:

```
println(rootProject.name)
println(name)
```

In a `settings.gradle(.kts)` script, both of these print the name of the root project. That’s because:

* In **Groovy**, unqualified property references like `name` are dynamically delegated to the `Settings` object.

* In **Kotlin**, the script is compiled as an extension of the `Settings` class, so `name` and `pluginManagement {}` are directly accessible.

Unlike in build scripts, where `name` refers to the current subproject, in settings scripts `name` typically refers to the **root project name**, and it can be set explicitly:

`rootProject.name = "my-awesome-project"`

[](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#default-script-imports)[Default Script Imports](https://docs.gradle.org/userguide/writing_build_scripts_intermediate.html#default-script-imports)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As a result, instead of writing `throw new org.gradle.api.tasks.StopExecutionException()`, you can write `throw new StopExecutionException()`.
