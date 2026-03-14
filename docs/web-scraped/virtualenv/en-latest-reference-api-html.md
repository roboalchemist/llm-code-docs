# Source: https://virtualenv.pypa.io/en/latest/reference/api.html

Title: Python - virtualenv

URL Source: https://virtualenv.pypa.io/en/latest/reference/api.html

Markdown Content:
The primary interface to `virtualenv` is the command line application. However, it can also be used programmatically via the `virtualenv.cli_run` function and the `Session` class.

See [Use virtualenv](https://virtualenv.pypa.io/en/latest/how-to/usage.html) for usage examples.

virtualenv module[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#module-virtualenv "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

virtualenv.cli_run(_args_, _options=None_, _setup\_logging=True_, _env=None_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.cli_run "Link to this definition")
Create a virtual environment given some command line interface arguments.

Parameters:

* **args** ([`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]) – the command line arguments

* **options** ([`VirtualEnvOptions`](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions "virtualenv.config.cli.parser.VirtualEnvOptions") | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")) – passing in a `VirtualEnvOptions` object allows return of the parsed options

* **setup_logging** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – `True` if setup logging handlers, `False` to use handlers already registered

* **env** ([`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "(in Python v3.14)")[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")) – environment variables to use

Return type:
[`Session`](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session "virtualenv.run.session.Session")

Returns:
the session object of the creation (its structure for now is experimental and might change on short notice)

virtualenv.session_via_cli(_args_, _options=None_, _setup\_logging=True_, _env=None_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.session_via_cli "Link to this definition")
Create a virtualenv session (same as cli_run, but this does not perform the creation). Use this if you just want to query what the virtual environment would look like, but not actually create it.

Parameters:

* **args** ([`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]) – the command line arguments

* **options** ([`VirtualEnvOptions`](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions "virtualenv.config.cli.parser.VirtualEnvOptions") | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")) – passing in a `VirtualEnvOptions` object allows return of the parsed options

* **setup_logging** ([`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – `True` if setup logging handlers, `False` to use handlers already registered

* **env** ([`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "(in Python v3.14)")[[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")) – environment variables to use

Return type:
[`Session`](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session "virtualenv.run.session.Session")

Returns:
the session object of the creation (its structure for now is experimental and might change on short notice)

Session class[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#session-class "Link to this heading")
--------------------------------------------------------------------------------------------------------------

The `Session` class represents a virtualenv creation session and provides access to the created environment’s properties.

class virtualenv.run.session.Session(_verbosity_, _app\_data_, _interpreter_, _creator_, _seeder_, _activators_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session "Link to this definition")
Represents a virtual environment creation session.

Parameters:

* **verbosity** ([`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"))

* **app_data** ([`AppData`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.app_data.base.AppData "virtualenv.app_data.base.AppData"))

* **interpreter** ([`PythonInfo`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo "python_discovery._py_info.PythonInfo"))

* **creator** ([`Creator`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator "virtualenv.create.creator.Creator"))

* **seeder** ([`Seeder`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.seed.seeder.Seeder "virtualenv.seed.seeder.Seeder"))

* **activators** ([`list`](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[`Activator`](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator "virtualenv.activation.activator.Activator")])

property verbosity:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session.verbosity "Link to this definition")
The verbosity of the run.

property interpreter:[PythonInfo](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.discovery.py_info.PythonInfo "python_discovery._py_info.PythonInfo")[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session.interpreter "Link to this definition")
Create a virtual environment based on this reference interpreter.

property creator:[Creator](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.create.creator.Creator "virtualenv.create.creator.Creator")[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session.creator "Link to this definition")
The creator used to build the virtual environment (must be compatible with the interpreter).

property seeder:[Seeder](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.seed.seeder.Seeder "virtualenv.seed.seeder.Seeder")[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session.seeder "Link to this definition")
The mechanism used to provide the seed packages (pip, setuptools, wheel).

property activators:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Activator](https://virtualenv.pypa.io/en/latest/plugin/api.html#virtualenv.activation.activator.Activator "virtualenv.activation.activator.Activator")][¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.run.session.Session.activators "Link to this definition")
Activators used to generate activations scripts.

VirtualEnvOptions[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenvoptions "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

Options namespace passed to plugin constructors, populated from the CLI, environment variables, and configuration files.

class virtualenv.config.cli.parser.VirtualEnvOptions(_**kwargs_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions "Link to this definition")Parameters:
**kwargs** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"))

set_src(_key_, _value_, _src_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions.set_src "Link to this definition")
Set an option value and record where it came from.

Parameters:

* **key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the option name

* **value** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")) – the option value

* **src** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the source of the value (e.g. `"cli"`, `"env var"`, `"default"`)

Return type:
[`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

get_source(_key_)[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions.get_source "Link to this definition")
Return the source that provided a given option value.

Parameters:
**key** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – the option name

Return type:
[`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")

Returns:
the source string (e.g. `"cli"`, `"env var"`, `"default"`), or `None` if not tracked

property verbosity:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[¶](https://virtualenv.pypa.io/en/latest/reference/api.html#virtualenv.config.cli.parser.VirtualEnvOptions.verbosity "Link to this definition")
The verbosity level, computed as `verbose - quiet`, clamped to zero.

Returns:
the verbosity level, or `None` if neither `--verbose` nor `--quiet` has been parsed yet
