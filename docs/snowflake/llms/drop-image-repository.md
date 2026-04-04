# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-image-repository.md

# DROP IMAGE REPOSITORY

Removes the specified [image repository](../../developer-guide/snowpark-container-services/tutorials/tutorial-1.md) from
the current or specified schema.

See also:
:   [CREATE IMAGE REPOSITORY](create-image-repository.md) , [SHOW IMAGE REPOSITORIES](show-image-repositories.md)

## Syntax

```sqlsyntax
DROP IMAGE REPOSITORY [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the repository to drop.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Image repository |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Dropping an image repository while services are running that reference images in that repository can cause problems. Currently
  running service instances and jobs will continue to run, but any attempt to create a new service instance will fail.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the repository named `tutorial_repository`:

```sqlexample
DROP IMAGE REPOSITORY tutorial_repository;
```

```output
+-------------------------------------------+
| status                                    |
|-------------------------------------------|
| TUTORIAL_REPOSITORY successfully dropped. |
+-------------------------------------------+
```
