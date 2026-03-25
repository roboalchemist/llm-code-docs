# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/masking_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/masking_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# MASKING_POLICIES view

This Account Usage view provides the masking policies in your account.

Each row in this view corresponds to a different masking policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| POLICY_NAME | VARCHAR | Name of the masking policy. |
| POLICY_ID | NUMBER | Internal/system-generated identifier for the masking policy. |
| POLICY_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema in which the policy resides. |
| POLICY_SCHEMA | VARCHAR | Schema to which the masking policy belongs. |
| POLICY_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database in which the policy resides. |
| POLICY_CATALOG | VARCHAR | Database to which the masking policy belongs. |
| POLICY_OWNER | VARCHAR | Name of the role that owns the masking policy. |
| POLICY_SIGNATURE | VARCHAR | Type signature of the masking policy’s arguments. |
| POLICY_RETURN_TYPE | VARCHAR | Return value data type. |
| POLICY_BODY | VARCHAR | Masking policy definition. |
| POLICY_COMMENT | VARIANT | Comments entered for the masking policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the masking policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the masking policy was dropped. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| OPTIONS | VARIANT | The value for the EXEMPT_OTHER_POLICIES property in the policy. If set to `TRUE`, the column returns `{ "EXEMPT_OTHER_POLICIES: "TRUE" }`. If the property is set to `FALSE` or not set at all, the column returns NULL. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
