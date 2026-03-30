# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/round-a-b-function.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/calculator/troubleshooting-the-calculator-step/round-a-b-function.md

# Rounding method for the Round (A, B) function

Starting in Pentaho 6.0, the **Round (A, B)** function rounds to the nearest positive infinity number. This rounding method is known as Round half to ceiling. Before version 6.0, **Round (A, B)** used the Round half to even method, also called unbiased rounding, convergent rounding, statistician's rounding, German mathematician's rounding, Dutch rounding, Gaussian rounding, odd-even rounding, bankers' rounding, or broken rounding. It is widely used in bookkeeping.

**Note:** The "Round half to even" method is the default rounding mode used in IEEE 754 computing functions and operators.

Perform these steps to override the default "Round half to ceiling" method and use the "Round half to even" method.

1. Stop the Pentaho Server.

   **Note:** See the **Install Pentaho Data Integration and Analytics** document for instructions on stopping and starting the Pentaho Server.
2. Open the `kettle.properties` file in a text editor. By default, the `kettle.properties` file is typically stored in your home directory or the `.pentaho` directory.
3. Edit the file and add the following lines:

   ```
   ROUND_2_MODE=ROUND_HALF_EVEN
   ROUND_2_MODE_BACKWARD_COMPATIBILITY_VALUE=ROUND_HALF_EVEN
   ```
4. When complete, close and save the file.
5. Start the Pentaho Server.
