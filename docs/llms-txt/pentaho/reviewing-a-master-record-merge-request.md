# Source: https://docs.pentaho.com/pentaho-data-mastering/transforming-master-records-into-golden-records/reviewing-a-master-record-merge-request.md

# Reviewing a Master Record merge request

Review merge requests for Master Records to verify that the edits made by the data steward to resolve match or merge conflicts are sufficient. After reviewing a merge request, you can approve or reject the merge request. When you approve a merge request, the Master Record is transformed into a Golden Record. When you reject a merge request, the Master Record is returned to the data steward for further edits.

You must have data reviewer privileges to review a merge request and approve or reject the edits made by the data steward.

Perform the following steps to review a merge request and approve or reject the request:

1. On the left navigation menu, click **Master Data**. The **Master Data** page opens with the Master Records listed in a table.
2. Click the **In Review** tab to view the Master Records that have the **In Review** status.
3. At the end of the edited Master Record row that you are reviewing, click the down-arrow icon to view change details.
4. Review the change details to determine whether you should accept or reject the merge request.
5. At the end of the edited Master Record row that you are reviewing, click the more actions icon and take one of the following actions:

| **Accept the merge request** | Complete the following steps to accept the merge request:1. Click **Accept Merge**. 2. In Accept Merge confirmation dialog box, enter a comment about accepting the merge request. 3. Click **Create Golden Record**. The Master Record is transformed into a Golden Record.           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reject the merge request** | Complete the following steps to reject the merge request:1. Click **Reject Merge**. 2. In Reject Merge confirmation dialog box, enter a comment about rejecting the merge request. 3. Click **Reject Merge**. The Master Record is sent back to the data steward for additional edits. |

The record status is changed from the \*\*To Review\*\* status to either the \*\*Accepted\*\* status or the \*\*Rejected\*\* status, based on your choice. The record is moved from the \*\*In Review\*\* tab to either the \*\*Accepted\*\* tab or \*\*Rejected\*\* tab.

```
**Note:** Golden Records in the **Accepted** tab are moved to the **Golden Record** tab the next time the Mastering Engine runs.
```
