# Source: https://docs.architect.co/getting-started-with-jupyter.md

# Getting started with Python (Jupyter)

We recommend using `uv` with the following `pyproject.toml`:

```toml
[project]
dependencies = [
    "architect-py",
    "numpy",
    "pandas",
]
description = "Add your description here"
name = "new-architect-project"
readme = "README.md"
requires-python = ">=3.12"
version = "0.1.0"
```

Then you can use one of the following commands to start a Jupyter notebook or lab session:

* `uv run --with jupyter jupyter notebook`
* `uv run --with jupyter jupyter lab`

Otherwise, in your own python environment, you can simply do

```
pip install architect-py
```

See [here](https://github.com/architect-xyz/architect-py/blob/main/examples/jupyter_example.ipynb) for a comprehensive example of a jupyter notebook.
