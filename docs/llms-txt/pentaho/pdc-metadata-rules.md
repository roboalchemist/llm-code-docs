# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-use-rules/pdc-metadata-rules.md

# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/pdc-manage-metadata-rules-cp/pdc-metadata-rules.md

# Metadata rules

Metadata rules execute rule definitions on a selected data source.

On the left navigation menu, click **Data Operations**. On the **Rules** on the card, click **Metadata Rules** to open the Manage Metadata Rules page.

![Metadata rules table](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-0b4fa928f324fea4919873acc644f90952ea6c73%2FPDC%20Metadata%20rules%20tab.png?alt=media)

The information in the **Metadata Rules** table is described below.

<table><thead><tr><th width="157.3333740234375">Column</th><th>Description</th></tr></thead><tbody><tr><td><strong>Metadata Rule</strong></td><td>The name of the metadata rule.</td></tr><tr><td><strong>Datasource</strong></td><td>The name of the data source.</td></tr><tr><td><strong>Rule Type</strong></td><td>The type of metadata rule.</td></tr><tr><td><strong>Owner</strong></td><td>The creator of the metadata rule.</td></tr><tr><td><strong>Last Run</strong></td><td>The date and time of the last execution of the metadata rule.</td></tr><tr><td><strong>Schedule</strong></td><td>The scheduled time for the metadata rule’s execution if applied.</td></tr><tr><td><strong>Details</strong></td><td><p>Click <strong>View</strong> to open the configuration and history of the metadata rule:</p><ul><li>The <strong>Configuration</strong> tab lists the metadata rule name, data source asset, and rule definition, and allows you to select <strong>Run rule definition now</strong> for immediate execution.</li><li>The <strong>History</strong> tab lists previous rule executions including the data source, start time, elapsed time, and the status, The tab allows you to select <strong>Terminate</strong> to disable the rule, or click <strong>Statistics</strong> to view the success and failure details of the operation.</li></ul></td></tr><tr><td><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media" alt="" width="14"></p></td><td><p>The <strong>More options</strong> icon:</p><ul><li>Click and choose <strong>Run</strong> to run the metadata rule.</li><li>Click and choose <strong>Edit</strong> to edit the metadata rule.</li><li>Click and choose <strong>Delete</strong> to delete the metadata rule.</li></ul></td></tr><tr><td><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-d79840076cb12462d477d00b09a7416ed18be18e%2FPDSO%20Run%20icon.png?alt=media" alt="" width="21"></p></td><td>The <strong>Run</strong> icon. Click to execute the selected metadata rule.</td></tr><tr><td><p><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-f7656d79ccf70697b6a1558e0afb87566dbe4651%2FPDSO%20Delete%20icon.png?alt=media" alt="" width="27"></p></td><td>The <strong>Delete</strong> icon. Click to delete the selected metadata rule.</td></tr></tbody></table>

Click **Add Rule** to add a new metadata rule. See the following topics when working with metadata rules:

* [Create a metadata rule](#create-a-metadata-rule)
* [Running a metadata rule](#running-a-metadata-rule)
* [Edit a metadata rule](#edit-a-metadata-rule)
* [Delete a metadata rule](#delete-a-metadata-rule)

## Create a metadata rule

You create metadata rules to execute rule definitions on a selected data source.

Perform the following steps to create a new metadata rule.

**Note:** If you create a rule with a rule definition that contains a Delete operation, you get a message that since a Delete operation is configured, all other configured operations will be ignored.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Add New**, and then select **Add Rule** from the menu.

   The Add Rule page opens.
3. Enter the **Rule Name**.
4. In **Select Rule Definition**, select the rule definition if you have already created it, or click **Create Rule Definition** to create a rule definition. See [Create a rule definition](https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/pdc-rule-definitions#create-a-rule-definition) for more information.
5. Select one or more **Source Data Assets** and click **Apply**.

   If the rule definition you selected has **Migrate** or **Move** as a process, you see an additional field, **Destination Data Asset**.
6. (Optional) Select the **Destination Data Asset**.

   You can select a destination data source that is:

   * not the same as the Source data source
   * supported for migration by Data Optimizer and enabled for migration (the **Available for Migration** setting for the data source is **Enabled**)\
     **Note:** If you use an HDFS data source as a source, the **Destination Data Source** field does not appear, because the destination is internally configured in the HDFS cluster.
7. (Optional) Select the **Run rule definition now** checkbox to immediately execute the new rule definition.
8. (Optional) Select **Add Schedule** to set a frequency or a specific time and day to run the metadata rule.
9. Click **Apply**.

   **Note:** Since multiple rules can run simultaneously, if a rule is already running on the Source data source, any additional rule intended for the same data source waits until the running rule finishes. The waiting rule remains in the CREATED state until the running rule finishes, after which the waiting rule can start.

   The metadata rule is created and a confirmation message appears in the upper corner of the page.

To check the progress of the metadata rule, click the **History** tab to view the status.

## Running a metadata rule

Running a metadata rule executes its associated rule definition. You can run a metadata rule immediately after creation, if necessary.

Perform the following steps to run a metadata rule:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Rules**.

   The Manage Metadata Rules page opens.
3. Locate the name of the rule that you want to run and select its check box.
4. Click **Run**.

The metadata rule runs after any current operations compete.

To check the rule’s status, click **View** and select the **History** tab.

## Edit a metadata rule

You can edit an existing metadata rule if needed, to change the rule definition or data source on which it runs.

Perform the following steps to edit a rule:

1. In the left navigation menu, click **Data Operations**.\
   The **Manage Data Operations** page opens.
2. On the **Metadata Rules** card, click **Rules**.\
   The **Manage Metadata Rules** page opens.
3. Locate the name of the rule that you want to edit, then in its row click More options (![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAPCAYAAAAoAdW+AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAAyElEQVQY05XNMW6DUBCE4X/fu4Ip4TI0FFwhFjew7+hHF1dYHCC+gBGSKXjaSWEldoJSZLvRaPazNWfxxwUA6dGHEPiRAcyMeZ4Zx5F5njGzx3TNWS7plJKaptEpJbmkNWcFAHenLEve9nvKssTdAbA1Z0kimBFCwN1xCTN7mrdp4v185jZNWzP1vdq2Ver7rVlVFV3XUVXVP837svBxvXJflm8zAMQYuQwDx8OByzAQY3yW7s6uKKjrml1RbE17MfXb/Prwmj8BZS6aS2X2EjMAAAAASUVORK5CYII=)) and select **Edit**.\
   The metadata rule opens.
4. Edit the fields as needed.
5. Click **Apply**.

The metadata rule is saved with your changes, and a status message appears in the upper corner of the page.

## Delete a metadata rule

You can delete a metadata rule if it is no longer needed.

Perform the following steps to delete a metadata rule:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Metadata Rules** card, click **Rules**.

   The Manage Metadata Rules page opens.
3. Locate the name of the metadata rule that you want to delete, then in its row, click **More options** (<img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-df92ee60a4db655bf59fd4e197fbbcd4fdbde731%2FPDSO%20More%20options.png?alt=media" alt="" data-size="line">) and select its check box.
4. Click **Delete**.

The metadata rule is deleted, and a confirmation message appears in the upper corner of the page.
