# Source: https://docs.anyscale.com/development/containers.md

# Container-driven development on Anyscale

[View Markdown](/development/containers.md)

# Container-driven development on Anyscale

This article provides an overview of developing in containers and provides recommendations for each stage in your development lifecycle.

## How does Anyscale use containers?[​](#how-does-anyscale-use-containers "Direct link to How does Anyscale use containers?")

Anyscale uses containers for deploying nodes in Ray clusters for workspaces, jobs, and services.

Each container is a replica of an immutable container image specified as part of the cluster definition. See [Define a Ray cluster](/configuration.md) and [What is a container image?](/container-image.md).

Anyscale recommends using managed base images when beginning development on a new workload. Users with a good grasp of containers might choose to build a custom image that extends a base image with their own dependencies, environmental variables, or init scripts before starting development.

For users new to the Anyscale platform or developing in containers, you can launch an Anyscale workspace using a base image and then iterate on this image using the Anyscale console. See [Runtime environments on Anyscale](/dependency-management/runtime-environment.md).

When you prepare your workload for production, you create a custom image that extends an Anyscale base image to add additional dependencies, code assets, and environmental variables. See [Custom images on Anyscale](/container-image/custom-image.md).

## What are the primary components of an Anyscale application?[​](#what-are-the-primary-components-of-an-anyscale-application "Direct link to What are the primary components of an Anyscale application?")

Anyscale launches Ray clusters as workspaces, jobs, or services.

Despite the differences in use cases for workspaces, jobs, and services, they all use the same two primary constructs for configuring and defining the Ray cluster and application: compute configurations and container images. See [Define a Ray cluster](/configuration.md).

When you are developing a new application on Anyscale, you are iterating on the code that you either package as a container image or inject using a runtime environment to submit to a Ray cluster. The following table provides an overview of the key components you need to iterate on during development:

| Application component | Description                                                                | Examples                                                                                                    |
| --------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Codebase              | The code and configuration files that define your workload or application. | Python Ray scripts, Python modules, Bash scripts, YAML configurations.                                      |
| Python dependencies   | Python packages from a public or private package index.                    | PyPi packages, Python libraries in index mirrors or caches, Python libraries from custom repositories.      |
| System packages       | Packages installed on the base Ubuntu operating system.                    | APT packages, programs downloaded and installed from the terminal, init scripts.                            |
| Environment variables | Variables set at the system level accessible to all Ray nodes.             | Default environment variables, variables set in init scripts, using secrets, runtime environment variables. |

## Develop in a container[​](#develop-in-a-container "Direct link to Develop in a container")

Anyscale recommends starting development using an Anyscale base image with a recent version of Ray. Use a `slim` image to reduce the size of containers. If you need access to a library excluded from slim images by default, you can install it using [runtime environments](/dependency-management/runtime-environment.md). You can choose Python and CUDA versions based on other dependencies in your environment, but Anyscale recommends you use recent versions to access the latest features. See [Anyscale base images](/reference/base-images.md).

The following table provides an overview of the recommended approaches to developing on Anyscale. See [Develop Anyscale applications](/development.md).

| Approach              | Description                                                                                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Workspace development | Develop code in hosted IDEs or SSH to your workspace. Run Ray code interactively using Jupyter notebooks or Python scripts. Manage dependencies using tools in the Anyscale console. Launch jobs or services using dependencies injected from the workspace environment. |
| Local development     | Develop in your preferred IDE on your personal machine. Launch services or submit jobs to Anyscale using the CLI or SDK, using built-in options for additional dependency management. Use the Anyscale console for monitoring and observability.                         |

note

You can optionally develop new workloads using a local Ray cluster or on-prem infrastructure such as KubeRay, and then deploy to Anyscale. Because most Anyscale features extend Ray, many of the same patterns apply, but you might need to refactor code and change configurations as you move to deploy on Anyscale.

If you need to use package managers such as `poetry` that aren't supported by runtime environments or uv, you need to install and configure them in a containerfile and build a custom image.

## Refactor development patterns to define custom images[​](#define-image "Direct link to Refactor development patterns to define custom images")

Anyscale recommends refactoring development code and configurations to solidify dependencies in a custom image before moving to production. See [Custom images on Anyscale](/container-image/custom-image.md).

