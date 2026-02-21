# Source: https://alembic.sqlalchemy.org/en/latest/api/

Title: API Details — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/

Markdown Content:
API Details — Alembic 1.18.4 documentation
===============

[Skip to main content](https://alembic.sqlalchemy.org/en/latest/api/#main-content)

Back to top- [x] - [x] 

Ctrl+K

[Alembic 1.18.4 documentation](https://alembic.sqlalchemy.org/en/latest/index.html)

[Download documentation as ZIP file](https://alembic.sqlalchemy.org/en/latest/api/alembic_latest.zip)

*   [GitHub](https://github.com/sqlalchemy/alembic "GitHub")
*   [![Image 1: PyPI](https://img.shields.io/pypi/dw/alembic)](https://pypi.org/project/alembic/ "PyPI")

Search Ctrl+K

*   [Front Matter](https://alembic.sqlalchemy.org/en/latest/front.html)
*   [Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
*   [Auto Generating Migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
*   [Generating SQL Scripts (a.k.a. “Offline Mode”)](https://alembic.sqlalchemy.org/en/latest/offline.html)
*   [The Importance of Naming Constraints](https://alembic.sqlalchemy.org/en/latest/naming.html)
*   [Running “Batch” Migrations for SQLite and Other Databases](https://alembic.sqlalchemy.org/en/latest/batch.html)
*   [Working with Branches](https://alembic.sqlalchemy.org/en/latest/branches.html)
*   [Operation Reference](https://alembic.sqlalchemy.org/en/latest/ops.html)
*   [Cookbook](https://alembic.sqlalchemy.org/en/latest/cookbook.html)
*   [API Details](https://alembic.sqlalchemy.org/en/latest/api/#)

    *   [Overview](https://alembic.sqlalchemy.org/en/latest/api/overview.html)
    *   [Runtime Objects](https://alembic.sqlalchemy.org/en/latest/api/runtime.html)
    *   [Configuration](https://alembic.sqlalchemy.org/en/latest/api/config.html)
    *   [Commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html)
    *   [Operation Directives](https://alembic.sqlalchemy.org/en/latest/api/operations.html)
    *   [Autogeneration](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html)
    *   [Script Directory](https://alembic.sqlalchemy.org/en/latest/api/script.html)
    *   [DDL Internals](https://alembic.sqlalchemy.org/en/latest/api/ddl.html)
    *   [Plugins](https://alembic.sqlalchemy.org/en/latest/api/plugins.html)
    *   [Exception Objects](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html)

*   [Changelog](https://alembic.sqlalchemy.org/en/latest/changelog.html)

*   [.rst](https://alembic.sqlalchemy.org/en/latest/_sources/api/index.rst "Download source file")
*   .pdf

API Details
===========

API Details[#](https://alembic.sqlalchemy.org/en/latest/api/#api-details "Link to this heading")
================================================================================================

Alembic’s internal API has many public integration points that can be used to extend Alembic’s functionality as well as to reuse its functionality in new ways. As the project has grown, more APIs are created and exposed for this purpose.

Direct use of the vast majority of API details discussed here is not needed for rudimentary use of Alembic; the only API that is used normally by end users is the methods provided by the [`Operations`](https://alembic.sqlalchemy.org/en/latest/ops.html#alembic.operations.Operations "alembic.operations.Operations") class, which is discussed outside of this subsection, and the parameters that can be passed to the [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") method, used when configuring one’s `env.py` environment. However, real-world applications will usually end up using more of the internal API, in particular being able to run commands programmatically, as discussed in the section [Commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html).

*   [Overview](https://alembic.sqlalchemy.org/en/latest/api/overview.html)
*   [Runtime Objects](https://alembic.sqlalchemy.org/en/latest/api/runtime.html)
    *   [The Environment Context](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#the-environment-context)
    *   [The Migration Context](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#the-migration-context)

*   [Configuration](https://alembic.sqlalchemy.org/en/latest/api/config.html)
    *   [`CommandFunction`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandFunction)
    *   [`CommandLine`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.CommandLine)
    *   [`Config`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.Config)
    *   [`MessagingOptions`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.MessagingOptions)
    *   [`main()`](https://alembic.sqlalchemy.org/en/latest/api/config.html#alembic.config.main)

*   [Commands](https://alembic.sqlalchemy.org/en/latest/api/commands.html)
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

*   [Operation Directives](https://alembic.sqlalchemy.org/en/latest/api/operations.html)
    *   [Operation Plugins](https://alembic.sqlalchemy.org/en/latest/api/operations.html#operation-plugins)
    *   [Built-in Operation Objects](https://alembic.sqlalchemy.org/en/latest/api/operations.html#built-in-operation-objects)
    *   [Extending Existing Operations](https://alembic.sqlalchemy.org/en/latest/api/operations.html#extending-existing-operations)

*   [Autogeneration](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html)
    *   [Getting Diffs](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#getting-diffs)
    *   [Customizing Revision Generation](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#customizing-revision-generation)
    *   [Autogenerating Custom Operation Directives](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#autogenerating-custom-operation-directives)

*   [Script Directory](https://alembic.sqlalchemy.org/en/latest/api/script.html)
    *   [`Script`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.Script)
    *   [`ScriptDirectory`](https://alembic.sqlalchemy.org/en/latest/api/script.html#alembic.script.ScriptDirectory)
    *   [Revision](https://alembic.sqlalchemy.org/en/latest/api/script.html#revision)
    *   [Write Hooks](https://alembic.sqlalchemy.org/en/latest/api/script.html#module-alembic.script.write_hooks)

*   [DDL Internals](https://alembic.sqlalchemy.org/en/latest/api/ddl.html)
    *   [`AddColumn`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.AddColumn)
    *   [`AlterColumn`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.AlterColumn)
    *   [`AlterTable`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.AlterTable)
    *   [`ColumnComment`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ColumnComment)
    *   [`ColumnDefault`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ColumnDefault)
    *   [`ColumnName`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ColumnName)
    *   [`ColumnNullable`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ColumnNullable)
    *   [`ColumnType`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ColumnType)
    *   [`ComputedColumnDefault`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.ComputedColumnDefault)
    *   [`DropColumn`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.DropColumn)
    *   [`IdentityColumnDefault`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.IdentityColumnDefault)
    *   [`RenameTable`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.RenameTable)
    *   [`add_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.add_column)
    *   [`alter_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.alter_column)
    *   [`alter_table()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.alter_table)
    *   [`drop_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.drop_column)
    *   [`format_column_name()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.format_column_name)
    *   [`format_server_default()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.format_server_default)
    *   [`format_table_name()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.format_table_name)
    *   [`format_type()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.format_type)
    *   [`quote_dotted()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.quote_dotted)
    *   [`visit_add_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_add_column)
    *   [`visit_column_default()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_column_default)
    *   [`visit_column_name()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_column_name)
    *   [`visit_column_nullable()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_column_nullable)
    *   [`visit_column_type()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_column_type)
    *   [`visit_computed_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_computed_column)
    *   [`visit_drop_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_drop_column)
    *   [`visit_identity_column()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_identity_column)
    *   [`visit_rename_table()`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.visit_rename_table)
    *   [`DefaultImpl`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.impl.DefaultImpl)
    *   [`ImplMeta`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.impl.ImplMeta)
    *   [`Params`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.impl.Params)
    *   [MySQL](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#module-alembic.ddl.mysql)
    *   [MS-SQL](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#module-alembic.ddl.mssql)
    *   [Postgresql](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#module-alembic.ddl.postgresql)
    *   [SQLite](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#module-alembic.ddl.sqlite)

*   [Plugins](https://alembic.sqlalchemy.org/en/latest/api/plugins.html)
    *   [Overview](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#overview)
    *   [Installing and Using Plugins](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#installing-and-using-plugins)
    *   [Enabling Autogenerate Plugins in env.py](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#enabling-autogenerate-plugins-in-env-py)
    *   [Writing a Plugin](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#writing-a-plugin)
    *   [Plugin API Reference](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugin-api-reference)

*   [Exception Objects](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html)
    *   [`AutogenerateDiffsDetected`](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html#alembic.util.exc.AutogenerateDiffsDetected)
    *   [`CommandError`](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html#alembic.util.exc.CommandError)
    *   [`DatabaseNotAtHead`](https://alembic.sqlalchemy.org/en/latest/api/exceptions.html#alembic.util.exc.DatabaseNotAtHead)

[previous Cookbook](https://alembic.sqlalchemy.org/en/latest/cookbook.html "previous page")[next Overview](https://alembic.sqlalchemy.org/en/latest/api/overview.html "next page")

By Mike Bayer

© Copyright 2010-2026, Mike Bayer.
