# Source: https://docs.axonius.com/docs/whats-new-in-axonius-61-compared-to-6018.md

# What's New in Axonius 6.1  compared to 6.0.18

#### Release Date: February  4th 2024

These Release Notes contain new features and enhancements added in versions 6.0.19 and 6.1

* Read [What's New in Axonius 6.1](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

## Assets Pages

The following features were added to all assets pages:

**Asset Investigation**
Asset Investigation queries can now be used in the Field Segmentation chart.

### Query Wizard Enhancements

**Asset Relationship Queries**

It is now possible to create queries in the Query Wizard based on '[Relationship](/docs/selecting-source-options-in-the-query-wizard#relationship)', that is to query on assets that are connected to each other based on the relationship between assets and by using a saved query from a different asset type. This creates powerful cross asset queries, as it is possible to easily create queries on assets connected to each other.
![RelationRN](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RelationRN.png)

**End of Support Queries**

You can create queries to find [End of support](/docs/devices-page#os-end-of-life-and-end-of-support) for various OS versions using 'Preferred OS: End of Support' or 'OS: End of Support'. End of support is an aggregated value  enriched by Axonius. Devices are enriched with data about the End of support for operating systems running on them.

**VMware ESXI**

End of Life and End of Support added for VMware ESXI Operating system.

## SaaS Management New Features and Enhancements

The following new counter fields in the [SaaS Application Extensions](/docs/application-extensions#counter-fields) module provide an additional level of detailed insights regarding the usage of application extensions in your SaaS environments. When you click the number displayed in these fields, Axonius redirects you to the list of User Extensions that the number represents.

* User Count
* Activity Status - Active Count
* Activity Status - Inactive Count
* Activity Status - Unused Count
* User Activity Status - Active Count
* User Activity Status - Inactive Count
* User Activity Status - Unused Count
* Active Status But Inactive User Count
* Permissions - Is Admin count
* Permissions - Is Identity count
* Permissions - Mail count
* Permissions - Drive count
* Permissions - Calendar count

## Case Management

When query results indicate a problem or anomaly in the system that requires fixing, it is possible for Axonius users to create a Case indicating the type of issue, assign the Case a priority, assign the case to a user or group of users, link it to an asset query, set a due date for resolving the case, and more. Once a Case is created, it can be managed together with already existing Cases from the new **Case Management** page, which shows a centralized summary of all cases, and enables opening any case to track its progress and change its status.
These Cases (similar to "in-house tickets") enable users to resolve issues of certain types from within Axonius, instead of opening a ticket in a third-party system.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

**Password Management Vaults**
[ Keeper Security Password Management Vault](/docs/managing-external-passwords#keeper-secrets-manager) now supported.

## Cloud Asset Compliance New Features and Enhancements

The following updates were made to [Axonius Cloud Asset Compliance](/docs/cloud-asset-compliance-page):

### Support for CIS Microsoft Azure Foundations Benchmark v2.0

Support for the CIS Microsoft Azure Foundations Benchmark v2.0 has been added to the [Cloud Asset Compliance Center](/docs/cloud-asset-compliance-page).

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

### Enhancements to Axonius Actions

#### Manage Custom Enrichment - Enrich assets with CSV file enforcement action

In the [**Manage Custom Enrichment - Enrich assets with CSV file** enforcement action](/docs/add-enrichment), it is now possible to validate the syntax of an enrichment statement to verify that it is valid before running the enrichment.

\####[Axonius - Send Email](/docs/send-email)
Added the option to hide adapter icons in the table.