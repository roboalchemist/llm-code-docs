# Source: https://docs.axonius.com/docs/tickets-1.md

# Tickets

All tickets opened by Axonius Action Center actions in third-party ticketing systems (for instance, ServiceNow) are recorded in Axonius and linked to assets.
The Tickets page displays all these tickets, enabling you to view their information and track their progress directly from Axonius.

<Callout icon="📘" theme="info">
  Note

  This article describes how to monitor all third-party tickets opened in Axonius. You can also monitor third-party tickets opened for an asset type from the [**Tickets** tab](/docs/asset-profile-page#tickets-tab) or [**Linked Tickets** complex field](/docs/asset-profile-page-complex-fields#linked-tickets) on the Asset Profile page.
</Callout>

You can determine the default table view/filter, as well as additional one-click filters.
Each time adapters fetch updated data about these tickets, the relevant ticket information is updated in the Tickets table.\
You can filter the Tickets table according to Axonius predefined filters, such as **My Open Cases**.
All Ticket fields are queryable and available for Dashboards and Reports as well.

## Required Permissions

You need permissions for **Tickets assets** in order to view this page.

## Opening the Tickets Assets

**To open the Tickets page**

* Click the **Assets** icon  and from the left-pane, expand the **Tickets** item and select **Tickets**.

<Image alt="TicketsPage" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TicketsPage.png" />

The **Tickets** page opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Ticket Fields

There are many fields that you can view and query on the **Tickets** page, including the following:

* **Key** - Display ID.
* **Ticket ID** - A unique ID assigned when the ticket is created by the Enforcement Action. The adapter fetches  information from the vendor on the ticket identified by this ID.
* **Summary** - The short Incident/ticket title taken from the Enforcement Action definition.
* **Status** - The status of the ticket at the vendor.
* **Linked Case** - This field is relevant only if the ticket was created from a Case Set. It displays the name of the Case associated with the Ticket. Clicking the Case name link opens the **Case Management** page with the **Case Details** drawer for that linked Case already open.
* **Case ID** - The identification number of the case associated with the ticket.
* **Reporter** - The reporter of the ticket.
* **Created** - The date and time (in UTC) that the Enforcement Action created the incident/ticket.
* **Updated** -  The date and time (in UTC) of when the incident/ticket was updated in Axonius.
* **Description** - A description of the Incident/ticket taken from the Enforcement Action that created it.
* **Tags** - Tags that have been added to the ticket.

## Creating Queries on Tickets

You can create queries on tickets using one of the following modes:

* **Query Wizard** (the default) - Create a query using the **Query Wizard**,  or in the query bar, selecting a saved query or writing a query.

* **Basic** mode - Create a query by selecting filters.

Use either of these modes to create a unique set of queries. You can query fields such as **Ticket Vendor**, **Key**, **Ticket ID**, **Status**, **Created**, **Updated**, and **Tags**.

Learn more about [how to create Queries using the Query Wizard](/docs/query-wizard-and-query-filter#working-with-the-query-wizard) and [how to create Queries in Basic mode](/docs/basic-query-mode).

The following screen shows how to create a Query using the **Query Wizard** (**Wizard** mode).

<Image alt="QueryTickets" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QueryTickets.png" />

The following screen shows how to create a Query using  **Filters** (**Basic** mode).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BasicFilter.png)

After running the query, the table shows the queried tickets, filtered by the criteria you defined in your query.

## Viewing a Ticket Asset Profile

You can click an individual Ticket asset to see all the data for that particular asset.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TicketAssetPRofile.png)

* For more information, see [Asset Profile Page](/docs/asset-profile-page).
* Refer to [Asset Actions](/docs/devices-actions) for a full description of actions that you can perform on tickets.

The Ticket Profile page includes the following complex fields:

* **Linked Tickets** - Lists other tickets that were opened on the current Ticket asset. Each listed ticket includes its relevant ticket fields.

* **Associated Ticket Devices** - Lists devices directly connected to the current ticket. Each listed device includes its associated device fields.

* **Affected Assets** - List assets impacted by the current Ticket asset. Each listed asset includes its associated asset fields.

Learn about these [complex fields](/docs/asset-profile-page-complex-fields).