# Source: https://docs.kedro.org/en/stable/api/io/kedro.io.SharedMemoryDataCatalog/index.md

## kedro.io.SharedMemoryDataCatalog

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

### default_runtime_patterns

```
default_runtime_patterns = {'{default}': {'type': 'kedro.io.SharedMemoryDataset'}}
```

### set_manager_datasets

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

### validate_catalog

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
