# Source: https://docs.pentaho.com/pba-schema-workbench/get-started-with-the-schema-workbench.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/get-started-with-the-schema-workbench.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/get-started-with-the-schema-workbench.md

# Get started with the Schema Workbench

Before you start using Schema Workbench, you should be aware of the following points:

* You start Schema Workbench by executing the `/pentaho/design-tools/schema-workbench/workbench` script. On Linux and OS X, this is a SH file; on Windows this is a BAT file.
* You must be familiar with your physical data model before you use Schema Workbench. If you don't know which are your fact tables and how your dimensions relate to them, you will not be able to make significant progress in developing a Mondrian schema.
* When you make a change to any field in Schema Workbench, the change will not be applied until you click out of that field such that it loses the cursor focus.
* Schema Workbench is designed to accommodate multiple sub-windows. By default they are arranged in a cascading fashion. However, you may find more value in a tiled format, especially if you put the JDBC Explorer window next to your Schema window so that you can see the database structure at a glance. Simply resize and move the sub-windows until they are in agreeable positions.

## Add a data source

Your data source must be available, its database driver JAR must be present in the`/pentaho/design-tools/schema-workbench/drivers/` directory, and you should know or be able to obtain the database connection information and user account credentials for it.

Follow the below process to connect to a data source in Schema Workbench.

1. Establish a connection to your data source by going to the **Options** menu and selecting **Connection**.

   The Database Connection dialog box appears.
2. Select your database type, then enter in the necessary database connection information, then click **Test**. When you've verified that the connection settings work, click **OK**.

   The database connection information includes the database name, port number, and user credentials. If you don't know what to type into any of these fields, consult your database administrator or database vendor's documentation.

   **Note:** The **Require Schema** check box, when selected in the **Options** menu, puts Schema Workbench into a mode where unpopulated elements appear in the schema.

   **Note:** If you are using an Oracle data source, selecting **Require Schema** will dramatically improve your analysis schema load time.
3. If you required a database schema in the previous step, you must now define it by going to the **Options** section of the database dialog box, and creating a parameter called **FILTER\_SCHEMA\_LIST** with a value of the schema name you want to use.

Your data is now available to Schema Workbench, and you can proceed with creating a Mondrian schema.

## Remove Mondrian data sources

As you phase out old analysis schemas, you will have to manually remove their data source entries in the Data Source Wizard in the User Console.

1. Log in to the User Console with administrator credentials.
2. On the **Home** page of the User Console, click **Manage Data Sources**.

   The Data Source Wizard appears.
3. Click to highlight the data source to be deleted, and click **Remove**.

The data source is removed and is no longer available for use.
