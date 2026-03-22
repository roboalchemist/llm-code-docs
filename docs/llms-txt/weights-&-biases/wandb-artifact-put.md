# Source: https://docs.wandb.ai/models/ref/cli/wandb-artifact/wandb-artifact-put.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb artifact put

Upload an artifact to wandb

## Usage

```bash  theme={null}
wandb artifact put PATH [OPTIONS]
```

## Arguments

| Argument | Description              | Required |
| :------- | :----------------------- | :------- |
| `PATH`   | No description available | Yes      |

## Options

| Option                | Description                                                               |
| :-------------------- | :------------------------------------------------------------------------ |
| `--name`, `-n`        | The name of the artifact to push: project/artifact\_name                  |
| `--description`, `-d` | A description of this artifact                                            |
| `--type`, `-t`        | The type of the artifact (default: dataset)                               |
| `--alias`, `-a`       | An alias to apply to this artifact (default: \['latest'])                 |
| `--id`                | The run you want to upload to.                                            |
| `--resume`            | Resume the last run from your current directory.                          |
| `--skip_cache`        | Skip caching while uploading artifact files. (default: False)             |
| `--policy`            | Set the storage policy while uploading artifact files. (default: mutable) |
