# Source: https://docs.anyscale.com/dependency-management.md

# Dependency management on Anyscale

[View Markdown](/dependency-management.md)

# Dependency management on Anyscale

This page provides an overview of dependency management on Anyscale.

## What features does Anyscale provide for dependency management?[​](#features "Direct link to What features does Anyscale provide for dependency management?")

Anyscale provides a suite of features to help you manage dependencies throughout your project lifecycle. Broadly, features related to dependency management fall into the following buckets:

* Stable container images provided by Anyscale.
* Building and using custom container images.
* Features for iterative development in Anyscale workspaces.
* Options to customize Anyscale jobs and services.

The following table provides an overview of Anyscale features related to dependency management:

| Feature                  | Description                                                                                                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Base images              | Official Ray distributions packaged with common Python and system dependencies, maintained by Anyscale. See [Anyscale base images](/reference/base-images.md).                                                                                                                  |
| Custom images            | User-defined container images built on Anyscale or other third-party tools. Typically extend Anyscale base images with custom packages, environmental variables, code, init scripts, and other custom logic. See [Custom images on Anyscale](/container-image/custom-image.md). |
| Workspace containerfiles | Use containerfile syntax to iterate and build custom container images while working with Anyscale workspaces. See [Iterate on workspace container images](/dependency-management/containerfiles.md).                                                                            |
| uv                       | Use uv to manage Python packages and projects during dev or production with workspaces, jobs, or services. See [Use uv to manage Python dependencies](/dependency-management/uv.md).                                                                                            |
| Runtime environments     | Use runtime environments to add custom dependency management at any level of your Ray application, such as for tasks and actors. See [Runtime environments on Anyscale](/dependency-management/runtime-environment.md).                                                         |

These features provide you with flexibility to use the tools and patterns you're comfortable with for development. See [Develop Anyscale applications](/development.md).

For most use cases, Anyscale recommends packaging all code and dependencies as custom images before deploying workloads to production. See [Container-driven development on Anyscale](/development/containers.md).
