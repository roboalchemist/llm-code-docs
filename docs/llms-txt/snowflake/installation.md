# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/installation/installation.md

# Installing Snowflake CLI

This topic explains how to install Snowflake CLI on [supported platforms](../../../release-notes/requirements.md). Note that Snowflake CLI is not currently available for AIX systems.

Snowflake recommends using binary installation methods, such as package managers, to install Snowflake CLI on your system.
You can download the binary installers from the official [Snowflake CLI repository](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html).

## Requirements

* Before using Snowflake CLI, you must have a valid Snowflake account.
* To run Streamlit in Snowflake using Snowflake CLI, you must have a Snowflake account with permission to use Streamlit.
* To run Snowpark Container Services in Snowflake using Snowflake CLI, you must have a Snowflake account with privileges to use Snowpark Container Services.

> **Tip:**
>
> If your Snowflake account requires MFA (multi-factor authentication), Snowflake CLI requires approval for every command. You can use MFA caching to require
> authentication only once every four hours. For more information, see [Use multi-factor authentication (MFA)](../connecting/configure-connections.md).

## Install Snowflake CLI using package managers

To install Snowflake CLI using platform-specific package managers, use one of the following procedures:

* Install using Linux package managers (rpm, deb).
* Install using MacOS installer.
* Install using Windows installer.
* Install using Homebrew.

### Install with Linux package managers

If you use a Linux operating system, you can install Snowflake CLI with package managers that support the following:

* `deb` packages,
* `rpm` packages.

To install Snowflake CLI using the `deb` package manager:

1. Download the Snowflake CLI `deb` from the [Snowflake CLI repository](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html).
2. Install the package by running the following command:

   ```bash
   sudo dpkg -i snowflake-cli-<version>.deb
   ```

To install Snowflake CLI using the `rpm` package manager:

1. Download the Snowflake CLI `rpm` package from the [Snowflake CLI repository](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html).
2. Install the package by running the following command:

   ```bash
   sudo rpm -i snowflake-cli-<version>.rpm
   ```

3. To verify that the software was installed successfully, run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

4. [Configure the Snowflake connection](../connecting/connect.md).

### Install with the MacOS package installer

To install Snowflake CLI on MacOS, do the following:

1. Download the Snowflake CLI installer from the [Snowflake CLI repository](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html).
2. Run the installer and follow the instructions to install Snowflake CLI.
3. To verify that the software was installed successfully, open new terminal and run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

4. [Configure the Snowflake connection](../connecting/connect.md).

### Install with the Windows installer

To install Snowflake CLI on Windows, do the following:

