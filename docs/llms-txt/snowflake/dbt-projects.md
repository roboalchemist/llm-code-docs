# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/data-pipelines/dbt-projects.md

# Managing dbt Projects on Snowflake using Snowflake CLI

> **Note:**
>
> The dbt Projects on Snowflake features in Snowflake CLI are available only in version 3.13.0 or later.

You can use Snowflake CLI to manage dbt projects with the following operations:

* Deploying a dbt project object
* Listing all available dbt project objects
* Executing a dbt project object command
* Describing a dbt project object
* Dropping a dbt project object

## Deploying a dbt project object

The [snow dbt deploy](../command-reference/dbt-commands/deploy.md) command uploads local files to a temporary stage and creates a new dbt project object, updates it by
making a new version, or completely recreates it. A valid dbt project must contain two files:

* `dbt_project.yml`: A standard dbt configuration file that specifies the profile to use.
* `profiles.yml`: A dbt connection profile definition referenced in `dbt_project.yml`. `profiles.yaml` must define the database, role, schema, and type.

  * By default, dbt Projects on Snowflake uses your target schema (`target.schema`) specified from your dbt environment or profile. Unlike dbt Core behavior, the target schema specified in the `profiles.yml`
    file must exist before you create your dbt Project in order for it to compile or execute successfully.

  ```yaml
  <profile_name>:
  target: dev
  outputs:
    dev:
      database: <database_name>
      role: <role_name>
      schema: <schema_name>
      type: snowflake
  ```

The following examples illustrate how to use the `snow dbt deploy` command:

* Deploy a dbt project object named `jaffle_shop`:

  ```snowcli
  snow dbt deploy jaffle_shop
  ```

* Deploy a project named `jaffle_shop` from a specified directory and create or add a new version depending on whether the dbt project object already exists:

  ```snowcli
  snow dbt deploy jaffle_shop --source /path/to/dbt/directory --profiles-dir ~/.dbt/ --force
  ```

* Deploy a project named `jaffle_shop` from a specified directory using a custom profiles directory, a specific dbt version, and enabling [external access integrations](../../external-network-access/creating-using-external-network-access.md):

  ```snowcli
  snow dbt deploy jaffle_shop --source /path/to/dbt/directory
  --profiles-dir ~/.dbt/
  --default-target prod
  --dbt-version 1.10.15
  --external-access-integration dbthub-integration
  --external-access-integration github-integration
  --force
  ```

## Listing all available dbt project objects

The [snow dbt list](../command-reference/dbt-commands/list.md) command lists all available dbt project objects on Snowflake.

The following examples illustrate how to use the `snow dbt list` command:

* List all available dbt project objects:

  ```snowcli
  snow dbt list
  ```

* List dbt project objects in the `product` database whose names begin with `JAFFLE`:

  ```snowcli
  snow dbt list --like JAFFLE% --in database product
  ```

## Executing a dbt project object command

The [snow dbt execute](../command-reference/dbt-commands/execute/overview.md) command executes one of the following [dbt commands](https://docs.getdbt.com/reference/dbt-commands) on a Snowflake dbt project object:

* [build](https://docs.getdbt.com/reference/commands/build)
* [compile](https://docs.getdbt.com/reference/commands/compile)
* [deps](https://docs.getdbt.com/reference/commands/deps)
* [list](https://docs.getdbt.com/reference/commands/list)
* [parse](https://docs.getdbt.com/reference/commands/parse)
* [retry](https://docs.getdbt.com/reference/commands/retry)
* [run](https://docs.getdbt.com/reference/commands/run)
* [run-operation](https://docs.getdbt.com/reference/commands/run-operation)
* [seed](https://docs.getdbt.com/reference/commands/seed)
* [show](https://docs.getdbt.com/reference/commands/show)
* [snapshot](https://docs.getdbt.com/reference/commands/snapshot)
* [test](https://docs.getdbt.com/reference/commands/test)

For more information about using dbt commands, see the [dbt Command reference](https://docs.getdbt.com/reference/dbt-commands).

The following examples illustrate how to use the `snow dbt execute` command:

* Execute the dbt `test` command:

  ```snowcli
  snow dbt execute jaffle_shop test
  ```

* Execute the `run` dbt command asynchronously:

  ```snowcli
  snow dbt execute --run-async jaffle_shop run --select @source:snowplow,tag:nightly models/export
  ```

## Describing a dbt project object

The [snow dbt describe](../command-reference/dbt-commands/describe.md) command describes a dbt project object on Snowflake.

The following example describes the dbt project object named `my_dbt_project` on Snowflake:

```console
snow dbt describe my_dbt_project
```

## Dropping a dbt project object

The [snow dbt drop](../command-reference/dbt-commands/drop.md) command deletes a dbt project object on Snowflake.

The following example deletes the dbt project object named `my_dbt_project` on Snowflake:

```console
snow dbt drop my_dbt_project
```

## Use `snow dbt` commands in a CI/CD workflow

> **Note:**
>
> When building CI/CD workflows, you only need your git server, such as Github, and Snowflake CLI. A Git repository object is not required.

You can run dbt commands with Snowflake CLI to build CI/CD pipelines. These pipelines are commonly used to test new code, such as new pull requests, or to update production applications whenever something is merged to the main branch.

To build a CI/CD workflow with `snow dbt` commands, follow these steps:

1. Prepare your dbt project:

   1. Download your dbt project or start a new one.

      * Ensure that the main project directory contains the `dbt_project.yml` and `profiles.yml` files.
      * Verify that the profile name referenced in `dbt_project.yml` is defined in `profiles.yml`.

        > **Note:**
        >
        > Snowflake’s dbt project objects don’t need passwords, so if `profiles.yml` contains any, deployment stops until
        > they are removed.
2. Set up Snowflake CLI GitHub Action.

   Follow the guidelines for [setting up GitHub Action for Snowflake CLI](../cicd/integrate-ci-cd.md) and [verify your connection](../connecting/configure-connections.md) to Snowflake.
3. Define your workflow.

   Determine which commands your workflow needs to run based on your organization’s needs. The following example illustrates a CI workflow that updates the version of the dbt project object named `product_pipeline` with new files, runs the transformations, and finally runs tests:

   ```yaml
   - name: Execute Snowflake CLI command
     run: |
       snow dbt deploy product_pipeline
       snow dbt execute product_pipeline run
       snow dbt execute product_pipeline test
   ```
