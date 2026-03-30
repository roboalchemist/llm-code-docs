# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6129.md

# What's New in Axonius 6.1.29

#### Release Date: August 25th 2024

These Release Notes contain new features and enhancements added in version 6.1.29.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Asset Investigation

#### All Asset Fields Can be Tracked with Asset Investigation

The new [Asset Investigation Fields](/docs/asset-investigation-fields) system settings page allows admins to select any asset field to track as part of the Asset Investigation functionality. Admins can select to track up to 50 fields per asset type.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Ignore Empty Values

A new option [**Ignore Empty Values on Asset Fields**](/docs/config-ec-conditions) has been added to the Dynamic Value statement configuration. When enabled, the statement ignores empty (null) values in asset list fields and processes only the non-empty values. This prevents an empty value in a list field from causing the function to fail. When disabled, the statement will fail if any value is empty and revert to the fallback values.

For example, consider the following statement: concat(\[field1("aaa")], \[field2(null)], \[field3("ccc")]).

* When enabled, the result will be \["aaa", "ccc"], as the empty field2 is ignored.
* When disabled, the statement will fail due to the empty field2, and the system will revert to the fallback values.

![DynamicValueStatementbox(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DynamicValueStatementbox\(1\).png)

**Ignore Empty Values in Queries  Using  Data  Refinement**
In Enforcement Actions running on queries with data refinement, empty (null) asset list fields are now automatically ignored by the Dynamic Value statement. Previously, these empty null values could affect count operations. This update resolves that issue.

#### New Functions

The following functions can now be used in a Dynamic Value statement:

* **concat\_array**
  * The new [*concat\_array*](/docs/using-functions-and-keywords#using-the-concatarray-function) function joins one or more arrays into one array containing all values of the joined arrays.
    Syntax: **concat\_array** (list1 \[a, b, c], list2 \[d, e, f]) → \[a, b, c, d, e, f]
* **concat\_prefix**
  * The new [*concat\_prefix*](/docs/using-functions-and-keywords#using-the-concatprefix-function) function appends a specified string to each field value in an array list. This enables creating a tag list field that appends a label to each field value in the array.
    Syntax: **concat\_prefix** ("prefix", array.field.name)
    results in \["prefixfield1", "prefixfield2", ...,"prefixfieldN"]

## Data Analytics New Features and Enhancements

The order of creating a new [Data Analytics report](/docs/analyzing-query-data) has changed. The user first selects the contents of the report, including the module, query, fields, and how to split data in the table, and only then loads the report. This saves on load time, especially when there are many assets returned from the query and each asset has many fields.