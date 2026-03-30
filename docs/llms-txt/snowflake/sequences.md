# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/sequences.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/sequences.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/sequences.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SEQUENCES view

This Account Usage view displays a row for each sequence defined in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SEQUENCE_ID | NUMBER | Internal/system-generated identifier for the sequence. |
| SEQUENCE_NAME | VARCHAR | Name of the sequence. |
| SEQUENCE_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the sequence. |
| SEQUENCE_SCHEMA | VARCHAR | Schema that the sequence belongs to. |
| SEQUENCE_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the sequence. |
| SEQUENCE_CATALOG | VARCHAR | Database that the sequence belongs to. |
| SEQUENCE_OWNER | VARCHAR | Name of the role that owns the sequence. |
| DATA_TYPE | VARCHAR | Data type of the sequence. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of the data type of the sequence. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of the numeric precision of the data type of the sequence. |
| NUMERIC_SCALE | NUMBER | Scale of the data type of the sequence. |
| START_VALUE | VARCHAR | Initial value of the sequence. |
| MINIMUM_VALUE | VARCHAR | Not applicable for Snowflake. |
| MAXIMUM_VALUE | VARCHAR | Not applicable for Snowflake. |
| NEXT_VALUE | VARCHAR | Next value that the sequence will produce. |
| INCREMENT | VARCHAR | Increment of the sequence generator. |
| CYCLE_OPTION | VARCHAR | Not applicable for Snowflake. |
| ORDERED | VARCHAR | If `YES`, the sequence has the ORDER property. If `NO`, the sequence has the NOORDER property. |
| CREATED | TIMESTAMP_LTZ | Date and time when the sequence was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the sequence was dropped. |
| COMMENT | VARCHAR | Comment for the sequence. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view does not recognize the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command
  executed by a user who holds the MANAGE GRANTS privilege.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
