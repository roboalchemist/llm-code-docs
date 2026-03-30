# Source: https://docs.snowflake.com/en/sql-reference/classes/custom_classifier/methods/delete_category.md

# `custom_classifier`!DELETE_CATEGORY

See also:
:   [Using custom classifiers to implement custom semantic categories](../../../../user-guide/classify-custom-using.md)

Deletes the specified semantic category with its associated privacy category, regular expression, and comment from the instance.

## Syntax

```sqlsyntax
<custom_classifier>!DELETE_CATEGORY( '<semantic_category>' )
```

## Arguments

`semantic_category`
:   Specifies the identifier (name) for the semantic category that you added to the instance when calling the
    [custom_classifier!ADD_REGEX](add_regex.md) method.

## Output

Returns a status message indicating the deletion of the specified semantic category.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Instance role | Object | Notes |
| --- | --- | --- |
| `custom_classifier`!PRIVACY_USER | The custom classification instance. | The account role that calls this method must be granted this instance role on the custom classifier.  By default, the account role used to create the instance can call this method. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Call the method in a separate SQL statement (no method chaining).

## Examples

Delete a category from the `medical_codes` instance:

```sqlexample
CALL medical_codes!DELETE_CATEGORY('IC_10_CODES');
```

Returns:

```output
+------------------------------+
|       DELETE_CATEGORY        |
+------------------------------+
| Deleted category IC_10_CODES |
+------------------------------+
```
