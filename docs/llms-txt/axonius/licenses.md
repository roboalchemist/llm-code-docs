# Source: https://docs.axonius.com/docs/licenses.md

# Licenses

Use the **Licenses** page to see a consolidated view of all Licenses for SaaS applications detected in your organization. Licenses are added automatically using data from your organization's applications. You can also manually add licenses when they are not added automatically; either [one at a time](/docs/licenses#manually-add-licenses) or in bulk via CSV adapter.  The **Licenses** page delivers increased management and oversight over the various SaaS licenses used in your organization.

It can help you understand:

* Utilization of the licenses in your organization
* Which licenses are active
* What are your upcoming renewals
* And more
  Click the **Assets** and from the left-pane, select **Licenses**.

<Image alt="licensesNEWUI.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/licensesNEWUI.png" />

## Overview

The Overview section contains two visual displays of the Licenses in your organization. These charts adjust reflect any query applied to the page.

You can click the Hide Charts icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HideDynamicCharts.png) to hide the graphs in the Overview section. Click it again to display the graphs.

* The **Upcoming Renewals** table shows the date and cost of upcoming renewals by application.
* The **SaaS Application by License Cost** graph shows the cost of licenses by application. Hover over the various bars to see the percentage of licenses for each application.

<Image alt="LicensesCharts" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/LicensesCharts.png" />

## Licenses Table

The **Licenses** table opens displaying the default view. Not all of the fields are displayed by default. Use **Edit Columns** to add or remove columns. Each user can customize what fields appear in their own, personalized default view. For more information, see [Setting Page Columns Displays](/docs/setting-page-columns-display).

Click the arrow next to any of the fields to see more details about that field.

## Adapter Connections

Licenses are added automatically using data from your organization's discovered licenses. You can also manually add licenses via a CSV adapter.

The icon in the Adapter Connections column indicates what source Axonius is drawing its data from for any of the displayed licenses (Zoom, Google, Okta, etc). License data can also be manually uploaded through the CSV adapter (for more information, see [CSV - Licenses](/docs/licenses-csv).)

## License Fields

There are many fields that you can view and query on the Licenses page. This includes the following fields:

* **Application** - The specific application the license applies to.
* **Is Active License** - Indicates if the license is active or expired.
* **License Payment** - Indicates if the license is Free or Paid.
* **Subscription Term** - Indicates if the license renewal plan is a Monthly Renewal, Annual Renewal, Expiration, or Other.
* **Quantity** - Shows the number of licenses of that type.
* **Unit Price** - The price for each individual license.
* **Total Cost** - The Unit Price \* Quantity.
* **License estimated total monthly cost** - The license's average cost per month.
* **License estimated total yearly cost** - The license's average cost per year.
* **Currency** - the currency in which the license is priced. Can be either of the following values: USD, EUR, GBP, AUD.
* **Start Date** - The license's starting date.
* **End Date** - The license's ending date. When this value is empty, you can manually select a date using the Date Picker.
  * To do this, first add the **End Date** to the table, using **Edit Table**.
  * Hover over a row, a pencil icon is displayed.
  * Click the icon and from the dialog that appears, edit the end date.

**Editing License Fields**
You can use inline edit to edit license fields.

1. Hover over a field.
2. Use the edit icon to update a value.
3. If there are other columns that are dependent on these fields, they are updated immediately without waiting for a discovery cycle. For example, if you use online edit to change the quantity or price, the annual total cost is updated automatically.

### Enrichment Fields

These fields provide an additional level of detailed insights on your SaaS environments' applications, their users, and spending (based on account). For more information, see [Enrichment Fields](/docs/saas-applications#enrichment-fields).

* **Number of Associated Users** - The number of users associated with the license. You can click the number to open the list of users.

* **Number of Active Associated Users** - The number of users associated with the license who have logged into the application in the past number of days defined in the [System Settings](/docs/configuring-data-aggregation-settings). You can click the number to open the list of users.

* **Number of Inactive Associated Users** - The number of users associated with the license who have not logged into the application in the past number of days defined in the [System Settings](/docs/configuring-data-aggregation-settings). You can click the number to open the list of users.

* **Possible Savings of Inactive Associated Users** - The cost (in US Dollars) of the licenses associated with inactive users.

* **Possible Savings of Available Licenses** - The cost (in US Dollars) of the licenses that have not been assigned to any users.

## Manually Add Licenses

For licenses that are not added automatically with an adapter, you can manually add the license records in your system.

**To Manually add a license**

1. In the Licenses page, click **Create new asset**.

   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAsset\(2\).png)

<br />

2. Enter the fields for the license you want to create. The following fields are required for new licenses:

* Application
* Name
* End Date
* Subscription Term
* Total Cost
  For descriptions of License fields, see the list of [License fields](/docs/licenses#license-fields).

3. Click **Save Changes**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManualAsset.png)

For more information on manually creating assets, see [Manually Creating an Asset](/docs/manually-creating-an-asset).

## Creating Queries on Licenses

You can create queries on this page using the Query Wizard or the Basic Query and query fields such as the fetch time, adapter connections, or Single Sign On. You can add additional levels to the query, such as querying fields such as application, adapter connections, or License Payment. Refer to [Creating Queries with the Queries Wizard](/docs/query-wizard-and-query-filter) and [how to create Queries in Basic mode](/docs/basic-query-mode) to learn more about creating queries.

For example, this query enables you to determine how many active licenses for applications in your SaaS environment are approaching their end date or actual renewal date:

<Image alt="Licenses Query" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Licenses%20Query.png" />

After running the query, the overview and table show the relevant licenses, filtered by the criteria you defined in your query.

## Adding Custom Data to a License

You can add custom fields to one or more licenses at the same time. You can use this to manually add a License Cost field or other data that's specific to your organization.

Select one or more licenses, and from the **Actions** menu, choose **Add Custom Fields**.

Refer to [Working with Custom Data](/docs/working-with-custom-data) to learn about adding custom fields.

## Add Tags to a License

Use tags to assign context to your licenses for granular filters and queries. Apply new or existing tags to the selected licenses. The list of selected tags is applied to all selected licenses.

Refer to [Working with Tags](/docs/working-with-tags) to learn about adding tags to licenses.

## View a License Profile

You can click on an individual asset in Licenses to see all its relevant data. For more information, see [Asset Profile Page](/docs/asset-profile-page).