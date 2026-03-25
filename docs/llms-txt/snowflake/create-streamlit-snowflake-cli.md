# Source: https://docs.snowflake.com/en/developer-guide/streamlit/getting-started/create-streamlit-snowflake-cli.md

# Create and deploy Streamlit apps using Snowflake CLI

This topic describes working with Streamlit in Snowflake using Snowflake CLI.

## What is Snowflake CLI?

Snowflake CLI is an open-source command-line tool explicitly designed for developer-centric workloads in addition to SQL operations.
For Streamlit developers who currently use a local IDE development flow and a Git-backed continuous integration and deployment
(CI/CD) collaboration workflow, Snowflake CLI provides familiar tooling to integrate Streamlit in Snowflake into their current development flow.

For more information, see [Snowflake CLI](../../snowflake-cli/index.md).

Before creating a Streamlit app by using Snowflake CLI:

* Ensure that you meet the required [prerequisites](overview.md) for using Streamlit in Snowflake.
* Install Snowflake CLI. See [Installing Snowflake CLI](../../snowflake-cli/installation/installation.md).

## Developer guides

| Guide | Description |
| --- | --- |
| [Creating a Streamlit app](../../snowflake-cli/streamlit-apps/manage-apps/initialize-app.md) | Learn about creating a Streamlit app using Snowflake CLI. |
| [Deploying a Streamlit app](../../snowflake-cli/streamlit-apps/manage-apps/deploy-app.md) | Learn about deploying a Streamlit app using Snowflake CLI. |
| [Retrieving the URL for a Streamlit app](../../snowflake-cli/streamlit-apps/manage-apps/get-url.md) | Learn about retrieving the URL for a Streamlit app. |
| [Share a Streamlit app](../../snowflake-cli/streamlit-apps/manage-apps/share-app.md) | Learn about sharing a Streamlit app with other roles using Snowflake CLI. |
| [Managing Streamlit apps](../../snowflake-cli/streamlit-apps/manage-apps/manage-app.md) | Learn about managing a Streamlit app using Snowflake CLI. |

## Create a CI/CD pipeline with Snowflake CLI and a GitHub Actions workflow

The following section describes how to deploy a Streamlit app in Snowflake by using Snowflake CLI and
a [GitHub Actions](https://docs.github.com/en/actions) workflow.
You can use a similar approach for other version control providers.

### Prerequisites

Before deploying a Streamlit app by using Snowflake CLI and a GitHub Actions workflow, ensure that you:

* Meet the required [prerequisites](overview.md) for using Streamlit in Snowflake.
* Have a GitHub repository to add files to.

### Example: Create a GitHub Actions workflow using Snowflake CLI

1. In your repository, in the `.github/workflows` directory, create a `main.yml` workflow file.
2. Create a `SNOWCLI_PW` secret to use in the GitHub Actions workflow.
3. Copy the following into the `main.yml` file:

   > ```yaml
   > # Name the GitHub Action
   > name: Deploy via Snowflake CLI
   >
   > on:
   > push:
   >     branches:
   >     - main
   >
   > env:
   > PYTHON_VERSION: '3.12'
   >
   > jobs:
   > build-and-deploy:
   >     runs-on: ubuntu-latest
   >     environment: dev
   >     steps:
   >     # Checks out your repository under $GITHUB_WORKSPACE, so your workflow can access it
   >     - name: 'Checkout GitHub Action'
   >     uses: actions/checkout@v3
   >
   >     - name: Install Python
   >     uses: actions/setup-python@v4
   >     with:
   >         python-version: ${{ env.PYTHON_VERSION }}
   >
   >     - name: 'Install Snowflake CLI'
   >     shell: bash
   >     run: |
   >         python -m pip install --upgrade pip
   >         pip install snowflake-cli
   >
   >     - name: 'Create config'
   >     shell: bash
   >     env:
   >         SNOWFLAKE_PASSWORD: ${{ secrets.SNOWCLI_PW }}
   >     run: |
   >         mkdir -p ~/.snowflake
   >         cp config.toml ~/.snowflake/config.toml
   >         echo "password = \"$SNOWFLAKE_PASSWORD\"" >> ~/.snowflake/config.toml
   >         chmod 0600 ~/.snowflake/config.toml
   >
   >     - name: 'Deploy the Streamlit app'
   >     shell: bash
   >     run: |
   >         snow streamlit deploy --replace
   > ```
>
4. To run your workflow, commit and push the changes to your repository.

For more information, see [GitHub Actions documentation](https://docs.github.com/en/actions).
