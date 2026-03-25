# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/get-system-info/general/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/get-system-info/general/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/data-types.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/data-types.md

# Data Types

* **Question**

  How do the data types work internally?

  * **Suggested Solution**

    You might notice that if you multiply an integer and a number, the result is always rounded. The Calculator step uses the data type of the value to the left side of the multiplication calculation, in this case the value in **Field A**, as the driver for the calculation.

    If you want more precision, place the value in **Field B** on the left side of the calculation. Alternatively, change the data type of **Field A** to Number.
