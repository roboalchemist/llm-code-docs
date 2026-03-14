# Source: https://virtualenv.pypa.io/en/latest/explanation.html

Title: Explanation - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/explanation.html

Published Time: Mon, 09 Mar 2026 17:39:03 GMT

Markdown Content:
This page explains the design decisions and concepts behind virtualenv. It focuses on understanding why things work the way they do.

virtualenv vs venv vs uv[¶](https://virtualenv.pypa.io/en/latest/explanation.html#virtualenv-vs-venv-vs-uv "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

Since Python 3.3, the standard library includes the `venv` module, which provides basic virtual environment creation following [PEP 405](https://www.python.org/dev/peps/pep-0405/). [uv](https://docs.astral.sh/uv/pip/environments/) is a newer, Rust-based tool that also creates virtual environments via `uv venv`.

virtualenv occupies a middle ground: faster and more featureful than `venv`, while remaining a pure Python solution with a plugin system for extensibility.

|  | `venv` | `virtualenv` | [uv](https://docs.astral.sh/uv/) |
| --- | --- | --- | --- |
| Performance | Slowest (60s+); spawns [pip](https://pip.pypa.io/) as a subprocess to seed. | Fast; caches pre-built install images, subsequent creation < 1 second. | Fastest; Rust implementation, milliseconds. Does not seed pip/setuptools by default. |
| Extensibility | No plugin system. | Plugin system for discovery, creation, seeding, and activation. | No plugin system. |
| Cross-version | Only the Python version it runs under. | Any installed Python via auto-discovery (registry, uv-managed, PATH). | Any installed or uv-managed Python. |
| Upgradeability | Tied to Python releases. | Independent via [PyPI](https://pypi.org/project/virtualenv/). | Independent via its own release cycle. |
| Programmatic API | Basic `create()` function only. | Full Python API; can describe environments without creating them. Used by [tox](https://tox.readthedocs.io/), [poetry](https://python-poetry.org/), [pipx](https://pipx.pypa.io/), etc. | Command line only. |
| Type annotations | No `py.typed` marker; limited annotations. | Fully typed with [**PEP 561**](https://peps.python.org/pep-0561/)`py.typed` marker; checked by [ty](https://docs.astral.sh/ty/). | Not applicable (Rust binary). |
| Best for | Zero dependencies, basic needs. | Plugin extensibility, programmatic API, tool compatibility ([tox](https://tox.readthedocs.io/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)). | Maximum speed, already using `uv` for package management. |

How virtualenv works[¶](https://virtualenv.pypa.io/en/latest/explanation.html#how-virtualenv-works "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Python packaging often faces a fundamental problem: different applications require different versions of the same library. If Application A needs `requests==2.25.1` but Application B needs `requests==2.28.0`, installing both into the global site-packages directory creates a conflict. Only one version can exist in a given location.

virtualenv solves this by creating isolated Python environments. Each environment has its own installation directories and can maintain its own set of installed packages, independent of other environments and the system Python.

virtualenv operates in two distinct phases:

**Phase 1: Discover a Python interpreter**
virtualenv first identifies which Python interpreter to use as the template for the virtual environment. By default, it uses the same Python version that virtualenv itself is running on. You can override this with the `--python` flag to specify a different interpreter.

**Phase 2: Create the virtual environment**
Once the target interpreter is identified, virtualenv creates the environment in four steps:

1. Create a Python executable matching the target interpreter

2. Install seed packages (pip, setuptools, wheel) to enable package installation

3. Install activation scripts for various shells

4. Create VCS ignore files (currently Git’s `.gitignore`, skip with `--no-vcs-ignore`)

An important design principle: virtual environments are not self-contained. A complete Python installation consists of thousands of files, and copying all of them into every virtual environment would be wasteful. Instead, virtual environments are lightweight shells that borrow most content from the system Python. They contain only what’s needed to redirect Python’s behavior.

This design has two implications:

* Environment creation is fast because only a small number of files need to be created.

* Upgrading the system Python might affect existing virtual environments, since they reference the system Python’s standard library and binary extensions.

The Python executable in a virtual environment is effectively isolated from the one used to create it, but the supporting files are shared.

Warning

If you upgrade your system Python, existing virtual environments will still report the old version (the version number is embedded in the Python executable itself), but they will use the new version’s standard library and binary extensions. This normally works without issues, but be aware that the environment is effectively running a hybrid of old and new Python versions.

Python discovery[¶](https://virtualenv.pypa.io/en/latest/explanation.html#python-discovery "Link to this heading")
------------------------------------------------------------------------------------------------------------------

Before creating a virtual environment, virtualenv must locate a Python interpreter. The interpreter determines the virtual environment’s Python version, implementation (CPython, PyPy, etc.), and architecture (32-bit or 64-bit).

The `--python` flag accepts several specifier formats:

**Path specifier**
An absolute or relative path to a Python executable, such as `/usr/bin/python3.8` or `./python`.

**Version specifier**
A string following the format `{implementation}{version}{architecture}{machine}` where:

* Implementation is alphabetic characters (`python` means any implementation; if omitted, defaults to `python`).

* Version is dot-separated numbers, optionally followed by `t` for free-threading builds.

* Architecture is `-64` or `-32` (if omitted, means any architecture).

* Machine is the CPU instruction set architecture, e.g. `-arm64`, `-x86_64`, `-aarch64` (if omitted, means any machine). Cross-platform aliases are normalized automatically (`amd64` ↔ `x86_64`, `aarch64` ↔ `arm64`).

Examples:

* `python3.8.1` - Any Python implementation with version 3.8.1

* `3` - Any Python implementation with major version 3

* `3.13t` - Any Python implementation version 3.13 with free-threading enabled

* `cpython3` - CPython implementation with major version 3

* `pypy2` - PyPy implementation with major version 2

* `cpython3.12-64-arm64` - CPython 3.12, 64-bit, ARM64 architecture

* `3.11-64-x86_64` - Any implementation, version 3.11, 64-bit, x86_64 architecture

* `rustpython` - RustPython implementation

**PEP 440 version specifier**
Version constraints using PEP 440 operators:

* `>=3.12` - Any Python 3.12 or later

* `~=3.11.0` - Compatible with Python 3.11.0

* `cpython>=3.10` - CPython 3.10 or later

When you provide a specifier, virtualenv searches for matching interpreters using this strategy:

1. **Windows Registry** (Windows only): Check registered Python installations per [PEP 514](https://www.python.org/dev/peps/pep-0514/).

2. **uv-managed installations**: Check the `UV_PYTHON_INSTALL_DIR` environment variable or platform-specific uv Python directories for managed Python installations.

3. **PATH search**: Search for executables on the `PATH` environment variable with names matching the specification.

### Version manager shim resolution[¶](https://virtualenv.pypa.io/en/latest/explanation.html#version-manager-shim-resolution "Link to this heading")

Version managers like [pyenv](https://github.com/pyenv/pyenv), [mise](https://mise.jdx.dev/), and [asdf](https://asdf-vm.com/) place lightweight shim scripts on `PATH` that delegate to the real Python binary. When virtualenv discovers a Python interpreter by running it as a subprocess, shims may resolve to the wrong Python version (typically the system Python) because the shim’s resolution logic depends on shell environment state that doesn’t fully propagate to child processes.

virtualenv detects shims by checking whether the candidate executable lives in a known shim directory (`$PYENV_ROOT/shims`, `$MISE_DATA_DIR/shims`, or `$ASDF_DATA_DIR/shims`). When a shim is detected, virtualenv bypasses it and locates the real binary directly under the version manager’s `versions` directory, using the active version from:

1. The `PYENV_VERSION` environment variable (colon-separated for multiple versions).

2. A `.python-version` file in the current directory or any parent directory.

3. The global version file at `$PYENV_ROOT/version`.

This convention is shared across pyenv, mise, and asdf, so the same resolution logic works for all three.

Warning

Virtual environments typically reference the system Python’s standard library. If you upgrade the system Python, the virtual environment will report the old version (embedded in its Python executable) but will actually use the new version’s standard library content. This can cause confusion when debugging version-specific behavior.

If you use a virtual environment’s Python as the target for creating another virtual environment, virtualenv will detect the system Python version and create an environment matching the actual (upgraded) version, not the version reported by the virtual environment.

Creators[¶](https://virtualenv.pypa.io/en/latest/explanation.html#creators "Link to this heading")
--------------------------------------------------------------------------------------------------

Creators are responsible for constructing the virtual environment structure. virtualenv supports two types of creators:

**venv creator**
This creator delegates the entire creation process to the standard library’s `venv` module, following [PEP 405](https://www.python.org/dev/peps/pep-0405/). The venv creator has two limitations:

* It only works with Python 3.5 or later.

* It requires spawning a subprocess to invoke the venv module, unless virtualenv is installed in the system Python.

The subprocess overhead can be significant, especially on Windows where process creation is expensive.

**builtin creator**
This creator means virtualenv performs the creation itself by knowing exactly which files to create and which system files to reference. The builtin creator is actually a family of specialized creators for different combinations of Python implementation (CPython, PyPy, GraalPy, RustPython) and platform (Windows, POSIX). The name `builtin` is an alias that selects the first available builtin creator for the target environment.

Because builtin creators don’t require subprocess invocation, they’re generally faster than the venv creator.

virtualenv defaults to using the builtin creator if one is available for the target environment, falling back to the venv creator otherwise.

Seeders[¶](https://virtualenv.pypa.io/en/latest/explanation.html#seeders "Link to this heading")
------------------------------------------------------------------------------------------------

After creating the virtual environment structure, virtualenv installs seed packages that enable package management within the environment. The seed packages are:

* `pip` - The package installer for Python (always installed).

* `setuptools` - Package development and installation library (disabled by default on Python 3.12+).

* `wheel` - Support for the wheel binary package format (only installed by default on Python 3.8).

virtualenv supports two seeding methods with dramatically different performance characteristics:

**pip seeder**
This method uses the bundled pip wheel to install seed packages by spawning a child pip process. The subprocess performs a full installation, including unpacking wheels and generating metadata. This method is reliable but slow, typically consuming 98% of the total virtual environment creation time.

**app-data seeder**
This method creates reusable install images in a user application data directory. The first time you create an environment with specific seed package versions, the app-data seeder builds complete install images and stores them in the cache. Subsequent environment creations simply link or copy these pre-built images into the virtual environment’s `site-packages` directory.

Performance comparison for creating virtual environments:

On platforms that support symlinks efficiently (Linux, macOS), the app-data seeder provides nearly instant seeding.

You can override the cache location using the `VIRTUALENV_OVERRIDE_APP_DATA` environment variable.

### Wheel acquisition[¶](https://virtualenv.pypa.io/en/latest/explanation.html#wheel-acquisition "Link to this heading")

Both seeding methods require wheel files for the seed packages. virtualenv acquires wheels using a priority system:

**Embedded wheels**
virtualenv ships with a set of wheels bundled directly into the package. These are tested with the virtualenv release and provide a baseline set of seed packages. Different Python versions require different package versions, so virtualenv bundles multiple wheels to support its wide Python version range.

**Upgraded embedded wheels**
Users can manually upgrade the embedded wheels by running virtualenv with the `--upgrade-embed-wheels` flag. This fetches newer versions of seed packages from PyPI and stores them in the user application data directory. Subsequent virtualenv invocations will use these upgraded wheels instead of the embedded ones.

virtualenv can also perform periodic automatic upgrades (see below).

**Extra search directories**
Users can specify additional directories containing wheels using the `--extra-search-dir` flag. This is useful in air-gapped environments or when using custom package builds.

**PyPI download**
If no suitable wheel is found in the above locations, or if the `--download` flag is set, virtualenv will use pip to download the latest compatible version from PyPI.

### Periodic update mechanism[¶](https://virtualenv.pypa.io/en/latest/explanation.html#periodic-update-mechanism "Link to this heading")

To keep the seed packages reasonably current without requiring users to manually upgrade virtualenv or run `--upgrade-embed-wheels`, virtualenv implements a periodic automatic update system:

The 28-day waiting period protects users from automatically adopting newly released packages that might contain bugs. The 1-hour delay after download ensures continuous integration systems don’t start using different package versions mid-run, which could cause confusing test failures.

You can disable the periodic update mechanism with the `--no-periodic-update` flag.

### Distribution maintainer patching[¶](https://virtualenv.pypa.io/en/latest/explanation.html#distribution-maintainer-patching "Link to this heading")

Operating system distributions and package managers sometimes need to customize which seed package versions virtualenv uses. They want to align virtualenv’s bundled packages with system package versions.

Distributions can patch the `virtualenv.seed.wheels.embed` module, replacing the `get_embed_wheel` function with their own implementation that returns distribution-provided wheels. If they want to use virtualenv’s test suite for validation, they should also provide the `BUNDLE_FOLDER`, `BUNDLE_SUPPORT`, and `MAX` variables.

Distributions should also consider patching `virtualenv.seed.embed.base_embed.PERIODIC_UPDATE_ON_BY_DEFAULT` to `False`, allowing the system package manager to control seed package updates rather than virtualenv’s periodic update mechanism. Users can still manually request upgrades via `--upgrade-embed-wheels`, but automatic updates won’t interfere with system-managed packages.

Activators[¶](https://virtualenv.pypa.io/en/latest/explanation.html#activators "Link to this heading")
------------------------------------------------------------------------------------------------------

Activation scripts modify the current shell environment to prioritize the virtual environment’s executables. This is purely a convenience mechanism - you can always use absolute paths to virtual environment executables without activating.

What activation does:

**PATH modification**
The activation script prepends the virtual environment’s `bin` directory (`Scripts` on Windows) to the `PATH` environment variable. This ensures that when you run `python`, `pip`, or other executables, the shell finds the virtual environment’s versions first.

**Environment variables**
Activation sets several environment variables:

* `VIRTUAL_ENV` - Absolute path to the virtual environment directory.

* `VIRTUAL_ENV_PROMPT` - The prompt prefix (the environment name or custom value from `--prompt`).

* `PKG_CONFIG_PATH` - Modified to include the virtual environment’s `lib/pkgconfig` directory.

**Prompt modification**
By default, activation prepends the environment name to your shell prompt, typically shown as `(venv)` before the regular prompt. This visual indicator helps you remember which environment is active. You can customize this with the `--prompt` flag when creating the environment, or disable it entirely by setting the `VIRTUAL_ENV_DISABLE_PROMPT` environment variable.

**Deactivation**
Activation scripts also provide a `deactivate` command that reverses the changes, restoring your original PATH and removing the environment variables and prompt modifications.

virtualenv provides activation scripts for multiple shells:

* [Bash](https://www.gnu.org/software/bash/) (`activate`)

* [Fish](https://fishshell.com/) (`activate.fish`)

* [Csh/Tcsh](https://www.tcsh.org/) (`activate.csh`)

* [PowerShell](https://learn.microsoft.com/en-us/powershell/) (`activate.ps1`)

* [Windows Batch](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) (`activate.bat`)

* [Nushell](https://www.nushell.sh/) (`activate.nu`)

* Python (`activate_this.py`) – for programmatic activation from within a running Python process, see [Programmatic activation](https://virtualenv.pypa.io/en/latest/how-to/usage.html#programmatic-activation)

Note

On Windows 7 and later, PowerShell’s default execution policy is `Restricted`, which prevents running the `activate.ps1` script. You can allow locally-generated scripts to run by changing the execution policy:

Set-ExecutionPolicy RemoteSigned

Since virtualenv generates `activate.ps1` locally for each environment, PowerShell considers it a local script rather than a remote one and allows execution under the `RemoteSigned` policy.

Remember: activation is optional. The following commands are equivalent:

# With activation

source venv/bin/activate
python script.py
deactivate

# Without activation

venv/bin/python script.py

For a deeper dive into how activation works under the hood, see Allison Kaptur’s blog post [There’s no magic: virtualenv edition](https://www.recurse.com/blog/14-there-is-no-magic-virtualenv-edition), which explains how virtualenv uses `PATH` and `PYTHONHOME` to isolate virtual environments.

See also[¶](https://virtualenv.pypa.io/en/latest/explanation.html#see-also "Link to this heading")
--------------------------------------------------------------------------------------------------

* [Use virtualenv](https://virtualenv.pypa.io/en/latest/how-to/usage.html) - Practical guides for common virtualenv tasks.

* [Command line](https://virtualenv.pypa.io/en/latest/reference/cli.html) - Complete CLI reference documentation.
