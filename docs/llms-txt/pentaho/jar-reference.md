# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/advanced-topics/jar-reference.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-reporting-functionality/advanced-topics/jar-reference.md

# JAR reference

The JAR reference includes these categories of available JARs:

* Pentaho-authored JARs
* Included third-party JARs
* JARs exclusive to the embedding samples

## Pentaho-authored JARs

The Pentaho Reporting SDK consists of the following Pentaho-authored JARs:

| JAR File Name                           | Purpose                                                                                                                                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `libbase`                               | The root project for all reporting projects. Provides base services like controlled boot-up, modularization, configuration. Also contains some commonly used helper classes.                                                |
| `libdocbundle`                          | Support for ODF-document-bundle handling. Provides the engine with the report-bundle capabilities and manages the bundle-metadata, parsing and writing.                                                                     |
| `libfonts`                              | Font-handling library. Performs the mapping between physical font files and logical font names. Also provides performance optimized font-metadata and font-metrics.                                                         |
| `libformat`                             | A performance optimized replacement for JDK TextFormat classes. Accepts the same patterns as the JDK classes, but skips the parsing. Therefore they are less expensive to use in terms of CPU and memory.                   |
| `libformula`                            | Our OpenFormula implementation. Provides a implementation of the OpenFormula specification. Basically a way to have Excel-style formulas without the nonsense Excel does.                                                   |
| `libloader`                             | Resourceloading and caching framework. Used heavily in the engine to load reports and other resources in the most efficient way.                                                                                            |
| `libpixie`                              | Support for rendering WMF (windows-meta-files).                                                                                                                                                                             |
| `librepository`                         | Abstraction-layer for content-repositories. Heavily used by `LibDocbundle` and our HTML export.                                                                                                                             |
| `libserializer`                         | Helper classes for serialization of Java-objects. A factory based approach to locate serializers based on the class of the object we want to serialize. needed as major parts of the JDK are not serializable on their own. |
| `libxml`                                | Advanced SAX-parsing framework and namespace aware XML writing framework used in the engine and `libdocbundle`.                                                                                                             |
| `pentaho-reporting-engine-classic-core` | The Pentaho Reporting engine core, which itself consists of modular sub-projects.                                                                                                                                           |

## Included third-party JARs

| JAR File Name                                                                                                                                                                      | Purpose                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `activation`                                                                                                                                                                       | The JavaBeans Activation Framework, which determines the type of the given data, encapsulates it, discovers the operations available on it, and to instantiates the appropriate bean to execute those operations. |
| `batik-awt-util`, `batik-bridge`, `batik-css`, `batik-dom`, `batik-ext`, `batik-gui-util`, `batik-gvt`, `batik-parser`, `batik-script`, `batik-svg-dom`, `batik-util`, `batik-xml` | The core Batik SVG toolkit, which adds scalable vector graphics support to a Java application.                                                                                                                    |
| `bsf`                                                                                                                                                                              | The Apache Jakarta Bean Scripting Framework, which provides scripting language support within Java applications, and access to Java objects and methods from scripting languages.                                 |
| `bsh`                                                                                                                                                                              | The Bean Shell, which dynamically executes standard Java syntax and extends it with common scripting conveniences such as loose types, commands, and method closures like those in Perl and JavaScript.           |
| `commons-logging-api`                                                                                                                                                              | The Apache Commons Logging library, which allows writing to a variety of different logging services in a common format.                                                                                           |
| `itext`                                                                                                                                                                            | Enables dynamic PDF generation.                                                                                                                                                                                   |
| `jsr107cache`                                                                                                                                                                      | A Java cache API specification.                                                                                                                                                                                   |
| `ehcache`                                                                                                                                                                          | A distributed cache library that uses the `jsr107cache` API.                                                                                                                                                      |
| `mail`                                                                                                                                                                             | The Java Mail API, which allows you to send email from a Java application without requiring a separate mail server.                                                                                               |
| `poi`                                                                                                                                                                              | A Java API that allows you to read from and write to Microsoft file formats.                                                                                                                                      |

## JARs exclusive to the embedding samples

The created samples use the 2.3.2 Engine for HSQLDB.

| JAR File Name                              | Purpose                                          |
| ------------------------------------------ | ------------------------------------------------ |
| `hsqldb`                                   | HSQLDB database engine and JDBC driver.          |
| `pentaho-reporting-engine-classic-samples` | The sample applications explained in this guide. |
