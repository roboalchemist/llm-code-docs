# Source: https://docs.axonius.com/docs/whats-new-axonius-50-compared-to-488.md

# What's New in Axonius 5.0 compared to 4.8.8

These Release Notes contain new features and enhancements added in version 5.0 after the most recent minor version 4.8.8.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features

## Software Management Module Add-On

The Software Management Module delivers a complete software inventory, contextualized with device, user, and vulnerability associations.
It enables users to:

* Gain a single unified view for all software from all sources across all devices - a credible, comprehensive distribution.
* Discover specific software and potential software gaps using Software Query.
* Categorize software - Authorized/Unauthorized (via Tags).
* Software utilization tracking - Identify over/under usage (via Device Counts).

![SWManagementV5](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SWManagementV5.png)

To learn more about all the capabilities of the Software Management Module, refer to:

* [Software](/docs/software)

* [Software Profile](/docs/software-profile)

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

### Last Successful Fetch

On the **[Adapter Connections](/docs/adapter-connections)** page a new **Last Successful Fetch** column  was added. This shows the time and date of the last successful fetch for that connection.

## Devices and Users Page New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

### Create New Asset

It is now possible to [manually create assets](/docs/manually-creating-an-asset) based on custom data. This allows you to create your own assets with your own data. This is useful in the case there are assets which have “one-off” characteristics Once created, these assets are exactly the same as any other asset in the system.

<Image alt="CreateNewAssetDialog.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateNewAssetDialog.png" />

### Query Wizard Enhancements

* **in (plain text)**

  * An option to use an **[in (plain text)](/docs/adding-multiple-values-to-query-expression#in-plain-text)** operator was added to the Query Wizard. This allows adding lists of items directly into the operator field in the Query Wizard. This is useful if you need to enter more than 2000 values.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Edit Single Select Custom Fields

It is now possible to  edit values of *Single Select* custom fields in the Management table on the **[System Settings `>` Data `>` Custom Data and Tags](/docs/managing-custom-fields-and-tags#editing-a-single-select-custom-field)** page, using a new  **Edit** action from the **Actions** menu. This includes modifying, deleting, and adding values of a custom field.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Discovery Cycle Added to Enforcement Activity Logs

The Discovery Cycle start date and time of activities from the **Enforcement** category is now displayed under the **Discovery Cycle** column in [Activity Logs](/docs/activity-logs-page).
You can also view  directly from the Axonius dashboard all the Enforcement activities in the current [Discovery Cycle](/docs/system-lifecycle-chart#system-lifecycle-chart), by selecting the **Activity Log** option from the **Post-Correlations** stage three-dot menu.

![DiscoveryCyclePostCorrelationMenu](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DiscoveryCyclePostCorrelationMenu.png)