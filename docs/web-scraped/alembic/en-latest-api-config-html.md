# Source: https://alembic.sqlalchemy.org/en/latest/api/config.html

Title: Configuration — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/config.html

Markdown Content:
Contents
--------

*   [`CommandFunction`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandFunction)
*   [`CommandLine`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine)
    *   [`CommandLine.main()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine.main)
    *   [`CommandLine.register_command()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine.register_command)

*   [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config)
    *   [`Config.attributes`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.attributes)
    *   [`Config.cmd_opts`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.cmd_opts)
    *   [`Config.config_file_name`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.config_file_name)
    *   [`Config.config_ini_section`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.config_ini_section)
    *   [`Config.file_config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.file_config)
    *   [`Config.get_alembic_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_alembic_option)
    *   [`Config.get_main_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_main_option)
    *   [`Config.get_section()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_section)
    *   [`Config.get_section_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_section_option)
    *   [`Config.get_template_directory()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_template_directory)
    *   [`Config.messaging_opts`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.messaging_opts)
    *   [`Config.print_stdout()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.print_stdout)
    *   [`Config.set_main_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_main_option)
    *   [`Config.set_section_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_section_option)
    *   [`Config.toml_alembic_config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.toml_alembic_config)
    *   [`Config.toml_file_name`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.toml_file_name)

