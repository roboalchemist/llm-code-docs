# Source: https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.load_ipython_extension/index.md

## kedro.ipython.load_ipython_extension

```
load_ipython_extension(ipython)
```

Main entry point when %load_ext kedro.ipython is executed, either manually or automatically through `kedro ipython` or `kedro jupyter lab/notebook`. IPython will look for this function specifically. See https://ipython.readthedocs.io/en/stable/config/extensions/index.html

Source code in `kedro/ipython/__init__.py`

```
def load_ipython_extension(ipython: InteractiveShell) -> None:
    """
    Main entry point when %load_ext kedro.ipython is executed, either manually or
    automatically through `kedro ipython` or `kedro jupyter lab/notebook`.
    IPython will look for this function specifically.
    See https://ipython.readthedocs.io/en/stable/config/extensions/index.html
    """
    ipython.register_magic_function(func=magic_reload_kedro, magic_name="reload_kedro")  # type: ignore[call-arg]
    logger.info("Registered line magic '%reload_kedro'")
    ipython.register_magic_function(func=magic_load_node, magic_name="load_node")  # type: ignore[call-arg]
    logger.info("Registered line magic '%load_node'")

    if find_kedro_project(Path.cwd()) is None:
        logger.warning(
            "Kedro extension was registered but couldn't find a Kedro project. "
            "Make sure you run '%reload_kedro <project_root>'."
        )
        return

    reload_kedro()
```
