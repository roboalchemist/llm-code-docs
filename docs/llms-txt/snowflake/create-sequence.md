# Source: https://docs.snowflake.com/en/sql-reference/sql/create-sequence.md

# CREATE SEQUENCE

Creates a new sequence, which can be used for generating sequential, unique numbers.

> **Important:**
>
> Snowflake does not guarantee generating sequence numbers without gaps. The generated numbers are not necessarily contiguous.

For more details, see [Using Sequences](../../user-guide/querying-sequences.md).

See also:
:   [DROP SEQUENCE](drop-sequence.md) , [ALTER SEQUENCE](alter-sequence.md) , [SHOW SEQUENCES](show-sequences.md) , [DESCRIBE SEQUENCE](desc-sequence.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SEQUENCE [ IF NOT EXISTS ] <name>
  [ WITH ]
  [ START [ WITH ] [ = ] <initial_value> ]
  [ INCREMENT [ BY ] [ = ] <sequence_interval> ]
  [ { ORDER | NOORDER } ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Specifies the identifier for the sequence; must be unique for the schema in which the sequence is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more details about identifiers, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`START [ WITH ] [ = ] initial_value`
:   Specifies the first value returned by the sequence. Supported values are any value that can be represented by a 64-bit two’s
    complement integer (from `-2^63` to `2^63 - 1`).

    Default: `1`

`INCREMENT [ BY ] [ = ] sequence_interval`
:   Specifies the step interval of the sequence:

    > * For positive sequence interval `n`, the next `n-1` values are reserved by each sequence call.
    > * For negative sequence interval `-n`, the next `n-1` lower values are reserved by each sequence call.

    Supported values are any non-zero value that can be represented by a 64-bit two’s complement integer.

    Default: `1`

`{ ORDER | NOORDER }`
:   Specifies whether or not the values are generated for the sequence in
    [increasing or decreasing order](../../user-guide/querying-sequences.md).

    * ORDER specifies that the values generated for a sequence or auto-incremented column are in increasing order (or, if the interval
      is a negative value, in decreasing order).

      For example, if a sequence or auto-incremented column has `START 1 INCREMENT 2`, the generated values might be
      `1`, `3`, `5`, `7`, `9`, etc.
    * NOORDER specifies that the values are not guaranteed to be in increasing order.

      For example, if a sequence has `START 1 INCREMENT 2`, the generated values might be `1`, `3`, `101`, `5`, `103`, etc.

      NOORDER can improve performance when multiple INSERT operations are performed concurrently (for example, when multiple
      clients are executing multiple INSERT statements).

    Default: The [NOORDER_SEQUENCE_AS_DEFAULT](../parameters.md) parameter determines which property is set by default.

`COMMENT = 'string_literal'`
:   Specifies a comment for the sequence.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SEQUENCE | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The first/initial value for a sequence cannot be changed after the sequence is created.
* A sequence does not necessarily produce a gap-free sequence. Values increase (until the limit is reached) and are unique,
  but are not necessarily contiguous. For more information, including the upper and lower limits, see [Sequence Semantics](../../user-guide/querying-sequences.md).
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Here is a simple example of using sequences:

> > ```sqlexample
> > CREATE OR REPLACE SEQUENCE seq_01 START = 1 INCREMENT = 1;
> > CREATE OR REPLACE TABLE sequence_test_table (i INTEGER);
> > ```
> >
> > ```sqlexample
> > SELECT seq_01.nextval;
> > +---------+
> > | NEXTVAL |
> > |---------|
> > |       1 |
> > +---------+
> > ```
>
> Run the same query again; note how the sequence numbers change:
>
> > ```sqlexample
> > SELECT seq_01.nextval;
> > +---------+
> > | NEXTVAL |
> > |---------|
> > |       2 |
> > +---------+
> > ```
>
> Now use the sequence while inserting into a table:
>
> > ```sqlexample
> > INSERT INTO sequence_test_table (i) VALUES (seq_01.nextval);
> > ```
> >
> > ```sqlexample
> > SELECT i FROM sequence_test_table;
> > +---+
> > | I |
> > |---|
> > | 3 |
> > +---+
> > ```

Create a sequence that increments by 5 rather than by 1:

> > ```sqlexample
> > CREATE OR REPLACE SEQUENCE seq_5 START = 1 INCREMENT = 5;
> > ```
> >
> > ```sqlexample
> > SELECT seq_5.nextval a, seq_5.nextval b, seq_5.nextval c, seq_5.nextval d;
> > +---+---+----+----+
> > | A | B |  C |  D |
> > |---+---+----+----|
> > | 1 | 6 | 11 | 16 |
> > +---+---+----+----+
> > ```
>
> Run the same query again; note how the sequence numbers change. You might expect that the next set of sequence numbers would start 5
> higher than the previous statement left off. However, the next sequence number starts 20 higher (5 \* 4, where 5 is the size of the
> increment and 4 is the number of `NEXTVAL` operations in the statement):
>
> > ```sqlexample
> > SELECT seq_5.nextval a, seq_5.nextval b, seq_5.nextval c, seq_5.nextval d;
> > +----+----+----+----+
> > |  A |  B |  C |  D |
> > |----+----+----+----|
> > | 36 | 41 | 46 | 51 |
> > +----+----+----+----+
> > ```

This example demonstrates that you can use a sequence as a default value for a column to provide unique identifiers for each row in
a table:

> ```sqlexample
> CREATE OR REPLACE SEQUENCE seq90;
> CREATE OR REPLACE TABLE sequence_demo (i INTEGER DEFAULT seq90.nextval, dummy SMALLINT);
> INSERT INTO sequence_demo (dummy) VALUES (0);
>
> -- Keep doubling the number of rows:
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
> ```
>
> ```sqlexample
> SELECT i FROM sequence_demo ORDER BY i LIMIT 10;
> +----+
> |  I |
> |----|
> |  1 |
> |  2 |
> |  3 |
> |  4 |
> |  5 |
> |  6 |
> |  7 |
> |  8 |
> |  9 |
> | 10 |
> +----+
> ```
>
> This query shows that each row in the table has a distinct value:
>
> ```sqlexample
> SELECT COUNT(i), COUNT(DISTINCT i) FROM sequence_demo;
> +----------+-------------------+
> | COUNT(I) | COUNT(DISTINCT I) |
> |----------+-------------------|
> |     1024 |              1024 |
> +----------+-------------------+
> ```

More examples are available in [Using Sequences](../../user-guide/querying-sequences.md).
