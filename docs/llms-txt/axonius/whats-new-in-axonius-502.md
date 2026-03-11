# Source: https://docs.axonius.com/docs/whats-new-in-axonius-502.md

# What's New in Axonius 5.0.2

These Release Notes contain new features and enhancements added in version 5.0.2.

* Read [What's New in Axonius 5.0](/docs/whats-new-axonius-50) to see all Axonius 5.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Axonius 5.0 Ongoing Adapter and Enforcement Action Updates](/docs/axonius-50-adapter-and-enforcement-action-updates).

## Dashboard New Features and Enhancements

The following new features and enhancements were added to the Dashboards:

### Dashboard Enhancements

**Field Segmentation  and  Field Summary Timeline Charts added support for Vulnerabilities and Software**
It is now possible to present historical dates and timelines on [Field Segmentation](/docs/field-segmentation-chart) and [Field Summary](/docs/field-summary-chart) charts based on Vulnerabilities and Software Management queries.

## Devices and Users Pages New Features and Enhancements

The following new features and enhancements were added to the **Devices** and **Users** pages.

### Customize Asset Profile ID

It is now possible to customize the [Asset Profile ID](/docs/asset-profile-page#deviceuser-profile-information), so that fields other than the default fields will be displayed.

![EditAssetPRofileID Dialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditAssetPRofileID%20Dialog.png)

## Reports  New Features and Enhancements

The following enhancements were added to reports.

### Generate Reports without the Cover Page or Table of Contents

You can now select whether to include the Cover page and Table of Contents pages in reports under [System Settings>UI Settings.](/docs/configuring-user-interface-settings)

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### Advanced Adapter Configuration

The following [settings can now be customized](/docs/advanced-settings#configuring-custom-settings-for-each-adapter-connection) for each adapter connection separately:

* 'Ignore devices that have not been seen by the source in the last X hours'

* 'Delete devices that have not been returned from the source in the last X hours'

* 'Ignore users that have not been seen by the source in the last X hours'

* 'Delete users that have not been returned from the source in the last X hours'

* 'Set as inactive after X failed attempts to connect'

![AdvCustom21](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdvCustom21.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### GCP Secret Manager

Added **GCP Secret Manager** as a new option to the Password Manager field under the [Enterprise Password Management Settings](/docs/managing-external-passwords) section.
The integration between Axonius and GCP Secret Manager enables Axonius to securely pull privileged credentials from GCP Secret Manager. The integration helps ensure that privileged credentials are secured in  GCP Secret Manager, rotated to meet company guidelines, and meet complexity requirements.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Conditional Statement Autocomplete

Conditional statements are used to add Dynamic Values to fields in Enforcement Actions.
As the user types a conditional statement, Autocomplete helps them quickly find and insert action form fields, functions, and operators, while minimizing typing and syntax errors.

<Callout icon="📘" theme="info">
  Note

  When the statement requires the user to enter an asset field,  Autocomplete directs the user to the Syntax Helper to make a choice.
</Callout>