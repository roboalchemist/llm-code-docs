# Source: https://docs.kedro.org/en/stable/api/framework/kedro.framework.context/index.md

## kedro.framework.context

`kedro.framework.context` provides functionality for loading Kedro project context.

| Name                                                                    | Type      | Description                                                                             |
| ----------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------- |
| [`KedroContext`](#kedro.framework.context.KedroContext)                 | Class     | The base class for Kedro project contexts.                                              |
| [`KedroContextError`](#kedro.framework.context.KedroContextError)       | Exception | Error occurred when loading project and running context pipeline.                       |
| [`CatalogCommandsMixin`](#kedro.framework.context.CatalogCommandsMixin) | Class     | A mixin class that provides additional commands for interacting with the `DataCatalog`. |

## kedro.framework.context.KedroContext

`KedroContext` is the base class which holds the configuration and Kedro's main functionality.

Create a context object by providing the root of a Kedro project and the environment configuration subfolders (see `kedro.config.OmegaConfigLoader`) Raises: KedroContextError: If there is a mismatch between Kedro project version and package version. Args: project_path: Project path to define the context for. config_loader: Kedro's `OmegaConfigLoader` for loading the configuration files. env: Optional argument for configuration default environment to be used for running the pipeline. If not specified, it defaults to "local". package_name: Package name for the Kedro project the context is created for. hook_manager: The `PluginManager` to activate hooks, supplied by the session. runtime_params: Optional dictionary containing runtime project parameters. If specified, will update (and therefore take precedence over) the parameters retrieved from the project configuration.

### \_hook_manager

```
_hook_manager = field(init=True)
```

### \_package_name

```
_package_name = field(init=True)
```

### \_runtime_params

```
_runtime_params = field(init=True, default=None, converter=deepcopy)
```

### catalog

```
catalog
```

Read-only property referring to Kedro's catalog\` for this context.

Returns:

- `CatalogProtocol` – catalog defined in catalog.yml.

Raises: KedroContextError: Incorrect catalog registered for the project.

### config_loader

```
config_loader = field(init=True)
```

### env

```
env = field(init=True)
```

### params

```
params
```

Read-only property referring to Kedro's parameters for this context.

Returns:

- `dict[str, Any]` – Parameters defined in parameters.yml with the addition of any extra parameters passed at initialization.

### project_path

```
project_path = field(init=True, converter=_expand_full_path)
```

### \_get_catalog

```
_get_catalog(catalog_class=DataCatalog, save_version=None, load_versions=None)
```

A hook for changing the creation of a catalog instance.

Returns:

- `CatalogProtocol` – catalog defined in catalog.yml.

Raises: KedroContextError: Incorrect catalog registered for the project.

Source code in `kedro/framework/context/context.py`

```
def _get_catalog(
    self,
    catalog_class: type = DataCatalog,
    save_version: str | None = None,
    load_versions: dict[str, str] | None = None,
) -> CatalogProtocol:
    """A hook for changing the creation of a catalog instance.

    Returns:
        catalog defined in `catalog.yml`.
    Raises:
        KedroContextError: Incorrect catalog registered for the project.

    """
    # '**/catalog*' reads modular pipeline configs
    conf_catalog = self.config_loader["catalog"]
    # turn relative paths in conf_catalog into absolute paths
    # before initializing the catalog
    conf_catalog = _convert_paths_to_absolute_posix(
        project_path=self.project_path, conf_dictionary=conf_catalog
    )
    conf_creds = self._get_config_credentials()

    if catalog_class is DataCatalog:
        catalog_class = compose_classes(catalog_class, CatalogCommandsMixin)

    catalog: CatalogProtocol = catalog_class.from_config(  # type: ignore[attr-defined]
        catalog=conf_catalog,
        credentials=conf_creds,
        load_versions=load_versions,
        save_version=save_version,
    )

    parameters = self._get_parameters()

    # Add parameters data to catalog.
    for param_name, param_value in parameters.items():
        catalog[param_name] = param_value

    _validate_transcoded_datasets(catalog)

    self._hook_manager.hook.after_catalog_created(
        catalog=catalog,
        conf_catalog=conf_catalog,
        conf_creds=conf_creds,
        parameters=parameters,
        save_version=save_version,
        load_versions=load_versions,
    )
    return catalog
```

### \_get_config_credentials

```
_get_config_credentials()
```

Getter for credentials specified in credentials directory.

Source code in `kedro/framework/context/context.py`

```
def _get_config_credentials(self) -> dict[str, Any]:
    """Getter for credentials specified in credentials directory."""
    try:
        conf_creds: dict[str, Any] = self.config_loader["credentials"]
    except MissingConfigException as exc:
        logging.getLogger(__name__).debug(
            "Credentials not found in your Kedro project config.\n %s", str(exc)
        )
        conf_creds = {}
    return conf_creds
```

### \_get_parameters

```
_get_parameters()
```

Returns a dictionary with data to be added in memory as \`MemoryDataset\`\` instances. Keys represent parameter names and the values are parameter values.

Source code in `kedro/framework/context/context.py`

````
def _get_parameters(self) -> dict[str, Any]:
    """Returns a dictionary with data to be added in memory as `MemoryDataset`` instances.
    Keys represent parameter names and the values are parameter values."""
    params = self.params
    params_dict = {"parameters": params}

    def _add_param_to_params_dict(param_name: str, param_value: Any) -> None:
        """This recursively adds parameter paths that are defined in `parameters.yml`
        with the addition of any extra parameters passed at initialization to the `params_dict`,
        whenever `param_value` is a dictionary itself, so that users can
        specify specific nested parameters in their node inputs.

        Example:
        ``` python
        param_name = "a"
        param_value = {"b": 1}
        _add_param_to_params_dict(param_name, param_value)
        assert params_dict["params:a"] == {"b": 1}
        assert params_dict["params:a.b"] == 1
        ```
        """
        key = f"params:{param_name}"
        params_dict[key] = param_value
        if isinstance(param_value, dict):
            for key, val in param_value.items():
                _add_param_to_params_dict(f"{param_name}.{key}", val)

    for param_name, param_value in params.items():
        _add_param_to_params_dict(param_name, param_value)

    return params_dict
````

## kedro.framework.context.KedroContextError

Bases: `Exception`

Error occurred when loading project and running context pipeline.

## kedro.framework.context.CatalogCommandsMixin

A mixin class that provides additional commands for interacting with the `DataCatalog`.

This class adds methods to list datasets, dataset factory patterns and resolve dataset factory patterns. It is designed to extend the functionality of the `DataCatalog` providing pipeline-based catalog functionality.

Methods:

- **`- describe_datasets`** – Show datasets per type for specified pipelines.
- **`- list_patterns`** – List all dataset factory patterns in the catalog.
- **`- resolve_patterns`** – Resolve dataset factories against pipeline datasets.

Usage:

You can integrate this mixin with the `DataCatalog` in two ways:

1. Using `compose_classes`:

   ```
   from kedro.io import DataCatalog
   from kedro.framework.context import CatalogCommandsMixin, compose_classes

   # DataCatalog instance without CatalogCommandsMixin
   assert not hasattr(DataCatalog(), "describe_datasets")

   # Compose a new class combining DataCatalog and CatalogCommandsMixin
   catalog_class = compose_classes(DataCatalog, CatalogCommandsMixin)

   # Create a catalog instance from configuration
   catalog = catalog_class.from_config(
       {
           "cars": {
               "type": "pandas.CSVDataset",
               "filepath": "cars.csv",
               "save_args": {"index": False},
           }
       }
   )

   # Assert that the catalog has the `describe_datasets` method
   assert hasattr(
       catalog, "describe_datasets"
   ), "describe_datasets method is not available"
   print("describe_datasets method is available!")
   # describe_datasets method is available!
   ```

1. Creating a new class with inheritance:

   ```
   from kedro.io import DataCatalog
   from kedro.framework.context import CatalogCommandsMixin


   class DataCatalogWithMixins(DataCatalog, CatalogCommandsMixin):
       pass


   catalog = DataCatalogWithMixins(datasets={"example": MemoryDataset()})
   assert hasattr(
       catalog, "describe_datasets"
   ), "describe_datasets method is not available"
   print("describe_datasets method is available!")
   # describe_datasets method is available!
   ```

### \_logger

```
_logger
```

### describe_datasets

```
describe_datasets(pipelines=None)
```

Describe datasets used in the specified pipelines, grouped by type.

This method provides a structured summary of datasets used in the selected pipelines, categorizing them into three groups:

- `datasets`: Datasets explicitly defined in the catalog.
- `factories`: Datasets resolved from dataset factory patterns.
- `defaults`: Datasets that do not match any pattern or explicit definition.

Parameters:

- **`pipelines`** (`list[str] | list[Pipeline] | None`, default: `None` ) – A list of pipeline names or Pipeline objects to analyze. If None, all pipelines are analyzed.

Returns:

- `dict` – A dictionary where keys are pipeline names and values are dictionaries
- `dict` – containing datasets grouped by type.

Example output: { "data_processing": { "datasets": { "kedro_datasets.pandas.parquet_dataset.ParquetDataset": ["model_input_table"] }, "factories": {}, "defaults": {"kedro.io.MemoryDataset": ["preprocessed_companies"]} } }

Source code in `kedro/framework/context/catalog_mixins.py`

```
def describe_datasets(
    self: DataCatalog, pipelines: list[str] | list[Pipeline] | None = None
) -> dict:
    """
    Describe datasets used in the specified pipelines, grouped by type.

    This method provides a structured summary of datasets used in the selected pipelines,
    categorizing them into three groups:
    - `datasets`: Datasets explicitly defined in the catalog.
    - `factories`: Datasets resolved from dataset factory patterns.
    - `defaults`: Datasets that do not match any pattern or explicit definition.

    Args:
        pipelines: A list of pipeline names or `Pipeline` objects to analyze.
            If `None`, all pipelines are analyzed.

    Returns:
        A dictionary where keys are pipeline names and values are dictionaries
        containing datasets grouped by type.

    Example output:
    {
        "data_processing": {
            "datasets": {
                "kedro_datasets.pandas.parquet_dataset.ParquetDataset": ["model_input_table"]
            },
            "factories": {},
            "defaults": {"kedro.io.MemoryDataset": ["preprocessed_companies"]}
        }
    }
    """
    target_pipelines = pipelines or _pipelines.keys()

    result = {}
    if not isinstance(target_pipelines, Iterable):
        target_pipelines = [target_pipelines]

    for i, pipe in enumerate(target_pipelines):
        pipeline_ds = set()
        pl_obj = _pipelines.get(pipe) if isinstance(pipe, str) else pipe
        if pl_obj:
            pipeline_ds = pl_obj.datasets()

        catalog_ds = set(self.keys())

        patterns_ds = set()
        default_ds = set()
        for ds_name in pipeline_ds - catalog_ds:
            if self.config_resolver.match_dataset_pattern(ds_name):
                patterns_ds.add(ds_name)
            else:
                default_ds.add(ds_name)

        used_ds_by_type = _group_ds_by_type(
            pipeline_ds - patterns_ds - default_ds, self
        )
        patterns_ds_by_type = _group_ds_by_type(patterns_ds, self)
        default_ds_by_type = _group_ds_by_type(default_ds, self)

        data = (
            ("datasets", used_ds_by_type),
            ("factories", patterns_ds_by_type),
            ("defaults", default_ds_by_type),
        )
        pipe_name = pipe if isinstance(pipe, str) else f"pipeline_{i}"
        result[pipe_name] = {key: value for key, value in data}

    return result
```

### list_patterns

```
list_patterns()
```

List all dataset factory patterns in the catalog, ranked by priority.

This method retrieves all dataset factory patterns defined in the catalog, ordered by the priority in which they are matched.

Returns:

- `list[str]` – A list of dataset factory patterns.

Source code in `kedro/framework/context/catalog_mixins.py`

```
def list_patterns(self: DataCatalog) -> list[str]:
    """
    List all dataset factory patterns in the catalog, ranked by priority.

    This method retrieves all dataset factory patterns defined in the catalog,
    ordered by the priority in which they are matched.

    Returns:
        A list of dataset factory patterns.
    """
    return self.config_resolver.list_patterns()
```

### resolve_patterns

```
resolve_patterns(pipelines=None)
```

Resolve dataset factory patterns against pipeline datasets.

This method resolves dataset factory patterns for datasets used in the specified pipelines. It includes datasets explicitly defined in the catalog as well as those resolved from dataset factory patterns.

Parameters:

- **`pipelines`** (`list[Pipeline] | None`, default: `None` ) – A list of Pipeline objects to analyze. If None, all pipelines are analyzed.

Returns:

- `dict[str, Any]` – A dictionary mapping dataset names to their unresolved configurations.

Source code in `kedro/framework/context/catalog_mixins.py`

```
def resolve_patterns(
    self: DataCatalog,
    pipelines: list[Pipeline] | None = None,
) -> dict[str, Any]:
    """
    Resolve dataset factory patterns against pipeline datasets.

    This method resolves dataset factory patterns for datasets used in the specified pipelines.
    It includes datasets explicitly defined in the catalog as well as those resolved
    from dataset factory patterns.

    Args:
        pipelines: A list of `Pipeline` objects to analyze.
            If `None`, all pipelines are analyzed.

    Returns:
        A dictionary mapping dataset names to their unresolved configurations.
    """
    target_pipelines = pipelines or _pipelines.keys()

    pipeline_datasets: set[str] = set()
    for pipe in target_pipelines:
        pl_obj = _pipelines.get(pipe) if isinstance(pipe, str) else pipe
        if pl_obj:
            pipeline_datasets.update(pl_obj.datasets())

    # We need to include datasets defined in the catalog.yaml and datasets added manually to the catalog
    explicit_datasets = {}
    for ds_name, ds in self.items():
        if is_parameter(ds_name):
            continue

        unresolved_config, _ = self.config_resolver._unresolve_credentials(
            ds_name, ds._init_config()
        )
        explicit_datasets[ds_name] = unresolved_config

    for ds_name in pipeline_datasets:
        if ds_name in explicit_datasets or is_parameter(ds_name):
            continue

        ds_config = self.config_resolver.resolve_pattern(ds_name)
        unresolved_config, _ = self.config_resolver._unresolve_credentials(
            ds_name, ds_config
        )
        explicit_datasets[ds_name] = unresolved_config

    return explicit_datasets
```
