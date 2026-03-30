# Source: https://docs.kedro.org/en/stable/api/runner/kedro.runner.AbstractRunner/index.md

## kedro.runner.AbstractRunner

```
AbstractRunner(is_async=False)
```

Bases: `ABC`

`AbstractRunner` is the base class for all `Pipeline` runner implementations.

Parameters:

- **`is_async`** (`bool`, default: `False` ) – If True, the node inputs and outputs are loaded and saved asynchronously with threads. Defaults to False.

Source code in `kedro/runner/runner.py`

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
    self._is_async = is_async
```

### \_is_async

```
_is_async = is_async
```

### \_logger

```
_logger
```

### \_filter_pipeline_for_missing_outputs

```
_filter_pipeline_for_missing_outputs(pipeline, catalog)
```

Filter pipeline to only include nodes that need to run.

Uses reverse topological order to determine which nodes need to run

Source code in `kedro/runner/runner.py`

```
def _filter_pipeline_for_missing_outputs(
    self, pipeline: Pipeline, catalog: CatalogProtocol | SharedMemoryCatalogProtocol
) -> Pipeline:
    """Filter pipeline to only include nodes that need to run.

    Uses reverse topological order to determine which nodes need to run
    """
    original_node_count = len(pipeline.nodes)

    # Get nodes in reverse topological order
    sorted_nodes = list(pipeline.nodes)
    sorted_nodes.reverse()

    # Build node mapping
    node_children = _build_node_children_map(pipeline)

    # Determine which nodes need to run
    nodes_to_run = _determine_nodes_to_run(
        sorted_nodes, catalog, node_children, self._logger
    )

    # Create filtered pipeline
    if not nodes_to_run:
        self._log_filtering_results(
            original_node_count, Pipeline([]), pipeline.nodes
        )
        return Pipeline([])

    filtered_pipeline = pipeline.filter(node_names=[n.name for n in nodes_to_run])
    self._log_filtering_results(
        original_node_count, filtered_pipeline, pipeline.nodes
    )

    return filtered_pipeline
```

### \_get_executor

```
_get_executor(max_workers)
```

Abstract method to provide the correct executor (e.g., ThreadPoolExecutor, ProcessPoolExecutor or None if running sequentially).

Source code in `kedro/runner/runner.py`

```
@abstractmethod  # pragma: no cover
def _get_executor(self, max_workers: int) -> Executor | None:
    """Abstract method to provide the correct executor (e.g., ThreadPoolExecutor, ProcessPoolExecutor or None if running sequentially)."""
    pass
```

### \_get_required_workers_count

```
_get_required_workers_count(pipeline)
```

Source code in `kedro/runner/runner.py`

```
def _get_required_workers_count(self, pipeline: Pipeline) -> int:
    return 1
```

### \_log_filtering_results

```
_log_filtering_results(original_node_count, filtered_pipeline, all_nodes)
```

Log the results of pipeline filtering.

Source code in `kedro/runner/runner.py`

```
def _log_filtering_results(
    self,
    original_node_count: int,
    filtered_pipeline: Pipeline,
    all_nodes: list[Node],
) -> None:
    """Log the results of pipeline filtering."""
    final_node_count = len(filtered_pipeline.nodes)

    if final_node_count == 0:
        self._logger.info(
            f"Skipping all {original_node_count} nodes (all persistent outputs exist)"
        )
        return

    skipped_count = original_node_count - final_node_count
    if skipped_count > 0:
        all_node_names = {n.name for n in all_nodes}
        running_node_names = {n.name for n in filtered_pipeline.nodes}
        skipped_names = all_node_names - running_node_names
        self._logger.info(
            f"Skipping {skipped_count} nodes with existing outputs: "
            f"{', '.join(sorted(skipped_names))}"
        )

    self._logger.info(
        f"Running {final_node_count} out of {original_node_count} nodes"
    )
