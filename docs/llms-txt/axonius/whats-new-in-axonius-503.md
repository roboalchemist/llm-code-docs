# Source: https://docs.axonius.com/docs/whats-new-in-axonius-503.md

# What's New in Axonius 5.0.3

These Release Notes contain new features and enhancements added in version 5.0.3.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### New Dashboard Templates

The new [Data Hygiene Dashboard Template](/docs/data-hygiene) was added.

## Asset Pages

The following features were added to all asset pages:

### Export CSV for Asset Inventory Pages

It is now possible to select which assets to export when **[Export CSV](/docs/exporting-devices-data-to-csv)** is selected.

## Devices and Users Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

**Alert for Asset Changes via Asset Investigation**

[Asset Investigation queries](/docs/advanced-asset-investigation#saving-filters-and-searches)(from Devices/Users pages) created using filters can be used as queries in the following basic enforcement set actions so that users can be notified about any change on the asset as soon as it is identified:

* [Send Email](/docs/send-email)
* [Send to Syslog Server](/docs/send-to-syslog-server)
* [Send to HTTPS Log Server](/docs/send-to-https-log-server)
* [Send Slack Message](/docs/send-slack-message)
* [Push System notification](/docs/push-system-notification).

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

**Date Refinement**
[**Data Refinement**](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows) is now supported for the Vulnerability Management Module. *Refine field values by adapter connection* and *Refine Asset entities by adapter connection* options are not available.

## Software Management Module New Features and Enhancements

**Data Refinement**
[**Data Refinement**](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows) is now supported for the Software Management Module.

## Reports New Features and Enhancements

The following enhancements were added to reports.

### Send Reports Every X Months

The capability was added to [send reports](/docs/report-configuration-page#setting-the-email-schedule) every X months on a specific day of the month.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Banner Indication

It is now possible to enable display of a banner with information for all users of the system, from the **[System Settings> GUI> UI](/docs/configuring-user-interface-settings)** page.  This capability was previously available on the **Instances** page.

### Notification that Scheduled Fetch Failed

You can configure the system to send a notification when a scheduled fetch fails to trigger from **[Notifications](/docs/configuring-notification-settings)** Settings under **System** Setting.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

### New Axonius - Calculate Risk Score Action

The new **[Axonius - Calculate Risk Score](/docs/risk-score)** enforcement action calculates a per-vulnerability-per-device risk score for each device that is returned from a query, and writes the risk score to a dedicated field on the device. Users can choose the Device and Vulnerability field values to include in the risk score calculation, as well as the weight % of each one. Each time the enforcement action runs, it performs a complex cross-entity calculation involving the field values from the selected Device and Vulnerability fields - streamlining work with the system.  Users can also use this enforcement action for single asset risk calculations (per device, per vulnerability).
![AxoniusCalculateRiskScoreActionConfigScreen](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AxoniusCalculateRiskScoreActionConfigScreen.png)