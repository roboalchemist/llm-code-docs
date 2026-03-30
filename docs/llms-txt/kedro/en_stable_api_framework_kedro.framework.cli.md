# Source: https://docs.kedro.org/en/stable/api/framework/kedro.framework.cli/index.md

## kedro.framework.cli

`kedro.framework.cli` implements commands available from Kedro's CLI.

| Submodule                                                       | Description                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [`kedro.framework.cli.catalog`](#kedro.framework.cli.catalog)   | A collection of CLI commands for working with Kedro catalog.              |
| [`kedro.framework.cli.cli`](#kedro.framework.cli.cli)           | `kedro` is a CLI for managing Kedro projects.                             |
| [`kedro.framework.cli.hooks`](#kedro.framework.cli.hooks)       | Provides primitives to use hooks to extend KedroCLI's behaviour.          |
| [`kedro.framework.cli.jupyter`](#kedro.framework.cli.jupyter)   | A collection of helper functions to integrate with Jupyter/IPython.       |
| [`kedro.framework.cli.pipeline`](#kedro.framework.cli.pipeline) | A collection of CLI commands for working with Kedro pipelines.            |
| [`kedro.framework.cli.project`](#kedro.framework.cli.project)   | A collection of CLI commands for working with Kedro projects.             |
| [`kedro.framework.cli.registry`](#kedro.framework.cli.registry) | A collection of CLI commands for working with registered Kedro pipelines. |
| [`kedro.framework.cli.starters`](#kedro.framework.cli.starters) | `kedro` is a CLI for managing Kedro projects.                             |
| [`kedro.framework.cli.utils`](#kedro.framework.cli.utils)       | Utilities for use with click.                                             |

## kedro.framework.cli.catalog

A collection of CLI commands for working with Kedro catalog.

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

### ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### \_create_session

```
_create_session(package_name, **kwargs)
```

Source code in `kedro/framework/cli/catalog.py`

```
def _create_session(package_name: str, **kwargs: Any) -> KedroSession:
    kwargs.setdefault("save_on_close", False)
    return KedroSession.create(**kwargs)
```

### catalog

```
catalog()
```

Commands for working with catalog.

Source code in `kedro/framework/cli/catalog.py`

```
@catalog_cli.group()
def catalog() -> None:
    """Commands for working with catalog."""
```

### catalog_cli

```
catalog_cli()
```

Source code in `kedro/framework/cli/catalog.py`

```
@click.group(name="kedro")
def catalog_cli() -> None:  # pragma: no cover
    pass
```

### describe_datasets

```
describe_datasets(metadata, pipeline, env)
```

Describe datasets used in the specified pipelines, grouped by type.

This command provides a structured overview of datasets used in the selected pipelines, categorizing them into three groups:

- `datasets`: Datasets explicitly defined in the catalog.
- `factories`: Datasets resolved from dataset factory patterns.
- `defaults`: Datasets that do not match any pattern or explicit definition.

Source code in `kedro/framework/cli/catalog.py`

```
@catalog.command("describe-datasets")
@env_option
@click.option(
    "--pipeline",
    "-p",
    type=str,
    default="",
    help="Name of the modular pipeline to run. If not set, "
    "the project pipeline is run by default.",
    callback=split_string,
)
@click.pass_obj
def describe_datasets(metadata: ProjectMetadata, pipeline: str, env: str) -> None:
    """
    Describe datasets used in the specified pipelines, grouped by type.\n

    This command provides a structured overview of datasets used in the selected pipelines,
    categorizing them into three groups:\n
    - `datasets`: Datasets explicitly defined in the catalog.\n
    - `factories`: Datasets resolved from dataset factory patterns.\n
    - `defaults`: Datasets that do not match any pattern or explicit definition.\n
    """
    session = _create_session(metadata.package_name, env=env)
    context = session.load_context()

    p = pipeline or None
    datasets_dict = context.catalog.describe_datasets(p)  # type: ignore

    secho(yaml.dump(datasets_dict))
```

### env_option

```
env_option(func_=None, **kwargs)
```

Add `--env` CLI option to a function.

Source code in `kedro/framework/cli/utils.py`

```
def env_option(func_: Any | None = None, **kwargs: Any) -> Any:
    """Add `--env` CLI option to a function."""
    default_args = {"type": str, "default": None, "help": ENV_HELP}
    kwargs = {**default_args, **kwargs}
    opt = click.option("--env", "-e", **kwargs)
    return opt(func_) if func_ else opt
```

### list_patterns

```
list_patterns(metadata, env)
```

List all dataset factory patterns in the catalog, ranked by priority.

This method retrieves all dataset factory patterns defined in the catalog, ordered by the priority in which they are matched.

Source code in `kedro/framework/cli/catalog.py`

```
@catalog.command("list-patterns")
@env_option
@click.pass_obj
def list_patterns(metadata: ProjectMetadata, env: str) -> None:
    """
    List all dataset factory patterns in the catalog, ranked by priority.

    This method retrieves all dataset factory patterns defined in the catalog,
    ordered by the priority in which they are matched.
    """
    session = _create_session(metadata.package_name, env=env)
    context = session.load_context()

    click.echo(yaml.dump(context.catalog.list_patterns()))  # type: ignore
```

### resolve_patterns

```
resolve_patterns(metadata, pipeline, env)
```

Resolve dataset factory patterns against pipeline datasets.

This method resolves dataset factory patterns for datasets used in the specified pipelines. It includes datasets explicitly defined in the catalog as well as those resolved from dataset factory patterns.

Source code in `kedro/framework/cli/catalog.py`

```
@catalog.command("resolve-patterns")
@env_option
@click.option(
    "--pipeline",
    "-p",
    type=str,
    default="",
    help="Name of the modular pipeline to run. If not set, "
    "the project pipeline is run by default.",
    callback=split_string,
)
@click.pass_obj
def resolve_patterns(metadata: ProjectMetadata, pipeline: str, env: str) -> None:
    """
    Resolve dataset factory patterns against pipeline datasets.

    This method resolves dataset factory patterns for datasets used in the specified pipelines.
    It includes datasets explicitly defined in the catalog as well as those resolved
    from dataset factory patterns.
    """
    session = _create_session(metadata.package_name, env=env)
    context = session.load_context()

    p = pipeline or None
    datasets_dict = context.catalog.resolve_patterns(p)  # type: ignore

    secho(yaml.dump(datasets_dict))
```

### split_string

```
split_string(ctx, param, value)
```

Split string by comma.

Source code in `kedro/framework/cli/utils.py`

```
def split_string(ctx: click.Context, param: Any, value: str) -> list[str]:
    """Split string by comma."""
    return [item.strip() for item in value.split(",") if item.strip()]
```

## kedro.framework.cli.cli

kedro is a CLI for managing Kedro projects.

This module implements commands available from the kedro CLI.

### BRIGHT_BLACK

```
BRIGHT_BLACK = (128, 128, 128)
```

### CONTEXT_SETTINGS

```
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
```

### ENTRY_POINT_GROUPS

```
ENTRY_POINT_GROUPS = {'global': 'kedro.global_commands', 'project': 'kedro.project_commands', 'init': 'kedro.init', 'line_magic': 'kedro.line_magic', 'hooks': 'kedro.hooks', 'cli_hooks': 'kedro.cli_hooks', 'starters': 'kedro.starters'}
```

### LOGGING

```
LOGGING = _ProjectLogging()
```

### LOGO

```
LOGO = f'
 _            _
| | _____  __| |_ __ ___
| |/ / _ \/ _` | '__/ _ \
|   <  __/ (_| | | | (_) |
|_|\_\___|\__,_|_|  \___/
v{__version__}
'
```

### ORANGE

```
ORANGE = (255, 175, 0)
```

### version

```
version = '1.2.0'
```

### CommandCollection

```
CommandCollection(*groups)
```

Bases: `CommandCollection`

Modified from the Click one to still run the source groups function.

Source code in `kedro/framework/cli/utils.py`

```
def __init__(self, *groups: tuple[str, Sequence[click.Group]]):
    self.groups = [
        (title, self._merge_same_name_collections(cli_list))
        for title, cli_list in groups
    ]
    sources = list(chain.from_iterable(cli_list for _, cli_list in self.groups))
    help_texts = [
        cli.help
        for cli_collection in sources
        for cli in cli_collection.sources
        if cli.help
    ]
    super().__init__(
        sources=sources,  # type: ignore[arg-type]
        help="\n\n".join(help_texts),
        context_settings=CONTEXT_SETTINGS,
    )
    self.params = sources[0].params
    self.callback = sources[0].callback
```

### KedroCLI

```
KedroCLI(project_path)
```

Bases: `CommandCollection`

A CommandCollection class to encapsulate the KedroCLI command loading.

Source code in `kedro/framework/cli/cli.py`

```
def __init__(self, project_path: Path):
    self._metadata = None  # running in package mode
    if is_kedro_project(project_path):
        self._metadata = bootstrap_project(project_path)
    self._cli_hook_manager = get_cli_hook_manager()

    super().__init__(
        ("Global commands", self.global_groups),
        ("Project specific commands", self.project_groups),
    )
```

#### global_groups

```
global_groups
```

Property which loads all global command groups from plugins and combines them with the built-in ones (eventually overriding the built-in ones if they are redefined by plugins).

#### project_groups

```
project_groups
```

Property which loads all project command groups from the project and the plugins, then combines them with the built-in ones. Built-in commands can be overridden by plugins, which can be overridden by a custom project cli.py. See https://docs.kedro.org/en/stable/extend/common_use_cases/#use-case-3-how-to-add-or-modify-cli-commands on how to add this.

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### LazyGroup

```
LazyGroup(*args, lazy_subcommands=None, **kwargs)
```

Bases: `Group`

A click Group that supports lazy loading of subcommands.

Source code in `kedro/framework/cli/utils.py`

```
def __init__(
    self,
    *args: Any,
    lazy_subcommands: dict[str, str] | None = None,
    **kwargs: Any,
):
    super().__init__(*args, **kwargs)
    # lazy_subcommands is a map of the form:
    #
    #   {command-name} -> {module-name}.{command-object-name}
    #
    self.lazy_subcommands = lazy_subcommands or {}
```

### \_get_entry_points

```
_get_entry_points(name)
```

Get all kedro related entry points

Source code in `kedro/framework/cli/utils.py`

```
def _get_entry_points(name: str) -> Any:
    """Get all kedro related entry points"""
    return importlib.metadata.entry_points().select(  # type: ignore[no-untyped-call]
        group=ENTRY_POINT_GROUPS[name]
    )
```

### \_init_plugins

```
_init_plugins()
```

Source code in `kedro/framework/cli/cli.py`

```
def _init_plugins() -> None:
    init_hooks = load_entry_points("init")
    for init_hook in init_hooks:
        init_hook()
```

### bootstrap_project

```
bootstrap_project(project_path)
```

Run setup required at the beginning of the workflow when running in project mode, and return project metadata.

Source code in `kedro/framework/startup.py`

```
def bootstrap_project(project_path: str | Path) -> ProjectMetadata:
    """Run setup required at the beginning of the workflow
    when running in project mode, and return project metadata.
    """

    project_path = Path(project_path).expanduser().resolve()
    metadata = _get_project_metadata(project_path)
    _add_src_to_path(metadata.source_dir, project_path)
    configure_project(metadata.package_name)
    return metadata
```

### cli

```
cli()
```

Kedro is a CLI for creating and using Kedro projects. For more information, type `kedro info`.

NOTE: If a command from a plugin conflicts with a built-in command from Kedro, the command from the plugin will take precedence.

Source code in `kedro/framework/cli/cli.py`

```
@click.group(context_settings=CONTEXT_SETTINGS, name="kedro")
@click.version_option(version, "--version", "-V", help="Show version and exit")
def cli() -> None:  # pragma: no cover
    """Kedro is a CLI for creating and using Kedro projects. For more
    information, type ``kedro info``.

    NOTE: If a command from a plugin conflicts with a built-in command from Kedro,
    the command from the plugin will take precedence.

    """
    pass
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

### get_cli_hook_manager

```
get_cli_hook_manager()
```

Create or return the global \_hook_manager singleton instance.

Source code in `kedro/framework/cli/hooks/manager.py`

```
def get_cli_hook_manager() -> PluginManager:
    """Create or return the global _hook_manager singleton instance."""
    global _cli_hook_manager  # noqa: PLW0603
    if _cli_hook_manager is None:
        _cli_hook_manager = CLIHooksManager()
    _cli_hook_manager.trace.root.setwriter(
        logger.debug if logger.getEffectiveLevel() == logging.DEBUG else None
    )
    _cli_hook_manager.enable_tracing()
    return _cli_hook_manager
```

### global_commands

```
global_commands()
```

Source code in `kedro/framework/cli/cli.py`

```
@click.group(
    context_settings=CONTEXT_SETTINGS,
    name="kedro",
    cls=LazyGroup,
    lazy_subcommands={
        "new": "kedro.framework.cli.starters.new",
        "starter": "kedro.framework.cli.starters.starter",
    },
)
def global_commands() -> None:
    pass  # pragma: no cover
```

### info

```
info()
```

Get more information about kedro.

Source code in `kedro/framework/cli/cli.py`

```
@cli.command()
def info() -> None:
    """Get more information about kedro."""
    click.secho(LOGO, fg="green")
    click.echo(
        "Kedro is a Python framework for\n"
        "creating reproducible, maintainable\n"
        "and modular data science code."
    )

    plugin_versions = {}
    plugin_entry_points = defaultdict(set)
    for plugin_entry_point in ENTRY_POINT_GROUPS:
        for entry_point in _get_entry_points(plugin_entry_point):
            module_name = entry_point.module.split(".")[0]
            plugin_versions[module_name] = entry_point.dist.version
            plugin_entry_points[module_name].add(plugin_entry_point)

    click.echo()
    if plugin_versions:
        click.echo("Installed plugins:")
        for plugin_name, plugin_version in sorted(plugin_versions.items()):
            entrypoints_str = ",".join(sorted(plugin_entry_points[plugin_name]))
            click.echo(
                f"{plugin_name}: {plugin_version} (entry points:{entrypoints_str})"
            )
    else:  # pragma: no cover
        click.echo("No plugins installed")
```

### is_kedro_project

```
is_kedro_project(project_path)
```

Evaluate if a given path is a root directory of a Kedro project or not.

Parameters:

- **`project_path`** (`str | Path`) – Path to be tested for being a root of a Kedro project.

Returns:

- `bool` – True if a given path is a root directory of a Kedro project, otherwise False.

Source code in `kedro/utils.py`

```
def is_kedro_project(project_path: str | Path) -> bool:
    """Evaluate if a given path is a root directory of a Kedro project or not.

    Args:
        project_path: Path to be tested for being a root of a Kedro project.

    Returns:
        True if a given path is a root directory of a Kedro project, otherwise False.
    """
    metadata_file = Path(project_path).expanduser().resolve() / _PYPROJECT
    if not metadata_file.is_file():
        return False

    try:
        return "[tool.kedro]" in metadata_file.read_text(encoding="utf-8")
    except Exception:
        return False
```

### load_entry_points

```
load_entry_points(name)
```

Load package entry point commands.

Parameters:

- **`name`** (`str`) – The key value specified in ENTRY_POINT_GROUPS.

Raises:

- `KedroCliError` – If loading an entry point failed.

Returns:

- `Sequence[Group]` – List of entry point commands.

Source code in `kedro/framework/cli/utils.py`

```
def load_entry_points(name: str) -> Sequence[click.Group]:
    """Load package entry point commands.

    Args:
        name: The key value specified in ENTRY_POINT_GROUPS.

    Raises:
        KedroCliError: If loading an entry point failed.

    Returns:
        List of entry point commands.

    """

    entry_point_commands = []
    for entry_point in _get_entry_points(name):
        loaded_entry_point = _safe_load_entry_point(entry_point)
        if loaded_entry_point:
            entry_point_commands.append(loaded_entry_point)
    return entry_point_commands
```

### main

```
main()
```

Main entry point. Look for a `cli.py`, and, if found, add its commands to `kedro`'s before invoking the CLI.

Source code in `kedro/framework/cli/cli.py`

```
def main() -> None:  # pragma: no cover
    """Main entry point. Look for a ``cli.py``, and, if found, add its
    commands to `kedro`'s before invoking the CLI.
    """
    _init_plugins()
    cli_collection = KedroCLI(project_path=find_kedro_project(Path.cwd()) or Path.cwd())
    cli_collection()
```

### project_commands

```
project_commands()
```

Source code in `kedro/framework/cli/cli.py`

```
@click.group(
    context_settings=CONTEXT_SETTINGS,
    cls=LazyGroup,
    name="kedro",
    lazy_subcommands={
        "registry": "kedro.framework.cli.registry.registry",
        "catalog": "kedro.framework.cli.catalog.catalog",
        "ipython": "kedro.framework.cli.project.ipython",
        "run": "kedro.framework.cli.project.run",
        "package": "kedro.framework.cli.project.package",
        "jupyter": "kedro.framework.cli.jupyter.jupyter",
        "pipeline": "kedro.framework.cli.pipeline.pipeline",
    },
)
def project_commands() -> None:
    pass  # pragma: no cover
```

## kedro.framework.cli.hooks

`kedro.framework.cli.hooks` provides primitives to use hooks to extend KedroCLI's behaviour

### __all__

```
__all__ = ['CLIHooksManager', 'cli_hook_impl', 'get_cli_hook_manager']
```

### cli_hook_impl

```
cli_hook_impl = HookimplMarker(CLI_HOOK_NAMESPACE)
```

### CLIHooksManager

```
CLIHooksManager()
```

Bases: `PluginManager`

Hooks manager to manage CLI hooks

Source code in `kedro/framework/cli/hooks/manager.py`

```
def __init__(self) -> None:
    super().__init__(CLI_HOOK_NAMESPACE)
    self.add_hookspecs(CLICommandSpecs)
    self._register_cli_hooks()
```

### get_cli_hook_manager

```
get_cli_hook_manager()
```

Create or return the global \_hook_manager singleton instance.

Source code in `kedro/framework/cli/hooks/manager.py`

```
def get_cli_hook_manager() -> PluginManager:
    """Create or return the global _hook_manager singleton instance."""
    global _cli_hook_manager  # noqa: PLW0603
    if _cli_hook_manager is None:
        _cli_hook_manager = CLIHooksManager()
    _cli_hook_manager.trace.root.setwriter(
        logger.debug if logger.getEffectiveLevel() == logging.DEBUG else None
    )
    _cli_hook_manager.enable_tracing()
    return _cli_hook_manager
```

## kedro.framework.cli.jupyter

A collection of helper functions to integrate with Jupyter/IPython and CLI commands for working with Kedro catalog.

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### \_check_module_importable

```
_check_module_importable(module_name)
```

Source code in `kedro/framework/cli/utils.py`

```
def _check_module_importable(module_name: str) -> None:
    try:
        import_module(module_name)
    except ImportError as exc:
        raise KedroCliError(
            f"Module '{module_name}' not found. Make sure to install required project "
            f"dependencies by running the 'pip install -r requirements.txt' command first."
        ) from exc
```

### \_create_kernel

```
_create_kernel(kernel_name, display_name)
```

Creates an IPython kernel for the kedro project. If one with the same kernel_name exists already it will be replaced.

Installs the default IPython kernel (which points towards `sys.executable`) and customises it to make the launch command load the kedro extension. This is equivalent to the method recommended for creating a custom IPython kernel on the CLI: https://ipython.readthedocs.io/en/stable/install/kernel_install.html.

On linux this creates a directory ~/.local/share/jupyter/kernels/{kernel_name} containing kernel.json, logo-32x32.png, logo-64x64.png and logo-svg.svg. An example kernel.json looks as follows:

{ "argv": [ "/Users/antony_milne/miniconda3/envs/spaceflights/bin/python", "-m", "ipykernel_launcher", "-f", "{connection_file}", "--ext", "kedro.ipython" ], "display_name": "Kedro (spaceflights)", "language": "python", "metadata": { "debugger": false } }

Parameters:

- **`kernel_name`** (`str`) – Name of the kernel to create.
- **`display_name`** (`str`) – Kernel name as it is displayed in the UI.

Returns:

- `str` – String of the path of the created kernel.

Raises:

- `KedroCliError` – When kernel cannot be setup.

Source code in `kedro/framework/cli/jupyter.py`

```
def _create_kernel(kernel_name: str, display_name: str) -> str:
    """Creates an IPython kernel for the kedro project. If one with the same kernel_name
    exists already it will be replaced.

    Installs the default IPython kernel (which points towards `sys.executable`)
    and customises it to make the launch command load the kedro extension.
    This is equivalent to the method recommended for creating a custom IPython kernel
    on the CLI: https://ipython.readthedocs.io/en/stable/install/kernel_install.html.

    On linux this creates a directory ~/.local/share/jupyter/kernels/{kernel_name}
    containing kernel.json, logo-32x32.png, logo-64x64.png and logo-svg.svg. An example kernel.json
    looks as follows:

    {
     "argv": [
      "/Users/antony_milne/miniconda3/envs/spaceflights/bin/python",
      "-m",
      "ipykernel_launcher",
      "-f",
      "{connection_file}",
      "--ext",
      "kedro.ipython"
     ],
     "display_name": "Kedro (spaceflights)",
     "language": "python",
     "metadata": {
      "debugger": false
     }
    }

    Args:
        kernel_name: Name of the kernel to create.
        display_name: Kernel name as it is displayed in the UI.

    Returns:
        String of the path of the created kernel.

    Raises:
        KedroCliError: When kernel cannot be setup.
    """
    # These packages are required by jupyter lab and notebook, which we have already
    # checked are importable, so we don't run _check_module_importable on them.
    from ipykernel.kernelspec import install

    try:
        # Install with user=True rather than system-wide to minimise footprint and
        # ensure that we have permissions to write there. Under the hood this calls
        # jupyter_client.KernelSpecManager.install_kernel_spec, which automatically
        # removes an old kernel spec if it already exists.
        kernel_path = install(
            user=True,
            kernel_name=kernel_name,
            display_name=display_name,
        )

        kernel_json = Path(kernel_path) / "kernel.json"
        kernel_spec = json.loads(kernel_json.read_text(encoding="utf-8"))
        kernel_spec["argv"].extend(["--ext", "kedro.ipython"])
        # indent=1 is to match the default ipykernel style (see
        # ipykernel.write_kernel_spec).
        kernel_json.write_text(json.dumps(kernel_spec, indent=1), encoding="utf-8")

        kedro_ipython_dir = Path(__file__).parents[2] / "ipython"
        shutil.copy(kedro_ipython_dir / "logo-32x32.png", kernel_path)
        shutil.copy(kedro_ipython_dir / "logo-64x64.png", kernel_path)
        shutil.copy(kedro_ipython_dir / "logo-svg.svg", kernel_path)
    except Exception as exc:
        raise KedroCliError(
            f"Cannot setup kedro kernel for Jupyter.\nError: {exc}"
        ) from exc
    return kernel_path
```

### env_option

```
env_option(func_=None, **kwargs)
```

Add `--env` CLI option to a function.

Source code in `kedro/framework/cli/utils.py`

```
def env_option(func_: Any | None = None, **kwargs: Any) -> Any:
    """Add `--env` CLI option to a function."""
    default_args = {"type": str, "default": None, "help": ENV_HELP}
    kwargs = {**default_args, **kwargs}
    opt = click.option("--env", "-e", **kwargs)
    return opt(func_) if func_ else opt
```

### forward_command

```
forward_command(group, name=None, forward_help=False)
```

A command that receives the rest of the command line as 'args'.

Source code in `kedro/framework/cli/utils.py`

```
def forward_command(
    group: Any, name: str | None = None, forward_help: bool = False
) -> Any:
    """A command that receives the rest of the command line as 'args'."""

    def wrapit(func: Any) -> Any:
        func = click.argument("args", nargs=-1, type=click.UNPROCESSED)(func)
        func = command_with_verbosity(
            group,
            name=name,
            context_settings={
                "ignore_unknown_options": True,
                "help_option_names": [] if forward_help else ["-h", "--help"],
            },
        )(func)
        return func

    return wrapit
```

### jupyter

```
jupyter()
```

Open Jupyter Notebook / Lab with project specific variables loaded.

Source code in `kedro/framework/cli/jupyter.py`

```
@jupyter_cli.group()
def jupyter() -> None:
    """Open Jupyter Notebook / Lab with project specific variables loaded."""
```

### jupyter_cli

```
jupyter_cli()
```

Source code in `kedro/framework/cli/jupyter.py`

```
@click.group(name="kedro")
def jupyter_cli() -> None:  # pragma: no cover
    pass
```

### jupyter_lab

```
jupyter_lab(metadata, /, env, args, **kwargs)
```

Open Jupyter Lab with project specific variables loaded.

Source code in `kedro/framework/cli/jupyter.py`

```
@forward_command(jupyter, "lab", forward_help=True)
@env_option
@click.pass_obj  # this will pass the metadata as first argument
def jupyter_lab(
    metadata: ProjectMetadata,
    /,
    env: str,
    args: Any,
    **kwargs: Any,
) -> None:
    """Open Jupyter Lab with project specific variables loaded."""
    _check_module_importable("jupyterlab")
    validate_settings()

    kernel_name = f"kedro_{metadata.package_name}"
    _create_kernel(kernel_name, f"Kedro ({metadata.package_name})")

    if env:
        os.environ["KEDRO_ENV"] = env

    python_call(
        "jupyter",
        ["lab", f"--MultiKernelManager.default_kernel_name={kernel_name}", *list(args)],
    )
```

### jupyter_notebook

```
jupyter_notebook(metadata, /, env, args, **kwargs)
```

Open Jupyter Notebook with project specific variables loaded.

Source code in `kedro/framework/cli/jupyter.py`

```
@forward_command(jupyter, "notebook", forward_help=True)
@env_option
@click.pass_obj  # this will pass the metadata as first argument
def jupyter_notebook(
    metadata: ProjectMetadata,
    /,
    env: str,
    args: Any,
    **kwargs: Any,
) -> None:
    """Open Jupyter Notebook with project specific variables loaded."""
    _check_module_importable("notebook")
    validate_settings()

    kernel_name = f"kedro_{metadata.package_name}"
    _create_kernel(kernel_name, f"Kedro ({metadata.package_name})")

    if env:
        os.environ["KEDRO_ENV"] = env

    python_call(
        "jupyter",
        [
            "notebook",
            f"--MultiKernelManager.default_kernel_name={kernel_name}",
            *list(args),
        ],
    )
```

### python_call

```
python_call(module, arguments, **kwargs)
```

Run a subprocess command that invokes a Python module.

Source code in `kedro/framework/cli/utils.py`

```
def python_call(
    module: str, arguments: Iterable[str], **kwargs: Any
) -> None:  # pragma: no cover
    """Run a subprocess command that invokes a Python module."""
    call([sys.executable, "-m", module, *list(arguments)], **kwargs)
```

### setup

```
setup(metadata, /, args, **kwargs)
```

Initialise the Jupyter Kernel for a kedro project.

Source code in `kedro/framework/cli/jupyter.py`

```
@forward_command(jupyter, "setup", forward_help=True)
@click.pass_obj  # this will pass the metadata as first argument
def setup(metadata: ProjectMetadata, /, args: Any, **kwargs: Any) -> None:
    """Initialise the Jupyter Kernel for a kedro project."""
    _check_module_importable("ipykernel")
    validate_settings()

    kernel_name = f"kedro_{metadata.package_name}"
    kernel_path = _create_kernel(kernel_name, f"Kedro ({metadata.package_name})")
    click.secho(f"\nThe kernel has been created successfully at {kernel_path}")
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

## kedro.framework.cli.pipeline

A collection of CLI commands for working with Kedro pipelines.

### \_SETUP_PY_TEMPLATE

```
_SETUP_PY_TEMPLATE = '# -*- coding: utf-8 -*-\nfrom setuptools import setup, find_packages\n\nsetup(\n    name="{name}",\n    version="{version}",\n    description="Modular pipeline `{name}`",\n    packages=find_packages(),\n    include_package_data=True,\n    install_requires={install_requires},\n)\n'
```

### settings

```
settings = _ProjectSettings()
```

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### PipelineArtifacts

Bases: `NamedTuple`

An ordered collection of source_path, tests_path, config_paths

### ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### \_assert_pkg_name_ok

```
_assert_pkg_name_ok(pkg_name)
```

Check that python package name is in line with PEP8 requirements.

Parameters:

- **`pkg_name`** (`str`) – Candidate Python package name.

Raises:

- `KedroCliError` – If package name violates the requirements.

Source code in `kedro/framework/cli/pipeline.py`

```
def _assert_pkg_name_ok(pkg_name: str) -> None:
    """Check that python package name is in line with PEP8 requirements.

    Args:
        pkg_name: Candidate Python package name.

    Raises:
        KedroCliError: If package name violates the requirements.
    """

    base_message = f"'{pkg_name}' is not a valid Python package name."
    if not re.match(r"^[a-zA-Z_]", pkg_name):
        message = base_message + " It must start with a letter or underscore."
        raise KedroCliError(message)
    if len(pkg_name) < 2:  # noqa: PLR2004
        message = base_message + " It must be at least 2 characters long."
        raise KedroCliError(message)
    if not re.match(r"^\w+$", pkg_name[1:]):
        message = (
            base_message + " It must contain only letters, digits, and/or underscores."
        )
        raise KedroCliError(message)
```

### \_check_pipeline_name

```
_check_pipeline_name(ctx, param, value)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _check_pipeline_name(ctx: click.Context, param: Any, value: str) -> str:
    if value:
        _assert_pkg_name_ok(value)
    return value
```

### \_clean_pycache

```
_clean_pycache(path)
```

Recursively clean all **pycache** folders from `path`.

Parameters:

- **`path`** (`Path`) – Existing local directory to clean pycache folders from.

Source code in `kedro/framework/cli/utils.py`

```
def _clean_pycache(path: Path) -> None:
    """Recursively clean all __pycache__ folders from `path`.

    Args:
        path: Existing local directory to clean __pycache__ folders from.
    """
    to_delete = [each.resolve() for each in path.rglob("__pycache__")]

    for each in to_delete:
        shutil.rmtree(each, ignore_errors=True)
```

### \_copy_pipeline_configs

```
_copy_pipeline_configs(result_path, conf_path, skip_config, env)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _copy_pipeline_configs(
    result_path: Path, conf_path: Path, skip_config: bool, env: str
) -> None:
    config_source = result_path / "config"
    try:
        if not skip_config:
            config_target = conf_path / env
            _sync_dirs(config_source, config_target)
    finally:
        shutil.rmtree(config_source)
```

### \_copy_pipeline_tests

```
_copy_pipeline_tests(pipeline_name, result_path, project_root)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _copy_pipeline_tests(
    pipeline_name: str, result_path: Path, project_root: Path
) -> None:
    tests_source = result_path / "tests"
    tests_target = project_root.parent / "tests" / "pipelines" / pipeline_name
    try:
        _sync_dirs(tests_source, tests_target)
    finally:
        shutil.rmtree(tests_source)
```

### \_create_pipeline

```
_create_pipeline(name, template_path, output_dir)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _create_pipeline(name: str, template_path: Path, output_dir: Path) -> Path:
    from cookiecutter.main import cookiecutter

    cookie_context = {"pipeline_name": name, "kedro_version": kedro.__version__}

    click.echo(f"Creating the pipeline '{name}': ", nl=False)

    try:
        cookiecutter_result = cookiecutter(
            str(template_path),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=cookie_context,
        )
    except Exception as exc:
        click.secho("FAILED", fg="red")
        cls = exc.__class__
        raise KedroCliError(f"{cls.__module__}.{cls.__qualname__}: {exc}") from exc

    click.secho("OK", fg="green")
    result_path = Path(cookiecutter_result)
    message = indent(f"Location: '{result_path.resolve()}'", " " * 2)
    click.secho(message, bold=True)

    _clean_pycache(result_path)

    return result_path
```

### \_delete_artifacts

```
_delete_artifacts(*artifacts)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _delete_artifacts(*artifacts: Path) -> None:
    for artifact in artifacts:
        click.echo(f"Deleting '{artifact}': ", nl=False)
        try:
            if artifact.is_dir():
                shutil.rmtree(artifact)
            else:
                artifact.unlink()
        except Exception as exc:
            click.secho("FAILED", fg="red")
            cls = exc.__class__
            raise KedroCliError(f"{cls.__module__}.{cls.__qualname__}: {exc}") from exc
        click.secho("OK", fg="green")
```

### \_echo_deletion_warning

```
_echo_deletion_warning(message, **paths)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _echo_deletion_warning(message: str, **paths: list[Path]) -> None:
    paths = {key: values for key, values in paths.items() if values}

    if paths:
        click.secho(message, bold=True)

    for key, values in paths.items():
        click.echo(f"\n{key.capitalize()}:")
        paths_str = "\n".join(str(value) for value in values)
        click.echo(indent(paths_str, " " * 2))
```

### \_ensure_pipelines_init_file

```
_ensure_pipelines_init_file(pipelines_dir)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _ensure_pipelines_init_file(pipelines_dir: Path) -> None:
    # Ensure the pipelines directory exists
    pipelines_dir.mkdir(exist_ok=True, parents=True)

    # Create __init__.py if it doesn't exist
    init_file = pipelines_dir / "__init__.py"
    if not init_file.is_file():
        click.echo(f"Creating '{init_file}': ", nl=False)
        init_file.touch()
        click.secho("OK", fg="green")
```

### \_get_artifacts_to_package

```
_get_artifacts_to_package(project_metadata, module_path, env)
```

From existing project, returns in order: source_path, tests_path, config_paths

Source code in `kedro/framework/cli/pipeline.py`

```
def _get_artifacts_to_package(
    project_metadata: ProjectMetadata, module_path: str, env: str
) -> tuple[Path, Path, Path]:
    """From existing project, returns in order: source_path, tests_path, config_paths"""
    package_dir = project_metadata.source_dir / project_metadata.package_name
    project_root = project_metadata.project_path
    project_conf_path = project_metadata.project_path / settings.CONF_SOURCE
    artifacts = (
        Path(package_dir, *module_path.split(".")),
        Path(project_root, "tests", *module_path.split(".")),
        project_conf_path / env,
    )
    return artifacts
```

### \_get_pipeline_artifacts

```
_get_pipeline_artifacts(project_metadata, pipeline_name, env)
```

Source code in `kedro/framework/cli/pipeline.py`

```
def _get_pipeline_artifacts(
    project_metadata: ProjectMetadata, pipeline_name: str, env: str
) -> PipelineArtifacts:
    artifacts = _get_artifacts_to_package(
        project_metadata, f"pipelines.{pipeline_name}", env
    )
    return PipelineArtifacts(*artifacts)
```

### \_sync_dirs

```
_sync_dirs(source, target, prefix='', overwrite=False)
```

Recursively copies `source` directory (or file) into `target` directory without overwriting any existing files/directories in the target using the following rules:

1. Skip any files/directories which names match with files in target, unless overwrite=True.
1. Copy all files from source to target.
1. Recursively copy all directories from source to target.

Parameters:

- **`source`** (`Path`) – A local directory to copy from, must exist.
- **`target`** (`Path`) – A local directory to copy to, will be created if doesn't exist yet.
- **`prefix`** (`str`, default: `''` ) – Prefix for CLI message indentation.

Source code in `kedro/framework/cli/pipeline.py`

```
def _sync_dirs(
    source: Path, target: Path, prefix: str = "", overwrite: bool = False
) -> None:
    """Recursively copies `source` directory (or file) into `target` directory without
    overwriting any existing files/directories in the target using the following
    rules:
        1) Skip any files/directories which names match with files in target,
        unless overwrite=True.
        2) Copy all files from source to target.
        3) Recursively copy all directories from source to target.

    Args:
        source: A local directory to copy from, must exist.
        target: A local directory to copy to, will be created if doesn't exist yet.
        prefix: Prefix for CLI message indentation.
    """

    existing = list(target.iterdir()) if target.is_dir() else []
    existing_files = {f.name for f in existing if f.is_file()}
    existing_folders = {f.name for f in existing if f.is_dir()}

    if source.is_dir():
        content = list(source.iterdir())
    elif source.is_file():
        content = [source]
    else:
        # nothing to copy
        content = []  # pragma: no cover

    for source_path in content:
        source_name = source_path.name
        target_path = target / source_name
        click.echo(indent(f"Creating '{target_path}': ", prefix), nl=False)

        if (  # rule #1
            not overwrite
            and source_name in existing_files
            or source_path.is_file()
            and source_name in existing_folders
        ):
            click.secho("SKIPPED (already exists)", fg="yellow")
        elif source_path.is_file():  # rule #2
            try:
                target.mkdir(exist_ok=True, parents=True)
                shutil.copyfile(str(source_path), str(target_path))
            except Exception:
                click.secho("FAILED", fg="red")
                raise
            click.secho("OK", fg="green")
        else:  # source_path is a directory, rule #3
            click.echo()
            new_prefix = (prefix or "") + " " * 2
            _sync_dirs(source_path, target_path, prefix=new_prefix)
```

### command_with_verbosity

```
command_with_verbosity(group, *args, **kwargs)
```

Custom command decorator with verbose flag added.

Source code in `kedro/framework/cli/utils.py`

```
def command_with_verbosity(group: click.core.Group, *args: Any, **kwargs: Any) -> Any:
    """Custom command decorator with verbose flag added."""

    def decorator(func: Any) -> Any:
        func = _click_verbose(func)
        func = group.command(*args, **kwargs)(func)
        return func

    return decorator
```

### create_pipeline

```
create_pipeline(metadata, /, name, template_path, skip_config, env, **kwargs)
```

Create a new modular pipeline by providing a name.

Source code in `kedro/framework/cli/pipeline.py`

```
@command_with_verbosity(pipeline, "create")
@click.argument("name", nargs=1, callback=_check_pipeline_name)
@click.option(
    "--skip-config",
    is_flag=True,
    help="Skip creation of config files for the new pipeline(s).",
)
@click.option(
    "template_path",
    "-t",
    "--template",
    type=click.Path(file_okay=False, dir_okay=True, exists=True, path_type=Path),
    help="Path to cookiecutter template to use for pipeline(s). Will override any local templates.",
)
@env_option(help="Environment to create pipeline configuration in. Defaults to `base`.")
@click.pass_obj  # this will pass the metadata as first argument
def create_pipeline(
    metadata: ProjectMetadata,
    /,
    name: str,
    template_path: Path,
    skip_config: bool,
    env: str,
    **kwargs: Any,
) -> None:
    """Create a new modular pipeline by providing a name."""
    package_dir = metadata.source_dir / metadata.package_name
    project_root = metadata.project_path / metadata.project_name
    conf_source = settings.CONF_SOURCE
    project_conf_path = metadata.project_path / conf_source
    base_env = settings.CONFIG_LOADER_ARGS.get("base_env", "base")
    env = env or base_env
    if not skip_config and not (project_conf_path / env).exists():
        raise KedroCliError(
            f"Unable to locate environment '{env}'. "
            f"Make sure it exists in the project configuration."
        )

    # Precedence for template_path is: command line > project templates/pipeline dir > global default
    # If passed on the CLI, click will verify that the path exists so no need to check again
    if template_path is None:
        # No path provided on the CLI, try `PROJECT_PATH/templates/pipeline`
        template_path = Path(metadata.project_path / "templates" / "pipeline")

        if not template_path.exists():
            # and if that folder doesn't exist fall back to the global default
            template_path = Path(kedro.__file__).parent / "templates" / "pipeline"

    click.secho(f"Using pipeline template at: '{template_path}'")

    # Ensure pipelines directory has __init__.py
    pipelines_dir = package_dir / "pipelines"
    _ensure_pipelines_init_file(pipelines_dir)

    result_path = _create_pipeline(name, template_path, pipelines_dir)
    _copy_pipeline_tests(name, result_path, project_root)
    _copy_pipeline_configs(result_path, project_conf_path, skip_config, env=env)
    click.secho(f"\nPipeline '{name}' was successfully created.\n", fg="green")
```

### delete_pipeline

```
delete_pipeline(metadata, /, name, env, yes, **kwargs)
```

Delete a modular pipeline by providing a name.

Source code in `kedro/framework/cli/pipeline.py`

```
@command_with_verbosity(pipeline, "delete")
@click.argument("name", nargs=1, callback=_check_pipeline_name)
@env_option(
    help="Environment to delete pipeline configuration from. Defaults to 'base'."
)
@click.option(
    "-y", "--yes", is_flag=True, help="Confirm deletion of pipeline non-interactively."
)
@click.pass_obj  # this will pass the metadata as first argument
def delete_pipeline(
    metadata: ProjectMetadata, /, name: str, env: str, yes: bool, **kwargs: Any
) -> None:
    """Delete a modular pipeline by providing a name."""
    package_dir = metadata.source_dir / metadata.package_name
    conf_source = settings.CONF_SOURCE
    project_conf_path = metadata.project_path / conf_source
    base_env = settings.CONFIG_LOADER_ARGS.get("base_env", "base")
    env = env or base_env
    if not (project_conf_path / env).exists():
        raise KedroCliError(
            f"Unable to locate environment '{env}'. "
            f"Make sure it exists in the project configuration."
        )

    pipeline_artifacts = _get_pipeline_artifacts(metadata, pipeline_name=name, env=env)

    files_to_delete = [
        pipeline_artifacts.pipeline_conf / filepath
        for confdir in ("parameters", "catalog")
        # Since we remove nesting in 'parameters' and 'catalog' folders,
        # we want to also del the old project's structure for backward compatibility
        for filepath in (Path(f"{confdir}_{name}.yml"), Path(confdir) / f"{name}.yml")
        if (pipeline_artifacts.pipeline_conf / filepath).is_file()
    ]

    dirs_to_delete = [
        path
        for path in (pipeline_artifacts.pipeline_dir, pipeline_artifacts.pipeline_tests)
        if path.is_dir()
    ]

    if not files_to_delete and not dirs_to_delete:
        raise KedroCliError(f"Pipeline '{name}' not found.")

    if not yes:
        _echo_deletion_warning(
            "The following paths will be removed:",
            directories=dirs_to_delete,
            files=files_to_delete,
        )
        click.echo()
        yes = click.confirm(f"Are you sure you want to delete pipeline '{name}'?")
        click.echo()

    if not yes:
        raise KedroCliError("Deletion aborted!")

    _delete_artifacts(*files_to_delete, *dirs_to_delete)
    click.secho(f"\nPipeline '{name}' was successfully deleted.", fg="green")
    click.secho(
        f"\nIf you added the pipeline '{name}' to 'register_pipelines()' in"
        f""" '{package_dir / "pipeline_registry.py"}', you will need to remove it.""",
        fg="yellow",
    )
```

### env_option

```
env_option(func_=None, **kwargs)
```

Add `--env` CLI option to a function.

Source code in `kedro/framework/cli/utils.py`

```
def env_option(func_: Any | None = None, **kwargs: Any) -> Any:
    """Add `--env` CLI option to a function."""
    default_args = {"type": str, "default": None, "help": ENV_HELP}
    kwargs = {**default_args, **kwargs}
    opt = click.option("--env", "-e", **kwargs)
    return opt(func_) if func_ else opt
```

### pipeline

```
pipeline()
```

Commands for working with pipelines.

Source code in `kedro/framework/cli/pipeline.py`

```
@pipeline_cli.group()
def pipeline() -> None:
    """Commands for working with pipelines."""
```

### pipeline_cli

```
pipeline_cli()
```

Source code in `kedro/framework/cli/pipeline.py`

```
@click.group(name="kedro")
def pipeline_cli() -> None:  # pragma: no cover
    pass
```

## kedro.framework.cli.project

A collection of CLI commands for working with Kedro project.

### ASYNC_ARG_HELP

```
ASYNC_ARG_HELP = 'Load and save node inputs and outputs asynchronously\nwith threads. If not specified, load and save datasets synchronously.'
```

### CONFIG_FILE_HELP

```
CONFIG_FILE_HELP = 'Specify a YAML configuration file to load the run\ncommand arguments from. If command line arguments are provided, they will\noverride the loaded ones.'
```

### CONF_SOURCE_HELP

```
CONF_SOURCE_HELP = 'Path of a directory where project configuration is stored.'
```

### FROM_INPUTS_HELP

```
FROM_INPUTS_HELP = 'A list of dataset names which should be used as a starting point.'
```

### FROM_NODES_HELP

```
FROM_NODES_HELP = 'A list of node names which should be used as a starting point.'
```

### INPUT_FILE_HELP

```
INPUT_FILE_HELP = 'Name of the requirements file to compile.'
```

### LINT_CHECK_ONLY_HELP

```
LINT_CHECK_ONLY_HELP = 'Check the files for style guide violations, unsorted /\nunformatted imports, and unblackened Python code without modifying the files.'
```

### LOAD_VERSION_HELP

```
LOAD_VERSION_HELP = 'Specify a particular dataset version (timestamp) for loading.'
```

### NAMESPACES_ARG_HELP

```
NAMESPACES_ARG_HELP = 'Run only node namespaces with specified names.'
```

### NODE_ARG_HELP

```
NODE_ARG_HELP = 'Run only nodes with specified names.'
```

### NO_DEPENDENCY_MESSAGE

```
NO_DEPENDENCY_MESSAGE = "{module} is not installed. Please make sure {module} is in\nrequirements.txt and run 'pip install -r requirements.txt'."
```

### ONLY_MISSING_OUTPUTS_HELP

```
ONLY_MISSING_OUTPUTS_HELP = 'Run only nodes with missing outputs.\nIf all outputs of a node exist and are persisted, skip the node execution.'
```

### OPEN_ARG_HELP

```
OPEN_ARG_HELP = 'Open the documentation in your default browser after building.'
```

### OUTPUT_FILE_HELP

```
OUTPUT_FILE_HELP = 'Name of the file where compiled requirements should be stored.'
```

### PARAMS_ARG_HELP

```
PARAMS_ARG_HELP = "Specify extra parameters that you want to pass\nto the context initialiser. Items must be separated by comma, keys - by colon or equals sign,\nexample: param1=value1,param2=value2. Each parameter is split by the first comma,\nso parameter values are allowed to contain colons, parameter keys are not.\nTo pass a nested dictionary as parameter, separate keys by '.', example:\nparam_group.param1:value1."
```

### PIPELINES_ARG_HELP

```
PIPELINES_ARG_HELP = "Comma-separated names of registered pipelines to run.\nExample: --pipelines data_engineering,feature_engineering\nIf not set, the '__default__' pipeline is run."
```

### PIPELINE_ARG_HELP

```
PIPELINE_ARG_HELP = "Name of the registered pipeline to run.\nIf not set, the '__default__' pipeline is run."
```

### RUNNER_ARG_HELP

```
RUNNER_ARG_HELP = "Specify a runner that you want to run the pipeline with.\nAvailable runners: 'SequentialRunner', 'ParallelRunner' and 'ThreadRunner'."
```

### TAG_ARG_HELP

```
TAG_ARG_HELP = 'Construct the pipeline using only nodes which have this tag\nattached. Option can be used multiple times, what results in a\npipeline constructed from nodes having any of those tags.'
```

### TO_NODES_HELP

```
TO_NODES_HELP = 'A list of node names which should be used as an end point.'
```

### TO_OUTPUTS_HELP

```
TO_OUTPUTS_HELP = 'A list of dataset names which should be used as an end point.'
```

### settings

```
settings = _ProjectSettings()
```

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

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

### ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### \_check_module_importable

```
_check_module_importable(module_name)
```

Source code in `kedro/framework/cli/utils.py`

```
def _check_module_importable(module_name: str) -> None:
    try:
        import_module(module_name)
    except ImportError as exc:
        raise KedroCliError(
            f"Module '{module_name}' not found. Make sure to install required project "
            f"dependencies by running the 'pip install -r requirements.txt' command first."
        ) from exc
```

### \_config_file_callback

```
_config_file_callback(ctx, param, value)
```

CLI callback that replaces command line options with values specified in a config file. If command line options are passed, they override config file values.

Source code in `kedro/framework/cli/utils.py`

```
@typing.no_type_check
def _config_file_callback(ctx: click.Context, param: Any, value: Any) -> Any:
    """CLI callback that replaces command line options
    with values specified in a config file. If command line
    options are passed, they override config file values.
    """

    ctx.default_map = ctx.default_map or {}
    section = ctx.info_name

    if value:
        config = OmegaConf.to_container(OmegaConf.load(value))[section]
        for key, value in config.items():  # noqa: PLR1704
            _validate_config_file(key)
        ctx.default_map.update(config)

    return value
```

### \_split_load_versions

```
_split_load_versions(ctx, param, value)
```

Split and format the string coming from the --load-versions flag in kedro run, e.g.: "dataset1:time1,dataset2:time2" -> {"dataset1": "time1", "dataset2": "time2"}

Parameters:

- **`value`** (`str`) – the string with the contents of the --load-versions flag.

Returns:

- `dict[str, str]` – A dictionary with the formatted load versions data.

Source code in `kedro/framework/cli/utils.py`

```
def _split_load_versions(ctx: click.Context, param: Any, value: str) -> dict[str, str]:
    """Split and format the string coming from the --load-versions
    flag in kedro run, e.g.:
    "dataset1:time1,dataset2:time2" -> {"dataset1": "time1", "dataset2": "time2"}

    Args:
        value: the string with the contents of the --load-versions flag.

    Returns:
        A dictionary with the formatted load versions data.
    """
    if not value:
        return {}

    lv_tuple = tuple(chain.from_iterable(value.split(",") for value in [value]))

    load_versions_dict = {}
    for load_version in lv_tuple:
        load_version = load_version.strip()  # noqa: PLW2901
        load_version_list = load_version.split(":", 1)
        if len(load_version_list) != 2:  # noqa: PLR2004
            raise KedroCliError(
                f"Expected the form of 'load_versions' to be "
                f"'dataset_name:YYYY-MM-DDThh.mm.ss.sssZ',"
                f"found {load_version} instead"
            )
        load_versions_dict[load_version_list[0]] = load_version_list[1]

    return load_versions_dict
```

### \_split_params

```
_split_params(ctx, param, value)
```

Source code in `kedro/framework/cli/utils.py`

```
def _split_params(ctx: click.Context, param: Any, value: Any) -> Any:
    if isinstance(value, dict):
        return value
    dot_list = []
    for item in split_string(ctx, param, value):
        equals_idx = item.find("=")
        if equals_idx == -1:
            # If an equals sign is not found, fail with an error message.
            ctx.fail(
                f"Invalid format of `{param.name}` option: "
                f"Item `{item}` must contain a key and a value separated by `=`."
            )
        # Split the item into key and value
        key, _, val = item.partition("=")
        key = key.strip()
        if not key:
            # If the key is empty after stripping whitespace, fail with an error message.
            ctx.fail(
                f"Invalid format of `{param.name}` option: Parameter key "
                f"cannot be an empty string."
            )
        # Add "key=value" pair to dot_list.
        dot_list.append(f"{key}={val}")

    conf = OmegaConf.from_dotlist(dot_list)
    return OmegaConf.to_container(conf)
```

### call

```
call(cmd, **kwargs)
```

Run a subprocess command and raise if it fails.

Parameters:

- **`cmd`** (`list[str]`) – List of command parts.
- **`**kwargs`** (`Any`, default: `{}` ) – Optional keyword arguments passed to subprocess.run.

Raises:

- `Exit` – If subprocess.run returns non-zero code.

Source code in `kedro/framework/cli/utils.py`

```
def call(cmd: list[str], **kwargs: Any) -> None:  # pragma: no cover
    """Run a subprocess command and raise if it fails.

    Args:
        cmd: List of command parts.
        **kwargs: Optional keyword arguments passed to `subprocess.run`.

    Raises:
        click.exceptions.Exit: If `subprocess.run` returns non-zero code.
    """
    click.echo(shlex.join(cmd))
    code = subprocess.run(cmd, **kwargs).returncode  # noqa: PLW1510, S603
    if code:
        raise click.exceptions.Exit(code=code)
```

### env_option

```
env_option(func_=None, **kwargs)
```

Add `--env` CLI option to a function.

Source code in `kedro/framework/cli/utils.py`

```
def env_option(func_: Any | None = None, **kwargs: Any) -> Any:
    """Add `--env` CLI option to a function."""
    default_args = {"type": str, "default": None, "help": ENV_HELP}
    kwargs = {**default_args, **kwargs}
    opt = click.option("--env", "-e", **kwargs)
    return opt(func_) if func_ else opt
```

### forward_command

```
forward_command(group, name=None, forward_help=False)
```

A command that receives the rest of the command line as 'args'.

Source code in `kedro/framework/cli/utils.py`

```
def forward_command(
    group: Any, name: str | None = None, forward_help: bool = False
) -> Any:
    """A command that receives the rest of the command line as 'args'."""

    def wrapit(func: Any) -> Any:
        func = click.argument("args", nargs=-1, type=click.UNPROCESSED)(func)
        func = command_with_verbosity(
            group,
            name=name,
            context_settings={
                "ignore_unknown_options": True,
                "help_option_names": [] if forward_help else ["-h", "--help"],
            },
        )(func)
        return func

    return wrapit
```

### ipython

```
ipython(metadata, /, env, args, **kwargs)
```

Open IPython with project specific variables loaded.

Makes the following variables available in your IPython or Jupyter session:

- `catalog`: catalog instance that contains all defined datasets; this is a shortcut for `context.catalog`.
- `context`: Kedro project context that provides access to Kedro's library components.
- `pipelines`: Pipelines defined in your pipeline registry.
- `session`: Kedro session that orchestrates a pipeline run.

To reload these variables (e.g. if you updated `catalog.yml`) use the `%reload_kedro` line magic, which can also be used to see the error message if any of the variables above are undefined.

Source code in `kedro/framework/cli/project.py`

```
@forward_command(project_group, forward_help=True)
@env_option
@click.pass_obj  # this will pass the metadata as first argument
def ipython(metadata: ProjectMetadata, /, env: str, args: Any, **kwargs: Any) -> None:
    """Open IPython with project specific variables loaded.\n

    Makes the following variables available in your IPython or Jupyter session:\n

    - `catalog`: catalog instance that contains all defined datasets; this is a shortcut for `context.catalog`.\n
    - `context`: Kedro project context that provides access to Kedro's library components.\n
    - `pipelines`: Pipelines defined in your pipeline registry.\n
    - `session`: Kedro session that orchestrates a pipeline run.\n

    To reload these variables (e.g. if you updated `catalog.yml`) use the `%reload_kedro` line magic,
    which can also be used to see the error message if any of the variables above are undefined.
    """
    _check_module_importable("IPython")

    if env:
        os.environ["KEDRO_ENV"] = env
    call(["ipython", "--ext", "kedro.ipython", *list(args)])
```

### load_obj

```
load_obj(obj_path, default_obj_path='')
```

Extract an object from a given path.

Parameters:

- **`obj_path`** (`str`) – Path to an object to be extracted, including the object name.
- **`default_obj_path`** (`str`, default: `''` ) – Default object path.

Returns:

- `Any` – Extracted object.

Raises:

- `AttributeError` – When the object does not have the given named attribute.

Source code in `kedro/utils.py`

```
def load_obj(obj_path: str, default_obj_path: str = "") -> Any:
    """Extract an object from a given path.

    Args:
        obj_path: Path to an object to be extracted, including the object name.
        default_obj_path: Default object path.

    Returns:
        Extracted object.

    Raises:
        AttributeError: When the object does not have the given named attribute.

    """
    obj_path_list = obj_path.rsplit(".", 1)
    obj_path = obj_path_list.pop(0) if len(obj_path_list) > 1 else default_obj_path
    obj_name = obj_path_list[0]
    module_obj = importlib.import_module(obj_path)
    return getattr(module_obj, obj_name)
```

### package

```
package(metadata)
```

Package the Kedro project as a Python wheel and export the configuration.

This command builds a `.whl` file for the project and saves it to the `dist/` directory. It also packages the project's configuration (excluding any `local/*.yml` files) into a separate `tar.gz` archive for deployment or sharing.

Both artifacts will appear in the `dist/` folder, unless an older project layout is detected.

Source code in `kedro/framework/cli/project.py`

```
@project_group.command()
@click.pass_obj  # this will pass the metadata as first argument
def package(metadata: ProjectMetadata) -> None:
    """Package the Kedro project as a Python wheel and export the configuration.\n

    This command builds a `.whl` file for the project and saves it to the `dist/` directory.
    It also packages the project's configuration (excluding any `local/*.yml` files)
    into a separate `tar.gz` archive for deployment or sharing.\n

    Both artifacts will appear in the `dist/` folder, unless an older project layout is detected.
    """
    # Even if the user decides for the older setup.py on purpose,
    # pyproject.toml is needed for Kedro metadata
    if (metadata.project_path / "pyproject.toml").is_file():
        metadata_dir = metadata.project_path
        destination_dir = "dist"
    else:
        # Assume it's an old Kedro project, packaging metadata was under src
        # (could be pyproject.toml or setup.py, it's not important)
        metadata_dir = metadata.source_dir
        destination_dir = "../dist"

    call(
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            destination_dir,
        ],
        cwd=str(metadata_dir),
    )

    directory = (
        str(Path(settings.CONF_SOURCE).parent)
        if settings.CONF_SOURCE != "conf"
        else metadata.project_path
    )
    call(
        [
            "tar",
            "--exclude=local/*.yml",
            "-czf",
            f"dist/conf-{metadata.package_name}.tar.gz",
            f"--directory={directory}",
            str(Path(settings.CONF_SOURCE).stem),
        ]
    )
```

### project_group

```
project_group()
```

Source code in `kedro/framework/cli/project.py`

```
@click.group(name="kedro")
def project_group() -> None:  # pragma: no cover
    pass
```

### run

```
run(tags, env, runner, is_async, node_names, to_nodes, from_nodes, from_inputs, to_outputs, load_versions, pipeline, pipelines, config, conf_source, params, namespaces, only_missing_outputs)
```

Run the pipeline.

Source code in `kedro/framework/cli/project.py`

```
@project_group.command()
@click.option(
    "--from-inputs",
    type=str,
    default="",
    help=FROM_INPUTS_HELP,
    callback=split_string,
)
@click.option(
    "--to-outputs",
    type=str,
    default="",
    help=TO_OUTPUTS_HELP,
    callback=split_string,
)
@click.option(
    "--from-nodes",
    type=str,
    default="",
    help=FROM_NODES_HELP,
    callback=split_node_names,
)
@click.option(
    "--to-nodes", type=str, default="", help=TO_NODES_HELP, callback=split_node_names
)
@click.option(
    "--nodes",
    "-n",
    "node_names",
    type=str,
    default="",
    help=NODE_ARG_HELP,
    callback=split_node_names,
)
@click.option("--runner", "-r", type=str, default=None, help=RUNNER_ARG_HELP)
@click.option("--async", "is_async", is_flag=True, help=ASYNC_ARG_HELP)
@env_option
@click.option(
    "--tags",
    "-t",
    type=str,
    default="",
    help=TAG_ARG_HELP,
    callback=split_string,
)
@click.option(
    "--load-versions",
    "-lv",
    type=str,
    default="",
    help=LOAD_VERSION_HELP,
    callback=_split_load_versions,
)
@click.option("--pipeline", "-p", type=str, default=None, help=PIPELINE_ARG_HELP)
@click.option(
    "--pipelines", type=str, default="", help=PIPELINES_ARG_HELP, callback=split_string
)
@click.option(
    "--namespaces",
    "-ns",
    type=str,
    default="",
    help=NAMESPACES_ARG_HELP,
    callback=split_node_names,
)
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, dir_okay=False, resolve_path=True),
    help=CONFIG_FILE_HELP,
    callback=_config_file_callback,
)
@click.option(
    "--conf-source",
    callback=validate_conf_source,
    help=CONF_SOURCE_HELP,
)
@click.option(
    "--params",
    type=click.UNPROCESSED,
    default="",
    help=PARAMS_ARG_HELP,
    callback=_split_params,
)
@click.option(
    "--only-missing-outputs",
    is_flag=True,
    help=ONLY_MISSING_OUTPUTS_HELP,
)
def run(  # noqa: PLR0913
    tags: str,
    env: str,
    runner: str,
    is_async: bool,
    node_names: str,
    to_nodes: str,
    from_nodes: str,
    from_inputs: str,
    to_outputs: str,
    load_versions: dict[str, str] | None,
    pipeline: str,
    pipelines: list[str],
    config: str,
    conf_source: str,
    params: dict[str, Any],
    namespaces: str,
    only_missing_outputs: bool,
) -> dict[str, Any]:
    """Run the pipeline."""

    if pipeline and pipelines:
        raise KedroCliError(
            "Options '--pipeline' and '--pipelines' cannot be used together"
        )

    pipelines_to_run = list(set(pipelines)) if pipelines else None

    runner_obj = load_obj(runner or "SequentialRunner", "kedro.runner")
    tuple_tags = tuple(tags)
    tuple_node_names = tuple(node_names)

    with KedroSession.create(
        env=env, conf_source=conf_source, runtime_params=params
    ) as session:
        return session.run(
            tags=tuple_tags,
            runner=runner_obj(is_async=is_async),
            node_names=tuple_node_names,
            from_nodes=from_nodes,
            to_nodes=to_nodes,
            from_inputs=from_inputs,
            to_outputs=to_outputs,
            load_versions=load_versions,
            pipeline_name=pipeline,
            pipeline_names=pipelines_to_run,
            namespaces=namespaces,
            only_missing_outputs=only_missing_outputs,
        )
```

### split_node_names

```
split_node_names(ctx, param, to_split)
```

Split string by comma, ignoring commas enclosed by square parentheses. This avoids splitting the string of nodes names on commas included in default node names, which have the pattern ([,...]) -> [,...])

Note

- `to_split` will have such commas if and only if it includes a default node name. User-defined node names cannot include commas or square brackets.
- This function will no longer be necessary from Kedro 0.19.\*, in which default node names will no longer contain commas

Parameters:

- **`to_split`** (`str`) – the string to split safely

Returns:

- `list[str]` – A list containing the result of safe-splitting the string.

Source code in `kedro/framework/cli/utils.py`

```
def split_node_names(ctx: click.Context, param: Any, to_split: str) -> list[str]:
    """Split string by comma, ignoring commas enclosed by square parentheses.
    This avoids splitting the string of nodes names on commas included in
    default node names, which have the pattern
    <function_name>([<input_name>,...]) -> [<output_name>,...])

    Note:
        - `to_split` will have such commas if and only if it includes a
        default node name. User-defined node names cannot include commas
        or square brackets.
        - This function will no longer be necessary from Kedro 0.19.*,
        in which default node names will no longer contain commas

    Args:
        to_split: the string to split safely

    Returns:
        A list containing the result of safe-splitting the string.
    """
    result = []
    argument, match_state = "", 0
    for char in to_split + ",":
        if char == "[":
            match_state += 1
        elif char == "]":
            match_state -= 1
        if char == "," and match_state == 0 and argument:
            argument = argument.strip()
            result.append(argument)
            argument = ""
        else:
            argument += char
    return result
```

### split_string

```
split_string(ctx, param, value)
```

Split string by comma.

Source code in `kedro/framework/cli/utils.py`

```
def split_string(ctx: click.Context, param: Any, value: str) -> list[str]:
    """Split string by comma."""
    return [item.strip() for item in value.split(",") if item.strip()]
```

### validate_conf_source

```
validate_conf_source(ctx, param, value)
```

Validate the conf_source, only checking existence for local paths.

Source code in `kedro/framework/cli/utils.py`

```
def validate_conf_source(ctx: click.Context, param: Any, value: str) -> str | None:
    """Validate the conf_source, only checking existence for local paths."""
    if not value:
        return None

    # Check for remote URLs (except file://)
    if "://" in value and not value.startswith("file://"):
        return value

    # For local paths
    try:
        path = Path(value)
        if not path.exists():
            raise click.BadParameter(f"Path '{value}' does not exist.")
        return str(path.resolve())
    except click.BadParameter:
        # Re-raise Click exceptions
        raise
    except Exception as exc:
        # Wrap other exceptions
        raise click.BadParameter(f"Invalid path: {value}. Error: {exc!s}")
```

## kedro.framework.cli.registry

A collection of CLI commands for working with registered Kedro pipelines.

### pipelines

```
pipelines = _ProjectPipelines()
```

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### ProjectMetadata

Bases: `NamedTuple`

Structure holding project metadata derived from `pyproject.toml`

### command_with_verbosity

```
command_with_verbosity(group, *args, **kwargs)
```

Custom command decorator with verbose flag added.

Source code in `kedro/framework/cli/utils.py`

```
def command_with_verbosity(group: click.core.Group, *args: Any, **kwargs: Any) -> Any:
    """Custom command decorator with verbose flag added."""

    def decorator(func: Any) -> Any:
        func = _click_verbose(func)
        func = group.command(*args, **kwargs)(func)
        return func

    return decorator
```

### describe_registered_pipeline

```
describe_registered_pipeline(metadata, /, name, **kwargs)
```

Describe a registered pipeline by providing a pipeline name. Defaults to the `__default__` pipeline.

Source code in `kedro/framework/cli/registry.py`

```
@command_with_verbosity(registry, "describe")
@click.argument("name", nargs=1, default="__default__")
@click.pass_obj
def describe_registered_pipeline(
    metadata: ProjectMetadata, /, name: str, **kwargs: Any
) -> None:
    """Describe a registered pipeline by providing a pipeline name.
    Defaults to the `__default__` pipeline.
    """
    pipeline_obj = pipelines.get(name)
    if not pipeline_obj:
        all_pipeline_names = pipelines.keys()
        existing_pipelines = ", ".join(sorted(all_pipeline_names))
        raise KedroCliError(
            f"'{name}' pipeline not found. Existing pipelines: [{existing_pipelines}]"
        )

    nodes = []
    for node in pipeline_obj.nodes:
        nodes.append(f"{node.name} ({node._func_name})")
    result = {"Nodes": nodes}

    click.echo(yaml.dump(result))
```

### list_registered_pipelines

```
list_registered_pipelines()
```

List all pipelines defined in your pipeline_registry.py file.

Source code in `kedro/framework/cli/registry.py`

```
@registry.command("list")
def list_registered_pipelines() -> None:
    """List all pipelines defined in your pipeline_registry.py file."""
    click.echo(yaml.dump(sorted(pipelines)))
```

### registry

```
registry()
```

Commands for working with registered pipelines.

Source code in `kedro/framework/cli/registry.py`

```
@registry_cli.group()
def registry() -> None:
    """Commands for working with registered pipelines."""
```

### registry_cli

```
registry_cli()
```

Source code in `kedro/framework/cli/registry.py`

```
@click.group(name="kedro")
def registry_cli() -> None:  # pragma: no cover
    pass
```

## kedro.framework.cli.starters

kedro is a CLI for managing Kedro projects.

This module implements commands available from the kedro CLI for creating projects.

### CHECKOUT_ARG_HELP

```
CHECKOUT_ARG_HELP = 'An optional tag, branch or commit to checkout in the starter repository.'
```

### CONFIG_ARG_HELP

```
CONFIG_ARG_HELP = "Non-interactive mode, using a configuration yaml file. This file\nmust supply  the keys required by the template's prompts.yml. When not using a starter,\nthese are `project_name`, `repo_name` and `python_package`."
```

### CONTEXT_SETTINGS

```
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
```

### DIRECTORY_ARG_HELP

```
DIRECTORY_ARG_HELP = 'An optional directory inside the repository where the starter resides.'
```

### EXAMPLE_ARG_HELP

```
EXAMPLE_ARG_HELP = 'Enter y to enable, n to disable the example pipeline.'
```

### KEDRO_PATH

```
KEDRO_PATH = parent
```

### NAME_ARG_HELP

```
NAME_ARG_HELP = 'The name of your new Kedro project.'
```

### NUMBER_TO_TOOLS_NAME

```
NUMBER_TO_TOOLS_NAME = {'1': 'Linting', '2': 'Testing', '3': 'Custom Logging', '4': 'Documentation', '5': 'Data Structure', '6': 'PySpark'}
```

### STARTER_ARG_HELP

```
STARTER_ARG_HELP = 'Specify the starter template to use when creating the project.\nThis can be the path to a local directory, a URL to a remote VCS repository supported\nby `cookiecutter` or one of the aliases listed in ``kedro starter list``.\n'
```

### TELEMETRY_ARG_HELP

```
TELEMETRY_ARG_HELP = 'Allow or not allow Kedro to collect usage analytics.\nWe cannot see nor store information contained into a Kedro project. Opt in with "yes"\nand out with "no".\n'
```

### TEMPLATE_PATH

```
TEMPLATE_PATH = KEDRO_PATH / 'templates' / 'project'
```

### TOOLS_ARG_HELP

```
TOOLS_ARG_HELP = "\nSelect which tools you'd like to include. By default, none are included.\n\n\nTools\n\n1) Linting: Provides a basic linting setup with Ruff\n\n2) Testing: Provides basic testing setup with pytest\n\n3) Custom Logging: Provides more logging options\n\n4) Documentation: Basic documentation setup with Sphinx\n\n5) Data Structure: Provides a directory structure for storing data\n\n6) PySpark: Provides set up configuration for working with PySpark\n\n\nExample usage:\n\nkedro new --tools=lint,test,log,docs,data,pyspark (or any subset of these options)\n\nkedro new --tools=all\n\nkedro new --tools=none\n\nFor more information on using tools, see https://docs.kedro.org/en/stable/create/new_project_tools/#tools-to-customise-a-new-kedro-project\n"
```

### TOOLS_SHORTNAME_TO_NUMBER

```
TOOLS_SHORTNAME_TO_NUMBER = {'lint': '1', 'test': '2', 'tests': '2', 'log': '3', 'logs': '3', 'docs': '4', 'doc': '4', 'data': '5', 'pyspark': '6'}
```

### \_OFFICIAL_STARTER_SPECS

```
_OFFICIAL_STARTER_SPECS = [KedroStarterSpec('astro-airflow-iris', _STARTERS_REPO, 'astro-airflow-iris'), KedroStarterSpec('spaceflights-pandas', _STARTERS_REPO, 'spaceflights-pandas'), KedroStarterSpec('spaceflights-pyspark', _STARTERS_REPO, 'spaceflights-pyspark'), KedroStarterSpec('databricks-iris', _STARTERS_REPO, 'databricks-iris'), KedroStarterSpec('support-agent-langgraph', _STARTERS_REPO, 'support-agent-langgraph')]
```

### \_OFFICIAL_STARTER_SPECS_DICT

```
_OFFICIAL_STARTER_SPECS_DICT = {(alias): spec for spec in _OFFICIAL_STARTER_SPECS}
```

### \_STARTERS_REPO

```
_STARTERS_REPO = 'git+https://github.com/kedro-org/kedro-starters.git'
```

### version

```
version = '1.2.0'
```

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### KedroStarterSpec

Specification of custom kedro starter template Args: alias: alias of the starter which shows up on `kedro starter list` and is used by the starter argument of `kedro new` template_path: path to a directory or a URL to a remote VCS repository supported by `cookiecutter` directory: optional directory inside the repository where the starter resides. origin: reserved field used by kedro internally to determine where the starter comes from, users do not need to provide this field.

### \_Prompt

```
_Prompt(*args, **kwargs)
```

Represent a single CLI prompt for `kedro new`

Source code in `kedro/framework/cli/starters.py`

```
def __init__(self, *args: Any, **kwargs: Any) -> None:
    try:
        self.title = kwargs["title"]
    except KeyError as exc:
        raise KedroCliError(
            "Each prompt must have a title field to be valid."
        ) from exc

    self.text = kwargs.get("text", "")
    self.regexp = kwargs.get("regex_validator", None)
    self.error_message = kwargs.get("error_message", "")
```

#### validate

```
validate(user_input)
```

Validate a given prompt value against the regex validator

Source code in `kedro/framework/cli/starters.py`

```
def validate(self, user_input: str) -> None:
    """Validate a given prompt value against the regex validator"""
    if self.regexp and not re.match(self.regexp, user_input):
        message = f"'{user_input}' is an invalid value for {(self.title).lower()}."
        click.secho(message, fg="red", err=True)
        click.secho(self.error_message, fg="red", err=True)
        sys.exit(1)
```

### \_clean_pycache

```
_clean_pycache(path)
```

Recursively clean all **pycache** folders from `path`.

Parameters:

- **`path`** (`Path`) – Existing local directory to clean pycache folders from.

Source code in `kedro/framework/cli/utils.py`

```
def _clean_pycache(path: Path) -> None:
    """Recursively clean all __pycache__ folders from `path`.

    Args:
        path: Existing local directory to clean __pycache__ folders from.
    """
    to_delete = [each.resolve() for each in path.rglob("__pycache__")]

    for each in to_delete:
        shutil.rmtree(each, ignore_errors=True)
```

### \_convert_tool_numbers_to_readable_names

```
_convert_tool_numbers_to_readable_names(tools_numbers)
```

Transform the list of tool numbers into a list of readable names, using 'None' for empty lists. Then, convert the result into a string format to prevent issues with Cookiecutter.

Source code in `kedro/framework/cli/starters.py`

```
def _convert_tool_numbers_to_readable_names(tools_numbers: list) -> str:
    """Transform the list of tool numbers into a list of readable names, using 'None' for empty lists.
    Then, convert the result into a string format to prevent issues with Cookiecutter.
    """
    tools_names = [NUMBER_TO_TOOLS_NAME[tool] for tool in tools_numbers]
    if tools_names == []:
        tools_names = ["None"]
    return str(tools_names)
```

### \_convert_tool_short_names_to_numbers

```
_convert_tool_short_names_to_numbers(selected_tools)
```

Prepares tools selection from the CLI or config input to the correct format to be put in the project configuration, if it exists. Replaces tool strings with the corresponding prompt number.

Parameters:

- **`selected_tools`** (`str`) – a string containing the value for the --tools flag or config file, or None in case none were provided, i.e. lint,docs.

Returns:

- `list` – String with the numbers corresponding to the desired tools, or
- `list` – None in case the --tools flag was not used.

Source code in `kedro/framework/cli/starters.py`

```
def _convert_tool_short_names_to_numbers(selected_tools: str) -> list:
    """Prepares tools selection from the CLI or config input to the correct format
    to be put in the project configuration, if it exists.
    Replaces tool strings with the corresponding prompt number.

    Args:
        selected_tools: a string containing the value for the --tools flag or config file,
            or None in case none were provided, i.e. lint,docs.

    Returns:
        String with the numbers corresponding to the desired tools, or
        None in case the --tools flag was not used.
    """
    if selected_tools.lower() == "none":
        return []
    if selected_tools.lower() == "all":
        return list(NUMBER_TO_TOOLS_NAME.keys())

    tools = []
    for tool in selected_tools.lower().split(","):
        tool_short_name = tool.strip()
        if tool_short_name in TOOLS_SHORTNAME_TO_NUMBER:
            tools.append(TOOLS_SHORTNAME_TO_NUMBER[tool_short_name])

    # Remove duplicates if any
    tools = sorted(list(set(tools)))

    return tools
```

### \_create_project

```
_create_project(template_path, cookiecutter_args, telemetry_consent)
```

Creates a new kedro project using cookiecutter.

Parameters:

- **`template_path`** (`str`) – The path to the cookiecutter template to create the project. It could either be a local directory or a remote VCS repository supported by cookiecutter. For more details, please see: https://cookiecutter.readthedocs.io/en/stable/usage.html#generate-your-project
- **`cookiecutter_args`** (`dict[str, Any]`) – Arguments to pass to cookiecutter.

Raises:

- `KedroCliError` – If it fails to generate a project.

Source code in `kedro/framework/cli/starters.py`

```
def _create_project(
    template_path: str, cookiecutter_args: dict[str, Any], telemetry_consent: str | None
) -> None:
    """Creates a new kedro project using cookiecutter.

    Args:
        template_path: The path to the cookiecutter template to create the project.
            It could either be a local directory or a remote VCS repository
            supported by cookiecutter. For more details, please see:
            https://cookiecutter.readthedocs.io/en/stable/usage.html#generate-your-project
        cookiecutter_args: Arguments to pass to cookiecutter.

    Raises:
        KedroCliError: If it fails to generate a project.
    """
    from cookiecutter.main import cookiecutter  # for performance reasons

    try:
        result_path = cookiecutter(template=template_path, **cookiecutter_args)

        if telemetry_consent is not None:
            with open(result_path + "/.telemetry", "w") as telemetry_file:
                telemetry_file.write("consent: " + telemetry_consent)
    except Exception as exc:
        raise KedroCliError(
            "Failed to generate project when running cookiecutter."
        ) from exc

    _clean_pycache(Path(result_path))
    extra_context = cookiecutter_args["extra_context"]
    project_name = extra_context.get("project_name", "New Kedro Project")

    # Print success message
    click.secho(
        "\nCongratulations!"
        f"\nYour project '{project_name}' has been created in the directory \n{result_path}\n"
    )
```

### \_fetch_validate_parse_config_from_file

```
_fetch_validate_parse_config_from_file(config_path, prompts_required, starter_alias)
```

Obtains configuration for a new kedro project non-interactively from a file. Validates that:

1. All keys specified in prompts_required are retrieved from the configuration.
1. The options 'tools' and 'example_pipeline' are not used in the configuration when any starter option is selected.
1. Variables sourced from the configuration file adhere to the expected format.

Parse tools from short names to list of numbers

Parameters:

- **`config_path`** (`str`) – The path of the config.yml which should contain the data required by prompts.yml.

Returns:

- `dict[str, str]` – Configuration for starting a new project. This is passed as extra_context to cookiecutter and will overwrite the cookiecutter.json defaults.

Raises:

- `KedroCliError` – If the file cannot be parsed.

Source code in `kedro/framework/cli/starters.py`

```
def _fetch_validate_parse_config_from_file(
    config_path: str, prompts_required: dict, starter_alias: str | None
) -> dict[str, str]:
    """Obtains configuration for a new kedro project non-interactively from a file.
    Validates that:
    1. All keys specified in prompts_required are retrieved from the configuration.
    2. The options 'tools' and 'example_pipeline' are not used in the configuration when any starter option is selected.
    3. Variables sourced from the configuration file adhere to the expected format.

    Parse tools from short names to list of numbers

    Args:
        config_path: The path of the config.yml which should contain the data required
            by ``prompts.yml``.

    Returns:
        Configuration for starting a new project. This is passed as ``extra_context``
            to cookiecutter and will overwrite the cookiecutter.json defaults.

    Raises:
        KedroCliError: If the file cannot be parsed.

    """
    try:
        with open(config_path, encoding="utf-8") as config_file:
            config: dict[str, str] = yaml.safe_load(config_file)

        if KedroCliError.VERBOSE_ERROR:
            click.echo(config_path + ":")
            click.echo(yaml.dump(config, default_flow_style=False))
    except Exception as exc:
        raise KedroCliError(
            f"Failed to generate project: could not load config at {config_path}."
        ) from exc

    if starter_alias and ("tools" in config or "example_pipeline" in config):
        raise KedroCliError(
            "The --starter flag can not be used with `example_pipeline` and/or `tools` keys in the config file."
        )

    _validate_config_file_against_prompts(config, prompts_required)

    _validate_input_with_regex_pattern(
        "project_name", config.get("project_name", "New Kedro Project")
    )

    example_pipeline = config.get("example_pipeline", "no")
    _validate_input_with_regex_pattern("yes_no", example_pipeline)
    config["example_pipeline"] = str(_parse_yes_no_to_bool(example_pipeline))

    tools_short_names = config.get("tools", "none").lower()
    _validate_selected_tools(tools_short_names)
    tools_numbers = _convert_tool_short_names_to_numbers(tools_short_names)
    config["tools"] = _convert_tool_numbers_to_readable_names(tools_numbers)

    return config
```

### \_fetch_validate_parse_config_from_user_prompts

```
_fetch_validate_parse_config_from_user_prompts(prompts, cookiecutter_context)
```

Interactively obtains information from user prompts.

Parameters:

- **`prompts`** (`dict[str, Any]`) – Prompts from prompts.yml.
- **`cookiecutter_context`** (`OrderedDict | None`) – Cookiecutter context generated from cookiecutter.json.

Returns:

- `dict[str, str]` – Configuration for starting a new project. This is passed as extra_context to cookiecutter and will overwrite the cookiecutter.json defaults.

Source code in `kedro/framework/cli/starters.py`

```
def _fetch_validate_parse_config_from_user_prompts(
    prompts: dict[str, Any],
    cookiecutter_context: OrderedDict | None,
) -> dict[str, str]:
    """Interactively obtains information from user prompts.

    Args:
        prompts: Prompts from prompts.yml.
        cookiecutter_context: Cookiecutter context generated from cookiecutter.json.

    Returns:
        Configuration for starting a new project. This is passed as ``extra_context``
            to cookiecutter and will overwrite the cookiecutter.json defaults.
    """
    if not cookiecutter_context:
        raise Exception("No cookiecutter context available.")

    config: dict[str, str] = {}

    for variable_name, prompt_dict in prompts.items():
        prompt = _Prompt(**prompt_dict)

        # render the variable on the command line
        default_value = cookiecutter_context.get(variable_name) or ""

        # read the user's input for the variable
        user_input = click.prompt(
            str(prompt),
            default=default_value,
            show_default=True,
            type=str,
        ).strip()

        if user_input:
            prompt.validate(user_input)
            config[variable_name] = user_input

    if "tools" in config:
        # convert tools input to list of numbers and validate
        tools_numbers = _parse_tools_input(config["tools"])
        _validate_tool_selection(tools_numbers)
        config["tools"] = _convert_tool_numbers_to_readable_names(tools_numbers)
    if "example_pipeline" in config:
        example_pipeline_bool = _parse_yes_no_to_bool(config["example_pipeline"])
        config["example_pipeline"] = str(example_pipeline_bool)

    return config
```

### \_get_available_tags

```
_get_available_tags(template_path)
```

Source code in `kedro/framework/cli/starters.py`

```
def _get_available_tags(template_path: str) -> list:
    # Not at top level so that kedro CLI works without a working git executable.
    import git

    try:
        tags = git.cmd.Git().ls_remote("--tags", template_path.replace("git+", ""))

        unique_tags = {
            tag.split("/")[-1].replace("^{}", "") for tag in tags.split("\n")
        }
        # Remove git ref "^{}" and duplicates. For example,
        # tags: ['/tags/version', '/tags/version^{}']
        # unique_tags: {'version'}

    except git.GitCommandError:  # pragma: no cover
        return []
    return sorted(unique_tags)
```

### \_get_cookiecutter_dir

```
_get_cookiecutter_dir(template_path, checkout, directory, tmpdir)
```

Gives a path to the cookiecutter directory. If template_path is a repo then clones it to `tmpdir`; if template_path is a file path then directly uses that path without copying anything.

Source code in `kedro/framework/cli/starters.py`

```
def _get_cookiecutter_dir(
    template_path: str, checkout: str, directory: str, tmpdir: str
) -> Path:
    """Gives a path to the cookiecutter directory. If template_path is a repo then
    clones it to ``tmpdir``; if template_path is a file path then directly uses that
    path without copying anything.
    """
    from cookiecutter.exceptions import RepositoryCloneFailed, RepositoryNotFound
    from cookiecutter.repository import determine_repo_dir  # for performance reasons

    try:
        cookiecutter_dir, _ = determine_repo_dir(
            template=template_path,
            abbreviations={},
            clone_to_dir=Path(tmpdir).resolve(),
            checkout=checkout,
            no_input=True,
            directory=directory,
        )
    except (RepositoryNotFound, RepositoryCloneFailed) as exc:
        error_message = f"Kedro project template not found at {template_path}."

        if checkout:
            error_message += (
                f" Specified tag {checkout}. The following tags are available: "
                + ", ".join(_get_available_tags(template_path))
            )
        official_starters = sorted(_OFFICIAL_STARTER_SPECS_DICT)
        raise KedroCliError(
            f"{error_message}. The aliases for the official Kedro starters are: \n"
            f"{yaml.safe_dump(official_starters, sort_keys=False)}"
        ) from exc

    return Path(cookiecutter_dir)
```

### \_get_entry_points

```
_get_entry_points(name)
```

Get all kedro related entry points

Source code in `kedro/framework/cli/utils.py`

```
def _get_entry_points(name: str) -> Any:
    """Get all kedro related entry points"""
    return importlib.metadata.entry_points().select(  # type: ignore[no-untyped-call]
        group=ENTRY_POINT_GROUPS[name]
    )
```

### \_get_extra_context

```
_get_extra_context(prompts_required, config_path, cookiecutter_context, selected_tools, project_name, example_pipeline, starter_alias)
```

Generates a config dictionary that will be passed to cookiecutter as `extra_context`, based on CLI flags, user prompts, configuration file or Default values. It is crucial to return a dictionary with string values, otherwise, there will be issues with Cookiecutter.

Parameters:

- **`prompts_required`** (`dict`) – a dictionary of all the prompts that will be shown to the user on project creation.
- **`config_path`** (`str`) – a string containing the value for the --config flag, or None in case the flag wasn't used.
- **`cookiecutter_context`** (`OrderedDict | None`) – the context for Cookiecutter templates.
- **`selected_tools`** (`str | None`) – a string containing the value for the --tools flag, or None in case the flag wasn't used.
- **`project_name`** (`str | None`) – a string containing the value for the --name flag, or None in case the flag wasn't used.
- **`example_pipeline`** (`str | None`) – a string containing the value for the --example flag, or None in case the flag wasn't used
- **`starter_alias`** (`str | None`) – a string containing the value for the --starter flag, or None in case the flag wasn't used

Returns:

- `dict[str, str]` – Config dictionary, passed the necessary processing, with default values if needed.

Source code in `kedro/framework/cli/starters.py`

```
def _get_extra_context(  # noqa: PLR0913
    prompts_required: dict,
    config_path: str,
    cookiecutter_context: OrderedDict | None,
    selected_tools: str | None,
    project_name: str | None,
    example_pipeline: str | None,
    starter_alias: str | None,
) -> dict[str, str]:
    """Generates a config dictionary that will be passed to cookiecutter as `extra_context`, based
    on CLI flags, user prompts, configuration file or Default values.
    It is crucial to return a dictionary with string values, otherwise, there will be issues with Cookiecutter.

    Args:
        prompts_required: a dictionary of all the prompts that will be shown to
            the user on project creation.
        config_path: a string containing the value for the --config flag, or
            None in case the flag wasn't used.
        cookiecutter_context: the context for Cookiecutter templates.
        selected_tools: a string containing the value for the --tools flag,
            or None in case the flag wasn't used.
        project_name: a string containing the value for the --name flag, or
            None in case the flag wasn't used.
        example_pipeline: a string containing the value for the --example flag,
            or None in case the flag wasn't used
        starter_alias: a string containing the value for the --starter flag, or
            None in case the flag wasn't used

    Returns:
        Config dictionary, passed the necessary processing, with default values if needed.
    """
    if config_path:
        extra_context = _fetch_validate_parse_config_from_file(
            config_path, prompts_required, starter_alias
        )
    else:
        extra_context = _fetch_validate_parse_config_from_user_prompts(
            prompts_required, cookiecutter_context
        )

    # Update extra_context, if CLI inputs are available
    if selected_tools is not None:
        tools_numbers = _convert_tool_short_names_to_numbers(selected_tools)
        extra_context["tools"] = _convert_tool_numbers_to_readable_names(tools_numbers)
    if project_name is not None:
        extra_context["project_name"] = project_name
    if example_pipeline is not None:
        extra_context["example_pipeline"] = str(_parse_yes_no_to_bool(example_pipeline))

    # set defaults for required fields, will be used mostly for starters
    extra_context.setdefault("kedro_version", version)
    extra_context.setdefault("tools", str(["None"]))
    extra_context.setdefault("example_pipeline", "False")

    return extra_context
```

### \_get_prompts_required_and_clear_from_CLI_provided

```
_get_prompts_required_and_clear_from_CLI_provided(cookiecutter_dir, selected_tools, project_name, example_pipeline)
```

Finds the information a user must supply according to prompts.yml, and clear it from what has already been provided via the CLI(validate it before)

Source code in `kedro/framework/cli/starters.py`

```
def _get_prompts_required_and_clear_from_CLI_provided(
    cookiecutter_dir: Path,
    selected_tools: str,
    project_name: str,
    example_pipeline: str,
) -> Any:
    """Finds the information a user must supply according to prompts.yml,
    and clear it from what has already been provided via the CLI(validate it before)"""
    prompts_yml = cookiecutter_dir / "prompts.yml"
    if not prompts_yml.is_file():
        return {}

    try:
        with prompts_yml.open("r") as prompts_file:
            prompts_required = yaml.safe_load(prompts_file)
    except Exception as exc:
        raise KedroCliError(
            "Failed to generate project: could not load prompts.yml."
        ) from exc

    if selected_tools is not None:
        _validate_selected_tools(selected_tools)
        del prompts_required["tools"]

    if project_name is not None:
        _validate_input_with_regex_pattern("project_name", project_name)
        del prompts_required["project_name"]

    if example_pipeline is not None:
        _validate_input_with_regex_pattern("yes_no", example_pipeline)
        del prompts_required["example_pipeline"]

    return prompts_required
```

### \_get_starters_dict

```
_get_starters_dict()
```

This function lists all the starter aliases declared in the core repo and in plugins entry points.

For example, the output for official kedro starters looks like: {"astro-airflow-iris": KedroStarterSpec( name="astro-airflow-iris", template_path="git+https://github.com/kedro-org/kedro-starters.git", directory="astro-airflow-iris", origin="kedro" ), }

Source code in `kedro/framework/cli/starters.py`

```
def _get_starters_dict() -> dict[str, KedroStarterSpec]:
    """This function lists all the starter aliases declared in
    the core repo and in plugins entry points.

    For example, the output for official kedro starters looks like:
    {"astro-airflow-iris":
        KedroStarterSpec(
            name="astro-airflow-iris",
            template_path="git+https://github.com/kedro-org/kedro-starters.git",
            directory="astro-airflow-iris",
            origin="kedro"
        ),
    }
    """
    starter_specs = _OFFICIAL_STARTER_SPECS_DICT

    for starter_entry_point in _get_entry_points(name="starters"):
        origin = starter_entry_point.module.split(".")[0]
        specs: EntryPoints | list = _safe_load_entry_point(starter_entry_point) or []
        for spec in specs:
            if not isinstance(spec, KedroStarterSpec):
                click.secho(
                    f"The starter configuration loaded from module {origin}"
                    f"should be a 'KedroStarterSpec', got '{type(spec)}' instead",
                    fg="red",
                )
            elif spec.alias in starter_specs:
                click.secho(
                    f"Starter alias `{spec.alias}` from `{origin}` "
                    f"has been ignored as it is already defined by"
                    f"`{starter_specs[spec.alias].origin}`",
                    fg="red",
                )
            else:
                spec.origin = origin
                starter_specs[spec.alias] = spec
    return starter_specs
```

### \_make_cookiecutter_args_and_fetch_template

```
_make_cookiecutter_args_and_fetch_template(config, checkout, directory, template_path)
```

Creates a dictionary of arguments to pass to cookiecutter and returns project template path.

Parameters:

- **`config`** (`dict[str, str]`) – Configuration for starting a new project. This is passed as extra_context to cookiecutter and will overwrite the cookiecutter.json defaults.
- **`checkout`** (`str`) – The tag, branch or commit in the starter repository to checkout. Maps directly to cookiecutter's checkout argument.
- **`directory`** (`str`) – The directory of a specific starter inside a repository containing multiple starters. Maps directly to cookiecutter's directory argument. Relevant only when using a starter. https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html
- **`template_path`** (`str`) – Starter path or kedro template path

Returns:

- `tuple[dict[str, object], str]` – Arguments to pass to cookiecutter, project template path

Source code in `kedro/framework/cli/starters.py`

```
def _make_cookiecutter_args_and_fetch_template(
    config: dict[str, str],
    checkout: str,
    directory: str,
    template_path: str,
) -> tuple[dict[str, object], str]:
    """Creates a dictionary of arguments to pass to cookiecutter and returns project template path.

    Args:
        config: Configuration for starting a new project. This is passed as
            ``extra_context`` to cookiecutter and will overwrite the cookiecutter.json
            defaults.
        checkout: The tag, branch or commit in the starter repository to checkout.
            Maps directly to cookiecutter's ``checkout`` argument.
        directory: The directory of a specific starter inside a repository containing
            multiple starters. Maps directly to cookiecutter's ``directory`` argument.
            Relevant only when using a starter.
            https://cookiecutter.readthedocs.io/en/1.7.2/advanced/directories.html
        template_path: Starter path or kedro template path

    Returns:
        Arguments to pass to cookiecutter, project template path
    """

    cookiecutter_args = {
        "output_dir": config.get("output_dir", str(Path.cwd().resolve())),
        "no_input": True,
        "extra_context": config,
    }

    if directory:
        cookiecutter_args["directory"] = directory
    cookiecutter_args["checkout"] = checkout

    tools = config["tools"]
    example_pipeline = config["example_pipeline"]
    starter_path = "git+https://github.com/kedro-org/kedro-starters.git"

    if "PySpark" in tools:
        # Use the spaceflights-pyspark starter if only PySpark is chosen.
        cookiecutter_args["directory"] = "spaceflights-pyspark"
        cookiecutter_args["checkout"] = _select_checkout_branch_for_cookiecutter(
            checkout
        )
    elif example_pipeline == "True":
        # Use spaceflights-pandas starter if example was selected, but PySpark wasn't
        cookiecutter_args["directory"] = "spaceflights-pandas"
        cookiecutter_args["checkout"] = _select_checkout_branch_for_cookiecutter(
            checkout
        )
    else:
        # Use the default template path for non PySpark or example options:
        starter_path = template_path

    return cookiecutter_args, starter_path
```

### \_make_cookiecutter_context_for_prompts

```
_make_cookiecutter_context_for_prompts(cookiecutter_dir)
```

Source code in `kedro/framework/cli/starters.py`

```
def _make_cookiecutter_context_for_prompts(cookiecutter_dir: Path) -> OrderedDict:
    from cookiecutter.generate import generate_context

    cookiecutter_context = generate_context(cookiecutter_dir / "cookiecutter.json")
    return cookiecutter_context.get("cookiecutter", {})  # type: ignore[no-any-return]
```

### \_parse_tools_input

```
_parse_tools_input(tools_str)
```

Parse the tools input string.

Parameters:

- **`tools_str`** (`str | None`) – Input string from prompts.yml.

Returns:

- `list` – List of selected tools as strings.

Source code in `kedro/framework/cli/starters.py`

```
def _parse_tools_input(tools_str: str | None) -> list[str]:
    """Parse the tools input string.

    Args:
        tools_str: Input string from prompts.yml.

    Returns:
        list: List of selected tools as strings.
    """

    def _validate_range(start: Any, end: Any) -> None:
        if int(start) > int(end):
            message = f"'{start}-{end}' is an invalid range for project tools.\nPlease ensure range values go from smaller to larger."
            click.secho(message, fg="red", err=True)
            sys.exit(1)
        # safeguard to prevent passing of excessively large intervals that could cause freezing:
        if int(end) > len(NUMBER_TO_TOOLS_NAME):
            message = f"'{end}' is not a valid selection.\nPlease select from the available tools: 1, 2, 3, 4, 5, 6."  # nosec
            if end == "7":
                message += "\nKedro Viz is automatically included in the project. Please remove 7 from your tool selection."
            click.secho(message, fg="red", err=True)
            sys.exit(1)

    if not tools_str:
        return []  # pragma: no cover

    tools_str = tools_str.lower()
    if tools_str == "all":
        return list(NUMBER_TO_TOOLS_NAME)
    if tools_str == "none":
        return []

    # Split by comma
    tools_choices = tools_str.replace(" ", "").split(",")
    selected: list[str] = []

    for choice in tools_choices:
        if "-" in choice:
            start, end = choice.split("-")
            _validate_range(start, end)
            selected.extend(str(i) for i in range(int(start), int(end) + 1))
        else:
            selected.append(choice.strip())

    return selected
```

### \_parse_yes_no_to_bool

```
_parse_yes_no_to_bool(value)
```

Source code in `kedro/framework/cli/starters.py`

```
def _parse_yes_no_to_bool(value: str) -> Any:
    return value.strip().lower() in ["y", "yes"] if value is not None else None
```

### \_print_selection_and_prompt_info

```
_print_selection_and_prompt_info(selected_tools, example_pipeline, interactive)
```

Source code in `kedro/framework/cli/starters.py`

```
def _print_selection_and_prompt_info(
    selected_tools: str, example_pipeline: str, interactive: bool
) -> None:
    # Confirm tools selection
    if selected_tools == "['None']":
        click.secho(
            "You have selected no project tools",
            fg="green",
        )
    else:
        click.secho(
            f"You have selected the following project tools: {selected_tools}",
            fg="green",
        )

    # Confirm example selection
    if example_pipeline == "True":
        click.secho(
            "It has been created with an example pipeline.",
            fg="green",
        )
    else:
        warnings.warn(
            "Your project does not contain any pipelines with nodes. "
            "Please ensure that at least one pipeline has been defined before "
            "executing 'kedro run'.",
            UserWarning,
        )

    # Give hint for skipping interactive flow
    if interactive:
        click.secho(
            "\nTo skip the interactive flow you can run `kedro new` with"
            "\nkedro new --name=<your-project-name> --tools=<your-project-tools> --example=<yes/no>",
            fg="green",
        )
```

### \_remove_readonly

```
_remove_readonly(func, path, excinfo)
```

Remove readonly files on Windows See: https://docs.python.org/3/library/shutil.html?highlight=shutil#rmtree-example

Source code in `kedro/framework/cli/starters.py`

```
def _remove_readonly(
    func: Callable, path: Path, excinfo: tuple
) -> None:  # pragma: no cover
    """Remove readonly files on Windows
    See: https://docs.python.org/3/library/shutil.html?highlight=shutil#rmtree-example
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)
```

### \_safe_load_entry_point

```
_safe_load_entry_point(entry_point)
```

Load entrypoint safely, if fails it will just skip the entrypoint.

Source code in `kedro/framework/cli/utils.py`

```
def _safe_load_entry_point(
    entry_point: Any,
) -> Any:
    """Load entrypoint safely, if fails it will just skip the entrypoint."""
    try:
        return entry_point.load()
    except Exception as exc:
        logger.warning(
            "Failed to load %s commands from %s. Full exception: %s",
            entry_point.module,
            entry_point,
            exc,
        )
        return
```

### \_select_checkout_branch_for_cookiecutter

```
_select_checkout_branch_for_cookiecutter(checkout)
```

Source code in `kedro/framework/cli/starters.py`

```
def _select_checkout_branch_for_cookiecutter(checkout: str | None) -> str:
    if checkout:
        return checkout
    else:
        return version
```

### \_starter_spec_to_dict

```
_starter_spec_to_dict(starter_specs)
```

Convert a dictionary of starters spec to a nicely formatted dictionary

Source code in `kedro/framework/cli/starters.py`

```
def _starter_spec_to_dict(
    starter_specs: dict[str, KedroStarterSpec],
) -> dict[str, dict[str, str]]:
    """Convert a dictionary of starters spec to a nicely formatted dictionary"""
    format_dict: dict[str, dict[str, str]] = {}
    for alias, spec in starter_specs.items():
        format_dict[alias] = {}  # Each dictionary represent 1 starter
        format_dict[alias]["template_path"] = spec.template_path
        if spec.directory:
            format_dict[alias]["directory"] = spec.directory
    return format_dict
```

### \_validate_config_file_against_prompts

```
_validate_config_file_against_prompts(config, prompts)
```

Checks that the configuration file contains all needed variables.

Parameters:

- **`config`** (`dict[str, str]`) – The config as a dictionary.
- **`prompts`** (`dict[str, Any]`) – Prompts from prompts.yml.

Raises:

- `KedroCliError` – If the config file is empty or does not contain all the keys required in prompts, or if the output_dir specified does not exist.

Source code in `kedro/framework/cli/starters.py`

```
def _validate_config_file_against_prompts(
    config: dict[str, str], prompts: dict[str, Any]
) -> None:
    """Checks that the configuration file contains all needed variables.

    Args:
        config: The config as a dictionary.
        prompts: Prompts from prompts.yml.

    Raises:
        KedroCliError: If the config file is empty or does not contain all the keys
            required in prompts, or if the output_dir specified does not exist.
    """
    if not config:
        raise KedroCliError("Config file is empty.")
    additional_keys = {"tools": "none", "example_pipeline": "no"}
    missing_keys = set(prompts) - set(config)
    missing_mandatory_keys = missing_keys - set(additional_keys)
    if missing_mandatory_keys:
        click.echo(yaml.dump(config, default_flow_style=False))
        raise KedroCliError(
            f"{', '.join(missing_mandatory_keys)} not found in config file."
        )
    for key, default_value in additional_keys.items():
        if key in missing_keys:
            click.secho(
                f"The `{key}` key not found in the config file, default value '{default_value}' is being used.",
                fg="yellow",
            )

    if "output_dir" in config and not Path(config["output_dir"]).exists():
        raise KedroCliError(
            f"'{config['output_dir']}' is not a valid output directory. "
            "It must be a relative or absolute path to an existing directory."
        )
```

### \_validate_flag_inputs

```
_validate_flag_inputs(flag_inputs)
```

Source code in `kedro/framework/cli/starters.py`

```
def _validate_flag_inputs(flag_inputs: dict[str, Any]) -> None:
    if flag_inputs.get("checkout") and not flag_inputs.get("starter"):
        raise KedroCliError("Cannot use the --checkout flag without a --starter value.")

    if flag_inputs.get("directory") and not flag_inputs.get("starter"):
        raise KedroCliError(
            "Cannot use the --directory flag without a --starter value."
        )

    if (flag_inputs.get("tools") or flag_inputs.get("example")) and flag_inputs.get(
        "starter"
    ):
        raise KedroCliError(
            "Cannot use the --starter flag with the --example and/or --tools flag."
        )
```

### \_validate_input_with_regex_pattern

```
_validate_input_with_regex_pattern(pattern_name, input)
```

Source code in `kedro/framework/cli/starters.py`

```
def _validate_input_with_regex_pattern(pattern_name: str, input: str) -> None:
    VALIDATION_PATTERNS = {
        "yes_no": {
            "regex": r"(?i)^\s*(y|yes|n|no)\s*$",
            "error_message": f"'{input}' is an invalid value for example pipeline. It must contain only y, n, YES, or NO (case insensitive).",
        },
        "project_name": {
            "regex": r"^[\w -]{2,}$",
            "error_message": f"'{input}' is an invalid value for project name. It must contain only alphanumeric symbols, spaces, underscores and hyphens and be at least 2 characters long",
        },
        "tools": {
            "regex": r"""^(
                all|none|                        # A: "all" or "none" or
                (\ *\d+                          # B: any number of spaces followed by one or more digits
                (\ *-\ *\d+)?                    # C: zero or one instances of: a hyphen followed by one or more digits, spaces allowed
                (\ *,\ *\d+(\ *-\ *\d+)?)*       # D: any number of instances of: a comma followed by B and C, spaces allowed
                \ *)?)                           # E: zero or one instances of (B,C,D) as empty strings are also permissible
                $""",
            "error_message": f"'{input}' is an invalid value for project tools. Please select valid options for tools using comma-separated values, ranges, or 'all/none'.",
        },
    }

    if not re.match(VALIDATION_PATTERNS[pattern_name]["regex"], input, flags=re.X):
        click.secho(
            VALIDATION_PATTERNS[pattern_name]["error_message"],
            fg="red",
            err=True,
        )
        sys.exit(1)
```

### \_validate_selected_tools

```
_validate_selected_tools(selected_tools)
```

Source code in `kedro/framework/cli/starters.py`

```
def _validate_selected_tools(selected_tools: str | None) -> None:
    valid_tools = [*list(TOOLS_SHORTNAME_TO_NUMBER), "all", "none"]

    if selected_tools is not None:
        tools = re.sub(r"\s", "", selected_tools).split(",")
        for tool in tools:
            if tool not in valid_tools:
                message = "Please select from the available tools: lint, test, log, docs, data, pyspark, all, none."
                if tool == "viz":
                    message += " Kedro Viz is automatically included in the project. Please remove 'viz' from your tool selection."
                click.secho(
                    message,
                    fg="red",
                    err=True,
                )
                sys.exit(1)
        if ("none" in tools or "all" in tools) and len(tools) > 1:
            click.secho(
                "Tools options 'all' and 'none' cannot be used with other options",
                fg="red",
                err=True,
            )
            sys.exit(1)
```

### \_validate_tool_selection

```
_validate_tool_selection(tools)
```

Source code in `kedro/framework/cli/starters.py`

```
def _validate_tool_selection(tools: list[str]) -> None:
    # start validating from the end, when user select 1-20, it will generate a message
    # '20' is not a valid selection instead of '8'
    for tool in tools[::-1]:
        if tool not in NUMBER_TO_TOOLS_NAME:
            message = f"'{tool}' is not a valid selection.\nPlease select from the available tools: 1, 2, 3, 4, 5, 6."  # nosec
            if tool == "7":
                message += "\nKedro Viz is automatically included in the project. Please remove 7 from your tool selection."
            click.secho(message, fg="red", err=True)
            sys.exit(1)
```

### command_with_verbosity

```
command_with_verbosity(group, *args, **kwargs)
```

Custom command decorator with verbose flag added.

Source code in `kedro/framework/cli/utils.py`

```
def command_with_verbosity(group: click.core.Group, *args: Any, **kwargs: Any) -> Any:
    """Custom command decorator with verbose flag added."""

    def decorator(func: Any) -> Any:
        func = _click_verbose(func)
        func = group.command(*args, **kwargs)(func)
        return func

    return decorator
```

### create_cli

```
create_cli()
```

Source code in `kedro/framework/cli/starters.py`

```
@click.group(context_settings=CONTEXT_SETTINGS, name="kedro")
def create_cli() -> None:  # pragma: no cover
    pass
```

### list_starters

```
list_starters()
```

List all official project starters available.

Source code in `kedro/framework/cli/starters.py`

```
@starter.command("list")
def list_starters() -> None:
    """List all official project starters available."""
    starters_dict = _get_starters_dict()

    # Group all specs by origin as nested dict and sort it.
    sorted_starters_dict: dict[str, dict[str, KedroStarterSpec]] = {
        origin: dict(sorted(starters_dict_by_origin))
        for origin, starters_dict_by_origin in groupby(
            starters_dict.items(), lambda item: item[1].origin
        )
    }

    # ensure kedro starters are listed first
    sorted_starters_dict = dict(
        sorted(sorted_starters_dict.items(), key=lambda x: x == "kedro")  # type: ignore[comparison-overlap]
    )

    for origin, starters_spec in sorted_starters_dict.items():
        click.secho(f"\nStarters from {origin}\n", fg="yellow")
        click.echo(
            yaml.safe_dump(_starter_spec_to_dict(starters_spec), sort_keys=False)
        )
```

### new

```
new(config_path, starter_alias, selected_tools, project_name, checkout, directory, example_pipeline, telemetry_consent, **kwargs)
```

Create a new kedro project.

Source code in `kedro/framework/cli/starters.py`

```
@command_with_verbosity(create_cli, short_help="Create a new kedro project.")
@click.option(
    "--config",
    "-c",
    "config_path",
    type=click.Path(exists=True),
    help=CONFIG_ARG_HELP,
)
@click.option("--starter", "-s", "starter_alias", help=STARTER_ARG_HELP)
@click.option("--checkout", help=CHECKOUT_ARG_HELP)
@click.option("--directory", help=DIRECTORY_ARG_HELP)
@click.option(
    "--name",
    "-n",
    "project_name",
    help=NAME_ARG_HELP,
)
@click.option(
    "--tools",
    "-t",
    "selected_tools",
    help=TOOLS_ARG_HELP,
)
@click.option(
    "--example",
    "-e",
    "example_pipeline",
    help=EXAMPLE_ARG_HELP,
)
@click.option(
    "--telemetry",
    "-tc",
    "telemetry_consent",
    help=TELEMETRY_ARG_HELP,
    type=click.Choice(["yes", "no", "y", "n"], case_sensitive=False),
)
def new(  # noqa: PLR0913
    config_path: str,
    starter_alias: str,
    selected_tools: str,
    project_name: str,
    checkout: str,
    directory: str,
    example_pipeline: str,
    telemetry_consent: str,
    **kwargs: Any,
) -> None:
    """Create a new kedro project."""
    flag_inputs = {
        "config": config_path,
        "starter": starter_alias,
        "tools": selected_tools,
        "name": project_name,
        "checkout": checkout,
        "directory": directory,
        "example": example_pipeline,
        "telemetry_consent": telemetry_consent,
    }

    _validate_flag_inputs(flag_inputs)
    starters_dict = _get_starters_dict()

    if starter_alias in starters_dict:
        if directory:
            raise KedroCliError(
                "Cannot use the --directory flag with a --starter alias."
            )
        spec = starters_dict[starter_alias]
        template_path = spec.template_path
        # "directory" is an optional key for starters from plugins, so if the key is
        # not present we will use "None".
        directory = spec.directory  # type: ignore[assignment]
        checkout = _select_checkout_branch_for_cookiecutter(checkout)
    elif starter_alias is not None:
        template_path = starter_alias
    else:
        template_path = str(TEMPLATE_PATH)

    # Format user input where necessary
    if selected_tools is not None:
        selected_tools = selected_tools.lower()

    # Get prompts.yml to find what information the user needs to supply as config.
    tmpdir = tempfile.mkdtemp()
    cookiecutter_dir = _get_cookiecutter_dir(template_path, checkout, directory, tmpdir)
    prompts_required = _get_prompts_required_and_clear_from_CLI_provided(
        cookiecutter_dir, selected_tools, project_name, example_pipeline
    )

    # We only need to make cookiecutter_context if interactive prompts are needed.
    cookiecutter_context = None

    if not config_path:
        cookiecutter_context = _make_cookiecutter_context_for_prompts(cookiecutter_dir)

    # Cleanup the tmpdir after it's no longer required.
    # Ideally we would want to be able to use tempfile.TemporaryDirectory() context manager
    # but it causes an issue with readonly files on windows
    # see: https://github.com/python/cpython/issues/70847.
    # So on error, we will attempt to clear the readonly bits and re-attempt the cleanup
    shutil.rmtree(tmpdir, onerror=_remove_readonly)  # type: ignore[arg-type]

    # Obtain config, either from a file or from interactive user prompts.

    extra_context = _get_extra_context(
        prompts_required=prompts_required,
        config_path=config_path,
        cookiecutter_context=cookiecutter_context,
        selected_tools=selected_tools,
        project_name=project_name,
        example_pipeline=example_pipeline,
        starter_alias=starter_alias,
    )

    cookiecutter_args, project_template = _make_cookiecutter_args_and_fetch_template(
        config=extra_context,
        checkout=checkout,
        directory=directory,
        template_path=template_path,
    )

    if telemetry_consent is not None:
        telemetry_consent = (
            "true" if _parse_yes_no_to_bool(telemetry_consent) else "false"
        )

    _create_project(project_template, cookiecutter_args, telemetry_consent)

    # If not a starter, print tools and example selection
    if not starter_alias:
        # If interactive flow used, print hint
        interactive_flow = prompts_required and not config_path
        _print_selection_and_prompt_info(
            extra_context["tools"],
            extra_context["example_pipeline"],
            interactive_flow,
        )
```

### starter

```
starter()
```

Commands for working with project starters.

Source code in `kedro/framework/cli/starters.py`

```
@create_cli.group()
def starter() -> None:
    """Commands for working with project starters."""
```

## kedro.framework.cli.utils

Utilities for use with click.

### CONTEXT_SETTINGS

```
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
```

### CUTOFF

```
CUTOFF = 0.5
```

### ENTRY_POINT_GROUPS

```
ENTRY_POINT_GROUPS = {'global': 'kedro.global_commands', 'project': 'kedro.project_commands', 'init': 'kedro.init', 'line_magic': 'kedro.line_magic', 'hooks': 'kedro.hooks', 'cli_hooks': 'kedro.cli_hooks', 'starters': 'kedro.starters'}
```

### ENV_HELP

```
ENV_HELP = 'Kedro configuration environment name. Defaults to `local`.'
```

### MAX_SUGGESTIONS

```
MAX_SUGGESTIONS = 3
```

### logger

```
logger = getLogger(__name__)
```

### CommandCollection

```
CommandCollection(*groups)
```

Bases: `CommandCollection`

Modified from the Click one to still run the source groups function.

Source code in `kedro/framework/cli/utils.py`

```
def __init__(self, *groups: tuple[str, Sequence[click.Group]]):
    self.groups = [
        (title, self._merge_same_name_collections(cli_list))
        for title, cli_list in groups
    ]
    sources = list(chain.from_iterable(cli_list for _, cli_list in self.groups))
    help_texts = [
        cli.help
        for cli_collection in sources
        for cli in cli_collection.sources
        if cli.help
    ]
    super().__init__(
        sources=sources,  # type: ignore[arg-type]
        help="\n\n".join(help_texts),
        context_settings=CONTEXT_SETTINGS,
    )
    self.params = sources[0].params
    self.callback = sources[0].callback
```

### KedroCliError

Bases: `ClickException`

Exceptions generated from the Kedro CLI.

Users should pass an appropriate message at the constructor.

### LazyGroup

```
LazyGroup(*args, lazy_subcommands=None, **kwargs)
```

Bases: `Group`

A click Group that supports lazy loading of subcommands.

Source code in `kedro/framework/cli/utils.py`

```
def __init__(
    self,
    *args: Any,
    lazy_subcommands: dict[str, str] | None = None,
    **kwargs: Any,
):
    super().__init__(*args, **kwargs)
    # lazy_subcommands is a map of the form:
    #
    #   {command-name} -> {module-name}.{command-object-name}
    #
    self.lazy_subcommands = lazy_subcommands or {}
```

### \_check_module_importable

```
_check_module_importable(module_name)
```

Source code in `kedro/framework/cli/utils.py`

```
def _check_module_importable(module_name: str) -> None:
    try:
        import_module(module_name)
    except ImportError as exc:
        raise KedroCliError(
            f"Module '{module_name}' not found. Make sure to install required project "
            f"dependencies by running the 'pip install -r requirements.txt' command first."
        ) from exc
```

### \_clean_pycache

```
_clean_pycache(path)
```

Recursively clean all **pycache** folders from `path`.

Parameters:

- **`path`** (`Path`) – Existing local directory to clean pycache folders from.

Source code in `kedro/framework/cli/utils.py`

```
def _clean_pycache(path: Path) -> None:
    """Recursively clean all __pycache__ folders from `path`.

    Args:
        path: Existing local directory to clean __pycache__ folders from.
    """
    to_delete = [each.resolve() for each in path.rglob("__pycache__")]

    for each in to_delete:
        shutil.rmtree(each, ignore_errors=True)
```

### \_click_verbose

```
_click_verbose(func)
```

Click option for enabling verbose mode.

Source code in `kedro/framework/cli/utils.py`

```
def _click_verbose(func: Any) -> Any:
    """Click option for enabling verbose mode."""
    return click.option(
        "--verbose",
        "-v",
        is_flag=True,
        callback=_update_verbose_flag,
        help="See extensive logging and error stack traces.",
    )(func)
```

### \_config_file_callback

```
_config_file_callback(ctx, param, value)
```

CLI callback that replaces command line options with values specified in a config file. If command line options are passed, they override config file values.

Source code in `kedro/framework/cli/utils.py`

```
@typing.no_type_check
def _config_file_callback(ctx: click.Context, param: Any, value: Any) -> Any:
    """CLI callback that replaces command line options
    with values specified in a config file. If command line
    options are passed, they override config file values.
    """

    ctx.default_map = ctx.default_map or {}
    section = ctx.info_name

    if value:
        config = OmegaConf.to_container(OmegaConf.load(value))[section]
        for key, value in config.items():  # noqa: PLR1704
            _validate_config_file(key)
        ctx.default_map.update(config)

    return value
```

### \_find_run_command_in_plugins

```
_find_run_command_in_plugins(plugins)
```

Source code in `kedro/framework/cli/utils.py`

```
def _find_run_command_in_plugins(plugins: Any) -> Any:
    for group in plugins:
        if "run" in group.commands:
            return group.commands["run"]
```

### \_get_entry_points

```
_get_entry_points(name)
```

Get all kedro related entry points

Source code in `kedro/framework/cli/utils.py`

```
def _get_entry_points(name: str) -> Any:
    """Get all kedro related entry points"""
    return importlib.metadata.entry_points().select(  # type: ignore[no-untyped-call]
        group=ENTRY_POINT_GROUPS[name]
    )
```

### \_safe_load_entry_point

```
_safe_load_entry_point(entry_point)
```

Load entrypoint safely, if fails it will just skip the entrypoint.

Source code in `kedro/framework/cli/utils.py`

```
def _safe_load_entry_point(
    entry_point: Any,
) -> Any:
    """Load entrypoint safely, if fails it will just skip the entrypoint."""
    try:
        return entry_point.load()
    except Exception as exc:
        logger.warning(
            "Failed to load %s commands from %s. Full exception: %s",
            entry_point.module,
            entry_point,
            exc,
        )
        return
```

### \_split_load_versions

```
_split_load_versions(ctx, param, value)
```

Split and format the string coming from the --load-versions flag in kedro run, e.g.: "dataset1:time1,dataset2:time2" -> {"dataset1": "time1", "dataset2": "time2"}

Parameters:

- **`value`** (`str`) – the string with the contents of the --load-versions flag.

Returns:

- `dict[str, str]` – A dictionary with the formatted load versions data.

Source code in `kedro/framework/cli/utils.py`

```
def _split_load_versions(ctx: click.Context, param: Any, value: str) -> dict[str, str]:
    """Split and format the string coming from the --load-versions
    flag in kedro run, e.g.:
    "dataset1:time1,dataset2:time2" -> {"dataset1": "time1", "dataset2": "time2"}

    Args:
        value: the string with the contents of the --load-versions flag.

    Returns:
        A dictionary with the formatted load versions data.
    """
    if not value:
        return {}

    lv_tuple = tuple(chain.from_iterable(value.split(",") for value in [value]))

    load_versions_dict = {}
    for load_version in lv_tuple:
        load_version = load_version.strip()  # noqa: PLW2901
        load_version_list = load_version.split(":", 1)
        if len(load_version_list) != 2:  # noqa: PLR2004
            raise KedroCliError(
                f"Expected the form of 'load_versions' to be "
                f"'dataset_name:YYYY-MM-DDThh.mm.ss.sssZ',"
                f"found {load_version} instead"
            )
        load_versions_dict[load_version_list[0]] = load_version_list[1]

    return load_versions_dict
```

### \_split_params

```
_split_params(ctx, param, value)
```

Source code in `kedro/framework/cli/utils.py`

```
def _split_params(ctx: click.Context, param: Any, value: Any) -> Any:
    if isinstance(value, dict):
        return value
    dot_list = []
    for item in split_string(ctx, param, value):
        equals_idx = item.find("=")
        if equals_idx == -1:
            # If an equals sign is not found, fail with an error message.
            ctx.fail(
                f"Invalid format of `{param.name}` option: "
                f"Item `{item}` must contain a key and a value separated by `=`."
            )
        # Split the item into key and value
        key, _, val = item.partition("=")
        key = key.strip()
        if not key:
            # If the key is empty after stripping whitespace, fail with an error message.
            ctx.fail(
                f"Invalid format of `{param.name}` option: Parameter key "
                f"cannot be an empty string."
            )
        # Add "key=value" pair to dot_list.
        dot_list.append(f"{key}={val}")

    conf = OmegaConf.from_dotlist(dot_list)
    return OmegaConf.to_container(conf)
```

### \_suggest_cli_command

```
_suggest_cli_command(original_command_name, existing_command_names)
```

Source code in `kedro/framework/cli/utils.py`

```
def _suggest_cli_command(
    original_command_name: str, existing_command_names: Iterable[str]
) -> str:
    matches = difflib.get_close_matches(
        original_command_name, existing_command_names, MAX_SUGGESTIONS, CUTOFF
    )

    if not matches:
        return ""

    if len(matches) == 1:
        suggestion = "\n\nDid you mean this?"
    else:
        suggestion = "\n\nDid you mean one of these?\n"
    suggestion += textwrap.indent("\n".join(matches), " " * 4)
    return suggestion
```

### \_update_verbose_flag

```
_update_verbose_flag(ctx, param, value)
```

Source code in `kedro/framework/cli/utils.py`

```
def _update_verbose_flag(ctx: click.Context, param: Any, value: bool) -> None:
    KedroCliError.VERBOSE_ERROR = value
```

### \_validate_config_file

```
_validate_config_file(key)
```

Validate the keys provided in the config file against the accepted keys.

Source code in `kedro/framework/cli/utils.py`

```
def _validate_config_file(key: str) -> None:
    """Validate the keys provided in the config file against the accepted keys."""
    from kedro.framework.cli.project import run

    run_args = [click_arg.name for click_arg in run.params]
    run_args.remove("config")
    if key not in run_args:
        KedroCliError.VERBOSE_EXISTS = False
        message = _suggest_cli_command(key, run_args)  # type: ignore[arg-type]
        raise KedroCliError(
            f"Key `{key}` in provided configuration is not valid. {message}"
        )
```

### call

```
call(cmd, **kwargs)
```

Run a subprocess command and raise if it fails.

Parameters:

- **`cmd`** (`list[str]`) – List of command parts.
- **`**kwargs`** (`Any`, default: `{}` ) – Optional keyword arguments passed to subprocess.run.

Raises:

- `Exit` – If subprocess.run returns non-zero code.

Source code in `kedro/framework/cli/utils.py`

```
def call(cmd: list[str], **kwargs: Any) -> None:  # pragma: no cover
    """Run a subprocess command and raise if it fails.

    Args:
        cmd: List of command parts.
        **kwargs: Optional keyword arguments passed to `subprocess.run`.

    Raises:
        click.exceptions.Exit: If `subprocess.run` returns non-zero code.
    """
    click.echo(shlex.join(cmd))
    code = subprocess.run(cmd, **kwargs).returncode  # noqa: PLW1510, S603
    if code:
        raise click.exceptions.Exit(code=code)
```

### command_with_verbosity

```
command_with_verbosity(group, *args, **kwargs)
```

Custom command decorator with verbose flag added.

Source code in `kedro/framework/cli/utils.py`

```
def command_with_verbosity(group: click.core.Group, *args: Any, **kwargs: Any) -> Any:
    """Custom command decorator with verbose flag added."""

    def decorator(func: Any) -> Any:
        func = _click_verbose(func)
        func = group.command(*args, **kwargs)(func)
        return func

    return decorator
```

### env_option

```
env_option(func_=None, **kwargs)
```

Add `--env` CLI option to a function.

Source code in `kedro/framework/cli/utils.py`

```
def env_option(func_: Any | None = None, **kwargs: Any) -> Any:
    """Add `--env` CLI option to a function."""
    default_args = {"type": str, "default": None, "help": ENV_HELP}
    kwargs = {**default_args, **kwargs}
    opt = click.option("--env", "-e", **kwargs)
    return opt(func_) if func_ else opt
```

### find_run_command

```
find_run_command(package_name)
```

Find the run command to be executed. This is either the default run command defined in the Kedro framework or a run command defined by an installed plugin.

Parameters:

- **`package_name`** (`str`) – The name of the package being run.

Raises:

- `KedroCliError` – If the run command is not found.

Returns:

- `Callable` – Run command to be executed.

Source code in `kedro/framework/cli/utils.py`

```
def find_run_command(package_name: str) -> Callable:
    """Find the run command to be executed.
       This is either the default run command defined in the Kedro framework or a run command defined by
       an installed plugin.

    Args:
        package_name: The name of the package being run.

    Raises:
        KedroCliError: If the run command is not found.

    Returns:
        Run command to be executed.
    """
    try:
        project_cli = importlib.import_module(f"{package_name}.cli")
        # fail gracefully if cli.py does not exist
    except ModuleNotFoundError as exc:
        if f"{package_name}.cli" not in str(exc):
            raise
        plugins = load_entry_points("project")
        run = _find_run_command_in_plugins(plugins) if plugins else None
        if run:
            # use run command from installed plugin if it exists
            return run  # type: ignore[no-any-return]
        # use run command from `kedro.framework.cli.project`
        from kedro.framework.cli.project import run

        return run  # type: ignore[return-value]
    # fail badly if cli.py exists, but has no `cli` in it
    if not hasattr(project_cli, "cli"):
        raise KedroCliError(f"Cannot load commands from {package_name}.cli")
    return project_cli.run  # type: ignore[no-any-return]
```

### forward_command

```
forward_command(group, name=None, forward_help=False)
```

A command that receives the rest of the command line as 'args'.

Source code in `kedro/framework/cli/utils.py`

```
def forward_command(
    group: Any, name: str | None = None, forward_help: bool = False
) -> Any:
    """A command that receives the rest of the command line as 'args'."""

    def wrapit(func: Any) -> Any:
        func = click.argument("args", nargs=-1, type=click.UNPROCESSED)(func)
        func = command_with_verbosity(
            group,
            name=name,
            context_settings={
                "ignore_unknown_options": True,
                "help_option_names": [] if forward_help else ["-h", "--help"],
            },
        )(func)
        return func

    return wrapit
```

### load_entry_points

```
load_entry_points(name)
```

Load package entry point commands.

Parameters:

- **`name`** (`str`) – The key value specified in ENTRY_POINT_GROUPS.

Raises:

- `KedroCliError` – If loading an entry point failed.

Returns:

- `Sequence[Group]` – List of entry point commands.

Source code in `kedro/framework/cli/utils.py`

```
def load_entry_points(name: str) -> Sequence[click.Group]:
    """Load package entry point commands.

    Args:
        name: The key value specified in ENTRY_POINT_GROUPS.

    Raises:
        KedroCliError: If loading an entry point failed.

    Returns:
        List of entry point commands.

    """

    entry_point_commands = []
    for entry_point in _get_entry_points(name):
        loaded_entry_point = _safe_load_entry_point(entry_point)
        if loaded_entry_point:
            entry_point_commands.append(loaded_entry_point)
    return entry_point_commands
```

### python_call

```
python_call(module, arguments, **kwargs)
```

Run a subprocess command that invokes a Python module.

Source code in `kedro/framework/cli/utils.py`

```
def python_call(
    module: str, arguments: Iterable[str], **kwargs: Any
) -> None:  # pragma: no cover
    """Run a subprocess command that invokes a Python module."""
    call([sys.executable, "-m", module, *list(arguments)], **kwargs)
```

### split_node_names

```
split_node_names(ctx, param, to_split)
```

Split string by comma, ignoring commas enclosed by square parentheses. This avoids splitting the string of nodes names on commas included in default node names, which have the pattern ([,...]) -> [,...])

Note

- `to_split` will have such commas if and only if it includes a default node name. User-defined node names cannot include commas or square brackets.
- This function will no longer be necessary from Kedro 0.19.\*, in which default node names will no longer contain commas

Parameters:

- **`to_split`** (`str`) – the string to split safely

Returns:

- `list[str]` – A list containing the result of safe-splitting the string.

Source code in `kedro/framework/cli/utils.py`

```
def split_node_names(ctx: click.Context, param: Any, to_split: str) -> list[str]:
    """Split string by comma, ignoring commas enclosed by square parentheses.
    This avoids splitting the string of nodes names on commas included in
    default node names, which have the pattern
    <function_name>([<input_name>,...]) -> [<output_name>,...])

    Note:
        - `to_split` will have such commas if and only if it includes a
        default node name. User-defined node names cannot include commas
        or square brackets.
        - This function will no longer be necessary from Kedro 0.19.*,
        in which default node names will no longer contain commas

    Args:
        to_split: the string to split safely

    Returns:
        A list containing the result of safe-splitting the string.
    """
    result = []
    argument, match_state = "", 0
    for char in to_split + ",":
        if char == "[":
            match_state += 1
        elif char == "]":
            match_state -= 1
        if char == "," and match_state == 0 and argument:
            argument = argument.strip()
            result.append(argument)
            argument = ""
        else:
            argument += char
    return result
```

### split_string

```
split_string(ctx, param, value)
```

Split string by comma.

Source code in `kedro/framework/cli/utils.py`

```
def split_string(ctx: click.Context, param: Any, value: str) -> list[str]:
    """Split string by comma."""
    return [item.strip() for item in value.split(",") if item.strip()]
```

### validate_conf_source

```
validate_conf_source(ctx, param, value)
```

Validate the conf_source, only checking existence for local paths.

Source code in `kedro/framework/cli/utils.py`

```
def validate_conf_source(ctx: click.Context, param: Any, value: str) -> str | None:
    """Validate the conf_source, only checking existence for local paths."""
    if not value:
        return None

    # Check for remote URLs (except file://)
    if "://" in value and not value.startswith("file://"):
        return value

    # For local paths
    try:
        path = Path(value)
        if not path.exists():
            raise click.BadParameter(f"Path '{value}' does not exist.")
        return str(path.resolve())
    except click.BadParameter:
        # Re-raise Click exceptions
        raise
    except Exception as exc:
        # Wrap other exceptions
        raise click.BadParameter(f"Invalid path: {value}. Error: {exc!s}")
```
