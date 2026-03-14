# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/postgres/data-types/postgresql-data-types.md

# SnowConvert AI - PostgreSQL - Data types

Current Data types conversion for PostgreSQL to Snowflake.

## Applies to

* PostgreSQL
* Greenplum
* Netezza

Snowflake supports most basic [SQL data types](https://docs.snowflake.com/en/sql-reference/intro-summary-data-types) (with some restrictions) for use in columns, local variables, expressions, parameters, and any other appropriate/suitable locations.

## Numeric Data Types

| PostgreSQL | Snowflake |
| --- | --- |
| INT | INT |
| INT2 | SMALLINT |
| INT4 | INTEGER |
| INT8 | INTEGER |
| INTEGER | INTEGER |
| BIGINT | BIGINT |
| DECIMAL | DECIMAL |
| DOUBLE PRECISION | DOUBLE PRECISION |
| NUMERIC​ | NUMERIC |
| SMALLINT | SMALLINT |
| FLOAT | FLOAT |
| FLOAT4 | FLOAT4 |
| FLOAT8 | FLOAT8 |
| REAL | REAL​ |
| BIGSERIAL/SERIAL8 | INTEGER  *Note: Snowflake supports defining columns as IDENTITY, which automatically generates sequential values. This is the more concise and often preferred approach in Snowflake.* |

## Character Types

| PostgreSQL | Snowflake |
| --- | --- |
| VARCHAR | VARCHAR  *Note: VARCHAR holds Unicode UTF-8 characters. If no length is specified, the default is the maximum allowed length (16,777,216).* |
| CHAR | CHAR |
| CHARACTER | CHARACTER  *Note:* Snowflake’s CHARACTER is an alias for VARCHAR. |
| NCHAR | NCHAR |
| BPCHAR | VARCHAR  *Note: BPCHAR data type is **not supported** in Snowflake. VARCHAR is used instead. For more information please refer to* [*SSC-FDM-PG0002*](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md)*.* |
| CHARACTER VARYING | CHARACTER VARYING |
| NATIONAL CHARACTER | NCHAR |
| NATIONAL CHARACTER VARYING | NCHAR VARYING |
| TEXT | TEXT |
| [NAME](https://www.postgresql.org/docs/current/datatype-character.html) (Special character type) | VARCHAR |

## Boolean Types

| PostgreSQL | Snowflake |
| --- | --- |
| BOOL/BOOLEAN | BOOLEAN |

## Binary Types

| PostgreSQL | Snowflake |
| --- | --- |
| BYTEA | BINARY |

## Bit String Types

| PostgreSQL | Snowflake |
| --- | --- |
| BIT | CHARACTER |
| BIT VARYING | CHARACTER VARYING |
| VARBIT | CHARACTER VARYING |

## Date & Time Data

| PostgreSQL | Snowflake |
| --- | --- |
| DATE | DATE |
| TIME | TIME |
| TIME WITH TIME ZONE | TIME  *Note: Time zone not supported for time data type. For more information, please refer to* [*SSC-FDM-0005*](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/generalFDM.md)*.* |
| TIME WITHOUT TIME ZONE | TIME |
| TIMESTAMP | TIMESTAMP |
| TIMESTAMPTZ | TIMESTAMP_TZ |
| TIMESTAMP WITH TIME ZONE | TIMESTAMP_TZ |
| TIMESTAMP WITHOUT TIME ZONE | TIMESTAMP_NTZ |
| INTERVAL YEAR TO MONTH | VARCHAR  *Note: Data type is **not supported** in Snowflake. VARCHAR is used instead. For more information please refer to* [*SSC-EWI-0036*](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)*.* |
| INTERVAL DAY TO SECOND | VARCHAR  *Note: Data type is **not supported** in Snowflake. VARCHAR is used instead. For more information please refer to* [*SSC-EWI-0036*](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)*.* |

## Pseudo Types

| PostgreSQL | Snowflake |
| --- | --- |
| UNKNOWN | TEXT  *Note: Data type is **not supported** in Snowflake. TEXT is used instead. For more information please refer to* [*SSC-EWI-0036*](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md)*.* |

## Array Types

| PostgreSQL | Snowflake |
| --- | --- |
| type [] | ARRAY  *Note: Strongly typed array transformed to ARRAY without type checking. For more information please refer to* [*SSC-FDM-PG0016*](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md)*.* |

## Related EWIs

1. [SSC-FDM-PG0002](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md): Bpchar converted to varchar.
2. [SSC-FDM-PG0003](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md): Bytea Converted To Binary
3. [SSC-FDM-PG0014](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md): Unknown Pseudotype transformed to Text Type
4. [SSC-FDM-0005](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/generalFDM.md): TIME ZONE not supported for time data type.
5. [SSC-EWI-0036](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/generalEWI.md): Data type converted to another data type.
6. [SSC-EWI-PG0016](../../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/postgresqlEWI.md): Bit String Type converted to Varchar Type.
7. [SSC-FDM-PG0016](../../../general/technical-documentation/issues-and-troubleshooting/functional-difference/postgresqlFDM.md): *Strongly typed array transformed to ARRAY without type checking*.
