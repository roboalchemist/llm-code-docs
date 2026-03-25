# Source: https://docs.axonius.com/docs/monitoring-third-party-tickets.md

# Monitoring Third-Party Tickets

You can track the progress of tickets created in third-party ticketing systems (for instance, ServiceNow) using Enforcement Actions, directly from Axonius.

<Callout icon="📘" theme="info">
  Note

  This article describes how to monitor third-party tickets per asset. You can also monitor all third-party tickets opened for all assets in the system from the [**Tickets** asset page](/docs/tickets-1).
</Callout>

When you use an Enforcement Action to create a ticket in a third-party ticketing system (see [Create Incident Category](/docs/risk-score)), the unique Ticket ID and other ticket information is saved in the **Linked Tickets** complex field on each asset that is linked to the ticket/incident. You can present these attributes of the **Linked Tickets** complex field in a table in the Asset Profile of the relevant asset, by opening one of the following:

* The [**Tickets** tab on the Asset Profile page](/docs/asset-profile-page#tickets-tab). Ticket information in this table is constantly updated.
* [**Tables> Linked Tickets**](/docs/asset-profile-page-complex-fields#linked-tickets) in the left navigation pane (by clicking the **Linked Tickets** complex field in the Asset Profile). Ticket information in this table is updated in cycles.

For example, you can run a **Create Incident** enforcement action to open tickets on all devices that have a vulnerability (Security Finding) for at least two months but with no remediation activity. You can then check the status of the ticket on each device in the Tickets tab of the device’s asset profile.

In order to track tickets, the **Fetch EC Action ticket updates** option in the Advanced Configuration of the relevant adapter (for instance, ServiceNow) must be enabled (the default), so that the adapter can fetch tickets created by Axonius users and get updates on the tickets.
The relevant adapter periodically fetches data (according to adapter scheduling) on each third-party ticket opened in Axonius, and updates their ticket data in the Tickets table of each relevant asset, enabling you to track the progress of the third-party tickets from within Axonius.

You can update the information on the tickets that were opened on an asset by doing one of the following:

* Run an Update Ticket enforcement action (such as Jira Service Management - Update Tickets) on assets that match a query, provided that such an enforcement action has been defined for the third-party vendor where you opened the ticket.
* Run the same Create Ticket/Incident enforcement action, which was used to create the original ticket, on the asset for which the ticket was created and update the last, all, or specific tickets linked to that asset.

<Callout icon="📘" theme="info">
  Note

  When an asset is deleted from Axonius, its tickets are also removed.
</Callout>

## Tickets Overview

The **Tickets** tab in the [Asset Profile page](/docs/asset-profile-page) displays a list of all tickets linked to the asset in the Axonius system, sorted from the newest to the oldest ticket.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TicketsTabinAssetProfile.png)

The Tickets table lists ticket details, including:

| Ticket Information | Description                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Ticket Vendor**  | The logo of the third-party vendor adapter where the ticket was created using the Enforcement Action.                                                  |
| **Ticket ID**      | A unique ID assigned when the ticket is created by the EC action. The adapter fetches from the vendor information on the ticket identified by this ID. |
| **Summary**        | The short Incident/Ticket title taken from the EC action definition.                                                                                   |
| **Status**         | The status of the ticket at the vendor.                                                                                                                |
| **Reporter**       | The name of the customer who created the ticket. This information exists, if supplied by the vendor.                                                   |
| **Created**        | The date and time in UTC time that the Enforcement Action created the incident/ticket.                                                                 |
| **Updated**        | The date and time in UTC time that the incident/ticket was updated in Axonius.                                                                         |
| **Description**    | A description of the Incident/Ticket. Taken from the Enforcement Action that created the incident/ticket.                                              |

### Changing the Order Columns are Displayed

You can change the order of columns displayed.
Drag and drop columns on the table to arrange them in the order that you want. The changes are only for the current session.

## Searching and Filtering

You can filter the tickets that are displayed.

The following filters are available:

* **Search** - Displays tickets with the specified search text.
* **Vendor** - Displays tickets opened at one or more specific vendors of third-party ticketing systems.
* **Status** - Displays tickets of one or more specific statuses.
* **Reporter** - Displays tickets opened by one or more specific customers.
* **From**, **To** - Displays tickets that were created in this date range.

### Filtering by Date

You can filter tickets by a specific day or date range using the date picker.

**To filter the display by tickets created on a specific date**

1. Click **Display by Date** above the Tickets table. The date picker only enables selecting dates on which tickets were created.
2. Select one of the enabled dates.

To learn more, refer to [Displaying Historical Data](/docs/asset-profile-page#displaying-historical-data).

**To filter the display by date range**

1. Click the **From - To** filter.
2. Select From and To dates. To filter results only for a specific date, select the same date twice.
3. If you want to include specific times in the date range, click **Select Time** in the date range picker.
4. Click **OK** to set the filter.

### Resetting Filters and Searches

You can clear a specific filter or reset all filters.

* Click **Clear All** to clear all selections in a specific filter.
* Click **Reset**  from the top right of the Tickets page to clear the search text and all filters, and display all the tickets.

## Tickets Retention

The Tickets page always displays the last 100,000 tickets.

## Exporting Tickets

You can export the tickets results table data to a CSV file.

**To export the results to a CSV file:**

* In the **Tickets** page, on the right side above the table, click **Export CSV** .
  The CSV file is automatically downloaded with a name format as:
  `axonius_entity_<entity#>_tickets< date >< time >.csv`

When you set a filter, only the filtered data is exported to the CSV file.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).