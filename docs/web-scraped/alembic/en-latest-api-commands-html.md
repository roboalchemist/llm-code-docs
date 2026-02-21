# Source: https://alembic.sqlalchemy.org/en/latest/api/commands.html

Title: Commands — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/commands.html

Markdown Content:
Contents
--------

*   [`branches()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.branches)
*   [`check()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.check)
*   [`current()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.current)
*   [`downgrade()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade)
*   [`edit()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.edit)
*   [`ensure_version()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.ensure_version)
*   [`heads()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.heads)
*   [`history()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history)
*   [`init()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init)
*   [`list_templates()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.list_templates)
*   [`merge()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge)
*   [`revision()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision)
*   [`show()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.show)
*   [`stamp()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp)
*   [`upgrade()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade)

Commands[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#commands "Link to this heading")
-------------------------------------------------------------------------------------------------------

Note

this section discusses the **internal API of Alembic** as regards its command invocation system. This section is only useful for developers who wish to extend the capabilities of Alembic. For documentation on using Alembic commands, please see [Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html).

Alembic commands are all represented by functions in the [Commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic-command-toplevel) package. They all accept the same style of usage, being sent the [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object as the first argument.

Commands can be run programmatically, by first constructing a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object, as in:

from alembic.config import Config
from alembic import command
alembic_cfg = Config("/path/to/yourapp/alembic.ini")
command.upgrade(alembic_cfg, "head")

In many cases, and perhaps more often than not, an application will wish to call upon a series of Alembic commands and/or other features. It is usually a good idea to link multiple commands along a single connection and transaction, if feasible. This can be achieved using the [`Config.attributes`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config.attributes "alembic.config.Config.attributes") dictionary in order to share a connection:

with engine.begin() as connection:
    alembic_cfg.attributes['connection'] = connection
    command.upgrade(alembic_cfg, "head")

This recipe requires that `env.py` consumes this connection argument; see the example in [Sharing a Connection across one or more programmatic migration commands](https://alembic.sqlalchemy.org/en/latest/cookbook.html#connection-sharing) for details.

To write small API functions that make direct use of database and script directory information, rather than just running one of the built-in commands, use the [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") and [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") classes directly.

alembic.command.branches(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _verbose:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.branches "Link to this definition")
Show current branch points.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.branches.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **verbose**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.branches.params.verbose) – output in verbose mode.

alembic.command.check(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.check "Link to this definition")
Check if revision command with autogenerate has pending upgrade ops.

Parameters:
**config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.check.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object.

Added in version 1.9.0.

alembic.command.current(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _check\_heads:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _verbose:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.current "Link to this definition")
Display the current revision for a database.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.current.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **check_heads**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.current.params.check_heads) –

Check if all head revisions are applied to the database. Raises [`DatabaseNotAtHead`](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html#alembic.util.exc.DatabaseNotAtHead "alembic.util.exc.DatabaseNotAtHead") if this is not the case.

Added in version 1.17.1.

*   **verbose**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.current.params.verbose) – output in verbose mode.

alembic.command.downgrade(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _sql:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _tag:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade "Link to this definition")
Revert to a previous version.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **revision**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade.params.revision) – string revision target or range for –sql mode. May be `"base"` to target the first revision.

*   **sql**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade.params.sql) – if True, use `--sql` mode.

*   **tag**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.downgrade.params.tag) – an arbitrary “tag” that can be intercepted by custom `env.py` scripts via the [`EnvironmentContext.get_tag_argument()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_tag_argument "alembic.runtime.environment.EnvironmentContext.get_tag_argument") method.

alembic.command.edit(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _rev:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.edit "Link to this definition")
Edit revision script(s) using $EDITOR.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.edit.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **rev**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.edit.params.rev) – target revision.

alembic.command.ensure_version(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _sql:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.ensure_version "Link to this definition")
Create the alembic version table if it doesn’t exist already .

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.ensure_version.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **sql**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.ensure_version.params.sql) –

use `--sql` mode.

Added in version 1.7.6.

alembic.command.heads(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _verbose:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _resolve\_dependencies:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.heads "Link to this definition")
Show current available heads in the script directory.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.heads.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **verbose**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.heads.params.verbose) – output in verbose mode.

*   **resolve_dependencies**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.heads.params.resolve_dependencies) – treat dependency version as down revisions.

alembic.command.history(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _rev\_range:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _verbose:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _indicate\_current:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history "Link to this definition")
List changeset scripts in chronological order.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **rev_range**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history.params.rev_range) – string revision range.

*   **verbose**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history.params.verbose) – output in verbose mode.

