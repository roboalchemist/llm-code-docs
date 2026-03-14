# Source: https://docs.anyscale.com/dependency-management/uv.md

# Use uv to manage Python dependencies

[View Markdown](/dependency-management/uv.md)

# Use uv to manage Python dependencies

You can use uv to run Ray scripts and manage dependencies throughout the development lifecycle on Anyscale.

warning

Support for uv on Anyscale is in beta. If you run into any issues, contact [Anyscale support](mailto:support@anyscale.com).

To use `uv run` to distribute the Python environment to all nodes in the Ray cluster with Ray 2.47.0 or earlier, you must set the following environment variable in your container:

```
RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook
```

For an example of using uv for project management during iterative development, see [Tutorial: Use uv to iterate in an Anyscale workspace](/dependency-management/uv-workspace-tutorial.md).

## What is uv?[​](#what-is "Direct link to What is uv?")

uv is a Python package and project manager. Due to its speed, ease of use, and features, many Python developers have adopted uv. Anyscale is actively working with the Ray community to build robust support for uv in Ray.

uv simplifies project management by replacing numerous tools to manage dependencies and environments. When you run a Python application with `uv run`, uv pulls in all the relevant Python dependencies and runs the script in the environment.

For complete documentation on uv, see the [uv docs](https://docs.astral.sh/uv/).

## How does uv work on Anyscale?[​](#how-it-works "Direct link to How does uv work on Anyscale?")

Ray provides a native integration with uv through a runtime environment plugin. This ensures that all nodes in the Ray cluster use the `uv run` command to run Python executors for your Ray tasks and actors.

When you run your Ray scripts with `uv run`, uv manages all aspects of the environment your code runs in. This means that uv ignores dependencies and runtime environments in your current Ray cluster, instead using the environment and dependencies you've configured with uv.

To use uv with Ray in Anyscale, you must do the following:

* Launch your Ray cluster using an image with uv installed.
* Run your scripts with the `uv run` command.

When used correctly, uv can simplify management for Anyscale environments and dependencies.

The following sections provide examples for configuring base images and running application code with uv.

## Build an image from a pyproject.toml file[​](#build-an-image-from-a-pyprojecttoml-file "Direct link to Build an image from a pyproject.toml file")

The following is an example Dockerfile definition that installs uv, copies the `pyproject.toml` from your current working directory, and then installs all dependencies.

note

The following code example assumes that you're building the Dockerfile in a directory that contains all the code for your project. You can configure this manually on your personal machine after cloning a project from your Git repository. Anyscale recommends using this pattern during the artifact build phase of your CI/CD pipeline.

```
# Start with an Anyscale base image.
FROM anyscale/ray:2.46.0-slim-py312-cu128

# Install uv.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set the uv runtime hook.
RUN echo "export RAY_RUNTIME_ENV_HOOK=ray._private.runtime_env.uv_runtime_env_hook.hook" >> /home/ray/.bashrc

# If you're developing using workspace containerfiles, add the following:
# COPY --chown=ray:ray working_dir /home/ray/default/
# RUN cd /home/ray/default/ && ...

# Copy the pyproject.toml and install dependencies.
COPY pyproject.toml .
RUN uv pip install -r pyproject.toml

# Copy the rest of the uv project from your local directory and install any remaining dependencies.
COPY . .
RUN uv pip install -e .
```

## Use uv with an Anyscale job[​](#use-uv-with-an-anyscale-job "Direct link to Use uv with an Anyscale job")

If you're developing a Ray application locally with uv, you can define a job configuration YAML and use it to submit the entire project to an Anyscale job to run the code.

The following example job config YAML uses a custom uv image created or uploaded to Anyscale and passes the content in your local current working directory to the job, providing access to the `pyproject.toml` and all code in your uv project:

```
name: uv-test-job
image_uri: anyscale/image/uv-job-image:1
entrypoint: uv run job.py
working_dir: .
```

To use this pattern, create a `config.yaml` file in your project directory, then run the following in your local terminal:

```
anyscale job submit config.yaml
```

## Submit a job with uv from a workspace[​](#submit-a-job-with-uv-from-a-workspace "Direct link to Submit a job with uv from a workspace")

If you're using uv in an Anyscale workspace to develop a Ray application, you can use the web terminal to test your application as an Anyscale job.

The following example syntax runs your application using an Anyscale job using the code in a file named `main.py`:

```
anyscale job submit -- uv run main.py
```

When you submit a job in this way, Anyscale uses the environment defined in the `pyproject.toml` in the top of your directory structure to configure the environment in your job containers. In this way, uv fully isolates your job cluster from the environment in your workspace.

## Using Anyscale Runtime with uv[​](#using-anyscale-runtime-with-uv "Direct link to Using Anyscale Runtime with uv")

If you're using Ray in your uv environment, you can use a local PyPI endpoint to substitute Ray with Anyscale Runtime. The local PyPI server is available in Anyscale workspaces, jobs, and services. This section walks you through how to do this for a new project and how to update an existing `pyproject.toml` and `uv.lock` file.

### Create a project with Anyscale Runtime[​](#create-a-project-with-anyscale-runtime "Direct link to Create a project with Anyscale Runtime")

To create a new uv project that uses Anyscale Runtime, first set the `UV_INDEX` environment variable and then initialize your project:

```
export UV_INDEX="anyscale=http://localhost:9478/simple"
uv init
uv add ray
```

This produces a `pyproject.toml` with the Anyscale index configured, such as the following:

```
[project]
name = "default"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "ray>=2.53.0",
]

[tool.uv.sources]
ray = { index = "anyscale" }

[[tool.uv.index]]
name = "anyscale"
url = "http://localhost:9478/simple"
```

### Update a project to use Anyscale Runtime[​](#update-a-project-to-use-anyscale-runtime "Direct link to Update a project to use Anyscale Runtime")

If you have an existing `pyproject.toml` and `uv.lock` that already include Ray, you can update them to use Anyscale Runtime using the following steps.

Add the following block to your `pyproject.toml`:

```
[tool.uv.sources]
ray = { index = "anyscale" }

[[tool.uv.index]]
name = "anyscale"
url = "http://localhost:9478/simple"
```

Run the following command to refresh your lock file and reinstall Ray to pick up the Anyscale Runtime version:

```
uv sync --refresh --reinstall-package ray
```

### Verify Anyscale Runtime installation[​](#verify-anyscale-runtime-installation "Direct link to Verify Anyscale Runtime installation")

Import the `ray.anyscale` Python module to validate that the Anyscale Runtime is available for your workload, as in the following example.

Run the following command to start a new Python session:

```
uv run python
```

Run the following imports to confirm the `ray.anyscale` module imports without errors:

```
import ray
import ray.anyscale
```
