# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/perform-calculations-in-report-designer-cp/use-the-formula-editor.md

# Use the Formula Editor

When adding conditional formatting or other constraints on data-driven report elements, you have the option of using a built-in Formula Editor to help you build an expression with a graphical interface. All element properties in Report Designer can have formulas. You can type in your own formula by hand, but it's much easier to use the built-in Formula Editor to build an expression.

The Formula Editor provides you with basic math and comparison operators so that you don't have to enter them manually. Also provided are concatenate and percent functions. Click the **Field Selector** to select fields in the report.

Follow the instructions below to use Formula Editor:

1. Click on the element you want to add a condition or constraint to.
2. In the **Style** pane, select the property you want to add a constraint to, then click the round green **+** icon on the right side of the field.
3. Click the **...** button.

   The Formula Editor window appears.
4. Select a function category from the drop-down box.

   The default category is All.
5. Select a function from the **Functions** list.

   If you click on a function, a description of what it does will appear in the tan-colored field at the bottom of the window.
6. Double-click on a function to bring up the option fields.
7. Erase the default values in the option fields, and replace them with your own settings.

   If you need to associate a column with a function, click the **Select Field** button to the right of the field, then select the data or function you want to use. Follow proper SQL syntax in your options; all values must be in quotes, and all column names must be in uppercase letters and enclosed in square brackets.
8. When you're done, click **OK**, then click **Close**.

You have applied a formula to a report element.

**Note:** If you want more information on formula functions, conditionals, and operators, refer to the OASIS OpenFormula reference: <http://www.oasis-open.org/committees/download.php/16826/openformula-spec-20060221.html>. Pentaho does not implement all OpenFormula functions, but the functions Report Designer includes are documented on the OASIS website.
