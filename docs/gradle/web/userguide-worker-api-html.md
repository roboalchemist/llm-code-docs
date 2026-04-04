# Source: https://docs.gradle.org/userguide/worker_api.html

Title: Developing Parallel Tasks

URL Source: https://docs.gradle.org/userguide/worker_api.html

Markdown Content:
The best way to understand how to use the API is to go through the process of converting an existing custom task to use the Worker API:

1. You’ll start by creating a custom task class that generates MD5 hashes for a configurable set of files.

2. Then, you’ll convert this custom task to use the Worker API.

3. Then, we’ll explore running the task with different levels of isolation.

In the process, you’ll learn about the basics of the Worker API and the capabilities it provides.

### [](https://docs.gradle.org/userguide/worker_api.html#step_1_create_a_custom_task_class)[Step 1. Create a custom task class](https://docs.gradle.org/userguide/worker_api.html#step_1_create_a_custom_task_class)

First, create a custom task that generates MD5 hashes of a configurable set of files.

In a new directory, create a `buildSrc/build.gradle(.kts)` file:

`Kotlin``Groovy`

buildSrc/build.gradle

```
repositories {
    mavenCentral()
}

dependencies {
    implementation 'commons-io:commons-io:2.5'
    implementation 'commons-codec:commons-codec:1.9' (1)
}
```

Next, create a custom task class in your `buildSrc/src/main/java` directory. You should name this class `CreateMD5`:

buildSrc/src/main/java/CreateMD5.java

```
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.io.FileUtils;
import org.gradle.api.file.DirectoryProperty;
import org.gradle.api.file.RegularFile;
import org.gradle.api.provider.Provider;
import org.gradle.api.tasks.OutputDirectory;
import org.gradle.api.tasks.SourceTask;
import org.gradle.api.tasks.TaskAction;
import org.gradle.workers.WorkerExecutor;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

abstract public class CreateMD5 extends SourceTask { (1)

    @OutputDirectory
    abstract public DirectoryProperty getDestinationDirectory(); (2)

    @TaskAction
    public void createHashes() {
        for (File sourceFile : getSource().getFiles()) { (3)
            try {
                InputStream stream = new FileInputStream(sourceFile);
                System.out.println("Generating MD5 for " + sourceFile.getName() + "...");
                // Artificially make this task slower.
                Thread.sleep(3000); (4)
                Provider<RegularFile> md5File = getDestinationDirectory().file(sourceFile.getName() + ".md5");  (5)
                FileUtils.writeStringToFile(md5File.get().getAsFile(), DigestUtils.md5Hex(stream), (String) null);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```

**1**[SourceTask](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/SourceTask.html) is a convenience type for tasks that operate on a set of source files.
**2**The task output will go into a configured directory.
**3**The task iterates over all the files defined as "source files" and creates an MD5 hash of each.
**4**Insert an artificial sleep to simulate hashing a large file (the sample files won’t be that large).
**5**The MD5 hash of each file is written to the output directory into a file of the same name with an "md5" extension.

Next, create a `build.gradle(.kts)` that registers your new `CreateMD5` task:

`Kotlin``Groovy`

build.gradle

```
plugins { id 'base' } (1)

tasks.register("md5", CreateMD5) {
    destinationDirectory = project.layout.buildDirectory.dir("md5") (2)
    source(project.layout.projectDirectory.file('src')) (3)
}
```

**1**Apply the `base` plugin so that you’ll have a `clean` task to use to remove the output.
**2**MD5 hash files will be written to `build/md5`.
**3**This task will generate MD5 hash files for every file in the `src` directory.

You will need some source to generate MD5 hashes from. Create three files in the `src` directory:

src/einstein.txt

`Intellectual growth should commence at birth and cease only at death.`

src/feynman.txt

`I was born not knowing and have had only a little time to change that here and there.`

src/hawking.txt

`Intelligence is the ability to adapt to change.`

At this point, you can test your task by running it `./gradlew md5`:

$ gradle md5

The output should look similar to:

> Task :md5
Generating MD5 for einstein.txt...
Generating MD5 for feynman.txt...
Generating MD5 for hawking.txt...

BUILD SUCCESSFUL in 9s
3 actionable tasks: 3 executed

