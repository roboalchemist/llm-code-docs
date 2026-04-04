# Source: https://docs.snowflake.com/en/sql-reference/sql/create-postgres-instance.md

# CREATE POSTGRES INSTANCE

Creates a new [Snowflake Postgres instance](../../user-guide/snowflake-postgres/about.md) or creates a
fork of an existing instance.

Forking creates a **full, independent copy** of an instance at a specific point in time using
[point-in-time recovery (PITR)](../../user-guide/snowflake-postgres/postgres-point-in-time-recovery.md).
This is useful for recovery, testing, or creating development environments from production data.

See also:
:   [ALTER POSTGRES INSTANCE](alter-postgres-instance.md), [DESCRIBE POSTGRES INSTANCE](desc-postgres-instance.md), [DROP POSTGRES INSTANCE](drop-postgres-instance.md), [SHOW POSTGRES INSTANCES](show-postgres-instances.md)

## Syntax

```sqlsyntax
CREATE POSTGRES INSTANCE <name>
  COMPUTE_FAMILY = '<compute_family>'
  STORAGE_SIZE_GB = <storage_gb>
  AUTHENTICATION_AUTHORITY = { POSTGRES | POSTGRES_OR_SNOWFLAKE }
  [ POSTGRES_VERSION = { 16 | 17 | 18 } ]
  [ NETWORK_POLICY = '<network_policy>' ]
  [ HIGH_AVAILABILITY = { TRUE | FALSE } ]
  [ STORAGE_INTEGRATION = '<storage_integration_name>' ]
  [ POSTGRES_SETTINGS = '<json_string>' ]
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , ... ] ) ]
```

The following syntax creates a fork of an existing instance at a point in time. The FORK clause uses
[point-in-time recovery](../../user-guide/snowflake-postgres/postgres-point-in-time-recovery.md)
with the same AT | BEFORE syntax as [Time Travel](../../user-guide/data-time-travel.md), but creates a
full physical copy of the Postgres instance:

```sqlsyntax
CREATE POSTGRES INSTANCE <name>
  FORK <source_instance>
  [ { AT | BEFORE } ( { TIMESTAMP => <timestamp> | OFFSET => <time_difference> } ) ]
  [ COMPUTE_FAMILY = '<compute_family>' ]
  [ STORAGE_SIZE_GB = <storage_gb> ]
  [ HIGH_AVAILABILITY = { TRUE | FALSE } ]
  [ POSTGRES_SETTINGS = '<json_string>' ]
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , ... ] ) ]
```

## Required parameters

`name`
:   Specifies the identifier (name) for the Postgres instance; must be unique for the account.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`COMPUTE_FAMILY = 'compute_family'`
:   Specifies the [instance size](../../user-guide/snowflake-postgres/postgres-instance-sizes.md) for the Postgres instance.

    Snowflake Postgres offers three tiers:

    * **Burstable** (BURST_XS, BURST_S, BURST_M): Cost-effective for development and intermittent workloads. Limited to
      100GB storage and does not support high availability.
    * **Standard** (STANDARD_M through STANDARD_24XL): Balanced CPU and memory for general-purpose workloads. Supports
      all features including high availability.
    * **Memory-optimized** (HIGHMEM_L through HIGHMEM_48XL): Higher memory-to-CPU ratio for memory-intensive queries
      and large indexes. Supports all features including high availability.

    > **Note:**
    >
    > Some features require specific compute families. For example, high availability (`HIGH_AVAILABILITY = TRUE`)
    > is only available on STANDARD and HIGHMEM instances, not on BURST instances.

`STORAGE_SIZE_GB = storage_gb`
:   Specifies the storage size in GB. Must be between 10 and 65,535.

    Storage is billed separately from compute based on the allocated amount. You can increase or decrease storage size later
    using ALTER POSTGRES INSTANCE. For more information about costs, see [Snowflake Postgres Cost Evaluation](../../user-guide/snowflake-postgres/postgres-cost.md).

    > **Note:**
    >
    > When you decrease the storage size, you can’t set it too close to current disk usage. The new size must be
    > at least 1.4x the disk space currently in use. That way, there’s still room to add more data without
    > triggering an automatic storage increase.

`AUTHENTICATION_AUTHORITY = { POSTGRES | POSTGRES_OR_SNOWFLAKE }`
:   Specifies the authentication method for the instance. POSTGRES indicates that only Postgres user passwords can be used.
    POSTGRES_OR_SNOWFLAKE also allows the use of short-lived access token passwords. See
    [Snowflake Token Authentication for Snowflake Postgres](../../user-guide/snowflake-postgres/postgres-token-auth.md) for more details.

## Optional parameters

`POSTGRES_VERSION = { 16 | 17 | 18 }`
:   Specifies the major version of Postgres to use.

    While the latest version includes new features and improvements, you might choose an earlier version for application
    compatibility or to match existing instances. You can upgrade to a newer version later using ALTER POSTGRES INSTANCE.

    Default: The latest Postgres version.

