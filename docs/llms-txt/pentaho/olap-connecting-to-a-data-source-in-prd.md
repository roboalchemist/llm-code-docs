# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/olap-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/olap-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/olap-connecting-to-a-data-source-in-prd.md

# OLAP

You may need to obtain database connection information from your system administrator, such as the URL, port number, JDBC connection string, database type, and user credentials.

Follow this procedure to add a Pentaho Analysis (Mondrian) data source in Report Designer.

1. Select the **Data** tab in the upper right pane.

   By default, Report Designer starts in the **Structure** tab, which shares a pane with **Data**.
2. Click the yellow cylinder icon in the upper left part of the **Data** pane, or right-click**Data Sets**.

   A drop-down menu with a list of supported data source types will appear.
3. Select **OLAP** from the drop-down menu, then select one of the following:
   * Pentaho Analysis
   * Pentaho Analysis (Denormalized)
   * Pentaho Analysis (Legacy)\
     The Mondrian Datasource Editor window will appear.
4. If you want to provide parameters that contain different Mondrian connection authentication credentials, click the **Edit Security** button in the upper left corner of the window, then type in the fields or variables that contain the user credentials you want to store as a parameter with this connection.

   The role, username, and password will be available as a security parameter when you are creating your report.
5. Click **Browse**, navigate to your Mondrian schema XML file, then click **Open**.
6. Above the **Connections** pane on the left, click the round green **+** icon to add a new data source.

   If you installed the Pentaho sample data, several **SampleData** entries will appear in the list. You must have HSQLDB to view the sample data.
7. In the subsequent Database Connection dialog box, perform the following actions:

   1. Type in a concise but reasonably descriptive name for this connection in the **Connection Name** field.
   2. Select your database brand from the **Connection Type** list.
   3. Select the access type in the **Access** list at the bottom.
   4. Type in your database connection details into the fields in the **Settings** section on the right.

   The **Access** list will change according to the connection type you select; the settings section will change depending on which item in the access list you choose.
8. Click the **Test** button to ensure that the connection settings are correct.
   * If they are not, the ensuing error message should give you some clues as to which settings need to be changed.
   * If the test dialogue says that the connection to the database is OK, then click the **OK** button to complete the data source configuration.

Now that your data source is configured, you must enter an MDX query before you can finish adding the data source. You can also create a dynamic query through scripts; see [Dynamic query scripting](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/dynamic-query-scripting) for more information.
