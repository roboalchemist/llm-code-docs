# Source: https://docs.baseten.co/development/model/configuration.md

# Configuration

> How to configure your model.

ML models often have dependencies on external libraries, data,
and other resources. These models also typically have particular
hardware configurations.

In this guide, we'll cover the basics of how to configure your model
to specify this information.

Configuration for models is specified in the `config.yaml` file. Here are some
of the common configuration options:

# Environment variables

You can specify environment variables to be set in the model serving environment
using the `environment_variables` key.

```yaml config.yaml theme={"system"}
environment_variables:
  MY_ENV_VAR: my_value
```

# Python Packages

Python packages can be specified in two ways in the `config.yaml` file:

1. `requirements`: A list of Python packages to install.
2. `requirements_file`: A requirements.txt file to install pip packages from.

For example, if you have a simple list of packages, you can specify them as follows:

```yaml config.yaml theme={"system"}
requirements:
  - package_name
  - package_name2
```

Note that you can pin versions using the `==` operator.

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

# System Packages

Truss also has support for installing apt-installable Debian packages. to
add system packages to your model serving environment, add the following to
your `config.yaml` file:

```yaml config.yaml theme={"system"}
system_packages:
  - package_name
  - package_name2
```

For a more concrete examples,

```yaml config.yaml theme={"system"}
system_packages:
  - tesseract-ocr
```

# Resources

Another key part of configuring your model is specifying hardware resources needed.
You can use the `resources` key to specify these. For a CPU model, your resources
configuration might look something like:

```yaml config.yaml theme={"system"}
resources:
  accelerator: null
  cpu: "1"
  memory: 2Gi
  use_gpu: false
```

For a GPU model, your resources configuration might look like:

```yaml config.yaml theme={"system"}
resources:
  accelerator: "L4"
```

When you push your model, it will be assigned an instance type matching the
specifications required.

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
