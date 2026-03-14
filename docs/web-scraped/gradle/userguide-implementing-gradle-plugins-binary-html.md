# Source: https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html

Title: Binary Plugins

URL Source: https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html

Markdown Content:
**Binary plugins** refer to plugins that are compiled and distributed as JAR files. These plugins are usually written in Java or Kotlin and provide custom functionality or tasks to a Gradle build.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin_anatomy)[Anatomy of a binary plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin_anatomy)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A typical Gradle plugin is composed of three cooperating parts:

| Part | Purpose | Notes |
| --- | --- | --- |
| Plugin class | Applies behavior to a target (`Project/Settings`), registers tasks, and wires defaults. | Implements `Plugin<Project>` (or `Plugin<Settings>`). Keeps configuration lazy; avoid doing work in apply. |
| Extension | Holds user configuration exposed as a DSL block. | Use `Property<T>`, `RegularFileProperty`, `DirectoryProperty`, and `ListProperty<T>` for laziness, validation, and Configuration Cache compatibility. |
| Task type | Implements the actual work when executed. | Model inputs/outputs with `@Input`, `@InputFile`, `@OutputFile`, etc., to enable incremental builds and caching. |

![Image 1: plugin anatomy](https://docs.gradle.org/current/userguide/img/plugin_anatomy.png)

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#example_of_a_binary_plugin)[Example of a binary plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#example_of_a_binary_plugin)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Here’s a detailed look at the project structure for a simple `Greeting` plugin:

`Kotlin``Groovy`

build.gradle

```
plugin/     (1)
├── build.gradle    (2)
└── src/
    └── main/
        └── groovy/
            └── org/
                └── example/    (3)
                    ├── GreetingPlugin.groovy
                    ├── GreetingPluginExtension.groovy
                    └── GreetingTask.groovy
```

**1****`plugin/`**: This is the root directory for the Gradle plugin project.
**2****`build.gradle`**: The build script for the plugin itself. It specifies dependencies like the Gradle API and Groovy, and it’s where you apply the `groovy-gradle-plugin` or `java-gradle-plugin` to make your code a runnable Gradle plugin.
**3****`src/main/groovy/org/example/`**: This is the standard source directory for Groovy code, organized by package name.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_plugin_class_greetingplugin_kt)[The plugin class (`GreetingPlugin.kt`)](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_plugin_class_greetingplugin_kt)

The core of the plugin is the `GreetingPlugin` class. It implements the `Plugin<Project>` interface and overrides the `apply` method, which is the entry point for your plugin’s logic:

[![Image 2: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/plugin-binary)

`Kotlin``Groovy`

plugin/src/main/groovy/org/example/GreetingPlugin.groovy

```
package org.example

import org.gradle.api.Plugin
import org.gradle.api.Project
import org.example.GreetingExtension
import org.example.GreetTask

class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        // Create extension and set sensible defaults (conventions)
        def ext = project.extensions.create("greeting", GreetingExtension)  (1)
        ext.message.convention("Hello from plugin")
        ext.outputFile.convention(project.layout.buildDirectory.file("greeting.txt"))

        // Register task and map extension -> task inputs (lazy wiring)
        project.tasks.register("greet", GreetTask) {    (2)
            group = "example"
            description = "Writes a greeting to a file"
            message.set(ext.message)
            outputFile.set(ext.outputFile)
        }
    }
}
```

**1**`project.extensions.create()`: This creates an extension named greeting. This is how users of your plugin can configure its behavior in their build.gradle file. The apply block sets convention values, which are default values that the user can override.
**2**`project.tasks.register()`: This registers a task of type GreetTask named greet. This is the action that your plugin provides.

**Lazy Wiring**: The `message.set(ext.message)` and `outputFile.set(ext.outputFile)` lines are examples of lazy wiring. The task’s inputs are not read immediately. Instead, they are connected to the extension’s properties, and the values are only resolved when the task actually runs. This is crucial for performance and correctness in Gradle builds.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_extension_greetingextension_kt)[The extension (`GreetingExtension.kt`)](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_extension_greetingextension_kt)

The extension defines the properties that a user can configure. It uses `Property` and `RegularFileProperty` types, which are designed for lazy evaluation:

