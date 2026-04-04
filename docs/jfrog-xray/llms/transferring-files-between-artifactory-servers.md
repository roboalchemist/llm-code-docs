# Source: https://docs.jfrog.com/artifactory/docs/transferring-files-between-artifactory-servers.md

# Transfer files between Artifactory servers

Use the `transfer-files` command to transfer (copy) all files stored in one Artifactory instance to a different Artifactory instance. The command allows transferring files from single or multiple repositories. The command expects the relevant repository to already exist on the target instance and have the same name and type as the repositories on the source.

Follow these guides for focused procedures:

* [Install the data-transfer plugin](/docs/jf-rt-transfer-plugin-install) — `jf rt transfer-plugin-install`
* [Transfer full configuration](/docs/jf-rt-transfer-config) — `jf rt transfer-config`
* [Merge configuration into an existing target](/docs/jf-rt-transfer-config-merge) — `jf rt transfer-config-merge`
* [Transfer artifact files](/docs/jf-rt-transfer-files) — `jf rt transfer-files`

***

## Before You Begin

Complete all of these checks before starting the transfer process:

* Ensure you have **JFrog Artifactory Pro or Enterprise edition** on the source instance. Artifactory OSS does not support the data-transfer user plugin required by this workflow.
* Ensure that you can log in to the UI of both the source and target instances with a user that has admin permissions and that you have the connection details for both instances.
* Ensure that all repositories on the source Artifactory instance that you want to transfer also exist on the target instance with the same name and type.
* Ensure that JFrog CLI is installed on a machine that has network access to both the source and target instances.
* Ensure that the `JFROG_HOME` environment variable is set on the **source Artifactory machine** and points to the JFrog installation directory (typically `/opt/jfrog`). This variable is required for the plugin installation step. If it is not set, configure it before proceeding:

  ```bash
  export JFROG_HOME=/opt/jfrog
  ```

  For more information, see the JFrog Product Directory Structure article.

***

## Command Reference

### transfer-files

Transfer files from one Artifactory instance to another.

#### Syntax

```
jf rt transfer-files [command options] <source-server-id> <target-server-id>
```

#### Arguments

| Argument           | Description                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `source-server-id` | Server ID of the Artifactory instance to transfer from. The server should be configured using the `jf c add` command. |
| `target-server-id` | Server ID of the Artifactory instance to transfer to. The server should be configured using the `jf c add` command.   |

#### Command Options

