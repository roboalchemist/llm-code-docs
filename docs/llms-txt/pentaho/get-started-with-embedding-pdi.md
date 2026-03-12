# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/get-started-with-embedding-pdi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/get-started-with-embedding-pdi.md

# Get started with embedding PDI

Consider the following dependencies while embedding PDI:

* Complete set of dependent PDI files
* OSGi features for PDI
* Kettle (non-OSGi) plugins
* Pentaho license file

## Complete set of dependent PDI files

The following PDI directories contain a complete set of all JAR files needed:

* `pentaho/design-tools/data-integration/lib`
* `pentaho/design-tools/data-integration/libswt/<os>`
* `pentaho/design-tools/data-integration/classes`

These dependencies must be included in your class path. You can copy the directories into your project’s directory structure or specify the path directly to your PDI installation, as shown in the following example code:

```java
java -classpath "lib/*;libswt/linux/*;classes/*" MyApp.java
java -classpath "$PDI_DI_DIR/lib/*;$PDI_DI_DIR/libswt/linux/*; $PDI_DI_DIR/classes/*" MyApp.java
```

## OSGi features for PDI

To use the OSGi features of PDI, make the `pentaho/design-tools/data-integration/system` directory available to your application. This directory is required for proper Karaf initialization. You can use either of following methods to specify this directory:

* Copy the `pentaho/design-tools/data-integration/system` directory into the `*&lt;working directory&gt;*/systems` directory of your application.
* Set the **pentaho.user.dir** system property to point to the PDI `pentaho/design-tools/data-integration` directory, either through the following command line option (`-Dpentaho.user.dir=<pdi install>/data-integration`) or directly in your code (`System.setProperty( "pentaho.user.dir", new File("<pdi install>/data-integration")`); for example).

## Kettle (non-OSGi) plugins

Make the kettle plugins (non-OSGi) available to your application. With a standard install, the kettle engine looks for plugins in either `*&lt;working directory&gt;*plugins` or `*&lt;user.home&gt;*/.kettle/plugins`. You can use either of following methods to make the default kettle plugins available:

* Copy the `pentaho/design-tools/data-integration/plugins` directory into the `<working directory>/plugins` directory of your application.
* Set the **KETTLE\_PLUGIN\_BASE\_FOLDERS** system property to point to the PDI `pentaho/design-tools/data-integration` directory, either through the following command line option (`-DKETTLE_PLUGIN_BASE_FOLDERS=<pdi install>/data-integration`) or directly in your code (`System.setProperty( "KETTLE_PLUGIN_BASE_FOLDERS", new File("<pdi install>/data-integration"`) ); for example).

Once the plugin location(s) are properly configured, you can add custom plugins to your specific locations. You can also add custom plugins in other locations as long as they are registered with the appropriate implementation of `PluginTypeInterface` prior to initializing the kettle environment, as shown in the following code example:

```
StepPluginType.getInstance().getPluginFolders().add( new PluginFolder( "<path to the plugin folder>" , false, true ) );
```

## Pentaho license file

Before initializing the Kettle environment, you must install the PDI Enterprise Edition license file for each user account. Then, to ensure that the Pentaho Server uses the same location to store and retrieve your Pentaho license, you must also create a **PENTAHO\_INSTALLED\_LICENSE\_PATH** system environment variable for each account. The location of your license path must be available to the user accounts that run the Pentaho Server. For information about installing the license and setting the variable path, see **Manage licenses using the command line interface** in the **Install Pentaho Data Integration and Analytics** guide.
