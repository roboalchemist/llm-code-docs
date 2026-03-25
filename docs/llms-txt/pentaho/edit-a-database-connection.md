# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/edit-a-database-connection.md

# Edit a database connection

You can edit an existing Database Connection to refine and change aspects of the connection.

To edit a database connection, complete the following steps:&#x20;

1. With a transformation or job open, on the left side of the Pipeline Designer interface, click the **View** icon. The **View** pane opens with the Transformations folder expanded, containing the **Database Connections**.
2. Expand **Database Connections**, find the database connection you want to edit, and click the **More Actions** icon.&#x20;
3. Select **Edit**. The Database Connection window opens.&#x20;
4. Configure the options in each tab of the Database Connections window. To learn more about the options in each tab, see the section for that tab in this topic.&#x20;
   1. [**General**](#general)
   2. [**Advanced**](#advanced)
   3. [**Options**](#options)
   4. [**Pooling**](#advanced)
   5. [**Clustering**](#clustering)
5. (Optional) To view features of the database connection, click **Feature List**.
6. (Optional) To explore configured database connections, click **Explore**. For more details, see [Explore configure database connections](https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/explore-configure-database-connections).
7. Click **Test Connection**. If the connection is established, a success message is displayed.&#x20;
8. Click **OK** to close Success message.
9. Click **Save**. The connection is saved and the **Database Connections** window closes.

## General

In the **General** tab, the options you have to edit depend on the type of database connection you are editing. Connection information depends on your access protocol. For details about general connection settings, refer to examples in the topic, [Define a new database connection](https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/define-a-new-database-connection).

## Advanced

The **Advanced** tab contains options for configuring properties associated with how SQL is generated. With these properties, you can set a standard across all your SQL tools, ETL tools, and design tools.

| Supports the Boolean data type                    | Instructs Pipeline Designer to use native Boolean data types supported by the database.                                                                                                                       |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supports the timestamp data type                  | Instructs Pipeline Designer to use the timestamp data type supported by the database.                                                                                                                         |
| Quote all in database                             | Enables case-sensitive table names. For example, MySQL is case-sensitive on Linux, but not case-sensitive on Microsoft Windows. If you quote the identifiers, the databases uses a case-sensitive table name. |
| Force all to lower-case                           | Enables the system to change the case of all database to lower-case.                                                                                                                                          |
| Force all to upper-case                           | Enables the system to change the case of all identifiers to upper-case.                                                                                                                                       |
| Preserve case of reserved words                   | Instructs Pipeline Designer to use a list of reserved words supported by the database.                                                                                                                        |
| The Preferred Schema name where no schema is used | For Pipeline Designer, enter the preferred schema name (for example, `MYSCHEMA`).                                                                                                                             |
| SQL Code Editor                                   | Enter the SQL statements to execute right after connecting.                                                                                                                                                   |

## Options

Use the Options tab to add or delete parameters. Parameters enable you to control database‑specific behavior.

* To add more Parameters to the list, click **Add Row**.&#x20;
* To Delete rows, click the **Delete** icon next to the row.

## Pooling&#x20;

Configure options in the **Pooling** tab to set up a connection pool and define options like the initial pool size, maximum pool size, and connection pool parameters. By default, a connection remains open for each individual report or set of reports in PUC and for each individual step in a transformation in PDI. For example, you might start by specifying a pool of ten or fifteen connections, and as you run reports in PUC or transformations in PDI, the unused connections drop off. Pooling helps control database access, especially if you have dashboards that contain many reports and require a large number of connections. Pooling can also be implemented when your database licensing restricts the number of active concurrent connections.

You can take the following action in the parameters section:

* To add a new parameter, click **Add Row** and then enter the **Parameter** name and **Value**.&#x20;
* To delete a parameter, click the **Delete** icon.
* To change how many parameters are shown at one time, select a new **Items per page** value.
* If there are multiple pages of parameters, scroll through the pages using the left and right arrow that appear under the list of parameters.

The following table shows an example of **Pooling** options that might be available in a typical JDBC driver. Check your driver documentation for driver-specific pooling details.

| Option                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enable Connection Pooling** | Enables connection pooling.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Pool Size**                 | <ul><li><strong>Initial</strong></li></ul><p>Set the initial size of the connection pool.</p><ul><li><strong>Maximum</strong></li></ul><p>Set the maximum number of connections in the connection pool.</p>                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Parameters**                | <p>You can define additional custom pool parameters. Click on any parameter to view a short description of that parameter. Click <strong>Restore Defaults</strong> when to restore the default values for selected parameters.The most commonly-used parameter is <strong>validationQuery</strong>. The parameter differs slightly depending on your RDBMS connection. The basic set of Pentaho databases use the following values for <strong>validationQuery</strong>:</p><ul><li>For Oracle and PostgreSQL, use <strong>Select 1 from dual</strong>.</li><li>For MS SQL Server and MySQL, use <strong>Select 1</strong>.</li></ul> |
| **Description**               | Enter a description for your parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Clustering

Use the **Clustering** options to cluster the database connection and create connections to data partitions in Pipeline Designer. To create a new connection to a data partition, enter a **Partition ID**, the **Host Name**, the **Port**, the **Database Name**, **User Name**, and **Password** for the connection.

If you have the Pentaho Server configured in a cluster of servers, and use the Data Source Wizard (DSW) in PUC to add a new data source, the new data source will only be seen on the cluster node where the user has a session. For the new data source to be seen by all the cluster nodes, you must disable DSW data source caching. This may cause the loading of the data source list to be slower since the list is not cached.

To disable the cache, navigate to the `server/pentaho-server/pentaho-solutions/system` folder and set the **enableDomainIdCache** value in the `system.properties` file to false.
