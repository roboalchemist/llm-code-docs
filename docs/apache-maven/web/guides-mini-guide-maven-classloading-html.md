# Source: https://maven.apache.org/guides/mini/guide-maven-classloading.html

Title: Guide to Maven Classloading – Maven

URL Source: https://maven.apache.org/guides/mini/guide-maven-classloading.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
This is a description of the classloader hierarchy in Maven.

*   [Overview](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Overview)
*   [Platform Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Platform_Classloader)
*   [System Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#System_Classloader)
*   [Core Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Core_Classloader)
*   [API Classloader](https://maven.apache.org/guides/mini/guide-maven-classloading.html#API_Classloader)
*   [Build Extension Classloaders](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Build_Extension_Classloaders)
*   [Project Classloaders](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Project_Classloaders)
*   [Plugin Classloaders](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Plugin_Classloaders)
*   [Custom Classloaders](https://maven.apache.org/guides/mini/guide-maven-classloading.html#Custom_Classloaders)

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Overview[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#overview)
---------------------------------------------------------------------------------------

Maven uses the [Plexus Classworlds](https://codehaus-plexus.github.io/plexus-classworlds/) classloading framework to create the classloader graph. If you look in your `${maven.home}/boot` directory, you will see a single JAR which is the Classworlds JAR we use to boot the classloader graph. The Classworlds JAR is the only element of the Java `CLASSPATH`. The other classloaders are built by Classworlds (“realms” in Classworlds terminology).

Each realm exposes

1.   optionally some classes imported from 0..n other classloaders
2.   optionally some classes from a directory or JAR
3.   one parent classloader

The search order is always as given above.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Platform Classloader[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#platform-classloader)
---------------------------------------------------------------------------------------------------------------

This is the classloader exposing all JRE classes.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
System Classloader[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#system-classloader)
-----------------------------------------------------------------------------------------------------------

It contains only Plexus Classworlds and imports the platform classloader.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Core Classloader[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#core-classloader)
-------------------------------------------------------------------------------------------------------

The second classloader down the graph contains the core requirements of Maven. **It is used by Maven internally but not by plugins**. The core classloader has the libraries in `${maven.home}/lib`. In general these are just Maven libraries. For example instances of [`MavenProject`](https://maven.apache.org/ref/current/apidocs/org/apache/maven/project/MavenProject.html) belong to this classloader.

You can add elements to this classloader by the means outlined in [Core Extension](https://maven.apache.org/guides/mini/guide-using-extensions.html). These are loaded through the same classloader as `${maven.home}/lib` and hence are available to the Maven core and all plugins for the current project (through the API Classloader, see next paragraph). More information is available in [Core Extension](https://maven.apache.org/guides/mini/guide-using-extensions.html).

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
API Classloader[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#api-classloader)
-----------------------------------------------------------------------------------------------------

The API classloader is a filtered view of the Core Classloader, done by exposing only the exported packages from all Core Extensions. The main API is listed in [Maven Core Extensions Reference](https://maven.apache.org/ref/current/maven-core/core-extensions.html).

This has been introduced with Maven 3.3.1 ([MNG-5771](https://issues.apache.org/jira/browse/MNG-5771)).

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Build Extension Classloaders[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#build-extension-classloaders)
-------------------------------------------------------------------------------------------------------------------------------

![Image 1: Build Extension Class Realm](https://maven.apache.org/buildExtensionClassRealm.svg)

For every plugin which is marked with `<extensions>true</extensions>` and every [build extension](https://maven.apache.org/ref/current/maven-model/maven.html#class_extension) listed in the according section of the POM, there is a dedicated classloader. Those are isolated. That is, one build extension does not have access to other build extensions. It imports everything from the API classloader. All JSR 330 or Plexus components declared in the underlying JAR are registered in the global Plexus container while creating the classloader. In addition all component references in the plugin descriptor are properly wired from the underlying Plexus container. Build extensions have limited effect as they are loaded late.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Project Classloaders[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#project-classloaders)
---------------------------------------------------------------------------------------------------------------

There is one project classloader per Maven project (identified through its coordinates). This one imports the API Classloader. In addition it exposes all classes from all Build Extension Classloaders which are bound to the current project. This is only released with the container. During the build outside Mojo executions, the thread's context classloader is set to the project classloader.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Plugin Classloaders[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#plugin-classloaders)
-------------------------------------------------------------------------------------------------------------

![Image 2: Plugin Class Realm](https://maven.apache.org/pluginClassRealm.svg)

Each plugin (which is not marked as build extension) has its own classloader that imports the Project classloader.

Plugins marked with `<extensions>true</extensions>` leverage the Build Extension classloader instead of the Plugin classloader.

Users can add dependencies to this classloader by adding dependencies to a plugin in the [`plugins/plugin`](https://maven.apache.org/ref/current/maven-model/maven.html#class_plugin) section of their project `pom.xml`. Here is a sample of adding `ant-nodeps` to the plugin classloader of the Antrun Plugin and hereby enabling the use of additional/optional Ant tasks:

1.   `<plugin>`
2.   `<groupId>org.apache.maven.plugins</groupId>`
3.   `<artifactId>maven-antrun-plugin</artifactId>`
4.   `<version>1.3</version>`
5.   `<dependencies>`
6.   `<dependency>`
7.   `<groupId>org.apache.ant</groupId>`
8.   `<artifactId>ant-nodeps</artifactId>`
9.   `<version>1.7.1</version>`
10.   `</dependency>`
11.   `</dependencies>`
12.   `...`
13.   `</plugin>`

Plugins can inspect their effective runtime class path via the expressions `${plugin.artifacts}` or `${plugin.artifactMap}` to have a list or map, respectively, of resolved artifacts injected from the [`PluginDescriptor`](https://maven.apache.org/ref/current/maven-plugin-api/apidocs/org/apache/maven/plugin/descriptor/PluginDescriptor.html).

Please note that the plugin classloader does neither contain the [dependencies](https://maven.apache.org/ref/current/maven-model/maven.html#class_dependency) of the current project nor its build output. Instead, plugins can query the project's compile, runtime and test class path from the [`MavenProject`](https://maven.apache.org/ref/current/apidocs/org/apache/maven/project/MavenProject.html) in combination with the mojo annotation `requiresDependencyResolution` from the [Mojo API Specification](https://maven.apache.org/developers/mojo-api-specification.html). For instance, flagging a mojo with `@requiresDependencyResolution runtime` enables it to query the runtime class path of the current project from which it could create further classloaders.

When a build plugin is executed, the thread's context classloader is set to the plugin classloader.

[](https://maven.apache.org/guides/mini/guide-maven-classloading.html)
Custom Classloaders[](https://maven.apache.org/guides/mini/guide-maven-classloading.html#custom-classloaders)
-------------------------------------------------------------------------------------------------------------

Plugins are free to create further classloaders. For example, a plugin might want to create a classloader that combines the plugin class path and the project class path.

It is important to understand that the plugin classloader cannot load classes from any of those custom classloaders. Some factory patterns require that. Here you must add the classes to the plugin classloader as shown before.
