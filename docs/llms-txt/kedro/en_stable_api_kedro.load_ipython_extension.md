# Source: https://docs.kedro.org/en/stable/api/kedro.load_ipython_extension/index.md

## kedro.load_ipython_extension

```
load_ipython_extension(ipython)
```

Source code in `kedro/__init__.py`

```
def load_ipython_extension(ipython: InteractiveShell) -> None:
    import kedro.ipython

    kedro.ipython.load_ipython_extension(ipython)
```
