# Source: https://docs.pentaho.com/pentaho-data-mastering/transforming-golden-records-into-master-records/rejecting-a-golden-record.md

# Rejecting Golden Records

Reject Golden Records if the records are outdated, require further modification, or must be removed from the application. Rejecting Golden Records transforms the Golden Records into Master Records that can be edited.

You must have data steward privileges to reject Golden Records.

Perform the following steps to reject one or more Golden Records and transform the records into Master Records:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens.
2. Click **Golden Records** tab. The **Golden Records** are shown in a table.
3. Select the checkbox for one or more Golden Records that you want to reject.
4. Click **Selected** > **Reject Golden Records**. The Reject Golden Records confirmation dialog box appears.
5. Insert a comment explaining why you are rejecting the Golden Records and click **Reject Records**.

   The rejected Golden Records are transformed into Master Records and the record status is changed to **Rejected**. The rejected Golden Records are removed from the **Golden Records** table and added to the **Rejected** table.
