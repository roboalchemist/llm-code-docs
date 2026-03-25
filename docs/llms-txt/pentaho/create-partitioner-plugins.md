# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/create-different-types-of-plugins/create-partitioner-plugins.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/create-different-types-of-plugins/create-partitioner-plugins.md

# Create partitioner plugins

This section explains the architecture and programming concepts for creating your own partitioner plugins. PDI uses partitioner plugins for its partitioning feature. Each partitioner plugin implements a specific partitioning method.

![Partitioning method selection](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-5d2691547ac3f02f9e2bec93e2bf108c636448a3%2Fscreenshot_mod_partitioning.png?alt=media)

For most applications, the **Remainder of division** partitioner works well. On the rare occasion that an application would benefit from an additional partitioning method, this section explains how to implement them.

We recommended you open and refer to the [sample partitioner plugin sources](#sample-partitioner-plugin) while following these instructions.

A partitioner plugin integrates with PDI by implementing two distinct Java interfaces. Each interface represents a set of responsibilities performed by a PDI partitioner. Each of the interfaces has a base class that implements the bulk of the interface in order to simplify plugin development.

| Package                        | Interface           | Base Class      | Main Responsibilities                                                                                                                                                              |
| ------------------------------ | ------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `org.pentaho.di.trans`         | Partitioner         | BasePartitioner | <ul><li>Maintain partitioner settings</li><li>Serialize partitioner enumerations</li><li>Provide access to dialog class</li><li>Assign rows to partitions during runtime</li></ul> |
| `org.pentaho.di.ui.trans.step` | StepDialogInterface | BaseStepDialog  | <ul><li>Partitioner settings dialog</li></ul>                                                                                                                                      |

## Implementing the partitioner interface

`Partitioner` is the main Java interface that a plugin implements.

* **Java interface**

  [org.pentaho.di.trans.Partitioner](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/Partitioner.html)
* **Base class**

  [org.pentaho.di.trans.BasePartitioner](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/BasePartitioner.html)

### Keep track of partitioner settings

The implementing class keeps track of partitioner settings using private fields with corresponding `get` and `set` methods. The `dialog` class implementing `PartionerDialogInterface` is using these methods to copy the user supplied configuration in and out of the dialog.

* **`public Object clone()`**

  This method is called when a step containing partitioning configuration is duplicated in the PDI client (Spoon). It needs to return a deep copy of this partitioner object. It is essential that the implementing class creates proper deep copies if the configuration is stored in modifiable objects, such as lists or custom helper objects. The copy is created by calling `super.clone()` and deep copying any fields the partitioner may have declared.
* **`public Partitioner getInstance()`**

  This method is required to return a new instance of the partitioner class, with the plugin id and plugin description inherited from the instance upon which this method is called.

### Serialize partitioner settings

The plugin serializes its settings to both XML and a PDI repository.

* **`public String getXML()`**

  This method is called by PDI whenever the plugin needs to serialize its settings to XML. It is called when saving a transformation in the PDI client (Spoon). The method returns an XML string containing the serialized settings. The string contains a series of XML tags, one tag per setting. The helper class `org.pentaho.di.core.xml.XMLHandler` constructs the XML string.
* **`public void loadXML()`**

  This method is called by PDI whenever a plugin reads its settings from XML. The XML node containing the plugin settings is passed in as an argument. Again, the helper class `org.pentaho.di.core.xml.XMLHandler` is used to read the settings from the XML node.
* **`public void saveRep()`**

  This method is called by PDI whenever a plugin saves its settings to a PDI repository. The repository object passed in as the first argument provides a convenient set of methods for serializing settings. The transformation id and step id passed in are used as identifiers when calling the repository serialization methods.
* **`public void readRep()`**

  This method is called by PDI whenever a plugin needs to read its configuration from a PDI repository. The step id given in the arguments should be used as the identifier when using the repositories serialization methods.

When developing plugins, make sure the serialization code is in synch with the settings available from the partitioner plugin dialog. When testing a partitioned step in the PDI client, PDI internally saves and loads a copy of the transformation before it is executed.

### Provide the name of the dialog class

PDI needs to know which class will take care of the settings dialog for the plugin. The interface method `getDialogClassName()` must return the name of the class implementing the `StepDialogInterface` for the partitioner.

### Partition incoming rows during runtime

The class implementing `Partitioner` executes the actual logic that distributes the rows to available partitions.

* **`public int getPartition()`**

  This method is called with the row structure and the actual row as arguments. It returns the partition to which this row is sent. The total number of partitions is available in the inherited field `nrPartitions` and the return value is between zero (0, inclusive) and `nrPartitions` (exclusive).

### Interface with the PDI plugin system

In order for PDI to recognize the plugin, the class implementing the `Partitioner` interface must also be annotated with the Java annotation [org.pentaho.di.core.annotations.PartitionerPlugin](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/core/annotations/PartitionerPlugin.html).

Supply these annotation attributes:

| Attribute         | Description                                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`              | A globally unique ID for the plugin.                                                                                                                                                                                                                                                                                             |
| `name`            | A short label for the plugin.                                                                                                                                                                                                                                                                                                    |
| `description`     | A longer description for the plugin.                                                                                                                                                                                                                                                                                             |
| `i18nPackageName` | If the `i18nPackageName` attribute is supplied in the annotation attributes, the values of name and description are interpreted as `i18n` keys. The keys may be supplied in the extended form `i18n:<packagename>` key to specify a package that is different from the default package given in the `i18nPackageName` attribute. |

## Implementing the Partitioner Settings dialog box

`StepDialogInterface` is the Java interface that implements the settings dialog of a partitioner plugin.

* **Java interface**

  [org.pentaho.di.trans.step.StepDialogInterface](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/step/StepDialogInterface.html)
* **Base class**

  [org.pentaho.di.ui.trans.step.BaseStepDialog](http://javadoc.pentaho.com/kettle530/kettle-ui-swt-5.3.0.0-javadoc/org/pentaho/di/ui/trans/step/BaseStepDialog.html)

### Maintain the dialog for partitioner settings

The `dialog` class is responsible for constructing and opening the settings dialog for the partitioner. When you open the partitioning settings in the PDI client (Spoon), the system instantiates the `dialog` class passing in a `StepPartitioningMeta` object. Retrieve the `Partitioner` object by calling `getPartitioner()` and call the `open()` method on the dialog. [SWT](http://www.eclipse.org/swt/) is the native windowing environment of the PDI client and the framework used for implementing dialogs.

* **public String open()**

  This method returns only after the dialog has been confirmed or cancelled. The method must conform to these rules:

  * If the dialog is confirmed:
    * The `Partition` object must be updated to reflect the new settings.
    * If you changed any settings, the `StepPartitioningMeta` object Changed flag must be set to `true`.
    * `open()` returns the name of the step to which the partitioning is applied—use the **stepname** field inherited from `BaseStepDialog`.
  * If the dialog is cancelled:
    * The `Partition` object must not be changed.
    * The `StepPartitioningMeta` object Changed flag must be set to the value it had at the time the dialog opened.
    * **open()** must return `null`.

The `StepPartitioningMeta` object has an internal Changed flag that is accessible using `hasChanged()` and `setChanged()`. The PDI client decides whether the transformation has unsaved changes based on the Changed flag, so it is important for the dialog to set the flag appropriately.

The [sample Partitioner plugin project](#sample-partitioner-plugin) has an implementation of the dialog class that is consistent with the these rules and is a good basis for creating your own dialogs.

## Deploying partitioner plugins

To deploy your plugin, follow the following steps:

1. Create a jar file containing your plugin class(es).
2. Create a new folder with a meaningful name, and place your jar file inside the folder.
3. Place the plugin folder you just created in a specific location for PDI to find.

   Depending on how you use PDI, you need to copy the plugin folder to one or more locations as per the following list:

   * Deploying to the PDI client (Spoon) or Carte:
     1. Copy the plugin folder into this location: `design-tools/data-integration/plugins/steps`
     2. Restart the PDI client. After restarting the PDI client, the new database type is available from the PDI database dialog.
   * Deploying to Pentaho Server for Data Integration:
     1. Copy the plugin folder to this location: `server/pentaho-server/pentaho-solutions/system/kettle/plugins/steps`
     2. Restart the Pentaho Server. After restarting the Pentaho Server, the plugin is available to the server.
   * Deploying to Pentaho Server for Business Analytics:
     1. Copy the plugin folder to this location: `server/pentaho-server/pentaho-solutions/system/kettle/plugins/steps`
     2. Restart the Pentaho Server. After restarting the Pentaho Server, the plugin is available to the server.

## Sample partitioner plugin

The sample partitioner plugin project is designed to show a minimal functional implementation of a partitioner plugin that you can use as a basis to develop your own custom plugins.

The sample partitioner plugin distributes rows to partitions based on the value of a string field, or more precisely the string length. The sample shows a partitioner executing on five partitions, assigning longer strings to higher partition numbers.

Follow the steps below to build and deploy the sample plugin:

1. Obtain the sample plugin source.

   The plugin source is available in the [download package](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/get-started-with-the-sample-pdi-project#download-the-sample-project). Download the package and unzip it. The partitioner plugin resides in the `kettle-sdk-partitioner-plugin` folder.
2. Configure the build by opening `kettle-sdk-partitioner-plugin/build/build.properties` and setting the **kettle-dir** property to the base directory of your PDI installation.
3. Build and deploy.

   You may choose to build and deploy the plugin from the command line, or work with the Eclipse IDE instead. Both options are described below.

   * Build and deploy from the command line:

     The plugin is built using [Apache Ant](http://ant.apache.org/). Build and deploy the plugin from the command line by invoking the install target from the build directory.

     ```
     kettle-sdk-partitioner-plugin $ cd build
     build $ ant install
     ```

     The install target compiles the source, creates a jar file, creates a plugin folder, and copies the plugin folder into the `plugins/steps` directory of your PDI installation.
   * Build and deploy from Eclipse:
     * Import the plugin sources into Eclipse:
       1. From the menu, select **File** > **Import** > **Existing Projects Into Worksapace**.
       2. Browse to the `kettle-sdk-partitioner-plugin` folder and choose the project to be imported.
     * To build and install the plugin, follow these steps:
       1. Open the Ant view in Eclipse by selecting **Window** > **Show View** from the main menu and select **Ant**.

          You may have to select **Other** > **Ant** if you have not used the Ant view before.
       2. Drag the file `build/build.xml` from your project into the Ant view, and execute the install target by double-clicking it.
       3. After the plugin has been deployed, restart Spoon.
4. You can test the new plugin using the transformation from the `demo_transform` folder.

   ![Partitioning](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-ca2c062f2acb2363226c03b0311ffba2d7dfac56%2Fscreenshot_partitioning2.png?alt=media)

## Exploring existing partitioners

[PDI sources](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/get-started-with-the-sample-pdi-project#get-pdi-sources) are useful if you want to investigate the implementation of the standard modulo partitioner. The main class is available as [org.pentaho.di.trans.ModPartitioner](http://javadoc.pentaho.com/kettle530/kettle-engine-5.3.0.0-javadoc/org/pentaho/di/trans/ModPartitioner.html). The corresponding `dialog` class is located in [org.pentaho.di.ui.trans.dialog.ModPartitionerDialog](http://javadoc.pentaho.com/kettle530/kettle-ui-swt-5.3.0.0-javadoc/org/pentaho/di/ui/trans/dialog/ModPartitionerDialog.html).
