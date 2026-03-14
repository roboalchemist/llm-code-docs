# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-dbt-project.md

# ALTER DBT PROJECT

Modifies the properties of an existing [dbt project object](../../user-guide/data-engineering/dbt-projects-on-snowflake.md).

See also:
:   [CREATE DBT PROJECT](create-dbt-project.md), [EXECUTE DBT PROJECT](execute-dbt-project.md), [DESCRIBE DBT PROJECT](desc-dbt-project.md), [DROP DBT PROJECT](drop-dbt-project.md), [SHOW DBT PROJECTS](show-dbt-projects.md)

## Syntax

```sqlsyntax
ALTER DBT PROJECT [ IF EXISTS ] <name> RENAME TO <new_name>

ALTER DBT PROJECT <name> ADD VERSION [ <version_name_alias> ]
  FROM '<source_location>'

ALTER DBT PROJECT [ IF EXISTS ] <name> SET
  [ DBT_VERSION = '<version_number>' ]
  [ DEFAULT_TARGET = '<default_target>'' ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <integration_name> [, ... ] ) ]
  [ COMMENT = '<string_literal>' ]

ALTER DBT PROJECT [ IF EXISTS ] <name> UNSET
  [ DBT_VERSION ]
  [ DEFAULT_TARGET ]
  [ EXTERNAL_ACCESS_INTEGRATIONS ]
  [ COMMENT ]
```

## Parameters

`name`
:   Specifies the identifier for the dbt project object to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`RENAME TO new_name`
:   Changes the name of the dbt project object to `new_name`. The new identifier must be unique for the schema.

    For more information about identifiers, see [Identifier requirements](../identifiers-syntax.md).

    You can move the object to a different database and/or schema while optionally renaming the object. To do so, specify
    a qualified `new_name` value that includes the new database and/or schema name in the form
    `db_name.schema_name.object_name` or `schema_name.object_name`, respectively.

    > **Note:**
    >
    > * The destination database and/or schema must already exist. In addition, an object with the same name cannot already
    >   exist in the new location; otherwise, the statement returns an error.
    > * Moving an object to a managed access schema is prohibited unless the object owner (that is, the role that has
    >   the OWNERSHIP privilege on the object) also owns the target schema.

    When an object is renamed, other objects that reference it must be updated with the new name.

`ADD VERSION [ version_name_alias ]`
:   Creates a new version by incrementally increasing the current version identifier by one; for example, from `version$2` to `version$3`.

    The `version name alias` is optional and is a custom identifier that corresponds to the newly created version identifier. The `version name alias` must follow [Identifier requirements](../identifiers-syntax.md).

    `FROM 'source_location'`
    :   A string that specifies the location of the source files and version for the dbt project from which the version will be created.

        The dbt project source files can be in any one of the following locations:

        > * **A Git repository stage**, for example:
        >
        >   `'@my_db.my_schema.my_git_repository_stage/branches/my_branch/path/to/dbt_project_or_projects_parent'`
        >
        >   For more information about creating a Git repository object in Snowflake that connects a Git repository to a workspace for dbt Projects on Snowflake, see [Create a workspace connected to your Git repository](../../user-guide/tutorials/dbt-projects-on-snowflake-getting-started-tutorial.md). For more information about creating and managing a Git repository object and stage without using a workspace, see [Using a Git repository in Snowflake](../../developer-guide/git/git-overview.md) and [CREATE GIT REPOSITORY](create-git-repository.md).
        > * **An existing dbt project stage**, for example:
        >
        >   `'snow://dbt/my_db.my_schema.my_existing_dbt_project_object/versions/last'`
        >
        >   The version specifier is required and can be `last` (as shown in the previous example), `first`, or the specifier for any existing version in the form `version$<num>`. For more information, see [Versions for dbt project objects and files](../../user-guide/data-engineering/dbt-projects-on-snowflake-versions.md).
        > * **An internal named stage**, for example:
        >
        >   `'@my_db.my_schema.my_internal_named_stage/path/to/dbt_projects_or_projects_parent'`
        >
        >   Internal user stages and table stages aren’t supported.
        > * **A workspace for dbt on Snowflake**, for example:
        >
        >   `'snow://workspace/user$.public."my_workspace_name"/versions/live/path/to/dbt_projects_or_projects_parent'`
        >
        >   We recommend enclosing the workspace name in double quotes because workspace names are case-sensitive and can contain special characters.
        >
        >   The version specifier is required and can be `last`, `first`, `live`, or the specifier for any existing version in the form `version$<num>`. For more information, see [Versions for dbt project objects and files](../../user-guide/data-engineering/dbt-projects-on-snowflake-versions.md).

