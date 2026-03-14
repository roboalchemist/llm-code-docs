# Source: https://maven.apache.org/guides/mini/guide-configuring-plugins.html

Title: Guide to Configuring Plug-ins – Maven

URL Source: https://maven.apache.org/guides/mini/guide-configuring-plugins.html

Published Time: Fri, 13 Mar 2026 07:11:32 GMT

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
*   [Introduction](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Introduction)
*   [Generic Configuration](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Generic_Configuration)
    *   [Help Goal](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Help_Goal)
    *   [Configuring Parameters](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Configuring_Parameters)
        *   [Mapping Value Objects](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Value_Objects)
        *   [Mapping Complex Objects](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Complex_Objects)
        *   [Mapping Collection Types](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Collection_Types)
            *   [Mapping Collections and Arrays](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Collections_and_Arrays)
            *   [Mapping Maps](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Maps)
            *   [Mapping Properties](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Mapping_Properties)

*   [Configuring Build Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Configuring_Build_Plugins)
    *   [Using the <executions> Tag](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3Cexecutions.3E_Tag)
    *   [Using the <dependencies> Tag](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3Cdependencies.3E_Tag)
    *   [Using the <inherited> Tag In Build Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3Cinherited.3E_Tag_In_Build_Plugins)

*   [Configuring Reporting Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Configuring_Reporting_Plugins)
    *   [Using the <reporting> Tag VS <build> Tag](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3Creporting.3E_Tag_VS_.3Cbuild.3E_Tag)
    *   [Using the <reportSets> Tag](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3CreportSets.3E_Tag)
    *   [Using the <inherited> Tag In Reporting Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#Using_the_.3Cinherited.3E_Tag_In_Reporting_Plugins)

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
Introduction[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#introduction)
------------------------------------------------------------------------------------------------

In Maven, there are two kinds of plugins, build and reporting:

*   **Build plugins** are executed during the build and configured in the `<build/>` element.
*   **Reporting plugins** are executed during the site generation and configured in the `<reporting/>` element.

All plugins should have at least the minimal required [information](https://maven.apache.org/ref/current/maven-model/maven.html#class_plugin): `groupId`, `artifactId` and `version`.

If no `groupId` is defined for a plugin in the `build` or `reporting` section of the POM file, Maven uses the group ID `org.apache.maven.plugins`. This means that Maven assumes an official Maven plugin will be used.

If a plugin is called from the command line without a fully qualified name, for example `mvn versions:set`, Maven searches for plugins with the group ID `org.apache.maven.plugins` or `org.codehaus.mojo`.

**Important Note**: Always define the version of each plugin to guarantee build reproducibility. A good practice is to specify each build plugin's version in a `<build><pluginManagement/></build>` element. Often the `<pluginManagement/>` element is found in the parent POM. For reporting plugins, specify each version in the `<reporting><plugins/></reporting>` element (and in the `<build><pluginManagement/></build>` element too).

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
Generic Configuration[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#generic-configuration)
------------------------------------------------------------------------------------------------------------------

Maven plugins (build and reporting) are configured by specifying a `<configuration>` element where the child elements of the `<configuration>` element are mapped to fields, or setters, inside your Mojo. (Remember that a plug-in consists of one or more Mojos where a Mojo maps to a goal.) Say, for example, you have a Mojo that performs a query against a particular URL, with a specified timeout and list of options. The Mojo might look like the following:

1.   `@Mojo( name = "query" )`
2.   `public class MyQueryMojo`
3.   `extends AbstractMojo`
4.   `{`
5.   `@Parameter(property = "query.url", required = true)`
6.   `private String url;`

8.   `@Parameter(property = "timeout", required = false, defaultValue = "50")`
9.   `private int timeout;`

11.   `@Parameter(property = "options")`
12.   `private String[] options;`

14.   `public void execute()`
15.   `throws MojoExecutionException`
16.   `{`
17.   `...`
18.   `}`
19.   `}`

To configure the Mojo from your POM with the desired URL, timeout and options you might have something like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<artifactId>maven-myquery-plugin</artifactId>`
7.   `<version>1.0</version>`
8.   `<configuration>`
9.   `<url>http://www.foobar.com/query</url>`
10.   `<timeout>10</timeout>`
11.   `<options>`
12.   `<option>one</option>`
13.   `<option>two</option>`
14.   `<option>three</option>`
15.   `</options>`
16.   `</configuration>`
17.   `</plugin>`
18.   `</plugins>`
19.   `</build>`
20.   `...`
21.   `</project>`

The elements in the configuration match the names of the fields in the Mojo. The mapping is straight forward. The `url` element maps to the `url` field, the `timeout` element maps to the `timeout` field, and the `options` element maps to the `options` field. The mapping mechanism can deal with arrays by inspecting the type of the field and determining if a suitable mapping is possible.

For Mojos that are intended to be executed directly from the CLI, their parameters usually provide a means to be configured via system properties instead of a `<configuration>` section in the POM. The plugin documentation for those parameters will list an _expression_ that denotes the system properties for the configuration. In the Mojo above, the parameter `url` is associated with the expression `${query.url}`, meaning its value can be specified by the system property `query.url` as shown below:

```
mvn myquery:query -Dquery.url=http://maven.apache.org
```

The name of the system property does not necessarily match the name of the mojo parameter. While this is a rather common practice, you will often notice plugins that employ some prefix for the system properties to avoid name clashes with other system properties. Though rarely, there are also plugin parameters that (e.g. for historical reasons) employ system properties which are completely unrelated to the parameter name. So be sure to have a close look at the plugin documentation.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Help Goal[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#help-goal)

Most Maven plugins have a `help` goal that prints a description of the plugin and its parameters and types. For instance, to see help for the javadoc goal, type:

```
mvn javadoc:help -Ddetail -Dgoal=javadoc
```

And you will see all parameters for the javadoc:javadoc goal, similar to this [page](https://maven.apache.org/plugins/maven-javadoc-plugin/javadoc-mojo.html).

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Configuring Parameters[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#configuring-parameters)

Parameterization of Mojos relies internally on the Plexus Component Configuration API provided by [sisu-plexus](https://github.com/eclipse/sisu.plexus).

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
#### Mapping Value Objects[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-value-objects)

Mapping value types, like Boolean or Integer, is very simple. The `<configuration>` element might look like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<configuration>`
4.   `<myString>a string</myString>`
5.   `<myBoolean>true</myBoolean>`
6.   `<myInteger>10</myInteger>`
7.   `<myDouble>1.0</myDouble>`
8.   `<myFile>c:\temp</myFile>`
9.   `<myURL>http://maven.apache.org</myURL>`
10.   `</configuration>`
11.   `...`
12.   `</project>`

The detailed type coercion is explained in the table below. For conversion to primitive types their according [wrapper classes are used and automatically unboxed](https://docs.oracle.com/javase/tutorial/java/data/autoboxing.html).

| Parameter Class | Conversion from String |
| --- | --- |
| `Boolean` | [`Boolean.valueOf(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html#valueOf-java.lang.String-) |
| `Byte` | [`Byte.decode(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Byte.html#decode-java.lang.String-) |
| `Character` | [`Character.valueOf(char)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#valueOf-char-) of the first character in the given string |
| `Class` | [`Class.forName(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#forName-java.lang.String-) |
| `java.util.Date` | [`SimpleDateFormat.parse(String)`](https://docs.oracle.com/javase/8/docs/api/java/text/DateFormat.html#parse-java.lang.String-) for the following patterns: `yyyy-MM-dd hh:mm:ss.S a`, `yyyy-MM-dd hh:mm:ssa`, `yyyy-MM-dd HH:mm:ss.S` or `yyyy-MM-dd HH:mm:ss` |
| `Double` | [`Double.valueOf(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html#valueOf-java.lang.String-) |
| `Enum` | [`Enum.valueOf(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.String-) |
| `java.io.File` | [`new File(String)`](https://docs.oracle.com/javase/8/docs/api/java/io/File.html#File-java.lang.String-) with the file separators normalized to `File.separatorChar`. In case the file is relative, is is made absolute by prefixing it with the project's base directory. |
| `Float` | [`Float.valueOf(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Float.html#valueOf-java.lang.String-) |
| `Integer` | [`Integer.decode(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html#decode-java.lang.String-) |
| `Long` | [`Long.decode(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html#decode-java.lang.String-) |
| `Short` | [`Short.decode(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/Short.html#decode-java.lang.String-) |
| `String` | n/a |
| `StringBuffer` | [`new StringBuffer(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html#StringBuffer-java.lang.String-) |
| `StringBuilder` | [`new StringBuilder(String)`](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html#StringBuilder-java.lang.String-) |
| `java.net.URI` | [`new URI(String)`](https://docs.oracle.com/javase/8/docs/api/java/net/URI.html#URI-java.lang.String-) |
| `java.net.URL` | [`new URL(String)`](https://docs.oracle.com/javase/8/docs/api/java/net/URL.html#URL-java.lang.String-) |
[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
#### Mapping Complex Objects[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-complex-objects)

Mapping complex types is also fairly straight forward. Let's look at a simple example where we are trying to map a configuration for Person object. The `<configuration/>` element might look like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<configuration>`
4.   `<person>`
5.   `<firstName>Jason</firstName>`
6.   `<lastName>van Zyl</lastName>`
7.   `</person>`
8.   `</configuration>`
9.   `...`
10.   `</project>`

The rules for mapping complex objects are as follows:

*   There must be a private field that corresponds to name of the element being mapped. So in our case the `person` element must map to a `person` field in the mojo.
*   The object instantiated must be in the same package as the Mojo itself. So if your mojo is in `com.mycompany.mojo.query` then the mapping mechanism will look in that package for an object named `Person`. The mechanism capitalizes the first letter of the element name and uses that to search for the object to instantiate.
*   If you wish to have the object to be instantiated live in a different package or have a more complicated name, specify this using an `implementation` attribute like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<configuration>`
4.   `<person implementation="com.mycompany.mojo.query.SuperPerson">`
5.   `<firstName>Jason</firstName>`
6.   `<lastName>van Zyl</lastName>`
7.   `</person>`
8.   `</configuration>`
9.   `...`
10.   `</project>`

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
#### Mapping Collection Types[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-collection-types)

The configuration mapping mechanism can easily deal with most collections so let's go through a few examples to show you how it's done:

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
##### Mapping Collections and Arrays[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-collections-and-arrays)

Mapping to collections works in much the same way as mapping to arrays. Each item is given in the XML as dedicated element. The element name does not matter in that case. So if you have a mojo like the following:

1.   `public class MyAnimalMojo`
2.   `extends AbstractMojo`
3.   `{`
4.   `@Parameter(property = "animals")`
5.   `private List<String> animals;`

7.   `public void execute()`
8.   `throws MojoExecutionException`
9.   `{`
10.   `...`
11.   `}`
12.   `}`

where you have a field named `animals` then your configuration for the plug-in would look like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<artifactId>maven-myanimal-plugin</artifactId>`
7.   `<version>1.0</version>`
8.   `<configuration>`
9.   `<animals>`
10.   `<animal>cat</animal>`
11.   `<animal>dog</animal>`
12.   `<animal>aardvark</animal>`
13.   `</animals>`
14.   `</configuration>`
15.   `</plugin>`
16.   `</plugins>`
17.   `</build>`
18.   `...`
19.   `</project>`

Where each of the animals listed would be entries in the `animals` field. Unlike arrays, collections do not necessarily have a specific component type. In order to derive the type of a collection item, the following strategy is used:

1.   If the first item XML element contains an `implementation` hint attribute, try to load the class with the given fully qualified class name from the attribute value
2.   If the first item XML element contains a `.`, try to load the class with the fully qualified class name given in the element name
3.   Try the first item XML element name (with capitalized first letter) as a class in the same package as the mojo/object being configured
4.   Use the parameter type information from either [`Field.getGenericType()`](https://docs.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getGenericType()) or [`Method.getGenericParameterTypes()`](https://docs.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getGenericParameterTypes())
5.   If the element has no children, assume its type is `String`. Otherwise, the configuration will fail.

The following collection implementations are being used when there is no `implementation` hint attribute in the XML element representing the collection:

| Collection Class | Used for |
| --- | --- |
| `TreeSet` | for all types assignable to `SortedSet` |
| `HashSet` | for all types assignable to `Set` |
| `ArrayList` | for every other `Collection` type which is not a `Map` |

Since Maven 3.3.9 ([MNG-5440](https://issues.apache.org/jira/browse/MNG-5440)), you can list individual items alternatively as comma-separated list in the XML value of animals directly. This approach is also used if configuring collection/array parameters via command line The following example is equivalent to the example above:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<artifactId>maven-myanimal-plugin</artifactId>`
7.   `<version>1.0</version>`
8.   `<configuration>`
9.   `<animals>cat,dog,aardvark</animals>`
10.   `</configuration>`
11.   `</plugin>`
12.   `</plugins>`
13.   `</build>`
14.   `...`
15.   `</project>`

Each item is mapped again according to the rules of this section depending on the type of the collection/array.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
##### Mapping Maps[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-maps)

In the same way, you could define maps like the following:

1.   `...`
2.   `@Parameter`
3.   `private Map<String,String> myMap;`
4.   `...`

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<configuration>`
4.   `<myMap>`
5.   `<key1>value1</key1>`
6.   `<key2>value2</key2>`
7.   `</myMap>`
8.   `</configuration>`
9.   `...`
10.   `</project>`

Unlike Collections the value type for Maps is always derived from the parameter type information from either [`Field.getGenericType()`](https://docs.oracle.com/javase/7/docs/api/java/lang/reflect/Field.html#getGenericType()) or [`Method.getGenericParameterTypes()`](https://docs.oracle.com/javase/7/docs/api/java/lang/reflect/Method.html#getGenericParameterTypes()). It falls back to `String`. The key type must always be `String`.

In contrast to value objects and collections/arrays there is no string coercion defined for maps, i.e. you cannot give parameters of that type via CLI argument.

The map implementation class is by default `TreeMap` but can be overridden with an `implementation` attribute on the XML element representing the map.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
##### Mapping Properties[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#mapping-properties)

Properties should be defined like the following:

1.   `...`
2.   `@Parameter`
3.   `private Properties myProperties;`
4.   `...`

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<configuration>`
4.   `<myProperties>`
5.   `<property>`
6.   `<name>propertyName1</name>`
7.   `<value>propertyValue1</value>`
8.   `</property>`
9.   `<property>`
10.   `<name>propertyName2</name>`
11.   `<value>propertyValue2</value>`
12.   `</property>`
13.   `</myProperties>`
14.   `</configuration>`
15.   `...`
16.   `</project>`

In contrast to value objects and collections/arrays there is no string coercion defined for properties, i.e. you cannot give parameters of those type via CLI argument.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
Configuring Build Plugins[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#configuring-build-plugins)
--------------------------------------------------------------------------------------------------------------------------

The following is only to configure Build plugins in the `<build>` element.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<executions>` Tag[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-executions-tag)

You can also configure a mojo using the `<executions>` tag. This is most commonly used for mojos that are intended to participate in some phases of the [build lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html). Using `MyQueryMojo` as an example, you may have something that will look like:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<artifactId>maven-myquery-plugin</artifactId>`
7.   `<version>1.0</version>`
8.   `<executions>`
9.   `<execution>`
10.   `<id>execution1</id>`
11.   `<phase>test</phase>`
12.   `<configuration>`
13.   `<url>http://www.foo.com/query</url>`
14.   `<timeout>10</timeout>`
15.   `<options>`
16.   `<option>one</option>`
17.   `<option>two</option>`
18.   `<option>three</option>`
19.   `</options>`
20.   `</configuration>`
21.   `<goals>`
22.   `<goal>query</goal>`
23.   `</goals>`
24.   `</execution>`
25.   `<execution>`
26.   `<id>execution2</id>`
27.   `<configuration>`
28.   `<url>http://www.bar.com/query</url>`
29.   `<timeout>15</timeout>`
30.   `<options>`
31.   `<option>four</option>`
32.   `<option>five</option>`
33.   `<option>six</option>`
34.   `</options>`
35.   `</configuration>`
36.   `<goals>`
37.   `<goal>query</goal>`
38.   `</goals>`
39.   `</execution>`
40.   `</executions>`
41.   `</plugin>`
42.   `</plugins>`
43.   `</build>`
44.   `...`
45.   `</project>`

The first execution with id `execution1` binds this configuration to the test phase. The second execution does not have a `<phase>` tag, how do you think will this execution behave? Well, goals can have a default phase binding as discussed further below. If the goal has a default phase binding then it will execute in that phase. But if the goal is not bound to any lifecycle phase then it simply won't be executed during the build lifecycle.

Note that while execution id's have to be unique among all executions of a single plugin within a POM, they don't have to be unique across an inheritance hierarchy of POMs. Executions with different id's are merged, meaning they are all executed in the hierarchy order (parent first). Executions with the same id from different POMs are overwritten by child configuration.

The same applies to executions that are defined by profiles.

How about if we have a multiple executions with different phases bound to it? How do you think will it behave? Let us use the example POM above again, but this time we shall bind `execution2` to a phase.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `...`
7.   `<executions>`
8.   `<execution>`
9.   `<id>execution1</id>`
10.   `<phase>test</phase>`
11.   `...`
12.   `</execution>`
13.   `<execution>`
14.   `<id>execution2</id>`
15.   `<phase>install</phase>`
16.   `<configuration>`
17.   `<url>http://www.bar.com/query</url>`
18.   `<timeout>15</timeout>`
19.   `<options>`
20.   `<option>four</option>`
21.   `<option>five</option>`
22.   `<option>six</option>`
23.   `</options>`
24.   `</configuration>`
25.   `<goals>`
26.   `<goal>query</goal>`
27.   `</goals>`
28.   `</execution>`
29.   `</executions>`
30.   `</plugin>`
31.   `</plugins>`
32.   `</build>`
33.   `...`
34.   `</project>`

If there are multiple executions bound to different phases, then the mojo is executed once for each phase indicated. Meaning, `execution1` will be executed applying the configuration setup during the test phase, while `execution2` will be executed applying the configuration setup during the install phase.

It's possible to bind multiple executions to the same phase, for example if you want to do multiple things inside the same phase. Those are executed in the same order as they are declared in the POM. This also applies to inherited definitions. A parents declaration is execution before the child's declaration. Since Maven 4 it's possible to explicit define the order of multiple executions by using square brackets with an integer at the end of the phase name. A higher number means a later execution. Using the following definition would execute `execution2` before `execution1`, but both in the test phase.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `...`
7.   `<executions>`
8.   `<execution>`
9.   `<id>execution1</id>`
10.   `<phase>test[200]</phase>`
11.   `...`
12.   `</execution>`
13.   `<execution>`
14.   `<id>execution2</id>`
15.   `<phase>test[100]</phase>`
16.   `...`
17.   `</execution>`
18.   `</executions>`
19.   `</plugin>`
20.   `</plugins>`
21.   `</build>`
22.   `...`
23.   `</project>`

Now, let us have another mojo example which shows a default lifecycle phase binding.

1.   `@Mojo( name = "query", defaultPhase = LifecyclePhase.PACKAGE )`
2.   `public class MyBoundQueryMojo`
3.   `extends AbstractMojo`
4.   `{`
5.   `@Parameter(property = "query.url", required = true)`
6.   `private String url;`

8.   `@Parameter(property = "timeout", required = false, defaultValue = "50")`
9.   `private int timeout;`

11.   `@Parameter(property = "options")`
12.   `private String[] options;`

14.   `public void execute()`
15.   `throws MojoExecutionException`
16.   `{`
17.   `...`
18.   `}`
19.   `}`

From the above mojo example, `MyBoundQueryMojo` is by default bound to the package phase (see the `@phase` notation). But if we want to execute this mojo during the install phase and not with package we can rebind this mojo into a new lifecycle phase using the `<phase>` tag under `<execution>`.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<artifactId>maven-myquery-plugin</artifactId>`
7.   `<version>1.0</version>`
8.   `<executions>`
9.   `<execution>`
10.   `<id>execution1</id>`
11.   `<phase>install</phase>`
12.   `<configuration>`
13.   `<url>http://www.bar.com/query</url>`
14.   `<timeout>15</timeout>`
15.   `<options>`
16.   `<option>four</option>`
17.   `<option>five</option>`
18.   `<option>six</option>`
19.   `</options>`
20.   `</configuration>`
21.   `<goals>`
22.   `<goal>query</goal>`
23.   `</goals>`
24.   `</execution>`
25.   `</executions>`
26.   `</plugin>`
27.   `</plugins>`
28.   `</build>`
29.   `...`
30.   `</project>`

Now, `MyBoundQueryMojo` default phase which is package has been overridden by install phase.

**Note:** Configurations inside the `<executions>` element used to differ from those that are outside `<executions>` in that they could not be used from a direct command line invocation because they were only applied when the lifecycle phase they were bound to was invoked. So you had to move a configuration section outside of the executions section to apply it globally to all invocations of the plugin. Since Maven 3.3.1 this is not the case anymore as you can specify on the command line the execution id for direct plugin goal invocation. Hence if you want to run the above plugin and it's specific `execution1`'s configuration from the command-line, you can execute:

```
mvn myquery:query@execution1
```
[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<dependencies>` Tag[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-dependencies-tag)

You could configure the dependencies of the Build plugins, commonly to use a more recent dependency version.

For instance, the Maven Antrun Plugin version 1.2 uses Ant version 1.6.5, if you want to use the latest Ant version when running this plugin, you need to add `<dependencies>` element like the following:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-antrun-plugin</artifactId>`
8.   `<version>1.2</version>`
9.   `...`
10.   `<dependencies>`
11.   `<dependency>`
12.   `<groupId>org.apache.ant</groupId>`
13.   `<artifactId>ant</artifactId>`
14.   `<version>1.7.1</version>`
15.   `</dependency>`
16.   `<dependency>`
17.   `<groupId>org.apache.ant</groupId>`
18.   `<artifactId>ant-launcher</artifactId>`
19.   `<version>1.7.1</version>`
20.   `</dependency>`
21.   `</dependencies>`
22.   `</plugin>`
23.   `</plugins>`
24.   `</build>`
25.   `...`
26.   `</project>`

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<inherited>` Tag In Build Plugins[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-inherited-tag-in-build-plugins)

By default, plugin configuration should be propagated to child POMs, so to break the inheritance, you could use the `<inherited>` tag:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-antrun-plugin</artifactId>`
8.   `<version>1.2</version>`
9.   `<inherited>false</inherited>`
10.   `...`
11.   `</plugin>`
12.   `</plugins>`
13.   `</build>`
14.   `...`
15.   `</project>`

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
Configuring Reporting Plugins[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#configuring-reporting-plugins)
----------------------------------------------------------------------------------------------------------------------------------

The following is only to configure Reporting plugins in the `<reporting>` element.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<reporting>` Tag VS `<build>` Tag[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-reporting-tag-vs-build-tag)

Configuring a reporting plugin in the `<reporting>` or `<build>` elements in the pom does not exactly have the same results.

`mvn site`Since maven-site-plugin 3.4, it uses the parameters defined in the `<configuration>` element of each reporting Plugin specified in the `<reporting>` element, in addition to the parameters defined in the `<configuration>` element of each plugin specified in `<build>` (parameters from `<build>` section were previously ignored).`mvn aplugin:areportgoal`It **ignores** the parameters defined in the `<configuration>` element of each reporting Plugin specified in the `<reporting>` element; only parameters defined in the `<configuration>` element of each plugin specified in `<build>` are used.[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<reportSets>` Tag[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-reportsets-tag)

You can configure a reporting plugin using the `<reportSets>` tag. This is most commonly used to generate reports selectively when running `mvn site`. The following will generate only the project team report.

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<reporting>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-project-info-reports-plugin</artifactId>`
8.   `<version>2.1.2</version>`
9.   `<reportSets>`
10.   `<reportSet>`
11.   `<reports>`
12.   `<report>project-team</report>`
13.   `</reports>`
14.   `</reportSet>`
15.   `</reportSets>`
16.   `</plugin>`
17.   `</plugins>`
18.   `</reporting>`
19.   `...`
20.   `</project>`

**Notes**:

1.   To exclude all reports, you need to use:

    1.   `<reportSets>`
    2.   `<reportSet>`
    3.   `<reports/>`
    4.   `</reportSet>`
    5.   `</reportSets>`

2.   Refer to each Plugin Documentation (i.e. plugin-info.html) to know the available report goals.

[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)
### Using the `<inherited>` Tag In Reporting Plugins[](https://maven.apache.org/guides/mini/guide-configuring-plugins.html#using-the-inherited-tag-in-reporting-plugins)

Similar to the build plugins, to break the inheritance, you can use the `<inherited>` tag:

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<reporting>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.apache.maven.plugins</groupId>`
7.   `<artifactId>maven-project-info-reports-plugin</artifactId>`
8.   `<version>2.1.2</version>`
9.   `<inherited>false</inherited>`
10.   `</plugin>`
11.   `</plugins>`
12.   `</reporting>`
13.   `...`
14.   `</project>`
