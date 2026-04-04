# Source: https://docs.snowflake.com/en/sql-reference/account-usage/join_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# JOIN_POLICIES view

This Account Usage view lists the [join policies](../../user-guide/join-policies.md) in your account.

Each row in this view corresponds to a different join policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| POLICY_ID | NUMBER | Internal/system-generated identifier for the policy. |
| POLICY_NAME | VARCHAR | Name of the policy. |
| POLICY_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema in which the policy resides. |
| POLICY_SCHEMA | VARCHAR | Schema that contains the policy. |
| POLICY_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database in which the policy resides. |
| POLICY_CATALOG | VARCHAR | Database to which the policy belongs. |
| POLICY_OWNER | VARCHAR | Name of the role that owns the policy. |
| POLICY_SIGNATURE | VARCHAR | Type signature of the policy’s arguments. |
| POLICY_RETURN_TYPE | VARCHAR | Return value data type. |
| POLICY_BODY | VARCHAR | Policy definition. |
| POLICY_COMMENT | VARIANT | Comments entered for the policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time when the policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time when the policy was last altered. |
| DELETED | TIMESTAMP_LTZ | Date and time when the policy was dropped. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

* Latency for the view can be up to 120 minutes (2 hours).
* The view only displays objects for which the current role for the session has been granted access privileges.

## Example

```sqlexample
SELECT policy_name, policy_body, created
  FROM SNOWFLAKE.ACCOUNT_USAGE.JOIN_POLICIES
  WHERE policy_name='JP2' AND created LIKE '2024-11-26%';
```

```output
+-------------+----------------------------------------------------------+-------------------------------+
| POLICY_NAME | POLICY_BODY                                              | CREATED                       |
|-------------+----------------------------------------------------------+-------------------------------|
| JP2         | CASE                                                     | 2024-11-26 11:22:54.848 -0800 |
|             |           WHEN CURRENT_ROLE() = 'ACCOUNTADMIN'           |                               |
|             |             THEN JOIN_CONSTRAINT(JOIN_REQUIRED => FALSE) |                               |
|             |           ELSE JOIN_CONSTRAINT(JOIN_REQUIRED => TRUE)    |                               |
|             |         END                                              |                               |
+-------------+----------------------------------------------------------+-------------------------------+
```
