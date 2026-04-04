# Source: https://docs.snowflake.com/en/sql-reference/account-usage/network_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# NETWORK_POLICIES view

This Account Usage view returns one row for each network policy in your account.

## Columns

| Column | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal system-generated identifier for network policy. |
| NAME | VARCHAR | Network policy name. |
| OWNER | VARCHAR | Name of role that owns the network policy. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| COMMENT | VARCHAR | Comment for the network policy (if any). |
| CREATED | TIMESTAMP_LTZ | Date and time that the network policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time that the network policy was last altered. |
| DELETED | TIMESTAMP_LTZ | Date and time that the network policy was dropped. |
| ALLOWED_IP_LIST | VARCHAR | List of allowed IPv4 addresses and CIDR block ranges in the corresponding network policy. |
| BLOCKED_IP_LIST | VARCHAR | List of blocked IPv4 addresses and CIDR block ranges in the corresponding network policy. |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