`NETWORK_POLICY = 'network_policy'`
:   Specifies the [network policy](../../user-guide/snowflake-postgres/postgres-network.md) to use for the instance.
    To specify this parameter, you must have been granted the USAGE privilege on the network policy object.

    Default: No network policy is applied.

    > **Important:**
    >
    > Without a network policy, the instance can’t accept incoming connections. You can still view the instance
    > using SHOW and DESCRIBE commands, but can’t connect to the Postgres database until you attach a network
    > policy using ALTER POSTGRES INSTANCE.

`STORAGE_INTEGRATION = 'storage_integration_name'`
:   Attaches a storage integration of type `POSTGRES_EXTERNAL_STORAGE` to the Postgres instance,
    enabling the pg_lake extension to access data in external object storage. For the complete setup
    procedure, see [Configuring S3 Storage for pg_lake](../../user-guide/snowflake-postgres/postgres-pg_lake.md).

    You can also attach or remove a storage integration later using [ALTER POSTGRES INSTANCE](alter-postgres-instance.md).

    [Preview Feature](../../release-notes/preview-features.md) — Open

    Available to all accounts.

    Default: No storage integration is attached.

`HIGH_AVAILABILITY = { TRUE | FALSE }`
:   Specifies whether to enable [high availability](../../user-guide/snowflake-postgres/high-availability.md) for the instance.

    High availability provisions a standby instance in a separate availability zone for automatic failover. This minimizes
    downtime if the primary becomes unavailable. Without HA, recovery requires restoring from backup, which can take hours
    for large or active instances. Note that enabling or disabling HA later using ALTER POSTGRES INSTANCE requires a
    [maintenance operation](../../user-guide/snowflake-postgres/managing-instances.md).

    > **Important:**
    >
    > Burstable instance sizes (BURST_XS, BURST_S, BURST_M) do not support high availability.

    Default: `FALSE`

`POSTGRES_SETTINGS = 'json_string'`
:   Specifies custom [Postgres server settings](../../user-guide/snowflake-postgres/postgres-server-settings.md) for the instance
    in JSON format:

    ```none
    '{"component:name" = "value", ...}'
    ```

    The format uses `component:name` where `component` is either `postgres` (for PostgreSQL server settings) or
    `pgbouncer` (for connection pooler settings). For example:

    ```none
    '{"postgres:work_mem" = "128MB", "pgbouncer:default_pool_size" = "200"}'
    ```

    See [Snowflake Postgres Server Settings](../../user-guide/snowflake-postgres/postgres-server-settings.md) for available settings.

    Default: No custom Postgres configuration parameters are set.

`COMMENT = 'string_literal'`
:   Specifies a comment for the Postgres instance.

    Comments are useful for documenting the purpose or ownership of an instance, such as “Production instance for billing
    service” or “QA environment for team X”. Unlike tags, comments are free-form text and not used for organization or
    cost tracking.

    Default: No value.

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Fork parameters

Forking a Snowflake Postgres instance creates an identical copy with all the same
schema objects and table data. You can also specify a point in time so that the forked
instance reflects a previous state of the instance. That way, you can recover from data
integrity issues such as accidentally dropping objects. You can also explore scenarios
in a development and test environment, such as trying different instance configurations
with identical data. For more information, see
[Snowflake Postgres point-in-time recovery](../../user-guide/snowflake-postgres/postgres-point-in-time-recovery.md).

`FORK source_instance`
:   Creates a new instance as a fork (copy) of the specified source instance.

`{ AT | BEFORE } ( { TIMESTAMP => timestamp | OFFSET => time_difference } )`
:   Specifies the point in time to fork from. You can’t fork from a point in time more than 10 days
    in the past. The timestamp or offset must fall within the 10-day Postgres data retention period.

    The [AT | BEFORE](../constructs/at-before.md) clause accepts one of the following parameters:

    `TIMESTAMP => timestamp`
    :   Specifies an exact date and time to use for Time Travel. The value must be explicitly cast to a
        TIMESTAMP, TIMESTAMP_LTZ, TIMESTAMP_NTZ, or TIMESTAMP_TZ data type.

    `OFFSET => time_difference`
    :   Specifies the difference in seconds from the current time, in the form `-N` where `N`
        can be an integer or arithmetic expression (for example, `-120` is 120 seconds, `-30*60` is 30 minutes).

    Default: Uses the current time.

When creating a fork, the following parameters are optional and default to the values from the source instance:

* `COMPUTE_FAMILY`
* `STORAGE_SIZE_GB`
* `HIGH_AVAILABILITY`
* `POSTGRES_SETTINGS`

## Output

When you create a new instance, the command returns one row with the following columns:

| Column | Description |
| --- | --- |
| `status` | Status of the create operation. |
| `host` | Hostname for connecting to the instance. |
| `access_roles` | User names and passwords for the `snowflake_admin` and `application` roles. |
| `default_database` | Default database for the instance. |

> **Important:**
>
> The `access_roles` column contains credentials that you can’t retrieve later. Save these details in a secure location.

