# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-iceberg-table-alter-column-set-data-type.md

# ALTER ICEBERG TABLE … ALTER COLUMN … SET DATA TYPE (structured types)

> **Note:**
>
> This variant of the syntax is not supported for Iceberg tables that use an external catalog.

Modifies (evolves) a [structured type](../data-types-structured.md)
column in a Snowflake-managed [Apache Iceberg™ table](../../user-guide/tables-iceberg.md).

With this command, you can modify structured types in an Iceberg table column. You can
either rename a key in a structured OBJECT or perform a combination of the following changes:

* Evolving the type of a field within a structured type.
* Reordering keys in a structured OBJECT.
* Adding keys to a structured OBJECT.
* Dropping keys from a structured OBJECT.

You can’t combine renaming a key with any other modifications.

For brevity, this topic refers to Iceberg tables as just “tables” except when making a distinction between
Iceberg tables and regular Snowflake tables.

See also:
:   [CREATE ICEBERG TABLE](create-iceberg-table.md) , [DROP ICEBERG TABLE](drop-iceberg-table.md) , [SHOW ICEBERG TABLES](show-iceberg-tables.md) , [DESCRIBE ICEBERG TABLE](desc-iceberg-table.md)

## Syntax

**Modify a structured type column**

```sqlsyntax
ALTER ICEBERG TABLE [ IF EXISTS ] <table_name> ALTER COLUMN <structured_column>
  SET DATA TYPE <new_structured_type>
```

**Rename keys in a structured OBJECT**

```sqlsyntax
ALTER ICEBERG TABLE [ IF EXISTS ] <table_name> ALTER COLUMN <structured_column>
  SET DATA TYPE <new_structured_type>
  RENAME FIELDS
```

## Parameters

`table_name`
:   Identifier for the table to modify.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`ALTER COLUMN structured_column`
:   Specifies the structured type column to modify.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET DATA TYPE new_structured_type`
:   A full specification for the new structured type to use for the column. For example, to specify a structured ARRAY of NUMBER elements,
    use ARRAY(NUMBER).

    For more information, see [Specifying a structured type](../data-types-structured.md) and the examples on this page.

`RENAME FIELDS`
:   Specifies that the command should rename one or more keys in a structured OBJECT.
    The old and new keys must differ only in name, and must have exactly the same hierarchy and data types. Renaming keys doesn’t change
    the field IDs.

    Renaming keys can’t be combined with any other modifications to structured types in an Iceberg table.

    See the RENAME FIELDS example.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Iceberg table | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| USAGE | External volume |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* This command doesn’t support the following actions:

  * Evolving a structured type into a non-structured type (or the other way around).
  * Setting a null constraint on a structured ARRAY element or on the key-value pairs of a structured MAP.
  * Using RENAME FIELDS to rename a key that is part of the clustering key for the table.
  * Altering the NULL constraint for a structured OBJECT.
  * Altering a table in a catalog-linked database.
* For tables that use data access policies,
  make sure the new data type for a column is compatible with the argument type of your data access policy. Otherwise, querying the table
  might fail. For example, if you add a key to a structured OBJECT column, you must alter your policy or
  create a new policy and apply it to your table.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

### Evolving types

You can evolve the type for a field in a structured type.
Evolving the type means widening it into a larger, related Iceberg data type.

Snowflake supports the following type evolutions, in accordance with the
[Apache Iceberg spec](https://iceberg.apache.org/spec/#schema-evolution):

* Changing a field of type `int` into type `long`.
* Changing a field of type `float` into type `double`.
* Changing a field of type `decimal(p,s)` into type `decimal(p',s)` where `p` is smaller than `p'`.

To evolve a field type, use the [Snowflake syntax for specifying a structured type](../data-types-structured.md).
You can use the Iceberg data type in your specification.
For example, the following statement changes the element type in a structured ARRAY column to (Iceberg) type `long`.

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table ALTER COLUMN col1
  SET DATA TYPE ARRAY(long);
```

For information about how Iceberg data types map to Snowflake data types, see [Data types for Apache Iceberg™ tables](../../user-guide/tables-iceberg-data-types.md).

### Reordering keys

To rearrange the order of keys in a structured OBJECT, specify a new order in your
ALTER ICEBERG TABLE statement. Rearranging the key order does not affect the data in the OBJECT.

For example, consider the following CREATE ICEBERG TABLE statement.
The table has one column (`column_1`) of type OBJECT with two keys in a specified order:

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (
  column_1 OBJECT(
      key_a int,
      key_b int
    )
  )
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = '';
```

The following command changes the order of the keys so that `key_b` comes before `key_a`:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table ALTER COLUMN column_1
  SET DATA TYPE OBJECT(
    key_b int,
    key_a int
  );
```

### Adding keys

You can add keys to a structured OBJECT.
A new key can use any of the [data types supported for Iceberg tables](../../user-guide/tables-iceberg-data-types.md) for its value.

> **Note:**
>
> You can’t set a null constraint when you add a key, because Snowflake sets the value of the key to NULL for
> all existing rows in the table.

For example, consider the following CREATE ICEBERG TABLE statement.
The table has one column (`column_1`) of type OBJECT with one key (`key_1`):

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (
  column_1 OBJECT(
      key_1 int
    )
  )
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = '';
```

The following command adds a key named `key_2` to `column_1`:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table ALTER COLUMN column_1
  SET DATA TYPE OBJECT(
    key_1 int,
    key_2 int
  );
```

### Dropping keys

> **Note:**
>
> Dropping a key whose value is a structured data type that belongs to a clustering key isn’t supported.

To drop a key from a structured OBJECT, use the ALTER ICEBERG TABLE … ALTER COLUMN command
to redefine the OBJECT.

Dropping the key removes the key and its value from all rows in the table.

For example, consider the following CREATE ICEBERG TABLE statement.
The table has one column (`column_1`) of type OBJECT with two keys:

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (
  column_1 OBJECT(
      key_1 int,
      key_2 ARRAY(string)
    )
  )
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = '';
```

The following command drops the key named `key_2` by omitting it from the OBJECT specification:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table ALTER COLUMN column_1
  SET DATA TYPE OBJECT(
    key_1 int
  );
```

### Renaming keys

To change the key names in a structured OBJECT, use the RENAME FIELDS keywords.

For example, consider the following CREATE ICEBERG TABLE statement:

```sqlexample
CREATE ICEBERG TABLE my_iceberg_table (
  column_1 OBJECT(
      key_1 int,
      key_2 int
    )
  )
  CATALOG = 'SNOWFLAKE'
  EXTERNAL_VOLUME = 'my_external_volume'
  BASE_LOCATION = '';
```

The following command uses RENAME FIELDS to rename the keys in `column_1`:

```sqlexample
ALTER ICEBERG TABLE my_iceberg_table ALTER COLUMN column_1
  SET DATA TYPE OBJECT(
    k_1 int,
    k_2 int
  )
  RENAME FIELDS;
```
