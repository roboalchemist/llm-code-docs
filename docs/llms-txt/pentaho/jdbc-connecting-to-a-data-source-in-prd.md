# Source: https://docs.pentaho.com/pba-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd.md

# JDBC

Any JDBC-compliant database will work with Report Designer, but you will probably have to provide your own JDBC driver JAR. This is accomplished by copying the appropriate JAR file to the `/pentaho/design-tools/report-designer/lib/` directory.

You may need to obtain database connection information from your system administrator, such as the URL, port number, JDBC connection string, database type, and user credentials.

**Note:** To pass security-related information, (such as user name and password), associated with a report over a JDBC connection, see the topics, [Passing security information to a report over a JDBC connection](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/connect-report-designer-to-a-data-source-cp/jdbc-connecting-to-a-data-source-in-prd/passing-security-information-to-a-report-over-a-jdbc-connection-connecting-to-a-data-source-in-prd).

Follow this procedure to add a standard JDBC data source in Report Designer.

1. Select the **Data** tab in the upper right pane.

   By default, Report Designer starts in the **Structure** tab, which shares a pane with **Data**.
2. Click the yellow cylinder icon in the upper left part of the **Data** pane, or right-click **Data Sets**.

   A drop-down menu with a list of supported data source types appears.
3. Select **JDBC** from the drop-down menu.

   The JDBC Data Source window appears.
4. If you want to provide parameters that contain different database connection authentication credentials, click the **Edit Security** button in the upper left corner of the window, then type in the fields or variables that contain the user credentials you want to store as a parameter with this connection.

   The role, username, and password will be available as a security parameter when you are creating your report.
5. Above the **Connections** pane on the left, click the round green **+** icon to add a new data source.

   If you installed the Pentaho sample data, several **SampleData** entries appear in the list. These sample data sources are useless if you do not have the Pentaho HSQLDB sample database installed, so if you don't have that, you can safely delete the **SampleData** entries. If you do have Pentaho's HSQLDB samples installed, it may be advantageous to leave the sample data sources intact in the event that you want to view the sample reports and charts at a later time.
6. In the Database Connection dialog, type in a concise but reasonably descriptive name for this connection in the **Connection Name** field; select your database brand from the **Connection Type** list; select the access type in the **Access** list at the bottom; then type in your database connection details into the fields in the **Settings** section on the right.

   The **Access** list changes according to the connection type you select; the settings section will change depending on which item in the access list you choose.
7. Click the **Test** button to ensure that the connection settings are correct.
   * If they are not, the ensuing error message should give you some clues as to which settings need to be changed.
   * If the test dialog says that the connection to the database is OK, then click the **OK** button to complete the data source configuration.

Now that your data source is configured, you must design or enter an SQL query before you can finish adding the data source. See [Create queries with SQL Query Designer](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PRD/Create%20queries/Create%20queries%20\(Report%20Designer%20cp\)/Create%20queries%20with%20SQL%20Query%20Designer%20\(Create%20queries%20in%20PRD\)=GUID-5F4C606C-D84D-49C9-B611-2E39F46AC00F=3=en=.md) for more details on using SQL Query Designer, or [Dynamic query scripting](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/create-queries-report-designer-cp/dynamic-query-scripting) for more information on building dynamic queries through scripts.