You can use containerfile syntax to iteratively edit and build custom containers during workspace development. See [Iterate on workspace container images](/dependency-management/containerfiles.md).

The following table provides an overview of job and service configuration options used during development that Anyscale recommends refactoring when building a production image:

note

Anyscale configures many of these options by default when you launch jobs or services from an Anyscale workspace. See [Launch jobs and services from an Anyscale workspace](/development/workspace-defaults.md).

| Option         | How to include in image                                                                                                                                                                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `working_dir`  | Include instructions in your containerfile to copy your codebase to the path `/home/ray/default/` in your container. Depending on how you build your container, this might be adding all files from your local directory, pushing artifacts from a CI/CD tool, or cloning code from one or more Git repositories. |
| `excludes`     | Exclude files or directories from your image by not including them in the artifacts copied to `/home/ray/default/`.                                                                                                                                                                                               |
| `requirements` | Install Python dependencies in your containerfile.                                                                                                                                                                                                                                                                |
| `env_vars`     | Define environment variables in your containerfile.                                                                                                                                                                                                                                                               |
| `py_modules`   | Install custom Python modules to `/home/ray/default/` or from a custom package repository.                                                                                                                                                                                                                        |

If you use uv during development, you can use uv to manage your environment while building images for production. See [Use uv to manage Python dependencies](/dependency-management/uv.md).

## Test code and package a container for production[​](#test-code-and-package-a-container-for-production "Direct link to Test code and package a container for production")

You can build a custom image on Anyscale using standard containerfile syntax, but images built this way can't include custom user code. Instead, you manage your code separate from your environment and inject it at runtime using the `working_dir` variable. Anyscale provides tools to build container images using the console, CLI, or SDK. See [Build a custom image on Anyscale](/container-image/build-image.md).

You can configure Anyscale to use container images stored in external image registries. Images built externally can include custom user code, meaning that your image can contain your entire application with no external dependencies. See [Use container images from an external registry](/container-image/image-registry.md).

Anyscale recommends testing custom images before deploying new workloads to production. Each application has different testing requirements, and the way you implement testing varies based on the tools you use and how the application interacts with the rest of your ecosystem. The following list provides a general overview of testing:

* Write unit tests to validate functions and modules in your Ray application.
* Write integration tests to ensure that modules and scripts in your Ray application interact as required.
* Write system tests to confirm the application meets the specified requirements for the end-to-end application.
* Gather feedback from users for acceptance testing to ensure that the results of the submitted Anyscale job or launched Anyscale service behave as expected.

As an example, you might run unit tests for each custom Python module in your application using lightweight Python testing before building a custom image, and then run integration and system tests using in a Ray cluster launched with your custom image. If you choose to build an image as the first step or start from a manually defined custom image, you run unit tests and integration tests in a Ray cluster launched with your custom image.

Depending on the maturity of your testing infrastructure and the frequency of changes to your applications, you might choose to have robust automation for testing or instead rely primarily on human quality assurance testing.

## Deploy a container in production[​](#deploy-a-container-in-production "Direct link to Deploy a container in production")

You deploy Ray apps to production by submitting an Anyscale job or launching an Anyscale service. In addition to a custom image, you must define a compute configuration to deploy an Anyscale cluster. See [Define a Ray cluster](/configuration.md).

Container images are immutable by definition. Compute configurations define the resources used by your cluster. Cluster size scales independently of your image.

If you have included all dependencies in your custom image, you can deploy your application without specifying options that install dependencies, define environment variables, or upload files. See [Refactor development patterns to define custom images](#define-image).

See the following sections in the CLI and SDK reference for a full list of options for Anyscale jobs and services:

| Cluster type | CLI                                                                            | SDK                                                                          | Config YAML                                                |
| ------------ | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Job          | [`anyscale job submit`](/reference/job-api.md#anyscale-job-submit)             | [`anyscale.job.submit`](/reference/job-api.md#anyscalejobsubmit)             | [`JobConfig`](/reference/job-api.md#jobconfig)             |
| Service      | [`anyscale service deploy`](/reference/service-api.md#anyscale-service-deploy) | [`anyscale.service.deploy`](/reference/service-api.md#anyscaleservicedeploy) | [`ServiceConfig`](/reference/service-api.md#serviceconfig) |
