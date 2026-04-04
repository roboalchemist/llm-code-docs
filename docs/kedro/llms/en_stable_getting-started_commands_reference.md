# Source: https://docs.kedro.org/en/stable/getting-started/commands_reference/index.md

# Kedro's command line interface

Kedro's command line interface (CLI) lets you run Kedro commands through a terminal shell, such as the terminal app on macOS or cmd.exe and PowerShell on Windows. Use the CLI to set up a new Kedro project and to run it.

## Autocompletion (optional)

If you are using macOS or Linux, you can set up your shell to autocomplete `kedro` commands. If you do not know which shell you are using, first type the following:

```
echo $0
```

Add the following to your `~/.bashrc` (or run it on the command line):

```
eval "$(_KEDRO_COMPLETE=bash_source kedro)"
```

Add the following to `~/.zshrc`:

```
eval "$(_KEDRO_COMPLETE=zsh_source kedro)"
```

Add the following to `~/.config/fish/completions/foo-bar.fish`:

```
eval (env _KEDRO_COMPLETE=fish_source kedro)
```

## Invoke Kedro CLI from Python (optional)

You can invoke the Kedro CLI as a Python module:

```
python -m kedro
```

## Kedro commands

Kedro provides a set of CLI commands, which are automatically grouped and documented below using their inline docstrings.

- **Global commands** can be run from anywhere and are not tied to any specific Kedro project.
- **Project commands** must be run from within a Kedro project directory and apply to that project.

### Global Kedro commands

### kedro

**Usage:**

```
kedro [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

#### kedro new

Create a new kedro project.

**Usage:**

```
kedro new [OPTIONS]
```

**Options:**

```
  -v, --verbose                  See extensive logging and error stack traces.
  -c, --config PATH              Non-interactive mode, using a configuration
                                 yaml file. This file must supply  the keys
                                 required by the template's prompts.yml. When
                                 not using a starter, these are
                                 `project_name`, `repo_name` and
                                 `python_package`.
  -s, --starter TEXT             Specify the starter template to use when
                                 creating the project. This can be the path to
                                 a local directory, a URL to a remote VCS
                                 repository supported by `cookiecutter` or one
                                 of the aliases listed in ``kedro starter
                                 list``.
  --checkout TEXT                An optional tag, branch or commit to checkout
                                 in the starter repository.
  --directory TEXT               An optional directory inside the repository
                                 where the starter resides.
  -n, --name TEXT                The name of your new Kedro project.
  -t, --tools TEXT               Select which tools you'd like to include. By
                                 default, none are included.

                                 Tools

                                 1) Linting: Provides a basic linting setup
                                 with Ruff

                                 2) Testing: Provides basic testing setup with
                                 pytest

                                 3) Custom Logging: Provides more logging
                                 options

                                 4) Documentation: Basic documentation setup
                                 with Sphinx

                                 5) Data Structure: Provides a directory
                                 structure for storing data

                                 6) PySpark: Provides set up configuration for
                                 working with PySpark

                                 Example usage:

                                 kedro new
                                 --tools=lint,test,log,docs,data,pyspark (or
                                 any subset of these options)

                                 kedro new --tools=all

                                 kedro new --tools=none

                                 For more information on using tools, see http
                                 s://docs.kedro.org/en/stable/create/new_proje
                                 ct_tools/#tools-to-customise-a-new-kedro-
                                 project
  -e, --example TEXT             Enter y to enable, n to disable the example
                                 pipeline.
  -tc, --telemetry [yes|no|y|n]  Allow or not allow Kedro to collect usage
                                 analytics. We cannot see nor store
                                 information contained into a Kedro project.
                                 Opt in with "yes" and out with "no".
  -h, --help                     Show this message and exit.
