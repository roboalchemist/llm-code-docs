# Source: https://docs.wandb.ai/models/ref/cli/wandb-beta/wandb-beta-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb beta sync

Upload .wandb files specified by PATHS.

This is a beta re-implementation of `wandb sync`. It is not feature complete, not guaranteed to work, and may change in backward-incompatible ways in any release of wandb.

PATHS can include .wandb files, run directories containing .wandb files, and "wandb" directories containing run directories.

For example, to sync all runs in a directory:

```bash  theme={null}
wandb beta sync ./wandb
```

To sync a specific run:

```bash  theme={null}
wandb beta sync ./wandb/run-20250813_124246-n67z9ude
```

Or equivalently:

```bash  theme={null}
wandb beta sync ./wandb/run-20250813_124246-n67z9ude/run-n67z9ude.wandb
```

## Usage

```bash  theme={null}
wandb beta sync [PATHS] [OPTIONS]
```

## Arguments

| Argument | Description              | Required |
| :------- | :----------------------- | :------- |
| `PATHS`  | No description available | No       |

## Options

| Option            | Description                                                                                                                                                                                                                                                                       |
| :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--live`          | Sync a run while it's still being logged. This may hang if the process generating the run crashes uncleanly. (default: False)                                                                                                                                                     |
| `-e`, `--entity`  | An entity override to use for all runs being synced. (default: )                                                                                                                                                                                                                  |
| `-p`, `--project` | A project override to use for all runs being synced. (default: )                                                                                                                                                                                                                  |
| `--id`            | A run ID override to use for all runs being synced. If setting this and syncing multiple files (with the same entity and project), the files will be synced in order of start time. This is intended to work with syncing multiple resumed fragments of the same run. (default: ) |
| `--job-type`      | A job type override for all runs being synced. (default: )                                                                                                                                                                                                                        |
| `--replace-tags`  | Rename tags using the format 'old1=new1,old2=new2'. (default: )                                                                                                                                                                                                                   |
| `--skip-synced`   | Skip runs that have already been synced with this command. (default: True)                                                                                                                                                                                                        |
| `--dry-run`       | Print what would happen without uploading anything. (default: False)                                                                                                                                                                                                              |
| `-v`, `--verbose` | Print more information. (default: False)                                                                                                                                                                                                                                          |
| `-n`              | Max number of runs to sync at a time. When syncing multiple files that are part of the same run, the files are synced sequentially in order of start time regardless of this setting. This happens for resumed runs or when using the --id parameter. (default: 5)                |
