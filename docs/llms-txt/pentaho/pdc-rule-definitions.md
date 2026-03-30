# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-use-rules/pdc-rule-definitions.md

# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/pdc-manage-metadata-rules-cp/pdc-rule-definitions.md

# Rule definitions

Rule definitions specify the criteria and actions performed by a rule.

On the left navigation menu, click **Data Operations**. On the **Metadata Rules** card, click **Definitions** to open the **Rule Definitions** table on the Manage Metadata Rules page.

![Manage Metadata Rules page](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-5f5da0cdddd5bb12385f0b41e1e570a38145b70d%2FPDC%20Manage%20Metadata%20Rules%20page.png?alt=media)

The information in the **Rule Definitions** table is described below.

<table><thead><tr><th width="140.66656494140625" align="center">Column</th><th>Description</th></tr></thead><tbody><tr><td align="center"><strong>Rule Definition</strong></td><td>The name of the rule definition.</td></tr><tr><td align="center"><strong>Description</strong></td><td>The description of the rule definition.</td></tr><tr><td align="center"><strong>Created By</strong></td><td>The creator of the rule definition.</td></tr><tr><td align="center"><strong>Rule Type</strong></td><td>The type of rule definition.</td></tr><tr><td align="center"><strong>Applied Rule</strong></td><td>Shows whether the rule definition was applied.</td></tr><tr><td align="center"><strong>State</strong></td><td><p>Controls the state of the rule definition:</p><ul><li>Click <strong>Enable</strong> to enable the rule definition for use.</li><li>Click <strong>Disable</strong> to disable the rule definition.</li></ul></td></tr><tr><td align="center"><strong>View</strong></td><td>Click to view the rule definition.</td></tr><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media" alt="" width="9"></p></td><td><p>The <strong>More options</strong> icon:</p><ul><li>Click and choose <strong>Edit</strong> to edit the rule definition.</li><li>Click and choose <strong>Delete</strong> to delete the rule definition.</li></ul></td></tr><tr><td align="center"><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-f7656d79ccf70697b6a1558e0afb87566dbe4651%2FPDSO%20Delete%20icon.png?alt=media" alt="" width="18"></p></td><td>The <strong>Delete</strong> icon. Click to delete a rule definition.</td></tr></tbody></table>

Click **Import Rule Definition** or **Export Rule Definition**, respectively, to import or export a rule definition. See the following topics when importing or exporting rule definitions:

* [Import rule definitions](#import-rule-definitions)
* [Export rule definitions](#export-rule-definitions)

Click **Add Rule Definition** to add a new rule definition. See the following topics when working with rule definitions:

* [Create a rule definition](#create-a-rule-definition)
* [Edit a rule definition](#edit-a-rule-definition)
* [Delete a rule definition](#delete-a-rule-definition)

## Create a rule definition

You create rule definitions to specify the criteria used and actions performed by a rule.

Perform the following steps to create a metadata rule definition:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
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

## Edit a rule definition

You can edit an existing rule definition if necessary.

Perform the following steps to edit a rule definition:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Definitions**.

   The Rule Definitions tab opens.
3. Locate the name of the rule definition that you want to edit, then in its row click **More options** (![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media)) and select **Edit**.

   The rule definition opens.
4. Edit the fields as needed.
5. Click **Save**.

The rule definition is saved with your changes, and a status message appears in the upper corner of the page.

## Delete a rule definition

You can delete a rule definition that is no longer needed. You can only delete rule definitions that are not currently being used by a metadata rule.

Perform the following steps to delete a rule definition:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Definitions**.

   The Rule Definitions tab opens.
3. Locate the name of the rule definition that you want to delete and select its check box.
4. Click **Delete**.

   If the rule definition you are trying to delete is attached to a metadata rule, the rule definition cannot be deleted, and you get a notification asking you to unlink the definition from all associated metadata rules before you can proceed.

The rule definition is deleted, and a confirmation message appears in the upper corner of the page.

## Import rule definitions

You can import rule definitions into the Data Catalog environment in JSON format.

By using the import rule definition feature, you can apply standard rule definitions across multiple Data Catalog environments or migrate rules from testing or staging to production without manually recreating each one, saving time and reducing errors.

Perform the following steps to import rule definitions.

Ensure you have a JSON file that contains all details of rule definitions. If you are migrating from different Data Catalog instances, you can export rule definitions in a JSON file containing. For more information, see [Export rule definitions](#export-rule-definitions).

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Definitions**.

   The **Rule Definitions** tab opens.
3. Click **Import Rule Definition**.

   The **Import Rule Definitions** dialog box opens.
4. Upload the JSON file containing the rule definition details and click **Upload**.

The rule definition is imported and appears in the Rule Definitions list.

You can export the rule definitions from Data Catalog. See [Export rule definitions](#export-rule-definitions) for more information.

## Export rule definitions

You can export existing rule definitions from Data Catalog in JSON format for backup purposes, to save the rule configurations and restore them if necessary.

Additionally, you can share metadata rule definitions across teams or environments.

Perform the following steps to export a rule definition:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Definitions**.

   The **Rule Definitions** tab opens.
3. Click **Export Rule Definition**.

   This downloads the file containing the rule definition details in JSON format.

You have successfully exported the rule definitions.

You can import the rule definitions into Data Catalog. See [Import rule definitions](#import-rule-definitions) for more information.
