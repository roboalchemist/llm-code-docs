# Source: https://alembic.sqlalchemy.org/en/latest/api/script.html

Title: Script Directory — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/script.html

Markdown Content:
Script Directory[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#script-directory "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

The [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") object provides programmatic access to the Alembic version files present in the filesystem.

class alembic.script.Script(_module:[ModuleType](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")_, _rev\_id:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "Link to this definition")
Represent a single revision file in a `versions/` directory.

The [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") instance is returned by methods such as [`ScriptDirectory.iterate_revisions()`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.iterate_revisions "alembic.script.ScriptDirectory.iterate_revisions").

property doc:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script.doc "Link to this definition")
Return the docstring given in the script.

property longdoc:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script.longdoc "Link to this definition")
Return the docstring given in the script.

module:[ModuleType](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script.module "Link to this definition")
The Python module representing the actual script itself.

path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script.path "Link to this definition")
Filesystem path of the script.

class alembic.script.ScriptDirectory(_dir:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[os.PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_, _file\_template:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='%(rev)s\_%(slug)s'_, _truncate\_slug\_length:[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=40_, _version\_locations:Sequence[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[os.PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _sourceless:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _output\_encoding:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='utf-8'_, _timezone:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _hooks:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[PostWriteHookConfig]=[]_, _recursive\_version\_locations:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _messaging\_opts:[MessagingOptions](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.MessagingOptions "alembic.config.MessagingOptions")={}_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "Link to this definition")
Provides operations upon an Alembic script directory.

This object is useful to get information as to current revisions, most notably being able to get at the “head” revision, for schemes that want to test if the current revision in the database is the most recent:

from alembic.script import ScriptDirectory
from alembic.config import Config
config = Config()
config.set_main_option("script_location", "myapp:migrations")
script = ScriptDirectory.from_config(config)

head_revision = script.get_current_head()

as_revision_number(_id\_:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.as_revision_number "Link to this definition")
Convert a symbolic revision, i.e. ‘head’ or ‘base’, into an actual revision number.

classmethod from_config(_config:[Config](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config")_)→[ScriptDirectory](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.from_config "Link to this definition")
Produce a new [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") given a [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") instance.

The [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config "alembic.config.Config") need only have the `script_location` key present.

generate_revision(_revid:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _message:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _head:\_RevIdType|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _splice:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=False_, _branch\_labels:\_RevIdType|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _version\_path:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[os.PathLike](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _file\_template:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _depends\_on:\_RevIdType|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _**kw:Any_)→[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.generate_revision "Link to this definition")
Generate a new revision file.

This runs the `script.py.mako` template, given template arguments, and creates a new file.

Parameters:
*   **revid**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.generate_revision.params.revid) – String revision id. Typically this comes from `alembic.util.rev_id()`.

*   **message**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.generate_revision.params.message) – the revision message, the one passed by the -m argument to the `revision` command.

*   **head**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.generate_revision.params.head) – the head revision to generate against. Defaults to the current “head” if no branches are present, else raises an exception.

*   **splice**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.generate_revision.params.splice) – if True, allow the “head” version to not be an actual head; otherwise, the selected head must be a head (e.g. endpoint) revision.

get_base()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_base "Link to this definition")
Return the “base” revision as a string.

This is the revision number of the script that has a `down_revision` of None.

If the script directory has multiple bases, an error is raised; [`ScriptDirectory.get_bases()`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_bases "alembic.script.ScriptDirectory.get_bases") should be preferred.

get_bases()→[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_bases "Link to this definition")
return all “base” revisions as strings.

This is the revision number of all scripts that have a `down_revision` of None.

get_current_head()→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_current_head "Link to this definition")
Return the current head revision.

If the script directory has multiple heads due to branching, an error is raised; [`ScriptDirectory.get_heads()`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_heads "alembic.script.ScriptDirectory.get_heads") should be preferred.

Returns:
a string revision number.

get_heads()→[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_heads "Link to this definition")
Return all “versioned head” revisions as strings.

This is normally a list of length one, unless branches are present. The [`ScriptDirectory.get_current_head()`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_current_head "alembic.script.ScriptDirectory.get_current_head") method can be used normally when a script directory has only one head.

Returns:
a tuple of string revision numbers.

get_revision(_id\_:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.base.Script")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_revision "Link to this definition")
Return the [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") instance with the given rev id.

get_revisions(_id\_:\_GetRevArg_)→Tuple[[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script"),...][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_revisions "Link to this definition")
Return the [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") instance with the given rev identifier, symbolic name, or sequence of identifiers.

iterate_revisions(_upper:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _lower:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _**kw:[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")_)→[Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.base.Script")][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.iterate_revisions "Link to this definition")
Iterate through script revisions, starting at the given upper revision identifier and ending at the lower.

The traversal uses strictly the down_revision marker inside each migration script, so it is a requirement that upper >= lower, else you’ll get nothing back.

The iterator yields [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") objects.

run_env()→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.run_env "Link to this definition")
Run the script environment.

This basically runs the `env.py` script present in the migration environment. It is called exclusively by the command functions in [`alembic.command`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#module-alembic.command "alembic.command").

property versions:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.versions "Link to this definition")
return a single version location based on the sole path passed within version_locations.

If multiple version locations are configured, an error is raised.

walk_revisions(_base:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='base'_, _head:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='heads'_)→[Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Script](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.base.Script")][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.walk_revisions "Link to this definition")
Iterate through all revisions.

Parameters:
*   **base**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.walk_revisions.params.base) – the base revision, or “base” to start from the empty revision.

*   **head**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.walk_revisions.params.head) – the head revision; defaults to “heads” to indicate all head revisions. May also be “head” to indicate a single head revision.

Revision[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#revision "Link to this heading")
-----------------------------------------------------------------------------------------------------

The [`RevisionMap`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap "alembic.script.revision.RevisionMap") object serves as the basis for revision management, used exclusively by [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory").

exception alembic.script.revision.CycleDetected(_revisions:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.CycleDetected "Link to this definition")exception alembic.script.revision.DependencyCycleDetected(_revisions:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.DependencyCycleDetected "Link to this definition")exception alembic.script.revision.DependencyLoopDetected(_revision:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.DependencyLoopDetected "Link to this definition")exception alembic.script.revision.LoopDetected(_revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.LoopDetected "Link to this definition")exception alembic.script.revision.MultipleHeads(_heads:[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_, _argument:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.MultipleHeads "Link to this definition")exception alembic.script.revision.RangeNotAncestorError(_lower:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _upper:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RangeNotAncestorError "Link to this definition")exception alembic.script.revision.ResolutionError(_message:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _argument:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.ResolutionError "Link to this definition")class alembic.script.revision.Revision(_revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _down\_revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _dependencies:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _branch\_labels:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "Link to this definition")
Base class for revisioned objects.

The [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") class is the base of the more public-facing [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") object, which represents a migration script. The mechanics of revision management and traversal are encapsulated within [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision"), while [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") applies this logic to Python files in a version directory.

branch_labels:[Set](https://docs.python.org/3/library/typing.html#typing.Set "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]=None[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.branch_labels "Link to this definition")
Optional string/tuple of symbolic names to apply to this revision’s branch

dependencies:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.dependencies "Link to this definition")
Additional revisions which this revision is dependent on.

From a migration standpoint, these dependencies are added to the down_revision to form the full iteration. However, the separation of down_revision from “dependencies” is to assist in navigating a history that contains many branches, typically a multi-root scenario.

down_revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[List](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.down_revision "Link to this definition")
The `down_revision` identifier(s) within the migration script.

Note that the total set of “down” revisions is down_revision + dependencies.

property is_base:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.is_base "Link to this definition")
Return True if this [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") is a ‘base’ revision.

property is_branch_point:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.is_branch_point "Link to this definition")
Return True if this [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") is a branch point.

A branchpoint is defined as a [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") which is referred to by more than one succeeding [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script"), that is more than one [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") has a down_revision identifier pointing here.

property is_head:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.is_head "Link to this definition")
Return True if this [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") is a ‘head’ revision.

This is determined based on whether any other [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") within the [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") refers to this [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script"). Multiple heads can be present.

property is_merge_point:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.is_merge_point "Link to this definition")
Return True if this [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") is a merge point.

nextrev:[FrozenSet](https://docs.python.org/3/library/typing.html#typing.FrozenSet "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]=frozenset({})[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.nextrev "Link to this definition")
following revisions, based on down_revision only.

revision:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision.revision "Link to this definition")
The string revision number.

exception alembic.script.revision.RevisionError[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionError "Link to this definition")class alembic.script.revision.RevisionMap(_generator:[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[],[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "(in Python v3.14)")[[Revision](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision")]]_)[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap "Link to this definition")
Maintains a map of [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") objects.

[`RevisionMap`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap "alembic.script.revision.RevisionMap") is used by [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory "alembic.script.ScriptDirectory") to maintain and traverse the collection of [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") objects, which are themselves instances of [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision").

Construct a new [`RevisionMap`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap "alembic.script.revision.RevisionMap").

Parameters:
**generator**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.params.generator) – a zero-arg callable that will generate an iterable of [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") instances to be used. These are typically [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script "alembic.script.Script") subclasses within regular Alembic use.

add_revision(_revision:[Revision](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision")_, _\_replace:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.add_revision "Link to this definition")
add a single revision to an existing map.

This method is for single-revision use cases, it’s not appropriate for fully populating an entire revision map.

bases[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.bases "Link to this definition")
All “base” revisions as strings.

These are revisions that have a `down_revision` of None, or empty tuple.

Returns:
a tuple of string revision numbers.

get_current_head(_branch\_label:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.get_current_head "Link to this definition")
Return the current head revision.

If the script directory has multiple heads due to branching, an error is raised; [`ScriptDirectory.get_heads()`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory.get_heads "alembic.script.ScriptDirectory.get_heads") should be preferred.

Parameters:
**branch_label**[¶](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.get_current_head.params.branch_label) – optional branch name which will limit the heads considered to those which include that branch_label.

Returns:
a string revision number.

get_revision(_id\_:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)→[Revision](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.get_revision "Link to this definition")
Return the [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") instance with the given rev id.

If a symbolic name such as “head” or “base” is given, resolves the identifier into the current head or base revision. If the symbolic name refers to multiples, [`MultipleHeads`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.MultipleHeads "alembic.script.revision.MultipleHeads") is raised.

Supports partial identifiers, where the given identifier is matched against all identifiers that start with the given characters; if there is exactly one match, that determines the full revision.

get_revisions(_id\_:\_GetRevArg|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)→Tuple[_RevisionOrBase|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"),...][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.get_revisions "Link to this definition")
Return the [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") instances with the given rev id or identifiers.

May be given a single identifier, a sequence of identifiers, or the special symbols “head” or “base”. The result is a tuple of one or more identifiers, or an empty tuple in the case of “base”.

In the cases where ‘head’, ‘heads’ is requested and the revision map is empty, returns an empty tuple.

Supports partial identifiers, where the given identifier is matched against all identifiers that start with the given characters; if there is exactly one match, that determines the full revision.

heads[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.heads "Link to this definition")
All “head” revisions as strings.

This is normally a tuple of length one, unless unmerged branches are present.

Returns:
a tuple of string revision numbers.

iterate_revisions(_upper:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _lower:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),...]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _implicit\_base:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _inclusive:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _assert\_relative\_length:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=True_, _select\_for\_downgrade:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_)→[Iterator](https://docs.python.org/3/library/typing.html#typing.Iterator "(in Python v3.14)")[[Revision](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision")][#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.RevisionMap.iterate_revisions "Link to this definition")
Iterate through script revisions, starting at the given upper revision identifier and ending at the lower.

The traversal uses strictly the down_revision marker inside each migration script, so it is a requirement that upper >= lower, else you’ll get nothing back.

The iterator yields [`Revision`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.revision.Revision "alembic.script.revision.Revision") objects.

Write Hooks[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#module-alembic.script.write_hooks "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

alembic.script.write_hooks.register(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.write_hooks.register "Link to this definition")
A function decorator that will register that function as a write hook.

See the documentation linked below for an example.
