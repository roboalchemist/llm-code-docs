# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/parameters-tab/order-of-processing.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/transformation-executor/options-transformation-executor/parameters-tab/order-of-processing.md

# Order of processing

The order of processing variables and parameters depends on if the transformation inherits all its variables from the transformation. Your selection for the **Inherit all variables from transformation** check box in the **Parameters** tab decides the processing order as described below:

* When the **Inherit all variables from transformation** is selected, the processing order is:

Parent Transformation \[**Parameter**] >> Transformation Executor \[**Variable/Parameter name**] >> Child Transformation \[**Parameter**]

1. First, the parameters and variables defined in the **Parameters** tab in the parent transformation.
2. Then the parameters and variables defined in the **Parameters** tab in the Transformation Executor step.

   **Note:** If the variable name matches between the one defined in the parent transformation and the one defined in the **Parameter** tab of the Transformation Executor step, then the system will select the value defined in the Transformation Executor step.
3. Finally, the parameters and variables defined in the **Parameters** tab in the child transformation.

   **Note:** If the variable name matches between the one defined in the **Parameter** tab of the Transformation Executor step and the one defined in the child transformation, then the system will select the value defined in the child transformation.

* When the **Inherit all variables from transformation** is cleared, the processing order is:

Transformation Executor \[**Variable/Parameter name**] >> Child Transformation \[**Parameter**]

1. First, the parameters and variables defined in the **Parameters** tab in the Transformation Executor step
2. Then the parameters and variables defined in the **Parameters** tab in the child transformation, such that any variables defined in the **Parameters** tab of the Transformation Executor step will pass to the child transformation.
