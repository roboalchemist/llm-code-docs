# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6016.md

# What's New in Axonius 6.0.16

#### Release Date: January  8th 2024

These Release Notes contain new features and enhancements added in versions 6.0.15 and 6.0.16.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

### Pivot Chart - Set a Filter on the Measures

Added the option to set a filter on the selected *[Measures](/docs/adv-pivot-chart#5-metrics)* field.

### Query Intersection - Calculate by Asset Entity

Ability was added to [calculate by asset entity](/docs/query-intersection-chart) instead of by the aggregated asset fields.

![CalculateAssetEntity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CalculateAssetEntity.png)

## Assets Pages

The following features were added to assets pages:

### Tickets

[New Tickets created as a result of an Enforcement Action are now created under the Axonius adapter connection](/docs/asset-profile-page-complex-fields#linked-tickets)' . Tickets, which are no longer linked to assets existing in the system, are cleaned and deleted by an automated Ticket Cleanup process.

## SaaS Management New Features and Enhancements

### Clickable Enrichment Fields

Users can click the number displayed in [SaaS Applications'](/docs/saas-applications) enrichment fields to display the lists of items the number represents. For example: Clicking the number displayed in the 'Managed Users by SSO' counter field redirects the user to the **Users** table, filtered for 'Is Managed by SSO'.

<Image alt="EnrichmentsClickable" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnrichmentsClickable.png" />

### Associated Licenses Field

A new ['Associated Licenses](/docs/users-page#saas-management)' User field displays all the licenses associated with a user, providing an easy way to query for licenses a user has across SaaS Applications. This complex field specifies the license names along with their pricing units and costs.

## Devices and Users Pages New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

**End of Life Queries**

You can create queries to find [End of life](/docs/devices-page#os-endoflife) for various OS versions using 'Preferred OS: End of Life' or 'OS: End of Life'. End of life is an aggregated value  enriched by Axonius. Devices are enriched with data about the End of life for operating systems running on them.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

### Software End-of-life and End-of-support Fields Added

The following fields, and filters for these fields were added to the **[Software Management Page](/docs/software)** and to the **[Software Versions](/docs/software-profile#software-versions)** tab on the **Software Profile** page as part of Axonius Catalog enrichment, which is expanded over time:

* End-of-life (date)
* Is End-of-life
* End-of-support (date)
* Is End-of-support

This allows users to track information about Software that reached or are about to reach End-of-life or End-of-support, and take appropriate action if required.

## Instance Page New Features and Enhancements

### Add Collectors Using User Interface

Added the capability to seamlessly choose between the [primary node and collector node during installation](/docs/configuring-the-axonius-platform#logging-on-to-the-web-ui), and to [add a collector node](/docs/connecting-additional-axonius-nodes#connecting-an-additional-node) using the User Interface.

<Image alt="AxoniusCollctor" width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AxoniusCollctor.png" />

## General Updates

### Actions on Table Rows

Actions are now displayed as icons at the right side of the row when the user hovers over any row in the table. When there are four actions or more, on hover, only the first three Actions are displayed; a **More Actions** icon shows the rest of the available actions. Once one or more rows are selected, the available actions are displayed at the top of the table. Actions are displayed in the same order whether displayed by hovering or by selecting items in the table.
![NewActions](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewActions.png)

## Enforcement Center New Features and Enhancements

The following enhancement was added to the Enforcement Center:

### Enhancements to Axonius Actions

### Updated Manage Custom Enrichment - Enrich Assets with CSV File Action

In the [**Manage Custom Enrichment - Enrich Assets with CSV File**](/docs/add-enrichment) enforcement action, added the ability to add or remove custom enrichment data contained in a SQL Server table to or from assets, using the Custom Enrichment feature.

![ManageCustomEnrichmentECFileInputMethodSQLDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageCustomEnrichmentECFileInputMethodSQLDropdown.png)