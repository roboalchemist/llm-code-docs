# Source: https://docs.kedro.org/en/stable/api/runner/kedro.runner.SequentialRunner/index.md

## kedro.runner.SequentialRunner

```
SequentialRunner(is_async=False)
```

Bases: `AbstractRunner`

`SequentialRunner` is an `AbstractRunner` implementation. It can be used to run the `Pipeline` in a sequential manner using a topological sort of provided nodes.

Parameters:

- **`is_async`** (`bool`, default: `False` ) – If True, the node inputs and outputs are loaded and saved asynchronously with threads. Defaults to False.

Source code in `kedro/runner/sequential_runner.py`

```
def __init__(
    self,
    is_async: bool = False,
):
    """Instantiates the runner class.

    Args:
        is_async: If True, the node inputs and outputs are loaded and saved
            asynchronously with threads. Defaults to False.
    """
    super().__init__(is_async=is_async)
```

### \_get_executor

```
_get_executor(max_workers)
```

Source code in `kedro/runner/sequential_runner.py`

```
def _get_executor(self, max_workers: int) -> None:
    return None
```

### \_run

```
_run(pipeline, catalog, hook_manager=None, run_id=None)
```

The method implementing sequential pipeline running.

Parameters:

- **`pipeline`** (`Pipeline`) – The Pipeline to run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol from which to fetch data.
- **`hook_manager`** (`PluginManager | None`, default: `None` ) – The PluginManager to activate hooks.
- **`run_id`** (`str | None`, default: `None` ) – The id of the run.

Raises:

- `Exception` – in case of any downstream node failure.

Source code in `kedro/runner/sequential_runner.py`

```
def _run(
    self,
    pipeline: Pipeline,
    catalog: CatalogProtocol,
    hook_manager: PluginManager | None = None,
    run_id: str | None = None,
) -> None:
    """The method implementing sequential pipeline running.

    Args:
        pipeline: The ``Pipeline`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` from which to fetch data.
        hook_manager: The ``PluginManager`` to activate hooks.
        run_id: The id of the run.

    Raises:
        Exception: in case of any downstream node failure.
    """
    if not self._is_async:
        self._logger.info(
            "Using synchronous mode for loading and saving data. Use the --async flag "
            "for potential performance gains. https://docs.kedro.org/en/stable/build/run_a_pipeline/#load-and-save-asynchronously"
        )
    super()._run(
        pipeline=pipeline,
        catalog=catalog,
        hook_manager=hook_manager,
        run_id=run_id,
    )
```