`SET ...`
:   Sets one or more specified properties or parameters for the dbt project object:

    `DBT_VERSION = 'version_number'`
    :   Specifies a version for the dbt Project.

        If no value is specified, the system uses version 1.9.4 by default.

    `DEFAULT_TARGET = default_target`
    :   Specifies the profile used for compilation and subsequent runs (for example, `prod`) of the dbt project object. This parameter can be overridden by using the [EXECUTE DBT PROJECT](execute-dbt-project.md)
        command with `ARGS = --target`.

    `EXTERNAL_ACCESS_INTEGRATIONS = ( integration_name [ , ... ] )`
    :   Specifies the external access integrations used to grant permissions to pull remote dependencies from dbt package hub or GitHub. When declared on an object, `dbt deps` will run automatically during deployment.
        For more information, see [Understand dependencies for dbt Projects on Snowflake](../../user-guide/data-engineering/dbt-projects-on-snowflake-dependencies.md).

    `COMMENT = 'string_literal'`
    :   Adds a comment or overwrites an existing comment for the dbt project object.

`UNSET ...`
:   Unsets one or more specified properties or parameters for the dbt project object to NULL or no value:

    * `DBT_VERSION`
    * `DEFAULT_TARGET`
    * `EXTERNAL_ACCESS_INTEGRATIONS`
    * `COMMENT`

    To unset multiple properties or parameters with a single ALTER statement, separate each property or parameter with a comma.

    When unsetting a property or parameter, specify only the property or parameter name (unless the syntax above indicates that you
    should specify the value). Specifying the value returns an error.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | dbt project | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

### Set a dbt version

The following example sets a new dbt version to a dbt project object:

```sqlexample
ALTER DBT PROJECT finance_analytics SET dbt_version = '1.10.15';
```

### Add a new version

The following example updates a Git repository object in Snowflake to fetch the latest code from the Git repository and then updates the
contents of the dbt project object by adding a new version:

```sqlexample
-- Update the Git repository object to fetch the latest code

ALTER GIT REPOSITORY sales_db.integrations_schema.sales_dbt_git_stage FETCH;

-- Add a new version to the dbt project object based on the updated Git repository object

ALTER DBT PROJECT sales_db.dbt_projects_schema.sales_model
  ADD VERSION
  FROM '@sales_db.integrations_schema.sales_dbt_git_stage/branches/main/sales_dbt_project';
```

### Set a default target and new external access integration

The following example updates an existing dbt project object with the following changes:

* Sets a default target that Snowflake uses when executing EXECUTE DBT PROJECT without specifying a `--target` argument. For example, if
  `DEFAULT_TARGET = 'prod'`, then a command such as `EXECUTE DBT PROJECT sales_db.dbt_projects_schema.sales_model RUN;` would
  automatically run using the `prod` target unless overridden by `ARGS = --target`.
* Assigns an external access integration for the dbt project to use.

  You can provide a single integration or a list: `EXTERNAL_ACCESS_INTEGRATIONS = ('integration1', 'integration2')`.

```sqlexample
ALTER DBT PROJECT sales_db.dbt_projects_schema.sales_model SET
  DEFAULT_TARGET = 'prod',
  EXTERNAL_ACCESS_INTEGRATIONS = ('my_external_access_integration');
```

### Revert to the system default version

The following example reverts the dbt project to the system default version, which is currently 1.9.4.

```sqlexample
ALTER DBT PROJECT finance_analytics UNSET DBT_VERSION;
```

```output
Statement executed successfully.
```
