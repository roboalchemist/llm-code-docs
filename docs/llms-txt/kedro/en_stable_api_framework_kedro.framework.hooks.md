# Source: https://docs.kedro.org/en/stable/api/framework/kedro.framework.hooks/index.md

## kedro.framework.hooks

`kedro.framework.hooks` provides primitives to use hooks to extend KedroContext's behaviour

| Module                                                            | Description                                                                                               |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| [`kedro.framework.hooks.manager`](#kedro.framework.hooks.manager) | Provides a utility function to retrieve the global `hook_manager` singleton in Kedro's execution process. |
| [`kedro.framework.hooks.markers`](#kedro.framework.hooks.markers) | Provides markers to declare Kedro's hook specs and implementations.                                       |
| [`kedro.framework.hooks.specs`](#kedro.framework.hooks.specs)     | Contains specifications for all callable hooks in Kedro's execution timeline.                             |

## kedro.framework.hooks.manager

This module provides an utility function to retrieve the global hook_manager singleton in a Kedro's execution process.

### HOOK_NAMESPACE

```
HOOK_NAMESPACE = 'kedro'
```

### \_PLUGIN_HOOKS

```
_PLUGIN_HOOKS = 'kedro.hooks'
```

### logger

```
logger = getLogger(__name__)
```

### DataCatalogSpecs

Namespace that defines all specifications for a data catalog's lifecycle hooks.

#### after_catalog_created

```
after_catalog_created(catalog, conf_catalog, conf_creds, parameters, save_version, load_versions)
```

Hooks to be invoked after a data catalog is created. It receives the `catalog` as well as all the arguments for `KedroContext._create_catalog`.

Parameters:

- **`catalog`** (`CatalogProtocol`) – The catalog that was created.
- **`conf_catalog`** (`dict[str, Any]`) – The config from which the catalog was created.
- **`conf_creds`** (`dict[str, Any]`) – The credentials conf from which the catalog was created.
- **`parameters`** (`dict[str, Any]`) – The parameters that are added to the catalog after creation.
- **`save_version`** (`str`) – The save_version used in save operations for all datasets in the catalog.
- **`load_versions`** (`dict[str, str]`) – The load_versions used in load operations for each dataset in the catalog.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_catalog_created(  # noqa: PLR0913
    self,
    catalog: CatalogProtocol,
    conf_catalog: dict[str, Any],
    conf_creds: dict[str, Any],
    parameters: dict[str, Any],
    save_version: str,
    load_versions: dict[str, str],
) -> None:
    """Hooks to be invoked after a data catalog is created.
    It receives the ``catalog`` as well as
    all the arguments for ``KedroContext._create_catalog``.

    Args:
        catalog: The catalog that was created.
        conf_catalog: The config from which the catalog was created.
        conf_creds: The credentials conf from which the catalog was created.
        parameters: The parameters that are added to the catalog after creation.
        save_version: The save_version used in ``save`` operations
            for all datasets in the catalog.
        load_versions: The load_versions used in ``load`` operations
            for each dataset in the catalog.
    """
    pass
```

### DatasetSpecs

Namespace that defines all specifications for a dataset's lifecycle hooks.

#### after_dataset_loaded

```
after_dataset_loaded(dataset_name, data, node)
```

Hook to be invoked after a dataset is loaded from the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset that was loaded from the catalog.
- **`data`** (`Any`) – the actual data that was loaded from the catalog.
- **`node`** (`Node`) – The Node to run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_dataset_loaded(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked after a dataset is loaded from the catalog.

    Args:
        dataset_name: name of the dataset that was loaded from the catalog.
        data: the actual data that was loaded from the catalog.
        node: The ``Node`` to run.
    """
    pass
```

#### after_dataset_saved

```
after_dataset_saved(dataset_name, data, node)
```

Hook to be invoked after a dataset is saved in the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset that was saved to the catalog.
- **`data`** (`Any`) – the actual data that was saved to the catalog.
- **`node`** (`Node`) – The Node that ran.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_dataset_saved(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked after a dataset is saved in the catalog.

    Args:
        dataset_name: name of the dataset that was saved to the catalog.
        data: the actual data that was saved to the catalog.
        node: The ``Node`` that ran.
    """
    pass
```

#### before_dataset_loaded

```
before_dataset_loaded(dataset_name, node)
```

Hook to be invoked before a dataset is loaded from the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset to be loaded from the catalog.
- **`node`** (`Node`) – The Node to run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_dataset_loaded(self, dataset_name: str, node: Node) -> None:
    """Hook to be invoked before a dataset is loaded from the catalog.

    Args:
        dataset_name: name of the dataset to be loaded from the catalog.
        node: The ``Node`` to run.
    """
    pass
```

#### before_dataset_saved

```
before_dataset_saved(dataset_name, data, node)
```

Hook to be invoked before a dataset is saved to the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset to be saved to the catalog.
- **`data`** (`Any`) – the actual data to be saved to the catalog.
- **`node`** (`Node`) – The Node that ran.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_dataset_saved(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked before a dataset is saved to the catalog.

    Args:
        dataset_name: name of the dataset to be saved to the catalog.
        data: the actual data to be saved to the catalog.
        node: The ``Node`` that ran.
    """
    pass
```

### KedroContextSpecs

Namespace that defines all specifications for a Kedro context's lifecycle hooks.

#### after_context_created

```
after_context_created(context)
```

Hooks to be invoked after a `KedroContext` is created. This is the earliest hook triggered within a Kedro run. The `KedroContext` stores useful information such as `credentials`, `config_loader` and `env`.

Parameters:

- **`context`** (`KedroContext`) – The context that was created.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_context_created(
    self,
    context: KedroContext,
) -> None:
    """Hooks to be invoked after a `KedroContext` is created. This is the earliest
    hook triggered within a Kedro run. The `KedroContext` stores useful information
    such as `credentials`, `config_loader` and `env`.

    Args:
        context: The context that was created.
    """
```

### NodeSpecs

Namespace that defines all specifications for a node's lifecycle hooks.

#### after_node_run

```
after_node_run(node, catalog, inputs, outputs, is_async, run_id)
```

Hook to be invoked after a node runs.

Parameters:

- **`node`** (`Node`) – The Node that ran.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`outputs`** (`dict[str, Any]`) – The dictionary of outputs dataset. The keys are dataset names and the values are the actual computed output data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_node_run(  # noqa: PLR0913
    self,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    outputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> None:
    """Hook to be invoked after a node runs.

    Args:
        node: The ``Node`` that ran.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        outputs: The dictionary of outputs dataset.
            The keys are dataset names and the values are the actual computed output data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.
    """
    pass
```

#### before_node_run

```
before_node_run(node, catalog, inputs, is_async, run_id)
```

Hook to be invoked before a node runs.

Parameters:

- **`node`** (`Node`) – The Node to run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Returns:

- `dict[str, Any] | None` – Either None or a dictionary mapping dataset name(s) to new value(s). If returned, this dictionary will be used to update the node inputs, which allows to overwrite the node inputs.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_node_run(
    self,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> dict[str, Any] | None:
    """Hook to be invoked before a node runs.

    Args:
        node: The ``Node`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.

    Returns:
        Either None or a dictionary mapping dataset name(s) to new value(s).
            If returned, this dictionary will be used to update the node inputs,
            which allows to overwrite the node inputs.
    """
    pass
```

#### on_node_error

```
on_node_error(error, node, catalog, inputs, is_async, run_id)
```

Hook to be invoked if a node run throws an uncaught error. The signature of this error hook should match the signature of `before_node_run` along with the error that was raised.

Parameters:

- **`error`** (`Exception`) – The uncaught exception thrown during the node run.
- **`node`** (`Node`) – The Node to run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def on_node_error(  # noqa: PLR0913
    self,
    error: Exception,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> None:
    """Hook to be invoked if a node run throws an uncaught error.
    The signature of this error hook should match the signature of ``before_node_run``
    along with the error that was raised.

    Args:
        error: The uncaught exception thrown during the node run.
        node: The ``Node`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.
    """
    pass
```

### PipelineSpecs

Namespace that defines all specifications for a pipeline's lifecycle hooks.

#### after_pipeline_run

```
after_pipeline_run(run_params, run_result, pipeline, catalog)
```

Hook to be invoked after a pipeline runs.

Parameters:

- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`run_result`** (`dict[str, Any]`) – The output of Pipeline run.
- **`pipeline`** (`Pipeline`) – The Pipeline that was run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_pipeline_run(
    self,
    run_params: dict[str, Any],
    run_result: dict[str, Any],
    pipeline: Pipeline,
    catalog: CatalogProtocol,
) -> None:
    """Hook to be invoked after a pipeline runs.

    Args:
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        run_result: The output of ``Pipeline`` run.
        pipeline: The ``Pipeline`` that was run.
        catalog: An implemented instance of ``CatalogProtocol`` used during the run.
    """
    pass
```

#### before_pipeline_run

```
before_pipeline_run(run_params, pipeline, catalog)
```

Hook to be invoked before a pipeline runs.

Parameters:

- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`pipeline`** (`Pipeline`) – The Pipeline that will be run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol to be used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_pipeline_run(
    self, run_params: dict[str, Any], pipeline: Pipeline, catalog: CatalogProtocol
) -> None:
    """Hook to be invoked before a pipeline runs.

    Args:
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        pipeline: The ``Pipeline`` that will be run.
        catalog: An implemented instance of ``CatalogProtocol`` to be used during the run.
    """
    pass
```

#### on_pipeline_error

```
on_pipeline_error(error, run_params, pipeline, catalog)
```

Hook to be invoked if a pipeline run throws an uncaught Exception. The signature of this error hook should match the signature of `before_pipeline_run` along with the error that was raised.

Parameters:

- **`error`** (`Exception`) – The uncaught exception thrown during the pipeline run.
- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`pipeline`** (`Pipeline`) – The Pipeline that will was run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def on_pipeline_error(
    self,
    error: Exception,
    run_params: dict[str, Any],
    pipeline: Pipeline,
    catalog: CatalogProtocol,
) -> None:
    """Hook to be invoked if a pipeline run throws an uncaught Exception.
    The signature of this error hook should match the signature of ``before_pipeline_run``
    along with the error that was raised.

    Args:
        error: The uncaught exception thrown during the pipeline run.
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        pipeline: The ``Pipeline`` that will was run.
        catalog: An implemented instance of ``CatalogProtocol`` used during the run.
    """
    pass
```

### \_NullPluginManager

```
_NullPluginManager(*args, **kwargs)
```

This class creates an empty `hook_manager` that will ignore all calls to hooks, allowing the runner to function if no `hook_manager` has been instantiated.

Source code in `kedro/framework/hooks/manager.py`

```
def __init__(self, *args: Any, **kwargs: Any) -> None:
    pass
```

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

## kedro.framework.hooks.markers

This module provides markers to declare Kedro's hook specs and implementations. For more information, please see [Pluggy's documentation](https://pluggy.readthedocs.io/en/stable/#marking-hooks).

### HOOK_NAMESPACE

```
HOOK_NAMESPACE = 'kedro'
```

### hook_impl

```
hook_impl = HookimplMarker(HOOK_NAMESPACE)
```

### hook_spec

```
hook_spec = HookspecMarker(HOOK_NAMESPACE)
```

## kedro.framework.hooks.specs

A module containing specifications for all callable hooks in the Kedro's execution timeline. For more information about these specifications, please visit [Pluggy's documentation](https://pluggy.readthedocs.io/en/stable/#specs)

### hook_spec

```
hook_spec = HookspecMarker(HOOK_NAMESPACE)
```

### CatalogProtocol

Bases: `Protocol[_C, _DS]`

#### __contains__

```
__contains__(ds_name)
```

Check if a dataset is in the catalog.

Source code in `kedro/io/core.py`

```
def __contains__(self, ds_name: str) -> bool:
    """Check if a dataset is in the catalog."""
    ...
```

#### __getitem__

```
__getitem__(ds_name)
```

Get a dataset by name from an internal collection of datasets.

Source code in `kedro/io/core.py`

```
def __getitem__(self, ds_name: str) -> _DS:
    """Get a dataset by name from an internal collection of datasets."""
    ...
```

#### __iter__

```
__iter__()
```

Returns an iterator for the object.

Source code in `kedro/io/core.py`

```
def __iter__(self) -> Iterator[str]:
    """Returns an iterator for the object."""
    ...
```

#### __repr__

```
__repr__()
```

Returns the canonical string representation of the object.

Source code in `kedro/io/core.py`

```
def __repr__(self) -> str:
    """Returns the canonical string representation of the object."""
    ...
```

#### __setitem__

```
__setitem__(key, value)
```

Adds dataset using the given key as a dataset name and the provided data as the value.

Source code in `kedro/io/core.py`

```
def __setitem__(self, key: str, value: Any) -> None:
    """Adds dataset using the given key as a dataset name and the provided data as the value."""
    ...
```

#### confirm

```
confirm(name)
```

Confirm a dataset by its name.

Source code in `kedro/io/core.py`

```
def confirm(self, name: str) -> None:
    """Confirm a dataset by its name."""
    ...
```

#### exists

```
exists(name)
```

Checks whether registered dataset exists by calling its `exists()` method.

Source code in `kedro/io/core.py`

```
def exists(self, name: str) -> bool:
    """Checks whether registered dataset exists by calling its `exists()` method."""
    ...
```

#### from_config

```
from_config(catalog)
```

Create a catalog instance from configuration.

Source code in `kedro/io/core.py`

```
@classmethod
def from_config(cls, catalog: dict[str, dict[str, Any]] | None) -> _C:
    """Create a catalog instance from configuration."""
    ...
```

#### get

```
get(key, fallback_to_runtime_pattern=False)
```

Get a dataset by name from an internal collection of datasets.

Source code in `kedro/io/core.py`

```
def get(self, key: str, fallback_to_runtime_pattern: bool = False) -> _DS | None:
    """Get a dataset by name from an internal collection of datasets."""
    ...
```

#### items

```
items()
```

List all dataset names and datasets registered in the catalog.

Source code in `kedro/io/core.py`

```
def items(self) -> List[tuple[str, _DS]]:  # noqa: UP006
    """List all dataset names and datasets registered in the catalog."""
    ...
```

#### keys

```
keys()
```

List all dataset names registered in the catalog.

Source code in `kedro/io/core.py`

```
def keys(self) -> List[str]:  # noqa: UP006
    """List all dataset names registered in the catalog."""
    ...
```

#### load

```
load(name, version=None)
```

Load data from a registered dataset.

Source code in `kedro/io/core.py`

```
def load(self, name: str, version: str | None = None) -> Any:
    """Load data from a registered dataset."""
    ...
```

#### release

```
release(name)
```

Release any cached data associated with a dataset.

Source code in `kedro/io/core.py`

```
def release(self, name: str) -> None:
    """Release any cached data associated with a dataset."""
    ...
```

#### save

```
save(name, data)
```

Save data to a registered dataset.

Source code in `kedro/io/core.py`

```
def save(self, name: str, data: Any) -> None:
    """Save data to a registered dataset."""
    ...
```

#### values

```
values()
```

List all datasets registered in the catalog.

Source code in `kedro/io/core.py`

```
def values(self) -> List[_DS]:  # noqa: UP006
    """List all datasets registered in the catalog."""
    ...
```

### DataCatalogSpecs

Namespace that defines all specifications for a data catalog's lifecycle hooks.

#### after_catalog_created

```
after_catalog_created(catalog, conf_catalog, conf_creds, parameters, save_version, load_versions)
```

Hooks to be invoked after a data catalog is created. It receives the `catalog` as well as all the arguments for `KedroContext._create_catalog`.

Parameters:

- **`catalog`** (`CatalogProtocol`) – The catalog that was created.
- **`conf_catalog`** (`dict[str, Any]`) – The config from which the catalog was created.
- **`conf_creds`** (`dict[str, Any]`) – The credentials conf from which the catalog was created.
- **`parameters`** (`dict[str, Any]`) – The parameters that are added to the catalog after creation.
- **`save_version`** (`str`) – The save_version used in save operations for all datasets in the catalog.
- **`load_versions`** (`dict[str, str]`) – The load_versions used in load operations for each dataset in the catalog.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_catalog_created(  # noqa: PLR0913
    self,
    catalog: CatalogProtocol,
    conf_catalog: dict[str, Any],
    conf_creds: dict[str, Any],
    parameters: dict[str, Any],
    save_version: str,
    load_versions: dict[str, str],
) -> None:
    """Hooks to be invoked after a data catalog is created.
    It receives the ``catalog`` as well as
    all the arguments for ``KedroContext._create_catalog``.

    Args:
        catalog: The catalog that was created.
        conf_catalog: The config from which the catalog was created.
        conf_creds: The credentials conf from which the catalog was created.
        parameters: The parameters that are added to the catalog after creation.
        save_version: The save_version used in ``save`` operations
            for all datasets in the catalog.
        load_versions: The load_versions used in ``load`` operations
            for each dataset in the catalog.
    """
    pass
```

### DatasetSpecs

Namespace that defines all specifications for a dataset's lifecycle hooks.

#### after_dataset_loaded

```
after_dataset_loaded(dataset_name, data, node)
```

Hook to be invoked after a dataset is loaded from the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset that was loaded from the catalog.
- **`data`** (`Any`) – the actual data that was loaded from the catalog.
- **`node`** (`Node`) – The Node to run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_dataset_loaded(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked after a dataset is loaded from the catalog.

    Args:
        dataset_name: name of the dataset that was loaded from the catalog.
        data: the actual data that was loaded from the catalog.
        node: The ``Node`` to run.
    """
    pass
```

#### after_dataset_saved

```
after_dataset_saved(dataset_name, data, node)
```

Hook to be invoked after a dataset is saved in the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset that was saved to the catalog.
- **`data`** (`Any`) – the actual data that was saved to the catalog.
- **`node`** (`Node`) – The Node that ran.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_dataset_saved(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked after a dataset is saved in the catalog.

    Args:
        dataset_name: name of the dataset that was saved to the catalog.
        data: the actual data that was saved to the catalog.
        node: The ``Node`` that ran.
    """
    pass
```

#### before_dataset_loaded

```
before_dataset_loaded(dataset_name, node)
```

Hook to be invoked before a dataset is loaded from the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset to be loaded from the catalog.
- **`node`** (`Node`) – The Node to run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_dataset_loaded(self, dataset_name: str, node: Node) -> None:
    """Hook to be invoked before a dataset is loaded from the catalog.

    Args:
        dataset_name: name of the dataset to be loaded from the catalog.
        node: The ``Node`` to run.
    """
    pass
```

#### before_dataset_saved

```
before_dataset_saved(dataset_name, data, node)
```

Hook to be invoked before a dataset is saved to the catalog.

Parameters:

- **`dataset_name`** (`str`) – name of the dataset to be saved to the catalog.
- **`data`** (`Any`) – the actual data to be saved to the catalog.
- **`node`** (`Node`) – The Node that ran.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_dataset_saved(self, dataset_name: str, data: Any, node: Node) -> None:
    """Hook to be invoked before a dataset is saved to the catalog.

    Args:
        dataset_name: name of the dataset to be saved to the catalog.
        data: the actual data to be saved to the catalog.
        node: The ``Node`` that ran.
    """
    pass
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

### KedroContextSpecs

Namespace that defines all specifications for a Kedro context's lifecycle hooks.

#### after_context_created

```
after_context_created(context)
```

Hooks to be invoked after a `KedroContext` is created. This is the earliest hook triggered within a Kedro run. The `KedroContext` stores useful information such as `credentials`, `config_loader` and `env`.

Parameters:

- **`context`** (`KedroContext`) – The context that was created.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_context_created(
    self,
    context: KedroContext,
) -> None:
    """Hooks to be invoked after a `KedroContext` is created. This is the earliest
    hook triggered within a Kedro run. The `KedroContext` stores useful information
    such as `credentials`, `config_loader` and `env`.

    Args:
        context: The context that was created.
    """
```

### Node

```
Node(func, inputs, outputs, *, name=None, tags=None, confirms=None, namespace=None, preview_fn=None)
```

`Node` is an auxiliary class facilitating the operations required to run user-provided functions as part of Kedro pipelines.

Parameters:

- **`func`** (`Callable`) – A function that corresponds to the node logic. The function should have at least one input or output.
- **`inputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as inputs to the function. The number of names should match the number of arguments in the definition of the provided function. When dict[str, str] is provided, variable names will be mapped to function argument names.
- **`outputs`** (`str | list[str] | dict[str, str] | None`) – The name or the list of the names of variables used as outputs of the function. The number of names should match the number of outputs returned by the provided function. When dict[str, str] is provided, variable names will be mapped to the named outputs the function returns.
- **`name`** (`str | None`, default: `None` ) – Optional node name to be used when displaying the node in logs or any other visualisations. Valid node name must contain only letters, digits, hyphens, underscores and/or fullstops.
- **`tags`** (`str | Iterable[str] | None`, default: `None` ) – Optional set of tags to be applied to the node. Valid node tag must contain only letters, digits, hyphens, underscores and/or fullstops.
- **`confirms`** (`str | list[str] | None`, default: `None` ) – Optional name or the list of the names of the datasets that should be confirmed. This will result in calling confirm() method of the corresponding dataset instance. Specified dataset names do not necessarily need to be present in the node inputs or outputs.
- **`namespace`** (`str | None`, default: `None` ) – Optional node namespace.
- **`preview_fn`** (`Callable[..., PreviewPayload] | None`, default: `None` ) – Optional preview function that returns one of the valid preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview). This is an experimental feature.

Raises:

- `ValueError` – Raised in the following cases: a) When the provided arguments do not conform to the format suggested by the type hint of the argument. b) When the node produces multiple outputs with the same name. c) When an input has the same name as an output. d) When the given node name violates the requirements: it must contain only letters, digits, hyphens, underscores and/or fullstops.

Source code in `kedro/pipeline/node.py`

```
def __init__(  # noqa: PLR0913, PLR0912
    self,
    func: Callable,
    inputs: str | list[str] | dict[str, str] | None,
    outputs: str | list[str] | dict[str, str] | None,
    *,
    name: str | None = None,
    tags: str | Iterable[str] | None = None,
    confirms: str | list[str] | None = None,
    namespace: str | None = None,
    preview_fn: Callable[..., PreviewPayload] | None = None,
):
    """Create a node in the pipeline by providing a function to be called
    along with variable names for inputs and/or outputs.

    Args:
        func: A function that corresponds to the node logic.
            The function should have at least one input or output.
        inputs: The name or the list of the names of variables used as
            inputs to the function. The number of names should match
            the number of arguments in the definition of the provided
            function. When dict[str, str] is provided, variable names
            will be mapped to function argument names.
        outputs: The name or the list of the names of variables used
            as outputs of the function. The number of names should match
            the number of outputs returned by the provided function.
            When dict[str, str] is provided, variable names will be mapped
            to the named outputs the function returns.
        name: Optional node name to be used when displaying the node in
            logs or any other visualisations. Valid node name must contain
            only letters, digits, hyphens, underscores and/or fullstops.
        tags: Optional set of tags to be applied to the node. Valid node tag must
            contain only letters, digits, hyphens, underscores and/or fullstops.
        confirms: Optional name or the list of the names of the datasets
            that should be confirmed. This will result in calling
            ``confirm()`` method of the corresponding dataset instance.
            Specified dataset names do not necessarily need to be present
            in the node ``inputs`` or ``outputs``.
        namespace: Optional node namespace.
        preview_fn: Optional preview function that returns one of the valid
            preview types (TextPreview, MermaidPreview, ImagePreview, or CustomPreview).
            This is an experimental feature.

    Raises:
        ValueError: Raised in the following cases:
            a) When the provided arguments do not conform to
            the format suggested by the type hint of the argument.
            b) When the node produces multiple outputs with the same name.
            c) When an input has the same name as an output.
            d) When the given node name violates the requirements:
            it must contain only letters, digits, hyphens, underscores
            and/or fullstops.

    """
    if not callable(func):
        raise ValueError(
            _node_error_message(
                f"first argument must be a function, not '{type(func).__name__}'."
            )
        )

    if inputs and not isinstance(inputs, (list | dict | str)):
        raise ValueError(
            _node_error_message(
                f"'inputs' type must be one of [String, List, Dict, None], "
                f"not '{type(inputs).__name__}'."
            )
        )

    for _input in _to_list(inputs):
        if not isinstance(_input, str):
            raise ValueError(
                _node_error_message(
                    f"names of variables used as inputs to the function "
                    f"must be of 'String' type, but {_input} from {inputs} "
                    f"is '{type(_input)}'."
                )
            )
        _node_dataset_name_validation(_input, namespace)

    if outputs and not isinstance(outputs, (list | dict | str)):
        raise ValueError(
            _node_error_message(
                f"'outputs' type must be one of [String, List, Dict, None], "
                f"not '{type(outputs).__name__}'."
            )
        )

    for _output in _to_list(outputs):
        if not isinstance(_output, str):
            raise ValueError(
                _node_error_message(
                    f"names of variables used as outputs of the function "
                    f"must be of 'String' type, but {_output} from {outputs} "
                    f"is '{type(_output)}'."
                )
            )
        _node_dataset_name_validation(_output, namespace)

    if not inputs and not outputs:
        raise ValueError(
            _node_error_message("it must have some 'inputs' or 'outputs'.")
        )

    self._validate_inputs(func, inputs)

    self._func = func
    self._inputs = inputs
    # The type of _outputs is picked up as possibly being None, however the checks above prevent that
    # ever being the case. Mypy doesn't get that though, so it complains about the assignment of outputs to
    # _outputs with different types.
    self._outputs: str | list[str] | dict[str, str] = outputs  # type: ignore[assignment]
    if name and not re.match(r"[\w\.-]+$", name):
        raise ValueError(
            f"'{name}' is not a valid node name. It must contain only "
            f"letters, digits, hyphens, underscores and/or fullstops."
        )
    self._name = name
    self._namespace = namespace
    self._tags = set(_to_list(tags))
    for tag in self._tags:
        if not re.match(r"[\w\.-]+$", tag):
            raise ValueError(
                f"'{tag}' is not a valid node tag. It must contain only "
                f"letters, digits, hyphens, underscores and/or fullstops."
            )

    self._validate_unique_outputs()
    self._validate_inputs_dif_than_outputs()
    self._confirms = confirms

    if preview_fn:
        if not callable(preview_fn):
            raise ValueError(
                _node_error_message(
                    f"preview_fn must be a function, not '{type(preview_fn).__name__}'."
                )
            )
        if not getattr(Node, "__preview_fn_warned__", False):
            warn(
                "The 'preview_fn' feature is experimental and may change in future versions.",
                category=KedroExperimentalWarning,
                stacklevel=2,
            )
            setattr(Node, "__preview_fn_warned__", True)

    self._preview_fn = preview_fn
```

#### confirms

```
confirms
```

Return dataset names to confirm as a list.

Returns:

- `list[str]` – Dataset names to confirm as a list.

#### func

```
func
```

Exposes the underlying function of the node.

Returns:

- `Callable` – Return the underlying function of the node.

#### inputs

```
inputs
```

Return node inputs as a list, in the order required to bind them properly to the node's function.

Returns:

- `list[str]` – Node input names as a list.

#### name

```
name
```

Node's name.

Returns:

- `str` – Node's name if provided or the name of its function.

#### namespace

```
namespace
```

Node's namespace.

Returns:

- `str | None` – String representing node's namespace, typically from outer to inner scopes.

#### namespace_prefixes

```
namespace_prefixes
```

Return all hierarchical prefixes of the node's namespace.

Returns:

- `list[str]` – A list of namespace prefixes, from shortest to longest.
- `list[str]` – For example, a namespace 'a.b.c' would return ['a', 'a.b', 'a.b.c'].
- `list[str]` – If the node has no namespace, returns an empty list.

#### outputs

```
outputs
```

Return node outputs as a list preserving the original order if possible.

Returns:

- `list[str]` – Node output names as a list.

#### short_name

```
short_name
```

Node's name.

Returns:

- `str` – Returns a short, user-friendly name that is not guaranteed to be unique.
- `str` – The namespace is stripped out of the node name.

#### tags

```
tags
```

Return the tags assigned to the node.

Returns:

- `set[str]` – Return the set of all assigned tags to the node.

#### preview

```
preview()
```

Execute the preview function if available and validate its return type.

Returns:

- `PreviewPayload | None` – A preview payload (one of TextPreview, MermaidPreview, ImagePreview, or CustomPreview) if preview_fn is set, None otherwise.

Raises:

- `ValueError` – If the preview function does not return one of the valid preview types.

Examples:

```
from kedro.pipeline.preview_contract import (
    MermaidPreview,
    ImagePreview,
)

# Define your preview methods


# Example 1: Mermaid diagram
def preview_pipeline_flow() -> MermaidPreview:
    steps = ["Load", "Validate", "Transform", "Save"]
    mermaid = "graph LR\n"
    for i, step in enumerate(steps):
        if i < len(steps) - 1:
            mermaid += f"    {step} --> {steps[i+1]}\n"

    return MermaidPreview(content=mermaid)


# Example 2: Image preview (URL or data URI)
def preview_image() -> ImagePreview:
    return ImagePreview(
        content="https://example.com/chart.png",
        # or use data URI: "data:image/png;base64,iVBORw0KGgo..."
    )


# Define your node which uses the preview_fn
my_node = node(
    func=process_data,
    inputs="raw_data",
    outputs="processed_data",
    preview_fn=your_preview_function,
)

# Receive the preview payload
payload = my_node.preview()

# Serialize for frontend/API use:
json_dict = payload.to_dict()  # Returns JSONObject
```

Source code in `kedro/pipeline/node.py`

````
def preview(self) -> PreviewPayload | None:
    """Execute the preview function if available and validate its return type.

    Returns:
        A preview payload (one of TextPreview, MermaidPreview, ImagePreview,
            or CustomPreview) if preview_fn is set, None otherwise.

    Raises:
        ValueError: If the preview function does not return one of the valid
            preview types.

    Examples:
        ```python
        from kedro.pipeline.preview_contract import (
            MermaidPreview,
            ImagePreview,
        )

        # Define your preview methods


        # Example 1: Mermaid diagram
        def preview_pipeline_flow() -> MermaidPreview:
            steps = ["Load", "Validate", "Transform", "Save"]
            mermaid = "graph LR\\n"
            for i, step in enumerate(steps):
                if i < len(steps) - 1:
                    mermaid += f"    {step} --> {steps[i+1]}\\n"

            return MermaidPreview(content=mermaid)


        # Example 2: Image preview (URL or data URI)
        def preview_image() -> ImagePreview:
            return ImagePreview(
                content="https://example.com/chart.png",
                # or use data URI: "data:image/png;base64,iVBORw0KGgo..."
            )


        # Define your node which uses the preview_fn
        my_node = node(
            func=process_data,
            inputs="raw_data",
            outputs="processed_data",
            preview_fn=your_preview_function,
        )

        # Receive the preview payload
        payload = my_node.preview()

        # Serialize for frontend/API use:
        json_dict = payload.to_dict()  # Returns JSONObject
        ```
    """
    if not self._preview_fn:
        return None

    result = self._preview_fn()

    # Import the specific preview classes for isinstance check
    from kedro.pipeline.preview_contract import (
        CustomPreview,
        ImagePreview,
        MermaidPreview,
        TextPreview,
    )

    valid_types = (
        TextPreview,
        MermaidPreview,
        ImagePreview,
        CustomPreview,
    )

    if not isinstance(result, valid_types):
        raise ValueError(
            f"preview_fn must return one of the valid preview types "
            f"(TextPreview, MermaidPreview, ImagePreview, or CustomPreview), "
            f"but got '{type(result).__name__}' instead."
        )

    return result
````

#### run

```
run(inputs=None)
```

Run this node using the provided inputs and return its results in a dictionary.

Parameters:

- **`inputs`** (`dict[str, Any] | None`, default: `None` ) – Dictionary of inputs as specified at the creation of the node.

Raises:

- `ValueError` – In the following cases: a) The node function inputs are incompatible with the node input definition. Example 1: node definition input is a list of 2 DataFrames, whereas only 1 was provided or 2 different ones were provided. b) The node function outputs are incompatible with the node output definition. Example 1: node function definition is a dictionary, whereas function returns a list. Example 2: node definition output is a list of 5 strings, whereas the function returns a list of 4 objects.
- `Exception` – Any exception thrown during execution of the node.

