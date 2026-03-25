# Source: https://docs.snowflake.com/en/sql-reference/functions/system_block_internal_stages_public_access.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$BLOCK_INTERNAL_STAGES_PUBLIC_ACCESS

Prevents all public traffic from accessing the internal stage of the current Snowflake account on Microsoft Azure.

This function uses settings for the internal stage’s Azure storage account to block public IP addresses. For details on which Azure settings
are affected, refer to [Blocking public access — Recommended](../../user-guide/private-internal-stages-azure.md).

> **Important:**
>
> Confirm that traffic via private connectivity is successfully reaching the internal stage before blocking public access. Blocking
> public access without configuring private connectivity can cause unintended disruptions, including interference with managed services like
> Azure Data Factory.

See also:
:   [SYSTEM$UNBLOCK_INTERNAL_STAGES_PUBLIC_ACCESS](system_unblock_internal_stages_public_access.md), [SYSTEM$INTERNAL_STAGES_PUBLIC_ACCESS_STATUS](system_internal_stages_public_access_status.md)

## Syntax

> ```sqlsyntax
> SYSTEM$BLOCK_INTERNAL_STAGES_PUBLIC_ACCESS()
> ```

## Arguments

None.

## Returns

This function returns the following status messages:

| Status Message | Description |
| --- | --- |
| Public Access to internal stages is blocked. Private link is required to connect to internal stages of this account. | Indicates that the function successfully blocked public access. |
| Network config is not found, Please contact support | Indicates that there is a problem with the system parameters. |
| Azure Error when attempting to block public access to internal stages. Please contact Snowflake support. | Indicates that the function was unable to change the Azure settings in order to block public access. |

## Usage notes

* Only account administrators (i.e. users with the ACCOUNTADMIN role) can execute this function.
* This function can take a few minutes to finish executing.
* This function can be used with Snowflake accounts on Azure only. AWS and Google Cloud are not supported.

## Examples

Block all public traffic trying to access the internal stage of an Azure account.

> ```sqlexample
> USE ROLE accountadmin;
>
> SELECT SYSTEM$BLOCK_INTERNAL_STAGES_PUBLIC_ACCESS();
> ```
