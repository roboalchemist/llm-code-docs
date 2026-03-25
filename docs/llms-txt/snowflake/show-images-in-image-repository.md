# Source: https://docs.snowflake.com/en/sql-reference/sql/show-images-in-image-repository.md

# SHOW IMAGES IN IMAGE REPOSITORY

Lists the images in an [image repository](../../developer-guide/snowpark-container-services/working-with-registry-repository.md).

See also:
:   [CREATE IMAGE REPOSITORY](create-image-repository.md), [DROP IMAGE REPOSITORY](drop-image-repository.md),
    [SHOW IMAGE REPOSITORIES](show-image-repositories.md)

## Syntax

```sqlsyntax
SHOW IMAGES IN IMAGE REPOSITORY <name>
```

## Parameters

`name`
:   Name of the image repository.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Image repository |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The command output provides the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the image was uploaded to the image repository. |
| `image_name` | Image name |
| `tags` | Image tags |
| `digest` | SHA256 digest of the image |
| `image_path` | Image path (`database_name/schema_name/repository_name/image_name:image_tag`) |

## Usage notes

* The command doesn’t require a running warehouse to execute.
* The command only returns objects for which the current user’s current role has been granted at least one access privilege.
* The MANAGE GRANTS access privilege implicitly allows its holder to see every object in the account. By default, only the account
  administrator (users with the ACCOUNTADMIN role) and security administrator (users with the SECURITYADMIN role) have the
  MANAGE GRANTS privilege.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

List the images in the `tutorial_repository` image repository.

```sqlexample
SHOW IMAGES IN IMAGE REPOSITORY tutorial_db.data_schema.tutorial_repository;
```

```output
+-------------------------------+-----------------------+--------+-------------------------------------------------------------------------+--------------------------------------------------------------------------+
| created_on                    | image_name            | tags   | digest                                                                  | image_path                                                               |
|-------------------------------+-----------------------+--------+-------------------------------------------------------------------------+--------------------------------------------------------------------------|
| 2024-04-18 13:51:35.000 -0700 | my_echo_service_image | latest | sha256:70421668b2635b2996c6d5bc80627cf6d98c0716948b5f60d198d6411d4b4681 | tutorial_db/data_schema/tutorial_repository/my_echo_service_image:latest |
+-------------------------------+-----------------------+--------+-------------------------------------------------------------------------+--------------------------------------------------------------------------+
```
