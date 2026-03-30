# Source: https://docs.pentaho.com/pba-aggregation-designer/get-started-with-the-pentaho-aggregation-designer.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/9.3-aggregation-designer/get-started-with-the-pentaho-aggregation-designer.md

# Source: https://docs.pentaho.com/pba-aggregation-designer/10.2-aggregation-designer/get-started-with-the-pentaho-aggregation-designer.md

# Get started with the Pentaho Aggregation Designer

The Pentaho Aggregation Designer workspace is shown below.

![Custom aggregates](https://2790200156-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMLn7wj5kT2VbUHEUieXY%2Fuploads%2Fgit-blob-a886b1c89f8ab7bf9c4365ff7faf8dc6dbfa53b2%2FPAD_custom_aggregates.png?alt=media)

The Aggregation Designer contains the following sections:

* **Impact Summary**

  The impact summary in the lower right pane provides you with information on the estimated impact for creating all of the currently selected aggregates. This summary includes the number of aggregate tables that will be created, the estimated number of rows contained in those tables, and the estimated amount of space it will occupy on the hard drive. The impact summary is automatically updated as you select and deselect aggregates from the list of proposed aggregates.
* **Cost/Benefit Chart**

  The Cost/Benefit chart provides a high-level comparison of the benefit of all currently selected aggregates relative to their estimated cost. The benefit scale represents the relative number of queries that can be fulfilled by an aggregate table versus having to be retrieved from the base fact table. The cost scale is an indicator of the impact in terms of number of tables and disk space needed to create the selected aggregate recommendations.
* **File Menu**

  You can save all aggregate-related data (custom- or advisor-created) in your workspace at any time. Saving ensures that all of the data (your designs) in the workspace is retained; you are saving the state of your workspace as an XML file in a location you specify. To save, go to the **File** menu and click **Save As**. To open a saved file, go to the **File** menu and click **Open**, then navigate to the design you previously saved.

## Define a data source

To design an aggregate table, you must first establish a connection with your target relational database, then select the OLAP model to optimize. You can connect to any relational database that is supported by Mondrian. In some instances, you may need to define additional parameter-related values for your JDBC driver.

![Sample data source connection to Pentaho Aggregation Designer](https://2790200156-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMLn7wj5kT2VbUHEUieXY%2Fuploads%2Fgit-blob-6c0efdcded14a73982195127e2be5609869b1c81%2FPAD_connection_properties.png?alt=media)

To define a data source connection, perform the following steps:

1. In the Pentaho Aggregation Designer toolbar, click **Connection** to open the Connect to Data Source dialog box.
2. Click **Configure**.

   The Connection Properties dialog box appears.
3. In the **Connection Name** field, enter a name for your connection; this is a free-text field.

   A connection name uniquely defines a connection.
4. In the **Connection Type** list, select a database.
5. In the **Access** list, keep the default choice, which should be Native (JDBC).
6. In the **Settings** section, enter the following information:
   1. Type the host name of the database server into the **Host Name** field.
   2. In the **Database Name** field, type the name of the database you're connecting to.
   3. In the **Port Number** field, enter the TCP port number.
   4. (Optional) In the **User Name** and **Password** fields, type the user name and password used to connect to the database.
7. Click **Test**.

   If the settings you typed in are correct, a success message appears.
8. Click **OK**.
9. (Optional) If you must define additional parameters for your JDBC driver, or if you want to enter your server settings manually, follow these instructions:
   1. Click **Options** in the left panel.
   2. Enter the parameter name and value for the settings you need to specify.

      For example, `PORT` (parameter name), `1025` (parameter value).
   3. Click **Test** when your settings are entered.

      A success message appears if everything was typed in correctly.
   4. Click **OK**.
