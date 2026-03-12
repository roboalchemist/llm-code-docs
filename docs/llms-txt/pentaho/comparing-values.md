# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/comparing-values.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/examples/comparing-values.md

# Comparing values

Values coming from the data row are Java objects, so you must use the compare methods that are specific to the Java object. For example, a compare between values with the operators `=`, `>`, `<` does not work.

The following values require the use of compare methods:

* String values
* Numeric values
* Filter rows
