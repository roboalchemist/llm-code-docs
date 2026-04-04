# Source: https://render.com/docs/uv-version.md

# Setting Your uv Version


| Current default uv version |
| --- |
| *`0.10.2`* |

[uv](https://docs.astral.sh/uv/) is a packaging and dependency manager for Python. Render automatically adds uv to your Python service's runtime if your project's root directory includes a `uv.lock` file.

To specify a uv version, set your service's `UV_VERSION` [environment variable](configure-environment-variables) to any version number that's compatible with your [Python version](python-version).

## History of default uv versions

| Service Creation Date | Default uv Version |
|---|---|
| 2026-02-11 and later | `0.10.2` |
| Before 2025-06-12 | `0.7.12` |
