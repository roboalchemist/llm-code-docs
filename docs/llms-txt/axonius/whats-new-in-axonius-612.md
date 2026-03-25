# Source: https://docs.axonius.com/docs/whats-new-in-axonius-612.md

# What's New in Axonius 6.1.2

#### Release Date: February  18th 2024

These Release Notes contain new features and enhancements added in versions 6.1.1  and 6.1.2.

* Read [What's New in Axonius 6.1.3](/docs/whats-new-in-axonius-613) for Axonius 6.1.3 features.

* Read [What's New in Axonius 6.1](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

#### Asset Table Chart

The [Asset Table](/docs/asset-table) chart now supports the Vulnerabilities and Software modules.

#### Pivot Chart

* Matrix visualization now available for [Pivot](/docs/adv-pivot-chart) chart (currently limited to one measure).

* The Matrix includes an option for dynamic color threshold that automatically distributes color intensity based on the minimum and maximum values in the table.

## Assets Pages

The following features were added to all assets pages:

**New Asset Types**
The following asset types were added:

* Certificates

### Saved Views

Users can now create [**Saved Views**](/docs/setting-page-columns-display#saved-views) for Assets Pages. The views are the arrangement of columns displayed in the Asset tables. This enables each user to have views most relevant for specific use cases  and switch between views as required.
For existing users upgrading to this version note that the **Saved Views** capability replaces the Reset System Default, Reset User Default, and Edit System Default buttons, allowing users to edit a view or set it as default.  If the User Default view  is defined in the existing version, after upgrade is will be presented as a predefined view called *View1*.
![ViewsLoadingView](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ViewsLoadingView.png)

#### Asset Investigation

The following user fields are now supported:

* User Title

* Hire Date

* Business Title

* Termination Date

* Is Terminated

* Location

* Employee ID

## Vulnerability Management Module and Software Management Module New Features and Enhancements

**Moving Between Pages in Context**
When a user clicks on the number of devices on the **Vulnerabilities** and **Software** pages
to open them on the **Devices** page, the **Devices** page now opens and displays relevant pre-defined contextual columns and results.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Tags  Management

The [Tags Management table](/docs/managing-tags#managing-tags-from-a-table) now displays the Enforcement Center icon in the **Used In** column of each tag that is used in the Enforcement Center. Hovering over this icon opens a table with links to each "used in" Enforcement Set (see below). Clicking a link opens in a new tab the Enforcement Set's configuration page.

![UsedInECs](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UsedInECs.png)

### External Password Managers

Added the capability to select an API prefix for the [CyberArk Vault](/docs/managing-external-passwords#cyberark-vault).

### Syslog Settings

An option was added to  send all messages to [Syslog](/docs/configuring-syslog-settings) using the RFC 5424 protocol.