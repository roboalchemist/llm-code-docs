# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/split-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/split-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/split-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/split-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/split-fields.md

# Split fields

Select **Compatibility mode** and use the following code to split a field containing numbers and characters, with inconsistent layout, and where the first part is numeric and the second part is characters (where *Merchant\_Code* is the name of the input field):

```javascript
java;
 
var str = Merchant_Code.getString();
 
var code = "";
var name = "";
 
for (i = 0; i < str.length(); i++ )
{
    c = str.charAt(i);
    if ( ! java.lang.Character.isDigit(c) )
    {
        code = str.substring(0, i);
        name = str.substring(i);
        Alert("code="+code+", name="+name);
        break;
    }
}
```

The `Alert()` displays the name of the fields.
