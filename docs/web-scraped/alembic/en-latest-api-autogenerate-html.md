# Source: https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html

Title: Autogeneration — Alembic 1.18.4 documentation

URL Source: https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html

Markdown Content:
Autogeneration[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#autogeneration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Note

this section discusses the **internal API of Alembic** as regards the autogeneration feature of the `alembic revision` command. This section is only useful for developers who wish to extend the capabilities of Alembic. For general documentation on the autogenerate feature, please see [Auto Generating Migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html).

The autogeneration system has a wide degree of public API, including the following areas:

1.   The ability to do a “diff” of a [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object against a database, and receive a data structure back. This structure is available either as a rudimentary list of changes, or as a [`MigrateOperation`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation") structure.

2.   The ability to alter how the `alembic revision` command generates revision scripts, including support for multiple revision scripts generated in one pass.

3.   The ability to add new operation directives to autogeneration, including custom schema/model comparison functions and revision script rendering.

Getting Diffs[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#getting-diffs "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

The simplest API autogenerate provides is the “schema comparison” API; these are simple functions that will run all registered “comparison” functions between a [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object and a database backend to produce a structure showing how they differ. The two functions provided are [`compare_metadata()`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata "alembic.autogenerate.compare_metadata"), which is more of the “legacy” function that produces diff tuples, and [`produce_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.produce_migrations "alembic.autogenerate.produce_migrations"), which produces a structure consisting of operation directives detailed in [Operation Directives](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic-operations-toplevel).

alembic.autogenerate.compare_metadata(_context:[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")_, _metadata:MetaData_)→Any[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata "Link to this definition")
Compare a database schema to that given in a [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") instance.

The database connection is presented in the context of a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") object, which provides database connectivity as well as optional comparison functions to use for datatypes and server defaults - see the “autogenerate” arguments at [`EnvironmentContext.configure()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure "alembic.runtime.environment.EnvironmentContext.configure") for details on these.

The return format is a list of “diff” directives, each representing individual differences:

from alembic.migration import MigrationContext
from alembic.autogenerate import compare_metadata
from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    Table,
    text,
)
import pprint

engine = create_engine("sqlite://")

with engine.begin() as conn:
    conn.execute(
        text(
 '''
 create table foo (
 id integer not null primary key,
 old_data varchar,
 x integer
 )
 '''
        )
    )
    conn.execute(text("create table bar (data varchar)"))

metadata = MetaData()
Table(
    "foo",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("data", Integer),
    Column("x", Integer, nullable=False),
)
Table("bat", metadata, Column("info", String))

mc = MigrationContext.configure(engine.connect())

diff = compare_metadata(mc, metadata)
pprint.pprint(diff, indent=2, width=20)

Output:

[
    (
        "add_table",
        Table(
            "bat",
            MetaData(),
            Column("info", String(), table=<bat>),
            schema=None,
        ),
    ),
    (
        "remove_table",
        Table(
            "bar",
            MetaData(),
            Column("data", VARCHAR(), table=<bar>),
            schema=None,
        ),
    ),
    (
        "add_column",
        None,
        "foo",
        Column("data", Integer(), table=<foo>),
    ),
    [
        (
            "modify_nullable",
            None,
            "foo",
            "x",
            {
                "existing_comment": None,
                "existing_server_default": False,
                "existing_type": INTEGER(),
            },
            True,
            False,
        )
    ],
    (
        "remove_column",
        None,
        "foo",
        Column("old_data", VARCHAR(), table=<foo>),
    ),
]

Parameters:
*   **context**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata.params.context) – a [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") instance.

*   **metadata**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata.params.metadata) – a [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") instance.

alembic.autogenerate.produce_migrations(_context:[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")_, _metadata:MetaData_)→[MigrationScript](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.produce_migrations "Link to this definition")
Produce a [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") structure based on schema comparison.

This function does essentially what [`compare_metadata()`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata "alembic.autogenerate.compare_metadata") does, but then runs the resulting list of diffs to produce the full [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") object. For an example of what this looks like, see the example in [Customizing Revision Generation](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#customizing-revision).

See also

[`compare_metadata()`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.compare_metadata "alembic.autogenerate.compare_metadata") - returns more fundamental “diff” data from comparing a schema.

Customizing Revision Generation[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#customizing-revision-generation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------

The `alembic revision` command, also available programmatically via [`command.revision()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision "alembic.command.revision"), essentially produces a single migration script after being run. Whether or not the `--autogenerate` option was specified basically determines if this script is a blank revision script with empty `upgrade()` and `downgrade()` functions, or was produced with alembic operation directives as the result of autogenerate.

In either case, the system creates a full plan of what is to be done in the form of a [`MigrateOperation`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation") structure, which is then used to produce the script.

For example, suppose we ran `alembic revision --autogenerate`, and the end result was that it produced a new revision `'eced083f5df'` with the following contents:

"""create the organization table."""

# revision identifiers, used by Alembic.
revision = 'eced083f5df'
down_revision = 'beafc7d709f'

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'organization',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )
    op.add_column(
        'user',
        sa.Column('organization_id', sa.Integer())
    )
    op.create_foreign_key(
        'org_fk', 'user', 'organization', ['organization_id'], ['id']
    )

def downgrade():
    op.drop_constraint('org_fk', 'user')
    op.drop_column('user', 'organization_id')
    op.drop_table('organization')

The above script is generated by a [`MigrateOperation`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation") structure that looks like this:

from alembic.operations import ops
import sqlalchemy as sa

migration_script = ops.MigrationScript(
    'eced083f5df',
    ops.UpgradeOps(
        ops=[
            ops.CreateTableOp(
                'organization',
                [
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('name', sa.String(50), nullable=False)
                ]
            ),
            ops.ModifyTableOps(
                'user',
                ops=[
                    ops.AddColumnOp(
                        'user',
                        sa.Column('organization_id', sa.Integer())
                    ),
                    ops.CreateForeignKeyOp(
                        'org_fk', 'user', 'organization',
                        ['organization_id'], ['id']
                    )
                ]
            )
        ]
    ),
    ops.DowngradeOps(
        ops=[
            ops.ModifyTableOps(
                'user',
                ops=[
                    ops.DropConstraintOp('org_fk', 'user'),
                    ops.DropColumnOp('user', 'organization_id')
                ]
            ),
            ops.DropTableOp('organization')
        ]
    ),
    message='create the organization table.'
)

When we deal with a [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") structure, we can render the upgrade/downgrade sections into strings for debugging purposes using the [`render_python_code()`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code "alembic.autogenerate.render_python_code") helper function:

from alembic.autogenerate import render_python_code
print(render_python_code(migration_script.upgrade_ops))

Renders:

### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('organization_id', sa.Integer(), nullable=True))
    op.create_foreign_key('org_fk', 'user', 'organization', ['organization_id'], ['id'])
    ### end Alembic commands ###

Given that structures like the above are used to generate new revision files, and that we’d like to be able to alter these as they are created, we then need a system to access this structure when the [`command.revision()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision "alembic.command.revision") command is used. The [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure") parameter gives us a way to alter this. This is a function that is passed the above structure as generated by Alembic, giving us a chance to alter it. For example, if we wanted to put all the “upgrade” operations into a certain branch, and we wanted our script to not have any “downgrade” operations at all, we could build an extension as follows, illustrated within an `env.py` script:

def process_revision_directives(context, revision, directives):
    script = directives[0]

    # set specific branch
    script.head = "mybranch@head"

    # erase downgrade operations
    script.downgrade_ops.ops[:] = []

# ...

def run_migrations_online():

    # ...
    with engine.connect() as connection:

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives)

        with context.begin_transaction():
            context.run_migrations()

Above, the `directives` argument is a Python list. We may alter the given structure within this list in-place, or replace it with a new structure consisting of zero or more [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") directives. The [`command.revision()`](https://alembic.sqlalchemy.org/en/latest/api/commands.html#alembic.command.revision "alembic.command.revision") command will then produce scripts corresponding to whatever is in this list.

alembic.autogenerate.render_python_code(_up\_or\_down\_op:[UpgradeOps](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps")|[DowngradeOps](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps")_, _sqlalchemy\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='sa.'_, _alembic\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")='op.'_, _render\_as\_batch:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=False_, _imports:Sequence[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]=()_, _render\_item:RenderItemFn|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _migration\_context:[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _user\_module\_prefix:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_)→[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code "Link to this definition")
Render Python code given an [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") or [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") object.

This is a convenience function that can be used to test the autogenerate output of a user-defined [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") structure.

Parameters:
*   **up_or_down_op**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.up_or_down_op) – [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") or [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") object

*   **sqlalchemy_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.sqlalchemy_module_prefix) – module prefix for SQLAlchemy objects

*   **alembic_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.alembic_module_prefix) – module prefix for Alembic constructs

*   **render_as_batch**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.render_as_batch) – use “batch operations” style for rendering

*   **imports**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.imports) – sequence of import symbols to add

*   **render_item**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.render_item) – callable to render items

*   **migration_context**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.migration_context) – optional [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")

*   **user_module_prefix**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.render_python_code.params.user_module_prefix) –

optional string prefix for user-defined types

Added in version 1.11.0.

### Fine-Grained Autogenerate Generation with Rewriters[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#fine-grained-autogenerate-generation-with-rewriters "Link to this heading")

The preceding example illustrated how we can make a simple change to the structure of the operation directives to produce new autogenerate output. For the case where we want to affect very specific parts of the autogenerate stream, we can make a function for [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure") which traverses through the whole [`MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") structure, locates the elements we care about and modifies them in-place as needed. However, to reduce the boilerplate associated with this task, we can use the [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") object to make this easier. [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") gives us an object that we can pass directly to [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure") which we can also attach handler functions onto, keyed to specific types of constructs.

Below is an example where we rewrite [`ops.AddColumnOp`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AddColumnOp "alembic.operations.ops.AddColumnOp") directives; based on whether or not the new column is “nullable”, we either return the existing directive, or we return the existing directive with the nullable flag changed, inside of a list with a second directive to alter the nullable flag in a second step:

# ... fragmented env.py script ....

from alembic.autogenerate import rewriter
from alembic.operations import ops

writer = rewriter.Rewriter()

@writer.rewrites(ops.AddColumnOp)
def add_column(context, revision, op):
    if op.column.nullable:
        return op
    else:
        op.column.nullable = True
        return [
            op,
            ops.AlterColumnOp(
                op.table_name,
                op.column.name,
                modify_nullable=False,
                existing_type=op.column.type,
            )
        ]

# ... later ...

def run_migrations_online():
    # ...

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=writer
        )

        with context.begin_transaction():
            context.run_migrations()

Above, in a full [`ops.MigrationScript`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript "alembic.operations.ops.MigrationScript") structure, the [`AddColumn`](https://alembic.sqlalchemy.org/en/latest/api/ddl.html#alembic.ddl.base.AddColumn "alembic.ddl.base.AddColumn") directives would be present within the paths `MigrationScript->UpgradeOps->ModifyTableOps` and `MigrationScript->DowngradeOps->ModifyTableOps`. The [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") handles traversing into these structures as well as rewriting them as needed so that we only need to code for the specific object we care about.

class alembic.autogenerate.rewriter.Rewriter[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "Link to this definition")
A helper object that allows easy ‘rewriting’ of ops streams.

The [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") object is intended to be passed along to the [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure") parameter in an `env.py` script. Once constructed, any number of “rewrites” functions can be associated with it, which will be given the opportunity to modify the structure without having to have explicit knowledge of the overall structure.

The function is passed the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") object and `revision` tuple that are passed to the 
```
Environment
Context.configure.process_revision_directives
```
 function normally, and the third argument is an individual directive of the type noted in the decorator. The function has the choice of returning a single op directive, which normally can be the directive that was actually passed, or a new directive to replace it, or a list of zero or more directives to replace it.

chain(_other:ProcessRevisionDirectiveFn|[Rewriter](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter")_)→[Rewriter](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter.chain "Link to this definition")
Produce a “chain” of this [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") to another.

This allows two or more rewriters to operate serially on a stream, e.g.:

writer1 = autogenerate.Rewriter()
writer2 = autogenerate.Rewriter()

@writer1.rewrites(ops.AddColumnOp)
def add_column_nullable(context, revision, op):
    op.column.nullable = True
    return op

@writer2.rewrites(ops.AddColumnOp)
def add_column_idx(context, revision, op):
    idx_op = ops.CreateIndexOp(
        "ixc", op.table_name, [op.column.name]
    )
    return [op, idx_op]

writer = writer1.chain(writer2)

Parameters:
**other**[¶](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter.chain.params.other) – a [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") instance

Returns:
a new [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") that will run the operations of this writer, then the “other” writer, in succession.

rewrites(_operator:Type[[AddColumnOp](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AddColumnOp "alembic.operations.ops.AddColumnOp")]|Type[[MigrateOperation](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation")]|Type[[AlterColumnOp](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.AlterColumnOp "alembic.operations.ops.AlterColumnOp")]|Type[[CreateTableOp](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.CreateTableOp "alembic.operations.ops.CreateTableOp")]|Type[[ModifyTableOps](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.ModifyTableOps "alembic.operations.ops.ModifyTableOps")]_)→Callable[...,Any][#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter.rewrites "Link to this definition")
Register a function as rewriter for a given type.

The function should receive three arguments, which are the [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext"), a `revision` tuple, and an op directive of the type indicated. E.g.:

@writer1.rewrites(ops.AddColumnOp)
def add_column_nullable(context, revision, op):
    op.column.nullable = True
    return op

### Revision Generation with Multiple Engines / `run_migrations()` calls[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#revision-generation-with-multiple-engines-run-migrations-calls "Link to this heading")

A lesser-used technique which allows autogenerated migrations to run against multiple database backends at once, generating changes into a single migration script, is illustrated in the provided `multidb` template. This template features a special `env.py` which iterates through multiple [`Engine`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Engine "(in SQLAlchemy v2.1)") instances and calls upon [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations") for each:

for name, rec in engines.items():
    logger.info("Migrating database %s" % name)
    context.configure(
        connection=rec['connection'],
        upgrade_token="%s_upgrades" % name,
        downgrade_token="%s_downgrades" % name,
        target_metadata=target_metadata.get(name)
    )
    context.run_migrations(engine_name=name)

Above, [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations") is run multiple times, once for each engine. Within the context of autogeneration, each time the method is called the [`upgrade_token`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.upgrade_token "alembic.runtime.environment.EnvironmentContext.configure") and [`downgrade_token`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.downgrade_token "alembic.runtime.environment.EnvironmentContext.configure") parameters are changed, so that the collection of template variables gains distinct entries for each engine, which are then referred to explicitly within `script.py.mako`.

In terms of the [`EnvironmentContext.configure.process_revision_directives`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.process_revision_directives "alembic.runtime.environment.EnvironmentContext.configure") hook, the behavior here is that the `process_revision_directives` hook is invoked **multiple times, once for each call to context.run_migrations()**. This means that if a multi-`run_migrations()` approach is to be combined with the `process_revision_directives` hook, care must be taken to use the hook appropriately.

The first point to note is that when a **second** call to `run_migrations()` occurs, the `.upgrade_ops` and `.downgrade_ops` attributes are **converted into Python lists**, and new [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") and [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") objects are appended to these lists. Each [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") and [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") object maintains an `.upgrade_token` and a `.downgrade_token` attribute respectively, which serves to render their contents into the appropriate template token.

For example, a multi-engine run that has the engine names `engine1` and `engine2` will generate tokens of `engine1_upgrades`, `engine1_downgrades`, `engine2_upgrades` and `engine2_downgrades` as it runs. The resulting migration structure would look like this:

from alembic.operations import ops
import sqlalchemy as sa

migration_script = ops.MigrationScript(
    'eced083f5df',
    [
        ops.UpgradeOps(
            ops=[
                # upgrade operations for "engine1"
            ],
            upgrade_token="engine1_upgrades"
        ),
        ops.UpgradeOps(
            ops=[
                # upgrade operations for "engine2"
            ],
            upgrade_token="engine2_upgrades"
        ),
    ],
    [
        ops.DowngradeOps(
            ops=[
                # downgrade operations for "engine1"
            ],
            downgrade_token="engine1_downgrades"
        ),
        ops.DowngradeOps(
            ops=[
                # downgrade operations for "engine2"
            ],
            downgrade_token="engine2_downgrades"
        )
    ],
    message='migration message'
)

Given the above, the following guidelines should be considered when the `env.py` script calls upon [`MigrationContext.run_migrations()`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.run_migrations "alembic.runtime.migration.MigrationContext.run_migrations") multiple times when running autogenerate:

*   If the `process_revision_directives` hook aims to **add elements based on inspection of the current database / connection**, it should do its operation **on each iteration**. This is so that each time the hook runs, the database is available.

*   Alternatively, if the `process_revision_directives` hook aims to **modify the list of migration directives in place**, this should be called **only on the last iteration**. This is so that the hook isn’t being given an ever-growing structure each time which it has already modified previously.

*   The [`Rewriter`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.rewriter.Rewriter "alembic.autogenerate.rewriter.Rewriter") object, if used, should be called **only on the last iteration**, because it will always deliver all directives every time, so again to avoid double/triple/etc. processing of directives it should be called only when the structure is complete.

*   The [`MigrationScript.upgrade_ops_list`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript.upgrade_ops_list "alembic.operations.ops.MigrationScript.upgrade_ops_list") and [`MigrationScript.downgrade_ops_list`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrationScript.downgrade_ops_list "alembic.operations.ops.MigrationScript.downgrade_ops_list") attributes should be consulted when referring to the collection of [`UpgradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.UpgradeOps "alembic.operations.ops.UpgradeOps") and [`DowngradeOps`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.DowngradeOps "alembic.operations.ops.DowngradeOps") objects.

Autogenerating Custom Operation Directives[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#autogenerating-custom-operation-directives "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the section [Operation Plugins](https://alembic.sqlalchemy.org/en/latest/api/operations.html#operation-plugins), we talked about adding new subclasses of [`MigrateOperation`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation") in order to add new `op.` directives. In the preceding section [Customizing Revision Generation](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#customizing-revision), we also learned that these same [`MigrateOperation`](https://alembic.sqlalchemy.org/en/latest/api/operations.html#alembic.operations.ops.MigrateOperation "alembic.operations.ops.MigrateOperation") structures are at the base of how the autogenerate system knows what Python code to render. Using this knowledge, we can create additional functions that plug into the autogenerate system so that our new operations can be generated into migration scripts when `alembic revision --autogenerate` is run.

The following sections will detail an example of this using the the `CreateSequenceOp` and `DropSequenceOp` directives we created in [Operation Plugins](https://alembic.sqlalchemy.org/en/latest/api/operations.html#operation-plugins), which correspond to the SQLAlchemy [`Sequence`](https://docs.sqlalchemy.org/en/21/core/defaults.html#sqlalchemy.schema.Sequence "(in SQLAlchemy v2.1)") construct.

### Tracking our Object with the Model[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#tracking-our-object-with-the-model "Link to this heading")

The basic job of an autogenerate comparison function is to inspect a series of objects in the database and compare them against a series of objects defined in our model. By “in our model”, we mean anything defined in Python code that we want to track, however most commonly we’re talking about a series of [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") objects present in a [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") collection.

Let’s propose a simple way of seeing what [`Sequence`](https://docs.sqlalchemy.org/en/21/core/defaults.html#sqlalchemy.schema.Sequence "(in SQLAlchemy v2.1)") objects we want to ensure exist in the database when autogenerate runs. While these objects do have some integrations with [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") and [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") already, let’s assume they don’t, as the example here intends to illustrate how we would do this for most any kind of custom construct. We associate the object with the `info` collection of [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)"), which is a dictionary we can use for anything, which we also know will be passed to the autogenerate process:

from sqlalchemy.schema import Sequence

def add_sequence_to_model(sequence, metadata):
    metadata.info.setdefault("sequences", set()).add(
        (sequence.schema, sequence.name)
    )

my_seq = Sequence("my_sequence")
add_sequence_to_model(my_seq, model_metadata)

The `info` dictionary is a good place to put things that we want our autogeneration routines to be able to locate, which can include any object such as custom DDL objects representing views, triggers, special constraints, or anything else we want to support.

### Registering a Comparison Function Globally[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#registering-a-comparison-function-globally "Link to this heading")

We now need to register a comparison hook, which will be used to compare the database to our model and produce `CreateSequenceOp` and `DropSequenceOp` directives to be included in our migration script. The example below illustrates registering a comparison function using the **global** dispatch:

from alembic.autogenerate import comparators
from alembic.autogenerate.api import AutogenContext
from alembic.operations.ops import UpgradeOps

# new in Alembic 1.18.0 - for older versions, no return value is needed
from alembic.util import PriorityDispatchResult

# the global dispatch includes a decorator function.
# for plugin level dispatch, use Plugin.add_autogenerate_comparator()
# instead.
@comparators.dispatch_for("schema")
def compare_sequences(
        autogen_context: AutogenContext,
        upgrade_ops: UpgradeOps,
        schemas: set[str | None]
) -> PriorityDispatchResult:
    all_conn_sequences = set()

    for sch in schemas:

        all_conn_sequences.update([
            (sch, row[0]) for row in
            autogen_context.connection.execute(
                "SELECT relname FROM pg_class c join "
                "pg_namespace n on n.oid=c.relnamespace where "
                "relkind='S' and n.nspname=%(nspname)s",

                # note that we consider a schema of 'None' in our
                # model to be the "default" name in the PG database;
                # this usually is the name 'public'
                nspname=autogen_context.dialect.default_schema_name
                if sch is None else sch
            )
        ])

    # get the collection of Sequence objects we're storing with
    # our MetaData
    metadata_sequences = autogen_context.metadata.info.setdefault(
        "sequences", set())

    # for new names, produce CreateSequenceOp directives
    for sch, name in metadata_sequences.difference(all_conn_sequences):
        upgrade_ops.ops.append(
            CreateSequenceOp(name, schema=sch)
        )

    # for names that are going away, produce DropSequenceOp
    # directives
    for sch, name in all_conn_sequences.difference(metadata_sequences):
        upgrade_ops.ops.append(
            DropSequenceOp(name, schema=sch)
        )

    return PriorityDispatchResult.CONTINUE

Above, we’ve built a new function `compare_sequences()` and registered it as a “schema” level comparison function with autogenerate. The job that it performs is that it compares the list of sequence names present in each database schema with that of a list of sequence names that we are maintaining in our [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object.

The registration of our function at the scope of “schema” means our autogenerate comparison function is called outside of the context of any specific table or column. The four available scopes are “autogenerate” (new in 1.18.0), “schema”, “table”, and “column”; these scopes are described fully in the section [Registering Autogenerate Comparators at the Plugin Level](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#plugins-registering-autogenerate), which details their use in terms of a custom plugin, however the interfaces are the same.

When autogenerate completes, it will have a series of `CreateSequenceOp` and `DropSequenceOp` directives in the list of “upgrade” operations; the list of “downgrade” operations is generated directly from these using the `CreateSequenceOp.reverse()` and `DropSequenceOp.reverse()` methods that we’ve implemented on these objects.

The example above illustrates registration with the so-called **global** autogenerate dispatch, at `alembic.autogenerate.comparators`. Alembic as of version 1.18 also includes a **plugin level** dispatch, where comparison functions are instead registered using [`Plugin.add_autogenerate_comparator()`](https://alembic.sqlalchemy.org/en/latest/api/plugins.html#alembic.runtime.plugins.Plugin.add_autogenerate_comparator "alembic.runtime.plugins.Plugin.add_autogenerate_comparator"). Comparison functions registered at the plugin level operate in the same way as those registered globally, with the exception that custom autogenerate compare functions must also be enabled at the environment level within the `EnvironmentContext.configure.autogenerate_plugins` parameter, and also have the ability to be omitted from an autogenerate run.

The [`AutogenContext`](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "alembic.autogenerate.api.AutogenContext") passed to these hooks is documented below.

class alembic.autogenerate.api.AutogenContext(_migration\_context:[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")_, _metadata:MetaData|Sequence[MetaData]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _opts:Dict[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"),Any]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None_, _autogenerate:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")=True_)[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext "Link to this definition")
Maintains configuration and state that’s specific to an autogenerate operation.

connection:Connection|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.connection "Link to this definition")
The [`Connection`](https://docs.sqlalchemy.org/en/21/core/connections.html#sqlalchemy.engine.Connection "(in SQLAlchemy v2.1)") object currently connected to the database backend being compared.

This is obtained from the [`MigrationContext.bind`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext.bind "alembic.runtime.migration.MigrationContext.bind") and is ultimately set up in the `env.py` script.

dialect:Dialect[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.dialect "Link to this definition")
The [`Dialect`](https://docs.sqlalchemy.org/en/21/core/internals.html#sqlalchemy.engine.Dialect "(in SQLAlchemy v2.1)") object currently in use.

This is normally obtained from the `dialect` attribute.

imports:Set[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]=None[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.imports "Link to this definition")
A `set()` which contains string Python import directives.

The directives are to be rendered into the `${imports}` section of a script template. The set is normally empty and can be modified within hooks such as the [`EnvironmentContext.configure.render_item`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.render_item "alembic.runtime.environment.EnvironmentContext.configure") hook.

metadata:MetaData|Sequence[MetaData]|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")=None[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.metadata "Link to this definition")
The [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object representing the destination.

This object is the one that is passed within `env.py` to the [`EnvironmentContext.configure.target_metadata`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.target_metadata "alembic.runtime.environment.EnvironmentContext.configure") parameter. It represents the structure of `Table` and other objects as stated in the current database model, and represents the destination structure for the database being examined.

While the [`MetaData`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.MetaData "(in SQLAlchemy v2.1)") object is primarily known as a collection of [`Table`](https://docs.sqlalchemy.org/en/21/core/metadata.html#sqlalchemy.schema.Table "(in SQLAlchemy v2.1)") objects, it also has an `info` dictionary that may be used by end-user schemes to store additional schema-level objects that are to be compared in custom autogeneration schemes.

migration_context:[MigrationContext](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.migration_context "Link to this definition")
The [`MigrationContext`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.migration.MigrationContext "alembic.runtime.migration.MigrationContext") established by the `env.py` script.

run_filters(_object\_:SchemaItem_, _name:sqla\_compat.\_ConstraintName_, _type\_:NameFilterType_, _reflected:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_, _compare\_to:SchemaItem|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.run_filters "Link to this definition")
Run the context’s object filters and return True if the targets should be part of the autogenerate operation.

This method should be run for every kind of object encountered within an autogenerate operation, giving the environment the chance to filter what objects should be included in the comparison. The filters here are produced directly via the [`EnvironmentContext.configure.include_object`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_object "alembic.runtime.environment.EnvironmentContext.configure") parameter.

run_name_filters(_name:[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_, _type\_:NameFilterType_, _parent\_names:NameFilterParentNames_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.run_name_filters "Link to this definition")
Run the context’s name filters and return True if the targets should be part of the autogenerate operation.

This method should be run for every kind of name encountered within the reflection side of an autogenerate operation, giving the environment the chance to filter what names should be reflected as database objects. The filters here are produced directly via the [`EnvironmentContext.configure.include_name`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_name "alembic.runtime.environment.EnvironmentContext.configure") parameter.

run_object_filters(_object\_:SchemaItem_, _name:sqla\_compat.\_ConstraintName_, _type\_:NameFilterType_, _reflected:[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")_, _compare\_to:SchemaItem|[None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")_)→[bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.run_object_filters "Link to this definition")
Run the context’s object filters and return True if the targets should be part of the autogenerate operation.

This method should be run for every kind of object encountered within an autogenerate operation, giving the environment the chance to filter what objects should be included in the comparison. The filters here are produced directly via the [`EnvironmentContext.configure.include_object`](https://alembic.sqlalchemy.org/en/latest/api/runtime.html#alembic.runtime.environment.EnvironmentContext.configure.params.include_object "alembic.runtime.environment.EnvironmentContext.configure") parameter.

sorted_tables[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.sorted_tables "Link to this definition")
Return an aggregate of the `MetaData.sorted_tables` collection(s).

For a sequence of `MetaData` objects, this concatenates the `MetaData.sorted_tables` collection for each individual `MetaData` in the order of the sequence. It does **not** collate the sorted tables collections.

table_key_to_table[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#alembic.autogenerate.api.AutogenContext.table_key_to_table "Link to this definition")
Return an aggregate of the `MetaData.tables` dictionaries.

The `MetaData.tables` collection is a dictionary of table key to `Table`; this method aggregates the dictionary across multiple `MetaData` objects into one dictionary.

Duplicate table keys are **not** supported; if two `MetaData` objects contain the same table key, an exception is raised.

### Creating a Render Function[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#creating-a-render-function "Link to this heading")

The second autogenerate integration hook is to provide a “render” function; since the autogenerate system renders Python code, we need to build a function that renders the correct “op” instructions for our directive:

from alembic.autogenerate import renderers

@renderers.dispatch_for(CreateSequenceOp)
def render_create_sequence(autogen_context, op):
    return "op.create_sequence(%r, **%r)" % (
        op.sequence_name,
        {"schema": op.schema}
    )

@renderers.dispatch_for(DropSequenceOp)
def render_drop_sequence(autogen_context, op):
    return "op.drop_sequence(%r, **%r)" % (
        op.sequence_name,
        {"schema": op.schema}
    )

The above functions will render Python code corresponding to the presence of `CreateSequenceOp` and `DropSequenceOp` instructions in the list that our comparison function generates.

### Running It[#](https://alembic.sqlalchemy.org/en/latest/api/autogenerate.html#running-it "Link to this heading")

All the above code can be organized however the developer sees fit; the only thing that needs to make it work is that when the Alembic environment `env.py` is invoked, it either imports modules which contain all the above routines, or they are locally present, or some combination thereof.

If we then have code in our model (which of course also needs to be invoked when `env.py` runs!) like this:

from sqlalchemy.schema import Sequence

my_seq_1 = Sequence("my_sequence_1")
add_sequence_to_model(my_seq_1, target_metadata)

When we first run `alembic revision --autogenerate`, we’ll see this in our migration file:

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_sequence('my_sequence_1', **{'schema': None})
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_sequence('my_sequence_1', **{'schema': None})
    ### end Alembic commands ###

These are our custom directives that will invoke when `alembic upgrade` or `alembic downgrade` is run.
