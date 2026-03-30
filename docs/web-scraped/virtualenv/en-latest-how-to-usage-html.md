# Source: https://virtualenv.pypa.io/en/latest/how-to/usage.html

Title: Use virtualenv - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/how-to/usage.html

Markdown Content:
Select a Python version[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#select-a-python-version "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

By default, virtualenv uses the same Python version it runs under. Override this with `--python` or `-p`.

### Using version specifiers[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-version-specifiers "Link to this heading")

Specify a Python version by name or version number:

$ virtualenv -p python3.8 venv
$ virtualenv -p 3.10 venv
$ virtualenv -p pypy3 venv
$ virtualenv -p rustpython venv

### Using PEP 440 specifiers[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-pep-440-specifiers "Link to this heading")

Use [PEP 440](https://peps.python.org/pep-0440/#version-specifiers) version specifiers to match Python versions:

$ virtualenv --python ">=3.12" venv
$ virtualenv --python "~=3.11.0" venv
$ virtualenv --python "cpython>=3.10" venv

* `>=3.12` – any Python 3.12 or later.

* `~=3.11.0` – compatible release, equivalent to `>=3.11.0, <3.12.0` (any 3.11.x patch).

* `cpython>=3.10` – restrict to CPython implementation, 3.10 or later.

### Using free-threading Python[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-free-threading-python "Link to this heading")

Create an environment with [free-threading Python](https://docs.python.org/3/howto/free-threading-python.html):

$ virtualenv -p 3.13t venv

### Targeting a specific CPU architecture[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#targeting-a-specific-cpu-architecture "Link to this heading")

On machines that support multiple architectures — such as Apple Silicon (arm64 + x86_64 via Rosetta) or Windows on ARM — you can request a specific CPU architecture by appending it to the spec string:

$ virtualenv -p cpython3.12-64-arm64 venv
$ virtualenv -p 3.11-64-x86_64 venv

Cross-platform aliases are normalized automatically, so `amd64` and `x86_64` are treated as equivalent, as are `aarch64` and `arm64`. If omitted, any architecture matches (preserving existing behavior).

### Using absolute paths[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-absolute-paths "Link to this heading")

Specify the full path to a Python interpreter:

$ virtualenv -p /usr/bin/python3.9 venv

### Using `--try-first-with`[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-try-first-with "Link to this heading")

Use `--try-first-with` to provide a hint about which Python to check first. Unlike `--python`, this is a hint rather than a rule. The interpreter at this path is checked first, but only used if it matches the `--python` constraint.

$ virtualenv --python ">=3.10" --try-first-with /usr/bin/python3.9 venv

In this example, /usr/bin/python3.9 is checked first but rejected because it does not satisfy the >=3.10 constraint.

### Using version managers (pyenv, mise, asdf)[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#using-version-managers-pyenv-mise-asdf "Link to this heading")

virtualenv automatically resolves shims from [pyenv](https://github.com/pyenv/pyenv), [mise](https://mise.jdx.dev/), and [asdf](https://asdf-vm.com/) to the real Python binary. Set the active Python version using any of the standard mechanisms and virtualenv will discover it:

$ pyenv local 3.12.0
$ virtualenv venv # uses pyenv's 3.12.0, not the system Python

$ PYENV_VERSION=3.11.0 virtualenv venv # uses 3.11.0

This also works with mise and asdf:

$ mise use python@3.12
$ virtualenv venv

No additional configuration is required. See [Explanation](https://virtualenv.pypa.io/en/latest/explanation.html) for details on how shim resolution works.

Activate a virtual environment[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#activate-a-virtual-environment "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

Activate the environment to modify your shell’s PATH and environment variables.

Bash/Zsh

$ source venv/bin/activate

Fish

$ source venv/bin/activate.fish

PowerShell

PS> .\venv\Scripts\Activate.ps1

Note

If you encounter an execution policy error, run `Set-ExecutionPolicy RemoteSigned` to allow local scripts.

CMD

> .\venv\Scripts\activate.bat

Nushell

$ overlay use venv/bin/activate.nu

### Deactivate the environment[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#deactivate-the-environment "Link to this heading")

Exit the virtual environment:

$ deactivate

### Use without activation[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#use-without-activation "Link to this heading")

Use the environment without activating it by calling executables with their full paths:

$ venv/bin/python script.py
$ venv/bin/pip install package

### Customize prompt[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#customize-prompt "Link to this heading")

Set a custom prompt prefix:

$ virtualenv --prompt myproject venv

Disable the prompt modification by setting the `VIRTUAL_ENV_DISABLE_PROMPT` environment variable.

Access the prompt string via the `VIRTUAL_ENV_PROMPT` environment variable.

### Programmatic activation[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#programmatic-activation "Link to this heading")

Activate the environment from within a running Python process using `activate_this.py`. This modifies `sys.path` and environment variables in the current process so that subsequent imports resolve from the virtual environment.

import runpy

runpy.run_path("venv/bin/activate_this.py")

A common use case is web applications served by a system-wide WSGI server (such as mod_wsgi or uWSGI) that need to load packages from a virtual environment:

import runpy
from pathlib import Path

runpy.run_path(str(Path("/var/www/myapp/venv/bin/activate_this.py")))

from myapp import create_app  # noqa: E402

application = create_app()

Configure defaults[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#configure-defaults "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Use a configuration file to set default options for virtualenv.

### Configuration file location[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#configuration-file-location "Link to this heading")

The configuration file is named `virtualenv.ini` and located in the platformdirs app config directory. Run `virtualenv --help` to see the exact location for your system.

Override the location with the `VIRTUALENV_CONFIG_FILE` environment variable.

### Configuration format[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#configuration-format "Link to this heading")

Derive configuration keys from command-line options by stripping leading `-` and replacing remaining `-` with `_`:

[virtualenv]
python = /opt/python-3.8/bin/python

### Multi-value options[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#multi-value-options "Link to this heading")

Specify multiple values on separate lines:

[virtualenv]
extra_search_dir =
 /path/to/dists
 /path/to/other/dists

### Environment variables[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#environment-variables "Link to this heading")

Set options using environment variables with the `VIRTUALENV_` prefix and uppercase key names:

$ export VIRTUALENV_PYTHON=/opt/python-3.8/bin/python

For multi-value options, separate values with commas or newlines.

### Override app-data location[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#override-app-data-location "Link to this heading")

Set the `VIRTUALENV_OVERRIDE_APP_DATA` environment variable to override the default app-data cache directory location.

### Configuration priority[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#configuration-priority "Link to this heading")

Options are resolved in this order (highest to lowest priority):

        block-beta
    columns 1
    A["Command-line arguments (highest)"]
    B["Environment variables"]
    C["Configuration file"]
    D["Default values (lowest)"]

    style A fill:#16a34a,stroke:#15803d,color:#fff
    style B fill:#2563eb,stroke:#1d4ed8,color:#fff
    style C fill:#d97706,stroke:#b45309,color:#fff
    style D fill:#6366f1,stroke:#4f46e5,color:#fff
    
Control seed packages[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#control-seed-packages "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

### Upgrade embedded wheels[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#upgrade-embedded-wheels "Link to this heading")

Update the embedded wheel files to the latest versions:

$ virtualenv --upgrade-embed-wheels

### Provide custom wheels[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#provide-custom-wheels "Link to this heading")

Use custom wheel files from a local directory:

$ virtualenv --extra-search-dir /path/to/wheels venv

### Download latest from PyPI[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#download-latest-from-pypi "Link to this heading")

Download the latest versions of seed packages from PyPI:

$ virtualenv --download venv

### Disable periodic updates[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#disable-periodic-updates "Link to this heading")

Disable automatic periodic updates of seed packages:

$ virtualenv --no-periodic-update venv

### For distribution maintainers[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#for-distribution-maintainers "Link to this heading")

Patch the `virtualenv.seed.wheels.embed` module and set `PERIODIC_UPDATE_ON_BY_DEFAULT` to `False` to disable periodic updates by default. See [Explanation](https://virtualenv.pypa.io/en/latest/explanation.html) for implementation details.

Use from Python code[¶](https://virtualenv.pypa.io/en/latest/how-to/usage.html#use-from-python-code "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Call virtualenv from Python code using the `cli_run` function:

from virtualenv import cli_run

cli_run(["venv"])

Pass options as list elements:

cli_run(["-p", "python3.8", "--without-pip", "myenv"])

Use the returned session object to access environment details:

result = cli_run(["venv"])
print(result.creator.dest)  # path to created environment
print(result.creator.exe)  # path to python executable

Use `session_via_cli` to describe the environment without creating it:

from virtualenv import session_via_cli

session = session_via_cli(["venv"])

# inspect session.creator, session.seeder, session.activators

See [Python](https://virtualenv.pypa.io/en/latest/reference/api.html) for complete API documentation.
