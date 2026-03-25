# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/cicd/integrate-ci-cd.md

# Integrating CI/CD with Snowflake CLI

Snowflake CLI integrates popular CI/CD (continuous integration and continuous delivery) systems and frameworks, such as [GitHub Actions](https://github.com/features/actions), to efficiently automate your Snowflake workflows for SQL, Snowpark, Native Apps, or Notebooks.

The following illustration shows a typical CI/CD workflow in Snowflake CLI.

## CI/CD workflow steps

1. **Store:** Configure a remote Git repository to manage your Snowflake files securely.
2. **Code:** Develop your Snowflake code using an IDE or Snowsight, tailored to your preferences.
3. **Install:** [Install](../installation/installation.md) Snowflake CLI, and provision your preferred CI/CD provider, such as GitHub Actions.
4. **Deploy:** Automate deployment by combining the Snowflake CLI with your selected CI/CD tool.
5. **Monitor:** Track code and workflow performance in Snowflake using [Snowflake Trail](https://www.snowflake.com/en/product/features/snowflake-trail/) for real-time insights.
6. **Iterate:** Apply small, frequent updates to your project for continuous improvement; smaller changes simplify management and rollback, if necessary.

## CI/CD with GitHub Actions

A Snowflake CLI action is a GitHub action designed to integrate Snowflake CLI into CI/CD pipelines. You can use it to automate execution of Snowflake CLI commands within your GitHub workflows. For more information, see the [snowflake-cli-action](https://github.com/snowflakedb/snowflake-cli-action) repository.

## Using Snowflake CLI actions

Github Actions streamlines the process of installing and using Snowflake CLI in your CI/CD workflows. The CLI is installed in an
isolated way, ensuring that it won’t conflict with the dependencies of your project. It automatically sets up
the input configuration file within the `~/.snowflake/` directory.

The action enables automation of your Snowflake CLI tasks, such as deploying Snowflake Native Apps or running Snowpark scripts within your Snowflake environment.

### Input parameters

A Snowflake CLI action uses the following inputs from your Github workflow YAML file, such as `<repo-name>/.github/workflows/my-workflow.yaml`:

* `cli-version`: The specified Snowflake CLI version, such as `3.11.0`. If not provided, the latest version of the Snowflake CLI is used.
* `custom-github-ref`: The branch, tag, or commit in the Github repository that you want to install Snowflake CLI directly from.

  > **Note:**
  >
  > You cannot use both `cli-version` and `custom-github-ref` together; specify only one of these parameters.
* `default-config-file-path`: Path to the configuration file (`config.toml`) in your repository. The path must be relative to the root of the repository. The configuration file is not required when a temporary connection (`-x` option) is used. For more information, see [Managing Snowflake connections](../connecting/configure-connections.md).
* `use-oidc`: Boolean flag to enable OIDC authentication. When set to `true`, the action configures the CLI to use GitHub’s OIDC token for authentication with Snowflake, eliminating the need for storing private keys as secrets. Default is `false`.

### Install Snowflake CLI from a GitHub branch or tag

* To install Snowflake CLI from a specific branch, tag, or commit in the GitHub repository (for example, to test unreleased features or a fork), use the following configuration:

```yaml
- uses: snowflakedb/snowflake-cli-action@v2.0
  with:
    custom-github-ref: "feature/my-branch" # or a tag/commit hash
```

You can also include other input parameters.

This feature is available in snowflake-cli-action version 1.6 or later.

### Safely configure the action in your CI/CD workflow

You can safely configure the action in your CI/CD workflow by using either of the following methods:

* Use workload identity federation (WIF) OpenID Connect (OIDC) authentication
* Use private key authentication

#### Use workload identity federation (WIF) OpenID Connect (OIDC) authentication

> **Note:**
>
> WIF OIDC authentication requires Snowflake CLI version 3.11.0 or later.

WIF OIDC authentication provides a secure and modern way to authenticate with Snowflake without storing private keys as secrets. This approach uses GitHub’s OIDC (OpenID Connect) token to authenticate with Snowflake.

To set up WIF OIDC authentication, follow these steps:

1. Configure WIF OIDC by setting up a service user with the OIDC workload identity type:

   ```sqlexample
   CREATE USER <username>
   TYPE = SERVICE
   WORKLOAD_IDENTITY = (
     TYPE = OIDC
     ISSUER = 'https://token.actions.githubusercontent.com'
     SUBJECT = '<your_subject>'
   )
   ```

> **Note:**
> > By default, your subject should look like `repo:<repository-owner/repository-name>:environment:<environment>`.
>
> * To simplify generation of the subject, use `gh` command, where `<environment_name>` is the environment defined in your repository settings, as shown in the following example:
>
> > ```bash
> > gh repo view <repository-owner/repository-name> --json nameWithOwner | jq -r '"repo:\(.nameWithOwner):environment:<environment_name>"'
> > ```
> >
> > For more information about customizing your subject, see the [OpenID Connect](https://docs.github.com/en/actions/reference/security/oidc) reference on GitHub.

1. Store your Snowflake account identifier in GitHub secrets. For more information, see [GitHub Actions documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).
2. Configure the Snowflake CLI action in your GitHub workflow YAML file, as shown:

   ```yaml
   name: Snowflake OIDC
   on: [push]

   permissions:
     id-token: write  # Required for OIDC token generation
     contents: read

   jobs:
     oidc-job:
       runs-on: ubuntu-latest
       environment: test-env # this should match the environment used in the subject
       steps:
         - uses: actions/checkout@v4
           with:
             persist-credentials: false
         - name: Set up Snowflake CLI
           uses: snowflakedb/snowflake-cli-action@v2.0
           with:
             use-oidc: true
             cli-version: "3.11"
         - name: test connection
           env:
             SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
           run: snow connection test -x
   ```

   For more information about setting up WIF OIDC authentication for your Snowflake account and configuring the GitHub OIDC provider, see [Workload identity federation](../../../user-guide/workload-identity-federation.md).

#### Use private key authentication

To use private key authentication, you need to store your Snowflake private key in GitHub secrets and configure the Snowflake CLI action to use it.

1. Store your Snowflake private key in GitHub secrets.

For more information, see [GitHub Actions documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).

1. Configure the Snowflake CLI action in your GitHub workflow YAML file, as shown:

   ```yaml
   name: Snowflake Private Key
   on: [push]

   jobs:
     private-key-job:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
           with:
             persist-credentials: false
         - name: Set up Snowflake CLI
           uses: snowflakedb/snowflake-cli-action@v2.0
   ```

## Defining connections

You can define a GitHub action to connect to Snowflake with a temporary connection or with a connection defined in your configuration file. For more information about managing connections, see [Managing Snowflake connections](../connecting/configure-connections.md).

### Use a temporary connection

For more information about temporary connections, see [Use a temporary connection](../connecting/configure-connections.md).

To set up your Snowflake credentials for a temporary connection, follow these steps:

1. Map secrets to environment variables in your GitHub workflow, in the form `SNOWFLAKE_<key>=<value>`, as shown:

   ```yaml
   env:
     SNOWFLAKE_PRIVATE_KEY_RAW: ${{ secrets.SNOWFLAKE_PRIVATE_KEY_RAW }}
     SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
   ```

2. Configure the Snowflake CLI action.

   If you use the latest version of Snowflake CLI, you do not need to include the `cli-version` parameter. The following example instructs the action to use Snowflake CLI version 3.11.0 specifically:

   ```yaml
   - uses: snowflakedb/snowflake-cli-action@v2.0
     with:
       cli-version: "3.11.0"
   ```

3. Optional: If your private key is encrypted, to set up a passphrase, set the PRIVATE_KEY_PASSPHRASE environment variable to the private key passphrase. Snowflake uses this passphrase to decrypt the private key. For example:

   ```yaml
   - name: Execute Snowflake CLI command
     env:
       PRIVATE_KEY_PASSPHRASE: ${{ secrets.PASSPHARSE }}
   ```

   To use a password instead of a private key, unset the `SNOWFLAKE_AUTHENTICATOR` environment variable, and add the `SNOWFLAKE_PASSWORD` variable, as follows:

   ```yaml
   - name: Execute Snowflake CLI command
     env:
       SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
       SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
       SNOWFLAKE_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
   ```

   > **Note:**
   >
   > To enhance your experience when using a password and MFA, Snowflake recommends that you [configure MFA caching](../connecting/configure-connections.md).

   For more information about setting Snowflake credentials in environment variables, see [Use environment variables for Snowflake credentials](../connecting/configure-connections.md), and for information about defining environment variables within your GitHub CI/CD workflow, see [Defining environment variables for a single workflow](https://docs.github.com/en/actions/learn-github-actions/variables#defining-environment-variables-for-a-single-workflow).
4. Add the `snow` commands you want to execute with the temporary connection, as shown:

   ```yaml
   run: |
     snow --version
     snow connection test --temporary-connection
   ```

The following example shows a completed sample `<repo-name>/.github/workflows/my-workflow.yaml` file:

```yaml
name: deploy
on: [push]

jobs:
  version:
    name: "Check Snowflake CLI version"
    runs-on: ubuntu-latest
    steps:
      # Snowflake CLI installation
      - uses: snowflakedb/snowflake-cli-action@v2.0

        # Use the CLI
      - name: Execute Snowflake CLI command
        env:
          SNOWFLAKE_AUTHENTICATOR: SNOWFLAKE_JWT
          SNOWFLAKE_USER: ${{ secrets.SNOWFLAKE_USER }}
          SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
          SNOWFLAKE_PRIVATE_KEY_RAW: ${{ secrets.SNOWFLAKE_PRIVATE_KEY_RAW }}
          PRIVATE_KEY_PASSPHRASE: ${{ secrets.PASSPHARSE }} # Passphrase is only necessary if private key is encrypted.
        run: |
          snow --help
          snow connection test -x
```

After verifying that your action can connect to Snowflake successfully, you can add more Snowflake CLI commands like `snow notebook create` or `snow git execute`. For information about supported commands, see [Snowflake CLI command reference](../command-reference/overview.md).

### Use a configuration file

For more information about defining connections, see [Define connections](../connecting/configure-connections.md).

To set up your Snowflake credentials for a specific connection, follow these steps:

1. Create a `config.toml` file at the root of your Git repository with an empty configuration connection, as shown:

   ```toml
   default_connection_name = "myconnection"

   [connections.myconnection]
   ```

   This file serves as a template and should not contain actual credentials.
2. Map secrets to environment variables in your GitHub workflow, in the form `SNOWFLAKE_<key>=<value>`, as shown:

   ```yaml
   env:
     SNOWFLAKE_CONNECTIONS_MYCONNECTION_PRIVATE_KEY_RAW: ${{ secrets.SNOWFLAKE_PRIVATE_KEY_RAW }}
     SNOWFLAKE_CONNECTIONS_MYCONNECTION_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
   ```

3. Configure the Snowflake CLI action.

   If you use the latest version of Snowflake CLI, you do not need to include the `cli-version` parameter. The following example specifies a desired version and the name of your default configuration file:

   ```yaml
   - uses: snowflakedb/snowflake-cli-action@v2.0
     with:
       cli-version: "3.11.0"
       default-config-file-path: "config.toml"
   ```

4. Optional: If your private key is encrypted, to set up a passphrase, set the PRIVATE_KEY_PASSPHRASE environment variable to the private key passphrase. Snowflake uses this passphrase to decrypt the private key. For example:

   ```yaml
   - name: Execute Snowflake CLI command
     env:
       PRIVATE_KEY_PASSPHRASE: ${{ secrets.PASSPHARSE }}
   ```

   To use a password instead of a private key, unset the `SNOWFLAKE_AUTHENTICATOR` environment variable, and add the `SNOWFLAKE_PASSWORD` variable, as follows:

   ```yaml
   - name: Execute Snowflake CLI command
     env:
       SNOWFLAKE_CONNECTIONS_MYCONNECTION_USER: ${{ secrets.SNOWFLAKE_USER }}
       SNOWFLAKE_CONNECTIONS_MYCONNECTION_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
       SNOWFLAKE_CONNECTIONS_MYCONNECTION_PASSWORD: ${{ secrets.SNOWFLAKE_PASSWORD }}
   ```

   > **Note:**
   >
   > To enhance your experience when using a password and MFA, Snowflake recommends that you [configure MFA caching](../connecting/configure-connections.md).
5. Add the `snow` commands you want to execute with a named connection, as shown:

   ```yaml
   run: |
     snow --version
     snow connection test
   ```

The following example shows a sample `config.toml` file in your Git repository and a completed sample `<repo-name>/.github/workflows/my-workflow.yaml` file:

* Sample `config.toml` file:

  ```toml
  default_connection_name = "myconnection"

  [connections.myconnection]
  ```

* Sample Git workflow file:

  ```yaml
  name: deploy
  on: [push]
  jobs:
    version:
      name: "Check Snowflake CLI version"
      runs-on: ubuntu-latest
      steps:
        # Checkout step is necessary if you want to use a config file from your repo
        - name: Checkout repo
          uses: actions/checkout@v4
          with:
            persist-credentials: false

          # Snowflake CLI installation
        - uses: snowflakedb/snowflake-cli-action@v2.0
          with:
            default-config-file-path: "config.toml"

          # Use the CLI
        - name: Execute Snowflake CLI command
          env:
            SNOWFLAKE_CONNECTIONS_MYCONNECTION_AUTHENTICATOR: SNOWFLAKE_JWT
            SNOWFLAKE_CONNECTIONS_MYCONNECTION_USER: ${{ secrets.SNOWFLAKE_USER }}
            SNOWFLAKE_CONNECTIONS_MYCONNECTION_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
            SNOWFLAKE_CONNECTIONS_MYCONNECTION_PRIVATE_KEY_RAW: ${{ secrets.SNOWFLAKE_PRIVATE_KEY_RAW }}
            PRIVATE_KEY_PASSPHRASE: ${{ secrets.PASSPHARSE }} #Passphrase is only necessary if private key is encrypted.
          run: |
            snow --help
            snow connection test
  ```

After verifying that your action can connect to Snowflake successfully, you can add more Snowflake CLI commands like `snow notebook create` or `snow git execute`. For information about supported commands, see [Snowflake CLI command reference](../command-reference/overview.md).
