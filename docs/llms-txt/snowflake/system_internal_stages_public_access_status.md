# Source: https://docs.snowflake.com/en/sql-reference/functions/system_internal_stages_public_access_status.md

Categories:
:   [System functions](../functions-system.md) (Information)

# SYSTEM$INTERNAL_STAGES_PUBLIC_ACCESS_STATUS

Checks to see whether public IP addresses are allowed to access the internal stage of the current Snowflake account on Microsoft Azure.

See also:
:   [SYSTEM$BLOCK_INTERNAL_STAGES_PUBLIC_ACCESS](system_block_internal_stages_public_access.md) , [SYSTEM$UNBLOCK_INTERNAL_STAGES_PUBLIC_ACCESS](system_unblock_internal_stages_public_access.md)

## Syntax

> ```sqlsyntax
> SYSTEM$INTERNAL_STAGES_PUBLIC_ACCESS_STATUS()
> ```

## Arguments

None.

## Returns

This function returns the following status messages:

| Status Message | Description |
| --- | --- |
| Public Access to internal stages is blocked | Indicates that the Azure settings that control access to the internal stage are currently blocking all public IP addresses. |
| Public Access to internal stages is unblocked | Indicates that at least some public IP addresses can access the internal stage. |

## Usage notes

* Only account administrators (i.e. users with the ACCOUNTADMIN role) can execute this function.
* This function can take a few minutes to finish executing.
* This function can be used with Snowflake accounts on Azure only. AWS and Google Cloud are not supported.

## Examples

> ```sqlexample
> USE ROLE accountadmin;
>
> SELECT SYSTEM$INTERNAL_STAGES_PUBLIC_ACCESS_STATUS();
> ```
>
> ```output
> Public Access to internal stages is blocked
> ```
