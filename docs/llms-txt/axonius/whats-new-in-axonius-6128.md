# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6128.md

# What's New in Axonius 6.1.28

#### Release Date: August 18th 2024

These Release Notes contain new features and enhancements added in version 6.1.28.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Management Enhancements

#### Updating Permissions of Underlying Chart Queries when Updating a Dashboard

When [updating access permissions of a dashboard](/docs/changing-dashboard-access-permissions), the ability has been added to update the access permissions of the queries used in the included charts at the same time. A message is displayed listing the affected charts, the relevant queries, and where the queries are used.

<Image alt="DashboardPermissionChanges.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DashboardPermissionChanges.png" />

### Chart Enhancements

#### Findings Module's Alerts Supported in Pivot and Field Segmentation Charts

The Pivot Chart and Field Segmentation Chart can now [display data from alerts in the Findings module](/docs/viewing-alerts#display-alerts-data-in-dashboard). This allows users to:

* Select 'Findings' from the chart's 'Modules' drop-down

* Select saved 'Finding alerts' queries

* Filter the chart data with Finding alerts' filters

## Assets Pages

The following features were added to all assets pages:

### Refine Data for the Entire Assets Table

In addition to refining data for each field separately in an Assets table, you can now [manage data refinement for all table fields in a single dialog](/docs/setting-page-columns-display#refining-data-for-the-entire-table). The new, general **Refine Data** dialog allows users to select multiple fields to refine and assign each of them a refinement method of their choice.

### View a Complex Field Table Inside Another Complex Field

When a complex field contains another complex field, a column is created in the complex field's table with a [link to open the inner field in a separate page](/docs/asset-profile-page-complex-fields#nested-complex-fields). This makes it easier to view the data and navigate between complex fields.

## Devices Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** page.

### EOL/EOS and Latest Version Support for AlmaLinux

[Devices](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) in Axonius now support 'End of Life', 'End of Support', 'Latest Version', and 'Is Latest Version' for the AlmaLinux operating system.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### External Password Manager

The configuration for the [**CyberArk Privilege Cloud Vault**](/docs/managing-external-passwords#cyberark-privilege-cloud-vault) password manager was  updated to be the same as that of the [CyberArk Privileged Account Security adapter](/docs/cyberark-privileged-account-security) and to use the same connection.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### New Functions

The following function can now be used in a Dynamic Value statement:

* **array**
  * The new [*array* function](/docs/using-functions-and-keywords#using-the-array-function) creates an array of multiple fields. Each field input to the function can be an adapter field or text string. The array resulting from this function can be written into a single multi-value custom field (of type array (list)). This enables taking multiple values from different fields and aggregating them into a single custom list field.
    Syntax: **array** (\[adapter.field1], \[adapter.field2], ..., \[adapter.fieldN])