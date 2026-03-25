# Source: https://maven.apache.org/guides/mini/guide-building-for-different-environments.html

Title: Building For Different Environments – Maven

URL Source: https://maven.apache.org/guides/mini/guide-building-for-different-environments.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-building-for-different-environments.html)
Building the same artifact for different environments has always been an annoyance. You have multiple environments, for instance test and production servers or, maybe a set of servers that run the same application with different configurations. In this guide I'll explain how you can use profiles to build and package artifacts configured for specific environments. See [Introduction to Build Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html) for a more in-depth explanation of the profile concept.

Note:

*   This guide assume that you have basic Maven knowledge.

*   It will show a way to configure Maven to solve simple configuration set-ups only. By simple configuration set-up I mean cases where you only have a single file or a small set of files that vary for each environment. There are other and better ways to handle two and many-dimensional configuration issues.

This example assume the use of the [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html).

```
pom.xml
src/
  main/
    java/
    resources/
  test/
    java/
```

Under `src/main/resources` there are three files:

*   `environment.properties` - This is the default configuration and will be packaged in the artifact by default.

*   `environment.test.properties` - This is the variant for the test environment.

*   `environment.prod.properties` - This is basically the same as the test variant and will be used in the production environment.

In the project descriptor, you need to configure the different profiles. Only the test profile is showed here.

    1.   `<profiles>`
    2.   `<profile>`
    3.   `<id>test</id>`
    4.   `<build>`
    5.   `<plugins>`
    6.   `<plugin>`
    7.   `<artifactId>maven-antrun-plugin</artifactId>`
    8.   `<executions>`
    9.   `<execution>`
    10.   `<phase>test</phase>`
    11.   `<goals>`
    12.   `<goal>run</goal>`
    13.   `</goals>`
    14.   `<configuration>`
    15.   `<tasks>`
    16.   `<delete file="${project.build.outputDirectory}/environment.properties"/>`
    17.   `<copy file="src/main/resources/environment.test.properties"`
    18.   `tofile="${project.build.outputDirectory}/environment.properties"/>`
    19.   `</tasks>`
    20.   `</configuration>`
    21.   `</execution>`
    22.   `</executions>`
    23.   `</plugin>`
    24.   `<plugin>`
    25.   `<artifactId>maven-surefire-plugin</artifactId>`
    26.   `<configuration>`
    27.   `<skip>true</skip>`
    28.   `</configuration>`
    29.   `</plugin>`
    30.   `<plugin>`
    31.   `<artifactId>maven-jar-plugin</artifactId>`
    32.   `<executions>`
    33.   `<execution>`
    34.   `<phase>package</phase>`
    35.   `<goals>`
    36.   `<goal>jar</goal>`
    37.   `</goals>`
    38.   `<configuration>`
    39.   `<classifier>test</classifier>`
    40.   `</configuration>`
    41.   `</execution>`
    42.   `</executions>`
    43.   `</plugin>`
    44.   `</plugins>`
    45.   `</build>`
    46.   `</profile>`

    48.   `.. Other profiles go here ..`

    50.   `</profiles>`

Three things are configured in this snippet:

    1.   It configures the antrun plugin to execute the run goal in the test phase where it will copy the `environment.test.properties` file to `environment.properties`.

    2.   It will configure the test plugin to skip all tests when building the test and production artifacts. This is useful as you probably don't want to run tests against the production system

    3.   It configures the JAR plugin to create an “attached” JAR with the “test” classifier.

To activate this profile execute `mvn -Ptest install` and Maven will execute the steps in the profile in addition to the normal steps. From this build you will get two artifacts, “foo-1.0.jar” and “foo-1.0-test.jar”. These two jars will identical.

[](https://maven.apache.org/guides/mini/guide-building-for-different-environments.html)
Caveats
-------

*   Currently Maven doesn't allow a project build to only produce attached artifacts. (i.e. it has to produce a “main” artifact as well) This results in two equal JARs being packaged and installed. The JAR plugin probably should also get improved support for this use case to that two different output directories will be used as the basis for building the JAR.
*   The usage of the delete task might seem a bit odd but is required to make sure that the copy task actually will copy the file. The copy task will look at the timestamps of the source and destination files, only when copying the files it won't know that the actually source file might be different than the last time it was executed.
*   After the build the test configuration will be in target/classes and won't be overridden because the resources plugin uses the same timestamp checking, so you should always do a clean after executing Maven with a profile.
*   For the reasons given above it's imperative that you only build an artifact for a single environment in a single execution at a time and that you execute “mvn clean” whenever you change the profile switches. If not, you might get artifacts with a mixed set of configuration files.

[](https://maven.apache.org/guides/mini/guide-building-for-different-environments.html)
Resources
---------

1.   [Introduction to Build Profiles](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)
2.   [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
