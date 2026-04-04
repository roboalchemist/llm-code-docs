# Source: https://docs.wandb.ai/models/ref/cli/wandb-server/wandb-server-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb server start

Start a local W\&B server

## Usage

```bash  theme={null}
wandb server start [OPTIONS]
```

## Options

| Option         | Description                                          |
| :------------- | :--------------------------------------------------- |
| `--port`, `-p` | The host port to bind W\&B server on (default: 8080) |
| `--env`, `-e`  | Env vars to pass to wandb/local (default: \[])       |
| `--daemon`     | Run or don't run in daemon mode (default: True)      |
