# Source: https://alembic.sqlalchemy.org/en/latest/api/runtime.html

Title: Runtime Objects — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/runtime.html

Markdown Content:
Runtime Objects[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#runtime-objects "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

The “runtime” of Alembic involves the [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") and [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") objects. These are the objects that are in play once the `env.py` script is loaded up by a command and a migration operation proceeds.

The Environment Context[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#the-environment-context "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

The [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") class provides most of the API used within an `env.py` script. Within `env.py`, the instantiated [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") is made available via a special _proxy module_ called `alembic.context`. That is, you can import `alembic.context` like a regular Python module, and each name you call upon it is ultimately routed towards the current [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") in use.

In particular, the key method used within `env.py` is [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure"), which establishes all the details about how the database will be accessed.

class alembic.runtime.environment.EnvironmentContext(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _script:[ScriptDirectory](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory")_, _**kw:Any_)[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "Link to this definition")
A configurational facade made available in an `env.py` script.

The [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") acts as a _facade_ to the more nuts-and-bolts objects of [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") as well as certain aspects of [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config"), within the context of the `env.py` script that is invoked by most Alembic commands.

[`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") is normally instantiated when a command in [`alembic.command`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#module-alembic.command "alembic.command") is run. It then makes itself available in the `alembic.context` module for the scope of the command. From within an `env.py` script, the current [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") is available by importing this module.

[`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") also supports programmatic usage. At this level, it acts as a Python context manager, that is, is intended to be used using the `with:` statement. A typical use of [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext"):

from alembic.config import Config
from alembic.script import ScriptDirectory

config = Config()
config.set_main_option("script_location", "myapp:migrations")
script = ScriptDirectory.from_config(config)

def my_function(rev, context):
 '''do something with revision "rev", which
 will be the current database revision,
 and "context", which is the MigrationContext
 that the env.py will create'''

with EnvironmentContext(
    config,
    script,
    fn=my_function,
    as_sql=False,
    starting_rev="base",
    destination_rev="head",
    tag="sometag",
):
    script.run_env()

The above script will invoke the `env.py` script within the migration environment. If and when `env.py` calls [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations"), the `my_function()` function above will be called by the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext"), given the context itself as well as the current revision in the database.

Note

For most API usages other than full blown invocation of migration scripts, the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") and [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") objects can be created and used directly. The [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") object is _only_ needed when you need to actually invoke the `env.py` module present in the migration environment.

Construct a new [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext").

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **script**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.params.script) – a [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") instance.

*   ****kw**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.params.**kw) – keyword options that will be ultimately passed along to the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") when [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") is called.

begin_transaction()→_ProxyTransaction|[ContextManager](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"),[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.begin_transaction "Link to this definition")
Return a context manager that will enclose an operation within a “transaction”, as defined by the environment’s offline and transactional DDL settings.

e.g.:

with context.begin_transaction():
    context.run_migrations()

[`begin_transaction()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.begin_transaction "alembic.runtime.environment.EnvironmentContext.begin_transaction") is intended to “do the right thing” regardless of calling context:

*   If [`is_transactional_ddl()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.is_transactional_ddl "alembic.runtime.environment.EnvironmentContext.is_transactional_ddl") is `False`, returns a “do nothing” context manager which otherwise produces no transactional state or directives.

*   If [`is_offline_mode()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.is_offline_mode "alembic.runtime.environment.EnvironmentContext.is_offline_mode") is `True`, returns a context manager that will invoke the [`DefaultImpl.emit_begin()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.impl.DefaultImpl.emit_begin "alembic.ddl.impl.DefaultImpl.emit_begin") and [`DefaultImpl.emit_commit()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.impl.DefaultImpl.emit_commit "alembic.ddl.impl.DefaultImpl.emit_commit") methods, which will produce the string directives `BEGIN` and `COMMIT` on the output stream, as rendered by the target backend (e.g. SQL Server would emit `BEGIN TRANSACTION`).

*   Otherwise, calls [`sqlalchemy.engine.Connection.begin()`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection.begin "(in SQLAlchemy v2.1)") on the current online connection, which returns a [`sqlalchemy.engine.Transaction`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Transaction "(in SQLAlchemy v2.1)") object. This object demarcates a real transaction and is itself a context manager, which will roll back if an exception is raised.

Note that a custom `env.py` script which has more specific transactional needs can of course manipulate the [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") directly to produce transactional state in “online” mode.

config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")=None[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.config "Link to this definition")
An instance of [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") representing the configuration file contents as well as other variables set programmatically within it.

configure(_connection:Connection|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _url:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|URL|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _dialect\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _dialect\_opts:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _transactional\_ddl:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _transaction\_per\_migration:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _output\_buffer:TextIO|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _starting\_rev:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _tag:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _template\_args:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _render\_as\_batch:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _target\_metadata:MetaData|Sequence[MetaData]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _include\_name:IncludeNameFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _include\_object:IncludeObjectFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _include\_schemas:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _process\_revision\_directives:ProcessRevisionDirectiveFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _compare\_type:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|CompareType=True_, _compare\_server\_default:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|CompareServerDefault=False_, _render\_item:RenderItemFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _literal\_binds:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _upgrade\_token:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='upgrades'_, _downgrade\_token:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='downgrades'_, _alembic\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='op.'_, _sqlalchemy\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='sa.'_, _user\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _on\_version\_apply:OnVersionApplyFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _autogenerate\_plugins:Sequence[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _**kw:Any_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "Link to this definition")
Configure a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") within this [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") which will provide database connectivity and other configuration to a series of migration scripts.

Many methods on [`EnvironmentContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext") require that this method has been called in order to function, as they ultimately need to have database access or at least access to the dialect in use. Those which do are documented as such.

The important thing needed by [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") is a means to determine what kind of database dialect is in use. An actual connection to that database is needed only if the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") is to be used in “online” mode.

If the [`is_offline_mode()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.is_offline_mode "alembic.runtime.environment.EnvironmentContext.is_offline_mode") function returns `True`, then no connection is needed here. Otherwise, the `connection` parameter should be present as an instance of [`sqlalchemy.engine.Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)").

This function is typically called from the `env.py` script within a migration environment. It can be called multiple times for an invocation. The most recent [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") for which it was called is the one that will be operated upon by the next call to [`run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.run_migrations "alembic.runtime.environment.EnvironmentContext.run_migrations").

General parameters:

Parameters:
*   **connection**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.connection) – a [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") to use for SQL execution in “online” mode. When present, is also used to determine the type of dialect in use.

*   **url**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.url) – a string database url, or a [`sqlalchemy.engine.url.URL`](https://docs.sqlalchemy.org/en/21/core/engines.html#sqlalchemy.engine.URL "(in SQLAlchemy v2.1)") object. The type of dialect to be used will be derived from this if `connection` is not passed.

*   **dialect_name**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.dialect_name) – string name of a dialect, such as “postgresql”, “mssql”, etc. The type of dialect to be used will be derived from this if `connection` and `url` are not passed.

*   **dialect_opts**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.dialect_opts) – dictionary of options to be passed to dialect constructor.

*   **transactional_ddl**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.transactional_ddl) – Force the usage of “transactional” DDL on or off; this otherwise defaults to whether or not the dialect in use supports it.

*   **transaction_per_migration**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.transaction_per_migration) – if True, nest each migration script in a transaction rather than the full series of migrations to run.

*   **output_buffer**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.output_buffer) – a file-like object that will be used for textual output when the `--sql` option is used to generate SQL scripts. Defaults to `sys.stdout` if not passed here and also not present on the [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object. The value here overrides that of the [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object.

*   **output_encoding**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.output_encoding) – when using `--sql` to generate SQL scripts, apply this encoding to the string output.

*   **literal_binds**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.literal_binds) –

when using `--sql` to generate SQL scripts, pass through the `literal_binds` flag to the compiler so that any literal values that would ordinarily be bound parameters are converted to plain strings.

Warning

Dialects can typically only handle simple datatypes like strings and numbers for auto-literal generation. Datatypes like dates, intervals, and others may still require manual formatting, typically using [`Operations.inline_literal()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.inline_literal "alembic.operations.Operations.inline_literal"). Note

the `literal_binds` flag is ignored on SQLAlchemy versions prior to 0.8 where this feature is not supported. 
*   **starting_rev**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.starting_rev) – Override the “starting revision” argument when using `--sql` mode.

*   **tag**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.tag) – a string tag for usage by custom `env.py` scripts. Set via the `--tag` option, can be overridden here.

*   **template_args**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.template_args) – dictionary of template arguments which will be added to the template argument environment when running the “revision” command. Note that the script environment is only run within the “revision” command if the –autogenerate option is used, or if the option “revision_environment=true” is present in the alembic.ini file.

*   **version_table**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.version_table) – The name of the Alembic version table. The default is `'alembic_version'`.

*   **version_table_schema**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.version_table_schema) – Optional schema to place version table within.

*   **version_table_pk**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.version_table_pk) – boolean, whether the Alembic version table should use a primary key constraint for the “value” column; this only takes effect when the table is first created. Defaults to True; setting to False should not be necessary and is here for backwards compatibility reasons.

*   **on_version_apply**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.on_version_apply) –

a callable or collection of callables to be run for each migration step. The callables will be run in the order they are given, once for each migration step, after the respective operation has been applied but before its transaction is finalized. Each callable accepts no positional arguments and the following keyword arguments:

    *   `ctx`: the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") running the migration,

    *   `step`: a `MigrationInfo` representing the step currently being applied,

    *   `heads`: a collection of version strings representing the current heads,

    *   `run_args`: the `**kwargs` passed to [`run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.run_migrations "alembic.runtime.environment.EnvironmentContext.run_migrations").

Parameters specific to the autogenerate feature, when `alembic revision` is run with the `--autogenerate` feature:

Parameters:
*   **target_metadata**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.target_metadata) – a [`sqlalchemy.schema.MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object, or a sequence of [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") objects, that will be consulted during autogeneration. The tables present in each [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") will be compared against what is locally available on the target [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") to produce candidate upgrade/downgrade operations.

*   **compare_type**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_type) –

Indicates type comparison behavior during an autogenerate operation. Defaults to `True` turning on type comparison, which has good accuracy on most backends. See [Comparing Types](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#compare-types) for an example as well as information on other type comparison options. Set to `False` which disables type comparison. A callable can also be passed to provide custom type comparison, see [Comparing Types](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#compare-types) for additional details.

Changed in version 1.12.0: The default value of [`EnvironmentContext.configure.compare_type`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_type "alembic.runtime.environment.EnvironmentContext.configure") has been changed to `True`.

*   **compare_server_default**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.compare_server_default) –

Indicates server default comparison behavior during an autogenerate operation. Defaults to `False` which disables server default comparison. Set to `True` to turn on server default comparison, which has varied accuracy depending on backend.

To customize server default comparison behavior, a callable may be specified which can filter server default comparisons during an autogenerate operation. defaults during an autogenerate operation. The format of this callable is:

def my_compare_server_default(context, inspected_column,
            metadata_column, inspected_default, metadata_default,
            rendered_metadata_default):
    # return True if the defaults are different,
    # False if not, or None to allow the default implementation
    # to compare these defaults
    return None

context.configure(
    # ...
    compare_server_default = my_compare_server_default
) 
`inspected_column` is a dictionary structure as returned by [`sqlalchemy.engine.reflection.Inspector.get_columns()`](https://docs.sqlalchemy.org/en/21/core/reflection.html#sqlalchemy.engine.reflection.Inspector.get_columns "(in SQLAlchemy v2.1)"), whereas `metadata_column` is a [`sqlalchemy.schema.Column`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Column "(in SQLAlchemy v2.1)") from the local model environment.

A return value of `None` indicates to allow default server default comparison to proceed. Note that some backends such as Postgresql actually execute the two defaults on the database side to compare for equivalence.

*   **include_name**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_name) –

A callable function which is given the chance to return `True` or `False` for any database reflected object based on its name, including database schema names when the [`EnvironmentContext.configure.include_schemas`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_schemas "alembic.runtime.environment.EnvironmentContext.configure") flag is set to `True`.

The function accepts the following positional arguments:

    *   `name`: the name of the object, such as schema name or table name. Will be `None` when indicating the default schema name of the database connection.

    *   `type`: a string describing the type of object; currently `"schema"`, `"table"`, `"column"`, `"index"`, `"unique_constraint"`, or `"foreign_key_constraint"`

    *   `parent_names`: a dictionary of “parent” object names, that are relative to the name being given. Keys in this dictionary may include: `"schema_name"`, `"table_name"` or `"schema_qualified_table_name"`.

E.g.:

def include_name(name, type_, parent_names):
    if type_ == "schema":
        return name in ["schema_one", "schema_two"]
    else:
        return True

context.configure(
    # ...
    include_schemas = True,
    include_name = include_name
)

*   **include_object**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_object) –

A callable function which is given the chance to return `True` or `False` for any object, indicating if the given object should be considered in the autogenerate sweep.

The function accepts the following positional arguments:

    *   `object`: a [`SchemaItem`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.SchemaItem "(in SQLAlchemy v2.1)") object such as a [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)"), [`Column`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Column "(in SQLAlchemy v2.1)"), [`Index`](https://docs.sqlalchemy.org/en/21/core/constraints.html#sqlalchemy.schema.Index "(in SQLAlchemy v2.1)")[`UniqueConstraint`](https://docs.sqlalchemy.org/en/21/core/constraints.html#sqlalchemy.schema.UniqueConstraint "(in SQLAlchemy v2.1)"), or [`ForeignKeyConstraint`](https://docs.sqlalchemy.org/en/21/core/constraints.html#sqlalchemy.schema.ForeignKeyConstraint "(in SQLAlchemy v2.1)") object

    *   `name`: the name of the object. This is typically available via `object.name`.

    *   `type`: a string describing the type of object; currently `"table"`, `"column"`, `"index"`, `"unique_constraint"`, or `"foreign_key_constraint"`

    *   `reflected`: `True` if the given object was produced based on table reflection, `False` if it’s from a local `MetaData` object.

    *   `compare_to`: the object being compared against, if available, else `None`.

E.g.:

def include_object(object, name, type_, reflected, compare_to):
    if (type_ == "column" and
        not reflected and
        object.info.get("skip_autogenerate", False)):
        return False
    else:
        return True

context.configure(
    # ...
    include_object = include_object
)

For the use case of omitting specific schemas from a target database when [`EnvironmentContext.configure.include_schemas`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_schemas "alembic.runtime.environment.EnvironmentContext.configure") is set to `True`, the [`schema`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table.schema "(in SQLAlchemy v2.1)") attribute can be checked for each [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") object passed to the hook, however it is much more efficient to filter on schemas before reflection of objects takes place using the [`EnvironmentContext.configure.include_name`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_name "alembic.runtime.environment.EnvironmentContext.configure") hook.

*   **render_as_batch**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.render_as_batch) –

if True, commands which alter elements within a table will be placed under a `with batch_alter_table():` directive, so that batch migrations will take place.

*   **include_schemas**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_schemas) –

If True, autogenerate will scan across all schemas located by the SQLAlchemy [`get_schema_names()`](https://docs.sqlalchemy.org/en/21/core/reflection.html#sqlalchemy.engine.reflection.Inspector.get_schema_names "(in SQLAlchemy v2.1)") method, and include all differences in tables found across all those schemas. When using this option, you may want to also use the [`EnvironmentContext.configure.include_name`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_name "alembic.runtime.environment.EnvironmentContext.configure") parameter to specify a callable which can filter the tables/schemas that get included.

*   **render_item**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.render_item) –

Callable that can be used to override how any schema item, i.e. column, constraint, type, etc., is rendered for autogenerate. The callable receives a string describing the type of object, the object, and the autogen context. If it returns False, the default rendering method will be used. If it returns None, the item will not be rendered in the context of a Table construct, that is, can be used to skip columns or constraints within op.create_table():

def my_render_column(type_, col, autogen_context):
    if type_ == "column" and isinstance(col, MySpecialCol):
        return repr(col)
    else:
        return False

context.configure(
    # ...
    render_item = my_render_column
) 
Available values for the type string include: `"column"`, `"primary_key"`, `"foreign_key"`, `"unique"`, `"check"`, `"type"`, `"server_default"`.

*   **upgrade_token**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.upgrade_token) – When autogenerate completes, the text of the candidate upgrade operations will be present in this template variable when `script.py.mako` is rendered. Defaults to `upgrades`.

*   **downgrade_token**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.downgrade_token) – When autogenerate completes, the text of the candidate downgrade operations will be present in this template variable when `script.py.mako` is rendered. Defaults to `downgrades`.

*   **alembic_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.alembic_module_prefix) – When autogenerate refers to Alembic [`alembic.operations`](https://alembic.sqlalchemy.org/en/latest/ops.html#module-alembic.operations "alembic.operations") constructs, this prefix will be used (i.e. `op.create_table`) Defaults to “`op.`”. Can be `None` to indicate no prefix.

*   **sqlalchemy_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.sqlalchemy_module_prefix) – When autogenerate refers to SQLAlchemy [`Column`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Column "(in SQLAlchemy v2.1)") or type classes, this prefix will be used (i.e. `sa.Column("somename", sa.Integer)`) Defaults to “`sa.`”. Can be `None` to indicate no prefix. Note that when dialect-specific types are rendered, autogenerate will render them using the dialect module name, i.e. `mssql.BIT()`, `postgresql.UUID()`.

*   **user_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.user_module_prefix) –

When autogenerate refers to a SQLAlchemy type (e.g. `TypeEngine`) where the module name is not under the `sqlalchemy` namespace, this prefix will be used within autogenerate. If left at its default of `None`, the `__module__` attribute of the type is used to render the import module. It’s a good practice to set this and to have all custom types be available from a fixed module space, in order to future-proof migration files against reorganizations in modules.

*   **process_revision_directives**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives) –

a callable function that will be passed a structure representing the end result of an autogenerate or plain “revision” operation, which can be manipulated to affect how the `alembic revision` command ultimately outputs new revision scripts. The structure of the callable is:

def process_revision_directives(context, revision, directives):
    pass 
The `directives` parameter is a Python list containing a single [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") directive, which represents the revision file to be generated. This list as well as its contents may be freely modified to produce any set of commands. The section [Customizing Revision Generation](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#customizing-revision) shows an example of doing this. The `context` parameter is the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") in use, and `revision` is a tuple of revision identifiers representing the current revision of the database.

The callable is invoked at all times when the `--autogenerate` option is passed to `alembic revision`. If `--autogenerate` is not passed, the callable is invoked only if the `revision_environment` variable is set to True in the Alembic configuration, in which case the given `directives` collection will contain empty [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") and [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") collections for `.upgrade_ops` and `.downgrade_ops`. The `--autogenerate` option itself can be inferred by inspecting `context.config.cmd_opts.autogenerate`.

The callable function may optionally be an instance of a [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") object. This is a helper object that assists in the production of autogenerate-stream rewriter functions.

*   **autogenerate_plugins**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.autogenerate_plugins) –

A list of string names of “plugins” that should participate in this autogenerate run. Defaults to the list `["alembic.autogenerate.*"]`, which indicates that Alembic’s default autogeneration plugins will be used.

See the section [Enabling Autogenerate Plugins in env.py](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugins-autogenerate) for complete background on how to use this parameter.

Added in version 1.18.0: Added a new plugin system for autogenerate compare directives.

Parameters specific to individual backends:

Parameters:
*   **mssql_batch_separator**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.mssql_batch_separator) – The “batch separator” which will be placed between each statement when generating offline SQL Server migrations. Defaults to `GO`. Note this is in addition to the customary semicolon `;` at the end of each statement; SQL Server considers the “batch separator” to denote the end of an individual statement execution, and cannot group certain dependent operations in one step.

*   **oracle_batch_separator**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.oracle_batch_separator) – The “batch separator” which will be placed between each statement when generating offline Oracle migrations. Defaults to `/`. Oracle doesn’t add a semicolon between statements like most other backends.

execute(_sql:Executable|[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _execution\_options:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.execute "Link to this definition")
Execute the given SQL using the current change context.

The behavior of [`execute()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.execute "alembic.runtime.environment.EnvironmentContext.execute") is the same as that of [`Operations.execute()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.execute "alembic.operations.Operations.execute"). Please see that function’s documentation for full detail including caveats and limitations.

This function requires that a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has first been made available via [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure").

get_bind()→Connection[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_bind "Link to this definition")
Return the current ‘bind’.

In “online” mode, this is the [`sqlalchemy.engine.Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") currently being used to emit SQL to the database.

This function requires that a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has first been made available via [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure").

get_context()→[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_context "Link to this definition")
Return the current [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") object.

If [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") has not been called yet, raises an exception.

get_head_revision()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_head_revision "Link to this definition")
Return the hex identifier of the ‘head’ script revision.

If the script directory has multiple heads, this method raises a [`CommandError`](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html#alembic.util.exc.CommandError "alembic.util.exc.CommandError"); [`EnvironmentContext.get_head_revisions()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_head_revisions "alembic.runtime.environment.EnvironmentContext.get_head_revisions") should be preferred.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

get_head_revisions()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_head_revisions "Link to this definition")
Return the hex identifier of the ‘heads’ script revision(s).

This returns a tuple containing the version number of all heads in the script directory.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

get_revision_argument()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_revision_argument "Link to this definition")
Get the ‘destination’ revision argument.

This is typically the argument passed to the `upgrade` or `downgrade` command.

If it was specified as `head`, the actual version number is returned; if specified as `base`, `None` is returned.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

get_starting_revision_argument()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_starting_revision_argument "Link to this definition")
Return the ‘starting revision’ argument, if the revision was passed using `start:end`.

This is only meaningful in “offline” mode. Returns `None` if no value is available or was configured.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

get_tag_argument()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_tag_argument "Link to this definition")
Return the value passed for the `--tag` argument, if any.

The `--tag` argument is not used directly by Alembic, but is available for custom `env.py` configurations that wish to use it; particularly for offline generation scripts that wish to generate tagged filenames.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

See also

[`EnvironmentContext.get_x_argument()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_x_argument "alembic.runtime.environment.EnvironmentContext.get_x_argument") - a newer and more open ended system of extending `env.py` scripts via the command line.

get_x_argument(_as\_dictionary:[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[False]_)→[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_x_argument "Link to this definition")get_x_argument(_as\_dictionary:[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[True]_)→[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]get_x_argument(_as\_dictionary:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]
Return the value(s) passed for the `-x` argument, if any.

The `-x` argument is an open ended flag that allows any user-defined value or values to be passed on the command line, then available here for consumption by a custom `env.py` script.

The return value is a list, returned directly from the `argparse` structure. If `as_dictionary=True` is passed, the `x` arguments are parsed using `key=value` format into a dictionary that is then returned. If there is no `=` in the argument, value is an empty string.

Changed in version 1.13.1: Support `as_dictionary=True` when arguments are passed without the `=` symbol.

For example, to support passing a database URL on the command line, the standard `env.py` script can be modified like this:

cmd_line_url = context.get_x_argument(
    as_dictionary=True).get('dbname')
if cmd_line_url:
    engine = create_engine(cmd_line_url)
else:
    engine = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix='sqlalchemy.',
            poolclass=pool.NullPool)

This then takes effect by running the `alembic` script as:

alembic -x dbname=postgresql://user:pass@host/dbname upgrade head

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

is_offline_mode()→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.is_offline_mode "Link to this definition")
Return True if the current migrations environment is running in “offline mode”.

This is `True` or `False` depending on the `--sql` flag passed.

This function does not require that the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has been configured.

is_transactional_ddl()→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.is_transactional_ddl "Link to this definition")
Return True if the context is configured to expect a transactional DDL capable backend.

This defaults to the type of database in use, and can be overridden by the `transactional_ddl` argument to [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure")

This function requires that a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has first been made available via [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure").

run_migrations(_**kw:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.run_migrations "Link to this definition")
Run migrations as determined by the current command line configuration as well as versioning information present (or not) in the current database connection (if one is present).

The function accepts optional `**kw` arguments. If these are passed, they are sent directly to the `upgrade()` and `downgrade()` functions within each target revision file. By modifying the `script.py.mako` file so that the `upgrade()` and `downgrade()` functions accept arguments, parameters can be passed here so that contextual information, usually information to identify a particular database in use, can be passed from a custom `env.py` script to the migration functions.

This function requires that a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") has first been made available via [`configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure").

script:[ScriptDirectory](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory")=None[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.script "Link to this definition")
An instance of [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") which provides programmatic access to version files within the `versions/` directory.

static_output(_text:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.static_output "Link to this definition")
Emit text directly to the “offline” SQL stream.

Typically this is for emitting comments that start with –. The statement is not treated as a SQL execution, no ; or batch separator is added, etc.

The Migration Context[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#the-migration-context "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

The [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") handles the actual work to be performed against a database backend as migration operations proceed. It is generally not exposed to the end-user, except when the [`on_version_apply`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.on_version_apply "alembic.runtime.environment.EnvironmentContext.configure") callback hook is used.

class alembic.runtime.migration.MigrationContext(_dialect:Dialect_, _connection:Connection|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _opts:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]_, _environment\_context:[EnvironmentContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "Link to this definition")
Represent the database state made available to a migration script.

[`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") is the front end to an actual database connection, or alternatively a string output stream given a particular database dialect, from an Alembic perspective.

When inside the `env.py` script, the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") is available via the [`EnvironmentContext.get_context()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_context "alembic.runtime.environment.EnvironmentContext.get_context") method, which is available at `alembic.context`:

# from within env.py script
from alembic import context

migration_context = context.get_context()

For usage outside of an `env.py` script, such as for utility routines that want to check the current version in the database, the [`MigrationContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure "alembic.runtime.migration.MigrationContext.configure") method to create new [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") objects. For example, to get at the current revision in the database using [`MigrationContext.get_current_revision()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.get_current_revision "alembic.runtime.migration.MigrationContext.get_current_revision"):

# in any application, outside of an env.py script
from alembic.migration import MigrationContext
from sqlalchemy import create_engine

engine = create_engine("postgresql://mydatabase")
conn = engine.connect()

context = MigrationContext.configure(conn)
current_rev = context.get_current_revision()

The above context can also be used to produce Alembic migration operations with an [`Operations`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations "alembic.operations.Operations") instance:

# in any application, outside of the normal Alembic environment
from alembic.operations import Operations

op = Operations(context)
op.alter_column("mytable", "somecolumn", nullable=True)

autocommit_block()→[Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.autocommit_block "Link to this definition")
Enter an “autocommit” block, for databases that support AUTOCOMMIT isolation levels.

This special directive is intended to support the occasional database DDL or system operation that specifically has to be run outside of any kind of transaction block. The PostgreSQL database platform is the most common target for this style of operation, as many of its DDL operations must be run outside of transaction blocks, even though the database overall supports transactional DDL.

The method is used as a context manager within a migration script, by calling on [`Operations.get_context()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.get_context "alembic.operations.Operations.get_context") to retrieve the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext"), then invoking [`MigrationContext.autocommit_block()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.autocommit_block "alembic.runtime.migration.MigrationContext.autocommit_block") using the `with:` statement:

def upgrade():
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE mood ADD VALUE 'soso'")

Above, a PostgreSQL “ALTER TYPE..ADD VALUE” directive is emitted, which must be run outside of a transaction block at the database level. The [`MigrationContext.autocommit_block()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.autocommit_block "alembic.runtime.migration.MigrationContext.autocommit_block") method makes use of the SQLAlchemy `AUTOCOMMIT` isolation level setting, which against the psycogp2 DBAPI corresponds to the `connection.autocommit` setting, to ensure that the database driver is not inside of a DBAPI level transaction block.

Warning

As is necessary, **the database transaction preceding the block is unconditionally committed**. This means that the run of migrations preceding the operation will be committed, before the overall migration operation is complete.

It is recommended that when an application includes migrations with “autocommit” blocks, that [`EnvironmentContext.transaction_per_migration`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.params.transaction_per_migration "alembic.runtime.environment.EnvironmentContext") be used so that the calling environment is tuned to expect short per-file migrations whether or not one of them has an autocommit block.

begin_transaction(_\_per\_migration:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→_ProxyTransaction|[ContextManager](https://docs.python.org/3/library/typing.html#typing.ContextManager "(in Python v3.14)")[[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"),[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.begin_transaction "Link to this definition")
Begin a logical transaction for migration operations.

This method is used within an `env.py` script to demarcate where the outer “transaction” for a series of migrations begins. Example:

def run_migrations_online():
    connectable = create_engine(...)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

Above, [`MigrationContext.begin_transaction()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.begin_transaction "alembic.runtime.migration.MigrationContext.begin_transaction") is used to demarcate where the outer logical transaction occurs around the [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations") operation.

A “Logical” transaction means that the operation may or may not correspond to a real database transaction. If the target database supports transactional DDL (or [`EnvironmentContext.configure.transactional_ddl`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.transactional_ddl "alembic.runtime.environment.EnvironmentContext.configure") is true), the [`EnvironmentContext.configure.transaction_per_migration`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.transaction_per_migration "alembic.runtime.environment.EnvironmentContext.configure") flag is not set, and the migration is against a real database connection (as opposed to using “offline” `--sql` mode), a real transaction will be started. If `--sql` mode is in effect, the operation would instead correspond to a string such as “BEGIN” being emitted to the string output.

The returned object is a Python context manager that should only be used in the context of a `with:` statement as indicated above. The object has no other guaranteed API features present.

property bind:Connection|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.bind "Link to this definition")
Return the current “bind”.

In online mode, this is an instance of [`sqlalchemy.engine.Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)"), and is suitable for ad-hoc execution of any kind of usage described in SQLAlchemy Core documentation as well as for usage with the [`sqlalchemy.schema.Table.create()`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table.create "(in SQLAlchemy v2.1)") and [`sqlalchemy.schema.MetaData.create_all()`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData.create_all "(in SQLAlchemy v2.1)") methods of [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)"), [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)").

Note that when “standard output” mode is enabled, this bind will be a “mock” connection handler that cannot return results and is only appropriate for a very limited subset of commands.

property config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.config "Link to this definition")
Return the [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") used by the current environment, if any.

classmethod configure(_connection:Connection|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _url:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|URL|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _dialect\_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _dialect:Dialect|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _environment\_context:[EnvironmentContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext "alembic.runtime.environment.EnvironmentContext")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _dialect\_opts:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _opts:Any|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure "Link to this definition")
Create a new [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext").

This is a factory method usually called by [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure").

Parameters:
*   **connection**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure.params.connection) – a [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") to use for SQL execution in “online” mode. When present, is also used to determine the type of dialect in use.

*   **url**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure.params.url) – a string database url, or a [`sqlalchemy.engine.url.URL`](https://docs.sqlalchemy.org/en/21/core/engines.html#sqlalchemy.engine.URL "(in SQLAlchemy v2.1)") object. The type of dialect to be used will be derived from this if `connection` is not passed.

*   **dialect_name**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure.params.dialect_name) – string name of a dialect, such as “postgresql”, “mssql”, etc. The type of dialect to be used will be derived from this if `connection` and `url` are not passed.

*   **opts**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.configure.params.opts) – dictionary of options. Most other options accepted by [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") are passed via this dictionary.

execute(_sql:Executable|[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _execution\_options:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.execute "Link to this definition")
Execute a SQL construct or string statement.

The underlying execution mechanics are used, that is if this is “offline mode” the SQL is written to the output buffer, otherwise the SQL is emitted on the current SQLAlchemy connection.

get_current_heads()→[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...][#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.get_current_heads "Link to this definition")
Return a tuple of the current ‘head versions’ that are represented in the target database.

For a migration stream without branches, this will be a single value, synonymous with that of [`MigrationContext.get_current_revision()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.get_current_revision "alembic.runtime.migration.MigrationContext.get_current_revision"). However when multiple unmerged branches exist within the target database, the returned tuple will contain a value for each head.

If this [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") was configured in “offline” mode, that is with `as_sql=True`, the `starting_rev` parameter is returned in a one-length tuple.

If no version table is present, or if there are no revisions present, an empty tuple is returned.

get_current_revision()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.get_current_revision "Link to this definition")
Return the current revision, usually that which is present in the `alembic_version` table in the database.

This method intends to be used only for a migration stream that does not contain unmerged branches in the target database; if there are multiple branches present, an exception is raised. The [`MigrationContext.get_current_heads()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.get_current_heads "alembic.runtime.migration.MigrationContext.get_current_heads") should be preferred over this method going forward in order to be compatible with branch migration support.

If this [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") was configured in “offline” mode, that is with `as_sql=True`, the `starting_rev` parameter is returned instead, if any.

run_migrations(_**kw:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "Link to this definition")
Run the migration scripts established for this [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext"), if any.

The commands in [`alembic.command`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#module-alembic.command "alembic.command") will set up a function that is ultimately passed to the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") as the `fn` argument. This function represents the “work” that will be done when [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations") is called, typically from within the `env.py` script of the migration environment. The “work function” then provides an iterable of version callables and other version information which in the case of the `upgrade` or `downgrade` commands are the list of version scripts to invoke. Other commands yield nothing, in the case that a command wants to run some other operation against the database such as the `current` or `stamp` commands.

Parameters:
****kw**[¶](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations.params.**kw) – keyword arguments here will be passed to each migration callable, that is the `upgrade()` or `downgrade()` method within revision scripts.

stamp(_script\_directory:[ScriptDirectory](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory")_, _revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.stamp "Link to this definition")
Stamp the version table with a specific revision.

This method calculates those branches to which the given revision can apply, and updates those branches as though they were migrated towards that revision (either up or down). If no current branches include the revision, it is added as a new branch head.