[![Image 3: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/plugin-binary)

`Kotlin``Groovy`

plugin/src/main/groovy/org/example/GreetingExtension.groovy

```
package org.example

import org.gradle.api.provider.Property
import org.gradle.api.file.RegularFileProperty

abstract class GreetingExtension {
    abstract Property<String> getMessage()          (1)
    abstract RegularFileProperty getOutputFile()    (2)
}
```

**1**`Property<T>`: This is a container for a value of type T. The actual value is not read until it’s needed, which enables lazy configuration.
**2**`RegularFileProperty`: A specific type of property for file paths. Gradle uses this to track file inputs and outputs for up-to-date checks and the build cache.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_custom_task_greettask_kt)[The custom task (`GreetTask.kt`)](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#the_custom_task_greettask_kt)

This is the class for the custom task. It defines the inputs and outputs, and the action to perform:

[![Image 4: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/plugin-binary)

`Kotlin``Groovy`

plugin/src/main/groovy/org/example/GreetTask.groovy

```
package org.example

import org.gradle.api.DefaultTask
import org.gradle.api.file.RegularFileProperty
import org.gradle.api.provider.Property
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.OutputFile
import org.gradle.api.tasks.TaskAction

abstract class GreetTask extends DefaultTask {
    @Input          (1)
    abstract Property<String> getMessage()

    @OutputFile     (2)
    abstract RegularFileProperty getOutputFile()

    @TaskAction     (3)
    void run() {
        def file = getOutputFile().get().asFile
        file.parentFile.mkdirs()
        file.write(getMessage().get())
        logger.lifecycle("Wrote greeting to ${file}")
    }
}
```

**1**`@Input`: This annotation marks a property as a task input. When a task has an input, Gradle will automatically track its value. If the value changes between builds, Gradle knows the task is out-of-date and needs to be re-run.
**2**`@OutputFile`: This annotation marks a property as a task output. Gradle tracks the location of this file. If the file is missing or its contents are older than the inputs, Gradle considers the task out-of-date.
**3**`@TaskAction`: This annotation marks the method that contains the work to be done. This method is executed when the task runs.

**Up-to-Date Checks**: By properly annotating inputs and outputs, Gradle can perform up-to-date checks. If the task’s inputs and outputs haven’t changed since the last build, Gradle can skip the task entirely, which dramatically speeds up the build process.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#applying_the_plugin)[Applying the plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#applying_the_plugin)

To use this `Greeting` plugin, you need to apply the plugin in your `build.gradle(.kts)` file. This makes the plugin’s tasks and extensions available to your project:

```
plugins {
    id("org.example.greeting")
}
```

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#configuring_the_plugin)[Configuring the plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#configuring_the_plugin)

Once the plugin is applied, you can configure it using the extension you defined, which is named `greeting`. This allows you to override the default values set in the `GreetingPlugin`. Using the `greeting` extension block:

```
greeting {
    // Override the default message
    message = "Hola from my custom build"
    // Set a custom output file path
    outputFile = layout.buildDirectory.file("custom-greeting.txt")
}
```

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#running_the_task)[Running the task](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#running_the_task)

The plugin registers a task named `greet`. After applying and configuring the plugin, you can execute this task from the command line.

`$ ./gradlew greet`

Running the `greet` task will:

* Use the `message` and `outputFile` properties, either with their default values or your custom configured values.

* Write the specified message to the output file (e.g., `build/custom-greeting.txt`).

* Print a log message to the console confirming the file has been written.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin-development-plugin)[Using the Plugin Development plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin-development-plugin)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This plugin will automatically apply the [Java Plugin](https://docs.gradle.org/current/userguide/java_plugin.html#java_plugin), add the `gradleApi()` dependency to the `api` configuration, generate the required plugin descriptors in the resulting JAR file, and configure the [Plugin Marker Artifact](https://docs.gradle.org/current/userguide/plugins_intermediate.html#sec:plugin_markers) to be used when publishing.

To apply and configure the plugin, add the following code to your build file:

[![Image 5: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/customPlugin)

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'java-gradle-plugin'
}

gradlePlugin {
    plugins {
        simplePlugin {
            id = 'org.example.greeting'
            implementationClass = 'org.example.GreetingPlugin'
        }
    }
}
```

Writing and using [custom task types](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:task_groups) is recommended when developing plugins as it automatically benefits from [incremental builds](https://docs.gradle.org/current/userguide/incremental_build.html#incremental_build). As an added benefit of applying the plugin to your project, the task `validatePlugins` automatically checks for an existing input/output annotation for every public property defined in a custom task type implementation.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:creating_a_plugin_id)[Creating a plugin ID](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:creating_a_plugin_id)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Plugin IDs are meant to be globally unique, similar to Java package names (i.e., a reverse domain name). This format helps prevent naming collisions and allows grouping plugins with similar ownership.

An explicit plugin identifier simplifies applying the plugin to a project. Your plugin ID should combine components that reflect the namespace (a reasonable pointer to you or your organization) and the name of the plugin it provides. For example, if your Github account is named `foo` and your plugin is named `bar`, a suitable plugin ID might be `com.github.foo.bar`. Similarly, if the plugin was developed at the `baz` organization, the plugin ID might be `org.baz.bar`.

Plugin IDs should adhere to the following guidelines:

* May contain any alphanumeric character, '.', and '-'.

* Must contain at least one '.' character separating the namespace from the plugin’s name.

* Conventionally use a lowercase reverse domain name convention for the namespace.

* Conventionally use only lowercase characters in the name.

* `org.gradle`, `com.gradle`, and `com.gradleware` namespaces may not be used.

* Cannot start or end with a '.' character.

* Cannot contain consecutive '.' characters (i.e., '..').

A namespace that identifies ownership and a name is sufficient for a plugin ID.

When bundling multiple plugins in a single JAR artifact, adhering to the same naming conventions is recommended. This practice helps logically group related plugins.

There is no limit to the number of plugins that can be defined and registered (by different identifiers) within a single project.

The identifiers for plugins written as a class should be defined in the project’s build script containing the plugin classes. For this, the `java-gradle-plugin` needs to be applied:

[![Image 6: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginIdentifier)

`Kotlin``Groovy`

buildSrc/build.gradle

```
plugins {
    id 'java-gradle-plugin'
}

gradlePlugin {
    plugins {
        androidApplicationPlugin {
            id = 'com.android.application'
            implementationClass = 'com.android.AndroidApplicationPlugin'
        }
        androidLibraryPlugin {
            id = 'com.android.library'
            implementationClass = 'com.android.AndroidLibraryPlugin'
        }
    }
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:working_with_files_in_custom_tasks_and_plugins)[Working with files](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:working_with_files_in_custom_tasks_and_plugins)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When developing plugins, it’s a good idea to be flexible when accepting input configuration for file locations.

It is recommended to use Gradle’s [managed properties](https://docs.gradle.org/current/userguide/properties_providers.html#managed_properties) and `project.layout` to select file or directory locations. This will enable lazy configuration so that the actual location will only be resolved when the file is needed and can be reconfigured at any time during build configuration.

This Gradle build file defines a task `GreetingToFileTask` that writes a greeting to a file. It also registers two tasks: `greet`, which creates the file with the greeting, and `sayGreeting`, which prints the file’s contents. The `greetingFile` property is used to specify the file path for the greeting:

[![Image 7: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/tasks/customTaskWithFileProperty)

`Kotlin``Groovy`

build.gradle

```
abstract class GreetingToFileTask extends DefaultTask {

    @OutputFile
    abstract RegularFileProperty getDestination()

    @TaskAction
    def greet() {
        def file = getDestination().get().asFile
        file.parentFile.mkdirs()
        file.write 'Hello!'
    }
}

def greetingFile = objects.fileProperty()

tasks.register('greet', GreetingToFileTask) {
    destination = greetingFile
}

tasks.register('sayGreeting') {
    dependsOn greet
    doLast {
        def file = greetingFile.get().asFile
        println "${file.text} (file: ${file.name})"
    }
}

greetingFile = layout.buildDirectory.file('hello.txt')
```

`$ ./gradlew -q sayGreeting`

`Hello! (file: hello.txt)`

In this example, we configure the `greet` task `destination` property as a closure/provider, which is evaluated with the [Project.file(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:file(java.lang.Object)) method to turn the return value of the closure/provider into a `File` object at the last minute. Note that we specify the `greetingFile` property value _after_ the task configuration. This lazy evaluation is a key benefit of accepting any value when setting a file property and then resolving that value when reading the property.

You can learn more about working with files lazily in [Working with Files](https://docs.gradle.org/current/userguide/working_with_files.html#working_with_files).

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#capturing_user_input_to_configure_plugin_runtime_behavior)[Making a plugin configurable using extensions](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#capturing_user_input_to_configure_plugin_runtime_behavior)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most plugins offer configuration options for build scripts and other plugins to customize how the plugin works. Plugins do this using **extension objects**.

A [Project](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html) has an associated [ExtensionContainer](https://docs.gradle.org/current/javadoc/org/gradle/api/plugins/ExtensionContainer.html) object that contains all the settings and properties for the plugins that have been applied to the project. You can provide configuration for your plugin by adding an extension object to this container.

An extension object is simply an object with Java Bean properties representing the configuration.

Let’s add a `greeting` extension object to the project, which allows you to configure the greeting:

[![Image 8: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/customPlugins/customPluginNoConvention)

`Kotlin``Groovy`

build.gradle

```
interface GreetingPluginExtension {
    Property<String> getMessage()
}

class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        // Add the 'greeting' extension object
        def extension = project.extensions.create('greeting', GreetingPluginExtension)
        // Add a task that uses configuration from the extension object
        project.task('hello') {
            doLast {
                println extension.message.get()
            }
        }
    }
}

apply plugin: GreetingPlugin

// Configure the extension
greeting.message = 'Hi from Gradle'
```

`$ ./gradlew -q hello`

`Hi from Gradle`

In this example, `GreetingPluginExtension` is an object with a property called `message`. The extension object is added to the project with the name `greeting`. This object becomes available as a project property with the same name as the extension object. `the<GreetingPluginExtension>()` is equivalent to `project.extensions.getByType(GreetingPluginExtension::class.java)`.

Often, you have several related properties you need to specify on a single plugin. Gradle adds a configuration block for each extension object, so you can group settings:

[![Image 9: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/customPlugins/customPluginWithAdvancedConvention)

`Kotlin``Groovy`

build.gradle

```
interface GreetingPluginExtension {
    Property<String> getMessage()
    Property<String> getGreeter()
}

class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        def extension = project.extensions.create('greeting', GreetingPluginExtension)
        project.task('hello') {
            doLast {
                println "${extension.message.get()} from ${extension.greeter.get()}"
            }
        }
    }
}

apply plugin: GreetingPlugin

// Configure the extension using a DSL block
greeting {
    message = 'Hi'
    greeter = 'Gradle'
}
```

`$ ./gradlew -q hello`

`Hi from Gradle`

In this example, several settings can be grouped within the `configure<GreetingPluginExtension>` block. The [`configure`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#configure-java.lang.Object-groovy.lang.Closure-) function is used to configure an extension object. It provides a convenient way to set properties or apply configurations to these objects. The type used in the build script’s `configure` function (`GreetingPluginExtension`) must match the extension type. Then, when the block is executed, the receiver of the block is the extension.

In this example, several settings can be grouped within the `greeting` closure. The name of the closure block in the build script (`greeting`) must match the extension object name. Then, when the closure is executed, the fields on the extension object will be mapped to the variables within the closure based on the standard Groovy closure delegate feature.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#declaring_a_dsl_configuration_container)[Declaring a DSL configuration container](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#declaring_a_dsl_configuration_container)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using an extension object _extends_ the Gradle DSL to add a project property and DSL block for the plugin. Because an extension object is a regular object, you can provide your own DSL nested inside the plugin block by adding properties and methods to the extension object.

Let’s consider the following build script for illustration purposes.

[![Image 10: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/namedDomainObjectContainer)

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'org.myorg.server-env'
}

environments {
    dev {
        url = 'http://localhost:8080'
    }

    staging {
        url = 'http://staging.enterprise.com'
    }

    production {
        url = 'http://prod.enterprise.com'
    }
}
```

The DSL exposed by the plugin exposes a container for defining a set of environments. Each environment the user configures has an arbitrary but declarative name and is represented with its own DSL configuration block. The example above instantiates a development, staging, and production environment, including its respective URL.

Each environment must have a data representation in code to capture the values. The name of an environment is immutable and can be passed in as a constructor parameter. Currently, the only other parameter the data object stores is a URL.

The following `ServerEnvironment` object fulfills those requirements:

[![Image 11: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/namedDomainObjectContainer)

ServerEnvironment.java

```
abstract public class ServerEnvironment {
    private final String name;

    @javax.inject.Inject
    public ServerEnvironment(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    abstract public Property<String> getUrl();
}
```

It’s common for a plugin to post-process the captured values within the plugin implementation, e.g., to configure tasks:

[![Image 12: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/namedDomainObjectContainer)

ServerEnvironmentPlugin.java

```
public class ServerEnvironmentPlugin implements Plugin<Project> {
    @Override
    public void apply(final Project project) {
        ObjectFactory objects = project.getObjects();

        NamedDomainObjectContainer<ServerEnvironment> serverEnvironmentContainer =
            objects.domainObjectContainer(ServerEnvironment.class, name -> objects.newInstance(ServerEnvironment.class, name));
        project.getExtensions().add("environments", serverEnvironmentContainer);

        serverEnvironmentContainer.all(serverEnvironment -> {
            String env = serverEnvironment.getName();
            String capitalizedServerEnv = env.substring(0, 1).toUpperCase() + env.substring(1);
            String taskName = "deployTo" + capitalizedServerEnv;
            project.getTasks().register(taskName, Deploy.class, task -> task.getUrl().set(serverEnvironment.getUrl()));
        });
    }
}
```

In the example above, a deployment task is created dynamically for every user-configured environment.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#modeling_dsl_like_apis)[Modeling DSL-like APIs](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#modeling_dsl_like_apis)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

DSLs exposed by plugins should be readable and easy to understand.

For example, let’s consider the following extension provided by a plugin. In its current form, it offers a "flat" list of properties for configuring the creation of a website:

[![Image 13: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginExtension)

`Kotlin``Groovy`

build-flat.gradle

```
plugins {
    id 'org.myorg.site'
}

site {
    outputDir = layout.buildDirectory.file("mysite")
    websiteUrl = 'https://gradle.org'
    vcsUrl = 'https://github.com/gradle/gradle-site-plugin'
}
```

As the number of exposed properties grows, you should introduce a nested, more expressive structure.

The following code snippet adds a new configuration block named `siteInfo` as part of the extension. This provides a stronger indication of what those properties mean:

[![Image 14: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginExtension)

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'org.myorg.site'
}

site {
    outputDir = layout.buildDirectory.file("mysite")

    siteInfo {
        websiteUrl = 'https://gradle.org'
        vcsUrl = 'https://github.com/gradle/gradle-site-plugin'
    }
}
```

Implementing the backing objects for such an extension is simple. First, introduce a new data object for managing the properties `websiteUrl` and `vcsUrl`:

[![Image 15: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginExtension)

SiteInfo.java

```
abstract public class SiteInfo {

    abstract public Property<String> getWebsiteUrl();

    abstract public Property<String> getVcsUrl();
}
```

In the extension, create an instance of the `siteInfo` class and a method to delegate the captured values to the data instance.

To configure underlying data objects, define a parameter of type [Action](https://docs.gradle.org/current/javadoc/org/gradle/api/Action.html).

The following example demonstrates the use of `Action` in an extension definition:

[![Image 16: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginExtension)

SiteExtension.java

```
abstract public class SiteExtension {

    abstract public RegularFileProperty getOutputDir();

    @Nested
    abstract public SiteInfo getSiteInfo();

    public void siteInfo(Action<? super SiteInfo> action) {
        action.execute(getSiteInfo());
    }
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:mapping_extension_properties_to_task_properties_in_binary_plugins)[Mapping extension properties to task properties](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:mapping_extension_properties_to_task_properties_in_binary_plugins)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Plugins commonly use an extension to capture user input from the build script and map it to a custom task’s input/output properties. The build script author interacts with the extension’s DSL, while the plugin implementation handles the underlying logic:

[![Image 17: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/mappingExtension)

`Kotlin``Groovy`

app/build.gradle

```
// Extension class to capture user input
class MyExtension {
    @Input
    String inputParameter = null
}

// Custom task that uses the input from the extension
class MyCustomTask extends DefaultTask {
    @Input
    String inputParameter = null

    @TaskAction
    def executeTask() {
        println("Input parameter: $inputParameter")
    }
}

// Plugin class that configures the extension and task
class MyPlugin implements Plugin<Project> {
    void apply(Project project) {
        // Create and configure the extension
        def extension = project.extensions.create("myExtension", MyExtension)
        // Create and configure the custom task
        project.tasks.register("myTask", MyCustomTask) {
            group = "custom"
            inputParameter = extension.inputParameter
        }
    }
}
```

In this example, the `MyExtension` class defines an `inputParameter` property that can be set in the build script. The `MyPlugin` class configures this extension and uses its `inputParameter` value to configure the `MyCustomTask` task. The `MyCustomTask` task then uses this input parameter in its logic.

You can learn more about types you can use in task implementations and extensions in [Lazy Configuration](https://docs.gradle.org/current/userguide/lazy_configuration.html#lazy_configuration).

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:plugin_conventions_in_binary_plugins)[Adding default configuration with conventions](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:plugin_conventions_in_binary_plugins)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Plugins should provide sensible defaults and standards in a specific context, reducing the number of decisions users need to make. Using the `project` object, you can define default values. These are known as **conventions**.

Conventions are properties that are initialized with default values and can be overridden by the user in their build script. For example:

[![Image 18: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/customPlugins/customPluginWithConvention)

`Kotlin``Groovy`

build.gradle

```
interface GreetingPluginExtension {
    Property<String> getMessage()
}

class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        // Add the 'greeting' extension object
        def extension = project.extensions.create('greeting', GreetingPluginExtension)
        extension.message.convention('Hello from GreetingPlugin')
        // Add a task that uses configuration from the extension object
        project.task('hello') {
            doLast {
                println extension.message.get()
            }
        }
    }
}

apply plugin: GreetingPlugin
```

`$ ./gradlew -q hello`

`Hello from GreetingPlugin`

In this example, `GreetingPluginExtension` is a class that represents the convention. The message property is the convention property with a default value of 'Hello from GreetingPlugin'.

Users can override this value in their build script:

`Kotlin``Groovy`

build.gradle

```
GreetingPluginExtension {
    message = 'Custom message'
}
```

`$ ./gradlew -q hello`

`Custom message`

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#capabilities-vs-conventions)[Separating capabilities from conventions](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#capabilities-vs-conventions)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Separating capabilities from conventions in plugins allows users to choose which tasks and conventions to apply.

For example, the Java Base plugin provides un-opinionated (i.e., generic) functionality like `SourceSets`, while the Java plugin adds tasks and conventions familiar to Java developers like `classes`, `jar` or `javadoc`.

When designing your own plugins, consider developing two plugins — one for capabilities and another for conventions — to offer flexibility to users.

In the example below, `MyPlugin` contains conventions, and `MyBasePlugin` defines capabilities. Then, `MyPlugin` applies `MyBasePlugin`, this is called _plugin composition_. To apply a plugin from another one:

[![Image 19: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/capabilitiesVsConventions)

MyBasePlugin.java

```
import org.gradle.api.Plugin;
import org.gradle.api.Project;

public class MyBasePlugin implements Plugin<Project> {
    public void apply(Project project) {
        // define capabilities
    }
}
```

MyPlugin.java

```
import org.gradle.api.Plugin;
import org.gradle.api.Project;

public class MyPlugin implements Plugin<Project> {
    public void apply(Project project) {
        project.getPluginManager().apply(MyBasePlugin.class);

        // define conventions
    }
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#reacting_to_plugins)[Reacting to plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#reacting_to_plugins)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A common pattern in Gradle plugin implementations is configuring the runtime behavior of existing plugins and tasks in a build.

For example, a plugin could assume that it is applied to a Java-based project and automatically reconfigure the standard source directory:

[![Image 20: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/reactingToPlugins)

InhouseStrongOpinionConventionJavaPlugin.java

```
public class InhouseStrongOpinionConventionJavaPlugin implements Plugin<Project> {
    public void apply(Project project) {
        // Careful! Eagerly appyling plugins has downsides, and is not always recommended.
        project.getPluginManager().apply(JavaPlugin.class);
        SourceSetContainer sourceSets = project.getExtensions().getByType(SourceSetContainer.class);
        SourceSet main = sourceSets.getByName(SourceSet.MAIN_SOURCE_SET_NAME);
        main.getJava().setSrcDirs(Arrays.asList("src"));
    }
}
```

The drawback to this approach is that it automatically forces the project to apply the Java plugin, imposing a strong opinion on it (i.e., reducing flexibility and generality). In practice, the project applying the plugin might not even deal with Java code.

Instead of automatically applying the Java plugin, the plugin could react to the fact that the consuming project applies the Java plugin. Only if that is the case, then a certain configuration is applied:

[![Image 21: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/reactingToPlugins)

InhouseConventionJavaPlugin.java

```
public class InhouseConventionJavaPlugin implements Plugin<Project> {
    public void apply(Project project) {
        project.getPluginManager().withPlugin("java", javaPlugin -> {
            SourceSetContainer sourceSets = project.getExtensions().getByType(SourceSetContainer.class);
            SourceSet main = sourceSets.getByName(SourceSet.MAIN_SOURCE_SET_NAME);
            main.getJava().setSrcDirs(Arrays.asList("src"));
        });
    }
}
```

Reacting to plugins is preferred over applying plugins if there is no good reason to assume that the consuming project has the expected setup.

The same concept applies to task types:

[![Image 22: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/reactingToPlugins)

InhouseConventionWarPlugin.java

```
public class InhouseConventionWarPlugin implements Plugin<Project> {
    public void apply(Project project) {
        project.getTasks().withType(War.class).configureEach(war ->
            war.setWebXml(project.file("src/someWeb.xml")));
    }
}
```

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#reacting_to_build_features)[Reacting to build features](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#reacting_to_build_features)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Plugins can access the status of build features in the build. The [Build Features API](https://docs.gradle.org/current/javadoc/org/gradle/api/configuration/BuildFeatures.html) allows checking whether the user requested a particular Gradle feature and if it is active in the current build. An example of a build feature is the [configuration cache](https://docs.gradle.org/current/userguide/configuration_cache.html#config_cache).

There are two main use cases:

* Using the status of build features in reports or statistics.

* Incrementally adopting experimental Gradle features by disabling incompatible plugin functionality.

Below is an example of a plugin that utilizes both of the cases.

[![Image 23: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/reactingToBuildFeatures)

Reacting to build features

```
public abstract class MyPlugin implements Plugin<Project> {

    @Inject
    protected abstract BuildFeatures getBuildFeatures(); (1)

    @Override
    public void apply(Project p) {
        BuildFeatures buildFeatures = getBuildFeatures();

        Boolean configCacheRequested = buildFeatures.getConfigurationCache().getRequested() (2)
            .getOrNull(); // could be null if user did not opt in nor opt out
        String configCacheUsage = describeFeatureUsage(configCacheRequested);
        MyReport myReport = new MyReport();
        myReport.setConfigurationCacheUsage(configCacheUsage);

        boolean isolatedProjectsActive = buildFeatures.getIsolatedProjects().getActive() (3)
            .get(); // the active state is always defined
        if (!isolatedProjectsActive) {
            myOptionalPluginLogicIncompatibleWithIsolatedProjects();
        }
    }

    private String describeFeatureUsage(Boolean requested) {
        return requested == null ? "no preference" : requested ? "opt-in" : "opt-out";
    }

    private void myOptionalPluginLogicIncompatibleWithIsolatedProjects() {
    }
}
```

**1**The `BuildFeatures` service can be injected into plugins, tasks, and other managed types.
**2**Accessing the `requested` status of a feature for reporting.
**3**Using the `active` status of a feature to disable incompatible functionality.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#build_feature_properties)[Build feature properties](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#build_feature_properties)

A `BuildFeature` status properties are represented with `Provider<Boolean>` types.

The [`BuildFeature.getRequested()`](https://docs.gradle.org/current/javadoc/org/gradle/api/configuration/BuildFeature.html#getRequested--) status of a build feature determines if the user requested to enable or disable the feature.

When the `requested` provider value is:

* `true` — the user opted in for using the feature

* `false` — the user opted out from using the feature

* `undefined` — the user neither opted in nor opted out from using the feature

The [`BuildFeature.getActive()`](https://docs.gradle.org/current/javadoc/org/gradle/api/configuration/BuildFeature.html#getActive--) status of a build feature is always defined. It represents the effective state of the feature in the build.

When the `active` provider value is:

* `true` — the feature _may_ affect the build behavior in a way specific to the feature

* `false` — the feature will not affect the build behavior

Note that the `active` status does not depend on the `requested` status. Even if the user requests a feature, it may still not be active due to other build options being used in the build. Gradle can also activate a feature by default, even if the user did not specify a preference.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#custom_dependencies_blocks)[Using a custom `dependencies` block](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#custom_dependencies_blocks)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A plugin can provide dependency declarations in custom blocks that allow users to declare dependencies in a type-safe and context-aware way.

For instance, instead of users needing to know and use the underlying `Configuration` name to add dependencies, a custom `dependencies` block lets the plugin pick a meaningful name that can be used consistently.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#adding_a_custom_dependencies_block)[Adding a custom `dependencies` block](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#adding_a_custom_dependencies_block)

To add a custom `dependencies` block, you need to create a new [type](https://docs.gradle.org/current/userguide/properties_providers.html#properties_and_providers) that will represent the set of dependency scopes available to users. That new type needs to be accessible from a part of your plugin (from a domain object or extension). Finally, the dependency scopes need to be wired back to underlying `Configuration` objects that will be used during dependency resolution.

#### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#2_add_accessors_for_dependency_scopes)[2. Add accessors for dependency scopes](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#2_add_accessors_for_dependency_scopes)

For each dependency scope your plugin wants to support, add a getter method that returns a `DependencyCollector`.

[![Image 24: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/dependenciesBlock)

#### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#3_add_accessors_for_custom_dependencies_block)[3. Add accessors for custom `dependencies` block](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#3_add_accessors_for_custom_dependencies_block)

To make the custom `dependencies` block configurable, the plugin needs to add a `getDependencies` method that returns the new type from above and a configurable block method named `dependencies`.

By convention, the accessors for your custom `dependencies` block should be called `getDependencies()`/`dependencies(Action)`. This method could be named something else, but users would need to know that a different block can behave like a `dependencies` block.

[![Image 25: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/dependenciesBlock)

#### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#4_wire_dependency_scope_to_configuration)[4. Wire dependency scope to `Configuration`](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#4_wire_dependency_scope_to_configuration)

Finally, the plugin needs to wire the custom `dependencies` block to some underlying `Configuration` objects. If this is not done, none of the dependencies declared in the custom block will be available to dependency resolution.

[![Image 26: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/dependenciesBlock)

In this example, the name users will use to add dependencies is "implementation", but the underlying `Configuration` is named `exampleImplementation`.

[![Image 27: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/plugins/dependenciesBlock)

`Kotlin``Groovy`

build.gradle

```
example {
    dependencies {
        implementation("junit:junit:4.13")
    }
}
```

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:differences_with_top_level_dependencies)[Differences between the custom `dependencies` and the top-level `dependencies` blocks](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#sec:differences_with_top_level_dependencies)

Each dependency scope returns a [`DependencyCollector`](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyCollector.html) that provides strongly-typed methods to add and configure dependencies.

There is also a [`DependencyFactory`](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyFactory.html) with factory methods to create new dependencies from different notations. Dependencies can be created lazily using these factory methods, as shown below.

A custom `dependencies` block differs from the top-level `dependencies` block in the following ways:

* Dependencies must be declared using a `String`, an instance of `Dependency`, a `FileCollection`, a `Provider` of `Dependency`, or a `ProviderConvertible` of `MinimalExternalModuleDependency`.

* Outside of Gradle build scripts, you must explicitly call a getter for the `DependencyCollector` and `add`.

  * `dependencies.add("implementation", x)` becomes `getImplementation().add(x)`

* You cannot add a dependency with an instance of `Project`. You must turn it into a `ProjectDependency` first.

* You cannot add version catalog bundles directly. Instead, use the `bundle` method on each configuration.

  * Kotlin and Groovy: `implementation(libs.bundles.testing)` becomes `implementation.bundle(libs.bundles.testing)`

* You cannot use providers for non-`Dependency` types directly. Instead, map them to a `Dependency` using the `DependencyFactory`.

  * Kotlin and Groovy: `implementation(myStringProvider)` becomes `implementation(myStringProvider.map { dependencyFactory.create(it) })`

  * Java: `implementation(myStringProvider)` becomes `getImplementation().add(myStringProvider.map(getDependencyFactory()::create)`

* Unlike the top-level `dependencies` block, constraints are not in a separate block.

  * Instead, constraints are added by decorating a dependency with `constraint(…​)` like `implementation(constraint("org:foo:1.0"))`.

Keep in mind that the `dependencies` block may not provide access to the same methods as the [top-level `dependencies` block](https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.dsl.DependencyHandler.html).

Plugins should prefer adding dependencies via their own `dependencies` block.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#providing_default_dependencies)[Providing default dependencies](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#providing_default_dependencies)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The implementation of a plugin sometimes requires the use of an external dependency.

You might want to automatically download an artifact using Gradle’s dependency management mechanism and later use it in the action of a task type declared in the plugin. Ideally, the plugin implementation does not need to ask the user for the coordinates of that dependency - it can simply predefine a sensible default version.

[![Image 28: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/defaultDependency)

DataProcessingPlugin.java

```
public class DataProcessingPlugin implements Plugin<Project> {
    public void apply(Project project) {
        Configuration dataFiles = project.getConfigurations().create("dataFiles", c -> {
            c.setVisible(false);
            c.setCanBeConsumed(false);
            c.setCanBeResolved(true);
            c.setDescription("The data artifacts to be processed for this plugin.");
            c.defaultDependencies(d -> d.add(project.getDependencies().create("org.myorg:data:1.4.6")));
        });

        project.getTasks().withType(DataProcessing.class).configureEach(
            dataProcessing -> dataProcessing.getDataFiles().from(dataFiles));
    }
}
```

DataProcessing.java

```
abstract public class DataProcessing extends DefaultTask {

    @InputFiles
    abstract public ConfigurableFileCollection getDataFiles();

    @TaskAction
    public void process() {
        System.out.println(getDataFiles().getFiles());
    }
}
```

This approach is convenient for the end user as there is no need to actively declare a dependency. The plugin already provides all the details about this implementation.

But what if the user wants to redefine the default dependency?

No problem. The plugin also exposes the custom configuration that can be used to assign a different dependency. Effectively, the default dependency is overwritten:

[![Image 29: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/defaultDependency)

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'org.myorg.data-processing'
}

dependencies {
    dataFiles 'org.myorg:more-data:2.6'
}
```

You will find that this pattern works well for tasks that require an external dependency when the task’s action is executed. You can go further and abstract the version to be used for the external dependency by exposing an extension property (e.g. `toolVersion` in [the JaCoCo plugin](https://docs.gradle.org/current/dsl/org.gradle.testing.jacoco.plugins.JacocoPluginExtension.html)).

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#minimizing_the_use_of_external_libraries)[Minimizing the use of external libraries](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#minimizing_the_use_of_external_libraries)

Using external libraries in your Gradle projects can bring great convenience, but be aware that they can introduce complex dependency graphs. Gradle’s `buildEnvironment` task can help you visualize these dependencies, including those of your plugins. Keep in mind that plugins share the same classloader, so conflicts may arise with different versions of the same library.

To demonstrate let’s assume the following build script:

[![Image 30: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/externalLibraries)

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'org.asciidoctor.jvm.convert' version '4.0.2'
}
```

The output of the task clearly indicates the classpath of the `classpath` configuration:

`$ ./gradlew buildEnvironment`

```
> Task :buildEnvironment

------------------------------------------------------------
Root project 'external-libraries'
------------------------------------------------------------

classpath
\--- org.asciidoctor.jvm.convert:org.asciidoctor.jvm.convert.gradle.plugin:4.0.2
     \--- org.asciidoctor:asciidoctor-gradle-jvm:4.0.2
          +--- org.ysb33r.gradle:grolifant-rawhide:3.0.0
          |    \--- org.tukaani:xz:1.6
          +--- org.ysb33r.gradle:grolifant-herd:3.0.0
          |    +--- org.tukaani:xz:1.6
          |    +--- org.ysb33r.gradle:grolifant40:3.0.0
          |    |    +--- org.tukaani:xz:1.6
          |    |    +--- org.apache.commons:commons-collections4:4.4
          |    |    +--- org.ysb33r.gradle:grolifant-core:3.0.0
          |    |    |    +--- org.tukaani:xz:1.6
          |    |    |    +--- org.apache.commons:commons-collections4:4.4
          |    |    |    \--- org.ysb33r.gradle:grolifant-rawhide:3.0.0 (*)
          |    |    \--- org.ysb33r.gradle:grolifant-rawhide:3.0.0 (*)
          |    +--- org.ysb33r.gradle:grolifant50:3.0.0
          |    |    +--- org.tukaani:xz:1.6
          |    |    +--- org.ysb33r.gradle:grolifant40:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    |    \--- org.ysb33r.gradle:grolifant40-legacy-api:3.0.0
          |    |         +--- org.tukaani:xz:1.6
          |    |         +--- org.apache.commons:commons-collections4:4.4
          |    |         +--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    |         \--- org.ysb33r.gradle:grolifant40:3.0.0 (*)
          |    +--- org.ysb33r.gradle:grolifant60:3.0.0
          |    |    +--- org.tukaani:xz:1.6
          |    |    +--- org.ysb33r.gradle:grolifant40:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant50:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    |    \--- org.ysb33r.gradle:grolifant-rawhide:3.0.0 (*)
          |    +--- org.ysb33r.gradle:grolifant70:3.0.0
          |    |    +--- org.tukaani:xz:1.6
          |    |    +--- org.ysb33r.gradle:grolifant40:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant50:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant60:3.0.0 (*)
          |    |    \--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    +--- org.ysb33r.gradle:grolifant80:3.0.0
          |    |    +--- org.tukaani:xz:1.6
          |    |    +--- org.ysb33r.gradle:grolifant40:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant50:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant60:3.0.0 (*)
          |    |    +--- org.ysb33r.gradle:grolifant70:3.0.0 (*)
          |    |    \--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    +--- org.ysb33r.gradle:grolifant-core:3.0.0 (*)
          |    \--- org.ysb33r.gradle:grolifant-rawhide:3.0.0 (*)
          +--- org.asciidoctor:asciidoctor-gradle-base:4.0.2
          |    \--- org.ysb33r.gradle:grolifant-herd:3.0.0 (*)
          \--- org.asciidoctor:asciidoctorj-api:2.5.7

(*) - Indicates repeated occurrences of a transitive dependency subtree. Gradle expands transitive dependency subtrees only once per project; repeat occurrences only display the root of the subtree, followed by this annotation.

A web-based, searchable dependency report is available by adding the --scan option.

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

A Gradle plugin does not run in its own, isolated classloader, so you must consider whether you truly need a library or if a simpler solution suffices.

For logic that is executed as part of task execution, use the [Worker API](https://docs.gradle.org/current/userguide/worker_api.html#tasks_parallel_worker) that allows you to isolate libraries.

[](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin-with-variants)[Providing multiple variants of a plugin](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin-with-variants)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Variants of a plugin refer to different flavors or configurations of the plugin that are tailored to specific needs or use cases. These variants can include different implementations, extensions, or configurations of the base plugin.

The most convenient way to configure additional plugin variants is to use [feature variants](https://docs.gradle.org/current/userguide/how_to_create_feature_variants_of_a_library.html#feature_variants), a concept available in all Gradle projects that apply one of the Java plugins:

```
dependencies {
    implementation 'com.google.guava:guava:30.1-jre'        // Regular dependency
    featureVariant 'com.google.guava:guava-gwt:30.1-jre'    // Feature variant dependency
}
```

In the following example, each plugin variant is developed in isolation. A separate source set is compiled and packaged in a separate jar for each variant.

The following sample demonstrates how to add a variant that is compatible with Gradle 7.0+ while the "main" variant is compatible with older versions:

[![Image 31: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginWithVariants)

`Kotlin``Groovy`

build.gradle

```
def gradle7 = sourceSets.create('gradle7')

java {
    registerFeature(gradle7.name) {
        usingSourceSet(gradle7)
        capability(project.group.toString(), project.name, project.version.toString()) (1)
    }
}

configurations.configureEach {
    if (canBeConsumed && name.startsWith(gradle7.name))  {
        attributes {
            attribute(GradlePluginApiVersion.GRADLE_PLUGIN_API_VERSION_ATTRIBUTE, (2)
                      objects.named(GradlePluginApiVersion, '7.0'))
        }
    }
}

tasks.named(gradle7.processResourcesTaskName) { (3)
    def copyPluginDescriptors = rootSpec.addChild()
    copyPluginDescriptors.into('META-INF/gradle-plugins')
    copyPluginDescriptors.from(tasks.pluginDescriptors)
}

dependencies {
    gradle7CompileOnly(gradleApi()) (4)
}
```

Only Gradle versions 7 or higher can be explicitly targeted by a variant, as support for this was only added in Gradle 7.

First, we declare a separate _source set_ and a _feature variant_ for our Gradle 7 plugin variant. Then, we do some specific wiring to turn the feature into a proper Gradle plugin variant:

Note that there is currently no convenient way to access the API of other Gradle versions as the one you are building the plugin with. Ideally, every variant should be able to declare a dependency on the API of the minimal Gradle version it supports. This will be improved in the future.

The above snippet assumes that all variants of your plugin have the plugin class at the same location. That is, if your plugin class is `org.example.GreetingPlugin`, you need to create a second variant of that class in `src/gradle7/java/org/example`.

### [](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#using_version_specific_variants_of_multi_variant_plugins)[Using version-specific variants of multi-variant plugins](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#using_version_specific_variants_of_multi_variant_plugins)

Given a dependency on a multi-variant plugin, Gradle will automatically choose its variant that best matches the current Gradle version when it resolves any of:

* plugins specified in the [`plugins {}` block](https://docs.gradle.org/current/userguide/plugins_intermediate.html#sec:plugins_block);

* `buildscript` classpath dependencies;

* dependencies in the root project of the [build source (`buildSrc`)](https://docs.gradle.org/current/userguide/sharing_build_logic_between_subprojects.html#sec:using_buildsrc) that appear on the compile or runtime classpath;

* dependencies in a project that applies the [Java Gradle Plugin Development plugin](https://docs.gradle.org/current/userguide/java_gradle_plugin.html#java_gradle_plugin) or the [Kotlin DSL plugin](https://docs.gradle.org/current/userguide/kotlin_dsl.html#sec:kotlin-dsl_plugin), appearing on the compile or runtime classpath.

The best matching variant is the variant that targets the highest Gradle API version and does not exceed the current build’s Gradle version.

In all other cases, a plugin variant that does not specify the supported Gradle API version is preferred if such a variant is present.

In projects that use plugins as dependencies, requesting the variants of plugin dependencies that support a different Gradle version is possible. This allows a multi-variant plugin that depends on other plugins to access their APIs, which are exclusively provided in their version-specific variants.

This snippet makes the [plugin variant `gradle7` defined above](https://docs.gradle.org/userguide/implementing_gradle_plugins_binary.html#plugin-with-variants) consume the matching variants of its dependencies on other multi-variant plugins:

[![Image 32: View full sample project on GitHub](https://img.shields.io/badge/View%20full%20project-GitHub-blue?logo=github&style=flat)](https://github.com/gradle/gradle/tree/master/platforms/documentation/docs/src/snippets/developingPlugins/pluginWithVariants)

`Kotlin``Groovy`

build.gradle

```
configurations.configureEach {
    if (canBeResolved && name.startsWith(gradle7.name))  {
        attributes {
            attribute(GradlePluginApiVersion.GRADLE_PLUGIN_API_VERSION_ATTRIBUTE,
                objects.named(GradlePluginApiVersion, '7.0'))
        }
    }
}
```
