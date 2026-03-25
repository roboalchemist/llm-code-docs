# Source: https://docs.gradle.org/userguide/lazy_configuration.html

Title: Configuring Tasks Lazily

URL Source: https://docs.gradle.org/userguide/lazy_configuration.html

Markdown Content:
Knowing when and where a particular value is configured is difficult to track as a build grows in complexity. Gradle provides several ways to manage this using **lazy configuration**.

![Image 1: writing tasks 4](https://docs.gradle.org/current/userguide/img/writing-tasks-4.png)

[](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_properties)[Understanding Lazy properties](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_properties)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle provides lazy properties, which delay calculating a property’s value until it’s actually required.

Lazy properties provide three main benefits:

1. **Deferred Value Resolution:** Allows wiring Gradle models without needing to know when a property’s value will be known. For example, you may want to set the input source files of a task based on the source directories property of an extension, but the extension property value isn’t known until the build script or some other plugin configures them.

2. **Automatic Task Dependency Management:** Connects output of one task to input of another, automatically determining task dependencies. Property instances carry information about which task, if any, produces their value. Build authors do not need to worry about keeping task dependencies in sync with configuration changes.

3. **Improved Build Performance:** Avoids resource-intensive work during configuration, impacting build performance positively. For example, when a configuration value comes from parsing a file but is only used when functional tests are run, using a property instance to capture this means that the file is parsed only when the functional tests are run (and not when `clean` is run, for example).

Gradle represents lazy properties with two interfaces:

[Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html)
Represents a value that can only be queried and cannot be changed.

* Properties with these types are read-only.

* The method [Provider.get()](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#get--) returns the current value of the property.

* A `Provider` can be created from another `Provider` using [Provider.map(Transformer)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#map-org.gradle.api.Transformer-).

* Many other types extend `Provider` and can be used wherever a `Provider` is required.

[Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html)
Represents a value that can be queried and changed.

* Properties with these types are configurable.

* `Property` extends the `Provider` interface.

* The method [Property.set(T)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#set-T-) specifies a value for the property, overwriting whatever value may have been present.

* The method [Property.set(Provider)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#set-org.gradle.api.provider.Provider-) specifies a `Provider` for the value for the property, overwriting whatever value may have been present. This allows you to wire together `Provider` and `Property` instances before the values are configured.

* A `Property` can be created by the factory method [ObjectFactory.property(Class)](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#property-java.lang.Class-).

Lazy properties are intended to be passed around and only queried when required. This typically happens during the [execution phase](https://docs.gradle.org/current/userguide/build_lifecycle.html#build_phases).

The following demonstrates a task with a configurable `greeting` property and a read-only `message` property:

`Kotlin``Groovy`

build.gradle

```
abstract class Greeting extends DefaultTask { (1)
    @Input
    abstract Property<String> getGreeting() (2)

    @Internal
    final Provider<String> message = greeting.map { it + ' from Gradle' } (3)

    @TaskAction
    void printMessage() {
        logger.quiet(message.get())
    }
}

tasks.register("greeting", Greeting) {
    greeting.set('Hi') (4)
    greeting = 'Hi' (5)
}
```

**1**A task that displays a greeting
**2**A configurable greeting
**3**Read-only property calculated from the greeting
**4**Configure the greeting
**5**Alternative notation to calling Property.set()

`$ ./gradlew greeting`

```
> Task :greeting
Hi from Gradle

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

The `Greeting` task has a property of type `Property<String>` to represent the configurable greeting and a property of type `Provider<String>` to represent the calculated, read-only, message. The message `Provider` is created from the greeting `Property` using the `map()` method; its value is kept up-to-date as the value of the greeting property changes.

[](https://docs.gradle.org/userguide/lazy_configuration.html#creating_property_provider)[Creating a Property or Provider instance](https://docs.gradle.org/userguide/lazy_configuration.html#creating_property_provider)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Neither `Provider` nor its subtypes, such as `Property`, are intended to be implemented by a build script or plugin. Gradle provides factory methods to create instances of these types instead.

In the previous example, two factory methods were presented:

* [ObjectFactory.property(Class)](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#property-java.lang.Class-) create a new `Property` instance. An instance of the [ObjectFactory](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html) can be referenced from [Project.getObjects()](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#getObjects--) or by injecting `ObjectFactory` through a constructor or method.

* [Provider.map(Transformer)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#map-org.gradle.api.Transformer-) creates a new `Provider` from an existing `Provider` or `Property` instance.

See the [Quick Reference](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration_reference) for all of the types and factories available.

There are no specific methods to create a provider using a `groovy.lang.Closure`.

When writing a plugin or build script with Groovy, you can use the `map(Transformer)` method with a closure, and Groovy will convert the closure to a `Transformer`.

Similarly, when writing a plugin or build script with Kotlin, the Kotlin compiler will convert a Kotlin function into a `Transformer`.

[](https://docs.gradle.org/userguide/lazy_configuration.html#connecting_properties_together)[Connecting properties together](https://docs.gradle.org/userguide/lazy_configuration.html#connecting_properties_together)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An important feature of lazy properties is that they can be connected together so that changes to one property are automatically reflected in other properties.

Here is an example where the property of a task is connected to a property of a project extension:

`Kotlin``Groovy`

build.gradle

```
// A project extension
interface MessageExtension {
    // A configurable greeting
    Property<String> getGreeting()
}

// A task that displays a greeting
abstract class Greeting extends DefaultTask {
    // Configurable by the user
    @Input
    abstract Property<String> getGreeting()

    // Read-only property calculated from the greeting
    @Internal
    final Provider<String> message = greeting.map { it + ' from Gradle' }

    @TaskAction
    void printMessage() {
        logger.quiet(message.get())
    }
}

// Create the project extension
project.extensions.create('messages', MessageExtension)

// Create the greeting task
tasks.register("greeting", Greeting) {
    // Attach the greeting from the project extension
    // Note that the values of the project extension have not been configured yet
    greeting = messages.greeting
}

messages {
    // Configure the greeting on the extension
    // Note that there is no need to reconfigure the task's `greeting` property. This is automatically updated as the extension property changes
    greeting = 'Hi'
}
```

`$ ./gradlew greeting`

```
> Task :greeting
Hi from Gradle

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

This example calls the [Property.set(Provider)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#set-org.gradle.api.provider.Provider-) method to attach a `Provider` to a `Property` to supply the value of the property. In this case, the `Provider` happens to be a `Property` as well, but you can connect any `Provider` implementation, for example one created using `Provider.map()`

[](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_files_in_lazy_properties)[Working with files](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_files_in_lazy_properties)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In [Working with Files](https://docs.gradle.org/current/userguide/working_with_files.html#working_with_files), we introduced four collection types for `File`-like objects:

| Read-only Type | Configurable Type |
| --- | --- |
| [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html) | [ConfigurableFileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ConfigurableFileCollection.html) |
| [FileTree](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTree.html) | [ConfigurableFileTree](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ConfigurableFileTree.html) |

Avoid using `FileTree` when order matters — it has no guaranteed, stable file order and may cause unpredictable behavior.

All of these types are also considered lazy types.

There are more strongly typed models used to represent elements of the file system: [Directory](https://docs.gradle.org/current/javadoc/org/gradle/api/file/Directory.html) and [RegularFile](https://docs.gradle.org/current/javadoc/org/gradle/api/file/RegularFile.html). These types shouldn’t be confused with the standard Java [File](https://docs.oracle.com/en/java/javase/17/docs/api//java/io/File.html) type as they are used to tell Gradle that you expect more specific values such as a directory or a non-directory, regular file.

A `DirectoryProperty` can also be used to create a lazily evaluated `Provider` for a `Directory` and `RegularFile` via [DirectoryProperty.dir(String)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html#dir-java.lang.String-) and [DirectoryProperty.file(String)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/DirectoryProperty.html#file-java.lang.String-) respectively. These methods create providers whose values are calculated relative to the location for the `DirectoryProperty` they were created from. The values returned from these providers will reflect changes to the `DirectoryProperty`.

`Kotlin``Groovy`

build.gradle

```
// A task that generates a source file and writes the result to an output directory
abstract class GenerateSource extends DefaultTask {
    // The configuration file to use to generate the source file
    @InputFile
    abstract RegularFileProperty getConfigFile()

    // The directory to write source files to
    @OutputDirectory
    abstract DirectoryProperty getOutputDir()

    @TaskAction
    def compile() {
        def inFile = configFile.get().asFile
        logger.quiet("configuration file = $inFile")
        def dir = outputDir.get().asFile
        logger.quiet("output dir = $dir")
        def className = inFile.text.trim()
        def srcFile = new File(dir, "${className}.java")
        srcFile.text = "public class ${className} { ... }"
    }
}

// Create the source generation task
tasks.register('generate', GenerateSource) {
    // Configure the locations, relative to the project and build directories
    configFile = layout.projectDirectory.file('src/config.txt')
    outputDir = layout.buildDirectory.dir('generated-source')
}

// Change the build directory
// Don't need to reconfigure the task properties. These are automatically updated as the build directory changes
layout.buildDirectory = layout.projectDirectory.dir('output')
```

`$ gradle generate`

```
> Task :generate
configuration file = /home/user/gradle/samples/kotlin/src/config.txt
output dir = /home/user/gradle/samples/kotlin/output/generated-source

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

`$ gradle generate`

```
> Task :generate
configuration file = /home/user/gradle/samples/src/config.txt
output dir = /home/user/gradle/samples/output/generated-source

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

[](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_task_dependencies_in_lazy_properties)[Working with task inputs and outputs](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_task_dependencies_in_lazy_properties)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many builds have several tasks connected together, where one task consumes the outputs of another task as an input.

To make this work, we need to configure each task to know where to look for its inputs and where to place its outputs. Ensure that the producing and consuming tasks are configured with the same location and attach task dependencies between the tasks. This can be cumbersome and brittle if any of these values are configurable by a user or configured by multiple plugins, as task properties need to be configured in the correct order and locations, and task dependencies kept in sync as values change.

The `Property` API makes this easier by keeping track of the value of a property and the task that produces the value.

As an example, consider the following plugin with a producer and consumer task which are wired together:

`Kotlin``Groovy`

build.gradle

```
abstract class Producer extends DefaultTask {
    @OutputFile
    abstract RegularFileProperty getOutputFile()

    @TaskAction
    void produce() {
        String message = 'Hello, World!'
        def output = outputFile.get().asFile
        output.text = message
        logger.quiet("Wrote '${message}' to ${output}")
    }
}

abstract class Consumer extends DefaultTask {
    @InputFile
    abstract RegularFileProperty getInputFile()

    @TaskAction
    void consume() {
        def input = inputFile.get().asFile
        def message = input.text
        logger.quiet("Read '${message}' from ${input}")
    }
}

def producer = tasks.register("producer", Producer)
def consumer = tasks.register("consumer", Consumer)

consumer.configure {
    // Connect the producer task output to the consumer task input
    // Don't need to add a task dependency to the consumer task. This is automatically added
    inputFile = producer.flatMap { it.outputFile }
}

producer.configure {
    // Set values for the producer lazily
    // Don't need to update the consumer.inputFile property. This is automatically updated as producer.outputFile changes
    outputFile = layout.buildDirectory.file('file.txt')
}

// Change the build directory.
// Don't need to update producer.outputFile and consumer.inputFile. These are automatically updated as the build directory changes
layout.buildDirectory = layout.projectDirectory.dir('output')
```

`$ ./gradlew consumer`

```
> Task :producer
Wrote 'Hello, World!' to /home/user/gradle/samples/kotlin/output/file.txt

> Task :consumer
Read 'Hello, World!' from /home/user/gradle/samples/kotlin/output/file.txt

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

`$ ./gradlew consumer`

```
> Task :producer
Wrote 'Hello, World!' to /home/user/gradle/samples/output/file.txt

> Task :consumer
Read 'Hello, World!' from /home/user/gradle/samples/output/file.txt

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

In the example above, the task outputs and inputs are connected before any location is defined. The setters can be called at any time before the task is executed, and the change will automatically affect all related input and output properties.

Another important thing to note in this example is the absence of any explicit task dependency. Task outputs represented using `Providers` keep track of which task produces their value, and using them as task inputs will implicitly add the correct task dependencies.

Implicit task dependencies also work for input properties that are not files:

`Kotlin``Groovy`

build.gradle

```
abstract class Producer extends DefaultTask {
    @OutputFile
    abstract RegularFileProperty getOutputFile()

    @TaskAction
    void produce() {
        String message = 'Hello, World!'
        def output = outputFile.get().asFile
        output.text = message
        logger.quiet("Wrote '${message}' to ${output}")
    }
}

abstract class Consumer extends DefaultTask {
    @Input
    abstract Property<String> getMessage()

    @TaskAction
    void consume() {
        logger.quiet(message.get())
    }
}

def producer = tasks.register('producer', Producer) {
    // Set values for the producer lazily
    // Don't need to update the consumer.inputFile property. This is automatically updated as producer.outputFile changes
    outputFile = layout.buildDirectory.file('file.txt')
}
tasks.register('consumer', Consumer) {
    // Connect the producer task output to the consumer task input
    // Don't need to add a task dependency to the consumer task. This is automatically added
    message = producer.flatMap { it.outputFile }.map { it.asFile.text }
}
```

`$ ./gradlew consumer`

```
> Task :producer
Wrote 'Hello, World!' to /home/user/gradle/samples/kotlin/build/file.txt

> Task :consumer
Hello, World!

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

`$ ./gradlew consumer`

```
> Task :producer
Wrote 'Hello, World!' to /home/user/gradle/samples/build/file.txt

> Task :consumer
Hello, World!

BUILD SUCCESSFUL in 0s
2 actionable tasks: 2 executed
```

[](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_collections)[Working with collections](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_collections)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle provides two lazy property types to help configure `Collection` properties.

These work exactly like any other `Provider` and, just like file providers, they have additional modeling around them:

* For `List` values the interface is called [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html).

 You can create a new `ListProperty` using [ObjectFactory.listProperty(Class)](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#listProperty-java.lang.Class-) and specifying the element type.

* For `Set` values the interface is called [SetProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/SetProperty.html).

 You can create a new `SetProperty` using [ObjectFactory.setProperty(Class)](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#setProperty-java.lang.Class-) and specifying the element type.

* [HasMultipleValues.add(T)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/HasMultipleValues.html#add-T-): Add a single element to the collection

* [HasMultipleValues.add(Provider)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/HasMultipleValues.html#add-org.gradle.api.provider.Provider-): Add a lazily calculated element to the collection

* [HasMultipleValues.addAll(Provider)](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/HasMultipleValues.html#addAll-org.gradle.api.provider.Provider-): Add a lazily calculated collection of elements to the list

Just like every `Provider`, the collection is calculated when [Provider.get()](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html#get--) is called. The following example shows the [ListProperty](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/ListProperty.html) in action:

`Kotlin``Groovy`

build.gradle

```
abstract class Producer extends DefaultTask {
    @OutputFile
    abstract RegularFileProperty getOutputFile()

    @TaskAction
    void produce() {
        String message = 'Hello, World!'
        def output = outputFile.get().asFile
        output.text = message
        logger.quiet("Wrote '${message}' to ${output}")
    }
}

abstract class Consumer extends DefaultTask {
    @InputFiles
    abstract ListProperty<RegularFile> getInputFiles()

    @TaskAction
    void consume() {
        inputFiles.get().each { inputFile ->
            def input = inputFile.asFile
            def message = input.text
            logger.quiet("Read '${message}' from ${input}")
        }
    }
}

def producerOne = tasks.register('producerOne', Producer)
def producerTwo = tasks.register('producerTwo', Producer)
tasks.register('consumer', Consumer) {
    // Connect the producer task outputs to the consumer task input
    // Don't need to add task dependencies to the consumer task. These are automatically added
    inputFiles.add(producerOne.get().outputFile)
    inputFiles.add(producerTwo.get().outputFile)
}

// Set values for the producer tasks lazily
// Don't need to update the consumer.inputFiles property. This is automatically updated as producer.outputFile changes
producerOne.configure { outputFile = layout.buildDirectory.file('one.txt') }
producerTwo.configure { outputFile = layout.buildDirectory.file('two.txt') }

// Change the build directory.
// Don't need to update the task properties. These are automatically updated as the build directory changes
layout.buildDirectory = layout.projectDirectory.dir('output')
```

`$ ./gradlew consumer`

```
> Task :producerOne
Wrote 'Hello, World!' to /home/user/gradle/samples/kotlin/output/one.txt

> Task :producerTwo
Wrote 'Hello, World!' to /home/user/gradle/samples/kotlin/output/two.txt

> Task :consumer
Read 'Hello, World!' from /home/user/gradle/samples/kotlin/output/one.txt
Read 'Hello, World!' from /home/user/gradle/samples/kotlin/output/two.txt

BUILD SUCCESSFUL in 0s
3 actionable tasks: 3 executed
```

`$ ./gradlew consumer`

```
> Task :producerOne
Wrote 'Hello, World!' to /home/user/gradle/samples/output/one.txt

> Task :producerTwo
Wrote 'Hello, World!' to /home/user/gradle/samples/output/two.txt

> Task :consumer
Read 'Hello, World!' from /home/user/gradle/samples/output/one.txt
Read 'Hello, World!' from /home/user/gradle/samples/output/two.txt

BUILD SUCCESSFUL in 0s
3 actionable tasks: 3 executed
```

[](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_maps)[Working with maps](https://docs.gradle.org/userguide/lazy_configuration.html#working_with_maps)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Similar to other property types, a `MapProperty` has a [set()](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/MapProperty.html#set-java.util.Map-) method that you can use to specify the value for the property. Some additional methods allow entries with lazy values to be added to the map.

`Kotlin``Groovy`

build.gradle

```
abstract class Generator extends DefaultTask {
    @Input
    abstract MapProperty<String, Integer> getProperties()

    @TaskAction
    void generate() {
        properties.get().each { key, value ->
            logger.quiet("${key} = ${value}")
        }
    }
}

// Some values to be configured later
def b = 0
def c = 0

tasks.register('generate', Generator) {
    properties.put("a", 1)
    // Values have not been configured yet
    properties.put("b", providers.provider { b })
    properties.putAll(providers.provider { [c: c, d: c + 1] })
}

// Configure the values. There is no need to reconfigure the task
b = 2
c = 3
```

`$ ./gradlew generate`

```
> Task :generate
a = 1
b = 2
c = 3
d = 4

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

[](https://docs.gradle.org/userguide/lazy_configuration.html#applying_conventions)[Applying a convention to a property](https://docs.gradle.org/userguide/lazy_configuration.html#applying_conventions)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Often, you want to apply some _convention_, or default value to a property to be used if no value has been configured. You can use the `convention()` method for this. This method accepts either a value or a `Provider`, and this will be used as the value until some other value is configured.

`Kotlin``Groovy`

build.gradle

```
tasks.register("show") {
    def property = objects.property(String)

    // Set a convention
    property.convention("convention 1")

    println("value = " + property.get())

    // Can replace the convention
    property.convention("convention 2")
    println("value = " + property.get())

    property.set("explicit value")

    // Once a value is set, the convention is ignored
    property.convention("ignored convention")

    doLast {
        println("value = " + property.get())
    }
}
```

`$ ./gradlew show`

```
value = convention 1
value = convention 2

> Task :show
value = explicit value

BUILD SUCCESSFUL in 0s
1 actionable task: 1 executed
```

### [](https://docs.gradle.org/userguide/lazy_configuration.html#where_to_apply_conventions_from)[Where to apply conventions from?](https://docs.gradle.org/userguide/lazy_configuration.html#where_to_apply_conventions_from)

There are several appropriate locations for setting a convention on a property at configuration time (i.e., before execution).

`Kotlin``Groovy`

build.gradle

```
// setting convention when registering a task from plugin
class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        project.getTasks().register("hello", GreetingTask) {
            greeter.convention("Greeter")
        }
    }
}

apply plugin: GreetingPlugin

tasks.withType(GreetingTask).configureEach {
    // setting convention from build script
    guest.convention("Guest")
}

abstract class GreetingTask extends DefaultTask {
    // setting convention from constructor
    @Input
    abstract Property<String> getGuest()

    GreetingTask() {
        guest.convention("person2")
    }

    // setting convention from declaration
    @Input
    final Property<String> greeter = project.objects.property(String).convention("person1")

    @TaskAction
    void greet() {
        println("hello, ${guest.get()}, from ${greeter.get()}")
    }
}
```

#### [](https://docs.gradle.org/userguide/lazy_configuration.html#from_a_plugins_apply_method)[From a plugin’s `apply()` method](https://docs.gradle.org/userguide/lazy_configuration.html#from_a_plugins_apply_method)

Plugin authors may configure a convention on a lazy property from a plugin’s `apply()` method, while performing preliminary configuration of the task or extension defining the property. This works well for regular plugins (meant to be distributed and used in the wild), and internal [convention plugins](https://docs.gradle.org/current/userguide/sharing_build_logic_between_subprojects.html#sec:sharing_logic_via_convention_plugins) (which often configure properties defined by third party plugins in a uniform way for the entire build).

`Kotlin``Groovy`

build.gradle

```
// setting convention when registering a task from plugin
class GreetingPlugin implements Plugin<Project> {
    void apply(Project project) {
        project.getTasks().register("hello", GreetingTask) {
            greeter.convention("Greeter")
        }
    }
}
```

#### [](https://docs.gradle.org/userguide/lazy_configuration.html#from_a_build_script)[From a build script](https://docs.gradle.org/userguide/lazy_configuration.html#from_a_build_script)

Build engineers may configure a convention on a lazy property from shared build logic that is configuring tasks (for instance, from third-party plugins) in a standard way for the entire build.

`Kotlin``Groovy`

build.gradle

```
tasks.withType(GreetingTask).configureEach {
    // setting convention from build script
    guest.convention("Guest")
}
```

Note that for project-specific values, instead of conventions, you should prefer setting explicit values (using `Property.set(…​)` or `ConfigurableFileCollection.setFrom(…​)`, for instance), as conventions are only meant to define defaults.

#### [](https://docs.gradle.org/userguide/lazy_configuration.html#from_the_task_initialization)[From the task initialization](https://docs.gradle.org/userguide/lazy_configuration.html#from_the_task_initialization)

A task author may configure a convention on a lazy property from the task constructor or (if in Kotlin) initializer block. This approach works for properties with trivial defaults, but it is not appropriate if additional context (external to the task implementation) is required in order to set a suitable default.

`Kotlin``Groovy`

build.gradle

```
// setting convention from constructor
@Input
abstract Property<String> getGuest()

GreetingTask() {
    guest.convention("person2")
}
```

#### [](https://docs.gradle.org/userguide/lazy_configuration.html#next_to_the_property_declaration)[Next to the property declaration](https://docs.gradle.org/userguide/lazy_configuration.html#next_to_the_property_declaration)

You may configure a convention on a lazy property next to the place where the property is declared. Note this option is not available for [managed properties](https://docs.gradle.org/current/userguide/properties_providers.html#managed_properties), and has the same caveats as configuring a convention from the task constructor.

`Kotlin``Groovy`

build.gradle

```
// setting convention from declaration
@Input
final Property<String> greeter = project.objects.property(String).convention("person1")
```

[](https://docs.gradle.org/userguide/lazy_configuration.html#unmodifiable_property)[Making a property unmodifiable](https://docs.gradle.org/userguide/lazy_configuration.html#unmodifiable_property)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most properties of a task or project are intended to be configured by plugins or build scripts so that they can use specific values for that build.

For example, a property that specifies the output directory for a compilation task may start with a value specified by a plugin. Then a build script might change the value to some custom location, then this value is used by the task when it runs. However, once the task starts to run, we want to prevent further property changes. This way we avoid errors that result from different consumers, such as the task action, Gradle’s up-to-date checks, build caching, or other tasks, using different values for the property.

Lazy properties provide several methods that you can use to disallow changes to their value once the value has been configured. The [finalizeValue()](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html#finalizeValue--) method calculates the _final_ value for the property and prevents further changes to the property.

`libVersioning.version.finalizeValue()`

When the property’s value comes from a `Provider`, the provider is queried for its current value, and the result becomes the final value for the property. This final value replaces the provider and the property no longer tracks the value of the provider. Calling this method also makes a property instance unmodifiable and any further attempts to change the value of the property will fail. Gradle automatically makes the properties of a task final when the task starts execution.

The [finalizeValueOnRead()](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/HasConfigurableValue.html#finalizeValueOnRead--) method is similar, except that the property’s final value is not calculated until the value of the property is queried.

`modifiedFiles.finalizeValueOnRead()`

In other words, this method calculates the final value lazily as required, whereas `finalizeValue()` calculates the final value eagerly. This method can be used when the value may be expensive to calculate or may not have been configured yet. You also want to ensure that all consumers of the property see the same value when they query the value.

[](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration_faqs)[Using the Provider API](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration_faqs)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Guidelines to be successful with the Provider API:

1. The [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html) and [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) types have all of the overloads you need to query or configure a value. For this reason, you should follow the following guidelines:

    *   For configurable properties, expose the [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html) directly through a single getter.

    *   For non-configurable properties, expose an [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) directly through a single getter.

2.   Do not try to simplify calls like `obj.getProperty().get()` and `obj.getProperty().set(T)` in your code by introducing additional getters and setters. Using such wrapper methods would undermine the purpose of `Property` and prevent wiring of properties together. It would cause the current value to be obtained immediately (rather than being lazily evaluated).

1. When migrating your plugin to use providers, follow these guidelines:

    *   If it’s a new property, expose it as a [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html) or [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) using a single getter.

    *   If it’s incubating, change it to use a [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html) or [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) using a single getter.

    *   If it’s a stable property, add a new [Property](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Property.html) or [Provider](https://docs.gradle.org/current/javadoc/org/gradle/api/provider/Provider.html) and deprecate the old one. You should wire the old getter/setters into the new property as appropriate.

### [](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration_reference)[Provider Files API Reference](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_configuration_reference)

Use these types for _read-only_ values:

### [](https://docs.gradle.org/userguide/lazy_configuration.html#property_files_api_reference)[Property Files API Reference](https://docs.gradle.org/userguide/lazy_configuration.html#property_files_api_reference)

Use these types for _mutable_ values:

### [](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_collections_api_reference)[Lazy Collections API Reference](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_collections_api_reference)

Use these types for _mutable_ values:

### [](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_objects_api_reference)[Lazy Objects API Reference](https://docs.gradle.org/userguide/lazy_configuration.html#lazy_objects_api_reference)

Use these types for _read only_ values:

Use these types for _mutable_ values:
