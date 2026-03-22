# Source: https://docs.wandb.ai/models/ref/cli/wandb-restore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb restore

Restore code, config and docker state for a run. Retrieves code from latest commit if code was not saved with `wandb.save()` or `wandb.init(save_code=True)`.

## Usage

```bash  theme={null}
wandb restore RUN [OPTIONS]
```

## Arguments

| Argument | Description              | Required |
| :------- | :----------------------- | :------- |
| `RUN`    | No description available | Yes      |

## Options

| Option            | Description                                                     |
| :---------------- | :-------------------------------------------------------------- |
| `--no-git`        | Don't restore git state (default: False)                        |
| `--branch`        | Whether to create a branch or checkout detached (default: True) |
| `--project`, `-p` | The project you wish to upload to.                              |
| `--entity`, `-e`  | The entity to scope the listing to.                             |
