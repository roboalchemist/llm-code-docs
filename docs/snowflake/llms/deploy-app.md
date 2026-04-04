# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/deploy-app.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/streamlit-apps/manage-apps/deploy-app.md

# Deploying a Streamlit app

The [snow streamlit deploy](../../command-reference/streamlit-commands/deploy.md) command creates a new Streamlit object
inside your chosen database and schema. By default, this command looks for a main file called `streamlit_app.py`
in your current working directory.

## Prerequisites

Before deploying a Streamlit app with Snowflake CLI, you should meet the following prerequisites:

* Ensure that you have a local Streamlit app with the correct directory structure and `snowflake.yml` project definition file must exist.
* Ensure that your account has the correct privileges as described in [Privileges required to create and use a Streamlit app](../../../streamlit/object-management/privileges.md).
* Ensure that you can create or have access to a named stage where you can upload your Streamlit app files.

## How to deploy a Streamlit app

> **Note:**
>
> With the release of Snowflake CLI 3.14.0, the `snow streamlit deploy` command now uses the updated CREATE STREAMLIT syntax (FROM *source_location*) instead of the deprecated syntax (ROOT_LOCATION = ‘<stage_path_and_root_directory>’). To continue using the deprecated syntax, you can use the `--legacy` option.

The `snow streamlit deploy` command uploads local files to a stage and creates a new Streamlit object inside your chosen database and schema. Your [project definition file](initialize-app.md) should specify the main Python file and query warehouse. You can also specify the following options:

* `--replace`: Replaces the specified Streamlit app, if it already exists.
* `--open`: Opens the Streamlit app in your default browser after deploying the app.
* `--prune`: Removes files that exist in the stage, but not files in the local filesystem (by default no files are removed).
* `--legacy`: Uses the deprecated SQLsyntax (ROOT_LOCATION = ‘<stage_path_and_root_directory>’).

By default the command automatically deploys the `environment.yml` file and the content of the `pages/`
directory, if any of those exists. You can use different files by using [command-line options](../../command-reference/streamlit-commands/deploy.md).

For more information about creating Streamlit apps, see the CLI [snow streamlit deploy](../../command-reference/streamlit-commands/deploy.md) and
SQL [CREATE STREAMLIT](../../../../sql-reference/sql/create-streamlit.md) commands.
