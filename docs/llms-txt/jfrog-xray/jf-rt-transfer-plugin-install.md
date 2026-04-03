# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-transfer-plugin-install.md

# Install the data-transfer plugin with jf rt transfer-plugin-install

Download and install the data-transfer user plugin on the primary node of Artifactory running on the local machine.

## Synopsis

```
jf rt transfer-plugin-install <server-id> [options]
```

**Aliases:** —

## Prerequisites

* JFrog CLI installed and configured with the source server ID (`jf config add`).
* This command **must be run on the same machine** where the source Artifactory primary node is installed. It writes plugin files directly to the local filesystem.
* The JFrog home directory (default `/opt/jfrog`) must exist and contain a valid Artifactory installation. If your installation uses a different path, identify it before running this command and use `--home-dir` to specify it.

## Arguments

| Argument      | Required | Description                                                                     |
| ------------- | -------- | ------------------------------------------------------------------------------- |
| `<server-id>` | Yes      | Server ID on which the plugin should be installed (typically the source server) |

## Options

| Flag         | Default      | Description                                                                                                                                                                                                 |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--dir`      | —            | Local directory containing the plugin files to install instead of downloading them. The path to the Artifactory home directory is still required (via `--home-dir` or auto-detection).                      |
| `--home-dir` | `/opt/jfrog` | Path to the local JFrog home directory where Artifactory is installed. The path must already exist and contain a valid Artifactory installation (the CLI looks for `var/etc/artifactory` within this path). |
| `--version`  | `latest`     | Plugin version to download and install. Omit to install the latest version.                                                                                                                                 |

## Examples

### Install the Latest Plugin

**To install the latest plugin version:**

1. Run:

```bash
jf rt transfer-plugin-install <server-id>
```

**Where:**

* `<server-id>` — JFrog CLI server ID for the source Artifactory instance (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt transfer-plugin-install my-server
```

Omitting `--version` installs the latest available plugin version.

**Expected output:**

```
[Info] Installing 'data-transfer' plugin...
[Info] Plugin installed successfully.
```

### Install a Specific Version

**To install a specific plugin version:**

1. Run:

```bash
jf rt transfer-plugin-install <server-id> --version <version>
```

**Full example:**

```bash
jf rt transfer-plugin-install my-server --version 1.2.3
```

**Expected output:**

```
[Info] Installing 'data-transfer' plugin...
[Info] Plugin version 1.2.3 installed successfully.
```

### Install from Local Directory

Use this when the machine does not have internet access. First, download the plugin archive from the [data-transfer releases page](https://github.com/jfrog/data-transfer/releases) on a connected machine, transfer it to the Artifactory host, and extract it to a local directory (for example, `./plugins/data-transfer`).

**To install from a local directory:**

1. Run:

```bash
jf rt transfer-plugin-install <server-id> --dir <plugin-dir>
```

**Where:**

* `<plugin-dir>` — path to the directory that contains the plugin files.

**Full example:**

```bash
jf rt transfer-plugin-install my-server --dir ./plugins/data-transfer
```

<Callout icon="📘" theme="info">
  Note

  `--dir` only replaces the download step. The CLI still requires a valid Artifactory installation on the local machine (auto-detected or specified via `--home-dir`).
</Callout>

**Expected output:**

```
[Info] Installing 'data-transfer' plugin...
[Info] Plugin installed successfully.
```

### Use a Custom Home Directory

Use this when Artifactory is installed in a non-default location. The path must point to an **existing** Artifactory installation directory.

**To install using a custom JFrog home directory:**

1. Run:

```bash
jf rt transfer-plugin-install <server-id> --home-dir <jfrog-home>
```

**Full example:**

```bash
jf rt transfer-plugin-install my-server --home-dir /opt/my-jfrog
```

**Expected output:**

```
[Info] Installing 'data-transfer' plugin...
[Info] Plugin installed successfully.
```

### View Command Help

**To view command help:**

1. Run:

```bash
jf rt transfer-plugin-install --help
```

<Callout icon="📘" theme="info">
  Note

  Run all installation commands on the machine where the Artifactory primary node runs. The plugin is required for `transfer-config` and `transfer-files` operations.
</Callout>

## Trace ID

Every invocation prints a `Trace ID for JFrog Platform logs` in the `[Info]` output. This ID is generated for each command run and can be used to search Artifactory's system logs (`$JFROG_HOME/var/log/artifactory-service.log`) when troubleshooting failures.

## Verifying the Installation

After the command completes, confirm the plugin is active by checking the Artifactory system log for a line similar to:

```
[INFO] Plugin data-transfer loaded successfully.
```

Alternatively, you can verify the plugin files were written to `$JFROG_HOME/var/etc/artifactory/plugins/`.

**To restart the Artifactory service if the plugin does not load:**

1. Run:

```bash
$JFROG_HOME/app/bin/artifactory.sh restart
```

## When to Use

This is the **first step** in any Artifactory-to-Artifactory migration. Run it on the machine where the **source** Artifactory primary node is running, before using `transfer-config` or `transfer-files`.

## Important Notes

* Must be run **on the same machine** as the Artifactory primary node (it installs files into the local filesystem).
* The default JFrog home directory is `/opt/jfrog`. Use `--home-dir` to specify a different path if your installation is in a non-standard location. The path must already exist and contain a valid Artifactory installation — pointing to a non-existent or empty directory produces an error.
* After installation, Artifactory loads the plugin automatically in most configurations. If it does not appear in the logs within a few minutes, restart Artifactory (see **Verifying the Installation** above).
* Use `--version` to install a specific plugin version if you need compatibility with a particular Artifactory version.

<br />