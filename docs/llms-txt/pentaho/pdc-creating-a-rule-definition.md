# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-use-rules/pdc-rule-definitions/pdc-creating-a-rule-definition.md

# Creating a rule definition

You create rule definitions to specify the criteria used and actions performed by a rule.

Perform the following steps to create a metadata rule definition:

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. On the **Metadata Rules** card, click **Add New**, and then select **Add Rule Definition** from the menu.

   The Rule Definition page opens.
3. In the **Name** field, enter a name for the rule definition.
4. (Optional) In the **Description** field, enter a description for the rule definition.
5. Under **Rule Criteria**, for **Object is**, select the object type.

   For example, Choosing **File** applies the rule definition at the file level. Choosing **Column** applies the rule definition at the column level.
6. Click **Create a condition** to define the rule’s conditions.

   * Choose **OR** to identify when any condition is satisfied.
   * Choose **AND** to identify when all conditions are satisfied.
   * For **Attribute**, select the attribute that you want to use to target the action.

     Only business terms and custom properties already created in Data Catalog are available.
   * For **Operator**, select the operator that you want to use.

     Available operators depend on the selected **Attribute**.
   * For **Value**, select the value you want to use.

     Available values vary based on the chosen **Operator**.
   * (Optional) Click **Add Group** to nest a query when performing multiple **AND** operations on the same attribute, or to create other complex queries.

   You can expand the **Query JSON** section to view the JSON code that was created as the result of your settings, or you can click **Copy Link** to copy the pseudo code.
7. For **Add Action**, select an action. Depending on the action you select, you might see additional fields.

   For example, if you select **Start Process**, you must select the process to start.

   **Important:** The **Move**, **Delete**, and **Rehydrate** options for **Start Process** are available only if you have a license for Data Optimizer and permission to use it. In addition, all involved data sources must have the **Available for Migration** setting **Enabled**. The **Rehydrate** operation is only supported for HDFS data sources when using metadata rules.

   **Note:** The order of the actions does not matter. For example, on the Rule Definition page, an action to apply a tag can be located below an action that moves the data. However, if there is a delete action, other actions on the same data are skipped and an error message displays.
8. When you are finished defining the action, click **Save**.

   The rule definition is saved, and a status message appears in the upper corner of the page.
