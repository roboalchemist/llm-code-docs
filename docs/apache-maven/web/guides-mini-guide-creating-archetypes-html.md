# Source: https://maven.apache.org/guides/mini/guide-creating-archetypes.html

Title: Guide to Creating Archetypes – Maven

URL Source: https://maven.apache.org/guides/mini/guide-creating-archetypes.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
Creating an archetype is a pretty straight forward process. An archetype is a very simple artifact, that contains the project prototype you wish to create. An archetype is made up of:

*   an [archetype descriptor](https://maven.apache.org/archetype/archetype-models/archetype-descriptor/archetype-descriptor.html) (`archetype-metadata.xml` in directory: `src/main/resources/META-INF/maven/`). It lists all the files that will be contained in the archetype and categorizes them so they can be processed correctly by the archetype generation mechanism.
*   the prototype files that are copied by the archetype plugin (directory: `src/main/resources/archetype-resources/`)
*   the prototype pom (`pom.xml` in: `src/main/resources/archetype-resources`)
*   a pom for the archetype (`pom.xml` in the archetype's root directory).

To create an archetype follow these steps:

[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
1. Create a new project and pom.xml for the archetype artifact[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html#1-create-a-new-project-and-pom-xml-for-the-archetype-artifact)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An example `pom.xml` for an archetype artifact looks as follows:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">`
3.   `<modelVersion>4.0.0</modelVersion>`

5.   `<groupId>my.groupId</groupId>`
6.   `<artifactId>my-archetype-id</artifactId>`
7.   `<version>1.0-SNAPSHOT</version>`
8.   `<packaging>maven-archetype</packaging>`

10.   `<build>`
11.   `<extensions>`
12.   `<extension>`
13.   `<groupId>org.apache.maven.archetype</groupId>`
14.   `<artifactId>archetype-packaging</artifactId>`
15.   `<version>3.4.1</version>`
16.   `</extension>`
17.   `</extensions>`
18.   `</build>`
19.   `</project>`

All you need to specify is a `groupId`, `artifactId` and `version`. These three parameters will be needed later for invoking the archetype via `archetype:generate` from the commandline.

[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
2. Create the archetype descriptor[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html#2-create-the-archetype-descriptor)
-------------------------------------------------------------------------------------------------------------------------------------------

The [archetype descriptor](https://maven.apache.org/archetype/archetype-models/archetype-descriptor/archetype-descriptor.html) is a file called `archetype-metadata.xml` which must be located in the `src/main/resources/META-INF/maven/` directory. An example of an archetype descriptor can be found in the quickstart archetype:

1.   `<archetype-descriptor`
2.   `xmlns="http://maven.apache.org/plugins/maven-archetype-plugin/archetype-descriptor/1.2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/plugins/maven-archetype-plugin/archetype-descriptor/1.2.0 https://maven.apache.org/xsd/archetype-descriptor-1.2.0.xsd"`
4.   `name="quickstart">`
5.   `<fileSets>`
6.   `<fileSet filtered="true" packaged="true">`
7.   `<directory>src/main/java</directory>`
8.   `</fileSet>`
9.   `<fileSet>`
10.   `<directory>src/test/java</directory>`
11.   `</fileSet>`
12.   `</fileSets>`
13.   `</archetype-descriptor>`

The attribute `name` tag should be the same as the `artifactId` in the archetype `pom.xml`.

The boolean attribute `partial` show if this archetype is representing a full Maven project or only parts.

The `requiredProperties`, `fileSets` and `modules` tags represent the differents parts of the project:

*   `<requiredProperties>` : List of required properties to generate a project from this archetype
*   `<fileSets>` : File sets definition
*   `<modules>` : Modules definition

At this point one can only specify individual files to be created but not empty directories.

Thus the quickstart archetype shown above defines the following directory structure:

```
archetype
|-- pom.xml
`-- src
    `-- main
        `-- resources
            |-- META-INF
            |   `-- maven
            |       `--archetype-metadata.xml
            `-- archetype-resources
                |-- pom.xml
                `-- src
                    |-- main
                    |   `-- java
                    |       `-- App.java
                    `-- test
                        `-- java
                            `-- AppTest.java
```
[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
3. Create the prototype files and the prototype pom.xml[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html#3-create-the-prototype-files-and-the-prototype-pom-xml)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The next component of the archetype to be created is the prototype `pom.xml`. Any `pom.xml` will do, just don't forget to the set `artifactId` and `groupId` as variables ( `${artifactId}` / `${groupId}` ). Both variables will be initialized from the commandline when calling `archetype:generate`.

An example for a prototype `pom.xml` is:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">`
3.   `<modelVersion>4.0.0</modelVersion>`

5.   `<groupId>${groupId}</groupId>`
6.   `<artifactId>${artifactId}</artifactId>`
7.   `<version>${version}</version>`
8.   `<packaging>jar</packaging>`

10.   `<name>${artifactId}</name>`
11.   `<url>http://www.myorganization.org</url>`

13.   `<dependencies>`
14.   `<dependency>`
15.   `<groupId>junit</groupId>`
16.   `<artifactId>junit</artifactId>`
17.   `<version>4.12</version>`
18.   `<scope>test</scope>`
19.   `</dependency>`
20.   `</dependencies>`
21.   `</project>`

[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
4. Install the archetype and run the archetype plugin[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html#4-install-the-archetype-and-run-the-archetype-plugin)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Now you are ready to install the archetype:

```
mvn install
```

Now that you have created an archetype, you can try it on your local system by using the following command. In this command, you need to specify the full information about the archetype you want to use (its `groupId`, its `artifactId`, its `version`) and the information about the new project you want to create (`artifactId` and `groupId`). Don't forget to include the version of your archetype (if you don't include the version, you archetype creation may fail with a message that version:RELEASE was not found)

```
mvn archetype:generate                                  \
  -DarchetypeGroupId=<archetype-groupId>                \
  -DarchetypeArtifactId=<archetype-artifactId>          \
  -DarchetypeVersion=<archetype-version>                \
  -DgroupId=<my.groupid>                                \
  -DartifactId=<my-artifactId>
```

Once you are happy with the state of your archetype, you can deploy (or submit it to [Maven Central](https://maven.apache.org/guides/mini/guide-central-repository-upload.html)) it as any other artifact and the archetype will then be available to any user of Maven.

[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html)
Alternative way to start creating your Archetype[](https://maven.apache.org/guides/mini/guide-creating-archetypes.html#alternative-way-to-start-creating-your-archetype)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Instead of manually creating the directory structure needed for an archetype, simply use

```
mvn archetype:generate
  -DgroupId=[your project's group id]
  -DartifactId=[your project's artifact id]
  -DarchetypeGroupId=org.apache.maven.archetypes
  -DarchetypeArtifactId=maven-archetype-archetype
```

Afterwhich, you can now customize the contents of the `archetype-resources` directory, and `archetype-metadata.xml`, then, proceed to Step#4 (Install the archetype and run the archetype plugin).