| Option            | Description                                                                                                                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--include-repos` | \[Optional] List of semicolon-separated(;) repositories to include in the transfer. You can use wildcards to specify patterns for the repositories' names.                                                                                                                    |
| `--exclude-repos` | \[Optional] List of semicolon-separated(;) repositories to exclude from the transfer. You can use wildcards to specify patterns for the repositories' names.                                                                                                                  |
| `--include-files` | \[Optional] List of semicolon-separated(;) path patterns to include in the transfer. Files will be filtered based on their directory path. Pattern examples: `folder/subfolder/*`, `org/company/*`.                                                                           |
| `--ignore-state`  | \[Default: false] Set to true to ignore the saved state from previous transfer-files operations and restart the transfer from scratch.                                                                                                                                        |
| `--proxy-key`     | \[Optional] The key of an HTTP proxy configuration in Artifactory. This proxy will be used for the transfer traffic between the source and target instances. To configure this proxy, go to **Proxies > Configuration > Proxy Configuration** in the JFrog Administration UI. |
| `--status`        | \[Default: false] Set to true to show the status of the transfer-files command currently in progress.                                                                                                                                                                         |
| `--stop`          | \[Default: false] Set to true to stop the transfer-files command currently in progress. Useful when running the transfer-files command in the background.                                                                                                                     |
| `--filestore`     | \[Default: false] Set to true to make the transfer mechanism check for the existence of artifacts on the target filestore. Used when the files are already expected to be located on the filestore.                                                                           |
| `--prechecks`     | \[Default: false] Set to true to run pre-transfer checks before starting the file transfer.                                                                                                                                                                                   |

#### Examples

Transfer all files from source to target:

```bash
jf rt transfer-files source-server target-server
```

Transfer only specific repositories:

```bash
jf rt transfer-files source-server target-server --include-repos="libs-release;libs-snapshot"
```

Transfer with wildcard patterns:

```bash
jf rt transfer-files source-server target-server --include-repos="libs-*" --exclude-repos="*-temp"
```

Filter files by path pattern:

```bash
jf rt transfer-files source-server target-server --include-files="org/mycompany/*"
```

Check transfer status:

```bash
jf rt transfer-files --status
```

When no transfer is in progress, this command exits 0 and prints:

```
Status: Not running
```

Stop a running transfer:

```bash
jf rt transfer-files --stop
```

<Callout icon="📘" theme="info">
  Note

  If no transfer is currently active, this command exits with a non-zero status and prints: `There is no active file transfer process.` This is expected behavior. Scripts that use `--stop` as an idempotent cleanup step should account for this exit code.
</Callout>

Run pre-transfer checks:

```bash
jf rt transfer-files source-server target-server --prechecks
```

Restart transfer from scratch:

```bash
jf rt transfer-files source-server target-server --ignore-state
```

***

## Limitations

* Artifacts in remote repository caches are not transferred.
* The file transfer process allows transferring files that were created or modified on the source instance after the process started. However, files that were deleted on the source instance after the process started are not deleted on the target instance by the process.
* The custom properties of newly created or modified files are updated on the target instance. However, if only the custom properties of a file were modified on the source, but not the file's content, the properties are not modified on the target instance by the process.
* The source and target repositories must have the same name and type.
* Since the files are pushed from the source to the target instance, the source instance must have a network connection to the target.

***

## Running the Transfer Process

### Step 1 - Set Up the Source Instance for File Transfer

To set up the source instance for file transfer, you must install the data-transfer user plugin on the primary node of the source instance. This section guides you through the installation steps.

<Callout icon="❗️" theme="error">
  Important

  The data-transfer user plugin requires **JFrog Artifactory Pro or Enterprise edition**. Artifactory OSS does not support user plugins.
</Callout>

1. Install JFrog CLI on the primary node machine of the source instance. For more information, see [Installing JFrog CLI on the Source Instance Machine](#installing-jfrog-cli-on-the-source-instance-machine).

2. Configure the connection details of the source Artifactory instance with your admin credentials by running the following command from the terminal:

   ```bash
   jf c add source-server
   ```

   > **Note:** This command produces no output on success. To verify the server was added, run `jf config show`.

3. Ensure that the `JFROG_HOME` environment variable is set and holds the value of the JFrog installation directory, which usually points to the `/opt/jfrog` directory. If the variable is not set, set its value to point to the correct directory. For more information, see the JFrog Product Directory Structure article.

4. Install the data-transfer user plugin.

   > **Important:** The `jf rt transfer-plugin-install` command must be run **directly on the primary node machine of the source Artifactory instance**. Running it from a remote workstation or a machine where Artifactory is not installed will fail with a directory lookup error. If you are setting up the transfer from a separate machine, SSH into the primary node first.

   If the source instance has internet access, install the plugin automatically:

   ```bash
   jf rt transfer-plugin-install source-server
   ```

   If the source instance does not have internet access, install the plugin manually. For more information, see [Installing the Data-Transfer User Plugin Manually](#installing-the-data-transfer-user-plugin-on-the-source-machine-manually).

### Step 2 - Push the Files from the Source to the Target Instance

Install JFrog CLI on any machine that has access to both the source and the target JFrog instances. To do this, follow the steps described in [Installing JFrog CLI on a Machine with Network Access to the Source and Target Machines](#installing-jfrog-cli-on-a-machine-with-network-access-to-the-source-and-target-machines).

Run the following command to start pushing the files from all the repositories in source instance to the target instance:

```bash
jf rt transfer-files source-server target-server
```

This command may take a few days to push all the files, depending on your system size and your network speed. While the command is running, it displays the transfer progress visually inside the terminal.

<br />

<Image align="center" alt="push-files-from-source-to-target.png" width="80% " src="https://files.readme.io/b5aca57c25980ad7148f6b5e8c13b16c318c5398cd000198c54f657612612bc3-uuid-dc8ae1fc-86ed-03d8-7558-004d0dac89a2.png" />

If you're running the command in the background, use the following command to view the transfer progress:

```bash
jf rt transfer-files --status
```

<br />

<Image align="center" alt="transfer-status.png" width="50% " src="https://files.readme.io/5f1df522c037c010c5f970c91460a5d87ca56728a37b461b08a4036b915bdc5d-uuid-5a4ba233-9047-d8bd-be1c-512babe3cc54.png" />

In case you do not wish to transfer the files from all repositories, or wish to run the transfer in phases, you can use the `--include-repos`, `--exclude-repos`, and `--include-files` command options. Run the following command to see the usage of these options:

```bash
jf rt transfer-files -h
```

If the traffic between the source and target instance needs to be routed through an HTTPS proxy, refer to [Routing the Traffic from the Source to the Target Through an HTTPS Proxy](#routing-the-traffic-from-the-source-to-the-target-through-an-https-proxy).

You can stop the transfer process by pressing **CTRL+C** if the process is running in the foreground, or by running the following command if you're running the process in the background:

```bash
jf rt transfer-files --stop
```

The process will continue from the point it stopped when you re-run the command.

While the file transfer is running, monitor the load on your source instance, and if needed, reduce the transfer speed or increase it for better performance. For more information, see [Controlling the File Transfer Speed](#controlling-the-file-transfer-speed).

A path to an errors summary file will be printed at the end of the run, referring to a generated CSV file. Each line on the summary CSV represents an error of a file that failed to be transferred. On subsequent executions of the `jf rt transfer-files` command, JFrog CLI will attempt to transfer these files again.

Once the `jf rt transfer-files` command finishes transferring the files, you can run it again to transfer files which were created or modified during the transfer. You can run the command as many times as needed. Subsequent executions of the command will also attempt to transfer files that failed to be transferred during previous executions of the command.

<Callout icon="📘" theme="info">
  **Note**

  Read more about how the transfer files works in [CLI for JFrog SaaS Transfer](/integrations/docs/cli-for-jfrog-cloud-transfer).
</Callout>

***

## Installing the data-transfer User Plugin on the Source Machine Manually

<Callout icon="❗️" theme="error">
  Important

  The data-transfer user plugin requires **JFrog Artifactory Pro or Enterprise edition**. Artifactory OSS does not support user plugins.
</Callout>

**To install the data-transfer user plugin on the source machine manually:**

1. Download the following two files from a machine that has internet access:
   * **data-transfer.jar** from `https://releases.jfrog.io/artifactory/jfrog-releases/data-transfer/[RELEASE]/lib/data-transfer.jar`

   * **dataTransfer.groovy** from `https://releases.jfrog.io/artifactory/jfrog-releases/data-transfer/[RELEASE]/dataTransfer.groovy`
   > **Note:** Replace `[RELEASE]` with the specific version number you want to install (for example, `1.0.0`).

2. Create a new directory on the primary node machine of the source instance and place the two files you downloaded inside this directory.

3. Install the **data-transfer** user plugin by running the following command from the terminal. Replace `[plugin files dir]` with the full path to the directory which includes the plugin files you downloaded:

   ```bash
   jf rt transfer-plugin-install source-server --dir "[plugin files dir]"
   ```

***

## Installing JFrog CLI on the Source Instance Machine

For detailed installation steps including Docker container support, see the [Installing JFrog CLI on the Source Instance Machine](/integrations/docs/cli-for-jfrog-cloud-transfer#installing-jfrog-cli-on-the-source-instance-machine) section in the CLI for JFrog SaaS Transfer guide.

Quick install:

```bash
curl -fL https://install-cli.jfrog.io | sh
```

***

## How Does Files Transfer Work?

For a detailed explanation of file transfer phases, transfer state, and how JFrog CLI manages incremental transfers, see the [How Does File Transfer Work?](/integrations/docs/cli-for-jfrog-cloud-transfer#how-does-file-transfer-work) section in the CLI for JFrog SaaS Transfer guide.

***

## Installing JFrog CLI on a Machine with Network Access to the Source and Target Machines

For step-by-step instructions on installing JFrog CLI on a machine with access to both instances, see the [Installing JFrog CLI on a Machine with Network Access to Both Instances](/integrations/docs/cli-for-jfrog-cloud-transfer#installing-jfrog-cli-on-a-machine-with-network-access-to-both-instances) section in the CLI for JFrog SaaS Transfer guide.

***

## Controlling the File Transfer Speed

For details on controlling transfer speed, adjusting working threads, and build-info repository throttling, see the [Controlling File Transfer Speed](/integrations/docs/cli-for-jfrog-cloud-transfer#controlling-file-transfer-speed) section in the CLI for JFrog SaaS Transfer guide.

***

## Pre-Transfer Checks

Before starting a full file transfer, you can run pre-transfer checks to validate the configuration and identify potential issues early. This is especially useful for large transfers that may take days to complete.

**To run pre-transfer checks:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --prechecks
```

**Where:**

* `<source-server-id>` and `<target-server-id>` — JFrog CLI server IDs configured with `jf config add`.

**Full example:**

```bash
jf rt transfer-files source-server target-server --prechecks
```

This will validate:

* Connectivity to both source and target servers
* Repository existence and compatibility
* Permission requirements
* Plugin installation status

Pre-transfer checks typically complete within a few seconds to a few minutes depending on the number of repositories. If all checks pass, the command exits 0 and reports the validation results. If any check fails, review the error output before proceeding with the full transfer.

<Callout icon="📘" theme="info">
  Note

  If the data-transfer plugin is not installed on the source instance, `--prechecks` will fail and print a plugin installation error. Complete [Step 1](#step-1---set-up-the-source-instance-for-file-transfer) before running pre-transfer checks.
</Callout>

***

## Routing the Traffic from the Source to the Target Through an HTTPS Proxy

The `jf rt transfer-files` command pushes the files directly from the source to the target instance over the network. In case the traffic from the source instance needs to be routed through an HTTPS proxy, follow these steps:

1. Define the proxy details in the source instance UI as described in Managing Proxies.

2. When running the `jf rt transfer-files` command, add the `--proxy-key` option to the command, with the Proxy Key you configured in the UI as the option value. For example, if the Proxy Key you configured is `my-proxy-key`, run the command as follows:

   ```bash
   jf rt transfer-files source-server target-server --proxy-key my-proxy-key
   ```

***

## Transfer Plugin Install Command

Install the data-transfer user plugin on an Artifactory server.

<Callout icon="❗️" theme="error">
  Important

  This command requires **JFrog Artifactory Pro or Enterprise edition**. Artifactory OSS does not support user plugins.
</Callout>

### Syntax

```
jf rt transfer-plugin-install <server-id> [command options]
```

### Arguments

| Argument    | Description                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `server-id` | The ID of the source server on which the plugin should be installed. The server should be configured using the `jf c add` command. |

### Command Options

| Option       | Description                                                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--version`  | \[Default: latest] The plugin version to download and install.                                                                                       |
| `--dir`      | \[Optional] The local directory that contains the plugin files to install. Use this option when installing from local files without internet access. |
| `--home-dir` | \[Default: /opt/jfrog] The local JFrog home directory to install the plugin in.                                                                      |

<Callout icon="📘" theme="info">
  Note

  The `--dir` and `--version` flags are mutually exclusive. Use `--dir` when installing from local files (no internet access), or `--version` when downloading from the internet. Providing both flags in the same command will result in an error.
</Callout>

### Examples

Install the latest version of the plugin:

```bash
jf rt transfer-plugin-install source-server
```

Install a specific version:

```bash
jf rt transfer-plugin-install source-server --version 1.0.0
```

Install from local files:

```bash
jf rt transfer-plugin-install source-server --dir "/path/to/plugin/files"
```

Install to a custom JFrog home directory:

```bash
jf rt transfer-plugin-install source-server --home-dir "/custom/jfrog/home"
```

***

## Transfer Settings Command

Configure the settings for the `jf rt transfer-files` command interactively.

### Syntax

```
jf rt transfer-settings
```

### Description

This interactive command allows you to configure the file transfer settings, including:

* **Number of working threads:** Controls how many parallel threads are used for transferring files. The default is 8 threads. You can increase this for faster transfers (higher load) or decrease it for slower transfers (lower load).

<Callout icon="📘" theme="info">
  Note

  For Build Info repositories, the number of working threads is automatically capped at 8, regardless of the value you configure here. This limit applies only to Build Info repositories; all other repository types use the full configured thread count.
</Callout>

The settings are cached by JFrog CLI and will be used for subsequent runs of the `jf rt transfer-files` command from the same machine.

### Example

```bash
jf rt transfer-settings
```

When you run this command, you will be prompted to enter the desired number of working threads. The change takes effect immediately, even if a transfer is currently in progress.

<br />