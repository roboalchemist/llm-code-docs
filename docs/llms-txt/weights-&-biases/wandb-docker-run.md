# Source: https://docs.wandb.ai/models/ref/cli/wandb-docker-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# wandb docker-run

Wrap `docker run` and adds WANDB\_API\_KEY and WANDB\_DOCKER environment variables.

This will also set the runtime to nvidia if the nvidia-docker executable is present on the system and --runtime wasn't set.

See `docker run --help` for more details.

## Usage

```bash  theme={null}
wandb docker-run [DOCKER_RUN_ARGS]
```

## Arguments

| Argument          | Description              | Required |
| :---------------- | :----------------------- | :------- |
| `DOCKER_RUN_ARGS` | No description available | No       |
