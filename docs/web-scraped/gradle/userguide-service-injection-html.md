# Source: https://docs.gradle.org/userguide/service_injection.html

Title: Services and Service Injection

URL Source: https://docs.gradle.org/userguide/service_injection.html

Published Time: Wed, 04 Mar 2026 11:20:44 GMT

Markdown Content:
Gradle provides a number of useful services that can be used by custom Gradle types. For example, the [WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html) service can be used by a task to run work in parallel, as seen in the [worker API](https://docs.gradle.org/current/userguide/worker_api.html#worker_api) section. The services are made available through _service injection_.

[](https://docs.gradle.org/userguide/service_injection.html#services_for_injection)[Available services](https://docs.gradle.org/userguide/service_injection.html#services_for_injection)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You should avoid injecting types not listed below. Internal services can sometimes technically be injected, but this practice is not supported and may lead to breaking changes in the future. Only inject the services explicitly listed below to ensure stability and compatibility.

The following services are available for injection in all Gradle instantiated objects:

1. [`ObjectFactory`](https://docs.gradle.org/userguide/service_injection.html#objectfactory) - Allows model objects to be created.

2. [`ProviderFactory`](https://docs.gradle.org/userguide/service_injection.html#providerfactory) - Creates `Provider` instances.

3. [`FileSystemOperations`](https://docs.gradle.org/userguide/service_injection.html#filesystemoperations) - Allows a task to run operations on the filesystem such as deleting files, copying files or syncing directories.

4. [`ArchiveOperations`](https://docs.gradle.org/userguide/service_injection.html#archiveoperations) - Allows a task to run operations on archive files such as ZIP or TAR files.

5. [`ExecOperations`](https://docs.gradle.org/userguide/service_injection.html#execoperations) - Allows a task to run external processes with dedicated support for running external `java` programs.

### [](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_workers)[Additional services in workers](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_workers)

The following services are available for injection in worker API actions and parameters:

1. [`WorkerExecutor`](https://docs.gradle.org/userguide/service_injection.html#workerexecutor) - Allows a task to run work in parallel.

### [](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_projects)[Additional services in projects](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_projects)

The following services are available for injection in project plugins, extensions and objects created in a project:

1. [`ProjectLayout`](https://docs.gradle.org/userguide/service_injection.html#sec:projectlayout) - Provides access to key project locations.

2. [`WorkerExecutor`](https://docs.gradle.org/userguide/service_injection.html#workerexecutor) - Allows a task to run work in parallel.

3. [`ToolingModelBuilderRegistry`](https://docs.gradle.org/userguide/service_injection.html#toolingmodelbuilderregistry) - Allows a plugin to registers a Gradle tooling API model.

4. [`TestEventReporterFactory`](https://docs.gradle.org/userguide/service_injection.html#testeventreporterfactory) - Allows a plugin to access Gradle’s test events and its corresponding API.

5. [`DependencyFactory`](https://docs.gradle.org/userguide/service_injection.html#dependencyfactory) - Allows a plugin to create dependencies in a type-safe way.

### [](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_settings)[Additional services in settings](https://docs.gradle.org/userguide/service_injection.html#additional_services_in_settings)

The following services are available for injection in settings plugins, extensions and objects created in a project:

1. [`BuildLayout`](https://docs.gradle.org/userguide/service_injection.html#buildlayout) - Provides access to important locations for a Gradle build.

2. [`ToolingModelBuilderRegistry`](https://docs.gradle.org/userguide/service_injection.html#toolingmodelbuilderregistry) - Allows a plugin to registers a Gradle tooling API model.

3. [`DependencyFactory`](https://docs.gradle.org/userguide/service_injection.html#dependencyfactory) - Allows a plugin to create dependencies in a type-safe way.

[](https://docs.gradle.org/userguide/service_injection.html#objectfactory)[`ObjectFactory`](https://docs.gradle.org/userguide/service_injection.html#objectfactory)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ObjectFactory`](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html) is a service for creating custom Gradle types, allowing you to define nested objects and DSLs in your build logic. It provides methods for creating instances of different types, such as properties (`Property<T>`), collections (`ListProperty<T>`, `SetProperty<T>`, `MapProperty<K, V>`), file-related objects (`RegularFileProperty`, `DirectoryProperty`, `ConfigurableFileCollection`, `ConfigurableFileTree`), and more.

You can obtain an instance of `ObjectFactory` using the `project.objects` property. Here’s a simple example demonstrating how to use `ObjectFactory` to create a property and set its value:

`Kotlin``Groovy`

build.gradle

```
tasks.register("myObjectFactoryTask") {
    doLast {
        def objectFactory = project.objects
        def myProperty = objectFactory.property(String)
        myProperty.set("Hello, Gradle!")
        println myProperty.get()
    }
}
```

Using `ObjectFactory` to create these objects ensures that they are properly managed by Gradle, especially in terms of configuration avoidance and lazy evaluation. This means that the values of these objects are only calculated when needed, which can improve build performance.

In the following example, a project extension called `DownloadExtension` receives an `ObjectFactory` instance through its constructor. The constructor uses this to create a nested `Resource` object (also a custom Gradle type) and makes this object available through the `resource` property:

DownloadExtension.java

```
public class DownloadExtension {
    // A nested instance
    private final Resource resource;

    @Inject
    public DownloadExtension(ObjectFactory objectFactory) {
        // Use an injected ObjectFactory to create a Resource object
        resource = objectFactory.newInstance(Resource.class);
    }

    public Resource getResource() {
        return resource;
    }
}

public interface Resource {
    Property<URI> getUri();
}
```

Here is another example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyObjectFactoryTask extends DefaultTask {
    private ObjectFactory objectFactory

    @Inject //@javax.inject.Inject
    MyObjectFactoryTask(ObjectFactory objectFactory) {
        this.objectFactory = objectFactory
    }

    @TaskAction
    void doTaskAction() {
        var outputDirectory = objectFactory.directoryProperty()
        outputDirectory.convention(project.layout.projectDirectory)
        println(outputDirectory.get())
    }
}

tasks.register("myInjectedObjectFactoryTask",MyObjectFactoryTask) {}
```

The `MyObjectFactoryTask` task uses an `ObjectFactory` instance, which is injected into the task’s constructor using the `@Inject` annotation.

[](https://docs.gradle.org/userguide/service_injection.html#sec:projectlayout)[`ProjectLayout`](https://docs.gradle.org/userguide/service_injection.html#sec:projectlayout)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ProjectLayout`](https://docs.gradle.org/current/dsl/org.gradle.api.file.ProjectLayout.html) is a service that provides access to the layout of a Gradle project’s directories and files. It’s part of the `org.gradle.api.file` package and allows you to query the project’s layout to get information about source sets, build directories, and other file-related aspects of the project.

You can obtain a `ProjectLayout` instance from a `Project` object using the `project.layout` property. Here’s a simple example:

`Kotlin``Groovy`

build.gradle

```
tasks.register('showLayout') {
    doLast {
        def layout = project.layout
        println "Project Directory: ${layout.projectDirectory}"
        println "Build Directory: ${layout.buildDirectory.get()}"
    }
}
```

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyProjectLayoutTask extends DefaultTask {
    private ProjectLayout projectLayout

    @Inject //@javax.inject.Inject
    MyProjectLayoutTask(ProjectLayout projectLayout) {
        this.projectLayout = projectLayout
    }

    @TaskAction
    void doTaskAction() {
        var outputDirectory = projectLayout.projectDirectory
        println(outputDirectory)
    }
}

tasks.register("myInjectedProjectLayoutTask",MyProjectLayoutTask) {}
```

The `MyProjectLayoutTask` task uses a `ProjectLayout` instance, which is injected into the task’s constructor using the `@Inject` annotation.

[](https://docs.gradle.org/userguide/service_injection.html#buildlayout)[`BuildLayout`](https://docs.gradle.org/userguide/service_injection.html#buildlayout)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

[`BuildLayout`](https://docs.gradle.org/current/dsl/org.gradle.api.file.BuildLayout.html) is a service that provides access to the root and settings directory in a Settings plugin or a Settings script, it is analogous to `ProjectLayout`. It’s part of the `org.gradle.api.file` package to access standard build-wide file system locations as lazily computed value.

These APIs are currently incubating but eventually should replace existing accessors in Settings, which return eagerly computed locations:

`Settings.rootDir` → `Settings.layout.rootDirectory`

`Settings.settingsDir` → `Settings.layout.settingsDirectory`

You can obtain a `BuildLayout` instance from a `Settings` object using the `settings.layout` property. Here’s a simple example:

`Kotlin``Groovy`

settings.gradle

```
println "Root Directory: ${settings.layout.rootDirectory}"
println "Settings Directory: ${settings.layout.settingsDirectory}"
```

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

settings.gradle

```
abstract class MyBuildLayoutPlugin implements Plugin<Settings> {
    private BuildLayout buildLayout

    @Inject //@javax.inject.Inject
    MyBuildLayoutPlugin(BuildLayout buildLayout) {
        this.buildLayout = buildLayout
    }

    @Override void apply(Settings settings) {
        // the meat and potatoes of the plugin
        println buildLayout.rootDirectory
    }
}

apply plugin: MyBuildLayoutPlugin
```

This code defines a `MyBuildLayoutPlugin` plugin that implements the `Plugin` interface for the `Settings` type. The plugin expects a `BuildLayout` instance to be injected into its constructor using the `@Inject` annotation.

[](https://docs.gradle.org/userguide/service_injection.html#providerfactory)[`ProviderFactory`](https://docs.gradle.org/userguide/service_injection.html#providerfactory)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ProviderFactory`](https://docs.gradle.org/current/dsl/org.gradle.api.provider.ProviderFactory.html) is a service that provides methods for creating different types of providers. Providers are used to model values that may be computed lazily in your build scripts.

The `ProviderFactory` interface provides methods for creating various types of providers, including:

* `provider(Callable<T> value)` to create a provider with a value that is lazily computed based on a `Callable`.

* `provider(Provider<T> value)` to create a provider that simply wraps an existing provider.

* `property(Class<T> type)` to create a property provider for a specific type.

* `gradleProperty(Class<T> type)` to create a property provider that reads its value from a Gradle project property.

Here’s a simple example demonstrating the use of `ProviderFactory` using `project.providers`:

`Kotlin``Groovy`

build.gradle

```
tasks.register('printMessage') {
    doLast {
        def providerFactory = project.providers
        def messageProvider = providerFactory.provider { "Hello, Gradle!" }
        println messageProvider.get()
    }
}
```

The task named `printMessage` uses the `ProviderFactory` to create a `provider` that supplies the message string.

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyProviderFactoryTask extends DefaultTask {
    private ProviderFactory providerFactory

    @Inject //@javax.inject.Inject
    MyProviderFactoryTask(ProviderFactory providerFactory) {
        this.providerFactory = providerFactory
    }

    @TaskAction
    void doTaskAction() {
        var outputDirectory = providerFactory.provider { "build/my-file.txt" }
        println(outputDirectory.get())
    }
}

tasks.register("myInjectedProviderFactoryTask",MyProviderFactoryTask) {}
```

The `ProviderFactory` service is injected into the `MyProviderFactoryTask` task’s constructor using the `@Inject` annotation.

[](https://docs.gradle.org/userguide/service_injection.html#workerexecutor)[`WorkerExecutor`](https://docs.gradle.org/userguide/service_injection.html#workerexecutor)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`WorkerExecutor`](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html) is a service that allows you to perform parallel execution of tasks using worker processes. This is particularly useful for tasks that perform CPU-intensive or long-running operations, as it allows them to be executed in parallel, improving build performance.

Using `WorkerExecutor`, you can submit units of work (called actions) to be executed in separate worker processes. This helps isolate the work from the main Gradle process, providing better reliability and performance.

Here’s a basic example of how you might use `WorkerExecutor` in a build script:

`Kotlin``Groovy`

build.gradle

```
abstract class MyWorkAction implements WorkAction<WorkParameters.None> {
    private final String greeting;

    @Inject
    public MyWorkAction() {
        this.greeting = "Hello from a Worker!";
    }

    @Override
    public void execute() {
        System.out.println(greeting);
    }
}

abstract class MyWorkerTask extends DefaultTask {
    @Input
    abstract Property<Boolean> getBooleanFlag()

    @Inject
    abstract WorkerExecutor getWorkerExecutor()

    @TaskAction
    void doThings() {
        workerExecutor.noIsolation().submit(MyWorkAction) {}
    }
}

tasks.register("myWorkTask", MyWorkerTask) {}
```

[](https://docs.gradle.org/userguide/service_injection.html#filesystemoperations)[`FileSystemOperations`](https://docs.gradle.org/userguide/service_injection.html#filesystemoperations)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`FileSystemOperations`](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileSystemOperations.html) is a service that provides methods for performing file system operations such as copying, deleting, and syncing. It is part of the `org.gradle.api.file` package and is typically used in custom tasks or plugins to interact with the file system.

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyFileSystemOperationsTask extends DefaultTask {
    private FileSystemOperations fileSystemOperations

    @Inject //@javax.inject.Inject
    MyFileSystemOperationsTask(FileSystemOperations fileSystemOperations) {
        this.fileSystemOperations = fileSystemOperations
    }

    @TaskAction
    void doTaskAction() {
        fileSystemOperations.sync {
            from 'src'
            into 'dest'
        }
    }
}

tasks.register("myInjectedFileSystemOperationsTask", MyFileSystemOperationsTask)
```

The `FileSystemOperations` service is injected into the `MyFileSystemOperationsTask` task’s constructor using the `@Inject` annotation.

With some ceremony, it is possible to use `FileSystemOperations` in an ad-hoc task defined in a build script:

`Kotlin``Groovy`

build.gradle

```
interface InjectedFsOps {
    @Inject //@javax.inject.Inject
    FileSystemOperations getFs()
}

tasks.register('myAdHocFileSystemOperationsTask') {
    def injected = project.objects.newInstance(InjectedFsOps)
    doLast {
        injected.fs.copy {
            from 'source'
            into 'destination'
        }
    }
}
```

First, you need to declare an interface with a property of type `FileSystemOperations`, here named `InjectedFsOps`, to serve as an injection point. Then call the method [`ObjectFactory.newInstance`](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#newInstance(java.lang.Class,java.lang.Object%2E%2E%2E)) to generate an implementation of the interface that holds an injected service.

This is a good time to consider extracting the ad-hoc task into a proper class.

[](https://docs.gradle.org/userguide/service_injection.html#archiveoperations)[`ArchiveOperations`](https://docs.gradle.org/userguide/service_injection.html#archiveoperations)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ArchiveOperations`](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ArchiveOperations.html) is a service that provides methods for accessing the contents of archives, such as ZIP and TAR files. It is part of the `org.gradle.api.file` package and is typically used in custom tasks or plugins to unpack archive files.

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyArchiveOperationsTask extends DefaultTask {
    private ArchiveOperations archiveOperations
    private ProjectLayout layout
    private FileSystemOperations fs

    @Inject
    MyArchiveOperationsTask(ArchiveOperations archiveOperations, ProjectLayout layout, FileSystemOperations fs) {
        this.archiveOperations = archiveOperations
        this.layout = layout
        this.fs = fs
    }

    @TaskAction
    void doTaskAction() {
        fs.sync {
            from(archiveOperations.zipTree(layout.projectDirectory.file("sources.jar")))
            into(layout.buildDirectory.dir("unpacked-sources"))
        }
    }
}

tasks.register("myInjectedArchiveOperationsTask", MyArchiveOperationsTask)
```

The `ArchiveOperations` service is injected into the `MyArchiveOperationsTask` task’s constructor using the `@Inject` annotation.

With some ceremony, it is possible to use `ArchiveOperations` in an ad-hoc task defined in a build script:

`Kotlin``Groovy`

build.gradle

```
interface InjectedArcOps {
    @Inject //@javax.inject.Inject
    ArchiveOperations getArcOps()
}

tasks.register('myAdHocArchiveOperationsTask') {
    def injected = project.objects.newInstance(InjectedArcOps)
    def archiveFile = "${projectDir}/sources.jar"

    doLast {
        injected.arcOps.zipTree(archiveFile)
    }
}
```

First, you need to declare an interface with a property of type `ArchiveOperations`, here named `InjectedArcOps`, to serve as an injection point. Then call the method [`ObjectFactory.newInstance`](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#newInstance(java.lang.Class,java.lang.Object%2E%2E%2E)) to generate an implementation of the interface that holds an injected service.

This is a good time to consider extracting the ad-hoc task into a proper class.

[](https://docs.gradle.org/userguide/service_injection.html#execoperations)[`ExecOperations`](https://docs.gradle.org/userguide/service_injection.html#execoperations)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ExecOperations`](https://docs.gradle.org/current/javadoc/org/gradle/process/ExecOperations.html) is a service that provides methods for executing external processes (commands) from within a build script. It is part of the `org.gradle.process` package and is typically used in custom tasks or plugins to run command-line tools or scripts as part of the build process.

Here is an example using `javax.inject.Inject`:

`Kotlin``Groovy`

build.gradle

```
abstract class MyExecOperationsTask extends DefaultTask {
    private ExecOperations execOperations

    @Inject //@javax.inject.Inject
    MyExecOperationsTask(ExecOperations execOperations) {
        this.execOperations = execOperations
    }

    @TaskAction
    void doTaskAction() {
        execOperations.exec {
            commandLine 'ls', '-la'
        }
    }
}

tasks.register("myInjectedExecOperationsTask", MyExecOperationsTask)
```

The `ExecOperations` is injected into the `MyExecOperationsTask` task’s constructor using the `@Inject` annotation.

With some ceremony, it is possible to use `ExecOperations` in an ad-hoc task defined in a build script:

`Kotlin``Groovy`

build.gradle

```
interface InjectedExecOps {
    @Inject //@javax.inject.Inject
    ExecOperations getExecOps()
}

tasks.register('myAdHocExecOperationsTask') {
    def injected = project.objects.newInstance(InjectedExecOps)

    doLast {
        injected.execOps.exec {
            commandLine 'ls', '-la'
        }
    }
}
```

First, you need to declare an interface with a property of type `ExecOperations`, here named `InjectedExecOps`, to serve as an injection point. Then call the method [`ObjectFactory.newInstance`](https://docs.gradle.org/current/javadoc/org/gradle/api/model/ObjectFactory.html#newInstance(java.lang.Class,java.lang.Object%2E%2E%2E)) to generate an implementation of the interface that holds an injected service.

This is a good time to consider extracting the ad-hoc task into a proper class.

[](https://docs.gradle.org/userguide/service_injection.html#toolingmodelbuilderregistry)[`ToolingModelBuilderRegistry`](https://docs.gradle.org/userguide/service_injection.html#toolingmodelbuilderregistry)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`ToolingModelBuilderRegistry`](https://docs.gradle.org/current/javadoc/org/gradle/tooling/provider/model/ToolingModelBuilderRegistry.html) is a service that allows you to register custom tooling model builders. Tooling models are used to provide rich IDE integration for Gradle projects, allowing IDEs to understand and work with the project’s structure, dependencies, and other aspects.

The `ToolingModelBuilderRegistry` interface is part of the `org.gradle.tooling.provider.model` package and is typically used in custom Gradle plugins that provide enhanced IDE support.

Here’s a simplified example:

`Kotlin``Groovy`

build.gradle

```
// Implements the ToolingModelBuilder interface.
// This interface is used in Gradle to define custom tooling models that can
// be accessed by IDEs or other tools through the Gradle tooling API.
class OrtModelBuilder implements ToolingModelBuilder {
    private Map<String, String> repositories = [:]

    private Set<String> platformCategories = ["platform", "enforced-platform"]

    private Set<ModuleComponentIdentifier> visitedDependencies = []
    private Set<ModuleVersionIdentifier> visitedProjects = []

    private static final logger = Logging.getLogger(OrtModelBuilder.class)
    private List<String> errors = []
    private List<String> warnings = []

    @Override
    boolean canBuild(String modelName) {
        return false
    }

    @Override
    Object buildAll(String modelName, Project project) {
        return null
    }
}

// Plugin is responsible for registering a custom tooling model builder
// (OrtModelBuilder) with the ToolingModelBuilderRegistry, which allows
// IDEs and other tools to access the custom tooling model.
class OrtModelPlugin implements Plugin<Project> {
    ToolingModelBuilderRegistry registry

    OrtModelPlugin(ToolingModelBuilderRegistry registry) {
        this.registry = registry
    }

    void apply(Project project) {
        registry.register(new OrtModelBuilder())
    }
}
```

[](https://docs.gradle.org/userguide/service_injection.html#testeventreporterfactory)[`TestEventReporterFactory`](https://docs.gradle.org/userguide/service_injection.html#testeventreporterfactory)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This API is incubating.

[](https://docs.gradle.org/userguide/service_injection.html#dependencyfactory)[`DependencyFactory`](https://docs.gradle.org/userguide/service_injection.html#dependencyfactory)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[`DependencyFactory`](https://docs.gradle.org/current/javadoc/org/gradle/api/artifacts/dsl/DependencyFactory.html) is a service that provides methods for creating dependencies in a type-safe way.

[](https://docs.gradle.org/userguide/service_injection.html#service_injection_patterns)[Service injection patterns](https://docs.gradle.org/userguide/service_injection.html#service_injection_patterns)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two ways that services can be provided to an object.

### [](https://docs.gradle.org/userguide/service_injection.html#constructor_injection)[Constructor injection](https://docs.gradle.org/userguide/service_injection.html#constructor_injection)

A service can be injected into the constructor of the class. The constructor must be public and annotated with the `javax.inject.Inject` annotation.

Gradle uses the declared type of each constructor parameter to determine the services that the object requires. The order of the constructor parameters and their names are not significant and can be whatever you like.

Here is an example that shows a task type that receives an `WorkerExecutor` via its constructor:

Download.java

```
public class Download extends DefaultTask {
    private final WorkerExecutor workerExecutor;

    // Inject an WorkerExecutor into the constructor
    @Inject
    public Download(WorkerExecutor workerExecutor) {
        this.workerExecutor = workerExecutor;
    }

    @TaskAction
    void run() {
        // ...use workerExecutor to run some work
    }
}
```

### [](https://docs.gradle.org/userguide/service_injection.html#property_injection)[Property injection](https://docs.gradle.org/userguide/service_injection.html#property_injection)

A service can be injected by adding a property getter method annotated with the `javax.inject.Inject` annotation to the class.

Gradle defers the creation of the service until the getter method is called. This can be more performant than constructor injection.

The property getter method must be `public` or `protected`. Gradle uses the declared return type of the getter method to determine the service to make available.

The method should be `abstract` or, in cases where this isn’t possible, should have a dummy method body. The method body is discarded. The name of the property is not significant and can be whatever you like.

Here is an example that shows a task type that receives two services via property getter methods:

Download.java

```
public abstract class Download extends DefaultTask {
    // Preferrably, use an abstract getter method
    @Inject
    protected abstract ObjectFactory getObjectFactory();

    // Alternatively, use a getter method with a dummy implementation
    @Inject
    protected WorkerExecutor getWorkerExecutor() {
        // Method body is ignored
        throw new UnsupportedOperationException();
    }

    @TaskAction
    void run() {
        WorkerExecutor workerExecutor = getWorkerExecutor();
        ObjectFactory objectFactory = getObjectFactory();
        // Use the executor and factory ...
    }
}
```
