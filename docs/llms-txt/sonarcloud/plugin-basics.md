# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/developing-a-plugin/plugin-basics.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/plugin-basics.md

# Plugin basics

### Building your plugin <a href="#building-your-plugin" id="building-your-plugin"></a>

#### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

To build a plugin, you need Java 8 and Maven 3.1 (or greater). Gradle can also be used thanks to the [gradle-sonar-packaging-plugin](https://github.com/iwarapter/gradle-sonar-packaging-plugin) (note that this plugin is not officially supported by Sonar).

#### Sonar Plugin API <a href="#sonar-plugin-api" id="sonar-plugin-api"></a>

The `sonar-plugin-api` is a Java API that is used to develop plugins.

{% hint style="warning" %}
The API used to be part of SonarQube Server and released with it, but it is a separate component since v9.5, with its own releases. You can find it here: [sonar-plugin-api](https://github.com/SonarSource/sonar-plugin-api).

The `groupId` was relocated from `org.sonarsource.sonarqube` to `org.sonarsource.api.plugin`.

The new coordinates of the dependency are

`org.sonarsource.api.plugin:sonar-plugin-api:<version>`
{% endhint %}

#### Create a Maven project <a href="#create-a-maven-project" id="create-a-maven-project"></a>

The recommended way to start is by duplicating the plugin example project: <https://github.com/SonarSource/sonar-custom-plugin-example>.

If you want to start the project from scratch, use the following Maven `pom.xml` template:

<details>

<summary>pom.xml</summary>

```css-79elbk
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>YOUR_GROUP_ID</groupId>
  <!-- it's recommended to follow the pattern "sonar-{key}-plugin", for example "sonar-myphp-plugin" -->
  <artifactId>YOUR_ARTIFACT_ID</artifactId>
  <version>YOUR_VERSION</version>
  
  <!-- this is important for sonar-packaging-maven-plugin -->
  <packaging>sonar-plugin</packaging>
 
  <dependencies>
    <dependency>
      <!-- groupId has changed to 'org.sonarsource.api.plugin' starting on version 9.5 -->
      <groupId>org.sonarsource.sonarqube</groupId>
      <artifactId>sonar-plugin-api</artifactId>
      <!-- minimal version of SonarQube to support. -->
      <version>8.9</version>
      <!-- mandatory scope -->
      <scope>provided</scope>
    </dependency>
  </dependencies>
 
  <build>
    <plugins>
      <plugin>
        <groupId>org.sonarsource.sonar-packaging-maven-plugin</groupId>
        <artifactId>sonar-packaging-maven-plugin</artifactId>
        <version>1.18.0.372</version>
        <extensions>true</extensions>
        <configuration>
          <!-- the entry-point class that extends org.sonar.api.SonarPlugin -->
          <pluginClass>com.mycompany.sonar.reference.ExamplePlugin</pluginClass>
           
          <!-- advanced properties can be set here. See paragraph "Advanced Build Properties". -->
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

</details>

#### Build <a href="#build" id="build"></a>

To build your plugin project, execute this command from the project root directory:

`mvn clean package`

The plugin jar file is generated in the project’s `target/` directory.

#### Deploy <a href="#deploy" id="deploy"></a>

**"Cold" Deploy**\
The standard way to install the plugin for regular users is to copy the jar artifact, from the `target/` directory to the `extensions/plugins/` directory of your SonarQube Server installation, then start the server. The file `logs/web.log` will then contain a log line similar to:\
`Deploy plugin Example Plugin / 0.1-SNAPSHOT`\
Scanner extensions such as sensors are immediately retrieved and loaded when scanning source code.

#### Debug <a href="#debug" id="debug"></a>

**Debugging web server extensions**

1. Edit conf/sonar.properties and set: `sonar.web.javaAdditionalOpts=-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8000`.
2. Install your plugin by copying its jar file to extensions/plugins.
3. Start the server. The line `Listening for transport dt_socket at address: 5005` is logged in `logs/sonar.log`.
4. Attach your IDE to the debug process (listening on port 8000 in the example).

**Debugging compute engine extensions**\
Same procedure as for web server extensions (see above), but with the following property:

```css-79elbk
sonar.ce.javaAdditionalOpts=-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8000
```

**Debugging scanner extensions**

```css-79elbk
$ export SONAR_SCANNER_OPTS="-agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=8000"
$ cd /path/to/project
$ sonar-scanner
```

When using the Scanner for Maven, then simply execute:

```css-79elbk
$ cd /path/to/project
$ mvnDebug org.sonarsource.scanner.maven:sonar-maven-plugin:sonar
```

#### Advanced build properties <a href="#advanced-build-properties" id="advanced-build-properties"></a>

Plugin properties are defined in the file `META-INF/MANIFEST.MF` of the plugin jar file.

Most of them are defined through the `<configuration>` section of the [sonar-packaging-maven-plugin](https://mvnrepository.com/artifact/org.sonarsource.sonar-packaging-maven-plugin/sonar-packaging-maven-plugin). Some are taken from standard pom nodes Effective values are listed at the end of the build log:

```css-79elbk
[INFO] --- sonar-packaging-maven-plugin:1.15:sonar-plugin (default-sonar-plugin) @ sonar-widget-lab-plugin ---
[INFO] -------------------------------------------------------
[INFO] Plugin definition in Marketplace
[INFO]     Key: widgetlab
[INFO]     Name: Widget Lab
[INFO]     Description: Additional widgets
[INFO]     Version: 1.9-SNAPSHOT
[INFO]     Entry-point Class: org.codehaus.sonar.plugins.widgetlab.WidgetLabPlugin
[INFO]     Required Plugins:
[INFO]     Use Child-first ClassLoader: false
[INFO]     Base Plugin:
[INFO]     Homepage URL: https://redirect.sonarsource.com/plugins/widgetlab.html
[INFO]     Minimal SonarQube Version: 4.5.1
[INFO]     Licensing: GNU LGPL 3
[INFO]     Organization: Shaw Industries
[INFO]     Organization URL: http://shawfloors.com
[INFO]     Terms and Conditions:
[INFO]     Issue Tracker URL: http://jira.codehaus.org/browse/SONARWIDLB
[INFO]     Build date: 2015-12-15T18:28:54+0100
[INFO]     Sources URL: https://github.com/SonarCommunity/sonar-widget-lab
[INFO]     Developers: G. Ann Campbell,Patroklos Papapetrou
[INFO] -------------------------------------------------------
[INFO] Building jar: /dev/sonar-widget-lab/target/sonar-widget-lab-plugin-1.9-SNAPSHOT.jar
```

Supported standard pom node properties:

|                       |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Maven property**    | **Manifest key**  | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `version`             | Plugin-Version    | (required) Plugin version as displayed in page "Marketplace". Default: `${project.version}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `pluginApiMinVersion` | Sonar-Version     | Minimal version of supported Sonar Plugin API at runtime. For example, if the value is 9.8.0.203, then deploying the plugin on SonarQube Server versions with `sonar-plugin-api` 9.6.1.114 (ie. SonarQube 9.5) and lower will fail. The default value is given by the version of `sonar-plugin-api` dependency. It can be overridden with the Maven property `pluginApiMinVersion` (since `sonar-packaging-maven-plugin` 1.22). That allows in some cases to use new features of recent API and to still be compatible at runtime with older versions of SonarQube Server. Default: version of dependency `sonar-plugin-api` |
| `license`             | Plugin-License    | Plugin license as displayed on page "Marketplace". Default `${project.licenses}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `developers`          | Plugin-Developers | A list of developers is displayed on the page "Marketplace". Default: `${project.developers}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Supported `<configuration>` properties:

|                            |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Maven property**         | **Manifest key**             | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `pluginKey`                | Plugin-Key                   | (required) Contains only letters/digits and is unique among all plugins. Examples: groovy, widgetlab. Constructed from `${project.artifactId}.` Given an artifactId of: `sonar-widget-lab-plugin`, your pluginKey will be: `widgetlab`                                                                                                                                                                                                                                                                                   |
| `pluginClass`              | Plugin-Class                 | (required) Name of the entry-point class that extends `org.sonar.api.SonarPlugin`. Example: `org.codehaus.sonar.plugins.widgetlab.WidgetLabPlugin`                                                                                                                                                                                                                                                                                                                                                                       |
| `pluginName`               | Plugin-Name                  | (required) Displayed in the page "Marketplace". Default: `${project.name}`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `pluginDescription`        | Plugin-Description           | Displayed in the page "Marketplace". Default: `${project.description}`                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `pluginUrl`                | Plugin-Homepage              | Homepage of website, for example <https://github.com/SonarQubeCommunity/sonar-widget-lab>`${project.url}`                                                                                                                                                                                                                                                                                                                                                                                                                |
| `pluginIssueTrackerUrl`    | Plugin-IssueTrackerUrl       | Example: <https://github.com/SonarQubeCommunity/sonar-widget-lab/issues>. Default: `${project.issueManagement.url}`                                                                                                                                                                                                                                                                                                                                                                                                      |
| `pluginTermsConditionsUrl` | Plugin-TermsConditionsUrl    | Users must read this document when installing the plugin from Marketplace. Default: `${sonar.pluginTermsConditionsUrl}`                                                                                                                                                                                                                                                                                                                                                                                                  |
| `useChildFirstClassLoader` | Plugin-ChildFirstClassLoader | Each plugin is executed in an isolated classloader, which inherits a shared classloader that contains API and some other classes. By default the loading strategy of classes is parent-first (look up in shared classloader then in plugin classloader). If the property is true, then the strategy is child-first. This property is mainly used when building plugin against API < 5.2, as the shared classloader contained many 3rd party libraries (guava 10, commons-lang, …) false.                                 |
| `basePlugin`               | Plugin-Base                  | If specified, then the plugin is executed in the same classloader as `basePlugin`.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `pluginSourcesUrl`         | Plugin-SourcesUrl            | URL of SCM repository for open-source plugins. Displayed on page "Marketplace". Default: `${project.scm.url}`                                                                                                                                                                                                                                                                                                                                                                                                            |
| `pluginOrganizationName`   | Plugin-Organization          | The organization which develops the plugin is displayed on the page "Marketplace". Default: `${project.organization.name}`                                                                                                                                                                                                                                                                                                                                                                                               |
| `pluginOrganizationUrl`    | Plugin-OrganizationUrl       | URL of the organization, displayed on the page "Marketplace". Default: `${project.organization.url}`                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sonarLintSupported`       | SonarQube for IDE-Supported  | Whether the language plugin supports SonarQube for IDE or not. Only SonarSource analyzers and custom rules plugins for SonarSource analyzers should set this to true.                                                                                                                                                                                                                                                                                                                                                    |
| `pluginDisplayVersion`     | Plugin-Display-Version       | The version is displayed in SonarQube Server administration console. By default it’s the raw version, for example, "1.2", but can be overridden to "1.2 (build 12345)" for instance. Supported in sonar-packaging-maven-plugin 1.18.0.372. Default: `${project.version}`                                                                                                                                                                                                                                                 |
| `requiredForLanguages`     | Plugin-RequiredForLanguages  | <p>Languages for which this plugin should be downloaded. Use to make sure dependency errors are avoided when <a data-mention href="../../server-update-and-maintenance/maintenance/improving-performance">improving-performance</a>. This property must be added to the <code>\<configuration></code> section of the plugin’s <code>pom.xml</code> file.</p><p>For an example, see the <strong>Custom Rules</strong> section of the <a data-mention href="../../analyzing-source-code/languages/java">java</a> page.</p> |

The Maven `sonar-packaging-maven-plugin` supports also these properties:

|                             |                                                                    |                                                           |
| --------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------- |
| **Maven property**          | **Manifest key**                                                   | **Notes**                                                 |
| `addMavenDescriptor`        | Copy pom file inside the directory META-INF of generated jar file? | Boolean. Default: `${sonar.addMavenDescriptor}` / `true`. |
| `skipDependenciesPackaging` | Do not copy Maven dependencies into jar file.                      | Default: `${sonar.skipDependenciesPackaging} /`false\`.   |

Other Manifest fields:

* `Implementation-Build`: Identifier of build or commit, for example, the Git SHA1. `94638028f0099de59f769cdca776e506684235d6`. It is displayed for debugging purposes in logs when SonarQube Server starts.

### API basics <a href="#api-basics" id="api-basics"></a>

#### Extension points <a href="#extension-points" id="extension-points"></a>

SonarQube Server provides extension points for its three technical stacks:

* Scanner, which runs the source code analysis.
* Compute Engine, which consolidates the output of scanners, for example by:
  * computing 2nd-level measures such as ratings.
  * aggregating measures (for example number of lines of code of project = sum of lines of code of all files).
  * assigning new issues to developers.
  * persisting everything in data stores.
* Web application.

Extension points are not designed to add new features but to complete existing features. Technically they are contracts defined by a Java interface or an abstract class annotated with `@ExtensionPoint`. The exhaustive list of extension points is available in the Javadoc.

The implementations of extension points (named *extensions*) provided by a plugin must be declared in its entry point class, which implements `org.sonar.api.Plugin`and which is referenced in the `pom.xml`:

**ExamplePlugin.java**

```css-79elbk
package org.sonarqube.plugins.example;
import org.sonar.api.Plugin;
 
public class ExamplePlugin implements Plugin {
  @Override
  public void define(Context context) {
    // implementations of extension points
    context.addExtensions(FooLanguage.class, ExampleProperties.class);
  }
}
```

**pom.xml**

```css-79elbk
<?xml version="1.0" encoding="UTF-8"?>
<project>
  ...
  <build>
    <plugins>
      <plugin>
        <groupId>org.sonarsource.sonar-packaging-maven-plugin</groupId>
        <artifactId>sonar-packaging-maven-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <pluginClass>org.sonarqube.plugins.example.ExamplePlugin</pluginClass>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

#### Lifecycle <a href="#lifecycle" id="lifecycle"></a>

A plugin extension exists only in its associated technical stacks. A scanner sensor is for example instantiated and executed only in a scanner runtime, but not in the web server nor in Compute Engine. The stack is defined by the annotations [@ScannerSide](https://javadocs.sonarsource.org/latest/org/sonar/api/batch/ScannerSide.html), [@ServerSide](https://javadocs.sonarsource.org/latest/org/sonar/api/server/ServerSide.html) (for a web server), and [@ComputeEngineSide](https://javadocs.sonarsource.org/latest/org/sonar/api/ce/ComputeEngineSide.html).

An extension can call core components or another extension of the same stack. These dependencies are defined by constructor injection:

```css-79elbk
@ScannerSide
public class Foo {
  public void call() {}
}
 
// Sensor is a scanner extension point 
public class MySensor implements Sensor {
  private final Foo foo;
  private final Languages languages;
  
  // Languages is core component which lists all the supported programming languages.
  public MySensor(Foo foo, Languages languages) {   
    this.foo = foo;
    this.languages = languages;
  }
  
  @Override
  public void execute(SensorContext context) {
    System.out.println(this.languages.all());
    foo.call();
  }
}
 
  
public class ExamplePlugin implements Plugin {
  @Override
  public void define(Context context) {
    // Languages is a core component. It must not be declared by plugins.
    context.addExtensions(Foo.class, MySensor.class);
  }
}
```

It is recommended not to call other components in constructors. Indeed, they may not be initialized at that time. Constructors should only be used for dependency injection.

A compilation will not fail if incorrect dependencies are defined, such as a scanner extension trying to call a web server extension. Still, it will fail at runtime when a plugin is loaded.

#### Third-party libraries <a href="#thirdparty-libraries" id="thirdparty-libraries"></a>

Plugins are executed in their own isolated classloaders. That allows the packaging and use of 3rd-party libraries without runtime conflicts with core internal libraries or other plugins. Note that since version 5.2, SonarQube Server API does not bring transitive dependencies, except SLF4J. The libraries just have to be declared in the `pom.xml` with the default scope "compile":

**pom.xml**

```css-79elbk
<?xml version="1.0" encoding="UTF-8"?>
<project>
  ...
  <dependencies>
    ...
    <dependency>
      <groupId>commons-codec</groupId>
      <artifactId>commons-codec</artifactId>
      <version>1.10</version>
    </dependency>
 </dependencies>
</project>
```

Technically, the libraries are packaged in the directory META-INF/lib of the generated jar file. An alternative is to shade libraries, for example with `maven-shade-plugin`. That minimizes the size of the plugin jar file by copying only the effective used classes.

The command `mvn dependency:tree` gives the list of all dependencies, including transitive ones.

#### Configuration <a href="#configuration" id="configuration"></a>

The core component [`org.sonar.api.config.Configuration`](http://javadocs.sonarsource.org/latest/org/sonar/api/config/Configuration.html) provides access to configuration. It deals with default values and the decryption of values. It is available in all stacks (scanner, web server, Compute Engine). As recommended earlier, it must not be called from constructors.

**MyExtension.java**

```css-79elbk
public class MyRules implements RulesDefinition {
  private final Configuration config;
  
  public MyRules(Configuration config) {   
    this.config = config; 
  }
  
  @Override
  public void define(Context context) {
    int value = config.getInt("sonar.property").orElse(0);
  }
}
```

Scanner sensors can get config directly from SensorContext, without using constructor injection:

**MySensor.java**

```css-79elbk
public class MySensor extends Sensor {
  @Override
  public void execute(SensorContext context) {
    int value = context.config().getInt("sonar.property").orElse(0);
  }
}
```

In the scanner stack, properties are checked in the following order, and the first non-blank value is the one that is used:

1. System property.
2. Scanner command-line (-Dsonar.property=foo for instance).
3. Scanner tool ( of scanner for Maven for instance).
4. Project configuration defined in the web UI.
5. Global configuration defined in the web UI.
6. Default value.

Plugins can define their own properties so that they can be configured from the web administration console. The extension point `org.sonar.api.config.PropertyDefinition` must be used:

```css-79elbk
public class ExamplePlugin implements Plugin {
  @Override
  public void define(Context context) {
    context.addExtension(
      PropertyDefinition.builder("sonar.my.property")
       .name("My Property")
       .description("This is the description displayed in web admin console")
       .defaultValue("42")
       .build()
    );
  }
}
```

{% hint style="info" %}
Values of the properties suffixed with `.secured` are not available to be read by any users. The `.secured` suffix is needed for passwords, for instance.
{% endhint %}

The annotation `org.sonar.api.config.PropertyDefinition` can be used on an extension to declare a property.

```css-79elbk
@Properties(
    @Property(key="sonar.my.property", name="My Property", defaultValue="42")
)
public class MySensor implements Sensor {
  // ...
}
  
public class ExamplePlugin implements Plugin {
  @Override
  public void define(Context context) {
    context.addExtension(MySensor.class);
  }
}
```

#### Logging <a href="#logging" id="logging"></a>

The class [`org.sonar.api.utils.log.Logger`](https://javadocs.sonarsource.org/latest/org/sonar/api/utils/log/Logger.html) is used to log messages to scanner output, web server logs/sonar.log, or Compute Engine logs (available from the administration web console). It’s convenient for unit testing (see class [`LogTester`](https://javadocs.sonarsource.org/latest/org/sonar/api/utils/log/LogTester.html)).

```css-79elbk
import org.sonar.api.utils.log.*;
public class MyClass {
  private static final Logger LOGGER = Loggers.get(MyClass.class);
 
  public void doSomething() {
    LOGGER.info("foo");
  }
}
```

Internally, [SLF4J](https://www.slf4j.org/) is used as a facade of various logging frameworks (`log4j`, `commons-log`, `logback`, `java.util.logging`). That allows all these frameworks to work at runtime, such as when they are required for a 3rd party library. SLF4J loggers can also be used instead of `org.sonar.api.utils.log.Logger`. Read the [SLF4J manual](https://www.slf4j.org/manual.html) for more details.

As an exception, plugins must not package logging libraries. Dependencies like SLF4J or `log4j` must be declared with the scope "provided".

#### Exposing APIs to other plugins <a href="#exposing-apis-to-other-plugins" id="exposing-apis-to-other-plugins"></a>

The common use case is to write a language plugin that will allow some other plugins to contribute additional rules (see for example how it is done for [Java](https://github.com/SonarSource/sonar-java) analysis). The main plugin will expose some APIs that will be implemented/used by the "rule" plugins.

Plugins are loaded in isolated classloaders. It means a plugin can’t access another plugin’s classes. There is an exception for package names following pattern `org.sonar.plugins.<pluginKey>.api`. For example, all classes in a plugin with the key `myplugin` that are located in `org.sonar.plugins.myplugin.api` are visible to other plugins.

#### Serving static resources <a href="#serving-static-resources" id="serving-static-resources"></a>

If you need to serve static resources from your plugin such as images or JavaScript files, place them in a directory under `resources` named `static` (`myplugin/src/main/resources/static`). At runtime, they’ll be available from `https://{server}/static/{pluginKey}/{file}`.

### Configuring plugins for analyzer loading optimization <a href="#configuring-plugins-for-analyzer-loading-optimization" id="configuring-plugins-for-analyzer-loading-optimization"></a>

By default, SonarQube Server downloads Sonar analyzers and third-party plugins only when they are really required by the scanner (see [improving-performance](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/improving-performance "mention")). To make this feature work, each analyzer or third-party plugin should declare the list of languages on which they expect to raise issues through a MANIFEST property called `Plugin-RequiredForLanguages`.

#### Optimization behavior <a href="#optimization-behavior" id="optimization-behavior"></a>

At the Scanner level, the behavior is as follows:

* **Case 1**: When the property is not set by the plugin, the plugin is downloaded whatever the contents of the project.
* **Case 2**: When the property is defined and there are files corresponding to the language declared by the plugin, the plugin is downloaded.
* **Case 3**: When the property is defined and there are no files corresponding to the language declared by the plugin, the plugin is not downloaded.

This helps save network bandwidth and speed up the bootstrap of the scans. As a side effect, the logs are also cleaner, with fewer "nothing to do" logs for plugins that really have nothing to perform on the repository content.

#### Avoiding dependency errors <a href="#avoiding-dependency-errors" id="avoiding-dependency-errors"></a>

For plugins that have a dependency on a base analyzer provided by default with SonarQube Server (for example, a plugin to add rules or reports to an existing language), it is mandatory to add to the MANIFEST the property `Plugin-RequiredForLanguages` to avoid a hard failure.

Take, for example, plugin sonar-xyz which provides additional rules for Java:

1. A user scans a repository that only contains Python code.
2. sonar-xyz is downloaded because it doesn’t declare the property. So it is downloaded from the server at each scan (case 1 above).
3. sonar-java is not downloaded because there are no .java files in the repository to scan (case 3 above).
4. Analysis errors-out because a `NoClassDefFoundError` is thrown since sonar-xyz has an unsatisfied dependency on sonar-java, which wasn’t downloaded.

#### Configuration steps <a href="#configuration-steps" id="configuration-steps"></a>

To avoid dependency errors, you’ll need to:

1. Upgrade sonar-packaging-maven-plugin to version [1.22.0.705 1](https://github.com/SonarSource/sonar-packaging-maven-plugin/releases/tag/1.22.0.705).
2. Add java to the configuration of sonar-packaging-maven-plugin where "java" is replaced by the language your plugin is dealing with.
3. Add the property `<requiredForLanguages>` to the configuration of sonar-packaging-maven-plugin, so that `Plugin-RequiredForLanguages` is added to the MANIFEST. The property accepts several values such as `js`,`ts`,`css`,`web`, `yaml`, etc.

Example configurations are available on the language pages (see the **Custom rules** section of the [java](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/java "mention") page for example).

### API deprecation <a href="#api-deprecation" id="api-deprecation"></a>

See [deprecation-policy](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/deprecation-policy "mention").

### API Changes <a href="#api-changes" id="api-changes"></a>

{% hint style="info" %}
Starting with v9.5, the API is released independently of SonarQube Server. You can find the changes for newer releases in its [code repository](https://github.com/SonarSource/sonar-plugin-api/releases).
{% endhint %}

#### Release 2025.3 <a href="#release-20253" id="release-20253"></a>

The following deprecated classes have been removed: `MutableModuleSettings` and `MutableProjectSettings`.

#### Release 9.3 <a href="#release-93" id="release-93"></a>

Added

* `sonar-plugin-api.src.main.java.org.sonar.api.resources.Language#publishAllFiles` to define whether the files identified with the language should be automatically published to SonarQube Server.
* `org.sonar.api.batch.sensor.SensorDescriptor#processesFilesIndependently`

#### Release 9.0 <a href="#release-90" id="release-90"></a>

Deprecated:

* `org.sonar.api.server.rule.RulesDefinitionXmlLoader` is deprecated. Use the `sonar-check-api` to annotate rule classes instead of loading the metadata from XML files.

Removed:

* `org.sonar.api.ExtensionProvider` Use `org.sonar.api.Plugin.Context#addExtensions()` to add objects to the container.
* `org.sonar.api.batch.sensor.SensorDescriptor#requireProperty()`. Use `#onlyWhenConfiguration()` instead.
* All API related to preview/issues analysis mode.
* Coverage types (unit, IT, overall) was removed.
* Resource perspectives. Use methods in `SensorContext`.
* `org.sonar.api.platform.Server#getRootDir()`. Use `ServerFileSystem#getHomeDir()`.
* `org.sonar.api.profiles.ProfileDefinition.java`. Define quality profiles with `BuiltInQualityProfilesDefinition`.
* `org.sonar.api.rules.XMLRuleParser`. Use the `sonar-check-api` to annotate rule classes.

#### Release 8.4 <a href="#release-84" id="release-84"></a>

Added:

* `org.sonar.api.batch.scm.ScmProvider#forkDate`

Deprecated:

* `org.sonar.api.rules.Rule#getId()` is deprecated and will always throw UnsupportedOperationException.

#### Release 8.3 <a href="#release-83" id="release-83"></a>

Deprecated:

* `org.sonar.api.utils.text.JsonWriter`

#### Release 7.8 <a href="#release-78" id="release-78"></a>

Added:

* `org.sonar.api.web.WebAnalytics`

Deprecated:

* `org.sonar.api.i18n.I18`
* `org.sonar.api.SonarQubeVersion` use `org.sonar.api.SonarRuntime` instead.
* `org.sonar.api.profiles.XMLProfileParser`
* `org.sonar.api.notifications.NotificationChannel`

Removed:

* Pico components relying on reflection to have their `start` or `stop` method called. Make your component implements `org.sonar.api.Startable` instead.

#### Release 7.7 <a href="#release-77" id="release-77"></a>

Added:

* `org.sonar.api.batch.scm.ScmProvider#ignoreCommand`

Deprecated:

* `org.sonar.api.batch.fs.InputFile::status`
* `org.sonar.api.resources.Qualifiers#BRC`

Removed:

* The preview/issues mode of the scanner has been removed.

#### Release 7.6 <a href="#release-76" id="release-76"></a>

Changed:

* `PostJob` moved to project level IoC container.
* `InputFileFilter` moved to project level IoC container.

Added:

* New annotation `org.sonar.api.scanner.ScannerSide` to mark (project level) scanner components.
* `org.sonar.api.batch.fs.InputProject` to create issues on projects.
* `org.sonar.api.scanner.ProjectSensor` to declare Sensors that only run at the project level.

Deprecated:

* `org.sonar.scanner.issue.IssueFilter` is deprecated.
* `org.sonar.api.batch.InstantiationStrategy` is deprecated.
* `org.sonar.api.batch.ScannerSide` is deprecated.
* `org.sonar.api.batch.fs.InputModule` is deprecated.
* The concept of global Sensor is deprecated (use `ProjectSensor` instead).

Removed:

* Support of scanner tasks was removed.
* `RulesProfile` is no longer available for scanner side components (use `ActiveRules` instead).

#### Release 7.4 <a href="#release-74" id="release-74"></a>

Changed:

* Allow identity provider to not provide login.

Added:

* Allow sensors to report adhoc rules metadata.

Removed:

* `org.sonar.api.rules.RuleFinder` removed from scanner side.
* `sonar-channel` removed from plugin classloader.
* stop support of plugins compiled with API < 5.2.

#### Release 7.3 <a href="#release-73" id="release-73"></a>

Added:

* `RulesDefinitions` supports HotSpots and security standards.

Deprecated:

* `org.sonar.api.batch.AnalysisMode` and `org.sonar.api.issue.ProjectIssues` since preview mode is already deprecated for a while.

#### Release 7.2 <a href="#release-72" id="release-72"></a>

Added:

* `org.sonar.api.batch.sensor.SensorContext#newExternalIssue` to report external issues.
* `org.sonar.api.batch.sensor.SensorContext#newSignificantCode` to report part of the source file that should be used for issue tracking.
* `org.sonar.api.scan.issue.filter.FilterableIssue#textRange`

Deprecated:

* `org.sonar.api.scan.issue.filter.FilterableIssue#line`

#### Release 7.1 <a href="#release-71" id="release-71"></a>

Added:

* `org.sonar.api.Plugin.Context#getBootConfiguration`
* `org.sonar.api.server.rule.RulesDefinition.NewRule#addDeprecatedRuleKey` to support deprecated rule keys.

#### Release 7.0 <a href="#release-70" id="release-70"></a>

Added:

* `org.sonar.api.batch.scm.ScmProvider#relativePathFromScmRoot`, `org.sonar.api.batch.scm.ScmProvider#branchChangedFiles` and `org.sonar.api.batch.scm.ScmProvider#revisionId` to improve branch and PR support.
