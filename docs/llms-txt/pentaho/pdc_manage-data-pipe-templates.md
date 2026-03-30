# Source: https://docs.pentaho.com/pdc-admin/pdc_manage-data-pipe-templates.md

# Manage data pipe templates

In Pentaho Data Catalog, you can create templates that helps to speed the migration, duplication, and purging of datasets (for both structured and unstructured) from a source to a target database. To know more about **Data Pipe Templates** and key features, see **Data Pipe Templates** section in **Use Pentaho Data Catalog** document.

The data pipes feature gives a user-friendly interface that you can access on the **Data Pipe Templates** card under the **Data Operations** section and you can create, configure, and manage data pipelines.

## View a data pipe template

Perform the following steps to view the existing data movement template in Data Catalog:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Click **View Data Pipe Templates** or the number shown in the Data Pipe Template card.

   The list of available data pipe templates opens.
3. Click the template name to view it. Alternatively, you can click the **More** icon and select **View**.

   The template with the scope, action, optional actions, and destination folder selected opens.
4. (Optional) You can edit the template name and optional actions if necessary.

   For more information, see [Edit a data pipe template](#edit-a-data-pipe-template) for more information.

You can schedule data movement using a data pipe template. For more information, see [Schedule data movement with a data pipe template](#schedule-data-movement-with-a-data-pipe-template).

## Schedule data movement with a data pipe template

Perform the following steps to schedule data movement using an existing data pipe template in Data Catalog:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Click **View Data Pipe Templates** or the number shown in the Data Pipe Templates card.

   The list of available data pipe templates opens.
3. Click the template name to view it. Alternatively, you can click the **More** icon and select **View**.

   The template with the scope, action, optional actions, and destination folder selected opens.
4. (Optional) You can edit the template name and optional actions if necessary.

   For more information, see [Edit a data pipe template](#edit-a-data-pipe-template) for more information.
5. Click **Schedule Run** and add the date and time for the data movement. You can also choose to run only once or **Repeat Daily**, **Weekly**, or **Monthly**.
6. Click **Schedule** to save the configurations.

You have successfully scheduled a data movement using the data pipe template. You can view the scheduled data movement on **Schedules** under **Management**.

## Create a data pipe template

Perform the following steps to create a data pipe template for moving or copying data from the source database to a destination database:

**Important:** The data pipe feature uses Pentaho Data Integration templates. For any support with Data Integration template setup and configuration, contact [Pentaho Support](https://support.pentaho.com/).

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Click **View Data Pipe Templates** or the number shown in the Data Pipe Templates card.

   The list of available data pipe templates opens.
3. Click **Add Data Pipe Template** and enter a name for the new template in the **Name** box.
4. (Optional) In the **Engine** list, select the appropriate engine:

   * Select the **Data Integration** engine for structured data sources, such as relational databases (RDBMS).
   * Select the **Data Optimizer** engine for unstructured data sources, such as object stores or file systems.\
     To learn more about engines, see **Dual engine processing** topic under **Data Pipe Templates** section in the Use Pentaho Data Catalog document.

   **Note:** Once you select an engine, Data Catalog restricts the data assets available in the Scope to match the selected engine.
5. On the Scope card, click **Add Scope**.

   The list of connected data sources appears.

   * If the required database is not listed and you want to add it to Data Catalog, see [Adding a data source](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag).
   * For existing databases, ensure they are enabled for data movement. If not, you can [edit the data source](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/edit-a-data-source-ldc-manage-data-sources-ag) settings and select **Available for Migration** and **Available for Writing** to enable data movement.
6. On the available database list, expand the database tree and select the items you want to move.

   If you did not select an engine earlier or accessed this page by clicking **Move Data** from the Data Canvas, Data Catalog automatically selects the appropriate engine based on the type of data assets added in the Scope.
7. For RDBMS data sources, to add subsets:
   1. Click **Add Subset**. The **Subset** dialogue box opens.

      You can create a subset for a single table or for multiple tables from the same schema within the same database.

      * When creating a subset involving joins between multiple tables, you must enable **privacy**.
      * When creating a subset for a single table, it works whether privacy is enabled or not.
   2. Use the query builder, such as SQL editor, add the required condition parameters to filter the data, then click **Add Subset**.\
      Additionally, you can utilize the **Smart Type to SQL** feature, an AI-powered enhancement that helps with adding subsets. This feature enables you to convert plain English text into executable SQL queries, simplifying the creation of subsets. It supports previewing results, syntax validation, and multi-table query generation. For more information, see the feature walkthrough of the [Text2sql generator](https://hitachi-vantara.navattic.com/42h0xxg?g=cmfuo2zz5000004l6a44302pi\&s=0). If the **Smart Type to SQL** feature is not configured, see Configure Smart Type to SQL feature in Data Catalog to configure it.
8. (Optional) To add multiple items, click **Add Scope** and select items.
9. On the Main Actions card, select an option:
   * **Duplicate Data**: Creates a copy of the selected data in the target destination.
   * **Move Data**: Moves the selected data to the destination and deletes it from the source.
   * **Purge Data**: Permanently deletes the selected data as part of the execution.

     **Note:** The options vary based on the data source and data migration configuration selected while creating the connection with Data Catalog. To edit the data source connection, see [Edit a data source](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/edit-a-data-source-ldc-manage-data-sources-ag).
10. Based on the selected **Main Actions**, on the Optional Actions card, you can enable the following optional actions:
    1. **Tag Source** and **Tag Destination**, then enter keywords to add as tags on source and destination data.
    2. **Send Notification** to notify a user or group of users.
    3. **Allow Stub Creation**: Enables the creation of stubs in place of the moved or purged files. Stubs are placeholders that retain metadata and can facilitate data rehydration in the future if needed.
    4. **Apply** privacy by configuring the masking or encrypting sensitive columns for structured (RDBMS) data. For more information, see the **Advanced data privacy** topic under the **Data Pipes Templates** section in the Use Pentaho Data Catalog document.

       **Note:** It appears only when duplicating structured data to another structured destination using the **Data Integration** engine.
11. On the Destination card, click **Add Destination** and select the target database.\
    Selecting a destination is mandatory to save or run a data pipe template. If no destination is selected, the **Save** and **Save & Run** options remain disabled.
12. When you have defined all the information, click **Save** to save the template. You can also click **Save & Run** to save and begin the data movement.

You have successfully created a data pipe template for data movement.

When the data movement begins, you can monitor the process and receive notifications when the tasks have been completed. For more information about tracking the progress, see [Manage worker processes](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Administer/Manage%20worker%20processes/Manage%20worker%20processes%20\(cp\)=GUID-A2CA0A62-02C6-44D2-B1CA-23101DC7C1CF=2=en=.md). Additionally, you can also schedule the data movement using a data movement template. For more information, see [Schedule data movement with a data pipe template](#schedule-data-movement-with-a-data-pipe-template).

## Edit a data pipe template

With applicable permissions, perform the following steps to edit an existing data movement template:

**Important:** Only the owner can modify the template scope, main actions, and destination folders.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Click **View Data Pipe Templates** or the number shown in the Data Pipe Templates card.

   The list of available data pipe templates opens.
3. To modify the template's name, click the pencil icon next to the name, enter the modified name in the **Name** box, and then click the check mark.
4. To update the subset in the existing scope, click **Edit Subset** and in the query builder, update the condition parameters to filter the data and click **Add Subset**.
5. To add an additional scope, on the **Scope** card, click **Add Scope**.

   The list of connected databases opens. If the database is unavailable on the list and you want to add it to Data Catalog, see [Adding a data source](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/adding-a-data-source-ldc-manage-data-sources-ag).
6. On the existing database list, expand the database tree for a database and select the items you want to move.
7. For RDBMS data sources, to add subsets:
   1. Click **Add Subset**. The Subset dialogue box opens.
   2. Use the query builder, such as SQL editor, add the required condition parameters to filter the data, then click **Add Subset**.
8. To update the action, you can select a different action on the Main Actions card, such as **Duplicate Data**, **Move Data**, and **Purge Data**.

   **Note:** The options vary based on the data source configured while creating the connection with Data Catalog. To edit the data source connection, see [Edit a data source](https://docs.pentaho.com/pdc-admin/ldc-manage-data-sources-cp/edit-a-data-source-ldc-manage-data-sources-ag).
9. On the Optional Actions card, you can enable:
   1. **Tag Source** and **Tag Destination**, then enter keywords to add as tags on source and destination data.
   2. **Send Notification** to notify a user or group of users.
10. To update the destination folder, on the Destination card, click **View** and select the target database to save data moved or copied.\
    Selecting a destination is mandatory to save or run a data pipe template. If no destination is selected, the **Save** and **Save & Run** options remain disabled.
11. When you have defined all the information, click **Save & Run** to begin the data movement.

You have successfully updated the data pipe template for data movement.

When the data movement begins, you can monitor the process and receive notifications when the tasks have been completed. For more information about tracking the progress, see [Manage worker processes](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Administer/Manage%20worker%20processes/Manage%20worker%20processes%20\(cp\)=GUID-A2CA0A62-02C6-44D2-B1CA-23101DC7C1CF=2=en=.md). Additionally, you can also schedule the data movement using a data pipe template. For more information, see [Schedule data movement with a data pipe template](#schedule-data-movement-with-a-data-pipe-template).

## Delete a data pipe template

Perform the following steps to delete an existing data pipe template:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Click **View Data Pipe Templates** or the number shown in the Data Pipe Templates card.

   The list of available data pipe templates opens.
3. Click the **More** icon and select the **Delete** icon on the template you want to delete.

   A confirmation window appears.
4. Click **Confirm** to confirm the deletion.

You have successfully deleted the data pipe template.