When you create a fork, the command returns one row with only `status` and `host` columns. The fork uses
the same credentials that the source instance had, at the point in time that the fork corresponds to.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE POSTGRES INSTANCE | Account | By default, only the ACCOUNTADMIN role has this privilege. |
| USAGE | Network policy | Required only if specifying a NETWORK_POLICY. |
| USAGE | Storage integration | Required only if specifying a STORAGE_INTEGRATION. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Creating a new instance takes some time to complete. The instance displays its current
  [state](../../user-guide/snowflake-postgres/managing-instances.md) while it’s being built. You can use the DESC POSTGRES INSTANCE
  command to track the status during the instance setup.
* When you create a fork, you don’t specify or see the credentials. That’s because the fork uses
  the same credentials that the source instance had, at the point in time that the fork corresponds
  to. You can regenerate credentials for the forked instance later, if you need to provide access to
  a different set of users than on the original instance.
* The time needed to create a fork depends on the amount of data in the source instance. Larger databases with more
  data take longer to fork. The compute family (instance size) of the source doesn’t significantly affect fork duration.
* Forking performs a complete data copy using backup and write-ahead log (WAL) replay, which means
  that the forked instance is entirely separate: dropping the source instance does not affect any
  forks that you created from it.

  > **Note:**
  >
  > Postgres forking isn’t part of the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature, which uses
  > zero-copy technology for tables. However, forking uses the same AT | BEFORE syntax to specify a point in time.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a basic Postgres instance:

```sqlexample
CREATE POSTGRES INSTANCE my_postgres
  COMPUTE_FAMILY = 'STANDARD_S'
  STORAGE_SIZE_GB = 50
  AUTHENTICATION_AUTHORITY = POSTGRES;
```

Create a Postgres instance with high availability and a network policy:

```sqlexample
CREATE POSTGRES INSTANCE prod_postgres
  COMPUTE_FAMILY = 'STANDARD_M'
  STORAGE_SIZE_GB = 500
  AUTHENTICATION_AUTHORITY = POSTGRES
  POSTGRES_VERSION = 17
  HIGH_AVAILABILITY = TRUE
  NETWORK_POLICY = 'my_network_policy'
  COMMENT = 'Production Postgres instance';
```

Create an instance and configure a network policy later:

```sqlexample
-- Step 1: Create instance without network policy
CREATE POSTGRES INSTANCE my_postgres
  COMPUTE_FAMILY = 'STANDARD_S'
  STORAGE_SIZE_GB = 50
  AUTHENTICATION_AUTHORITY = POSTGRES;

-- Step 2: Monitor instance creation
DESCRIBE POSTGRES INSTANCE my_postgres
  ->> SELECT "property", "value"
      FROM $1
      WHERE "property" IN ('name', 'state', 'host');

-- Step 3: Once READY, attach network policy to enable connections
ALTER POSTGRES INSTANCE my_postgres
  SET NETWORK_POLICY = 'my_network_policy';

-- Step 4: Now you can connect to the Postgres database using the host and credentials
-- from the CREATE output
```

Create a fork of an existing instance:

```sqlexample
CREATE POSTGRES INSTANCE my_fork
  FORK my_source_instance;
```

Create a fork at a specific point in time:

```sqlexample
CREATE POSTGRES INSTANCE my_fork
  FORK my_source_instance
  AT (TIMESTAMP => '2025-01-15 12:00:00'::TIMESTAMP_NTZ);
```

Create a fork from 2 hours ago with a different instance size:

```sqlexample
CREATE POSTGRES INSTANCE my_fork
  FORK my_source_instance
  AT (OFFSET => -7200)
  COMPUTE_FAMILY = 'STANDARD_L';
```

Create a fork for reporting with a larger instance size and different storage:

```sqlexample
-- Fork production instance for reporting workload
CREATE POSTGRES INSTANCE reporting_instance
  FORK prod_instance
  COMPUTE_FAMILY = 'HIGHMEM_XL'
  STORAGE_SIZE_GB = 500
  COMMENT = 'Dedicated reporting instance to offload analytics queries';
```

Create a fork at midnight UTC for daily testing:

```sqlexample
-- Fork at start of day (midnight UTC)
CREATE POSTGRES INSTANCE daily_test_instance
  FORK prod_instance
  AT (TIMESTAMP => '2026-02-05 00:00:00'::TIMESTAMP_NTZ);
```

Create a development fork with HA disabled to reduce costs:

```sqlexample
CREATE POSTGRES INSTANCE dev_instance
  FORK prod_instance
  COMPUTE_FAMILY = 'STANDARD_S'
  STORAGE_SIZE_GB = 100
  HIGH_AVAILABILITY = FALSE
  COMMENT = 'Development environment from prod data';
```

Recover from accidental data deletion using a fork from before the incident:

```sqlexample
-- Recover by forking from 30 minutes ago
CREATE POSTGRES INSTANCE recovered_instance
  FORK damaged_instance
  AT (OFFSET => -1800)
  COMMENT = 'Recovery fork from before data deletion';
```