*   [`MessagingOptions`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.MessagingOptions)
*   [`main()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.main)

Configuration[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#configuration "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Note

this section discusses the **internal API of Alembic** as regards internal configuration constructs. This section is only useful for developers who wish to extend the capabilities of Alembic. For documentation on configuration of an Alembic environment, please see [Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

The [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object represents the configuration passed to the Alembic environment. From an API usage perspective, it is needed for the following use cases:

*   to create a [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory"), which allows you to work with the actual script files in a migration environment

*   to create an [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext"), which allows you to actually run the `env.py` module within the migration environment

*   to programmatically run any of the commands in the [Commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic-command-toplevel) module.

The [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") is _not_ needed for these cases:

*   to instantiate a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") directly - this object only needs a SQLAlchemy connection or dialect name.

*   to instantiate a [`Operations`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations "alembic.operations.Operations") object - this object only needs a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext").

class alembic.config.CommandFunction(_*args_, _**kwargs_)[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandFunction "Link to this definition")
A function that may be registered in the CLI as an alembic command. It must be a named function and it must accept a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object as the first argument.

Added in version 1.15.3.

class alembic.config.CommandLine(_prog:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine "Link to this definition")
Provides the command line interface to Alembic.

main(_argv:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine.main "Link to this definition")
Executes the command line with the provided arguments.

register_command(_fn:[CommandFunction](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandFunction "alembic.config.CommandFunction")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine.register_command "Link to this definition")
Registers a function as a CLI subcommand. The subcommand name matches the function name, the arguments are extracted from the signature and the help text is read from the docstring.

Added in version 1.15.3.

class alembic.config.Config(_file\_:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _toml\_file:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _ini\_section:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='alembic'_, _output\_buffer:[TextIO](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _stdout:[TextIO](https://docs.python.org/3/library/typing.html#typing.TextIO "(in Python v3.14)")=<\_io.TextIOWrapper name='<stdout>'mode='w'encoding='utf-8'>_, _cmd\_opts:[Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _config\_args:Mapping[str_, _~typing.Any]={}_, _attributes:Dict[str_, _~typing.Any]|None=None_)[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "Link to this definition")
Represent an Alembic configuration.

Within an `env.py` script, this is available via the [`EnvironmentContext.config`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.config "alembic.runtime.environment.EnvironmentContext.config") attribute, which in turn is available at `alembic.context`:

from alembic import context

some_param = context.config.get_main_option("my option")

When invoking Alembic programmatically, a new [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") can be created by passing the name of an .ini file to the constructor:

from alembic.config import Config
alembic_cfg = Config("/path/to/yourapp/alembic.ini")

With a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object, you can then run Alembic commands programmatically using the directives in [`alembic.command`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#module-alembic.command "alembic.command").

The [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object can also be constructed without a filename. Values can be set programmatically, and new sections will be created as needed:

from alembic.config import Config
alembic_cfg = Config()
alembic_cfg.set_main_option("script_location", "myapp:migrations")
alembic_cfg.set_main_option("sqlalchemy.url", "postgresql://foo/bar")
alembic_cfg.set_section_option("mysection", "foo", "bar")

Warning

When using programmatic configuration, make sure the `env.py` file in use is compatible with the target configuration; including that the call to Python `logging.fileConfig()` is omitted if the programmatic configuration doesn’t actually include logging directives.

For passing non-string values to environments, such as connections and engines, use the [`Config.attributes`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.attributes "alembic.config.Config.attributes") dictionary:

with engine.begin() as connection:
    alembic_cfg.attributes['connection'] = connection
    command.upgrade(alembic_cfg, "head")

Parameters:
*   **file_**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.file_) – name of the .ini file to open if an `alembic.ini` is to be used. This should refer to the `alembic.ini` file, either as a filename or a full path to the file. This filename if passed must refer to an **ini file in ConfigParser format** only.

*   **toml_file**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.toml_file) –

name of the pyproject.toml file to open if a `pyproject.toml` file is to be used. This should refer to the `pyproject.toml` file, either as a filename or a full path to the file. This file must be in toml format. Both [`Config.file_`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.file_ "alembic.config.Config") and [`Config.toml_file`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.toml_file "alembic.config.Config") may be passed simultaneously, or exclusively.

Added in version 1.16.0.

*   **ini_section**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.ini_section) – name of the main Alembic section within the .ini file

*   **output_buffer**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.output_buffer) – optional file-like input buffer which will be passed to the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") - used to redirect the output of “offline generation” when using Alembic programmatically.

*   **stdout**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.stdout) – buffer where the “print” output of commands will be sent. Defaults to `sys.stdout`.

*   **config_args**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.config_args) – A dictionary of keys and values that will be used for substitution in the alembic config file, as well as the pyproject.toml file, depending on which / both are used. The dictionary as given is **copied** to two new, independent dictionaries, stored locally under the attributes `.config_args` and `.toml_args`. Both of these dictionaries will also be populated with the replacement variable `%(here)s`, which refers to the location of the .ini and/or .toml file as appropriate.

*   **attributes**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.attributes) –

optional dictionary of arbitrary Python keys/values, which will be populated into the [`Config.attributes`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.attributes "alembic.config.Config.attributes") dictionary.

Construct a new [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")

attributes[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.attributes "Link to this definition")
A Python dictionary for storage of additional state.

This is a utility dictionary which can include not just strings but engines, connections, schema objects, or anything else. Use this to pass objects into an env.py script, such as passing a [`sqlalchemy.engine.base.Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") when calling commands from [`alembic.command`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#module-alembic.command "alembic.command") programmatically.

cmd_opts:[Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.cmd_opts "Link to this definition")
The command-line options passed to the `alembic` script.

Within an `env.py` script this can be accessed via the [`EnvironmentContext.config`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.config "alembic.runtime.environment.EnvironmentContext.config") attribute.

config_file_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.config_file_name "Link to this definition")
Filesystem path to the .ini file in use.

config_ini_section:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.config_ini_section "Link to this definition")
Name of the config file section to read basic configuration from. Defaults to `alembic`, that is the `[alembic]` section of the .ini file. This value is modified using the `-n/--name` option to the Alembic runner.

file_config[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.file_config "Link to this definition")
Return the underlying `ConfigParser` object.

Dir*-ect access to the .ini file is available here, though the [`Config.get_section()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_section "alembic.config.Config.get_section") and [`Config.get_main_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_main_option "alembic.config.Config.get_main_option") methods provide a possibly simpler interface.

