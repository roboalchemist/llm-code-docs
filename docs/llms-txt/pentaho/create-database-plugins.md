# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/create-different-types-of-plugins/create-database-plugins.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/embed-and-extend-pdi-functionality/extend-pentaho-data-integration/create-different-types-of-plugins/create-database-plugins.md

# Create database plugins

PDI uses database plugins to support specific database systems beyond generic JDBC functionality.

A database plugin helps in the following areas:

* Constructing connection strings
* Passing connection settings to JDBC
* Dialect-aware SQL generation
* Detecting special abilities and limitations of JDBC drivers

## Understanding database plugins

A database plugin introduces a new entry in the PDI database dialog box.

![Database Connection dialog box](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-efde69f36f66dfef84d25da9cf9e672714d10b3e%2FssPDIExtendPDI_DatabasePlugins.png?alt=media)

This section explains the architecture and programming concepts for creating your own database plugin. We recommend that you open and refer to the [sample database plugin sources](#sample-database-plugin) while following these instructions.

* **Java Interface**

  [org.pentaho.di.core.database.DatabaseInterface](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/DatabaseInterface.html)
* **Base class**

  [org.pentaho.di.core.database.BaseDatabaseMeta](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/BaseDatabaseMeta.html)

PDI database plugins consist of a single Java class that implements the interface [org.pentaho.di.core.database.DatabaseInterface](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/DatabaseInterface.html).

In order for PDI to recognize the database plugin, the class implementing `DatabaseInterface` must also be annotated with the Java annotation [org.pentaho.di.core.plugins.DatabaseMetaPlugin](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/plugins/DatabaseMetaPlugin.html).

Supply these annotation attributes.

* **type**

  A globally unique ID for database plugin
* **typeDescription**

  The label to use in the database dialog box

It is recommended to extend [org.pentaho.di.core.database.BaseDatabaseMeta](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/BaseDatabaseMeta.html), which provides default implementations for most of the methods in `DatabaseInterface`. Existing PDI database interfaces are a great source of information when developing a new database plugin.

The following section classifies some of the most commonly overridden methods. They can be roughly classified into three subject areas: information about connections, SQL dialect, and general capability flags.

#### Connection Details

These methods are called when PDI establishes a connection to the database, or the database dialog is populated with database-specific defaults.

* `public String getDriverClass()`
* `public int getDefaultDatabasePort()`
* `public int[] getAccessTypeList()`
* `public boolean supportsOptionsInURL()`
* `public String getURL()`

#### SQL Generation

These methods are called when PDI constructs SQL.

* `public String getFieldDefinition()`
* `public String getAddColumnStatement()`
* `public String getSQLColumnExists()`
* `public String getSQLQueryFields()`

#### Capability Flags

These methods are called when PDI determines the run-time characteristics of the database system. For instance, the database systems may support different notions of metadata retrieval.

* `public boolean supportsTransactions()`
* `public boolean releaseSavepoint()`
* `public boolean supportsPreparedStatementMetadataRetrieval()`
* `public boolean supportsResultSetMetadataRetrievalOnly()`

## Exploring existing database implementations

[PDI sources](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/get-started-with-the-sample-pdi-project#get-pdi-sources) are invaluable when seeking example implementations of databases. Each of the PDI core database support classes is located in the `org.pentaho.di.core.database` package found in the `core/src` folder.

For example, here are the classes that define behavior for some major database systems.

| **Database**                                                                                                                            | **DatabaseInterface Class**                           |
| --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [MySQL](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/MySQLDatabaseMeta.html)           | `org.pentaho.di.core.database.MySQLDatabaseMeta`      |
| [Oracle](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/OracleDatabaseMeta.html)         | `org.pentaho.di.core.database.OracleDatabaseMeta`     |
| [PostgreSQL](http://javadoc.pentaho.com/kettle530/kettle-core-5.3.0.0-javadoc/org/pentaho/di/core/database/PostgreSQLDatabaseMeta.html) | `org.pentaho.di.core.database.PostgreSQLDatabaseMeta` |

When implementing a database plugin for a new database system, we recommended starting from an existing database class that already shares characteristics with the new database system.

## Deploying database plugins

To deploy your database plugin, perform the following steps:

1. Create a JAR file containing your plugin class(es).
2. Create a new folder, give it a meaningful name, and place your JAR file inside the folder.
3. Place the plugin folder you just created in a specific location for PDI to find.

   Depending on how you use PDI, you need to copy the plugin folder to one or more locations as per the following list.

   * Deploying to the PDI client or Carte: Copy the plugin folder into `design-tools/data-integration/plugins/databases`, then restart the PDI client. After restarting the PDI client, the new database type is available from the PDI database dialog box.
   * Deploying to the Pentaho Server for Data Integration: Copy the plugin folder into `server/pentaho-server/pentaho-solutions/system/kettle/plugins/databases`, then restart the server. After restarting the Pentaho Server, the plugin is available to the server.
   * Deploying to Pentaho Server for Business Analytics: Copy the plugin folder into `server/pentaho-server/pentaho-solutions/system/kettle/plugins/databases`, then restart the server. After restarting thePentaho Server, the plugin is available to the server.
4. When deploying database plugins, make sure to also deploy the corresponding JDBC drivers. See the **Install Pentaho Data Integration and Analytics** document for instructions about adding JDBC drivers.

## Sample database plugin

The sample database plugin project is designed to show an implementation of a database plugin that you can use as a basis to develop your own database plugins.

The sample database plugin registers the CSV JDBC driver from <http://csvjdbc.sourceforge.net/> as a database in PDI. This enables reading from CSV files in a directory using basic SQL.

The included sample transformation in `demo_transform/demo_database.ktr` uses the database plugin to read a basic CSV file through JDBC.

Follow these steps in order to build and deploy the sample plugin.

1. Obtain the sample plugin source.

   The database plugin source is available in the [download package](https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/get-started-with-the-sample-pdi-project#download-the-sample-project). Download the package and unzip it. The database plugin resides in the `kettle-sdk-database-plugin` folder.
2. Configure the build by opening `kettle-sdk-database-plugin/build/build.properties` and setting the **kettle-dir** property to the base directory of your PDI installation.
3. Build and deploy.

   You may choose to build and deploy the plugin from the command line, or work with the Eclipse IDE instead. Both options are described below.

   * [Build and deploy from the command line](#build-and-deploy-sample-database-plugin-from-the-command-line).
   * [Build and deploy from Eclipse](#build-and-deploy-sample-database-plugin-from-eclipse).
4. You can test the new plugin using the transformation from the database plugin `demo_transform` folder.

![Results of database plugin example](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-5d70e0144152c68c09d2d43792b2495d11596de0%2FssPDIExtendPDI_DatabasePlugins_ExampleResults.png?alt=media)

### Build and deploy sample database plugin from the command line

The plugin is built using [Apache Ant](http://ant.apache.org/). Build and deploy the plugin from the command line by invoking the install target from the build directory.

```
kettle-sdk-database-plugin $ cd build
build $ ant install
```

The install target compiles the source, creates a JAR file, creates a plugin folder, and copies the plugin folder into the `plugins/databases` directory of your PDI installation. It also copies `csvjdbc.jar` to PDI's `lib/` directory, which provides the JDBC driver the plugin depends on.

### Build and deploy sample database plugin from Eclipse

Import the plugin sources into Eclipse:

1. From the menu, select **File** > **Import** > **Existing Projects Into Workspace**.
2. Browse to the `kettle-sdk-database-plugin` folder and choose the project to be imported.

To build and install the plugin, follow these steps:

1. Open the **Ant** view in Eclipse by selecting **Window** > **Show View** from the main menu and select **Ant**.

   You may have to select **Other** > **Ant** if you have not used the **Ant** view before.
2. Drag the file `build/build.xml` from your project into the **Ant** view, and execute the install target by double-clicking it.
3. After the plugin has been deployed, restart the PDI client.
