# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6126.md

# What's New in Axonius 6.1.26

#### Release Date: August 4th 2024

These Release Notes contain new features and enhancements added in version 6.1.26.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Devices

#### EOL and Latest Version Support for Linux Suse

[Devices in Axonius](/docs/devices-page#os-end-of-life-end-of-support-and-latest-os-version) now support End of Life, Latest Version, and Is Latest Version for the Linux Suse operating system.

### Query Wizard Enhancements

#### Count Function Supported for User Company Field

The 'Count' function can now be applied to the 'User Company' field in the Query Wizard.

## Data Analytics Enhancements

[Data Analytics](/docs/analyzing-query-data) now supports queries configured with [data refinement](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows), allowing you to filter and analyze with greater detail.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value Statement functionality:

#### Enhancements to the Wizard

In the [Dynamic Value Statement wizard](/docs/using-the-dynamic-value-statement-wizard) for creating Switch/Case statements, the operators have been updated with more user-friendly names.
![OperatorDropdown](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OperatorDropdown.png)

#### Enhancements to Syntax Helper

The [Syntax Helper](/docs/using-the-syntax-helper) now shows the following information for the Adapter field selected for the Dynamic Value Statement:

* **Field Type** - The type of field. For example, **Single Value**, **Multiple Value**, **Single Select**, **Multiple Select**.
* **Value Type** - The type of value in the field. For example, **bool**, **integer**, **float**, **string**, **date**, **array**, **array (string)**, **number**.

![SyntaxHelperActionFormFieldsNewB](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SyntaxHelperActionFormFieldsNewB.png)

## Axonius REST API v2 Beta

This release includes the following schema changes in the Data Scopes API:

* The schema of the `_fields` parameters have changed when creating a new Data Scope. It is now an object instead of an array of values. **This change is not backwards-compatible.**
* The response schema of the different Data Scope endpoints have changed. All the `_fields` keys are now returned as objects, instead of an array of values.

**Early Adoption Program**
Interested in joining our Early Adoption Program? Open a [Zendesk ticket](http://support.axonius.com) and select the APIv2 option, to request access to the documentation.