1. Download the Snowflake CLI installer from the [Snowflake CLI repository](https://sfc-repo.snowflakecomputing.com/snowflake-cli/index.html).
2. Run the installer and follow the instructions to install Snowflake CLI.
3. To verify that the software was installed successfully, open new terminal and run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

4. [Configure the Snowflake connection](../connecting/connect.md).

### Install with Homebrew

If you use a Mac operating system, you can install Snowflake CLI with [Homebrew](https://brew.sh/).

1. Install [Homebrew](https://brew.sh/), if necessary.
2. To give Homebrew access to the Snowflake CLI repository, run the following command:

   ```bash
   brew tap snowflakedb/snowflake-cli
   brew update
   ```

3. To install Snowflake CLI, run the following command:

   ```bash
   brew install snowflake-cli
   ```

4. To verify that the software was installed successfully, run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

5. [Configure the Snowflake connection](../connecting/connect.md).

## Advanced local installations

You can also install Snowflake CLI as a Python package using either of the following:

* pip (PyPi)
* pipx

Snowflake recommends installing as a Python package only for development purposes or when installing binaries isn’t possible in your environment.

### Install with pip (PyPi)

> **Note:**
>
> This method modifies the Python environment where you install Snowflake CLI. Consider using pipx instead to avoid dependency conflicts.

To install Snowflake CLI using `pip`, you must have [Python](https://python.org) version 3.10 or later installed.

1. Run the following shell command:

   ```bash
   pip install snowflake-cli
   ```

2. To verify that the software was installed successfully, run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

3. [Configure the Snowflake connection](../connecting/connect.md).

### Install with pipx

[pipx](https://github.com/pypa/pipx) provides an alternative to `pip` that installs and executes Python packages into isolated virtual environments. Installing Snowflake CLI with `pipx` does not, therefore, modify your current Python environment.

To install Snowflake CLI using `pipx`, you must have [pipx](https://github.com/pypa/pipx) installed.

1. Run the following shell command:

   ```bash
   pipx install snowflake-cli
   ```

2. To verify that the software was installed successfully, run the following command:

   ```bash
   snow --help
   ```

   ```output
   Usage: snow [OPTIONS] COMMAND [ARGS]...

   Snowflake CLI tool for developers.

   ╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ --version                           Shows version of the Snowflake CLI                                                                   │
   │ --info                              Shows information about the Snowflake CLI                                                            │
   │ --config-file                 FILE  Specifies Snowflake CLI configuration file that should be used [default: None]                       │
   │ --install-completion                Install completion for the current shell.                                                            │
   │ --show-completion                   Show completion for the current shell, to copy it or customize the installation.                     │
   │ --help                -h            Show this message and exit.                                                                          │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
   │ app          Manages a Snowflake Native App                                                                                              │
   │ connection   Manages connections to Snowflake.                                                                                           │
   │ cortex       Provides access to Snowflake Cortex.                                                                                        │
   │ git          Manages git repositories in Snowflake.                                                                                      │
   │ notebook     Manages notebooks in Snowflake.                                                                                             │
   │ object       Manages Snowflake objects like warehouses and stages                                                                        │
   │ snowpark     Manages procedures and functions.                                                                                           │
   │ spcs         Manages Snowpark Container Services compute pools, services, image registries, and image repositories.                      │
   │ sql          Executes Snowflake query.                                                                                                   │
   │ stage        Manages stages.                                                                                                             │
   │ streamlit    Manages a Streamlit app in Snowflake.                                                                                       │
   ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
   ```

3. [Configure the Snowflake connection](../connecting/connect.md).

## Installing Snowflake CLI in FIPS-compliant environments

You can use a Docker image to install Snowflake CLI in an environment that is compliant with FIPS (Federal Information Processing Standards).

### Prerequisites

Before installing Snowflake CLI in a FIPS-compliant environment, ensure that you meet the following prerequisites:

* **FIPS-compliant Python**: Python must be preinstalled, built, and configured for FIPS compliance. This typically means Python is linked against a FIPS-enabled OpenSSL library.
* **FIPS-enabled OpenSSL**: The system’s OpenSSL libraries must be FIPS-compliant and available to Python at runtime.
* **Build tools**: Standard build tools (such as a C compiler and Python development headers) must be available, as dependencies will be built from source.
* **Network Access**: The environment must allow access to PyPI or your internal package index for downloading source distributions.

### Install Snowflake CLI in a FIPS-compliant Dockerfile

To install Snowflake CLI in a FIPS-compliant environment, follow these steps:

1. Create a Python virtual environment in the container, as shown in the following example:

   ```bash
   python -m venv .venv
   ```

2. Activate the Python virtual environment in the container, as shown in the following example:

   ```bash
   source ~/.venv/bin/activate
   ```

3. Upgrade `pip` and `setuptools` in the container, as shown in the following example:

   ```bash
   pip install -U setuptools pip
   ```

4. Install the cryptography, Python connector, and Snowflake CLI dependencies from source in the container, as shown in the following example. Note that all dependencies must be installed from source to ensure they are built against your FIPS-compliant libraries.

   ```bash
   pip install cryptography==44.0.3 --no-binary cryptography
   pip install -U snowflake-connector-python[secure-local-storage] --no-binary snowflake-connector-python[secure-local-storage]
   pip install -U snowflake-cli --no-binary snowflake-cli
   ```

   The `--no-binary` option forces installation from source, ensuring that the builds use FIPS-ready libraries.

### Validate the Docker image

To confirm that your Python environment uses a FIPS-enabled OpenSSL library, enter the following command in the running container:

```bash
python -c "import ssl; print(ssl.OPENSSL_VERSION)"
```

After installing Snowflake CLI and validating the Docker image, you can use Snowflake CLI in the container.

```bash
snow <your-command>
```

where <*your-command*> is any valid Snowflake CLI command, such as `snow --help`.

## Install command auto-completion functionality

Snowflake CLI supports standard shell tab completion functionality.

To install auto-completion into Snowflake CLI, perform the following steps:

1. Run the `snow --install-completion` command:

   ```snowcli
   snow --install-completion
   ```

   ```output
   zsh completion installed in <user home>/.zfunc/_snow
   Completion will take effect once you restart the terminal
   ```

2. Run the `snow --show-completion` command to generate the commands you need to add to your shell profile (`.bashrc`, `.bash_profile`, `.zshrc`, and others):

   ```bash
   snow --show-completion
   ```

   ```output
   _snow_completion() {
      local IFS=$'
   '
      COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                     COMP_CWORD=$COMP_CWORD \
                     _SNOW_COMPLETE=complete_bash $1 ) )
      return 0
   }

   complete -o default -F _snow_completion snow
   ```

3. Select and copy the command output text.
4. Open your shell profile file, `.bashrc` in this example, and paste the copied text:

   ```output
   export SHELL=/bin/bash

   ...

   _snow_completion() {
      local IFS=$'
   '
      COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                     COMP_CWORD=$COMP_CWORD \
                     _SNOW_COMPLETE=complete_bash $1 ) )
      return 0
   }

   complete -o default -F _snow_completion snow
   ```

5. Save the file.
6. To activate the tab-completion functionality, restart your shell or `source` your shell profile file, such as:

   ```bash
   source ~/.bashrc
   ```

7. To test the feature, enter a snow command followed by a `TAB`, as shown:

   ```bash
   snow app [TAB]
   ```

   ```output
   deploy    init      open      run       teardown  version
   ```
