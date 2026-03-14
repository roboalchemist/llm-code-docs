# Source: https://docs.anyscale.com/development.md

# Develop Anyscale applications

[View Markdown](/development.md)

# Develop Anyscale applications

This page provides recommended best practices while developing Anyscale applications. For an overview of how Anyscale uses containers and the full Ray application lifecycle, see [Container-driven development on Anyscale](/development/containers.md).

## Differences between developing on Anyscale workspaces and on your local machine[​](#differences "Direct link to Differences between developing on Anyscale workspaces and on your local machine")

When you develop in an Anyscale workspace, you have access to development tools in the Anyscale console to write and iterate on code, manage dependencies, and configure workloads.

When you develop locally with an IDE running on your own machine, you submit applications for testing on Anyscale jobs or services using the Anyscale CLI or SDK. These developer tools have access to many of the same dependency management features as workspaces, but you interact with them through options while configuring or launching your Ray cluster. See [Anyscale API reference](/reference.md).

When you work in an Anyscale workspace, Anyscale manages injecting certain dependencies into your Ray clusters. See [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md).

## Iterate on code[​](#iterate-code "Direct link to Iterate on code")

Anyscale recommends using Git for code versioning and portability. Anyscale workloads might require simultaneous edits to code in multiple repositories. For example, you might define your core workload logic in one repository and import helper functions or boilerplate logic from other repositories.

If you're developing in an Anyscale workspace, configure your Git credentials to connect your workspace to a Git provider. Clone code from one or more repositories into the working directory for your workspace. Sync changes back to your remote Git repository. See [Connect to GitHub](/platform/workspaces/workspaces-git.md).

Workspaces automatically make all directories and files in your workspace available on Ray nodes in your workspace cluster or launched as jobs or services from the web terminal.

When you're developing locally, if you choose to include all files and custom Python modules in a single directory, you can submit them to an Anyscale job or service using the `working_dir` option. You can also use the `py_module` option to include Python modules sourced from other locations on your local machine.

note

While you can use Jupyter notebooks during data exploration and interactive development, Anyscale recommends refactoring code from notebooks into Python scripts and modules before moving to production with jobs or services.

## Manage Python dependencies during development[​](#python-deps "Direct link to Manage Python dependencies during development")

Anyscale supports the following patterns for managing Python dependencies during development:

| Pattern                       | Description                                                                                                                                                                                                                                                                                  |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime dependencies          | Define Python packages to `pip install` using the **Dependencies** tab of the Anyscale console or the `requirements` option for the CLI or SDK. Runtime dependencies extend Ray runtime environments. See [Runtime environments on Anyscale](/dependency-management/runtime-environment.md). |
| Custom images                 | You can include Python packages in custom images, such as those you build on Anyscale. See [Build a custom image on Anyscale](/container-image/build-image.md).                                                                                                                              |
| Edit workspace containerfiles | Use containerfile syntax to add Python dependencies to the container image in your workspace cluster. Jobs and services launched from the workspace use the same image. See [Iterate on workspace container images](/dependency-management/containerfiles.md).                               |
| uv                            | Use uv as an alternate approach to runtime dependencies for installing and managing Python dependencies during workspace development. See [Use uv to manage Python dependencies](/dependency-management/uv.md).                                                                              |

Use lockfiles, `pyproject.toml` files, and `requirements.txt` files to freeze the dependencies for your development environment, then use these files to define a custom image. See [Refactor development patterns to define custom images](/development/containers.md#define-image).

## Manage system packages during development[​](#system-packages "Direct link to Manage system packages during development")

You can install system packages on your driver node using the web terminal in an Anyscale workspace, but these packages don't persist when the cluster restarts.

When developing in a local IDE, local code execution or testing might rely on system packages on your personal machine. If you launch an Anyscale job or service using an Anyscale base image, these system packages might not be available. See [Anyscale base images](/reference/base-images.md).

You must install and configure system packages in a containerfile and build a custom image to ensure that Anyscale distributes these packages to all nodes in your Ray cluster. You can iteratively edit your container image to make system packages available when developing with workspaces. See [Iterate on workspace container images](/dependency-management/containerfiles.md).

You can use init scripts to define common system package installations and configurations. See [Use init scripts with custom images](/dependency-management/init-scripts.md).

## Manage environment variables during development[​](#env-vars "Direct link to Manage environment variables during development")

Anyscale supports the following patterns for managing environment variables during development:

| Pattern                       | Description                                                                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runtime dependencies          | Define environment variables using the **Dependencies** tab of the Anyscale console or the `env` option for the CLI or SDK. See [Runtime environments on Anyscale](/dependency-management/runtime-environment.md).                                               |
| Custom images                 | You can define environment variables in custom images, such as those you build on Anyscale. See [Build a custom image on Anyscale](/container-image/build-image.md).                                                                                             |
| Edit workspace containerfiles | Use containerfile syntax to add environment variables to the container image in your workspace cluster. Jobs and services launched from the workspace use the same image. See [Iterate on workspace container images](/dependency-management/containerfiles.md). |

Environment variable set interactively on your Anyscale workspace might not be available on nodes in your Ray cluster. See [Environment variables in workspaces](/development/workspace-defaults.md#env-var).

When developing locally, you might rely on environment variables that aren't available on Anyscale. You might also use patterns such as the following to programmatically set environment variables within your Python scripts:

```
import os
os.environ["VAR_NAME"] = "value"
```

Depending on how you've structured your Ray code, environment variables set this way might only be available in the driver environment. Use Anyscale built-in functionality for managing environment variables to simplify this pattern.

To avoid passing passwords and tokens in plaintext, refactor your code to use secrets. See [Secret management on Anyscale](/secrets.md).
