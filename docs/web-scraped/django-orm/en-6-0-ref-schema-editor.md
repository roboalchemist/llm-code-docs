# Source: https://docs.djangoproject.com/en/6.0/ref/schema-editor/

Title: SchemaEditor | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/schema-editor/

Markdown Content:
_class_ BaseDatabaseSchemaEditor[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L78)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor "Link to this definition")
Django’s migration system is split into two parts; the logic for calculating and storing what operations should be run (`django.db.migrations`), and the database abstraction layer that turns things like “create a model” or “delete a field” into SQL - which is the job of the `SchemaEditor`.

It’s unlikely that you will want to interact directly with `SchemaEditor` as a normal developer using Django, but if you want to write your own migration system, or have more advanced needs, it’s a lot nicer than writing SQL.

Each database backend in Django supplies its own version of `SchemaEditor`, and it’s always accessible via the `connection.schema_editor()` context manager:

with connection.schema_editor() as schema_editor:
    schema_editor.delete_model(MyModel)

It must be used via the context manager as this allows it to manage things like transactions and deferred SQL (like creating `ForeignKey` constraints).

It exposes all possible operations as methods, that should be called in the order you wish changes to be applied. Some possible operations or types of change are not possible on all databases - for example, MyISAM does not support foreign key constraints.

If you are writing or maintaining a third-party database backend for Django, you will need to provide a `SchemaEditor` implementation in order to work with Django’s migration functionality - however, as long as your database is relatively standard in its use of SQL and relational design, you should be able to subclass one of the built-in Django `SchemaEditor` classes and tweak the syntax a little.

Methods[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#methods "Link to this heading")
---------------------------------------------------------------------------------------------------

### `execute()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#execute "Link to this heading")

BaseDatabaseSchemaEditor.execute(_sql_, _params=()_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L176)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.execute "Link to this definition")
Executes the SQL statement passed in, with parameters if supplied. This is a wrapper around the normal database cursors that allows capture of the SQL to a `.sql` file if the user wishes.

### `create_model()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#create-model "Link to this heading")

BaseDatabaseSchemaEditor.create_model(_model_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L505)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.create_model "Link to this definition")
Creates a new table in the database for the provided model, along with any unique constraints or indexes it requires.

### `delete_model()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#delete-model "Link to this heading")

BaseDatabaseSchemaEditor.delete_model(_model_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L540)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.delete_model "Link to this definition")
Drops the model’s table in the database along with any unique constraints or indexes it has.

### `add_index()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#add-index "Link to this heading")

BaseDatabaseSchemaEditor.add_index(_model_, _index_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L561)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_index "Link to this definition")
Adds `index` to `model`’s table.

### `remove_index()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#remove-index "Link to this heading")

BaseDatabaseSchemaEditor.remove_index(_model_, _index_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L572)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_index "Link to this definition")
Removes `index` from `model`’s table.

### `rename_index()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#rename-index "Link to this heading")

BaseDatabaseSchemaEditor.rename_index(_model_, _old\_index_, _new\_index_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L581)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.rename_index "Link to this definition")
Renames `old_index` from `model`’s table to `new_index`.

### `add_constraint()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#add-constraint "Link to this heading")

BaseDatabaseSchemaEditor.add_constraint(_model_, _constraint_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L591)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_constraint "Link to this definition")
Adds `constraint` to `model`’s table.

### `remove_constraint()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#remove-constraint "Link to this heading")

BaseDatabaseSchemaEditor.remove_constraint(_model_, _constraint_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L599)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_constraint "Link to this definition")
Removes `constraint` from `model`’s table.

### `alter_unique_together()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-unique-together "Link to this heading")

BaseDatabaseSchemaEditor.alter_unique_together(_model_, _old\_unique\_together_, _new\_unique\_together_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L605)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_unique_together "Link to this definition")
Changes a model’s [`unique_together`](https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.unique_together "django.db.models.Options.unique_together") value; this will add or remove unique constraints from the model’s table until they match the new value.

### `alter_index_together()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-index-together "Link to this heading")

