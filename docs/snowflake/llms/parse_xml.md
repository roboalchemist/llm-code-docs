# Source: https://docs.snowflake.com/en/sql-reference/functions/parse_xml.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Parsing)

# PARSE_XML

Interprets an input string as an [XML](../../user-guide/semistructured-data-formats.md) document, producing an [OBJECT](../data-types-semistructured.md) value.
If the input is NULL, the output is NULL.

See also:
:   [CHECK_XML](check_xml.md), [TO_XML](to_xml.md), [XMLGET](xmlget.md)

## Syntax

```sqlsyntax
PARSE_XML( <string_containing_xml> [ , <disable_auto_convert> ] )
```

```sqlsyntax
PARSE_XML( STR => <string_containing_xml>
  [ , DISABLE_AUTO_CONVERT => <disable_auto_convert> ] )
```

## Arguments

**Required:**

`string_containing_xml` . OR . `STR => string_containing_xml`
:   Specify an expression that evaluates to a VARCHAR value that contains valid XML.

**Optional:**

`disable_auto_convert` . OR . `DISABLE_AUTO_CONVERT => disable_auto_convert`
:   A Boolean expression that specifies whether or not the function should attempt to convert numeric and Boolean values in
    `string_containing_xml` to Snowflake data types. (For details about this conversion, see Usage Notes below.)

    * If you don’t want the function to convert these values, set this argument to `TRUE`. This setting
      has an effect that is similar to the `DISABLE_AUTO_CONVERT` parameter in [CREATE FILE FORMAT](../sql/create-file-format.md).
    * If you want the function to convert these values, set this argument to `FALSE` or omit this argument.

    Default: `FALSE`

## Returns

The data type of the returned value is OBJECT. The OBJECT contains an internal representation of the XML.

## Usage notes

* You must either specify all arguments by name or by position. You can’t specify some of the arguments by name and other
  arguments by position.

  When specifying an argument by name, you can’t use double quotes around the argument name.
* The content of every element in XML documents is text. PARSE_XML attempts to convert some XML data from text to native
  (Snowflake SQL). For more information, see [SQL data types reference](../../sql-reference-data-types.md).

  * NUMERIC and BOOLEAN:

    PARSE_XML attempts to convert obviously numeric and Boolean values to the native representation in a way that printing
    these values back produces textually identical results. For example, when parsing decimal numbers, PARSE_XML attempts
    to preserve exactness of the representation by treating 123.45 as NUMBER(5,2), not as a DOUBLE. However:

    * Numbers in scientific notation (i.e. 1.2345e+02) or numbers that cannot be stored as fixed-point decimals due to range or
      scale limitations are stored as DOUBLE.
    * If the content of an XML element is a number with digits after the decimal point, then PARSE_XML might truncate trailing zeros.

    If you do not want the function to perform this conversion, pass `TRUE` for the `disable_auto_convert` argument.
  * TIMESTAMP, DATE, TIME, BINARY:

    Because XML doesn’t represent values such as TIMESTAMP, DATE, TIME, or BINARY natively, these have to be represented as strings
    in XML. PARSE_XML doesn’t automatically recognize these values. They are retained as strings, so convert
    the values from strings to native SQL data types if needed.
* XML attributes are an unordered collection of name/value pairs. The PARSE_XML function doesn’t necessarily
  preserve order. For example, converting text to XML and back to text might result in a string that contains the
  original information in a different order.
* You might see changes in whitespace between elements when converting from string to XML.
* When PARSE_XML is used to insert [numeric values](../data-types-numeric.md) into a VARIANT column that are a
  mix of integers (for example, INT or INTEGER) and values in decimal notation (for example, NUMBER or FLOAT), the function
  might add trailing zeros to the values.

  The following example uses PARSE_XML to insert a mix of integer values and values in decimal notation into a VARIANT column:

  ```sqlexample
  CREATE OR REPLACE TABLE test_xml_table(xmlcol VARIANT);

  INSERT INTO test_xml_table (
    SELECT PARSE_XML($1) FROM VALUES
      ('<c>3.1</c>'),
      ('<e>2</e>'),
      ('<b>0.123</b>'));
  ```

  Query the table:

  ```sqlexample
  SELECT * FROM test_xml_table;
  ```

  ```output
  +--------------+
  | XMLCOL       |
  |--------------|
  | <c>3.100</c> |
  | <e>2.000</e> |
  | <b>0.123</b> |
  +--------------+
  ```

  The output shows that trailing zeros were added to the values in the first two rows.

## Examples

The following example demonstrates how to use the PARSE_XML function to convert a string of XML to an OBJECT that can be inserted
into an OBJECT column:

```sqlexample
CREATE OR REPLACE TABLE xtab (v OBJECT);

INSERT INTO xtab SELECT PARSE_XML(column1) AS v
  FROM VALUES ('<a/>'), ('<a attr="123">text</a>'), ('<a><b>X</b><b>Y</b></a>');

SELECT * FROM xtab;
```

```output
+------------------------+
| V                      |
|------------------------|
| <a></a>                |
| <a attr="123">text</a> |
| <a>                    |
|   <b>X</b>             |
|   <b>Y</b>             |
| </a>                   |
+------------------------+
```

The following example demonstrates the differences between using and disabling the conversion of numeric values. In this example,
when the conversion isn’t disabled, the function interprets a number in scientific notation as a DOUBLE.

```sqlexample
SELECT PARSE_XML('<test>22257e111</test>'), PARSE_XML('<test>22257e111</test>', TRUE);
```

```output
+-------------------------------------+-------------------------------------------+
| PARSE_XML('<TEST>22257E111</TEST>') | PARSE_XML('<TEST>22257E111</TEST>', TRUE) |
|-------------------------------------+-------------------------------------------|
| <test>2.225700000000000e+115</test> | <test>22257e111</test>                    |
+-------------------------------------+-------------------------------------------+
```

The following example demonstrates how to specify the arguments to the function by name:

```sqlexample
SELECT PARSE_XML(STR => '<test>22257e111</test>', DISABLE_AUTO_CONVERT => TRUE);
```

```output
+--------------------------------------------------------------------------+
| PARSE_XML(STR => '<TEST>22257E111</TEST>', DISABLE_AUTO_CONVERT => TRUE) |
|--------------------------------------------------------------------------|
| <test>22257e111</test>                                                   |
+--------------------------------------------------------------------------+
```
