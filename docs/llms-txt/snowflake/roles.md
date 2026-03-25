# Source: https://docs.snowflake.com/en/connectors/postgres6/roles.md

# Source: https://docs.snowflake.com/en/connectors/mysql6/roles.md

# Source: https://docs.snowflake.com/en/user-guide/cleanrooms/v2/roles.md

# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/roles.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/roles.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# ROLES view

This Account Usage view can be used to query a list of all roles defined in the account. The data is retained for 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ROLE_ID | NUMBER | Internal/system-generated identifier for the role. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time (in the UTC time zone) when the role was created. |
| DELETED_ON | TIMESTAMP_LTZ | Date and time (in the UTC time zone) when the role was deleted. |
| NAME | VARCHAR | Name of the role. |
| COMMENT | VARCHAR | Comment for the role. |
| OWNER | VARCHAR | Role with the OWNERSHIP privilege on the object. |
| ROLE_TYPE | VARCHAR | Either `ROLE`, `DATABASE_ROLE`, `INSTANCE_ROLE`, or `APPLICATION_ROLE`. |
| ROLE_DATABASE_NAME | VARCHAR | Name of the database that contains the database role if the role is a database role. |
| ROLE_INSTANCE_ID | NUMBER | Internal/system-generated identifier for the class instance that the role belongs to. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| IS_FROM_ORGANIZATION_USER_GROUP | BOOLEAN | If TRUE, the role was imported from an [organization user group](../../user-guide/organization-users.md). |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view does not include database roles for databases created from shares.

### Internal Snowflake role for Snowsight

The first time [Snowsight](../../user-guide/ui-snowsight.md) is accessed in an account, Snowflake creates the internal APPADMIN and
WORKSHEETS_APP_RL roles to support the web interface. These roles are used to cache query results in an internal stage in your account.
This cached data is encrypted and protected by the key hierarchy for the account. The limited privileges granted to these internal roles
only allow Snowsight to access the internal stage to store those results. Thes roles cannot list objects in your account or access
data in your tables. For more information, see [Getting started with Snowsight](../../user-guide/ui-snowsight-gs.md).
