# Source: https://docs.snowflake.com/en/sql-reference/functions/current_version.md

Categories:
:   [Context functions](../functions-context.md) (General)

# CURRENT_VERSION

Returns the current Snowflake version.

See also:
:   [CURRENT_CLIENT](current_client.md)

## Syntax

```sqlsyntax
CURRENT_VERSION()
```

## Arguments

None.

## Returns

The data type of the returned value is VARCHAR.

The returned value contains four fields:

> ```sqlexample
> <major_version>.<minor_version>.<patch_version>  <internal_identifier>
> ```
>
> `major_version`
> :   Major version numbers change annually. For example, the major version for all releases in 2023 is 7. For all releases in 2022, the major version is 6.
>
> `minor_version`
> :   Minor version numbers change for each weekly release.
>
> `patch_version`
> :   Patch version numbers represent minor changes within a weekly release.
>
> `internal_identifier`
> :   This field is for internal use only.
>
> For example, for version 7.32.1, the major version is 7, the minor version is 32, and the patch version is 1.

## Usage notes

* This function returns version number information for Snowflake. To retrieve information about client versions,
  see [CURRENT_CLIENT](current_client.md).

## Examples

This shows the version of Snowflake on which the query is run:

> ```sqlexample
> SELECT CURRENT_VERSION();
> ```
>
> Output:
>
> ```sqlexample
> +-------------------+
> | CURRENT_VERSION() |
> |-------------------|
> | 7.32.1            |
> +-------------------+
> ```
