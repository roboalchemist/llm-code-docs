# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6132.md

# What's New in Axonius 6.1.32

#### Release Date: September 16th 2024

These Release Notes contain new features and enhancements added in version 6.1.32.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### New 'Domains and URLs' Asset Type

**New asset type added: 'Domains and URLs'**

* **Domains and URLs** assets are web-based assets including domains, URLs, and application details. Fetched from adapters such as BitSight Security Ratings and CyCognito platform.

### New Option to Expand Assets by Complex Field Data

A new [**Expand Assets by**](/docs/expanding-assets-by-a-complex-field) option was added to all Assets pages under the **Edit Table** (previously Edit Columns) menu. This enables users to select a complex field that is most interesting to them, and expand the rows in the table so that each row lists data from this complex field.
![expandby](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/expandby.png)

### 'Exists' Operator Supported in Data Refinement

Users can use the 'Exists' Operator in creating queries to refine the data displayed on asset pages.
![RefineDataExistsOperator](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RefineDataExistsOperator.png)

### Query Wizard Enhancements

### Query for Complex Field Values Inside Another Complex Field

It is now possible to use the Query Wizard to create a query for [values of a complex field that is nested in another complex field](/docs/asset-profile-page-complex-fields#nested-complex-fields). This allows users to filter and locate data with greater ease and precision.
![QW\_NestedComplex](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/QW_NestedComplex.png)

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Field Mapping and Data Transformations

Customers now have a central location where they can perform **Field Mappings and Data Transformations** to generate their own variations of the data fetched from adapters during the Discovery Cycle. Using the new [Field Mapping](/docs/managing-field-mapping) feature, it is possible to copy a source Axonius field to a target custom string field. It is also possible to perform additional manipulations on the mapped data using internal or user-defined [Data Transformation rules](/docs/managing-data-transformations).

### Adapter Interface

When configuring a single [Ingestion Rule](/docs/setting-adapter-ingestion-rules) for an adapter (**Adapter Profile> Ingestion Rules Configuration**), it is now possible to create a complex condition with an unlimited number of OR and AND operators and parentheses.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Deleting a Gateway

The system now prevents [deleting a Gateway](/docs/manage-gateways#deleting-a-gateway) that is in use by at least one Enforcement Action. This is in addition to the previously existing condition that a Gateway used to access adapter connections cannot be deleted.

### Backup Gateway Configuration

The capability has been added to [configure a backup gateway](/docs/installing-axonius-gateway). Multiple backups can be configured. If the primary gateway is unavailable for any reason, the system will automatically attempt to use one of the backup gateways. This improves reliability and stability of the system.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Updated Function

The following function used in a Dynamic Value statement was updated:

* **regex\_extract**
  * The [*regex\_extract* function](/docs/using-functions-and-keywords#using-the-regexextract-function) now enables specifying an index (optional).
    The *regex\_extract* function checks if a part of a specified field's string value matches the string in regex\_expression, and if it does, extracts from the field that part of the string so that it can be used to populate Custom Fields or Tags.

    * If  index is not specified, it captures the first occurrence of the string in the specified field.
    * If index is specified (optional), it extracts the occurrence of the string specified by the index (**0** is first occurrence, **1** is second, and so on).

  * Syntax: **regex\_extract** (\[field], "regex\_expression", index)

## Adapter and Enforcement Action Updates

### New Enforcement Actions

The following Enforcement Actions were added:

* [**Axonius - Suspend All Entities in User**](/docs/suspend-all-users) - Deactivates all entities in an Axonius user.