```

#### kedro starter

Commands for working with project starters.

**Usage:**

```
kedro starter [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

##### kedro starter list

List all official project starters available.

**Usage:**

```
kedro starter list [OPTIONS]
```

**Options:**

```
  -h, --help  Show this message and exit.
```

### Project Kedro commands

### kedro

**Usage:**

```
kedro [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

#### kedro catalog

Commands for working with catalog.

**Usage:**

```
kedro catalog [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

##### kedro catalog describe-datasets

Describe datasets used in the specified pipelines, grouped by type.

This command provides a structured overview of datasets used in the selected pipelines, categorizing them into three groups:

- `datasets`: Datasets explicitly defined in the catalog.
- `factories`: Datasets resolved from dataset factory patterns.
- `defaults`: Datasets that do not match any pattern or explicit definition.

**Usage:**

```
kedro catalog describe-datasets [OPTIONS]
```

**Options:**

```
  -e, --env TEXT       Kedro configuration environment name. Defaults to
                       `local`.
  -p, --pipeline TEXT  Name of the modular pipeline to run. If not set, the
                       project pipeline is run by default.
  -h, --help           Show this message and exit.
```

##### kedro catalog list-patterns

List all dataset factory patterns in the catalog, ranked by priority.

This method retrieves all dataset factory patterns defined in the catalog, ordered by the priority in which they are matched.

**Usage:**

```
kedro catalog list-patterns [OPTIONS]
```

**Options:**

```
  -e, --env TEXT  Kedro configuration environment name. Defaults to `local`.
  -h, --help      Show this message and exit.
```

##### kedro catalog resolve-patterns

Resolve dataset factory patterns against pipeline datasets.

This method resolves dataset factory patterns for datasets used in the specified pipelines. It includes datasets explicitly defined in the catalog as well as those resolved from dataset factory patterns.

**Usage:**

```
kedro catalog resolve-patterns [OPTIONS]
```

**Options:**

```
  -e, --env TEXT       Kedro configuration environment name. Defaults to
                       `local`.
  -p, --pipeline TEXT  Name of the modular pipeline to run. If not set, the
                       project pipeline is run by default.
  -h, --help           Show this message and exit.
```

#### kedro ipython

Open IPython with project specific variables loaded.

Makes the following variables available in your IPython or Jupyter session:

- `catalog`: catalog instance that contains all defined datasets; this is a shortcut for `context.catalog`.
- `context`: Kedro project context that provides access to Kedro's library components.
- `pipelines`: Pipelines defined in your pipeline registry.
- `session`: Kedro session that orchestrates a pipeline run.

To reload these variables (e.g. if you updated `catalog.yml`) use the `%reload_kedro` line magic, which can also be used to see the error message if any of the variables above are undefined.

**Usage:**

```
kedro ipython [OPTIONS] [ARGS]...
```

**Options:**

```
  -v, --verbose   See extensive logging and error stack traces.
  -e, --env TEXT  Kedro configuration environment name. Defaults to `local`.
```

#### kedro jupyter

Open Jupyter Notebook / Lab with project specific variables loaded.

**Usage:**

```
kedro jupyter [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

##### kedro jupyter lab

Open Jupyter Lab with project specific variables loaded.

**Usage:**

```
kedro jupyter lab [OPTIONS] [ARGS]...
```

**Options:**

```
  -v, --verbose   See extensive logging and error stack traces.
  -e, --env TEXT  Kedro configuration environment name. Defaults to `local`.
```

##### kedro jupyter notebook

Open Jupyter Notebook with project specific variables loaded.

**Usage:**

```
kedro jupyter notebook [OPTIONS] [ARGS]...
```

**Options:**

```
  -v, --verbose   See extensive logging and error stack traces.
  -e, --env TEXT  Kedro configuration environment name. Defaults to `local`.
```

##### kedro jupyter setup

Initialise the Jupyter Kernel for a kedro project.

**Usage:**

```
kedro jupyter setup [OPTIONS] [ARGS]...
```

**Options:**

```
  -v, --verbose  See extensive logging and error stack traces.
```

#### kedro package

Package the Kedro project as a Python wheel and export the configuration.

This command builds a `.whl` file for the project and saves it to the `dist/` directory. It also packages the project's configuration (excluding any `local/*.yml` files) into a separate `tar.gz` archive for deployment or sharing.

Both artifacts will appear in the `dist/` folder, unless an older project layout is detected.

**Usage:**

```
kedro package [OPTIONS]
```

**Options:**

```
  -h, --help  Show this message and exit.
```

#### kedro pipeline

Commands for working with pipelines.

**Usage:**

```
kedro pipeline [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

##### kedro pipeline create

Create a new modular pipeline by providing a name.

**Usage:**

```
kedro pipeline create [OPTIONS] NAME
```

**Options:**

```
  -v, --verbose             See extensive logging and error stack traces.
  --skip-config             Skip creation of config files for the new
                            pipeline(s).
  -t, --template DIRECTORY  Path to cookiecutter template to use for
                            pipeline(s). Will override any local templates.
  -e, --env TEXT            Environment to create pipeline configuration in.
                            Defaults to `base`.
  -h, --help                Show this message and exit.
```

##### kedro pipeline delete

Delete a modular pipeline by providing a name.

**Usage:**

```
kedro pipeline delete [OPTIONS] NAME
```

**Options:**

```
  -v, --verbose   See extensive logging and error stack traces.
  -e, --env TEXT  Environment to delete pipeline configuration from. Defaults
                  to 'base'.
  -y, --yes       Confirm deletion of pipeline non-interactively.
  -h, --help      Show this message and exit.
```

#### kedro registry

Commands for working with registered pipelines.

**Usage:**

```
kedro registry [OPTIONS] COMMAND [ARGS]...
```

**Options:**

```
  -h, --help  Show this message and exit.
```

##### kedro registry describe

Describe a registered pipeline by providing a pipeline name. Defaults to the `__default__` pipeline.

**Usage:**

```
kedro registry describe [OPTIONS] [NAME]
```

**Options:**

```
  -v, --verbose  See extensive logging and error stack traces.
  -h, --help     Show this message and exit.
```

##### kedro registry list

List all pipelines defined in your pipeline_registry.py file.

**Usage:**

```
kedro registry list [OPTIONS]
```

**Options:**

```
  -h, --help  Show this message and exit.
```

#### kedro run

Run the pipeline.

**Usage:**

```
kedro run [OPTIONS]
```

**Options:**

```
  --from-inputs TEXT         A list of dataset names which should be used as a
                             starting point.
  --to-outputs TEXT          A list of dataset names which should be used as
                             an end point.
  --from-nodes TEXT          A list of node names which should be used as a
                             starting point.
  --to-nodes TEXT            A list of node names which should be used as an
                             end point.
  -n, --nodes TEXT           Run only nodes with specified names.
  -r, --runner TEXT          Specify a runner that you want to run the
                             pipeline with. Available runners:
                             'SequentialRunner', 'ParallelRunner' and
                             'ThreadRunner'.
  --async                    Load and save node inputs and outputs
                             asynchronously with threads. If not specified,
                             load and save datasets synchronously.
  -e, --env TEXT             Kedro configuration environment name. Defaults to
                             `local`.
  -t, --tags TEXT            Construct the pipeline using only nodes which
                             have this tag attached. Option can be used
                             multiple times, what results in a pipeline
                             constructed from nodes having any of those tags.
  -lv, --load-versions TEXT  Specify a particular dataset version (timestamp)
                             for loading.
  -p, --pipeline TEXT        Name of the registered pipeline to run. If not
                             set, the '__default__' pipeline is run.
  --pipelines TEXT           Comma-separated names of registered pipelines to
                             run. Example: --pipelines
                             data_engineering,feature_engineering If not set,
                             the '__default__' pipeline is run.
  -ns, --namespaces TEXT     Run only node namespaces with specified names.
  -c, --config FILE          Specify a YAML configuration file to load the run
                             command arguments from. If command line arguments
                             are provided, they will override the loaded ones.
  --conf-source TEXT         Path of a directory where project configuration
                             is stored.
  --params TEXT              Specify extra parameters that you want to pass to
                             the context initialiser. Items must be separated
                             by comma, keys - by colon or equals sign,
                             example: param1=value1,param2=value2. Each
                             parameter is split by the first comma, so
                             parameter values are allowed to contain colons,
                             parameter keys are not. To pass a nested
                             dictionary as parameter, separate keys by '.',
                             example: param_group.param1:value1.
  --only-missing-outputs     Run only nodes with missing outputs. If all
                             outputs of a node exist and are persisted, skip
                             the node execution.
  -h, --help                 Show this message and exit.
```

## Customise or override project-specific Kedro commands

Note

Project-related CLI commands can be run from any subdirectory within a Kedro project.

Kedro's command line interface (CLI) allows you to associate a set of commands and dependencies with a target, which you can then execute from inside the project directory.

The commands a project supports are specified on the framework side. If you want to customise any of the Kedro commands you can do this either by adding a file called `cli.py` or by injecting commands into it through the [`plugin` framework](https://docs.kedro.org/en/stable/extend/plugins/index.md). Find the template for the `cli.py` file below.

View code

```
"""Command line tools for manipulating a Kedro project.
Intended to be invoked via `kedro`."""
import click
from kedro.framework.cli.project import (
    ASYNC_ARG_HELP,
    CONFIG_FILE_HELP,
    CONF_SOURCE_HELP,
    FROM_INPUTS_HELP,
    FROM_NODES_HELP,
    LOAD_VERSION_HELP,
    NODE_ARG_HELP,
    PARAMS_ARG_HELP,
    PIPELINE_ARG_HELP,
    RUNNER_ARG_HELP,
    TAG_ARG_HELP,
    TO_NODES_HELP,
    TO_OUTPUTS_HELP,
)
from kedro.framework.cli.utils import (
    CONTEXT_SETTINGS,
    _config_file_callback,
    _split_params,
    _split_load_versions,
    env_option,
    split_string,
    split_node_names,
)
from kedro.framework.session import KedroSession
from kedro.utils import load_obj


@click.group(context_settings=CONTEXT_SETTINGS, name=__file__)
def cli():
    """Command line tools for manipulating a Kedro project."""
@cli.command()

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
def run(
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
    config: str,
    conf_source: str,
    params: dict[str, Any],
    namespaces: str,
    only_missing_outputs: bool,
) -> dict[str, Any]:
    """Run the pipeline."""

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
            namespaces=namespaces,
            only_missing_outputs=only_missing_outputs,
        )
```
