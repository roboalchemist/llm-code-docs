# Source: https://docs.anyscale.com/development/workspace-defaults.md

# Launch jobs and services from an Anyscale workspace

[View Markdown](/development/workspace-defaults.md)

# Launch jobs and services from an Anyscale workspace

This page provides an overview of the default configurations for jobs and services launched from workspaces.

When you submit jobs or deploy services from an Anyscale workspace, Anyscale automatically configures additional options and parameters to simplify the process of replicating your current development environment.

When you run a job or start a service, you're deploying a new Ray cluster. While it's possible to use workspaces to launch production workloads, most users package project dependencies by building stable images and use automation tools such as schedulers or CI/CD tools to deploy into production.

Jobs and services launched from workspaces inherit the following configurations from the workspace by default:

* Anyscale cloud.
* Anyscale project.
* Container image.
* Compute config.
* Working directory.
* Python packages.
* Environment variables.

## How do workspaces handle credentials?[​](#credentials "Direct link to How do workspaces handle credentials?")

When you create a workspace, Anyscale configures a cluster CLI token using the environmental variable `ANYSCALE_CLI_TOKEN`.

All requests through the CLI or SDK use this token to authenticate to Anyscale.

See [Manual CLI token configuration](/reference/quickstart-cli.md#cli-token).

### Credentials outside workspaces[​](#creds-outside "Direct link to Credentials outside workspaces")

When working in your local terminal, you configure permissions to Anyscale using the `anyscale login` CLI command.

The `ANYSCALE_CLI_TOKEN` variable takes precedence over the credentials configured by `anyscale login`, so authenticating this way in the workspace terminal doesn't change how you authenticate.

When configuring integrated services, Anyscale recommends using service accounts. See [Anyscale service accounts](/auth/service-accounts.md).

## Local files, code, and directories in workspaces[​](#files "Direct link to Local files, code, and directories in workspaces")

When you launch a job or service from the workspace, Anyscale packages all the files in your directory and loads them into your Ray nodes.

This means that you can seamlessly transition from running a Python script in the workspace terminal to deploying an Anyscale job with the CLI.

For example, if you have a script named `main.py`, the following command runs this in a workspace:

```
python main.py
```

Because Anyscale packages all the code for you when you submit a job from a workspace, you only need to define the entrypoint to run the script as a job, as in the following command:

```
anyscale job submit -- main.py
```

### Files and code outside workspaces[​](#files-and-code-outside-workspaces "Direct link to Files and code outside workspaces")

The Anyscale CLI and SDK use the `--working-dir` option to allow you to pass a directory of files into your Ray cluster. This directory becomes the current working directory for the launched cluster. You define the entrypoint to your application relative to the base of your working directory.

If you're developing code on your personal machine and you want to submit an Anyscale job using code and files on your local machine, pass the relative path to the directory containing your Ray application to the `--working-dir` option.

The following example syntax demonstrates this pattern, given the following:

* You have used your local terminal to change directories into the top level of your Ray application.
* A Python script named `main.py` is the entrypoint for your application.

```
anyscale job submit --working-dir . -- python main.py
```

note

If you use a job config or service config YAML, use the `working_dir` field to specify the path.

For speed and stability, Anyscale recommends packaging code alongside dependencies when building custom images to support production workloads.

## Packages and variables in workspaces[​](#packages-and-variables-in-workspaces "Direct link to Packages and variables in workspaces")

When you launch a job or service from the workspace, Anyscale uses the same container image and automatically configures any additional environment variables and Python packages you've added to your workspace.

note

If you're using uv on an Anyscale workspace, Anyscale automatically uses the `pyproject.toml` file defined in the top of your workspace directory to configure the environment for jobs or services. When using uv, Anyscale relies exclusively on the environment tracked by uv to define the cluster environment. You must set the entrypoint with `uv run` to use this feature.

You can use the **Dependencies** tab in the Anyscale console to view and edit Python packages and environment variables. Review the following sections for details and caveats.

### Dependencies in workspaces[​](#dependencies-in-workspaces "Direct link to Dependencies in workspaces")

Because Anyscale creates workspaces using container images, the container image defines most of the dependencies and packages in your workspace environment.

Anyscale only tracks Python packages installed with pip. You can install Python packages using `pip install` or use the **Dependencies** tab of the console to edit the list of installed packages.

All Python packages installed with pip are immediately available to system Python and all nodes in your workspace cluster. Ray clusters launched as jobs or services also include Python packages installed with pip.

Anyscale doesn't track other packages installed through the workspace terminal. If you need to install system dependencies using package managers such as APT, you must install these dependencies while building an image.

### Environment variables in workspaces[​](#env-var "Direct link to Environment variables in workspaces")

Anyscale's support for environment variables focuses primarily on setting environmental variables for your Ray workloads. This section describes the behavior of environment variables in workspaces.

Anyscale doesn't track environment variables declared from the workspace terminal as runtime dependencies. This has the following implications:

* Jobs and services launched from a workspace don't have access to environment variables you declare them in the terminal.
* You can reference environment variables declared in the terminal from non-Ray Python code, but these variables aren't available to code distributed by Ray.
* If you restart a workspace, environment variables previously defined in the workspace terminal are unavailable.

When you add or edit an environment variable in the **Dependencies** tab of the console, the behavior is as follows:

* All Ray nodes in your workspace cluster have access to the environment variable.
* Jobs and services launched from the workspace can access the environment variable.
* The system environment for your head node doesn't set the environment variable, meaning that you can't access it from the workspace terminal or non-Ray Python code.

Because of these behaviors, if you are actively developing with environment variables, Anyscale recommends the following:

* Always specify environment variables using the **Dependencies** tab in the Anyscale console.
* Restart your workspace to ensure that environment variables are available in the same contexts on your workspace cluster as clusters you launch for jobs or services.

note

Anyscale sets a number of environment variables during cluster initialization. See [Environment variables](/resources/environment-variables.md).

#### Test environment variables[​](#test-environment-variables "Direct link to Test environment variables")

You can optionally use the following code example to explore the behaviors for environment variables:

```
import os
import ray

print(os.environ['MY_VAR']) # Non-Ray Python code accessing the system environment

@ray.remote
def f():
    return os.environ['MY_VAR'] # Ray code accessing the Ray environment

print(ray.get(f.remote()))
```

### Manage environments outside workspaces[​](#manage-environments-outside-workspaces "Direct link to Manage environments outside workspaces")

The Anyscale CLI and SDK provide options to specify the image, environment variables, and Python packages required for your workload.

The following table provides an overview of the options you might use during development:

| CLI option       | Config option  | Description                                                        |
| ---------------- | -------------- | ------------------------------------------------------------------ |
| `--image-uri`    | `image_uri`    | The URI that identifies a container image.                         |
| `--ray-version`  | `ray_version`  | The Ray version used in your image.                                |
| `--env`          | `env_vars`     | Environment variables to define on top of your container image.    |
| `--requirements` | `requirements` | A list of pip requirements or a path to a `requirements.txt` file. |

If you are comfortable working with Dockerfile syntax, you might prefer to use the `--containerfile` option with a path to a valid Dockerfile. When you submit a job or launch a service using the `--containerfile` option, Anyscale builds and caches an optimized image from your Dockerfile definition in your data plane, then uses that image to launch your Ray cluster. This pattern works well for both development and production workloads.

Many Anyscale customers use CI/CD tools to automate testing of code and dependencies before building custom container images for deployment. Anyscale recommends against using the `--requirements` option to extend these images, as the additional library installation occurs for each node added to the cluster, which can increase latency and adds to network traffic.

Anyscale also supports uv for development, building images, and launching production workloads. See [Use uv to manage Python dependencies](/dependency-management/uv.md).
