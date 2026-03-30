# Source: https://docs.pentaho.com/pentaho-data-mastering/configuring-match-rules/adding-a-match-rule.md

# Adding a match rule

Add a match rule to control how Pentaho Data Mastering identifies matches in the data from different data sources

You must have admin privileges to add a match rule.

Perform the following steps to add a match rule:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. In the **Match Rules** card, click **Add Match Rule**.

   The Create Match Rule page opens.
3. Specify the following information for the match rule:

   | Field               | Description                                                                       |
   | ------------------- | --------------------------------------------------------------------------------- |
   | **Priority**\*      | Priority of the match rule in the order of execution for the Mastering Engine.    |
   | **Name**\*          | Name of the match rule.                                                           |
   | **Description**     | Description of the match rule.                                                    |
   | **Scope**\*         | SQL filter definitions that divide the data into subsets for the merge operation. |
   | **Enabled**         | Checkbox that indicates whether a match rule is used by the Mastering Engine.     |
   | **Standalone**      | Checkbox that indicates whether a match rule is standalone.                       |
   | **Review Required** | Checkbox that indicates whether a match rule must be reviewed.                    |
   | **Append Only**     | Checkbox that indicates whether a match rule is only appended.                    |

   \* Mandatory Field
4. Click **Create Match Rule**.

   A confirmation message is shown in the top-right corner of the page and the match rule record is added to the match rule table.

   **Tip:** To add multiple match rules at one time, see [Adding match rules in bulk](https://docs.pentaho.com/pentaho-data-mastering/configuring-match-rules/adding-a-match-rule/adding-match-rules-in-bulk).
