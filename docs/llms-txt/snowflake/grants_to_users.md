# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/grants_to_users.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/grants_to_users.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# GRANTS_TO_USERS view

This Account Usage view can be used to query the roles that have been granted to a user.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| CREATED_ON | TIMESTAMP_LTZ | Time and date (in the UTC time zone) when the role is granted. |
| DELETED_ON | TIMESTAMP_LTZ | Time and date (in the UTC time zone) when the role is revoked. |
| ROLE | VARCHAR | Identifier for the role granted to the user. |
| GRANTED_TO | VARCHAR | For this view, the value is `USER`. |
| GRANTEE_NAME | VARCHAR | Name of the user to whom the privilege is granted. |
| GRANTED_BY | VARCHAR | Identifier for the role that granted the privilege. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The GRANTS_TO_USERS view **does not** include grants of privileges and non-account roles to users. For that information, see the
  [GRANTS_TO_ROLES view](../organization-usage/grants_to_roles.md).
* This view records current grants and historical grants, including grants that were revoked and granted again. When a single grant occurs
  and as long as it remains active (that is, not revoked):

  * The view includes one row for the grant of the same role to the same user.
  * A regrant of the same role to the same user is not recorded as a new row. Instead, the DELETED_ON column remains NULL while the grant
    is active.
* When a grant is revoked from the user, the DELETED_ON column for the grant is updated from NULL to the timestamp when the grant was
  revoked.
* After revoking the role from the user, a grant of the same role to the same user is recorded in a new row. In this new row, the
  DELETED_ON column value is NULL because the grant is now active.
