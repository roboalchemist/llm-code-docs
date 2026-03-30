# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/java-script-functions-pane.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/modified-java-script-value/java-script-functions-pane.md

# Java script functions pane

The **Java script functions** pane contains a tree view of scripts, constants, functions, input fields, and output fields as follows:

* **Transform Scripts**

  Scripts you have created in this step.
* **Transform Constants**

  Pre-defined, static constants that control what happens to the data rows. You must assign a constant value to the**trans\_Status** variable. To use these constants, you must first set the **trans\_Status** variable to `CONTINUE_TRANSFORMATION` at the beginning of the script, so that the variable assignment is made to the first row being processed. Otherwise, any subsequent assignments to the **trans\_Status** variable are ignored. Double-click a constant to add it to the Java script pane.

The constants are:

* **CONTINUE\_TRANSFORMATION**

  Includes the current row in the output row set.
* **SKIP\_TRANSFORMATION**

  Excludes the current row from the output row set and continues processing on the next row.
* **ERROR\_TRANSFORMATION**

  Excludes the current row from the output row set, generates an error, and any remaining rows are not processed.
* **ABORT\_TRANSFORMATION**

  Excludes the current row from the output row set, and any remaining rows are not processed, but does not generate an error. (This constant does not display in the PDI clientPDI client, but can be used in your script)
* **Transform Functions**: String, numeric, date, logic, special, and file functions you can use in scripts. These included functions are implemented in Java and execute faster than JavaScript functions. Each function has a sample script demonstrating its use. Double-click the function to add it to the Java script pane. Right-click and choose Sample to add the sample to the Java script pane.

**Note:** Not all JavaScript functions are listed here. You can use functions not included in this list.

* **Input Fields**

  Input fields for the step.
* **Output Fields**

  Output fields for the step.