```

### \_raise_runtime_error

```
_raise_runtime_error(todo_nodes, done_nodes, ready, done)
```

Source code in `kedro/runner/runner.py`

```
@staticmethod
def _raise_runtime_error(
    todo_nodes: set[Node],
    done_nodes: set[Node],
    ready: set[Node],
    done: set[Future[Node]] | None,
) -> None:
    debug_data = {
        "todo_nodes": todo_nodes,
        "done_nodes": done_nodes,
        "ready_nodes": ready,
        "done_futures": done,
    }
    debug_data_str = "\n".join(f"{k} = {v}" for k, v in debug_data.items())
    raise RuntimeError(
        f"Unable to schedule new tasks although some nodes "
        f"have not been run:\n{debug_data_str}"
    )
```

### \_release_datasets

```
_release_datasets(node, catalog, load_counts, pipeline)
```

Decrement dataset load counts and release any datasets we've finished with

Source code in `kedro/runner/runner.py`

```
@staticmethod
def _release_datasets(
    node: Node,
    catalog: CatalogProtocol | SharedMemoryCatalogProtocol,
    load_counts: dict,
    pipeline: Pipeline,
) -> None:
    """Decrement dataset load counts and release any datasets we've finished with"""
    for dataset in node.inputs:
        load_counts[dataset] -= 1
        if load_counts[dataset] < 1 and dataset not in pipeline.inputs():
            catalog.release(dataset)
    for dataset in node.outputs:
        if load_counts[dataset] < 1 and dataset not in pipeline.outputs():
            catalog.release(dataset)
```

### \_run

```
_run(pipeline, catalog, hook_manager=None, run_id=None)
```

The abstract interface for running pipelines, assuming that the inputs have already been checked and normalized by run(). This contains the Common pipeline execution logic using an executor.

Parameters:

- **`pipeline`** (`Pipeline`) – The Pipeline to run.
- **`catalog`** (`CatalogProtocol | SharedMemoryCatalogProtocol`) – An implemented instance of CatalogProtocol or SharedMemoryCatalogProtocol from which to fetch data.
- **`hook_manager`** (`PluginManager | None`, default: `None` ) – The PluginManager to activate hooks.
- **`run_id`** (`str | None`, default: `None` ) – The id of the run.

Source code in `kedro/runner/runner.py`

```
@abstractmethod  # pragma: no cover
def _run(
    self,
    pipeline: Pipeline,
    catalog: CatalogProtocol | SharedMemoryCatalogProtocol,
    hook_manager: PluginManager | None = None,
    run_id: str | None = None,
) -> None:
    """The abstract interface for running pipelines, assuming that the
     inputs have already been checked and normalized by run().
     This contains the Common pipeline execution logic using an executor.

    Args:
        pipeline: The ``Pipeline`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` or ``SharedMemoryCatalogProtocol`` from which to fetch data.
        hook_manager: The ``PluginManager`` to activate hooks.
        run_id: The id of the run.
    """

    nodes = pipeline.nodes

    self._validate_catalog(catalog)
    self._validate_nodes(nodes)
    self._set_manager_datasets(catalog)

    load_counts = Counter(chain.from_iterable(n.inputs for n in pipeline.nodes))
    node_dependencies = pipeline.node_dependencies
    todo_nodes = set(node_dependencies.keys())
    done_nodes: set[Node] = set()
    futures = set()
    done = None
    max_workers = self._get_required_workers_count(pipeline)

    pool = self._get_executor(max_workers)
    if pool is None:
        for exec_index, node in enumerate(nodes):
            try:
                Task(
                    node=node,
                    catalog=catalog,
                    hook_manager=hook_manager,
                    is_async=self._is_async,
                    run_id=run_id,
                ).execute()
                done_nodes.add(node)
            except Exception:
                self._suggest_resume_scenario(pipeline, done_nodes, catalog)
                raise
            self._logger.info("Completed node: %s", node.name)
            self._logger.info(
                "Completed %d out of %d tasks", len(done_nodes), len(nodes)
            )
            self._release_datasets(node, catalog, load_counts, pipeline)

        return  # Exit early since everything runs sequentially

    with pool as executor:
        while True:
            ready = {n for n in todo_nodes if node_dependencies[n] <= done_nodes}
            todo_nodes -= ready
            for node in ready:
                task = Task(
                    node=node,
                    catalog=catalog,
                    hook_manager=hook_manager,
                    is_async=self._is_async,
                    run_id=run_id,
                )
                if isinstance(executor, ProcessPoolExecutor):
                    task.parallel = True
                futures.add(executor.submit(task))
            if not futures:
                if todo_nodes:
                    self._raise_runtime_error(todo_nodes, done_nodes, ready, done)
                break
            done, futures = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                try:
                    node = future.result()
                except Exception:
                    self._suggest_resume_scenario(pipeline, done_nodes, catalog)
                    raise
                done_nodes.add(node)
                self._logger.info("Completed node: %s", node.name)
                self._logger.info(
                    "Completed %d out of %d tasks", len(done_nodes), len(nodes)
                )
                self._release_datasets(node, catalog, load_counts, pipeline)
