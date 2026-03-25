# Source: https://maven.apache.org/guides/plugin/guide-java-plugin-development.html

Title: Guide to Developing Java Plugins – Maven

URL Source: https://maven.apache.org/guides/plugin/guide-java-plugin-development.html

Markdown Content:
[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
This guide is intended to assist users in developing Java plugins for Maven.

*   [Important Notice](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Important_Notice)
*   [Your First Plugin](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Your_First_Plugin)
    *   [Your First Mojo](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Your_First_Mojo)
        *   [A Simple Mojo](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#A_Simple_Mojo)

    *   [Project Definition](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Project_Definition)
    *   [Building a Plugin](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Building_a_Plugin)
    *   [Executing Your First Mojo](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Executing_Your_First_Mojo)
        *   [Shortening the Command Line](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Shortening_the_Command_Line)
        *   [Attaching the Mojo to the Build Lifecycle](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Attaching_the_Mojo_to_the_Build_Lifecycle)

*   [Mojo archetype](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Mojo_archetype)
*   [Parameters](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Parameters)
    *   [Defining Parameters Within a Mojo](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Defining_Parameters_Within_a_Mojo)
    *   [Configuring Parameters in a Project](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Configuring_Parameters_in_a_Project)

*   [Using Setters](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Using_Setters)
*   [Plugin Documentation](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Plugin_Documentation)
*   [Resources](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Resources)

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Important Notice[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#important-notice)
--------------------------------------------------------------------------------------------------------------

[**Plugin Naming Convention and Apache Maven Trademark**](https://maven.apache.org/guides/mini/guide-naming-conventions.html)

You will typically name your plugin `<yourplugin>-maven-plugin`.

Calling it `maven-<yourplugin>-plugin` (note "Maven" is at the beginning of the plugin name) is **strongly discouraged** since it's a **reserved naming pattern for official Apache Maven plugins maintained by the Apache Maven team** with groupId `org.apache.maven.plugins`.

Using this naming pattern is an infringement of the Apache Maven Trademark.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Your First Plugin[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#your-first-plugin)
----------------------------------------------------------------------------------------------------------------

In this section we will build a simple plugin with one goal that takes no parameters and displays a message on the screen when run. Along the way, we will cover setting up a project to create a plugin, the minimal contents of a Java mojo which will define goal code, and a couple ways to execute the mojo.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Your First Mojo[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#your-first-mojo)

At its simplest, a Java mojo consists simply of a single class representing one plugin's goal. When processing the source tree to find mojos, [`plugin-tools`](https://maven.apache.org/plugin-tools/) looks for classes with the `@Mojo` annotation. Any class with this annotation is included in the plugin configuration file.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
#### A Simple Mojo[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#a-simple-mojo)

Listed below is a simple mojo class which has no parameters. This is about as simple as a mojo can be. After the listing is a description of the various parts of the source.

1.   `package sample.plugin;`

3.   `import org.apache.maven.plugin.AbstractMojo;`
4.   `import org.apache.maven.plugin.MojoExecutionException;`
5.   `import org.apache.maven.plugins.annotations.Mojo;`

7.   `/**`
8.   `* Says "Hi" to the user.`
9.   `*`
10.   `*/`
11.   `@Mojo(name = "sayhi")`
12.   `public class GreetingMojo extends AbstractMojo`
13.   `{`
14.   `@Override`
15.   `public void execute() throws MojoExecutionException`
16.   `{`
17.   `getLog().info("Hello, world.");`
18.   `}`
19.   `}`

*   The class `org.apache.maven.plugin.AbstractMojo` provides most of the infrastructure required to implement a mojo except for the `execute` method.
*   The annotation "`@Mojo`" is required and controls how and when the mojo is executed.
*   The `execute` method can throw `org.apache.maven.plugin.MojoExecutionException` if a problem occurs. Throwing this exception causes a `BUILD FAILURE` message to be displayed.
*   The `getLog` method (defined in `AbstractMojo`) returns a log4j-like logger object which allows plugins to create messages at levels of "debug", "info", "warn", and "error". This logger is the accepted means to display information to the user. See [Retrieving the Mojo Logger](https://maven.apache.org/plugin-developers/common-bugs.html#Retrieving_the_Mojo_Logger) for a hint on its proper usage.

All Mojo annotations are described by the [Mojo API Specification](https://maven.apache.org/developers/mojo-api-specification.html#The_Descriptor_and_Annotations).

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Project Definition[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#project-definition)

Once the mojos have been written for the plugin, it is time to build the plugin. To do this properly, the project's pom.xml must set these things:

`groupId`This is the group ID for the plugin, and should match the common prefix to the packages used by the mojos.
`artifactId`This is the name of the plugin.
`version`This is the version of the plugin.
`packaging`This must be set to "`maven-plugin`"
`dependencies`A dependency must be declared on the Maven Plugin Tools API to resolve "`AbstractMojo`" and related classes

Listed below is an illustration of the sample mojo project's pom with the parameters set as described in the above table:

1.   `<project>`
2.   `<modelVersion>4.0.0</modelVersion>`

4.   `<groupId>sample.plugin</groupId>`
5.   `<artifactId>hello-maven-plugin</artifactId>`
6.   `<version>1.0-SNAPSHOT</version>`
7.   `<packaging>maven-plugin</packaging>`

9.   `<name>Sample Parameter-less Maven Plugin</name>`

11.   `<properties>`
12.   `<maven-plugin-tools.version>3.15.2</maven-plugin-tools.version>`
13.   `</properties>`

15.   `<dependencies>`
16.   `<dependency>`
17.   `<groupId>org.apache.maven</groupId>`
18.   `<artifactId>maven-plugin-api</artifactId>`
19.   `<version>3.9.9</version>`
20.   `<scope>provided</scope>`
21.   `</dependency>`

23.   `<!-- dependency on annotations -->`
24.   `<dependency>`
25.   `<groupId>org.apache.maven.plugin-tools</groupId>`
26.   `<artifactId>maven-plugin-annotations</artifactId>`
27.   `<version>${maven-plugin-tools.version}</version>`
28.   `<scope>provided</scope>`
29.   `</dependency>`
30.   `</dependencies>`

32.   `<build>`
33.   `<pluginManagement>`
34.   `<plugins>`
35.   `<plugin>`
36.   `<groupId>org.apache.maven.plugins</groupId>`
37.   `<artifactId>maven-plugin-plugin</artifactId>`
38.   `<version>${maven-plugin-tools.version}</version>`
39.   `<executions>`
40.   `<execution>`
41.   `<id>help-mojo</id>`
42.   `<goals>`
43.   `<!-- good practice is to generate help mojo for plugin -->`
44.   `<goal>helpmojo</goal>`
45.   `</goals>`
46.   `</execution>`
47.   `</executions>`
48.   `</plugin>`
49.   `</plugins>`
50.   `</pluginManagement>`
51.   `</build>`

53.   `<reporting>`
54.   `<plugins>`
55.   `<!-- automatically generate plugin documentation when running `mvn site` -->`
56.   `<plugin>`
57.   `<groupId>org.apache.maven.plugins</groupId>`
58.   `<artifactId>maven-plugin-report-plugin</artifactId>`
59.   `<version>${maven-plugin-tools.version}</version>`
60.   `</plugin>`
61.   `</plugins>`
62.   `</reporting>`
63.   `</project>`

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Building a Plugin[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#building-a-plugin)

There are few plugin goals bound to the standard build lifecycle defined with the `maven-plugin` packaging:

`compile`Compiles the Java code for the plugin
`process-classes`Extracts data to build the [plugin descriptor](https://maven.apache.org/ref/current/maven-plugin-api/plugin.html)
`test`Runs the plugin's unit tests
`package`Builds the plugin jar
`install`Installs the plugin jar in the local repository
`deploy`Deploys the plugin jar to the remote repository

For more details, you can look at [detailed bindings for `maven-plugin` packaging](https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_maven-plugin_packaging).

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Executing Your First Mojo[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#executing-your-first-mojo)

The most direct means of executing your new plugin is to specify the plugin goal directly on the command line. To do this, configure the `hello-maven-plugin` plugin in the project:

1.   `<project>`
2.   `...`
3.   `<build>`
4.   `<pluginManagement>`
5.   `<plugins>`
6.   `<plugin>`
7.   `<groupId>sample.plugin</groupId>`
8.   `<artifactId>hello-maven-plugin</artifactId>`
9.   `<version>1.0-SNAPSHOT</version>`
10.   `</plugin>`
11.   `</plugins>`
12.   `</pluginManagement>`
13.   `</build>`
14.   `...`
15.   `</project>`

Then on the command line specify a fully-qualified goal in the form of:

mvn groupId:artifactId:version:goal
For example, to run the simple mojo in the sample plugin, enter "`mvn sample.plugin:hello-maven-plugin:1.0-SNAPSHOT:sayhi`" on the command line.

**Tips**: `version` is not required to run a standalone goal.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
#### Shortening the Command Line[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#shortening-the-command-line)

There are several ways to reduce the amount of required typing:

*   To run the latest version of a plugin installed in the local repository, you can omit its version number. So just use "`mvn sample.plugin:hello-maven-plugin:sayhi`" to run your plugin.
*   You can assign a shortened prefix to your plugin, such as `mvn hello:sayhi`. This is done automatically if you follow the convention of using `${prefix}-maven-plugin` (or `maven-${prefix}-plugin` if the plugin is part of the Apache Maven project). You may also assign one through additional configuration. For more information, see [Introduction to Plugin Prefix Mapping](https://maven.apache.org/guides/introduction/introduction-to-plugin-prefix-mapping.html).
*   Finally, you can also add your plugin's group ID to the list of group IDs searched by default. To do this, add the following to your `${user.home}/.m2/settings.xml` file: 
    1.   `<pluginGroups>`
    2.   `<pluginGroup>sample.plugin</pluginGroup>`
    3.   `</pluginGroups>`

At this point, you can run the mojo with "`mvn hello:sayhi`".

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
#### Attaching the Mojo to the Build Lifecycle[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#attaching-the-mojo-to-the-build-lifecycle)

You can also configure the plugin to attach specific goals to a particular phase of the build lifecycle. Here is an example:

1.   `<build>`
2.   `<pluginManagement>`
3.   `<plugins>`
4.   `<plugin>`
5.   `<groupId>sample.plugin</groupId>`
6.   `<artifactId>hello-maven-plugin</artifactId>`
7.   `<version>1.0-SNAPSHOT</version>`
8.   `</plugin>`
9.   `</plugins>`
10.   `</pluginManagement>`
11.   `<plugins>`
12.   `<plugin>`
13.   `<groupId>sample.plugin</groupId>`
14.   `<artifactId>hello-maven-plugin</artifactId>`
15.   `<executions>`
16.   `<execution>`
17.   `<phase>compile</phase>`
18.   `<goals>`
19.   `<goal>sayhi</goal>`
20.   `</goals>`
21.   `</execution>`
22.   `</executions>`
23.   `</plugin>`
24.   `</plugins>`
25.   `</build>`

This causes the simple mojo to be executed whenever Java code is compiled. For more information on binding a mojo to phases in the lifecycle, see the [Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html) document.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Mojo archetype[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#mojo-archetype)
----------------------------------------------------------------------------------------------------------

To create a new plugin project, you can use the Mojo [archetype](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html) with the following command line:

mvn archetype:generate \
  -DgroupId=sample.plugin \
  -DartifactId=hello-maven-plugin \
  -DarchetypeGroupId=org.apache.maven.archetypes \
  -DarchetypeArtifactId=maven-archetype-plugin[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Parameters[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#parameters)
--------------------------------------------------------------------------------------------------

It is unlikely that a mojo will be very useful without parameters. Parameters provide a few very important functions:

*   They provide hooks to allow the user to adjust the operation of the plugin to suit their needs.
*   They provide a means to easily extract the value of elements from the POM without the need to navigate the objects.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Defining Parameters Within a Mojo[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#defining-parameters-within-a-mojo)

Defining a parameter is as simple as creating an instance variable in the mojo and adding the proper annotations. Listed below is an example of a parameter for the simple mojo:

1.   `/**`
2.   `* The greeting to display.`
3.   `*/`
4.   `@Parameter(property = "sayhi.greeting", defaultValue = "Hello World!" )`
5.   `private String greeting;`

The Javadoc comment is the description of the parameter. The `@Parameter` annotation identifies the variable as a mojo parameter. The `defaultValue` element defines the default value for the parameter. This value can include expressions which reference the project, such as "`${project.version}`". (More can be found in the ["Parameter Expressions" document.](https://maven.apache.org/ref/current/maven-core/apidocs/org/apache/maven/plugin/PluginParameterExpressionEvaluator.html)) The `property` element enables configuration of the mojo parameter from the command line by referencing a system property that the user sets via the `-D` option.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
### Configuring Parameters in a Project[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#configuring-parameters-in-a-project)

Each Maven project can configure the plugins it uses in the `pluginManagement` section of the pom.xml. For example:

1.   `<plugin>`
2.   `<groupId>sample.plugin</groupId>`
3.   `<artifactId>hello-maven-plugin</artifactId>`
4.   `<version>1.0-SNAPSHOT</version>`
5.   `<configuration>`
6.   `<greeting>Welcome</greeting>`
7.   `</configuration>`
8.   `</plugin>`

In the configuration section, the element name ("`greeting`") is the parameter name and the content of the element ("`Welcome`") is the value to be assigned to the parameter.

**Note**: More details can be found in the [Guide to Configuring Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html).

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Using Setters[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#using-setters)
--------------------------------------------------------------------------------------------------------

You are not restricted to using private field mapping which is helpful if you are trying to make your Mojos reusable outside the context of Maven. In the example above, we could define public setter methods that the configuration mapping mechanism can use. You can also add an `@Parameter` annotation on the setter method (from version 3.7.0 of `plugin-tools`)

So the Mojo would look like the following:

2.   `public class MyQueryMojo extends AbstractMojo {`

4.   `// provide name for non matching field and setter name`
5.   `@Parameter(name = "url", property = "url")`
6.   `private String url;`

8.   `@Parameter(property = "timeout")`
9.   `private int timeout;`

11.   `private String option0;`
12.   `private String option1;`

14.   `public void setUrl(String url) {`
15.   `this.url = url;`
16.   `}`

18.   `public void setTimeout(int timeout) {`
19.   `this.timeout = timeout;`
20.   `}`

22.   `@Parameter(property = "options")`
23.   `public void setOptions(String[] options) {`
24.   `// we can do something more with provided parameter`
25.   `this.option0 = options[0];`
26.   `this.option1 = options[1];`
27.   `}`

29.   `@Override`
30.   `public void execute() throws MojoExecutionException {`
31.   `...`
32.   `}`
33.   `}`

The property annotation for each parameter tells Maven which setter and getter to use when the field's name does not match the name of the parameter in the plugin configuration.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Plugin Documentation[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#plugin-documentation)
----------------------------------------------------------------------------------------------------------------------

To make it easy for others to use your plugin, you should document it. See the [Plugin Documentation Guide](https://maven.apache.org/guides/development/guide-plugin-documentation.html) for more information.

[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
Resources[](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#resources)
------------------------------------------------------------------------------------------------

1.   [Mojo Documentation](https://maven.apache.org/developers/mojo-api-specification.html): Mojo API, Mojo annotations
2.   [Maven Plugin Testing Harness](https://maven.apache.org/shared/maven-plugin-testing-harness/): Testing framework for your Mojos.
3.   [Eclipse Sisu](https://eclipse.dev/sisu/index.html): The IoC container used by Maven 3.
4.   [Maven & JSR 330](https://maven.apache.org/maven-jsr330.html): How to use JSR 330 in Plugins
5.   [Common Bugs and Pitfalls](https://maven.apache.org/plugin-developers/common-bugs.html): Overview of problematic coding patterns.
