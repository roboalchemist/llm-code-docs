# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6136.md

# What's New in Axonius 6.1.36

#### Release Date: October 13th 2024

These Release Notes contain new features and enhancements added in version 6.1.36.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

## SaaS Management New Features and Enhancements

### Dynamic Charts Displayed by Default in Asset Page

Axonius now [displays dynamic charts](/docs/saas-applications#overview) by default at the top of the asset page for SaaS Management assets. Users can select to hide the charts.
![DynamicCharts(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DynamicCharts\(1\).png)

### Basic Query Mode Enabled by Default on SaaS Management Asset pages

When a user opens a SaaS Management Asset page, the [Basic Query mode](/docs/accounts#creating-queries-on-accounts) is enabled as the default  option for querying the assets on the page. Users can select to enable the Query Wizard mode instead.
![BasicQuery](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BasicQuery.png)

## Licenses Page New Features and Enhancements

### New Enrichment Fields for Licenses

The following [new License fields](/docs/licenses#enrichment-fields) provide data on users associated with the licenses:

* **Number of Associated Users** - The number of users associated with the license. Click the number to open the list of users.
* **Number of Active Associated Users** - The number of users associated with the license who logged in within the past 30 days. Click the number to open the list of users.
* **Number of Inactive Associated Users** - The number of users associated with the license who did not log in within the past 30 days. Click the number to open the list of users.
* **Possible Savings of Inactive Associated Users** - The cost (in US Dollars) of the licenses associated with inactive users.
* **Possible Savings of Available Licenses** - The cost (in US Dollars) of the licenses that were not assigned to any users.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Advanced Settings Enhancements

The following enhancements are currently implemented for the Google Workspace adapter and will be gradually deployed to additional adapters.

* **Dropdown for Selecting Asset Types**

New dropdown in Advanced Settings (Advanced Configuration section) added that allows the user to select one or more asset types. Once the asset types are selected, the relevant advanced configurations are displayed. Advanced Configuration is divided into subcategories to make finding of relevant settings easier.

![Adapter Advanced Settings Asset Type Dropdown.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Advanced%20Settings%20Asset%20Type%20Dropdown.png)

* **Tooltip for Advanced Configurations**

Advanced configurations now have a description in a tooltip which provides information such as asset  types, permissions, description, and more.

![Adapter Tooltip for Advanced Configurations.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Tooltip%20for%20Advanced%20Configurations.png)

![Adapter Advanced Settings Asset Type Fetch User Audit Logs Dropdown warning.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Adapter%20Advanced%20Settings%20Asset%20Type%20Fetch%20User%20Audit%20Logs%20Dropdown%20warning.png)