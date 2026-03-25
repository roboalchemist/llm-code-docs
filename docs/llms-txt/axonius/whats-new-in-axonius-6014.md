# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6014.md

# What's New in Axonius 6.0.14

#### Release Date: December 24th 2023

These Release Notes contain new features and enhancements added in versions 6.0.13 and 6.0.14.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Management Enhancements

#### Charts Field Lists the Charts in a Dashboard

The new Charts field in the Dashboard Manager allows you to view a [list of charts](/docs/manage-dashboards) for each dashboard.

### Dashboard Import/Export Enhancements

Dashboards with Custom or Private access permissions can now be [exported](/docs/importing-and-exporting-dashboards).

### Dashboard Navigation Enhancements

#### Subfolders Appear on the Dashboard Page

Subfolders created on the [Dashboard Manager](/docs/manage-dashboards) page, and dashboards placed in them, now appear in the same arrangement on the [Dashboards](/docs/working-with-dashboard-spaces) page.

### Chart Enhancements

#### Asset Table Widget

A new [Asset Table](/docs/asset-table) widget was added. This allows users to view the results of a given query in an asset table format as part of the dashboard. View the result of a given query in a dashboards in the same way as in the asset tables (limited to aggregated view) with ability to set the columns displayed.

<Image alt="AssetTable" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetTable.png" />

## Assets Pages

### SaaS Applications - New Enrichment Fields

The following new [enrichment fields](/docs/saas-applications#enrichment-fields) provide an additional level of detailed insights on users, applications, and spending in your SaaS environment:

* Non Operational / Unknown Activity Status

* Last enrichment run

* Admins

* Operational Users

* Suspended Users

* Deleted Users

* Expense Amount

* License Cost

* External Users

* Paid Users

* User Extensions Used by App

* App User Extensions

* Upcoming renewals

* Total Misconfigured Settings

* Total Settings

* Total Accounts

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

**Version Count field added**
New Version Count field added to the [Software Management Module](/docs/software). This shows the number of software versions that a software has. This field can be queried, using `<`, `>` and =.  Use the Version Count field in software to help identify software that have "older" versions of software on them by identifying software that have software greater than the number of versions back that   permitted on the system.

## Asset Graph New Features and Enhancements

### Save and Load Graphs

Save and Load Graphs lets users save and load any graph  created with Axonius [Asset Graph](/docs/asset-graph), along with the steps that are part of it. It enables users to preserve work, resume their investigation, and share their graphs with others while being aligned with the roles and permission restrictions.

### Asset Graph Manager

The [Asset Graph Manager](/docs/managing-asset-graphs) helps users manage all their saved graphs in one place. Users  can organize graphs into folders, mark them as favorites, search specific graphs based on the steps taken in each one, edit them, and more. Users can access and use their graphs more easily and efficiently, and also enjoy pre-defined content to help get started.

## Administrator Settings New Features and Enhancements

### AI Query Assistant

The [AI Query Assistant](/docs/configuring-chatgpt-settings) can now use a local version of ChatGPT as well as the Microsoft Azure version, in addition to the standard ChatGPT.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enforcement Action Delay Mechanism

It is possible to [delay the execution of a Post, Success, or Failure action](/docs/create-ec-set#delaying-enforcement-action-execution)(but not a Main action) by a defined amount of time. For example, an Enforcement Action can be configured to send an email to a user about losing access to an application, and trigger a Revoke action a week later.

### Dynamic Value Statement Updates

#### Unique function

Added the option to [apply the *unique* function on another function](/docs/using-functions-and-keywords#applying-the-unique-function-on-a-nested-function).
Syntax: **unique** (nested function)

## Findings Center New Features and Enhancements

The following new features and enhancements were added to the Findings Center:

* A Mute icon was added near muted alerts inside the [Alerts drawer - Name field](/docs/viewing-alert-information#viewing-a-findings-center-alert) to enable easy differentiation between triggered alerts and muted ones.
* For *Query comparison* and *Query change over time* trigger conditions, the [Alerts drawer - 1st Count  and 2nd Count fields](/docs/viewing-alert-information#viewing-a-findings-center-alert) display the number of assets that were compared in the condition that created the alert.