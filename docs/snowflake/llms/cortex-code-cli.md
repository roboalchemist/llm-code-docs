# Source: https://docs.snowflake.com/en/user-guide/cortex-code/cortex-code-cli.md

# Cortex Code CLI

This topic helps you get started with Cortex Code CLI, including installation, connection setup, and validation.

Before you begin, ensure you have a Snowflake account with access to the required Cortex models. See Prerequisites for full details.

> **Note:**
>
> If you do not have a Snowflake account, you can [sign up for a free Cortex Code CLI trial](https://signup.snowflake.com/cortex-code).

## Install Cortex Code CLI

### Linux (including WSL) and macOS

To install Cortex Code CLI on Linux, macOS, or WSL, issue the following command in a shell:

```shell
curl -LsS https://ai.snowflake.com/static/cc-scripts/install.sh | sh
```

This command downloads and runs the installation script, which installs the latest version of Cortex Code CLI.
The `cortex` executable is installed in `~/.local/bin` by default. The installation script adds this directory
to your PATH by modifying your shell profile.

### Windows native

To install Cortex Code CLI on Windows, issue the following command in PowerShell:

```shell
irm https://ai.snowflake.com/static/cc-scripts/install.ps1 | iex
```

This command downloads and runs the installation script, which installs the latest version of Cortex Code CLI.
The `cortex` executable is installed in `%LOCALAPPDATA%\cortex` by default. The installation script adds
this directory to your PATH.

## Connect to Snowflake

After installing the Cortex Code CLI, issue the `cortex` command. A setup wizard guides you through the
initial configuration steps, including choosing or setting up a connection to Snowflake.

The first prompt asks you to choose a connection from the existing connections in the `~/.snowflake/connections.toml` file
or to create a new connection.

* To use an existing connection, choose the connection from the list using the up and down arrow keys, then press Enter.
* To create a new connection, choose More options\* by pressing the down arrow key until it is highlighted, then press Enter.
  Follow the prompts to enter your Snowflake account details.

> **Note:**
>
> The `connections.toml` is also used by the [Snowflake CLI](../../developer-guide/snowflake-cli/index.md) (`snow` command). If you have already set up a connection
> for use with the Snowflake CLI, you can use that connection with the Cortex Code CLI.

## Start using Cortex Code

Once connected, try your first request:

```text
What can I do with Cortex Code?
```

Type natural-language requests (such as “find tables with PII tags” or “generate a Streamlit app for
SALES_MART.REVENUE”) and Cortex Code attempts to fulfill the request by orchestrating Snowflake-native skills and any
MCP tools you have configured. For more information on configuring MCP tools, see [Model Context Protocol (MCP)](extensibility.md).

As it works on your request, Cortex Code CLI displays its reasoning steps and actions in the terminal. From time to
time, it may ask you for information that it needs. If you’re in plan mode, it will ask you to confirm each action.

### Example requests

#### Discover your catalog

```text
What databases do I have access to?
List every table tagged PII = TRUE in ANALYTICS_DB
Show the lineage from RAW_DB.ORDERS to downstream dashboards
```

#### Generate and run SQL commands

```text
Write a query for top 10 customers by revenue
Add a 7-day moving average and show me the results
Explain why this query is slow and optimize it
```

#### Build applications

```text
Build a Streamlit dashboard on SALES_MART.REVENUE with filters for date and region
Create a dbt project to transform raw sales data
```

#### Work with Cortex Analyst

```text
Use the @models/revenue.yaml semantic model to answer "What was revenue last month?"
Debug my semantic model at @models/revenue.yaml
```

## Prerequisites

To use Cortex Code CLI, you need the following:

* A Snowflake user account with the necessary permissions to access the data you intend to use with Cortex Code CLI and to perform operations on them.
  This user must also have the SNOWFLAKE.CORTEX_USER database role. (Initially, all users have the SNOWFLAKE.CORTEX_USER role through the PUBLIC role, but
  your organization may have explicitly revoked it to implement stricter access control.)
* Network access to your Snowflake server.
* [Snowflake CLI](../../developer-guide/snowflake-cli/index.md) installed on your workstation.
* One of the following supported platforms:

  > * macOS on Apple Silicon or Intel
  > * Linux on Intel
  > * Windows Subsystem for Linux (WSL) on Intel
  > * Windows Native on Intel (in preview)
  > > **Note:**
  > >
  > > Snowflake may add support for other platforms from time to time. Please let your Snowflake representative know if you
  > > have a specific platform requirement.
* Local terminal access to the `bash`, `zsh`, or `fish` shell on your platform.

For additional configuration options, troubleshooting, and advanced setup, see [Cortex Code CLI reference](cli-reference.md).

## Supported platforms and models

### Supported platforms

Cortex Code CLI currently supports the following platforms:

| Platform | Architecture |
| --- | --- |
| macOS | arm64, x64 |
| Linux | x64, arm64 |
| Windows | WSL on x64/amd64  Native on x64 (in preview) |

> **Note:**
>
> Snowflake may add support for other platforms from time to time. Please contact your Snowflake representative if you
> have a specific platform requirement.

### Supported models

Cortex Code CLI supports the following models. At least one of these models must be available to your account (for
example, by being included in your account’s allowlist, CORTEX_MODELS_ALLOWLIST). See [Control model access](../snowflake-cortex/aisql.md)
for more information.

Snowflake recommends specifying `auto` for the model. Cortex automatically selects the highest quality model available to your
account. When a new, more capable, model becomes available, `auto` then refers to that model.

To choose a different model, use the `/model` command inside a Cortex Code CLI session.

| Model | Identifier |
| --- | --- |
| Auto | `auto` |
| Claude Opus 4.6 | `claude-opus-4-6` |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` |
| Claude Opus 4.5 | `claude-opus-4-5` |
| Claude Sonnet 4.5 | `claude-sonnet-4-5` |
| Claude Sonnet 4.0 | `claude-4-sonnet` |
| OpenAI GPT 5.2 | `openai-gpt-5.2` |

Model quality and capability vary, so choose a model based on your requirements.

### Cloud regions

If a model you want to use is not [available in your region](../snowflake-cortex/aisql.md), you can use Cortex
cross-region inference to access the model in another region where it is available. For more information about
configuring cross-region inference, see [Cross-region inference](../snowflake-cortex/cross-region-inference.md).

Cortex Code requires an `ACCOUNTADMIN` to configure
[CORTEX_ENABLED_CROSS_REGION](../snowflake-cortex/cross-region-inference.md) to one of the following
values.

The following table shows the models that are available for each cross-region inference setting:

| Model | Cross-cloud  (Any region) | AWS US  (Cross-region) | AWS EU  (Cross-region) | AWS APJ  (Cross-region) | Azure US  (Cross-region) | Azure EU  (Cross-region) |
| --- | --- | --- | --- | --- | --- | --- |
| `claude-opus-4-6` | ✔ | ✔ | ✔ |  |  |  |
| `claude-sonnet-4-6` | ✔ | ✔ | ✔ |  |  |  |
| `claude-opus-4-5` | ✔ | ✔ | ✔ |  |  |  |
| `claude-sonnet-4-5` | ✔ | ✔ | ✔ |  |  |  |
| `claude-4-sonnet` | ✔ | ✔ | ✔ | ✔ |  |  |
| `openai-gpt-5.2` | \* |  |  |  | \* |  |

**\*** Indicates a preview model. Preview models are not suitable for production workloads.

To enable cross-region inference, an ACCOUNTADMIN must run:

```sqlexample
ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'AWS_US';
```

Replace `AWS_US` with the appropriate region identifier.

> **Important:**
>
> **Cross-region inference is required when the selected model is not available in your region.** We recommend the
> following settings based on your needs:
>
> * **AWS_US**: Recommended for the best experience with **Claude Opus 4.x** models.
> * **AWS_EU**: Access Claude models from the EU.
> * **AWS_APJ**: Access Claude models from APJ (may be limited to Claude Sonnet 4.0).
> * **ANY_REGION**: Access **all** available models (best-effort global routing).
> * **AZURE_US**: Access OpenAI GPT 5.2.
>
> Your organization can restrict model access, so you may not have access to all models. See
> [Control model access](../snowflake-cortex/aisql.md) for details.

## Legal notices

Where your configuration of Cortex Code uses a model provided on the
[Model and Service Pass-Through Terms](https://www.snowflake.com/en/legal/optional-offerings/offering-specific-terms/ai-features/model-pass-through-terms/),
your use of that model is further subject to the terms for that model on that page.

The data classification of inputs and outputs are as set forth in the following table.

| Input data classification | Output data classification | Designation |
| --- | --- | --- |
| Usage Data | Customer Data | Cortex Code CLI: Covered AI Features. Cortex Code in Snowsight: Preview AI Features. [1] |

[1]

Represents the defined term used in the AI Terms and Acceptable Use Policy.

For additional information, refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).
