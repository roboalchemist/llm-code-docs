# Source: https://docs.anyscale.com/dependency-management/runtime-environment.md

# Runtime environments on Anyscale

[View Markdown](/dependency-management/runtime-environment.md)

# Runtime environments on Anyscale

This page provides an overview of using Ray runtime environments on Anyscale.

For an overview of how runtime environments and dependency management work when developing in Anyscale workspaces, see [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md).

See the following sections in the CLI and SDK reference for details on using runtime environments with Anyscale workspace, jobs, and services:

| Cluster type | CLI                                                                                     | SDK                                                                             | Config YAML                                                   |
| ------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Workspace    | [`anyscale workspace_v2 create`](/reference/workspaces.md#anyscale-workspace_v2-create) | [`anyscale.workspace.create`](/reference/workspaces.md#anyscaleworkspacecreate) | [`WorkspaceConfig`](/reference/workspaces.md#workspaceconfig) |
| Job          | [`anyscale job submit`](/reference/job-api.md#anyscale-job-submit)                      | [`anyscale.job.submit`](/reference/job-api.md#anyscalejobsubmit)                | [`JobConfig`](/reference/job-api.md#jobconfig)                |
| Service      | [`anyscale service deploy`](/reference/service-api.md#anyscale-service-deploy)          | [`anyscale.service.deploy`](/reference/service-api.md#anyscaleservicedeploy)    | [`ServiceConfig`](/reference/service-api.md#serviceconfig)    |

## What is a Ray runtime environment?[​](#what-is-a-ray-runtime-environment "Direct link to What is a Ray runtime environment?")

A Ray *runtime environment* describes a collection of dependencies installed to each node in your cluster when your Ray application launches or your cluster adds new nodes. Runtime environments extend the base environment for your Ray application.

Ray allows you to set runtime environments per-task, per-actor, or per-job in your Ray code. See [Ray docs on runtime environment](https://docs.ray.io/en/latest/ray-core/handling-dependencies.html#runtime-environments).

## How do runtime environments work on Anyscale?[​](#how-do-runtime-environments-work-on-anyscale "Direct link to How do runtime environments work on Anyscale?")

Anyscale uses Ray runtime environments to add dependencies, define environment variables, and inject user code on top of the container image used to initialize nodes.

For example, when you specify **Runtime dependencies** for workspaces using the Anyscale console, Anyscale applies these configurations at the app level by setting a runtime environment in `ray.init()`.

Anyscale provides interfaces to define runtime environment for workspaces in the Anyscale console, CLI, and SDK. Jobs and services provides runtime environment options in the CLI and SDK. You can define environment variables using option flags or within the configuration YAML for your workload.

The following table provides a high-level overview of the primary runtime environment options you can define in the config YAML for your Anyscale workspace, job, or service:

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `working_dir`  | Specifies a directory of files to inject as the current working directory in your Ray app. Use this option to add Python scripts, local modules, and other files from your development environment into your Ray nodes. For jobs and services, define your `entrypoint` relative to the path provided.<br /><br />Follows symlinks when present in the included directory. |
| `requirements` | Specifies the Python packages to install using pip. You can define this as a list of Python packages or a path to a `requirements.txt` file. If using a path, define it relative to your `working_dir`. Anyscale doesn't support all pip parameters.                                                                                                                       |
| `env_vars`     | Specifies system environment variables for your cluster. Specify environment variables as key-value pairs in a dictionary, where the key becomes the environment variable name.                                                                                                                                                                                            |

When you develop interactively with Anyscale workspaces, Anyscale automatically injects runtime environment settings into any job or service you launch from the workspace. See [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md).

## How do runtime environments in Ray code interact with Anyscale runtime environment features?[​](#how-do-runtime-environments-in-ray-code-interact-with-anyscale-runtime-environment-features "Direct link to How do runtime environments in Ray code interact with Anyscale runtime environment features?")

You can migrate Ray code that uses runtime environments to Anyscale and run it as-is, but Anyscale recommends refactoring your code to use Anyscale features.

Anyscale recommends against using runtime environments with `ray.init()` for most migrated code, as this can complicate dependency management. Some advanced users might choose to use runtime environments with image URIs to deploy multiple applications on a single cluster when using jobs or services. See [Multi-application services](/services/multi-app.md).

Anyscale doesn't sync runtime environments declared programmatically in Ray code back to the workspace **Dependency management** tab in the Anyscale console. Search your Ray code for the `runtime_env` option to discover runtime environments in your code.

The follow table describes the outcome of conflicts between dependencies set in both `ray.init()` and Anyscale runtime environment features:

| Dependency type       | Outcome of setting in code and Anyscale                                                                                                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Python packages       | Ray attempts to append packages set using Anyscale dependency management features to packages specified in `ray.init()`. In case of a conflict, Ray raises an error.                                                                                             |
| Environment variables | Ray first evaluates the environment variables set using Anyscale dependency management features, then evaluates environment variables specified using `ray.init()`. In case of conflict, the value set using `ray.init()` overrides the value set with Anyscale. |
| Working directory     | Ray always uses the working directory set in `ray.init()`. This includes overriding the default working directory typically used in Anyscale workspaces.                                                                                                         |

note

Runtime environments set at the actor or task level override runtime environments set by `ray.init()` or Anyscale runtime environment features.

## Use runtime environments for development[​](#use-runtime-environments-for-development "Direct link to Use runtime environments for development")

Runtime environments are one of the options available for quick iteration during development on Anyscale.

Anyscale recommends only using runtime environments during development. Runtime environments have the following disadvantages for production workloads:

* Runtime environments don't generate or use a lockfile for Python packages. Using runtime environments can make reliability and reproducibility difficult.
* Runtime environments install Python dependencies on top of container images, which slows down node initialization.
* You must configure permissions to use private package repositories.
* You must configure network permissions to allow access to package repositories.
* Network traffic to package managers can be a limiting factor when adding many nodes to a cluster.

To ensure stability and optimize Ray workloads on Anyscale, Anyscale recommends that you refactor dependencies from runtime environments to use custom images before moving to production.
