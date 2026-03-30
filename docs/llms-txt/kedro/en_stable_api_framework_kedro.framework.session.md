# Source: https://docs.kedro.org/en/stable/api/framework/kedro.framework.session/index.md

## kedro.framework.session

`kedro.framework.session` provides access to KedroSession responsible for project lifecycle.

| Module                                                                | Description                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`kedro.framework.session.session`](#kedro.framework.session.session) | Implements Kedro session responsible for project lifecycle.         |
| [`kedro.framework.session.store`](#kedro.framework.session.store)     | Implements a dict-like store object used to persist Kedro sessions. |

## kedro.framework.session.session

This module implements Kedro session responsible for project lifecycle.

### kedro_version

```
kedro_version = '1.2.0'
```

### pipelines

```
pipelines = _ProjectPipelines()
```

### settings

```
settings = _ProjectSettings()
```

### AbstractConfigLoader

```
AbstractConfigLoader(conf_source, env=None, runtime_params=None, **kwargs)
```

Bases: `UserDict`

`AbstractConfigLoader` is the abstract base class for all `ConfigLoader` implementations. All user-defined `ConfigLoader` implementations should inherit from `AbstractConfigLoader` and implement all relevant abstract methods.

Source code in `kedro/config/abstract_config.py`

```
def __init__(
    self,
    conf_source: str | Path,
    env: str | None = None,
    runtime_params: dict[str, Any] | None = None,
    **kwargs: Any,
):
    super().__init__()
    self.conf_source = conf_source
    self.env = env
    self.runtime_params = runtime_params or {}
```

#### get

```
get(key, default=None)
```

D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.

Source code in `kedro/config/abstract_config.py`

```
def get(self, key: str, default: Any = None) -> Any:
    "D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."
    try:
        return self[key]
    except KeyError:
        return default
```

### AbstractRunner

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

#### run

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

### BaseSessionStore

```
BaseSessionStore(path, session_id)
```

Bases: `UserDict`

`BaseSessionStore` is the base class for all session stores. `BaseSessionStore` is an ephemeral store implementation that doesn't persist the session data.

Source code in `kedro/framework/session/store.py`

```
def __init__(self, path: str, session_id: str):
    self._path = path
    self._session_id = session_id
    super().__init__(self.read())
```

#### read

```
read()
```

Read the data from the session store.

Returns:

- `dict[str, Any]` – A mapping containing the session store data.

Source code in `kedro/framework/session/store.py`

```
def read(self) -> dict[str, Any]:
    """Read the data from the session store.

    Returns:
        A mapping containing the session store data.
    """
    self._logger.debug(
        "'read()' not implemented for '%s'. Assuming empty store.",
        self.__class__.__name__,
    )
    return {}
```

#### save

```
save()
```

Persist the session store

Source code in `kedro/framework/session/store.py`

```
def save(self) -> None:
    """Persist the session store"""
    self._logger.debug(
        "'save()' not implemented for '%s'. Skipping the step.",
        self.__class__.__name__,
    )
```

### KedroContext

`KedroContext` is the base class which holds the configuration and Kedro's main functionality.

Create a context object by providing the root of a Kedro project and the environment configuration subfolders (see `kedro.config.OmegaConfigLoader`) Raises: KedroContextError: If there is a mismatch between Kedro project version and package version. Args: project_path: Project path to define the context for. config_loader: Kedro's `OmegaConfigLoader` for loading the configuration files. env: Optional argument for configuration default environment to be used for running the pipeline. If not specified, it defaults to "local". package_name: Package name for the Kedro project the context is created for. hook_manager: The `PluginManager` to activate hooks, supplied by the session. runtime_params: Optional dictionary containing runtime project parameters. If specified, will update (and therefore take precedence over) the parameters retrieved from the project configuration.

#### catalog

```
catalog
```

Read-only property referring to Kedro's catalog\` for this context.

Returns:

- `CatalogProtocol` – catalog defined in catalog.yml.

Raises: KedroContextError: Incorrect catalog registered for the project.

#### params

```
params
```

Read-only property referring to Kedro's parameters for this context.

Returns:

- `dict[str, Any]` – Parameters defined in parameters.yml with the addition of any extra parameters passed at initialization.

### KedroSession

```
KedroSession(session_id, package_name=None, project_path=None, save_on_close=False, conf_source=None)
```

`KedroSession` is the object that is responsible for managing the lifecycle of a Kedro run. Use `KedroSession.create()` as a context manager to construct a new KedroSession with session data provided (see the example below).

Example:

```
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path

# If you are creating a session outside of a Kedro project (i.e. not using
# `kedro run` or `kedro jupyter`), you need to run `bootstrap_project` to
# let Kedro find your configuration.
bootstrap_project(Path("<project_root>"))
with KedroSession.create() as session:
    session.run()
```

Source code in `kedro/framework/session/session.py`

```
def __init__(
    self,
    session_id: str,
    package_name: str | None = None,
    project_path: Path | str | None = None,
    save_on_close: bool = False,
    conf_source: str | None = None,
):
    self._project_path = Path(
        project_path or find_kedro_project(Path.cwd()) or Path.cwd()
    ).resolve()
    self.session_id = session_id
    self.save_on_close = save_on_close
    self._package_name = package_name or kedro_project.PACKAGE_NAME
    self._store = self._init_store()
    self._run_called = False

    hook_manager = _create_hook_manager()
    _register_hooks(hook_manager, settings.HOOKS)
    _register_hooks_entry_points(hook_manager, settings.DISABLE_HOOKS_FOR_PLUGINS)
    self._hook_manager = hook_manager

    self._conf_source = conf_source or str(
        self._project_path / settings.CONF_SOURCE
    )
```

#### store

```
store
```

Return a copy of internal store.

#### close

```
close()
```

Close the current session and save its store to disk if `save_on_close` attribute is True.

Source code in `kedro/framework/session/session.py`

```
def close(self) -> None:
    """Close the current session and save its store to disk
    if `save_on_close` attribute is True.
    """
    if self.save_on_close:
        self._store.save()
```

#### create

```
create(project_path=None, save_on_close=True, env=None, runtime_params=None, conf_source=None)
```

Create a new instance of `KedroSession` with the session data.

Parameters:

- **`project_path`** (`Path | str | None`, default: `None` ) – Path to the project root directory. Default is current working directory Path.cwd().
- **`save_on_close`** (`bool`, default: `True` ) – Whether or not to save the session when it's closed.
- **`conf_source`** (`str | None`, default: `None` ) – Path to a directory containing configuration
- **`env`** (`str | None`, default: `None` ) – Environment for the KedroContext.
- **`runtime_params`** (`dict[str, Any] | None`, default: `None` ) – Optional dictionary containing extra project parameters for underlying KedroContext. If specified, will update (and therefore take precedence over) the parameters retrieved from the project configuration.

Returns:

- `KedroSession` – A new KedroSession instance.

Source code in `kedro/framework/session/session.py`

```
@classmethod
def create(
    cls,
    project_path: Path | str | None = None,
    save_on_close: bool = True,
    env: str | None = None,
    runtime_params: dict[str, Any] | None = None,
    conf_source: str | None = None,
) -> KedroSession:
    """Create a new instance of ``KedroSession`` with the session data.

    Args:
        project_path: Path to the project root directory. Default is
            current working directory Path.cwd().
        save_on_close: Whether or not to save the session when it's closed.
        conf_source: Path to a directory containing configuration
        env: Environment for the KedroContext.
        runtime_params: Optional dictionary containing extra project parameters
            for underlying KedroContext. If specified, will update (and therefore
            take precedence over) the parameters retrieved from the project
            configuration.

    Returns:
        A new ``KedroSession`` instance.
    """
    validate_settings()

    session = cls(
        project_path=project_path,
        session_id=generate_timestamp(),
        save_on_close=save_on_close,
        conf_source=conf_source,
    )

    # have to explicitly type session_data otherwise mypy will complain
    # possibly related to this: https://github.com/python/mypy/issues/1430
    session_data: dict[str, Any] = {
        "project_path": session._project_path,
        "session_id": session.session_id,
    }

    ctx = click.get_current_context(silent=True)
    if ctx:
        session_data["cli"] = _jsonify_cli_context(ctx)

    env = env or os.getenv("KEDRO_ENV")
    if env:
        session_data["env"] = env

    if runtime_params:
        session_data["runtime_params"] = runtime_params

    try:
        session_data["username"] = getpass.getuser()
    except Exception as exc:
        logging.getLogger(__name__).debug(
            "Unable to get username. Full exception: %s", exc
        )

    session_data.update(**_describe_git(session._project_path))
    session._store.update(session_data)

    return session
```

#### load_context

```
load_context()
```

An instance of the project context.

Source code in `kedro/framework/session/session.py`

```
def load_context(self) -> KedroContext:
    """An instance of the project context."""
    env = self.store.get("env")
    runtime_params = self.store.get("runtime_params")
    config_loader = self._get_config_loader()
    context_class = settings.CONTEXT_CLASS
    context = context_class(
        package_name=self._package_name,
        project_path=self._project_path,
        config_loader=config_loader,
        env=env,
        runtime_params=runtime_params,
        hook_manager=self._hook_manager,
    )
    self._hook_manager.hook.after_context_created(context=context)

    return context  # type: ignore[no-any-return]
```

#### run

```
run(pipeline_name=None, pipeline_names=None, tags=None, runner=None, node_names=None, from_nodes=None, to_nodes=None, from_inputs=None, to_outputs=None, load_versions=None, namespaces=None, only_missing_outputs=False)
```

Runs the pipeline with a specified runner.

Parameters:

- **`pipeline_name`** (`str | None`, default: `None` ) – Name of the pipeline that is being run.
- **`pipeline_names`** (`list[str] | None`, default: `None` ) – Name of the pipelines that is being run.
- **`tags`** (`Iterable[str] | None`, default: `None` ) – An optional list of node tags which should be used to filter the nodes of the Pipeline. If specified, only the nodes containing any of these tags will be run.
- **`runner`** (`AbstractRunner | None`, default: `None` ) – An optional parameter specifying the runner that you want to run the pipeline with.
- **`node_names`** (`Iterable[str] | None`, default: `None` ) – An optional list of node names which should be used to filter the nodes of the Pipeline. If specified, only the nodes with these names will be run.
- **`from_nodes`** (`Iterable[str] | None`, default: `None` ) – An optional list of node names which should be used as a starting point of the new Pipeline.
- **`to_nodes`** (`Iterable[str] | None`, default: `None` ) – An optional list of node names which should be used as an end point of the new Pipeline.
- **`from_inputs`** (`Iterable[str] | None`, default: `None` ) – An optional list of input datasets which should be used as a starting point of the new Pipeline.
- **`to_outputs`** (`Iterable[str] | None`, default: `None` ) – An optional list of output datasets which should be used as an end point of the new Pipeline.
- **`load_versions`** (`dict[str, str] | None`, default: `None` ) – An optional flag to specify a particular dataset version timestamp to load.
- **`namespaces`** (`Iterable[str] | None`, default: `None` ) – The namespaces of the nodes that are being run.
- **`only_missing_outputs`** (`bool`, default: `False` ) – Run only nodes with missing outputs.

Raises: ValueError: If the named or `__default__` pipeline is not defined by `register_pipelines`. Exception: Any uncaught exception during the run will be re-raised after being passed to `on_pipeline_error` hook. KedroSessionError: If more than one run is attempted to be executed during a single session. Returns: Dictionary with pipeline outputs, where keys are dataset names and values are dataset objects.

Source code in `kedro/framework/session/session.py`

```
def run(  # noqa: PLR0913
    self,
    pipeline_name: str | None = None,
    pipeline_names: list[str] | None = None,
    tags: Iterable[str] | None = None,
    runner: AbstractRunner | None = None,
    node_names: Iterable[str] | None = None,
    from_nodes: Iterable[str] | None = None,
    to_nodes: Iterable[str] | None = None,
    from_inputs: Iterable[str] | None = None,
    to_outputs: Iterable[str] | None = None,
    load_versions: dict[str, str] | None = None,
    namespaces: Iterable[str] | None = None,
    only_missing_outputs: bool = False,
) -> dict[str, Any]:
    """Runs the pipeline with a specified runner.

    Args:
        pipeline_name: Name of the pipeline that is being run.
        pipeline_names: Name of the pipelines that is being run.
        tags: An optional list of node tags which should be used to
            filter the nodes of the ``Pipeline``. If specified, only the nodes
            containing *any* of these tags will be run.
        runner: An optional parameter specifying the runner that you want to run
            the pipeline with.
        node_names: An optional list of node names which should be used to
            filter the nodes of the ``Pipeline``. If specified, only the nodes
            with these names will be run.
        from_nodes: An optional list of node names which should be used as a
            starting point of the new ``Pipeline``.
        to_nodes: An optional list of node names which should be used as an
            end point of the new ``Pipeline``.
        from_inputs: An optional list of input datasets which should be
            used as a starting point of the new ``Pipeline``.
        to_outputs: An optional list of output datasets which should be
            used as an end point of the new ``Pipeline``.
        load_versions: An optional flag to specify a particular dataset
            version timestamp to load.
        namespaces: The namespaces of the nodes that are being run.
        only_missing_outputs: Run only nodes with missing outputs.
    Raises:
        ValueError: If the named or `__default__` pipeline is not
            defined by `register_pipelines`.
        Exception: Any uncaught exception during the run will be re-raised
            after being passed to ``on_pipeline_error`` hook.
        KedroSessionError: If more than one run is attempted to be executed during
            a single session.
    Returns:
        Dictionary with pipeline outputs, where keys are dataset names
        and values are dataset objects.
    """
    # Report project name
    project_name = self._package_name or self._project_path.name
    self._logger.info("Kedro project %s", project_name)
    if pipeline_name:
        self._logger.warning(
            "`pipeline_name` is deprecated and will be removed in a future release. "
            "Please use `pipeline_names` instead."
        )
        pipeline_names = [pipeline_name]

    if self._run_called:
        raise KedroSessionError(
            "A run has already been completed as part of the"
            " active KedroSession. KedroSession has a 1-1 mapping with"
            " runs, and thus only one run should be executed per session."
        )

    session_id = self.store["session_id"]
    save_version = session_id
    runtime_params = self.store.get("runtime_params") or {}
    context = self.load_context()

    names = pipeline_names or ["__default__"]
    combined_pipelines = Pipeline([])
    for name in names:
        try:
            combined_pipelines += pipelines[name]
        except KeyError as exc:
            raise ValueError(
                f"Failed to find the pipeline named '{name}'. "
                f"It needs to be generated and returned "
                f"by the 'register_pipelines' function."
            ) from exc

    filtered_pipeline = combined_pipelines.filter(
        tags=tags,
        from_nodes=from_nodes,
        to_nodes=to_nodes,
        node_names=node_names,
        from_inputs=from_inputs,
        to_outputs=to_outputs,
        node_namespaces=namespaces,
    )

    record_data = {
        "session_id": session_id,
        "project_path": self._project_path.as_posix(),
        "env": context.env,
        "kedro_version": kedro_version,
        "tags": tags,
        "from_nodes": from_nodes,
        "to_nodes": to_nodes,
        "node_names": node_names,
        "from_inputs": from_inputs,
        "to_outputs": to_outputs,
        "load_versions": load_versions,
        "runtime_params": runtime_params,
        "pipeline_names": pipeline_names,
        "namespaces": namespaces,
        "runner": getattr(runner, "__name__", str(runner)),
        "only_missing_outputs": only_missing_outputs,
    }

    runner = runner or SequentialRunner()
    if not isinstance(runner, AbstractRunner):
        raise KedroSessionError(
            "KedroSession expect an instance of Runner instead of a class."
            "Have you forgotten the `()` at the end of the statement?"
        )

    catalog_class = (
        SharedMemoryDataCatalog
        if isinstance(runner, ParallelRunner)
        else settings.DATA_CATALOG_CLASS
    )

    catalog = context._get_catalog(
        catalog_class=catalog_class,
        save_version=save_version,
        load_versions=load_versions,
    )

    # Run the runner
    hook_manager = self._hook_manager
    hook_manager.hook.before_pipeline_run(
        run_params=record_data, pipeline=filtered_pipeline, catalog=catalog
    )
    try:
        run_result = runner.run(
            filtered_pipeline,
            catalog,
            hook_manager,
            run_id=session_id,
            only_missing_outputs=only_missing_outputs,
        )
        self._run_called = True
    except Exception as error:
        hook_manager.hook.on_pipeline_error(
            error=error,
            run_params=record_data,
            pipeline=filtered_pipeline,
            catalog=catalog,
        )
        raise

    hook_manager.hook.after_pipeline_run(
        run_params=record_data,
        run_result=run_result,
        pipeline=filtered_pipeline,
        catalog=catalog,
    )
    return run_result
```

### KedroSessionError

Bases: `Exception`

`KedroSessionError` raised by `KedroSession` in the case that multiple runs are attempted in one session.

### ParallelRunner

```
ParallelRunner(max_workers=None, is_async=False)
```

Bases: `AbstractRunner`

`ParallelRunner` is an `AbstractRunner` implementation. It can be used to run the `Pipeline` in parallel groups formed by toposort. Please note that this `runner` implementation validates dataset using the `_validate_catalog` method, which checks if any of the datasets are single process only using the `_SINGLE_PROCESS` dataset attribute.

Parameters:

- **`max_workers`** (`int | None`, default: `None` ) – Number of worker processes to spawn. If not set, calculated automatically based on the pipeline configuration and CPU core count. On windows machines, the max_workers value cannot be larger than 61 and will be set to min(61, max_workers).
- **`is_async`** (`bool`, default: `False` ) – If True, the node inputs and outputs are loaded and saved asynchronously with threads. Defaults to False.

Raises: ValueError: bad parameters passed

Source code in `kedro/runner/parallel_runner.py`

```
def __init__(
    self,
    max_workers: int | None = None,
    is_async: bool = False,
):
    """
    Instantiates the runner by creating a Manager.

    Args:
        max_workers: Number of worker processes to spawn. If not set,
            calculated automatically based on the pipeline configuration
            and CPU core count. On windows machines, the max_workers value
            cannot be larger than 61 and will be set to min(61, max_workers).
        is_async: If True, the node inputs and outputs are loaded and saved
            asynchronously with threads. Defaults to False.
    Raises:
        ValueError: bad parameters passed
    """
    super().__init__(is_async=is_async)
    self._manager = ParallelRunnerManager()
    self._manager.start()

    self._max_workers = self._validate_max_workers(max_workers)
```

### Pipeline

```
Pipeline(nodes, *, inputs=None, outputs=None, parameters=None, tags=None, namespace=None, prefix_datasets_with_namespace=True)
```

A `Pipeline` defined as a collection of `Node` objects. This class treats nodes as part of a graph representation and provides inputs, outputs and execution order.

Parameters:

- **`nodes`** (`Iterable[Node | Pipeline] | Pipeline`) – The iterable of nodes the Pipeline will be made of. If you provide pipelines among the list of nodes, those pipelines will be expanded and all their nodes will become part of this new pipeline.
- **`inputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of input names to be exposed as connection points to other pipelines upstream. This is optional; if not provided, the pipeline inputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed input names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current input names will be mapped to new names. Must only refer to the pipeline's free inputs.
- **`outputs`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of names to be exposed as connection points to other pipelines downstream. This is optional; if not provided, the pipeline outputs are automatically inferred from the pipeline structure. When str or set[str] is provided, the listed output names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current output names will be mapped to new names. Can refer to both the pipeline's free outputs, as well as intermediate results that need to be exposed.
- **`parameters`** (`str | set[str] | dict[str, str] | None`, default: `None` ) – A name or collection of parameters to namespace. When str or set[str] are provided, the listed parameter names will stay the same as they are named in the provided pipeline. When dict[str, str] is provided, current parameter names will be mapped to new names. The parameters can be specified without the params: prefix.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to all the pipeline nodes.
- **`namespace`** (`str | None`, default: `None` ) – A prefix to give to all dataset names, except those explicitly named with the inputs/outputs arguments, and parameter references (params: and parameters).
- **`prefix_datasets_with_namespace`** (`bool`, default: `True` ) – A flag to specify if the inputs, outputs, and parameters of the nodes should be prefixed with the namespace. It is set to True by default. It is useful to turn off when namespacing is used for grouping nodes for deployment purposes.

Raises:

- `ValueError` – When an empty list of nodes is provided, or when not all nodes have unique names.
- `CircularDependencyError` – When visiting all the nodes is not possible due to the existence of a circular dependency.
- `OutputNotUniqueError` – When multiple Node instances produce the same output.
- `ConfirmNotUniqueError` – When multiple Node instances attempt to confirm the same dataset.
- `PipelineError` – When inputs, outputs or parameters are incorrectly specified, or they do not exist on the original pipeline.

Example:

```
from kedro.pipeline import Pipeline
from kedro.pipeline import node

# In the following scenario first_ds and second_ds
# are datasets provided by io. Pipeline will pass these
# datasets to first_node function and provides the result
# to the second_node as input.


def first_node(first_ds, second_ds):
    return dict(third_ds=first_ds + second_ds)


def second_node(third_ds):
    return third_ds


pipeline = Pipeline(
    [
        node(first_node, ["first_ds", "second_ds"], ["third_ds"]),
        node(second_node, dict(third_ds="third_ds"), "fourth_ds"),
    ]
)

pipeline.describe()
```

Source code in `kedro/pipeline/pipeline.py`

````
def __init__(  # noqa: PLR0913
    self,
    nodes: Iterable[Node | Pipeline] | Pipeline,
    *,
    inputs: str | set[str] | dict[str, str] | None = None,
    outputs: str | set[str] | dict[str, str] | None = None,
    parameters: str | set[str] | dict[str, str] | None = None,
    tags: str | Iterable[str] | None = None,
    namespace: str | None = None,
    prefix_datasets_with_namespace: bool = True,
):
    """Initialise ``Pipeline`` with a list of ``Node`` instances.

    Args:
        nodes: The iterable of nodes the ``Pipeline`` will be made of. If you
            provide pipelines among the list of nodes, those pipelines will
            be expanded and all their nodes will become part of this
            new pipeline.
        inputs: A name or collection of input names to be exposed as connection points
            to other pipelines upstream. This is optional; if not provided, the
            pipeline inputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed input names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current input names will be
            mapped to new names.
            Must only refer to the pipeline's free inputs.
        outputs: A name or collection of names to be exposed as connection points
            to other pipelines downstream. This is optional; if not provided, the
            pipeline outputs are automatically inferred from the pipeline structure.
            When str or set[str] is provided, the listed output names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current output names will be
            mapped to new names.
            Can refer to both the pipeline's free outputs, as well as
            intermediate results that need to be exposed.
        parameters: A name or collection of parameters to namespace.
            When str or set[str] are provided, the listed parameter names will stay
            the same as they are named in the provided pipeline.
            When dict[str, str] is provided, current parameter names will be
            mapped to new names.
            The parameters can be specified without the `params:` prefix.
        tags: Optional set of tags to be applied to all the pipeline nodes.
        namespace: A prefix to give to all dataset names,
            except those explicitly named with the `inputs`/`outputs`
            arguments, and parameter references (`params:` and `parameters`).
        prefix_datasets_with_namespace: A flag to specify if the inputs, outputs, and parameters of the nodes
            should be prefixed with the namespace. It is set to True by default. It is
            useful to turn off when namespacing is used for grouping nodes for deployment purposes.

    Raises:
        ValueError:
            When an empty list of nodes is provided, or when not all
            nodes have unique names.
        CircularDependencyError:
            When visiting all the nodes is not
            possible due to the existence of a circular dependency.
        OutputNotUniqueError:
            When multiple ``Node`` instances produce the same output.
        ConfirmNotUniqueError:
            When multiple ``Node`` instances attempt to confirm the same
            dataset.
        PipelineError: When inputs, outputs or parameters are incorrectly
            specified, or they do not exist on the original pipeline.
    Example:
    ``` python
    from kedro.pipeline import Pipeline
    from kedro.pipeline import node

    # In the following scenario first_ds and second_ds
    # are datasets provided by io. Pipeline will pass these
    # datasets to first_node function and provides the result
    # to the second_node as input.


    def first_node(first_ds, second_ds):
        return dict(third_ds=first_ds + second_ds)


    def second_node(third_ds):
        return third_ds


    pipeline = Pipeline(
        [
            node(first_node, ["first_ds", "second_ds"], ["third_ds"]),
            node(second_node, dict(third_ds="third_ds"), "fourth_ds"),
        ]
    )

    pipeline.describe()
    ```
    """
    if isinstance(nodes, Pipeline):
        nodes = nodes.nodes

    if any([inputs, outputs, parameters, namespace]):
        nodes = self._map_nodes(
            nodes=nodes,
            inputs=inputs,
            outputs=outputs,
            parameters=parameters,
            tags=tags,
            namespace=namespace,
            prefix_datasets_with_namespace=prefix_datasets_with_namespace,
        )

    if nodes is None:
        raise ValueError(
            "'nodes' argument of 'Pipeline' is None. It must be an "
            "iterable of nodes and/or pipelines instead."
        )
    nodes_list = list(nodes)  # in case it's a generator
    _validate_duplicate_nodes(nodes_list)

    nodes_chain = list(
        chain.from_iterable(
            [[n] if isinstance(n, Node) else n.nodes for n in nodes_list]
        )
    )
    _validate_transcoded_inputs_outputs(nodes_chain)
    _tags = set(_to_list(tags))

    if _tags:
        tagged_nodes = [n.tag(_tags) for n in nodes_chain]
    else:
        tagged_nodes = nodes_chain

    self._nodes_by_name = {node.name: node for node in tagged_nodes}
    _validate_unique_outputs(tagged_nodes)
    _validate_unique_confirms(tagged_nodes)

    # input -> nodes with input
    self._nodes_by_input: dict[str, set[Node]] = defaultdict(set)
    for node in tagged_nodes:
        for input_ in node.inputs:
            self._nodes_by_input[_strip_transcoding(input_)].add(node)

    # output -> node with output
    self._nodes_by_output: dict[str, Node] = {}
    for node in tagged_nodes:
        for output in node.outputs:
            self._nodes_by_output[_strip_transcoding(output)] = node

    self._nodes = tagged_nodes
    self._toposorter = TopologicalSorter(self.node_dependencies)

    # test for circular dependencies without executing the toposort for efficiency
    try:
        self._toposorter.prepare()
    except CycleError as exc:
        loop = list(set(exc.args[1]))
        message = f"Circular dependencies exist among the following {len(loop)} item(s): {loop}"
        raise CircularDependencyError(message) from exc

    self._toposorted_nodes: list[Node] = []
    self._toposorted_groups: list[list[Node]] = []
    if any(n.namespace for n in self._nodes):
        self._validate_namespaces()
````

#### grouped_nodes

```
grouped_nodes
```

Return a list of the pipeline nodes in topologically ordered groups, i.e. if node A needs to be run before node B, it will appear in an earlier group.

Returns:

- `list[list[Node]]` – The pipeline nodes in topologically ordered groups.

#### node_dependencies

```
node_dependencies
```

All dependencies of nodes where the first Node has a direct dependency on the second Node.

Returns:

- `dict[Node, set[Node]]` – Dictionary where keys are nodes and values are sets made up of
- `dict[Node, set[Node]]` – their parent nodes. Independent nodes have this as empty sets.

#### nodes

```
nodes
```

Return a list of the pipeline nodes in topological order, i.e. if node A needs to be run before node B, it will appear earlier in the list.

Returns:

- `list[Node]` – The list of all pipeline nodes in topological order.

#### __repr__

```
__repr__()
```

Pipeline ([node1, ..., node10 ...], name='pipeline_name')

Source code in `kedro/pipeline/pipeline.py`

```
def __repr__(self) -> str:  # pragma: no cover
    """Pipeline ([node1, ..., node10 ...], name='pipeline_name')"""
    max_nodes_to_display = 10

    nodes_reprs = [repr(node) for node in self.nodes[:max_nodes_to_display]]
    if len(self.nodes) > max_nodes_to_display:
        nodes_reprs.append("...")
    sep = ",\n"
    nodes_reprs_str = f"[\n{sep.join(nodes_reprs)}\n]" if nodes_reprs else "[]"
    constructor_repr = f"({nodes_reprs_str})"
    return f"{self.__class__.__name__}{constructor_repr}"
```

#### all_inputs

```
all_inputs()
```

All inputs for all nodes in the pipeline.

Returns:

- `set[str]` – All node input names as a Set.

Source code in `kedro/pipeline/pipeline.py`

```
def all_inputs(self) -> set[str]:
    """All inputs for all nodes in the pipeline.

    Returns:
        All node input names as a Set.

    """
    return set.union(set(), *(node.inputs for node in self._nodes))
```

#### all_outputs

```
all_outputs()
```

All outputs of all nodes in the pipeline.

Returns:

- `set[str]` – All node outputs.

Source code in `kedro/pipeline/pipeline.py`

```
def all_outputs(self) -> set[str]:
    """All outputs of all nodes in the pipeline.

    Returns:
        All node outputs.

    """
    return set.union(set(), *(node.outputs for node in self._nodes))
```

#### datasets

```
datasets()
```

The names of all datasets used by the `Pipeline`, including inputs and outputs.

Returns:

- `set[str]` – The set of all pipeline datasets.

Source code in `kedro/pipeline/pipeline.py`

```
def datasets(self) -> set[str]:
    """The names of all datasets used by the ``Pipeline``,
    including inputs and outputs.

    Returns:
        The set of all pipeline datasets.

    """
    return self.all_outputs() | self.all_inputs()
```

#### describe

```
describe(names_only=True)
```

Obtain the order of execution and expected free input variables in a loggable pre-formatted string. The order of nodes matches the order of execution given by the topological sort.

Parameters:

- **`names_only`** (`bool`, default: `True` ) – The flag to describe names_only pipeline with just node names.

Example:

```
pipeline = Pipeline([...])

logger = logging.getLogger(__name__)

logger.info(pipeline.describe())
```

After invocation the following will be printed as an info level log statement: ::

```
#### Pipeline execution order ####
Inputs: C, D

func1([C]) -> [A]
func2([D]) -> [B]
func3([A, D]) -> [E]

Outputs: B, E
##################################
```

Returns:

- `str` – The pipeline description as a formatted string.

Source code in `kedro/pipeline/pipeline.py`

````
def describe(self, names_only: bool = True) -> str:
    """Obtain the order of execution and expected free input variables in
    a loggable pre-formatted string. The order of nodes matches the order
    of execution given by the topological sort.

    Args:
        names_only: The flag to describe names_only pipeline with just
            node names.

    Example:
    ``` python
    pipeline = Pipeline([...])

    logger = logging.getLogger(__name__)

    logger.info(pipeline.describe())
    ```

    After invocation the following will be printed as an info level log
    statement:
    ::

        #### Pipeline execution order ####
        Inputs: C, D

        func1([C]) -> [A]
        func2([D]) -> [B]
        func3([A, D]) -> [E]

        Outputs: B, E
        ##################################

    Returns:
        The pipeline description as a formatted string.

    """

    def set_to_string(set_of_strings: set[str]) -> str:
        """Convert set to a string but return 'None' in case of an empty
        set.
        """
        return ", ".join(sorted(set_of_strings)) if set_of_strings else "None"

    nodes_as_string = "\n".join(
        node.name if names_only else str(node) for node in self.nodes
    )

    str_representation = (
        "#### Pipeline execution order ####\n"
        "Inputs: {0}\n\n"
        "{1}\n\n"
        "Outputs: {2}\n"
        "##################################"
    )

    return str_representation.format(
        set_to_string(self.inputs()), nodes_as_string, set_to_string(self.outputs())
    )
````

#### filter

```
filter(tags=None, from_nodes=None, to_nodes=None, node_names=None, from_inputs=None, to_outputs=None, node_namespaces=None)
```

Creates a new `Pipeline` object with the nodes that meet all of the specified filtering conditions.

The new pipeline object is the intersection of pipelines that meet each filtering condition. This is distinct from chaining multiple filters together.

Parameters:

- **`tags`** (`Iterable[str] | None`, default: `None` ) – A list of node tags which should be used to lookup the nodes of the new Pipeline.
- **`from_nodes`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be used as a starting point of the new Pipeline.
- **`to_nodes`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be used as an end point of the new Pipeline.
- **`node_names`** (`Iterable[str] | None`, default: `None` ) – A list of node names which should be selected for the new Pipeline.
- **`from_inputs`** (`Iterable[str] | None`, default: `None` ) – A list of inputs which should be used as a starting point of the new Pipeline
- **`to_outputs`** (`Iterable[str] | None`, default: `None` ) – A list of outputs which should be the final outputs of the new Pipeline.
- **`node_namespaces`** (`Iterable[str] | None`, default: `None` ) – A list of node namespaces which should be used to select nodes in the new Pipeline.

Returns:

- `Pipeline` – A new Pipeline object with nodes that meet all of the specified filtering conditions.

Raises:

- `ValueError` – The filtered Pipeline has no nodes.

Example:

```
pipeline = Pipeline(
    [
        node(func, "A", "B", name="node1"),
        node(func, "B", "C", name="node2"),
        node(func, "C", "D", name="node3"),
    ]
)
pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
# Gives a new pipeline object containing node1 and node3.
```

Source code in `kedro/pipeline/pipeline.py`

````
def filter(  # noqa: PLR0913
    self,
    tags: Iterable[str] | None = None,
    from_nodes: Iterable[str] | None = None,
    to_nodes: Iterable[str] | None = None,
    node_names: Iterable[str] | None = None,
    from_inputs: Iterable[str] | None = None,
    to_outputs: Iterable[str] | None = None,
    node_namespaces: Iterable[str] | None = None,
) -> Pipeline:
    """Creates a new ``Pipeline`` object with the nodes that meet all of the
    specified filtering conditions.

    The new pipeline object is the intersection of pipelines that meet each
    filtering condition. This is distinct from chaining multiple filters together.

    Args:
        tags: A list of node tags which should be used to lookup
            the nodes of the new ``Pipeline``.
        from_nodes: A list of node names which should be used as a
            starting point of the new ``Pipeline``.
        to_nodes:  A list of node names which should be used as an
            end point of the new ``Pipeline``.
        node_names: A list of node names which should be selected for the
            new ``Pipeline``.
        from_inputs: A list of inputs which should be used as a starting point
            of the new ``Pipeline``
        to_outputs: A list of outputs which should be the final outputs of
            the new ``Pipeline``.
        node_namespaces: A list of node namespaces which should be used to select
            nodes in the new ``Pipeline``.

    Returns:
        A new ``Pipeline`` object with nodes that meet all of the specified
            filtering conditions.

    Raises:
        ValueError: The filtered ``Pipeline`` has no nodes.

    Example:
    ``` python
    pipeline = Pipeline(
        [
            node(func, "A", "B", name="node1"),
            node(func, "B", "C", name="node2"),
            node(func, "C", "D", name="node3"),
        ]
    )
    pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
    # Gives a new pipeline object containing node1 and node3.
    ```
    """

    filter_methods = {
        self.only_nodes_with_tags: tags,
        self.from_nodes: from_nodes,
        self.to_nodes: to_nodes,
        self.only_nodes: node_names,
        self.from_inputs: from_inputs,
        self.to_outputs: to_outputs,
        self.only_nodes_with_namespaces: [node_namespaces]
        if node_namespaces
        else None,
    }

    subset_pipelines = {
        filter_method(*filter_args)  # type: ignore
        for filter_method, filter_args in filter_methods.items()
        if filter_args
    }

    # Intersect all the pipelines subsets. We apply each filter to the original
    # pipeline object (self) rather than incrementally chaining filter methods
    # together. Hence, the order of filtering does not affect the outcome, and the
    # resultant pipeline is unambiguously defined.
    # If this were not the case then, for example,
    # pipeline.filter(node_names=["node1", "node3"], from_inputs=["A"])
    # would give different outcomes depending on the order of filter methods:
    # only_nodes and then from_inputs would give node1, while only_nodes and then
    # from_inputs would give node1 and node3.
    filtered_pipeline = Pipeline(self._nodes)
    for subset_pipeline in subset_pipelines:
        filtered_pipeline &= subset_pipeline

    if not filtered_pipeline.nodes:
        raise ValueError(
            "Pipeline contains no nodes after applying all provided filters. "
            "Please ensure that at least one pipeline with nodes has been defined."
        )
    return filtered_pipeline
````

#### from_inputs

```
from_inputs(*inputs)
```

Create a new `Pipeline` object with the nodes which depend directly or transitively on the provided inputs. If provided a name, but no format, for a transcoded input, it includes all the nodes that use inputs with that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*inputs`** (`str`, default: `()` ) – A list of inputs which should be used as a starting point of the new Pipeline

Raises:

- `ValueError` – Raised when any of the given inputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the current one such that only nodes depending directly or transitively on the provided inputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def from_inputs(self, *inputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly or transitively on the provided inputs.
    If provided a name, but no format, for a transcoded input, it
    includes all the nodes that use inputs with that name, otherwise it
    matches to the fully-qualified name only (i.e. name@format).

    Args:
        *inputs: A list of inputs which should be used as a starting point
            of the new ``Pipeline``

    Raises:
        ValueError: Raised when any of the given inputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes depending
            directly or transitively on the provided inputs are being
            copied.

    """
    starting = set(inputs)
    result: set[Node] = set()
    next_nodes = self._get_nodes_with_inputs_transcode_compatible(starting)

    while next_nodes:
        result |= next_nodes
        outputs = set(chain.from_iterable(node.outputs for node in next_nodes))
        starting = outputs

        next_nodes = set(
            chain.from_iterable(
                self._nodes_by_input[_strip_transcoding(input_)]
                for input_ in starting
            )
        )

    return Pipeline(result)
```

#### from_nodes

```
from_nodes(*node_names)
```

Create a new `Pipeline` object with the nodes which depend directly or transitively on the provided nodes.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – A list of node_names which should be used as a starting point of the new Pipeline.

Raises: ValueError: Raised when any of the given names do not exist in the `Pipeline` object. Returns: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes depending directly or transitively on the provided nodes are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def from_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly or transitively on the provided nodes.

    Args:
        *node_names: A list of node_names which should be used as a
            starting point of the new ``Pipeline``.
    Raises:
        ValueError: Raised when any of the given names do not exist in the
            ``Pipeline`` object.
    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of
            the current one such that only nodes depending directly or
            transitively on the provided nodes are being copied.

    """

    res = self.only_nodes(*node_names)
    res += self.from_inputs(*map(_strip_transcoding, res.all_outputs()))
    return res
```

#### group_nodes_by

```
group_nodes_by(group_by='namespace')
```

Return a list of grouped nodes based on the specified strategy.

Parameters:

- **`group_by`** (`str | None`, default: `'namespace'` ) – Strategy for grouping. Supported values:
  - "namespace": Groups nodes by their top-level namespace.
  - None or "none": No grouping, each node is its own group.

Returns:

- `list[GroupedNodes]` – A list of GroupedNodes instances.

Source code in `kedro/pipeline/pipeline.py`

```
def group_nodes_by(
    self,
    group_by: str | None = "namespace",
) -> list[GroupedNodes]:
    """Return a list of grouped nodes based on the specified strategy.

    Args:
        group_by: Strategy for grouping. Supported values:
            - "namespace": Groups nodes by their top-level namespace.
            - None or "none": No grouping, each node is its own group.

    Returns:
        A list of GroupedNodes instances.
    """
    if group_by is None or group_by.lower() == "none":
        return self._group_by_none()
    if group_by.lower() == "namespace":
        return self._group_by_namespace()
    raise ValueError(f"Unsupported group_by strategy: {group_by}")
```

#### inputs

```
inputs()
```

The names of free inputs that must be provided at runtime so that the pipeline is runnable. Does not include intermediate inputs which are produced and consumed by the inner pipeline nodes. Resolves transcoded names where necessary.

Returns:

- `set[str]` – The set of free input names needed by the pipeline.

Source code in `kedro/pipeline/pipeline.py`

```
def inputs(self) -> set[str]:
    """The names of free inputs that must be provided at runtime so that
    the pipeline is runnable. Does not include intermediate inputs which
    are produced and consumed by the inner pipeline nodes. Resolves
    transcoded names where necessary.

    Returns:
        The set of free input names needed by the pipeline.

    """
    return self._remove_intermediates(self.all_inputs())
```

#### only_nodes

```
only_nodes(*node_names)
```

Create a new `Pipeline` which will contain only the specified nodes by name.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – One or more node names. The returned Pipeline will only contain these nodes.

Raises:

- `ValueError` – When some invalid node name is given.

Returns:

- `Pipeline` – A new Pipeline, containing only nodes.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` which will contain only the specified
    nodes by name.

    Args:
        *node_names: One or more node names. The returned ``Pipeline``
            will only contain these nodes.

    Raises:
        ValueError: When some invalid node name is given.

    Returns:
        A new ``Pipeline``, containing only ``nodes``.

    """
    unregistered_nodes = set(node_names) - set(self._nodes_by_name.keys())
    if unregistered_nodes:
        # check if unregistered nodes are available under namespace
        namespaces = []
        for unregistered_node in unregistered_nodes:
            namespaces.extend(
                [
                    node_name
                    for node_name in self._nodes_by_name.keys()
                    if node_name.endswith(f".{unregistered_node}")
                ]
            )
        if namespaces:
            raise ValueError(
                f"Pipeline does not contain nodes named {list(unregistered_nodes)}. "
                f"Did you mean: {namespaces}?"
            )
        raise ValueError(
            f"Pipeline does not contain nodes named {list(unregistered_nodes)}."
        )

    nodes = [self._nodes_by_name[name] for name in node_names]
    return Pipeline(nodes)
```

#### only_nodes_with_inputs

```
only_nodes_with_inputs(*inputs)
```

Create a new `Pipeline` object with the nodes which depend directly on the provided inputs. If provided a name, but no format, for a transcoded input, it includes all the nodes that use inputs with that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*inputs`** (`str`, default: `()` ) – A list of inputs which should be used as a starting point of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given inputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the current one such that only nodes depending directly on the provided inputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_inputs(self, *inputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which depend
    directly on the provided inputs.
    If provided a name, but no format, for a transcoded input, it
    includes all the nodes that use inputs with that name, otherwise it
    matches to the fully-qualified name only (i.e. name@format).

    Args:
        *inputs: A list of inputs which should be used as a starting
            point of the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given inputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes depending
            directly on the provided inputs are being copied.

    """
    starting = set(inputs)
    nodes = self._get_nodes_with_inputs_transcode_compatible(starting)

    return Pipeline(nodes)
```

#### only_nodes_with_namespaces

```
only_nodes_with_namespaces(node_namespaces)
```

Creates a new `Pipeline` containing only nodes with the specified namespaces.

Parameters:

- **`node_namespaces`** (`list[str]`) – A list of node namespaces.

Raises:

- `ValueError` – When pipeline contains no nodes with the specified namespaces.

Returns:

- `Pipeline` – A new Pipeline containing nodes with the specified namespaces.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_namespaces(self, node_namespaces: list[str]) -> Pipeline:
    """Creates a new ``Pipeline`` containing only nodes with the specified
    namespaces.

    Args:
        node_namespaces: A list of node namespaces.

    Raises:
        ValueError: When pipeline contains no nodes with the specified namespaces.

    Returns:
        A new ``Pipeline`` containing nodes with the specified namespaces.
    """
    nodes = []
    unmatched_namespaces = []  # Track namespaces that don't match any nodes

    for node_namespace in node_namespaces:
        matching_nodes = []
        for n in self._nodes:
            if n.namespace and (
                n.namespace == node_namespace
                or n.namespace.startswith(f"{node_namespace}.")
            ):
                matching_nodes.append(n)

        if not matching_nodes:
            unmatched_namespaces.append(node_namespace)
        nodes.extend(matching_nodes)

    if unmatched_namespaces:
        raise ValueError(
            f"Pipeline does not contain nodes with the following namespaces: {unmatched_namespaces}"
        )

    return Pipeline(nodes)
```

#### only_nodes_with_outputs

```
only_nodes_with_outputs(*outputs)
```

Create a new `Pipeline` object with the nodes which are directly required to produce the provided outputs. If provided a name, but no format, for a transcoded dataset, it includes all the nodes that output to that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*outputs`** (`str`, default: `()` ) – A list of outputs which should be the final outputs of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given outputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the
- `Pipeline` – current one such that only nodes which are directly required to
- `Pipeline` – produce the provided outputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_outputs(self, *outputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which are directly
    required to produce the provided outputs.
    If provided a name, but no format, for a transcoded dataset, it
    includes all the nodes that output to that name, otherwise it matches
    to the fully-qualified name only (i.e. name@format).

    Args:
        *outputs: A list of outputs which should be the final outputs
            of the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given outputs do not exist in the
            ``Pipeline`` object.

    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
        current one such that only nodes which are directly required to
        produce the provided outputs are being copied.
    """
    starting = set(outputs)
    nodes = self._get_nodes_with_outputs_transcode_compatible(starting)

    return Pipeline(nodes)
```

#### only_nodes_with_tags

```
only_nodes_with_tags(*tags)
```

Creates a new `Pipeline` object with the nodes which contain *any* of the provided tags. The resulting `Pipeline` is empty if no tags are provided.

Parameters:

- **`*tags`** (`str`, default: `()` ) – A list of node tags which should be used to lookup the nodes of the new Pipeline.

Returns: Pipeline: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes containing *any* of the tags provided are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def only_nodes_with_tags(self, *tags: str) -> Pipeline:
    """Creates a new ``Pipeline`` object with the nodes which contain *any*
    of the provided tags. The resulting ``Pipeline`` is empty if no tags
    are provided.

    Args:
        *tags: A list of node tags which should be used to lookup
            the nodes of the new ``Pipeline``.
    Returns:
        Pipeline: A new ``Pipeline`` object, containing a subset of the
            nodes of the current one such that only nodes containing *any*
            of the tags provided are being copied.
    """
    unique_tags = set(tags)
    nodes = [node for node in self._nodes if unique_tags & node.tags]
    return Pipeline(nodes)
```

#### outputs

```
outputs()
```

The names of outputs produced when the whole pipeline is run. Does not include intermediate outputs that are consumed by other pipeline nodes. Resolves transcoded names where necessary.

Returns:

- `set[str]` – The set of final pipeline outputs.

Source code in `kedro/pipeline/pipeline.py`

```
def outputs(self) -> set[str]:
    """The names of outputs produced when the whole pipeline is run.
    Does not include intermediate outputs that are consumed by
    other pipeline nodes. Resolves transcoded names where necessary.

    Returns:
        The set of final pipeline outputs.

    """
    return self._remove_intermediates(self.all_outputs())
```

#### tag

```
tag(tags)
```

Tags all the nodes in the pipeline.

Parameters:

- **`tags`** (`str | Iterable[str]`) – The tags to be added to the nodes.

Returns:

- `Pipeline` – New Pipeline object with nodes tagged.

Source code in `kedro/pipeline/pipeline.py`

```
def tag(self, tags: str | Iterable[str]) -> Pipeline:
    """Tags all the nodes in the pipeline.

    Args:
        tags: The tags to be added to the nodes.

    Returns:
        New ``Pipeline`` object with nodes tagged.
    """
    nodes = [n.tag(tags) for n in self._nodes]
    return Pipeline(nodes)
```

#### to_json

```
to_json()
```

Return a json representation of the pipeline.

Source code in `kedro/pipeline/pipeline.py`

```
def to_json(self) -> str:
    """Return a json representation of the pipeline."""
    transformed = [
        {
            "name": n.name,
            "inputs": list(n.inputs),
            "outputs": list(n.outputs),
            "tags": list(n.tags),
        }
        for n in self._nodes
    ]
    pipeline_versioned = {
        "kedro_version": kedro.__version__,
        "pipeline": transformed,
    }

    return json.dumps(pipeline_versioned)
```

#### to_nodes

```
to_nodes(*node_names)
```

Create a new `Pipeline` object with the nodes required directly or transitively by the provided nodes.

Parameters:

- **`*node_names`** (`str`, default: `()` ) – A list of node_names which should be used as an end point of the new Pipeline.

Raises: ValueError: Raised when any of the given names do not exist in the `Pipeline` object. Returns: A new `Pipeline` object, containing a subset of the nodes of the current one such that only nodes required directly or transitively by the provided nodes are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def to_nodes(self, *node_names: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes required directly
    or transitively by the provided nodes.

    Args:
        *node_names: A list of node_names which should be used as an
            end point of the new ``Pipeline``.
    Raises:
        ValueError: Raised when any of the given names do not exist in the
            ``Pipeline`` object.
    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
            current one such that only nodes required directly or
            transitively by the provided nodes are being copied.

    """

    res = self.only_nodes(*node_names)
    res += self.to_outputs(*map(_strip_transcoding, res.all_inputs()))
    return res
```

#### to_outputs

```
to_outputs(*outputs)
```

Create a new `Pipeline` object with the nodes which are directly or transitively required to produce the provided outputs. If provided a name, but no format, for a transcoded dataset, it includes all the nodes that output to that name, otherwise it matches to the fully-qualified name only (i.e. name@format).

Parameters:

- **`*outputs`** (`str`, default: `()` ) – A list of outputs which should be the final outputs of the new Pipeline.

Raises:

- `ValueError` – Raised when any of the given outputs do not exist in the Pipeline object.

Returns:

- `Pipeline` – A new Pipeline object, containing a subset of the nodes of the
- `Pipeline` – current one such that only nodes which are directly or transitively
- `Pipeline` – required to produce the provided outputs are being copied.

Source code in `kedro/pipeline/pipeline.py`

```
def to_outputs(self, *outputs: str) -> Pipeline:
    """Create a new ``Pipeline`` object with the nodes which are directly
    or transitively required to produce the provided outputs.
    If provided a name, but no format, for a transcoded dataset, it
    includes all the nodes that output to that name, otherwise it matches
    to the fully-qualified name only (i.e. name@format).

    Args:
        *outputs: A list of outputs which should be the final outputs of
            the new ``Pipeline``.

    Raises:
        ValueError: Raised when any of the given outputs do not exist in the
            ``Pipeline`` object.


    Returns:
        A new ``Pipeline`` object, containing a subset of the nodes of the
        current one such that only nodes which are directly or transitively
        required to produce the provided outputs are being copied.

    """
    starting = set(outputs)
    result: set[Node] = set()
    next_nodes = self._get_nodes_with_outputs_transcode_compatible(starting)

    while next_nodes:
        result |= next_nodes
        inputs = set(chain.from_iterable(node.inputs for node in next_nodes))
        starting = inputs

        next_nodes = {
            self._nodes_by_output[_strip_transcoding(output)]
            for output in starting
            if _strip_transcoding(output) in self._nodes_by_output
        }

    return Pipeline(result)
```

### SequentialRunner

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

### SharedMemoryDataCatalog

```
SharedMemoryDataCatalog(datasets=None, config_resolver=None, load_versions=None, save_version=None)
```

Bases: `DataCatalog`

A specialized `DataCatalog` for managing datasets in a shared memory context.

The `SharedMemoryDataCatalog` extends the base `DataCatalog` to support multiprocessing by ensuring that datasets are serializable and synchronized across threads or processes. It provides additional functionality for managing shared memory datasets, such as setting a multiprocessing manager and validating dataset compatibility with multiprocessing.

Attributes:

- **`default_runtime_patterns`** (`ClassVar`) – A dictionary defining the default runtime pattern for datasets of type kedro.io.SharedMemoryDataset.

Example:

```
    from multiprocessing.managers import SyncManager
    from kedro.io import MemoryDataset
    from kedro.io.data_catalog import SharedMemoryDataCatalog

    # Create a shared memory catalog
    catalog = SharedMemoryDataCatalog(
        datasets={"shared_data": MemoryDataset(data=[1, 2, 3])}
    )

    # Set a multiprocessing manager
    manager = SyncManager()
    manager.start()
    catalog.set_manager_datasets(manager)

    # Validate the catalog for multiprocessing compatibility
    catalog.validate_catalog()
```

Source code in `kedro/io/data_catalog.py`

````
def __init__(
    self,
    datasets: dict[str, AbstractDataset] | None = None,
    config_resolver: CatalogConfigResolver | None = None,
    load_versions: dict[str, str] | None = None,
    save_version: str | None = None,
) -> None:
    """Initializes a ``DataCatalog`` to manage datasets with loading, saving, and versioning capabilities.

    This catalog combines datasets passed directly via the `datasets` argument and dynamic datasets
    resolved from config (e.g., from YAML).

    If a dataset name is present in both `datasets` and the resolved config, the dataset from `datasets`
    takes precedence. A warning is logged, and the config-defined dataset is skipped and removed from
    the internal config.

    Args:
        datasets: A dictionary of dataset names and dataset instances.
        config_resolver: An instance of CatalogConfigResolver to resolve dataset factory patterns and configurations.
        load_versions: A mapping between dataset names and versions
            to load. Has no effect on datasets without enabled versioning.
        save_version: Version string to be used for ``save`` operations
            by all datasets with enabled versioning. It must: a) be a
            case-insensitive string that conforms with operating system
            filename limitations, b) always return the latest version when
            sorted in lexicographical order.

    Example:
    ``` python

        from kedro.io import DataCatalog, MemoryDataset
        from kedro_datasets.pandas import CSVDataset

        # Define datasets
        datasets = {
            "cars": CSVDataset(filepath="cars.csv"),
            "planes": MemoryDataset(data={"type": "jet", "capacity": 200}),
        }

        # Initialize the catalog
        catalog = DataCatalog(
            datasets=datasets,
            load_versions={"cars": "2023-01-01T00.00.00"},
            save_version="2023-01-02T00.00.00",
        )

        print(catalog)
    ```
    """
    self._config_resolver = config_resolver or CatalogConfigResolver(
        default_runtime_patterns=self.default_runtime_patterns
    )
    self._datasets: dict[str, AbstractDataset] = datasets or {}
    self._lazy_datasets: dict[str, _LazyDataset] = {}
    self._load_versions, self._save_version = self._validate_versions(
        datasets, load_versions or {}, save_version
    )

    self._use_rich_markup = _has_rich_handler()

    for ds_name in list(self._config_resolver.config):
        if ds_name in self._datasets:
            self._logger.warning(
                f"Cannot register dataset '{ds_name}' from config: a dataset with the same name "
                f"was already provided in the `datasets` argument."
            )
            self._config_resolver.config.pop(ds_name)
        else:
            self._add_from_config(ds_name, self._config_resolver.config[ds_name])
````

#### set_manager_datasets

```
set_manager_datasets(manager)
```

Associate a multiprocessing manager with all shared memory datasets in the catalog.

This method iterates through all datasets in the catalog and sets the provided multiprocessing manager for datasets of type `SharedMemoryDataset`. This ensures that these datasets are properly synchronized across threads or processes.

Parameters:

- **`manager`** (`SyncManager`) – A multiprocessing manager to be associated with shared memory datasets.

Example:

```
    from multiprocessing.managers import SyncManager
    from kedro.io.data_catalog import SharedMemoryDataCatalog
    catalog = SharedMemoryDataCatalog(datasets={"shared_data": MemoryDataset(data=[1, 2, 3])})
    manager = SyncManager()
    manager.start()
    catalog.set_manager_datasets(manager)
    print(catalog)
    # {'shared_data': kedro.io.memory_dataset.MemoryDataset(data='<list>')}
```

Source code in `kedro/io/data_catalog.py`

````
def set_manager_datasets(self, manager: SyncManager) -> None:
    """
    Associate a multiprocessing manager with all shared memory datasets in the catalog.

    This method iterates through all datasets in the catalog and sets the provided
    multiprocessing manager for datasets of type `SharedMemoryDataset`. This ensures
    that these datasets are properly synchronized across threads or processes.

    Args:
        manager: A multiprocessing manager to be associated with
            shared memory datasets.

    Example:
    ```python
        from multiprocessing.managers import SyncManager
        from kedro.io.data_catalog import SharedMemoryDataCatalog
        catalog = SharedMemoryDataCatalog(datasets={"shared_data": MemoryDataset(data=[1, 2, 3])})
        manager = SyncManager()
        manager.start()
        catalog.set_manager_datasets(manager)
        print(catalog)
        # {'shared_data': kedro.io.memory_dataset.MemoryDataset(data='<list>')}
    ```
    """
    for _, ds in self._datasets.items():
        if isinstance(ds, SharedMemoryDataset):
            ds.set_manager(manager)
````

#### validate_catalog

```
validate_catalog()
```

Validate the catalog to ensure all datasets are serializable and compatible with multiprocessing.

This method checks that all datasets in the catalog are serializable and do not include non-proxied memory datasets as outputs. Non-serializable datasets or datasets that rely on single-process memory cannot be used in a multiprocessing context. If any such datasets are found, an exception is raised with details.

Raises:

- `AttributeError` – If any datasets are found to be non-serializable or incompatible with multiprocessing.

Example:

```
    from kedro.io.data_catalog import SharedMemoryDataCatalog

    catalog = SharedMemoryDataCatalog(datasets={"shared_data": MemoryDataset(data=[1, 2, 3])})
    try:
        catalog.validate_catalog()
    except AttributeError as e:
        print(f"Validation failed: {e}")
    # No error
```

Source code in `kedro/io/data_catalog.py`

````
def validate_catalog(self) -> None:
    """
    Validate the catalog to ensure all datasets are serializable and compatible with multiprocessing.

    This method checks that all datasets in the catalog are serializable and do not
    include non-proxied memory datasets as outputs. Non-serializable datasets or
    datasets that rely on single-process memory cannot be used in a multiprocessing
    context. If any such datasets are found, an exception is raised with details.

    Raises:
        AttributeError: If any datasets are found to be non-serializable or incompatible
            with multiprocessing.

    Example:
    ```python
        from kedro.io.data_catalog import SharedMemoryDataCatalog

        catalog = SharedMemoryDataCatalog(datasets={"shared_data": MemoryDataset(data=[1, 2, 3])})
        try:
            catalog.validate_catalog()
        except AttributeError as e:
            print(f"Validation failed: {e}")
        # No error
    ```
    """
    unserialisable = []
    for name, dataset in self._datasets.items():
        if getattr(dataset, "_SINGLE_PROCESS", False):  # SKIP_IF_NO_SPARK
            unserialisable.append(name)
            continue
        try:
            ForkingPickler.dumps(dataset)
        except (AttributeError, PicklingError):
            unserialisable.append(name)

    if unserialisable:
        raise AttributeError(
            f"The following datasets cannot be used with multiprocessing: "
            f"{sorted(unserialisable)}\nIn order to utilize multiprocessing you "
            f"need to make sure all datasets are serialisable, i.e. datasets "
            f"should not make use of lambda functions, nested functions, closures "
            f"etc.\nIf you are using custom decorators ensure they are correctly "
            f"decorated using functools.wraps()."
        )
````

### \_create_hook_manager

```
_create_hook_manager()
```

Create a new PluginManager instance and register Kedro's hook specs.

Source code in `kedro/framework/hooks/manager.py`

```
def _create_hook_manager() -> PluginManager:
    """Create a new PluginManager instance and register Kedro's hook specs."""
    manager = PluginManager(HOOK_NAMESPACE)
    manager.trace.root.setwriter(
        logger.debug if logger.getEffectiveLevel() == logging.DEBUG else None
    )
    manager.enable_tracing()
    manager.add_hookspecs(NodeSpecs)
    manager.add_hookspecs(PipelineSpecs)
    manager.add_hookspecs(DataCatalogSpecs)
    manager.add_hookspecs(DatasetSpecs)
    manager.add_hookspecs(KedroContextSpecs)
    return manager
```

### \_describe_git

```
_describe_git(project_path)
```

Source code in `kedro/framework/session/session.py`

```
def _describe_git(project_path: Path) -> dict[str, dict[str, Any]]:
    path = str(project_path)
    try:
        res = subprocess.check_output(  # noqa: S603
            ["git", "rev-parse", "--short", "HEAD"],  # noqa: S607
            cwd=path,
            stderr=subprocess.STDOUT,
        )
        git_data: dict[str, Any] = {"commit_sha": res.decode().strip()}
        git_status_res = subprocess.check_output(  # noqa: S603
            ["git", "status", "--short"],  # noqa: S607
            cwd=path,
            stderr=subprocess.STDOUT,
        )
        git_data["dirty"] = bool(git_status_res.decode().strip())

    # `subprocess.check_output()` raises `NotADirectoryError` on Windows
    except Exception:
        logger = logging.getLogger(__name__)
        logger.debug("Unable to git describe %s", path)
        logger.debug(traceback.format_exc())
        return {}

    return {"git": git_data}
```

### \_jsonify_cli_context

```
_jsonify_cli_context(ctx)
```

Source code in `kedro/framework/session/session.py`

```
def _jsonify_cli_context(ctx: click.core.Context) -> dict[str, Any]:
    return {
        "args": ctx.args,
        "params": ctx.params,
        "command_name": ctx.command.name,
        "command_path": " ".join(["kedro"] + sys.argv[1:]),
    }
```

### \_register_hooks

```
_register_hooks(hook_manager, hooks)
```

Register all hooks as specified in `hooks` with the global `hook_manager`.

Parameters:

- **`hook_manager`** (`PluginManager`) – Hook manager instance to register the hooks with.
- **`hooks`** (`Iterable[Any]`) – Hooks that need to be registered.

Source code in `kedro/framework/hooks/manager.py`

```
def _register_hooks(hook_manager: PluginManager, hooks: Iterable[Any]) -> None:
    """Register all hooks as specified in ``hooks`` with the global ``hook_manager``.

    Args:
        hook_manager: Hook manager instance to register the hooks with.
        hooks: Hooks that need to be registered.

    """
    for hooks_collection in hooks:
        # Sometimes users might call hook registration more than once, in which
        # case hooks have already been registered, so we perform a simple check
        # here to avoid an error being raised and break user's workflow.
        if not hook_manager.is_registered(hooks_collection):
            if isclass(hooks_collection):
                raise TypeError(
                    "KedroSession expects hooks to be registered as instances. "
                    "Have you forgotten the `()` when registering a hook class ?"
                )
            hook_manager.register(hooks_collection)
```

### \_register_hooks_entry_points

```
_register_hooks_entry_points(hook_manager, disabled_plugins)
```

Register pluggy hooks from python package entrypoints.

Parameters:

- **`hook_manager`** (`PluginManager`) – Hook manager instance to register the hooks with.
- **`disabled_plugins`** (`Iterable[str]`) – An iterable returning the names of plugins which hooks must not be registered; any already registered hooks will be unregistered.

Source code in `kedro/framework/hooks/manager.py`

```
def _register_hooks_entry_points(
    hook_manager: PluginManager, disabled_plugins: Iterable[str]
) -> None:
    """Register pluggy hooks from python package entrypoints.

    Args:
        hook_manager: Hook manager instance to register the hooks with.
        disabled_plugins: An iterable returning the names of plugins
            which hooks must not be registered; any already registered
            hooks will be unregistered.

    """
    already_registered = hook_manager.get_plugins()
    # Method name is misleading:
    # entry points are standard and don't require setuptools,
    # see https://packaging.python.org/en/latest/specifications/entry-points/
    hook_manager.load_setuptools_entrypoints(_PLUGIN_HOOKS)
    disabled_plugins = set(disabled_plugins)

    # Get list of plugin/distinfo tuples for all registered plugins.
    plugininfo = hook_manager.list_plugin_distinfo()
    plugin_names = set()
    disabled_plugin_names = set()
    for plugin, dist in plugininfo:
        if dist.project_name in disabled_plugins:
            # `unregister()` is used instead of `set_blocked()` because
            # we want to disable hooks for specific plugin based on project
            # name and not `entry_point` name. Also, we log project names with
            # version for which hooks were registered.
            hook_manager.unregister(plugin=plugin)
            disabled_plugin_names.add(f"{dist.project_name}-{dist.version}")
        elif plugin not in already_registered:
            plugin_names.add(f"{dist.project_name}-{dist.version}")

    if disabled_plugin_names:
        logger.debug(
            "Hooks are disabled for plugin(s): %s",
            ", ".join(sorted(disabled_plugin_names)),
        )

    if plugin_names:
        logger.debug(
            "Registered hooks from %d installed plugin(s): %s",
            len(plugin_names),
            ", ".join(sorted(plugin_names)),
        )
```

### find_kedro_project

```
find_kedro_project(current_dir)
```

Given a path, find a Kedro project associated with it.

Can be

- Itself, if a path is a root directory of a Kedro project.
- One of its parents, if self is not a Kedro project but one of the parent path is.
- None, if neither self nor any parent path is a Kedro project.

Returns:

- `Any` – Kedro project associated with a given path,
- `Any` – or None if no relevant Kedro project is found.

Source code in `kedro/utils.py`

```
def find_kedro_project(current_dir: Path) -> Any:  # pragma: no cover
    """Given a path, find a Kedro project associated with it.

    Can be:
        - Itself, if a path is a root directory of a Kedro project.
        - One of its parents, if self is not a Kedro project but one of the parent path is.
        - None, if neither self nor any parent path is a Kedro project.

    Returns:
        Kedro project associated with a given path,
        or None if no relevant Kedro project is found.
    """
    paths_to_check = [current_dir, *list(current_dir.parents)]
    for parent_dir in paths_to_check:
        if is_kedro_project(parent_dir):
            return parent_dir
    return None
```

### generate_timestamp

```
generate_timestamp()
```

Generate the timestamp to be used by versioning.

Returns:

- `str` – String representation of the current timestamp.

Source code in `kedro/io/core.py`

```
def generate_timestamp() -> str:
    """Generate the timestamp to be used by versioning.

    Returns:
        String representation of the current timestamp.

    """
    current_ts = datetime.now(tz=timezone.utc).strftime(VERSION_FORMAT)
    return current_ts[:-4] + current_ts[-1:]  # Don't keep microseconds
```

### validate_settings

```
validate_settings()
```

Eagerly validate that the settings module is importable if it exists. This is desirable to surface any syntax or import errors early. In particular, without eagerly importing the settings module, dynaconf would silence any import error (e.g. missing dependency, missing/mislabelled pipeline), and users would instead get a cryptic error message `` Expected an instance of `ConfigLoader`, got `NoneType` instead ``. More info on the dynaconf issue: https://github.com/dynaconf/dynaconf/issues/460

Source code in `kedro/framework/project/__init__.py`

```
def validate_settings() -> None:
    """Eagerly validate that the settings module is importable if it exists. This is desirable to
    surface any syntax or import errors early. In particular, without eagerly importing
    the settings module, dynaconf would silence any import error (e.g. missing
    dependency, missing/mislabelled pipeline), and users would instead get a cryptic
    error message ``Expected an instance of `ConfigLoader`, got `NoneType` instead``.
    More info on the dynaconf issue: https://github.com/dynaconf/dynaconf/issues/460
    """
    if PACKAGE_NAME is None:
        raise ValueError(
            "Package name not found. Make sure you have configured the project using "
            "'bootstrap_project'. This should happen automatically if you are using "
            "Kedro command line interface."
        )
    # Check if file exists, if it does, validate it.
    if importlib.util.find_spec(f"{PACKAGE_NAME}.settings") is not None:
        importlib.import_module(f"{PACKAGE_NAME}.settings")
    else:
        logger = logging.getLogger(__name__)
        logger.warning("No 'settings.py' found, defaults will be used.")
```

## kedro.framework.session.store

This module implements a dict-like store object used to persist Kedro sessions.

### BaseSessionStore

```
BaseSessionStore(path, session_id)
```

Bases: `UserDict`

`BaseSessionStore` is the base class for all session stores. `BaseSessionStore` is an ephemeral store implementation that doesn't persist the session data.

Source code in `kedro/framework/session/store.py`

```
def __init__(self, path: str, session_id: str):
    self._path = path
    self._session_id = session_id
    super().__init__(self.read())
```

#### read

```
read()
```

Read the data from the session store.

Returns:

- `dict[str, Any]` – A mapping containing the session store data.

Source code in `kedro/framework/session/store.py`

```
def read(self) -> dict[str, Any]:
    """Read the data from the session store.

    Returns:
        A mapping containing the session store data.
    """
    self._logger.debug(
        "'read()' not implemented for '%s'. Assuming empty store.",
        self.__class__.__name__,
    )
    return {}
```

#### save

```
save()
```

Persist the session store

Source code in `kedro/framework/session/store.py`

```
def save(self) -> None:
    """Persist the session store"""
    self._logger.debug(
        "'save()' not implemented for '%s'. Skipping the step.",
        self.__class__.__name__,
    )
```
