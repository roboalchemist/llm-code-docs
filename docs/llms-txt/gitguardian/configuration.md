# Source: https://docs.gitguardian.com/ggshield-docs/configuration.md

# Configuration

> Configure ggshield via CLI options, environment variables, and config files, and how settings interact with the GitGuardian dashboard.

## Dependencies between the dashboard and ggshield

The following paragraph describes how the GitGuardian REST API and ggshield (CLI) work in relation to the dashboard and how you can customize the dashboard experience to best fit your approach to secrets scanning in developer workflows.

Here is the complete list of settings and interactions between the dashboard and the API or CLI:

- **Ignored secret incidents**
  Secrets for which the related incident has been ignored on your GitGuardian dashboard will no longer be raised by ggshield.
- **Resolved secret incidents**
  If the [Regression setting is OFF](https://dashboard.gitguardian.com/settings/workspace/general), secrets for which the related incident has been resolved on your GitGuardian dashboard will no longer be raised by ggshield. However, if the Regression setting is turned ON, ggshield will raise them.
- **Disabled/enabled detectors**
  Secrets associated with detectors you have disabled on your GitGuardian dashboard will not be raised by ggshield.
- **Activated/de-activated validity checks for secret**
  ggshield follows the [validity check setting](../secrets-detection/customize-detection/validity-checks#enabling-and-disabling-validity-checks) of your GitGuardian dashboard. If this setting is turned OFF, ggshield will no longer perform validity checks, and neither will your dashboard.
- **Filepath exclusions**
  Secrets found in a [filepath excluded on your GitGuardian dashboard](../secrets-detection/customize-detection/exclusion-rules#filepath-exclusions) will not be raised by ggshield.

**For each secret found with ggshield, we indicate whether it is known by your GitGuardian dashboard**. If a secret incident already exists on your GitGuardian dashboard, ggshield will also print the URL of the associated secret incident to your console.

This information can be leveraged by using the [`--ignore-known-secrets` option](./reference/secret/scan/overview.md), which makes ggshield ignore secrets that are already known to your dashboard.

## General Configuration

When it comes to configuration, you can fine-tune ggshield's behavior using three sources of parameters.
From higher priority to lower priority:

- CLI options
- Environment variables
- Configuration files
  This means that CLI options override environment variables, which override settings set in configuration files.

### CLI options

A few configuration parameters are available as CLI options. We recommend using `--help` with the command you intend
to use to get more insights on what behaviors can be configured this way.

### Environment Variables

Some of ggshield's behaviors can be tuned via environment variables.
When starting up, ggshield will attempt to load environment variables from different environment files in the following order:

- the file pointed by the `GITGUARDIAN_DOTENV_PATH` environment variable.
- A `.env` file at the current working directory.
- A `.env` file at the root of the current git directory.

Only one of the env files will be loaded out of the three.

#### List of supported environment variables

- `GITGUARDIAN_API_KEY`: API Key for the GitGuardian API. Use this if you don't want to use the `ggshield auth` commands.

- `GITGUARDIAN_INSTANCE`: Custom URL of the GitGuardian dashboard. The API URL will be inferred from it.

- `GITGUARDIAN_DONT_LOAD_ENV`: If set to any value then environment variables won't be loaded from a file.

- `GITGUARDIAN_DOTENV_PATH`: If set to a path, ggshield will attempt to load the environment from the specified file.

- `GITGUARDIAN_TIMEOUT`: If set to a float, `ggshield secret scan pre-receive` will timeout after the specified value. Set to 0 to disable the timeout.

- `GITGUARDIAN_MAX_COMMITS_FOR_HOOK`: If set to an int, `ggshield secret scan pre-receive` and `ggshield secret scan pre-push` will not scan more than the specified value of commits in a single scan.

- `GITGUARDIAN_CRASH_LOG`: If set to True, ggshield will display a full traceback when crashing.

- `GITGUARDIAN_LOG_FILE`: If set to a file, ggshield will send log output to it. You can also set it to `-` to send output to stderr. Equivalent to the [`--log-file` option](reference/overview#options).

### Configuration files

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/xzFtZQCOgBc?controls=0&loop=1" title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; fullscreen; encrypted-media; gyroscope; picture-in-picture; web-share; loop" allowFullScreen></iframe>

Configuration files selection in `ggshield` follows a global to local hierarchy.

`ggshield` will first search for a **global** configuration file in the user's home directory:

- `~/.gitguardian.yaml` on Linux or MacOS
- `%USERPROFILE%\.gitguardian.yaml` on Windows

`ggshield` will then search for a **local** configuration file in the current working directory (i.e.: `./.gitguardian.yaml`).

Alternatively, the `--config-path` or `-c` option can be used to specify a custom configuration file:

```
ggshield --config-path ~/Desktop/custom_config.yaml secret scan path -r .
```

In this case, neither local nor global configuration files will be evaluated.

Here is a sample configuration file:

```yml
# Required, otherwise ggshield considers the file to use the deprecated v1 format
version: 2

# Set to true if the desired exit code for the CLI is always 0, otherwise the
# exit code will be 1 if incidents are found.
exit_zero: false # default: false

verbose: false # default: false

instance: https://dashboard.gitguardian.com # default: https://dashboard.gitguardian.com

# Maximum commits to scan in a hook.
max_commits_for_hook: 50 # default: 50

# Disable SSL/TLS certificate verification (not recommended).
# Was called `allow_self_signed` before.
insecure: false # default: false

secret:
  # Exclude files and paths by globbing
  ignored_paths:
    - '**/README.md'
    - 'doc/*'
    - 'LICENSE'

  # Ignore security incidents with the SHA256 of the occurrence obtained at output or the secret itself
  ignored_matches:
    - name:
      match: 530e5a4a7ea00814db8845dd0cae5efaa4b974a3ce1c76d0384ba715248a5dc1
    - name: credentials
      match: MY_TEST_CREDENTIAL

  show_secrets: false # default: false

  ignore_known_secrets: false # default: false

  # Detectors to ignore.
  ignored_detectors: # default: []
    - Generic Password
```

## Support for self-signed certificates

If your network access requires self-signed certificates, the recommended approach is to install your certificate in your system's trust store. With Python 3.10 or later, ggshield automatically uses the system trust store, providing secure certificate validation.

If you can't use Python 3.10, the alternative is to use the `insecure: true` option, but this is not recommended because it skips all certificate validation checks. This means your connection to the GitGuardian API is vulnerable to man-in-the-middle (MITM) attacks. API keys, scanned content and results can be intercepted and modified.

## Size limits and API call volume considerations

`ggshield` relies on the GitGuardian API to perform secret scanning. The maximum size for a document that can be scanned is 1MB. Any files larger than 1MB will be ignored. Using the `--verbose` option will show information about any files skipped when performing a secret scan.

The GitGuardian API limits batches of files per call to a maximum of 20 documents. If a repository or folder contains more than 20 documents, `ggshield` will bundle files into groups of 20 or fewer to be scanned per API call. Scanning repositories containing more than 20 documents will result in multiple API calls.

You can explore this topic further in the [GitGuardian API reference documentation](https://api.gitguardian.com/docs#tag/Scan-Methods).

## Specificities for on-premise configuration

`ggshield` can also be configured to run on your on-premise GitGuardian instance.

First, you need to point ggshield to your instance, by either defining the `instance` key in your `.gitguardian.yaml` configuration file or by defining the `GITGUARDIAN_INSTANCE` environment variable.

Then, you need to authenticate against your instance using the `ggshield auth login --instance https://mygitguardianinstance.mycorp.local` command using the `--instance` option, or by obtaining an API key from your dashboard administrator and storing it in the `GITGUARDIAN_API_KEY` environment variable.
