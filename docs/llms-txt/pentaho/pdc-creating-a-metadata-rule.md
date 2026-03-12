# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-use-rules/pdc-metadata-rules/pdc-creating-a-metadata-rule.md

# Creating a metadata rule

You create metadata rules to execute rule definitions on a selected data source.

Perform the following steps to create a new metadata rule.

**Note:** If you create a rule with a rule definition that contains a Delete operation, you get a message that since a Delete operation is configured, all other configured operations will be ignored.

1. Click **Management** in the left navigation menu.

   The Manage Your Environment page opens.
2. On the **Metadata Rules** card, click **Add New**, and then select **Add Rule** from the menu.

   The Add Rule page opens.
3. Enter the **Rule Name**.
4. In **Select Rule Definition**, select the rule definition if you have already created it, or click **Create Rule Definition** to create a rule definition. See [Creating a rule definition](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-management/pdso-use-rules/pdc-rule-definitions/pdc-creating-a-rule-definition) for more information.
5. Select one or more **Source Data Assets** and click **Apply**.

   If the rule definition you selected has **Migrate** or **Move** as a process, you see an additional field, **Destination Data Asset**.
6. (Optional) Select the **Destination Data Asset**.

   You can select a destination data source that is:

   * not the same as the Source data source
   * supported for migration by Data Optimizer and enabled for migration (the **Available for Migration** setting for the data source is **Enabled**)**Note:** If you use an HDFS data source as a source, the **Destination Data Source** field does not appear, because the destination is internally configured in the HDFS cluster.
7. (Optional) Select the **Run rule definition now** checkbox to immediately execute the new rule definition.
8. (Optional) Select **Add Schedule** to set a frequency or a specific time and day to run the metadata rule.
9. Click **Apply**.

   **Note:** Since multiple rules can run simultaneously, if a rule is already running on the Source data source, any additional rule intended for the same data source waits until the running rule finishes. The waiting rule remains in the CREATED state until the running rule finishes, after which the waiting rule can start.

   The metadata rule is created and a confirmation message appears in the upper corner of the page.

To check the progress of the metadata rule, click the **History** tab to view the status.
