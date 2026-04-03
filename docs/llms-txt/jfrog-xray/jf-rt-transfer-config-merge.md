# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-transfer-config-merge.md

# Merge Artifactory configuration with jf rt transfer-config-merge

Merge projects and repositories from a source Artifactory instance to a target instance when no conflicts exist.

## Prerequisites

* JFrog CLI is installed. See [Installing JFrog CLI](https://jfrog.com/getcli/).
* Both the source and target Artifactory instances are configured as JFrog CLI servers. Run `jf config add` for each instance before using this command. See [Configuring JFrog CLI](https://jfrog.com/help/r/jfrog-cli/configuring-jfrog-cli).
* The source and target server IDs must refer to **different** Artifactory instances.

## Synopsis

```
jf rt transfer-config-merge [command options] <source-server-id> <target-server-id>
```

**Aliases:** —

## Arguments

| Argument             | Required | Description                            |
| -------------------- | -------- | -------------------------------------- |
| `<source-server-id>` | Yes      | Server ID to export configuration from |
| `<target-server-id>` | Yes      | Server ID to import configuration to   |

## Options

| Flag                 | Required | Default | Description                                                                                                              |
| -------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| `--exclude-projects` | No       | —       | Semicolon-separated list of JFrog Project keys to exclude from the transfer. Supports wildcards (for example, `team-*`). |
| `--exclude-repos`    | No       | —       | Semicolon-separated list of repositories to exclude from the transfer. Supports wildcards (for example, `temp-*`).       |
| `--include-projects` | No       | —       | Semicolon-separated list of JFrog Project keys to include in the transfer. Supports wildcards.                           |
| `--include-repos`    | No       | —       | Semicolon-separated list of repositories to include in the transfer. Supports wildcards.                                 |

## Examples

### Basic Merge

Merge all repositories and projects from the source server to the target server.

**To merge all repositories and projects:**

1. Run:

```bash
jf rt transfer-config-merge <source-server-id> <target-server-id>
```

**Full example:**

```bash
jf rt transfer-config-merge my-source-server my-target-server
```

Expected output:

```
[Info] ========== Preparations ==========
[Info] Verifying source and target servers are different...
[Info] ========== Merging repositories ==========
...
[Info] Configuration merge completed successfully.
```

<Callout icon="👍" theme="okay">
  Tip

  Each execution emits a Trace ID (for example, `[Info] Trace ID for JFrog Platform logs: abc123def456`). If you need to contact JFrog Support, include this ID in your support ticket to help with diagnostics.
</Callout>

### Merge Specific Repositories

**To merge only selected repositories:**

1. Run:

```bash
jf rt transfer-config-merge <source-server-id> <target-server-id> --include-repos "<repo-list>"
```

**Full example:**

```bash
jf rt transfer-config-merge source-server target-server --include-repos "libs-release;libs-snapshot"
```

### Merge Specific Projects

**To merge only selected projects:**

1. Run:

```bash
jf rt transfer-config-merge <source-server-id> <target-server-id> --include-projects "<project-list>"
```

**Full example:**

```bash
jf rt transfer-config-merge source-server target-server --include-projects "my-project;other-project"
```

### Exclude Repositories and Projects

**To merge while excluding repository and project patterns:**

1. Run:

```bash
jf rt transfer-config-merge <source-server-id> <target-server-id> --exclude-repos "<repo-patterns>" --exclude-projects "<project-patterns>"
```

**Full example:**

```bash
jf rt transfer-config-merge source-server target-server --exclude-repos "temp-*" --exclude-projects "test-*"
```

<Callout icon="📘" theme="info">
  Note

  Merging only adds new configuration. Existing target configuration is not overwritten when conflicts exist.
</Callout>

## When to Use

Use `transfer-config-merge` when you want to **add** repositories and projects from one Artifactory to another **without wiping** the target. This is the safe alternative to `transfer-config` when the target already has data.

**Choose this vs alternatives:**

| Scenario                               | Command                                      |
| -------------------------------------- | -------------------------------------------- |
| Target is empty, full migration        | `jf rt transfer-config`                      |
| Target has data, merge safely          | `jf rt transfer-config-merge` (this command) |
| Config already transferred, move files | `jf rt transfer-files`                       |

## Important Notes

* The merge only adds **new** configuration. If a repository or project with the same key already exists on the target, it is **not** overwritten — the conflict is skipped.
* Use `--include-repos` and `--include-projects` to selectively merge specific items.
* Wildcards are supported in repository and project filters (for example, `libs-*`, `team-*`).
* **Source and target must be different servers.** Providing the same server ID for both arguments will result in an error.
* Before the merge begins, the CLI runs a preparations phase to verify server connectivity and confirm the source and target instances are different.

<br />