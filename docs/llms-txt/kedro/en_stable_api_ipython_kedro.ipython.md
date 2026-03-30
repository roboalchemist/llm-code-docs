# Source: https://docs.kedro.org/en/stable/api/ipython/kedro.ipython/index.md

## kedro.ipython

This script creates an IPython extension to load Kedro-related variables in local scope.

| Name                                                                                                                   | Type     | Description                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`load_ipython_extension`](https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.load_ipython_extension/index.md) | Function | Main entry point when `%load_ext kedro.ipython` is executed, either manually or automatically through Kedro IPython or Kedro Jupyter Lab/Notebook. |
| [`magic_load_node`](https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.magic_load_node/index.md)               | Function | .                                                                                                                                                  |
| [`magic_reload_kedro`](https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.magic_reload_kedro/index.md)         | Function | .                                                                                                                                                  |
| [`reload_kedro`](https://docs.kedro.org/en/stable/api/ipython/kedro.ipython.reload_kedro/index.md)                     | Function | Function that underlies the `%reload_kedro` Line magic.                                                                                            |
