# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-applications-overview.md

# Manage applications

Manage applications in Pentaho Data Catalog to help your organization understand what type of data is being linked from an external application. Use Data Catalog to create, organize, curate, and identify application assets like external applications, groups, and categories. By organizing external applications into groups and then into categories, you create applications hierarchy that you can use with role-based access control to secure and separate valuable data and metadata and prevent such data from reaching unintended audiences.

You can perform the following actions based on your permissions in Data Catalog.

## Create an application category

Perform the following steps to create an application category to use for organizing the application assets in Data Catalog:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. Click **Actions** > **Add New Category**.

   The **Create Category** dialog box opens.
3. In the **Category Name** box, enter a name for the application category that you want to create and then click **Create**.

   The application category is created and added to the list of applications, which is in the **Applications** navigation tree.
4. In the **Description** box, click **Edit**, enter the description, and then click **Save**.
5. In the **Purpose** box, click **Edit**, enter the purpose, and then click **Save**.
6. (Optional) To change the application category name, click the pencil icon that is next to the application category name and then update the name.
7. (Optional) In the Properties and Style windows, update the values to help you identify the application asset.

   For more information, see the [Applications](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-applications-ug) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created the application category.

See [Create an application group](#create-an-application-group) to create groups.

## Remove an application category

Whenever the application category is not required, you can remove it from Data Catalog, but deleting an application category irrevocably removes all its associated groups and applications in Data Catalog.

**CAUTION:** Because you cannot recover applications asset data, use caution when removing it.

Perform the following steps to remove an application category:

1. In the left navigation tree, select the application category that you want to remove.
2. Click the **More** icon and then click **Delete**.

   A dialog box opens, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully removed the application category along with its associated groups and applications in Data Catalog.

## Create an application group

Perform the following steps to create an application group to use for organizing the applications under categories in Data Catalog:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. click **Actions** > **Add New Group**.

   The **Create Group** dialog box opens.
3. In the **Group Name** box, enter a name for the application group that you want to create.
4. In the **Parent** box, select an application category from the list and then click **Create**.

   **Note:** If you select an application category from the list before creating a new application group, that category is automatically pre-selected as the new group's category. You can choose a different category if necessary.

   The group is created and shown under the selected application category, which is in the **Applications** navigation tree.
5. In the **Description** box, click **Edit**, enter the description, and then click **Save**.
6. In the **Purpose** box, click **Edit**, enter the purpose, and then click **Save**.
7. (Optional) To change the application group name, click the pencil icon that is next to the application category name and then update the name.
8. (Optional) In the Properties and Style windows, update the values to help you identify the application asset.

   For more information, see the [Applications](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-applications-ug) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created the application group.

See [Create an application](#create-an-application) to create an application in Data Catalog.

## Remove an application group

Whenever the application group is not required, you can remove it from Data Catalog, but deleting an application group irrevocably removes all its associated applications in Data Catalog.

**CAUTION:** Because you cannot recover applications asset data, use caution when removing it.

Perform the following steps to remove an application group:

1. In the left navigation tree, select the application group that you want to remove.
2. Click the **More** icon and then click **Delete**.

   A dialog box opens, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully removed the application group along with its associated applications in Data Catalog.

## Create an application

Perform the following steps to create an application and organize it in Data Catalog:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. click **Actions** > **Add New Application**.

   The **Create Application** dialog box opens.
3. In the **Application Name** box, enter a name for the application that you want to create.
4. In the **Parent** box, select an application category and group from the list and then click **Create**.

   **Note:** If you select an application group from the list before creating a new application, that group is automatically pre-selected as the new parent item. You can choose a different category and group if necessary.

   The application is created and shown under the selected category and group, which is in the **Applications** navigation tree.
5. In the **Description** box, click **Edit**, enter the description, and then click **Save**.
6. In the **Purpose** box, click **Edit**, enter the purpose, and then click **Save**.
7. (Optional) To change the application name, click the pencil icon that is next to the application name and then update the name.
8. (Optional) In the Properties and Style windows, update the values to help you identify the application asset.

   For more information, see the [Applications](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-applications-ug) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

You have successfully created the application.

## Remove an application

Whenever the application is not required, you can remove it from Data Catalog, but deleting an application irrevocably removes all its associations in Data Catalog

**CAUTION:** Because you cannot recover applications asset data, use caution when removing it.

Perform the following steps to remove an application:

1. In the left navigation tree, select the application that you want to remove.
2. Click the **More** icon and then click **Delete**.

   A dialog box opens, asking you to confirm the deletion.
3. To confirm the deletion, click **Confirm**.

You have successfully removed the application.

## Edit an application, group, or category

Whenever required, you can reorganize application assets and modify the related information. Users with appropriate permissions can edit the application assets such as an application, group, or category, and their features, such as name, definition, and purpose, including tags added to the item.

**Note:** When you update an application asset name, the changes are reflected for all users.

Perform the following steps to edit an application item:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. Select the application, group, or category that you want to edit.
3. Complete one or both of the following actions:
   * To edit the application asset's name, in the Summary tab, click the pencil icon that is next to the name box, update the name, and then click outside of the name box to save the changes.
   * To edit the application asset's description and purpose, in the Summary tab, click **Edit**, update the description and purpose, and then click **Save** to save the update.

You have successfully modified the application asset.

## Import application hierarchy

An application hierarchy is an organized structure that represents the relationships among application assets, like external applications, groups, and categories within Data Catalog. You can import an application hierarchy from a file with one of the following file types and quickly set up or update the structure:

* JSON Lines (See [https://jsonlines.org/](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fjsonlines.org%2F\&data=05%7C02%7Cmike.dwyer%40hitachivantara.com%7C40e66de83087428a480508dd370afff3%7C18791e1761594f52a8d4de814ca8284a%7C0%7C0%7C638727242553751122%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C\&sdata=hroGNKkzU7vLRdb8j7vS%2FoshJlJ%2B6Bzm%2FcY0K1WxGIU%3D\&reserved=0) for more information)
* Comma Separated Values (text/csv)

Perform the following steps to import an application hierarchy:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. click **Actions** > **Import**.

   The **Import Assets** dialog box opens.
3. In the **Label** box, browse to select the file you want to import, and then click **Submit**.

You have imported the application hierarchy. The imported application assets are now visible in the left applications tree.

## Export application hierarchy

An application hierarchy is an organized structure that represents the relationships among application assets, like external applications, groups, and categories within Data Catalog. You can export an application hierarchy into a JavaScript Object Notation (application/json) or Comma Separated Values (text/csv) file, so that you can use the file to import whenever required. Perform the following steps to import an application hierarchy:

1. In the left navigation menu, click **Applications**.

   The Applications page opens.
2. Click **Actions** > **Export**.

   The **Export Assets** dialog box opens.
3. Select what to export. Select individual applications, or choose **Select all** to export every application in the list.\
   You can also use **Search** to find items. The counter (for example, **0/11**) shows how many are selected.
4. Select the file type (**CSV** or **JSON**) to which you want to export the application hierarchy and then click **Submit**. This downloads the file containing the application assets in the selected format into the local folder.

You have successfully exported the application hierarchy into the selected file type.
