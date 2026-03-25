# Source: https://maven.apache.org/guides/mini/guide-assemblies.html

Title: Guide to creating assemblies – Maven

URL Source: https://maven.apache.org/guides/mini/guide-assemblies.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-assemblies.html)
The assembly mechanism in Maven provides an easy way to create distributions using a assembly descriptor and dependency information found in you POM. In order to use the assembly plug-in you need to configure the assembly plug-in in your POM and it might look like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `<parent>`
3.   `<artifactId>maven</artifactId>`
4.   `<groupId>org.apache.maven</groupId>`
5.   `<version>2.0-beta-3-SNAPSHOT</version>`
6.   `</parent>`
7.   `<modelVersion>4.0.0</modelVersion>`
8.   `<groupId>org.apache.maven</groupId>`
9.   `<artifactId>maven-embedder</artifactId>`
10.   `<name>Maven Embedder</name>`
11.   `<version>2.0-beta-3-SNAPSHOT</version>`
12.   `<build>`
13.   `<plugins>`
14.   `<plugin>`
15.   `<artifactId>maven-assembly-plugin</artifactId>`
16.   `<version>3.3.0</version>`
17.   `<configuration>`
18.   `<descriptors>`
19.   `<descriptor>src/assembly/dep.xml</descriptor>`
20.   `</descriptors>`
21.   `</configuration>`
22.   `<executions>`
23.   `<execution>`
24.   `<id>create-archive</id>`
25.   `<phase>package</phase>`
26.   `<goals>`
27.   `<goal>single</goal>`
28.   `</goals>`
29.   `</execution>`
30.   `</executions>`
31.   `</plugin>`
32.   `</plugins>`
33.   `</build>`
34.   `...`
35.   `</project>`

You'll notice that the assembly descriptor is located in `${project.basedir}/src/assembly` which is the [standard](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html) location for assembly descriptors.

[](https://maven.apache.org/guides/mini/guide-assemblies.html)
Creating a binary assembly[](https://maven.apache.org/guides/mini/guide-assemblies.html#creating-a-binary-assembly)
-------------------------------------------------------------------------------------------------------------------

This is the most typical usage of the assembly plugin where you are creating a distribution for standard use.

1.   `<assembly xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2 http://maven.apache.org/xsd/assembly-1.1.2.xsd">`
3.   `<id>bin</id>`
4.   `<formats>`
5.   `<format>tar.gz</format>`
6.   `<format>tar.bz2</format>`
7.   `<format>zip</format>`
8.   `</formats>`
9.   `<fileSets>`
10.   `<fileSet>`
11.   `<directory>${project.basedir}</directory>`
12.   `<outputDirectory>/</outputDirectory>`
13.   `<includes>`
14.   `<include>README*</include>`
15.   `<include>LICENSE*</include>`
16.   `<include>NOTICE*</include>`
17.   `</includes>`
18.   `</fileSet>`
19.   `<fileSet>`
20.   `<directory>${project.build.directory}</directory>`
21.   `<outputDirectory>/</outputDirectory>`
22.   `<includes>`
23.   `<include>*.jar</include>`
24.   `</includes>`
25.   `</fileSet>`
26.   `<fileSet>`
27.   `<directory>${project.build.directory}/site</directory>`
28.   `<outputDirectory>docs</outputDirectory>`
29.   `</fileSet>`
30.   `</fileSets>`
31.   `</assembly>`

You can use a manually defined assembly descriptor as mentioned before but it is simpler to use the [pre-defined assembly descriptor bin](https://maven.apache.org/plugins/maven-assembly-plugin/descriptor-refs.html#bin) in such cases.

How to use such pre-defined assembly descriptors is described in the [documentation of maven-assembly-plugin](https://maven.apache.org/plugins/maven-assembly-plugin/usage.html#Configuration).

1.   `<assembly`
2.   `xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
3.   `xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2`
4.   `http://maven.apache.org/xsd/assembly-1.1.2.xsd">`

6.   `<!-- TODO: a jarjar format would be better -->`
7.   `<id>dep</id>`
8.   `<formats>`
9.   `<format>jar</format>`
10.   `</formats>`
11.   `<includeBaseDirectory>false</includeBaseDirectory>`
12.   `<fileSets>`
13.   `<fileSet>`
14.   `<outputDirectory>/</outputDirectory>`
15.   `</fileSet>`
16.   `</fileSets>`
17.   `<dependencySets>`
18.   `<dependencySet>`
19.   `<outputDirectory>/</outputDirectory>`
20.   `<unpack>true</unpack>`
21.   `<scope>runtime</scope>`
22.   `<excludes>`
23.   `<exclude>junit:junit</exclude>`
24.   `<exclude>commons-lang:commons-lang</exclude>`
25.   `<exclude>commons-logging:commons-logging</exclude>`
26.   `<exclude>commons-cli:commons-cli</exclude>`
27.   `<exclude>jsch:jsch</exclude>`
28.   `<exclude>org.apache.maven.wagon:wagon-ssh</exclude>`
29.   `<!-- TODO: can probably be removed now -->`
30.   `<exclude>plexus:plexus-container-default</exclude>`
31.   `</excludes>`
32.   `</dependencySet>`
33.   `</dependencySets>`
34.   `</assembly>`

If you like to create a source distribution package the best solution is to use the [pre-defined assembly descriptor src](https://maven.apache.org/plugins/maven-assembly-plugin/descriptor-refs.html#src) for such purposes.

1.   `<assembly xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.2 http://maven.apache.org/xsd/assembly-1.1.2.xsd">`
3.   `<id>src</id>`
4.   `<formats>`
5.   `<format>tar.gz</format>`
6.   `<format>tar.bz2</format>`
7.   `<format>zip</format>`
8.   `</formats>`
9.   `<fileSets>`
10.   `<fileSet>`
11.   `<directory>${project.basedir}</directory>`
12.   `<includes>`
13.   `<include>README*</include>`
14.   `<include>LICENSE*</include>`
15.   `<include>NOTICE*</include>`
16.   `<include>pom.xml</include>`
17.   `</includes>`
18.   `<useDefaultExcludes>true</useDefaultExcludes>`
19.   `</fileSet>`
20.   `<fileSet>`
21.   `<directory>${project.build.sourceDirectory}/src</directory>`
22.   `<useDefaultExcludes>true</useDefaultExcludes>`
23.   `</fileSet>`
24.   `</fileSets>`
25.   `</assembly>`

You can now create the defined distribution packages via command line like this:

```
mvn package
```