In the `build/md5` directory, you should now see corresponding files with an `md5` extension containing MD5 hashes of the files from the `src` directory. Notice that the task takes at least 9 seconds to run because it hashes each file one at a time (i.e., three files at ~3 seconds apiece).

### [](https://docs.gradle.org/userguide/worker_api.html#converting_to_worker_api)[Step 2. Convert to the Worker API](https://docs.gradle.org/userguide/worker_api.html#converting_to_worker_api)

Although this task processes each file in sequence, the processing of each file is independent of any other file. This work can be done in parallel and take advantage of multiple processors. This is where the Worker API can help.

To use the Worker API, you need to define an interface that represents the parameters of each unit of work and extends `org.gradle.workers.WorkParameters`.

For the generation of MD5 hash files, the unit of work will require two parameters:

1. the file to be hashed and,

2. the file to write the hash to.

There is no need to create a concrete implementation because Gradle will generate one for us at runtime.

buildSrc/src/main/java/MD5WorkParameters.java

```
import org.gradle.api.file.RegularFileProperty;
import org.gradle.workers.WorkParameters;

public interface MD5WorkParameters extends WorkParameters {
    RegularFileProperty getSourceFile(); (1)
    RegularFileProperty getMD5File();
}
```

**1**Use `Property` objects to represent the source and MD5 hash files.

Then, you need to refactor the part of your custom task that does the work for each individual file into a separate class. This class is your "unit of work" implementation, and it should be an abstract class that extends `org.gradle.workers.WorkAction`:

buildSrc/src/main/java/GenerateMD5.java

```
import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.io.FileUtils;
import org.gradle.workers.WorkAction;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

public abstract class GenerateMD5 implements WorkAction<MD5WorkParameters> { (1)
    @Override
    public void execute() {
        try {
            File sourceFile = getParameters().getSourceFile().getAsFile().get();
            File md5File = getParameters().getMD5File().getAsFile().get();
            InputStream stream = new FileInputStream(sourceFile);
            System.out.println("Generating MD5 for " + sourceFile.getName() + "...");
            // Artificially make this task slower.
            Thread.sleep(3000);
            FileUtils.writeStringToFile(md5File, DigestUtils.md5Hex(stream), (String) null);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```

**1**Do not implement the `getParameters()` method - Gradle will inject this at runtime.

Now, change your custom task class to submit work to the [WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html) instead of doing the work itself.

buildSrc/src/main/java/CreateMD5.java

```
import org.gradle.api.Action;
import org.gradle.api.file.RegularFile;
import org.gradle.api.provider.Provider;
import org.gradle.api.tasks.*;
import org.gradle.workers.*;
import org.gradle.api.file.DirectoryProperty;

import javax.inject.Inject;
import java.io.File;

abstract public class CreateMD5 extends SourceTask {

    @OutputDirectory
    abstract public DirectoryProperty getDestinationDirectory();

    @Inject
    abstract public WorkerExecutor getWorkerExecutor(); (1)

    @TaskAction
    public void createHashes() {
        WorkQueue workQueue = getWorkerExecutor().noIsolation(); (2)

        for (File sourceFile : getSource().getFiles()) {
            Provider<RegularFile> md5File = getDestinationDirectory().file(sourceFile.getName() + ".md5");
            workQueue.submit(GenerateMD5.class, parameters -> { (3)
                parameters.getSourceFile().set(sourceFile);
                parameters.getMD5File().set(md5File);
            });
        }
    }
}
```

