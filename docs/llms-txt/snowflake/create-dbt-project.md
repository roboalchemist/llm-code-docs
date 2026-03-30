# Source: https://docs.snowflake.com/en/sql-reference/sql/create-dbt-project.md

# CREATE DBT PROJECT

Creates a new [dbt project object](../../user-guide/data-engineering/dbt-projects-on-snowflake.md) or replaces an existing dbt project. Running CREATE DBT PROJECT with the OR REPLACE option resets the version identifier to `version$1` and removes all version name aliases. For more information, see [Versions for dbt project objects and files](../../user-guide/data-engineering/dbt-projects-on-snowflake-versions.md).

See also:
:   [ALTER DBT PROJECT](alter-dbt-project.md), [DESCRIBE DBT PROJECT](desc-dbt-project.md), [EXECUTE DBT PROJECT](execute-dbt-project.md), [SHOW DBT PROJECTS](show-dbt-projects.md), [DROP DBT PROJECT](drop-dbt-project.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] DBT PROJECT [ IF NOT EXISTS ] <name>
  [ FROM '<source_location>' ]
  [ COMMENT = '<string_literal>' ]
  [ DBT_VERSION = <version_number> ]
  [ DEFAULT_TARGET = <default_target> ]
  [ EXTERNAL_ACCESS_INTEGRATIONS = ( <integration_name> [ , ... ] ) ]
```

## Parameters

`name`
:   String that specifies the identifier (that is, the name) for the dbt project object within Snowflake; must be unique for the schema in which the dbt project is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`FROM 'source_location'`
:   A string that specifies the location in Snowflake of the source files for the dbt project object. This can be a parent directory that contains multiple dbt projects, or a specific subdirectory that contains a dbt project and `dbt_project.yml` file.

    If the specified location doesn’t contain a `dbt_project.yml` file, the [EXECUTE DBT PROJECT](execute-dbt-project.md) command must use the PROJECT_ROOT parameter to specify the subdirectory path to a `dbt_project.yml` file.

    If no value is specified, Snowflake creates an empty dbt project.

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

    Default: No value

`COMMENT = 'string_literal'`
:   Specifies a comment for the dbt project object.

    Default: No value

`DBT_VERSION = version_number`
:   Specifies a version for the dbt Project.

    Default: `1.9.4`, unless an administrator set a version using the [DEFAULT_DBT_VERSION](../parameters.md) account parameter.

`DEFAULT_TARGET = default_target`
:   Specifies the profile used for compilation and subsequent runs (for example, `prod`) of the dbt project object. You can override this parameter by using the [EXECUTE DBT PROJECT](execute-dbt-project.md)
    command with `ARGS = --target`.

    Default: No value

`EXTERNAL_ACCESS_INTEGRATIONS = ( integration_name [ , ... ] )`
:   Specifies the external access integration used to grant permissions to pull remote dependencies from dbt package hub or GitHub. When declared on an object, `dbt deps` will run automatically during deployment.
    For more information, see [Understand dependencies for dbt Projects on Snowflake](../../user-guide/data-engineering/dbt-projects-on-snowflake-dependencies.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| CREATE DBT PROJECT | Schema |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

* Create a dbt project object from a Git repository stage in Snowflake
* Create a dbt project object from a subdirectory within a Git repository stage in Snowflake
* Create a dbt project object from a specific version of an existing dbt project object
* Create a dbt project object from a workspace that contains multiple dbt projects

### Create a dbt project object from a Git repository stage in Snowflake

Create a dbt project object named `sales_dbt_model` from dbt project files in a Git repository stage. This example references the `main`
branch of a Git repository stage named `sales_dbt_git_stage` in Snowflake, where the project’s `dbt_project.yml` file is saved in the
repository root. The command also sets the default target used when executing dbt commands and specifies the external access integrations required
by the project.

```sqlexample
CREATE DBT PROJECT sales_db.dbt_projects_schema.sales_model
  FROM '@sales_db.integrations_schema.sales_dbt_git_stage/branches/main'
  DEFAULT_TARGET = 'prod'
  EXTERNAL_ACCESS_INTEGRATIONS = 'my_external_access_integration'
  COMMENT = 'Generates sales data models.';
```

### Create a dbt project object from a subdirectory within a Git repository stage in Snowflake

Create a dbt project object named `sw_region_sales_model` from a subdirectory inside a Git repository stage that contains multiple dbt projects.
The example references the `main` branch of a Git repository stage named `sales_dbt_git_stage` in Snowflake, where the project’s
`dbt_project.yml` file is saved in the `sw_region_dbt_project` subdirectory of the `sales_dbt_projects_parent` directory.

This example also sets the following properties:

* dbt version
* Default execution target (for example, `prod` or `dev`) used by dbt commands executed through Snowflake.
* External access integrations the dbt Project is permitted to use to pull remote dependencies from dbt package hub or Github.

```sqlexample
CREATE DBT PROJECT sales_db.dbt_projects_schema.sw_region_sales_model
  FROM '@sales_db.integrations_schema.sales_dbt_git_stage/branches/main/sales_dbt_projects_parent/sw_region_dbt_project'
  DBT_VERSION = '1.10.15'
  DEFAULT_TARGET = 'prod'
  EXTERNAL_ACCESS_INTEGRATIONS = 'my_external_access_integration'
  COMMENT = 'Generates data models for SW sales region.';
```

### Create a dbt project object from a specific version of an existing dbt project object

Create a new dbt project object named `sales_model_nw_region` from `version$2` of the existing `sales_model` dbt project.

This example also sets a default execution target using DEFAULT_TARGET, and specifies allowed external access integrations using EXTERNAL_ACCESS_INTEGRATIONS.

```sqlexample
CREATE DBT PROJECT sales_db.dbt_projects_schema.sales_model_nw_region
  FROM 'snow://dbt/sales_db.dbt_projects_schema.sales_model/versions/version$2'
  DEFAULT_TARGET = 'prod'
  EXTERNAL_ACCESS_INTEGRATIONS = (my_ext_integration_1, my_ext_integration_2)
  COMMENT = 'Generates data models for the NW sales region.';
```

### Create a dbt project object from a workspace that contains multiple dbt projects

Create a new dbt project object named `sales_model_from_workspace` from the live version of a workspace containing multiple dbt project directories. “My dbt
Project Workspace” inside the user’s personal database. This is useful when the workspace has several subprojects and you want to create a dbt project object
from a specific subdirectory. Workspaces are case-sensitive and can include special characters, so we recommend enclosing the workspace name in double quotes.

```sqlexample
CREATE DBT PROJECT sales_db.dbt_projects_schema.sales_model_from_workspace
  FROM 'snow://workspace/user$.public."My dbt Project Workspace"/versions/live/project2'

EXECUTE DBT PROJECT sales_db.dbt_projects_schema.sales_model_from_workspace
  ARGS = 'run --target prod';
```
