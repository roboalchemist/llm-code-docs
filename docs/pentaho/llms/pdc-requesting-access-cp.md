# Source: https://docs.pentaho.com/pdc-use/pdc-requesting-access-cp.md

# Requesting access

As a Pentaho Data Catalog user, you can request permission for yourself and other users to view, copy, write, and delete metadata or data from tables, schemas, files, and folders. Similarly, you can request metadata request access for published data products. You can request access for a limited or an unlimited time.

Metadata access is managed at the root level, not at the column level or below.

See the following table for details on the process flow for different types of access requests:

| When…                                                                    | then…                                                                                            | and:                                                                           |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| you request metadata access                                              | the assigned administrator receives email that your request is pending and awaiting their action | you and any other users receive email when the request is approved or rejected |
| you request data access                                                  | the request is sent to an external ticketing system such as Jira or ServiceNow                   |                                                                                |
| you request access for a limited time                                    | access is revoked when the time has elapsed                                                      | you and any other users will receive an email notification                     |
| you no longer need access to the resources or have left the organization | an administrator can revoke your access at any time                                              |                                                                                |

| When…                          | and…                             | then:                              |
| ------------------------------ | -------------------------------- | ---------------------------------- |
| you request any kind of access | the request is in Pending status | you can edit or cancel the request |

## Request access

In Pentaho Data Catalog, you can request access to a resource for yourself and other users.

Use the following steps to request access:

1. In the left navigation menu, click **Management**.
2. From the Management page, on the **Request Access** card, click **View Requests**.

   The Request Access page opens.

   **Note:** You can also open the Request Access form by clicking the **Access Request** icon on the top menu bar of any page.
3. Click **Create New Request**.

   The Request Access form opens.
4. In the form that appears, select or enter information for the following fields:

<table><thead><tr><th width="206.22222900390625">Field or button</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>You can change the default name of the request.</td></tr><tr><td>Click <strong>Select item</strong></td><td><p>In the <strong>Select Items</strong> panel, you’ll find two tabs:</p><ol><li><strong>Data Canvas</strong> – Displays all connected data sources. To request access, select the desired data source and click <strong>Apply</strong>.</li><li><strong>Data Product</strong> – Lists all published data products. To request access, select the relevant data product and click <strong>Apply</strong>.</li></ol><p>You can also use the search bar to quickly locate specific items.</p><p></p><p><strong>Note:</strong> If you already selected an item in the Data Canvas or Data Product, the <strong>Select item</strong> button is unavailable.</p></td></tr><tr><td>Access Type</td><td><p>Select <strong>Metadata</strong> or <strong>Data</strong>. </p><p><strong>Note:</strong> For requesting access to Data Product, you need to select <strong>Metadata.</strong> </p></td></tr><tr><td>Permissions</td><td><p>Select the permissions you want, and then click <strong>Apply</strong>.</p><p><strong>Note:</strong> Permission to copy from a resource is paired with the permission to delete.</p></td></tr><tr><td>Requested For</td><td>Select one or more users for which you are requesting access</td></tr><tr><td>Request Priority</td><td>Select a priority. The default is P3.</td></tr><tr><td>Description</td><td>Describe why you would like access.</td></tr><tr><td>Request Access for unlimited time</td><td>Select the checkbox if you want unlimited access or specify a date and time range for the access requested</td></tr></tbody></table>

5\. When you are finished filling out the request, click **Send**.\
You see a confirmation message.

If the request access is Metadata access, the assigned administrative user receives an email that an access request is pending and awaiting their action.

If the request is for data access, the request is sent to an external ticketing system such as Jira or ServiceNow.

When the administrator approves the request, the users for whom you have requested access receive an email stating that the access request has been approved. Users are also notified by email if the request is rejected.

## View access requests

You can view, filter, and search your own access requests in Pentaho Data Catalog.

To view access requests, click **Management** in the left navigation menu, then on the **Request Access** card, click **View Requests**. A sample Request Access page is shown below.

**Note:** This example shows all the requests in the system, which only an administrator can view.

![Request Access page with numbered areas](https://1472315382-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FRAKLVv06oBKpy9VLbw7P%2Fuploads%2Fgit-blob-c70f82b87c924427d171faa9fc06b6468c9e45c4%2FPDC%20Req%20Acc%20page%20with%20callouts.png?alt=media)

The following table describes the numbered areas and their functions:

<table><thead><tr><th width="139.5555419921875" align="center">Screen area</th><th>Description</th></tr></thead><tbody><tr><td align="center">1</td><td>The top menu bar of every page has an <strong>Access Request</strong> icon that you can click to go directly to the <strong>Request Access</strong> form.</td></tr><tr><td align="center">2</td><td>At the top of the Request Access page is the <strong>Create New Request</strong> button, which opens the <strong>Request Access</strong> form.</td></tr><tr><td align="center">3</td><td>The <strong>Latest access requests</strong> section shows the most recent access requests, and is closed by default. Click the down arrow to expand it. This example shows it open with the latest requests.</td></tr><tr><td align="center">4</td><td>Below the <strong>Latest access requests</strong> section are cards for each request status. You can filter the access requests by clicking on a card. In this example, the <strong>Approved</strong> card is selected, and three access requests are shown on the <strong>All</strong> tab in the table. You can click the <strong>My Requests</strong> or <strong>Requests to me</strong> tabs to filter the requests in the table.</td></tr><tr><td align="center">5</td><td>You can search the requests by entering a keyword in the <strong>Search in requests</strong> field. If you click the Filter icon, a field opens on the columns you can filter, where you can type a keyword or select an option, such as a <strong>Priority</strong> level.</td></tr><tr><td align="center">6</td><td>When you click the <strong>Settings</strong> icon, the Filter Columns window opens. You can select the checkboxes of the columns you want to display, and with your cursor on the <strong>Drag</strong> icon, drag the column names into the order you want them to display.</td></tr><tr><td align="center">7</td><td>The checkbox for one approved request is selected and the cursor is on the only available action for this request, <strong>Revoke</strong>. You can select checkboxes for more than one request, to act on more than one request at a time. You can also scroll and page through the requests in the table.</td></tr><tr><td align="center">8</td><td><p>Each request in the table has a View icon for viewing the details of the request.<br>When you click the More actions icon, you see the available actions for the corresponding request. In this example, the available action is <strong>Revoke</strong>.</p><p><strong>Note:</strong> The <strong>Revoke</strong> option is only available to an administrator.</p></td></tr></tbody></table>

## Edit an access request

If your Pentaho Data Catalog access request is Pending, you can edit the request.

Use the following steps to edit an access request:

1. In the left navigation menu, click **Management**.
2. On the **Request Access** card, click **View Requests**.

   The **Request Access** page opens.
3. Click the **Pending** card.
4. At the end of the row for the request you want to edit, click the actions menu and click **Edit**.

   The **Access Request** page opens.
5. Make your changes and click **Save**.

   **Note:** You can also cancel the request from the **Access Request** page.

The request is updated.

## Cancel an access request

If you change your mind after requesting access to items in Pentaho Data Catalog and the request is in Pending status, you can cancel the request. Administrators can also cancel pending access requests.

Use the following steps to cancel an access request:

1. In the left navigation menu, click **Management**.
2. On the **Request Access** card, click **View Requests**.

   The **Request Access** page opens.
3. Click the **My Requests** tab.
4. Select the checkbox next to the request you want to cancel and click **Cancel**.

   The request is canceled.

You receive an email confirming the cancellation.
