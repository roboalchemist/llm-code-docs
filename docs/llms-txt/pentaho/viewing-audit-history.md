# Source: https://docs.pentaho.com/pentaho-data-mastering/viewing-history/viewing-audit-history.md

# Viewing audit history

View the audit history of Master Records to verify that the information in the record is correct and to determine whether you must take an action to process the Master Record.

The Audit History page contains information to help you trace records, such as the **Golden Record Key** and the **Source Application Identifier**. Merged records information can also be viewed in the Audit History page.

You must have admin privileges to view the audit history.

Perform the following steps to view the audit history:

1. On the left navigation menu, click **Master Data**.

   The Master Data page opens with the Master Records listed in a table.
2. Select the **Audit** tab. The Audit History page appears with the following fields:

   | Field             | Description                                                                                                                                     |
   | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   | Golden Record Key | A unique alphanumeric value to identify a Golden Record.                                                                                        |
   | Master Record ID  | A unique number to identify the Master Record.                                                                                                  |
   | Last Updated      | Date and time of the most recent modification to the Master Record.                                                                             |
   | Last Updated By   | Name of the user who last modified the Master Record.                                                                                           |
   | Action            | Action performed by the user while modifying the Master Record (for example: create, change status, or delete).                                 |
   | Comments          | Comments entered by the user.                                                                                                                   |
   | Status            | Current status of the Master Record. The status of a Master Record can be **Draft**, **Accepted**, **In Review**, **Rejected**, or **Removed**. |
3. At the end of a Master Record row, click the more actions icon and select **View Details**.

   The Master Record page opens and shows Master Record, Golden Record, and source record details.
4. Review the details for the Master Records, Golden Records, and source records.
5. Click the **Audit** tab to return to the Audit History page.
6. At the end of the audit history record row, click the down-arrow icon.

   Information about Golden Records and merged records is shown, which includes, but is not limited to, the values in **Golden Record Table Key** column, **Source Record Table Key** column, and the **Source Application Identifier** column.
7. Review the information about the Golden Records and merged records.
