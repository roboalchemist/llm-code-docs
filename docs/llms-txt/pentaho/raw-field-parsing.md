# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/splunk-input/raw-field-parsing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/splunk-input/raw-field-parsing.md

# Raw field parsing

The input step automatically attempts to parse the raw field into a number of child fields denoted by:

```
_raw.<Field Name>
```

It parses the raw field assuming that the field is formatted with name value pairs separated by a new line character, like this:

```
<Name1>=<Value1>\n <Name2>=<Value2>\n
```

If raw field data is not formatted like this, you must post-process those fields with other steps in the transformation flow. Note that your secondary steps may include String variables.
