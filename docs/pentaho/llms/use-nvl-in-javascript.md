# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/use-nvl-in-javascript.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/use-nvl-in-javascript.md

# Use NVL in JavaScript

**NVL** (replace null value function) lets you replace a null (returned as a blank) with a string in the results of a query.

Select **Compatibility mode** and use the following code to replace the value of **fieldName** with the value of `1`, if **fieldName** is null:

```javascript
var a;
if ( fieldname.isNull() )
{
    a = '0';
}
else
{
    a = fieldName.getString();
}

```

You can also use:

```javascript
fieldName.nvl('1');
```
