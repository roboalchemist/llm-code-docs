# Source: https://docs.gradle.org/userguide/writing_tasks_intermediate.html

Title: Creating and Registering Tasks

URL Source: https://docs.gradle.org/userguide/writing_tasks_intermediate.html

Markdown Content:
The work that Gradle can do on a project is defined by one or more _tasks_.

![Image 1: gradle basic 14](https://docs.gradle.org/current/userguide/img/gradle-basic-14.png)

A **task** represents some independent unit of work that a build performs. This might be compiling some classes, creating a JAR, generating Javadoc, or publishing some archives to a repository.

When a user runs `./gradlew build` in the command line, Gradle will execute the `build`**task** along with any other tasks it depends on.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_types)[Task Types](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_types)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A **task type** defines what kind of work a **task** can do. It’s like a blueprint or class.

Gradle includes many **built-in task types**, such as `Copy`, `Jar`, and `Test`, and you can also define your own. By default, a **task** is of **type**[`DefaultTask`](https://docs.gradle.org/current/javadoc/org/gradle/api/DefaultTask.html) .

Let’s start with a simple custom task that prints a message:

`Kotlin``Groovy`

build.gradle

```
tasks.register('hello') {
    doLast {
        println 'Hello world!'
    }
}
```

You just registered a **task** called `hello` of **type**`DefaultTask` and gave it an action using `doLast{}`.

A task is **created** in the build script using the [`TaskContainer.register()`](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskContainer.html) method, which allows it to be then used in the build logic.

When you run the `hello` task in the command-line using `./gradlew hello`, it prints your message:

`$ ./gradlew hello`

`Hello world!`

When you **register** (i.e. create) a **task** in your build script, you can:

* Use the default **task type** (`DefaultTask`) and define the behavior inline.

* Use a **built-in task type**, like `Copy`, to take advantage of pre-defined behavior.

* Create and use a **custom task type** if you need reusable behavior across tasks.

This example registers a **task** called `copyTask` which copies `\*.war` files from the `source` directory to the `target` directory using the `Copy`**built-in task type**:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyTask', Copy) {
    from("source")
    into("target")
    include("*.war")
}
```

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#built_in_task_types)[Built-in Task Types](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#built_in_task_types)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle provides many **built-in task types** with common and popular functionality, such as copying or deleting files.

This registers a Gradle **task** named `removeOutput` of **type**`Delete`. When the **task** runs, it will delete the file `build/outputs/1.txt` relative to the project directory.

`Kotlin``Groovy`

build.gradle

```
tasks.register('removeOutput', Delete) {
    delete layout.buildDirectory.file("outputs/1.txt")
}
```

There are many **task types** developers can take advantage of, including `GroovyDoc`, `Zip`, `Jar`, `JacocoReport`, `Sign`, or `Delete`, which are detailed in the [DSL](link:../dsl/org.gradle.api.plugins.antlr.AntlrTask.html).

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:sample_task)[Custom Task Types](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:sample_task)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Gradle **tasks** are a subclass of [`Task`](https://docs.gradle.org/current/javadoc/org/gradle/api/Task.html).

In the example below, the `HelloTask` class, a **custom task type**, is created by extending [`DefaultTask`](https://docs.gradle.org/current/javadoc/org/gradle/api/DefaultTask.html) (our default task type):

`Kotlin``Groovy`

build.gradle

```
// Extend the DefaultTask class to create a HelloTask class
class HelloTask extends DefaultTask {
    @TaskAction
    void hello() {
        println("hello from HelloTask")
    }
}

// Register the hello Task with type HelloTask
tasks.register("hello", HelloTask) {
    group = "Custom tasks"
    description = "A lovely greeting task."
}
```

The `hello`**task** is registered with the new **type**`HelloTask`.

Executing our new `hello`**task** results in the following:

`$ ./gradlew hello`

```
> Task :app:hello
hello from HelloTask
```

The Gradle `help`**task** can reveal the specifications of the `hello` task:

`$ ./gradlew help --task hello`

```
> Task :help
Detailed task information for hello

Path
:app:hello

Type
HelloTask (Build_gradle$HelloTask)

Options
--rerun     Causes the task to be re-run even if up-to-date.

Description
A lovely greeting task.

Group
Custom tasks
```

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_inputs_and_outputs)[Task Input and Outputs](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_inputs_and_outputs)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For a **custom task** to do useful work, it typically needs some **inputs** which it uses to produce **outputs**.

A **task** can declare those **inputs** (files, values) and **outputs** (files it creates). Ideally, these inputs and outputs leverage Gradle managed types. This helps Gradle skip work when nothing has changed:

`Kotlin``Groovy`

build.gradle

```
abstract class CreateAFileTask extends DefaultTask {
    @Input
    abstract Property<String> getFileText()

    @Input
    final String fileName = "myfile.txt"

    @OutputFile
    final File myFile = new File(fileName)

    @TaskAction
    void action() {
        myFile.createNewFile()
        myFile.text = fileText.get()
    }
}
```

Now Gradle knows what the **task** needs and what it produces. If nothing changes, the **task** is skipped.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_action)[Task Action](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_action)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Task actions** are the blocks of code that define what the **custom task** does when it runs.

Every **task** can have one or more actions, and they’re executed during the execution phase of the Gradle build lifecycle.

In the example below, a **custom task type** is created called `GreetingTask`. The `@TaskAction` annotation marks a method that Gradle should call when the **task** of this **type** is executed:

`Kotlin``Groovy`

build.gradle

```
abstract class GreetingTask extends DefaultTask {
    @TaskAction
    def greet() {
        println 'hello from GreetingTask'
    }
}

