# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/manage-hadoop-configurations-through-pdi.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/manage-hadoop-configurations-through-pdi.md

# Configure PDI for Hadoop connections

Within PDI, a Hadoop configuration is the collection of Hadoop libraries required to communicate with a specific version of Hadoop and related tools, such as Hive, HBase, or Sqoop.

Hadoop configurations are defined in the `plugin.properties` file and are designed to be easily configured within PDI by changing the active `hadoop.configuration` property. The `plugin.properties` file resides in the `pentaho-big-data-plugin/` folder.

All Hadoop configurations share a basic structure. Elements of the structure are defined following the code sample:

```
configuration/
|-- lib/
|--  |-- pmr/
|--  '-- *.jar
|-- config.properties
|-- core-site.xml
`-- configuration-implementation.jar
```

| Configuration Element              | Definition                                                                                                                                                                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lib/`                             | Libraries specific to the version of Hadoop with which this configuration was created to communicate.                                                                                                                                                    |
| `pmr/`                             | Jar files that contain libraries required for parsing data in input/output formats or otherwise outside of any PDI-based execution.                                                                                                                      |
| `*.jar`                            | All other libraries required for Hadoop configuration that are not client-only or special PMR JAR files that need to be available to the entire JVM of Hadoop job tasks.                                                                                 |
| `config.properties`                | Contains metadata and configuration options for this Hadoop configuration. It provides a way to define a configuration name, additional classpath, and native libraries that the configuration requires. See the comments in this file for more details. |
| `core-site.xml`                    | Configuration file that can be replaced to set a site-specific configuration. For example, `hdfs-site.xml` would be used to configure HDFS.                                                                                                              |
| `configuration-implementation.jar` | File that must be replaced to communicate with this configuration.                                                                                                                                                                                       |
