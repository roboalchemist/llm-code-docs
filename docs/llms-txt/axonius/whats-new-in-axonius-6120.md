# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6120.md

# What's New in Axonius 6.1.20

#### Release Date: June 23rd 2024

These Release Notes contain new features and enhancements added in version 6.1.20.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### New SaaS Management Dashboard Templates

The following new SaaS Management Dashboard templates were added:

* '[Cost Optimization](/docs/cost-optimization-dashboard-template)'
* '[Application Settings](/docs/application-settings-dashboard-template)'

## Assets Pages

The following features were added to all assets pages:

### Inline Edit of Values

It is now possible to [inline edit values of certain predefined aggregated fields](/docs/assets-page#inline-editing-aggregated-fields) directly from the Assets page, provided the field has an existing value. Once edited, the Aggregated field becomes a Custom Field with the new value.

## SaaS Management New Features and Enhancements

### Dynamic Charts Display Visual Data for Assets

You can display [predefined charts](/docs/saas-applications) on the top of SaaS Management asset pages that adjust to reflect the data for the queried assets.
![DynamicCharts2](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DynamicCharts2.png)

### Users Module - Expand Rows by SaaS Applications

In the new [Pre-defined “SM Users” view](/docs/users-page#sm-users-view), expands rows by the “Assigned Applications” field instead of by adapter connections. Each SaaS application is displayed in a separate row.
This clarifies which SaaS applications are assigned to each user, and which user applications fit specified query criteria.

![SMUserView\_Expanded](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SMUserView_Expanded.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Two-Factor Authentication

You can now use [two-factor authentication](/docs/managing-password-settings) for your Axonius user accounts. This enhances system security and adherence to compliance requirements. When enabled, users will receive an email notification with a verification code to complete the login process.

### Allow Token in Syslog Messages

You can now add a token to [Syslog](/docs/configuring-syslog-settings) messages.

<Image alt="Syslog-EnableToken" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Syslog-EnableToken.png" />