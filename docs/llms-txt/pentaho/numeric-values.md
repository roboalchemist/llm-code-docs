# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/numeric-values.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/numeric-values.md

# Numeric values

Most values that are assigned in JavaScript are floating point values by default, even if you think you have assigned an integer value. If you are having trouble using `==` or `switch/case` on values that you know are integers, use the following constructs:

```javascript
parseInt(num)==parseInt(num2)
```

or

```javascript
switch(parseInt(valuename))
{
case 1:
case 2:
case 3:
 strvalueswitch = "one, two, three";
 break;
case 4:
 strvalueswitch = "four";
 break;
default:
 strvalueswitch = "five";
}
```
