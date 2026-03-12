# Source: https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.magic_reload_kedro/index.md

## kedro.ipython.magic_reload_kedro

```
magic_reload_kedro(line, local_ns=None, conf_source=None)
```

The `%reload_kedro` IPython line magic. See https://docs.kedro.org/en/stable/integrations-and-plugins/notebooks_and_ipython/kedro_and_notebooks/#reload_kedro-line-magic for more.

Source code in `kedro/ipython/__init__.py`

```
@typing.no_type_check
@needs_local_scope
@magic_arguments()
@argument(
    "path",
    type=str,
    help=(
        "Path to the project root directory. If not given, use the previously set"
        "project root."
    ),
    nargs="?",
    default=None,
)
@argument("-e", "--env", type=str, default=None, help=ENV_HELP)
@argument(
    "--params",
    type=lambda value: _split_params(None, None, value),
    default=None,
    help=PARAMS_ARG_HELP,
)
@argument("--conf-source", type=str, default=None, help=CONF_SOURCE_HELP)
def magic_reload_kedro(
    line: str,
    local_ns: dict[str, Any] | None = None,
    conf_source: str | None = None,
) -> None:
    """
    The `%reload_kedro` IPython line magic.
    See https://docs.kedro.org/en/stable/integrations-and-plugins/notebooks_and_ipython/kedro_and_notebooks/#reload_kedro-line-magic
    for more.
    """
    args = parse_argstring(magic_reload_kedro, line)
    reload_kedro(args.path, args.env, args.params, local_ns, args.conf_source)
```
