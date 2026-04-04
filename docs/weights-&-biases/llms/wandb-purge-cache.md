# Source: https://docs.wandb.ai/models/ref/cli/wandb-purge-cache.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb purge-cache

Purges cached logs, run history, and artifacts from the local W\&B cache.

## Usage

```bash  theme={null}
wandb purge-cache [OPTIONS]
```

## Options

| Option    | Description                                                                                                  |
| :-------- | :----------------------------------------------------------------------------------------------------------- |
| `--age`   | Removes items older than the specified time period (e.g., '10s', '5m', '8h', '7d', '6M', '1y') (default: 0d) |
| `--force` | Do not prompt for confirmation when deleting files. (default: False)                                         |
