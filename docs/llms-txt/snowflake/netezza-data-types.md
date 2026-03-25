# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/postgres/data-types/netezza-data-types.md

# SnowConvert AI - Netezza - Data types

Current Data types conversion for Netezza to Snowflake.

The following data types are specific to [Netezza](https://www.ibm.com/docs/en/netezza?topic=vc-data-types-aliases). For more information please refer to the [PostgreSQL & based languages data types documentation](postgresql-data-types.md).

| Netezza | Snowflake |
| --- | --- |
| DOUBLE | DOUBLE |
| BYTEINT | BYTEINT |
| INT1 | BYTEINT    *Notes: This type is an alias* of BYTEINT at Netezza. |
| TIMESPAN | *VARCHAR*    *Notes: This type is an alias* of INTERVAL at Netezza*. This data type is **not supported** in Snowflake. VARCHAR is used instead. For more information please refer to* [*SSC-EWI-0036*](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)*.* |

## Related EWIs

1. [SSC-EWI-0036](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Data type converted to another data type.
