# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-data-labels.md

# Manage data labels

In Pentaho Data Catalog, data labels are structured metadata elements defined as key-value pairs that enable consistent, machine-readable classification of data assets. By managing data labels, you can improve metadata quality, streamline search and filtering, and support AI and machine learning workflows. You can use labels to identify key attributes such as data quality, sensitivity, or customer sentiment. As a data steward or administrator, you can add, edit, or remove data labels to ensure the catalog stays organized and aligned with your organization’s data classification standards.

## Add a data label

Adding a new data label helps you consistently categorize and annotate data assets in the catalog using structured, predefined values. This improves data quality, discoverability, and supports AI and machine learning initiatives by enabling meaningful classification.

Perform the following steps to add a data label to the data resource in Data Catalog:

1. In the left navigation menu, select **Data Canvas**.

   The list of available data sources and folders appears.
2. Expand the data source hierarchy and select a resource, such as a schema, table, column, folder, file, or more.
3. Select the **Properties** tab and click **Add Custom Property**.

   The Add Custom Property dialog box appears.
4. In the **Property Name** field, enter a name for the data label.
5. Enable the **Data Label** toggle.

   This identifies the entry as a data label instead of a custom property, and the **Field Type** will be greyed out as it applies only to custom properties.
6. Under **Available Values**, enter the allowed values for the label. Click **Add Value** to include additional values.

   **Note:** You can define up to six values.
7. (Optional) In the **Description** field, add a brief description of the label's purpose.
8. From the **Default Value** list, select a default value to assign when no other is specified.
9. Under **Assign to an Item Type**, select the data asset types the label applies to, such as **Tables**, **Columns**, **Datasets**, and more.
10. Verify the entered data and click **Save**.

You have successfully created and added the data label, and it appears in the **Properties** tab for the selected resource.

You can now use this label to classify data across your catalog consistently.

## Associate a data label with data assets

Associating a data label with a data asset helps you to apply meaningful and standardized properties, which improves data governance, searchability, and machine learning workflows.

Perform the following steps to associate a data label with a data asset in Data Catalog:

1. In the left navigation menu, select **Data Canvas**.

   The list of available data sources and folders appears.
2. In the data hierarchy, select the data asset you want to associate with a data label and select the **Properties** tab.

   The list of available custom properties and data labels appears.
3. Locate the data label you want to associate with the selected asset.
4. In the **Value** column, click the drop-down list for the data label and select the required value.

You have successfully associated the selected data label value with the data asset and can be used to drive classification, filtering, and ML-based insights.

## Edit a data label

By editing a data label, you can refine the metadata applied across data assets in Data Catalog. You can rename the label, add new predefined values, update the default value, and extend its scope to additional item types. This helps ensure your data remains accurately categorized and aligned with evolving business or machine learning requirements.

Perform the following steps to edit a data label in Data Catalog:

1. In the left navigation menu, select **Data Canvas**.

   The list of available data sources and folders appears.
2. Expand the data source hierarchy, select a resource that contains the data label and select the **Properties** tab.

   The list of available custom properties and data labels appears.
3. Locate the data label you want to edit and click the **Edit** icon.

   The Edit Custom Property dialog box appears.
4. In the **Edit Custom Property** dialog box, you can:
   1. Update the label name in the **Property Name** field.
   2. Add any additional values you want to support under **Available Values**. To add new values, click **Add Value**.

      **Note:** You cannot remove or modify existing values, and you can define up to six values.
   3. Select a new default value in the **Default Value** list.
   4. Select any additional data asset types where this data label should apply (for example, **Files**, **Datasets**, or **Data Products**) under **Assign to an item type**.

      **Note:** You cannot deselect previously assigned item types.
5. Verify the updated values and click **Save**.

You have successfully updated the data labels, and the updates are applied to all objects that use this data label.

## Remove a data label

Removing a data label helps you eliminate outdated or unused metadata from Data Catalog, keeping the data classifications clean and relevant.

**Note:** You can only remove a data label if it is not associated with any data asset.

Perform the following steps to remove a data label in Data Catalog:

1. In the left navigation menu, select **Data Canvas**.

   The list of available data sources and folders appears.
2. Expand the data source hierarchy and select a resource that contains the data label. Then, select the **Properties** tab.
3. Locate the data label you want to remove and click the **Delete** icon.
4. In the confirmation dialog box, click **Confirm**.

If the data label is not currently in use, it is deleted from Data Catalog. If it is already associated with one or more data assets, a message appears:

```
Failed to remove property: This property is associated with another entity and cannot be removed.
```
