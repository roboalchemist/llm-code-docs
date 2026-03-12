# Source: https://docs.kedro.org/en/stable/api/runner/kedro.runner/index.md

# kedro.runner

## kedro.runner

`kedro.runner` provides runners that are able to execute `Pipeline` instances.

| Name                                                                                                                  | Type  | Description                                |
| --------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------ |
| [`kedro.runner.AbstractRunner`](https://docs.kedro.org/en/stable/api/runner/kedro.runner.AbstractRunner/index.md)     | Class | Abstract base class for all Kedro runners. |
| [`kedro.runner.SequentialRunner`](https://docs.kedro.org/en/stable/api/runner/kedro.runner.SequentialRunner/index.md) | Class | Runs nodes sequentially in a pipeline.     |
| [`kedro.runner.ParallelRunner`](https://docs.kedro.org/en/stable/api/runner/kedro.runner.ParallelRunner/index.md)     | Class | Runs nodes in parallel in a pipeline.      |
| [`kedro.runner.ThreadRunner`](https://docs.kedro.org/en/stable/api/runner/kedro.runner.ThreadRunner/index.md)         | Class | Runs nodes in parallel using threads.      |
