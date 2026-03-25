# Source: https://docs.pentaho.com/pentaho-data-mastering/transforming-master-records-into-golden-records/determining-status-of-master-records.md

# Determining status of Master Records

View the list of Master Records to determine that status of Master Records, including which records must be edited to resolve match or merge conflicts.

You must have data steward privileges to edit Master Records.

Perform the following steps to determine the status of Master Records:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens with the Master Records listed in a table.
2. Click one of the following tabs to view Master Records that have the corresponding status:
   * **Draft:** Master Records with match or merge conflicts that a data steward must edit to resolve, and then submit for review as a merge request. Match and merge conflicts are found during data curation. **Draft** is the default status assigned to Master Records when the records are created.
   * **In Review:** Master Records with a pending merge request that a reviewer must evaluate to determine whether those Master Records can be transformed into Golden Records. The reviewer evaluates only the Master Records that have the **In Review**status.
   * **Accepted:** Master Records with an approved merge request. Accepted Master Records are transformed into Golden Records.
   * **Rejected:** Master Records with a merge request that was rejected by the reviewer. Rejected Master Records are sent back to the data steward for additional edits.
3. In the tab that you selected, at the end of a Master Record row, click the more actions icon and select **View Details**. The Master Record details, along with Golden Record and source record information, are shown.
