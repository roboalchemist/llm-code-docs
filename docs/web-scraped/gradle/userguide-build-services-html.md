# Source: https://docs.gradle.org/userguide/build_services.html

Title: Using Shared Build Services

URL Source: https://docs.gradle.org/userguide/build_services.html

Markdown Content:
Shared build services allow tasks to share state or resources. For example, tasks might share a cache of pre-computed values or use a web service or database instance.

A build service is an object that holds the state for tasks to use. It provides an alternative mechanism for hooking into a Gradle build and receiving information about task execution and operation completion.

Build services are configuration cacheable.

Gradle manages the service lifecycle, creating the service instance only when required and cleaning it up when no longer needed. Gradle can also coordinate access to the build service, ensuring that no more than a specified number of tasks use the service concurrently.

[](https://docs.gradle.org/userguide/build_services.html#implementing_a_build_service)[Implementing a build service](https://docs.gradle.org/userguide/build_services.html#implementing_a_build_service)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To implement a build service, create an abstract class that implements [BuildService](https://docs.gradle.org/current/javadoc/org/gradle/api/services/BuildService.html). Then, define methods you want the tasks to use on this type.

```
abstract class BaseCountingService implements BuildService<CountingParams>, AutoCloseable {

}
```

A build service implementation is treated as a [custom Gradle type](https://docs.gradle.org/current/userguide/properties_providers.html#properties_and_providers) and can use any of the features available to custom Gradle types.

A build service can optionally take parameters, which Gradle injects into the service instance when creating it. To provide parameters, you define an abstract class (or interface) that holds the parameters. The parameters type must implement (or extend) [BuildServiceParameters](https://docs.gradle.org/current/javadoc/org/gradle/api/services/BuildServiceParameters.html). The service implementation can access the parameters using `this.getParameters()`. The parameters type is also a [custom Gradle type](https://docs.gradle.org/current/userguide/properties_providers.html#properties_and_providers).

When the build service does not require any parameters, you can use [BuildServiceParameters.None](https://docs.gradle.org/current/javadoc/org/gradle/api/services/BuildServiceParameters.None.html) as the type of parameter.

```
interface CountingParams extends BuildServiceParameters {
    Property<Integer> getInitial()
}
```

A build service implementation can also optionally implement `AutoCloseable`, in which case Gradle will call the build service instance’s `close()` method when it discards the service instance. This happens sometime between the completion of the last task that uses the build service and the end of the build.

Here is an example of a service that takes parameters and is closeable:

WebServer.java

```
import org.gradle.api.file.DirectoryProperty;
import org.gradle.api.provider.Property;
import org.gradle.api.services.BuildService;
import org.gradle.api.services.BuildServiceParameters;

import java.net.URI;
import java.net.URISyntaxException;

public abstract class WebServer implements BuildService<WebServer.Params>, AutoCloseable {

    // Some parameters for the web server
    interface Params extends BuildServiceParameters {
        Property<Integer> getPort();

        DirectoryProperty getResources();
    }

    private final URI uri;

    public WebServer() throws URISyntaxException {
        // Use the parameters
        int port = getParameters().getPort().get();
        uri = new URI(String.format("https://localhost:%d/", port));

        // Start the server ...

        System.out.println(String.format("Server is running at %s", uri));
    }

    // A public method for tasks to use
    public URI getUri() {
        return uri;
    }

    @Override
    public void close() {
        // Stop the server ...
    }
}
```

Note that you should **not** implement the [BuildService.getParameters()](https://docs.gradle.org/current/javadoc/org/gradle/api/services/BuildService.html#getParameters--) method, as Gradle will provide an implementation of this.

A build service implementation must be thread-safe, as it will potentially be used by multiple tasks concurrently.

[](https://docs.gradle.org/userguide/build_services.html#using_a_build_service_from_a_task)[Registering a build service and connecting it to a task](https://docs.gradle.org/userguide/build_services.html#using_a_build_service_from_a_task)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Registering the service does not create the service instance. This happens on demand when a task first uses the service. The service instance will not be created if no task uses the service during a build.

Currently, build services are scoped to a build, rather than a project, and these services are available to be shared by the tasks of all projects. You can access the registry of shared build services via `Project.getGradle().getSharedServices()`.

### [](https://docs.gradle.org/userguide/build_services.html#sec:service_references)[Registering a build service to be consumed via `@ServiceReference` task properties](https://docs.gradle.org/userguide/build_services.html#sec:service_references)

Here is an example of a plugin that registers the previous service when the task property consuming the service is annotated with `@ServiceReference`:

DownloadPlugin.java

```
import org.gradle.api.Plugin;
import org.gradle.api.Project;
import org.gradle.api.provider.Provider;

public class DownloadPlugin implements Plugin<Project> {
    public void apply(Project project) {
        // Register the service
        project.getGradle().getSharedServices().registerIfAbsent("web", WebServer.class, spec -> {
            // Provide some parameters
            spec.getParameters().getPort().set(5005);
        });

        project.getTasks().register("download", Download.class, task -> {
            task.getOutputFile().set(project.getLayout().getBuildDirectory().file("result.zip"));
        });
    }
}
```

As you can see, there is no need to assign the build service provider returned by `registerIfAbsent()` to the task, the service is automatically injected into all matching properties that were annotated with `@ServiceReference`.

Here is an example of a task that consumes the previous service via a property annotated with `@ServiceReference`:

Download.java

```
import org.gradle.api.DefaultTask;
import org.gradle.api.file.RegularFileProperty;
import org.gradle.api.provider.Property;
import org.gradle.api.services.ServiceReference;
import org.gradle.api.tasks.OutputFile;
import org.gradle.api.tasks.TaskAction;

import java.net.URI;

public abstract class Download extends DefaultTask {
    // This property provides access to the service instance
    @ServiceReference("web")
    abstract Property<WebServer> getServer();

    @OutputFile
    abstract RegularFileProperty getOutputFile();

    @TaskAction
    public void download() {
        // Use the server to download a file
        WebServer server = getServer().get();
        URI uri = server.getUri().resolve("somefile.zip");
        System.out.println(String.format("Downloading %s", uri));
    }
}
```

Automatic matching of registered build services with service reference properties is done by type and (optionally) by name (for properties that declare the name of the service they expect). In case multiple services would match the requested service type (i.e. multiple services were registered for the same type, and a service name was not provided in the `@ServiceReference` annotation), you will need also to assign the shared build service provider manually to the task property.

Read on to compare that to when the task property consuming the service is instead annotated with `@Internal`.

### [](https://docs.gradle.org/userguide/build_services.html#registering_a_build_service_to_be_consumed_via_internal_task_properties)[Registering a build service to be consumed via `@Internal` task properties](https://docs.gradle.org/userguide/build_services.html#registering_a_build_service_to_be_consumed_via_internal_task_properties)

DownloadPlugin.java

```
import org.gradle.api.Plugin;
import org.gradle.api.Project;
import org.gradle.api.provider.Provider;

public class DownloadPlugin implements Plugin<Project> {
    public void apply(Project project) {
        // Register the service
        Provider<WebServer> serviceProvider = project.getGradle().getSharedServices().registerIfAbsent("web", WebServer.class, spec -> {
            // Provide some parameters
            spec.getParameters().getPort().set(5005);
        });

        project.getTasks().register("download", Download.class, task -> {
            // Connect the service provider to the task
            task.getServer().set(serviceProvider);
            // Declare the association between the task and the service
            task.usesService(serviceProvider);
            task.getOutputFile().set(project.getLayout().getBuildDirectory().file("result.zip"));
        });
    }
}
```

In this case, the plugin registers the service and receives a `Provider<WebService>` back. This provider can be connected to task properties to pass the service to the task. Note that for a task property annotated with `@Internal`, the task property needs to (1) be explicitly assigned with the provider obtained during registation, and (2) you must tell Gradle the task uses the service via [Task.usesService](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:usesService(org.gradle.api.provider.Provider)). None of that is needed when the task property consuming the service is annotated with `@ServiceReference`.

Here is an example of a task that consumes the previous service via a property annotated with `@Internal`:

Download.java

```
import org.gradle.api.DefaultTask;
import org.gradle.api.file.RegularFileProperty;
import org.gradle.api.provider.Property;
import org.gradle.api.tasks.Internal;
import org.gradle.api.tasks.OutputFile;
import org.gradle.api.tasks.TaskAction;

import java.net.URI;

public abstract class Download extends DefaultTask {
    // This property provides access to the service instance
    @Internal
    abstract Property<WebServer> getServer();

    @OutputFile
    abstract RegularFileProperty getOutputFile();

    @TaskAction
    public void download() {
        // Use the server to download a file
        WebServer server = getServer().get();
        URI uri = server.getUri().resolve("somefile.zip");
        System.out.println(String.format("Downloading %s", uri));
    }
}
```

Note that using a service with any annotation other than `@ServiceReference` or `@Internal` is currently not supported. For example, it is currently impossible to mark a service as an input to a task.

### [](https://docs.gradle.org/userguide/build_services.html#using_shared_build_services_from_configuration_actions)[Using shared build services from configuration actions](https://docs.gradle.org/userguide/build_services.html#using_shared_build_services_from_configuration_actions)

Generally, build services are intended to be used by tasks, and as they usually represent some potentially expensive state to create, you should avoid using them at configuration time. However, sometimes, using the service at configuration time can make sense. This is possible; call `get()` on the provider.

[](https://docs.gradle.org/userguide/build_services.html#using_a_build_service_with_the_worker_api)[Using a build service with the Worker API](https://docs.gradle.org/userguide/build_services.html#using_a_build_service_with_the_worker_api)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to using a build service from a task, you can use a build service from a [Worker API action](https://docs.gradle.org/current/userguide/worker_api.html#converting_to_worker_api), an [artifact transform](https://docs.gradle.org/current/userguide/artifact_transforms.html#sec:implementing-artifact-transforms) or another build service. To do this, pass the build service `Provider` as a parameter of the consuming action or service, in the same way you pass other parameters to the action or service.

For example, to pass a `MyServiceType` service to Worker API action, you might add a property of type `Property<MyServiceType>` to the action’s parameters object and then connect the `Provider<MyServiceType>` that you receive when registering the service to this property:

Download.java

```
import org.gradle.api.DefaultTask;
import org.gradle.api.provider.Property;
import org.gradle.api.services.ServiceReference;
import org.gradle.api.tasks.TaskAction;
import org.gradle.workers.WorkAction;
import org.gradle.workers.WorkParameters;
import org.gradle.workers.WorkQueue;
import org.gradle.workers.WorkerExecutor;

import javax.inject.Inject;
import java.net.URI;

public abstract class Download extends DefaultTask {

    public static abstract class DownloadWorkAction implements WorkAction<DownloadWorkAction.Parameters> {
        interface Parameters extends WorkParameters {
            // This property provides access to the service instance from the work action
            abstract Property<WebServer> getServer();
        }

        @Override
        public void execute() {
            // Use the server to download a file
            WebServer server = getParameters().getServer().get();
            URI uri = server.getUri().resolve("somefile.zip");
            System.out.println(String.format("Downloading %s", uri));
        }
    }

    @Inject
    abstract public WorkerExecutor getWorkerExecutor();

    // This property provides access to the service instance from the task
    @ServiceReference("web")
    abstract Property<WebServer> getServer();

    @TaskAction
    public void download() {
        WorkQueue workQueue = getWorkerExecutor().noIsolation();
        workQueue.submit(DownloadWorkAction.class, parameter -> {
            parameter.getServer().set(getServer());
        });
    }
}
```

Currently, it is impossible to use a build service with a worker API action that uses ClassLoader or process isolation modes.

[](https://docs.gradle.org/userguide/build_services.html#accessing_the_build_service_concurrently)[Accessing the build service concurrently](https://docs.gradle.org/userguide/build_services.html#accessing_the_build_service_concurrently)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can constrain concurrent execution when you register the service, by using the `Property` object returned from [BuildServiceSpec.getMaxParallelUsages()](https://docs.gradle.org/current/javadoc/org/gradle/api/services/BuildServiceSpec.html#getMaxParallelUsages--). When this property has no value, which is the default, Gradle does not constrain access to the service. When this property has a value > 0, Gradle will allow no more than the specified number of tasks to use the service concurrently.

When the consuming task property is annotated with `@Internal`, for the constraint to take effect, the build service **must** be registered with the consuming task via [Task.usesService](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:usesService(org.gradle.api.provider.Provider)). NOTE: at this time, Gradle cannot discover indirect usage of services (for instance, if an additional service is used only by a service that the task uses directly). As a workaround, indirect usage may be declared explicitly to Gradle by either adding a `@ServiceReference` property to the task and assigning the service that is only used indirectly to it (making it a direct reference), or invoking [Task.usesService](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:usesService(org.gradle.api.provider.Provider)).

[](https://docs.gradle.org/userguide/build_services.html#operation_listener)[Receiving information about task execution](https://docs.gradle.org/userguide/build_services.html#operation_listener)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A build service can be used to receive events as tasks are executed. To do this, create and register a build service that implements [OperationCompletionListener](https://docs.gradle.org/current/javadoc/org/gradle/tooling/events/OperationCompletionListener.html):

TaskEventsService.java

```
import org.gradle.api.services.BuildService;
import org.gradle.api.services.BuildServiceParameters;
import org.gradle.tooling.events.FinishEvent;
import org.gradle.tooling.events.OperationCompletionListener;
import org.gradle.tooling.events.task.TaskFinishEvent;

public abstract class TaskEventsService implements BuildService<BuildServiceParameters.None>,
    OperationCompletionListener { (1)

    @Override
    public void onFinish(FinishEvent finishEvent) {
        if (finishEvent instanceof TaskFinishEvent) { (2)
            // Handle task finish event...
        }
    }
}
```

**1**Implement the `OperationCompletionListener` interface and the `BuildService` interface.
**2**Check if the finish event is a [TaskFinishEvent](https://docs.gradle.org/current/javadoc/org/gradle/tooling/events/task/TaskFinishEvent.html).

Then, in the plugin, you can use the methods on the [BuildEventsListenerRegistry](https://docs.gradle.org/current/javadoc/org/gradle/build/event/BuildEventsListenerRegistry.html) service to start receiving events:

TaskEventsPlugin.java

```
import org.gradle.api.Plugin;
import org.gradle.api.Project;
import org.gradle.api.provider.Provider;
import org.gradle.build.event.BuildEventsListenerRegistry;

import javax.inject.Inject;

public abstract class TaskEventsPlugin implements Plugin<Project> {
    @Inject
    public abstract BuildEventsListenerRegistry getEventsListenerRegistry(); (1)

    @Override
    public void apply(Project project) {
        Provider<TaskEventsService> serviceProvider =
            project.getGradle().getSharedServices().registerIfAbsent(
                "taskEvents", TaskEventsService.class, spec -> {}); (2)

        getEventsListenerRegistry().onTaskCompletion(serviceProvider); (3)
    }
}
```

**1**Use [service injection](https://docs.gradle.org/current/userguide/service_injection.html#service_injection) to obtain an instance of the `BuildEventsListenerRegistry`.
**2**Register the build service as usual.
**3**Use the service `Provider` to subscribe to the build service to build events.