// Create a task using the task type
tasks.register('hello', GreetingTask)
```

A **task action** can also be added using `doLast {}` or `doFirst {}`:

`Kotlin``Groovy`

build.gradle

```
tasks.register('hello') {
    doLast {
        println 'Hello world!'
    }
}
```

In this example, the **action** is `println("Hello world!")`. It will run when the **task** is executed.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_group_and_description)[Task Group and Description](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_group_and_description)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Group** and **description** are metadata properties used to organize and document tasks. They are primarily used to make the project easier to navigate for developers.

1. The group acts as a **category** for the task. When you run `./gradlew tasks`, Gradle clusters all tasks with the same group name together.

2. The description is a **short summary** explaining what the task actually does.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:task_dependencies)[Task Dependencies](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:task_dependencies)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can declare **tasks** that depend on other **tasks**:

`Kotlin``Groovy`

build.gradle

```
tasks.register('hello') {
    doLast {
        println 'Hello world!'
    }
}
tasks.register('intro') {
    dependsOn tasks.hello
    doLast {
        println "I'm Gradle"
    }
}
```

`$ gradle -q intro`

```
Hello world!
I'm Gradle
```

The dependency of `taskX` to `taskY` may be declared before `taskY` is defined:

`Kotlin``Groovy`

build.gradle

```
tasks.register('taskX') {
    dependsOn 'taskY'
    doLast {
        println 'taskX'
    }
}
tasks.register('taskY') {
    doLast {
        println 'taskY'
    }
}
```

`$ ./gradlew -q taskX`

```
taskY
taskX
```

The `hello`**task** from the previous example is updated to include a dependency:

`Kotlin``Groovy`

build.gradle

```
tasks.register('hello') {
    group = "Custom"
    description = "A lovely greeting task."
    doLast {
        println("Hello world!")
    }
    dependsOn(tasks.assemble)
}
```

The `hello`**task** now depends on the `assemble`**task**, which means that Gradle must execute the `assemble`**task****before** it can execute the `hello`**task**:

`$ ./gradlew :app:hello`

```
> Task :app:compileJava UP-TO-DATE
> Task :app:processResources NO-SOURCE
> Task :app:classes UP-TO-DATE
> Task :app:jar UP-TO-DATE
> Task :app:startScripts UP-TO-DATE
> Task :app:distTar UP-TO-DATE
> Task :app:distZip UP-TO-DATE
> Task :app:assemble UP-TO-DATE

> Task :app:hello
Hello world!
```

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:manipulating_existing_tasks)[Task Configuration](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#sec:manipulating_existing_tasks)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once registered, **tasks** can be accessed via the [`TaskProvider`](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html) API for further configuration.

For instance, you can add behavior to an existing **task**:

`Kotlin``Groovy`

build.gradle

```
tasks.register('hello') {
    doLast {
        println 'Hello Earth'
    }
}
tasks.named('hello') {
    doFirst {
        println 'Hello Venus'
    }
}
tasks.named('hello') {
    doLast {
        println 'Hello Mars'
    }
}
tasks.named('hello') {
    doLast {
        println 'Hello Jupiter'
    }
}
```

`$ ./gradlew -q hello`

```
Hello Venus
Hello Earth
Hello Mars
Hello Jupiter
```

The calls `doFirst` and `doLast` can be executed multiple times. They add an action to the beginning or the end of the task’s actions list. When the task executes, the actions in the action list are executed in order.

A task is optionally **configured** in a build script using the [`TaskCollection.named()`](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskCollection.html) method.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_classification)[Task Classification](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_classification)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two classes of tasks that can be executed:

1. **Actionable tasks** have some action(s) attached to do work in your build: `compileJava`.

2. **Lifecycle tasks** are tasks with no actions attached: `assemble`, `build`.

Typically, a **lifecycle** tasks depends on many **actionable** tasks, and is used to execute many tasks at once.

[](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_performance)[Task Performance](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#task_performance)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To write "good" Gradle tasks, you should focus on three things: **speed**, **clarity**, and **intelligence**.

### [](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#1_load_configuration_lazily)[1. Load configuration lazily](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#1_load_configuration_lazily)

A "fast" task is one that loads configuration lazily.

Use lazy APIs like `tasks.register()` instead of eager ones like `tasks.create()`. `register()` tells Gradle to only configure the task if someone actually runs it. If you use `create()`, Gradle sets up that task every single time you do **anything** (even just checking the version), which adds up to a very slow experience.

### [](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#2_define_inputs_and_outputs)[2. Define inputs and outputs](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#2_define_inputs_and_outputs)

A "clear" task is one that knows when it doesn’t need to run.

By defining your inputs and outputs, Gradle can perform **up-to-date checks**. If you run the task twice and nothing has changed, Gradle should say `UP-TO-DATE` and finish in milliseconds.

### [](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#3_do_work_during_execution)[3. Do work during execution](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#3_do_work_during_execution)

A "smart" task does the work during the Execution Phase, not the Configuration Phase.

One of the most common beginner mistakes is putting code in the wrong place:

* **Configuration Block:** Use this only to set up settings (like the `group` or `description`).

* **Execution Block (`doLast` or `@TaskAction`):** Use this for the actual work (moving files, compiling code, etc.)

### [](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#4_document_your_work)[4. Document Your Work](https://docs.gradle.org/userguide/writing_tasks_intermediate.html#4_document_your_work)

A "good" task defines a `group` and a `description`. When a teammate runs `./gradlew tasks`, your custom task will appear in a neat category with a clear explanation of what it does, rather than being buried in the "Other" category.
