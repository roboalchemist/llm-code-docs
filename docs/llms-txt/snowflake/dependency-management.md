# Source: https://docs.snowflake.com/en/developer-guide/streamlit/app-development/dependency-management.md

# Manage dependencies for your Streamlit app

By default, Streamlit in Snowflake environments come with Python, Streamlit, and Snowflake Snowpark installed.
How you manage your app’s dependencies differs based on the runtime environment you choose:

* Container runtimes manage packages with [uv](https://docs.astral.sh/uv/). You can specify
  dependencies in a `pyproject.toml` (recommended) or `requirements.txt` file. By default, your
  app doesn’t have access to a package index like PyPI. Therefore, if you want to edit or specify the
  versions of your app’s dependencies, you must create an external access integration (EAI).
  Additionally, you can install packages from wheel files included in your project directory.
* Warehouse runtimes manage packages with [conda](https://docs.conda.io/en/latest/). You can
  specify dependencies using an `environment.yml` file or the built-in package picker
  in Snowsight. You can only install packages from the
  [Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/).

To learn how to add or edit files in your deployed app, see
[Editing a deployed Streamlit app](editing-your-app.md).

| Supported dependency sources | Warehouse runtime | Container runtime |
| --- | --- | --- |
| PyPI or other external [“simple”](https://peps.python.org/pep-0503/) package indexes | No | Yes (with EAI) |
| Snowflake Anaconda Channel | Yes, with limitations on Streamlit versions | No |
| Internal stage | No | Yes, but only via relative paths within the app’s source files |
| Snowflake Artifact Repository (`snowflake.snowpark.pypi_shared_repository`) | No | No |

## Supported versions of Python

Newly created Streamlit in Snowflake apps run in Python 3.11 by default.

* For container runtimes, Python 3.11 is the only currently supported version.
* For warehouse runtimes, you can choose Python 3.9, 3.10, or 3.11.

## Supported versions of Streamlit

Newly created Streamlit in Snowflake apps use the latest supported version of Streamlit available in
their runtime environment. When a new version of Streamlit is released, there
might be a delay before the new version becomes the default.

* For container runtimes, the minimum required version of Streamlit is 1.50. You can
  use any later version of Streamlit, including `streamlit-nightly` versions.

  > **Important:**
  >
  > `streamlit-nightly` versions are experimental. For more information, see
  > [Nightly releases](https://docs.streamlit.io/develop/quick-reference/prerelease#nightly-releases)
  > in the Streamlit documentation.

  You can immediately use the latest Streamlit version by installing it from a package index.
* For warehouse runtimes, you are limited to a subset of versions starting from 1.22.0.
  `streamlit-nightly` versions aren’t supported.

  It’s not possible to immediately use the latest Streamlit version in a warehouse runtime.

To prevent unexpected package upgrades, configure your app’s dependencies as
described on this page.

### Supported versions of the Streamlit library in warehouse runtimes

Streamlit in Snowflake supports the following versions of the Streamlit open-source library:

* 1.51.0
* 1.50.0
* 1.49.1
* 1.48.0
* 1.47.0
* 1.46.1
* 1.45.1
* 1.45.0
* 1.44.1
* 1.44.0
* 1.42.0
* 1.39.0
* 1.35.0
* 1.31.1
* 1.29.0
* 1.26.0
* 1.22.0

## Non-Python dependencies

Some Python packages require non-Python system libraries to be installed in the
runtime environment. For example, the `Pillow` package requires libraries for
handling different image formats.

* For non-Python dependencies in container runtimes, you can only use the pre-installed
  system libraries. Installing additional non-Python dependencies isn’t supported yet.
* For non-Python dependencies in warehouse runtimes, some system libraries are available
  in the Snowflake Anaconda Channel.

## Best practices for declaring dependencies

When declaring your app’s dependencies, consider the following best practices:

* Pin critical package versions.

  * For container runtimes, use the `==` operator in `pyproject.toml` or `requirements.txt` files.
  * For warehouse runtimes, use the `=` operator in `environment.yml` files.
* Use version ranges for flexibility.

  * For container runtimes, use the `<`, `<=`, `>=`, and `>` operators in `pyproject.toml` or `requirements.txt` files.
  * For warehouse runtimes, use `*` wildcard suffixes in `environment.yml` files.
* Keep dependency lists minimal to reduce build time.
* Test dependency changes in development before deploying.
* Ensure your dependencies are compatible with the Python version in your runtime.

When migrating between runtimes or changing your package manager,
review your dependency names. For example, some packages have different names between
Conda and PyPI:

| Package | Conda Name | PyPI Name |
| --- | --- | --- |
| Pillow | `pillow` | `Pillow` |
| OpenCV | `opencv` | `opencv-python` |
| PyYAML | `pyyaml` | `PyYAML` |

## Managing dependencies for container runtimes

Container-runtime apps require an external access integration (EAI) to install packages
from an external package index like PyPI. Without an EAI, you can only use packages
shipped with the runtime or included in your app’s source files.

Even if you only want to specify the version of Streamlit, you must include an EAI with
your app. Without an EAI, if you attempt to use version specifiers on pre-installed packages,
you might encounter an error when the runtime base image is updated. This is because your
version specifier might no longer be compatible with the pre-installed packages.

### External access integrations for container runtimes

For a general overview of external access integrations (EAIs), see [External network access overview](../../external-network-access/external-network-access-overview.md).

#### PyPI EAI

PyPI is the default package index used by uv to install Python packages in your container runtime.
To create an EAI for PyPI, you need a network rule that allows access to all
necessary PyPI domains. EAIs are typically created and maintained by your account
administrator or security team.

For example, the following SQL commands create an EAI (`pypi_access_integration`) to PyPI
and grants USAGE to an app-development role (`app_developer_role`).

```sqlexample
CREATE OR REPLACE NETWORK RULE pypi_network_rule
  MODE = EGRESS
  TYPE = HOST_PORT
  VALUE_LIST = ('pypi.org', 'pypi.python.org', 'pythonhosted.org', 'files.pythonhosted.org');

CREATE OR REPLACE EXTERNAL ACCESS INTEGRATION pypi_access_integration
  ALLOWED_NETWORK_RULES = (pypi_network_rule)
  ENABLED = true;

GRANT USAGE ON EXTERNAL ACCESS INTEGRATION pypi_access_integration TO ROLE app_developer_role;
```

After creating the EAI, you need to add it to your Streamlit object. You can do
this in Snowsight or with SQL:

SnowsightSQL

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Projects » Streamlit, and then select your app.
3. In the upper-right corner, select  (more options) » App settings.
4. In the App settings dialog, select the External networks tab.
5. From the list of available EAIs, select the EAI for PyPI.
6. To save the change and close the dialog, select Save.

```sqlexample
ALTER STREAMLIT my_app SET
  EXTERNAL_ACCESS_INTEGRATIONS = (pypi_access_integration);
```

### Dependency files

Container runtimes use uv for fast, reliable dependency resolution. uv works
like pip to install Python packages, but it’s more performant and customizable. For more information
about uv’s features, see the [Features](https://docs.astral.sh/uv/getting-started/features/) overview
in the uv documentation.

Container runtimes search for dependency files in the same directory as your app’s entrypoint file. If no dependency files
are found, the search continues up the directory tree until reaching the root of your app’s source location. The first
dependency file found is used to install your app’s dependencies.

When multiple dependency files exist in the same directory, they are used in the following order of precedence:

* `requirements.txt`: Lists the Python packages and versions required by your Streamlit app,
  including Streamlit itself. You can’t configure your Python version with `requirements.txt`.

  For more information about the format of `requirements.txt`, see
  [Requirements File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) in the pip documentation.
* `pyproject.toml` (recommended): Manages your Python version and dependencies. Currently, only
  Python version 3.11 is supported. When you provide a `pyproject.toml` file, uv will generate
  a `uv.lock` file to lock your dependency versions. This lock file will be updated whenever you update
  your dependencies. You must use `pyproject.toml` if you want to use a different package index than PyPI.

  For more information about the format of `pyproject.toml`, see [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
  in the Python documentation.

`requirements.txt` is the simplest way to declare your app’s dependencies
and is provided for the convenience of getting started. However, for more advanced
dependency management, Snowflake recommends using `pyproject.toml` instead.
For example, this lets you lock dependency versions to ensure that your builds are reproducible.

> **Tip:**
>
> * You can install a package from any URL if you have the necessary EAI assigned to your app. URLs requiring
>   authentication must support embedded credentials.
> * You can install a package from within your project directory by using a relative path from the
>   dependency file to a wheel file.
> * If you use version specifiers on pre-installed packages, you must have an EAI to a package index to avoid
>   errors when the runtime base image is updated.

Commonly, your entrypoint file and dependency file will be in the root of your project directory.
However, your entrypoint file can be in a subdirectory and your dependency file can be in the same
directory or any parent up to the root of your project.

For example, your project directory might have one of the following structures:

```none
source_directory/
├── requirements.txt
└── streamlit_app.py
```

```none
source_directory/
├── pyproject.toml
├── streamlit_app.py
└── uv.lock
```

```none
source_directory/
├── pyproject.toml
├── subdirectory/
│   └── streamlit_app.py
└── uv.lock
```

```none
source_directory/
└── subdirectory/
    ├── pyproject.toml
    ├── streamlit_app.py
    └── uv.lock
```

> **Note:**
>
> The container runtime will use the directory containing the dependency file as its working directory
> for uv. Therefore, if you use a relative path to install a package from among your app source files,
> the path should be relative to the dependency file location. For more information about declaring
> package sources, see [Dependency sources](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)
> in the uv documentation.

#### PyPI dependency file examples

Your `pyproject.toml` file must include a `name` and `version` to be in a valid format
for uv, but their values can be arbitrary. Use `requires-python` to set your Python
version, even though container runtimes only support Python 3.11 for now. Use `dependencies`
to list your Python packages for your container runtime.

> **Tip:**
>
> Install Streamlit as `streamlit[snowflake]` to include its Snowflake connector
> dependencies (`snowflake-snowpark-python`).

If you have an EAI for PyPI, the following `pyproject.toml` file declares
a minimum Python version of 3.11 and includes five Python packages which will be
installed from PyPI:

```toml
[project]
name = "my-streamlit-app"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "streamlit[snowflake]==1.50.0",
    "pandas>=2.0.0",
    "plotly>5.0.0",
    "requests>2.0.0,<3.0.0"
]
```

As an alternative to `pyproject.toml`, you can use a `requirements.txt` file
to declare your app’s dependencies. The following `requirements.txt` contains the
same Python packages as the previous `pyproject.toml` example:

```text
streamlit[snowflake]==1.50.0
pandas>=2.0.0
plotly>5.0.0
requests>2.0.0,<3.0.0
```

> **Note:**
>
> To pin a version of a package, you must use the `==` operator. To specify a version range,
> you must use `<`, `<=`, `>=`, and `>` operators. For example, `pandas>=2.0.0,<3.0.0` will install
> any version between 2.0.0 and 2.99.99. For more information, see [Dependency specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/).

#### JFrog dependency file examples

For added security, your system administrator may require you to use a curated or private
package index like JFrog Artifactory. This is an exclusive feature for container runtimes.
With JFrog, you can create a public or private package index that proxies PyPI or hosts
custom packages. This allows you to control which packages and versions are available to
your Streamlit apps.

To specify a package index, you must use `pyproject.toml`. For more information, see
[Using alternative package indexes](https://docs.astral.sh/uv/guides/integration/alternative-indexes/)
in the uv documentation.

The following `pyproject.toml` file declares a minimum Python version of 3.11,
includes five Python packages, and specifies JFrog as the package index that proxies PyPI:

```toml
[project]
name = "my-streamlit-app"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "streamlit[snowflake]==1.50.0",
    "pandas>=2.0.0",
    "plotly>=5.0.0",
    "requests>2.0.0,<3.0.0"
]

[[tool.uv.index]]
name = "jfrog"
url = "<server_name>.jfrog.io/artifactory/api/pypi/<repository_key>/simple"
default = true
```

If your JFrog repository requires authentication, generate a personal access
token or get a scoped token from your JFrog system administrator. Then, include the
token in the URL. Don’t use your JFrog password in the URL. In this case, the `[[tool.uv.index]]`
table in the previous example would be replaced with the following:

```toml
[[tool.uv.index]]
name = "jfrog"
url = "https://<username>:<access_token>@<server_name>.jfrog.io/artifactory/api/pypi/<repository_key>/simple"
default = true
```

## Managing dependencies for warehouse runtimes

Warehouse runtimes use conda to manage your app’s dependencies. You can declare
your dependencies using an `environment.yml` file or the built-in package picker
in Snowsight. Dependencies are installed from the
[Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/),
which includes both Python packages and some non-Python system libraries.

The Snowflake Anaconda Channel contains more versions of Streamlit than are supported
in Streamlit in Snowflake warehouse runtimes. To avoid compatibility issues, only use versions of
Streamlit that are listed in Supported versions of the Streamlit library in warehouse runtimes. Otherwise,
you may install any other package available in the Snowflake Anaconda Channel.

### `environment.yml` file

To install dependencies in your warehouse runtime environment using an `environment.yml`
file, create or edit the file in the root of your app’s source location. If you don’t provide an
`environment.yml` file, Snowflake uses only the pre-installed packages for your selected
environment. For more information about the structure of `environment.yml`, see the
[conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually).

The following limitations apply when using `environment.yml` files in Streamlit in Snowflake warehouse runtimes:

* You can only use the Snowflake Anaconda Channel to install packages.
* You can only use the Streamlit versions listed in Supported versions of the Streamlit library in warehouse runtimes.
* You can’t declare `pip` packages in the `dependencies` section, including relative paths to local packages.

The following `environment.yml` declares Python 3.11 and five Python packages:

```yaml
name: my-streamlit-app
channels:
  - snowflake
dependencies:
  - python=3.11
  - streamlit=1.50.0
  - pandas=2.*
  - plotly=5.0.*
  - requests
  - snowflake-snowpark-python
```

Snowflake recommends pinning a version of Streamlit to prevent the app from being upgraded when a new version
of Streamlit becomes available in the Snowflake Anaconda Channel.

> **Note:**
>
> To pin a version of a package, you must use the `=` operator. To specify a version range,
> you must use `*` wildcards. For example, `pandas=2.*` will install
> any version of pandas between 2.0.0 and 2.99.99.

### Local development with conda

When developing your warehouse-runtime app locally with conda, you must include
additional details in your `environment.yml` file to ensure the dependencies
are installed correctly.

* Identify the Snowflake Anaconda Channel by its URL: `https://repo.anaconda.com/pkgs/snowflake`.
* Block the default channel.

In your `environment.yml` file, use the following two channels:

```yaml
channels:
  - https://repo.anaconda.com/pkgs/snowflake
  - nodefaults
```

If `defaults` appears in your `~/.condarc` file, comment it out:

```yaml
channels:
  # - defaults
```

### Snowsight package picker

Besides editing the `environment.yml` file directly for your warehouse-runtime app, you can also
use the built-in package picker in Snowsight to add or remove packages from your
app’s environment. The package picker is only available for apps using warehouse runtimes.
Additionally, the package picker only displays packages compatible with the current Python
version of your app. Some system libraries that are independent of Python version might not
be shown in the package picker and must be added manually to `environment.yml`.

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Projects » Streamlit, and then select your Streamlit app.
3. In the upper-right corner, select Edit.
4. In the upper-left corner of the editor pane, select Packages.

   A drop-down pane appears with the Anaconda Packages tab selected.
5. Do any of the following actions:

> * To set the Python version, in the Python version selector, choose the desired version.
> * To add a package, use the search bar to find packages by name, then select the desired package.
> * To remove a package, in the Installed Packages section, select the x icon
>   to the right of the package version.
> * To set the version of an installed package, in the Installed Packages section,
>   use the version selector next to the package name.
>
> Snowflake updates your `environment.yml` file automatically and reboots your app.
> If you have the `environment.yml` file open in the editor, refresh the page to
> see the changes.
