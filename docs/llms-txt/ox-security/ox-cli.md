# Source: https://docs.ox.security/scan-and-analyze-with-ox/scanning/ox-cli.md

# OX CLI

OX CLI tool allows developers to scan modified files in their local repositories for security issues. It works similarly to the [IDE extension](https://docs.ox.security/scan-and-analyze-with-ox/scanning/broken-reference), but is designed for command-line usage.

Currently the following issue categories are supported: Open Source Security, Code Security, SBOM, IaC, Secret/PII.

The repository you scan must exist in your organization and be known to OX.

In case the repository is not recognized, scans will fail.

## Prerequisites

Before you begin the installation process, make sure the following tools are installed:

* [Node.js](https://nodejs.org/), version 16 and newer
* npm
* [Git](https://git-scm.com/downloads)

## Installing OX CLI

The CLI installation method is for users installing from the public npm registry.

**To install OX CLI:**

```bash
npm install -g @oxappsec/ox-cli
```

### Verifying successful installation

To verify that the CLI is working, run `ox-cli --version`. The available commands, options, and the current version appear.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ca7430dc491112bbcf2a3fdadda39ba8445e5ea6%2FCLI_verify%20version%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

### Updating OX CLI

**To update OX CLI, update public NPM builds:**

* Run:

```
ox-cli update
```

**To verify the update in both distributions:**

```bash
ox-cli --version
```

### Uninstalling OX CLI

**To uninstall OX CLI, run:**

```bash
npm uninstall -g @oxappsec/ox-cli
```

## Before you begin running scans in OX CLI

Before you start scanning, you need to perform the initial configuration, which includes configuring the OX CLI tool with the necessary credentials.\
In addition, you can set API endpoints for staging or development environments, and also enable sending logs/events to datalog.

**To perform the initial configuration:**

1. [Retrieve your IDE/CLI integration key from the OX platform.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/broken-reference)
2. In **OX CLI**, run:

```bash
ox-cli config set api-key <your-api-key>
```

**Note:** You can also run `ox-cli config` with no parameters and press **Enter**, to be prompted for the API key interactively.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-71ca976fcdc5c9ea266b7d8517b8536123f593e3%2FCLI_adding%20API%20key.png?alt=media" alt=""><figcaption></figcaption></figure>

1. (Optional) Set API endpoint for staging or development environments:

```bash
ox-cli config set api-host https://custom.api.endpoint.com
```

1. (Optional) Enable telemetry.

```bash
ox-cli config set enable-telemetry true
```

1. Use environment variables as an alternative to `config`:

   ```bash
   export OX_API_KEY=your-api-key
   export OX_API_ENDPOINT=https://your-api-endpoint.com
   ox-cli scan
   ```

   > **Recommended:** Run `ox-cli config` without arguments to securely enter your API key.
2. To confirm your current configuration:

```bash
ox-cli config get <parameter>
```

## Scanning modified files in OX CLI

During the scan process, OX CLI detects changes in the repository, such as new lines, changed dependencies, deleted files, and so on using the `scan [targetDir]` command.

It compresses only those changes and then sends them securely to the backend for analysis.

> **Important:** Only local modifications are scanned, not the entire repository. The scanned repository must already exist in your OX organization.

OX CLI scans a repository for security issues. If `targetDir` is not provided, the current directory is scanned.

**Usage:**

```bash
ox-cli scan [targetDir] [options]
```

**Arguments:**

* `targetDir` Directory to scan (defaults to the current directory)

**Options:**

| Option                       | Description                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--format <format>`          | Set the output format. Supported values: `text` (default), `json`, `sarif`.                                                                                                                                                                                                                                                                                        |
| `--severity <severities>`    | <p>Filter results by severity. Provide a comma-separated list, e.g., <code>Critical,High</code>.<br><br>Supported severities: <code>Critical</code>, <code>High</code>, <code>Medium</code>, <code>Low</code>, <code>Info</code>.<br><br>The Appoxalypse severity level issues are always presented by default and you cannot set the CLI not to display them.</p> |
| `--group <group>`            | <p>OX CLI allows <a href="broken-reference">the same grouping options, as OX IDE extension</a>.<br><br>Group results in the report. Supported values: <code>severity</code> (default), <code>category</code>.</p>                                                                                                                                                  |
| `--git-remote-name <remote>` | [Specify the Git remote name](#specifying-git-remote).                                                                                                                                                                                                                                                                                                             |

**Example command:**

```bash
ox-cli scan ./my-project --severity Critical,High --format json
```

**Example output:**

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e2ee7466fd736216d8b8479ca5d1168d5fcb524a%2FCLI_scan_results_first_scan%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

### Specifying Git remote

You can compare your local changes against a specific Git remote, which helps determining what is new or modified compared to the remote repository.

**To compare your local changes against a specific Git remote:**

* Replace `origin` with the name of your Git remote and run:

```bash
ox-cli scan --git-remote-name origin
```

### Git Hook Integration

OX CLI can be integrated with Git hooks to block risky code before commit or push.

**To integrate Git hooks:**

1. To install pre-push hook (default):

```bash
ox-cli install-git-hook --type pre-push 
```

1. To install pre-commit hook:

```bash
ox-cli install-git-hook --type pre-commit
```

1. To uninstall pre-push hook:

```bash
ox-cli uninstall-git-hook --type pre-push
```

1. To overwrite an existing hook, use `--force` .

For further support, contact your OX Security representative.
