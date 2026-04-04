# Source: https://docs.pentaho.com/install/9.3-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/manage-hadoop-configurations-through-pdi/include-or-exclude-classes-or-packages-for-a-hadoop-configuration.md

# Source: https://docs.pentaho.com/install/10.2-install/use-hadoop-with-pentaho/get-started-with-hadoop-and-pdi/before-you-begin-get-started-with-hadoop-and-pdi/manage-hadoop-configurations-through-pdi/include-or-exclude-classes-or-packages-for-a-hadoop-configuration.md

# Include or exclude classes or packages for a Hadoop configuration

You have the option to include or exclude classes or packages from loading with a Hadoop configuration.

Configure these options within the `plugin.properties` file located at `plugins/pentaho-big-data-plugin`. For additional information, see the comments within the `plugin.properties` file.

* **Include Additional Class Paths or Libraries**

  To include additional class paths, native libraries, or a user-friendly configuration name, include the directory within **classpath** property within the big data `plugin.properties` file.
* **Exclude Classes or Packages**

  To exclude classes or packages from duplicate loading by a Hadoop configuration class loader, include them in the **ignored.classes** property within the `plugin.properties` file. This is necessary when logging libraries expect a single class shared by all class loaders, as with Apache Commons Logging for example
