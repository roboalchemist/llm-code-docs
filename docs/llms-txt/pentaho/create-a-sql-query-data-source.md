# Source: https://docs.pentaho.com/pba/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-sql-query-data-source.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-sql-query-data-source.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-sql-query-data-source.md

# Create a SQL query data source

Once you create the data source, it is available to users of Interactive Reports, Analyzer, and Dashboard Designer reports.

1. Log in to the **User Console**.
2. Click the **Create New** button, then choose **Data Source** from the menu.
3. Click the **New Data Source** button.

   The Data Source Wizard appears.
4. Enter a name that identifies your new data source in the **Data Source Name** field.

   The following characters are not allowed in data source names:

   ```
   %/:[]*|\t\r\n
   ```

   ![SQL Query Data Source Wizard dialog](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ba60b8dce3e701d947aeadfdab9af4819ad09b71%2FPUC_SQL_Query_Data_Source_Wizard_dialog.png?alt=media)
5. Select **SQL Query** from the **Source Type** drop-down menu. Click **Next**.
6. Select a database connection from the list, under **Data Connection**.
7. Enter your SQL query in the **SQL Query** text field.

   Click **Data Preview** to make sure that your query returns data. The SQL query `select * from CUSTOMERS` is shown in this example.

   ![SQL Query Data Preview](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ed5b63b9601067bc4134dd39972b23db3bbb4881%2FPUC_SQL_Query_Data_Preview.png?alt=media)
8. Click **Close** to exit the **Preview window**. Click **Finish**.
9. The **Data Source Created** window appears.

   You can choose to **Keep default model** or click **Customize model now** to launch the Data Source Model Editor and refine the model. Click **OK**.

   ![SQL Query Data Source Created](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-20e5098187b129a28916da09d95801ce592fc2cc%2FPUC_SQL_Query_Data_Source_Created.png?alt=media)

A relational model is generated based on the SQL query for use in Analyzer, Interactive Reports, and Dashboard Designer reports, or the [Data Source Model Editor](https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp) appears.
