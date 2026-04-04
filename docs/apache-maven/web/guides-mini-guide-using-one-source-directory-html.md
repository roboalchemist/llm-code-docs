# Source: https://maven.apache.org/guides/mini/guide-using-one-source-directory.html

Title: Using Maven When You Can't Use the Conventions – Maven

URL Source: https://maven.apache.org/guides/mini/guide-using-one-source-directory.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
There is a common misconception that Maven can't build a project that doesn't conform to certain directory structures or build practices. This often isn't the case. However, it is true that some Maven features or plugins (especially by third parties) may not work or work completely.

This guide will help you set up Maven on your project when the directive from on high is to not change the existing layout, and detail some of the feature that you might miss when doing so.

Use this as a last resort. There are good reasons why the defaults are the way they are, and we strongly recommend you use them if you can. It encourages consistency and means one less thing you ever need to worry about when starting a new project. There are more interesting things to do than change your layout for the sake of it. Hopefully having used any of these techniques you find that Maven proves itself capable, you will reconsider restructuring to address these issues.>

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
Using Multiple Source Directories[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#using-multiple-source-directories)
-------------------------------------------------------------------------------------------------------------------------------------------------

This occurs when you are producing a single JAR (or other artifact), and have several source directories with classes you want to include.

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### Why isn't this recommended?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#why-isnt-this-recommended)

…

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### How do I do this?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#how-do-i-do-this)

…

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### What are the limitations?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#what-are-the-limitations)

There should be no limitations in this approach. Maven natively supports multiple source directories for the purposes of generated sources.

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
Producing Multiple Unique JARs from a Single Source Directory[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#producing-multiple-unique-jars-from-a-single-source-directory)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As many people that complain about not being able to spread out their sources into multiple source directories seem to complain about not wanting to spread anything out, producing several unique artifacts from a single directory using includes and excludes.

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### Why isn't this recommended?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#why-isnt-this-recommended-1)

This practice can be confusing and risky.

*   You may end up building two JARs that include the same classes - this indicates that the common functionality should have been abstracted into a separate dependency.
*   You may end up introducing a dependency between the two JARs that you didn't realise, and often a circular dependency. This indicates that the classes are in the wrong JAR, or perhaps that everything should just be a single JAR.

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### How do I do this?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#how-do-i-do-this-1)

You still should adhere to producing one artifact per POM, but this requires having multiple POMs, and hence multiple subdirectories. The positive to this is that these introduced directories won't change the layout of existing code, and will establish a future layout should you decide to separate.

Here is an example of setting it up when there is a project with two JARs produced: `core` and `module`.

You might like to review the [Getting Started Guide](https://maven.apache.org/guides/getting-started/)

that demonstrates how this is normally done in Maven, as it is quite similar.

Your directory will look something like this:

```
/
+- pom.xml
+- src/
   +- main/
      +- java/
          +- core/
             +- Core.java
          +- module/
             +- Module.java
```

First, you set up your `pom.xml` at the top level not to produce anything, but to include the other modules we plan to create:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<artifactId>my-parent</artifactId>`
3.   `<packaging>pom</packaging>`
4.   `...`
5.   `<modules>`
6.   `<module>core</module>`
7.   `<module>module</module>`
8.   `</modules>`
9.   `</project>`

Next, the modules themselves are created. Here is the `core/pom.xml` file you should create. The one in the `module` subdirectory will be similar.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<modelVersion>4.0.0</modelVersion>`
3.   `<parent>`
4.   `<groupId>my-groupId</groupId>`
5.   `<artifactId>my-parent</artifactId>`
6.   `<version>1.0-SNAPSHOT</version>`
7.   `</parent>`

9.   `<artifactId>my-core</artifactId>`

11.   `<build>`
12.   `<sourceDirectory>../src/main/java</sourceDirectory>`

14.   `<plugins>`
15.   `<plugin>`
16.   `<artifactId>maven-compiler-plugin</artifactId>`
17.   `<version>2.0.2</version>`
18.   `<configuration>`
19.   `<includes><include>**/core/**</include></includes>`
20.   `</configuration>`
21.   `</plugin>`
22.   `</plugins>`
23.   `</build>`
24.   `</project>`

In this example, the sources are found in the parent directory `../src/main/java`, and only Java files within a `core` package are included.

The final result when building will look like this:

```
/
+- pom.xml
+- src/
   +- main/
      +- java/
          +- core/
             +- Core.java
          +- module/
             +- Module.java
+- core/
   +- pom.xml
   +- target/
      +- my-core-1.0-SNAPSHOT.jar
+- module/
   +- pom.xml
   +- target/
      +- my-module-1.0-SNAPSHOT.jar
```
[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
### What are the limitations?[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#what-are-the-limitations-1)

There is no universal inclusion/exclusion specification, so each plugin needs to be configured individually, and some might not have that capability. In particular, expect that site reports may include all sources, for example.

[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html)
Producing Multiple JARs from a single POM[](https://maven.apache.org/guides/mini/guide-using-one-source-directory.html#producing-multiple-jars-from-a-single-pom)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Source directories aside, sometimes people desire to produce multiple JARs from a single POM. Depending on your use case, Maven can support this.

*   If you are looking to produce JARs that are different (i.e., they have their own dependencies and metadata), Maven doesn't support this. This usually is only needed when sharing a source directory for intrinsically different things, so the use case above applies instead.
*   If you are producing a JAR that is a derivative of the original (e.g., just a subset of classes, or the same JAR with debugging enabled), Maven supports this using profiles. See [Introduction to Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html) for more information.
