# Source: https://docs.snowflake.com/en/sql-reference/ddl-other.md

# Account & session DDL

The following DDL commands are used to view and manage account-level and session operations, including:

* Viewing parameters at multiple levels in the system (account, session, object).
* Setting parameters at the account-level and within a session.
* Using a role, warehouse, database, or schema within a session.
* Using multi-statement transactions within a session.
* Setting and using SQL variables within a session.

## Account parameters & functions

|  |  |
| --- | --- |
| [ALTER ACCOUNT](sql/alter-account.md) | For setting parameters at the account-level; can only be performed by users with the ACCOUNTADMIN role. |
| [SHOW FUNCTIONS](sql/show-functions.md) | Displays system-defined functions, as well as any user-defined functions. |
| [SHOW PARAMETERS](sql/show-parameters.md) | For viewing parameter settings for the account. |

## Accounts

|  |  |
| --- | --- |
| [CREATE ACCOUNT](sql/create-account.md) | Used to create accounts in an organization. |
| [DROP ACCOUNT](sql/drop-account.md) |  |
| [SHOW ACCOUNTS](sql/show-accounts.md) | Lists the accounts in an organization. |
| [SHOW ORGANIZATION ACCOUNTS](sql/show-organization-accounts.md) | Use SHOW ACCOUNTS instead. |
| [SHOW REGIONS](sql/show-regions.md) |  |
| [UNDROP ACCOUNT](sql/undrop-account.md) |  |

## Managed accounts

|  |  |
| --- | --- |
| [CREATE MANAGED ACCOUNT](sql/create-managed-account.md) | Currently used to create [reader accounts](../user-guide/data-sharing-reader-create.md) for providers who wish to share data with non-Snowflake customers. |
| [DROP MANAGED ACCOUNT](sql/drop-managed-account.md) |  |
| [SHOW MANAGED ACCOUNTS](sql/show-managed-accounts.md) |  |

## Replication and failover/failback

|  |  |
| --- | --- |
| [ALTER CONNECTION](sql/alter-connection.md) |  |
| [CREATE CONNECTION](sql/create-connection.md) |  |
| [DROP CONNECTION](sql/drop-connection.md) |  |
| [SHOW CONNECTIONS](sql/show-connections.md) |  |
| [SHOW GLOBAL ACCOUNTS](sql/show-global-accounts.md) | Deprecated. Use [SHOW REPLICATION ACCOUNTS](sql/show-replication-accounts.md) instead. |
| [SHOW REPLICATION ACCOUNTS](sql/show-replication-accounts.md) |  |
| [SHOW REPLICATION DATABASES](sql/show-replication-databases.md) |  |

## Session parameters

|  |  |
| --- | --- |
| [ALTER SESSION](sql/alter-session.md) | For setting parameters within a session; can be performed by any user. |
| [SHOW PARAMETERS](sql/show-parameters.md) | For viewing parameter settings for the session (or account); can also be used to view parameter settings for a specified object. |

## Session context

|  |  |
| --- | --- |
| [USE ROLE](sql/use-role.md) | Specifies the primary role to use in the session. |
| [USE SECONDARY ROLES](sql/use-secondary-roles.md) | Specifies the secondary roles to use in the session. |
| [USE WAREHOUSE](sql/use-warehouse.md) | Specifies the virtual warehouse to use in the session. |
| [USE DATABASE](sql/use-database.md) | Specifies the database to use in the session. |
| [USE SCHEMA](sql/use-schema.md) | Specifies the schema to use in the session (specified schema must be in the current database for the session). |

See also:
:   [Context functions](functions-context.md)

## Queries

|  |  |
| --- | --- |
| [DESCRIBE RESULT](sql/desc-result.md) | Describes the columns in the results from a specified query (must have been executed within the last 24 hours). |
| [SHOW LOCKS](sql/show-locks.md) | For use with multi-statement transactions. |

## Session transactions

|  |  |
| --- | --- |
| [BEGIN](sql/begin.md) | For use with multi-statement transactions. |
| [COMMIT](sql/commit.md) | For use with multi-statement transactions. |
| [DESCRIBE TRANSACTION](sql/desc-transaction.md) | Describes the state of the transaction (e.g. committed, rolled back, running), etc. |
| [ROLLBACK](sql/rollback.md) | For use with multi-statement transactions. |
| [SHOW TRANSACTIONS](sql/show-transactions.md) | Lists all running transactions. |

## SQL variables

|  |  |
| --- | --- |
| [SET](sql/set.md) | For defining SQL variables in the session. |
| [SHOW VARIABLES](sql/show-variables.md) | For showing SQL variables in the session. |
| [UNSET](sql/unset.md) | For dropping SQL variables in the session. |
