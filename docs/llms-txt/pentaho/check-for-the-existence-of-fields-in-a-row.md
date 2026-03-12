# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/check-for-the-existence-of-fields-in-a-row.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/check-for-the-existence-of-fields-in-a-row.md

# Check for the existence of fields in a row

The following code examples check for the existence of fields in rows:

```javascript
var idx = getInputRowMeta().indexOfValue("lookup");
if ( idx < 0 )
{
   var lookupValue = 0;
}
else
{
   var lookupValue = row[idx];
}
```

With **Compatibility mode** selected:

```javascript
var idx = row.searchValueIndex("lookup");
if ( idx < 0 )
{
   var lookupValue = 0;
}
else
{
   var lookupValue = row.getValue(idx);
}
```

You cannot mix rows in PDI. All rows flowing over a single hop must have the same name, type, and number of fields.
