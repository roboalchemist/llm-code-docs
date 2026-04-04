# Source: https://docs.snowflake.com/en/sql-reference/account-usage/aggregation_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# AGGREGATION_POLICIES view

This Account Usage view provides the aggregation policies in your account.

Each row in this view corresponds to a different aggregation policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| POLICY_NAME | VARCHAR | Name of the aggregation policy. |
| POLICY_ID | NUMBER | Internal/system-generated identifier for the aggregation policy. |
| POLICY_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema in which the policy resides. |
| POLICY_SCHEMA | VARCHAR | Schema that contains the aggregation policy. |
| POLICY_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database in which the policy resides. |
| POLICY_CATALOG | VARCHAR | Database to which the aggregation policy belongs. |
| POLICY_OWNER | VARCHAR | Name of the role that owns the aggregation policy. |
| POLICY_SIGNATURE | VARCHAR | Type signature of the aggregation policy’s arguments. |
| POLICY_RETURN_TYPE | VARCHAR | Return value data type. |
| POLICY_BODY | VARCHAR | Aggregation policy definition. |
| POLICY_COMMENT | VARIANT | Comments entered for the aggregation policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the aggregation policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time when the aggregation policy was last altered. |
| DELETED | TIMESTAMP_LTZ | Date and time when the aggregation policy was dropped. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).
* The view only displays objects for which the current role for the session has been granted access privileges.
