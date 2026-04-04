# Source: https://docs.pentaho.com/pba/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-database-table-source/create-a-database-table-data-source-for-reporting-and-analysis.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-database-table-source/create-a-database-table-data-source-for-reporting-and-analysis.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-wizard-cp-overview/choose-a-data-source-type/create-a-database-table-source/create-a-database-table-data-source-for-reporting-and-analysis.md

# Create a database table data source for reporting and analysis

Follow these steps to create a database table data source for reporting and analysis.

**Note:** Your database must be up and running in order for you to complete these steps:

1. Log in to the **User Console**.
2. Click the **Create New** button, then choose **Data Source** from the menu.
3. Click the **New Data Source** button.

   The **Data\*\*\*\*Source Wizard**appears.
4. Enter a name that identifies your new data source in the **Data Source Name** field.

   The following characters are not allowed in data source names:

   ```
   %/:[]*|\t\r\n
   ```

   ![Table Data Source Reporting and Analysis](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-21b0e089ce214cb9e90e7af6d0f2e8724d8ff07c%2FPUC_Table_Data_Source_Reporting_and_Analysis.png?alt=media)
5. Select **Database Table(s)** from the **Source Type** drop-down menu. Under **Connection**, click to choose a database connection.
6. Click to select **Reporting and Analysis**. Click **Next**.
7. Choose a schema from the **Schema**drop-down menu.

   A list of **Available Tables** appears.

   ![Table Data Source Reporting and Analysis Available Tables](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-8e905d6a777f334a656307da7060084b1604f83c%2FPUC_Table_Data_Source_Reporting_and_Analysis_Available_Tables.png?alt=media)
8. Choose a table from **Available Tables** and click the Right Arrow to move the table into the **Selected Tables** field.

   If you add a table you decide not to use, highlight the table and click the Left Arrow to remove it from the list of **Selected Tables**. To choose multiple tables, press the CTRL key down as you make your selections.
9. Choose a **Fact Table** from the drop-down list and click **Next**.

   While you can create a data source from a single table, the more common scenario is that you will choose multiple tables which must then be joined.

   ![Table Data Source Reporting and Analysis Define Joins](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-e0b727f2070edfb906ed13f05235705bd9f78043%2FPUC_Table_Data_Source_Reporting_and_Analysis_Define_Joins.png?alt=media)
10. Choose the fact table from the **Left Table** drop-down menu, then choose a table to join to it from the **Right Table** drop-down menu. Click **Create Join**to define the inner join between each table.

    The join relationship for each table is based on the field selected and is displayed in the lower portion of the dialog box. To delete a join, select the join and click **Delete Join**.

    1. Create join conditions for each entry in the **Left Table** and **Right Table** drop-down menus.
11. Click **Finish**.

    The **Data Source Created** window appears. You can choose to **Keep default model** or click **Customize model now**to launch the Data Source Model Editor and refine the model. Click **OK**.

    ![Table Data Source Reporting and Analysis Data Source Created](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-20e5098187b129a28916da09d95801ce592fc2cc%2FPUC_Table_Data_Source_Reporting_and_Analysis_Data_Source_Created.png?alt=media)

A multidimensional model is generated for use in Analyzer, Interactive Reports, and Dashboard Designer, or the [Data Source Model Editor](https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp) appears.

**Note:** Before trying to access your new data source in the PDI client (also known as Spoon), you must clear out any shared objects in the PDI client by selecting **Tools** > **Repository** > **Clear Shared Object**.
