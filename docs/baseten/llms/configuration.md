# Source: https://docs.baseten.co/development/model/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration

> How to configure your model.

ML models depend on external libraries, data files, and specific hardware configurations.

This guide shows you how to configure your model's dependencies and resources.

The `config.yaml` file defines your model's configuration. Common options include:

# Environment variables

To set environment variables in the model serving environment, use the `environment_variables` key:

```yaml config.yaml theme={"system"}
environment_variables:
  MY_ENV_VAR: my_value
```

# Python packages

Python packages can be specified in two ways in the `config.yaml` file:

1. `requirements`: A list of Python packages to install.
2. `requirements_file`: A requirements.txt file to install pip packages from.

To specify Python packages as a list, use the following:

```yaml config.yaml theme={"system"}
requirements:
  - package_name
  - package_name2
```

Pin package versions using the `==` operator:

```yaml config.yaml theme={"system"}
requirements:
  - package_name==1.0.0
  - package_name2==2.0.0
```

If you need more control over the installation process and want to use
different pip options or repositories, you can specify a `requirements_file`
instead.

```yaml config.yaml theme={"system"}
requirements_file: ./requirements.txt
```

# System packages

Truss also has support for installing apt-installable Debian packages. To add
system packages to your model serving environment, add the following to your
`config.yaml` file:

```yaml config.yaml theme={"system"}
system_packages:
  - package_name
  - package_name2
```

For example, to install Tesseract OCR:

```yaml config.yaml theme={"system"}
system_packages:
  - tesseract-ocr
```

# Resources

Specify hardware resources in the `resources` section.

**Option 1: Specify individual resource fields**

For a CPU model:

```yaml config.yaml theme={"system"}
resources:
  cpu: "1"
  memory: 2Gi
```

For a GPU model:

```yaml config.yaml theme={"system"}
resources:
  accelerator: "L4"
```

When you push your model, it will be assigned an instance type matching the
specifications required.

**Option 2: Specify an exact instance type**

```yaml config.yaml theme={"system"}
resources:
  instance_type: "L4:4x16"
```

Using `instance_type` lets you select an exact SKU. When specified, other resource fields are ignored.

See the [Resources](/deployment/resources) page for more information on
options available.

# Advanced configuration

There are numerous other options for configuring your model. See some
of the other guides:

* [Secrets](/development/model/secrets)
* [Data](/development/model/data-directory)
* [Custom Build Commands](/development/model/build-commands)
* [Base Docker Images](/development/model/base-images)
* [Custom Servers](/development/model/custom-server)
* [Custom Health Checks](/development/model/custom-health-checks)
