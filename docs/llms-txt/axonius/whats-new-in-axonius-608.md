# Source: https://docs.axonius.com/docs/whats-new-in-axonius-608.md

# What's New in Axonius 6.0.8

#### Release Date: November 12th 2023

These Release Notes contain new features and enhancements added in versions 6.0.7 and 6.0.8.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### New Dashboard Manager

A new [**Dashboard Manager**](/docs/manage-dashboards) was added to the System. Use the Dashboard Manager page to manage the dashboards on your system. The Dashboard Manager table provides a centralized summary of information about all existing dashboards. You can create, update, and delete dashboards. You can also assign and arrange dashboard Favorites. You can also define the default dashboards for your Data Scope.

![DashboardManager-Full.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardManager-Full.png)

### Chart Enhancements

#### Aggregate Data by Hour and Quarter on Timeline Charts

The capability has been added to aggregate data in a chart by hour and quarter when using the Timeline visualization.
![TimeAggregationQuarter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TimeAggregationQuarter.png)

This is available on the following charts:

* [Field Segmentation Chart](/docs/field-segmentation-chart)

* [Field Summary Chart](/docs/field-summary-chart)

* [Query Timeline Chart](/docs/query-timeline-chart)

* [Pivot Chart](/docs/adv-pivot-chart)

## Vulnerability Management Module and Software Management Module New Features and Enhancements

The following new features and enhancements were added to   both the Vulnerability Management Module and the  Software Management Module:

**Displaying Historical Data on the Vulnerabilities and Software Profile Pages**
It is now possible to use a date picker to display the data of a specific date on the [Vulnerabilities Profile](/docs/vulnerabilities-profile) and the [Software Profile](/docs/software-profile) pages. This enables users to look at various software or vulnerability assets for a specific date without having to go back to the relevant  table to adjust the dates.

**Edit Columns on Associated Devices Page**
**Edit Columns** was added to the Associated Devices Page on the [Vulnerabilities Profile](/docs/vulnerabilities-profile) and the [Software Profile](/docs/software-profile) pages to set the columns displayed  so that columns related to the devices investigated are displayed.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

* **Axonius Catalog Enrichment Added**
  * The Installed Software: Name and Installed Software: Vendor fields are now enriched by Axonius Catalog.
  * Software Category is now added as a default field, enriched by Axonius Catalog.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the Asset Graph:

### Enforcement Sets, Tags, Custom Fields and Create Tickets from the Asset Graph

The ability has been added to create new [Enforcement Sets](/docs/asset-graph#using-enforcement-actions-from-the-asset-graph) based on the results of investigation in the Asset Graph. Existing Enforcement Sets can also be used.
You can also [assign tags](/docs/working-with-tags), add [custom fields](/docs/working-with-custom-data) and [create tickets](/docs/devices-actions#create-ticket) directly from the Asset Graph.

<Image alt="AssetGraph-UsingECs.png" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-UsingECs.png" />

### Exploring Connections between Assets

You can now use the new [Explore Connections](/docs/asset-graph#exploring-connections) pane to customize what connections to expand. You can also select to show assets that have no connection to the selected asset. This is useful when looking for unmanaged assets and other scenarios where the lack of connection is important.

![AssetGraph-ExploreConnections.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-ExploreConnections.png)

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Query Search

On the [Queries page](/docs/managing-queries) the Query search box now enables the user to type all or part of the Query name to make finding a query easier.

## Reports New Features and Enhancements

The following updates were made to Reports:

### Adding Individual Dashboard Charts to a Report

You can now add individual charts to a [report](/docs/report-configuration-page#configuring-reports). This is useful when you want to add only the specific chart and not the whole dashboard.

<Image alt="ReportsSelectingDashboardsCharts.png" width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ReportsSelectingDashboardsCharts.png" />

## General Updates

### Open Page in New Tab

**Open Page in New Tab or Window using Browser Context Menu**
It is now possible to  right click the following items and open  a regular browser  context menu with the option to open the page in a new tab or a new window:

* Main side panel navigation items
* Findings top panel icon
* Settings icon

**Open Page from Link Button in New Tab**

Right click any link button at the top of any page to open the linked page in a new tab.

![OpneInNEwTab](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OpneInNEwTab.png)

**Open Page in New Tab Using Actions Menu**

It is now possible to open various pages in Axonius in a new tab using the Actions menu

* Asset Profile pages from the Asset page.
* Enforcement Sets with more than one action.
* Reports

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### External Password Managers Settings

**HashiCorp Vault**
Namespace is now supported for this vault.

**Click Studios Passwordstate**
Dialog for fetching the password was updated.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Defining the Default Enforcement Sets Table View

Users can filter the Enforcement Sets table to show only those Enforcement Sets of interest to them, and save that view as their [default table view](/docs/using-the-ec-page#Defining-the-Default-Table-View) instead of the system default table view, which displays all Enforcements created by all users in their data scope. Users can revert to their saved default view from any other view, and also reset the filters and restore the unfiltered view as the default view.

### Enhancements to Axonius Actions

### Custom Enrichment

[**Custom Enrichment**](/docs/add-enrichment) is supported for Software.

### Axonius - Send Email

* [**Axonius - Send Email**](/docs/send-email)
  * Added the ability to set a name for the CSV file instead of using the default file name set by Axonius.
  * Custom message can be up to 10000 characters long.
  * The email message body can now include data extracted from fields in Queries based on filters (such as **Activity Logs** and  **Adapters Fetch History**) results.