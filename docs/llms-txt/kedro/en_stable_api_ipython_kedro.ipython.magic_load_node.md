# Source: https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.magic_load_node/index.md

## kedro.ipython.magic_load_node

```
magic_load_node(args)
```

The line magic %load_node . Currently, this feature is only available for Jupyter Notebook (>7.0), Jupyter Lab, IPython, and VSCode Notebook. This line magic will generate code in multiple cells to load datasets from `DataCatalog`, import relevant functions and modules, node function definition and a function call. If generating code is not possible, it will print the code instead.

Source code in `kedro/ipython/__init__.py`

```
@typing.no_type_check
@magic_arguments()
@argument(
    "node",
    type=str,
    help=("Name of the Node."),
    nargs="?",
    default=None,
)
def magic_load_node(args: str) -> None:
    """The line magic %load_node <node_name>.
    Currently, this feature is only available for Jupyter Notebook (>7.0), Jupyter Lab, IPython,
    and VSCode Notebook. This line magic will generate code in multiple cells to load
    datasets from `DataCatalog`, import relevant functions and modules, node function
    definition and a function call. If generating code is not possible, it will print
    the code instead.
    """
    parameters = parse_argstring(magic_load_node, args)
    node_name = parameters.node

    cells = _load_node(node_name, pipelines)

    run_environment = _guess_run_environment()

    if run_environment in ("ipython", "vscode", "jupyter"):
        # Combine multiple cells into one for IPython or VSCode or Jupyter
        combined_cell = "\n\n".join(cells)
        _create_cell_with_text(combined_cell)
    else:
        # For other environments or if detection fails, just print the cells
        _print_cells(cells)
```