*   **indicate_current**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.history.params.indicate_current) – indicate current revision.

alembic.command.init(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _directory:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _template:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='generic'_, _package:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init "Link to this definition")
Initialize a new scripts directory.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object.

*   **directory**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init.params.directory) – string path of the target directory.

*   **template**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init.params.template) – string name of the migration environment template to use.

*   **package**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.init.params.package) – when True, write `__init__.py` files into the environment location as well as the versions/ location.

alembic.command.list_templates(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.list_templates "Link to this definition")
List available templates.

Parameters:
**config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.list_templates.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object.

alembic.command.merge(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _revisions:\_RevIdType_, _message:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _branch\_label:\_RevIdType|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _rev\_id:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge "Link to this definition")
Merge two revisions together. Creates a new migration file.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance

*   **revisions**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge.params.revisions) – The revisions to merge.

*   **message**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge.params.message) – string message to apply to the revision.

*   **branch_label**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge.params.branch_label) – string label name to apply to the new revision.

*   **rev_id**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.merge.params.rev_id) – hardcoded revision identifier instead of generating a new one.

alembic.command.revision(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _message:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _autogenerate:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _sql:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _head:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='head'_, _splice:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _branch\_label:\_RevIdType|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _version\_path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[os.PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _rev\_id:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _depends\_on:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _process\_revision\_directives:ProcessRevisionDirectiveFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")|List[[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision "Link to this definition")
Create a new revision file.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") object.

*   **message**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.message) – string message to apply to the revision; this is the `-m` option to `alembic revision`.

*   **autogenerate**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.autogenerate) – whether or not to autogenerate the script from the database; this is the `--autogenerate` option to `alembic revision`.

*   **sql**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.sql) – whether to dump the script out as a SQL string; when specified, the script is dumped to stdout. This is the `--sql` option to `alembic revision`.

*   **head**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.head) – head revision to build the new revision upon as a parent; this is the `--head` option to `alembic revision`.

*   **splice**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.splice) – whether or not the new revision should be made into a new head of its own; is required when the given `head` is not itself a head. This is the `--splice` option to `alembic revision`.

*   **branch_label**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.branch_label) – string label to apply to the branch; this is the `--branch-label` option to `alembic revision`.

*   **version_path**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.version_path) – string symbol identifying a specific version path from the configuration; this is the `--version-path` option to `alembic revision`.

*   **rev_id**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.rev_id) – optional revision identifier to use instead of having one generated; this is the `--rev-id` option to `alembic revision`.

*   **depends_on**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.depends_on) – optional list of “depends on” identifiers; this is the `--depends-on` option to `alembic revision`.

*   **process_revision_directives**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision.params.process_revision_directives) – this is a callable that takes the same form as the callable described at [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure"); will be applied to the structure generated by the revision process where it can be altered programmatically. Note that unlike all the other parameters, this option is only available via programmatic use of [`command.revision()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision "alembic.command.revision").

alembic.command.show(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _rev:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.show "Link to this definition")
Show the revision(s) denoted by the given symbol.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.show.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **rev**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.show.params.rev) – string revision target. May be `"current"` to show the revision(s) currently applied in the database.

alembic.command.stamp(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _revision:\_RevIdType_, _sql:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _tag:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _purge:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp "Link to this definition")
‘stamp’ the revision table with the given revision; don’t run any migrations.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **revision**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp.params.revision) –

target revision or list of revisions. May be a list to indicate stamping of multiple branch heads; may be `"base"` to remove all revisions from the table or `"heads"` to stamp the most recent revision(s).

Note

this parameter is called “revisions” in the command line interface. 
*   **sql**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp.params.sql) – use `--sql` mode

*   **tag**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp.params.tag) – an arbitrary “tag” that can be intercepted by custom `env.py` scripts via the `EnvironmentContext.get_tag_argument` method.

*   **purge**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.stamp.params.purge) – delete all entries in the version table before stamping.

alembic.command.upgrade(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_, _revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _sql:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _tag:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade "Link to this definition")
Upgrade to a later version.

Parameters:
*   **config**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade.params.config) – a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

*   **revision**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade.params.revision) – string revision target or range for –sql mode. May be `"heads"` to target the most recent revision(s).

*   **sql**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade.params.sql) – if True, use `--sql` mode.

*   **tag**[¶](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.upgrade.params.tag) – an arbitrary “tag” that can be intercepted by custom `env.py` scripts via the [`EnvironmentContext.get_tag_argument()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.get_tag_argument "alembic.runtime.environment.EnvironmentContext.get_tag_argument") method.
