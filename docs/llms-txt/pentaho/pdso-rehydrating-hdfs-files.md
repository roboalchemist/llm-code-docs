# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-rehydration/pdso-rehydrating-hdfs-files.md

# Rehydrating HDFS files

Perform the following steps to rehydrate HDFS files:

**Note:** Rules-governed rehydration is only available for tiered HDFS files.

1. Click **Management**. 

   The Manage Your Environment page opens.
2. On the **Rules** card, click **Add New** > **Add Rule Definition**.

   The **Rule Definition** page opens.
3. Create a rule definition. The following example uses a file size for the definition.
   1. Enter a name for the rule definition in the **Name** field.

      For example, `Rehydrate Moved Files`.
   2. Enter a description of the rule definition in the **Description** field.
   3. Click **Select an option** and choose **FILE** or **FOLDER** as the object type.
   4. Click **Add Condition** to create the query condition.
   5. Click **Select attribute** and select the attribute from the menu.

      For example, **File Size**.
   6. Click **Operator** and select an operator.

      For example, **Greater than or equal to**.
   7. Enter a size in the **Size** field.

      For example, `9`.
   8. Click **Unit** and select the unit size from the menu.

      For example, `GB`.
   9. Click **Add Action** > **Start Process**.
   10. Click **Select Process** > **Rehydrate**.
   11. Click **Save**.
4. On the **Rules** card, click **Add New** > **Add Rule**.

   The **Metadata Rule** page opens.
5. Create a metadata rule. The following example uses the `Rehydrate Moved Files` rule definition, above.
   1. Enter a name for the rule in the **Rule Name** field.

      For example, `Restore Tiered Files`.
   2. Click **Source Data Asset** and select the data source on which to run the metadata rule.
   3. Click **Select the rule definition** and select the rule definition.

      For example, `Rehydrate Moved Files`.
   4. Select **Run rule definition now** to run the rule immediately.
   5. You can also click **Add Schedule** to enter a time to run it later.
6. Click **Apply**.

Files marked Tiered that are greater than or equal to 9 GB are rehydrated.

To view the results, go to the Manage Your Environment page and on the **Data Operations** card, click **Submitted**. On the Data Operations page, the status of the operation, file name, path, source, type, and destination are provided.
