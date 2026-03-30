# Source: https://docs.axonius.com/docs/whats-new-in-axonius-505.md

# What's New in Axonius 5.0.5

These Release Notes contain new features and enhancements added in version 5.0.5.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Enhancements

#### Query Timeline Chart Shows Percentages

Capability was added to the [Query Timeline chart](/docs/query-timeline-chart) to choose between displaying the asset count or the percentage of assets in the chart.

## Assets Pages

The following features were added to all assets pages:

### New Tickets Tab in Asset Profile Page

Users can now track the progress of tickets created in a third-party ticketing system (such as Jira and ServiceNow), directly from Axonius.
The new  **[Tickets](/docs/monitoring-third-party-tickets)** tab on the **Asset Profile** page  presents a table with information about all tickets created using Enforcement Actions linked to that asset, enabling users to track the progress of their third-party tickets from within Axonius. Ticket information is presented as a complex  field (and can be viewed on the relevant asset pages, and as a table on the **Asset Profile** page).
![TicketsTabinAssetProfile](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TicketsTabinAssetProfile.png)

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Expanding Nested Saved Queries

It is now possible to [view details of saved queries](/docs/managing-queries#viewing-and-editing-query-details) on which another query is based. An expand arrow in a nested saved query allows users to expand each saved query which is part of another saved query.

<Image alt="Nest3" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nest3.png" />

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Only Delete Devices if Fetch Was Successful

[Added adapter advanced setting ](/docs/advanced-settings#delete-devices-and-other-assets-not-returned-by-adapter-after-y-hours-only-if-fetch-was-successful) to only delete devices not returned by the adapter after a set number of hours,  if the fetch was successful.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Legacy System Settings Deprecation

The [**Axonius System Settings**](/docs/system-settings-overview) were completely redesigned in version 5.0 to make them easier and faster to use. Both the new and legacy System Settings have been available in parallel since Version 5.0. As of version 5.0.5, the toggle to switch between legacy and new System Settings has been removed, and the legacy settings are now deprecated and no longer available.

### Custom Enrichment

#### New "contains" Custom Enrichment Operator

A new "[contains](/docs/creating-the-rule)" operator was added to Custom Enrichment and can be used in a  Custom Enrichment statement (in **System Settings> Enrichment**)   to perform a case-insensitive search.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### New Enforcement Run Condition

An **Only when following adapter connections successfully completed fetch earlier in discovery cycle** option was added to the **[Enforcement Set Scheduling Additional conditions](/docs/scheduling-ec-set-runs)** section. This setting is used to make sure that the Enforcement Set runs only if the selected adapter connections have completed successfully their fetches. This ensures that the Enforcement Set runs on updated asset data.

![ECRN1](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECRN1.png)

### Condition Statements Updates

The following updates were made to the condition statement functionality.

**Renaming of Feature**

* **[Configure Action Conditions](/docs/config-ec-conditions)** was renamed to **Configure Dynamic Values**, and instead of defining a condition, the user defines a statement.

**New Divide Function**

* The new *[divide](/docs/using-functions-and-keywords)* function can be used in a Dynamic Value statement to divide the number values in a list from left to right. Its syntax is: divide (item1, item2,…, itemN)

**Switch/Case Statements Support set\_value of Field Paths**

* Switch/Case statements support set\_value of field paths. Additionally, "or" is supported with set\_value inside a Case statement and sets the value of the action field to the first field value in the "or" list that exists on the device.

#### Dynamic Value Statements Support Saved Query Filters (Refine Data)

An enforcement set configured with a dynamic value statement runs on the [query including data refinement](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows). This is the case for queries with all data refinement options except "Refine field values by adapter connection".