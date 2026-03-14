# Source: https://docs.anyscale.com/reference/quickstart-cli.md

# CLI configuration

[View Markdown](/reference/quickstart-cli.md)

# CLI configuration

This page contains an overview of installing and configuring the Anyscale CLI.

You configure and use the Anyscale CLI from a terminal with Python installed.

important

The Anyscale CLI supports Python versions 3.9-3.13.

## Install the Anyscale CLI[​](#install-the-anyscale-cli "Direct link to Install the Anyscale CLI")

Run the following code to install the Anyscale CLI using pip:

```
pip install anyscale
```

## Authenticate the Anyscale CLI[​](#authenticate-the-anyscale-cli "Direct link to Authenticate the Anyscale CLI")

caution

Be sure to keep your API key private and secure to prevent unwanted access to your Anyscale resources.

Run the following command to authenticate to Anyscale from interactive development environments:

```
anyscale login
```

A new browser window opens to confirm that you want to authenticate access to your current Anyscale organization from the IP address of the machine where you ran this command.

Once you approve access, the CLI stores the access token in a local credential file named `~/.anyscale/credentials.json`. The CLI uses this token to authenticate all requests.

note

API keys created by `anyscale login` expire after 7 days. If you want them to persist longer or not to expire, use `--expire-in-days=<# of days>` or `--no-expire` flags.

Anyscale recommends regularly rotating API keys to reduce risks associated with leaked keys.

### Manual CLI token configuration[​](#cli-token "Direct link to Manual CLI token configuration")

You can manually generate API keys and set them using environmental variables. Use this method when you need to authenticate the CLI for a non-interactive use case such as a CI/CD integration.

Complete the following steps:

1. Generate of an API key using [API key generation UI](https://console.anyscale.com/v2/api-keys).
2. Specify the API using the `ANYSCALE_CLI_TOKEN` environment variable in the environment where the CLI commands run.

note

This environmental variable overrides the credentials configured using `anyscale login` in the `~/.anyscale/credentials.json` file.

## Verify CLI configuration[​](#verify-cli-configuration "Direct link to Verify CLI configuration")

Run a command to confirm the CLI is working.

The following command lists all the jobs you own in the Anyscale cloud:

```
anyscale job list
```

If the command runs without an error, you have installed and configured the Anyscale CLI correctly.

note

If you haven't run any Anyscale jobs, this command returns the name of the fields without any values.

## Anyscale CLI in the workspace terminal[​](#anyscale-cli-in-the-workspace-terminal "Direct link to Anyscale CLI in the workspace terminal")

The Anyscale workspace terminal includes the Anyscale CLI configured with a cluster CLI token set using `ANYSCALE_CLI_TOKEN`.

## Next steps[​](#next-steps "Direct link to Next steps")

For a full overview of CLI commands and their parameters, see the [Anyscale CLI reference](/reference.md).