Returns:

- `dict[str, Any]` – All produced node outputs are returned in a dictionary, where the
- `dict[str, Any]` – keys are defined by the node outputs.

Source code in `kedro/pipeline/node.py`

```
def run(self, inputs: dict[str, Any] | None = None) -> dict[str, Any]:
    """Run this node using the provided inputs and return its results
    in a dictionary.

    Args:
        inputs: Dictionary of inputs as specified at the creation of
            the node.

    Raises:
        ValueError: In the following cases:
            a) The node function inputs are incompatible with the node
            input definition.
            Example 1: node definition input is a list of 2
            DataFrames, whereas only 1 was provided or 2 different ones
            were provided.
            b) The node function outputs are incompatible with the node
            output definition.
            Example 1: node function definition is a dictionary,
            whereas function returns a list.
            Example 2: node definition output is a list of 5
            strings, whereas the function returns a list of 4 objects.
        Exception: Any exception thrown during execution of the node.

    Returns:
        All produced node outputs are returned in a dictionary, where the
        keys are defined by the node outputs.

    """
    self._logger.info("Running node: %s", str(self))

    outputs = None

    if not (inputs is None or isinstance(inputs, dict)):
        raise ValueError(
            f"Node.run() expects a dictionary or None, "
            f"but got {type(inputs)} instead"
        )

    try:
        inputs = {} if inputs is None else inputs
        if not self._inputs:
            outputs = self._run_with_no_inputs(inputs)
        elif isinstance(self._inputs, str):
            outputs = self._run_with_one_input(inputs, self._inputs)
        elif isinstance(self._inputs, list):
            outputs = self._run_with_list(inputs, self._inputs)
        elif isinstance(self._inputs, dict):
            outputs = self._run_with_dict(inputs, self._inputs)

        return self._outputs_to_dictionary(outputs)

    # purposely catch all exceptions
    except Exception as exc:
        self._logger.error(
            "Node %s failed with error: \n%s",
            str(self),
            str(exc),
            extra={"markup": True},
        )
        raise exc
```

