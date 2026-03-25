# Source: https://maven.apache.org/guides/mini/guide-using-toolchains.html

Title: Guide to Using Toolchains – Maven

URL Source: https://maven.apache.org/guides/mini/guide-using-toolchains.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-using-toolchains.html)[](https://maven.apache.org/guides/mini/guide-using-toolchains.html)
What are Toolchains?[](https://maven.apache.org/guides/mini/guide-using-toolchains.html#what-are-toolchains)
------------------------------------------------------------------------------------------------------------

Maven Toolchains provide a way for a project to specify the JDK (or other tools) used to build the project, without needing to configure this in each plugin or in every `pom.xml`.

When Maven Toolchains are used to specify the JDK, a project can be built by a specific version of the JDK independent of the one Maven is running with. This is similar to how JDK versions can be set in IDEs like IDEA, NetBeans and Eclipse.

[](https://maven.apache.org/guides/mini/guide-using-toolchains.html)
### Prerequisites[](https://maven.apache.org/guides/mini/guide-using-toolchains.html#prerequisites)

For more details about Toolchains' design and implementation, see [Toolchains](https://cwiki.apache.org/confluence/display/MAVENOLD/Toolchains).

Below are some plugins which are toolchain-aware, with the toolchain-type used:

| Toolchain type | **Plugin** | **Starting with** | **Hosted at** |
| --- | --- | --- | --- |
| jdk | [`maven-compiler-plugin`](https://maven.apache.org/plugins/maven-compiler-plugin/) | 2.1 | Apache Maven |
| jdk | [`maven-jarsigner-plugin`](https://maven.apache.org/plugins/maven-jarsigner-plugin/) | 1.3 | Apache Maven |
| jdk | [`maven-javadoc-plugin`](https://maven.apache.org/plugins/maven-javadoc-plugin/) | 2.5 | Apache Maven |
| jdk | [`maven-pmd-plugin`](https://maven.apache.org/plugins/maven-pmd-plugin/) | 3.14.0 | Apache Maven |
| jdk | [`maven-surefire-plugin`](https://maven.apache.org/plugins/maven-surefire-plugin/) | 2.5 | Apache Maven |
| jdk | [`maven-failsafe-plugin`](https://maven.apache.org/plugins/maven-failsafe-plugin/) | 2.5 | Apache Maven |
| jdk | [`animal-sniffer-maven-plugin`](https://www.mojohaus.org/animal-sniffer/animal-sniffer-maven-plugin/) | 1.3 | MojoHaus |
| jdk | [`cassandra-maven-plugin`](https://www.mojohaus.org/cassandra-maven-plugin/) | 0.7.0-1 | MojoHaus |
| jdk | [`exec-maven-plugin`](https://www.mojohaus.org/exec-maven-plugin/) | 1.1.1 | MojoHaus |
| jdk | [`jdiff-maven-plugin`](https://www.mojohaus.org/jdiff-maven-plugin/) | 1.0-beta-1-SNAPSHOT | MojoHaus |
| jdk | [`keytool-maven-plugin`](https://www.mojohaus.org/keytool/keytool-maven-plugin/) | 1.4 | MojoHaus |
| protobuf | [`protobuf-maven-plugin`](https://www.xolstice.org/protobuf-maven-plugin/examples/protobuf-toolchain.html) | 0.6.1 | github |
[](https://maven.apache.org/guides/mini/guide-using-toolchains.html)
Using Toolchains in Your Project[](https://maven.apache.org/guides/mini/guide-using-toolchains.html#using-toolchains-in-your-project)
-------------------------------------------------------------------------------------------------------------------------------------

There are two essential components that you need to configure in order to use toolchains:

1.   the [`maven-toolchains-plugin`](https://maven.apache.org/plugins/maven-toolchains-plugin/) in your project POM,
2.   the [`toolchains.xml`](https://maven.apache.org/ref/current/maven-core/toolchains.html) file on the building machine.

The `maven-toolchains-plugin` is the one that sets the toolchain to be used by the toolchain-aware plugins in your project.

For example, you want to use a different JDK version to build your project than the version used to run Maven, you can configure the version you want to use via this plugin as shown in the `pom.xml` below:

1.   `<plugins>`
2.   `...`
3.   `<plugin>`
4.   `<groupId>org.apache.maven.plugins</groupId>`
5.   `<artifactId>maven-compiler-plugin</artifactId>`
6.   `<version>3.1</version>`
7.   `</plugin>`
8.   `<plugin>`
9.   `<groupId>org.apache.maven.plugins</groupId>`
10.   `<artifactId>maven-toolchains-plugin</artifactId>`
11.   `<version>1.1</version>`
12.   `<executions>`
13.   `<execution>`
14.   `<goals>`
15.   `<goal>toolchain</goal>`
16.   `</goals>`
17.   `</execution>`
18.   `</executions>`
19.   `<configuration>`
20.   `<toolchains>`
21.   `<jdk>`
22.   `<version>1.8</version>`
23.   `<vendor>openjdk</vendor>`
24.   `</jdk>`
25.   `</toolchains>`
26.   `</configuration>`
27.   `</plugin>`
28.   `...`
29.   `</plugins>`

As you can see in the example above, a JDK toolchain with `<version>` “1.8” and `<vendor>` “openjdk” is to be used. Now how does the plugin know where this JDK is installed? This is where the `toolchains.xml` file comes in.

The `toolchains.xml` file (see below) is the configuration file where you set the installation paths of your toolchains. This file should be put in the `${user.home}/.m2` directory. When the `maven-toolchains-plugin` executes, it looks for the `toolchains.xml` file, reads it and looks for a toolchain matching the toolchains requirements configured in the plugin. In this example, that is a JDK toolchain with `<version>` “1.8” and `<vendor>` “openjdk”. Once a match is found, the plugin then stores the toolchain to be used in the MavenSession. As you can see in the `toolchains.xml` below, there is indeed a JDK toolchain with `<version>` “1.8” and `<vendor>` “openjdk” configured. So when the `maven-compiler-plugin` configured in the `pom.xml` above executes, it sees that a JDK toolchain is set in the MavenSession and will use that toolchain (that would be the JDK installed at `/path/to/jdk/1.8` in this example) to compile the sources.

Starting with [Maven 3.3.1](https://maven.apache.org/docs/3.3.1/release-notes.html) you can put the `toolchains.xml` file wherever you like by using the `--global-toolchains file` option, but it is recommended to locate it into `${user.home}/.m2/`.

1.   `<?xml version="1.0" encoding="UTF-8"?>`
2.   `<toolchains>`
3.   `<!-- JDK toolchains -->`
4.   `<toolchain>`
5.   `<type>jdk</type>`
6.   `<provides>`
7.   `<version>1.8</version>`
8.   `<vendor>openjdk</vendor>`
9.   `</provides>`
10.   `<configuration>`
11.   `<jdkHome>/path/to/jdk/1.8</jdkHome>`
12.   `</configuration>`
13.   `</toolchain>`
14.   `<toolchain>`
15.   `<type>jdk</type>`
16.   `<provides>`
17.   `<version>17</version>`
18.   `<vendor>azul</vendor>`
19.   `</provides>`
20.   `<configuration>`
21.   `<jdkHome>/path/to/jdk/17</jdkHome>`
22.   `</configuration>`
23.   `</toolchain>`

25.   `<!-- other toolchains -->`
26.   `<toolchain>`
27.   `<type>netbeans</type>`
28.   `<provides>`
29.   `<version>5.5</version>`
30.   `</provides>`
31.   `<configuration>`
32.   `<installDir>/path/to/netbeans/5.5</installDir>`
33.   `</configuration>`
34.   `</toolchain>`
35.   `</toolchains>`

You can configure as many toolchains as you want in your `toolchains.xml` file.
