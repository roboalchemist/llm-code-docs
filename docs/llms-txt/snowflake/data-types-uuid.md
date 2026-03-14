# Source: https://docs.snowflake.com/en/sql-reference/data-types-uuid.md

# UUID data type

The UUID data type stores universally unique identifiers (UUIDs). A UUID is a 128-bit binary value that
uniquely identifies information. Each UUID value is designed to be globally unique, which means that
there is a very low probability that two different systems will generate the exact same UUID independently.
However, uniqueness depends on how the UUID values are generated, and the Snowflake UUID data type
itself doesn’t guarantee uniqueness. For example, a user can insert the same UUID value multiple
times without errors.

UUID values are in UUID format, which is a 36-character string of hexadecimal digits, separated by
hyphens, in the pattern 8-4-4-4-12. For example, `f353ca91-4fc5-49f2-9b9e-304f83d11914` is a string
in UUID format.

For more information about the UUID data type, see the
[Universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) Wikipedia
article.

The following considerations apply to the UUID data type:

* [Snowflake drivers](../developer-guide/drivers.md) treat UUID values as text strings.
* The ANSI literal form of UUID is supported as input.
* UUID values of any version can be inserted into tables.
* UUID values are case-insensitive.

## Specify a UUID data type

* To specify a UUID type, use the following syntax:

  ```sqlsyntax
  <column_name> UUID
  ```

  Where:

  * `column_name` is the name of a column in a table.

## Limitations for the UUID data type

The following limitations apply to the UUID data type:

* A UUID value can’t be stored in a value of a
  [semi-structured data type](data-types-semistructured.md) or
  [structured data type](data-types-structured.md).

  To store a UUID value as a string in a value of one of these types, you can [cast](data-type-conversion.md)
  the UUID value to a VARCHAR value.
* The UUID data type isn’t supported in stored procedures or user-defined functions (UDFs) written in a
  language other than SQL, such as Python or Java.
* The UUID data type isn’t supported in [hybrid tables](../user-guide/tables-hybrid.md).
* The UUID data type isn’t supported in Snowpark.
* The following features don’t support the UUID data type:

  * [Differential privacy](../user-guide/diff-privacy/differential-privacy-sql-reference.md)
  * [Sensitive data classification](../user-guide/classify-intro.md)

## Examples for the UUID data type

The following examples insert UUID values into tables:

* Insert a UUID value into a table
* Automatically generate UUID values when you insert rows into a table

### Insert a UUID value into a table

* Create a table with a column of UUID type and insert a UUID value:

  ```sqlexample
  CREATE TABLE sample_uuid_table(uuid_col UUID);

  INSERT INTO sample_uuid_table VALUES ('c73d9175-0a1d-48c6-8d30-df165461328b');
  ```

### Automatically generate UUID values when you insert rows into a table

The following example shows you how to automatically generate UUID values when you insert rows into a table:

1. Create a table that uses the [UUID_STRING](functions/uuid_string.md) function to
   generate a UUID value for each row inserted into the table:

   ```sqlexample
   CREATE OR REPLACE TABLE sample_generate_uuid (
     id UUID DEFAULT UUID_STRING() NOT NULL,
     sample_column VARCHAR);
   ```

2. Insert values into the table and omit the `id` column so that a UUID value is generated and
   inserted automatically:

   ```sqlexample
   INSERT INTO sample_generate_uuid (sample_column) VALUES
     ('value_a'),
     ('value_b');
   ```

3. Query the table to view the generated UUID values:

   ```sqlexample
   SELECT * FROM sample_generate_uuid;
   ```

   ```output
   +--------------------------------------+---------------+
   | ID                                   | SAMPLE_COLUMN |
   |--------------------------------------+---------------|
   | f353ca91-4fc5-49f2-9b9e-304f83d11914 | value_a       |
   | da563283-e201-4744-b158-221dd204a61f | value_b       |
   +--------------------------------------+---------------+
   ```
