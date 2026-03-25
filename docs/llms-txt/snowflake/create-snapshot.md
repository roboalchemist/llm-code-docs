# Source: https://docs.snowflake.com/en/sql-reference/sql/create-snapshot.md

# CREATE SNAPSHOT

> **Note:**
>
> This operation is not currently covered by the Service Level set forth in
> [Snowflake’s Support Policy and Service Level Agreement](https://www.snowflake.com/legal/support-policy-and-service-level-agreement/).

Creates or replaces a [snapshot of a block storage volume](../../developer-guide/snowpark-container-services/block-storage-volume.md) for a specified volume and service instance. The snapshot is created in the current schema.

See also:
:   [ALTER SNAPSHOT](alter-snapshot.md), [DESCRIBE SNAPSHOT](desc-snapshot.md), [DROP SNAPSHOT](drop-snapshot.md) , [SHOW SNAPSHOTS](show-snapshots.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNAPSHOT [ IF NOT EXISTS ] <name>
  FROM SERVICE <service_name>
  VOLUME "<volume_name>"
  INSTANCE <instance_id>
  [ COMMENT = '<string_literal>']
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , ... ] ) ]
```

## Required parameters

`name`
:   String that specifies the identifier (that is, name) for the snapshot; must be unique for the schema in which the snapshot is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`FROM SERVICE service_name`
:   Specifies the name of the service.

`VOLUME "volume_name"`
:   Specifies the name of the volume associated with the service. Snapshots can only be taken for block storage volumes (and not for local, memory, or stage volumes).

    Volume names are case-sensitive. Therefore, double quotes should always be used to match the corresponding name in the service specification.

`INSTANCE instance_id`
:   Index of the service instance. The service instance index starts at 0 and the range is `[0, ...,  MAX_INSTANCES - 1]`. You can call the [SYSTEM$GET_SERVICE_STATUS — Deprecated](../functions/system_get_service_status.md) function to get the relevant information.

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the service.

    Default: No value

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SNAPSHOT | Schema |  |
| OPERATE | Service |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Snowflake deletes job services approximately 10 minutes after its execution completes. To preserve the content of a block storage volume used by the job service, you must create a snapshot before Snowflake deletes the job. For example, you might use a stored procedure to first execute a job service and create a snapshot immediately following it.
* A schema cannot contain snapshots with the same name. When creating a snapshot, if a snapshot with the same name already exists in the schema, an error is returned and the snapshot is not created, unless the optional `OR REPLACE` keyword is included in the command, in which case Snowflake deletes the existing snapshot and creates a new snapshot.

  > **Important:**
  >
  > A snapshot deleted using the DROP SNAPSHOT or the CREATE OR REPLACE SNAPSHOT command cannot be restored. For volumes containing critical data, create new snapshots with unique names, such as using timestamps in the snapshot name.

## Examples

If you create a service with two instances (the number of containers isn’t relevant) with a volume named “data”, you would create a snapshot of the volume associated with the first instance using the following SQL:

```sqlexample
CREATE SNAPSHOT snapshot_0
  FROM SERVICE example_service
  VOLUME "data"
  INSTANCE 0
  COMMENT='new snapshot';
```

To create a snapshot of the volume associated with the second service instance, you specify `INSTANCE 1` in the preceding SQL.
