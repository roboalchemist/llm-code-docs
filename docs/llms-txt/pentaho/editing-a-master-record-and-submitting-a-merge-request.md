# Source: https://docs.pentaho.com/pentaho-data-mastering/transforming-master-records-into-golden-records/editing-a-master-record-and-submitting-a-merge-request.md

# Editing a Master Record and submitting a merge request

Edit a Master Record to resolve match or merge conflicts and then submit a merge request to a reviewer.

You must have **data steward** privileges to edit a Master Record and submit a merge request.

Perform the following steps to edit a Master Record and submit a merge request:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens with the Master Records listed in a table.
2. Click the **Draft** tab. The list of Master Records with the **Draft** status is displayed in the table.
3. At the end of the Master Record row that you want to edit, click the down-arrow icon. The Master Record and the linked source records are displayed.

   The Master Record row is highlighted at the top and the Source Records are displayed below the Master Record.
4. Edit the Master Record by taking one of the following actions:
   * If a column is blank, click the column and select the appropriate value from a linked source record.
   * If there is a match or merge conflict for the data in the column, modify the column value to resolve the conflict.
5. Insert a comment about the edits that you made to the Maste Record and click **Put In Review**.

   A merge request for the Master Record is submitted to a reviewer, the Master Record status is changed from **Draft** to To Review, and the edited record is removed from the Draft tab and added to the In Review tab.
6. Insert a comment about the changes made and click **Put In Review**.

   The Master Record status is changed from **Draft** to **To Review** and the edited record is removed from the **Draft** tab and added into the **In Review** tab. The merge request for the edited Master Record is now submitted to the reviewer.
