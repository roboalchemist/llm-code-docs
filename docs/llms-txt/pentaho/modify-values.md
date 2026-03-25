# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/java-script-pane/modify-values.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/java-script-pane/modify-values.md

# Modify values

To change an input value, enter the value in the **Rename to** field, and set the **Replace value 'Fieldname' or 'Rename To'** field to `Y`. The **Rename to** field (or if this is blank, the **Fieldname**field) is used to lookup an existing field and replace its value and metadata type. If the specified field does not exist in the input stream, an error is passed onto the next step indicating that the field to be replaced could not be found.

The following example changes the value of the **field1** field in the input row with **Compatibility mode**selected:

```javascript
field1.setValue(100);
```

**Note:** `setValue()` takes all possible types that can be used in PDI.