```

### \_set_manager_datasets

```
_set_manager_datasets(catalog)
```

Source code in `kedro/runner/runner.py`

```
def _set_manager_datasets(
    self, catalog: CatalogProtocol | SharedMemoryCatalogProtocol
) -> None:
    # Set up any necessary manager datasets here
    pass
```

### \_suggest_resume_scenario

```
_suggest_resume_scenario(pipeline, done_nodes, catalog)
```

Suggest a command to the user to resume a run after it fails. The run should be started from the point closest to the failure for which persisted input exists.

Parameters:

- **`pipeline`** (`Pipeline`) – the Pipeline of the run.
- **`done_nodes`** (`Iterable[Node]`) – the Nodes that executed successfully.
- **`catalog`** (`CatalogProtocol | SharedMemoryCatalogProtocol`) – an implemented instance of CatalogProtocol or SharedMemoryCatalogProtocol of the run.

Source code in `kedro/runner/runner.py`

```
def _suggest_resume_scenario(
    self,
    pipeline: Pipeline,
    done_nodes: Iterable[Node],
    catalog: CatalogProtocol | SharedMemoryCatalogProtocol,
) -> None:
    """
    Suggest a command to the user to resume a run after it fails.
    The run should be started from the point closest to the failure
    for which persisted input exists.

    Args:
        pipeline: the ``Pipeline`` of the run.
        done_nodes: the ``Node``s that executed successfully.
        catalog: an implemented instance of ``CatalogProtocol`` or ``SharedMemoryCatalogProtocol`` of the run.

    """
    remaining_nodes = set(pipeline.nodes) - set(done_nodes)

    postfix = ""
    if done_nodes:
        start_node_names = _find_nodes_to_resume_from(
            pipeline=pipeline,
            unfinished_nodes=remaining_nodes,
            catalog=catalog,
        )
        start_nodes_str = ",".join(sorted(start_node_names))
        postfix += f'  --from-nodes "{start_nodes_str}"'

    if not postfix:
        self._logger.warning(
            "No nodes ran. Repeat the previous command to attempt a new run."
        )
    else:
        self._logger.warning(
            f"There are {len(remaining_nodes)} nodes that have not run.\n"
            "You can resume the pipeline run from the nearest nodes with "
            "persisted inputs by adding the following "
            f"argument to your previous command:\n{postfix}"
        )
```

### \_validate_catalog

```
_validate_catalog(catalog)
```

Source code in `kedro/runner/runner.py`

```
def _validate_catalog(
    self, catalog: CatalogProtocol | SharedMemoryCatalogProtocol
) -> None:
    # Add catalog validation logic here if needed
    pass
```

### \_validate_max_workers

```
_validate_max_workers(max_workers)
```

Validates and returns the number of workers. Sets to os.cpu_count() or 1 if max_workers is None, and limits max_workers to 61 on Windows.

Parameters:

- **`max_workers`** (`int | None`) – Desired number of workers. If None, defaults to os.cpu_count() or 1.

Returns:

- `int` – A valid number of workers to use.

Raises:

- `ValueError` – If max_workers is set and is not positive.

Source code in `kedro/runner/runner.py`

```
@classmethod
def _validate_max_workers(cls, max_workers: int | None) -> int:
    """
    Validates and returns the number of workers. Sets to os.cpu_count() or 1 if max_workers is None,
    and limits max_workers to 61 on Windows.

    Args:
        max_workers: Desired number of workers. If None, defaults to os.cpu_count() or 1.

    Returns:
        A valid number of workers to use.

    Raises:
        ValueError: If max_workers is set and is not positive.
    """
    if max_workers is None:
        max_workers = os.cpu_count() or 1
        if sys.platform == "win32":
            max_workers = min(_MAX_WINDOWS_WORKERS, max_workers)
    elif max_workers <= 0:
        raise ValueError("max_workers should be positive")

    return max_workers