get_alembic_option(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_alembic_option "Link to this definition")get_alembic_option(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
Return an option from the “[alembic]” or “[tool.alembic]” section of the configparser-parsed .ini file (e.g. `alembic.ini`) or toml-parsed `pyproject.toml` file.

The value returned is expected to be None, string, list of strings, or dictionary of strings. Within each type of string value, the `%(here)s` token is substituted out with the absolute path of the `pyproject.toml` file, as are other tokens which are extracted from the [`Config.config_args`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.params.config_args "alembic.config.Config") dictionary.

Searches always prioritize the configparser namespace first, before searching in the toml namespace.

If Alembic was run using the `-n/--name` flag to indicate an alternate main section name, this is taken into account **only** for the configparser-parsed .ini file. The section name in toml is always `[tool.alembic]`.

Added in version 1.16.0.

get_main_option(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_main_option "Link to this definition")get_main_option(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
Return an option from the ‘main’ section of the .ini file.

This defaults to being a key from the `[alembic]` section, unless the `-n/--name` flag were used to indicate a different section.

Does **NOT** consume from the pyproject.toml file.

See also

[`Config.get_alembic_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_alembic_option "alembic.config.Config.get_alembic_option") - includes pyproject support

get_section(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_section "Link to this definition")get_section(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)→[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]get_section(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)→[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]
Return all the configuration options from a given .ini file section as a dictionary.

If the given section does not exist, the value of `default` is returned, which is expected to be a dictionary or other mapping.

get_section_option(_section:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _default:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_section_option "Link to this definition")
Return an option from the given section of the .ini file.

get_template_directory()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_template_directory "Link to this definition")
Return the directory where Alembic setup templates are found.

This method is used by the alembic `init` and `list_templates` commands.

messaging_opts[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.messaging_opts "Link to this definition")
The messaging options.

print_stdout(_text:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _*arg:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.print_stdout "Link to this definition")
Render a message to standard out.

When [`Config.print_stdout()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.print_stdout "alembic.config.Config.print_stdout") is called with additional args those arguments will formatted against the provided text, otherwise we simply output the provided text verbatim.

This is a no-op when the``quiet`` messaging option is enabled.

e.g.:

>>> config.print_stdout('Some text %s', 'arg')
Some Text arg

set_main_option(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _value:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_main_option "Link to this definition")
Set an option programmatically within the ‘main’ section.

This overrides whatever was in the .ini file.

Parameters:
*   **name**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_main_option.params.name) – name of the value

*   **value**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_main_option.params.value) – the value. Note that this value is passed to `ConfigParser.set`, which supports variable interpolation using pyformat (e.g. `%(some_value)s`). A raw percent sign not part of an interpolation symbol must therefore be escaped, e.g. `%%`. The given value may refer to another value already in the file using the interpolation format.

set_section_option(_section:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _value:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_section_option "Link to this definition")
Set an option programmatically within the given section.

The section is created if it doesn’t exist already. The value here will override whatever was in the .ini file.

Does **NOT** consume from the pyproject.toml file.

See also

[`Config.get_alembic_option()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.get_alembic_option "alembic.config.Config.get_alembic_option") - includes pyproject support

Parameters:
*   **section**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_section_option.params.section) – name of the section

*   **name**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_section_option.params.name) – name of the value

*   **value**[¶](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.set_section_option.params.value) – the value. Note that this value is passed to `ConfigParser.set`, which supports variable interpolation using pyformat (e.g. `%(some_value)s`). A raw percent sign not part of an interpolation symbol must therefore be escaped, e.g. `%%`. The given value may refer to another value already in the file using the interpolation format.

toml_alembic_config[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.toml_alembic_config "Link to this definition")
Return a dictionary of the [tool.alembic] section from pyproject.toml

toml_file_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.toml_file_name "Link to this definition")
Filesystem path to the pyproject.toml file in use.

Added in version 1.16.0.

class alembic.config.MessagingOptions[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.MessagingOptions "Link to this definition")alembic.config.main(_argv:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _prog:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _**kwargs:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.main "Link to this definition")
The console runner function for Alembic.