**1**The [WorkerExecutor](https://docs.gradle.org/current/javadoc/org/gradle/workers/WorkerExecutor.html) service is required in order to submit your work. Create an abstract getter method annotated `javax.inject.Inject`, and Gradle will inject the service at runtime when the task is created.
**2**Before submitting work, get a `WorkQueue` object with the desired isolation mode (described below).
**3**When submitting the unit of work, specify the unit of work implementation, in this case `GenerateMD5`, and configure its parameters.

At this point, you should be able to rerun your task:

$ gradle clean md5

> Task :md5
Generating MD5 for einstein.txt...
Generating MD5 for feynman.txt...
Generating MD5 for hawking.txt...

BUILD SUCCESSFUL in 3s
3 actionable tasks: 3 executed

The results should look the same as before, although the MD5 hash files may be generated in a different order since the units of work are executed in parallel. This time, however, the task runs much faster. This is because the Worker API executes the MD5 calculation for each file in parallel rather than in sequence.

### [](https://docs.gradle.org/userguide/worker_api.html#step_3_change_the_isolation_mode)[Step 3. Change the isolation mode](https://docs.gradle.org/userguide/worker_api.html#step_3_change_the_isolation_mode)

The isolation mode controls how strongly Gradle will isolate items of work from each other and the rest of the Gradle runtime.

There are three methods on `WorkerExecutor` that control this:

1. `noIsolation()`

2. `classLoaderIsolation()`

3. `processIsolation()`

The `noIsolation()` mode is the lowest level of isolation and will prevent a unit of work from changing the project state. This is the fastest isolation mode because it requires the least overhead to set up and execute the work item. However, it will use a single shared classloader for all units of work. This means that each unit of work can affect one another through static class state. It also means that every unit of work uses the same version of libraries on the buildscript classpath. If you wanted the user to be able to configure the task to run with a different (but compatible) version of the [Apache Commons Codec](https://commons.apache.org/proper/commons-codec/) library, you would need to use a different isolation mode.

First, you must change the dependency in `buildSrc/build.gradle` to be `compileOnly`. This tells Gradle that it should use this dependency when building the classes, but should not put it on the build script classpath:

`Kotlin``Groovy`

buildSrc/build.gradle

```
repositories {
    mavenCentral()
}

dependencies {
    implementation 'commons-io:commons-io:2.5'
    compileOnly 'commons-codec:commons-codec:1.9'
}
```

Next, change the `CreateMD5` task to allow the user to configure the version of the codec library that they want to use. It will resolve the appropriate version of the library at runtime and configure the workers to use this version.

The `classLoaderIsolation()` method tells Gradle to run this work in a thread with an isolated classloader:

buildSrc/src/main/java/CreateMD5.java

```
import org.gradle.api.Action;
import org.gradle.api.file.ConfigurableFileCollection;
import org.gradle.api.file.DirectoryProperty;
import org.gradle.api.file.RegularFile;
import org.gradle.api.provider.Provider;
import org.gradle.api.tasks.*;
import org.gradle.process.JavaForkOptions;
import org.gradle.workers.*;

import javax.inject.Inject;
import java.io.File;
import java.util.Set;

abstract public class CreateMD5 extends SourceTask {

    @InputFiles
    abstract public ConfigurableFileCollection getCodecClasspath(); (1)

    @OutputDirectory
    abstract public DirectoryProperty getDestinationDirectory();

    @Inject
    abstract public WorkerExecutor getWorkerExecutor();

    @TaskAction
    public void createHashes() {
        WorkQueue workQueue = getWorkerExecutor().classLoaderIsolation(workerSpec -> {
            workerSpec.getClasspath().from(getCodecClasspath()); (2)
        });

        for (File sourceFile : getSource().getFiles()) {
            Provider<RegularFile> md5File = getDestinationDirectory().file(sourceFile.getName() + ".md5");
            workQueue.submit(GenerateMD5.class, parameters -> {
                parameters.getSourceFile().set(sourceFile);
                parameters.getMD5File().set(md5File);
            });
        }
    }
}
```

**1**Expose an input property for the codec library classpath.
**2**Configure the classpath on the [ClassLoaderWorkerSpec](https://docs.gradle.org/current/javadoc/org/gradle/workers/ClassLoaderWorkerSpec.html) when creating the work queue.

Next, you need to configure your build so that it has a repository to look up the codec version at task execution time. We also create a dependency to resolve our codec library from this repository:

`Kotlin``Groovy`

build.gradle

```
plugins { id 'base' }

repositories {
    mavenCentral() (1)
}

configurations.create('codec') { (2)
    attributes {
        attribute(Usage.USAGE_ATTRIBUTE, objects.named(Usage, Usage.JAVA_RUNTIME))
    }
    canBeConsumed = false
}

dependencies {
    codec 'commons-codec:commons-codec:1.10' (3)
}

tasks.register('md5', CreateMD5) {
    codecClasspath.from(configurations.codec) (4)
    destinationDirectory = project.layout.buildDirectory.dir('md5')
    source(project.layout.projectDirectory.file('src'))
}
```

**1**Add a repository to resolve the codec library - this can be a different repository than the one used to build the `CreateMD5` task class.
**2**Add a _configuration_ to resolve our codec library version.
**3**Configure an alternate, compatible version of [Apache Commons Codec](https://commons.apache.org/proper/commons-codec/).
**4**Configure the `md5` task to use the configuration as its classpath. Note that the configuration will not be resolved until the task is executed.

Now, if you run your task, it should work as expected using the configured version of the codec library:

$ gradle clean md5

> Task :md5
Generating MD5 for einstein.txt...
Generating MD5 for feynman.txt...
Generating MD5 for hawking.txt...

BUILD SUCCESSFUL in 3s
3 actionable tasks: 3 executed

### [](https://docs.gradle.org/userguide/worker_api.html#step_4_create_a_worker_daemon)[Step 4. Create a Worker Daemon](https://docs.gradle.org/userguide/worker_api.html#step_4_create_a_worker_daemon)

Sometimes, it is desirable to utilize even greater levels of isolation when executing items of work. For instance, external libraries may rely on certain system properties to be set, which may conflict between work items. Or a library might not be compatible with the version of JDK that Gradle is running with and may need to be run with a different version.

The Worker API can accommodate this using the `processIsolation()` method that causes the work to execute in a separate "worker daemon". These worker processes are session-scoped, meaning they live only for the duration of a single build and can be reused within that build. They do not persist across multiple builds. Gradle will stop these worker daemons when the build completes or if system resources get low during the build.

To utilize a worker daemon, use the `processIsolation()` method when creating the `WorkQueue`. You may also want to configure custom settings for the new process:

buildSrc/src/main/java/CreateMD5.java

```
import org.gradle.api.Action;
import org.gradle.api.file.ConfigurableFileCollection;
import org.gradle.api.file.DirectoryProperty;
import org.gradle.api.file.RegularFile;
import org.gradle.api.provider.Provider;
import org.gradle.api.tasks.*;
import org.gradle.process.JavaForkOptions;
import org.gradle.workers.*;

import javax.inject.Inject;
import java.io.File;
import java.util.Set;

abstract public class CreateMD5 extends SourceTask {

    @InputFiles
    abstract public ConfigurableFileCollection getCodecClasspath(); (1)

    @OutputDirectory
    abstract public DirectoryProperty getDestinationDirectory();

    @Inject
    abstract public WorkerExecutor getWorkerExecutor();

    @TaskAction
    public void createHashes() {
        (1)
        WorkQueue workQueue = getWorkerExecutor().processIsolation(workerSpec -> {
            workerSpec.getClasspath().from(getCodecClasspath());
            workerSpec.forkOptions(options -> {
                options.setMaxHeapSize("64m"); (2)
            });
        });

        for (File sourceFile : getSource().getFiles()) {
            Provider<RegularFile> md5File = getDestinationDirectory().file(sourceFile.getName() + ".md5");
            workQueue.submit(GenerateMD5.class, parameters -> {
                parameters.getSourceFile().set(sourceFile);
                parameters.getMD5File().set(md5File);
            });
        }
    }
}
```

**1**Change the isolation mode to `PROCESS`.
**2**Set up the [JavaForkOptions](https://docs.gradle.org/current/javadoc/org/gradle/process/JavaForkOptions.html) for the new process.

Now, you should be able to run your task, and it will work as expected but using worker daemons instead:

$ gradle clean md5

> Task :md5
Generating MD5 for einstein.txt...
Generating MD5 for feynman.txt...
Generating MD5 for hawking.txt...

BUILD SUCCESSFUL in 3s
3 actionable tasks: 3 executed

Note that the execution time may be high. This is because Gradle has to start a new process for each worker daemon, which is expensive.

However, if you run your task a second time, you will see that it runs much faster. This is because the worker daemon(s) started during the initial build have persisted and are available for use immediately during subsequent builds:

$ gradle clean md5

> Task :md5
Generating MD5 for einstein.txt...
Generating MD5 for feynman.txt...
Generating MD5 for hawking.txt...

BUILD SUCCESSFUL in 1s
3 actionable tasks: 3 executed
