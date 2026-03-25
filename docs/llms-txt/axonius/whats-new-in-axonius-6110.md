# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6110.md

# What's New in Axonius 6.1.10

#### Release Date: April 14th 2024

These Release Notes contain new features and enhancements added in version 6.1.10.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Granular Permissions

Admins now have more control and flexibility in [granting permissions](/docs/permissions-list) for activities on Assets pages as a result of the following changes:

* The ‘Edit Asset’ permission on each asset type has been split into two permissions:
  * **Create, Delete, and Link**
  * **Edit Tags and Custom data**

* In addition a separate ‘**Export to CSV**’ permission has been added to each relevant permission type, instead of one permission for the whole system.
  All existing users will maintain the same access and capabilities that were previously set for them.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

### Last Used

The **Last Used** field is now displayed as a field on the **[Versions](/docs/software-profile#software-versions)** tab of the **Software Management Module**. The table can be filtered by this field.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the Asset Graph:

### Apply a Filter to All Assets Displayed in the Asset Graph

The ability has been added to [apply a filter](/docs/applying-a-filter-to-the-asset-graph) to all assets and asset groups displayed in the asset graph allowing users to focus in on the assets they want to know about. One filter can be configured for each asset type represented. The applied filters are indicated at the top of the graph and on the filter icon to the right.

![AssetGraph-GlobalFilter.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraph-GlobalFilter.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Permissions Updates

See above for information about permissions changes to Asset pages. In addition, as mentioned, the existing Global Action permissions **Export to CSV enabled** was removed, and there is a new **Export to CSV** permission that can be set for every permission type. All existing permissions have been retained.

## General Updates

### Gateways supported for  Customer-hosted (on-premise / private cloud)

Gateways are now supported for  Customer-hosted (on-premise / private cloud) instances of Axonius, to use for segregated data sources within the organization.