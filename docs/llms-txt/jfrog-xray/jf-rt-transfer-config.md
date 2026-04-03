# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-transfer-config.md

# Copy Artifactory configuration with jf rt transfer-config

Copy full Artifactory configuration from a source Artifactory server to a target Artifactory server.

## Synopsis

```
jf rt transfer-config <source-server-id> <target-server-id> [options]
```

**Aliases:** —

## Arguments

| Argument             | Required | Description                            |
| -------------------- | -------- | -------------------------------------- |
| `<source-server-id>` | Yes      | Server ID to export configuration from |
| `<target-server-id>` | Yes      | Server ID to import configuration to   |

## Options

| Flag                   | Default               | Description                                                                                                                                          |
| ---------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--exclude-repos`      | —                     | Semicolon-separated list of repositories to exclude. Supports wildcards                                                                              |
| `--force`              | `false`               | Set to true to allow transfer to a non-empty Artifactory server                                                                                      |
| `--include-repos`      | —                     | Semicolon-separated list of repositories to include. Supports wildcards                                                                              |
| `--prechecks`          | `false`               | Set to true to run pre-transfer checks against the source server before any data is moved. Pre-check mode skips the interactive confirmation prompt. |
| `--source-working-dir` | `$JFROG_CLI_TEMP_DIR` | Local working directory on the source server                                                                                                         |
| `--target-working-dir` | `/storage`            | Local working directory on the target server                                                                                                         |
| `--verbose`            | `false`               | Set to true to increase verbosity during export                                                                                                      |

## When to Use

Use `transfer-config` when **migrating an entire Artifactory instance** to a new server — for example, moving from self-hosted to JFrog SaaS, or upgrading to new infrastructure. This copies all repositories, users, groups, permissions, and other configuration.

**Choose this vs alternatives:**

| Scenario                                                | Use This Command              |
| ------------------------------------------------------- | ----------------------------- |
| Full migration to a new empty server                    | `jf rt transfer-config`       |
| Add repos from source to existing target without wiping | `jf rt transfer-config-merge` |
| Move only files (config already transferred)            | `jf rt transfer-files`        |

## Prerequisites

**Before you run `transfer-config`:**

1. Install the data-transfer plugin on the source server:

   ```bash
   jf rt transfer-plugin-install <source-server>
   ```

   > **Note:** If your JFrog home directory is not at the default `/opt/jfrog`, specify the path with `--home-dir <path>`. Use `--version` to pin a specific plugin version instead of `latest`.

2. Configure both source and target servers with `jf config add`.

3. Use admin access tokens (or equivalent credentials) for both servers.

4. Ensure the target server is empty unless you intend to use `--force`.

## Examples

<Callout icon="🚧" theme="warn">
  Warning

  This command always wipes all Artifactory content on the target server before importing. `--force` is required only when the target is non-empty — it does not protect existing content from being overwritten.
</Callout>

<Callout icon="📘" theme="info">
  Note

  Before executing, the CLI displays a confirmation prompt and a credential-security reminder. Enter `y` to proceed. There is no `--yes` flag; to run non-interactively (for example, in CI/CD pipelines), pipe input:

  ```bash
  echo "y" | jf rt transfer-config <source-server> <target-server> [options]
  ```
</Callout>

### Verify Command Help

**To view command help:**

1. Run:

```bash
jf rt transfer-config --help
```

### Transfer Full Configuration

**To transfer full configuration between servers:**

1. Run:

```bash
jf rt transfer-config <source-server-id> <target-server-id> --force
```

**Where:**

* `<source-server-id>` and `<target-server-id>` — CLI server IDs (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt transfer-config source-server target-server --force
```

On success, the CLI prints progress through five phases:

```
[Info] ========== Phase 1/5 - Preparations ==========
[Info] ========== Phase 2/5 - Export configuration from source ==========
[Info] ========== Phase 3/5 - Import configuration to target ==========
[Info] ========== Phase 4/5 - Copy files ==========
[Info] ========== Phase 5/5 - Cleanup ==========
```

### Transfer Specific Repositories

**To transfer configuration for specific repositories:**

1. Run:

```bash
jf rt transfer-config <source-server-id> <target-server-id> --include-repos "<repo-list>"
```

**Full example:**

```bash
jf rt transfer-config source-server target-server --include-repos "libs-release;libs-snapshot"
```

### Run Pre-Transfer Checks

**To run pre-transfer checks with verbose output:**

1. Run:

```bash
jf rt transfer-config <source-server-id> <target-server-id> --prechecks --verbose
```

**Full example:**

```bash
jf rt transfer-config source-server target-server --prechecks --verbose
```

Pre-check mode validates the source configuration without transferring any data and skips the interactive confirmation prompt. It may take significant time for large configurations (thousands of repositories).

### CI/CD Usage (Non-Interactive)

**To confirm the transfer non-interactively:**

1. Pipe confirmation into the command (the CLI prompts for `y` before proceeding):

```bash
echo "y" | jf rt transfer-config <source-server-id> <target-server-id> --force
```

**Full example:**

```bash
echo "y" | jf rt transfer-config source-server target-server --force
```

## Known Limitations

* The target server content is **always wiped** during transfer. `--force` is required only when the target is non-empty; it does not prevent existing content from being overwritten.
* Very large configurations (thousands of repositories) may take significant time for pre-checks
* Some configuration elements (for example, custom plugins, LDAP settings) may require manual migration
* The source server must be accessible from the machine running the CLI

<br />