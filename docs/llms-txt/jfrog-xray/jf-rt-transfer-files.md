# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-transfer-files.md

# Transfer artifact files with jf rt transfer-files

Transfer files from one Artifactory instance to another.

## Synopsis

```
jf rt transfer-files [options] <source-server-id> <target-server-id>
```

**Aliases:** —

## Arguments

| Argument             | Required | Description                                            |
| -------------------- | -------- | ------------------------------------------------------ |
| `<source-server-id>` | Yes      | Server ID of the Artifactory instance to transfer from |
| `<target-server-id>` | Yes      | Server ID of the Artifactory instance to transfer to   |

## Options

| Flag              | Default | Description                                                                                                                                                                                                        |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--exclude-repos` | —       | Semicolon-separated list of repositories to exclude from the transfer. Supports wildcards.                                                                                                                         |
| `--filestore`     | `false` | Set to true to make the transfer check for the existence of artifacts on the target filestore before transferring. Use this for shared-storage scenarios where files are already physically present on the target. |
| `--ignore-state`  | `false` | Set to true to ignore the saved state from previous transfer-files runs.                                                                                                                                           |
| `--include-files` | —       | Semicolon-separated path patterns to include in the transfer. Files are filtered by directory path. Examples: `folder/subfolder/*`, `org/company/*`.                                                               |
| `--include-repos` | —       | Semicolon-separated list of repositories to include in the transfer. Supports wildcards.                                                                                                                           |
| `--prechecks`     | `false` | Set to true to run pre-transfer checks (plugin presence, connectivity, configuration validity) before starting a transfer.                                                                                         |
| `--proxy-key`     | —       | Key of an HTTP proxy configured in Artifactory to route transfer traffic between source and target. Configure the proxy first under **Administration → Proxies → Configuration** in the Artifactory UI.            |
| `--status`        | `false` | Set to true to show the status of the transfer-files command currently in progress. Reads local state — does not require an active server connection.                                                              |
| `--stop`          | `false` | Set to true to stop the transfer-files command currently in progress. Useful when running the transfer in the background. Reads local state — does not require an active server connection.                        |

## Examples

### Transfer All Files Between Servers

Transfer all artifacts from one Artifactory instance to another.

**To transfer all repositories between two servers:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id>
```

**Where:**

* `<source-server-id>` — CLI server ID for the source Artifactory instance.
* `<target-server-id>` — CLI server ID for the target Artifactory instance.

**Full example:**

```bash
jf rt transfer-files source-server target-server
```

Expected output (initial lines):

```
[Info] Starting files transfer from 'source-server' to 'target-server'...
[Info] Found 12 repositories to transfer.
[Info] Transferring repository: libs-release (1 of 12)
...
```

<Callout icon="📘" theme="info">
  Note

  : Large transfers run for hours or days. Use `--status` in a separate terminal to monitor progress.
</Callout>

### Transfer Specific Repositories

Transfer only the listed repositories.

**To transfer only selected repositories:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --include-repos "<repo-list>"
```

**Where:**

* `<repo-list>` — semicolon-separated repository keys or patterns.

**Full example:**

```bash
jf rt transfer-files source-server target-server --include-repos "libs-release;libs-snapshot"
```

Expected output (initial lines):

```
[Info] Starting files transfer from 'source-server' to 'target-server'...
[Info] Found 2 repositories to transfer (filtered by --include-repos).
[Info] Transferring repository: libs-release (1 of 2)
...
```

### Exclude Repositories

Transfer all repositories except the ones matching the exclusion patterns.

**To exclude repositories by pattern:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --exclude-repos "<repo-patterns>"
```

**Full example:**

```bash
jf rt transfer-files source-server target-server --exclude-repos "temp-*;archive-*"
```

Expected output (initial lines):

```
[Info] Starting files transfer from 'source-server' to 'target-server'...
[Info] Repositories excluded by --exclude-repos: temp-builds, archive-2023.
...
```

### Run Pre-Transfer Checks

Validate connectivity and plugin installation before starting a large transfer.

**To run pre-transfer checks:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --prechecks
```

**Full example:**

```bash
jf rt transfer-files source-server target-server --prechecks
```

Expected output (when checks pass):

```
[Info] Running pre-transfer checks...
[Info] data-transfer plugin found on source instance.
[Info] Source and target instances are reachable.
[Info] Pre-transfer checks passed.
```

### Check Transfer Status

Check the progress of a transfer running in the background. This command reads local state and does not require a server connection.

**To check transfer status:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --status
```

**Full example:**

```bash
jf rt transfer-files source-server target-server --status
```

Expected output when a transfer is in progress:

```
 Status: Running
 Transferred: 3,412 / 10,000 files (34%)
 Current repository: libs-release
```

Expected output when no transfer is running:

```
 Status: Not running
```

### Stop an In-Progress Transfer

Gracefully stop a transfer that is running in the background. This command reads local state and does not require a server connection.

**To stop an in-progress transfer:**

1. Run:

```bash
jf rt transfer-files <source-server-id> <target-server-id> --stop
```

**Full example:**

```bash
jf rt transfer-files source-server target-server --stop
```

Expected output:

```
[Info] Gracefully stopping files transfer...
```

<Callout icon="📘" theme="info">
  Note

  : Re-running `jf rt transfer-files` after a stop will resume from the last checkpoint. Use `--ignore-state` only if you want to restart completely from scratch.
</Callout>

### Get Command Help

**To view command help:**

1. Run:

```bash
jf rt transfer-files --help
```

## When to Use

Use `transfer-files` after `transfer-config` (or `transfer-config-merge`) to move the actual artifact binaries from one Artifactory to another. This is the final step in a full migration workflow.

**Typical migration workflow:**

1. [`jf rt transfer-plugin-install <source-server>`](/docs/transferring-files-between-artifactory-servers/jf-rt-transfer-plugin-install) — Install the data-transfer plugin on the source instance. **Required before any other transfer commands.**
2. [`jf rt transfer-config <source> <target>`](/docs/transferring-files-between-artifactory-servers/jf-rt-transfer-config) — Copy repositories, users, permissions, and other configuration from source to target.
3. `jf rt transfer-files <source> <target>` — Transfer all artifact binaries. Run `--prechecks` first to validate readiness.

## Known Limitations

* Requires the data-transfer plugin installed on the source Artifactory instance. See [`jf rt transfer-plugin-install`](/docs/transferring-files-between-artifactory-servers/jf-rt-transfer-plugin-install).
* Transfer progress is saved; if interrupted, re-running the command resumes from where it stopped (unless `--ignore-state` is set).
* Large-scale transfers (millions of artifacts) may take hours or days depending on network bandwidth.
* The `--filestore` flag makes the transfer check whether artifacts already exist on the target filestore before copying them — useful for shared-storage migrations where files are physically present but not yet indexed.
* Performance depends on network bandwidth between source and target; use `--proxy-key` to route traffic through Artifactory's proxy in controlled environments.

## Performance Considerations

| Repository Size | Expected Duration  | Recommendation                                                     |
| --------------- | ------------------ | ------------------------------------------------------------------ |
| \< 10 GB        | Minutes to an hour | Default settings work fine                                         |
| 10-100 GB       | Hours              | Monitor with `--status`; ensure stable network                     |
| 100 GB - 1 TB   | Hours to a day     | Run during off-peak; use `--include-repos` to batch                |
| > 1 TB          | Days               | Split into batches with `--include-repos`; monitor with `--status` |

<Callout icon="👍" theme="okay">
  Tip

  : If the transfer stalls, use `--status` to check progress. If it has failed, re-run the same command — it resumes from the last checkpoint. Use `--ignore-state` only if you want to start completely fresh.
</Callout>

## Troubleshooting

### "It looks like the 'data-transfer' user plugin isn't installed"

**Full message:**

```
[Error] server response: 400 Bad Request
It looks like the 'data-transfer' user plugin isn't installed on the source instance.
Please refer to the documentation available at https://jfrog.com/help/r/...
```

**What it means:** This error can appear for multiple reasons, not only a missing plugin. Before reinstalling the plugin, work through this checklist:

1. **Verify the source server is reachable.** Run `jf rt ping --server-id <source-server>` to confirm connectivity.
2. **Check for a proxy or load-balancer issue.** An nginx-level `400 Request Header Or Cookie Too Large` in the error body means the request never reached Artifactory. This is a network/proxy configuration issue, not a plugin issue.
3. **Confirm the plugin is installed.** If the source server is reachable and the error persists, follow the [plugin installation instructions](/docs/transferring-files-between-artifactory-servers/jf-rt-transfer-plugin-install) to install or reinstall the data-transfer plugin.

***

### `--stop` shows "Gracefully stopping files transfer..." but nothing was running

This is expected behavior. The CLI emits this message and exits 0 regardless of whether a transfer was in progress. If you need to confirm whether a transfer was actually stopped, run `--status` before and after:

```bash
jf rt transfer-files source-server target-server --status
jf rt transfer-files source-server target-server --stop
jf rt transfer-files source-server target-server --status
```

***

### `--prechecks` reports "Files transfer is already running" unexpectedly

If you ran `--stop` just before `--prechecks`, a transient state file may cause this false positive. Wait a moment and re-run `--prechecks`. If the error persists, check `--status` to determine whether a transfer is genuinely in progress.

<br />