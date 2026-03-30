# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/pdc-manage-business-rules-cp.md

# Manage business rules

Define business rules to manage your data and ensure its quality. These rules allow you to set particular guidelines to measure the quality of your data by determining whether it meets specific standards and regulations. By defining these business rules, you can make sure that your organization's data is accurate, consistent, and reliable.

Business rules are used for JDBC data sources, and run on the actual data. On the Business Rules page, you can create, update, edit, and delete rules.

Your role determines your ability to create or execute rules. See the [Default user roles and permissions](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-user-roles-and-permissions#default-user-roles-and-permissions) section in [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/) document for more information.

## Create a rule

Perform the following steps to create a new rule. After you create a rule, you can configure it using [Configure a rule](https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/broken-reference).

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Business Rules** card, select **Business Rules**.

   The Business Rules page opens.
3. Click **Add Business Rule**.
4. In the Create Business Rule page, enter the following information.

<table><thead><tr><th width="179.5555419921875">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Business Rule Name</strong> (Required)</td><td>Enter the unique name of the rule that your users will recognize. Names must start with a letter, and contain only letters, digits, hyphens, or underscores. White spaces are supported, but trailing spaces are not allowed in names.</td></tr><tr><td><strong>Description</strong></td><td>Enter a description for this rule. For example, you may want to indicate the purpose of the rule to assist other users.</td></tr><tr><td><strong>Note</strong></td><td>Enter additional comments for the rule. For example, you may want to describe the workflow or use case of the rule.</td></tr><tr><td><strong>Custom Tags</strong></td><td>Add specific keywords or labels to categorize and easily search for the business rule.</td></tr><tr><td><strong>Rule Enabled</strong></td><td>By default, a new rule is enabled. Clear the check box to disable the rule. When a Rules Execution job is run, disabled rules are skipped and are not evaluated.</td></tr><tr><td><strong>Rule Approved</strong></td><td>Select to approve the rule. This option is only available to users with the applicable permissions.</td></tr></tbody></table>

5\. Click **Create Business Rule** to save your rule.

6. In the confirmation window, click **Configure** to [Configure a rule](https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/broken-reference) or click **Close** to configure it later.

## Configure a rule

After you create a business rule, you can configure it in the **Configuration** view of the Business Rule page. This task assumes you have completed [Create a rule](https://docs.pentaho.com/pdc-admin/pdc-manage-rules-cp-ag/broken-reference) and are on the Business Rules page.

1. Locate the business rule you want to configure in the table of rules and select the **View Details** button (**>**) in its row.

   **Note:** If you have a large number of rules, select **Show Filters** to help you find the rule you want to edit.

   The Business Rules page opens to the **Details** view for the selected rule.
2. (Optional) Click **Configuration** tab and select the **Business Rule Type**.

   The business rule type helps you differentiate between rules.
3. (Optional) Select the **Data Quality Dimension** to differentiate between different quality rules that you create. Options are Accuracy, Uniqueness, Consistency, Timeliness, Conformity, Completeness, and Validity.
4. Set the schedule to run the business rule, select one of the following schedules:
   * **Daily**
   * **Weekly**
   * **Monthly**
5. Set the rule scope and condition:

   1. Select resources on which you want the rule to be evaluated and applied. Select the target table or column.
   2. Define the rule's condition for evaluation using the SQL query. Write an SQL query to identify non-compliant data by returning rows that do not match compliant rows and the scope count.

      In the following SQL example Customer table is selected to identify the customers with missing fax numbers.

      ```
      SELECT 
      	count(*) total_count,
      	count(c."Fax") scopeCount,
      	SUM(CASE 
      		WHEN c."Fax" isnull THEN 1
      		ELSE 0
      	END) nonCompliant
      FROM chinook."Customer" c
      ```

   `total_count`: The total number of rows in the Fax column in the Customer table.

   `scopeCount`: The number of customers with a fax number value in the Fax column.

   `nonCompliant`: The number of customers missing the value in the Fax column.
6. In **Configure Rule Actions**, click **Add Action**, to add actions like **Set Status**, **Apply Tags**, and **Webhook**

   Set the threshold at either a percentage or a specified row count and add the following action

   * **Set Status:** Set thresholds for PASS, WARNING, and FAIL status.
   * **Apply Tags**: If the threshold is met, the tags are applied to the resource.
   * **Webhook:** Configure an external system capable of receiving HTTP requests. If the condition is met, the external system will receive a notification.
7. If the rule configuration values are entered correctly, click **Save Changes**.

   If there is a problem while saving your rule, an error message appears indicating the problem. Fix the problem and save changes.
8. To execute the rule, click **Run Now** at the top right of the page.
9. You can monitor the progress on the **Workers** page.

Your created and configured business rule appears on the Business Rules page.

Select the rule if you want to view execution details, run, edit, or remove the rule.

## Update a rule

If you have already created and configured a rule, you can edit it from the Business Rules page.

Perform the following steps to edit a rule:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Business Rules** card, select **Business Rules**.

   The Business Rules page opens.
3. Locate the business rule you want to configure in the rules table and select the **View Details** button (**>**) in its row.

   If you have a large number of rules, select **Show Filters** to help you find the rule you want to edit.

   The Business Rule page opens to the **Details** view for the selected rule.
4. Edit the fields as needed in the **Details** and **Configuration** views.
5. Click **Save Changes**.

   The rule is saved with your changes. If there is a problem while creating your rule, an error notification will be displayed at the top of the page. Resolve the error and click **Save Changes**.

## Delete a rule

If a rule is no longer needed, you can delete it. Perform the following steps to delete a rule:

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Business Rules** card, select **Business Rules**.

   The Business Rules page opens.
3. Click **Management** on the menu bar to open the Manage Your Environment page, and then select **Business Rules**.

   The Business Rules page opens.
4. Use the check box to select the rule you want to delete.
5. Click **Remove**.
6. In the confirmation message window, click **Remove** to delete the rule.

## View rule execution information

You can access and view rule execution from the **Business Rules** page and the **History** page.

On the **Business Rules** page, you can find a list of all the rules that have been set up in the system. The list includes information about each rule, such as its name, description, execution status, and so on.

On the **History** page, you can view the information of the specific rule. This helps you to keep track of the status of the rule.

Perform the following to access the **Business Rules** page and the **History** page.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. On the **Business Rules** card, select **Business Rules**.

   The Business Rules page opens with a list of all the rules set up in the system.
3. Locate the business rule to view details of a specific business rule and select the **View Details** button (**>**) in its row.

   If you have a large number of rules, select **Show Filters** to help you find the rule you want to edit.

   The Business Rules page opens to the **Details** view for the selected rule.
4. To view information on the selected rule, click the **History** tab, and then select the **View Details** button (**>**) in the row.

   The **View Details** page opens.\
   ![Rule details](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-20522a594c99187f23c63c074fd1747aaa56ba67%2FPDC_Business_Rule_Details.png?alt=media)

## Creating a rule group and assigning rules to a group

To organize the business rules, you can create a rule group and add your rules. This helps you keep your rules organized and easily accessible.

1. In the left navigation menu, click **Data Operations**.

   The Manage Data Operations page opens.
2. Select **Rules Group**.

   The Business Rules Group page opens.
3. Enter the `Rule group name`, `Description`, and `Note`.
4. Set the schedule to run all the business rules in a group, and select one of the following schedules: **Daily**, **Weekly**, and **Monthly**.
5. Click **Assign Rules**, select the rules you want to add to a group, and then click **Assign**.
6. Click **Save Changes**.
