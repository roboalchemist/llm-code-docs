# Source: https://docs.pentaho.com/pba-report-designer/function-reference/script-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/function-reference/script-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/function-reference/script-functions.md

# Script functions

The **Script** category contains functions that enable you to directly type in code from a supported scripting language.

* Bean-Scripting Framework (BSF)
* Bean-Scripting Host (BSH)
* JavaScript
* Single Value Query

The only unique object Pentaho offers in Report Designer for a scripting language is getValue for the Bean-Scripting Framework, which retrieves the current record or row, as shown below:

```
Object getValue()
  {
  	Object value = dataRow.get(&quot;RegionVariance&quot;);
      if (value instanceof Number == false)
      {
      	return Boolean.FALSE;
      }
      Number number = (Number) value;
      if (number.doubleValue() &lt; 0)
      {
      return Boolean.TRUE;
      }
      return Boolean.FALSE;
  }
```
