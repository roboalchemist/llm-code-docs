# Source: https://docs.snowflake.com/en/sql-reference/functions/check_xml.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Parsing)

# CHECK_XML

Checks the validity of an [XML](../../user-guide/semistructured-data-formats.md) document. If the input string is NULL or a valid XML document,
the output is NULL. In case of an XML parsing error, the output string contains the error message.

See also:
:   [PARSE_XML](parse_xml.md), [TO_XML](to_xml.md), [XMLGET](xmlget.md)

## Syntax

```sqlsyntax
CHECK_XML( <string_containing_xml> [ , <disable_auto_convert> ] )
```

```sqlsyntax
CHECK_XML( STR => <string_containing_xml>
  [ , DISABLE_AUTO_CONVERT => <disable_auto_convert> ] )
```

## Arguments

**Required:**

`string_containing_xml` . OR . `STR => string_containing_xml`
:   Specify an expression that evaluates to a VARCHAR value that contains valid XML.

**Optional:**

`disable_auto_convert` . OR . `DISABLE_AUTO_CONVERT => disable_auto_convert`
:   Specify the same value that you pass to the [PARSE_XML](parse_xml.md) function.

    Default: `FALSE`

## Returns

The data type of the returned value is VARCHAR.

## Usage notes

* You must either specify all arguments by name or by position. You can’t specify some of the arguments by name and other
  arguments by position.

  When specifying an argument by name, you can’t use double quotes around the argument name.

## Examples

The following examples use the CHECK_XML function.

### Show the output of the function when the XML is valid

```sqlexample
SELECT CHECK_XML('<name> Valid </name>');
```

```output
+-----------------------------------+
| CHECK_XML('<NAME> VALID </NAME>') |
|-----------------------------------|
| NULL                              |
+-----------------------------------+
```

### Show the output of the function when the XML is invalid

```sqlexample
SELECT CHECK_XML('<name> Invalid </WRONG_CLOSING_TAG>');
```

```output
+--------------------------------------------------+
| CHECK_XML('<NAME> INVALID </WRONG_CLOSING_TAG>') |
|--------------------------------------------------|
| no opening tag for </WRONG_CLOSING_TAG>, pos 35  |
+--------------------------------------------------+
```

### Locate records with invalid XML

```sqlexample
SELECT xml_str, CHECK_XML(xml_str)
  FROM my_table
  WHERE CHECK_XML(xml_str) IS NOT NULL;
```
