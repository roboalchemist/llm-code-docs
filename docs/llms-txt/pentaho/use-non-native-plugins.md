# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/use-non-native-plugins.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/embed-pentaho-data-integration/use-non-native-plugins.md

# Use non-native plugins

To use non-native plugins with an embedded Pentaho Server, you must configure the server to find where the plugins reside. How you configure the server depends on whether your plugin is a directory with associated files or a single JAR file.

If your plugins are directories with associated files, register the directories by setting the **KETTLE\_PLUGIN\_BASE\_FOLDERS** system property just before the call to `KettleEnvironment.init()`, as shown in the following example for the “plugins” and “plugins2” plugins:

```
System.setProperty("KETTLE_PLUGIN_BASE_FOLDERS", "C:\\pentaho\\data-integration\\plugins,c:\\plugins2");
KettleEnvironment.init();
```

If your plugin is a single JAR file, annotate the classes for the plugin and include them in the class path, then set the**KETTLE\_PLUGIN\_CLASSES** system property to register the fully-qualified class names just before the call to `KettleEnvironment.init()`, as shown in the following example for a “jsonoutput” plugin:

```
System.setProperty("KETTLE_PLUGIN_CLASSES","org.pentaho.di.trans.steps.jsonoutput.JsonOutputMeta");
KettleEnvironment.init();
```

**Note:** Refer to the [Extend Pentaho Data Integration](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration) article for more information on creating plugins.

If you have custom transformation steps or job entries, you must use one of the above two methods to configure the locations where the embedded server will search for your custom transformation steps or custom job entries.
