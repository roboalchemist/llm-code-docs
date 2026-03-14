# Source: https://docs.gradle.org/userguide/working_with_files.html

Title: Working With Files

URL Source: https://docs.gradle.org/userguide/working_with_files.html

Markdown Content:
File operations are fundamental to nearly every Gradle build. They involve handling source files, managing file dependencies, and generating reports. Gradle provides a robust API that simplifies these operations, enabling developers to perform necessary file tasks easily.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:hard_coded_file_paths)[Hardcoded paths and laziness](https://docs.gradle.org/userguide/working_with_files.html#sec:hard_coded_file_paths)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is best practice to **avoid** hardcoded paths in build scripts.

In addition to avoiding hardcoded paths, Gradle encourages laziness in its build scripts. This means that tasks and operations should be deferred until they are actually needed rather than executed eagerly.

Many examples in this chapter use hard-coded paths as string literals. This makes them easy to understand, but it is not good practice. The problem is that paths often change, and the more places you need to change them, the more likely you will miss one and break the build.

Where possible, you should use tasks, task properties, and [project properties](https://docs.gradle.org/current/userguide/properties_providers.html#understanding_properties) — in that order of preference — to configure file paths.

For example, if you create a task that packages the compiled classes of a Java application, you should use an implementation similar to this:

`Kotlin``Groovy`

build.gradle

```
def archivesDirPath = layout.buildDirectory.dir('archives')

tasks.register('packageClasses', Zip) {
    archiveAppendix = "classes"
    destinationDirectory = archivesDirPath

    from compileJava
}
```

The `compileJava` task is the source of the files to package, and the project property `archivesDirPath` stores the location of the archives, as we are likely to use it elsewhere in the build.

Using a task directly as an argument like this relies on it having [defined outputs](https://docs.gradle.org/current/userguide/incremental_build.html#sec:task_inputs_outputs), so it won’t always be possible. This example could be further improved by relying on the Java plugin’s convention for `destinationDirectory` rather than overriding it, but it does demonstrate the use of project properties.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:locating_files)[Locating files](https://docs.gradle.org/userguide/working_with_files.html#sec:locating_files)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To perform some action on a file, you need to know where it is, and that’s the information provided by file paths. Gradle builds on the standard Java `File` class, which represents the location of a single file and provides APIs for dealing with collections of paths.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_projectlayout)[Using `ProjectLayout`](https://docs.gradle.org/userguide/working_with_files.html#using_projectlayout)

The [`ProjectLayout`](https://docs.gradle.org/current/dsl/org.gradle.api.file.ProjectLayout.html) class is used to access various directories and files within a project. It provides methods to retrieve paths to the project directory, build directory, settings file, and other important locations within the project’s file structure. This class is particularly useful when you need to work with files in a build script or plugin in different project paths:

`Kotlin``Groovy`

build.gradle

`def archivesDirPath = layout.buildDirectory.dir('archives')`

You can learn more about the `ProjectLayout` class in [Services](https://docs.gradle.org/current/userguide/service_injection.html#sec:projectlayout).

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:single_file_paths)[Using `Project.file()`](https://docs.gradle.org/userguide/working_with_files.html#sec:single_file_paths)

Relative paths are resolved relative to the project directory, while absolute paths remain unchanged.

Never use `new File(relative path)` unless passed to `file()` or `files()` or `from()` or other methods defined in terms of `file()` or `files()`. Otherwise, this creates a path relative to the current working directory (CWD). Gradle can make no guarantees about the location of the CWD, which means builds that rely on it may break at any time.

Here are some examples of using the `file()` method with different types of arguments:

`Kotlin``Groovy`

build.gradle

```
// Using a relative path
File configFile = file('src/config.xml')

// Using an absolute path
configFile = file(configFile.absolutePath)

// Using a File object with a relative path
configFile = file(new File('src/config.xml'))

// Using a java.nio.file.Path object with a relative path
configFile = file(Paths.get('src', 'config.xml'))

// Using an absolute java.nio.file.Path object
configFile = file(Paths.get(System.getProperty('user.home')).resolve('global-config.xml'))
```

As you can see, you can pass strings, `File` instances and `Path` instances to the `file()` method, all of which result in an absolute `File` object.

In the case of multi-project builds, the `file()` method will always turn relative paths into paths relative to the current project directory, which may be a child project.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_projectlayout_settingsdirectory)[Using `ProjectLayout.settingsDirectory()`](https://docs.gradle.org/userguide/working_with_files.html#using_projectlayout_settingsdirectory)

To use a path relative to the _settings_ directory, access the [`Project.layout`](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:layout), retrieve the [`settingsDirectory`](https://docs.gradle.org/current/dsl/org.gradle.api.file.ProjectLayout.html#org.gradle.api.file.ProjectLayout:settingsDirectory) from it, and construct an absolute path.

For example:

`Kotlin``Groovy`

build.gradle

`File configFile = layout.settingsDirectory.file("shared/config.xml").asFile`

Let’s say you’re working on a multi-project build in the directory: `dev/projects/AcmeHealth`. The build script above is at: `AcmeHealth/subprojects/AcmePatientRecordLib/build.gradle`. The absolute file path will resolve to: `dev/projects/AcmeHealth/shared/config.xml`:

```
dev
├── projects
│   ├── AcmeHealth
│   │   ├── subprojects
│   │   │   ├── AcmePatientRecordLib
│   │   │   │   └── build.gradle
│   │   │   └── ...
│   │   ├── shared
│   │   │   └── config.xml
│   │   └── ...
│   └── ...
└── settings.gradle
```

Note that `Project` also provides [Project.getRootProject()](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:rootProject) for multi-project builds which, in the example, would resolve to: `dev/projects/AcmeHealth/subprojects/AcmePatientRecordLib`.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:file_collections)[Using `FileCollection`](https://docs.gradle.org/userguide/working_with_files.html#sec:file_collections)

A _file collection_ is simply a set of file paths represented by the [FileCollection](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html) interface.

The set of paths can be _any_ file path. The file paths don’t have to be related in any way, so they don’t have to be in the same directory or have a shared parent directory.

The recommended way to specify a collection of files is to use the [ProjectLayout.files(java.lang.Object...)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ProjectLayout.html#files-java.lang.Object...-) method, which returns a `FileCollection` instance. This flexible method allows you to pass multiple strings, `File` instances, collections of strings, collections of `File`s, and more. You can also pass in tasks as arguments if they have [defined outputs](https://docs.gradle.org/current/userguide/incremental_build.html#sec:task_inputs_outputs).

`files()` properly handles relative paths and `File(relative path)` instances, resolving them relative to the project directory.

As with the [Project.file(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:file(java.lang.Object)) method covered in the [previous section](https://docs.gradle.org/userguide/working_with_files.html#sec:single_file_paths), all relative paths are evaluated relative to the current project directory. The following example demonstrates some of the variety of argument types you can use — strings, `File` instances, lists, or `Paths`:

`Kotlin``Groovy`

build.gradle

```
FileCollection collection = layout.files('src/file1.txt',
                                  new File('src/file2.txt'),
                                  ['src/file3.csv', 'src/file4.csv'],
                                  Paths.get('src', 'file5.txt'))
```

File collections have important attributes in Gradle. They can be:

* created lazily

* iterated over

* filtered

* combined

_Lazy creation_ of a file collection is useful when evaluating the files that make up a collection when a build runs. In the following example, we query the file system to find out what files exist in a particular directory and then make those into a file collection:

`Kotlin``Groovy`

build.gradle

```
tasks.register('list') {
    Directory projectDirectory = layout.projectDirectory
    doLast {
        File srcDir

        // Create a file collection using a closure
        collection = projectDirectory.files { srcDir.listFiles() }

        srcDir = projectDirectory.file('src').asFile
        println "Contents of $srcDir.name"
        collection.collect { projectDirectory.asFile.relativePath(it) }.sort().each { println it }

        srcDir = projectDirectory.file('src2').asFile
        println "Contents of $srcDir.name"
        collection.collect { projectDirectory.asFile.relativePath(it) }.sort().each { println it }
    }
}
```

`$ ./gradlew -q list`

```
Contents of src
src/dir1
src/file1.txt
Contents of src2
src2/dir1
src2/dir2
```

The key to lazy creation is passing a closure (in Groovy) or a `Provider` (in Kotlin) to the `files()` method. Your closure or provider must return a value of a type accepted by `files()`, such as `List<File>`, `String`, or `FileCollection`.

_Iterating over a file collection_ can be done through the `each()` method (in Groovy) or `forEach` method (in Kotlin) on the collection or using the collection in a `for` loop. In both approaches, the file collection is treated as a set of `File` instances, i.e., your iteration variable will be of type `File`.

The following example demonstrates such iteration. It also demonstrates how you can convert file collections to other types using the `as` operator (or supported properties):

`Kotlin``Groovy`

build.gradle

```
// Iterate over the files in the collection
collection.each { File file ->
    println file.name
}

// Convert the collection to various types
Set set = collection.files
Set set2 = collection as Set
List list = collection as List
String path = collection.asPath
File file = collection.singleFile

// Add and subtract collections
def union = collection + projectLayout.files('src/file2.txt')
def difference = collection - projectLayout.files('src/file2.txt')
```

You can also see at the end of the example _how to combine file collections_ using the `+` and `-` operators to merge and subtract them. An important feature of the resulting file collections is that they are _live_. In other words, when you combine file collections this way, the result always reflects what’s currently in the source file collections, even if they change during the build.

For example, imagine `collection` in the above example gains an extra file or two after `union` is created. As long as you use `union` after those files are added to `collection`, `union` will also contain those additional files. The same goes for the `different` file collection.

Live collections are also important when it comes to _filtering_. Suppose you want to use a subset of a file collection. In that case, you can take advantage of the [FileCollection.filter(org.gradle.api.specs.Spec)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileCollection.html#filter-org.gradle.api.specs.Spec-) method to determine which files to "keep". In the following example, we create a new collection that consists of only the files that end with `.txt` in the source collection:

`Kotlin``Groovy`

build.gradle

```
FileCollection textFiles = collection.filter { File f ->
    f.name.endsWith(".txt")
}
```

`$ ./gradlew -q filterTextFiles`

```
src/file1.txt
src/file2.txt
src/file5.txt
```

If `collection` changes at any time, either by adding or removing files from itself, then `textFiles` will immediately reflect the change because it is also a live collection. Note that the closure you pass to `filter()` takes a `File` as an argument and should return a boolean.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:specifying_multiple_files)[Understanding implicit conversion to file collections](https://docs.gradle.org/userguide/working_with_files.html#sec:specifying_multiple_files)

Many objects in Gradle have properties which accept a set of input files. For example, the [JavaCompile](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.compile.JavaCompile.html) task has a `source` property that defines the source files to compile. You can set the value of this property using any of the types supported by the [files()](https://docs.gradle.org/userguide/working_with_files.html#sec:file_collections) method, as mentioned in the API docs. This means you can, for example, set the property to a `File`, `String`, collection, `FileCollection` or even a closure or `Provider`.

**This is a feature of specific tasks**! That means implicit conversion will not happen for just any task that has a `FileCollection` or `FileTree` property. If you want to know whether implicit conversion happens in a particular situation, you will need to read the relevant documentation, such as the corresponding task’s API docs. Alternatively, you can remove all doubt by explicitly using [ProjectLayout.files(java.lang.Object...)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/ProjectLayout.html#files-java.lang.Object...-) in your build.

Here are some examples of the different types of arguments that the `source` property can take:

`Kotlin``Groovy`

build.gradle

```
tasks.register('compile', JavaCompile) {

    // Use a File object to specify the source directory
    source = file('src/main/java')

    // Use a String path to specify the source directory
    source = 'src/main/java'

    // Use a collection to specify multiple source directories
    source = ['src/main/java', '../shared/java']

    // Use a FileCollection (or FileTree in this case) to specify the source files
    source = fileTree(dir: 'src/main/java').matching { include 'org/gradle/api/**' }

    // Using a closure to specify the source files.
    source = {
        // Use the contents of each zip file in the src dir
        file('src').listFiles().findAll {it.name.endsWith('.zip')}.collect { zipTree(it) }
    }
}
```

One other thing to note is that properties like `source` have corresponding methods in core Gradle tasks. Those methods follow the convention of _appending_ to collections of values rather than replacing them. Again, this method accepts any of the types supported by the [files()](https://docs.gradle.org/userguide/working_with_files.html#sec:file_collections) method, as shown here:

`Kotlin``Groovy`

build.gradle

```
compile {
    // Add some source directories use String paths
    source 'src/main/java', 'src/main/groovy'

    // Add a source directory using a File object
    source file('../shared/java')

    // Add some source directories using a closure
    source { file('src/test/').listFiles() }
}
```

As this is a common convention, we recommend that you follow it in your own custom tasks. Specifically, if you plan to add a method to configure a collection-based property, make sure the method appends rather than replaces values.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:file_trees)[Using `FileTree`](https://docs.gradle.org/userguide/working_with_files.html#sec:file_trees)

A _file tree_ is a file collection that retains the directory structure of the files it contains and has the type [FileTree](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTree.html). This means all the paths in a file tree must have a shared parent directory. The following diagram highlights the distinction between file trees and file collections in the typical case of copying files:

![Image 1: file collection vs file tree](https://docs.gradle.org/current/userguide/img/file-collection-vs-file-tree.png)

Although `FileTree` extends `FileCollection` (an is-a relationship), their behaviors differ. In other words, you can use a file tree wherever a file collection is required, but remember that a file collection is a flat list/set of files, while a file tree is a file and directory hierarchy. To convert a file tree to a flat collection, use the [FileTree.getFiles()](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTree.html#getFiles--) property.

The simplest way to create a file tree is to pass a file or directory path to the [Project.fileTree(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:fileTree(java.lang.Object)) method. This will create a tree of all the files and directories in that base directory (but not the base directory itself). The following example demonstrates how to use this method and how to filter the files and directories using Ant-style patterns:

`Kotlin``Groovy`

build.gradle

```
// Create a file tree with a base directory
ConfigurableFileTree tree = fileTree(dir: 'src/main')

// Add include and exclude patterns to the tree
tree.include '**/*.java'
tree.exclude '**/Abstract*'

// Create a tree using closure
tree = fileTree('src') {
    include '**/*.java'
}

// Create a tree using a map
tree = fileTree(dir: 'src', include: '**/*.java')
tree = fileTree(dir: 'src', includes: ['**/*.java', '**/*.xml'])
tree = fileTree(dir: 'src', include: '**/*.java', exclude: '**/*test*/**')
```

You can see more examples of supported patterns in the API docs for [PatternFilterable](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/util/PatternFilterable.html).

By default, `fileTree()` returns a `FileTree` instance that applies some default exclude patterns for convenience — the same defaults as Ant. For the complete default exclude list, see [the Ant manual](http://ant.apache.org/manual/dirtasks.html#defaultexcludes).

If those default excludes prove problematic, you can work around the issue by changing the default excludes in the settings script:

`Kotlin``Groovy`

settings.gradle

```
import org.apache.tools.ant.DirectoryScanner

DirectoryScanner.removeDefaultExclude('**/.git')
DirectoryScanner.removeDefaultExclude('**/.git/**')
```

Gradle does not support changing default excludes during the execution phase.

You can do many of the same things with file trees that you can with file collections:

* iterate over them (depth first)

* filter them (using [FileTree.matching(org.gradle.api.Action)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTree.html#matching-org.gradle.api.Action-) and Ant-style patterns)

* merge them

You can also traverse file trees using the [FileTree.visit(org.gradle.api.Action)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTree.html#visit-org.gradle.api.Action-) method. All of these techniques are demonstrated in the following example:

`Kotlin``Groovy`

build.gradle

```
// Iterate over the contents of a tree
tree.each {File file ->
    println file
}

// Filter a tree
FileTree filtered = tree.matching {
    include 'org/gradle/api/**'
}

// Add trees together
FileTree sum = tree + fileTree(dir: 'src/test')

// Visit the elements of the tree
tree.visit {element ->
    println "$element.relativePath => $element.file"
}
```

[](https://docs.gradle.org/userguide/working_with_files.html#copying_files)[Copying files](https://docs.gradle.org/userguide/working_with_files.html#copying_files)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Copying files in Gradle primarily uses `CopySpec`, a mechanism that makes it easy to manage resources such as source code, configuration files, and other assets in your project build process.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:using_the_copyspec_class)[Understanding `CopySpec`](https://docs.gradle.org/userguide/working_with_files.html#sec:using_the_copyspec_class)

`CopySpec` is a copy specification that allows you to define what files to copy, where to copy them from, and where to copy them. It provides a flexible and expressive way to specify complex file copying operations, including filtering files based on patterns, renaming files, and including/excluding files based on various criteria.

`CopySpec` instances are used in the `Copy` task to specify the files and directories to be copied.

`CopySpec` has two important attributes:

1. It is independent of tasks, allowing you to _share copy specs within a build_.

2. It is hierarchical, providing _fine-grained control_ within the overall copy specification.

#### [](https://docs.gradle.org/userguide/working_with_files.html#sub:sharing_copy_specs)[1. Sharing copy specs](https://docs.gradle.org/userguide/working_with_files.html#sub:sharing_copy_specs)

Consider a build with several tasks that copy a project’s static website resources or add them to an archive. One task might copy the resources to a folder for a local HTTP server, and another might package them into a distribution. You could manually specify the file locations and appropriate inclusions each time they are needed, but human error is more likely to creep in, resulting in inconsistencies between tasks.

`Kotlin``Groovy`

build.gradle

```
CopySpec webAssetsSpec = copySpec {
    from 'src/main/webapp'
    include '**/*.html', '**/*.png', '**/*.jpg'
    rename '(.+)-staging(.+)', '$1$2'
}

tasks.register('copyAssets', Copy) {
    into layout.buildDirectory.dir("inPlaceApp")
    with webAssetsSpec
}

tasks.register('distApp', Zip) {
    archiveFileName = 'my-app-dist.zip'
    destinationDirectory = layout.buildDirectory.dir('dists')

    from appClasses
    with webAssetsSpec
}
```

Both the `copyAssets` and `distApp` tasks will process the static resources under `src/main/webapp`, as specified by `webAssetsSpec`.

The configuration defined by `webAssetsSpec` will _not_ apply to the app classes included by the `distApp` task. That’s because `from appClasses` is its own child specification independent of `with webAssetsSpec`.

This can be confusing, so it’s probably best to treat `with()` as an extra `from()` specification in the task. Hence, it doesn’t make sense to define a standalone copy spec without at least one `from()` defined.

Suppose you encounter a scenario in which you want to apply the same copy configuration to _different_ sets of files. In that case, you can share the configuration block directly without using `copySpec()`. Here’s an example that has two independent tasks that happen to want to process image files only:

`Kotlin``Groovy`

build.gradle

```
def webAssetPatterns = {
    include '**/*.html', '**/*.png', '**/*.jpg'
}

tasks.register('copyAppAssets', Copy) {
    into layout.buildDirectory.dir("inPlaceApp")
    from 'src/main/webapp', webAssetPatterns
}

tasks.register('archiveDistAssets', Zip) {
    archiveFileName = 'distribution-assets.zip'
    destinationDirectory = layout.buildDirectory.dir('dists')

    from 'distResources', webAssetPatterns
}
```

In this case, we assign the copy configuration to its own variable and apply it to whatever `from()` specification we want. This doesn’t just work for inclusions but also exclusions, file renaming, and file content filtering.

#### [](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications)[2. Using child specifications](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications)

If you only use a single copy spec, the file filtering and renaming will apply to _all_ files copied. Sometimes, this is what you want, but not always. Consider the following example that copies files into a directory structure that a Java Servlet container can use to deliver a website:

![Image 2: exploded war child copy spec example](https://docs.gradle.org/current/userguide/img/exploded-war-child-copy-spec-example.png)

This is not a straightforward copy as the `WEB-INF` directory and its subdirectories don’t exist within the project, so they must be created during the copy. In addition, we only want HTML and image files going directly into the root folder — `build/explodedWar` — and only JavaScript files going into the `js` directory. We need separate filter patterns for those two sets of files.

The solution is to use _child specifications_, which can be applied to both `from()` and `into()` declarations. The following task definition does the necessary work:

`Kotlin``Groovy`

build.gradle

```
tasks.register('nestedSpecs', Copy) {
    into layout.buildDirectory.dir("explodedWar")
    exclude '**/*staging*'
    from('src/dist') {
        include '**/*.html', '**/*.png', '**/*.jpg'
    }
    from(sourceSets.main.output) {
        into 'WEB-INF/classes'
    }
    into('WEB-INF/lib') {
        from configurations.runtimeClasspath
    }
}
```

Notice how the `src/dist` configuration has a nested inclusion specification; it is the child copy spec. You can, of course, add content filtering and renaming here as required. A child copy spec is still a copy spec.

The above example also demonstrates how you can copy files into a subdirectory of the destination either by using a child `into()` on a `from()` or a child `from()` on an `into()`. Both approaches are acceptable, but you should create and follow a convention to ensure consistency across your build files.

Don’t get your `into()` specifications mixed up. For a normal copy, one to the filesystem rather than an archive, there should always be _one_ "root" `into()` that specifies the overall destination directory of the copy. Any other `into()` should have a child spec attached, and its path will be relative to the root `into()`.

One final thing to be aware of is that a child copy spec inherits its destination path, include patterns, exclude patterns, copy actions, name mappings, and filters from its parent. So, be careful where you place your configuration.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:sync_task)[Using the `Sync` task](https://docs.gradle.org/userguide/working_with_files.html#sec:sync_task)

The [Sync](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.Sync.html) task, which extends the `Copy` task, copies the source files into the destination directory and then removes any files from the destination directory which it did not copy. It synchronizes the contents of a directory with its source.

This can be useful for doing things such as installing your application, creating an exploded copy of your archives, or maintaining a copy of the project’s dependencies.

Here is an example that maintains a copy of the project’s runtime dependencies in the `build/libs` directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('libs', Sync) {
    from configurations.runtime
    into layout.buildDirectory.dir('libs')
}
```

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_single_file_example)[Using the `Copy` task](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_single_file_example)

You can copy a file by creating an instance of Gradle’s builtin [Copy](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.Copy.html) task and configuring it with the location of the file and where you want to put it.

This example mimics copying a generated report into a directory that will be packed into an archive, such as a ZIP or TAR:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyReport', Copy) {
    from layout.buildDirectory.file("reports/my-report.pdf")
    into layout.buildDirectory.dir("toArchive")
}
```

Although hard-coded paths make for simple examples, they make the build brittle. Using a reliable, single source of truth, such as a task or shared project property, is better. In the following modified example, we use a report task defined elsewhere that has the report’s location stored in its `outputFile` property:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyReport2', Copy) {
    from myReportTask.outputFile
    into archiveReportsTask.dirToArchive
}
```

We have also assumed that the reports will be archived by `archiveReportsTask`, which provides us with the directory that will be archived and hence where we want to put the copies of the reports.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_multiple_files_example)[Copying multiple files](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_multiple_files_example)

You can extend the previous examples to multiple files very easily by providing multiple arguments to `from()`:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyReportsForArchiving', Copy) {
    from layout.buildDirectory.file("reports/my-report.pdf"), layout.projectDirectory.file("src/docs/manual.pdf")
    into layout.buildDirectory.dir("toArchive")
}
```

Two files are now copied into the archive directory.

You can also use multiple `from()` statements to do the same thing, as shown in the first example of the section [File copying in depth](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_files).

But what if you want to copy all the PDFs in a directory without specifying each one? To do this, attach inclusion and/or exclusion patterns to the copy specification. Here, we use a string pattern to include PDFs only:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyPdfReportsForArchiving', Copy) {
    from layout.buildDirectory.dir("reports")
    include "*.pdf"
    into layout.buildDirectory.dir("toArchive")
}
```

One thing to note, as demonstrated in the following diagram, is that only the PDFs that reside directly in the `reports` directory are copied:

![Image 3: copy with flat filter example](https://docs.gradle.org/current/userguide/img/copy-with-flat-filter-example.png)

You can include files in subdirectories by using an Ant-style glob pattern (`**/*`), as done in this updated example:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyAllPdfReportsForArchiving', Copy) {
    from layout.buildDirectory.dir("reports")
    include "**/*.pdf"
    into layout.buildDirectory.dir("toArchive")
}
```

This task has the following effect:

![Image 4: copy with deep filter example](https://docs.gradle.org/current/userguide/img/copy-with-deep-filter-example.png)

Remember that a deep filter like this has the side effect of copying the directory structure below `reports` and the files. If you want to copy the files without the directory structure, you must use an explicit `fileTree(dir) { includes }.files` expression.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_directories_example)[Copying directory hierarchies](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_directories_example)

You may need to copy files as well as the directory structure in which they reside. This is the default behavior when you specify a directory as the `from()` argument, as demonstrated by the following example that copies everything in the `reports` directory, including all its subdirectories, to the destination:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyReportsDirForArchiving', Copy) {
    from layout.buildDirectory.dir("reports")
    into layout.buildDirectory.dir("toArchive")
}
```

The key aspect that users need help with is controlling how much of the directory structure goes to the destination. In the above example, do you get a `toArchive/reports` directory, or does everything in `reports` go straight into `toArchive`? The answer is the latter. If a directory is part of the `from()` path, then it _won’t_ appear in the destination.

So how do you ensure that `reports` itself is copied across, but not any other directory in `${layout.buildDirectory}`? The answer is to add it as an include pattern:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyReportsDirForArchiving2', Copy) {
    from(layout.buildDirectory) {
        include "reports/**"
    }
    into layout.buildDirectory.dir("toArchive")
}
```

You’ll get the same behavior as before except with one extra directory level in the destination, i.e., `toArchive/reports`.

One thing to note is how the `include()` directive applies only to the `from()`, whereas the directive in the previous section applied to the whole task. These different [levels of granularity](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications) in the copy specification allow you to handle most requirements that you will come across easily.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_files)[Understanding file copying](https://docs.gradle.org/userguide/working_with_files.html#sec:copying_files)

The basic process of copying files in Gradle is a simple one:

* Define a task of type [Copy](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.Copy.html)

* Specify which files (and potentially directories) to copy

* Specify a destination for the copied files

But this apparent simplicity hides a rich API that allows fine-grained control of which files are copied, where they go, and what happens to them as they are copied — renaming of the files and token substitution of file content are both possibilities, for example.

Let’s start with the last two items on the list, which involve [`CopySpec`](https://docs.gradle.org/userguide/working_with_files.html#sec:using_the_copyspec_class). The [CopySpec](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html) interface, which the `Copy` task implements, offers:

* A [CopySpec.from(java.lang.Object…​)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html#from-java.lang.Object...-) method to define what to copy

* An [CopySpec.into(java.lang.Object)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html#into-java.lang.Object-) method to define the destination

`CopySpec` has several additional methods that allow you to control the copying process, but these two are the only required ones. `into()` is straightforward, requiring a directory path as its argument in any form supported by the [Project.file(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:file(java.lang.Object)) method. The `from()` configuration is far more flexible.

Not only does `from()` accept multiple arguments, it also allows several different types of argument. For example, some of the most common types are:

* A `String` — treated as a file path or, if it starts with "file://", a file URI

* A `File` — used as a file path

* A `FileCollection` or `FileTree` — all files in the collection are included in the copy

* A task — the files or directories that form a task’s [defined outputs](https://docs.gradle.org/current/userguide/incremental_build.html#sec:task_inputs_outputs) are included

In fact, `from()` accepts all the same arguments as [Project.files(java.lang.Object…​)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:files(java.lang.Object[])) so see that method for a more detailed list of acceptable types.

Something else to consider is what type of thing a file path refers to:

* A file — the file is copied as is

* A directory — this is effectively treated as a file tree: everything in it, including subdirectories, is copied. However, the directory itself is not included in the copy.

* A non-existent file — the path is ignored

Here is an example that uses multiple `from()` specifications, each with a different argument type. You will probably also notice that `into()` is configured lazily using a closure (in Groovy) or a Provider (in Kotlin) — a technique that also works with `from()`:

`Kotlin``Groovy`

build.gradle

```
tasks.register('anotherCopyTask', Copy) {
    // Copy everything under src/main/webapp
    from 'src/main/webapp'
    // Copy a single file
    from 'src/staging/index.html'
    // Copy the output of a task
    from copyTask
    // Copy the output of a task using Task outputs explicitly.
    from copyTaskWithPatterns.outputs
    // Copy the contents of a Zip file
    from zipTree('src/main/assets.zip')
    // Determine the destination directory later
    into { getDestDir() }
}
```

Note that the lazy configuration of `into()` is different from a [child specification](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications), even though the syntax is similar. Keep an eye on the number of arguments to distinguish between them.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:project_copy_method)[Copying files in your own tasks](https://docs.gradle.org/userguide/working_with_files.html#sec:project_copy_method)

Occasionally, you want to copy files or directories as _part_ of a task. For example, a custom archiving task based on an unsupported archive format might want to copy files to a temporary directory before they are archived. You still want to take advantage of Gradle’s copy API without introducing an extra `Copy` task.

The solution is to use the [Project.copy(org.gradle.api.Action)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:copy(org.gradle.api.Action)) method. Configuring it with a copy spec works like the `Copy` task. Here’s a trivial example:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyMethod') {
    doLast {
        copy {
            from 'src/main/webapp'
            into layout.buildDirectory.dir('explodedWar')
            include '**/*.html'
            include '**/*.jsp'
        }
    }
}
```

The above example demonstrates the basic syntax and also highlights two major limitations of using the `copy()` method:

1. The `copy()` method is not [incremental](https://docs.gradle.org/current/userguide/incremental_build.html#incremental_build). The example’s `copyMethod` task will _always_ execute because it has no information about what files make up the task’s inputs. You have to define the task inputs and outputs manually.

2. Using a task as a copy source, i.e., as an argument to `from()`, won’t create an automatic task dependency between your task and that copy source. As such, if you use the `copy()` method as part of a task action, you must explicitly declare all inputs and outputs to get the correct behavior.

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyMethodWithExplicitDependencies') {
    // up-to-date check for inputs, plus add copyTask as dependency
    inputs.files(copyTask)
        .withPropertyName("inputs")
        .withPathSensitivity(PathSensitivity.RELATIVE)
    outputs.dir('some-dir') // up-to-date check for outputs
        .withPropertyName("outputDir")
    doLast {
        copy {
            // Copy the output of copyTask
            from copyTask
            into 'some-dir'
        }
    }
}
```

These limitations make it preferable to use the `Copy` task wherever possible because of its built-in support for incremental building and task dependency inference. That is why the `copy()` method is intended for use by [custom tasks](https://docs.gradle.org/current/userguide/custom_tasks.html#custom_tasks) that need to copy files as part of their function. Custom tasks that use the `copy()` method should declare the necessary inputs and outputs relevant to the copy action.

[](https://docs.gradle.org/userguide/working_with_files.html#renaming_files)[Renaming files](https://docs.gradle.org/userguide/working_with_files.html#renaming_files)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Renaming files in Gradle can be done using the `CopySpec` API, which provides methods for renaming files as they are copied.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files_example)[Using `Copy.rename()`](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files_example)

If the files used and generated by your builds sometimes don’t have names that suit, you can rename those files as you copy them. Gradle allows you to do this as part of a copy specification using the `rename()` configuration.

The following example removes the "-staging" marker from the names of any files that have it:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyFromStaging', Copy) {
    from "src/main/webapp"
    into layout.buildDirectory.dir('explodedWar')

    rename '(.+)-staging(.+)', '$1$2'
}
```

As in the above example, you can use regular expressions for this or closures that use more complex logic to determine the target filename. For example, the following task truncates filenames:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyWithTruncate', Copy) {
    from layout.buildDirectory.dir("reports")
    rename { String filename ->
        if (filename.size() > 10) {
            return filename[0..7] + "~" + filename.size()
        }
        else return filename
    }
    into layout.buildDirectory.dir("toArchive")
}
```

As with filtering, you can also rename a subset of files by configuring it as part of a child specification on a `from()`.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files)[Using `Copyspec.rename{}`](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files)

The [example of how to rename files on copy](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files_example) gives you most of the information you need to perform this operation. It demonstrates the two options for renaming:

1. Using a regular expression

2. Using a closure

Regular expressions are a flexible approach to renaming, particularly as Gradle supports regex groups that allow you to remove and replace parts of the source filename. The following example shows how you can remove the string "-staging" from any filename that contains it using a simple regular expression:

`Kotlin``Groovy`

build.gradle

```
tasks.register('rename', Copy) {
    from 'src/main/webapp'
    into layout.buildDirectory.dir('explodedWar')
    // Use a regular expression to map the file name
    rename '(.+)-staging(.+)', '$1$2'
    rename(/(.+)-staging(.+)/, '$1$2')
    // Use a closure to convert all file names to upper case
    rename { String fileName ->
        fileName.toUpperCase()
    }
}
```

You can use any regular expression supported by the Java `Pattern` class and the substitution string. The second argument of `rename()` works on the same principles as the `Matcher.appendReplacement()` method.

Regular expressions in Groovy build scripts

There are two common issues people come across when using regular expressions in this context:

1. If you use a slashy string (those delimited by '/') for the first argument, you _must_ include the parentheses for `rename()` as shown in the above example.

2. It’s safest to use single quotes for the second argument, otherwise you need to escape the '$' in group substitutions, i.e. `"\$1\$2"`.

The first is a minor inconvenience, but slashy strings have the advantage that you don’t have to escape backslash ('\') characters in the regular expression. The second issue stems from Groovy’s support for embedded expressions using `${ }` syntax in double-quoted and slashy strings.

The closure syntax for `rename()` is straightforward and can be used for any requirements that simple regular expressions can’t handle. You’re given a file’s name, and you return a new name for that file or `null` if you don’t want to change the name. Be aware that the closure will be executed for every file copied, so try to avoid expensive operations where possible.

[](https://docs.gradle.org/userguide/working_with_files.html#filtering_files)[Filtering files](https://docs.gradle.org/userguide/working_with_files.html#filtering_files)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Filtering files in Gradle involves selectively including or excluding files based on certain criteria.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_include_and_copyspec_exclude)[Using `CopySpec.include()` and `CopySpec.exclude()`](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_include_and_copyspec_exclude)

These methods are typically used with Ant-style include or exclude patterns, as described in [PatternFilterable](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/util/PatternFilterable.html).

You can also perform more complex logic by using a closure that takes a [FileTreeElement](https://docs.gradle.org/current/javadoc/org/gradle/api/file/FileTreeElement.html) and returns `true` if the file should be included or `false` otherwise. The following example demonstrates both forms, ensuring that only `.html` and `.jsp` files are copied, except for those `.html` files with the word "DRAFT" in their content:

`Kotlin``Groovy`

build.gradle

```
tasks.register('copyTaskWithPatterns', Copy) {
    from 'src/main/webapp'
    into layout.buildDirectory.dir('explodedWar')
    include '**/*.html'
    include '**/*.jsp'
    exclude { FileTreeElement details ->
        details.file.name.endsWith('.html') &&
            details.file.text.contains('DRAFT')
    }
}
```

A question you may ask yourself at this point is what happens when inclusion and exclusion patterns overlap? Which pattern wins? Here are the basic rules:

* If there are no explicit inclusions or exclusions, everything is included

* If at least one inclusion is specified, only files and directories matching the patterns are included

* Any exclusion pattern overrides any inclusions, so if a file or directory matches at least one exclusion pattern, it won’t be included, regardless of the inclusion patterns

Bear these rules in mind when creating combined inclusion and exclusion specifications so that you end up with the exact behavior you want.

Note that the inclusions and exclusions in the above example will apply to _all_`from()` configurations. If you want to apply filtering to a subset of the copied files, you’ll need to use [child specifications](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications).

[](https://docs.gradle.org/userguide/working_with_files.html#sec:filtering_files)[Filtering file content](https://docs.gradle.org/userguide/working_with_files.html#sec:filtering_files)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Filtering file content in Gradle involves replacing placeholders or tokens in files with dynamic values.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_filter)[Using `CopySpec.filter()`](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_filter)

Transforming the content of files while they are being copied involves basic templating that uses token substitution, removal of lines of text, or even more complex filtering using a full-blown template engine.

`Kotlin``Groovy`

build.gradle

```
import org.apache.tools.ant.filters.FixCrLfFilter
import org.apache.tools.ant.filters.ReplaceTokens

tasks.register('filter', Copy) {
    from 'src/main/webapp'
    into layout.buildDirectory.dir('explodedWar')
    // Substitute property tokens in files
    expand(copyright: '2009', version: '2.3.1')
    // Use some of the filters provided by Ant
    filter(FixCrLfFilter)
    filter(ReplaceTokens, tokens: [copyright: '2009', version: '2.3.1'])
    // Use a closure to filter each line
    filter { String line ->
        "[$line]"
    }
    // Use a closure to remove lines
    filter { String line ->
        line.startsWith('-') ? null : line
    }
    filteringCharset = 'UTF-8'
}
```

The `filter()` method has two variants, which behave differently:

* one takes a `FilterReader` and is designed to work with Ant filters, such as `ReplaceTokens`

* one takes a closure or [Transformer](https://docs.gradle.org/current/javadoc/org/gradle/api/Transformer.html) that defines the transformation for each line of the source file

Note that both variants assume the source files are text-based. When you use the `ReplaceTokens` class with `filter()`, you create a template engine that replaces tokens of the form `@tokenName@` (the Ant-style token) with values you define.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_expand)[Using `CopySpec.expand()`](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_expand)

The `expand()` method treats the source files as [Groovy templates](https://docs.groovy-lang.org/latest/html/api/groovy/text/SimpleTemplateEngine.html), which evaluates and expands expressions of the form `${expression}.`

You can pass in property names and values that are then expanded in the source files. `expand()` allows for more than basic token substitution as the embedded expressions are full-blown Groovy expressions.

Specifying the character set when reading and writing the file is good practice. Otherwise, the transformations won’t work properly for non-ASCII text. You configure the character set with the [CopySpec.setFilteringCharset(String)](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopySpec.html#setFilteringCharset-java.lang.String-) property. If it’s not specified, the JVM default character set is used, which will likely differ from the one you want.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:setting_file_permissions)[Setting file permissions](https://docs.gradle.org/userguide/working_with_files.html#sec:setting_file_permissions)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setting file permissions in Gradle involves specifying the permissions for files or directories created or modified during the build process.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_filepermissions)[Using `CopySpec.filePermissions{}`](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_filepermissions)

For any `CopySpec` involved in copying files, may it be the `Copy` task itself, or any child specifications, you can explicitly set the permissions the destination files will have via the [CopySpec.filePermissions {}](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopyProcessingSpec.html#filePermissions-org.gradle.api.Action-) configurations block.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_dirpermissions)[Using `CopySpec.dirPermissions{}`](https://docs.gradle.org/userguide/working_with_files.html#using_copyspec_dirpermissions)

You can do the same for directories too, independently of files, via the [CopySpec.dirPermissions {}](https://docs.gradle.org/current/javadoc/org/gradle/api/file/CopyProcessingSpec.html#dirPermissions-org.gradle.api.Action-) configurations block.

Not setting permissions explicitly will preserve the permissions of the original files or directories. The exception are archive tasks, see [Reproducible archives](https://docs.gradle.org/userguide/working_with_files.html#sec:reproducible_archives) for details.

Example 1. [Setting file permissions for files and directories](https://docs.gradle.org/userguide/working_with_files.html#ex-setting-file-permissions-for-files-and-directories)

`Kotlin``Groovy`

build.gradle

```
tasks.register('permissions', Copy) {
    from 'src/main/webapp'
    into layout.buildDirectory.dir('explodedWar')
    filePermissions {
        user {
            read = true
            execute = true
        }
        other.execute = false
    }
    dirPermissions {
        unix('r-xr-x---')
    }
}
```

Using empty configuration blocks for file or directory permissions still sets them explicitly, just to fixed default values. Everything inside one of these configuration blocks is relative to the default values. Default permissions differ for files and directories:

* **file**: read & write for **owner**, read for **group**, read for **other** (`0644`, `rw-r—​r--`)

* **directory**: read, write & execute for **owner**, read & execute for **group**, read & execute for **other** (`0755`, `rwxr-xr-x`)

It’s also possible to set permissions for a specific file. See the following example:

Example 2. [Setting file permissions for a specific file](https://docs.gradle.org/userguide/working_with_files.html#ex-setting-file-permissions-for-a-specific-file)

`Kotlin``Groovy`

build.gradle

```
tasks.register("specificPermissions", Copy) {
    from 'src/main/webapp'
    into layout.buildDirectory.dir('explodedWarWithScript')
    eachFile {
        if (name == "script.sh") {
            permissions {
                user {
                    execute = true
                }
            }
        }
    }
}
```

Setting file permissions explicitly for a file doesn’t support `UP-TO-DATE` checks, so a task using this setting will always run.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:moving_files_example)[Moving files and directories](https://docs.gradle.org/userguide/working_with_files.html#sec:moving_files_example)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Moving files and directories in Gradle is a straightforward process that can be accomplished using several APIs. When implementing file-moving logic in your build scripts, it’s important to consider file paths, conflicts, and task dependencies.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_file_renameto)[Using `File.renameTo()`](https://docs.gradle.org/userguide/working_with_files.html#using_file_renameto)

`File.renameTo()` is a method in Java (and by extension, in Gradle’s Groovy DSL) used to rename or move a file or directory. When you call `renameTo()` on a `File` object, you provide another `File` object representing the new name or location. If the operation is successful, `renameTo()` returns `true`; otherwise, it returns `false`.

It’s important to note that `renameTo()` has some limitations and platform-specific behavior.

In this example, the `moveFile` task uses the `Copy` task type to specify the source and destination directories. Inside the `doLast` closure, it uses `File.renameTo()` to move the file from the source directory to the destination directory:

```
task moveFile {
    doLast {
        def sourceFile = file('source.txt')
        def destFile = file('destination/new_name.txt')

        if (sourceFile.renameTo(destFile)) {
            println "File moved successfully."
        }
    }
}
```

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task)[Using the `Copy` task](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task)

In this example, the `moveFile` task copies the file `source.txt` to the destination directory and renames it to `new_name.txt` in the process. This achieves a similar effect to moving a file.

```
task moveFile(type: Copy) {
    from 'source.txt'
    into 'destination'
    rename { fileName ->
        'new_name.txt'
    }
}
```

[](https://docs.gradle.org/userguide/working_with_files.html#sec:deleting_files_example)[Deleting files and directories](https://docs.gradle.org/userguide/working_with_files.html#sec:deleting_files_example)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deleting files and directories in Gradle involves removing them from the file system.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_delete_task)[Using the `Delete` task](https://docs.gradle.org/userguide/working_with_files.html#using_the_delete_task)

You can easily delete files and directories using the [Delete](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.Delete.html) task. You must specify which files and directories to delete in a way supported by the [Project.files(java.lang.Object…​)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:files(java.lang.Object[])) method.

For example, the following task deletes the entire contents of a build’s output directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('myClean', Delete) {
    delete buildDir
}
```

If you want more control over which files are deleted, you can’t use inclusions and exclusions the same way you use them for copying files. Instead, you use the built-in filtering mechanisms of `FileCollection` and `FileTree`. The following example does just that to clear out temporary files from a source directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('cleanTempFiles', Delete) {
    delete fileTree("src").matching {
        include "**/*.tmp"
    }
}
```

### [](https://docs.gradle.org/userguide/working_with_files.html#using_project_delete)[Using `Project.delete()`](https://docs.gradle.org/userguide/working_with_files.html#using_project_delete)

This method takes one or more arguments representing the files or directories to be deleted.

For example, the following task deletes the entire contents of a build’s output directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('myClean', Delete) {
    delete buildDir
}
```

If you want more control over which files are deleted, you can’t use inclusions and exclusions the same way you use them for copying files. Instead, you use the built-in filtering mechanisms of `FileCollection` and `FileTree`. The following example does just that to clear out temporary files from a source directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('cleanTempFiles', Delete) {
    delete fileTree("src").matching {
        include "**/*.tmp"
    }
}
```

[](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_archives_example)[Creating archives](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_archives_example)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

From the perspective of Gradle, packing files into an archive is effectively a copy in which the destination is the archive file rather than a directory on the file system. Creating archives looks a lot like copying, with all the same features.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_zip_tar_or_jar_task)[Using the `Zip`, `Tar`, or `Jar` task](https://docs.gradle.org/userguide/working_with_files.html#using_the_zip_tar_or_jar_task)

The simplest case involves archiving the entire contents of a directory, which this example demonstrates by creating a ZIP of the `toArchive` directory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('packageDistribution', Zip) {
    archiveFileName = "my-distribution.zip"
    destinationDirectory = layout.buildDirectory.dir('dist')

    from layout.buildDirectory.dir("toArchive")
}
```

Notice how we specify the destination and name of the archive instead of an `into()`: both are required. You often won’t see them explicitly set because most projects apply the [Base Plugin](https://docs.gradle.org/current/userguide/base_plugin.html#base_plugin). It provides some conventional values for those properties.

The following example demonstrates this; you can learn more about the conventions in the [archive naming](https://docs.gradle.org/userguide/working_with_files.html#sec:archive_naming) section.

Each type of archive has its own task type, the most common ones being [Zip](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Zip.html), [Tar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Tar.html) and [Jar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Jar.html). They all share most of the configuration options of `Copy`, including filtering and renaming.

One of the most common scenarios involves copying files into specified archive subdirectories. For example, let’s say you want to package all PDFs into a `docs` directory in the archive’s root. This `docs` directory doesn’t exist in the source location, so you must create it as part of the archive. You do this by adding an `into()` declaration for just the PDFs:

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'base'
}

version = "1.0.0"

tasks.register('packageDistribution', Zip) {
    from(layout.buildDirectory.dir("toArchive")) {
        exclude "**/*.pdf"
    }

    from(layout.buildDirectory.dir("toArchive")) {
        include "**/*.pdf"
        into "docs"
    }
}
```

As you can see, you can have multiple `from()` declarations in a copy specification, each with its own configuration. See [Using child copy specifications](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications) for more information on this feature.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:archives)[Understanding archive creation](https://docs.gradle.org/userguide/working_with_files.html#sec:archives)

Archives are essentially self-contained file systems, and Gradle treats them as such. This is why working with archives is similar to working with files and directories.

Out of the box, Gradle supports the creation of ZIP and TAR archives and, by extension, Java’s JAR, WAR, and EAR formats—Java’s archive formats are all ZIPs. Each of these formats has a corresponding task type to create them: [Zip](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Zip.html), [Tar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Tar.html), [Jar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Jar.html), [War](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.War.html), and [Ear](https://docs.gradle.org/current/dsl/org.gradle.plugins.ear.Ear.html). These all work the same way and are based on copy specifications, just like the `Copy` task.

Creating an archive file is essentially a file copy in which the destination is implicit, i.e., the archive file itself. Here is a basic example that specifies the path and name of the target archive file:

`Kotlin``Groovy`

build.gradle

```
tasks.register('packageDistribution', Zip) {
    archiveFileName = "my-distribution.zip"
    destinationDirectory = layout.buildDirectory.dir('dist')

    from layout.buildDirectory.dir("toArchive")
}
```

The full power of copy specifications is available to you when creating archives, which means you can do content filtering, file renaming, or anything else covered in the previous section. A common requirement is copying files into subdirectories of the archive that don’t exist in the source folders, something that can be achieved with `into()`[child specifications](https://docs.gradle.org/userguide/working_with_files.html#sub:using_child_copy_specifications).

Gradle allows you to create as many archive tasks as you want, but it’s worth considering that many convention-based plugins provide their own. For example, the Java plugin adds a `jar` task for packaging a project’s compiled classes and resources in a JAR. Many of these plugins provide sensible conventions for the names of archives and the copy specifications used. We recommend you use these tasks wherever you can rather than overriding them with your own.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:archive_naming)[Naming archives](https://docs.gradle.org/userguide/working_with_files.html#sec:archive_naming)

Gradle has several conventions around the naming of archives and where they are created based on the plugins your project uses. The main convention is provided by the [Base Plugin](https://docs.gradle.org/current/userguide/base_plugin.html#base_plugin), which defaults to creating archives in the `layout.buildDirectory.dir("distributions")` directory and typically uses archive names of the form _[projectName]-[version].[type]_.

The following example comes from a project named `archive-naming`, hence the `myZip` task creates an archive named `archive-naming-1.0.zip`:

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'base'
}

version = 1.0

tasks.register('myZip', Zip) {
    from 'somedir'
    File projectDir = layout.projectDirectory.asFile
    doLast {
        println archiveFileName.get()
        println projectDir.relativePath(destinationDirectory.get().asFile)
        println projectDir.relativePath(archiveFile.get().asFile)
    }
}
```

`$ ./gradlew -q myZip`

```
archive-naming-1.0.zip
build/distributions
build/distributions/archive-naming-1.0.zip
```

Note that the archive name does _not_ derive from the task’s name that creates it.

If you want to change the name and location of a generated archive file, you can provide values for the corresponding task’s `archiveFileName` and `destinationDirectory` properties. These override any conventions that would otherwise apply.

Alternatively, you can make use of the default archive name pattern provided by [AbstractArchiveTask.getArchiveFileName()](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.AbstractArchiveTask.html#org.gradle.api.tasks.bundling.AbstractArchiveTask:archiveFileName): _[archiveBaseName]-[archiveAppendix]-[archiveVersion]-[archiveClassifier].[archiveExtension]_. You can set each of these properties on the task separately. Note that the Base Plugin uses the convention of the project name for _archiveBaseName_, project version for _archiveVersion_, and the archive type for _archiveExtension_. It does not provide values for the other properties.

This example — from the same project as the one above — configures just the `archiveBaseName` property, overriding the default value of the project name:

`Kotlin``Groovy`

build.gradle

```
tasks.register('myCustomZip', Zip) {
    archiveBaseName = 'customName'
    from 'somedir'

    doLast {
        println archiveFileName.get()
    }
}
```

`$ ./gradlew -q myCustomZip`

`customName-1.0.zip`

You can also override the default `archiveBaseName` value for _all_ the archive tasks in your build by configuring the `archivesName` property in the `base` block, as demonstrated by the following example. The block is defined by the `base` plugin and backed by the `BasePluginExtension` class.

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'base'
}

version = 1.0
base {
    archivesName = "gradle"
    distsDirectory = layout.buildDirectory.dir('custom-dist')
    libsDirectory = layout.buildDirectory.dir('custom-libs')
}

def myZip = tasks.register('myZip', Zip) {
    from 'somedir'
}

def myOtherZip = tasks.register('myOtherZip', Zip) {
    archiveAppendix = 'wrapper'
    archiveClassifier = 'src'
    from 'somedir'
}

tasks.register('echoNames') {
    def projectNameString = project.name
    def archiveFileName = myZip.flatMap { it.archiveFileName }
    def myOtherArchiveFileName = myOtherZip.flatMap { it.archiveFileName }
    doLast {
        println "Project name: $projectNameString"
        println archiveFileName.get()
        println myOtherArchiveFileName.get()
    }
}
```

`$ ./gradlew -q echoNames`

```
Project name: archives-changed-base-name
gradle-1.0.zip
gradle-wrapper-1.0-src.zip
```

You can find all the possible archive task properties in the API documentation for [AbstractArchiveTask](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.AbstractArchiveTask.html). Still, we have also summarized the main ones here:

`archiveFileName` — `Property<String>`, default: `archiveBaseName-archiveAppendix-archiveVersion-archiveClassifier.archiveExtension`
The complete file name of the generated archive. If any of the properties in the default value are empty, their '-' separator is dropped.

`archiveFile` — `Provider<RegularFile>`, _read-only_, default: `destinationDirectory/archiveFileName`
The absolute file path of the generated archive.

`destinationDirectory` — `DirectoryProperty`, default: depends on archive type
The target directory in which to put the generated archive. By default, JARs and WARs go into `layout.buildDirectory.dir("libs")`. ZIPs and TARs go into `layout.buildDirectory.dir("distributions")`.

`archiveBaseName` — `Property<String>`, default: `project.name`
The base name portion of the archive file name, typically a project name or some other descriptive name for what it contains.

`archiveAppendix` — `Property<String>`, default: `null`
The appendix portion of the archive file name that comes immediately after the base name. It is typically used to distinguish between different forms of content, such as code and docs, or a minimal distribution versus a full or complete one.

`archiveVersion` — `Property<String>`, default: `project.version`
The version portion of the archive file name, typically in the form of a normal project or product version.

`archiveClassifier` — `Property<String>`, default: `null`
The classifier portion of the archive file name. Often used to distinguish between archives that target different platforms.

`archiveExtension` — `Property<String>`, default: depends on archive type and compression type
The filename extension for the archive. By default, this is set based on the archive task type and the compression type (if you’re creating a TAR). Will be one of: `zip`, `jar`, `war`, `tar`, `tgz` or `tbz2`. You can of course set this to a custom extension if you wish.

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:archive_contents)[Using archives as file trees](https://docs.gradle.org/userguide/working_with_files.html#sec:archive_contents)

An archive is a directory and file hierarchy packed into a single file. In other words, it’s a special case of a file tree, and that’s exactly how Gradle treats archives.

Instead of using the `fileTree()` method, which only works on normal file systems, you use the [Project.zipTree(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:zipTree(java.lang.Object)) and [Project.tarTree(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:tarTree(java.lang.Object)) methods to wrap archive files of the corresponding type (note that JAR, WAR and EAR files are ZIPs). Both methods return `FileTree` instances that you can then use in the same way as normal file trees. For example, you can extract some or all of the files of an archive by copying its contents to some directory on the file system. Or you can merge one archive into another.

Here are some simple examples of creating archive-based file trees:

`Kotlin``Groovy`

build.gradle

```
// Create a ZIP file tree using path
FileTree zip = zipTree('someFile.zip')

// Create a TAR file tree using path
FileTree tar = tarTree('someFile.tar')

//tar tree attempts to guess the compression based on the file extension
//however if you must specify the compression explicitly you can:
FileTree someTar = tarTree(resources.gzip('someTar.ext'))
```

You can see a practical example of extracting an archive file [in the unpacking archives section](https://docs.gradle.org/userguide/working_with_files.html#sec:unpacking_archives_example) below.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:reproducible_archives)[Reproducible archives](https://docs.gradle.org/userguide/working_with_files.html#sec:reproducible_archives)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting with Gradle 9, archives are reproducible by default.

It’s desirable to recreate archives exactly the same, byte for byte, on different machines. Building an artifact from source code should produce the same result no matter when and where it is built. This is necessary for projects like [reproducible-builds.org](https://reproducible-builds.org/).

Reproducing the same byte-for-byte archive generally poses some challenges since the order of the files in an archive can be influenced by the underlying file system. Each time a ZIP, TAR, JAR, WAR or EAR is built from source, the order of the files inside the archive may change. Files on disk can also have different timestamps or permissions depending on the environment.

Starting with Gradle 9.0.0, all [AbstractArchiveTask](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.AbstractArchiveTask.html) (e.g. `Jar`, `Zip`) tasks produce reproducible archives by default:

* File order in the archive is deterministic

* Files have fixed timestamps (exact values depend on the archive type)

* Directories have fixed permissions set to `0755`

* Files have fixed permissions set to `0644`

### [](https://docs.gradle.org/userguide/working_with_files.html#sec:revert_reproducible_archives)[Preserve file system-defined aspects](https://docs.gradle.org/userguide/working_with_files.html#sec:revert_reproducible_archives)

If desired, you can revert individual aspects of reproducible archives.

`Kotlin``Groovy`

build.gradle

```
tasks.withType(AbstractArchiveTask).configureEach {
    // Use file timestamps from the file system
    preserveFileTimestamps = true  (1)
    // Make file order based on the file system
    reproducibleFileOrder = false  (2)
    // Use permissions from the file system
    useFileSystemPermissions()     (3)
}
```

In case the file system is already the source of truth for the permissions, e.g., via the version control tools, you can preserve the permissions across all archives tasks by configuring a property:

gradle.properties

`org.gradle.archives.use-file-system-permissions=true`

[](https://docs.gradle.org/userguide/working_with_files.html#sec:permissions_inside_archives)[Permissions for files inside archives](https://docs.gradle.org/userguide/working_with_files.html#sec:permissions_inside_archives)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Setting file permissions in Gradle archives is done in the same way as when copying file, see [Setting file permissions](https://docs.gradle.org/userguide/working_with_files.html#sec:setting_file_permissions) for details. The main difference is that archive tasks by default set the permissions of files and directories in the archive to fixed values, which are `0644` for files and `0755` for directories for reproducibility.

We recognize two main cases, where users may want to change the permissions of files and directories in archives:

1. Case where the file system is already the source of truth for the permissions. For such configuration see [Preserve file system-defined aspects](https://docs.gradle.org/userguide/working_with_files.html#sec:revert_reproducible_archives) section.

2. Case where the permissions of files and directories in the archive should be set to specific values, for example to set the executable bit on a script file. For such configuration see [Setting file permissions](https://docs.gradle.org/userguide/working_with_files.html#sec:setting_file_permissions) section.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:unpacking_archives_example)[Unpacking archives](https://docs.gradle.org/userguide/working_with_files.html#sec:unpacking_archives_example)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Archives are effectively self-contained file systems, so unpacking them is a case of copying the files from that file system onto the local file system — or even into another archive. Gradle enables this by providing some wrapper functions that make archives available as hierarchical collections of files ([file trees](https://docs.gradle.org/userguide/working_with_files.html#sec:file_trees)).

### [](https://docs.gradle.org/userguide/working_with_files.html#using_project_ziptree_and_project_tartree)[Using `Project.zipTree` and `Project.tarTree`](https://docs.gradle.org/userguide/working_with_files.html#using_project_ziptree_and_project_tartree)

That file tree can then be used in a `from()` specification, like so:

`Kotlin``Groovy`

build.gradle

```
tasks.register('unpackFiles', Copy) {
    from zipTree("src/resources/thirdPartyResources.zip")
    into layout.buildDirectory.dir("resources")
}
```

As with a normal copy, you can control which files are unpacked via [filters](https://docs.gradle.org/userguide/working_with_files.html#sec:filtering_files) and even [rename files](https://docs.gradle.org/userguide/working_with_files.html#sec:renaming_files) as they are unpacked.

More advanced processing can be handled by the [eachFile()](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.AbstractCopyTask.html#eachFile(org.gradle.api.Action)) method. For example, you might need to extract different subtrees of the archive into different paths within the destination directory. The following sample uses the method to extract the files within the archive’s `libs` directory into the root destination directory, rather than into a `libs` subdirectory:

`Kotlin``Groovy`

build.gradle

```
tasks.register('unpackLibsDirectory', Copy) {
    from(zipTree("src/resources/thirdPartyResources.zip")) {
        include "libs/**"  (1)
        eachFile { fcd ->
            fcd.relativePath = new RelativePath(true, fcd.relativePath.segments.drop(1))  (2)
        }
        includeEmptyDirs = false  (3)
    }
    into layout.buildDirectory.dir("resources")
}
```

**1**Extracts only the subset of files that reside in the `libs` directory
**2**Remaps the path of the extracting files into the destination directory by dropping the `libs` segment from the file path
**3**Ignores the empty directories resulting from the remapping, see Caution note below

You can not change the destination path of empty directories with this technique. You can learn more in [this issue](https://github.com/gradle/gradle/issues/2940).

If you’re a Java developer wondering why there is no `jarTree()` method, that’s because `zipTree()` works perfectly well for JARs, WARs, and EARs.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_uber_jar_example)[Creating "uber" or "fat" JARs](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_uber_jar_example)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Java, applications and their dependencies were typically packaged as separate JARs within a single distribution archive. That still happens, but another approach that is now common is placing the classes and resources of the dependencies directly into the application JAR, creating what is known as an Uber or fat JAR.

Creating "uber" or "fat" JARs in Gradle involves packaging all dependencies into a single JAR file, making it easier to distribute and run the application.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_shadow_plugin)[Using the Shadow Plugin](https://docs.gradle.org/userguide/working_with_files.html#using_the_shadow_plugin)

Gradle does not have full built-in support for creating uber JARs, but you can use third-party plugins like the [Shadow plugin](https://github.com/GradleUp/shadow) (`com.gradleup.shadow`) to achieve this. This plugin packages your project classes and dependencies into a single JAR file.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_project_ziptree_and_the_jar_task)[Using `Project.zipTree()` and the `Jar` task](https://docs.gradle.org/userguide/working_with_files.html#using_project_ziptree_and_the_jar_task)

To copy the contents of other JAR files into the application JAR, use the [Project.zipTree(java.lang.Object)](https://docs.gradle.org/current/dsl/org.gradle.api.Project.html#org.gradle.api.Project:zipTree(java.lang.Object)) method and the [Jar](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.bundling.Jar.html) task. This is demonstrated by the `uberJar` task in the following example:

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'java'
}

version = '1.0.0'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'commons-io:commons-io:2.6'
}

tasks.register('uberJar', Jar) {
    archiveClassifier = 'uber'

    from sourceSets.main.output

    dependsOn configurations.runtimeClasspath
    from {
        configurations.runtimeClasspath.findAll { it.name.endsWith('jar') }.collect { zipTree(it) }
    }
}
```

In this case, we’re taking the runtime dependencies of the project — `configurations.runtimeClasspath.files` — and wrapping each of the JAR files with the `zipTree()` method. The result is a collection of ZIP file trees, the contents of which are copied into the uber JAR alongside the application classes.

[](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_directories_example)[Creating directories](https://docs.gradle.org/userguide/working_with_files.html#sec:creating_directories_example)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Many tasks need to create directories to store the files they generate, which is why Gradle [automatically manages](https://docs.gradle.org/current/userguide/incremental_build.html#incremental_build) this aspect of tasks when they explicitly define file and directory outputs. All core Gradle tasks ensure that any output directories they need are created, if necessary, using this mechanism.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_file_mkdirs_and_files_createdirectories)[Using `File.mkdirs` and `Files.createDirectories`](https://docs.gradle.org/userguide/working_with_files.html#using_file_mkdirs_and_files_createdirectories)

In cases where you need to create a directory manually, you can use the standard `Files.createDirectories` or `File.mkdirs` methods from within your build scripts or custom task implementations.

Here is a simple example that creates a single `images` directory in the project folder:

`Kotlin``Groovy`

build.gradle

```
tasks.register('ensureDirectory') {
    // Store target directory into a variable to avoid project reference in the configuration cache
    def directory = file("images")

    doLast {
        Files.createDirectories(directory.toPath())
    }
}
```

As described in the [Apache Ant manual](https://ant.apache.org/manual/Tasks/mkdir.html), the `mkdir` task will automatically create all necessary directories in the given path. It will do nothing if the directory already exists.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_project_mkdir)[Using `Project.mkdir`](https://docs.gradle.org/userguide/working_with_files.html#using_project_mkdir)

You can create directories in Gradle using the `mkdir` method, which is available in the [`Project` object](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#mkdir-java.lang.Object-). This method takes a `File` object or a `String` representing the path of the directory to be created:

```
tasks.register('createDirs') {
    doLast {
        mkdir 'src/main/resources'
        mkdir file('build/generated')

        // Create multiple dirs
        mkdir files(['src/main/resources', 'src/test/resources'])

        // Check dir existence
        def dir = file('src/main/resources')
        if (!dir.exists()) {
            mkdir dir
        }
    }
}
```

[](https://docs.gradle.org/userguide/working_with_files.html#sec:install_executable)[Installing executables](https://docs.gradle.org/userguide/working_with_files.html#sec:install_executable)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you are building a standalone executable, you may want to install this file on your system, so it ends up in your path.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task_2)[Using the `Copy` task](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task_2)

You can use a `Copy` task to install the executable into shared directories like `/usr/local/bin`. The installation directory probably contains many other executables, some of which may even be unreadable by Gradle. To support the unreadable files in the `Copy` task’s destination directory and to avoid time consuming up-to-date checks, you can use [Task.doNotTrackState()](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:doNotTrackState(java.lang.String)):

`Kotlin``Groovy`

build.gradle

```
tasks.register("installExecutable", Copy) {
    from "build/my-binary"
    into "/usr/local/bin"
    doNotTrackState("Installation directory contains unrelated files")
}
```

[](https://docs.gradle.org/userguide/working_with_files.html#sec:copy_deploy)[Deploying single files into application servers](https://docs.gradle.org/userguide/working_with_files.html#sec:copy_deploy)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deploying a single file to an application server typically refers to the process of transferring a packaged application artifact, such as a WAR file, to the application server’s deployment directory.

### [](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task_3)[Using the `Copy` task](https://docs.gradle.org/userguide/working_with_files.html#using_the_copy_task_3)

When working with application servers, you can use a `Copy` task to deploy the application archive (e.g. a WAR file). Since you are deploying a single file, the destination directory of the `Copy` is the whole deployment directory. The deployment directory sometimes does contain unreadable files like named pipes, so Gradle may have problems doing up-to-date checks. In order to support this use-case, you can use [Task.doNotTrackState()](https://docs.gradle.org/current/dsl/org.gradle.api.Task.html#org.gradle.api.Task:doNotTrackState(java.lang.String)):

`Kotlin``Groovy`

build.gradle

```
plugins {
    id 'war'
}

tasks.register("deployToTomcat", Copy) {
    from war
    into layout.projectDirectory.dir('tomcat/webapps')
    doNotTrackState("Deployment directory contains unreadable files")
}
```
