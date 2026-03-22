# Source: https://docs.wandb.ai/models/ref/cli/wandb-local.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb local

Start a local W\&B container (deprecated, see wandb server --help)

## Usage

```bash  theme={null}
wandb local [OPTIONS]
```

## Options

| Option         | Description                                         |
| :------------- | :-------------------------------------------------- |
| `--port`, `-p` | The host port to bind W\&B local on (default: 8080) |
| `--env`, `-e`  | Env vars to pass to wandb/local (default: \[])      |
| `--daemon`     | Run or don't run in daemon mode (default: True)     |
| `--upgrade`    | Upgrade to the most recent version (default: False) |
