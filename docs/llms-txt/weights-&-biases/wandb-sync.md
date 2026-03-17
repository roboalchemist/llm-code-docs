# Source: https://docs.wandb.ai/models/ref/cli/wandb-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb sync

Synchronize W\&B run data to the cloud.

If PATH is provided, sync runs found at the given path. If a path is not specified, search for `./wandb` first, then search for a `wandb/` subdirectory.

To sync a specific run:

wandb sync ./wandb/run-20250813\_124246-n67z9ude

Or equivalently:

wandb sync ./wandb/run-20250813\_124246-n67z9ude/run-n67z9ude.wandb

## Usage

```bash  theme={null}
wandb sync [PATH] [OPTIONS]
```

## Arguments

| Argument | Description              | Required |
| :------- | :----------------------- | :------- |
| `PATH`   | No description available | No       |

## Options

| Option               | Description                                                                                  |
| :------------------- | :------------------------------------------------------------------------------------------- |
| `--id`               | The run you want to upload to.                                                               |
| `--project`, `-p`    | The project you want to upload to.                                                           |
| `--entity`, `-e`     | The entity to scope to.                                                                      |
| `--job_type`         | Specifies the type of run for grouping related runs together.                                |
| `--sync-tensorboard` | Stream tfevent files to wandb.                                                               |
| `--include-globs`    | Comma separated list of globs to include.                                                    |
| `--exclude-globs`    | Comma separated list of globs to exclude.                                                    |
| `--include-online`   | Include online runs                                                                          |
| `--include-offline`  | Include offline runs                                                                         |
| `--include-synced`   | Include synced runs                                                                          |
| `--mark-synced`      | Mark runs as synced (default: True)                                                          |
| `--sync-all`         | Sync all runs (default: False)                                                               |
| `--clean`            | Delete synced runs (default: False)                                                          |
| `--clean-old-hours`  | Delete runs created before this many hours. To be used alongside --clean flag. (default: 24) |
| `--clean-force`      | Clean without confirmation prompt. (default: False)                                          |
| `--show`             | Number of runs to show (default: 5)                                                          |
| `--append`           | Append run (default: False)                                                                  |
| `--skip-console`     | Skip console logs (default: False)                                                           |
| `--replace-tags`     | Replace tags in the format 'old\_tag1=new\_tag1,old\_tag2=new\_tag2'                         |
