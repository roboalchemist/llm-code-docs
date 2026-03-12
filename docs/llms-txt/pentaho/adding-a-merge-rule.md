# Source: https://docs.pentaho.com/pentaho-data-mastering/configuring-merge-rules/adding-a-merge-rule.md

# Adding a merge rule

Add a merge rule to control how matched data from different sources is merged to create Master Records.

You must have admin privileges to add a merge rule.

Perform the following steps to add a merge rule:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the **Merge Rules** card, click **Add Merge Rule**.

   The Create Merge Rule page opens.
3. Specify the following information for the merge rule:

   | Field                          | Description                                                                                                                                             |
   | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Code**\*                     | A unique alphanumeric code to identify the merge rule.                                                                                                  |
   | **Name**\*                     | Name of the merge rule.                                                                                                                                 |
   | **Description**                | Description of the merge rule.                                                                                                                          |
   | **Ignored Values**             | Value specified to replace any missing or null values in the source data.                                                                               |
   | **IF any source values match** | Value to match in the source data.                                                                                                                      |
   | **THEN surviving value**       | Value to use as a replacement when the value that is specified in the **IF any source values match** field is matched in the source data.               |
   | **ELSE surviving value**       | Value to use as a replacement when the value that is specified in the **IF any source values match** field is not matched in the source data.           |
   | **Value Ranking**              | The value with highest score survives as the Master Record value. For example: Circle, 34, Square, 21, Triangle, 55, then Triangle is chosen, if found. |
   | \* Mandatory                   |                                                                                                                                                         |
4. Click **Create Merge Rule**.

   A confirmation message is shown at the top of the page and the merge rule is added to the merge rule table.

   **Tip:** To add multiple merge rules at one time, see [Adding merge rules in bulk](https://docs.pentaho.com/pentaho-data-mastering/configuring-merge-rules/adding-a-merge-rule/adding-merge-rules-in-bulk).
