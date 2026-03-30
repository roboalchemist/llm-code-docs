# Source: https://docs.axonius.com/docs/whats-new-in-axonius-604.md

# What's New in Axonius 6.0.4

#### Release Date: October 15th 2023

These Release Notes contain new features and enhancements added in versions 6.0.3 and 6.0.4.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Chart Enhancements

**Adapter Segmentation Chart**
[Adapter Segmentation](/docs/adapter-segmentation-chart) chart now supports charts based on Vulnerabilities and Software queries.

**Query Intersection Chart**
[Query Intersection](/docs/query-intersection-chart) chart now supports charts based on Vulnerabilities and Software queries.

## Assets Pages

The following features were added to all assets pages:

### Adding Custom Fields from Asset Pages

When adding [custom fields](/docs/working-with-custom-data) to assets (by selecting **Actions> Add Custom Field** for selected assets on an **Assets** page), it is possible to differentiate between adding custom data fields and adding values to existing Axonius fields.
Custom fields can now be filtered by type:

* **Axonius Fields** - Fields from the adapter.

* **Custom Fields** - Tailormade fields created by users.

* **All Fields** (default) - Axonius Fields and Custom Fields.

![AddCustomNewFilter](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AddCustomNewFilter.png)

### Display List Fields as Tables on Asset Profile Page

Fields which contain lists can now be displayed as tables on the Asset Profile page.

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

### Associated Devices Tab

An Associated Devices tab was added to the **[Vulnerabilities Profile](/docs/vulnerabilities-profile)** page. It shows the adapter connections and preferred hostname  for the Device from which the Vulnerability was fetched.

**Enrich Vulnerabilities from MSRC DB**

Axonius now enriches vulnerabilities with data from MSRC  via connected adapters. This option is set by default under [System Settings>Enrichment](/docs/configuring-enrichment-settings).

**NVD CVE status**
A new column added to the Vulnerabilities page called NVD CVE status.

## Software Management Module New Features and Enhancements

### Software Profile Page Updates

The [Software Profile](/docs/software-profile) page now contains all functionality of the regular Asset Profile pages.

* **Software Profile page**

  * The [Associated Devices](/docs/software-profile#associated-devices) tab on the Software Profile pages now shows Installed Software: Software Name and Installed Software: Software Vendor

**Export CSV from Software Profile page**

* It is now possible to export  CSV files from the [Software Profile Page](/docs/software-profile).   On the Associated Devices tab it is possible to split the CSV file by Installed Software.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Data Aggregation Settings

**Preferred OS fields: Allow the following adapters**

* **[New Preferred OS fields: Allow the following adapters](/docs/configuring-data-aggregation-settings)**  setting - This settings allows users to enter a comma separated list of adapters to include in the Preferred\_OS calculations.

**Preferred Fields Device Model**

* **[New Preferred Fields Device Model](/docs/configuring-data-aggregation-settings)** Setting - This setting allows users to select an option for converting the case of the value of the preferred device model in Axonius.

### Enterprise Password Management settings:

**[HashiCorp Vault](/docs/managing-external-passwords#hashicorp-vault)**

* Role name parameter changed to Role ID

#### New Enterprise Password Managers

**[ManageEngine Password Manager Pro Vault](/docs/manageengine-password-manager-pro-vault)**

## Instance Page New Features and Enhancements

**Delete Collector Nodes from the Instances Page**

* It is now possible to delete collector nodes from the Instances page. Deleting a  node, completely removes it from the system and means that it needs to be installed again if required.

## General Updates

It is now possible to resize table columns on asset tables. Columns that contain logos with text  fields cannot be resized.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Values Wizard

You can now create Dynamic Value statements using the [Wizard](/docs/using-the-dynamic-value-statement-wizard). You can also convert from Wizard to Syntax and Syntax to Wizard.
The following screen shows the Wizard used to build an *All* statement.

![WizardCOmpleted](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WizardCOmpleted.png)