```

### \_validate_nodes

```
_validate_nodes(node)
```

Source code in `kedro/runner/runner.py`

```
def _validate_nodes(self, node: Iterable[Node]) -> None:
    # Add node validation logic here if needed
    pass
```

### run

```
run(pipeline, catalog, hook_manager=None, run_id=None, only_missing_outputs=False)
```

Run the `Pipeline` using the datasets provided by `catalog` and save results back to the same objects.

Parameters:

- **`pipeline`** (`Pipeline`) – The Pipeline to run.
- **`catalog`** (`CatalogProtocol | SharedMemoryCatalogProtocol`) – An implemented instance of CatalogProtocol or SharedMemoryCatalogProtocol from which to fetch data.
- **`hook_manager`** (`PluginManager | None`, default: `None` ) – The PluginManager to activate hooks.
- **`run_id`** (`str | None`, default: `None` ) – The id of the run.
- **`only_missing_outputs`** (`bool`, default: `False` ) – Run only nodes with missing outputs.

Raises:

- `ValueError` – Raised when Pipeline inputs cannot be satisfied.

Returns:

- `dict[str, Any]` – Dictionary with pipeline outputs, where keys are dataset names
- `dict[str, Any]` – and values are dataset objects.

Source code in `kedro/runner/runner.py`

```
def run(
    self,
    pipeline: Pipeline,
    catalog: CatalogProtocol | SharedMemoryCatalogProtocol,
    hook_manager: PluginManager | None = None,
    run_id: str | None = None,
    only_missing_outputs: bool = False,
) -> dict[str, Any]:
    """Run the ``Pipeline`` using the datasets provided by ``catalog``
    and save results back to the same objects.

    Args:
        pipeline: The ``Pipeline`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` or ``SharedMemoryCatalogProtocol`` from which to fetch data.
        hook_manager: The ``PluginManager`` to activate hooks.
        run_id: The id of the run.
        only_missing_outputs: Run only nodes with missing outputs.

    Raises:
        ValueError: Raised when ``Pipeline`` inputs cannot be satisfied.

    Returns:
        Dictionary with pipeline outputs, where keys are dataset names
        and values are dataset objects.
    """
    # Apply missing outputs filtering if requested
    if only_missing_outputs:
        pipeline = self._filter_pipeline_for_missing_outputs(pipeline, catalog)

    # Check which datasets used in the pipeline are in the catalog or match
    # a pattern in the catalog, not including extra dataset patterns
    # Run a warm-up to materialize all datasets in the catalog before run
    warmed_up_ds = []
    for ds in pipeline.datasets():
        if ds in catalog:
            warmed_up_ds.append(ds)
        _ = catalog.get(ds, fallback_to_runtime_pattern=True)

    # Check if there are any input datasets that aren't in the catalog and
    # don't match a pattern in the catalog.
    unsatisfied = pipeline.inputs() - set(warmed_up_ds)

    if unsatisfied:
        raise ValueError(
            f"Pipeline input(s) {unsatisfied} not found in the {catalog.__class__.__name__}"
        )

    hook_or_null_manager = hook_manager or _NullPluginManager()

    if self._is_async:
        self._logger.info(
            "Asynchronous mode is enabled for loading and saving data."
        )

    start_time = perf_counter()
    self._run(pipeline, catalog, hook_or_null_manager, run_id)  # type: ignore[arg-type]
    end_time = perf_counter()
    run_duration = end_time - start_time

    self._logger.info(
        f"Pipeline execution completed successfully in {run_duration:.1f} sec."
    )

    # Now we return all pipeline outputs, but we do not load datasets data
    run_output = {ds_name: catalog[ds_name] for ds_name in pipeline.outputs()}

    return run_output
```
