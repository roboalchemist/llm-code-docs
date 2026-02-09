# Source: https://docs.upsun.com/languages/python/dependencies.md

# Manage Python dependencies


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

You can manage Python packages in different ways.
Python images come with pip installed,
but they're flexible enough so you can choose what package manager you want.
This article describes how to configure major package management tools.

This package management is different from global dependencies (packages available as commands),
which you can add in your [app configuration](https://docs.upsun.com../../create-apps.md).
See more about [managing global dependencies](https://docs.upsun.com/languages/python.md#package-management).

## Pip

[pip](https://pip.pypa.io/en/stable/) is the primary package installer for Python
and comes installed on every Python container.
You can use it to install packages from the Python Package Index and other locations.

To manage packages with pip,
commit a `requirements.txt` file with all of the dependencies needed for your app.
Then install the packages in your [`build` hook](https://docs.upsun.com../../create-apps/hooks.md),
such as by running the following command: `pip install -r requirements.txt`.

The following sections present ideas to keep in mind to ensure repeatable deployments on Upsun.

### pip version

The version of pip on Python containers gets updated regularly.
But it isn't guaranteed to be the latest version or the version that matches your local environment.
You might want to define a specific version of pip in your deployments to further enforce repeatable builds.

To do so, modify your [app configuration](https://docs.upsun.com../../create-apps.md), as in the following examples:

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    type: 'python:3.14'
    hooks:
      build: |
        # Fail the build if any errors occur
        set -eu
        # Download the latest version of pip
        python3.14 -m pip install --upgrade pip
        # Install dependencies
        pip install -r requirements.txt        
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    type: 'python:3.14'
    variables:
      env:
        PIP_VERSION: '22.3.1'
    hooks:
      build: |
        # Fail the build if any errors occur
        set -eu
        # Download a specific version of pip
        python3.14 -m pip install pip==$PIP_VERSION
        # Install dependencies
        pip install -r requirements.txt        
```

### pip freeze

You can write `requirements.txt` files in various ways.
You can specify anything from the latest major to a specific patch version in a [requirement specifier](https://pip.pypa.io/en/stable/reference/requirement-specifiers/).
Use `pip freeze` before committing your requirements to pin specific package versions.
This ensures repeatable builds on Upsun with the same packages.

## Pipenv

[Pipenv](https://pipenv.pypa.io/en/latest/) is a package manager for Python
that creates and manages a virtual environment for Python projects.
Dependencies are tracked and defined within a `Pipfile`.
It also generates a `Pipfile.lock` file to produce repeatable installs.

You can specify the latest or a specific version of Pipenv
in your deployments to ensure repeatable builds.
Because Pipenv depends on pip, you might want to also specify the pip version.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    type: 'python:3.14'
    dependencies:
      python3:
        pipenv: '*'
    hooks:
      build: |
        # Fail the build if any errors occur
        set -eu
        # Download the latest version of pip
        python3.14 -m pip install --upgrade pip
        # Install dependencies
        # Include `--deploy` to fail the build if `Pipfile.lock` isn't up to date
        pipenv install --deploy        
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    type: 'python:3.14'
    variables:
      env:
        PIP_VERSION: '22.3.1'
    dependencies:
      python3:
        pipenv: '2024.4.1'
    hooks:
      build: |
        # Fail the build if any errors occur
        set -eu
        # Download a specific version of pip
        python3.14 -m pip install pip==$PIP_VERSION
        # Install dependencies
        # Include `--deploy` to fail the build if `Pipfile.lock` isn't up to date
        pipenv install --deploy        
```

## UV

[uv](https://docs.astral.sh/uv/) is an extremely fast Python package and project
manager, written in Rust.

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.14'
    dependencies:
      python3:
        uv: "*"
```

## Poetry

[Poetry](https://python-poetry.org/docs/) is a tool for dependency management and packaging in Python.
It allows you to declare the libraries your project depends on and manages them for you.
Poetry offers a lock file to ensure repeatable installs and can build your project for distribution.
It also creates and manages virtual environments to keep project work isolated from the rest of your system.

To set up Poetry on Upsun, follow these steps:

1.  Configure your virtual environment by setting two variables in your [app configuration](https://docs.upsun.com../../create-apps.md).

    - [`POETRY_VIRTUALENVS_IN_PROJECT`](https://python-poetry.org/docs/configuration/#virtualenvsin-project):
      Setting this to `true` places the virtual environment at the root of the app container: `/app/.venv`.
    - [`POETRY_VIRTUALENVS_CREATE`](https://python-poetry.org/docs/configuration/#virtualenvscreate):
      Setting this to `true` ensures that the same virtual environment created during the build hook is reused in subsequent steps.

    Set the variables as follows:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'python:3.14'
    variables:
      env:
        POETRY_VIRTUALENVS_IN_PROJECT: true
        POETRY_VIRTUALENVS_CREATE: true
```
2.  Install Poetry.
    You can specify the latest or a specific version of Poetry in your deployments to ensure repeatable builds.

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
    # The location of the application's code.
    source:
      root: "myapp"
    type: 'python:3.14'
    dependencies:
      python3:
        poetry: '*'
    variables:
      env:
        POETRY_VIRTUALENVS_IN_PROJECT: true
        POETRY_VIRTUALENVS_CREATE: true
    hooks:
      build: |
        # Fail the build if any errors occur
        set -eu
        # Download the latest version of pip
        python3.14 -m pip install --upgrade pip
        # Install dependencies
        poetry install        
```

    .upsun/config.yaml

```yaml {}
applications:
  # The name of the app container. Must be unique within a project.
  myapp:
     # The location of the application's code.
     source:
       root: "myapp"
     type: 'python:3.14'
     dependencies:
       python3:
         poetry: '>=1.8'
       variables:
         env:
           POETRY_VIRTUALENVS_IN_PROJECT: true
           POETRY_VIRTUALENVS_CREATE: true

        hooks:
          build: |
            # Fail the build if any errors occur
            set -eu
            # Download the latest version of pip
            python3.14 -m pip install --upgrade pip
            # Install dependencies
            poetry install            
```

3.  Make Poetry available outside the build hook.
    Although step 2 updated the `PATH` to make Poetry available during the build hook,
    it isn't enough to make it available at subsequent stages.

    To use Poetry in a start command, a deploy hook, or during SSH sessions,
    update the `PATH` in a [`.environment` file](https://docs.upsun.com../../development/variables/set-variables.md#set-variables-via-script).

    ```text  {location=".environment"}
    # Updates PATH when Poetry is used, making it available during deploys, start commands, and SSH.
    if [ -n "$POETRY_VERSION" ]; then
      export PATH="/app/.local/bin:$PATH"
    fi
    ```

