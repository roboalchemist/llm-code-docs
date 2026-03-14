# Source: https://docs.snowflake.com/en/sql-reference/stored-procedures/deregister_extension.md

# DEREGISTER_EXTENSION

Deregisters an extension from the Trust Center.

For more information, see [Using Trust Center extensions](../../user-guide/trust-center/trust-center-extensions.md).

## Syntax

```sqlsyntax
SNOWFLAKE.TRUST_CENTER.DEREGISTER_EXTENSION(
  '<source_type>',
  '<source>',
  '<extension_name>')

SNOWFLAKE.TRUST_CENTER.DEREGISTER_EXTENSION(
  '<source_type>',
  '<source>',
  '<extension_id>')
```

## Arguments

`'source_type'`
:   The source type of the extension. Possible values are `LISTING` and
    `APPLICATION PACKAGE`.

`'source'`
:   The listing ID or the name of the application package.

    You can run the [SHOW APPLICATIONS](../sql/show-applications.md) SQL command to see all of the
    Snowflake Native Apps that are installed in your account, including the extensions. The listing ID
    or application package for an extension is shown in the `source` column in the output.

`'extension_name'`
:   Name of the extension.

    In the output for the SHOW APPLICATIONS SQL command, the extension names are shown in the
    `name` column.

`'extension_id'`
:   The identifier of the extension.

    To find the identifiers for registered extensions, query the
    [EXTENSIONS view](../trust_center/extensions.md).

## Returns

Returns a VARCHAR value:

* If deregistration is successful, the VARCHAR value contains the following message:

  ```output
  Extension is successfully deregistered.
  ```

* If deregistration fails, the VARCHAR value contains an error message. Deregistration can fail for the following reasons:

  * The specified `source_type` is invalid.
  * The specified `source` is invalid.
  * The specified `extension_name` is invalid.
  * The specified `extension_id` is invalid.
  * The combination of the `source_type`, `source`, and `extension_name` or
    `extension_id` is invalid.

  The following example shows an error message that is returned for an invalid `extension_id`:

  ```output
  Either the extension with given id does not exist or it is already deregistered
  ```

## Examples

The following example deregisters an extension that is named `tc_extension`:

```sqlexample
CALL SNOWFLAKE.TRUST_CENTER.DEREGISTER_EXTENSION(
  'LISTING',
  'GZ13Z1VEWNG',
  'tc_extension');
```
