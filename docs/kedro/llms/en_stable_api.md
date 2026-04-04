# Source: https://docs.kedro.org/en/stable/api/index.md

Kedro is a framework that makes it easy to build robust and scalable data pipelines by providing uniform project templates, data abstraction, configuration and pipeline assembly.

## Modules

| Name                                                                                         | Description                                                                                             |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [`kedro.config`](https://docs.kedro.org/en/stable/api/config/kedro.config/index.md)          | Provides functionality for loading Kedro configuration from different file formats.                     |
| [`kedro.framework`](https://docs.kedro.org/en/stable/api/framework/kedro.framework/index.md) | Provides Kedro's framework components.                                                                  |
| [`kedro.io`](https://docs.kedro.org/en/stable/api/io/kedro.io/index.md)                      | Provides functionality to read and write to a number of datasets.                                       |
| [`kedro.ipython`](https://docs.kedro.org/en/stable/api/ipython/kedro.ipython/index.md)       | This script creates an IPython extension to load Kedro-related variables in local scope.                |
| [`kedro.logging`](https://docs.kedro.org/en/stable/api/kedro.logging/index.md)               |                                                                                                         |
| [`kedro.pipeline`](https://docs.kedro.org/en/stable/api/pipeline/kedro.pipeline/index.md)    | Provides functionality to define and execute data-driven pipelines.                                     |
| [`kedro.runner`](https://docs.kedro.org/en/stable/api/runner/kedro.runner/index.md)          | Provides runners that are able to execute Pipeline instances.                                           |
| [`kedro.utils`](https://docs.kedro.org/en/stable/api/kedro.utils/index.md)                   | This module provides a set of helper functions being used across different components of Kedro package. |

## Functions

| Name                                                                                                   | Description |
| ------------------------------------------------------------------------------------------------------ | ----------- |
| [`load_ipython_extension`](https://docs.kedro.org/en/stable/api/kedro.load_ipython_extension/index.md) |             |

## Exceptions

| Name                                                                                                         | Description                                                             |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| [`KedroDeprecationWarning`](https://docs.kedro.org/en/stable/api/kedro.KedroDeprecationWarning/index.md)     | Custom class for warnings about deprecated Kedro features.              |
| [`KedroPythonVersionWarning`](https://docs.kedro.org/en/stable/api/kedro.KedroPythonVersionWarning/index.md) | Custom class for warnings about incompatibilities with Python versions. |
