# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6111.md

# What's New in Axonius 6.1.11

#### Release Date: April 21st 2024

These Release Notes contain new features and enhancements added in version 6.1.11.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

### Chart Enhancement

#### Display More Than One Dimension in the Pivot Chart

Users can add more than one dimension to display for supported visualizations in the [Pivot chart](/docs/adv-pivot-chart#4-dimensions), increasing the flexibility for how and what data can be displayed.

#### Support for Preferred and Complex Fields

Values for complex fields and preferred fields can now be selected for dimensions and measures in the Pivot chart.

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Used In Available for All Users

All users can now see in which Axonius modules (Dashboards, Queries, Enforcements, Findings etc.) queries are used. This helps manage the saved queries. Previously, this functionality was available only to Admin users.

![UsedINRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsedINRN.png)

## Case Management New Features and Enhancements

[Cases](/docs/case-management-page) can now be viewed and managed in Kanban view.  In Kanban view, you can see the statuses of all Cases in the system in a convenient fashion and easily change the status of a Case by dragging and dropping it to the relevant status.
![CaseManagementTileView](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseManagementTileView.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Syslog RFC5424 Format

In Syslog Settings,   **Use RFC5424 Compliant Timestamp**  was renamed to **Use RFC5424 Compliant messages format** to send all Syslog log messages  using the RFC 5424 protocol.