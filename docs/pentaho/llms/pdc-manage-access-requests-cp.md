# Source: https://docs.pentaho.com/pdc-admin/pdc-manage-access-requests-cp.md

# Manage access requests

If you are the assigned administrative user for Pentaho Data Catalog access requests, you can manage requests to access metadata and data in Data Catalog.

Users can request access for a limited or an unlimited time, and can request access to metadata or data. Metadata access is managed at the root level, not at the column level or below.

If your organization has configured an external ticketing system (such as Jira or ServiceNow) for managing data requests, all data access requests are forwarded to the external ticketing system, and only metadata requests are managed within Data Catalog.

See the following table for details on the process flow for different types of access requests:

| When…                                                                       | then…                                                                                  | and:                                                                   |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| A user requests metadata access                                             | you can approve or reject the request                                                  | the user receives an email that their request is approved or rejected. |
| A user requests access for a limited time                                   | access is automatically revoked when the time has expired                              | the user receives an email that their access is revoked.               |
| A user no longer needs access to the resources or has left the organization | You can revoke the user’s access                                                       | the user receives an email that their access is revoked.               |
| **When…**                                                                   | **and…**                                                                               | **then:**                                                              |
| A user requests data access                                                 | an external ticketing system such as Jira or ServiceNow is configured to work with PDC | the request is sent to the external ticketing system.                  |
| there is not an external ticketing system configured to work with PDC       | the data access request fails.                                                         |                                                                        |
| An administrator requests any kind of access                                | the request is in Pending status                                                       | you can edit or cancel the request.                                    |

See also **Requesting access** in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ "mention")for information on a non-administrative user’s request access process flow.

## Viewing access requests

Users with administrative permissions can view, filter, and search access requests in Pentaho Data Catalog that are in any status. Non-administrative users can only see their own access requests.

To view access requests, click **Management** in the left navigation menu, then on the **Request Access** card, click **View Requests**. A sample Request Access page is shown below.

**Note:** This example shows all the requests in the system, which only an administrator can view.

![Request Access page with numbered areas](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-c70f82b87c924427d171faa9fc06b6468c9e45c4%2FPDC%20Req%20Acc%20page%20with%20callouts.png?alt=media)

The following table describes the numbered areas and their functions:

<table><thead><tr><th width="122.33331298828125">Screen area</th><th width="615.333251953125">Description</th></tr></thead><tbody><tr><td>1</td><td>The top menu bar of every page has an <strong>Access Request</strong> icon that you can click to go directly to the <strong>Request Access</strong> form.</td></tr><tr><td>2</td><td>At the top of the Request Access page is the <strong>Create New Request</strong> button, which opens the <strong>Request Access</strong> form.</td></tr><tr><td>3</td><td>The <strong>Latest access requests</strong> section shows the most recent access requests, and is closed by default. Click the down arrow to expand it. This example shows it open with the latest requests.</td></tr><tr><td>4</td><td>Below the <strong>Latest access requests</strong> section are cards for each request status. You can filter the access requests by clicking on a card. In this example, the <strong>Approved</strong> card is selected, and three access requests are shown on the <strong>All</strong> tab in the table. You can click the <strong>My Requests</strong> or <strong>Requests to me</strong> tabs to filter the requests in the table.</td></tr><tr><td>5</td><td>You can search the requests by entering a keyword in the <strong>Search in requests</strong> field. If you click the Filter icon, a field opens on the columns you can filter, where you can type a keyword or select an option, such as a <strong>Priority</strong> level.</td></tr><tr><td>6</td><td>When you click the <strong>Settings</strong> icon, the Filter Columns window opens. You can select the checkboxes of the columns you want to display, and with your cursor on the <strong>Drag</strong> icon, drag the column names into the order you want them to display.<br><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2FQ5ZHaYLq6pwAFJnHoWuL%2Fimage.png?alt=media&#x26;token=d1d72b72-1e9e-48e8-870d-c1854d4b7937" alt=""></td></tr><tr><td>7</td><td>The checkbox for one approved request is selected and the cursor is on the only available action for this request, <strong>Revoke</strong>. You can select checkboxes for more than one request, to act on more than one request at a time. You can also scroll and page through the requests in the table.</td></tr><tr><td>8</td><td>Each request in the table has a View icon for viewing the details of the request.When you click the More actions icon, you see the available actions for the corresponding request. In this example, the available action is <strong>Revoke</strong>.<br><img src="https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fd8LjAhqBGfCJNTtds64j%2Fimage.png?alt=media&#x26;token=aab9b287-343b-44ae-9e20-c46ffba48d1f" alt=""></td></tr></tbody></table>

## Approve an access request

Users with Pentaho Data Catalog administrative permissions can approve one or more access requests.

**Note:** If your deployment of Data Catalog has an external ticketing system such as Jira or ServiceNow integrated for processing data access requests, you can only approve metadata access requests from Data Catalog. Data access requests are routed to the external ticketing system.

Use the following steps to approve an access request:

1. In the left navigation menu, click **Management**.
2. On the **Request Access** card, click **View Requests**.

   The Request Access page opens.
3. Click the **Pending** card.

   The **All** tab shows the Pending requests.
4. Select the checkbox for one or more access requests to approve, and click **Approve**.

   You see a confirmation message.
5. Click **Approve**.

One or more access requests are approved, and each user is notified by email.

## Reject an access request

Users with Pentaho Data Catalog administrative permissions can reject one or more Pending access requests.

Use the following steps to reject an access request:

1. In the left navigation menu, click **Management**.
2. On the **Request Access** card, click **View Requests**.

   The Request Access page opens.
3. Click the **Pending** card.

   The **All** tab shows the Pending requests.
4. Select the checkbox for one or more access requests to reject, and click **Reject**.

   You see a confirmation message.

One or more access requests are rejected, and each user is notified by email.

## Revoke access

Users with Pentaho Data Catalog administrative permissions can revoke one or more Approved access requests.

Use the following steps to revoke access:

1. In the left navigation menu, click **Management**.
2. On the **Request Access** card, click **View Requests**.

   The Request Access page opens.
3. Click the **Approved** card.

   The **All** tab shows the Approved requests.
4. Select the checkbox for one or more access requests to revoke, and click **Revoke**.

   You see a confirmation message.

One or more access requests are revoked, and each user is notified by email.
