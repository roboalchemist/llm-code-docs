# Source: https://docs.axonius.com/docs/whats-new-in-axonius-507.md

# What's New in Axonius 5.0.7

These Release Notes contain new features and enhancements added in version 5.0.7.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

Icons are now supported on additional columns on the table:

* OS type and preferred OS type are now displayed with both text and icons.
* Severity type for vulnerabilities on both the [Vulnerabilities](/docs/vulnerabilities) and [Devices](/docs/devices-page) pages are displayed as colored icons.
* Cloud Provider is displayed with an icon.

### Create Asset Dialog Presents Required Fields

When [creating a new asset](/docs/manually-creating-an-asset), the required field names for that asset are automatically presented in the dialog. The new asset can only be saved after values are assigned to all required fields.

![CreateNewAssetRequiredFields](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAssetRequiredFields.png)

## Devices and Users Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

### Refine by Asset Entity

Added the capability to refine asset entities by condition from the Query Wizard when a  query is created.

![NEW\_Refinebyasset entity](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NEW_Refinebyasset%20entity.png)

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the [Vulnerability Management Module](/docs/vulnerabilities):

**Free Text Search**
Free text search was added to the **Vulnerabilities** page.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the [Software Management Module](/docs/software):

* **Free Text Search**

  * Free text search was added to the **Software** page.

* **'Earlier than' and 'Later than' operators are supported for software version queries**

  * Support for querying software versions using Earlier than and later than operators added to  the software management query wizard. This enables users to filter and retrieve software versions by their chronological placement.

**Sorting Software**

The default sort on the Software Profile page is now by Software Version.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Tag Grouping

The new **Tag Hierarchy** view on the **Manage Tags** page enables users to create a hierarchical tree (organizational chart) of tags in the system and assign tags to configured groups and hierarchies. Tags can be moved from one group to another and queries can be run to filter all assets having tags of a specific tag group.  Note that under **System Settings `>` Data**,[**Managing Custom Fields**](/docs/managing-custom-fields) and [**Managing Tags**](/docs/managing-tags) are now under 2 separate pages.

![TagHierarchyB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TagHierarchyB.png)