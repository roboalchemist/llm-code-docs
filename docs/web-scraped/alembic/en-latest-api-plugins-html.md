# Source: https://alembic.sqlalchemy.org/en/latest/api/plugins.html

Title: Plugins — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/plugins.html

Markdown Content:
Plugins[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugins "Link to this heading")
----------------------------------------------------------------------------------------------------

Added in version 1.18.0.

Alembic provides a plugin system that allows third-party extensions to integrate with Alembic’s functionality. Plugins can register custom operations, operation implementations, autogenerate comparison functions, and other extension points to add new capabilities to Alembic.

The plugin system provides a structured way to organize and distribute these extensions, allowing them to be discovered automatically using Python entry points.

Overview[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#overview "Link to this heading")
------------------------------------------------------------------------------------------------------

The [`Plugin`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "alembic.runtime.plugins.Plugin") class provides the foundation for creating plugins. A plugin’s `setup()` function can perform various types of registrations:

*   **Custom operations** - Register new operation directives using [`Operations.register_operation()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.register_operation "alembic.operations.Operations.register_operation") (e.g., `op.create_view()`)

*   **Operation implementations** - Provide database-specific implementations using [`Operations.implementation_for()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.implementation_for "alembic.operations.Operations.implementation_for")

*   **Autogenerate comparators** - Add comparison functions for detecting schema differences during autogeneration

*   **Other extensions** - Register any other global handlers or customizations

A single plugin can register handlers across all of these categories. For example, a plugin for custom database objects might register both the operations to create/drop those objects and the autogenerate logic to detect changes to them.

See also

[Replaceable Objects](https://alembic.sqlalchemy.org/en/latest/cookbook.html#replaceable-objects) - Cookbook recipe demonstrating custom operations and implementations that would be suitable for packaging as a plugin

Installing and Using Plugins[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#installing-and-using-plugins "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Third-party plugins are typically distributed as Python packages that can be installed via pip or other package managers:

pip install mycompany-alembic-plugin

Once installed, plugins that use Python’s entry point system are automatically discovered and loaded by Alembic at startup, which calls the plugin’s `setup()` function to perform any registrations.

### Enable Autogenerate Plugins[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#enable-autogenerate-plugins "Link to this heading")

For plugins that provide autogenerate comparison functions via the [`Plugin.add_autogenerate_comparator()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator "alembic.runtime.plugins.Plugin.add_autogenerate_comparator") hook, the specific autogenerate functionality registered by the plugin must be enabled with [`EnvironmentContext.configure.autogenerate_plugins`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.autogenerate_plugins "alembic.runtime.environment.EnvironmentContext.configure") parameter, which by default indicates that only Alembic’s built-in plugins should be used. Note that this step does not apply to older plugins that may be registering autogenerate comparison functions globally.

See the section [Enabling Autogenerate Plugins in env.py](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugins-autogenerate) for background on enabling autogenerate comparison plugins per environment.

### Using Plugins without entry points (such as local plugin code)[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#using-plugins-without-entry-points-such-as-local-plugin-code "Link to this heading")

Plugins do not need to be published with entry points to be used. A plugin can be manually registered by calling [`Plugin.setup_plugin_from_module()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.setup_plugin_from_module "alembic.runtime.plugins.Plugin.setup_plugin_from_module") in the `env.py` file:

from alembic.runtime.plugins import Plugin
import myproject.alembic_plugin

# Register the plugin manually
Plugin.setup_plugin_from_module(
    myproject.alembic_plugin,
    "myproject.custom_operations"
)

This approach is useful for project-specific plugins that are not intended for distribution, or for testing plugins during development.

Enabling Autogenerate Plugins in env.py[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#enabling-autogenerate-plugins-in-env-py "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

If a plugin provides autogenerate functionality that’s registered via the [`Plugin.add_autogenerate_comparator()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator "alembic.runtime.plugins.Plugin.add_autogenerate_comparator") hook, it can be selectively enabled or disabled using the [`EnvironmentContext.configure.autogenerate_plugins`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.autogenerate_plugins "alembic.runtime.environment.EnvironmentContext.configure") parameter in the [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") call, typically as used within the `env.py` file. This parameter is passed as a list of strings each naming a specific plugin or a matching wildcard. The default value is `["alembic.autogenerate.*"]` which indicates that the full set of Alembic’s internal plugins should be used.

The [`EnvironmentContext.configure.autogenerate_plugins`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.autogenerate_plugins "alembic.runtime.environment.EnvironmentContext.configure") parameter accepts a list of string patterns:

*   Simple names match plugin names exactly: `"alembic.autogenerate.tables"`

*   Wildcards match multiple plugins: `"alembic.autogenerate.*"` matches all built-in plugins

*   Negation patterns exclude plugins: `"~alembic.autogenerate.comments"` excludes the comments plugin

For example, to use all built-in plugins except comments, plus a custom plugin:

context.configure(
    # ...
    autogenerate_plugins=[
        "alembic.autogenerate.*",
        "~alembic.autogenerate.comments",
        "mycompany.custom_types",
    ]
)

The wildcard syntax using `*` indicates that tokens in that segment of the name (separated by period characters) will match any name. For Alembic’s `alembic.autogenerate.*` namespace, the built in names being invoked are:

*   `alembic.autogenerate.schemas` - Schema creation and dropping

*   `alembic.autogenerate.tables` - Table creation, dropping, and modification. This plugin depends on the `schemas` plugin in order to iterate through tables.

*   `alembic.autogenerate.types` - Column type changes. This plugin depends on the `tables` plugin in order to iterate through columns.

*   `alembic.autogenerate.constraints` - Constraint creation and dropping. This plugin depends on the `tables` plugin in order to iterate through columns.

*   `alembic.autogenerate.defaults` - Server default changes. This plugin depends on the `tables` plugin in order to iterate through columns.

*   `alembic.autogenerate.comments` - Table and column comment changes. This plugin depends on the `tables` plugin in order to iterate through columns.

While these names can be specified individually, they are subject to change as Alembic evolves. Using the wildcard pattern is recommended.

Omitting the built-in plugins entirely would prevent autogeneration from proceeding, unless other plugins were provided that replaced its functionality (which is possible!). Additionally, as noted above, the column-oriented plugins rely on the table- and schema- oriented plugins in order to receive iterated columns.

The [`EnvironmentContext.configure.autogenerate_plugins`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.autogenerate_plugins "alembic.runtime.environment.EnvironmentContext.configure") parameter only controls which plugins participate in autogenerate operations. Other plugin functionality, such as custom operations registered with [`Operations.register_operation()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.register_operation "alembic.operations.Operations.register_operation"), is available regardless of this setting.

Writing a Plugin[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#writing-a-plugin "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

### Creating a Plugin Module[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#creating-a-plugin-module "Link to this heading")

A plugin module must define a `setup()` function that accepts a [`Plugin`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "alembic.runtime.plugins.Plugin") instance. This function is called when the plugin is loaded, either automatically via entry points or manually via [`Plugin.setup_plugin_from_module()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.setup_plugin_from_module "alembic.runtime.plugins.Plugin.setup_plugin_from_module"):

from alembic import op
from alembic.operations import Operations
from alembic.runtime.plugins import Plugin
from alembic.util import DispatchPriority

def setup(plugin: Plugin) -> None:
 """Setup function called by Alembic when loading the plugin."""

    # Register custom operations
    Operations.register_operation("create_view")(CreateViewOp)
    Operations.implementation_for(CreateViewOp)(create_view_impl)

    # Register autogenerate comparison functions
    plugin.add_autogenerate_comparator(
        _compare_views,
        "view",
        qualifier="default",
        priority=DispatchPriority.MEDIUM,
    )

The `setup()` function serves as the entry point for all plugin registrations. It can call various Alembic APIs to extend functionality.

### Publishing a Plugin[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#publishing-a-plugin "Link to this heading")

To make a plugin available for installation via pip, create a package with an entry point in `pyproject.toml`:

[project.entry-points."alembic.plugins"]
mycompany.plugin_name = "mycompany.alembic_plugin"

Where `mycompany.alembic_plugin` is the module containing the `setup()` function.

When the package is installed, Alembic automatically discovers and loads the plugin through the entry point system. If the plugin provides autogenerate functionality, users can then enable it by adding its name `mycompany.plugin_name` to the `autogenerate_plugins` list in their `env.py`.

### Registering Custom Operations[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#registering-custom-operations "Link to this heading")

Plugins can register new operation directives that become available as `op.custom_operation()` in migration scripts. This is done using [`Operations.register_operation()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.register_operation "alembic.operations.Operations.register_operation") and [`Operations.implementation_for()`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations.implementation_for "alembic.operations.Operations.implementation_for").

Example from the [Replaceable Objects](https://alembic.sqlalchemy.org/en/latest/cookbook.html#replaceable-objects) recipe:

from alembic.operations import Operations, MigrateOperation

class CreateViewOp(MigrateOperation):
    def  __init__ (self, view_name, select_stmt):
        self.view_name = view_name
        self.select_stmt = select_stmt

@Operations.register_operation("create_view")
class CreateViewOp(CreateViewOp):
    pass

@Operations.implementation_for(CreateViewOp)
def create_view(operations, operation):
    operations.execute(
        f"CREATE VIEW {operation.view_name} AS {operation.select_stmt}"
    )

These registrations can be performed in the plugin’s `setup()` function, making the custom operations available globally.

### Registering Autogenerate Comparators at the Plugin Level[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#registering-autogenerate-comparators-at-the-plugin-level "Link to this heading")

Plugins can register comparison functions that participate in the autogenerate process, detecting differences between database schema and SQLAlchemy metadata. These functions may be registered globally, where they take place unconditionally as documented at [Registering a Comparison Function Globally](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#autogenerate-global-comparison-function); for older versions of Alembic prior to 1.18.0 this is the only registration system available. However when targeting Alembic 1.18.0 or higher, the [`Plugin`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "alembic.runtime.plugins.Plugin") approach provides a more configurable version of these registration hooks.

Plugin level comparison functions are registered using [`Plugin.add_autogenerate_comparator()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator "alembic.runtime.plugins.Plugin.add_autogenerate_comparator"). Each comparison function establishes itself as part of a named “target”, which is invoked by a parent handler. For example, if a handler establishes itself as part of the `"column"` target, it will be invoked when the `alembic.autogenerate.tables` plugin proceeds through SQLAlchemy `Table` objects and invokes comparison operations for pairs of same-named columns.

For an example of a complete comparison function, see the example at [Registering a Comparison Function Globally](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#autogenerate-global-comparison-function).

The current levels of comparison are the same between global and plugin-level comparison functions, and include:

*   `"autogenerate"` - this target is invoked at the top of the autogenerate chain. These hooks are passed a [`AutogenContext`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "alembic.autogenerate.api.AutogenContext") and an [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") collection. Functions that subscribe to the `autogenerate` target should look like:

from alembic.autogenerate.api import AutogenContext
from alembic.operations.ops import UpgradeOps
from alembic.runtime.plugins import Plugin
from alembic.util import PriorityDispatchResult

def autogen_toplevel(
    autogen_context: AutogenContext, upgrade_ops: UpgradeOps
) -> PriorityDispatchResult:
    # ...

def setup(plugin: Plugin) -> None:
    plugin.add_autogenerate_comparator(autogen_toplevel, "autogenerate") 
The function should return either [`PriorityDispatchResult.CONTINUE`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.CONTINUE "alembic.util.langhelpers.PriorityDispatchResult.CONTINUE") or [`PriorityDispatchResult.STOP`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.STOP "alembic.util.langhelpers.PriorityDispatchResult.STOP") to halt any further comparisons from proceeding, and should respond to detected changes by mutating the given [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") collection in place (the [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") version is produced later by reversing the [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps")).

An autogenerate compare function that seeks to run entirely independently of Alembic’s built-in autogenerate plugins, or to replace them completely, would register at the `"autogenerate"` level. The remaining levels indicated below are all invoked from within Alembic’s own autogenerate plugins and will not take place if `alembic.autogenerate.*` is not enabled.

Added in version 1.18.0: The `"autogenerate"` comparison scope was introduced, replacing `"schema"` as the topmost comparison scope.

*   `"schema"` - this target is invoked for each individual “schema” being compared, and hooks are passed a [`AutogenContext`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "alembic.autogenerate.api.AutogenContext"), an [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") collection, and a set of schema names, featuring the value `None` for the “default” schema. Functions that subscribe to the `"schema"` target should look like:

from alembic.autogenerate.api import AutogenContext
from alembic.operations.ops import UpgradeOps
from alembic.runtime.plugins import Plugin
from alembic.util import PriorityDispatchResult

def autogen_for_tables(
    autogen_context: AutogenContext,
    upgrade_ops: UpgradeOps,
    schemas: set[str | None],
) -> PriorityDispatchResult:
    # ...

def setup(plugin: Plugin) -> None:
    plugin.add_autogenerate_comparator(
        autogen_for_tables,
        "schema",
        "tables",
    ) 
The function should normally return [`PriorityDispatchResult.CONTINUE`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.CONTINUE "alembic.util.langhelpers.PriorityDispatchResult.CONTINUE") and should respond to detected changes by mutating the given [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") collection in place (the [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") version is produced later by reversing the [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps")).

The registration example above includes the `"tables"` “compare element”, which is optional. This indicates that the comparison function is part of a chain called “tables”, which is what Alembic’s own `alembic.autogenerate.tables` plugin uses. If our custom comparison function were to return the value [`PriorityDispatchResult.STOP`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.STOP "alembic.util.langhelpers.PriorityDispatchResult.STOP"), further comparison functions in the `"tables"` chain would not be called. Similarly, if another plugin in the `"tables"` chain returned [`PriorityDispatchResult.STOP`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.STOP "alembic.util.langhelpers.PriorityDispatchResult.STOP"), then our plugin would not be called. Making use of [`PriorityDispatchResult.STOP`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.STOP "alembic.util.langhelpers.PriorityDispatchResult.STOP") in terms of other plugins in the same “compare element” may be assisted by placing our function in the comparator chain using [`DispatchPriority.FIRST`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.FIRST "alembic.util.langhelpers.DispatchPriority.FIRST") or [`DispatchPriority.LAST`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.LAST "alembic.util.langhelpers.DispatchPriority.LAST") when registering.

*   `"table"` - this target is invoked per `Table` being compared between a database autoloaded version and the local metadata version. These hooks are passed an [`AutogenContext`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "alembic.autogenerate.api.AutogenContext"), a [`ModifyTableOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.ModifyTableOps "alembic.operations.ops.ModifyTableOps") collection, a schema name, table name, a [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") reflected from the database if any or `None`, and a [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") present in the local [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)"). If the [`ModifyTableOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.ModifyTableOps "alembic.operations.ops.ModifyTableOps") collection contains changes after all hooks are run, it is included in the migration script:

from sqlalchemy import quoted_name
from sqlalchemy import Table

from alembic.autogenerate.api import AutogenContext
from alembic.operations.ops import ModifyTableOps
from alembic.runtime.plugins import Plugin
from alembic.util import PriorityDispatchResult

def compare_tables(
    autogen_context: AutogenContext,
    modify_table_ops: ModifyTableOps,
    schema: str | None,
    tname: quoted_name | str,
    conn_table: Table | None,
    metadata_table: Table | None,
) -> PriorityDispatchResult:
    # ...

def setup(plugin: Plugin) -> None:
    plugin.add_autogenerate_comparator(compare_tables, "table") 
This hook may be used to compare elements of tables, such as comments or database-specific storage configurations. It should mutate the given [`ModifyTableOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.ModifyTableOps "alembic.operations.ops.ModifyTableOps") object in place to add new change operations.

*   `"column"` - this target is invoked per `Column` being compared between a database autoloaded version and the local metadata version. These hooks are passed an [`AutogenContext`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "alembic.autogenerate.api.AutogenContext"), an [`AlterColumnOp`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AlterColumnOp "alembic.operations.ops.AlterColumnOp") object, a schema name, table name, column name, a [`Column`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Column "(in SQLAlchemy v2.1)") reflected from the database and a [`Column`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Column "(in SQLAlchemy v2.1)") present in the local table. If the [`AlterColumnOp`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AlterColumnOp "alembic.operations.ops.AlterColumnOp") contains changes after all hooks are run, it is included in the migration script; a “change” is considered to be present if any of the `modify_` attributes are set to a non-default value, or there are any keys in the `.kw` collection with the prefix `"modify_"`:

from typing import Any
from sqlalchemy import quoted_name
from sqlalchemy import Table

from alembic.autogenerate.api import AutogenContext
from alembic.operations.ops import AlterColumnOp
from alembic.runtime.plugins import Plugin
from alembic.util import PriorityDispatchResult

def compare_columns(
    autogen_context: AutogenContext,
    alter_column_op: AlterColumnOp,
    schema: str | None,
    tname: quoted_name | str,
    cname: quoted_name | str,
    conn_col: Column[Any],
    metadata_col: Column[Any],
) -> PriorityDispatchResult:
  # ...

def setup(plugin: Plugin) -> None:
    plugin.add_autogenerate_comparator(compare_columns, "column") 
Pre-existing compare chains within the `"column"` target include `"comment"`, `"server_default"`, and `"types"`. Comparison functions here should mutate the given [`AlterColumnOp`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AlterColumnOp "alembic.operations.ops.AlterColumnOp") object in place to add new change operations.

Plugin API Reference[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugin-api-reference "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

class alembic.runtime.plugins.Plugin(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "Link to this definition")
Describe a series of functions that are pulled in as a plugin.

This is initially to provide for portable lists of autogenerate comparison functions, however the setup for a plugin can run any other kinds of global registration as well.

Added in version 1.18.0.

add_autogenerate_comparator(_fn:Callable[...,[PriorityDispatchResult](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult "alembic.util.langhelpers.PriorityDispatchResult")]_, _compare\_target:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_, _compare\_element:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _*_, _qualifier:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='default'_, _priority:[DispatchPriority](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority "alembic.util.langhelpers.DispatchPriority")=DispatchPriority.MEDIUM_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator "Link to this definition")
Register an autogenerate comparison function.

See the section [Registering Autogenerate Comparators at the Plugin Level](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugins-registering-autogenerate) for detailed examples on how to use this method.

Parameters:
*   **fn**[¶](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator.params.fn) – The comparison function to register. The function receives arguments specific to the type of comparison being performed and should return a [`PriorityDispatchResult`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult "alembic.util.langhelpers.PriorityDispatchResult") value.

*   **compare_target**[¶](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator.params.compare_target) – The type of comparison being performed (e.g., `"table"`, `"column"`, `"type"`).

*   **compare_element**[¶](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator.params.compare_element) – Optional sub-element being compared within the target type.

*   **qualifier**[¶](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator.params.qualifier) – Database dialect qualifier. Use `"default"` for all dialects, or specify a dialect name like `"postgresql"` to register a dialect-specific handler. Defaults to `"default"`.

*   **priority**[¶](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator.params.priority) – Execution priority for this comparison function. Functions are executed in priority order from [`DispatchPriority.FIRST`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.FIRST "alembic.util.langhelpers.DispatchPriority.FIRST") to [`DispatchPriority.LAST`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.LAST "alembic.util.langhelpers.DispatchPriority.LAST"). Defaults to [`DispatchPriority.MEDIUM`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.MEDIUM "alembic.util.langhelpers.DispatchPriority.MEDIUM").

classmethod populate_autogenerate_priority_dispatch(_comparators:PriorityDispatcher_, _include\_plugins:[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.populate_autogenerate_priority_dispatch "Link to this definition")
Populate all current autogenerate comparison functions into a given PriorityDispatcher.

remove()→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.remove "Link to this definition")
remove this plugin

classmethod setup_plugin_from_module(_module:[ModuleType](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.14)")_, _name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")_)→[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.setup_plugin_from_module "Link to this definition")
Call the `setup()` function of a plugin module, identified by passing the module object itself.

E.g.:

from alembic.runtime.plugins import Plugin
import myproject.alembic_plugin

# Register the plugin manually
Plugin.setup_plugin_from_module(
    myproject.alembic_plugin,
    "myproject.custom_operations"
)

This will generate a new [`Plugin`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "alembic.runtime.plugins.Plugin") object with the given name, which will register itself in the global list of plugins. Then the module’s `setup()` function is invoked, passing that [`Plugin`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin "alembic.runtime.plugins.Plugin") object.

This exact process is invoked automatically at import time for any plugin module that is published via the `alembic.plugins` entrypoint.

class alembic.util.langhelpers.PriorityDispatchResult(_*values_)[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult "Link to this definition")
indicate an action after running a function within a `PriorityDispatcher`

Added in version 1.18.0.

CONTINUE=1[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.CONTINUE "Link to this definition")
Continue running more functions.

Any return value that is not PriorityDispatchResult.STOP is equivalent to this.

STOP=2[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.PriorityDispatchResult.STOP "Link to this definition")
Stop running any additional functions within the subgroup

class alembic.util.langhelpers.DispatchPriority(_*values_)[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority "Link to this definition")
Indicate which of three sub-collections a function inside a `PriorityDispatcher` should be placed.

Added in version 1.18.0.

FIRST=50[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.FIRST "Link to this definition")
Run the funciton in the first batch of functions (highest priority)

LAST=10[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.LAST "Link to this definition")
Run the function in the last batch of functions

MEDIUM=25[#](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.util.langhelpers.DispatchPriority.MEDIUM "Link to this definition")
Run the function at normal priority (this is the default)