BaseDatabaseSchemaEditor.alter_index_together(_model_, _old\_index\_together_, _new\_index\_together_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L626)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_index_together "Link to this definition")
Changes a model’s `index_together` value; this will add or remove indexes from the model’s table until they match the new value.

### `alter_db_table()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-db-table "Link to this heading")

BaseDatabaseSchemaEditor.alter_db_table(_model_, _old\_db\_table_, _new\_db\_table_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L681)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_table "Link to this definition")
Renames the model’s table from `old_db_table` to `new_db_table`.

### `alter_db_table_comment()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-db-table-comment "Link to this heading")

BaseDatabaseSchemaEditor.alter_db_table_comment(_model_, _old\_db\_table\_comment_, _new\_db\_table\_comment_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L700)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_table_comment "Link to this definition")
Change the `model`’s table comment to `new_db_table_comment`.

### `alter_db_tablespace()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-db-tablespace "Link to this heading")

BaseDatabaseSchemaEditor.alter_db_tablespace(_model_, _old\_db\_tablespace_, _new\_db\_tablespace_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L710)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_db_tablespace "Link to this definition")
Moves the model’s table from one tablespace to another.

### `add_field()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#add-field "Link to this heading")

BaseDatabaseSchemaEditor.add_field(_model_, _field_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L721)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field "Link to this definition")
Adds a column (or sometimes multiple) to the model’s table to represent the field. This will also add indexes or a unique constraint if the field has `db_index=True` or `unique=True`.

If the field is a `ManyToManyField` without a value for `through`, instead of creating a column, it will make a table to represent the relationship. If `through` is provided, it is a no-op.

If the field is a `ForeignKey`, this will also add the foreign key constraint to the column.

### `remove_field()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#remove-field "Link to this heading")

BaseDatabaseSchemaEditor.remove_field(_model_, _field_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L809)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field "Link to this definition")
Removes the column(s) representing the field from the model’s table, along with any unique constraints, foreign key constraints, or indexes caused by that field.

If the field is a ManyToManyField without a value for `through`, it will remove the table created to track the relationship. If `through` is provided, it is a no-op.

### `alter_field()`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#alter-field "Link to this heading")

BaseDatabaseSchemaEditor.alter_field(_model_, _old\_field_, _new\_field_, _strict=False_)[[source]](https://github.com/django/django/blob/stable/6.0.x/django/db/backends/base/schema.py#L841)[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.alter_field "Link to this definition")
This transforms the field on the model from the old field to the new one. This includes changing the name of the column (the [`db_column`](https://docs.djangoproject.com/en/6.0/ref/models/fields/#django.db.models.Field.db_column "django.db.models.Field.db_column") attribute), changing the type of the field (if the field class changes), changing the `NULL` status of the field, adding or removing field-only unique constraints and indexes, changing primary key, and changing the destination of `ForeignKey` constraints.

The most common transformation this cannot do is transforming a `ManyToManyField` into a normal Field or vice-versa; Django cannot do this without losing data, and so it will refuse to do it. Instead, [`remove_field()`](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field "django.db.backends.base.schema.BaseDatabaseSchemaEditor.remove_field") and [`add_field()`](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field "django.db.backends.base.schema.BaseDatabaseSchemaEditor.add_field") should be called separately.

If the database has the `supports_combined_alters`, Django will try and do as many of these in a single database call as possible; otherwise, it will issue a separate ALTER statement for each change, but will not issue ALTERs where no change is required.

Attributes[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#attributes "Link to this heading")
---------------------------------------------------------------------------------------------------------

All attributes should be considered read-only unless stated otherwise.

### `connection`[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#connection "Link to this heading")

SchemaEditor.connection[¶](https://docs.djangoproject.com/en/6.0/ref/schema-editor/#django.db.backends.base.schema.SchemaEditor.connection "Link to this definition")
A connection object to the database. A useful attribute of the connection is `alias` which can be used to determine the name of the database being accessed.

This is useful when doing data migrations for [migrations with multiple databases](https://docs.djangoproject.com/en/6.0/howto/writing-migrations/#data-migrations-and-multiple-databases).
