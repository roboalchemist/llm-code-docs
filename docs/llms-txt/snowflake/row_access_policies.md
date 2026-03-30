# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/row_access_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/row_access_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# ROW_ACCESS_POLICIES view

This Account Usage view displays a row for each row access policy defined in your account.

Each row corresponds to a different row access policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| POLICY_NAME | VARCHAR | Name of the row access policy. |
| POLICY_ID | NUMBER | Internal/system-generated identifier for the row access policy. |
| POLICY_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema in which the policy resides. |
| POLICY_SCHEMA | VARCHAR | Schema to which the row access policy belongs. |
| POLICY_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database in which the policy resides. |
| POLICY_CATALOG | VARCHAR | Database to which the row access policy belongs. |
| POLICY_OWNER | VARCHAR | Name of the role that owns the row access policy. |
| POLICY_SIGNATURE | VARCHAR | Type signature of the row access policy’s arguments. |
| POLICY_RETURN_TYPE | VARCHAR | Return value data type. |
| POLICY_BODY | VARCHAR | Row access policy definition. |
| POLICY_COMMENT | VARIANT | Comments entered for the row access policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the row access policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the row access policy was dropped. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| OPTIONS | VARIANT | The value for the EXEMPT_OTHER_POLICIES property in the policy. If set to `TRUE`, the column returns `{ "EXEMPT_OTHER_POLICIES: "TRUE" }`. If the property is set to `FALSE` or not set at all, the column returns NULL. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only returns rows if at least one row access policy has been created.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Example

Obtain all of the row access policies created in your account, ordered by the timestamp on which the policy was created:

> ```sqlexample
> select policy_name, policy_signature, created
> from row_access_policies
> order by created
> ;
> ```
