# Pdm Documentation

Source: https://pdm-project.org/llms-full.txt

---

# PDM

# Usage

# Introduction

PDM, as described, is a modern Python package and dependency manager supporting the latest PEP standards. But it is more than a package manager. It boosts your development workflow in various aspects.

## Feature highlights

- Simple and fast dependency resolver, mainly for large binary distributions.
- A [PEP 517](https://www.python.org/dev/peps/pep-0517) build backend.
- [PEP 621](https://www.python.org/dev/peps/pep-0621) project metadata.
- Flexible and powerful plug-in system.
- Versatile user scripts.
- Install Pythons using [indygreg's python-build-standalone](https://github.com/astral-sh/python-build-standalone).
- Opt-in centralized installation cache like [pnpm](https://pnpm.io/motivation#saving-disk-space-and-boosting-installation-speed).

## Installation

PDM requires Python 3.9+ to be installed. It works on multiple platforms including Windows, Linux and macOS.

Note

You can still have your project working on lower Python versions, read how to do it [here](usage/project/#working-with-python-37).

Note

Alternatively, you can download the standalone binary file from the [release assets](https://github.com/pdm-project/pdm/releases).

### Recommended installation method

Install the prebuilt binary directly with the installer scripts.

```
curl -sSL https://pdm-project.org/install.sh | bash
```

To install a specific version:

```
curl -sSL https://pdm-project.org/install.sh | bash -s -- -v <version>
```

```
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install.ps1 | iex"
```

To install a specific version:

```
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install.ps1 | iex -Args '-v <version>'"
```

### Install via Python script

PDM requires python version 3.9 or higher.

Like Pip, PDM provides an installation script that will install PDM into an isolated environment.

```
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

```
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
```

Note

On Windows, if you do not have the optional `py` launcher installed (including if you installed Python through the Microsoft store), replace `py` with `python`.

For security reasons, you should verify the checksum of `install-pdm.py`. It can be downloaded from [install-pdm.py.sha256](https://pdm-project.org/install-pdm.py.sha256).

For example, on Linux/Mac:

```
curl -sSLO https://pdm-project.org/install-pdm.py
curl -sSL https://pdm-project.org/install-pdm.py.sha256 | shasum -a 256 -c -
# Run the installer
python3 install-pdm.py [options]
```

The installer will install PDM into the user site and the location depends on the system:

- `$HOME/.local/bin` for Unix
- `$HOME/Library/Python/<version>/bin` for MacOS
- `%APPDATA%\Python\Scripts` on Windows

You can pass additional options to the script to control how PDM is installed:

```
usage: install-pdm.py [-h] [-v VERSION] [--prerelease] [--remove] [-p PATH] [-d DEP]

optional arguments:
  -h, --help            show this help message and exit
  -v VERSION, --version VERSION | envvar: PDM_VERSION
                        Specify the version to be installed, or HEAD to install from the main branch
  --prerelease | envvar: PDM_PRERELEASE    Allow prereleases to be installed
  --remove | envvar: PDM_REMOVE            Remove the PDM installation
  -p PATH, --path PATH | envvar: PDM_HOME  Specify the location to install PDM
  -d DEP, --dep DEP | envvar: PDM_DEPS     Specify additional dependencies, can be given multiple times
```

You can either pass the options after the script or set the env var value.

### Other installation methods

```
brew install pdm
```

```
scoop bucket add frostming https://github.com/frostming/scoop-frostming.git
scoop install pdm
```

```
uv tool install pdm
```

```
pipx install pdm
```

Install the head version of GitHub repository. Make sure you have installed [Git LFS](https://git-lfs.github.com/) on your system.

```
pipx install git+https://github.com/pdm-project/pdm.git@main#egg=pdm
```

To install PDM with all features:

```
pipx install pdm[all]
```

See also: <https://pypa.github.io/pipx/>

```
pip install --user pdm
```

Assuming you have [asdf](https://asdf-vm.com/) installed.

```
asdf plugin add pdm
asdf install pdm latest
asdf local pdm latest
```

By copying the [Pyprojectx](https://pyprojectx.github.io/) wrapper scripts to a project, you can install PDM as (npm-style) dev dependency inside that project. This allows different projects/branches to use different PDM versions.

To [initialize a new or existing project](https://pyprojectx.github.io/usage/#initialize-a-new-or-existing-project), cd into the project folder and:

```
curl -LO https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip && unzip wrappers.zip && rm -f wrappers.zip
./pw --add pdm
```

```
Invoke-WebRequest https://github.com/pyprojectx/pyprojectx/releases/latest/download/wrappers.zip -OutFile wrappers.zip; Expand-Archive -Path wrappers.zip -DestinationPath .; Remove-Item -Path wrappers.zip
.\pw --add pdm
```

When installing pdm with this method, you need to run all `pdm` commands through the `pw` wrapper:

```
./pw pdm install
```

### Update the PDM version

```
pdm self update
```

### Uninstallation

If you need to remove PDM from your system, you can use the following script:

```
curl -sSL https://pdm-project.org/install-pdm.py | python3 - --remove
```

```
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py - --remove"
```

If you installed PDM using a third-party package management tool like Homebrew, you can also uninstall PDM using the tool's uninstall method, such as `brew uninstall pdm`.

## Packaging Status

## Shell Completion

PDM supports generating completion scripts for Bash, Zsh, Fish or Powershell. Here are some common locations for each shell:

```
pdm completion bash > /etc/bash_completion.d/pdm.bash-completion # Requires root (sudo). For an alternative, see next
pdm completion bash > ~/.bash_completion # Does not require root (sudo). Installed only for your user account
```

```
# Make sure ~/.zfunc is added to fpath, before compinit.
pdm completion zsh > ~/.zfunc/_pdm
```

Oh-My-Zsh:

```
mkdir $ZSH_CUSTOM/plugins/pdm
pdm completion zsh > $ZSH_CUSTOM/plugins/pdm/_pdm
```

Then make sure pdm plugin is enabled in ~/.zshrc

```
pdm completion fish > ~/.config/fish/completions/pdm.fish
```

```
# Create a directory to store completion scripts
mkdir $PROFILE\..\Completions
echo @'
Get-ChildItem "$PROFILE\..\Completions\" | ForEach-Object {
    . $_.FullName
}
'@ | Out-File -Append -Encoding utf8 $PROFILE
# Generate script
Set-ExecutionPolicy Unrestricted -Scope CurrentUser
pdm completion powershell | Out-File -Encoding utf8 $PROFILE\..\Completions\pdm_completion.ps1
```

## Virtualenv and PEP 582

PDM offers experimental support for [PEP 582](https://www.python.org/dev/peps/pep-0582/) as an opt-in feature, in addition to virtualenv management. Although [the Python Steering Council has rejected PEP 582](https://discuss.python.org/t/pep-582-python-local-packages-directory/963/430), you can still test it out using PDM.

To learn more about the two modes, refer to the relevant chapters on [Working with virtualenv](usage/venv/) and [Working with PEP 582](usage/pep582/).

## PDM Eco-system

[Awesome PDM](https://github.com/pdm-project/awesome-pdm) is a curated list of awesome PDM plugins and resources.

## Sponsors

# Advanced Usage

## Automatic Testing

### Use Tox as the runner

[Tox](https://tox.readthedocs.io/en/latest/) is a great tool for testing against multiple Python versions or dependency sets. You can configure a `tox.ini` like the following to integrate your testing with PDM:

```
[tox]
env_list = py{36,37,38},lint

[testenv]
setenv =
    PDM_IGNORE_SAVED_PYTHON="1"
deps = pdm
commands =
    pdm install --dev
    pytest tests

[testenv:lint]
deps = pdm
commands =
    pdm install -G lint
    flake8 src/
```

To use the virtualenv created by Tox, you should make sure you have set `pdm config python.use_venv true`. PDM then will install dependencies from [`pdm lock`](../../reference/cli/#lock) into the virtualenv. In the dedicated venv you can directly run tools by `pytest tests/` instead of `pdm run pytest tests/`.

You should also make sure you don't run `pdm add/pdm remove/pdm update/pdm lock` in the test commands, otherwise the [`pdm lock`](../../reference/cli/#lock) file will be modified unexpectedly. Additional dependencies can be supplied with the `deps` config. Besides, `isolated_build` and `passenv` config should be set as the above example to make PDM work properly.

To get rid of these constraints, there is a Tox plugin [tox-pdm](https://github.com/pdm-project/tox-pdm) which can ease the usage. You can install it by

```
pip install tox-pdm
```

Or,

```
pdm add --dev tox-pdm
```

And you can make the `tox.ini` much tidier as following, :

```
[tox]
env_list = py{36,37,38},lint

[testenv]
groups = dev
commands =
    pytest tests

[testenv:lint]
groups = lint
commands =
    flake8 src/
```

See the [project's README](https://github.com/pdm-project/tox-pdm) for a detailed guidance.

### Use Nox as the runner

[Nox](https://nox.thea.codes/) is another great tool for automated testing. Unlike tox, Nox uses a standard Python file for configuration.

It is much easier to use PDM in Nox, here is an example of `noxfile.py`:

```
import os
import nox

os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})

@nox.session
def tests(session):
    session.run_always('pdm', 'install', '-G', 'test', external=True)
    session.run('pytest')

@nox.session
def lint(session):
    session.run_always('pdm', 'install', '-G', 'lint', external=True)
    session.run('flake8', '--import-order-style', 'google')
```

Note that `PDM_IGNORE_SAVED_PYTHON` should be set so that PDM can pick up the Python in the virtualenv correctly. Also make sure `pdm` is available in the `PATH`. Before running nox, you should also ensure configuration item `python.use_venv` is true to enable venv reusing.

### About PEP 582 `__pypackages__` directory

By default, if you run tools by [`pdm run`](../../reference/cli/#run), `__pypackages__` will be seen by the program and all subprocesses created by it. This means virtual environments created by those tools are also aware of the packages inside `__pypackages__`, which result in unexpected behavior in some cases. For `nox`, you can avoid this by adding a line in `noxfile.py`:

```
os.environ.pop("PYTHONPATH", None)
```

For `tox`, `PYTHONPATH` will not be passed to the test sessions so this isn't going to be a problem. Moreover, it is recommended to make `nox` and `tox` live in their own pipx environments so you don't need to install for every project. In this case, PEP 582 packages will not be a problem either.

## Use PDM in Continuous Integration

Only one thing to keep in mind -- PDM can't be installed on Python < 3.7, so if your project is to be tested on those Python versions, you have to make sure PDM is installed on the correct Python version, which can be different from the target Python version the particular job/task is run on.

Fortunately, if you are using GitHub Action, there is [pdm-project/setup-pdm](https://github.com/marketplace/actions/setup-pdm) to make this process easier. Here is an example workflow of GitHub Actions, while you can adapt it for other CI platforms.

```
Testing:
  runs-on: ${{ matrix.os }}
  strategy:
    matrix:
      python-version: ['3.9', '3.10', '3.11', '3.12', '3.13']
      os: [ubuntu-latest, macOS-latest, windows-latest]

  steps:
    - uses: actions/checkout@v4
    - name: Set up PDM
      uses: pdm-project/setup-pdm@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        pdm sync -d -G testing
    - name: Run Tests
      run: |
        pdm run -v pytest tests
```

TIPS

For GitHub Action users, there is a [known compatibility issue](https://github.com/actions/virtual-environments/issues/2803) on Ubuntu virtual environment. If PDM parallel install is failed on that machine you should either set `parallel_install` to `false` or set env `LD_PRELOAD=/lib/x86_64-linux-gnu/libgcc_s.so.1`. It is already handled by the `pdm-project/setup-pdm` action.

Note

If your CI scripts run without a proper user set, you might get permission errors when PDM tries to create its cache directory. To work around this, you can set the HOME environment variable yourself, to a writable directory, for example:

```
export HOME=/tmp/home
```

## Use PDM in a multi-stage Dockerfile

It is possible to use PDM in a multi-stage Dockerfile to first install the project and dependencies into `__pypackages__` and then copy this folder into the final stage, adding it to `PYTHONPATH`.

```
ARG PYTHON_BASE=3.10-slim
# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false
# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

# install dependencies and project into the local packages directory
WORKDIR /project
RUN pdm install --check --prod --no-editable

# run stage
FROM python:$PYTHON_BASE

# retrieve packages from build stage
COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
# set command/entrypoint, adapt to fit your needs
COPY src /project/src
CMD ["python", "src/__main__.py"]
```

## Use PDM to manage a monorepo

With PDM, you can have multiple sub-packages within a single project, each with its own `pyproject.toml` file. And you can create only one `pdm.lock` file to lock all dependencies. The sub-packages can have each other as their dependencies. To achieve this, follow these steps:

`project/pyproject.toml`:

```
[dependency-groups]
dev = [
    "-e file:///${PROJECT_ROOT}/packages/foo-core",
    "-e file:///${PROJECT_ROOT}/packages/foo-cli",
    "-e file:///${PROJECT_ROOT}/packages/foo-app",
]
```

`packages/foo-cli/pyproject.toml`:

```
[project]
dependencies = ["foo-core"]
```

`packages/foo-app/pyproject.toml`:

```
[project]
dependencies = ["foo-core"]
```

Now, run `pdm install` in the project root, and you will get a `pdm.lock` with all dependencies locked. All sub-packages will be installed in editable mode.

Look at the [🚀 Example repository](https://github.com/pdm-project/pdm-example-monorepo) for more details.

## Hooks for `pre-commit`

[`pre-commit`](https://pre-commit.com/) is a powerful framework for managing git hooks in a centralized fashion. PDM already uses `pre-commit` [hooks](https://github.com/pdm-project/pdm/blob/main/.pre-commit-config.yaml) for its internal QA checks. PDM exposes also several hooks that can be run locally or in CI pipelines.

### Export `requirements.txt`

This hook wraps the command `pdm export` along with any valid argument. It can be used as a hook (e.g., for CI) to ensure that you are going to check in the codebase a `requirements.txt`, which reflects the actual content of [`pdm lock`](../../reference/cli/#lock).

```
# export python requirements
- repo: https://github.com/pdm-project/pdm
  rev: 2.x.y # a PDM release exposing the hook
  hooks:
    - id: pdm-export
      # command arguments, e.g.:
      args: ['-o', 'requirements.txt', '--without-hashes']
      files: ^pdm.lock$
```

### Check `pdm.lock` is up to date with pyproject.toml

This hook wraps the command `pdm lock --check` along with any valid argument. It can be used as a hook (e.g., for CI) to ensure that whenever `pyproject.toml` has a dependency added/changed/removed, that `pdm.lock` is also up to date.

```
- repo: https://github.com/pdm-project/pdm
  rev: 2.x.y # a PDM release exposing the hook
  hooks:
    - id: pdm-lock-check
```

### Sync current working set with `pdm.lock`

This hook wraps the command `pdm sync` along with any valid argument. It can be used as a hook to ensure that your current working set is synced with `pdm.lock` whenever you checkout or merge a branch. Add *keyring* to `additional_dependencies` if you want to use your systems credential store.

```
- repo: https://github.com/pdm-project/pdm
  rev: 2.x.y # a PDM release exposing the hook
  hooks:
    - id: pdm-sync
      additional_dependencies:
        - keyring
```

# Configure the Project

PDM's `config` command works just like `git config`, except that `--list` isn't needed to show configurations.

Show the current configurations:

```
pdm config
```

Get one single configuration:

```
pdm config pypi.url
```

Change a configuration value and store in home configuration:

```
pdm config pypi.url "https://test.pypi.org/simple"
```

By default, the configuration are changed globally, if you want to make the config seen by this project only, add a `--local` flag:

```
pdm config --local pypi.url "https://test.pypi.org/simple"
```

Any local configurations will be stored in `pdm.toml` under the project root directory.

## Configuration files

The configuration files are searched in the following order:

1. `<PROJECT_ROOT>/pdm.toml` - The project configuration
1. `<CONFIG_ROOT>/config.toml` - The home configuration
1. `<SITE_CONFIG_ROOT>/config.toml` - The site configuration

where `<CONFIG_ROOT>` is:

- `$XDG_CONFIG_HOME/pdm` (`~/.config/pdm` in most cases) on Linux as defined by [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
- `~/Library/Application Support/pdm` on macOS as defined by [Apple File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)
- `%USERPROFILE%\AppData\Local\pdm\pdm` on Windows as defined in [Known folders](https://docs.microsoft.com/en-us/windows/win32/shell/known-folders)

and `<SITE_CONFIG_ROOT>` is:

- `$XDG_CONFIG_DIRS/pdm` (`/etc/xdg/pdm` in most cases) on Linux as defined by [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html)
- `/Library/Application Support/pdm` on macOS as defined by [Apple File System Basics](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)
- `%ProgramData%\pdm\pdm` on Windows as defined in [Known folders](https://docs.microsoft.com/en-us/windows/win32/shell/known-folders)

If `-g/--global` option is used, the first item will be replaced by `<CONFIG_ROOT>/global-project/pdm.toml`.

You can find all available configuration items in [Configuration Page](../../reference/configuration/).

## Configure the Python finder

By default, PDM will try to find Python interpreters in the following sources:

- `venv`: The PDM virtualenv location
- `path`: The `PATH` environment variable
- `pyenv`: The [pyenv](https://github.com/pyenv/pyenv) install root
- `rye`: The [rye](https://rye-up.com/) toolchain install root
- `asdf`: The [asdf](https://asdf-vm.com/) python install root
- `winreg`: The Windows registry

You can unselect some of them or change the order by setting `python.providers` config key:

```
pdm config python.providers rye   # Rye source only
pdm config python.providers pyenv,asdf  # pyenv and asdf
```

## Allow prereleases in resolution result

By default, `pdm`'s dependency resolver will ignore prereleases unless there are no stable versions for the given version range of a dependency. This behavior can be changed by setting `allow-prereleases` to `true` in `[tool.pdm.resolution]` table:

```
[tool.pdm.resolution]
allow-prereleases = true
```

## Configure the package indexes

You can tell PDM where to to find the packages by either specifying sources in the `pyproject.toml` or via `pypi.*` configurations.

Add sources in `pyproject.toml`:

```
[[tool.pdm.source]]
name = "private"
url = "https://private.pypi.org/simple"
verify_ssl = true
```

Change the default index via `pdm config`:

```
pdm config pypi.url "https://test.pypi.org/simple"
```

Add extra indexes via `pdm config`:

```
pdm config pypi.extra.url "https://extra.pypi.org/simple"
```

The available configuration options are:

- `url`: The URL of the index
- `verify_ssl`: (Optional)Whether to verify SSL certificates, default to true
- `username`: (Optional)The username for the index
- `password`: (Optional)The password for the index
- `type`: (Optional) index or find_links, default to index

About the source types

By default, all sources are [PEP 503](https://www.python.org/dev/peps/pep-0503/) style "indexes" like pip's `--index-url` and `--extra-index-url`, however, you can set the type to `find_links` which contains files or links to be looked for directly. See [this answer](https://stackoverflow.com/a/46651848) for the difference between the two types.

For example, to use a local directory as a source:

```
[[tool.pdm.source]]
name = "local"
url = "file:///${PROJECT_ROOT}/packages"
type = "find_links"
```

These configurations are read in the following order to build the final source list:

- `pypi.url`, if `pypi` doesn't appear in the `name` field of any source in `pyproject.toml`
- Sources in `pyproject.toml`
- `pypi.<name>.url` in PDM config.

You can set `pypi.ignore_stored_index` to `true` to disable all additional indexes from the PDM config and only use those specified in `pyproject.toml`.

Disable the default PyPI index

If you want to omit the default PyPI index, just set the source name to `pypi` and that source will **replace** it.

```
[[tool.pdm.source]]
url = "https://private.pypi.org/simple"
verify_ssl = true
name = "pypi"
```

Indexes in `pyproject.toml` or config

When you want to share the indexes with other people who are going to use the project, you should add them in `pyproject.toml`. For example, some packages only exist in a private index and can't be installed if someone doesn't configure the index. Otherwise, store them in the local config which won't be seen by others.

### Respect the order of the sources

By default, all sources are considered equal, packages from them are sorted by the version and wheel tags, the most matching one with the highest version is selected.

In some cases you may want to return packages from the preferred source, and search for others if they are missing from the former source. PDM supports this by reading the configuration `respect-source-order`. For example:

```
[tool.pdm.resolution]
respect-source-order = true

[[tool.pdm.source]]
name = "private"
url = "https://private.pypi.org/simple"

[[tool.pdm.source]]
name = "pypi"
url = "https://pypi.org/simple"
```

A package will be searched from the `private` index first, and only if no matching version is found there, it will be searched from the `pypi` index.

### Specify index for individual packages

You can bind packages to specific sources with `include_packages` and `exclude_packages` config under `tool.pdm.source` table.

```
[[tool.pdm.source]]
name = "private"
url = "https://private.pypi.org/simple"
include_packages = ["foo", "foo-*"]
exclude_packages = ["bar-*"]
```

With the above configuration, any package matching `foo` or `foo-*` will only be searched from the `private` index, and any package matching `bar-*` will be searched from all indexes except `private`.

Both `include_packages` and `exclude_packages` are optional and accept a list of glob patterns, and `include_packages` takes effect exclusively when the pattern matches.

### Store credentials with the index

You can specify credentials in the URL with `${ENV_VAR}` variable expansion and these variables will be read from the environment variables:

```
[[tool.pdm.source]]
name = "private"
url = "https://${PRIVATE_PYPI_USERNAME}:${PRIVATE_PYPI_PASSWORD}@private.pypi.org/simple"
```

### Configure HTTPS certificates

You can use a custom CA bundle or client certificate for HTTPS requests. It can be configured for both indexes(for package download) and repositories(for upload):

```
pdm config pypi.ca_certs /path/to/ca_bundle.pem
pdm config repository.pypi.ca_certs /path/to/ca_bundle.pem
```

Besides, it is possible to use the system trust store, instead of the bundled certifi certificates for verifying HTTPS certificates. This approach will typically support corporate proxy certificates without additional configuration.

To use `truststore`, you need Python 3.10 or newer and install `truststore` into the same environment as PDM:

```
pdm self add truststore
```

In addition, CA certificates specified by env vars `REQUESTS_CA_BUNDLE` and `CURL_CA_BUNDLE` will be used if they are set.

### Index configuration merging

Index configurations are merged with the `name` field of `[[tool.pdm.source]]` table or `pypi.<name>` key in the config file. This enables you to store the url and credentials separately, to avoid secrets being exposed in the source control. For example, if you have the following configuration:

```
[[tool.pdm.source]]
name = "private"
url = "https://private.pypi.org/simple"
```

You can store the credentials in the config file:

```
pdm config pypi.private.username "foo"
pdm config pypi.private.password "bar"
```

PDM can retrieve the configurations for `private` index from both places.

If the index requires a username and password, but they can't be found from the environment variables nor config file, PDM will prompt you to enter them. Or, if `keyring` is installed, it will be used as the credential store. PDM can use the `keyring` from either the installed package or the CLI.

## Central installation caches

If a package is required by many projects on the system, each project has to keep its own copy. This can be a waste of disk space, especially for data science and machine learning projects.

PDM supports *caching* installations of the same wheel by installing it in a centralized package repository and linking to that installation in different projects. To enable it, run:

```
pdm config install.cache on
```

It can be enabled on a per-project basis by adding the `--local` option to the command.

The caches are located in `$(pdm config cache_dir)/packages`. You can view the cache usage with `pdm cache info`. Note that the cached installations are managed automatically -- they will be deleted if they are not linked to any projects. Manually deleting the caches from disk may break some projects on the system.

In addition, several different link methods are supported:

- `symlink`(default), create symlinks to the package files.
- `hardlink`, create hard links to the package files of the cache entry.

You can switch between them by running `pdm config [--local] install.cache_method <method>`.

Note

Only packages installed from one of the package sources can be cached.

## Configure the repositories for upload

When using the [`pdm publish`](../../reference/cli/#publish) command, it reads the repository secrets from the **global** config file(`<CONFIG_ROOT>/config.toml`). The content of the config is as follows:

```
[repository.pypi]
username = "frostming"
password = "<secret>"

[repository.company]
url = "https://pypi.company.org/legacy/"
username = "frostming"
password = "<secret>"
ca_certs = "/path/to/custom-cacerts.pem"
```

Alternatively, these credentials can be provided with env vars:

```
export PDM_PUBLISH_REPO=...
export PDM_PUBLISH_USERNAME=...
export PDM_PUBLISH_PASSWORD=...
export PDM_PUBLISH_CA_CERTS=...
```

A PEM-encoded Certificate Authority bundle (`ca_certs`) can be used for local / custom PyPI repositories where the server certificate is not signed by the standard [certifi](https://github.com/certifi/python-certifi/blob/master/certifi/cacert.pem) CA bundle.

Note

Repositories are different from indexes in the previous section. Repositories are for publishing while indexes are for locking and resolving. They don't share the configuration.

Tip

You don't need to configure the `url` for `pypi` and `testpypi` repositories, they are filled by default values. The username, password, and certificate authority bundle can be passed in from the command line for `pdm publish` via `--username`, `--password`, and `--ca-certs`, respectively.

To change the repository config from the command line, use the [`pdm config`](../../reference/cli/#config) command:

```
pdm config repository.pypi.username "__token__"
pdm config repository.pypi.password "my-pypi-token"

pdm config repository.company.url "https://pypi.company.org/legacy/"
pdm config repository.company.ca_certs "/path/to/custom-cacerts.pem"
```

## Password management with keyring

When keyring is available and supported, the passwords will be stored to and retrieved from the keyring instead of writing to the config file. This supports both indexes and upload repositories. The service name will be `pdm-pypi-<name>` for an index and `pdm-repository-<name>` for a repository.

You can enable keyring by either installing `keyring` into the same environment as PDM or installing globally. To add keyring to the PDM environment:

```
pdm self add keyring
```

Alternatively, if you have installed a copy of keyring globally, make sure the CLI is exposed in the `PATH` env var to make it discoverable by PDM:

```
export PATH=$PATH:path/to/keyring/bin
```

### Password management with keyring for Azure Artifacts

When trying to authenticate towards azure artifacts, this can be achieved by either using AD groups to authenticate: `pdm self add keyring artifacts-keyring` ensuring that artifacts-keyring will be used for authentication.

And then adding the artifacts url to `pyproject.toml`

```
[[tool.pdm.source]]
name = "NameOfFeed"
url = "https://pkgs.dev.azure.com/[org name]/_packaging/[feed name]/pypi/simple/"
```

## Exclude specific packages and their dependencies from the lock file

Added in version 2.12.0

Sometimes you don't even want to include certain packages in the locked file because you are sure they won't be used by any code. In this case, you can completely skip them and their dependencies during dependency resolution:

```
[tool.pdm.resolution]
excludes = ["requests"]
```

With this config, `requests` will not be locked in the lockfile, and its dependencies such as `urllib3` and `idna` will also not show up in the resolution result, if not depended on by other packages. The installer will not be able to pick them up either.

## Passing constant arguments to every pdm invocation

Added in version 2.7.0

You can add extra options passed to individual pdm commands by `tool.pdm.options` configuration:

```
[tool.pdm.options]
add = ["--no-isolation", "--no-self"]
install = ["--no-self"]
lock = ["--no-cross-platform"]
```

These options will be added right after the command name. For instance, based on the configuration above, `pdm add requests` is equivalent to `pdm add --no-isolation --no-self requests`.

## Ignore package warnings

Added in version 2.10.0

You may see some warnings when resolving dependencies like this:

```
PackageWarning: Skipping scipy@1.10.0 because it requires Python
<3.12,>=3.8 but the project claims to work with Python>=3.9.
Narrow down the `requires-python` range to include this version. For example, ">=3.9,<3.12" should work.
  warnings.warn(record.message, PackageWarning, stacklevel=1)
Use `-q/--quiet` to suppress these warnings, or ignore them per-package with `ignore_package_warnings` config in [tool.pdm] table.
```

This is because the supported range of Python versions of the package doesn't cover the `requires-python` value specified in the `pyproject.toml`. You can ignore these warnings in a per-package basis by adding the following config:

```
[tool.pdm]
ignore_package_warnings = ["scipy", "tensorflow-*"]
```

Where each item is a case-insensitive glob pattern to match the package name.

# Manage Dependencies

PDM provides a bunch of useful commands to help manage your project and dependencies. The following examples are run on Ubuntu 18.04, a few changes must be done if you are using Windows.

## Add dependencies

[`pdm add`](../../reference/cli/#add) can be followed by one or several dependencies, and the dependency specification is described in [PEP 508](https://www.python.org/dev/peps/pep-0508/).

Examples:

```
pdm add requests   # add requests
pdm add requests==2.25.1   # add requests with version constraint
pdm add requests[socks]   # add requests with extra dependency
pdm add "flask>=1.0" flask-sqlalchemy   # add multiple dependencies with different specifiers
```

PDM also allows extra dependency groups by providing `-G/--group <name>` option, and those dependencies will go to `[project.optional-dependencies.<name>]` table in the project file, respectively.

You can reference other optional groups in `optional-dependencies`, even before the package is uploaded:

```
[project]
name = "foo"
version = "0.1.0"

[project.optional-dependencies]
socks = ["pysocks"]
jwt = ["pyjwt"]
all = ["foo[socks,jwt]"]
```

After that, dependencies and sub-dependencies will be resolved properly and installed for you, you can view `pdm.lock` to see the resolved result of all dependencies.

### Local dependencies

Local packages can be added with their paths. The path can be a file or a directory:

```
pdm add ./sub-package
pdm add ./first-1.0.0-py2.py3-none-any.whl
```

The paths MUST start with a `.`, otherwise it will be recognized as a normal named requirement. The local dependencies will be written to the `pyproject.toml` file with the URL format:

```
[project]
dependencies = [
    "sub-package @ file:///${PROJECT_ROOT}/sub-package",
    "first @ file:///${PROJECT_ROOT}/first-1.0.0-py2.py3-none-any.whl",
]
```

Using other build backends

If you are using `hatchling` instead of the pdm backend, the URLs would be as follows:

```
sub-package @ {root:uri}/sub-package
first @ {root:uri}/first-1.0.0-py2.py3-none-any.whl
```

Other backends doesn't support encoding relative paths in the URL and will write the absolute path instead.

### URL dependencies

PDM also supports downloading and installing packages directly from a web address.

Examples:

```
# Install gzipped package from a plain URL
pdm add "https://github.com/numpy/numpy/releases/download/v1.20.0/numpy-1.20.0.tar.gz"
# Install wheel from a plain URL
pdm add "https://github.com/explosion/spacy-models/releases/download/en_core_web_trf-3.5.0/en_core_web_trf-3.5.0-py3-none-any.whl"
```

### VCS dependencies

You can also install from a git repository url or other version control systems. The following are supported:

- Git: `git`
- Mercurial: `hg`
- Subversion: `svn`
- Bazaar: `bzr`

The URL should be like: `{vcs}+{url}@{rev}`

Examples:

```
# Install pip repo on tag `22.0`
pdm add "git+https://github.com/pypa/pip.git@22.0"
# Provide credentials in the URL
pdm add "git+https://username:password@github.com/username/private-repo.git@master"
# Give a name to the dependency
pdm add "pip @ git+https://github.com/pypa/pip.git@22.0"
# Or use the #egg fragment
pdm add "git+https://github.com/pypa/pip.git@22.0#egg=pip"
# Install from a subdirectory
pdm add "git+https://github.com/owner/repo.git@master#egg=pkg&subdirectory=subpackage"
```

To use ssh scheme for git, just replace `https://` to `ssh://git@`

Example:

```
pdm add "wheel @ git+ssh://git@github.com/pypa/wheel.git@main"
```

Or the short non-URI form, which uses a colon(`:`) to separate the host and path:

```
pdm add "wheel @ git+git@github.com:pypa/wheel.git@main"
```

### Hide credentials in the URL

You can hide the credentials in the URL by using the `${ENV_VAR}` variable syntax:

```
[project]
dependencies = [
  "mypackage @ git+http://${VCS_USER}:${VCS_PASSWD}@test.git.com/test/mypackage.git@master"
]
```

These variables will be read from the environment variables when installing the project.

### Add development only dependencies

Added in version 1.5.0

PDM also supports defining groups of dependencies that are useful for development, e.g. some for testing and others for linting. We usually don't want these dependencies to appear in the distribution's metadata so using `optional-dependencies` is probably not a good idea. We can define them as development dependencies:

```
pdm add -dG test pytest
```

This will result in a `pyproject.toml` as following:

```
[dependency-groups]
test = ["pytest"]
```

You can have several groups of development only dependencies. Unlike `optional-dependencies`, they won't appear in the package distribution metadata such as `PKG-INFO` or `METADATA`, which means the package index won't be aware of these dependencies. The schema is similar to that of `optional-dependencies`.

```
[dependency-groups]
lint = [
    "flake8",
    "black"
]
test = ["pytest", "pytest-cov"]
doc = ["mkdocs"]
```

For backward-compatibility, if only `-d` or `--dev` is specified, dependencies will go to `dev` group under `[dependency-groups]` by default.

Note

The same group name MUST NOT appear in both `[dependency-groups]` and `[project.optional-dependencies]`.

### Editable dependencies

**Local directories** and **VCS dependencies** can be installed in [editable mode](https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs). If you are familiar with `pip`, it is just like `pip install -e <package>`. **Editable packages are allowed only in development dependencies**:

Note

Editable installs are only allowed in the `dev` dependency group. Other groups, including the default, will fail with a `[PdmUsageError]`.

```
# A relative path to the directory
pdm add -e ./sub-package --dev
# A file URL to a local directory
pdm add -e file:///path/to/sub-package --dev
# A VCS URL
pdm add -e git+https://github.com/pallets/click.git@main#egg=click --dev
```

### Save version specifiers

If the package is given without a version specifier like `pdm add requests`. PDM provides three different behaviors of what version specifier is saved for the dependency, which is given by `--save-<strategy>`(Assume `2.21.0` is the latest version that can be found for the dependency):

- `minimum`: Save the minimum version specifier: `>=2.21.0` (default).
- `compatible`: Save the compatible version specifier: `>=2.21.0,<3.0.0`.
- `exact`: Save the exact version specifier: `==2.21.0`.
- `wildcard`: Don't constrain version and leave the specifier to be wildcard: `*`.

### Add prereleases

One can give `--pre/--prerelease` option to [`pdm add`](../../reference/cli/#add) so that prereleases are allowed to be pinned for the given packages.

## Update existing dependencies

To update all dependencies in the lock file:

```
pdm update
```

To update the specified package(s):

```
pdm update requests
```

To update multiple groups of dependencies:

```
pdm update -G security -G http
```

Or using comma-separated list:

```
pdm update -G "security,http"
```

To update a given package in the specified group:

```
pdm update -G security cryptography
```

If the group is not given, PDM will search for the requirement in the default dependencies set and raises an error if none is found.

To update packages in development dependencies:

```
# Update all default + dev-dependencies
pdm update -d
# Update a package in the specified group of dev-dependencies
pdm update -dG test pytest
```

### About update strategy

Similarly, PDM also provides 3 different behaviors of updating dependencies and sub-dependencies, which is given by `--update-<strategy>` option:

- `reuse`: Keep all locked dependencies except for those given in the command line (default).
- `reuse-installed`: Try to reuse the versions installed in the working set. **This will also affect the packages requested in the command line**.
- `eager`: Try to lock a newer version of the packages in command line and their recursive sub-dependencies and keep other dependencies as they are.
- `all`: Update all dependencies and sub-dependencies.

### Update packages to the versions that break the version specifiers

One can give `-u/--unconstrained` to tell PDM to ignore the version specifiers in the `pyproject.toml`. This works similarly to the `yarn upgrade -L/--latest` command. Besides, [`pdm update`](../../reference/cli/#update_2) also supports the `--pre/--prerelease` option.

## Remove existing dependencies

To remove existing dependencies from project file and the library directory:

```
# Remove requests from the default dependencies
pdm remove requests
# Remove h11 from the 'web' group of optional-dependencies
pdm remove -G web h11
# Remove pytest-cov from the `test` group of dependency-groups
pdm remove -dG test pytest-cov
```

## List outdated packages and the latest versions

Added in version 2.13.0

To list outdated packages and the latest versions:

```
pdm outdated
```

You can pass glob patterns to filter the packages to show:

```
pdm outdated requests* flask*
```

## Select a subset of dependency groups to install

Say we have a project with following dependencies:

```
[project]  # This is production dependencies
dependencies = ["requests"]

[project.optional-dependencies]  # This is optional dependencies
extra1 = ["flask"]
extra2 = ["django"]

[dependency-groups]  # This is dev dependencies
dev1 = ["pytest"]
dev2 = ["mkdocs"]
```

| Command                         | What it does                                                         | Comments                  |
| ------------------------------- | -------------------------------------------------------------------- | ------------------------- |
| `pdm install`                   | install all groups locked in the lockfile                            |                           |
| `pdm install -G extra1`         | install prod deps, dev deps, and "extra1" optional group             |                           |
| `pdm install -G dev1`           | install prod deps and only "dev1" dev group                          |                           |
| `pdm install -G:all`            | install prod deps, dev deps and "extra1", "extra2" optional groups   |                           |
| `pdm install -G extra1 -G dev1` | install prod deps, "extra1" optional group and only "dev1" dev group |                           |
| `pdm install --prod`            | install prod only                                                    |                           |
| `pdm install --prod -G extra1`  | install prod deps and "extra1" optional                              |                           |
| `pdm install --prod -G dev1`    | Fail, `--prod` can't be given with dev dependencies                  | Leave the `--prod` option |

**All** development dependencies are included as long as `--prod` is not passed and `-G` doesn't specify any dev groups.

Besides, if you don't want the root project to be installed, add `--no-self` option, and `--no-editable` can be used when you want all packages to be installed in non-editable versions.

You may also use the pdm lock command with these options to lock only the specified groups, which will be recorded in the `[metadata]` table of the lock file. If no `--group/--prod/--dev/--no-default` option is specified, `pdm sync` and `pdm update` will operate using the groups in the lockfile. However, if any groups that are not included in the lockfile are given as arguments to the commands, PDM will raise an error.

## Dependency Overrides

If none of versions of a specific package doesn't meet all the constraints, the resolution will fail. In this case, you can tell the resolver to use a specific version of the package with dependency overrides.

Overrides are a useful last resort for cases in which the user knows that a dependency is compatible with a newer version of a package than the package declares, but the package has not yet been updated to declare that compatibility.

For example, if a transitive dependency declares `pydantic>=1.0,<2.0`, but the user knows that the package is compatible with `pydantic>=2.0`, the user can override the declared dependency with `pydantic>=2.0,<3` to allow the resolver to continue.

In PDM, there are two ways to specify overrides:

### In the project file

Added in version 1.12.0

You can specify the overrides in the `pyproject.toml` file, under the `[tool.pdm.resolution.overrides]` table:

```
[tool.pdm.resolution.overrides]
asgiref = "3.2.10"  # exact version
urllib3 = ">=1.26.2"  # version range
pytz = "https://mypypi.org/packages/pytz-2020.9-py3-none-any.whl"  # absolute URL
```

Each entry in the table is a package name and a version specifier. The version specifier can be a version range, an exact version, or an absolute URL.

### Via CLI option

Added in version 2.17.0

PDM also supports reading dependency overrides from a requirements file. The file works similarly to the constraint file in pip(`--constraint constraints.txt`), and the syntax is the same as the requirements file:

```
requests==2.20.0
django==1.11.8
certifi==2018.11.17
chardet==3.0.4
idna==2.7
pytz==2019.3
urllib3==1.23
```

Override files serve as an easy way to store the dependencies in a centralized location that can be shared by multiple projects in your organization.

You can pass the constraint file to various PDM commands that would perform a resolution, such as [`pdm install`](../../reference/cli/#install), [`pdm lock`](../../reference/cli/#lock), [`pdm add`](../../reference/cli/#add), etc.

```
pdm lock --override constraints.txt
```

This option can be supplied multiple times.

Override files can also be served via a URL, e.g. `--override http://example.com/constraints.txt`, so that your organization can store and serve them in a remote server.

## Show what packages are installed

Similar to `pip list`, you can list all packages installed in the packages directory:

```
pdm list
```

### Include and exclude groups

By default, all packages installed in the working set will be listed. You can specify which groups to be listed by `--include/--exclude` options, and `include` has a higher priority than `exclude`.

```
pdm list --include dev
pdm list --exclude test
```

There is a special group `:sub`, when included, all transitive dependencies will also be shown. It is included by default.

You can also pass `--resolve` to `pdm list`, which will show the packages resolved in `pdm.lock`, rather than installed in the working set.

### Change the output fields and format

By default, name, version and location will be shown in the list output, you can view more fields or specify the order of fields by `--fields` option:

```
pdm list --fields name,licenses,version
```

For all supported fields, please refer to the [CLI reference](../../reference/cli/#list_1).

Also, you can specify the output format other than the default table output. The supported formats and options are `--csv`, `--json`, `--markdown` and `--freeze`.

### Show the dependency tree

Or show a dependency tree by:

```
$ pdm list --tree
tempenv 0.0.0
└── click 7.0 [ required: <7.0.0,>=6.7 ]
black 19.10b0
├── appdirs 1.4.3 [ required: Any ]
├── attrs 19.3.0 [ required: >=18.1.0 ]
├── click 7.0 [ required: >=6.5 ]
├── pathspec 0.7.0 [ required: <1,>=0.6 ]
├── regex 2020.2.20 [ required: Any ]
├── toml 0.10.0 [ required: >=0.9.4 ]
└── typed-ast 1.4.1 [ required: >=1.4.0 ]
bump2version 1.0.0
```

Note that `--fields` option doesn't work with `--tree`.

### Filter packages by patterns

You can also limit the packages to show by passing the patterns to `pdm list`:

```
pdm list flask-* requests-*
```

Be careful with the shell expansion

In most shells, the wildcard `*` will be expanded if there are matching files under the current directory. To avoid getting unexpected results, you can wrap the patterns with single quotes: `pdm list 'flask-*' 'requests-*'`.

In `--tree` mode, only the subtree of the matched packages will be displayed. This can be used to achieve the same purpose as `pnpm why`, which is to show why a specific package is required.

```
$ pdm list --tree --reverse certifi
certifi 2023.7.22
└── requests 2.31.0 [ requires: >=2017.4.17 ]
    └── cachecontrol[filecache] 0.13.1 [ requires: >=2.16.0 ]
```

## Manage global project

Sometimes users may want to keep track of the dependencies of global Python interpreter as well. It is easy to do so with PDM, via `-g/--global` option which is supported by most subcommands.

If the option is passed, `<CONFIG_ROOT>/global-project` will be used as the project directory, which is almost the same as normal project except that `pyproject.toml` will be created automatically for you and it doesn't support build features. The idea is taken from Haskell's [stack](https://docs.haskellstack.org).

However, unlike `stack`, by default, PDM won't use global project automatically if a local project is not found. Users should pass `-g/--global` explicitly to activate it, since it is not very pleasing if packages go to a wrong place. But PDM also leave the decision to users, just set the config `global_project.fallback` to `true`.

By default, when `pdm` uses global project implicitly the following message is printed: `Project is not found, fallback to the global project`. To disable this message set the config `global_project.fallback_verbose` to `false`.

If you want global project to track another project file other than `<CONFIG_ROOT>/global-project`, you can provide the project path via `-p/--project <path>` option. Especially if you pass `--global --project .`, PDM will install the dependencies of the current project into the global Python.

Warning

Be careful with `remove` and `sync --clean/--pure` commands when global project is used, because it may remove packages installed in your system Python.

# Lifecycle and Hooks

As any Python deliverable, your project will go through the different phases of a Python project lifecycle and PDM provides commands to perform the expected tasks for those phases.

It also provides hooks attached to these steps allowing for:

- plugins to listen to the signals of the same name.
- developers to define custom scripts with the same name.

Besides, `pre_invoke` signal is emitted before ANY command is invoked, allowing plugins to modify the project or options beforehand.

The built-in commands are currently split into 3 groups:

- the [initialization phase](#initialization)
- the [dependencies management](#dependencies-management).
- the [publication phase](#publication).

You will most probably need to perform some recurrent tasks between the installation and publication phases (housekeeping, linting, testing, ...) this is why PDM lets you define your own tasks/phases using [user scripts](#user-scripts).

To provides full flexibility, PDM allows to [skip some hooks and tasks](#skipping) on demand.

## Initialization

The initialization phase should occur only once in a project lifetime by running the [`pdm init`](../../reference/cli/#init) command to initialize an existing project (prompt to fill the `pyproject.toml` file).

They trigger the following hooks:

- post_init

```
flowchart LR
  subgraph pdm-init [pdm init]
    direction LR
    post-init{{Emit post_init}}
    init --> post-init
  end
```

## Dependencies management

The dependencies management is required for the developer to be able to work and perform the following:

- `lock`: compute a lock file from the `pyproject.toml` requirements.
- `sync`: synchronize (add/remove/update) PEP582 packages from the lock file and install the current project as editable.
- `add`: add a dependency
- `remove`: remove a dependency

All those steps are directly available with the following commands:

- [`pdm lock`](../../reference/cli/#lock): execute the `lock` task
- [`pdm sync`](../../reference/cli/#sync): execute the `sync` task
- [`pdm install`](../../reference/cli/#install): execute the `sync` task, preceded from `lock` if required
- [`pdm add`](../../reference/cli/#add): add a dependency requirement, re-lock and then sync
- [`pdm remove`](../../reference/cli/#remove): remove a dependency requirement, re-lock and then sync
- [`pdm update`](../../reference/cli/#update): re-lock dependencies from their latest versions and then sync

They trigger the following hooks:

- pre_install
- post_install
- pre_lock
- post_lock

```
flowchart LR
  subgraph pdm-install [pdm install]
    direction LR

    subgraph pdm-lock [pdm lock]
      direction TB
      pre-lock{{Emit pre_lock}}
      post-lock{{Emit post_lock}}
      pre-lock --> lock --> post-lock
    end

    subgraph pdm-sync [pdm sync]
      direction TB
      pre-install{{Emit pre_install}}
      post-install{{Emit post_install}}
      pre-install --> sync --> post-install
    end

    pdm-lock --> pdm-sync
  end
```

### Switching Python version

This is a special case in dependency management: you can switch the current Python version using [`pdm use`](../../reference/cli/#use) and it will emit the post_use signal with the new Python interpreter.

```
flowchart LR
  subgraph pdm-use [pdm use]
    direction LR
    post-use{{Emit post_use}}
    use --> post-use
  end
```

## Publication

As soon as you are ready to publish your package/library, you will require the publication tasks:

- `build`: build/compile assets requiring it and package everything into a Python package (sdist, wheel)
- `upload`: upload/publish the package to a remote PyPI index

All those steps are available with the following commands:

- [`pdm build`](../../reference/cli/#build)
- [`pdm publish`](../../reference/cli/#publish)

They trigger the following hooks:

- pre_publish
- post_publish
- pre_build
- post_build

```
flowchart LR
  subgraph pdm-publish [pdm publish]
    direction LR
    pre-publish{{Emit pre_publish}}
    post-publish{{Emit post_publish}}

    subgraph pdm-build [pdm build]
      pre-build{{Emit pre_build}}
      post-build{{Emit post_build}}
      pre-build --> build --> post-build
    end

    %% subgraph pdm-upload [pdm upload]
    %%   pre-upload{{Emit pre_upload}}
    %%   post-upload{{Emit post_upload}}
    %%   pre-upload --> upload --> post-upload
    %% end

    pre-publish --> pdm-build --> upload --> post-publish
  end
```

Execution will stop at first failure, hooks included.

## User scripts

[User scripts are detailed in their own section](../scripts/) but you should know that:

- each user script can define a `pre_*` and `post_*` script, including composite scripts.
- each `run` execution will trigger the pre_run and post_run hooks
- each script execution will trigger the pre_script and post_script hooks

Given the following `scripts` definition:

```
[tool.pdm.scripts]
pre_script = ""
post_script = ""
pre_test = ""
post_test = ""
test = ""
pre_composite = ""
post_composite = ""
composite = {composite = ["test"]}
```

a `pdm run test` will have the following lifecycle:

```
flowchart LR
  subgraph pdm-run-test [pdm run test]
    direction LR
    pre-run{{Emit pre_run}}
    post-run{{Emit post_run}}
    subgraph run-test [test task]
      direction TB
      pre-script{{Emit pre_script}}
      post-script{{Emit post_script}}
      pre-test[Execute pre_test]
      post-test[Execute post_test]
      test[Execute test]

      pre-script --> pre-test --> test --> post-test --> post-script
    end

    pre-run --> run-test --> post-run
  end
```

while `pdm run composite` will have the following:

```
flowchart LR
  subgraph pdm-run-composite [pdm run composite]
    direction LR
    pre-run{{Emit pre_run}}
    post-run{{Emit post_run}}

    subgraph run-composite [composite task]
      direction TB
      pre-script-composite{{Emit pre_script}}
      post-script-composite{{Emit post_script}}
      pre-composite[Execute pre_composite]
      post-composite[Execute post_composite]

      subgraph run-test [test task]
        direction TB
        pre-script-test{{Emit pre_script}}
        post-script-test{{Emit post_script}}
        pre-test[Execute pre_test]
        post-test[Execute post_test]

        pre-script-test --> pre-test --> test --> post-test --> post-script-test
      end

      pre-script-composite --> pre-composite --> run-test --> post-composite --> post-script-composite
    end

     pre-run --> run-composite --> post-run
  end
```

## Skipping

It is possible to control which task and hook runs for any built-in command as well as custom user scripts using the `--skip` option.

It accepts a comma-separated list of hooks/task names to skip as well as the predefined `:all`, `:pre` and `:post` shortcuts respectively skipping all hooks, all `pre_*` hooks and all `post_*` hooks. You can also provide the skip list in `PDM_SKIP_HOOKS` environment variable but it will be overridden as soon as the `--skip` parameter is provided.

Given the previous script block, running `pdm run --skip=:pre,post_test composite` will result in the following reduced lifecycle:

```
flowchart LR
  subgraph pdm-run-composite [pdm run composite]
    direction LR
    post-run{{Emit post_run}}

    subgraph run-composite [composite task]
      direction TB
      post-script-composite{{Emit post_script}}
      post-composite[Execute post_composite]

      subgraph run-test [test task]
        direction TB
        post-script-test{{Emit post_script}}

        test --> post-script-test
      end

      run-test --> post-composite --> post-script-composite
    end

     run-composite --> post-run
  end
```

# Lock for specific platforms or Python versions

Added in version 2.17.0

By default, PDM will try to make a lock file that works on all platforms within the Python versions specified by [`requires-python` in `pyproject.toml`](../project/#specify-requires-python). This is very convenient during development. You can generate a lock file in your development environment and then use this lock file to replicate the same dependency versions in CI/CD or production environments.

However, there are times when this approach may not work. For example, your project or dependency has some platform-specific dependencies, or conditional dependencies depending on the Python version, like the following:

```
[project]
name = "myproject"
requires-python = ">=3.9"
dependencies = [
    "numpy<1.25; python_version < '3.9'",
    "numpy>=1.25; python_version >= '3.9'",
    "pywin32; sys_platform == 'win32'",
]
```

In this case, it's almost impossible to get a single resolution for each package on all platforms and Python versions(`>=3.9`). You should, instead, make lock files for specific platforms or Python versions.

## Specify lock target when generating lock file

PDM supports specifying one or more environment criteria when generating a lock file. These criteria include:

- `--python=<PYTHON_RANGE>`: A [PEP 440](https://www.python.org/dev/peps/pep-0440/) compatible Python version specifier. For example, `--python=">=3.9,<3.10"` will generate a lock file for Python versions `>=3.9` and `<3.10`. For convenience, `--python=3.10` is equivalent to `--python=">=3.10"`, meaning to resolve for Python 3.10 and above.
- `--platform=<PLATFORM>`: A platform specifier. For example, `pdm lock --platform=linux` will generate a lock file for Linux x86_64 platform. Available options are:
  - `linux`
  - `windows`
  - `macos`
  - `alpine`
  - `windows_amd64`
  - `windows_x86`
  - `windows_arm64`
  - `macos_arm64`
  - `macos_x86_64`
  - `macos_X_Y_arm64`
  - `macos_X_Y_x86_64`
  - `manylinux_X_Y_x86_64`
  - `manylinux_X_Y_aarch64`
  - `musllinux_X_Y_x86_64`
  - `musllinux_X_Y_aarch64`
- `--implementation=cpython|pypy|pyston`: A Python implementation specifier. Currently only `cpython`, `pypy`, and `pyston` are supported.

You can ignore some of the criteria, for example, by specifying only `--platform=linux`, the generated lock file will be applicable to Linux platform and all implementations.

`python` criterion and `requires-python`

`--python` option, or `requires-python` criterion in the lock target is still limited by the `requires-python` in `pyproject.toml`. For example, if `requires-python` is `>=3.9` and you specified `--python="<3.11"`, the lock target will be `>=3.9,<3.11`.

## Separate lock files or merge into one

If you need more than one lock targets, you can either create separate lock files for each target or combine them into a single lock file. PDM supports both ways.

To create separate lock file with a specific target:

```
# Generate a lock file for Linux platform and Python 3.9, write the result to py38-linux.lock
pdm lock --platform=linux --python="==3.9.*" --lockfile=py38-linux.lock
```

When you install dependencies on Linux and Python 3.9, you can use this lock file:

```
pdm install --lockfile=py38-linux.lock
```

Additionally, you can also select a subset of dependency groups for the lock file, see [here](../lockfile/#specify-another-lock-file-to-use) for more details.

If you would like to use the same lock file for multiple targets, add `--append` to the `pdm lock` command:

```
# Generate a lock file for Linux platform and Python 3.9, append the result to pdm.lock
pdm lock --platform=linux --python="==3.9.*" --append
```

The advantages of using a single lock file are you don't need to manage multiple lock files when updating dependencies. However, you can't specify different lock strategies for different targets in a single lock file. And the time cost of updating the locks is expected to be higher.

What's more, each lock file can have one or more lock targets, making it rather flexible to use. You can choose to merge some targets in a lock file and lock specific groups and targets in separate lock files. We'll illustrate this with an example in the next section.

## Example

Here is the `pyproject.toml` content:

```
[project]
name = "myproject"
requires-python = ">=3.9"
dependencies = [
    "numpy<1.25; python_version < '3.10'",
    "numpy>=1.25; python_version >= '3.10'",
    "pandas"
]

[project.optional-dependencies]
windows = ["pywin32"]
macos = ["pyobjc"]
```

In the above example, we have conditional dependency versions for `numpy` and platform-specific optional dependencies for Windows and MacOS. We want to generate lock files for Linux, Windows, and MacOS platforms, and Python 3.9 and 3.10.

```
pdm lock --python=">=3.10"
pdm lock --python="<3.10" --append

pdm lock --platform=windows --python=">=3.10" --lockfile=py310-windows.lock --with windows
pdm lock --platform=macos --python=">=3.10" --lockfile=py310-macos.lock --with macos
```

Run the above commands in order, and you will get 3 lockfiles:

- `pdm.lock`: the default main lock file, which works on all platforms and Python versions in `>=3.9`. No platform specific dependencies are included. In this lock file, there are two versions of `numpy`, suitable for Python 3.10 and above and below respectively. The PDM installer will choose the correct version according to the Python version.
- `py39-windows.lock`: lock file for Windows platform and Python 3.10 above, including the optional dependencies for Windows.
- `py39-macos.lock`: lock file for MacOS platform and Python 3.10 above, including the optional dependencies for MacOS.

# Lock file

PDM installs packages exclusively from the existing lock file named `pdm.lock`. This file serves as the sole source of truth for installing dependencies. The lock file contains essential information such as:

- All packages and their versions
- The file names and hashes of the packages
- Optionally, the origin URLs to download the packages (See also: [Static URLs](#static-urls))
- The dependencies and markers of each package (See also: [Inherit the metadata from parents](#inherit-the-metadata-from-parents))

To create or overwrite the lock file, run [`pdm lock`](../../reference/cli/#lock), and it supports the same [update strategies](../dependency/#about-update-strategy) as [`pdm add`](../../reference/cli/#add). In addition, the [`pdm install`](../../reference/cli/#install) and [`pdm add`](../../reference/cli/#add) commands will also automatically create the `pdm.lock` file.

Should I add `pdm.lock` to version control?

It depends. If your goal is to make CI use the same dependency versions as local development and avoid unexpected failures, you should add the `pdm.lock` file to version control. Otherwise, if your project is a library and you want CI to mimic the installation on user site to ensure that the current version on PyPI doesn't break anything, then do not submit the `pdm.lock` file.

## Install the packages pinned in lock file

There are a few similar commands to do this job with slight differences:

- [`pdm sync`](../../reference/cli/#sync) installs packages from the lock file.
- [`pdm update`](../../reference/cli/#update) will update the lock file, then `pdm sync`.
- [`pdm install`](../../reference/cli/#install) will check the project file for changes, update the lock file if needed, then `pdm sync`.

`pdm sync` also has a few options to manage installed packages:

- `--clean`: will remove packages no longer in the lockfile
- `--clean-unselected` (or `--only-keep`): more thorough version of `--clean` that will also remove packages not in the groups specified by the `-G`, `-d`, and `--prod` options. Note: by default, `pdm sync` selects all groups from the lockfile, so `--clean-unselected` is identical to `--clean` unless `-G`, `-d`, and `--prod` are used.

## Hashes in the lock file

By default, `pdm install` will check if the lock file matches the content of `pyproject.toml`, this is done by storing a content hash of `pyproject.toml` in the lock file.

To check if the hash in the lock file is up-to-date:

```
pdm lock --check
```

If you want to refresh the lock file without changing the dependencies, you can use the `--refresh` option:

```
pdm lock --refresh
```

This command also refreshes *all* file hashes recorded in the lock file.

## Change lock file format

PDM supports two lock file formats: `pdm`(default file name is `pdm.lock`) and `pylock`(default file name is `pylock.toml`). The default format is `pdm`.

Added in version 2.25.0

Added experimental support for the [PEP 751](https://packaging.python.org/en/latest/specifications/pylock-toml/#pylock-toml-spec) pylock file format. It's a standard lock file format designed to minimize discrepancies among different Python package managers, enhancing interoperability with other tools. It is set to become the default in a future version of PDM. Read the specification for more details.

You can switch to the `pylock` format with `pdm config` command:

```
pdm config lock.format pylock
```

## Specify another lock file to use

By default, PDM uses `pdm.lock` in the current directory. You can specify another lock file with the `-L/--lockfile` option or the `PDM_LOCKFILE` environment variable:

```
pdm install --lockfile my-lockfile.lock
```

This command installs packages from `my-lockfile.lock` instead of `pdm.lock`.

Alternate lock files are helpful when there exist conflicting dependencies for different environments. In this case, if you lock them as a whole, PDM will raise an error. So you have to [select a subset of dependency groups](../dependency/#select-a-subset-of-dependency-groups-to-install) and lock them separately.

For a realistic example, your project depends on a release version of `werkzeug` and you may want to work with a local in-development copy of it when developing. You can add the following to your `pyproject.toml`:

```
[project]
requires-python = ">=3.7"
dependencies = ["werkzeug"]

[dependency-groups]
dev = ["werkzeug @ file:///${PROJECT_ROOT}/dev/werkzeug"]
```

Then, run `pdm lock` with different options to generate lockfiles for different purposes:

```
# Lock default + dev, write to pdm.lock
# with the local copy of werkzeug pinned.
pdm lock
# Lock default, write to pdm.prod.lock
# with the release version of werkzeug pinned.
pdm lock --prod -L pdm.prod.lock
```

Check the `metadata.groups` field in the lockfile to see which groups are included.

## Option to not write lock file

Sometimes you want to add or update dependencies without updating the lock file, or you don't want to generate `pdm.lock`, you can use the `--frozen-lockfile` option:

```
pdm add --frozen-lockfile flask
```

In this case, the lock file, if existing, will become read-only, no write operation will be performed on it. However, dependency resolution step will still be performed if needed.

## Lock strategies

Currently, we support three flags to control the locking behavior: `cross_platform`, `static_urls` and `direct_minimal_versions`, with the meanings as follows. You can pass one or more flags to `pdm lock` by `--strategy/-S` option, either by giving a comma-separated list or by passing the option multiple times. Both of these commands function in the same way:

```
pdm lock -S cross_platform,static_urls
pdm lock -S cross_platform -S static_urls
```

The flags will be encoded in the lockfile and get read when you run `pdm lock` next time. But you can disable flags by prefixing the flag name with `no_`:

```
pdm lock -S no_cross_platform
```

This command makes the lockfile not cross-platform.

### Cross platform

Added in version 2.6.0

Deprecated in 2.17.0

See [Lock for specific platforms or Python versions](../lock-targets/) for the new behavior.

By default, the generated lockfile is **cross-platform**, which means the current platform isn't taken into account when resolving the dependencies. The result lockfile will contain wheels and dependencies for all possible platforms and Python versions. However, sometimes this will result in a wrong lockfile when a release doesn't contain all wheels. To avoid this, you can tell PDM to create a lockfile that works for **this platform** only, trimming the wheels not relevant to the current platform. This can be done by passing the `--strategy no_cross_platform` option to `pdm lock`:

```
pdm lock --strategy no_cross_platform
```

### Static URLs

Added in version 2.8.0

By default, PDM only stores the filenames of the packages in the lockfile, which benefits the reusability across different package indexes. However, if you want to store the static URLs of the packages in the lockfile, you can pass the `--strategy static_urls` option to `pdm lock`:

```
pdm lock --strategy static_urls
```

The settings will be saved and remembered for the same lockfile. You can also pass `--strategy no_static_urls` to disable it.

### Direct minimal versions

Added in version 2.10.0

When it is enabled by passing `--strategy direct_minimal_versions`, dependencies specified in the `pyproject.toml` will be resolved to the minimal versions available, rather than the latest versions. This is useful when you want to test the compatibility of your project within a range of dependency versions.

For example, if you specified `flask>=2.0` in the `pyproject.toml`, `flask` will be resolved to version `2.0.0` if there is no other compatibility issue.

Note

Version constraints in package dependencies are not future-proof. If you resolve the dependencies to the minimal versions, there will likely be backwards-compatibility issues. For example, `flask==2.0.0` requires `werkzeug>=2.0`, but in fact, it can not work with `Werkzeug 3.0.0`, which is released 2 years after it.

### Inherit the metadata from parents

Added in version 2.11.0

Previously, the `pdm lock` command would record package metadata as it is. When installing, PDM would start from the top requirements and traverse down to the leaf node of the dependency tree. It would then evaluate any marker it encounters against the current environment. If a marker is not satisfied, the package would be discarded. In other words, we need an additional "resolution" step in installation.

When the `inherit_metadata` strategy is enabled, PDM will inherit and merge environment markers from a package's ancestors. These markers are then encoded in the lockfile during locking, resulting in faster installations. This has been enabled by default from version `2.11.0`, to disable this strategy in the config, use `pdm config strategy.inherit_metadata false`.

### Exclude packages newer than specific date

Added in version 2.13.0

You can exclude packages that are newer than a specified date by passing the `--exclude-newer` option to `pdm lock`. This is useful when you want to lock the dependencies to a specific date, for example, to ensure reproducibility of the build.

The date may be specified as a RFC 3339 timestamp (e.g., `2006-12-02T02:07:43Z`) or UTC date in the same format (e.g., `2006-12-02`).

```
pdm lock --exclude-newer 2024-01-01
```

Note

The package index must support the `upload-time` field as specified in [PEP 700](https://peps.python.org/pep-0700/). If the field is not present for a given distribution, the distribution will be treated as unavailable.

## Set acceptable format for locking or installing

If you want to control the format(binary/sdist) of the packages, you can set the env vars `PDM_NO_BINARY`, `PDM_ONLY_BINARY` and `PDM_PREFER_BINARY`.

Each env var is a comma-separated list of package name. You can set it to `:all:` to apply to all packages. For example:

```
# No binary for werkzeug will be locked nor used for installation
PDM_NO_BINARY=werkzeug pdm add flask
# Only binaries will be locked in the lock file
PDM_ONLY_BINARY=:all: pdm lock
# No binaries will be used for installation
PDM_NO_BINARY=:all: pdm install
# Prefer binary distributions and even if sdist with higher version is available
PDM_PREFER_BINARY=flask pdm install
```

You can also defined those values in your project `pyproject.toml` with the `no-binary`, `only-binary` and `prefer-binary` keys of the `tool.pdm.resolution` section. They accept the same format as the environment variables and also support lists.

```
[tool.pdm.resolution]
# No binary for werkzeug and flask will be locked nor used for installation
no-binary = "werkzeug,flask"
# equivalent to
no-binary = ["werkzeug", "flask"]
# Only binaries will be locked in the lock file
only-binary = ":all:"
# Prefer binary distributions and even if sdist with higher version is available
prefer-binary = "flask"
```

Note

Each environment variable takes precedence over its `pyproject.toml` alternative.

## Allow prerelease versions to be installed

Include the following setting in `pyproject.toml` to enable:

```
[tool.pdm.resolution]
allow-prereleases = true
```

## Solve the locking failure

If PDM is not able to find a resolution to satisfy the requirements, it will raise an error. For example,

```
pdm django==3.1.4 "asgiref<3"
...
🔒 Lock failed
Unable to find a resolution for asgiref because of the following conflicts:
    asgiref<3 (from project)
    asgiref<4,>=3.2.10 (from <Candidate django 3.1.4 from https://pypi.org/simple/django/>)
To fix this, you could loosen the dependency version constraints in pyproject.toml. If that is not possible, you could also override the resolved version in `[tool.pdm.resolution.overrides]` table.
```

You can either change to a lower version of `django` or remove the upper bound of `asgiref`. But if it is not eligible for your project, you can try [overriding the resolved package versions](../config/#override-the-resolved-package-versions) or even [don't lock that specific package](../config/#exclude-specific-packages-and-their-dependencies-from-the-lock-file) in `pyproject.toml`.

## Export locked packages to alternative formats

You can export the `pdm.lock` file to other formats, which will simplify the CI flow or image building process. At present, only the `requirements.txt` format is supported.

```
pdm export -o requirements.txt
```

Tip

You can also run `pdm export` with a [`.pre-commit` hook](../advanced/#hooks-for-pre-commit).

Added in version 2.24.0

Additionally, PDM supports exporting to `pylock.toml` format as defined by [PEP 751](https://packaging.python.org/en/latest/specifications/pylock-toml/#pylock-toml-spec). The following command will convert your lock file to a PEP 751 compatible format:

```
pdm export -f pylock -o pylock.toml
```

# Working with PEP 582

PEP 582 has been rejected

This is a rejected PEP. However, due to the fact that this feature is the reason for PDM's birth, PDM will retain the support. We recommend using [virtual environments](../venv/) instead.

With [PEP 582](https://www.python.org/dev/peps/pep-0582/), dependencies will be installed into `__pypackages__` directory under the project root. With [PEP 582 enabled globally](#enable-pep-582-globally), you can also use the project interpreter to run scripts directly.

**When the project interpreter is a normal Python, this mode is enabled.**

Besides, on a project you work with for the first time on your machine, if it contains an empty `__pypackages__` directory, PEP 582 is enabled automatically, and virtualenv won't be created.

## Enable PEP 582 in projects managed my pdm

To make pdm use PEP 582 instead of virtual environment, set `python.use_venv` config variable to False:

```
pdm config python.use_venv False
```

## Enable PEP 582 globally

To make the Python interpreters aware of PEP 582 packages, one needs to add the `pdm/pep582/sitecustomize.py` to the Python library search path.

One just needs to execute `pdm --pep582`, then environment variable will be changed automatically. Don't forget to restart the terminal session to take effect.

The command to change the environment variables can be printed by `pdm --pep582 [<SHELL>]`. If `<SHELL>` isn't given, PDM will pick one based on some guesses. You can run `eval "$(pdm --pep582)"` to execute the command.

You may want to write a line in your `.bash_profile`(or similar profiles) to make it effective when logging in. For example, in bash you can do this:

```
pdm --pep582 >> ~/.bash_profile
```

Once again, Don't forget to restart the terminal session to take effect.

How is it done?

Thanks to the [site packages loading](https://docs.python.org/3/library/site.html) on Python startup. It is possible to patch the `sys.path` by executing the `sitecustomize.py` shipped with PDM. The interpreter can search the directories for the nearest `__pypackage__` folder and append it to the `sys.path` variable.

## Configure IDE to support PEP 582

Now there are no built-in support or plugins for PEP 582 in most IDEs, you have to configure your tools manually.

### PyCharm

Mark `__pypackages__/<major.minor>/lib` as [Sources Root](https://www.jetbrains.com/help/pycharm/configuring-project-structure.html#mark-dir-project-view). Then, select as [Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#interpreter) a Python installation with the same `<major.minor>` version.

Additionally, if you want to use tools from the environment (e.g. `pytest`), you have to add the `__pypackages__/<major.minor>/bin` directory to the `PATH` variable in the corresponding run/debug configuration.

### VSCode

Add the following two entries to the top-level dict in `.vscode/settings.json`:

```
{
  "python.autoComplete.extraPaths": ["__pypackages__/<major.minor>/lib"],
  "python.analysis.extraPaths": ["__pypackages__/<major.minor>/lib"]
}
```

This file can be auto-generated with plugin [`pdm-vscode`](https://github.com/frostming/pdm-vscode).

[Enable PEP582 globally](#enable-pep-582-globally), and make sure VSCode runs using the same user and shell you enabled PEP582 for.

Cannot enable PEP582 globally?

If for some reason you cannot enable PEP582 globally, you can still configure each "launch" in each project: set the `PYTHONPATH` environment variable in your launch configuration, in `.vscode/launch.json`. For example, to debug your `pytest` run:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "pytest",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests"],
            "justMyCode": false,
            "env": {"PYTHONPATH": "__pypackages__/<major.minor>/lib"}
        }
    ]
}
```

If your package resides in a `src` directory, add it to `PYTHONPATH` as well:

```
"env": {"PYTHONPATH": "src:__pypackages__/<major.minor>/lib"}
```

Using Pylance/Pyright?

If you have configured `"python.analysis.diagnosticMode": "workspace"`, and you see a ton of errors/warnings as a result. you may need to create `pyrightconfig.json` in the workspace directory, and fill in the following fields:

```
{
    "exclude": ["__pypackages__"]
}
```

Then restart the language server or VS Code and you're good to go. In the future ([microsoft/pylance-release#1150](https://github.com/microsoft/pylance-release/issues/1150)), maybe the problem will be solved.

Using Jupyter Notebook?

If you wish to use pdm to install jupyter notebook and use it in vscode in conjunction with the python extension:

1. Use `pdm add notebook` or so to install notebook
1. Add a `.env` file inside of your project directory with contents like the following:

```
PYTHONPATH=/your-workspace-path/__pypackages__/<major>.<minor>/lib
```

If the above still doesn't work, it's most likely because the environment variable is not properly loaded when the Notebook starts. There are two workarounds.

1. Run `code .` in Terminal. It will open a new VSCode window in the current directory with the path set correctly. Use the Jupyter Notebook in the new window
1. If you prefer not to open a new window, run the following at the beginning of your Jupyter Notebook to explicitly set the path:

```
import sys
sys.path.append('/your-workspace-path/__pypackages__/<major>.<minor>/lib')
```

> [Reference Issue](https://github.com/pdm-project/pdm/issues/848)

PDM Task Provider

In addition, there is a [VSCode Task Provider extension](https://marketplace.visualstudio.com/items?itemName=knowsuchagency.pdm-task-provider) available for download.

This makes it possible for VSCode to automatically detect [pdm scripts](../scripts/) so they can be run natively as [VSCode Tasks](https://code.visualstudio.com/docs/editor/tasks).

### Neovim

If using [neovim-lsp](https://github.com/neovim/nvim-lspconfig) with [pyright](https://github.com/Microsoft/pyright) and want your `__pypackages__` directory to be added to the path, you can add this to your project's `pyproject.toml`.

```
[tool.pyright]
extraPaths = ["__pypackages__/<major.minor>/lib/"]
```

### Emacs

You have a few options, but basically you'll want to tell an LSP client to add `__pypackages__` to the paths it looks at. Here are a few options that are available:

#### Using `pyproject.toml` and pyright

Add this to your project's `pyproject.toml`:

```
[tool.pyright]
extraPaths = ["__pypackages__/<major.minor>/lib/"]
```

#### eglot + pyright

Using [pyright](https://github.com/microsoft/pyright) and [eglot](https://github.com/joaotavora/eglot) (included in Emacs 29), add the following to your config:

```
(defun get-pdm-packages-path ()
  "For the current PDM project, find the path to the packages."
  (let ((packages-path (string-trim (shell-command-to-string "pdm info --packages"))))
    (concat packages-path "/lib")))

(defun my/eglot-workspace-config (server)
  "For the current PDM project, dynamically generate a python lsp config."
  `(:python\.analysis (:extraPaths ,(vector (get-pdm-packages-path)))))

(setq-default eglot-workspace-configuration #'my/eglot-workspace-config)
```

You'll want pyright installed either globally, or in your project (probably as a dev dependency). You can add this with, for example:

```
pdm add --dev --group devel pyright
```

#### LSP-Mode + lsp-python-ms

Below is a sample code snippet showing how to make PDM work with [lsp-python-ms](https://github.com/emacs-lsp/lsp-python-ms) in Emacs. Contributed by [@linw1995](https://github.com/pdm-project/pdm/discussions/372#discussion-3303501).

```
  ;; TODO: Cache result
  (defun linw1995/pdm-get-python-executable (&optional dir)
    (let ((pdm-get-python-cmd "pdm info --python"))
      (string-trim
       (shell-command-to-string
        (if dir
            (concat "cd "
                    dir
                    " && "
                    pdm-get-python-cmd)
          pdm-get-python-cmd)))))

  (defun linw1995/pdm-get-packages-path (&optional dir)
    (let ((pdm-get-packages-cmd "pdm info --packages"))
      (concat (string-trim
               (shell-command-to-string
                (if dir
                    (concat "cd "
                            dir
                            " && "
                            pdm-get-packages-cmd)
                  pdm-get-packages-cmd)))
              "/lib")))

  (use-package lsp-python-ms
    :ensure t
    :init (setq lsp-python-ms-auto-install-server t)
    :hook (python-mode
           . (lambda ()
               (setq lsp-python-ms-python-executable (linw1995/pdm-get-python-executable))
               (setq lsp-python-ms-extra-paths (vector (linw1995/pdm-get-packages-path)))
               (require 'lsp-python-ms)
               (lsp))))  ; or lsp-deferred
```

# New Project

To start with, create a new project with [`pdm new`](../../reference/cli/#new):

```
pdm new my-project
```

You will need to answer a few questions, to help PDM to create a `pyproject.toml` file for you. For more usages of `pdm new`, please read [Create your project from a template](../template/).

## Create pyproject.toml for an existing project

If you already have a project and want to create a `pyproject.toml` file for it, you can use [`pdm init`](../../reference/cli/#init):

```
cd my-project
pdm init
```

## Choose a Python interpreter

At first, you need to choose a Python interpreter from a list of Python versions installed on your machine. The interpreter path will be stored in `.pdm-python` and used by subsequent commands. You can also change it later with [`pdm use`](../../reference/cli/#use).

Alternatively, you can specify the Python interpreter path via `PDM_PYTHON` environment variable. When it is set, the path saved in `.pdm-python` will be ignored.

Added in version 2.23.0

If `.python-version` is present in the project root or `PDM_PYTHON_VERSION` env var is set, PDM will use the Python version specified in it. The file or env var should contain a valid Python version string, such as `3.11`.

Using an existing environment

If you choose to use an existing environment, such as reusing an environment created by `conda`, please note that PDM will *remove* dependencies not listed in `pyproject.toml` or `pdm.lock` when running `pdm sync --clean` or `pdm remove`. This may lead to destructive consequences. Therefore, try not to share environment among multiple projects.

### Install Python interpreters with PDM

Added in version 2.13.0

PDM supports installing additional Python interpreters from [@indygreg's python-build-standalone](https://github.com/indygreg/python-build-standalone) with the `pdm python install` command. For example, to install CPython 3.9.8:

```
pdm python install 3.9.8
```

You can view all available Python versions with `pdm python install --list`.

This will install the Python interpreter into the location specified by `python.install_root` configuration.

List the currently installed Python interpreters:

```
pdm python list
```

Remove an installed Python interpreter:

```
pdm python remove 3.9.8
```

Install a free-threaded Python interpreter:

```
pdm python install 3.13t
```

Share installations with Rye

PDM installs Python interpreters using the same source as [Rye](https://rye-up.com). If you are using Rye at the same time, you can point the `python.install_root` to the same directory as Rye to share the Python interpreters:

```
pdm config python.install_root ~/.rye/py
```

Afterwards you can manage the installations using either `rye toolchain` or `pdm python`.

### Installation strategy based on `requires-python`

Added in version 2.16.0

If Python `version` is not given, PDM will try to install the best match for the current platform/arch combination based on `requires-python` from `pyproject.toml` (if pyproject.toml or requires-python attribute is not available, all install-able Python interpreters are considered).

Default strategy is `maximum`, i.e. the highest cPython interpreter version will be installed.

If `minimum` is preferred, use the option `--min` and leave `version` empty.

```
pdm python install --min
```

The same principles apply to [`pdm use`](../../reference/cli/#use) (incl. an automatic installation feature) which make it a good unattended set up command for CI/CD or 'fresh start with existing pyproject.toml' use-cases.

### Virtualenv or not

After you select the Python interpreter, PDM will ask you whether you want to create a virtual environment for the project. If you choose **yes**, PDM will create a virtual environment in the project root directory, and use it as the Python interpreter for the project.

If the selected Python interpreter is in a virtual environment, PDM will use it as the project environment and install dependencies into it. Otherwise, `__pypackages__` will be created in the project root and dependencies will be installed into it.

For the difference between these two approaches, please refer to the corresponding sections in the docs:

- [Virtualenv](../venv/)
- [`__pypackages__`(PEP 582)](../pep582/)

## Library or Application

A library and an application differ in many ways. In short, a library is a package that is intended to be installed and used by other projects. In most cases it also needs to be uploaded to PyPI. An application, on the other hand, is one that is directly facing end users and may need to be deployed into some production environments.

In PDM, if you choose to create a library, PDM will add a `name`, `version` field to the `pyproject.toml` file, as well as a `[build-system]` table for the [build backend](../../reference/build/), which is only useful if your project needs to be built and distributed. So you need to manually add these fields to `pyproject.toml` if you want to change the project from an application to a library. Also, a library project will be installed into the environment when you run `pdm install` or `pdm sync`, unless `--no-self` is specified.

In `pyproject.toml`, there is a field `distribution` under the `[tool.pdm]` table. If it is set to true, PDM will treat the project as a library.

## Specify `requires-python`

You need to set an appropriate `requires-python` value for your project. This is an important property that affects how dependencies are resolved. Basically, each package's `requires-python` must *cover* the project's `requires-python` range. For example, consider the following setup:

- Project: `requires-python = ">=3.9"`
- Package `foo`: `requires-python = ">=3.7,<3.11"`

Resolving the dependencies will cause a `ResolutionImpossible`:

```
Unable to find a resolution because the following dependencies don't work
on all Python versions defined by the project's `requires-python`
```

Because the dependency's `requires-python` is `>=3.7,<3.11`, it *doesn't* cover the project's `requires-python` range of `>=3.9`. In other words, the project promises to work on Python 3.9, 3.10, 3.11 (and so on), but the dependency doesn't support Python 3.11 (or any higher). Since PDM creates a cross-platform lockfile that should work on all Python versions within the `requires-python` range, it can't find a valid resolution. To fix this, you need add a maximum version to `requires-python`, like `>=3.9,<3.11`.

The value of `requires-python` is a [version specifier as defined in PEP 440](https://peps.python.org/pep-0440/#version-specifiers). Here are some examples:

| `requires-python`       | Meaning                                  |
| ----------------------- | ---------------------------------------- |
| `>=3.7`                 | Python 3.7 and above                     |
| `>=3.7,<3.11`           | Python 3.7, 3.8, 3.9 and 3.10            |
| `>=3.6,!=3.8.*,!=3.9.*` | Python 3.6 and above, except 3.8 and 3.9 |

## Working with older Python versions

Removed in version 2.21.0

PDM now supports 3.9 and above as the python version of projects.

Although PDM run on Python 3.9 and above, you can still have lower Python versions for your **working project**. But remember, if your project is a library, which needs to be built, published or installed, you make sure the PEP 517 build backend being used supports the lowest Python version you need. For instance, the default backend `pdm-backend` only works on Python 3.7+, so if you run [`pdm build`](../../reference/cli/#build) on a project with Python 3.6, you will get an error. Most modern build backends have dropped the support for Python 3.6 and lower, so it is highly recommended to upgrade the Python version to 3.7+. Here are the supported Python range for some commonly used build backends, we only list those that support PEP 621 since otherwise PDM can't work with them.

| Backend               | Supported Python | Support PEP 621 |
| --------------------- | ---------------- | --------------- |
| `pdm-backend`         | `>=3.7`          | Yes             |
| `setuptools>=60`      | `>=3.7`          | Experimental    |
| `hatchling`           | `>=3.7`          | Yes             |
| `flit-core>=3.4`      | `>=3.6`          | Yes             |
| `flit-core>=3.2,<3.4` | `>=3.4`          | Yes             |

Note that if your project is an application (i.e. without the `name` metadata), the above limitation of backends does not apply. Therefore, if you don't need a build backend you can use any Python version `>=2.7`.

## Import the project from other package managers

If you are already using other package manager tools like Pipenv or Poetry, it is easy to migrate to PDM. PDM provides `import` command so that you don't have to initialize the project manually, it now supports:

1. Pipenv's `Pipfile`
1. Poetry's section in `pyproject.toml`
1. Flit's section in `pyproject.toml`
1. `requirements.txt` format used by pip
1. setuptools `setup.py`(It requires `setuptools` to be installed in the project environment. You can do this by configuring `venv.with_pip` to `true` for venv and `pdm add setuptools` for `__pypackages__`)

Also, when you are executing [`pdm init`](../../reference/cli/#init) or [`pdm install`](../../reference/cli/#install), PDM can auto-detect possible files to import if your PDM project has not been initialized yet.

Info

Converting a `setup.py` will execute the file with the project interpreter. Make sure `setuptools` is installed with the interpreter and the `setup.py` is trusted.

## Working with version control

You **must** commit the `pyproject.toml` file. You **should** commit the `pdm.lock` and `pdm.toml` file. **Do not** commit the `.pdm-python` file.

The `pyproject.toml` file must be committed as it contains the project's build metadata and dependencies needed for PDM. It is also commonly used by other python tools for configuration. Read more about the `pyproject.toml` file at [Pip documentation](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/).

You should be committing the `pdm.lock` file, by doing so you ensure that all installers are using the same versions of dependencies. To learn how to update dependencies see [update existing dependencies](../dependency/#update-existing-dependencies).

`pdm.toml` contains some project-wide configuration and it may be useful to commit it for sharing.

`.pdm-python` stores the **Python path** used by the **current** project and doesn't need to be shared.

## Show the current Python environment

```
$ pdm info
PDM version:
  2.0.0
Python Interpreter:
  /opt/homebrew/opt/python@3.9/bin/python3.9 (3.9)
Project Root:
  /Users/fming/wkspace/github/test-pdm
Project Packages:
  /Users/fming/wkspace/github/test-pdm/__pypackages__/3.9

# Show environment info
$ pdm info --env
{
  "implementation_name": "cpython",
  "implementation_version": "3.9.0",
  "os_name": "nt",
  "platform_machine": "AMD64",
  "platform_release": "10",
  "platform_system": "Windows",
  "platform_version": "10.0.18362",
  "python_full_version": "3.9.0",
  "platform_python_implementation": "CPython",
  "python_version": "3.9",
  "sys_platform": "win32"
}
```

[This command](../../reference/cli/#info) is useful for checking which mode is being used by the project:

- If **Project Packages** is `None`, [virtualenv mode](../venv/) is enabled.
- Otherwise, [PEP 582 mode](../pep582/) is enabled.

Now, you have set up a new PDM project and get a `pyproject.toml` file. Refer to [metadata section](../../reference/pep621/) about how to write `pyproject.toml` properly.

# Build and Publish

If you are developing a library, after adding dependencies to your project, and finishing the coding, it's time to build and publish your package. It is as simple as one command:

```
pdm publish
```

This will automatically build a wheel and a source distribution(sdist), and upload them to the PyPI index.

PyPI requires API tokens to publish packages, you can use `__token__` as the username and API token as the password.

To specify another repository other than PyPI, use the `--repository` option, the parameter can be either the upload URL or the name of the repository stored in the config file.

```
pdm publish --repository testpypi
pdm publish --repository https://test.pypi.org/legacy/
```

## Publish with trusted publishers

You can configure trusted publishers for PyPI so that you don't need to expose the PyPI tokens in the release workflow. To do this, follow [the guide](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) to add a publisher write a action as below:

### GitHub Actions

```
on:
  release:
    types: [published]

jobs:
  pypi-publish:
    name: upload release to PyPI
    runs-on: ubuntu-latest
    permissions:
      # This permission is needed for private repositories.
      contents: read
      # IMPORTANT: this permission is mandatory for trusted publishing
      id-token: write
    steps:
      - uses: actions/checkout@v4

      - uses: pdm-project/setup-pdm@v4

      - name: Publish package distributions to PyPI
        run: pdm publish
```

### GitLab CI

```
image: python:3.12-bookworm
before_script:
  - pip install pdm

publish-package:
  stage: release
  environment: production
  id_tokens:
    PYPI_ID_TOKEN: # for testpypi: TESTPYPI_ID_TOKEN
      aud: "pypi" # testpypi
  script:
    - pdm publish
```

## Build and publish separately

You can also build the package and upload it in two steps, to allow you to inspect the built artifacts before uploading.

```
pdm build
```

There are many options to control the build process, depending on the backend used. Refer to the [build configuration](../../reference/build/) section for more details.

The artifacts will be created at `dist/` and able to upload to PyPI.

```
pdm publish --no-build
```

# PDM Scripts

Like `npm run`, with PDM, you can run arbitrary scripts or commands with local packages loaded.

## Arbitrary Scripts

```
pdm run flask run -p 54321
```

It will run `flask run -p 54321` in the environment that is aware of packages in your project environment.

## Single-file Scripts

Added in version 2.16.0

PDM can run single-file scripts with [inline script metadata](https://peps.python.org/pep-0723/) specified by PEP 723.

The following is an example of a script with embedded metadata:

```
# test_script.py
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

When you run it with `pdm run test_script.py`, PDM will create a temporary environment with the specified dependencies installed and run the script:

```
[
│   ('1', 'PEP Purpose and Guidelines'),
│   ('2', 'Procedure for Adding New Modules'),
│   ('3', 'Guidelines for Handling Bug Reports'),
│   ('4', 'Deprecation of Standard Modules'),
│   ('5', 'Guidelines for Language Evolution'),
│   ('6', 'Bug Fix Releases'),
│   ('7', 'Style Guide for C Code'),
│   ('8', 'Style Guide for Python Code'),
│   ('9', 'Sample Plaintext PEP Template'),
│   ('10', 'Voting Guidelines')
]
```

Add `--reuse-env` option if you want to reuse the environment created last time. You can also add `[tool.pdm]` section to the script metadata to configure PDM. For example:

```
# test_script.py
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
#
# [[tool.pdm.source]]  # Use a custom index
# url = "https://mypypi.org/simple"
# name = "pypi"
# ///
```

Read the [specification](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) for more details.

## User Scripts

PDM also supports custom script shortcuts in the optional `[tool.pdm.scripts]` section of `pyproject.toml`.

Confuse with `[project.scripts]`?

There is another field `[project.scripts]` in `pyproject.toml`, and the scripts can also be invoked with `pdm run`. It's used to define the console script entry points to be installed with the package. Therefore, the executables can only be run after the project itself is installed into the environment. That is to say, you must have `distribution = true`.

In contrast, `[tool.pdm.scripts]` defines some tasks to be run in your project. It works for projects regardless of whether the `distribution` is `true` or `false`. The tasks are primarily for development and testing purposes and support more types and settings, as will be shown later., you can regard it as a replacement for `Makefile`. It doesn't require the project to be installed but requires the existence of a `pyproject.toml` file.

See more explanations about `[project.scripts]` [here](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#creating-executable-scripts).

You can then run `pdm run <script_name>` to invoke the script in the context of your PDM project. For example:

```
[tool.pdm.scripts]
start = "flask run -p 54321"
```

And then in your terminal:

```
$ pdm run start
Flask server started at http://127.0.0.1:54321
```

Any following arguments will be appended to the command:

```
$ pdm run start -h 0.0.0.0
Flask server started at http://0.0.0.0:54321
```

Yarn-like script shortcuts

There is a builtin shortcut making all scripts available as root commands as long as the script does not conflict with any builtin or plugin-contributed command. Said otherwise, if you have a `start` script, you can run both `pdm run start` and `pdm start`. But if you have an `install` script, only `pdm run install` will run it, `pdm install` will still run the builtin `install` command.

PDM supports 4 types of scripts:

### `cmd`

Plain text scripts are regarded as normal command, or you can explicitly specify it:

```
[tool.pdm.scripts]
start = {cmd = "flask run -p 54321"}
```

In some cases, such as when wanting to add comments between parameters, it might be more convenient. to specify the command as an array instead of a string:

```
[tool.pdm.scripts]
start = {cmd = [
    "flask",
    "run",
    # Important comment here about always using port 54321
    "-p", "54321"
]}
```

### `shell`

Shell scripts can be used to run more shell-specific tasks, such as pipeline and output redirecting. This is basically run via `subprocess.Popen()` with `shell=True`:

```
[tool.pdm.scripts]
filter_error = {shell = "cat error.log|grep CRITICAL > critical.log"}
```

### `call`

The script can be also defined as calling a python function in the form `<module_name>:<func_name>`:

```
[tool.pdm.scripts]
foobar = {call = "foo_package.bar_module:main"}
```

The function can be supplied with literal arguments:

```
[tool.pdm.scripts]
foobar = {call = "foo_package.bar_module:main('dev')"}
```

### `composite`

This script kind execute other defined scripts:

```
[tool.pdm.scripts]
lint = "flake8"
test = "pytest"
all = {composite = ["lint", "test"]}
```

Running `pdm run all` will run `lint` first and then `test` if `lint` succeeded.

Added in version 2.13.0

To override the default behavior and continue the execution of the remaining scripts after a failure, set the `keep_going` option to `true`:

```
[tool.pdm.scripts]
lint = "flake8"
test = "pytest"
all.composite = ["lint", "test"]
all.keep_going = true
```

If `keep_going` set to `true` return code of composite script is either '0' if all succeeded or the code of last failed individual script.

You can also provide arguments to the called scripts:

```
[tool.pdm.scripts]
lint = "flake8"
test = "pytest"
all = {composite = ["lint mypackage/", "test -v tests/"]}
```

Note

Argument passed on the command line are given to each called task.

You can also use the `composite` script to combine multiple commands:

```
[tool.pdm.scripts]
mytask.composite = [
    "echo 'Hello'",
    "echo 'World'"
]
```

## Script Options

### `env`

All environment variables set in the current shell can be seen by `pdm run` and will be expanded when executed. Besides, you can also define some fixed environment variables in your `pyproject.toml`:

```
[tool.pdm.scripts]
start.cmd = "flask run -p 54321"
start.env = {FOO = "bar", FLASK_DEBUG = "1"}
```

Note how we use [TOML's syntax](https://github.com/toml-lang/toml) to define a composite dictionary.

About environment variable substitution

Variables in script specifications can be substituted in all script types. In `cmd` scripts, only `${VAR}` syntax is supported on all platforms, however in `shell` scripts, the syntax is platform-dependent. For example, Windows cmd uses `%VAR%` while bash uses `$VAR`.

Note

Environment variables specified on a composite task level will override those defined by called tasks.

### `env_file`

You can also store all environment variables in a dotenv file and let PDM read it:

```
[tool.pdm.scripts]
start.cmd = "flask run -p 54321"
start.env_file = ".env"
```

The variables within the dotenv file will *not* override any existing environment variables. If you want the dotenv file to override existing environment variables use the following:

```
[tool.pdm.scripts]
start.cmd = "flask run -p 54321"
start.env_file.override = ".env"
```

Environment variable loading order

Env vars loaded from different sources are loaded in the following order:

1. OS environment variables
1. Project environments such as `PDM_PROJECT_ROOT`, `PATH`, `VIRTUAL_ENV`, etc
1. Dotenv file specified by `env_file`
1. Env vars mapping specified by `env`

Env vars from the latter sources will override those from the former sources. A dotenv file specified on a composite task level will override those defined by called tasks.

An env var can contain a reference to another env var from the sources loaded before, for example:

```
VAR=42
FOO=hello-${VAR}
```

will result in `FOO=hello-42`. The reference can also contain a default value with the syntax `${VAR:-default}`.

### `working_dir`

Added in version 2.13.0

You can set the current working directory for the script:

```
[tool.pdm.scripts]
start.cmd = "flask run -p 54321"
start.working_dir = "subdir"
```

Relative paths are resolved against the project root.

Added in version 2.20.2

To identify the original calling working directory, each script gets the environment variable `PDM_RUN_CWD` injected.

### `site_packages`

To make sure the running environment is properly isolated from the outer Python interpreter, site-packages from the selected interpreter WON'T be loaded into `sys.path`, unless any of the following conditions holds:

1. The executable is from `PATH` but not inside the `__pypackages__` folder.
1. `-s/--site-packages` flag is following `pdm run`.
1. `site_packages = true` is in either the script table or the global setting key `_`.

Note that site-packages will always be loaded if running with PEP 582 enabled(without the `pdm run` prefix).

### Shared Options

If you want the options to be shared by all tasks run by `pdm run`, you can write them under a special key `_` in `[tool.pdm.scripts]` table:

```
[tool.pdm.scripts]
_.env_file = ".env"
start = "flask run -p 54321"
migrate_db = "flask db upgrade"
```

Besides, inside the tasks, `PDM_PROJECT_ROOT` environment variable will be set to the project root.

### Arguments placeholder

By default, all user provided extra arguments are simply appended to the command (or to all the commands for `composite` tasks).

If you want more control over the user provided extra arguments, you can use the `{args}` placeholder. It is available for all script types and will be interpolated properly for each:

```
[tool.pdm.scripts]
cmd = "echo '--before {args} --after'"
shell = {shell = "echo '--before {args} --after'"}
composite = {composite = ["cmd --something", "shell {args}"]}
```

will produce the following interpolations (those are not real scripts, just here to illustrate the interpolation):

```
$ pdm run cmd --user --provided
--before --user --provided --after
$ pdm run cmd
--before --after
$ pdm run shell --user --provided
--before --user --provided --after
$ pdm run shell
--before --after
$ pdm run composite --user --provided
cmd --something
shell --before --user --provided --after
$ pdm run composite
cmd --something
shell --before --after
```

You may optionally provide default values that will be used if no user arguments are provided:

```
[tool.pdm.scripts]
test = "echo '--before {args:--default --value} --after'"
```

will produce the following:

```
$ pdm run test --user --provided
--before --user --provided --after
$ pdm run test
--before --default --value --after
```

Note

As soon a placeholder is detected, arguments are not appended anymore. This is important for `composite` scripts because if a placeholder is detected on one of the subtasks, none for the subtasks will have the arguments appended, you need to explicitly pass the placeholder to every nested command requiring it.

Note

`call` scripts don't support the `{args}` placeholder as they have access to `sys.argv` directly to handle such complex cases and more.

### `{pdm}` placeholder

Sometimes you may have multiple PDM installations, or `pdm` installed with a different name. This could for example occur in a CI/CD situation, or when working with different PDM versions in different repos. To make your scripts more robust you can use `{pdm}` to use the PDM entrypoint executing the script. This will expand to `{sys.executable} -m pdm`.

```
[tool.pdm.scripts]
whoami = { shell = "echo `{pdm} -V` was called as '{pdm} -V'" }
```

will produce the following output:

```
$ pdm whoami
PDM, version 0.1.dev2501+g73651b7.d20231115 was called as /usr/bin/python3 -m pdm -V

$ pdm2.8 whoami
PDM, version 2.8.0 was called as <snip>/venvs/pdm2-8/bin/python -m pdm -V
```

Note

While the above example uses PDM 2.8, this functionality was introduced in the 2.10 series and only backported for the showcase.

## Show the List of Scripts

Use `pdm run --list/-l` to show the list of available script shortcuts:

```
$ pdm run --list
╭─────────────┬───────┬───────────────────────────╮
│ Name        │ Type  │ Description               │
├─────────────┼───────┼───────────────────────────┤
│ test_cmd    │ cmd   │ flask db upgrade          │
│ test_script │ call  │ call a python function    │
│ test_shell  │ shell │ shell command             │
╰─────────────┴───────┴───────────────────────────╯
```

You can add an `help` option with the description of the script, and it will be displayed in the `Description` column in the above output.

Note

Tasks with a name starting with an underscore (`_`) are considered internal (helpers...) and are not shown in the listing.

## Pre & Post Scripts

Like `npm`, PDM also supports tasks composition by pre and post scripts, pre script will be run before the given task and post script will be run after.

```
[tool.pdm.scripts]
pre_compress = "{{ Run BEFORE the `compress` script }}"
compress = "tar czvf compressed.tar.gz data/"
post_compress = "{{ Run AFTER the `compress` script }}"
```

In this example, `pdm run compress` will run all these 3 scripts sequentially.

The pipeline fails fast

In a pipeline of pre - self - post scripts, a failure will cancel the subsequent execution.

## Hook Scripts

Under certain situations PDM will look for some special hook scripts for execution:

- `post_init`: Run after `pdm init`
- `pre_install`: Run before installing packages
- `post_install`: Run after packages are installed
- `pre_lock`: Run before dependency resolution
- `post_lock`: Run after dependency resolution
- `pre_build`: Run before building distributions
- `post_build`: Run after distributions are built
- `pre_publish`: Run before publishing distributions
- `post_publish`: Run after distributions are published
- `pre_script`: Run before any script
- `post_script`: Run after any script
- `pre_run`: Run once before run script invocation
- `post_run`: Run once after run script invocation

Note

Pre & post scripts can't receive any arguments.

Avoid name conflicts

If there exists an `install` scripts under `[tool.pdm.scripts]` table, `pre_install` scripts can be triggered by both `pdm install` and `pdm run install`. So it is recommended to not use the preserved names.

Note

Composite tasks can also have pre and post scripts. Called tasks will run their own pre and post scripts.

## Skipping scripts

Because, sometimes it is desirable to run a script but without its hooks or pre and post scripts, there is a `--skip=:all` which will disable all hooks, pre and post. There is also `--skip=:pre` and `--skip=:post` allowing to respectively skip all `pre_*` hooks and all `post_*` hooks.

It is also possible to need a pre script but not the post one, or to need all tasks from a composite tasks except one. For those use cases, there is a finer grained `--skip` parameter accepting a list of tasks or hooks name to exclude.

```
pdm run --skip pre_task1,task2 my-composite
```

This command will run the `my-composite` task and skip the `pre_task1` hook as well as the `task2` and its hooks.

You can also provide you skip list in `PDM_SKIP_HOOKS` environment variable but it will be overridden as soon as the `--skip` parameter is provided.

There is more details on hooks and pre/post scripts behavior on [the dedicated hooks page](../hooks/).

# Create Project From a Template

Similar to `yarn create` and `npm create`, PDM also supports initializing or creating a project from a template. The template is given as a positional argument of `pdm new`, in one of the following forms:

- `pdm new django my-project` - Create a new project `my-project` from the template `https://github.com/pdm-project/template-django`
- `pdm new https://github.com/frostming/pdm-template-django my-project` - Initialize the project from a Git URL. Both HTTPS and SSH URL are acceptable.
- `pdm new django@v2 my-project` - To check out the specific branch or tag. Full Git URL also supports it.
- `pdm new /path/to/template my-project` - Initialize the project from a template directory on local filesystem.
- `pdm new minimal my-project` - Initialize with the builtin "minimal" template, that only generates a `pyproject.toml`.

And `pdm new my-project` will use the default template built in and create a project at the given path.

`pdm init` command also supports the same template argument. The project will be initialized at the current directory, existing files with the same name will be overwritten.

## Contribute a template

According to the first form of the template argument, `pdm init <name>` will refer to the template repository located at `https://github.com/pdm-project/template-<name>`. To contribute a template, you can create a template repository and establish a request to transfer the ownership to `pdm-project` organization(it can be found at the bottom of the repository settings page). The administrators of the organization will review the request and complete the subsequent steps. You will be added as the repository maintainer if the transfer is accepted.

## Requirements for a template

A template repository must be a pyproject-based project, which contains a `pyproject.toml` file with PEP-621 compliant metadata. No other special config files are required.

## Project name replacement

On initialization, the project name in the template will be replaced by the name of the new project. This is done by a recursive full-text search and replace. The import name, which is derived from the project name by replacing all non-alphanumeric characters with underscores and lowercasing, will also be replaced in the same way.

For example, if the project name is `foo-project` in the template and you want to initialize a new project named `bar-project`, the following replacements will be made:

- `foo-project` -> `bar-project` in all `.md` files and `.rst` files
- `foo_project` -> `bar_project` in all `.py` files
- `foo_project` -> `bar_project` in the directory name
- `foo_project.py` -> `bar_project.py` in the file name

Therefore, we don't support name replacement if the import name isn't derived from the project name.

## Use other project generators

If you are seeking for a more powerful project generator, you can use [cookiecutter](https://github.com/cookiecutter/cookiecutter) via `--cookiecutter` option and [copier](https://github.com/copier-org/copier) via `--copier` option.

You need to install `cookiecutter` and `copier` respectively to use them. You can do this by running `pdm self add <package>`. To use them:

```
pdm init --cookiecutter gh:cjolowicz/cookiecutter-hypermodern-python
# or
pdm init --copier gh:pawamoy/copier-pdm --UNSAFE
```

# Use uv (Experimental)

Added in version 2.19.0

PDM has experimental support for [uv](https://github.com/astral-sh/uv) as the resolver and installer. To enable it:

```
pdm config use_uv true
```

PDM will automatically detect the `uv` binary on your system. You need to install `uv` first. See [uv's installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more details.

## Reuse the Python installations of uv

uv also supports installing Python interpreters. To avoid overhead, you can configure PDM to reuse the Python installations of uv by:

```
pdm config python.install_root $(uv python dir --color never)
```

## Limitations

Despite the significant performance improvements brought by uv, it is important to note the following limitations:

- The cache files are stored in uv's own cache directory, and you have to use `uv` command to manage them.
- PEP 582 local packages layout is not supported.
- `inherit_metadata` lock strategy is not supported by uv. This will be ignored when writing to the lock file.
- Update strategies other than `all` and `reuse` are not supported.
- Editable requirement must be a local path. Requirements like `-e git+<git_url>` are not supported.
- `excludes` settings under `[tool.pdm.resolution]` are not supported.
- Cross-platform lock targets are not needed by uv resolver, uv always generates universal lock files.
- `include_packages` and `exclude_packages` settings under `[tool.pdm.source]` are not supported.

# Working with Virtual Environments

When you run [`pdm init`](../../reference/cli/#init) command, PDM will [ask for the Python interpreter to use](../project/#choose-a-python-interpreter) in the project, which is the base interpreter to install dependencies and run tasks.

Compared to [PEP 582](https://www.python.org/dev/peps/pep-0582/), virtual environments are considered more mature and have better support in the Python ecosystem as well as IDEs. Therefore, virtualenv is the default mode if not configured otherwise.

Configure pdm to use virtual environment or PEP 582

By default pdm is configured to use virtual environment instead of PEP 582. But this behavior can be changed with `pdm config python.use_venv False` config variable.

**Virtual environments will be used if the project interpreter (the interpreter stored in `.pdm-python`, which can be checked by `pdm info`) is from a virtualenv.**

## Virtualenv auto-creation

By default, PDM prefers to use the virtualenv layout as other package managers do. When you run `pdm install` the first time on a new PDM-managed project, whose Python interpreter is not decided yet, PDM will create a virtualenv in `<project_root>/.venv`, and install dependencies into it. In the interactive session of `pdm init`, PDM will also ask to create a virtualenv for you.

You can choose the backend used by PDM to create a virtualenv. Currently it supports three backends:

- [`virtualenv`](https://virtualenv.pypa.io/)(default)
- `venv`
- `conda`

You can change it by `pdm config venv.backend [virtualenv|venv|conda]`.

Added in version 2.13.0

Moreover, when `python.use_venv` config is set to `true`, PDM will always try to create a virtualenv when using `pdm use` to switch the Python interpreter.

## Create a virtualenv yourself

You can create more than one virtualenvs with whatever Python version you want.

```
# Create a virtualenv based on 3.9 interpreter
pdm venv create 3.9
# Assign a different name other than the version string
pdm venv create --name for-test 3.9
# Use venv as the backend to create, support 3 backends: virtualenv(default), venv, conda
pdm venv create --with venv 3.10
```

## The location of virtualenvs

If no `--name` is given, PDM will create the venv in `<project_root>/.venv`. Otherwise, virtualenvs go to the location specified by the `venv.location` configuration. They are named as `<project_name>-<path_hash>-<name_or_python_version>` to avoid name collision. You can disable the in-project virtualenv creation by `pdm config venv.in_project false`. And all virtualenvs will be created under `venv.location`.

## Reuse the virtualenv you created elsewhere

You can tell PDM to use a virtualenv you created in preceding steps, with [`pdm use`](../../reference/cli/#use):

```
pdm use -f /path/to/venv
```

## Virtualenv auto-detection

When no interpreter is stored in the project config or `PDM_IGNORE_SAVED_PYTHON` env var is set, PDM will try to detect possible virtualenvs to use:

- `venv`, `env`, `.venv` directories in the project root
- The currently activated virtualenv, unless `PDM_IGNORE_ACTIVE_VENV` is set

## List all virtualenvs created with this project

```
$ pdm venv list
Virtualenvs created with this project:

-  3.8.6: C:\Users\Frost Ming\AppData\Local\pdm\pdm\venvs\test-project-8Sgn_62n-3.8.6
-  for-test: C:\Users\Frost Ming\AppData\Local\pdm\pdm\venvs\test-project-8Sgn_62n-for-test
-  3.9.1: C:\Users\Frost Ming\AppData\Local\pdm\pdm\venvs\test-project-8Sgn_62n-3.9.1
```

## Show the path or python interpreter of a virtualenv

```
pdm venv --path for-test
pdm venv --python for-test
```

## Remove a virtualenv

```
$ pdm venv remove for-test
Virtualenvs created with this project:
Will remove: C:\Users\Frost Ming\AppData\Local\pdm\pdm\venvs\test-project-8Sgn_62n-for-test, continue? [y/N]:y
Removed C:\Users\Frost Ming\AppData\Local\pdm\pdm\venvs\test-project-8Sgn_62n-for-test
```

## Activate a virtualenv

Instead of spawning a subshell like what `pipenv` and `poetry` do, `pdm venv` doesn't create the shell for you but print the activate command to the console. In this way you won't leave the current shell. You can then feed the output to `eval` to activate the virtualenv:

```
$ eval $(pdm venv activate for-test)
(test-project-for-test) $  # Virtualenv entered
```

```
eval (pdm venv activate for-test)
```

```
PS1> Invoke-Expression (pdm venv activate for-test)
```

Additionally, if the project interpreter is a venv Python, you can omit the name argument following activate.

Note

`venv activate` **does not** switch the Python interpreter used by the project. It only changes the shell by injecting the virtualenv paths to environment variables. For the aforementioned purpose, use the `pdm use` command.

For more CLI usage, see the [`pdm venv`](../../reference/cli/#venv) documentation.

Looking for `pdm shell`?

PDM doesn't provide a `shell` command because many fancy shell functions may not work perfectly in a subshell, which brings a maintenance burden to support all the corner cases. However, you can still gain the ability via the following ways:

- Use `pdm run $SHELL`, this will spawn a subshell with the environment variables set properly. **The subshell can be quit with `exit` or `Ctrl+D`.**
- Add a shell function to activate the virtualenv, here is an example of BASH function that also works on ZSH:

```
pdm() {
  local command=$1

  if [[ "$command" == "shell" ]]; then
      eval $(pdm venv activate)
  else
      command pdm $@
  fi
}
```

Copy and paste this function to your `~/.bashrc` file and restart your shell.

For `fish` shell you can put the following into your `~/fish/config.fish` or in `~/.config/fish/config.fish`

```
  function pdm
      set cmd $argv[1]

      if test "$cmd" = "shell"
          eval (pdm venv activate)
      else
          command pdm $argv
      end
  end
```

Now you can run `pdm shell` to activate the virtualenv. **The virtualenv can be deactivated with `deactivate` command as usual.**

## Prompt customization

By default when you activate a virtualenv, the prompt will show: `{project_name}-{python_version}`.

For example if your project is named `test-project`:

```
$ eval $(pdm venv activate for-test)
(test-project-3.10) $  # {project_name} == test-project and {python_version} == 3.10
```

The format can be customized before virtualenv creation with the [`venv.prompt`](../../reference/configuration/) configuration or `PDM_VENV_PROMPT` environment variable (before a `pdm init` or `pdm venv create`). Available variables are:

- `project_name`: name of your project
- `python_version`: version of Python (used by the virtualenv)

```
$ PDM_VENV_PROMPT='{project_name}-py{python_version}' pdm venv create --name test-prompt
$ eval $(pdm venv activate test-prompt)
(test-project-py3.10) $
```

## Run a command in a virtual environment without activating it

```
# Run a script
pdm run --venv test test
# Install packages
pdm sync --venv test
# List the packages installed
pdm list --venv test
```

There are other commands supporting `--venv` flag or `PDM_IN_VENV` environment variable, see the [CLI reference](../../reference/cli/). You should create the virtualenv with `pdm venv create --name <name>` before using this feature.

## Switch to a virtualenv as the project environment

By default, if you use `pdm use` and select a non-venv Python, the project will be switched to [PEP 582 mode](../pep582/). We also allow you to switch to a named virtual environment via the `--venv` flag:

```
# Switch to a virtualenv named test
$ pdm use --venv test
# Switch to the in-project venv located at $PROJECT_ROOT/.venv
$ pdm use --venv in-project
```

## Disable virtualenv mode

You can disable the auto-creation and auto-detection for virtualenv by `pdm config python.use_venv false`. **If venv is disabled, PEP 582 mode will always be used even if the selected interpreter is from a virtualenv.**

## Including pip in your virtual environment

By default PDM will not include `pip` in virtual environments. This increases isolation by ensuring that *only your dependencies* are installed in the virtual environment.

To install `pip` once (if for example you want to install arbitrary dependencies in CI) you can run:

```
# Install pip in the virtual environment
pdm run python -m ensurepip
# Install arbitrary dependencies
# These dependencies are not checked for conflicts against lockfile dependencies!
pdm run python -m pip install coverage
```

Or you can create the virtual environment with `--with-pip`:

```
pdm venv create --with-pip 3.9
```

See the [ensurepip docs](https://docs.python.org/3/library/ensurepip.html) for more details on `ensurepip`.

If you want to permanently configure PDM to include `pip` in virtual environments you can use the [`venv.with_pip`](../../reference/configuration/) configuration.

# Reference

# API Reference

## `pdm.core.Core`

A high level object that manages all classes and configurations

### `add_config(name, config_item)`

Add a config item to the configuration class.

Parameters:

| Name          | Type         | Description                 | Default    |
| ------------- | ------------ | --------------------------- | ---------- |
| `name`        | `str`        | The name of the config item | *required* |
| `config_item` | `ConfigItem` | The config item to add      | *required* |

### `create_project(root_path=None, is_global=False, global_config=None)`

Create a new project object

Parameters:

| Name            | Type       | Description                             | Default |
| --------------- | ---------- | --------------------------------------- | ------- |
| `root_path`     | `PathLike` | The path to the project root directory  | `None`  |
| `is_global`     | `bool`     | Whether the project is a global project | `False` |
| `global_config` | `str`      | The path to the global config file      | `None`  |

Returns:

| Type      | Description        |
| --------- | ------------------ |
| `Project` | The project object |

### `get_command(args)`

Get the command name from the arguments

### `handle(project, options)`

Called before command invocation

### `load_plugins()`

Import and load plugins under `pdm.plugin` namespace A plugin is a callable that accepts the core object as the only argument.

Example

```
def my_plugin(core: pdm.core.Core) -> None:
    ...
```

### `main(args=None, prog_name=None, obj=None, **extra)`

The main entry function

### `register_command(command, name=None)`

Register a subcommand to the subparsers, with an optional name of the subcommand.

Parameters:

| Name      | Type                | Description                                                    | Default    |
| --------- | ------------------- | -------------------------------------------------------------- | ---------- |
| `command` | `Type[BaseCommand]` | The command class to register                                  | *required* |
| `name`    | `str`               | The name of the subcommand, if not given, command.name is used | `None`     |

## `pdm.core.Project`

Core project class.

Parameters:

| Name            | Type   | Description                    | Default    |
| --------------- | ------ | ------------------------------ | ---------- |
| `core`          | `Core` | The core instance.             | *required* |
| `root_path`     | \`str  | Path                           | None\`     |
| `is_global`     | `bool` | Whether the project is global. | `False`    |
| `global_config` | \`str  | Path                           | None\`     |

### `config`

A read-only dict configuration

### `default_source`

Get the default source from the pypi setting

### `project_config`

Read-and-writable configuration dict for project settings

### `add_dependencies(requirements, to_group='default', dev=False, show_message=True, write=True)`

Add requirements to the given group, and return the requirements of that group.

### `env_or_setting(var, key)`

Get a value from environment variable and fallback on a given setting.

Returns `None` if both the environment variable and the key does not exists.

### `find_interpreters(python_spec=None, search_venv=None)`

Return an iterable of interpreter paths that matches the given specifier, which can be:

1. a version specifier like 3.7
1. an absolute path
1. a short name like python3
1. None that returns all possible interpreters

### `get_best_matching_cpython_version(use_minimum=False, freethreaded=False)`

Returns the best matching CPython version that fits requires-python, this platform and arch. If no best match could be found, return None.

Default for best match strategy is "highest" possible interpreter version. If "minimum" shall be used, set `use_minimum` to True.

### `get_provider(strategy='all', tracked_names=None, for_install=False, ignore_compatibility=NotSet, direct_minimal_versions=False, env_spec=None, locked_repository=None)`

Build a provider class for resolver.

:param strategy: the resolve strategy :param tracked_names: the names of packages that needs to update :param for_install: if the provider is for install :param ignore_compatibility: if the provider should ignore the compatibility when evaluating candidates :param direct_minimal_versions: if the provider should prefer minimal versions instead of latest :returns: The provider object

### `get_reporter(requirements, tracked_names=None)`

Return the reporter object to construct a resolver.

:param requirements: requirements to resolve :param tracked_names: the names of packages that needs to update :param spinner: optional spinner object :returns: a reporter

### `get_repository(cls=None, ignore_compatibility=NotSet, env_spec=None)`

Get the repository object

### `get_resolver(allow_uv=True)`

Get the resolver class to use for the project.

### `get_setting(key)`

Get a setting from its dotted key (without the `tool.pdm` prefix).

Returns `None` if the key does not exists.

### `get_synchronizer(quiet=False, allow_uv=True)`

Get the synchronizer class to use for the project.

### `iter_interpreters(python_spec=None, search_venv=None, filter_func=None, respect_version_file=True)`

Iterate over all interpreters that matches the given specifier. And optionally install the interpreter if not found.

### `resolve_interpreter()`

Get the Python interpreter path.

### `split_extras_groups(all_groups)`

Split the groups into extras and non-extras.

### `use_pyproject_dependencies(group, dev=False)`

Get the dependencies array and setter in the pyproject.toml Return a tuple of two elements, the first is the dependencies array, and the second value is a callable to set the dependencies array back.

### `write_lockfile(toml_data=None, show_message=True, write=True, **_kwds)`

Write the lock file to disk.

## Signals

Added in version 1.12.0

The signal definition for PDM.

Example

```
from pdm.signals import post_init, post_install

def on_post_init(project):
    project.core.ui.echo("Project initialized")
# Connect to the signal
post_init.connect(on_post_init)
# Or use as a decorator
@post_install.connect
def on_post_install(project, candidates, dry_run):
    project.core.ui.echo("Project install succeeded")
```

### `post_build = pdm_signals.signal('post_build')`

Called after a project is built.

Parameters:

| Name              | Type             | Description                      | Default                                    |
| ----------------- | ---------------- | -------------------------------- | ------------------------------------------ |
| `project`         | `Project`        | The project object               | *required*                                 |
| `artifacts`       | `Sequence[str]`  | The locations of built artifacts | *required*                                 |
| `config_settings` | \`dict[str, str] | None\`                           | Additional config settings passed via args |

### `post_init = pdm_signals.signal('post_init')`

Called after a project is initialized. Args: project (Project): The project object

### `post_install = pdm_signals.signal('post_install')`

Called after a project is installed.

Parameters:

| Name       | Type            | Description                        | Default    |
| ---------- | --------------- | ---------------------------------- | ---------- |
| `project`  | `Project`       | The project object                 | *required* |
| `packages` | `list[Package]` | The packages installed             | *required* |
| `dry_run`  | `bool`          | If true, won't perform any actions | *required* |

### `post_lock = pdm_signals.signal('post_lock')`

Called after a project is locked.

Parameters:

| Name         | Type                         | Description                        | Default    |
| ------------ | ---------------------------- | ---------------------------------- | ---------- |
| `project`    | `Project`                    | The project object                 | *required* |
| `resolution` | `dict[str, list[Candidate]]` | The resolved candidates            | *required* |
| `dry_run`    | `bool`                       | If true, won't perform any actions | *required* |

### `post_publish = pdm_signals.signal('post_publish')`

Called after a project is published.

Parameters:

| Name      | Type      | Description        | Default    |
| --------- | --------- | ------------------ | ---------- |
| `project` | `Project` | The project object | *required* |

### `post_run = pdm_signals.signal('post_run')`

Called after any run.

Parameters:

| Name      | Type            | Description                         | Default    |
| --------- | --------------- | ----------------------------------- | ---------- |
| `project` | `Project`       | The project object                  | *required* |
| `script`  | `str`           | the script name                     | *required* |
| `args`    | `Sequence[str]` | the command line provided arguments | *required* |

### `post_script = pdm_signals.signal('post_script')`

Called after any script.

Parameters:

| Name      | Type            | Description                         | Default    |
| --------- | --------------- | ----------------------------------- | ---------- |
| `project` | `Project`       | The project object                  | *required* |
| `script`  | `str`           | the script name                     | *required* |
| `args`    | `Sequence[str]` | the command line provided arguments | *required* |

### `post_use = pdm_signals.signal('post_use')`

Called after use switched to a new Python version.

Parameters:

| Name      | Type         | Description                                  | Default    |
| --------- | ------------ | -------------------------------------------- | ---------- |
| `project` | `Project`    | The project object                           | *required* |
| `python`  | `PythonInfo` | Information about the new Python interpreter | *required* |

### `pre_build = pdm_signals.signal('pre_build')`

Called before a project is built.

Parameters:

| Name              | Type             | Description              | Default                                    |
| ----------------- | ---------------- | ------------------------ | ------------------------------------------ |
| `project`         | `Project`        | The project object       | *required*                                 |
| `dest`            | `str`            | The destination location | *required*                                 |
| `config_settings` | \`dict[str, str] | None\`                   | Additional config settings passed via args |

### `pre_install = pdm_signals.signal('pre_install')`

Called before a project is installed.

Parameters:

| Name       | Type            | Description                        | Default    |
| ---------- | --------------- | ---------------------------------- | ---------- |
| `project`  | `Project`       | The project object                 | *required* |
| `packages` | `list[Package]` | The packages to install            | *required* |
| `dry_run`  | `bool`          | If true, won't perform any actions | *required* |

### `pre_invoke = pdm_signals.signal('pre_invoke')`

Called before any command is invoked.

Parameters:

| Name      | Type        | Description          | Default          |
| --------- | ----------- | -------------------- | ---------------- |
| `project` | `Project`   | The project object   | *required*       |
| `command` | \`str       | None\`               | the command name |
| `options` | `Namespace` | the parsed arguments | *required*       |

### `pre_lock = pdm_signals.signal('pre_lock')`

Called before a project is locked. Args: project (Project): The project object requirements (list[Requirement]): The requirements to lock dry_run (bool): If true, won't perform any actions

### `pre_publish = pdm_signals.signal('pre_publish')`

Called before a project is published.

Parameters:

| Name      | Type      | Description        | Default    |
| --------- | --------- | ------------------ | ---------- |
| `project` | `Project` | The project object | *required* |

### `pre_run = pdm_signals.signal('pre_run')`

Called before any run.

Parameters:

| Name      | Type            | Description                         | Default    |
| --------- | --------------- | ----------------------------------- | ---------- |
| `project` | `Project`       | The project object                  | *required* |
| `script`  | `str`           | the script name                     | *required* |
| `args`    | `Sequence[str]` | the command line provided arguments | *required* |

### `pre_script = pdm_signals.signal('pre_script')`

Called before any script.

Parameters:

| Name      | Type            | Description                         | Default    |
| --------- | --------------- | ----------------------------------- | ---------- |
| `project` | `Project`       | The project object                  | *required* |
| `script`  | `str`           | the script name                     | *required* |
| `args`    | `Sequence[str]` | the command line provided arguments | *required* |

# Build Configuration

`pdm` uses the [PEP 517](https://www.python.org/dev/peps/pep-0517/) to build the package. It acts as a build frontend that calls the build backend to build the package.

A build backend is what drives the build system to build source distributions and wheels from arbitrary source trees.

If you run [`pdm init`](../cli/#init), PDM will let you choose the build backend to use. Unlike other package managers, PDM does not force you to use a specific build backend. You can choose the one you like. Here is a list of build backends and corresponding configurations initially supported by PDM:

`pyproject.toml` configuration:

```
[build-system]
requires = ["pdm-backend"]
build-backend = "pdm.backend"
```

`pyproject.toml` configuration:

```
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

`pyproject.toml` configuration:

```
[build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"
```

`pyproject.toml` configuration:

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

`pyproject.toml` configuration:

```
[build-system]
requires = ["maturin>=1.4,<2.0"]
build-backend = "maturin"
```

Apart from the above mentioned backends, you can also use any other backend that supports PEP 621, however, [poetry-core](https://python-poetry.org/) is not supported because it does not support reading PEP 621 metadata.

Info

If you are using a custom build backend that is not in the above list, PDM will handle the relative paths as PDM-style(`${PROJECT_ROOT}` variable).

# CLI Reference

## pdm

Options:

- `-h`, `--help`: Show this help message and exit.
- `-V`, `--version`: Show the version and exit
- `-c`, `--config`: Specify another config file path \[env var: `PDM_CONFIG_FILE`\]
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--no-cache`: Disable the cache for the current command. \[env var: `PDM_NO_CACHE`\]
- `-I`, `--ignore-python`: Ignore the Python path saved in`.pdm-python`. \[env var: `PDM_IGNORE_SAVED_PYTHON`\]
- `--pep582` `SHELL`: Print the command line to be eval'd by the shell for PEP 582
- `-n`, `--non-interactive`: Don't show interactive prompts but use defaults. \[env var: `PDM_NON_INTERACTIVE`\]

Commands:

### add

> Add package(s) to pyproject.toml and install them

Update Strategy:

- `--update-reuse`: Reuse pinned versions already present in lock file if possible
- `--update-eager`: Try to update the packages and their dependencies recursively
- `--update-all`: Update all dependencies and sub-dependencies
- `--update-reuse-installed`: Reuse installed packages if possible

Save Strategy:

- `--save-compatible`: Save compatible version specifiers
- `--save-safe-compatible`: Save safe compatible version specifiers
- `--save-wildcard`: Save wildcard version specifiers
- `--save-exact`: Save exact version specifiers
- `--save-minimum`: Save minimum version specifiers

Package Arguments:

- `-e`, `--editable`: Specify editable packages
- `packages`: Specify packages

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `--frozen-lockfile`, `--no-lock`: Don't try to create or update the lockfile. \[env var: `PDM_FROZEN_LOCKFILE`\]
- `--override`: Use the constraint file in pip-requirements format for overriding. \[env var: `PDM_OVERRIDE`\] This option can be used multiple times. See https://pip.pypa.io/en/stable/user_guide/#constraints-files
- `--pre`, `--prerelease`: Allow prereleases to be pinned
- `--stable`: Only allow stable versions to be pinned (default: `True`)
- `-u`, `--unconstrained`: Ignore the version constraints in`pyproject.toml` and overwrite with new ones from the resolution result
- `--dry-run`: Show the difference only and don't perform any action
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `-d`, `--dev`: Add packages into dev dependencies
- `-G`, `--group`: Specify the target dependency group to add into
- `--no-sync`: Only write`pyproject.toml` and do not sync the working set (default: `False`)

Install Options:

- `--no-editable`: Install non-editable versions for all packages. \[env var: `PDM_NO_EDITABLE`\]
- `--no-self`: Don't install the project itself. \[env var: `PDM_NO_SELF`\]
- `--fail-fast`, `-x`: Abort on first installation error
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`

### build

> Build artifacts for distribution

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`
- `--no-sdist`: Don't build source tarballs (default: `False`)
- `--no-wheel`: Don't build wheels (default: `False`)
- `-d`, `--dest`: Target directory to put artifacts (default: `dist`)
- `--no-clean`: Do not clean the target directory (default: `False`)

### cache

> Control the caches of PDM

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

Commands:

#### clear

> Clean all the files under cache directory

Positional Arguments:

- `type`: Clear the given type of caches

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### remove

> Remove files matching the given pattern

Positional Arguments:

- `pattern`: The pattern to remove

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### list

> List the built wheels stored in the cache

Positional Arguments:

- `pattern`: The pattern to list (default: `*`)

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### info

> Show the info and current size of caches

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

### completion

> Generate completion scripts for the given shell

Positional Arguments:

- `shell`: The shell to generate the scripts for. If not given, PDM will properly guess from `SHELL` env var.

Options:

- `-h`, `--help`: Show this help message and exit.

### config

> Display the current configuration

Positional Arguments:

- `key`: Config key
- `value`: Config value

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-l`, `--local`: Set config in the project's local configuration file
- `-d`, `--delete`: Unset a configuration key
- `-e`, `--edit`: Edit the configuration file in the default editor(defined by EDITOR env var)

### export

> Export the locked packages set to other formats

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `-f`, `--format`: Export to requirements.txt format or pylock.toml format (default: `requirements`)
- `--no-hashes`, `--without-hashes`: Don't include artifact hashes (default: `False`)
- `--no-markers`: (DEPRECATED)Don't include platform markers (default: `False`)
- `--no-extras`: Strip extras from the requirements (default: `False`)
- `-o`, `--output`: Write output to the given file, or print to stdout if not given
- `--pyproject`: Read the list of packages from`pyproject.toml`
- `--expandvars`: Expand environment variables in requirements
- `--self`: Include the project itself
- `--editable-self`: Include the project itself as an editable dependency

Dependencies Selection:

- `-G`, `--group`, `--with` `GROUP`: Select group of optional-dependencies separated by comma or dependency-groups (with `-d`). Can be supplied multiple times, use`:all` to include all groups under the same species.
- `--without`: Exclude groups of optional-dependencies or dependency-groups
- `--no-default`: Don't include dependencies from the default group (default: `False`)
- `-d`, `--dev`: Select dev dependencies
- `--prod`, `--production`: Unselect dev dependencies (default: `True`)

### fix

> Fix the project problems according to the latest version of PDM

Positional Arguments:

- `problem`: Fix the specific problem, or all if not given

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--dry-run`: Only show the problems

### import

> Import project metadata from other formats

Positional Arguments:

- `filename`: The file name

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-d`, `--dev`: import packages into dev dependencies
- `-G`, `--group`: Specify the target dependency group to import into
- `-f`, `--format`: Specify the file format explicitly

### info

> Show the project information

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `--python`: Show the interpreter path
- `--where`: Show the project root path
- `--packages`: Show the local packages root
- `--env`: Show PEP 508 environment markers
- `--json`: Dump the information in JSON

### init

> Initialize a pyproject.toml for PDM.

```
Built-in templates:
- default: `pdm init`, A simple template with a basic structure.
- minimal: `pdm init minimal`, A minimal template with only `pyproject.toml`.
```

Positional Arguments:

- `template`: Specify the project template, which can be a local path or a Git URL
- `generator_args`: Arguments passed to the generator

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--copier`: Use Copier to generate project [not installed] (default: `builtin`)
- `--cookiecutter`: Use Cookiecutter to generate project [not installed] (default: `builtin`)
- `-r`, `--overwrite`: Overwrite existing files

Builtin Generator Options:

- `-n`, `--non-interactive`: Don't ask questions but use default values
- `--python`: Specify the Python version/path to use
- `--dist`, `--lib`: Create a package for distribution
- `--backend`: Specify the build backend, which implies --dist
- `--license`: Specify the license (SPDX name)
- `--name`: Specify the project name
- `--project-version`: Specify the project's version
- `--no-git`: Do not initialize a git repository (default: `False`)

### install

> Install dependencies from lock file

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--override`: Use the constraint file in pip-requirements format for overriding. \[env var: `PDM_OVERRIDE`\] This option can be used multiple times. See https://pip.pypa.io/en/stable/user_guide/#constraints-files
- `--dry-run`: Show the difference only and don't perform any action
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `--frozen-lockfile`, `--no-lock`: Don't try to create or update the lockfile. \[env var: `PDM_FROZEN_LOCKFILE`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `--check`: Check if the lock file is up to date and fail otherwise
- `--plugins`: Install the plugins specified in`pyproject.toml`

Install Options:

- `--no-editable`: Install non-editable versions for all packages. \[env var: `PDM_NO_EDITABLE`\]
- `--no-self`: Don't install the project itself. \[env var: `PDM_NO_SELF`\]
- `--fail-fast`, `-x`: Abort on first installation error
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`

Dependencies Selection:

- `-G`, `--group`, `--with` `GROUP`: Select group of optional-dependencies separated by comma or dependency-groups (with `-d`). Can be supplied multiple times, use`:all` to include all groups under the same species.
- `--without`: Exclude groups of optional-dependencies or dependency-groups
- `--no-default`: Don't include dependencies from the default group (default: `False`)
- `-d`, `--dev`: Select dev dependencies
- `--prod`, `--production`: Unselect dev dependencies (default: `True`)

### list

> List packages installed in the current working set

Positional Arguments:

- `patterns`: Filter packages by patterns. e.g. pdm list requests- *flask-*. In --tree mode, only show the subtree of the matched packages.

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `--freeze`: Show the installed dependencies in pip's requirements.txt format
- `--tree`, `--graph`: Display a tree of dependencies
- `-r`, `--reverse`: Reverse the dependency tree
- `--resolve`: Resolve all requirements to output licenses (instead of just showing those currently installed)
- `--fields`: Select information to output as a comma separated string. All fields: groups,homepage,licenses,location,name,version. (default: `name,version,location`)
- `--sort`: Sort the output using a given field name. If nothing is set, no sort is applied. Multiple fields can be combined with ','.
- `--csv`: Output dependencies in CSV document format
- `--json`: Output dependencies in JSON document format
- `--markdown`: Output dependencies and legal notices in markdown document format - best effort basis
- `--include`: Dependency groups to include in the output. By default all are included
- `--exclude`: Exclude dependency groups from the output

### lock

> Resolve and lock dependencies

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`
- `--override`: Use the constraint file in pip-requirements format for overriding. \[env var: `PDM_OVERRIDE`\] This option can be used multiple times. See https://pip.pypa.io/en/stable/user_guide/#constraints-files
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--refresh`: Refresh the content hash and file hashes in the lock file
- `--check`: Check if the lock file is up to date and quit
- `--update-reuse`: Reuse pinned versions already present in lock file if possible (default: `all`)
- `--update-reuse-installed`: Reuse installed packages if possible
- `--exclude-newer`: Exclude packages newer than the given UTC date in format `YYYY-MM-DD[THH:MM:SSZ]`

Lock Target:

- `--python`: The Python range to lock for. E.g. `>=3.9`, `==3.12.*`
- `--platform`: The platform to lock for. E.g. `windows`, `linux`, `macos`, `manylinux_2_17_x86_64`. See docs for available choices: http://pdm-project.org/en/latest/usage/lock-targets/
- `--implementation`: The Python implementation to lock for. E.g. `cpython`, `pypy`, `pyston`
- `--append`: Append the result to the current lock file

Lock Strategy:

- `--strategy`, `-S` `STRATEGY`: Specify lock strategy (cross_platform, static_urls, direct_minimal_versions, inherit_metadata). Add 'no\_' prefix to disable. Can be supplied multiple times or split by comma.
- `--no-cross-platform`: [DEPRECATED] Only lock packages for the current platform
- `--static-urls`: [DEPRECATED] Store static file URLs in the lockfile
- `--no-static-urls`: [DEPRECATED] Do not store static file URLs in the lockfile

Dependencies Selection:

- `-G`, `--group`, `--with` `GROUP`: Select group of optional-dependencies separated by comma or dependency-groups (with `-d`). Can be supplied multiple times, use`:all` to include all groups under the same species.
- `--without`: Exclude groups of optional-dependencies or dependency-groups
- `--no-default`: Don't include dependencies from the default group (default: `False`)
- `-d`, `--dev`: Select dev dependencies
- `--prod`, `--production`: Unselect dev dependencies (default: `True`)

### new

> Create a new Python project at

Positional Arguments:

- `template`: Specify the project template, which can be a local path or a Git URL
- `project_path`: The path to create the new project

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `-r`, `--overwrite`: Overwrite existing files

Builtin Generator Options:

- `-n`, `--non-interactive`: Don't ask questions but use default values
- `--python`: Specify the Python version/path to use
- `--dist`, `--lib`: Create a package for distribution
- `--backend`: Specify the build backend, which implies --dist
- `--license`: Specify the license (SPDX name)
- `--name`: Specify the project name
- `--project-version`: Specify the project's version
- `--no-git`: Do not initialize a git repository (default: `False`)

### outdated

> Check for outdated packages and list the latest versions on indexes.

Positional Arguments:

- `patterns`: The packages to check

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--json`: Output in JSON format (default: `table`)
- `--include-sub`: Include sub-dependencies

### publish

> Build and publish the project to PyPI

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `-r`, `--repository`: The repository name or url to publish the package to \[env var: `PDM_PUBLISH_REPO`\]
- `-u`, `--username`: The username to access the repository \[env var: `PDM_PUBLISH_USERNAME`\]
- `-P`, `--password`: The password to access the repository \[env var: `PDM_PUBLISH_PASSWORD`\]
- `-S`, `--sign`: Upload the package with PGP signature
- `-i`, `--identity`: GPG identity used to sign files.
- `-c`, `--comment`: The comment to include with the distribution file.
- `--no-build`: Don't build the package before publishing (default: `False`)
- `-d`, `--dest`: The directory to upload the package from (default: `dist`)
- `--skip-existing`: Skip uploading files that already exist. This may not work with some repository implementations.
- `--no-very-ssl`: Disable SSL verification
- `--ca-certs`: The path to a PEM-encoded Certificate Authority bundle to use for publish server validation \[env var: `PDM_PUBLISH_CA_CERTS`\]

### python

> Manage installed Python interpreters

Options:

- `-h`, `--help`: Show this help message and exit.

Commands:

#### list

> List all Python interpreters installed with PDM

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### remove

> Remove a Python interpreter installed with PDM

Positional Arguments:

- `version`: The Python version to remove. E.g. cpython@3.10.3

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### install

> Install a Python interpreter with PDM

Positional Arguments:

- `version`: The Python version to install (e.g. cpython@3.10.3). If left empty, highest cPython version that matches this platform/arch is installed. If`pyproject.toml` with requires-python is available, this is considered as well.

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--list`, `-l`: List all available Python versions
- `--min`: Use minimum instead of highest version for installation if `version` is left empty

#### link

> Link an external Python interpreter to PDM

Positional Arguments:

- `interpreter`: The path to the Python interpreter to link

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--name`: The name of the link

#### find

> Search for a Python interpreter

Positional Arguments:

- `request`: The Python version to find. E.g. 3.12, cpython@3.13

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--managed`: Only find interpreters managed by PDM

### py

> Manage installed Python interpreters

Options:

- `-h`, `--help`: Show this help message and exit.

Commands:

#### list

> List all Python interpreters installed with PDM

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### remove

> Remove a Python interpreter installed with PDM

Positional Arguments:

- `version`: The Python version to remove. E.g. cpython@3.10.3

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### install

> Install a Python interpreter with PDM

Positional Arguments:

- `version`: The Python version to install (e.g. cpython@3.10.3). If left empty, highest cPython version that matches this platform/arch is installed. If`pyproject.toml` with requires-python is available, this is considered as well.

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--list`, `-l`: List all available Python versions
- `--min`: Use minimum instead of highest version for installation if `version` is left empty

#### link

> Link an external Python interpreter to PDM

Positional Arguments:

- `interpreter`: The path to the Python interpreter to link

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--name`: The name of the link

#### find

> Search for a Python interpreter

Positional Arguments:

- `request`: The Python version to find. E.g. 3.12, cpython@3.13

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--managed`: Only find interpreters managed by PDM

### remove

> Remove packages from pyproject.toml

Positional Arguments:

- `packages`: Specify the packages to remove

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--dry-run`: Show the difference only and don't perform any action
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `--override`: Use the constraint file in pip-requirements format for overriding. \[env var: `PDM_OVERRIDE`\] This option can be used multiple times. See https://pip.pypa.io/en/stable/user_guide/#constraints-files
- `--frozen-lockfile`, `--no-lock`: Don't try to create or update the lockfile. \[env var: `PDM_FROZEN_LOCKFILE`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `-d`, `--dev`: Remove packages from dev dependencies
- `-G`, `--group`: Specify the target dependency group to remove from
- `--no-sync`: Only write`pyproject.toml` and do not uninstall packages (default: `False`)

Install Options:

- `--no-editable`: Install non-editable versions for all packages. \[env var: `PDM_NO_EDITABLE`\]
- `--no-self`: Don't install the project itself. \[env var: `PDM_NO_SELF`\]
- `--fail-fast`, `-x`: Abort on first installation error
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`

### run

> Run commands or scripts with local packages loaded

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `-l`, `--list`: Show all available scripts defined in`pyproject.toml`
- `-j`, `--json`: Output all scripts infos in JSON

Execution Parameters:

- `-s`, `--site-packages`: Load site-packages from the selected interpreter
- `--recreate`: Recreate the script environment for self-contained scripts
- `script`: The command to run
- `args`: Arguments that will be passed to the command

### search

> [DEPRECATED] Search for PyPI packages

Positional Arguments:

- `query`: Query string to search

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

### self

> Manage the PDM program itself (previously known as plugin)

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

Commands:

#### list

> List all packages installed with PDM

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--plugins`: List plugins only

#### add

> Install packages to the PDM's environment

Positional Arguments:

- `packages`: Specify one or many package names, each package can have a version specifier

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--pip-args`: Arguments that will be passed to pip install

#### remove

> Remove packages from PDM's environment

Positional Arguments:

- `packages`: Specify one or many package names

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--pip-args`: Arguments that will be passed to pip uninstall
- `-y`, `--yes`: Answer yes on the question

#### update

> Update PDM itself

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--head`: Update to the latest commit on the main branch
- `--pre`: Update to the latest prerelease version
- `--no-frozen-deps`: Do not install frozen dependency versions (default: `False`)
- `--pip-args`: Additional arguments that will be passed to pip install

### plugin

> Manage the PDM program itself (previously known as plugin)

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

Commands:

#### list

> List all packages installed with PDM

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--plugins`: List plugins only

#### add

> Install packages to the PDM's environment

Positional Arguments:

- `packages`: Specify one or many package names, each package can have a version specifier

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--pip-args`: Arguments that will be passed to pip install

#### remove

> Remove packages from PDM's environment

Positional Arguments:

- `packages`: Specify one or many package names

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--pip-args`: Arguments that will be passed to pip uninstall
- `-y`, `--yes`: Answer yes on the question

#### update

> Update PDM itself

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `--head`: Update to the latest commit on the main branch
- `--pre`: Update to the latest prerelease version
- `--no-frozen-deps`: Do not install frozen dependency versions (default: `False`)
- `--pip-args`: Additional arguments that will be passed to pip install

### show

> Show the package information

Positional Arguments:

- `package`: Specify the package name, or show this package if not given

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `--name`: Show name
- `--version`: Show version
- `--summary`: Show summary
- `--license`: Show license
- `--platform`: Show platform
- `--keywords`: Show keywords

### sync

> Synchronize the current working set with lock file

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--dry-run`: Show the difference only and don't perform any action
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--clean`: Clean packages not in the lockfile
- `--only-keep`, `--clean-unselected`: Only keep the selected packages
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `-r`, `--reinstall`: Force reinstall existing dependencies

Install Options:

- `--no-editable`: Install non-editable versions for all packages. \[env var: `PDM_NO_EDITABLE`\]
- `--no-self`: Don't install the project itself. \[env var: `PDM_NO_SELF`\]
- `--fail-fast`, `-x`: Abort on first installation error
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`

Dependencies Selection:

- `-G`, `--group`, `--with` `GROUP`: Select group of optional-dependencies separated by comma or dependency-groups (with `-d`). Can be supplied multiple times, use`:all` to include all groups under the same species.
- `--without`: Exclude groups of optional-dependencies or dependency-groups
- `--no-default`: Don't include dependencies from the default group (default: `False`)
- `-d`, `--dev`: Select dev dependencies
- `--prod`, `--production`: Unselect dev dependencies (default: `True`)

### update

> Update package(s) in pyproject.toml

Update Strategy:

- `--update-reuse`: Reuse pinned versions already present in lock file if possible
- `--update-eager`: Try to update the packages and their dependencies recursively
- `--update-all`: Update all dependencies and sub-dependencies
- `--update-reuse-installed`: Reuse installed packages if possible

Save Strategy:

- `--save-compatible`: Save compatible version specifiers
- `--save-safe-compatible`: Save safe compatible version specifiers
- `--save-wildcard`: Save wildcard version specifiers
- `--save-exact`: Save exact version specifiers
- `--save-minimum`: Save minimum version specifiers

Positional Arguments:

- `packages`: If packages are given, only update them

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-L`, `--lockfile`: Specify another lockfile path. Default:`pdm.lock`. \[env var: `PDM_LOCKFILE`\]
- `--frozen-lockfile`, `--no-lock`: Don't try to create or update the lockfile. \[env var: `PDM_FROZEN_LOCKFILE`\]
- `--override`: Use the constraint file in pip-requirements format for overriding. \[env var: `PDM_OVERRIDE`\] This option can be used multiple times. See https://pip.pypa.io/en/stable/user_guide/#constraints-files
- `--pre`, `--prerelease`: Allow prereleases to be pinned
- `--stable`: Only allow stable versions to be pinned (default: `True`)
- `-u`, `--unconstrained`: Ignore the version constraints in`pyproject.toml` and overwrite with new ones from the resolution result
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `--venv` `NAME`: Run the command in the virtual environment with the given key. \[env var: `PDM_IN_VENV`\]
- `-t`, `--top`: Only update those listed in`pyproject.toml`
- `--dry-run`, `--outdated`: Show the difference only without modifying the lockfile content
- `--no-sync`: Only update lock file but do not sync packages (default: `False`)

Install Options:

- `--no-editable`: Install non-editable versions for all packages. \[env var: `PDM_NO_EDITABLE`\]
- `--no-self`: Don't install the project itself. \[env var: `PDM_NO_SELF`\]
- `--fail-fast`, `-x`: Abort on first installation error
- `--no-isolation`: Disable isolation when building a source distribution that follows PEP 517, as in: build dependencies specified by PEP 518 must be already installed if this option is used.
- `--config-setting`, `-C`: Pass options to the builder. Options with a value must be specified after "=": `--config-setting=key(=value)` or `-Ckey(=value)`

Dependencies Selection:

- `-G`, `--group`, `--with` `GROUP`: Select group of optional-dependencies separated by comma or dependency-groups (with `-d`). Can be supplied multiple times, use`:all` to include all groups under the same species.
- `--without`: Exclude groups of optional-dependencies or dependency-groups
- `--no-default`: Don't include dependencies from the default group (default: `False`)
- `-d`, `--dev`: Select dev dependencies
- `--prod`, `--production`: Unselect dev dependencies

### use

> Use the given python version or path as base interpreter. If not found, PDM will try to install one.

Positional Arguments:

- `python`: Specify the Python version or path

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-g`, `--global`: Use the global project, supply the project root with `-p` option
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `-k`, `--skip`: Skip some tasks and/or hooks by their comma-separated names. Can be supplied multiple times. Use`:all` to skip all hooks. Use`:pre` and`:post` to skip all pre or post hooks.
- `-f`, `--first`: Select the first matched interpreter - no auto install
- `--auto-install-min`: If `python` argument not given, auto install minimal best match - otherwise has no effect
- `--auto-install-max`: If `python` argument not given, auto install maximum best match - otherwise has no effect
- `-i`, `--ignore-remembered`: Ignore the remembered selection
- `--no-version-file`: Do not write .python-version file (default: `False`)
- `--venv`: Use the interpreter in the virtual environment with the given name

### venv

> Virtualenv management

Options:

- `-h`, `--help`: Show this help message and exit.
- `-p`, `--project`: Specify another path as the project root, which changes the base of`pyproject.toml` and `__pypackages__` \[env var: `PDM_PROJECT`\]
- `--path`: Show the path to the given virtualenv
- `--python`: Show the python interpreter path for the given virtualenv

Commands:

#### create

> Create a virtualenv

Positional Arguments:

- `python`: Specify which python should be used to create the virtualenv
- `venv_args`: Additional arguments that will be passed to the backend

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-w`, `--with`: Specify the backend to create the virtualenv
- `-f`, `--force`: Recreate if the virtualenv already exists
- `-n`, `--name`: Specify the name of the virtualenv
- `--with-pip`: Install pip with the virtualenv

#### list

> List all virtualenvs associated with this project

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### remove

> Remove the virtualenv with the given name

Positional Arguments:

- `env`: The key of the virtualenv

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-y`, `--yes`: Answer yes on the following question

#### activate

> Print the command to activate the virtualenv with the given name

Positional Arguments:

- `env`: The key of the virtualenv

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output

#### purge

> Purge selected/all created Virtualenvs

Options:

- `-h`, `--help`: Show this help message and exit.
- `-v`, `--verbose`: Use `-v` for detailed output and `-vv` for more detailed
- `-q`, `--quiet`: Suppress output
- `-f`, `--force`: Force purging without prompting for confirmation
- `-i`, `--interactive`: Interactively purge selected Virtualenvs

# Configurations

## Color Theme

The default theme used by PDM is as follows:

| Key       | Default Style |
| --------- | ------------- |
| `primary` | cyan          |
| `success` | green         |
| `warning` | yellow        |
| `error`   | red           |
| `info`    | blue          |
| `req`     | bold green    |

You can change the theme colors with [`pdm config`](../cli/#config) command. For example, to change the `primary` color to `magenta`:

```
pdm config theme.primary magenta
```

Or use a hex color code:

```
pdm config theme.success '#51c7bd'
```

## Available Configurations

The following configuration items can be retrieved and modified by [`pdm config`](../cli/#config) command.

Environment Variable Overrides

If the corresponding env var is set, the value will take precedence over what is saved in the config file.

| Config Item                       | Description                                                                                                                                                | Default Value                                                         | Available in Project | Env var                   |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------- | ------------------------- |
| `cache_dir`                       | The root directory of cached files                                                                                                                         | `/home/docs/.cache/pdm`                                               | No                   | `PDM_CACHE_DIR`           |
| `log_dir`                         | The root directory of log files                                                                                                                            | `/home/docs/.local/state/pdm/log`                                     | No                   | `PDM_LOG_DIR`             |
| `check_update`                    | Check if there is any newer version available                                                                                                              | `True`                                                                | No                   | `PDM_CHECK_UPDATE`        |
| `build_isolation`                 | Isolate build environment from the project environment                                                                                                     | `True`                                                                | Yes                  | `PDM_BUILD_ISOLATION`     |
| `request_timeout`                 | The timeout for network requests in seconds                                                                                                                | `15`                                                                  | No                   | `PDM_REQUEST_TIMEOUT`     |
| `use_uv`                          | Use uv for faster resolution and installation                                                                                                              | `False`                                                               | Yes                  | `PDM_USE_UV`              |
| `lock.format`                     | The format of the lock file, can be `pdm` or `pylock`                                                                                                      | `pdm`                                                                 | Yes                  | `PDM_LOCK_FORMAT`         |
| `global_project.fallback`         | Use the global project implicitly if no local project is found                                                                                             | `False`                                                               | No                   |                           |
| `global_project.fallback_verbose` | If True show message when global project is used implicitly                                                                                                | `True`                                                                | No                   |                           |
| `global_project.path`             | The path to the global project                                                                                                                             | `/home/docs/.config/pdm/global-project`                               | No                   |                           |
| `global_project.user_site`        | Whether to install to user site                                                                                                                            | `False`                                                               | No                   |                           |
| `strategy.update`                 | The default strategy for updating packages                                                                                                                 | `reuse`                                                               | Yes                  |                           |
| `strategy.save`                   | Specify how to save versions when a package is added                                                                                                       | `minimum`                                                             | Yes                  |                           |
| `strategy.resolve_max_rounds`     | Specify the max rounds of resolution process                                                                                                               | `10000`                                                               | Yes                  | `PDM_RESOLVE_MAX_ROUNDS`  |
| `strategy.inherit_metadata`       | Inherit the groups and markers from parents for each package                                                                                               | `True`                                                                | Yes                  |                           |
| `install.parallel`                | Whether to perform installation and uninstallation in parallel                                                                                             | `True`                                                                | Yes                  | `PDM_INSTALL_PARALLEL`    |
| `install.cache`                   | Cache wheel installation and only put symlinks in the library root                                                                                         | `False`                                                               | Yes                  |                           |
| `install.cache_method`            | Specify how to create links to the caches(`symlink/hardlink`)                                                                                              | `symlink`                                                             | Yes                  |                           |
| `python.providers`                | List of python provider names for findpython                                                                                                               | `[]`                                                                  | Yes                  |                           |
| `python.use_pyenv`                | Use the pyenv interpreter                                                                                                                                  | `True`                                                                | Yes                  |                           |
| `python.use_venv`                 | Use virtual environments when available                                                                                                                    | `True`                                                                | Yes                  | `PDM_USE_VENV`            |
| `python.use_python_version`       | Use .python-version file next to pyproject.toml to find python interpreters                                                                                | `True`                                                                | Yes                  | `PDM_USE_PYTHON_VERSION`  |
| `python.install_root`             | The root directory to install python interpreters                                                                                                          | `/home/docs/.local/share/pdm/python`                                  | No                   |                           |
| `pypi.url`                        | The URL of PyPI mirror, defaults to https://pypi.org/simple                                                                                                | `https://pypi.org/simple`                                             | Yes                  | `PDM_PYPI_URL`            |
| `pypi.verify_ssl`                 | Verify SSL certificate when query PyPI                                                                                                                     | `True`                                                                | Yes                  | `PDM_PYPI_VERIFY_SSL`     |
| `pypi.username`                   | The username to access PyPI                                                                                                                                |                                                                       | Yes                  | `PDM_PYPI_USERNAME`       |
| `pypi.password`                   | The password to access PyPI                                                                                                                                |                                                                       | Yes                  | `PDM_PYPI_PASSWORD`       |
| `pypi.ca_certs`                   | Path to a CA certificate bundle used for verifying the identity of the PyPI server                                                                         |                                                                       | No                   |                           |
| `pypi.ignore_stored_index`        | Don't add the indexes from the config that is not listed in project                                                                                        | `False`                                                               | Yes                  | `PDM_IGNORE_STORED_INDEX` |
| `pypi.client_cert`                | Path to client certificate file, or combined cert/key file                                                                                                 |                                                                       | No                   |                           |
| `pypi.client_key`                 | Path to client cert keyfile, if not in pypi.client_cert                                                                                                    |                                                                       | No                   |                           |
| `pypi.json_api`                   | Consult PyPI's JSON API for package metadata                                                                                                               | `False`                                                               | Yes                  | `PDM_PYPI_JSON_API`       |
| `scripts.show_header`             | Display script name and help before running                                                                                                                | `False`                                                               | Yes                  | `PDM_SCRIPTS_SHOW_HEADER` |
| `venv.location`                   | Parent directory for virtualenvs                                                                                                                           | `/home/docs/.local/share/pdm/venvs`                                   | No                   |                           |
| `venv.backend`                    | Default backend to create virtualenv                                                                                                                       | `virtualenv`                                                          | Yes                  | `PDM_VENV_BACKEND`        |
| `venv.in_project`                 | Create virtualenv in `.venv` under project root                                                                                                            | `True`                                                                | Yes                  | `PDM_VENV_IN_PROJECT`     |
| `venv.prompt`                     | Define a custom template to be displayed in the prompt when virtualenv isactive. Variables `project_name` and `python_version` are available forformatting | `{project_name}-{python_version}`                                     | Yes                  | `PDM_VENV_PROMPT`         |
| `venv.with_pip`                   | Install pip when creating a new venv                                                                                                                       | `False`                                                               | Yes                  | `PDM_VENV_WITH_PIP`       |
| `theme.primary`                   | Theme color for primary                                                                                                                                    | `cyan`                                                                | No                   |                           |
| `theme.success`                   | Theme color for success                                                                                                                                    | `green`                                                               | No                   |                           |
| `theme.warning`                   | Theme color for warning                                                                                                                                    | `yellow`                                                              | No                   |                           |
| `theme.error`                     | Theme color for error                                                                                                                                      | `red`                                                                 | No                   |                           |
| `theme.info`                      | Theme color for info                                                                                                                                       | `blue`                                                                | No                   |                           |
| `theme.req`                       | Theme color for req                                                                                                                                        | `bold green`                                                          | No                   |                           |
| `pypi.<name>.url`                 | The URL of custom package source                                                                                                                           | `https://pypi.org/simple`                                             | Yes                  |                           |
| `pypi.<name>.username`            | The username to access custom source                                                                                                                       |                                                                       | Yes                  |                           |
| `pypi.<name>.password`            | The password to access custom source                                                                                                                       |                                                                       | Yes                  |                           |
| `pypi.<name>.type`                | `index` or `find_links`                                                                                                                                    | `index`                                                               | Yes                  |                           |
| `pypi.<name>.verify_ssl`          | Verify SSL certificate when query custom source                                                                                                            | `True`                                                                | Yes                  |                           |
| `repository.<name>.url`           | The URL of custom package source                                                                                                                           | `https://pypi.org/simple`                                             | Yes                  |                           |
| `repository.<name>.username`      | The username to access custom repository                                                                                                                   |                                                                       | Yes                  |                           |
| `repository.<name>.password`      | The password to access custom repository                                                                                                                   |                                                                       | Yes                  |                           |
| `repository.<name>.ca_certs`      | Path to a PEM-encoded CA cert bundle (used for server cert verification)                                                                                   | The CA certificates from [certifi](https://pypi.org/project/certifi/) | Yes                  |                           |
| `repository.<name>.verify_ssl`    | Verify SSL certificate when uploading to repository                                                                                                        | `True`                                                                | Yes                  |                           |

# PEP 621 Metadata

The project metadata are stored in the `pyproject.toml`. The specifications are defined by [PEP 621](https://www.python.org/dev/peps/pep-0621/), [PEP 631](https://www.python.org/dev/peps/pep-0631/) and [PEP 639](https://www.python.org/dev/peps/pep-0639/). Read the detailed specifications in the PEPs.

*In the following part of this document, metadata should be written under `[project]` table if not given explicitly.*

## Multiline description

You can split a long description onto multiple lines, thanks to TOML support for multiline strings. Just remember to escape new lines, so the final description appears [on one line only in your package metadata](https://packaging.python.org/specifications/core-metadata/#summary). Indentation will be removed as well when escaping new lines:

```
description = """\
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
    Ut enim ad minim veniam, quis nostrud exercitation ullamco \
    laboris nisi ut aliquip ex ea commodo consequat.\
"""
```

See [TOML's specification on strings](https://toml.io/en/v1.0.0#string).

## Package version

```
[project]
version = "1.0.0"
```

```
[project]
...
dynamic = ["version"]

[tool.pdm]
version = { source = "file", path = "mypackage/__version__.py" }
```

The version will be read from the `mypackage/__version__.py` file searching for the pattern: `__version__ = "{version}"`.

Read more information about other configurations in [dynamic project version](https://backend.pdm-project.org/metadata/#dynamic-project-version) from the `pdm-backend` documentation.

## Python version

The required version of Python is specified as the string `requires-python`:

```
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    ...
]
```

Note: As per [PEP 621](https://peps.python.org/pep-0621/#allow-tools-to-add-extend-data), PDM is not permitted to dynamically update the `classifiers` section like some other non-compliant tools. Thus, you should also include the appropriate [trove classifiers](https://pypi.org/classifiers/) as shown above if you plan on publishing your package on [PyPI](https://pypi.org/).

## License

The license is specified as the string `license`:

```
license = {text = "BSD-2-Clause"}
classifiers = [
    "License :: OSI Approved :: BSD License",
    ...
]
```

Note: As per [PEP 621](https://peps.python.org/pep-0621/#allow-tools-to-add-extend-data), PDM is not permitted to dynamically update the `classifiers` section like some other non-compliant tools. Thus, you should also include the appropriate [trove classifiers](https://pypi.org/classifiers/) as shown above if you plan on publishing your package on [PyPI](https://pypi.org/).

## Dependency specification

The `project.dependencies` is an array of dependency specification strings following the [PEP 440](https://www.python.org/dev/peps/pep-0440/) and [PEP 508](https://www.python.org/dev/peps/pep-0508/).

Examples:

```
[project]
...
dependencies = [
    # Named requirement
    "requests",
    # Named requirement with version specifier
    "flask >= 1.1.0",
    # Requirement with environment marker
    "pywin32; sys_platform == 'win32'",
    # URL requirement
    "pip @ git+https://github.com/pypa/pip.git@20.3.1"
]
```

## Optional dependencies

You can have some requirements optional, which is similar to `setuptools`' `extras_require` parameter.

```
[project.optional-dependencies]
socks = [ 'PySocks >= 1.5.6, != 1.5.7, < 2' ]
tests = [
  'ddt >= 1.2.2, < 2',
  'pytest < 6',
  'mock >= 1.0.1, < 4; python_version < "3.4"',
]
```

To install a group of optional dependencies:

```
pdm install -G socks
```

`-G` option can be given multiple times to include more than one group.

## Context variables expansion

Depending on which build backend you are using, PDM will expand some variables in the dependency strings.

### Environment variables

```
[project]
dependencies = ["flask @ https://${USERNAME}:${PASSWORD}/artifacts.io/Flask-1.1.2.tar.gz"]
```

```
[project]
dependencies = ["flask @ https://{env:USERNAME}:{env:PASSWORD}/artifacts.io/Flask-1.1.2.tar.gz"]
```

Find more usages [here](https://hatch.pypa.io/dev/config/context/#environment-variables)

Don't worry about credential leakage, the environment variables will be expanded when needed and kept untouched in the lock file.

### Relative paths

When you add a package from a relative path, PDM will automatically save it as a relative path for `pdm-backend` and `hatchling`.

For example, if you run `pdm add ./my-package`, it will result in the following line in `pyproject.toml`.

```
[project]
dependencies = ["my-package @ file:///${PROJECT_ROOT}/my-package"]
```

```
[project]
dependencies = ["my-package @ {root:uri}/my-package"]
```

By default, hatchling doesn't support [direct references](https://hatch.pypa.io/dev/config/dependency/#direct-references) in the dependency string, you need to turn it on in `pyproject.toml`:

```
[tool.hatch.metadata]
allow-direct-references = true
```

The relative path will be expanded based on the project root when installing or locking.

## Console scripts

The following content:

```
[project.scripts]
mycli = "mycli.__main__:main"
```

will be translated to `setuptools` style:

```
entry_points = {
    'console_scripts': [
        'mycli=mycli.__main__:main'
    ]
}
```

Also, `[project.gui-scripts]` will be translated to `gui_scripts` entry points group in `setuptools` style.

## Entry points

Other types of entry points are given by `[project.entry-points.<type>]` section, with the same format of `[project.scripts]`:

```
[project.entry-points.pytest11]
myplugin = "mypackage.plugin:pytest_plugin"
```

If the entry point name contains dots or other special characters, wrap it in quotes:

```
[project.entry-points."flake8.extension"]
myplugin = "mypackage.plugin:flake8_plugin"
```

# Development

# Benchmark

This page has been removed, please visit [Python Package Manager Shootout by Lincoln Loop](https://lincolnloop.github.io/python-package-manager-shootout/) for a detailed benchmark report.

# Changelog

Attention

Major and minor releases also include changes listed within prior beta releases.

## Release v2.26.6 (2026-01-22)

### Bug Fixes

- Support `packaging==26.0` changes for version comparison ([#3729](https://github.com/pdm-project/pdm/issues/3729))

## Release v2.26.5 (2026-01-21)

### Bug Fixes

- Respect the project path when using cookiecutter template in `pdm init` command. ([#3721](https://github.com/pdm-project/pdm/issues/3721))
- Fix a bug that `resolution.excludes` is not applied when evaluating candidates from the lock file. ([#3726](https://github.com/pdm-project/pdm/issues/3726))

### Documentation

- Remove chatbot from the docs page footer. ([#3722](https://github.com/pdm-project/pdm/issues/3722))
- Generate llms.txt for docs powered by `mkdocs-llmstxt`. ([#3723](https://github.com/pdm-project/pdm/issues/3723))

## Release v2.26.4 (2026-01-09)

### Bug Fixes

- Make sure cursor closing for fixing PyPy different gc mode also add PyPy in CI. ([#3708](https://github.com/pdm-project/pdm/issues/3708))
- Fix a bug that old HTTP cache directories cause PDM to crash when trying to clear them. ([#3715](https://github.com/pdm-project/pdm/issues/3715))

## Release v2.26.3 (2025-12-24)

### Features & Improvements

- Port to `hishel` 1.0.0. ([#3700](https://github.com/pdm-project/pdm/issues/3700))

### Bug Fixes

- Update `.gitignore` file in the default template. ([#3686](https://github.com/pdm-project/pdm/issues/3686))
- Correct the sysconfig variables for Python standalone build installations. ([#3693](https://github.com/pdm-project/pdm/issues/3693))
- Ignore `packages.vcs.requested-revision` if it's None when formatting pylock.toml. ([#3694](https://github.com/pdm-project/pdm/issues/3694))
- Fix test failures with uv test cases using non-venv Python interpreters. ([#3698](https://github.com/pdm-project/pdm/issues/3698))

## Release v2.26.2 (2025-11-24)

### Features & Improvements

- Only parse TOML document with `tomlkit` when writing is required. ([#3672](https://github.com/pdm-project/pdm/issues/3672))
- Add SHA256 checksums for binary releases during the release workflow and create an installer script that downloads binaries from GitHub releases with automatic platform detection and checksum verification. ([#3679](https://github.com/pdm-project/pdm/issues/3679))

### Bug Fixes

- Fix test_use_python_write_file_multiple_versions to match PDM's actual behavior. ([#3660](https://github.com/pdm-project/pdm/issues/3660))
- Correctly calculate the venv path for `UV_PROJECT_ENVIRONMENT` env var when using uv mode. ([#3675](https://github.com/pdm-project/pdm/issues/3675))
- Ensure `implementation.gil_disabled` is a boolean in `get_current_env_spec`. This fix an issue that free-threaded wheels get rejected incorrectly. ([#3677](https://github.com/pdm-project/pdm/issues/3677))
- Fix CLI help formatting on Python 3.14+. ([#3683](https://github.com/pdm-project/pdm/issues/3683))
- Make `PdmBasicAuth` a `cached_property` to accelerate execution. ([#3684](https://github.com/pdm-project/pdm/issues/3684))

### Removals and Deprecations

- Add deprecation warning for `pdm search` command as PyPI no longer supports search API. ([#3674](https://github.com/pdm-project/pdm/issues/3674))

### Miscellany

- Add tests to utils.fs_supports_link_method and utils.convert_to_datetime. ([#3541](https://github.com/pdm-project/pdm/issues/3541))

## Release v2.26.1 (2025-10-29)

### Bug Fixes

- Substitute missing env vars with empty string in `expand_env_vars`. ([#3653](https://github.com/pdm-project/pdm/issues/3653))
- Constrained hishel to be less than 1.0.0 due to its refactor ([#3657](https://github.com/pdm-project/pdm/issues/3657))

## Release v2.26.0 (2025-10-11)

### Features & Improvements

- Limit the log file size to 100MB and truncate the log output if exceeded. ([#3633](https://github.com/pdm-project/pdm/issues/3633))
- Speed up dependency resolution in the bad path by skipping candidates of the same version when resolving. ([#3647](https://github.com/pdm-project/pdm/issues/3647))

### Bug Fixes

- Reload project files after running hook scripts. ([#3615](https://github.com/pdm-project/pdm/issues/3615))
- Fix a bug when using UV as the resolver does not respect the venv.location configuration. ([#3616](https://github.com/pdm-project/pdm/issues/3616))
- Fix `publish --skip-existing` for Nexus Repository OSS >= 3.70 ([#3617](https://github.com/pdm-project/pdm/issues/3617))
- Fix a resolution failure when both prerelease and non-prerelease requirements exist. ([#3634](https://github.com/pdm-project/pdm/issues/3634))
- Ignore invalid `python` requirement during locking. ([#3635](https://github.com/pdm-project/pdm/issues/3635))
- Isolate PDM loggers with the root logger to avoid log leakage. ([#3637](https://github.com/pdm-project/pdm/issues/3637))
- Fix a crash when resolving URL dependencies under `use_uv=true`. ([#3640](https://github.com/pdm-project/pdm/issues/3640))

## Release v2.25.9 (2025-08-22)

No significant changes.

## Release v2.25.8 (2025-08-22)

### Bug Fixes

- Fix a careless error by fast apply in AI coding. ([#3612](https://github.com/pdm-project/pdm/issues/3612))

## Release v2.25.7 (2025-08-22)

### Features & Improvements

- Show the path to site-packages in the output of `pdm info`. ([#3600](https://github.com/pdm-project/pdm/issues/3600))

### Bug Fixes

- Fix `uv python dir` path resolution on Windows ([#3603](https://github.com/pdm-project/pdm/issues/3603))
- Strip local version in version specifiers when writing package locks. ([#3605](https://github.com/pdm-project/pdm/issues/3605))
- Show an error message when 'default' is used in optional dependencies or dependency groups. ([#3609](https://github.com/pdm-project/pdm/issues/3609))
- Prevent hash clearing when appending to lockfile with env_spec. ([#3610](https://github.com/pdm-project/pdm/issues/3610))

## Release v2.25.6 (2025-08-14)

### Features & Improvements

- The `pdm python install -v` command now shows the download URL for the Python interpreter. ([#3552](https://github.com/pdm-project/pdm/issues/3552))

### Bug Fixes

- Ensure `make_array` always returns a tomlkit array type. ([#3586](https://github.com/pdm-project/pdm/issues/3586))
- Preserve multi-line help text in the CLI help output. ([#3587](https://github.com/pdm-project/pdm/issues/3587))
- Re-caculate artifact files and hashes when the lock target changes. ([#3595](https://github.com/pdm-project/pdm/issues/3595))

### Dependencies

- Require packaging>22.0 and remove conditional PACKAGING_22 version checks. ([#3601](https://github.com/pdm-project/pdm/issues/3601))
- Bump truststore to version 0.10.4. ([#3602](https://github.com/pdm-project/pdm/issues/3602))

## Release v2.25.5 (2025-07-30)

### Features & Improvements

- Tell the difference between free-threaded Python and normal ones. Users need to request for free-threaded versions explicitly by adding `t` to the version string, otherwise the normal build will be preferred. ([#3562](https://github.com/pdm-project/pdm/issues/3562))

### Bug Fixes

- Fix a bug that editable local package URLs are empty when using `pylock.toml`. ([#3565](https://github.com/pdm-project/pdm/issues/3565))
- Fix a bug where `pdm export` with `--lockfile pylock.toml` produced empty requirements.txt files due to missing group information extraction from pylock format markers. ([#3573](https://github.com/pdm-project/pdm/issues/3573))
- Read metadata from installed distribution when using reuse-installed strategy. ([#3579](https://github.com/pdm-project/pdm/issues/3579))
- Fix a lockfile writing error when locking git dependencies in the pylock.toml format. ([#3582](https://github.com/pdm-project/pdm/issues/3582))

## Release v2.25.4 (2025-06-30)

### Bug Fixes

- Add credentials when passing source urls to uv resolver. ([#3553](https://github.com/pdm-project/pdm/issues/3553))
- Redact credentials in source urls in the log output, and inject credentials into the source url for uv sync command as well. ([#3555](https://github.com/pdm-project/pdm/issues/3555))
- Fix a bug that extra dependencies of transitive dependencies are not properly installed when USE_UV=true ([#3558](https://github.com/pdm-project/pdm/issues/3558))
- Improve the terminal output when setting up a script environment. ([#3560](https://github.com/pdm-project/pdm/issues/3560))
- Skip non-existent library paths in post-install steps when trying to fix the pth files. ([#3561](https://github.com/pdm-project/pdm/issues/3561))

### Dependencies

- Update `resolvelib` to 1.2.0. ([#3557](https://github.com/pdm-project/pdm/issues/3557))

## Release v2.25.3 (2025-06-22)

### Bug Fixes

- Fix a bug that local file package metadata was missing when reading the lockfile. ([#3545](https://github.com/pdm-project/pdm/issues/3545))
- Extract `dependency-groups` and `extras` markers from `marker` value when parsing pylock.toml. ([#3550](https://github.com/pdm-project/pdm/issues/3550))

## Release v2.25.2 (2025-06-16)

No significant changes.

## Release v2.25.1 (2025-06-14)

### Bug Fixes

- Fix duplicated dependencies added to the lock file when the same dependency with extras is requested. ([#3542](https://github.com/pdm-project/pdm/issues/3542))
- Stabilize order of the `extras` and `dependency-groups` fields in pylock output. ([#3543](https://github.com/pdm-project/pdm/issues/3543))

## Release v2.25.0 (2025-06-13)

### Features & Improvements

- Support pylock as alternative lock format and make it opt-in by config. ([#3481](https://github.com/pdm-project/pdm/issues/3481))
- Search for package metadata in lock file first when reuse strategy is used. ([#3522](https://github.com/pdm-project/pdm/issues/3522))

### Bug Fixes

- Fix Windows 11 install pdm error, which is because of msgpack install failure. ([#3485](https://github.com/pdm-project/pdm/issues/3485))
- Change the return type of `array_of_inline_tables` to list[dict] from list[str] ([#3523](https://github.com/pdm-project/pdm/issues/3523))
- Ensure uv resolver to include hash for package files. ([#3531](https://github.com/pdm-project/pdm/issues/3531))
- Avoid infinite recursion when reading pyproject.toml with circular file dependencies. ([#3539](https://github.com/pdm-project/pdm/issues/3539))

## Release v2.24.2 (2025-05-23)

### Bug Fixes

- Reinstalling local wheel if its checksum changes. ([#3503](https://github.com/pdm-project/pdm/issues/3503))
- Ignore HTTP cache entries if deserialization fails. ([#3515](https://github.com/pdm-project/pdm/issues/3515))
- Fetch missing URLs when `static_urls` is not enabled when running `pdm export -f pylock`. ([#3517](https://github.com/pdm-project/pdm/issues/3517))
- Missing self package when `--self` or `--editable-self` is passed to `pdm export -f pylock`. ([#3518](https://github.com/pdm-project/pdm/issues/3518))

### Miscellany

- Add Python 3.14 to the test matrix. ([#3506](https://github.com/pdm-project/pdm/issues/3506))

## Release v2.24.1 (2025-04-23)

### Bug Fixes

- Install the project when using the `BaseSynchronizer` with `install_self` set to `True`. This fixes the bug that when calling `pdm sync --quiet`, it skips installing the project itself. ([#3484](https://github.com/pdm-project/pdm/issues/3484))
- Mark one additional test as requiring network, and fix another one not to require it anymore. ([#3487](https://github.com/pdm-project/pdm/issues/3487))

## Release v2.24.0 (2025-04-18)

### Features & Improvements

- New command `pdm new` that behaves like `pdm init` but creates a new project. ([#3462](https://github.com/pdm-project/pdm/issues/3462))
- Support use `--name` as project name for command `pdm new` e.g. `pdm new hello --name world` ([#3476](https://github.com/pdm-project/pdm/issues/3476))
- Support exporting to pylock.toml format as described by PEP 751. ([#3480](https://github.com/pdm-project/pdm/issues/3480))

### Bug Fixes

- Pass the `--quiet` option to `pdm sync` command. ([#3401](https://github.com/pdm-project/pdm/issues/3401))
- If a `.python-version` file is found and it contains multiple lines, the file will be ignored. The usage of the `.python-version` file can be disabled, if configuration value `python.use_python_version` (or environment variable `PDM_USE_PYTHON_VERSION`) is `False`. ([#3417](https://github.com/pdm-project/pdm/issues/3417))
- fix `pdm config -e` command to open read-only file under linux ([#3423](https://github.com/pdm-project/pdm/issues/3423))
- Replace project names and import names in both `README.md` and `pyproject.toml` when running `pdm init <template>`. ([#3460](https://github.com/pdm-project/pdm/issues/3460))
- Fix a bug that URL dependency hashes are not updated if running `pdm lock --update-reuse`. ([#3461](https://github.com/pdm-project/pdm/issues/3461))

## Release v2.23.1 (2025-04-09)

### Features & Improvements

- Use `pyapp` to wrap `pdm` as a Python application that bootstrap itself at runtime. ([#3429](https://github.com/pdm-project/pdm/issues/3429))
- Support all providers `id` is supporting currently for OIDC trusted publishing ([#3441](https://github.com/pdm-project/pdm/issues/3441))

### Bug Fixes

- Installation error for local plugins specified with file URL without a name. ([#3407](https://github.com/pdm-project/pdm/issues/3407))
- Eliminate the warning about inherit_metadata when using uv mode. ([#3434](https://github.com/pdm-project/pdm/issues/3434))
- Fix an installation failure when installing editable local dependencies on Windows and Python 3.13. ([#3444](https://github.com/pdm-project/pdm/issues/3444))
- Fix a bug that overridden requirements in lock file get rewritten when adding a new requirement. ([#3446](https://github.com/pdm-project/pdm/issues/3446))
- Cyclic group inclusion is detected incorrectly. Also show the cyclic group names in the error message. ([#3447](https://github.com/pdm-project/pdm/issues/3447))
- Fix a bug that `pdm remove` doesn't handle dependency groups include correctly. ([#3452](https://github.com/pdm-project/pdm/issues/3452))
- Update `unearth` to address an issue downloading git repos with short commit hash. ([#3455](https://github.com/pdm-project/pdm/issues/3455))

## Release v2.23.0 (2025-04-01)

### Features & Improvements

- Add `pdm python find` command to search for a python interpreter. ([#3389](https://github.com/pdm-project/pdm/issues/3389))
- `pdm import` now converts `package-mode` from Poetry's settings table to `distribution`. ([#3427](https://github.com/pdm-project/pdm/issues/3427))

### Bug Fixes

- Excluding non-existing groups for `pdm remove`. ([#3404](https://github.com/pdm-project/pdm/issues/3404))
- Fix a bug that `pdm add` and `pdm update` remove dependency groups incorrectly. ([#3418](https://github.com/pdm-project/pdm/issues/3418))
- Fix a bug that using resolution overrides drops extra dependencies. ([#3426](https://github.com/pdm-project/pdm/issues/3426))

## Release v2.22.4 (2025-03-07)

### Bug Fixes

- Ensure dev-dependencies are added to the correct group when the `tool.pdm.dev-dependencies` table has groups. ([#3392](https://github.com/pdm-project/pdm/issues/3392))

## Release v2.22.3 (2025-01-27)

### Bug Fixes

- Don't validate local file requirements that are not used. ([#3376](https://github.com/pdm-project/pdm/issues/3376))
- Don't set "dependencies" as empty list for uv toml if there is no dependencies in the raw toml file. ([#3378](https://github.com/pdm-project/pdm/issues/3378))
- Add a dummy project name to the script environment pyproject.toml. ([#3382](https://github.com/pdm-project/pdm/issues/3382))

## Release v2.22.2 (2025-01-11)

### Features & Improvements

- Write installer metadata like `INSTALLER` and `REQUESTED` to dist-info directory when installing packages. ([#3359](https://github.com/pdm-project/pdm/issues/3359))
- Respect `.python-version` file in the project root directory when selecting the Python interpreter. By default, it will be written when running `pdm use` command. ([#3367](https://github.com/pdm-project/pdm/issues/3367))

### Bug Fixes

- Fix a problem of missing dependencies when adding to dev dependencies if both editable and non-editable dependencies exist. ([#3361](https://github.com/pdm-project/pdm/issues/3361))
- Use stdlib for URL \<-> Path conversions. ([#3362](https://github.com/pdm-project/pdm/issues/3362))
- `shellingham.detect_shell()` returns `('tcsh', '/bin/tcsh')` for tcsh on FreeBSD, so the current code tries to use the Bash venv activation script and fails due to syntax error. This change fixes the issue. ([#3366](https://github.com/pdm-project/pdm/issues/3366))
- Fix a performance issue because pypi source credentials were being queried many times from keyring. ([#3368](https://github.com/pdm-project/pdm/issues/3368))

## Release v2.22.1 (2024-12-19)

### Bug Fixes

- Fix zsh hanging issue by removing PyPI package completion. ([#3329](https://github.com/pdm-project/pdm/issues/3329))
- Write dev dependencies to `dependency-groups` section when importing project from other package managers. ([#3354](https://github.com/pdm-project/pdm/issues/3354))

### Miscellany

- Show a warning when resolving against cross-platform targets under uv mode. ([#3341](https://github.com/pdm-project/pdm/issues/3341))

## Release v2.22.0 (2024-12-09)

### Features & Improvements

- Use minimal template if the project is an application. ([#3295](https://github.com/pdm-project/pdm/issues/3295))
- Add one `safe_compatible` version specifiers saving strategy. ([#3301](https://github.com/pdm-project/pdm/issues/3301))
- Allow customizing scripts display with `scripts.show_header` settings. ([#3313](https://github.com/pdm-project/pdm/issues/3313))
- Speed up the resolution by only resolving wheel candidates if possible. ([#3319](https://github.com/pdm-project/pdm/issues/3319))
- Drop version from the search result, following the change of warehouse. ([#3328](https://github.com/pdm-project/pdm/issues/3328))
- Support `overrides` settings under `[tool.pdm.resolution]` with use_uv ([#3330](https://github.com/pdm-project/pdm/issues/3330))

### Bug Fixes

- No longer requires `wheel` to build a setuptools-backed package. ([#3320](https://github.com/pdm-project/pdm/issues/3320))
- Fix an inconsistent behavior when running `pdm remove <package>` with uv enabled. ([#3323](https://github.com/pdm-project/pdm/issues/3323))
- Fix: uninstallation error when pdm is not installed before. ([#3325](https://github.com/pdm-project/pdm/issues/3325))
- Fix a bug in uv mode that direct URL dependencies can't be installed. ([#3332](https://github.com/pdm-project/pdm/issues/3332))
- Fix a crash issue when rewriting dependency groups with `include-group` items. ([#3333](https://github.com/pdm-project/pdm/issues/3333))
- Also read username from keyring if missing in source/repository config. ([#3334](https://github.com/pdm-project/pdm/issues/3334))
- Allow configuring repositories in project. ([#3335](https://github.com/pdm-project/pdm/issues/3335))

### Miscellany

- Mark tests that require uv and skip them if uv is not found. ([#3324](https://github.com/pdm-project/pdm/issues/3324))

## Release v2.21.0 (2024-11-25)

### Features & Improvements

- Pass original working directory as env variable to pdm scripts ([#3179](https://github.com/pdm-project/pdm/issues/3179))
- Output similar commands or script command when the input command is not correct ([#3270](https://github.com/pdm-project/pdm/issues/3270))
- improve readability of Python interpreter validation message ([#3276](https://github.com/pdm-project/pdm/issues/3276))
- Print task name by default when using `pdm run` ([#3277](https://github.com/pdm-project/pdm/issues/3277))
- Make `OrderedSet.__contains__` run in O(1) ([#3280](https://github.com/pdm-project/pdm/issues/3280))
- Emit `post_lock` after writing pyproject.toml and pdm.lock in add/update ([#3285](https://github.com/pdm-project/pdm/issues/3285))
- Drop support of Python 3.8 ([#3298](https://github.com/pdm-project/pdm/issues/3298))

### Bug Fixes

- Fix the name normalization issue for optional dependency groups. ([#3271](https://github.com/pdm-project/pdm/issues/3271))
- Don't use uv when installing plugins in project. ([#3283](https://github.com/pdm-project/pdm/issues/3283))
- Fix the bug that pdm plugins are invalid after installation on ubuntu system python. ([#3289](https://github.com/pdm-project/pdm/issues/3289))

## Release v2.20.1 (2024-11-09)

### Features & Improvements

- Add a fixer to remove the deprecated `cross_platform` strategy from lock file. ([#3259](https://github.com/pdm-project/pdm/issues/3259))

### Bug Fixes

- Fix the bug that `pdm build` would fail when `use_uv` is true. ([#3231](https://github.com/pdm-project/pdm/issues/3231))
- Fix group name normalization when comparing groups. ([#3247](https://github.com/pdm-project/pdm/issues/3247))
- Inherit file descriptors instead of closing when running child processes in `pdm run`. ([#3252](https://github.com/pdm-project/pdm/issues/3252))
- Fix using `no_proxy` when `all_proxy` is set. ([#3254](https://github.com/pdm-project/pdm/issues/3254))
- Preserve multiline arrays and don't add empty tool.pdm table header when updating the pyproject.toml. ([#3258](https://github.com/pdm-project/pdm/issues/3258))
- Fix compatibility of `ErrorArgumentParser` for Python 3.12 and above. ([#3264](https://github.com/pdm-project/pdm/issues/3264))

## Release v2.20.0 (2024-10-31)

### Features & Improvements

- Support dependency groups as standardized by [PEP 735](https://peps.python.org/pep-0735/). By default, dev dependencies will be written to `[dependency-groups]` table. ([#3230](https://github.com/pdm-project/pdm/issues/3230))

### Bug Fixes

- Fix a bug that `strategy.inherit_metadata` config is not honored when using `--lockfile` option. ([#3232](https://github.com/pdm-project/pdm/issues/3232))
- Always perform install-time resolution when `use_uv` is on. ([#3233](https://github.com/pdm-project/pdm/issues/3233))

### Miscellany

- Update `resolvelib` to 1.1.0. ([#3235](https://github.com/pdm-project/pdm/issues/3235))

## Release v2.19.3 (2024-10-19)

### Features & Improvements

- Allow linking existing Python interpreters to PDM's managed location. ([#3215](https://github.com/pdm-project/pdm/issues/3215))

### Bug Fixes

- Fix a bug that overrides provided by environment variables do not work. ([#3182](https://github.com/pdm-project/pdm/issues/3182))
- Allow prereleases when the requirement is pinned even if disabled by project ([#3202](https://github.com/pdm-project/pdm/issues/3202))
- Pass the python path to the uv venv command. ([#3204](https://github.com/pdm-project/pdm/issues/3204))
- Fix the infinite loop when running in uv mode if the current project has dynamic metadata. ([#3207](https://github.com/pdm-project/pdm/issues/3207))
- Add `--no-frozen-deps` option to `install-pdm.py` script to allow installing newer versions of dependencies. ([#3213](https://github.com/pdm-project/pdm/issues/3213))
- `pdm self update` now prefers the locked dependencies unless `--no-frozen-deps` is specified. ([#3216](https://github.com/pdm-project/pdm/issues/3216))
- By default, `pdm outdated` will only list direct dependencies. This can be changed by adding the `--include-sub` option. ([#3218](https://github.com/pdm-project/pdm/issues/3218))

### Documentation

- Show users the way to uninstall pdm in a more obvious way ([#2470](https://github.com/pdm-project/pdm/issues/2470))

## Release v2.19.2 (2024-10-11)

### Features & Improvements

- Support installing free-threaded Python interpreters with the `t` suffix. ([#3201](https://github.com/pdm-project/pdm/issues/3201))

### Bug Fixes

- `use_uv` fails to lock when there are non-ascii characters in pyproject.toml on Windows. ([#3181](https://github.com/pdm-project/pdm/issues/3181))
- Fix the `pre_install` and `post_install` signals receiving an exhausted generator, instead of a list of packages. ([#3190](https://github.com/pdm-project/pdm/issues/3190))
- Create backup file with random filename to avoid conflicts. ([#3193](https://github.com/pdm-project/pdm/issues/3193))
- Fix the logic error in the `uv` format marker matching. ([#3197](https://github.com/pdm-project/pdm/issues/3197))
- `pdm lock --check` on a lockfile generated with older PDM version has a 0 exit code when there's a change in `pyproject.toml`. ([#3199](https://github.com/pdm-project/pdm/issues/3199))

### Documentation

- Fixed *Bash Completion* suggestion so it doesn't require root privileges ([#3183](https://github.com/pdm-project/pdm/issues/3183))

## Release v2.19.1 (2024-09-23)

### Bug Fixes

- PDM libraries are not loaded correctly for in-process scripts when installed in the user site. ([#3178](https://github.com/pdm-project/pdm/issues/3178))

## Release v2.19.0 (2024-09-23)

### Breaking Changes

- The minimum supported Python version of projects using PDM has been bumped to 3.8. ([#3176](https://github.com/pdm-project/pdm/issues/3176))

### Bug Fixes

- Fallback version to 0.0.0 when the version is not specified or empty. This can avoid crash when building such project. ([#3163](https://github.com/pdm-project/pdm/issues/3163))
- Ensures that `/` is URL encoded in sources URL environment variables. ([#3169](https://github.com/pdm-project/pdm/issues/3169))
- Call functions from shared library in the in-process `env_spec.py` script. ([#3176](https://github.com/pdm-project/pdm/issues/3176))

### Removals and Deprecations

- PDM no longer falls back to `setuptools-pep660` when the build backend doesn't support PEP 660. ([#3159](https://github.com/pdm-project/pdm/issues/3159))

### Miscellany

- Change the project structure to a normal package from a namespace package. ([#3155](https://github.com/pdm-project/pdm/issues/3155))

## Release v2.18.2 (2024-09-10)

### Bug Fixes

- Respect the `excludes` and `overrides` settings when installing packages. ([#3113](https://github.com/pdm-project/pdm/issues/3113))
- Fix a bug of export command that packages with extras are included twice. ([#3123](https://github.com/pdm-project/pdm/issues/3123))
- Remove empty groups when removing packages with `pdm remove`. ([#3133](https://github.com/pdm-project/pdm/issues/3133))
- When running `pdm venv purge`, if the current project's python version had been referencing the removed venv then clear it out. ([#3137](https://github.com/pdm-project/pdm/issues/3137))
- Fix command `pdm config` to not show site configuration file path if it doesn't exist. ([#3149](https://github.com/pdm-project/pdm/issues/3149))
- Now when `--no-markers` is used, the exported requirements can only work on the current platform. ([#3152](https://github.com/pdm-project/pdm/issues/3152))

### Miscellany

- Skip tests related to python installation on non-standard platforms. ([#3053](https://github.com/pdm-project/pdm/issues/3053))

## Release v2.19.0a0 (2024-09-05)

### Breaking Changes

- `pre_install` and `post_install` signals now receive the list of packages to be installed, instead of a candidate mapping. ([#3144](https://github.com/pdm-project/pdm/issues/3144))

### Features & Improvements

- Deprecate `Core.synchronizer_class` attribute. To get the synchronizer class, use `Project.get_synchronizer` method instead. Deprecate `Core.resolver_class` attribute. To get the resolver class, use `Project.get_resolver` method instead. ([#3144](https://github.com/pdm-project/pdm/issues/3144))
- Add experimental support for `uv` as the resolver and installer. One can opt in by setting `use_uv` to `true` using `pdm config` command. ([#3144](https://github.com/pdm-project/pdm/issues/3144))

## Release v2.18.1 (2024-08-16)

### Bug Fixes

- Skip checking `project.name` if it is absent when running `pdm outdated`. ([#3095](https://github.com/pdm-project/pdm/issues/3095))
- Don't remove the `cross_platform` strategy from old lock files. ([#3105](https://github.com/pdm-project/pdm/issues/3105))
- Fix a bug that the VCS revision is lost if the candidate metadata is cached during resolution. ([#3107](https://github.com/pdm-project/pdm/issues/3107))
- Fix a bug that PDM can't delete source password when saved in keyring. ([#3108](https://github.com/pdm-project/pdm/issues/3108))

## Release v2.18.0 (2024-08-14)

### Features & Improvements

- Respect certificates in env vars `REQUESTS_CA_BUNDLE` and `CURL_CA_BUNDLE` when verifying SSL certificates. ([#3076](https://github.com/pdm-project/pdm/issues/3076))
- Allow pypi.verify_ssl to be configured via PDM_PYPI_VERIFY_SSL environmental variable. ([#3081](https://github.com/pdm-project/pdm/issues/3081))
- Clean logs older than 7 days. ([#3091](https://github.com/pdm-project/pdm/issues/3091))
- Polish the UI looking of locking packages to display the progress. ([#3100](https://github.com/pdm-project/pdm/issues/3100))

### Bug Fixes

- Fixed `pdm venv activate` to remove quotes such that `iex (pdm venv activate)` works correctly ([#2895](https://github.com/pdm-project/pdm/issues/2895))
- Don't crash if the version can't be resolved from the self project. ([#3077](https://github.com/pdm-project/pdm/issues/3077))
- Don't fail `install-pdm.py` if there is an invalid `pyproject.toml` file under the current directory. ([#3085](https://github.com/pdm-project/pdm/issues/3085))
- Make it able to expand env vars in the the dotenv file. Expose `PDM_PROJECT_ROOT` to the dotenv file for expansion. ([#3087](https://github.com/pdm-project/pdm/issues/3087))
- Fix a bug that Python markers from the existing locked packages are considered when locking with `--append` option. ([#3089](https://github.com/pdm-project/pdm/issues/3089))
- Backfill urls from configured indexed when exporting to requirements.txt. ([#3094](https://github.com/pdm-project/pdm/issues/3094))
- Consider the auto-selected Python range when installing from requirements.txt. ([#3095](https://github.com/pdm-project/pdm/issues/3095))
- Fix a bug that env vars do not override project config correctly. ([#3099](https://github.com/pdm-project/pdm/issues/3099))

## Release v2.17.3 (2024-08-01)

### Bug Fixes

- Fix a crash issue when `requires-python` is absent in the project metadata. ([#3062](https://github.com/pdm-project/pdm/issues/3062))
- Now correctly sets related config for PDM_IGNORE_SAVED_PYTHON when it is set to "false", "no", "0". ([#3064](https://github.com/pdm-project/pdm/issues/3064))
- Fix a bug that PDM plugins installed from project-root cannot be loaded, if they have dependencies. ([#3067](https://github.com/pdm-project/pdm/issues/3067))

## Release v2.17.2 (2024-07-31)

### Features & Improvements

- Improve the installation progress output to show the time elapsed. ([#3051](https://github.com/pdm-project/pdm/issues/3051))
- The effect of `pypi.ignore_stored_index` changes a bit. Now even if it is true, index configurations in the config will still be loaded if the index is listed in the `pyproject.toml`. ([#3052](https://github.com/pdm-project/pdm/issues/3052))

### Bug Fixes

- Ignore invalid requires-python values from index. ([#3038](https://github.com/pdm-project/pdm/issues/3038))
- Fix the group selection logic, to make `--without GROUP` work as expected. ([#3045](https://github.com/pdm-project/pdm/issues/3045))
- Suppress outputs for `pdm python install --quiet`. ([#3049](https://github.com/pdm-project/pdm/issues/3049))

## Release v2.17.1 (2024-07-19)

### Bug Fixes

- Raise dep-logic lower bound to 0.4.2 to fix issues with pdm lock after upgrading from older pdm versions ([#3033](https://github.com/pdm-project/pdm/issues/3033))
- Correct the current platform and architecture for win32 and macos systems. ([#3035](https://github.com/pdm-project/pdm/issues/3035))

### Miscellany

- Fix zsh completions ([#3031](https://github.com/pdm-project/pdm/issues/3031))

## Release v2.17.0 (2024-07-18)

### Breaking Changes

- `LockedRepository.all_candidates` now returns a `dict[str, list[Candidate]]` instead of `dict[str, Candidate]`. ([#2995](https://github.com/pdm-project/pdm/issues/2995))
- `post_lock` hook now receives a resolution result of type `dict[str, list[Candidate]]`, instead of `dict[str, Candidate]`. ([#2995](https://github.com/pdm-project/pdm/issues/2995))

### Features & Improvements

- Support reading requirement constraints from pip-style requirement files for "overriding" via `--override` option. ([#2896](https://github.com/pdm-project/pdm/issues/2896))
- Add a `--non-interactive` option for automation scenarios, also interactive prompts will not show up when not running in an interactive terminal. ([#2934](https://github.com/pdm-project/pdm/issues/2934))
- Refactored `pdm python install --list` to reuse the same implementation as other cli commands that work with Python interpreters from pbs_installer. ([#2977](https://github.com/pdm-project/pdm/issues/2977))
- Add `--license` and `--project-version` as CLI options to control and streamline them during `pdm init` - especially in automated scenarios with `--non-interactive` ([#2978](https://github.com/pdm-project/pdm/issues/2978))
- Run pdm sync in "post-rewrite" stage of pre-commit ([#2994](https://github.com/pdm-project/pdm/issues/2994))
- `Project.get_dependencies()` now returns a list of `Requirement` instead of a mapping. The first argument of `Project.add_dependencies()` now accepts a list of `Requirement` instead of a mapping. The old usage will be kept working for a short period of time and will be removed in the future. ([#2995](https://github.com/pdm-project/pdm/issues/2995))
- Support locking for specific target, which is a combination of (python, platform, implementation) triple. Bump lock file version to `4.5.0`.

Example usage: `pdm lock --platform=linux --python="==3.8.*" --implementation=cpython`. See the [docs](https://pdm-project.org/en/latest/usage/lock-targets) for more details. ([#2995](https://github.com/pdm-project/pdm/issues/2995))

- Rename `--reuse-env` to `--recreate` for `run` command, and reverse the behavior. ([#2999](https://github.com/pdm-project/pdm/issues/2999))
- PDM is now published with optional pinned dependencies using the pdm plugin [pdm-build-locked](https://pdm-build-locked.readthedocs.io/).

To install pdm with its dependencies pinned to the versions it was tested with, run:

```
    pipx install pdm[locked]
```

To install optional dependency group copier:

```
    pipx install pdm[locked,copier-locked]
```

This feature is entirely optional. Installing pdm without the extra will work the same way as before this change. ([#3001](https://github.com/pdm-project/pdm/issues/3001))

- Added `--clean-unselected` alias for `--only-keep` ([#3007](https://github.com/pdm-project/pdm/issues/3007))
- Group options for update strategy and save strategy. ([#3016](https://github.com/pdm-project/pdm/issues/3016))

### Bug Fixes

- When locking dependencies that references the self project, the referenced groups should also be recorded in the lockfile. ([#2976](https://github.com/pdm-project/pdm/issues/2976))
- Retry failed installation jobs if they are run sequentially, such as for editable dependencies. ([#3005](https://github.com/pdm-project/pdm/issues/3005))
- Fix the local path issue when `-p` is passed to change the project root. ([#3009](https://github.com/pdm-project/pdm/issues/3009))
- Fix a bug that PDM can't install editable self package with non-isolated build in one go. ([#3018](https://github.com/pdm-project/pdm/issues/3018))
- Add context when parsing version failed. ([#3020](https://github.com/pdm-project/pdm/issues/3020))
- Fix a mistake in build env setup that will cause the `PATH` env var length to grow. ([#3022](https://github.com/pdm-project/pdm/issues/3022))

### Removals and Deprecations

- Remove the deprecation warning of `BaseCommand.__init__()` method. Now it doesn't take any arguments. ([#2995](https://github.com/pdm-project/pdm/issues/2995))
- `Provider.get_reuse_candidate()` method is deprecated in favor of `Provider.iter_reuse_candidates()`, to return an iterable of reuse candidates. ([#2995](https://github.com/pdm-project/pdm/issues/2995))
- `--no-markers` option in `pdm export` command becomes a no-op and is marked as deprecated, because it doesn't make sense anymore. ([#2995](https://github.com/pdm-project/pdm/issues/2995))
- `ignore_compatibility` parameter of `Project.get_provider()`/`Project.get_repository()`/`Environment.get_finder()` is deprecated. Pass in a `EnvSpec` via `env_spec` parameter instead. `requires_python` parameter of `pdm.resolver.core.resolve()` function is deprecated and has no effect. `cross_platform` parameter of `pdm.cli.actions.resolve_candidates_from_lockfile()` function is deprecated and has no effect. ([#2995](https://github.com/pdm-project/pdm/issues/2995))

## Release v2.16.1 (2024-06-26)

### Bug Fixes

- Fix new interface from pbs_installer regarding `build_dir` and best match auto-install strategy for `pdm use` (same as for `pdm python install --list`) ([#2943](https://github.com/pdm-project/pdm/issues/2943))
- Fix crash when pdm is used with `importlib-metadata` version 8.0. ([#2974](https://github.com/pdm-project/pdm/issues/2974))

## Release v2.16.0 (2024-06-25)

### Features & Improvements

- Add `--no-extras` to `pdm export` to strip extras from the requirements. Now the default behavior is to keep extras. ([#2519](https://github.com/pdm-project/pdm/issues/2519))
- Support PEP 723: running scripts with inline metadata in standalone environment with dependencies. ([#2924](https://github.com/pdm-project/pdm/issues/2924))
- `pdm use` and `pdm python install` now take `requires-python` into account (incl. from pyproject.toml) if python version not specified and `pdm use` provides auto installation by that. ([#2943](https://github.com/pdm-project/pdm/issues/2943))
- `--no-isolation` no longer installs `build-requires` nor dynamic build dependencies, to be consistent with `pip`. ([#2944](https://github.com/pdm-project/pdm/issues/2944))
- Add notifiers in CLI output when global project is being used. ([#2952](https://github.com/pdm-project/pdm/issues/2952))
- Use `tool.pdm.resolution` table when calculating the content hash of project file, previously only `overrides` table was used. This will change the hash already stored in the lockfile, so bump the lockfile version to `4.4.2`. ([#2956](https://github.com/pdm-project/pdm/issues/2956))

### Bug Fixes

- Add max retries on read timeout or bad connection. ([#2914](https://github.com/pdm-project/pdm/issues/2914))
- Don't update local files if they don't change. ([#2966](https://github.com/pdm-project/pdm/issues/2966))
- Don't list python versions that don't have any installation link for the current platform. ([#2970](https://github.com/pdm-project/pdm/issues/2970))

### Documentation

- Clarify the purposes of `pdm outdated` and `--unconstrained` option. ([#2965](https://github.com/pdm-project/pdm/issues/2965))
- Some clarifications on the interpreter selection and central package cache. ([#2967](https://github.com/pdm-project/pdm/issues/2967))

## Release v2.15.4 (2024-05-30)

### Bug Fixes

- Build wheel from sdist if available, to make sure sdist is built properly. This behavior is consistent with [pypa/build](https://pypi.org/project/build). ([#2843](https://github.com/pdm-project/pdm/issues/2843))
- Fix the issue of self-referencing extra dependencies failing to be resolved for local packages. ([#2898](https://github.com/pdm-project/pdm/issues/2898))
- Fix an issue of max recursion depth error when parsing a poetry project with circular dependencies on local packages. ([#2900](https://github.com/pdm-project/pdm/issues/2900))
- Fix a bug that VCS dependencies and `--self` don't work in the exported requirements.txt with hashes. ([#2908](https://github.com/pdm-project/pdm/issues/2908))
- Fix a cache miss when there exist built wheels for a given link. ([#2912](https://github.com/pdm-project/pdm/issues/2912))
- Don't try to store caches when `--no-cache` is given. ([#2913](https://github.com/pdm-project/pdm/issues/2913))

## Release v2.15.3 (2024-05-20)

### Bug Fixes

- Fixed pdm venv activate, to also work for windows. And added documentation on how to authenticate to Azure Artifacts ([#2851](https://github.com/pdm-project/pdm/issues/2851))
- Don't show unsupported formats in `pdm export`. ([#2877](https://github.com/pdm-project/pdm/issues/2877))
- Proxy (`HTTP_PROXY` env vars) settings are ignored for custom indexes. ([#2880](https://github.com/pdm-project/pdm/issues/2880))
- Fix the quoting of venv activate command for powershell. ([#2881](https://github.com/pdm-project/pdm/issues/2881))
- Raise an error if the package given by `pdm update` does not exist in the select dependency group but in other groups. ([#2885](https://github.com/pdm-project/pdm/issues/2885))

## Release v2.15.2 (2024-05-08)

### Features & Improvements

- Use `get_runner()` method to build the task runner in `run` command. `runner_cls` attribute is deprecated. ([#2872](https://github.com/pdm-project/pdm/issues/2872))

### Bug Fixes

- Expand `${PROJECT_ROOT}` in source URLs. ([#2846](https://github.com/pdm-project/pdm/issues/2846))
- Fix env and other options being inherited in nested composite scripts. ([#2849](https://github.com/pdm-project/pdm/issues/2849))
- Keep the `${PROJECT_ROOT}` variable in dependencies after running `pdm lock --update-reuse`. ([#2852](https://github.com/pdm-project/pdm/issues/2852))
- Make `direct_minimal_versions` work on newly added dependencies. ([#2853](https://github.com/pdm-project/pdm/issues/2853))
- Fix a syntax error in the zsh completion script. ([#2868](https://github.com/pdm-project/pdm/issues/2868))

## Release v2.15.1 (2024-04-25)

### Bug Fixes

- Disable check update in `zsh` completion script. ([#2838](https://github.com/pdm-project/pdm/issues/2838))
- Fixes cached packages metadata files (`.referrers`) collisions on `sync` when using a `venv` with `symlink` cache method. ([#2839](https://github.com/pdm-project/pdm/issues/2839))

### Documentation

- Build docs with object inventory to support cross references from Sphinx documentation projects. ([#2841](https://github.com/pdm-project/pdm/issues/2841))

## Release v2.15.0 (2024-04-19)

### Features & Improvements

- Packages format preferences can now be defined in the project `pyproject.toml` using the `no-binary`, `only-binary` and `prefer-binary` keys of the `tool.pdm.resolution` section. ([#2656](https://github.com/pdm-project/pdm/issues/2656))

### Bug Fixes

- Don't create project and virtualenv when running `pdm python install`. ([#2809](https://github.com/pdm-project/pdm/issues/2809))
- Clean up the python installation directory if a previous download was unsuccessful. ([#2810](https://github.com/pdm-project/pdm/issues/2810))
- Don't cache editable installations. ([#2816](https://github.com/pdm-project/pdm/issues/2816))
- Fix a bug that installing in-project plugins with editable local paths doesn't work. ([#2820](https://github.com/pdm-project/pdm/issues/2820))
- Don't create log directory until it's needed, to fix a PermissionError in docker environment. ([#2825](https://github.com/pdm-project/pdm/issues/2825))
- Fix recursive script detection on multiple invocations. ([#2829](https://github.com/pdm-project/pdm/issues/2829))

## Release v2.14.0 (2024-04-12)

### Features & Improvements

- Revert the package cache introduced in 2.13. Don't cache the decompressed contents of wheels unless being told so. ([#2803](https://github.com/pdm-project/pdm/issues/2803))

### Bug Fixes

- Fix inconsistent logging when `pdm use` a different python interpreter ([#2776](https://github.com/pdm-project/pdm/issues/2776))
- Fix PDM unable to find Python interpreters when `PDM_IGNORE_ACTIVE_VENV` is set ([#2779](https://github.com/pdm-project/pdm/issues/2779))
- Check verify_ssl when trusting each source. ([#2784](https://github.com/pdm-project/pdm/issues/2784))
- Fix name check for project itself in `pdm outdated` ([#2785](https://github.com/pdm-project/pdm/issues/2785))
- Fix a regression that proxy env vars are not respected. ([#2788](https://github.com/pdm-project/pdm/issues/2788))
- Fix an issue that venv provider can't be found when providers are explicitly configured. ([#2792](https://github.com/pdm-project/pdm/issues/2792))
- Fix a bug that `[tool.pdm.options]` are ignored if `-c/--config CONFIG` is given. ([#2793](https://github.com/pdm-project/pdm/issues/2793))
- Make `--without` respect groups in `dev-dependencies` ([#2799](https://github.com/pdm-project/pdm/issues/2799))

## Release v2.13.3 (2024-04-08)

### Bug Fixes

- Per-source configuration for ca-certs and client-cert. [#2754](https://github.com/pdm-project/pdm/issues/2754)
- Remove all caches by removing individual cache types one by one. [#2757](https://github.com/pdm-project/pdm/issues/2757)
- Use the default HTTP client when downloading the pythons, to use the certificates settings. [#2759](https://github.com/pdm-project/pdm/issues/2759)
- Fix a race condition where pth files take effect when multiple packages are installed in parallel. [#2762](https://github.com/pdm-project/pdm/issues/2762)
- Refuse to run recursive composite scripts. [#2766](https://github.com/pdm-project/pdm/issues/2766)

## Release v2.13.2 (2024-03-30)

### Bug Fixes

- Fix errors when parsing poetry format that contains special characters in author name. Poetry-specific `parse_name_email` and `NAME_EMAIL_RE` moved from `pdm.formats.base` to `pdm.formats.poetry`. [#2665](https://github.com/pdm-project/pdm/issues/2665)
- Fix a race condition in cached packages. When a cached package is being created it shouldn't be used for installation. [#2739](https://github.com/pdm-project/pdm/issues/2739)
- Add back `PreparedCandidate.build()` for backward-compatibility. [#2747](https://github.com/pdm-project/pdm/issues/2747)

### Documentation

- Fixed a small non-code typo in docs and provided better wording. [#2740](https://github.com/pdm-project/pdm/issues/2740)

## Release v2.13.1 (2024-03-29)

### Bug Fixes

- Fix a bug that PDM couldn't find interpreters for global project. [#2726](https://github.com/pdm-project/pdm/issues/2726)
- Make the cache package path shorter to solve the Windows path problem. [#2730](https://github.com/pdm-project/pdm/issues/2730)

### Documentation

- Extract "Lock file" doc from "Manage Dependencies" doc. [#2725](https://github.com/pdm-project/pdm/issues/2725)

## Release v2.13.0 (2024-03-27)

### Features & Improvements

- Add option to exclude group(s) when running `pdm sync/install -G:all` by adding flag `--without group1,group2,...` [#2258](https://github.com/pdm-project/pdm/issues/2258)
- Default to log to user home and make logs directory configurable. [#2398](https://github.com/pdm-project/pdm/issues/2398)
- Add an option `keep_going` to continue on errors for composite scripts and return the last failing exit code. [#2582](https://github.com/pdm-project/pdm/issues/2582)
- Add an option `working_dir` for PDM's scripts to set the current working directory. [#2620](https://github.com/pdm-project/pdm/issues/2620)
- Allow updating specific sub-dependencies (i.e., transitive dependencies) in the lock file. [#2628](https://github.com/pdm-project/pdm/issues/2628)
- Add `--config-setting` option to `add/install/sync/update/remove/export` commands, the config settings dictionary will be shared by all packages. [#2636](https://github.com/pdm-project/pdm/issues/2636)
- Cache the decompressed contents of wheels for faster access. [#2660](https://github.com/pdm-project/pdm/issues/2660)
- Add configuration for timeout for network requests. [#2680](https://github.com/pdm-project/pdm/issues/2680)
- Reuse the request session within the environment. [#2697](https://github.com/pdm-project/pdm/issues/2697)
- Caches can be disabled by using the `--no-cache` option or setting the `PDM_NO_CACHE` environment variable. [#2702](https://github.com/pdm-project/pdm/issues/2702)
- Switch to `httpx.Client` for HTTP requests, drop `requests` dependency. [#2709](https://github.com/pdm-project/pdm/issues/2709)
- We have timemachine now! You can exclude packages published newer than a certain date via `pdm lock --exclude-newer=<date>`, allowing reproduction of resolutions regardless of new package releases. [#2712](https://github.com/pdm-project/pdm/issues/2712)
- Add command `pdm outdated` to check the outdated packages and list the latest versions. [#2718](https://github.com/pdm-project/pdm/issues/2718)
- When `python.use_venv` is on, always try to create a virtualenv when using `pdm use` to switch the Python interpreter. [#2720](https://github.com/pdm-project/pdm/issues/2720)
- Support installing Pythons from [python-build-standalone](https://github.com/indygreg/python-build-standalone). Add command group `pdm python` to manage Python installations. And `pdm use` can automatically install the Python interpreter if it's not found. [#2721](https://github.com/pdm-project/pdm/issues/2721)
- Supports custom distribution files path via `-d/--dest` option for `pdm publish`. [#2723](https://github.com/pdm-project/pdm/issues/2723)

### Bug Fixes

- Don't modify TOML tables that are not related to PDM. [#2666](https://github.com/pdm-project/pdm/issues/2666)
- Made `--without` imply `--with :all`. [#2670](https://github.com/pdm-project/pdm/issues/2670)
- Expand user path for `venv.location` and other path-like config values. [#2672](https://github.com/pdm-project/pdm/issues/2672)
- Give a default version when it's missing in `pyproject.toml` when parsing candidate's metadata. [#2677](https://github.com/pdm-project/pdm/issues/2677)
- Fix the issue that ANSI codes are shown in the output of `pdm --help` on Windows. [#2678](https://github.com/pdm-project/pdm/issues/2678)
- Don't show empty configuration sections in `pdm config`. [#2683](https://github.com/pdm-project/pdm/issues/2683)

### Documentation

- Document the difference between `[tool.pdm.scripts]` and `[project.scripts]` [#2121](https://github.com/pdm-project/pdm/issues/2121)

### Removals and Deprecations

- Remove the support of `pth` cache method. And `symlink` cache method now behaves the same as `symlink_individual` cache method. [#2660](https://github.com/pdm-project/pdm/issues/2660)
- Remove `pdm.models.environment` module deprecated before. Also remove the renamed members from `pdm.environments`. [#2710](https://github.com/pdm-project/pdm/issues/2710)

### Miscellany

- Delete `setup.cfg`, move tool configurations under it to `pyproject.toml` [#2703](https://github.com/pdm-project/pdm/issues/2703)

## Release v2.12.4 (2024-02-26)

### Features & Improvements

- Use env PDM_NO_EDITABLE as the default value for --no-editable option. [#2613](https://github.com/pdm-project/pdm/issues/2613)

### Bug Fixes

- Reset project.environment when importing from setup.py, to fix resolution error. [#2608](https://github.com/pdm-project/pdm/issues/2608)
- Do not fetch package hashes when `--frozen-lockfile` is passed. [#2630](https://github.com/pdm-project/pdm/issues/2630)
- Make sure non-venv interpreters are used by venv creator. [#2631](https://github.com/pdm-project/pdm/issues/2631)
- Don't cause a hard failure if the local directory doesn't exist. [#2650](https://github.com/pdm-project/pdm/issues/2650)

### Documentation

- Fix the default value for negative CLI flags. [#2642](https://github.com/pdm-project/pdm/issues/2642)
- Auto-gen configuration reference documentation. [#2645](https://github.com/pdm-project/pdm/issues/2645)

## Release v2.12.3 (2024-02-01)

### Bug Fixes

- fix the package-type fixer won't update toml properly for "Nested Section Ordering Issue in TOML". [#2578](https://github.com/pdm-project/pdm/issues/2578)
- Unable to force override a package if the package is required with extras. [#2586](https://github.com/pdm-project/pdm/issues/2586)
- Failed to clone template repository if the URL contains the rev part. [#2597](https://github.com/pdm-project/pdm/issues/2597)
- Handle legacy specifiers when converting from poetry project. [#2599](https://github.com/pdm-project/pdm/issues/2599)

### Documentation

- Fix typo in template docs [#2588](https://github.com/pdm-project/pdm/issues/2588)

## Release v2.12.2 (2024-01-21)

### Bug Fixes

- Fix the auto fixer for package-type. [#2564](https://github.com/pdm-project/pdm/issues/2564)
- Fix the wrong installation destination for header files when installing build requirements. [#2573](https://github.com/pdm-project/pdm/issues/2573)
- Install header files into package namespace under `include` directory. [#2574](https://github.com/pdm-project/pdm/issues/2574)

## Release v2.12.1 (2024-01-17)

### Bug Fixes

- Hotfix: missing `identifier` attribute for package type fixer. [#2564](https://github.com/pdm-project/pdm/issues/2564)

## Release v2.12.0 (2024-01-17)

### Features & Improvements

- Allow excluding packages from the lockfile via `tool.pdm.resolution.excludes` setting, the dependencies will also be skipped. [#1316](https://github.com/pdm-project/pdm/issues/1316)
- Rename `--no-lock` option to `--frozen-lockfile`. [#2496](https://github.com/pdm-project/pdm/issues/2496)
- Add `--no-hashes` as the recommended option name in favor of `--without-hashes` for `pdm export` command. [#2497](https://github.com/pdm-project/pdm/issues/2497)
- Add `--no-markers` to `export` command to exclude markers from the output. [#2497](https://github.com/pdm-project/pdm/issues/2497)
- Allow initializing a project without extra project files, with a new builtin template "minimal". Run it with `pdm init minimal`. [#2543](https://github.com/pdm-project/pdm/issues/2543)
- Change the warning category emitted by `deprecated_warning()` to `PDMDeprecationWarning`. [#2547](https://github.com/pdm-project/pdm/issues/2547)
- Prereleases will be allowed if a prerelease version is pinned in the lockfile. This can be disabled by passing `--stable` option. [#2552](https://github.com/pdm-project/pdm/issues/2552)
- Change `tracked_names` argument to keyword-only. Move `allow_prereleases` setting to `tool.pdm.resolution` table. [#2552](https://github.com/pdm-project/pdm/issues/2552)
- Rename the `preferred_pins` argument of provider classes to `locked_candidates`, and deprecate the old name. [#2552](https://github.com/pdm-project/pdm/issues/2552)
- Rename the `package-type` field under `tool.pdm` settings table to `distribution` to make it more clear. [#2564](https://github.com/pdm-project/pdm/issues/2564)

### Bug Fixes

- `tool.pdm.resolution` settings won't be honored when installing dependencies into the build environment. [#1316](https://github.com/pdm-project/pdm/issues/1316)
- Fixed pdm list output containing full license text in some cases [#2538](https://github.com/pdm-project/pdm/issues/2538)
- Fix the environment variable substitution for `cmd` scripts. [#2542](https://github.com/pdm-project/pdm/issues/2542)
- Allow normal extension modules in wheel tags when the python is debug build. [#2548](https://github.com/pdm-project/pdm/issues/2548)
- Don't use pypi.org when pypi.url is set. [#2560](https://github.com/pdm-project/pdm/issues/2560)

### Removals and Deprecations

- Remove deprecated methods from `Project`. Remove deprecated helper functions from `actions.py`. [#2547](https://github.com/pdm-project/pdm/issues/2547)

## Release v2.11.2 (2024-01-02)

### Bug Fixes

- Fix a KeyError raised when resolving a URL dependency without package name given. [#2488](https://github.com/pdm-project/pdm/issues/2488)
- `pdm update --update-eager` can hit InconsistentCandidate error when dependency is included both through default dependencies and extra. [#2495](https://github.com/pdm-project/pdm/issues/2495)
- `pdm install` should not warn when overwriting its own symlinks on `install`/`update`. [#2502](https://github.com/pdm-project/pdm/issues/2502)
- Fix a bug that candidates without local version are rejected when the local version is pinned. [#2507](https://github.com/pdm-project/pdm/issues/2507)

### Documentation

- Add maturin as a compatible build backend in the docs. [#2510](https://github.com/pdm-project/pdm/issues/2510)

## Release v2.11.1 (2023-12-14)

### Bug Fixes

- Update candidate names before resolving markers, to fix a KeyError when the requirement is not named. [#2488](https://github.com/pdm-project/pdm/issues/2488)
- Fix a KeyError when resolving packages that have parents that are no longer needed. [#2489](https://github.com/pdm-project/pdm/issues/2489)

## Release v2.11.0 (2023-12-14)

### Features & Improvements

- Officially drop the support for Python 3.7.
- Allow exporting current project as editable dependency with `pdm export`. [#1910](https://github.com/pdm-project/pdm/issues/1910)
- Improve the lockfile compatibility checking by using 3-digit version numbers. This can distinguish forward-compatibility and backward-compatibility. [#2164](https://github.com/pdm-project/pdm/issues/2164)
- Add `--skip-existing` to `pdm publish` to ignore the uploading error if the package already exists. [#2362](https://github.com/pdm-project/pdm/issues/2362)
- Use `==major.minor.*` as default requires python for application projects. [#2382](https://github.com/pdm-project/pdm/issues/2382)
- We now use the `package-type` field in the `tool.pdm` table to differentiate between library and application projects. [#2394](https://github.com/pdm-project/pdm/issues/2394)
- Add support for {pdm} placeholder in script definitions to call the same PDM entrypoint [#2408](https://github.com/pdm-project/pdm/issues/2408)
- When exporting requirements, record the environment markers from all parents for each requirement. This allows the exported requirements to work on different platforms and Python versions. [#2418](https://github.com/pdm-project/pdm/issues/2418)
- `pdm lock` now supports `--update-reuse` option to keep the pinned versions in the lockfile if possible. [#2419](https://github.com/pdm-project/pdm/issues/2419)
- Introduce a new lock strategy `inherit_metadata` to inherit and merge markers from parent requirements. This is enabled by default when creating a new lockfile. [#2421](https://github.com/pdm-project/pdm/issues/2421)
- New cache methods: `symlink_individual` for creating a symlink for each individual package file and `hardlink` for creating hardlinks. [#2425](https://github.com/pdm-project/pdm/issues/2425)
- Add "pdm sync" pre-commit hook [#2474](https://github.com/pdm-project/pdm/issues/2474)
- New update strategy: `reuse-installed`. When this strategy is enabled, PDM will try to reuse the versions already installed in the environment, even if the package names are given in the command line following `add` or `update`. This strategy is supported by `add`, `update` and `lock` commands. [#2479](https://github.com/pdm-project/pdm/issues/2479)
- Show subcommand's help info when passing unrecognized arguments. [#2480](https://github.com/pdm-project/pdm/issues/2480)
- add `PDM_CACHE_DIR` environment variable to configure cache directory location. [#2485](https://github.com/pdm-project/pdm/issues/2485)

### Bug Fixes

- Use the same order of Python interpreters as interactive mode in `pdm init -n`. [#2436](https://github.com/pdm-project/pdm/issues/2436)
- `pdm init` now implies `--lib` if `--backend` is passed. [#2437](https://github.com/pdm-project/pdm/issues/2437)
- Fix a bug that link collection ignores package-index-binding. [#2442](https://github.com/pdm-project/pdm/issues/2442)
- Fix the wrong installation candidates for different architectures on Windows. [#2464](https://github.com/pdm-project/pdm/issues/2464)
- Fix installing PEP 561 stub-only packages with `install.cache_method = "symlink"`. [#2466](https://github.com/pdm-project/pdm/issues/2466)
- Fix a `KeyError` raised by `pdm update --unconstrained` when the project itself is listed as a dependency. [#2483](https://github.com/pdm-project/pdm/issues/2483)

## Release v2.10.4 (2023-11-24)

### Bug Fixes

- Do not detect as requirements.txt if the file is a python script. [#2416](https://github.com/pdm-project/pdm/issues/2416)
- Provide information of the original line when parsing requirement fails. [#2417](https://github.com/pdm-project/pdm/issues/2417)
- Resolve `-r` requirements paths relative to the requirement file they are specified in [#2422](https://github.com/pdm-project/pdm/issues/2422)
- Updating package now overwrites the old files instead of removing before installing. [#2423](https://github.com/pdm-project/pdm/issues/2423)

## Release v2.10.3 (2023-11-16)

### Bug Fixes

- Create virtualenv for conda base Python. [#2409](https://github.com/pdm-project/pdm/issues/2409)

## Release v2.10.2 (2023-11-16)

### Features & Improvements

- Log the response text when `pdm publish` fails with HTTP error. [#2400](https://github.com/pdm-project/pdm/issues/2400)

### Bug Fixes

- Improve the error message when a specific package can't be found in the lockfile. [#2358](https://github.com/pdm-project/pdm/issues/2358)
- prevent wrong project name (including space and illegal characters) [#2360](https://github.com/pdm-project/pdm/issues/2360)
- Fix a bug that PDM cannot detect namespace packages correctly when creating symlinks. The package's `__init__.py` contains an unusual line. [#2378](https://github.com/pdm-project/pdm/issues/2378)
- Fix template files created by `pdm init` being read-only when copied from a read-only PDM installation. [#2379](https://github.com/pdm-project/pdm/issues/2379)
- Don't reset the build backend when asking for import. [#2388](https://github.com/pdm-project/pdm/issues/2388)
- Never wrap the output of the `export` command. [#2390](https://github.com/pdm-project/pdm/issues/2390)
- Forbid global project in conda base environment, since it may remove conda-managed packages. [#2409](https://github.com/pdm-project/pdm/issues/2409)

## Release v2.10.1 (2023-11-07)

### Bug Fixes

- Fix a bug preventing ctrl-c from interrupting program execution on 2nd invocation when using "pdm run" (Windows only). [#2292](https://github.com/pdm-project/pdm/issues/2292)
- Fix list index out of range when build error message is empty. [#2337](https://github.com/pdm-project/pdm/issues/2337)
- Fix find_link sources being exported as `--extra--index-url` [#2342](https://github.com/pdm-project/pdm/issues/2342)
- Fix an installation failure when install.cache = true. [#2355](https://github.com/pdm-project/pdm/issues/2355)
- Fix a resolution issue that extra dependencies are not resolved when the bare dependency has more specific version constraint. [#2369](https://github.com/pdm-project/pdm/issues/2369)

### Documentation

- Set up a chatbot powered by LLM on the doc page. [#2365](https://github.com/pdm-project/pdm/issues/2365)

## Release v2.10.0 (2023-10-26)

### Features & Improvements

- Allow binding packages to specific sources with `include_packages` and `exclude_packages` config under `tool.pdm.source` table. [#1645](https://github.com/pdm-project/pdm/issues/1645)
- Show warnings when a package is rejected by the resolve because of uncovered `requires-python` range. And provide a way to ignore them per-package. [#2304](https://github.com/pdm-project/pdm/issues/2304)
- Add `-q/--quiet` option to suppress some warnings printed to the console. This option is mutually exclusive with `-v/--verbose`. [#2304](https://github.com/pdm-project/pdm/issues/2304)
- Introduce a new `--strategy/-S` option for `lock` command, to specify one or more strategy flags for resolving dependencies. `--static-urls` and `--no-cross-platform` are deprecated at the same time. [#2310](https://github.com/pdm-project/pdm/issues/2310)
- Add lock option to resolve direct dependencies to the minimal versions available. [#2310](https://github.com/pdm-project/pdm/issues/2310)
- Report the progress of download and unpacking when installing packages. [#2328](https://github.com/pdm-project/pdm/issues/2328)

### Bug Fixes

- Change the venv backend clean function `pdm.cli.commands.venv.backend.Backend._ensure_clean` to empty the `.venv` folder instead of deleting it. [#2282](https://github.com/pdm-project/pdm/issues/2282)
- Fix a bug that dependency groups from Poetry 1.2+ do not migrate properly to PDM. [#2285](https://github.com/pdm-project/pdm/issues/2285)
- Fix a bug that build requirements are installed into wrong location when using `--venv` option. [#2314](https://github.com/pdm-project/pdm/issues/2314)
- Fix a bug that global repository setting results in TypeError . [#2330](https://github.com/pdm-project/pdm/issues/2330)
- Fix a credentials error when working with two indices on the same host [#2333](https://github.com/pdm-project/pdm/issues/2333)

### Miscellany

- Officially supports python3.12 now. [#2301](https://github.com/pdm-project/pdm/issues/2301)

## Release v2.9.3 (2023-09-25)

### Bug Fixes

- Revert the changes to the behavior of installing self, introduced in #2162. Self package won't be installed when `--no-default` is requested. [#2230](https://github.com/pdm-project/pdm/issues/2230)
- Reject the candidate if it contains invalid metadata, to avoid a crash in the process of resolution. [#2261](https://github.com/pdm-project/pdm/issues/2261)

### Documentation

- Clarify what `--no-isolated` does. [#2071](https://github.com/pdm-project/pdm/issues/2071)

## Release v2.9.2 (2023-09-12)

### Features & Improvements

- Fix an issue that `--no-lock` option doesn't work as expected. Also support `--no-lock` option for `add`, `remove` and `update` commands. [#2245](https://github.com/pdm-project/pdm/issues/2245)

### Bug Fixes

- Use `findpython` to find pythons with the spec given by the user. [#2225](https://github.com/pdm-project/pdm/issues/2225)
- Use UTF-8 to read pyvenv.cfg. [#2227](https://github.com/pdm-project/pdm/issues/2227)
- On Windows, try looking for the `virtualenv` `python.exe` binary under `bin/` as well as `Scripts/` and the `virtualenv`/`conda` root. [#2236](https://github.com/pdm-project/pdm/issues/2236)
- Write relocatable dependency URLs with `${PROJECT_ROOT}` variable in the lockfile. [#2240](https://github.com/pdm-project/pdm/issues/2240)

## Release v2.9.1 (2023-09-03)

### Features & Improvements

- Support convert setup.cfg without existing setup.py. [#2222](https://github.com/pdm-project/pdm/issues/2222)

### Bug Fixes

- `pdm run` should only find local file if the command starts with `./`. [#2221](https://github.com/pdm-project/pdm/issues/2221)

## Release v2.9.0 (2023-08-31)

### Features & Improvements

- Add an `--overwrite` option to `pdm init` to overwrite existing files(default False). [#2163](https://github.com/pdm-project/pdm/issues/2163)
- Support passing filter patterns as positional arguments to `pdm list` command. Add `--tree` as an alias and preferred name of `--graph` option. [#2165](https://github.com/pdm-project/pdm/issues/2165)
- Switch to truststore by default. [#2195](https://github.com/pdm-project/pdm/issues/2195)
- Consider packages as installed if the venv includes them from the system-site-packages. [#2216](https://github.com/pdm-project/pdm/issues/2216)
- Allow `pdm run` to run a script with the relative or absolute path. [#2217](https://github.com/pdm-project/pdm/issues/2217)

### Bug Fixes

- Fix a bug that removing dev dependency uninstalls the project as well. [#2150](https://github.com/pdm-project/pdm/issues/2150)
- Fix a bug that `@ file://` dependencies can not be updated. [#2169](https://github.com/pdm-project/pdm/issues/2169)
- Fix a bug that dependencies requested out of the range of `requires-python` cause PDM to crash. [#2175](https://github.com/pdm-project/pdm/issues/2175)
- Fix the compatibility issue with copier 8.0+. [#2177](https://github.com/pdm-project/pdm/issues/2177)
- Makes `comparable_version("1.2.3+local1") == Version("1.2.3")`. [#2182](https://github.com/pdm-project/pdm/issues/2182)
- Default behavior for pdm venv activate when shell detection fails. [#2187](https://github.com/pdm-project/pdm/issues/2187)
- Handle parsing errors when converting from poetry-style metadata. [#2203](https://github.com/pdm-project/pdm/issues/2203)
- Don't copy .pyc files from the template directory. [#2213](https://github.com/pdm-project/pdm/issues/2213)

### Removals and Deprecations

- Remove the legacy build backend `pdm-pep517`. [#2167](https://github.com/pdm-project/pdm/issues/2167)

## Release v2.8.2 (2023-07-31)

### Features & Improvements

- Allow setting username and password in URL for publish command [#2140](https://github.com/pdm-project/pdm/issues/2140)

### Bug Fixes

- Use UTF-8 encoding when writing `sitecustomize.py`. [#2139](https://github.com/pdm-project/pdm/issues/2139)

## Release v2.8.1 (2023-07-26)

### Features & Improvements

- Add `keyring`, `copier`, `cookiecutter`, `template`, `truststore` dependency groups. [#2109](https://github.com/pdm-project/pdm/issues/2109)
- Ignore wheels for python versions not in range. [#2113](https://github.com/pdm-project/pdm/issues/2113)
- Read default value from env var `PDM_PROJECT` for `-p/--project` option. [#2126](https://github.com/pdm-project/pdm/issues/2126)

### Bug Fixes

- Fix the comparison of the candidate keys in the lockfile. [#2120](https://github.com/pdm-project/pdm/issues/2120)
- Don't update `pyproject.toml` if both `--unconstrained` and `--dry-run` are passed to `pdm update`. [#2125](https://github.com/pdm-project/pdm/issues/2125)
- Overwrite the `build-system` table when importing from other package manager. [#2126](https://github.com/pdm-project/pdm/issues/2126)
- Skip sources with empty URL when merging sources. [#2130](https://github.com/pdm-project/pdm/issues/2130)
- Fix the invalid requirement converted from poetry metadata. [#2133](https://github.com/pdm-project/pdm/issues/2133)

### Dependencies

- Update `unearth` to 0.10.0 [#2113](https://github.com/pdm-project/pdm/issues/2113)

## Release v2.8.0 (2023-07-15)

### Features & Improvements

- Support target python with other architectures. [#2078](https://github.com/pdm-project/pdm/issues/2078)
- Display the help information when running pdm directly. [#2081](https://github.com/pdm-project/pdm/issues/2081)
- Allow to change the python providers from the config. Support finding pythons from Rye installation location with the new findpython. [#2099](https://github.com/pdm-project/pdm/issues/2099)
- Option to save static URLs in the lockfile. By default only filenames are saved. [#2101](https://github.com/pdm-project/pdm/issues/2101)

### Bug Fixes

- Fix a bug that egg-info directories are not removed completely, leading to incomplete distribution. [#2027](https://github.com/pdm-project/pdm/issues/2027)
- Skip distributions with wrong package meta information and duplicate path. [#2075](https://github.com/pdm-project/pdm/issues/2075)
- Avoid mistakenly passing command-line arguments while testing. [#2083](https://github.com/pdm-project/pdm/issues/2083)
- Fix a bug that lockfile groups are overwritten when running locking in a preceding step of `pdm install`. [#2086](https://github.com/pdm-project/pdm/issues/2086)
- Tolerate and actually ignore the local versions in version specifiers. [#2102](https://github.com/pdm-project/pdm/issues/2102)
- Fix a bug that shared cache cannot support overlapping namespace packages. [#2105](https://github.com/pdm-project/pdm/issues/2105)

### Documentation

- Add notes about using custom venv path. [#2096](https://github.com/pdm-project/pdm/issues/2096)

## Release v2.8.0a2 (2023-06-30)

### Bug Fixes

- Fix a bug that dependencies can't be updated when the table is separated by another table. [#2056](https://github.com/pdm-project/pdm/issues/2056)
- Fix a bug that `*_lock` hooks are always emitted with dry_run=True in `pdm update`. [#2060](https://github.com/pdm-project/pdm/issues/2060)
- Fix a bug that `pdm install --plugins` can't install self. [#2062](https://github.com/pdm-project/pdm/issues/2062)
- Fix a cache collision between named requirements and url requirements. [#2064](https://github.com/pdm-project/pdm/issues/2064)

## Release v2.8.0a1 (2023-06-27)

### Features & Improvements

- Add support for `cookiecutter` and `copier` as project generator. [#2059](https://github.com/pdm-project/pdm/issues/2059)

## Release v2.8.0a0 (2023-06-27)

### Features & Improvements

- `pdm init` now accepts a template argument to initialize project from a built-in or Git template. [#2053](https://github.com/pdm-project/pdm/issues/2053)
- Replace the `DeprecationWarning` with `FutureWarning` for better exposure. [#2012](https://github.com/pdm-project/pdm/issues/2012)
- Serve `install-pdm.py` and its checksum file on the docs site. [#2026](https://github.com/pdm-project/pdm/issues/2026)
- Add new option `--edit/-e` to `pdm config` to edit the config file in default editor. [#2028](https://github.com/pdm-project/pdm/issues/2028)
- Add `--project` option to `pdm venv` to support another path as the project root. [#2042](https://github.com/pdm-project/pdm/issues/2042)
- Add support for using `truststore` as the SSL backend. This only works on Python 3.10 or newer. [#2049](https://github.com/pdm-project/pdm/issues/2049)

### Bug Fixes

- Fix the breaking change by adding the functions back to the old location with deprecation warnings. [#2013](https://github.com/pdm-project/pdm/issues/2013)
- Fix the duplicate entries in the output of `pdm self list`. [#2018](https://github.com/pdm-project/pdm/issues/2018)
- Disable hashes caching for local files. [#2019](https://github.com/pdm-project/pdm/issues/2019)
- Populate the `url` field when converting requirements from a Pipfile-style file requirement. [#2032](https://github.com/pdm-project/pdm/issues/2032)
- Fix a bug that empty source tables in configuration files causes errors when running pdm commands. [#2034](https://github.com/pdm-project/pdm/issues/2034)
- Fix a resolution conflict caused by requested yanked version also in other transitive dependencies. [#2038](https://github.com/pdm-project/pdm/issues/2038)
- Fix a bug that binary executables are corrupted when replacing shebangs. [#2045](https://github.com/pdm-project/pdm/issues/2045)
- Do not normalize the package name when uploading to PyPI. [#2057](https://github.com/pdm-project/pdm/issues/2057)

## Release v2.7.4 (2023-06-13)

No significant changes.

## Release v2.7.3 (2023-06-13)

### Bug Fixes

- Fix the warning of extras not found due to extra names not normalized. [#2006](https://github.com/pdm-project/pdm/issues/2006)
- Pop up a warning when the deprecated `parser` argument is passed to `BaseCommand.__init__()` method. [#2007](https://github.com/pdm-project/pdm/issues/2007)
- Fix a bug that merging settings with AoTs causing a failure. [#2011](https://github.com/pdm-project/pdm/issues/2011)

## Release v2.7.2 (2023-06-12)

### Features & Improvements

- Add option to expand environment variables when exporting requirements. [#1997](https://github.com/pdm-project/pdm/issues/1997)

### Bug Fixes

- Case-insensitive sorting in `pdm list`. [#1973](https://github.com/pdm-project/pdm/issues/1973)
- Make a compatible cache reader to read the old cache files. [#1981](https://github.com/pdm-project/pdm/issues/1981)
- Fix a bug that `pdm init -n` doesn't respect the `--python` option. [#1984](https://github.com/pdm-project/pdm/issues/1984)
- Do not use the deprecated nested argument groups. [#1988](https://github.com/pdm-project/pdm/issues/1988)
- Fix an error parsing `setup.py` if it prints something to stdout. [#1995](https://github.com/pdm-project/pdm/issues/1995)
- Exclude yanked versions when running `install-pdm.py`. [#1996](https://github.com/pdm-project/pdm/issues/1996)

## Release v2.7.1 (2023-06-06)

### Features & Improvements

- Switch HTTP data cache to use a split body setup, where the actual body contents are not written to disk unless changed. Previously, any changed headers would write the whole body to disk again. [#1971](https://github.com/pdm-project/pdm/issues/1971)
- Show the specific install commands for different installations when checking update. This was removed before. [#1972](https://github.com/pdm-project/pdm/issues/1972)

### Bug Fixes

- PDM ignores env vars `PDM_PYPI_USERNAME` and `PDM_PYPI_PASSWORD` when there are no defaults in config. [#1961](https://github.com/pdm-project/pdm/issues/1961)
- Guess the project name from VCS url if it is missing when importing from requirements.txt. [#1970](https://github.com/pdm-project/pdm/issues/1970)
- Correctly read the config from environment variables. [#1977](https://github.com/pdm-project/pdm/issues/1977)

## Release v2.7.0 (2023-05-29)

### Features & Improvements

- When keyring is available, either by importing or by CLI, the credentials of repositories and PyPI indexes will be saved into it. [#1908](https://github.com/pdm-project/pdm/issues/1908)
- Add support for reading metadata from simple index directly. [#1919](https://github.com/pdm-project/pdm/issues/1919)
- Add a configuration to specify constant command arguments for every pdm invocation. [#1923](https://github.com/pdm-project/pdm/issues/1923)
- Add ability to skip SSL verification for publish repositories via `repository.custom.verify_ssl` config option as well as new command line argument of `publish` command. [#1928](https://github.com/pdm-project/pdm/issues/1928)
- Use lazy import to reduce the startup time of the CLI. [#1929](https://github.com/pdm-project/pdm/issues/1929)
- Add the local plugin scripts to `PATH` env var. [#1944](https://github.com/pdm-project/pdm/issues/1944)

### Bug Fixes

- Don't use install cache when installing build requirements to avoid race condition. [#1869](https://github.com/pdm-project/pdm/issues/1869)
- Fix a number of `ResourceWarning`s when running the test suite with warnings enabled. [#1915](https://github.com/pdm-project/pdm/issues/1915)
- Fix a bug that dev-dependencies group gets updated with the optional dependencies, causing the hash mismatch. [#1916](https://github.com/pdm-project/pdm/issues/1916)
- Fix format conversion error from Poetry when `tool.poetry.build` doesn't exist. [#1935](https://github.com/pdm-project/pdm/issues/1935)
- Add timeout when fetching .gitignore from GitHub. [#1937](https://github.com/pdm-project/pdm/issues/1937)
- Keep the variables in the URL credentials when exporting. [#1939](https://github.com/pdm-project/pdm/issues/1939)
- Convert to boolean when setting verify_ssl for custom indexes. [#1945](https://github.com/pdm-project/pdm/issues/1945)
- `pdm import` clobbers `build-system.requires` value in `pyproject.toml`. [#1948](https://github.com/pdm-project/pdm/issues/1948)

### Documentation

- Update publish.md to use run instead of runs to match GitHub Actions steps documentation [#1936](https://github.com/pdm-project/pdm/issues/1936)
- Update advanced.md to use `pdm sync` instead of `pdm install --no-lock`. [#1947](https://github.com/pdm-project/pdm/issues/1947)

## Release v2.6.1 (2023-05-10)

### Bug Fixes

- Fix the error when publishing using trusted publisher. [#1868](https://github.com/pdm-project/pdm/issues/1868)
- Fix a bug that `PATH` env var isn't set correctly when running under non-isolation mode. [#1904](https://github.com/pdm-project/pdm/issues/1904)

## Release v2.6.0 (2023-05-09)

### Features & Improvements

- Install project-level plugins from project config, with `tool.pdm.plugins` setting. [#1461](https://github.com/pdm-project/pdm/issues/1461)
- Added a `--json` flag to both `run` and `info` command allowing to dump scripts and infos as JSON. [#1854](https://github.com/pdm-project/pdm/issues/1854)
- Consider tasks with a name starting by an underscore (`_`) as internal tasks and hide them from the listing. [#1855](https://github.com/pdm-project/pdm/issues/1855)
- When running `pdm init -n`(non-interactive mode), a venv will be created by default. Previously, the selected Python will be used under PEP 582 mode. [#1862](https://github.com/pdm-project/pdm/issues/1862)
- Support [Trusted Publisher](https://docs.pypi.org/trusted-publishers/). [#1868](https://github.com/pdm-project/pdm/issues/1868)
- Add an ephemeral wheel cache in process for wheels built from non-static revision sources. [#1885](https://github.com/pdm-project/pdm/issues/1885)
- Allow self-referencing groups in dev-dependencies. [#1890](https://github.com/pdm-project/pdm/issues/1890)
- Add an option `--no-cross-platform` to `pdm lock` to create a non-cross-platform lockfile. [#1898](https://github.com/pdm-project/pdm/issues/1898)

### Bug Fixes

- Fix brackets in `--venv` option descriptions in zsh completion script. [#1847](https://github.com/pdm-project/pdm/issues/1847)
- The resolver doesn't take into account of the requirements for both bare `package` and `package[extra]`. [#1851](https://github.com/pdm-project/pdm/issues/1851)
- Default pypi source does not use configured pypi.password, but "" instead. [#1856](https://github.com/pdm-project/pdm/issues/1856)
- Detect Python interpreters under the root of virtual environments. [#1866](https://github.com/pdm-project/pdm/issues/1866)
- Fix a race condition when the builder is creating a new build directory. [#1869](https://github.com/pdm-project/pdm/issues/1869)
- Raise `FileNotFoundError` if the requirement path is not found. [#1875](https://github.com/pdm-project/pdm/issues/1875)
- Fix a bug that the self package isn't uninstallable. [#1901](https://github.com/pdm-project/pdm/issues/1901)

## Release v2.5.6 (2023-05-07)

### Bug Fixes

- Fix a double reading issue due to cachecontrol not compatible with urllib3 2.0. [#1894](https://github.com/pdm-project/pdm/issues/1894)

## Release v2.5.5 (2023-05-05)

No significant changes.

## Release v2.5.4 (2023-05-05)

### Bug Fixes

- Pin the urllib3 to `<2.0` to avoid incompatibility with `cachecontrol`. [#1886](https://github.com/pdm-project/pdm/issues/1886)

## Release v2.5.3 (2023-04-19)

### Bug Fixes

- Fix the wrong argument validation for update command, where packages given with group option should be allowed. [#1836](https://github.com/pdm-project/pdm/issues/1836)

### Documentation

- Update `markdown-exec` to `1.5.0` for rendering TOC in CLI reference page. [#1836](https://github.com/pdm-project/pdm/issues/1836)
- Remove advertizing of PEP-582 from the feature highlights. Improve the anchor links for CLI reference. [#1840](https://github.com/pdm-project/pdm/issues/1840)

## Release v2.5.2 (2023-04-10)

### Bug Fixes

- Regression(#1710): Don't crash when trying to update the shebang in a binary script [#1827](https://github.com/pdm-project/pdm/issues/1827)
- Rename the env var `PDM_USE_VENV` as `PDM_IN_VENV` for `--venv` flag as it mistakenly override another existing env var. [#1829](https://github.com/pdm-project/pdm/issues/1829)

## Release v2.5.1 (2023-04-09)

### Bug Fixes

- Fix a bug that `pdm --pep582` raises an argument error. [#1823](https://github.com/pdm-project/pdm/issues/1823)

## Release v2.5.0 (2023-04-09)

### Features & Improvements

- When `resolution.respect-source-order` is enabled, sources are lazily evaluated. This means that if a match is found on the first source, the remaining sources will not be requested. [#1509](https://github.com/pdm-project/pdm/issues/1509)
- New option `--venv <venv>` to run a command in the virtual environment with the given name. [#1705](https://github.com/pdm-project/pdm/issues/1705)
- Allow to prefer binary distributions when locking and installing packages, via `PDM_PREFER_BINARY` environment variable. [#1817](https://github.com/pdm-project/pdm/issues/1817)

### Bug Fixes

- Do not validate selected groups against the locked grouped when running `pdm lock`. [#1796](https://github.com/pdm-project/pdm/issues/1796)
- Avoid duplicate .pdm-python in .gitignore. [#1800](https://github.com/pdm-project/pdm/issues/1800)
- Fix a backwards compatibility issue by adding back the `environment.is_global` property. [#1814](https://github.com/pdm-project/pdm/issues/1814)
- Fix a resolution conflict when a relative path requirement resolves to the same path as another file requirement with absolute path. [#1822](https://github.com/pdm-project/pdm/issues/1822)
- Fix an error when running `pdm init -p <dir>` if the target directory is not created yet. [#1822](https://github.com/pdm-project/pdm/issues/1822)

## Release v2.5.0b0 (2023-03-29)

### Breaking Changes

- Switch the default build backend to `pdm-backend`. [#1684](https://github.com/pdm-project/pdm/issues/1684)
- Only lock selected groups into the lockfile. Modify other commands to honor the groups included in the lockfile. [#1704](https://github.com/pdm-project/pdm/issues/1704)
- Move the project python path to its own file, and rename the project config file as `pdm.toml` which can be committed to the VCS. [#1742](https://github.com/pdm-project/pdm/issues/1742)
- Refactor the environment package. `Environment` is renamed to `PythonLocalEnvironment` and `GlobalEnvironment` is renamed to `PythonEnvironment`. Move `pdm.models.environment` module to `pdm.environments` package. [#1791](https://github.com/pdm-project/pdm/issues/1791)

### Features & Improvements

- Add option to fail on the first install error. [#1614](https://github.com/pdm-project/pdm/issues/1614)
- Upgrade `unearth` to 0.8 to allow calling keyring from CLI. [#1653](https://github.com/pdm-project/pdm/issues/1653)
- Merge the index parameters from different configuration files. [#1667](https://github.com/pdm-project/pdm/issues/1667)
- Add new options to `venv` command to show the path or the python interpreter for a managed venv. [#1680](https://github.com/pdm-project/pdm/issues/1680)
- Write the groups of resolved dependencies to the metadata table in lockfile. [#1692](https://github.com/pdm-project/pdm/issues/1692)
- Introduce `--lib` option to `init` command to create a library project without prompting. [#1708](https://github.com/pdm-project/pdm/issues/1708)
- New command: `pdm fix` to migrate to the new PDM features. Add a hint when invoking PDM commands. [#1743](https://github.com/pdm-project/pdm/issues/1743)
- Include `.pdm-python` in project root `.gitignore` when running `pdm init`. [#1749](https://github.com/pdm-project/pdm/issues/1749)
- Allow to ignore the activated venv with `PDM_IGNORE_ACTIVE_VENV` env var. [#1782](https://github.com/pdm-project/pdm/issues/1782)
- Add a signal `pre_invoke` to emit before any command is invoked. [#1792](https://github.com/pdm-project/pdm/issues/1792)

### Bug Fixes

- Fix a bug that install warning prints to terminal under non-verbose mode. [#1635](https://github.com/pdm-project/pdm/issues/1635)
- Fix the random failure of `pdm export` due to non-deterministic order of group iteration. [#1786](https://github.com/pdm-project/pdm/issues/1786)
- Show the actual version when running `pdm show --version` [#1788](https://github.com/pdm-project/pdm/issues/1788)

### Documentation

- Restructure the documentation. [#1687](https://github.com/pdm-project/pdm/issues/1687)

### Dependencies

- Update `installer` to `0.7.0` and emit a warning if the RECORD validation fails. [#1784](https://github.com/pdm-project/pdm/issues/1784)

## Release v2.4.9 (2023-03-16)

### Bug Fixes

- Fix a bug of synchronization of not considering the revision of VCS requirement in comparison. [#1762](https://github.com/pdm-project/pdm/issues/1762)
- Improve the error message when parsing an invalid requirement string. [#1765](https://github.com/pdm-project/pdm/issues/1765)
- Fix a bug that `pdm export` output doesn't include the extras of the dependencies. [#1767](https://github.com/pdm-project/pdm/issues/1767)

## Release v2.4.8 (2023-03-09)

### Bug Fixes

- Fix the resolution order to prefer the packages causing the conflict. This can make the resolution reach a solution faster. [#1752](https://github.com/pdm-project/pdm/issues/1752)
- Fix a bug that embedded credentials in URL are not respected for the default source. [#1757](https://github.com/pdm-project/pdm/issues/1757)

## Release v2.4.7 (2023-03-02)

### Bug Fixes

- Abort if lockfile isn't generated when executing `pdm export`. [#1730](https://github.com/pdm-project/pdm/issues/1730)
- Ignore `venv.prompt` configuration when using `conda` as the backend. [#1734](https://github.com/pdm-project/pdm/issues/1734)
- Fix a bug of finding local packages in the parent folder when it exists in the current folder. [#1736](https://github.com/pdm-project/pdm/issues/1736)
- Ensure UTF-8 encoding when generating README.md. [#1739](https://github.com/pdm-project/pdm/issues/1739)
- Fix a bug of show command not showing metadata of the current project. [#1740](https://github.com/pdm-project/pdm/issues/1740)
- Replace `.` with `-` when normalizing package name. [#1745](https://github.com/pdm-project/pdm/issues/1745)

### Documentation

- Support using `pdm venv activate` without specifying `env_name` to activate in project venv created by conda [#1735](https://github.com/pdm-project/pdm/issues/1735)

## Release v2.4.6 (2023-02-20)

### Bug Fixes

- Fix a resolution failure when the project has cascading relative path dependencies. [#1702](https://github.com/pdm-project/pdm/issues/1702)
- Don't crash when trying to update the shebang in a binary script. [#1709](https://github.com/pdm-project/pdm/issues/1709)
- Handle the legacy specifiers that is unable to parse with packaging>22.0. [#1719](https://github.com/pdm-project/pdm/issues/1719)
- Fix the setup.py parser to ignore the expressions unable to parse as a string. This is safe for initializing a requirement. [#1720](https://github.com/pdm-project/pdm/issues/1720)
- Fix a bug converting from flit metadata when the source file can't be found. [#1726](https://github.com/pdm-project/pdm/issues/1726)

### Documentation

- Add config example for Emacs using eglot + pyright [#1721](https://github.com/pdm-project/pdm/issues/1721)

### Miscellany

- Use `ruff` as the linter. [#1715](https://github.com/pdm-project/pdm/issues/1715)
- Document installation via `asdf`. [#1725](https://github.com/pdm-project/pdm/issues/1725)

## Release v2.4.5 (2023-02-10)

### Bug Fixes

- Fix a bug that built wheels are prioritized over source distributions with higher version number. [#1698](https://github.com/pdm-project/pdm/issues/1698)

## Release v2.4.4 (2023-02-10)

### Features & Improvements

- Add more intuitive error message when the `requires-python` doesn't work for all dependencies. [#1690](https://github.com/pdm-project/pdm/issues/1690)

### Bug Fixes

- Prefer built distributions when finding packages for metadata extraction. [#1535](https://github.com/pdm-project/pdm/issues/1535)

## Release v2.4.3 (2023-02-06)

### Features & Improvements

- Allow creating venv in project forcibly if it already exists. [#1666](https://github.com/pdm-project/pdm/issues/1666)
- Always ignore remembered selection in pdm init. [#1672](https://github.com/pdm-project/pdm/issues/1672)

### Bug Fixes

- Fix the fallback build backend to `pdm-pep517` instead of `setuptools`. [#1658](https://github.com/pdm-project/pdm/issues/1658)
- Eliminate the deprecation warnings from `importlib.resources`. [#1660](https://github.com/pdm-project/pdm/issues/1660)
- Don't crash when failed to get the latest version of PDM for checking update. [#1663](https://github.com/pdm-project/pdm/issues/1663)
- Fix the priorities of importable formats to make sure the correct format is used. [#1669](https://github.com/pdm-project/pdm/issues/1669)
- Import editable requirements into dev dependencies. [#1674](https://github.com/pdm-project/pdm/issues/1674)

## Release v2.4.2 (2023-01-31)

### Bug Fixes

- Skip some tests on packaging < 22. [#1649](https://github.com/pdm-project/pdm/issues/1649)
- Fix a bug that sources from the project config are not loaded. [#1651](https://github.com/pdm-project/pdm/issues/1651)
- Set VIRTUAL_ENV in `pdm run`. [#1652](https://github.com/pdm-project/pdm/issues/1652)

## Release v2.4.1 (2023-01-28)

### Features & Improvements

- Add proper display for the extra pypi sources in `pdm config`. [#1622](https://github.com/pdm-project/pdm/issues/1622)
- Support running python scripts without prefixing with `python`. [#1626](https://github.com/pdm-project/pdm/issues/1626)

### Bug Fixes

- Ignore the python requirement for overridden packages. [#1575](https://github.com/pdm-project/pdm/issues/1575)
- Fix the wildcards in requirement specifiers to make it pass the new parser of `packaging>=22`. [#1619](https://github.com/pdm-project/pdm/issues/1619)
- Add the missing `subdirectory` attribute to the lockfile entry. [#1630](https://github.com/pdm-project/pdm/issues/1630)
- Fix a bug that VCS locks don't update when the rev part changes. [#1640](https://github.com/pdm-project/pdm/issues/1640)
- Redirect the spinner output to stderr. [#1646](https://github.com/pdm-project/pdm/issues/1646)
- Ensure the destination directory exists before building the packages. [#1647](https://github.com/pdm-project/pdm/issues/1647)

## Release v2.4.0 (2023-01-12)

### Features & Improvements

- Support multiple PyPI indexes in the configuration. They will be tried after the sources in `pyproject.toml`. [#1310](https://github.com/pdm-project/pdm/issues/1310)
- Accept yanked versions when the requirement version is pinned. [#1575](https://github.com/pdm-project/pdm/issues/1575)
- Expose PDM fixtures as a `pytest` plugin `pdm.pytest` for plugin developers. [#1594](https://github.com/pdm-project/pdm/issues/1594)
- Show message in the status when fetching package hashes. Fetch hashes from the JSON API response as well. [#1609](https://github.com/pdm-project/pdm/issues/1609)
- Mark `pdm.lock` with an `@generated` comment. [#1611](https://github.com/pdm-project/pdm/issues/1611)

### Bug Fixes

- Exclude site-packages for symlinks of the python interpreter as well. [#1598](https://github.com/pdm-project/pdm/issues/1598)
- Fix a bug that error output can't be decoded correctly on Windows. [#1602](https://github.com/pdm-project/pdm/issues/1602)

## Release v2.3.4 (2022-12-27)

### Features & Improvements

- Detect PDM inside a zipapp and disable some functions. [#1578](https://github.com/pdm-project/pdm/issues/1578)

### Bug Fixes

- Don't write `sitecustomize` to the home directory if it exists in the filesystem(not packed in a zipapp). [#1572](https://github.com/pdm-project/pdm/issues/1572)
- Fix a bug that a directory is incorrectly marked as to be deleted when it contains symlinks. [#1580](https://github.com/pdm-project/pdm/issues/1580)

## Release v2.3.3 (2022-12-15)

### Bug Fixes

- Allow relative paths in `build-system.requires`, since `build` and `hatch` both support it. Be aware it is not allowed in the standard. [#1560](https://github.com/pdm-project/pdm/issues/1560)
- Strip the local part when building a specifier for comparison with the package version. This is not permitted by PEP 508 as implemented by `packaging 22.0`. [#1562](https://github.com/pdm-project/pdm/issues/1562)
- Update the version for check_update after self update [#1563](https://github.com/pdm-project/pdm/issues/1563)
- Replace the `__file__` usages with `importlib.resources`, to make PDM usable in a zipapp. [#1567](https://github.com/pdm-project/pdm/issues/1567)
- Fix the matching problem of packages in the lockfile. [#1569](https://github.com/pdm-project/pdm/issues/1569)

### Dependencies

- Exclude `package==22.0` from the dependencies to avoid some breakages to the end users. [#1568](https://github.com/pdm-project/pdm/issues/1568)

## Release v2.3.2 (2022-12-08)

### Bug Fixes

- Fix an installation failure when the RECORD file contains commas in the file path. [#1010](https://github.com/pdm-project/pdm/issues/1010)
- Fallback to `pdm.pep517` as the metadata transformer for unknown custom build backends. [#1546](https://github.com/pdm-project/pdm/issues/1546)
- Fix a bug that Ctrl + C kills the python interactive session instead of clearing the current line. [#1547](https://github.com/pdm-project/pdm/issues/1547)
- Fix a bug with egg segment for local dependency [#1552](https://github.com/pdm-project/pdm/issues/1552)

### Dependencies

- Update `installer` to `0.6.0`. [#1550](https://github.com/pdm-project/pdm/issues/1550)
- Update minimum version of `unearth` to `0.6.3` and test against `packaging==22.0`. [#1555](https://github.com/pdm-project/pdm/issues/1555)

## Release v2.3.1 (2022-12-05)

### Bug Fixes

- Fix a resolution loop issue when the current project depends on itself and it uses the dynamic version from SCM. [#1541](https://github.com/pdm-project/pdm/issues/1541)
- Don't give duplicate results when specifying a relative path for `pdm use`. [#1542](https://github.com/pdm-project/pdm/issues/1542)

## Release v2.3.0 (2022-12-02)

### Features & Improvements

- Beautify the error message of build errors. Default to showing the last 10 lines of the build output. [#1491](https://github.com/pdm-project/pdm/issues/1491)
- Rename the `tool.pdm.overrides` table to `tool.pdm.resolution.overrides`. The old name is deprecated at the same time. [#1503](https://github.com/pdm-project/pdm/issues/1503)
- Add backend selection and `--backend` option to `pdm init` command, users can choose a favorite backend from `setuptools`, `flit`, `hatchling` and `pdm-pep517`(default), since they all support PEP 621 standards. [#1504](https://github.com/pdm-project/pdm/issues/1504)
- Allows specifying the insertion position of user provided arguments in scripts with the `{args[:default]}` placeholder. [#1507](https://github.com/pdm-project/pdm/issues/1507)

### Bug Fixes

- The local package is now treated specially during installation and locking. This means it will no longer be included in the lockfile, and should never be installed twice even when using nested extras. This will ensure the lockdown stays relevant when the version changes. [#1481](https://github.com/pdm-project/pdm/issues/1481)
- Fix the version diff algorithm of installed packages to consider local versions as compatible. [#1497](https://github.com/pdm-project/pdm/issues/1497)
- Fix the confusing message when detecting a Python interpreter under `python.use_venv=False` [#1508](https://github.com/pdm-project/pdm/issues/1508)
- Fix the test failure with the latest `findpython` installed. [#1516](https://github.com/pdm-project/pdm/issues/1516)
- Fix the module missing error of pywin32 in a virtualenv with `install.cache` set to `true` and caching method is `pth`. [#863](https://github.com/pdm-project/pdm/issues/863)

### Dependencies

- Drop the dependency `pdm-pep517`. [#1504](https://github.com/pdm-project/pdm/issues/1504)
- Replace `pep517` with `pyproject-hooks` because of the rename. [#1528](https://github.com/pdm-project/pdm/issues/1528)

### Removals and Deprecations

- Remove the support for exporting the project file to a `setup.py` format, users are encouraged to migrate to the PEP 621 metadata. [#1504](https://github.com/pdm-project/pdm/issues/1504)

## Release v2.2.1 (2022-11-03)

### Features & Improvements

- Make `sitecustomize.py` respect the `PDM_PROJECT_MAX_DEPTH` environment variable [#1471](https://github.com/pdm-project/pdm/issues/1471)

### Bug Fixes

- Fix the comparison of `python_version` in the environment marker. When the version contains only one digit, the result was incorrect. [#1484](https://github.com/pdm-project/pdm/issues/1484)

## Release v2.2.0 (2022-10-31)

### Features & Improvements

- Add `venv.prompt` configuration to allow customizing prompt when a virtualenv is activated [#1332](https://github.com/pdm-project/pdm/issues/1332)
- Allow the use of custom CA certificates per publish repository using `ca_certs` or from the command line via `pdm publish --ca-certs <path> ...`. [#1392](https://github.com/pdm-project/pdm/issues/1392)
- Rename the `plugin` command to `self`, and it can not only manage plugins but also all dependencies. Add a subcommand `self update` to update PDM itself. [#1406](https://github.com/pdm-project/pdm/issues/1406)
- Allow `pdm init` to receive a Python path or version via `--python` option. [#1412](https://github.com/pdm-project/pdm/issues/1412)
- Add a default value for `requires-python` when importing from other formats. [#1426](https://github.com/pdm-project/pdm/issues/1426)
- Use `pdm` instead of `pip` to resolve and install build requirements. So that PDM configurations can control the process. [#1429](https://github.com/pdm-project/pdm/issues/1429)
- Customizable color theme via `pdm config` command. [#1450](https://github.com/pdm-project/pdm/issues/1450)
- A new `pdm lock --check` flag to validate whether the lock is up to date. [#1459](https://github.com/pdm-project/pdm/issues/1459)
- Add both option and config item to ship `pip` when creating a new venv. [#1463](https://github.com/pdm-project/pdm/issues/1463)
- Issue warning and skip the requirement if it has the same name as the current project. [#1466](https://github.com/pdm-project/pdm/issues/1466)
- Enhance the `pdm list` command with new formats: `--csv,--markdown` and add options `--fields,--sort` to control the output contents. Users can also include `licenses` in the `--fields` option to display the package licenses. [#1469](https://github.com/pdm-project/pdm/issues/1469)
- A new pre-commit hook to run `pdm lock --check` in pre-commit. [#1471](https://github.com/pdm-project/pdm/issues/1471)

### Bug Fixes

- Fix the issue that relative paths don't work well with `--project` argument. [#1220](https://github.com/pdm-project/pdm/issues/1220)
- It is now possible to refer to a package from outside the project with relative paths in dependencies. [#1381](https://github.com/pdm-project/pdm/issues/1381)
- Ensure `pypi.[ca,client]_cert[s]` config items are passed to distribution builder install steps to allow for custom PyPI index sources with self signed certificates. [#1396](https://github.com/pdm-project/pdm/issues/1396)
- Fix a crash issue when depending on editable packages with extras. [#1401](https://github.com/pdm-project/pdm/issues/1401)
- Do not save the python path when using non-interactive mode in `pdm init`. [#1410](https://github.com/pdm-project/pdm/issues/1410)
- Fix the matching of `python*` command in `pdm run`. [#1414](https://github.com/pdm-project/pdm/issues/1414)
- Show the Python path, instead of the real executable, in the Python selection menu. [#1418](https://github.com/pdm-project/pdm/issues/1418)
- Fix the HTTP client of package publishment to prompt for password and read PDM configurations correctly. [#1430](https://github.com/pdm-project/pdm/issues/1430)
- Ignore the unknown fields when constructing a requirement object. [#1445](https://github.com/pdm-project/pdm/issues/1445)
- Fix a bug of unrelated candidates being fetched if the requirement is matching wildcard versions(e.g. `==1.*`). [#1465](https://github.com/pdm-project/pdm/issues/1465)
- Use `importlib-metadata` from PyPI for Python < 3.10. [#1467](https://github.com/pdm-project/pdm/issues/1467)

### Documentation

- Clarify the difference between a library and an application. Update the guide of multi-stage docker build. [#1371](https://github.com/pdm-project/pdm/issues/1371)

### Removals and Deprecations

- Remove all top-level imports, users should import from the submodules instead. [#1404](https://github.com/pdm-project/pdm/issues/1404)
- Remove the usages of old config names deprecated since 2.0. [#1422](https://github.com/pdm-project/pdm/issues/1422)
- Remove the deprecated color functions, use [rich's console markup](https://rich.readthedocs.io/en/latest/markup.html) instead. [#1452](https://github.com/pdm-project/pdm/issues/1452)

## Release v2.1.5 (2022-10-05)

### Bug Fixes

- Ensure `pypi.[ca,client]_cert[s]` config items are passed to distribution builder install steps to allow for custom PyPI index sources with self signed certificates. [#1396](https://github.com/pdm-project/pdm/issues/1396)
- Fix a crash issue when depending on editable packages with extras. [#1401](https://github.com/pdm-project/pdm/issues/1401)
- Do not save the python path when using non-interactive mode in `pdm init`. [#1410](https://github.com/pdm-project/pdm/issues/1410)
- Restrict importlib-metadata (\<5.0.0) for Python \<3.8 [#1411](https://github.com/pdm-project/pdm/issues/1411)

## Release v2.1.4 (2022-09-17)

### Bug Fixes

- Fix a lock failure when depending on self with URL requirements. [#1347](https://github.com/pdm-project/pdm/issues/1347)
- Ensure list to concatenate args for composite scripts. [#1359](https://github.com/pdm-project/pdm/issues/1359)
- Fix an error in `pdm lock --refresh` if some packages has URLs. [#1361](https://github.com/pdm-project/pdm/issues/1361)
- Fix unnecessary package downloads and VCS clones for certain commands. [#1370](https://github.com/pdm-project/pdm/issues/1370)
- Fix a conversion error when converting a list of conditional dependencies from a Poetry format. [#1383](https://github.com/pdm-project/pdm/issues/1383)

### Documentation

- Adds a section to the docs on how to correctly work with PDM and version control systems. [#1364](https://github.com/pdm-project/pdm/issues/1364)

## Release v2.1.3 (2022-08-30)

### Features & Improvements

- When adding a package to (or removing from) a group, enhance the formatting of the group name in the printed message. [#1329](https://github.com/pdm-project/pdm/issues/1329)

### Bug Fixes

- Fix a bug of missing hashes for packages with `file://` links the first time they are added. [#1325](https://github.com/pdm-project/pdm/issues/1325)
- Ignore invalid values of `data-requires-python` when parsing package links. [#1334](https://github.com/pdm-project/pdm/issues/1334)
- Leave an incomplete project metadata if PDM fails to parse the project files, but emit a warning. [#1337](https://github.com/pdm-project/pdm/issues/1337)
- Fix the bug that `editables` package isn't installed for self package. [#1344](https://github.com/pdm-project/pdm/issues/1344)
- Fix a decoding error for non-ASCII characters in package description when publishing it. [#1345](https://github.com/pdm-project/pdm/issues/1345)

### Documentation

- Clarify documentation explaining `setup-script`, `run-setuptools`, and `is-purelib`. [#1327](https://github.com/pdm-project/pdm/issues/1327)

## Release v2.1.2 (2022-08-15)

### Bug Fixes

- Fix a bug that dependencies from different versions of the same package override each other. [#1307](https://github.com/pdm-project/pdm/issues/1307)
- Forward SIGTERM to child processes in `pdm run`. [#1312](https://github.com/pdm-project/pdm/issues/1312)
- Fix errors when running on FIPS 140-2 enabled systems using Python 3.9 and newer. [#1313](https://github.com/pdm-project/pdm/issues/1313)
- Fix the build failure when the subprocess outputs with non-UTF8 characters. [#1319](https://github.com/pdm-project/pdm/issues/1319)
- Delay the trigger of `post_lock` for `add` and `update` operations, to ensure the `pyproject.toml` is updated before the hook is run. [#1320](https://github.com/pdm-project/pdm/issues/1320)

## Release v2.1.1 (2022-08-05)

### Features & Improvements

- Add a env_file.override option that allows the user to specify that the env_file should override any existing environment variables. This is not the default as the environment the code runs it should take precedence. [#1299](https://github.com/pdm-project/pdm/issues/1299)

### Bug Fixes

- Fix a bug that unnamed requirements can't override the old ones in either `add` or `update` command. [#1287](https://github.com/pdm-project/pdm/issues/1287)
- Support mutual TLS to private repositories via pypi.client_cert and pypi.client_key config options. [#1290](https://github.com/pdm-project/pdm/issues/1290)
- Set a minimum version for the `packaging` dependency to ensure that `packaging.utils.parse_wheel_filename` is available. [#1293](https://github.com/pdm-project/pdm/issues/1293)
- Fix a bug that checking for PDM update creates a venv. [#1301](https://github.com/pdm-project/pdm/issues/1301)
- Prefer compatible packages when fetching metadata. [#1302](https://github.com/pdm-project/pdm/issues/1302)

## Release v2.1.0 (2022-07-29)

### Features & Improvements

- Allow the use of custom CA certificates using the `pypi.ca_certs` config entry. [#1240](https://github.com/pdm-project/pdm/issues/1240)
- Add `pdm export` to available pre-commit hooks. [#1279](https://github.com/pdm-project/pdm/issues/1279)

### Bug Fixes

- Skip incompatible requirements when installing build dependencies. [#1264](https://github.com/pdm-project/pdm/issues/1264)
- Fix a crash when pdm tries to publish a package with non-ASCII characters in the metadata. [#1270](https://github.com/pdm-project/pdm/issues/1270)
- Try to read the lock file even if the lock version is incompatible. [#1273](https://github.com/pdm-project/pdm/issues/1273)
- For packages that are only available as source distribution, the `summary` field in `pdm.lock` contains the `description` from the package's `pyproject.toml`. [#1274](https://github.com/pdm-project/pdm/issues/1274)
- Do not crash when calling `pdm show` for a package that is only available as source distribution. [#1276](https://github.com/pdm-project/pdm/issues/1276)
- Fix a bug that completion scripts are interpreted as rich markups. [#1283](https://github.com/pdm-project/pdm/issues/1283)

### Dependencies

- Remove the dependency of `pip`. [#1268](https://github.com/pdm-project/pdm/issues/1268)

### Removals and Deprecations

- Deprecate the top-level imports from `pdm` module, it will be removed in the future. [#1282](https://github.com/pdm-project/pdm/issues/1282)

## Release v2.0.3 (2022-07-22)

### Bug Fixes

- Support Conda environments when detecting the project environment. [#1253](https://github.com/pdm-project/pdm/issues/1253)
- Fix the interpreter resolution to first try `python` executable in the `PATH`. [#1255](https://github.com/pdm-project/pdm/issues/1255)
- Stabilize sorting of URLs in `metadata.files` in `pdm.lock`. [#1256](https://github.com/pdm-project/pdm/issues/1256)
- Don't expand credentials in the file URLs in the `[metadata.files]` table of the lock file. [#1259](https://github.com/pdm-project/pdm/issues/1259)

## Release v2.0.2 (2022-07-20)

### Features & Improvements

- `env_file` variables no longer override existing environment variables. [#1235](https://github.com/pdm-project/pdm/issues/1235)
- Support referencing other optional groups in optional-dependencies with `<this_package_name>[group1, group2]` [#1241](https://github.com/pdm-project/pdm/issues/1241)

### Bug Fixes

- Respect `requires-python` when creating the default venv. [#1237](https://github.com/pdm-project/pdm/issues/1237)

## Release v2.0.1 (2022-07-17)

### Bug Fixes

- Write lockfile before calling 'post_lock' hook [#1224](https://github.com/pdm-project/pdm/issues/1224)
- Suppress errors when cache dir isn't accessible. [#1226](https://github.com/pdm-project/pdm/issues/1226)
- Don't save python path for venv commands. [#1230](https://github.com/pdm-project/pdm/issues/1230)

## Release v2.0.0 (2022-07-15)

### Bug Fixes

- Fix a bug that the running env overrides the PEP 582 `PYTHONPATH`. [#1211](https://github.com/pdm-project/pdm/issues/1211)
- Add [`pwsh`](https://github.com/PowerShell/PowerShell) as an alias of `powershell` for shell completion. [#1216](https://github.com/pdm-project/pdm/issues/1216)
- Fixed a bug with `zsh` completion regarding `--pep582` flag. [#1218](https://github.com/pdm-project/pdm/issues/1218)
- Fix a bug of requirement checking under non-isolated mode. [#1219](https://github.com/pdm-project/pdm/issues/1219)
- Fix a bug when removing packages, TOML document might become invalid. [#1221](https://github.com/pdm-project/pdm/issues/1221)

## Release v2.0.0b2 (2022-07-08)

### Breaking Changes

- Store file URLs instead of filenames in the lock file, bump lock version to `4.0`. [#1203](https://github.com/pdm-project/pdm/issues/1203)

### Features & Improvements

- Read site-wide configuration, which serves as the lowest-priority layer. This layer will be read-only in the CLI. [#1200](https://github.com/pdm-project/pdm/issues/1200)
- Get package links from the urls stored in the lock file. [#1204](https://github.com/pdm-project/pdm/issues/1204)

### Bug Fixes

- Fix a bug that the host pip(installed with pdm) may not be compatible with the project python. [#1196](https://github.com/pdm-project/pdm/issues/1196)
- Update `unearth` to fix a bug that install links with weak hashes are skipped. This often happens on self-hosted PyPI servers. [#1202](https://github.com/pdm-project/pdm/issues/1202)

## Release v2.0.0b1 (2022-07-02)

### Features & Improvements

- Integrate `pdm venv` commands into the main program. Make PEP 582 an opt-in feature. [#1162](https://github.com/pdm-project/pdm/issues/1162)
- Add config `global_project.fallback_verbose` defaulting to `True`. When set to `False` disables message `Project is not found, fallback to the global project` [#1188](https://github.com/pdm-project/pdm/issues/1188)
- Add `--only-keep` option to `pdm sync` to keep only selected packages. Originally requested at #398. [#1191](https://github.com/pdm-project/pdm/issues/1191)

### Bug Fixes

- Fix a bug that requirement extras and underlying are resolved to the different version [#1173](https://github.com/pdm-project/pdm/issues/1173)
- Update `unearth` to `0.4.1` to skip the wheels with invalid version parts. [#1178](https://github.com/pdm-project/pdm/issues/1178)
- Fix reading `PDM_RESOLVE_MAX_ROUNDS` environment variable (was spelled `…ROUDNS` before). [#1180](https://github.com/pdm-project/pdm/issues/1180)
- Deduplicate the list of found Python versions. [#1182](https://github.com/pdm-project/pdm/issues/1182)
- Use the normal stream handler for logging, to fix some display issues under non-tty environments. [#1184](https://github.com/pdm-project/pdm/issues/1184)

### Removals and Deprecations

- Remove the useless `--no-clean` option from `pdm sync` command. [#1191](https://github.com/pdm-project/pdm/issues/1191)

## Release v2.0.0a1 (2022-06-29)

### Breaking Changes

- Editable dependencies in the `[project]` table is not allowed, according to PEP 621. They are however still allowed in the `[tool.pdm.dev-dependencies]` table. PDM will emit a warning when it finds editable dependencies in the `[project]` table, or will abort when you try to add them into the `[project]` table via CLI. [#1083](https://github.com/pdm-project/pdm/issues/1083)
- Now the paths to the global configurations and global project are calculated according to platform standards. [#1161](https://github.com/pdm-project/pdm/issues/1161)

### Features & Improvements

- Add support for importing from a `setup.py` project. [#1062](https://github.com/pdm-project/pdm/issues/1062)
- Switch the UI backend to `rich`. [#1091](https://github.com/pdm-project/pdm/issues/1091)
- Improved the terminal UI and logging. Disable live progress under verbose mode. The logger levels can be controlled by the `-v` option. [#1096](https://github.com/pdm-project/pdm/issues/1096)
- Use `unearth` to replace `pip`'s `PackageFinder` and related data models. PDM no longer relies on `pip` internals, which are unstable across updates. [#1096](https://github.com/pdm-project/pdm/issues/1096)
- Lazily load the candidates returned by `find_matches()` to speed up the resolution. [#1098](https://github.com/pdm-project/pdm/issues/1098)
- Add a new command `publish` to PDM since it is required for so many people and it will make the workflow easier. [#1107](https://github.com/pdm-project/pdm/issues/1107)
- Add a `composite` script kind allowing to run multiple defined scripts in a single command as well as reusing scripts but overriding `env` or `env_file`. [#1117](https://github.com/pdm-project/pdm/issues/1117)
- Add a new execution option `--skip` to opt-out some scripts and hooks from any execution (both scripts and PDM commands). [#1127](https://github.com/pdm-project/pdm/issues/1127)
- Add the `pre/post_publish`, `pre/post_run` and `pre/post_script` hooks as well as an extensive lifecycle and hooks documentation. [#1147](https://github.com/pdm-project/pdm/issues/1147)
- Shorter scripts listing, especially for multilines and composite scripts. [#1151](https://github.com/pdm-project/pdm/issues/1151)
- Build configurations have been moved to `[tool.pdm.build]`, according to `pdm-pep517 1.0.0`. At the same time, warnings will be shown against old usages. [#1153](https://github.com/pdm-project/pdm/issues/1153)
- Improve the lock speed by parallelizing the hash fetching. [#1154](https://github.com/pdm-project/pdm/issues/1154)
- Retrieve the candidate metadata by parsing the `pyproject.toml` rather than building it. [#1156](https://github.com/pdm-project/pdm/issues/1156)
- Update the format converters to support the new `[tool.pdm.build]` table. [#1157](https://github.com/pdm-project/pdm/issues/1157)
- Scripts are now available as root command if they don't conflict with any builtin or plugin-contributed command. [#1159](https://github.com/pdm-project/pdm/issues/1159)
- Add a `post_use` hook triggered after successfully switching Python version. [#1163](https://github.com/pdm-project/pdm/issues/1163)
- Add project configuration `respect-source-order` under `[tool.pdm.resolution]` to respect the source order in the `pyproject.toml` file. Packages will be returned by source earlier in the order or later ones if not found. [#593](https://github.com/pdm-project/pdm/issues/593)

### Bug Fixes

- Fix a bug that candidates with local part in the version can't be found and installed correctly. [#1093](https://github.com/pdm-project/pdm/issues/1093)

### Dependencies

- Prefer `tomllib` on Python 3.11 [#1072](https://github.com/pdm-project/pdm/issues/1072)
- Drop the vendored libraries `click`, `halo`, `colorama` and `log_symbols`. PDM has no vendors now. [#1091](https://github.com/pdm-project/pdm/issues/1091)
- Update dependency version `pdm-pep517` to `1.0.0`. [#1153](https://github.com/pdm-project/pdm/issues/1153)

### Removals and Deprecations

- PDM legacy metadata format(from `pdm 0.x`) is no longer supported. [#1157](https://github.com/pdm-project/pdm/issues/1157)

### Miscellany

- Provide a `tox.ini` file for easier local testing against all Python versions. [#1160](https://github.com/pdm-project/pdm/issues/1160)

## Release v1.15.4 (2022-06-28)

### Bug Fixes

- Revert #1106: Do not use `venv` scheme for `prefix` kind install scheme. [#1158](https://github.com/pdm-project/pdm/issues/1158)
- Fix a bug when updating a package with extra requirements, the package version doesn't get updated correctly. [#1166](https://github.com/pdm-project/pdm/issues/1166)

### Miscellany

- Add additional installation option via [asdf-pdm](https://github.com/1oglop1/asdf-pdm). Add `skip-add-to-path` option to installer in order to prevent changing `PATH`. Replace `bin` variable name with `bin_dir`. [#1145](https://github.com/pdm-project/pdm/issues/1145)

## Release v1.15.3 (2022-06-14)

### Bug Fixes

- Fix a defect in the resolution preferences that causes an infinite resolution loop. [#1119](https://github.com/pdm-project/pdm/issues/1119)
- Update the poetry importer to support the new `[tool.poetry.build]` config table. [#1131](https://github.com/pdm-project/pdm/issues/1131)

### Improved Documentation

- Add support for multiple versions of documentations. [#1126](https://github.com/pdm-project/pdm/issues/1126)

## Release v1.15.2 (2022-06-06)

### Bug Fixes

- Fix bug where SIGINT is sent to the main `pdm` process and not to the process actually being run. [#1095](https://github.com/pdm-project/pdm/issues/1095)
- Fix a bug due to the build backend fallback, which causes different versions of the same requirement to exist in the build environment, making the building unstable depending on which version being used. [#1099](https://github.com/pdm-project/pdm/issues/1099)
- Don't include the `version` in the cache key of the locked candidates if they are from a URL requirement. [#1099](https://github.com/pdm-project/pdm/issues/1099)
- Fix a bug where dependencies with `requires-python` pre-release versions caused `pdm update` to fail with `InvalidPyVersion`. [#1111](https://github.com/pdm-project/pdm/issues/1111)

## Release v1.15.1 (2022-06-02)

### Bug Fixes

- Fix a bug that dependencies are missing from the dep graph when they are depended by a requirement with extras. [#1097](https://github.com/pdm-project/pdm/issues/1097)
- Give a default version if the version is dynamic in `setup.cfg` or `setup.py`. [#1101](https://github.com/pdm-project/pdm/issues/1101)
- Fix a bug that the hashes for file URLs are not included in the lock file. [#1103](https://github.com/pdm-project/pdm/issues/1103)
- Fix a bug that package versions are updated even when they are excluded by `pdm update` command. [#1104](https://github.com/pdm-project/pdm/issues/1104)
- Prefer `venv` install scheme when available. This scheme is more stable than `posix_prefix` scheme since the latter is often patched by distributions. [#1106](https://github.com/pdm-project/pdm/issues/1106)

### Miscellany

- Move the test artifacts to a submodule. It will make it easier to package this project. [#1084](https://github.com/pdm-project/pdm/issues/1084)

## Release v1.15.0 (2022-05-16)

### Features & Improvements

- Allow specifying lockfile other than `pdm.lock` by `--lockfile` option or `PDM_LOCKFILE` env var. [#1038](https://github.com/pdm-project/pdm/issues/1038)

### Bug Fixes

- Replace the editable entry in `pyproject.toml` when running `pdm add --no-editable <package>`. [#1050](https://github.com/pdm-project/pdm/issues/1050)
- Ensure the pip module inside venv in installation script. [#1053](https://github.com/pdm-project/pdm/issues/1053)
- Fix the py2 compatibility issue in the in-process `get_sysconfig_path.py` script. [#1056](https://github.com/pdm-project/pdm/issues/1056)
- Fix a bug that file paths in URLs are not correctly unquoted. [#1073](https://github.com/pdm-project/pdm/issues/1073)
- Fix a bug on Python 3.11 that overriding an existing command from plugins raises an error. [#1075](https://github.com/pdm-project/pdm/issues/1075)
- Replace the `${PROJECT_ROOT}` variable in the result of `export` command. [#1079](https://github.com/pdm-project/pdm/issues/1079)

### Removals and Deprecations

- Show a warning if Python 2 interpreter is being used and remove the support on 2.0. [#1082](https://github.com/pdm-project/pdm/issues/1082)

## Release v1.14.1 (2022-04-21)

### Features & Improvements

- Ask for description when doing `pdm init` and create default README for libraries. [#1041](https://github.com/pdm-project/pdm/issues/1041)

### Bug Fixes

- Fix a bug of missing subdirectory fragment when importing from a `requirements.txt`. [#1036](https://github.com/pdm-project/pdm/issues/1036)
- Fix use_cache.json with corrupted python causes `pdm use` error. [#1039](https://github.com/pdm-project/pdm/issues/1039)
- Ignore the `optional` key when converting from Poetry's dependency entries. [#1042](https://github.com/pdm-project/pdm/issues/1042)

### Improved Documentation

- Clarify documentation on enabling PEP582 globally. [#1033](https://github.com/pdm-project/pdm/issues/1033)

## Release v1.14.0 (2022-04-08)

### Features & Improvements

- Editable installations won't be overridden unless `--no-editable` is passed. `pdm add --no-editable` will now override the `editable` mode of the given packages. [#1011](https://github.com/pdm-project/pdm/issues/1011)
- Re-calculate the file hashes when running `pdm lock --refresh`. [#1019](https://github.com/pdm-project/pdm/issues/1019)

### Bug Fixes

- Fix a bug that requirement with extras isn't resolved to the version as specified by the range. [#1001](https://github.com/pdm-project/pdm/issues/1001)
- Replace the `${PROJECT_ROOT}` in the output of `pdm list`. [#1004](https://github.com/pdm-project/pdm/issues/1004)
- Further fix the python path issue of macOS system installed Python. [#1023](https://github.com/pdm-project/pdm/issues/1023)
- Fix the install path issue on Python 3.10 installed from homebrew. [#996](https://github.com/pdm-project/pdm/issues/996)

### Improved Documentation

- Document how to install PDM inside a project with Pyprojectx. [#1004](https://github.com/pdm-project/pdm/issues/1004)

### Dependencies

- Support `installer 0.5.x`. [#1002](https://github.com/pdm-project/pdm/issues/1002)

## Release v1.13.6 (2022-03-28)

### Bug Fixes

- Default the optional `license` field to "None". [#991](https://github.com/pdm-project/pdm/issues/991)
- Don't create project files in `pdm search` command. [#993](https://github.com/pdm-project/pdm/issues/993)
- Fix a bug that the env vars in source urls in exported result are not expanded. [#997](https://github.com/pdm-project/pdm/issues/997)

## Release v1.13.5 (2022-03-23)

### Features & Improvements

- Users can change the install destination of global project to the user site(`~/.local`) with `global_project.user_site` config. [#885](https://github.com/pdm-project/pdm/issues/885)
- Make the path to the global project configurable. Rename the configuration `auto_global` to `global_project.fallback` and deprecate the old name. [#986](https://github.com/pdm-project/pdm/issues/986)

### Bug Fixes

- Fix the compatibility when fetching license information in `show` command. [#966](https://github.com/pdm-project/pdm/issues/966)
- Don't follow symlinks for the paths in the requirement strings. [#976](https://github.com/pdm-project/pdm/issues/976)
- Use the default install scheme when installing build requirements. [#983](https://github.com/pdm-project/pdm/issues/983)
- Fix a bug that `_.site_packages` is overridden by default option value. [#985](https://github.com/pdm-project/pdm/issues/985)

## Release v1.13.4 (2022-03-09)

### Features & Improvements

- Update the dependency `pdm-pep517` to support PEP 639. [#959](https://github.com/pdm-project/pdm/issues/959)

### Bug Fixes

- Filter out the unmatched python versions when listing the available versions. [#941](https://github.com/pdm-project/pdm/issues/941)
- Fix a bug displaying the available python versions. [#943](https://github.com/pdm-project/pdm/issues/943)
- Fix a bug under non-UTF8 console encoding. [#960](https://github.com/pdm-project/pdm/issues/960)
- Fix a bug that data files are not copied to the destination when using installation cache. [#961](https://github.com/pdm-project/pdm/issues/961)

## Release v1.13.3 (2022-02-24)

### Bug Fixes

- Fix a bug that VCS repo name are parsed as the package name. [#928](https://github.com/pdm-project/pdm/issues/928)
- Support prerelease versions for global projects. [#932](https://github.com/pdm-project/pdm/issues/932)
- Fix a bug that VCS revision in the lock file isn't respected when installing. [#933](https://github.com/pdm-project/pdm/issues/933)

### Dependencies

- Switch from `pythonfinder` to `findpython` as the Python version finder. [#930](https://github.com/pdm-project/pdm/issues/930)

## Release v1.13.2 (2022-02-20)

### Bug Fixes

- Fix a regression issue that prereleases can't be installed if the version specifier of the requirement doesn't imply that. [#920](https://github.com/pdm-project/pdm/issues/920)

## Release v1.13.1 (2022-02-18)

### Bug Fixes

- Fix a bug that bad pip cache dir value breaks PDM's check update function. [#922](https://github.com/pdm-project/pdm/issues/922)
- Fix a race condition in parallel installation by changing metadata to a lazy property. This fixes a bug that incompatible wheels are installed unexpectedly. [#924](https://github.com/pdm-project/pdm/issues/924)

## Release v1.13.0.post0 (2022-02-18)

### Bug Fixes

- Fix a bug that incompatible platform-specific wheels are installed. [#921](https://github.com/pdm-project/pdm/issues/921)

## Release v1.13.0 (2022-02-18)

### Features & Improvements

- Support `pre_*` and `post_*` scripts for task composition. Pre- and Post- scripts for `init`, `build`, `install` and `lock` will be run if present. [#789](https://github.com/pdm-project/pdm/issues/789)
- Support `--config/-c` option to specify another global configuration file. [#883](https://github.com/pdm-project/pdm/issues/883)
- Packages with extras require no longer inherit the dependencies from the same package without extras. It is because the package without extras are returned as one of the dependencies. This change won't break the existing lock files nor dependency cache. [#892](https://github.com/pdm-project/pdm/issues/892)
- Support version ranges in `[tool.pdm.overrides]` table. [#909](https://github.com/pdm-project/pdm/issues/909)
- Rename config `use_venv` to `python.use_venv`; rename config `feature.install_cache` to `install.cache`; rename config `feature.install_cache_method` to `install.cache_method`; rename config `parallel_install` to `install.parallel`. [#914](https://github.com/pdm-project/pdm/issues/914)

### Bug Fixes

- Fix a bug that file URLs or VCS URLs don't work in `[tool.pdm.overrides]` table. [#861](https://github.com/pdm-project/pdm/issues/861)
- Fix a bug of identifier mismatch for URL requirements without an explicit name. [#901](https://github.com/pdm-project/pdm/issues/901)
- No `requires-python` should be produced if ANY(`*`) is given. [#917](https://github.com/pdm-project/pdm/issues/917)
- Fix a bug that `pdm.lock` gets created when `--dry-run` is passed to `pdm add`. [#918](https://github.com/pdm-project/pdm/issues/918)

### Improved Documentation

- The default editable backend becomes `path`. [#904](https://github.com/pdm-project/pdm/issues/904)

### Removals and Deprecations

- Stop auto-migrating projects from PDM 0.x format. [#912](https://github.com/pdm-project/pdm/issues/912)

### Refactor

- Rename `ExtrasError` to `ExtrasWarning` for better understanding. Improve the warning message. [#892](https://github.com/pdm-project/pdm/issues/892)
- Extract the environment related code from `Candidate` into a new class `PreparedCandidate`. `Candidate` no longer holds an `Environment` instance. [#920](https://github.com/pdm-project/pdm/issues/920)

## Release v1.12.8 (2022-02-06)

### Features & Improvements

- Print the error and continue if a plugin fails to load. [#878](https://github.com/pdm-project/pdm/issues/878)

### Bug Fixes

- PDM now ignores configuration of uninstalled plugins. [#872](https://github.com/pdm-project/pdm/issues/872)
- Fix the compatibility issue with `pip>=22.0`. [#875](https://github.com/pdm-project/pdm/issues/875)

## Release v1.12.7 (2022-01-31)

### Features & Improvements

- If no command is given to `pdm run`, it will run the Python REPL. [#856](https://github.com/pdm-project/pdm/issues/856)

### Bug Fixes

- Fix the hash calculation when generating `direct_url.json` for a local pre-built wheel. [#861](https://github.com/pdm-project/pdm/issues/861)
- PDM no longer migrates project meta silently. [#867](https://github.com/pdm-project/pdm/issues/867)

### Dependencies

- Pin `pip<22.0`. [#874](https://github.com/pdm-project/pdm/issues/874)

### Miscellany

- Reduce the number of tests that require network, and mark the rest with `network` marker. [#858](https://github.com/pdm-project/pdm/issues/858)

## Release v1.12.6 (2022-01-12)

### Bug Fixes

- Fix a bug that cache dir isn't created. [#843](https://github.com/pdm-project/pdm/issues/843)

## Release v1.12.5 (2022-01-11)

### Bug Fixes

- Fix a resolution error that dots in the package name are normalized to `-` unexpectedly. [#853](https://github.com/pdm-project/pdm/issues/853)

## Release v1.12.4 (2022-01-11)

### Features & Improvements

- Remember the last selection in `use` command to save the human effort. And introduce an `-i` option to ignored that remembered value. [#846](https://github.com/pdm-project/pdm/issues/846)

### Bug Fixes

- Fix a bug of uninstall crash when the package has directories in `RECORD`. [#847](https://github.com/pdm-project/pdm/issues/847)
- Fix the `ModuleNotFoundError` during uninstall when the modules required are removed. [#850](https://github.com/pdm-project/pdm/issues/850)

## Release v1.12.3 (2022-01-07)

### Features & Improvements

- Support setting Python path in global configuration. [#842](https://github.com/pdm-project/pdm/issues/842)

### Bug Fixes

- Lowercase the package names in the lock file make it more stable. [#836](https://github.com/pdm-project/pdm/issues/836)
- Show the packages to be updated in dry run mode of `pdm update` even if `--no-sync` is passed. [#837](https://github.com/pdm-project/pdm/issues/837)
- Improve the robustness of update check code. [#841](https://github.com/pdm-project/pdm/issues/841)
- Fix a bug that export result has environment markers that don't apply for all requirements. [#843](https://github.com/pdm-project/pdm/issues/843)

## Release v1.12.2 (2021-12-30)

### Features & Improvements

- Allow changing the installation linking method by `feature.install_cache_method` config. [#822](https://github.com/pdm-project/pdm/issues/822)

### Bug Fixes

- Fix a bug that namespace packages can't be symlinked to the cache due to existing links. [#820](https://github.com/pdm-project/pdm/issues/820)
- Make PDM generated pth files processed as early as possible. [#821](https://github.com/pdm-project/pdm/issues/821)
- Fix a UnicodeDecodeError for subprocess logger under Windows/GBK. [#823](https://github.com/pdm-project/pdm/issues/823)

## Release v1.12.1 (2021-12-24)

### Bug Fixes

- Don't symlink pycaches to the target place. [#817](https://github.com/pdm-project/pdm/issues/817)

## Release v1.12.0 (2021-12-22)

### Features & Improvements

- Add `lock --refresh` to update the hash stored with the lock file without updating the pinned versions. [#642](https://github.com/pdm-project/pdm/issues/642)
- Support resolution overriding in the `[tool.pdm.overrides]` table. [#790](https://github.com/pdm-project/pdm/issues/790)
- Add support for signals for basic operations, now including `post_init`, `pre_lock`, `post_lock`, `pre_install` and `post_install`. [#798](https://github.com/pdm-project/pdm/issues/798)
- Add `install --check` to check if the lock file is up to date. [#810](https://github.com/pdm-project/pdm/issues/810)
- Use symlinks to cache installed packages when it is supported by the file system. [#814](https://github.com/pdm-project/pdm/issues/814)

### Bug Fixes

- Fix a bug that candidates from urls are rejected by the `allow_prereleases` setting. Now non-named requirements are resolved earlier than pinned requirements. [#799](https://github.com/pdm-project/pdm/issues/799)

### Improved Documentation

- Add a new doc page: **API reference**. [#802](https://github.com/pdm-project/pdm/issues/802)

### Dependencies

- Switch back from `atoml` to `tomlkit` as the style-preserving TOML parser. The latter has supported TOML v1.0.0. [#809](https://github.com/pdm-project/pdm/issues/809)

### Miscellany

- Cache the latest version of PDM for one week to reduce the request frequency. [#800](https://github.com/pdm-project/pdm/issues/800)

## Release v1.11.3 (2021-12-15)

### Features & Improvements

- Change the default version save strategy to `minimum`, without upper bounds. [#787](https://github.com/pdm-project/pdm/issues/787)

### Bug Fixes

- Fix the patching of sysconfig in PEP 582 initialization script. [#796](https://github.com/pdm-project/pdm/issues/796)

### Miscellany

- Fix an installation failure of the bootstrap script on macOS Catalina. [#793](https://github.com/pdm-project/pdm/issues/793)
- Add a basic benchmarking script. [#794](https://github.com/pdm-project/pdm/issues/794)

## Release v1.11.2 (2021-12-10)

### Bug Fixes

- Fix the resolution order to reduce the loop number to find a conflict. [#781](https://github.com/pdm-project/pdm/issues/781)
- Patch the functions in `sysconfig` to return the PEP 582 scheme in `pdm run`. [#784](https://github.com/pdm-project/pdm/issues/784)

### Dependencies

- Remove the upper bound of version constraints for most dependencies, except for some zero-versioned ones. [#787](https://github.com/pdm-project/pdm/issues/787)

## Release v1.11.1 (2021-12-08)

### Features & Improvements

- Support `--pre/--prerelease` option for `pdm add` and `pdm update`. It will allow prereleases to be pinned. [#774](https://github.com/pdm-project/pdm/issues/774)
- Improve the error message when python is found but not meeting the python requirement. [#777](https://github.com/pdm-project/pdm/issues/777)

### Bug Fixes

- Fix a bug that `git+https` candidates cannot be resolved. [#771](https://github.com/pdm-project/pdm/issues/771)
- Fix an infinite resolution loop by resolving the top-level packages first. Also deduplicate the lines from the same requirement in the error output. [#776](https://github.com/pdm-project/pdm/issues/776)

### Miscellany

- Fix the install script to use a zipapp of virtualenv when it isn't installed. [#780](https://github.com/pdm-project/pdm/issues/780)

## Release v1.11.0 (2021-11-30)

### Features & Improvements

- Move `version` from `[project]` table to `[tool.pdm]` table, delete `classifiers` from `dynamic`, and warn usage about the deprecated usages. [#748](https://github.com/pdm-project/pdm/issues/748)
- Add support for Conda environments in addition to Python virtual environments. [#749](https://github.com/pdm-project/pdm/issues/749)
- Add support for saving only the lower bound `x >= VERSION` when adding dependencies. [#752](https://github.com/pdm-project/pdm/issues/752)
- Improve the error message when resolution fails. [#754](https://github.com/pdm-project/pdm/issues/754)

### Bug Fixes

- Switch to self-implemented `pdm list --freeze` to fix a bug due to Pip's API change. [#533](https://github.com/pdm-project/pdm/issues/533)
- Fix an infinite loop issue when resolving candidates with incompatible `requires-python`. [#744](https://github.com/pdm-project/pdm/issues/744)
- Fix the python finder to support pyenv-win. [#745](https://github.com/pdm-project/pdm/issues/745)
- Fix the ANSI color output for Windows cmd and Powershell terminals. [#753](https://github.com/pdm-project/pdm/issues/753)

### Removals and Deprecations

- Remove `-s/--section` option from all previously supported commands. Use `-G/--group` instead. [#756](https://github.com/pdm-project/pdm/issues/756)

## Release v1.10.3 (2021-11-18)

### Bug Fixes

- Use `importlib` to replace `imp` in the `sitecustomize` module for Python 3. [#574](https://github.com/pdm-project/pdm/issues/574)
- Fix the lib paths under non-isolated build. [#740](https://github.com/pdm-project/pdm/issues/740)
- Exclude the dependencies with extras in the result of `pdm export`. [#741](https://github.com/pdm-project/pdm/issues/741)

## Release v1.10.2 (2021-11-14)

### Features & Improvements

- Add a new option `-s/--site-packages` to `pdm run` as well as a script config item. When it is set to `True`, site-packages from the selected interpreter will be loaded into the running environment. [#733](https://github.com/pdm-project/pdm/issues/733)

### Bug Fixes

- Now `NO_SITE_PACKAGES` isn't set in `pdm run` if the executable is out of local packages. [#733](https://github.com/pdm-project/pdm/issues/733)

## Release v1.10.1 (2021-11-09)

### Features & Improvements

- Isolate the project environment with system site packages in `pdm run`, but keep them seen when PEP 582 is enabled. [#708](https://github.com/pdm-project/pdm/issues/708)

### Bug Fixes

- Run `pip` with `--isolated` when building wheels. In this way some env vars like `PIP_REQUIRE_VIRTUALENV` can be ignored. [#669](https://github.com/pdm-project/pdm/issues/669)
- Fix the install script to ensure `pip` is not DEBUNDLED. [#685](https://github.com/pdm-project/pdm/issues/685)
- Fix a bug that when `summary` is `None`, the lockfile can't be generated. [#719](https://github.com/pdm-project/pdm/issues/719)
- `${PROJECT_ROOT}` should be written in the URL when relative path is given. [#721](https://github.com/pdm-project/pdm/issues/721)
- Fix a bug that when project table already exists, `pdm import` can't merge the settings correctly. [#723](https://github.com/pdm-project/pdm/issues/723)

## Release v1.10.0 (2021-10-25)

### Features & Improvements

- Add `--no-sync` option to `update` command. [#684](https://github.com/pdm-project/pdm/issues/684)
- Support `find_links` source type. It can be specified via `type` key of `[[tool.pdm.source]]` table. [#694](https://github.com/pdm-project/pdm/issues/694)
- Add `--dry-run` option to `add`, `install` and `remove` commands. [#698](https://github.com/pdm-project/pdm/issues/698)

### Bug Fixes

- Remove trailing whitespace with terminal output of tables (via `project.core.ui.display_columns`), fixing unnecessary wrapping due to / with empty lines full of spaces in case of long URLs in the last column. [#680](https://github.com/pdm-project/pdm/issues/680)
- Include files should be installed under venv's base path. [#682](https://github.com/pdm-project/pdm/issues/682)
- Ensure the value of `check_update` is boolean. [#689](https://github.com/pdm-project/pdm/issues/689)

### Improved Documentation

- Update the contributing guide, remove the usage of `setup_dev.py` in favor of `pip install`. [#676](https://github.com/pdm-project/pdm/issues/676)

## Release v1.9.0 (2021-10-12)

### Bug Fixes

- Fix a bug that `requires-python` is not recognized in candidates evaluation. [#657](https://github.com/pdm-project/pdm/issues/657)
- Fix the path order when pdm run so that executables in local packages dir are found first. [#678](https://github.com/pdm-project/pdm/issues/678)

### Dependencies

- Update `installer` to `0.3.0`, fixing a bug that broke installation of some packages with unusual wheel files. [#653](https://github.com/pdm-project/pdm/issues/653)
- Change `packaging` and `typing-extensions` to direct dependencies. [#674](https://github.com/pdm-project/pdm/issues/674)

### Refactor

- `requires-python` now participates in the resolution as a dummy requirement. [#658](https://github.com/pdm-project/pdm/issues/658)

## Release v1.8.5 (2021-09-16)

### Bug Fixes

- Fix the error of regex to find the shebang line. [#656](https://github.com/pdm-project/pdm/issues/656)

## Release v1.8.4 (2021-09-15)

### Features & Improvements

- Support `--no-isolation` option for `install`, `lock`, `update`, `remove`, `sync` commands. [#640](https://github.com/pdm-project/pdm/issues/640)
- Make `project_max_depth` configurable and default to `5`. [#643](https://github.com/pdm-project/pdm/issues/643)

### Bug Fixes

- Don't try `pdm-pep517` backend on Python 2.7 when installing self as editable. [#640](https://github.com/pdm-project/pdm/issues/640)
- Fix a bug that existing shebang can't be replaced correctly. [#651](https://github.com/pdm-project/pdm/issues/651)
- Fix the version range saving for prerelease versions. [#654](https://github.com/pdm-project/pdm/issues/654)

## Release v1.8.3 (2021-09-07)

### Features & Improvements

- Allow to build in non-isolated environment, to enable optional speedups depending on the environment. [#635](https://github.com/pdm-project/pdm/issues/635)

### Bug Fixes

- Don't copy `*-nspkg.pth` files in `install_cache` mode. It will still work without them. [#623](https://github.com/pdm-project/pdm/issues/623)

## Release v1.8.2 (2021-09-01)

### Bug Fixes

- Fix the removal issue of standalone pyc files [#633](https://github.com/pdm-project/pdm/issues/633)

## Release v1.8.1 (2021-08-26)

### Features & Improvements

- Add `-r/--reinstall` option to `sync` command to force re-install the existing dependencies. [#601](https://github.com/pdm-project/pdm/issues/601)
- Show update hint after every pdm command. [#603](https://github.com/pdm-project/pdm/issues/603)
- `pdm cache clear` can clear cached installations if not needed any more. [#604](https://github.com/pdm-project/pdm/issues/604)

### Bug Fixes

- Fix the editable install script so that `setuptools` won't see the dependencies under local packages. [#601](https://github.com/pdm-project/pdm/issues/601)
- Preserve the executable bit when installing wheels. [#606](https://github.com/pdm-project/pdm/issues/606)
- Write PEP 610 metadata `direct_url.json` when installing wheels. [#607](https://github.com/pdm-project/pdm/issues/607)
- Fix a bug that `*` fails to be converted as `SpecifierSet`. [#609](https://github.com/pdm-project/pdm/issues/609)

### Refactor

- Build editable packages are into wheels via PEP 660 build backend. Now all installations are unified into wheels. [#612](https://github.com/pdm-project/pdm/issues/612)

## Release v1.8.0 (2021-08-16)

### Features & Improvements

- Added a new mode `--json` to the list command which outputs the dependency graph as a JSON document. [#583](https://github.com/pdm-project/pdm/issues/583)
- Add a new config `feature.install_cache`. When it is turned on, wheels will be installed into a centralized package repo and create `.pth` files under project packages directory to link to the cached package. [#589](https://github.com/pdm-project/pdm/issues/589)

### Bug Fixes

- Fix env vars in source URLs not being expanded in all cases. [#570](https://github.com/pdm-project/pdm/issues/570)
- Fix the weird output of `pdm show`. [#580](https://github.com/pdm-project/pdm/issues/580)
- Prefer `~/.pyenv/shims/python3` as the pyenv interpreter. [#590](https://github.com/pdm-project/pdm/issues/590)
- Fix a bug that installing will download candidates that do not match the locked hashes. [#596](https://github.com/pdm-project/pdm/issues/596)

### Improved Documentation

- Added instructions to the Contributing section for creating news fragments [#573](https://github.com/pdm-project/pdm/issues/573)

### Removals and Deprecations

- Deprecate `-s/--section` option in favor of `-G/--group`. [#591](https://github.com/pdm-project/pdm/issues/591)

### Refactor

- Switch to a self-implemented version of uninstaller. [#586](https://github.com/pdm-project/pdm/issues/586)
- `pdm/installers/installers.py` is renamed to `pdm/installers/manager.py` to be more accurate. The `Installer` class under that file is renamed to `InstallerManager` and is exposed in the `pdm.core.Core` object for overriding. The new `pdm/installers/installers.py` contains some installation implementations. [#589](https://github.com/pdm-project/pdm/issues/589)
- Switch from `pkg_resources.Distribution` to the implementation of `importlib.metadata`. [#592](https://github.com/pdm-project/pdm/issues/592)

## Release v1.7.2 (2021-07-30)

### Bug Fixes

- Remove the existing files before installing. [#565](https://github.com/pdm-project/pdm/issues/565)
- Deduplicate the plugins list. [#566](https://github.com/pdm-project/pdm/issues/566)

## Release v1.7.1 (2021-07-29)

### Bug Fixes

- Accept non-canonical distribution name in the wheel's dist-info directory name. [#529](https://github.com/pdm-project/pdm/issues/529)
- Prefer requirements with narrower version constraints or allowing prereleases to find matches. [#551](https://github.com/pdm-project/pdm/issues/551)
- Use the underlying real executable path for writing shebangs. [#553](https://github.com/pdm-project/pdm/issues/553)
- Fix a bug that extra markers cannot be extracted when combined with other markers with "and". [#559](https://github.com/pdm-project/pdm/issues/559)
- Fix a bug that redacted credentials in source urls get overwritten with the plain text after locking. [#561](https://github.com/pdm-project/pdm/issues/561)

### Refactor

- Use installer as the wheel installer, replacing `distlib`. [#519](https://github.com/pdm-project/pdm/issues/519)

## Release v1.7.0 (2021-07-20)

### Features & Improvements

- Support showing individual fields by `--<field-name>` options in pdm show. When no package is given, show this project. [#527](https://github.com/pdm-project/pdm/issues/527)
- Add `--freeze` option to `pdm list` command which shows the dependencies list as pip's requirements.txt format. [#531](https://github.com/pdm-project/pdm/issues/531)

### Bug Fixes

- Fix the path manipulation on Windows, now the PEP 582 path is prepended to the `PYTHONPATH`. [#522](https://github.com/pdm-project/pdm/issues/522)
- Fix the handling of auth prompting: will try keyring in non-verbose mode. [#523](https://github.com/pdm-project/pdm/issues/523)
- Recognize old entry point name "pdm.plugin" for backward-compatibility. [#530](https://github.com/pdm-project/pdm/issues/530)
- Match the VCS scheme in case-insensitive manner. [#537](https://github.com/pdm-project/pdm/issues/537)
- Use the default permission bits when writing project files. [#542](https://github.com/pdm-project/pdm/issues/542)
- Fix the VCS url to be consistent between lock and install. [#547](https://github.com/pdm-project/pdm/issues/547)

### Improved Documentation

- Add installation instructions for Scoop. [#522](https://github.com/pdm-project/pdm/issues/522)

### Dependencies

- Update `pdm-pep517` to `0.8.0`. [#524](https://github.com/pdm-project/pdm/issues/524)
- Switch from `toml` to `tomli`. [#541](https://github.com/pdm-project/pdm/issues/541)

### Refactor

- Separate the build env into two different levels for better caching. [#541](https://github.com/pdm-project/pdm/issues/541)
- Refactor the build part into smaller functions. [#543](https://github.com/pdm-project/pdm/issues/543)

## Release v1.6.4 (2021-06-23)

### Features & Improvements

- Extract package name from egg-info in filename when eligible. Remove the patching code of resolvelib's inner class. [#441](https://github.com/pdm-project/pdm/issues/441)
- Support installing packages from subdirectories of VCS repository. [#507](https://github.com/pdm-project/pdm/issues/507)
- Add an install script to bootstrap PDM quickly without help of other tools. Modify docs to recommend this installation method. [#508](https://github.com/pdm-project/pdm/issues/508)
- Add a new subcommand `plugin` to manage pdm plugins, including `add`, `remove` and `list` commands. [#510](https://github.com/pdm-project/pdm/issues/510)

### Bug Fixes

- Don't monkeypatch the internal class of `resolvelib` any more. This makes PDM more stable across updates of sub-dependencies. [#515](https://github.com/pdm-project/pdm/issues/515)

### Miscellany

- Clear the type errors from mypy. [#261](https://github.com/pdm-project/pdm/issues/261)

## Release v1.6.3 (2021-06-17)

### Features & Improvements

- Add an option `-u/--unconstrained` to support unconstraining version specifiers when adding packages. [#501](https://github.com/pdm-project/pdm/issues/501)

### Bug Fixes

- Fix the format of dependency arrays when a new value is appended. [#487](https://github.com/pdm-project/pdm/issues/487)
- Allow missing email attribute for authors and maintainers. [#492](https://github.com/pdm-project/pdm/issues/492)
- Fix a bug that editable install shouldn't require pyproject.toml to be valid. [#497](https://github.com/pdm-project/pdm/issues/497)
- Fix a bug on macOS that purelib and platlib paths of isolated build envs cannot be substituted correctly if the Python is a framework build. [#502](https://github.com/pdm-project/pdm/issues/502)
- Fix the version sort of candidates. [#506](https://github.com/pdm-project/pdm/issues/506)

## Release v1.6.2 (2021-05-31)

No significant changes.

## Release v1.6.1 (2021-05-31)

No significant changes.

## Release v1.6.0 (2021-05-31)

### Features & Improvements

- Use a new approach to determine the packages to be installed. This requires a quick resolution step before installation. [#456](https://github.com/pdm-project/pdm/issues/456)
- `pdm export` no longer produces requirements file applicable for all platforms due to the new approach. [#456](https://github.com/pdm-project/pdm/issues/456)
- Add structural typing for requirements module. Refactor the requirements module for that purpose. [#433](https://github.com/pdm-project/pdm/issues/433)
- Introduce `--no-editable` option to install non-editable versions of all packages. [#443](https://github.com/pdm-project/pdm/issues/443)
- Introduce `--no-self` option to prevent the project itself from being installed. [#444](https://github.com/pdm-project/pdm/issues/444)
- Add a default `.gitignore` file in the `__pypackages__` directory. [#446](https://github.com/pdm-project/pdm/issues/446)
- Check if the lock file version is compatible with PDM program before installation. [#463](https://github.com/pdm-project/pdm/issues/463)
- Expose the project root path via `PDM_PROJECT_ROOT` env var. Change to the project root when executing scripts. [#470](https://github.com/pdm-project/pdm/issues/470)
- Fix a bug that installation resolution doesn't respect the requirement markers from pyproject config. [#480](https://github.com/pdm-project/pdm/issues/480)

### Bug Fixes

- Changing to multiline breaks the parsing of TOML document. [#462](https://github.com/pdm-project/pdm/issues/462)
- Fix a bug that transient dependencies of conditional requirements can't be resolved. [#472](https://github.com/pdm-project/pdm/issues/472)
- Fix a bug that invalid wheels are rejected while they are acceptable for resolution. [#473](https://github.com/pdm-project/pdm/issues/473)
- Fix a bug that build environment is not fully isolated with the hosted environment. [#477](https://github.com/pdm-project/pdm/issues/477)
- Ensure the lock file is compatible before looking for the locked candidates. [#484](https://github.com/pdm-project/pdm/issues/484)

### Improved Documentation

- Fix 404 links in documentation. [#472](https://github.com/pdm-project/pdm/issues/472)

### Dependencies

- Migrate from `tomlkit` to `atoml` as the style-preserving TOML parser and writer. [#465](https://github.com/pdm-project/pdm/issues/465)

### Removals and Deprecations

- Remove the warning of `--dev` flag for older versions of PDM. [#444](https://github.com/pdm-project/pdm/issues/444)

### Miscellany

- Add Python 3.10 beta CI job. [#457](https://github.com/pdm-project/pdm/issues/457)

## Release v1.5.3 (2021-05-10)

### Features & Improvements

- Support passing options to the build backends via `--config-setting`. [#452](https://github.com/pdm-project/pdm/issues/452)

### Bug Fixes

- Seek for other sitecustomize.py to import. [#422](https://github.com/pdm-project/pdm/issues/422)
- Fix an unescaped single quote in fish completion script. [#423](https://github.com/pdm-project/pdm/issues/423)
- The hashes of a remote file candidate should be calculated from the link itself. [#450](https://github.com/pdm-project/pdm/issues/450)

### Dependencies

- Remove `keyring` as a dependency and guide users to install it when it is not available. [#442](https://github.com/pdm-project/pdm/issues/442)
- Specify the minimum version of `distlib`. [#447](https://github.com/pdm-project/pdm/issues/447)

### Miscellany

- Add log output about found candidates and their origin. [#421](https://github.com/pdm-project/pdm/issues/421)
- Add [mypy](https://github.com/python/mypy) pre-commit hook [#427](https://github.com/pdm-project/pdm/issues/427)
- Improve type safety of `pdm.cli.actions` [#428](https://github.com/pdm-project/pdm/issues/428)
- Fix wrong mypy configuration. [#451](https://github.com/pdm-project/pdm/issues/451)

## Release v1.5.2 (2021-04-27)

### Features & Improvements

- Allow `pdm use` with no argument given, which will list all available pythons for pick. [#409](https://github.com/pdm-project/pdm/issues/409)

### Bug Fixes

- Inform user to enable PEP 582 for development script to work. [#404](https://github.com/pdm-project/pdm/issues/404)
- Check the existence of pyenv shim Python interpreter before using it. [#406](https://github.com/pdm-project/pdm/issues/406)
- Fix a bug that executing `setup.py` failed for NameError. [#407](https://github.com/pdm-project/pdm/issues/407)
- Check before setting the PYTHONPATH environment variable for PEP582 [#410](https://github.com/pdm-project/pdm/issues/410)
- Fix development setup error. [#415](https://github.com/pdm-project/pdm/issues/415)

### Dependencies

- Update pip to 21.1 and fix compatibility issues. [#412](https://github.com/pdm-project/pdm/issues/412)

## Release v1.5.1 (2021-04-22)

### Bug Fixes

- Make func translate_sections pure to avoid exporting requirements in random order. [#401](https://github.com/pdm-project/pdm/issues/401)
- Expand the variables in install requirements' attributes for build. [#402](https://github.com/pdm-project/pdm/issues/402)

## Release v1.5.0 (2021-04-20)

### Features & Improvements

- Include dev dependencies by default for `install` and `sync` commands. Add a new option `--prod/--production` to exclude them. Improve the dependency selection logic to be more convenient to use — the more common the usage is, the shorter the command is. [#391](https://github.com/pdm-project/pdm/issues/391)

### Bug Fixes

- Enquote executable path to ensure generating valid scripts. [#387](https://github.com/pdm-project/pdm/issues/387)
- Consider hashes when fetching artifact link for build. [#389](https://github.com/pdm-project/pdm/issues/389)
- Consider the sources settings when building. [#399](https://github.com/pdm-project/pdm/issues/399)

### Improved Documentation

- New pdm setting `source-includes` to mark files to be included only in sdist builds. [#390](https://github.com/pdm-project/pdm/issues/390)

### Dependencies

- Update `pdm-pep517` to `0.7.0`; update `resolvelib` to`0.7.0`. [#390](https://github.com/pdm-project/pdm/issues/390)

### Removals and Deprecations

- Deprecate the usage of `-d/--dev` option in `install` and `sync` commands. [#391](https://github.com/pdm-project/pdm/issues/391)

## Release v1.5.0b1 (2021-04-12)

### Features & Improvements

- Improve the env builder to run in isolated mode. [#384](https://github.com/pdm-project/pdm/issues/384)

### Bug Fixes

- Remove the incompatible code from the files that will be run in-process. [#375](https://github.com/pdm-project/pdm/issues/375)
- Get the correct Python ABI tag of selected interpreter [#378](https://github.com/pdm-project/pdm/issues/378)
- Error out when doing `pdm run` on a directory not initialized yet.
- Give warning message when the project automatically fallbacks to the global project.

### Dependencies

- Upgrade `resolvelib` to `0.6.0`. [#381](https://github.com/pdm-project/pdm/issues/381)

### Miscellany

- refactor `pdm.models.readers` to improve typing support [#321](https://github.com/pdm-project/pdm/issues/321)
- Add a basic integration test for cross-python check. [#377](https://github.com/pdm-project/pdm/issues/377)
- Refactor the `project.python_executable` to `project.python` that contains all info of the interpreter. [#382](https://github.com/pdm-project/pdm/issues/382)
- Continue refactoring Python info to extract to its own module. [#383](https://github.com/pdm-project/pdm/issues/383)
- Refactor the creation of project.

## Release v1.5.0b0 (2021-04-03)

### Features & Improvements

- Add hand-written zsh completion script. [#188](https://github.com/pdm-project/pdm/issues/188)
- Add a special value `:all` given to `-s/--section` to refer to all sections under the same species. Adjust `add`, `sync`, `install`, `remove` and `update` to support the new `dev-dependencies` groups. Old behavior will be kept the same. [#351](https://github.com/pdm-project/pdm/issues/351)
- `dev-dependencies` is now a table of dependencies groups, where key is the group name and value is an array of dependencies. These dependencies won't appear in the distribution's metadata. `dev-dependencies` of the old format will turn into `dev` group under `dev-dependencies`. [#351](https://github.com/pdm-project/pdm/issues/351)
- Move `dev-dependencies`, `includes`, `excludes` and `package-dir` out from `[project]` table to `[tool.pdm]` table. The migration will be done automatically if old format is detected. [#351](https://github.com/pdm-project/pdm/issues/351)
- Throws an error with meaningful message when no candidate is found for one requirement. [#357](https://github.com/pdm-project/pdm/issues/357)
- Support `--dry-run` option for `update` command to display packages that need update, install or removal. Add `--top` option to limit to top level packages only. [#358](https://github.com/pdm-project/pdm/issues/358)
- Full-featured completion scripts for Zsh and Powershell - section selection, package name autocompletion and so on. Windows is a first-class citizen! [#367](https://github.com/pdm-project/pdm/issues/367)
- Support non-interactive `init` command via `-n/--non-interactive` option. No question will be asked in this mode. [#368](https://github.com/pdm-project/pdm/issues/368)
- Show project packages path(PEP 582) in the output of `pdm info`, also add an option `--packages` to show that value only. [#372](https://github.com/pdm-project/pdm/issues/372)

### Bug Fixes

- Fix a bug that pure python libraries are not loaded to construct the WorkingSet. [#346](https://github.com/pdm-project/pdm/issues/346)
- Don't write `<script>-X.Y` variant to the bin folder. [#365](https://github.com/pdm-project/pdm/issues/365)
- Python is now run in isolated mode via subprocess to avoid accidentally importing user packages. [#369](https://github.com/pdm-project/pdm/issues/369)
- Don't overwrite existing dependencies when importing from requirements.txt. [#370](https://github.com/pdm-project/pdm/issues/370)

### Improved Documentation

- Add instructions of how to integrate PDM with Emacs, contributed by @linw1995. [#372](https://github.com/pdm-project/pdm/issues/372)

### Removals and Deprecations

- Remove the support of project path following `-g/--global` that was deprecated in `1.4.0`. One should use `-g -p <project_path>` for that purpose. [#361](https://github.com/pdm-project/pdm/issues/361)

### Miscellany

- Add test coverage to PDM. [#109](https://github.com/pdm-project/pdm/issues/109)
- Add type annotations into untyped functions to start using mypy. [#354](https://github.com/pdm-project/pdm/issues/354)
- Refactor the format converter code to be more explicit. [#360](https://github.com/pdm-project/pdm/issues/360)

## Release v1.4.5 (2021-03-30)

### Features & Improvements

- Skip the first prompt of `pdm init` [#352](https://github.com/pdm-project/pdm/issues/352)

### Bug Fixes

- Fix a test failure when using homebrew installed python. [#348](https://github.com/pdm-project/pdm/issues/348)
- Get revision from the VCS URL if source code isn't downloaded to local. [#349](https://github.com/pdm-project/pdm/issues/349)

### Dependencies

- Update dependency `pdm-pep517` to `0.6.1`. [#353](https://github.com/pdm-project/pdm/issues/353)

## Release v1.4.4 (2021-03-27)

### Features & Improvements

- Emit warning if version or description can't be retrieved when importing from flit metadata. [#342](https://github.com/pdm-project/pdm/issues/342)
- Add `type` argument to `pdm cache clear` and improve its UI. [#343](https://github.com/pdm-project/pdm/issues/343)
- Always re-install the editable packages when syncing the working set. This can help tracking the latest change of `entry-points`. [#344](https://github.com/pdm-project/pdm/issues/344)

### Bug Fixes

- Make installer quit early if a wheel isn't able to build. [#338](https://github.com/pdm-project/pdm/issues/338)

### Miscellany

- ignore type checking in `models.project_info.ProjectInfo`, which indexes `distlib.metadata._data` [#335](https://github.com/pdm-project/pdm/issues/335)

## Release v1.4.3 (2021-03-24)

### Features & Improvements

- Change the group name of entry points from `pdm.plugins` to `pdm`. Export some useful objects and models for shorter import path. [#318](https://github.com/pdm-project/pdm/issues/318)
- Field `cmd` in `tools.pdm.scripts` configuration items now allows specifying an argument array instead of a string.
- Refactor: Remove the reference of `stream` singleton, improve the UI related code. [#320](https://github.com/pdm-project/pdm/issues/320)
- Support dependencies managed by poetry and flit being installed as editable packages. [#324](https://github.com/pdm-project/pdm/issues/324)
- Refactor: Extract the logic of finding interpreters to method for the sake of subclass overriding. [#326](https://github.com/pdm-project/pdm/issues/326)
- Complete the `cache` command, add `list`, `remove` and `info` subcommands. [#329](https://github.com/pdm-project/pdm/issues/329)
- Refactor: Unify the code about selecting interpreter to reduce the duplication. [#331](https://github.com/pdm-project/pdm/issues/331)
- Retrieve the version and description of a flit project by parsing the AST of the main file. [#333](https://github.com/pdm-project/pdm/issues/333)

### Bug Fixes

- Fix a parsing error when non-ascii characters exist in `pyproject.toml`. [#308](https://github.com/pdm-project/pdm/issues/308)
- Fix a bug that non-editable VCS candidates can't satisfy their requirements once locked in the lock file. [#314](https://github.com/pdm-project/pdm/issues/314)
- Fix a bug of import-on-init that fails when requirements.txt is detected. [#328](https://github.com/pdm-project/pdm/issues/328)

### Miscellany

- refactor `pdm.iostream` to improve 'typing' support [#301](https://github.com/pdm-project/pdm/issues/301)
- fix some typos [#323](https://github.com/pdm-project/pdm/issues/323)

## Release v1.4.2 (2021-03-18)

### Features & Improvements

- Refactor the code, extract the version related logic from `specifiers.py` to a separated module. [#303](https://github.com/pdm-project/pdm/issues/303)

### Bug Fixes

- Fix a bug that get_dependencies() returns error when the `setup.py` has no `install_requires` key. [#299](https://github.com/pdm-project/pdm/issues/299)
- Pin the VCS revision for non-editable VCS candidates in the lock file. [#305](https://github.com/pdm-project/pdm/issues/305)
- Fix a bug that editable build hits the cached wheel unexpectedly. [#307](https://github.com/pdm-project/pdm/issues/307)

### Miscellany

- replace 'typing comments' with type annotations throughout [#298](https://github.com/pdm-project/pdm/issues/298)

## Release v1.4.1 (2021-03-12)

### Features & Improvements

- Support importing dependencies from requirements.txt to dev-dependencies or sections. [#291](https://github.com/pdm-project/pdm/issues/291)

### Bug Fixes

- Fallback to static parsing when building was failed to find the dependencies of a candidate. [#293](https://github.com/pdm-project/pdm/issues/293)
- Fix a bug that `pdm init` fails when `pyproject.toml` exists but has no `[project]` section. [#295](https://github.com/pdm-project/pdm/issues/295)

### Improved Documentation

- Document about how to use PDM with Nox. [#281](https://github.com/pdm-project/pdm/issues/281)

## Release v1.4.0 (2021-03-05)

### Features & Improvements

- When `-I/--ignore-python` passed or `PDM_IGNORE_SAVED_PYTHON=1`, ignore the interpreter set in `.pdm.toml` and don't save to it afterwards. [#283](https://github.com/pdm-project/pdm/issues/283)
- A new option `-p/--project` is introduced to specify another path for the project base. It can also be combined with `-g/--global` option. The latter is changed to a flag only option that does not accept values. [#286](https://github.com/pdm-project/pdm/issues/286)
- Support `-f setuppy` for `pdm export` to export the metadata as setup.py [#289](https://github.com/pdm-project/pdm/issues/289)

### Bug Fixes

- Fix a bug that editable local package requirements cannot be parsed rightly. [#285](https://github.com/pdm-project/pdm/issues/285)
- Change the priority of metadata files to parse so that PEP 621 metadata will be parsed first. [#288](https://github.com/pdm-project/pdm/issues/288)

### Improved Documentation

- Add examples of how to integrate with CI pipelines (and tox). [#281](https://github.com/pdm-project/pdm/issues/281)

## Release v1.3.4 (2021-03-01)

### Improved Documentation

- added documentation on a [task provider for vscode](https://marketplace.visualstudio.com/items?itemName=knowsuchagency.pdm-task-provider) [#280](https://github.com/pdm-project/pdm/issues/280)

### Bug Fixes

- Ignore the python requires constraints when fetching the link from the PyPI index.

## Release v1.3.3 (2021-02-26)

### Bug Fixes

- Fix the requirement string of a VCS requirement to comply with PEP 508. [#275](https://github.com/pdm-project/pdm/issues/275)
- Fix a bug that editable packages with `src` directory can't be uninstalled correctly. [#277](https://github.com/pdm-project/pdm/issues/277)
- Fix a bug that editable package doesn't override the non-editable version in the working set. [#278](https://github.com/pdm-project/pdm/issues/278)

## Release v1.3.2 (2021-02-25)

### Features & Improvements

- Abort and tell user the selected section following `pdm sync` or `pdm install` is not present in the error message. [#274](https://github.com/pdm-project/pdm/issues/274)

### Bug Fixes

- Fix a bug that candidates' sections cannot be retrieved rightly when circular dependencies exist. [#270](https://github.com/pdm-project/pdm/issues/270)
- Don't pass the help argument into the run script method. [#272](https://github.com/pdm-project/pdm/issues/272)

## Release v1.3.1 (2021-02-19)

### Bug Fixes

- Use the absolute path when importing from a Poetry pyproject.toml. [#262](https://github.com/pdm-project/pdm/issues/262)
- Fix a bug that old toml table head is kept when converting to PEP 621 metadata format. [#263](https://github.com/pdm-project/pdm/issues/263)
- Postpone the evaluation of `requires-python` attribute when fetching the candidates of a package. [#264](https://github.com/pdm-project/pdm/issues/264)

## Release v1.3.0 (2021-02-09)

### Features & Improvements

- Increase the default value of the max rounds of resolution to 1000, make it configurable. [#238](https://github.com/pdm-project/pdm/issues/238)
- Rewrite the project's `egg-info` directory when dependencies change. So that `pdm list --graph` won't show invalid entries. [#240](https://github.com/pdm-project/pdm/issues/240)
- When importing requirements from a `requirements.txt` file, build the package to find the name if not given in the URL. [#245](https://github.com/pdm-project/pdm/issues/245)
- When initializing the project, prompt user for whether the project is a library, and give empty `name` and `version` if not. [#253](https://github.com/pdm-project/pdm/issues/253)

### Bug Fixes

- Fix the version validator of wheel metadata to align with the implementation of `packaging`. [#130](https://github.com/pdm-project/pdm/issues/130)
- Preserve the `sections` value of a pinned candidate to be reused. [#234](https://github.com/pdm-project/pdm/issues/234)
- Strip spaces in user input when prompting for the python version to use. [#252](https://github.com/pdm-project/pdm/issues/252)
- Fix the version parsing of Python requires to allow `>`, `>=`, `<`, `<=` to combine with star versions. [#254](https://github.com/pdm-project/pdm/issues/254)

## Release v1.2.0 (2021-01-26)

### Features & Improvements

- Change the behavior of `--save-compatible` slightly. Now the version specifier saved is using the REAL compatible operator `~=` as described in PEP 440. Before: `requests<3.0.0,>=2.19.1`, After: `requests~=2.19`. The new specifier accepts `requests==2.19.0` as compatible version. [#225](https://github.com/pdm-project/pdm/issues/225)
- Environment variable `${PROJECT_ROOT}` in the dependency specification can be expanded to refer to the project root in pyproject.toml. The environment variables will be kept as they are in the lock file. [#226](https://github.com/pdm-project/pdm/issues/226)
- Change the dependencies of a package in the lock file to a list of PEP 508 strings [#236](https://github.com/pdm-project/pdm/issues/236)

### Bug Fixes

- Ignore user's site and `PYTHONPATH`(with `python -I` mode) when executing pip commands. [#231](https://github.com/pdm-project/pdm/issues/231)

### Improved Documentation

- Document about how to activate and use a plugin. [#227](https://github.com/pdm-project/pdm/issues/227)

### Dependencies

- Test project on `pip 21.0`. [#235](https://github.com/pdm-project/pdm/issues/235)

## Release v1.1.0 (2021-01-18)

### Features & Improvements

- Allow users to hide secrets from the `pyproject.toml`.
- Dynamically expand env variables in the URLs in dependencies and indexes.
- Ask whether to store the credentials provided by the user.
- A user-friendly error will show when credentials are not provided nor correct. [#198](https://github.com/pdm-project/pdm/issues/198)
- Use a different package dir for 32-bit installation(Windows). [#212](https://github.com/pdm-project/pdm/issues/212)
- Auto disable PEP 582 when a venv-like python is given as the interpreter path. [#219](https://github.com/pdm-project/pdm/issues/219)
- Support specifying Python interpreter by `pdm use <path-to-python-root>`. [#221](https://github.com/pdm-project/pdm/issues/221)

### Bug Fixes

- Fix a bug of `PYTHONPATH` manipulation under Windows platform. [#215](https://github.com/pdm-project/pdm/issues/215)

### Removals and Deprecations

- Remove support of the old PEP 517 backend API path. [#217](https://github.com/pdm-project/pdm/issues/217)

## Release v1.0.0 (2021-01-05)

### Bug Fixes

- Correctly build wheels for dependencies with build-requirements but without a specified build-backend [#213](https://github.com/pdm-project/pdm/issues/213)

## Release v1.0.0b2 (2020-12-29)

### Features & Improvements

- Fallback to pypi.org when `/search` endpoint is not available on given index. [#211](https://github.com/pdm-project/pdm/issues/211)

### Bug Fixes

- Fix a bug that PDM fails to parse python version specifiers with more than 3 parts. [#210](https://github.com/pdm-project/pdm/issues/210)

## Release v1.0.0b0 (2020-12-24)

### Features & Improvements

- Fully support of PEP 621 specification.
- Old format is deprecated at the same time.
- PDM will migrate the project file for you when old format is detected.
- Other metadata formats(`Poetry`, `Pipfile`, `flit`) can also be imported as PEP 621 metadata. [#175](https://github.com/pdm-project/pdm/issues/175)
- Re-implement the `pdm search` to query the `/search` HTTP endpoint. [#195](https://github.com/pdm-project/pdm/issues/195)
- Reuse the cached built wheels to accelerate the installation. [#200](https://github.com/pdm-project/pdm/issues/200)
- Make update strategy and save strategy configurable in pdm config. [#202](https://github.com/pdm-project/pdm/issues/202)
- Improve the error message to give more insight on what to do when resolution fails. [#207](https://github.com/pdm-project/pdm/issues/207)
- Set `classifiers` dynamic in `pyproject.toml` template for autogeneration. [#209](https://github.com/pdm-project/pdm/issues/209)

### Bug Fixes

- Fix a bug that distributions are not removed clearly in parallel mode. [#204](https://github.com/pdm-project/pdm/issues/204)
- Fix a bug that python specifier `is_subset()` returns incorrect result. [#206](https://github.com/pdm-project/pdm/issues/206)

## Release v0.12.3 (2020-12-21)

### Dependencies

- Pin `pdm-pep517` to `<0.3.0`, this is the last version to support legacy project metadata format.

## Release v0.12.2 (2020-12-17)

### Features & Improvements

- Update the lock file schema, move the file hashes to `[metadata.files]` table. [#196](https://github.com/pdm-project/pdm/issues/196)
- Retry failed jobs when syncing packages. [#197](https://github.com/pdm-project/pdm/issues/197)

### Removals and Deprecations

- Drop `pip-shims` package as a dependency. [#132](https://github.com/pdm-project/pdm/issues/132)

### Miscellany

- Fix the cache path for CI. [#199](https://github.com/pdm-project/pdm/issues/199)

## Release v0.12.1 (2020-12-14)

### Features & Improvements

- Provide an option to export requirements from pyproject.toml [#190](https://github.com/pdm-project/pdm/issues/190)
- For Windows users, `pdm --pep582` can enable PEP 582 globally by manipulating the WinReg. [#191](https://github.com/pdm-project/pdm/issues/191)

### Bug Fixes

- Inject `__pypackages__` into `PATH` env var during `pdm run`. [#193](https://github.com/pdm-project/pdm/issues/193)

## Release v0.12.0 (2020-12-08)

### Features & Improvements

- Improve the user experience of `pdm run`:
- Add a special key in tool.pdm.scripts that holds configurations shared by all scripts.
- Support loading env var from a dot-env file.
- Add a flag `-s/--site-packages` to include system site-packages when running. [#178](https://github.com/pdm-project/pdm/issues/178)
- Now PEP 582 can be enabled in the Python interpreter directly! [#181](https://github.com/pdm-project/pdm/issues/181)

### Bug Fixes

- Ensure `setuptools` is installed before invoking editable install script. [#174](https://github.com/pdm-project/pdm/issues/174)
- Require `wheel` not `wheels` for global projects [#182](https://github.com/pdm-project/pdm/issues/182)
- Write a `sitecustomize.py` instead of a `.pth` file to enable PEP 582. Thanks @Aloxaf. Update `get_package_finder()` to be compatible with `pip 20.3`. [#185](https://github.com/pdm-project/pdm/issues/185)
- Fix the help messages of commands "cache" and "remove" [#187](https://github.com/pdm-project/pdm/issues/187)

## Release v0.11.0 (2020-11-20)

### Features & Improvements

- Support custom script shortcuts in `pyproject.toml`.
- Support custom script shortcuts defined in `[tool.pdm.scripts]` section.
- Add `pdm run --list/-l` to show the list of script shortcuts. [#168](https://github.com/pdm-project/pdm/issues/168)
- Patch the halo library to support parallel spinners.
- Change the looking of `pdm install`. [#169](https://github.com/pdm-project/pdm/issues/169)

### Bug Fixes

- Fix a bug that package's marker fails to propagate to its grandchildren if they have already been resolved. [#170](https://github.com/pdm-project/pdm/issues/170)
- Fix a bug that bare version specifiers in Poetry project can't be converted correctly. [#172](https://github.com/pdm-project/pdm/issues/172)
- Fix the build error that destination directory is not created automatically. [#173](https://github.com/pdm-project/pdm/issues/173)

## Release v0.10.2 (2020-11-05)

### Bug Fixes

- Building editable distribution does not install `build-system.requires` anymore. [#167](https://github.com/pdm-project/pdm/issues/167)

## Release v0.10.1 (2020-11-04)

### Bug Fixes

- Switch the PEP 517 build frontend from `build` to a home-grown version. [#162](https://github.com/pdm-project/pdm/issues/162)
- Synchronize the output of `LogWrapper`. [#164](https://github.com/pdm-project/pdm/issues/164)
- Fix a bug that `is_subset` and `is_superset` may return wrong result when wildcard excludes overlaps with the upper bound. [#165](https://github.com/pdm-project/pdm/issues/165)

## Release v0.10.0 (2020-10-20)

### Features & Improvements

- Change to Git style config command. [#157](https://github.com/pdm-project/pdm/issues/157)
- Add a command to generate scripts for autocompletion, which is backed by `pycomplete`. [#159](https://github.com/pdm-project/pdm/issues/159)

### Bug Fixes

- Fix a bug that `sitecustomize.py` incorrectly gets injected into the editable console scripts. [#158](https://github.com/pdm-project/pdm/issues/158)

## Release v0.9.2 (2020-10-13)

### Features & Improvements

- Cache the built wheels to accelerate resolution and installation process. [#153](https://github.com/pdm-project/pdm/issues/153)

### Bug Fixes

- Fix a bug that no wheel is matched when finding candidates to install. [#155](https://github.com/pdm-project/pdm/issues/155)
- Fix a bug that installation in parallel will cause encoding initialization error on Ubuntu. [#156](https://github.com/pdm-project/pdm/issues/156)

## Release v0.9.1 (2020-10-13)

### Features & Improvements

- Display plain text instead of spinner bar under verbose mode. [#150](https://github.com/pdm-project/pdm/issues/150)

### Bug Fixes

- Fix a bug that the result of `find_matched()` is exhausted when accessed twice. [#149](https://github.com/pdm-project/pdm/issues/149)

## Release v0.9.0 (2020-10-08)

### Features & Improvements

- Allow users to combine several dependency sections to form an extra require. [#131](https://github.com/pdm-project/pdm/issues/131)
- Split the PEP 517 backend to its own(battery included) package. [#134](https://github.com/pdm-project/pdm/issues/134)
- Add a new option to list command to show reverse dependency graph. [#137](https://github.com/pdm-project/pdm/issues/137)

### Bug Fixes

- Fix a bug that spaces in path causes requirement parsing error. [#138](https://github.com/pdm-project/pdm/issues/138)
- Fix a bug that requirement's python constraint is not respected when resolving. [#141](https://github.com/pdm-project/pdm/issues/141)

### Dependencies

- Update `pdm-pep517` to `0.2.0` that supports reading version from SCM. [#146](https://github.com/pdm-project/pdm/issues/146)

### Miscellany

- Add Python 3.9 to the CI version matrix to verify. [#144](https://github.com/pdm-project/pdm/issues/144)

## Release v0.8.7 (2020-09-04)

### Bug Fixes

- Fix a compatibility issue with `wheel==0.35`. [#135](https://github.com/pdm-project/pdm/issues/135)

## Release v0.8.6 (2020-07-09)

### Bug Fixes

- Fix a bug that extra sources are not respected when fetching distributions. [#127](https://github.com/pdm-project/pdm/issues/127)

## Release v0.8.5 (2020-06-24)

### Bug Fixes

- Fix a bug that `pdm export` fails when the project doesn't have `name` property. [#126](https://github.com/pdm-project/pdm/issues/126)

### Dependencies

- Upgrade dependency `pip` to `20.1`. [#125](https://github.com/pdm-project/pdm/issues/125)

## Release v0.8.4 (2020-05-21)

### Features & Improvements

- Add a new command `export` to export to alternative formats. [#117](https://github.com/pdm-project/pdm/issues/117)

### Miscellany

- Add Dockerfile and pushed to Docker Hub. [#122](https://github.com/pdm-project/pdm/issues/122)

## Release v0.8.3 (2020-05-15)

### Bug Fixes

- Fix the version constraint parsing of wheel metadata. [#120](https://github.com/pdm-project/pdm/issues/120)

## Release v0.8.2 (2020-05-03)

### Bug Fixes

- Update resolvers to `resolvelib` 0.4.0. [#118](https://github.com/pdm-project/pdm/issues/118)

## Release v0.8.1 (2020-04-22)

### Dependencies

- Switch to upstream `resolvelib 0.3.0`. [#116](https://github.com/pdm-project/pdm/issues/116)

## Release v0.8.0 (2020-04-20)

### Features & Improvements

- Add a new command to search for packages [#111](https://github.com/pdm-project/pdm/issues/111)
- Add `show` command to show package metadata. [#114](https://github.com/pdm-project/pdm/issues/114)

### Bug Fixes

- Fix a bug that environment markers cannot be evaluated correctly if extras are connected with "or". [#107](https://github.com/pdm-project/pdm/issues/107)
- Don't consult PyPI JSON API by default for package metadata. [#112](https://github.com/pdm-project/pdm/issues/112)
- Eliminate backslashes in markers for TOML documents. [#115](https://github.com/pdm-project/pdm/issues/115)

## Release v0.7.1 (2020-04-13)

### Bug Fixes

- Editable packages requires `setuptools` to be installed in the isolated environment.

## Release v0.7.0 (2020-04-12)

### Features & Improvements

- Disable loading of site-packages under PEP 582 mode. [#100](https://github.com/pdm-project/pdm/issues/100)

### Bug Fixes

- Fix a bug that TOML parsing error is not correctly captured. [#101](https://github.com/pdm-project/pdm/issues/101)
- Fix a bug of building wheels with C extensions that the platform in file name is incorrect. [#99](https://github.com/pdm-project/pdm/issues/99)

## Release v0.6.5 (2020-04-07)

### Bug Fixes

- Unix style executable script suffix is missing.

## Release v0.6.4 (2020-04-07)

### Features & Improvements

- Update shebang lines in the executable scripts when doing `pdm use`. [#96](https://github.com/pdm-project/pdm/issues/96)
- Auto-detect commonly used venv directories. [#97](https://github.com/pdm-project/pdm/issues/97)

## Release v0.6.3 (2020-03-30)

### Bug Fixes

- Fix a bug of moving files across different file system. [#95](https://github.com/pdm-project/pdm/issues/95)

## Release v0.6.2 (2020-03-29)

### Bug Fixes

- Validate user input for `python_requires` when initializing project. [#89](https://github.com/pdm-project/pdm/issues/89)
- Ensure `wheel` package is available before building packages. [#90](https://github.com/pdm-project/pdm/issues/90)
- Fix an issue of remove command that will unexpectedly uninstall packages in default section. [#92](https://github.com/pdm-project/pdm/issues/92)

### Dependencies

- Update dependencies `pythonfinder`, `python-cfonts`, `pip-shims` and many others. Drop dependency `vistir`. [#89](https://github.com/pdm-project/pdm/issues/89)

## Release v0.6.1 (2020-03-25)

### Features & Improvements

- Redirect output messages to log file for installation and locking. [#84](https://github.com/pdm-project/pdm/issues/84)

### Bug Fixes

- Fix a bug that parallel installation fails due to setuptools reinstalling. [#83](https://github.com/pdm-project/pdm/issues/83)

## Release v0.6.0 (2020-03-20)

### Features & Improvements

- Support specifying build script for C extensions. [#23](https://github.com/pdm-project/pdm/issues/23)
- Add test cases for `pdm build`. [#81](https://github.com/pdm-project/pdm/issues/81)
- Make it configurable whether to consult PyPI JSON API since it may be not trustable.
- Support parallel installation.
- Add new command `pmd import` to import project metadata from `Pipfile`, `poetry`, `flit`, `requirements.txt`. [#79](https://github.com/pdm-project/pdm/issues/79)
- `pdm init` and `pdm install` will auto-detect possible files that can be imported.

### Bug Fixes

- Fix wheel builds when `package_dir` is mapped. [#81](https://github.com/pdm-project/pdm/issues/81)
- `pdm init` will use the current directory rather than finding the parents when global project is not activated.

## Release v0.5.0 (2020-03-14)

### Features & Improvements

- Introduce a super easy-to-extend plug-in system to PDM. [#75](https://github.com/pdm-project/pdm/issues/75)

### Improved Documentation

- Documentation on how to write a plugin. [#75](https://github.com/pdm-project/pdm/issues/75)

### Bug Fixes

- Fix a typo in metadata parsing from `plugins` to `entry_points`

## Release v0.4.2 (2020-03-13)

### Features & Improvements

- Refactor the CLI part, switch from `click` to `argparse`, for better extensibility. [#73](https://github.com/pdm-project/pdm/issues/73)
- Allow users to configure to install packages into venv when it is activated. [#74](https://github.com/pdm-project/pdm/issues/74)

## Release v0.4.1 (2020-03-11)

### Features & Improvements

- Add a minimal dependency set for global project. [#72](https://github.com/pdm-project/pdm/issues/72)

## Release v0.4.0 (2020-03-10)

### Features & Improvements

- Global project support
- Add a new option `-g/--global` to manage global project. The default location is at `~/.pdm/global-project`.
- Use the virtualenv interpreter when detected inside an activated venv.
- Add a new option `-p/--project` to select project root other than the default one. [#30](https://github.com/pdm-project/pdm/issues/30)
- Add a new command `pdm config del` to delete an existing config item. [#71](https://github.com/pdm-project/pdm/issues/71)

### Bug Fixes

- Fix a URL parsing issue that username will be dropped in the SSH URL. [#68](https://github.com/pdm-project/pdm/issues/68)

### Improved Documentation

- Add docs for global project and selecting project path. [#30](https://github.com/pdm-project/pdm/issues/30)

## Release v0.3.2 (2020-03-08)

### Features & Improvements

- Display all available Python interpreters if users don't give one in `pdm init`. [#67](https://github.com/pdm-project/pdm/issues/67)

### Bug Fixes

- Regard `4.0` as infinite upper bound when checking subsetting. [#66](https://github.com/pdm-project/pdm/issues/66)

## Release v0.3.1 (2020-03-07)

### Bug Fixes

- Fix a bug that `ImpossiblePySpec`'s hash clashes with normal one.

## Release v0.3.0 (2020-02-28)

### Features & Improvements

- Add a new command `pdm config` to inspect configurations. [#26](https://github.com/pdm-project/pdm/issues/26)
- Add a new command `pdm cache clear` to clean caches. [#63](https://github.com/pdm-project/pdm/issues/63)

### Bug Fixes

- Correctly show dependency graph when circular dependencies exist. [#62](https://github.com/pdm-project/pdm/issues/62)

### Improved Documentation

- Write the initial documentation for PDM. [#14](https://github.com/pdm-project/pdm/issues/14)

## Release v0.2.6 (2020-02-25)

### Features & Improvements

- Improve the user interface of selecting Python interpreter. [#54](https://github.com/pdm-project/pdm/issues/54)

### Bug Fixes

- Fix the wheel installer to correctly unparse the flags of console scripts. [#56](https://github.com/pdm-project/pdm/issues/56)
- Fix a bug that OS-dependent hashes are not saved. [#57](https://github.com/pdm-project/pdm/issues/57)

## Release v0.2.5 (2020-02-22)

### Features & Improvements

- Allow specifying Python interpreter via `--python` option in `pdm init`. [#49](https://github.com/pdm-project/pdm/issues/49)
- Set `python_requires` when initializing and defaults to `>={current_version}`. [#50](https://github.com/pdm-project/pdm/issues/50)

### Bug Fixes

- Always consider wheels before tarballs; correctly merge markers from different parents. [#47](https://github.com/pdm-project/pdm/issues/47)
- Filter out incompatible wheels when installing. [#48](https://github.com/pdm-project/pdm/issues/48)

## Release v0.2.4 (2020-02-21)

### Bug Fixes

- Use the project local interpreter to build wheels. [#43](https://github.com/pdm-project/pdm/issues/43)
- Correctly merge Python specifiers when possible. [#4](https://github.com/pdm-project/pdm/issues/4)

## Release v0.2.3 (2020-02-21)

### Bug Fixes

- Fix a bug that editable build generates a malformed `setup.py`.

## Release v0.2.2 (2020-02-20)

### Features & Improvements

- Add a fancy greeting banner when user types `pdm --help`. [#42](https://github.com/pdm-project/pdm/issues/42)

### Bug Fixes

- Fix the RECORD file in built wheel. [#41](https://github.com/pdm-project/pdm/issues/41)

### Dependencies

- Add dependency `python-cfonts` to display banner. [#42](https://github.com/pdm-project/pdm/issues/42)

## Release v0.2.1 (2020-02-18)

### Bug Fixes

- Fix a bug that short python_version markers can't be parsed correctly. [#38](https://github.com/pdm-project/pdm/issues/38)
- Make `_editable_install.py` compatible with Py2.

## Release v0.2.0 (2020-02-14)

### Features & Improvements

- New option: `pdm list --graph` to show a dependency graph of the working set. [#10](https://github.com/pdm-project/pdm/issues/10)
- New option: `pdm update --unconstrained` to ignore the version constraint of given packages. [#13](https://github.com/pdm-project/pdm/issues/13)
- Improve the error message when project is not initialized before running commands. [#19](https://github.com/pdm-project/pdm/issues/19)
- Pinned candidates in lock file are reused when relocking during `pdm install`. [#33](https://github.com/pdm-project/pdm/issues/33)
- Use the pyenv interpreter value if pyenv is installed. [#36](https://github.com/pdm-project/pdm/issues/36)
- Introduce a new command `pdm info` to show project environment information. [#9](https://github.com/pdm-project/pdm/issues/9)

### Bug Fixes

- Fix a bug that candidate hashes will be lost when reused. [#11](https://github.com/pdm-project/pdm/issues/11)

### Dependencies

- Update `pip` to `20.0`, update `pip_shims` to `0.5.0`. [#28](https://github.com/pdm-project/pdm/issues/28)

### Miscellany

- Add a script named `setup_dev.py` for the convenience to setup pdm for development. [#29](https://github.com/pdm-project/pdm/issues/29)

## Release v0.1.2 (2020-02-09)

### Features

- New command pdm use to switch python versions. [#8](https://github.com/pdm-project/pdm/issues/8)
- New option pdm list --graph to show a dependency graph. [#10](https://github.com/pdm-project/pdm/issues/10)
- Read metadata from lockfile when pinned candidate is reused.

## Release v0.1.1 (2020-02-07)

### Features

- Get version from the specified file. [#6](https://github.com/pdm-project/pdm/issues/6)
- Add column header to pdm list output.

## Release v0.1.0 (2020-02-07)

### Bugfixes

- Pass exit code to parent process in pdm run.
- Fix error handling for CLI. [#19](https://github.com/pdm-project/pdm/issues/19)

### Miscellany

- Refactor the installer mocking for tests.

## Release v0.0.5 (2020-01-22)

### Improvements

- Ensure pypi index url is fetched in addition to the source settings. [#3](https://github.com/pdm-project/pdm/issues/3)

### Bugfixes

- Fix an issue that leading "c"s are mistakenly stripped. [#5](https://github.com/pdm-project/pdm/issues/5)
- Fix an error with PEP 517 building.

## Release v0.0.4 (2020-01-22)

### Improvements

- Fix editable installation, now editable scripts can also be executed from outside!
- Content hash is calculated based on dependencies and sources, not other metadata.

### Bugfixes

- Fix an issue that editable distributions can not be removed.

## Release v0.0.3 (2020-01-22)

### Features

- Add `pdm init` to bootstrap a project.

## Release v0.0.2 (2020-01-22)

### Features

- A complete functioning PEP 517 build backend.
- `pdm build` command.

### Miscellany

- Add a Chinese README

### Features

- Add `pdm init` to bootstrap a project.

## Release v0.0.1 (2020-01-20)

### Features

- A dependency resolver that just works.
- A PEP 582 installer.
- PEP 440 version specifiers.
- PEP 508 environment markers.
- Running scripts with PEP 582 local packages.
- Console scripts are injected with local paths.
- A neat CLI.
- add, lock, list, update, remove commands.
- PEP 517 build backends.
- Continuous Integration.

# Contributing to PDM

First off, thanks for taking the time to contribute! Contributions include but are not restricted to:

- Reporting bugs
- Contributing to code
- Writing tests
- Writing documentation

The following is a set of guidelines for contributing.

## A recommended flow of contributing to an Open Source project

This section is for beginners to OSS. If you are an experienced OSS developer, you can skip this section.

1. First, fork this project to your own namespace using the fork button at the top right of the repository page.

1. Clone the **upstream** repository to local:

   ```
   git clone https://github.com/pdm-project/pdm.git
   # Or if you prefer SSH clone:
   git clone git@github.com:pdm-project/pdm.git
   ```

1. Add the fork as a new remote:

   ```
   git remote add fork https://github.com/yourname/pdm.git
   git fetch fork
   ```

Where `fork` is the remote name of the fork repository.

**ProTips:**

1. Don't modify code on the main branch, the main branch should always keep track of origin/main.

   To update main branch to date:

   ```
   git pull origin main
   # In rare cases that your local main branch diverges from the remote main:
   git fetch origin && git reset --hard main
   ```

1. Create a new branch based on the up-to-date main branch for new patches.

1. Create a Pull Request from that patch branch.

## Local development

We recommend working in a virtual environment. Feel free to create a virtual environment with either the `venv` module or the `virtualenv` tool. For example:

```
python -m venv .venv
. .venv/bin/activate  # linux
.venv/Scripts/activate  # windows
```

Make sure your `pip` is newer than `21.3` to install PDM in develop/editable mode:

```
python -m pip install -U "pip>=21.3"
python -m pip install -e .
```

Make sure PDM uses the virtual environment you just created:

```
pdm config -l python.use_venv true
pdm config -l venv.in_project true
```

Install PDM development dependencies:

```
pdm install
```

Now, all dependencies are installed into the Python environment you chose, which will be used for development after this point.

### Run tests

```
pdm run test
```

Faster test using pytest-xdist:

```
pdm run test -n auto
```

The test suite is still simple and needs expansion! Please help write more test cases.

Note

You can also run your test suite against all supported Python version using `tox` with the `tox-pdm` plugin. You can either run it by yourself with:

```
tox
```

Or from `pdm` with:

```
pdm run tox
```

### Code style

PDM uses pre-commit hooks for linting. You need to install [prek](https://github.com/j178/prek) to run the hooks.

Please refer to the [prek documentation](https://github.com/j178/prek?tab=readme-ov-file#installation) and install it with your preferred method.

Then you can install the hooks by running:

```
prek install
```

You can now lint the code with:

```
pdm run lint
```

PDM uses `ruff` for code style and sorting import statements. If you are not following them, the CI will fail and your Pull Request will not be merged.

### News fragments

When you make changes such as fixing a bug or adding a feature, you must add a news fragment describing your change.

News fragments are placed in the `news/` directory, and should be named according to this pattern: `<issue_num>.<issue_type>.md` (e.g., `566.bugfix.md`).

#### Issue Types

- `feature`: Features and improvements
- `bugfix`: Bug fixes
- `refactor`: Code restructures
- `doc`: Added or improved documentation
- `dep`: Changes to dependencies
- `removal`: Removals or deprecations in the API
- `misc`: Miscellaneous changes that don't fit any of the other categories

The contents of the file should be a single sentence in the imperative mood that describes your changes. (e.g. `Deduplicate the plugins list.` )

See entries in the [Change Log](/CHANGELOG.md) for more examples.

### Preview the documentation

PDM docs development requires a few additional dependencies. Install them as:

```
sudo apt install libffi-dev # Or equivalent with the package manager of your choice
```

Now, whenever you make some changes to the `docs/` and you want to preview the build result, simply do:

```
pdm run doc
```

## Release

Once all changes are done and ready to release, you can preview the changelog contents by running:

```
pdm run release --dry-run
```

Make sure the next version and the changelog are as expected in the output.

Then cut a release on the **main** branch:

```
pdm run release
```

GitHub action will create the release and upload the distributions to PyPI.

Read more options about version bumping by `pdm run release --help`.

# Pytest fixtures

Some reusable fixtures for `pytest`.

+++ 2.4.0

To enable them in your test, add `pdm.pytest` as a plugin. You can do so in your root `conftest.py`:

```
# single plugin
pytest_plugins = "pytest.plugin"

# many plugins
pytest_plugins = [
    ...
    "pdm.pytest",
    ...
]
```

## `IndexMap = dict[str, Path]`

Path some root-relative http paths to some local paths

## `IndexOverrides = dict[str, bytes]`

PyPI indexes overrides fixture format

## `IndexesDefinition = dict[str, Union[tuple[IndexMap, IndexOverrides, bool], IndexMap]]`

Mock PyPI indexes format

## `Distribution`

A mock Distribution

## `LocalIndexTransport`

Bases: `BaseTransport`

A local file transport for HTTPX.

Allows to mock some HTTP requests with some local files

## `MockWorkingSet`

Bases: `MutableMapping`

A mock working set

## `PDMCallable`

Bases: `Protocol`

The PDM fixture callable signature

### `__call__(args, strict=False, input=None, obj=None, env=None, cleanup=True, **kwargs)`

Parameters:

| Name     | Type                | Description                                                   | Default                                                             |
| -------- | ------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- |
| `args`   | \`str               | list[str]\`                                                   | the command arguments as a single lexable string or a strings array |
| `strict` | `bool`              | raise an exception on failure instead of returning if enabled | `False`                                                             |
| `input`  | \`str               | None\`                                                        | an optional string to be submitted too stdin                        |
| `obj`    | \`Project           | None\`                                                        | an optional existing Project.                                       |
| `env`    | \`Mapping[str, str] | None\`                                                        | override the environment variables with those                       |

Returns:

| Type        | Description        |
| ----------- | ------------------ |
| `RunResult` | The command result |

## `RunResult`

Store a command execution result.

### `exception = None`

If set, the exception raised on execution

### `exit_code`

The execution exit code

### `output`

The execution `stdout` output (`stdout` alias)

### `outputs`

The execution `stdout` and `stderr` outputs concatenated

### `stderr`

The execution `stderr` output

### `stdout`

The execution `stdout` output

### `print()`

A debugging facility

## `TestRepository`

Bases: `BaseRepository`

A mock repository to ease testing dependencies

## `build_env(build_env_wheels, tmp_path_factory)`

A fixture build environment

Parameters:

| Name               | Type             | Description                                   | Default    |
| ------------------ | ---------------- | --------------------------------------------- | ---------- |
| `build_env_wheels` | `Iterable[Path]` | a list of wheel to install in the environment | *required* |

Returns:

| Type   | Description                          |
| ------ | ------------------------------------ |
| `Path` | The build environment temporary path |

## `build_env_wheels()`

Expose some wheels to be installed in the build environment.

Override to provide your owns.

Returns:

| Type             | Description                       |
| ---------------- | --------------------------------- |
| `Iterable[Path]` | a list of wheels paths to install |

## `local_finder_artifacts()`

The local finder search path as a fixture

Override to provides your own artifacts.

Returns:

| Type   | Description                    |
| ------ | ------------------------------ |
| `Path` | The path to the artifacts root |

## `pdm(core, monkeypatch)`

A fixture allowing to execute PDM commands

Returns:

| Type          | Description            |
| ------------- | ---------------------- |
| `PDMCallable` | A pdm fixture command. |

## `project(project_no_init)`

A fixture creating an initialized test project for the current test.

Returns:

| Type      | Description             |
| --------- | ----------------------- |
| `Project` | The initialized project |

## `project_no_init(tmp_path, mocker, core, build_test_session, monkeypatch, build_env)`

A fixture creating a non-initialized test project for the current test.

Returns:

| Type      | Description                 |
| --------- | --------------------------- |
| `Project` | The non-initialized project |

## `pypi_indexes()`

Provides some mocked PyPI entries

Returns:

| Type                | Description                        |
| ------------------- | ---------------------------------- |
| `IndexesDefinition` | a definition of the mocked indexes |

## `remove_pep582_path_from_pythonpath(pythonpath)`

Remove all pep582 paths of PDM from PYTHONPATH

## `repository(core, mocker, repository_pypi_json, local_finder)`

A fixture providing a mock PyPI repository

Returns:

| Type             | Description       |
| ---------------- | ----------------- |
| `RepositoryData` | A mock repository |

## `repository_pypi_json()`

The test repository fake PyPI definition path as a fixture

Override to provides your own definition path.

Returns:

| Type   | Description                                        |
| ------ | -------------------------------------------------- |
| `Path` | The path to a fake PyPI repository JSON definition |

## `venv_backends(project, request)`

A fixture iterating over `venv` backends

## `working_set(mocker, repository)`

a mock working set as a fixture

Returns:

| Type             | Description        |
| ---------------- | ------------------ |
| `MockWorkingSet` | a mock working set |

# PDM Plugins

PDM is aiming at being a community driven package manager. It is shipped with a full-featured plug-in system, with which you can:

- Develop a new command for PDM
- Add additional options to existing PDM commands
- Change PDM's behavior by reading additional config items
- Control the process of dependency resolution or installation

## What should a plugin do

The core PDM project focuses on dependency management and package publishing. Other functionalities you wish to integrate with PDM are preferred to lie in their own plugins and released as standalone PyPI projects. In case the plugin is considered a good supplement of the core project it may have a chance to be absorbed into PDM.

## Write your own plugin

In the following sections, I will show an example of adding a new command `hello` which reads the `hello.name` config.

### Write the command

The PDM's CLI module is designed in a way that user can easily "inherit and modify". To write a new command:

```
from pdm.cli.commands.base import BaseCommand

class HelloCommand(BaseCommand):
    """Say hello to the specified person.
    If none is given, will read from "hello.name" config.
    """

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", help="the person's name to whom you greet")

    def handle(self, project, options):
        if not options.name:
            name = project.config["hello.name"]
        else:
            name = options.name
        print(f"Hello, {name}")
```

First, let's create a new `HelloCommand` class inheriting from `pdm.cli.commands.base.BaseCommand`. It has two major functions:

- `add_arguments()` to manipulate the argument parser passed as the only argument, where you can add additional command line arguments to it
- `handle()` to do something when the subcommand is matched, you can do nothing by writing a single `pass` statement. It accepts two arguments: an `pdm.project.Project` object as the first one and the parsed `argparse.Namespace` object as the second.

The document string will serve as the command help text, which will be shown in `pdm --help`.

Besides, PDM's subcommand has two default options: `-v/--verbose` to change the verbosity level and `-g/--global` to enable global project. If you don't want these default options, override the `arguments` class attribute to a list of `pdm.cli.options.Option` objects, or assign it to an empty list to have no default options:

```
class HelloCommand(BaseCommand):

    arguments = []
```

Note

The default options are loaded first, then `add_arguments()` is called.

### Register the command to the core object

Write a function somewhere in your plugin project. There is no limit on what the name of the function is, but the function should take only one argument -- the PDM core object:

```
def hello_plugin(core):
    core.register_command(HelloCommand, "hello")
```

Call `core.register_command()` to register the command. The second argument as the name of the subcommand is optional. PDM will look for the `HelloCommand`'s `name` attribute if the name is not passed.

### Add a new config item

Let's recall the first code snippet, `hello.name` config key is consulted for the name if not passed via the command line.

```
class HelloCommand(BaseCommand):
    """Say hello to the specified person.
    If none is given, will read from "hello.name" config.
    """

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", help="the person's name to whom you greet")

    def handle(self, project, options):
        if not options.name:
            name = project.config["hello.name"]
        else:
            name = options.name
        print(f"Hello, {name}")
```

Till now, if you query the config value by `pdm config get hello.name`, an error will pop up saying it is not a valid config key. You need to register the config item, too:

```
from pdm.project.config import ConfigItem

def hello_plugin(core):
    core.register_command(HelloCommand, "hello")
    core.add_config("hello.name", ConfigItem("The person's name", "John"))
```

where `ConfigItem` class takes 4 parameters, in the following order:

- `description`: a description of the config item
- `default`: default value of the config item
- `global_only`: whether the config is allowed to set in home config only
- `env_var`: the name of environment variable which will be read as the config value

### Other plugin points

Besides of commands and configurations, the `core` object exposes some other methods and attributes to override. PDM also provides some signals you can listen to. Please read the [API reference](../../reference/api/) for more details.

### Tips about developing a PDM plugin

When developing a plugin, one hopes to activate and plugin in development and get updated when the code changes.

You can achieve this by installing the plugin in editable mode. To do this, specify the dependencies in `tool.pdm.plugins` array:

```
[tool.pdm]
plugins = [
    "-e file:///${PROJECT_ROOT}"
]
```

Then install it with:

```
pdm install --plugins
```

After that, all the dependencies are available in a project plugin library, including the plugin itself, in editable mode. That means any change to the codebase will take effect immediately without re-installation. The `pdm` executable also uses a Python interpreter under the hood, so if you run `pdm` from inside the plugin project, the plugin in development will be activated automatically, and you can do some testing to see how it works.

### Testing your plugin

PDM exposes some pytest fixtures as a plugin in the [`pdm.pytest`](../fixtures/) module. To benefit from them, you must add `pdm[pytest]` as a test dependency.

To enable them in your test, add `pdm.pytest` as a plugin. You can do so by in your root `conftest.py`:

```
# single plugin
pytest_plugins = "pytest.plugin"

# many plugins
pytest_plugins = [
    ...
    "pdm.pytest",
    ...
]
```

You can see some usage examples into PDM own [tests](https://github.com/pdm-project/pdm/tree/main/tests), especially the [conftest.py file](https://github.com/pdm-project/pdm/blob/main/tests/conftest.py) for configuration.

See the [pytest fixtures documentation](../fixtures/) for more details.

## Publish your plugin

Now you have defined your plugin already, let's distribute it to PyPI. PDM's plugins are discovered by entry point types. Create an `pdm` entry point and point to your plugin callable (yeah, it doesn't need to be a function, any callable object can work):

**PEP 621**:

```
# pyproject.toml

[project.entry-points.pdm]
hello = "my_plugin:hello_plugin"
```

**setuptools**:

```
# setup.py

setup(
    ...
    entry_points={"pdm": ["hello = my_plugin:hello_plugin"]}
    ...
)
```

## Activate the plugin

As plugins are loaded via entry points, they can be activated with no more steps than just installing the plugin. For convenience, PDM provides a `plugin` command group to manage plugins.

Assume your plugin is published as `pdm-hello`:

```
pdm self add pdm-hello
```

Now type `pdm --help` in the terminal, you will see the new added `hello` command and use it:

```
$ pdm hello Jack
Hello, Jack
```

See more plugin management subcommands by typing `pdm self --help` in the terminal.

## Specify the plugins in project

To specify the required plugins for a project, you can use the `tool.pdm.plugins` config in the `pyproject.toml` file. These dependencies can be installed into a project plugin library by running `pdm install --plugins`. The project plugin library will be loaded in subsequent PDM commands.

This is useful when you want to share the same plugin set with the contributors.

```
# pyproject.toml
[tool.pdm]
plugins = [
    "pdm-packer"
]
```

Run `pdm install --plugins` to install and activate the plugins.

Alternatively, you can have project-local plugins that are not published to PyPI, by using editable local dependencies:

```
# pyproject.toml
[tool.pdm]
plugins = [
    "-e file:///${PROJECT_ROOT}/plugins/my_plugin"
]
```