#### tag

```
tag(tags)
```

Create a new `Node` which is an exact copy of the current one, but with more tags added to it.

Parameters:

- **`tags`** (`str | Iterable[str]`) – The tags to be added to the new node.

Returns:

- `Node` – A copy of the current Node object with the tags added.

Source code in `kedro/pipeline/node.py`

```
def tag(self, tags: str | Iterable[str]) -> Node:
    """Create a new ``Node`` which is an exact copy of the current one,
        but with more tags added to it.

    Args:
        tags: The tags to be added to the new node.

    Returns:
        A copy of the current ``Node`` object with the tags added.

    """
    return self._copy(tags=self.tags | set(_to_list(tags)))
```

### NodeSpecs

Namespace that defines all specifications for a node's lifecycle hooks.

#### after_node_run

```
after_node_run(node, catalog, inputs, outputs, is_async, run_id)
```

Hook to be invoked after a node runs.

Parameters:

- **`node`** (`Node`) – The Node that ran.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`outputs`** (`dict[str, Any]`) – The dictionary of outputs dataset. The keys are dataset names and the values are the actual computed output data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_node_run(  # noqa: PLR0913
    self,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    outputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> None:
    """Hook to be invoked after a node runs.

    Args:
        node: The ``Node`` that ran.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        outputs: The dictionary of outputs dataset.
            The keys are dataset names and the values are the actual computed output data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.
    """
    pass
```

#### before_node_run

```
before_node_run(node, catalog, inputs, is_async, run_id)
```

Hook to be invoked before a node runs.

Parameters:

- **`node`** (`Node`) – The Node to run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Returns:

- `dict[str, Any] | None` – Either None or a dictionary mapping dataset name(s) to new value(s). If returned, this dictionary will be used to update the node inputs, which allows to overwrite the node inputs.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_node_run(
    self,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> dict[str, Any] | None:
    """Hook to be invoked before a node runs.

    Args:
        node: The ``Node`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.

    Returns:
        Either None or a dictionary mapping dataset name(s) to new value(s).
            If returned, this dictionary will be used to update the node inputs,
            which allows to overwrite the node inputs.
    """
    pass
```

#### on_node_error

```
on_node_error(error, node, catalog, inputs, is_async, run_id)
```

Hook to be invoked if a node run throws an uncaught error. The signature of this error hook should match the signature of `before_node_run` along with the error that was raised.

Parameters:

- **`error`** (`Exception`) – The uncaught exception thrown during the node run.
- **`node`** (`Node`) – The Node to run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol containing the node's inputs and outputs.
- **`inputs`** (`dict[str, Any]`) – The dictionary of inputs dataset. The keys are dataset names and the values are the actual loaded input data, not the dataset instance.
- **`is_async`** (`bool`) – Whether the node was run in async mode.
- **`run_id`** (`str`) – The id of the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def on_node_error(  # noqa: PLR0913
    self,
    error: Exception,
    node: Node,
    catalog: CatalogProtocol,
    inputs: dict[str, Any],
    is_async: bool,
    run_id: str,
) -> None:
    """Hook to be invoked if a node run throws an uncaught error.
    The signature of this error hook should match the signature of ``before_node_run``
    along with the error that was raised.

    Args:
        error: The uncaught exception thrown during the node run.
        node: The ``Node`` to run.
        catalog: An implemented instance of ``CatalogProtocol`` containing the node's inputs and outputs.
        inputs: The dictionary of inputs dataset.
            The keys are dataset names and the values are the actual loaded input data,
            not the dataset instance.
        is_async: Whether the node was run in ``async`` mode.
        run_id: The id of the run.
    """
    pass
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

### PipelineSpecs

Namespace that defines all specifications for a pipeline's lifecycle hooks.

#### after_pipeline_run

```
after_pipeline_run(run_params, run_result, pipeline, catalog)
```

Hook to be invoked after a pipeline runs.

Parameters:

- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`run_result`** (`dict[str, Any]`) – The output of Pipeline run.
- **`pipeline`** (`Pipeline`) – The Pipeline that was run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def after_pipeline_run(
    self,
    run_params: dict[str, Any],
    run_result: dict[str, Any],
    pipeline: Pipeline,
    catalog: CatalogProtocol,
) -> None:
    """Hook to be invoked after a pipeline runs.

    Args:
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        run_result: The output of ``Pipeline`` run.
        pipeline: The ``Pipeline`` that was run.
        catalog: An implemented instance of ``CatalogProtocol`` used during the run.
    """
    pass
```

#### before_pipeline_run

```
before_pipeline_run(run_params, pipeline, catalog)
```

Hook to be invoked before a pipeline runs.

Parameters:

- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`pipeline`** (`Pipeline`) – The Pipeline that will be run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol to be used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def before_pipeline_run(
    self, run_params: dict[str, Any], pipeline: Pipeline, catalog: CatalogProtocol
) -> None:
    """Hook to be invoked before a pipeline runs.

    Args:
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        pipeline: The ``Pipeline`` that will be run.
        catalog: An implemented instance of ``CatalogProtocol`` to be used during the run.
    """
    pass
```

#### on_pipeline_error

```
on_pipeline_error(error, run_params, pipeline, catalog)
```

Hook to be invoked if a pipeline run throws an uncaught Exception. The signature of this error hook should match the signature of `before_pipeline_run` along with the error that was raised.

Parameters:

- **`error`** (`Exception`) – The uncaught exception thrown during the pipeline run.
- **`run_params`** (`dict[str, Any]`) – The params used to run the pipeline. Should have the following schema:: { "run_id": str "project_path": str, "env": str, "kedro_version": str, "tags": Optional\[List[str]\], "from_nodes": Optional\[List[str]\], "to_nodes": Optional\[List[str]\], "node_names": Optional\[List[str]\], "from_inputs": Optional\[List[str]\], "to_outputs": Optional\[List[str]\], "load_versions": Optional\[List[str]\], "runtime_params": Optional\[Dict[str, Any]\] "pipeline_name": str, "namespace": Optional[str], "runner": str, }
- **`pipeline`** (`Pipeline`) – The Pipeline that will was run.
- **`catalog`** (`CatalogProtocol`) – An implemented instance of CatalogProtocol used during the run.

Source code in `kedro/framework/hooks/specs.py`

```
@hook_spec
def on_pipeline_error(
    self,
    error: Exception,
    run_params: dict[str, Any],
    pipeline: Pipeline,
    catalog: CatalogProtocol,
) -> None:
    """Hook to be invoked if a pipeline run throws an uncaught Exception.
    The signature of this error hook should match the signature of ``before_pipeline_run``
    along with the error that was raised.

    Args:
        error: The uncaught exception thrown during the pipeline run.
        run_params: The params used to run the pipeline.
            Should have the following schema::

               {
                 "run_id": str
                 "project_path": str,
                 "env": str,
                 "kedro_version": str,
                 "tags": Optional[List[str]],
                 "from_nodes": Optional[List[str]],
                 "to_nodes": Optional[List[str]],
                 "node_names": Optional[List[str]],
                 "from_inputs": Optional[List[str]],
                 "to_outputs": Optional[List[str]],
                 "load_versions": Optional[List[str]],
                 "runtime_params": Optional[Dict[str, Any]]
                 "pipeline_name": str,
                 "namespace": Optional[str],
                 "runner": str,
               }

        pipeline: The ``Pipeline`` that will was run.
        catalog: An implemented instance of ``CatalogProtocol`` used during the run.
    """
    pass
```
