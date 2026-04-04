# Source: https://virtualenv.pypa.io/en/latest/reference/cli.html

Title: Command line - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/reference/cli.html

Markdown Content:
`virtualenv` is primarily a command line application. All options have sensible defaults, and there is one required argument: the name or path of the virtual environment to create.

See [Use virtualenv](https://virtualenv.pypa.io/en/latest/how-to/usage.html) for how to select Python versions, configure defaults, and use environment variables.

Command line options[¶](https://virtualenv.pypa.io/en/latest/reference/cli.html#command-line-options "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

**virtualenv [OPTIONS]**

**Named Arguments**
[`--version`](https://virtualenv.pypa.io/en/latest/reference/cli.html#version)`'==SUPPRESS=='`display the version of the virtualenv package and its location, then exit
[`--with-traceback`](https://virtualenv.pypa.io/en/latest/reference/cli.html#with-traceback)`False`on failure also display the stacktrace internals of virtualenv
[`--read-only-app-data`](https://virtualenv.pypa.io/en/latest/reference/cli.html#read-only-app-data)`False`use app data folder in read-only mode (write operations will fail with error)
[`--app-data`](https://virtualenv.pypa.io/en/latest/reference/cli.html#app-data)platform specific application data folder a data folder used as cache by the virtualenv
[`--reset-app-data`](https://virtualenv.pypa.io/en/latest/reference/cli.html#reset-app-data)`False`start with empty app data folder
[`--upgrade-embed-wheels`](https://virtualenv.pypa.io/en/latest/reference/cli.html#upgrade-embed-wheels)`False`trigger a manual update of the embedded wheels

**verbosity** ⇒ verbosity = verbose - quiet, default INFO, mapping => CRITICAL=0, ERROR=1, WARNING=2, INFO=3, DEBUG=4, NOTSET=5
[`-v`](https://virtualenv.pypa.io/en/latest/reference/cli.html#v), [`--verbose`](https://virtualenv.pypa.io/en/latest/reference/cli.html#verbose)`2`increase verbosity
[`-q`](https://virtualenv.pypa.io/en/latest/reference/cli.html#q), [`--quiet`](https://virtualenv.pypa.io/en/latest/reference/cli.html#quiet)`0`decrease verbosity

### discovery[¶](https://virtualenv.pypa.io/en/latest/reference/cli.html#section-discovery "Link to this heading")

**core** ⇒ options shared across all discovery
[`--discovery`](https://virtualenv.pypa.io/en/latest/reference/cli.html#discovery)`'builtin'`interpreter discovery method; choice of: `builtin`
[`-p`](https://virtualenv.pypa.io/en/latest/reference/cli.html#p), [`--python`](https://virtualenv.pypa.io/en/latest/reference/cli.html#python)the python executable virtualenv is installed into interpreter based on what to create environment (path/identifier/version-specifier) - by default use the interpreter where the tool is installed - first found wins. Version specifiers (e.g., >=3.12, ~=3.11.0, ==3.10) are also supported
[`--try-first-with`](https://virtualenv.pypa.io/en/latest/reference/cli.html#try-first-with)`[]`try first these interpreters before starting the discovery

### creator[¶](https://virtualenv.pypa.io/en/latest/reference/cli.html#section-creator "Link to this heading")

**core** ⇒ options shared across all creator
[`--creator`](https://virtualenv.pypa.io/en/latest/reference/cli.html#creator)`builtin` if exist, else `venv`create environment via; choice of: `cpython3-mac-brew`, `cpython3-mac-framework`, `cpython3-posix`, `cpython3-win`, `graalpy-posix`, `graalpy-win`, `pypy3-posix`, `pypy3-win`, `rustpython-posix`, `rustpython-win`, `venv`
[`dest`](https://virtualenv.pypa.io/en/latest/reference/cli.html#dest)directory to create virtualenv at
[`--clear`](https://virtualenv.pypa.io/en/latest/reference/cli.html#clear)`False`remove the destination directory if exist before starting (will overwrite files otherwise)
[`--no-vcs-ignore`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-vcs-ignore)`False`don’t create VCS ignore directive in the destination directory
[`--system-site-packages`](https://virtualenv.pypa.io/en/latest/reference/cli.html#system-site-packages)`False`give the virtual environment access to the system site-packages dir
[`--symlinks`](https://virtualenv.pypa.io/en/latest/reference/cli.html#symlinks)`True`try to use symlinks rather than copies, when symlinks are not the default for the platform
[`--copies`](https://virtualenv.pypa.io/en/latest/reference/cli.html#copies), [`--always-copy`](https://virtualenv.pypa.io/en/latest/reference/cli.html#always-copy)`False`try to use copies rather than symlinks, even when symlinks are the default for the platform

### seeder[¶](https://virtualenv.pypa.io/en/latest/reference/cli.html#section-seeder "Link to this heading")

**core** ⇒ options shared across all seeder
[`--seeder`](https://virtualenv.pypa.io/en/latest/reference/cli.html#seeder)`'app-data'`seed packages install method; choice of: `app-data`, `pip`
[`--no-seed`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-seed), [`--without-pip`](https://virtualenv.pypa.io/en/latest/reference/cli.html#without-pip)`False`do not install seed packages
[`--no-download`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-download), [`--never-download`](https://virtualenv.pypa.io/en/latest/reference/cli.html#never-download)`True`pass to disable download of the latest pip/setuptools/wheel from PyPI
[`--download`](https://virtualenv.pypa.io/en/latest/reference/cli.html#download)`False`pass to enable download of the latest pip/setuptools/wheel from PyPI
`[]`a path containing wheels to extend the internal wheel list (can be set 1+ times)
[`--pip`](https://virtualenv.pypa.io/en/latest/reference/cli.html#pip)`'bundle'`version of pip to install as seed: embed, bundle, none or exact version
[`--setuptools`](https://virtualenv.pypa.io/en/latest/reference/cli.html#setuptools)`'none'`version of setuptools to install as seed: embed, bundle, none or exact version
[`--no-pip`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-pip)`False`do not install pip
[`--no-setuptools`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-setuptools)`False`do not install setuptools
[`--no-periodic-update`](https://virtualenv.pypa.io/en/latest/reference/cli.html#no-periodic-update)`False`disable the periodic (once every 14 days) update of the embedded wheels

**app-data** ⇒ options specific to seeder app-data
[`--symlink-app-data`](https://virtualenv.pypa.io/en/latest/reference/cli.html#symlink-app-data)`False`symlink the python packages from the app-data folder (requires seed pip>=19.3)

### activators[¶](https://virtualenv.pypa.io/en/latest/reference/cli.html#section-activators "Link to this heading")

**core** ⇒ options shared across all activators
[`--activators`](https://virtualenv.pypa.io/en/latest/reference/cli.html#activators)comma separated list of activators supported activators to generate - default is all supported; choice of: `bash`, `batch`, `cshell`, `fish`, `nushell`, `powershell`, `python`
[`--prompt`](https://virtualenv.pypa.io/en/latest/reference/cli.html#prompt)provides an alternative prompt prefix for this environment (value of . means name of the current working directory)
