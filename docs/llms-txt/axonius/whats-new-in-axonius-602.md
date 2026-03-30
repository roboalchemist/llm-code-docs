# Source: https://docs.axonius.com/docs/whats-new-in-axonius-602.md

# What's New in Axonius 6.0.2

These Release Notes contain new features and enhancements added in version 6.0.1 and 6.0.2.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Asset Investigation Available for Additional Asset Types

[Asset Investigation](/docs/advanced-asset-investigation) is now supported for all asset types in the system, apart from Vulnerabilities, Vulnerabilities Repository, Software and Activities.

### Filter Asset Investigation by Event Type

* It is now possible to filter [Asset Investigation by Event Type](/docs/advanced-asset-investigation#filtering): *Earliest Value Added*, *Value Added*, *Value Removed* or *Value  Changed*.

### Filtering Asset Investigation by Hours

It is now possible to filter  **Asset Investigation** by a specified last number of hours or for a time range prior to the number of hours,  in addition to already available filtering by days, weeks, months, or years.

## Asset Graph New Features and Enhancements

A new sidebar in the [Asset Graph](/docs/asset-graph) shows each step in the investigation with the Data Layers at the bottom. Breadcrumbs have been replaced by step tiles making it easier to move between invenstigation steps.

<Image alt="AssetGraphMultipleAssets-Expanded.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraphMultipleAssets-Expanded.png" />

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

* **Vulnerability Profile page**

  * A Vulnerability Profile page was now added to the system.

* **Device related asset entities - refine by condition**

  * In  **Refine data** it is now possible to use  **[Device related asset entities - refine by condition](/docs/vulnerabilities#refining-the-device-count-displayed-from-devicebased-fields-in-vulnerabilities)**  for the **Device Count** column to enable the adjustment of device count for specific device-based Vulnerabilitiy fields.

  <Image alt="MitigVuln\(1\)" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MitigVuln(1).png" />

## Data Analytics New Features and Enhancements

The following new features and enhancements were added to Data Analytics:

* A new [Export to CSV](/docs/analyzing-query-data#exporting-query-data-to-csv) function was added to export data from the Data Analytics table to a CSV file.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Manually Stopping and Starting a Discovery Cycle

When a user manually initiates a discovery cycle,  the system now asks the user to confirm their action. When a user stops a discovery cycle, the system asks the user to confirm their action.

### Filtering Adapters Fetch History by Hours

It is now possible to filter Adapters Fetch History by a specified last number of hours or for a time range prior to the number of hours, in addition to already available filtering by days, weeks, months, or years.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Activity Logs Settings

It is now possible to configure in the **[Activity Logs Settings](/docs/configuring-activity-logs-settings)** (accessible from **System Settings> System> Activity Logs**) whether or not access (read) activities are written to activity logs and displayed in the **Activity Logs** page.

### Service Account Settings

For each [service account](/docs/manage-service-accounts)(i.e., accounts that can connect to Axonius only using API), added an option to configure one or more IP address ranges in CIDR notation (accessible from **System Settings> User and Role Management> Service Accounts> Add Service Account**). This provides extra validation that service accounts are accessed via REST API calls only for known IP addresses.

## General Updates

### Link to the Release Notes for the Current Version

You can open the release notes of the current version of Axonius using the new link on the [Viewing System Information page](/docs/viewing-about-information)(the About page) in **System Settings**. The release notes for the current version are opened in a new browser tab.

## Findings Center New Features and Enhancements

The following new features and enhancements were added to the Findings Center:

### Bulk Marking Alerts as Seen

It is now possible to mark a [bulk selection of Finding Center](/docs/modifying-alert-status#bulk-marking-alerts-as-seen) alerts that are in 'Unseen' status as seen (i.e., change their statuses to 'Open') using a single action - **Mark as unseen** from the **Actions** menu.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### New Enforcement Action Trigger

The Enforcement Set Run History now shows **Notify** enforcement actions that are initiated by **Findings Rules** (new **Trigger Type**) that are preconfigured to send an [external notification](/docs/creating-a-findings-rule#adding-external-notification) when triggering an alert.

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

* **New now Function**

  * The new *[now](/docs/enforcement-action-condition-syntax-table)* function can be used in a Dynamic Value statement to return the current day's date and time. Its syntax is: now ()

* **New subtract Function**

  * The new *[subtract](/docs/using-functions-and-keywords#using-the-subtract-function)* function can be used in a Dynamic Value statement to return the result of subtracting item2 from item1. Supports two numbers (typed or values from fields) or two date-time fields. When subtracting two date-time fields, the result is the number of days with one decimal point. For example: 2.3
    Its syntax is: subtract(item1, item2)

## Activity Logs New Features and Enhancements

The following new features and enhancements were added to the Activity Logs:

### Filtering Activity Logs by Hours

It is now possible to  filter Activity Logs by a specified last number of hours or for a time range prior to the number of hours. This is in addition to already available filtering by days, weeks, months, or years.

### Enhancements to Axonius Actions

### Custom Enrichment

[Custom Enrichment](/docs/add-enrichment) is supported for Vulnerabilities.

### Export CSV for supported Software and Vulnerabilities queries

It is now possible to include the associated devices with preferred hostname as a predefined field for each software or vulnerability for relevant Enforcement Actions that create a CSV file.