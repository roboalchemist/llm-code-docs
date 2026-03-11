# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6010.md

# What's New in Axonius 6.0.10

#### Release Date: November 26th 2023

These Release Notes contain new features and enhancements added in versions 6.0.9 and 6.0.10.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Chart Configuration Moved to the Left Side of the Chart

When a chart is in Edit mode, the chart configuration now appears to the left of the chart.

<Image alt="ChartConfigPane-Left.png" width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartConfigPane-Left.png" />

#### Create a Query on the Fly from the Chart Configuration

You can now create a new query from [within the chart](/docs/creating-a-query-on-the-fly) configuration. Use filters to find  the set of assets you want represented on the chart and, using the Asset Preview pane, save the filter as a new saved query.

#### New Asset Preview Pane Lists the Assets in a Selected Segment

The ability has been added to view a [preview of assets](/docs/viewing-the-asset-preview) represented in a chart. Clicking on a segment in the chart legend, or on the chart itself, opens the Asset Preview pane. From there, you can create a query from the list of assets, list the assets that match  a specific date and search the assets in the list.

<Image alt="ChartDetailsPane.png" width="700px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChartDetailsPane.png" />

## Assets Pages

The following features were added to all assets pages:

### Shows Asset Count for Each Asset Type

On the [Assets page](/docs/assets-page), the number of assets of each type is indicated in the Asset tab.

![AssetsPage-AssetCountInPane.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetsPage-AssetCountInPane.png)

### Query Wizard Enhancements

**IPv4 Count Operators**

* Count operators were added for IPv4.

## Vulnerability Management Module and Software Management Module New Features and Enhancements

The following new features and enhancements were added to the [Vulnerability Management Module](/docs/vulnerabilities):

**Additional Date Fields Added**

* **First Seen** is an aggregated date field that shows the earliest date that a Vulnerability was seen on the source.
* **Last  Seen** is an aggregated date field that shows the latest date that a Vulnerability was seen on the source.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the [Software Management Module](/docs/software):

**New Fields Added**

* **Preferred Software Name** and **Preferred Vendor Name** fields were added and are displayed by default.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the [Asset Graph](/docs/asset-graph):

### Custom Relationship Management

It is now possible to create custom relationships between asset types and expand an Asset Graph according to the new relationship. Manage your Custom Relationships in the new **[Custom Relationships Management](/docs/managing-custom-relationships)** page under **System Settings**.

<Image alt="CustomRelationshipMgmtPage.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CustomRelationshipMgmtPage.png" />

### Select Multiple Assets in the Asset Graph

You can now [select  multiple assets](/docs/asset-graph#selecting-multiple-assets) or asset groups in the Asset Graph and investigate them as a group.

You can do all of the following as long as the selected assets/groups are the same asset type:

* Expand connections

* Segment

* Filter

* Ungroup

* Preview

* View details

* View asset profile

* Enforce

## Findings Center New Features and Enhancements

Findings rules are now executed after Enforcement Sets are executed, in the Post-Correlation phase of the [Discovery Cycle](/docs/discovery-cycle).

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Enterprise Password Management

Thycotic Secret Server renamed Delinea Secret Server.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Setting Enforcement Set Run Priority

It is now possible to control the order of running Enforcement Sets scheduled to run every Discovery cycle, by assigning them a [run priority level](/docs/scheduling-ec-set-runs#setting-the-run-priority). This is especially useful when multiple Enforcement Sets running at the same time are dependent on each other.

### Enhancements to Axonius Actions

**[Axonius - Add Custom Data to Assets](/docs/add-custom-data)**

It is possible to add an existing custom field (name and value) to assets by selecting it from a filtered dropdown of existing Custom Fields or Axonius Fields. When selecting a field, its field type and value type are automatically filled in to the action fields.

**Enforcement Actions which Send CSV for Vulnerabilities or Software Include Selection of Associated Devices Fields**
For Enforcement Sets which send CSV files for Vulnerabilities or Software. When **Include  associated devices** is selected, the user can choose the device fields to include in the CSV file.