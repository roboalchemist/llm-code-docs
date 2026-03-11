# Source: https://docs.axonius.com/docs/useful-tips-and-tricks.md

# Useful Tips and Tricks for Working with Dynamic Value Statements

The following are useful tips for creating Dynamic Value statements (also referred to as "statements".)

* Before you configure a Dynamic Value statement, make sure you do the following:
  * Select the asset type in the Enforcement Set Query. It is not possible to select or change the asset type from the Module dropdown in the Syntax Helper.
  * Fill in default values for the action fields that are below the statement. These will be the fallback values for the Dynamic Value Statement.

* Syntax tips:
  * Write all values, operators, and syntax elements in lower case and case sensitive.
  * Write static string values within quotation marks " ". For example: "@gmail.com". Do not paste them from other systems.
  * Make sure that the quotation marks are straight and not curly, as curly ones are not supported.
  * Following functions and operators, make sure to place (values) in parentheses.

* Function and Operator tips:
  * Autocomplete and [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) show available options for action fields, operators, and functions.
  * A list of exact names of both adapter fields and action fields, as well as their field types, is available from the Syntax Helper and [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard).
  * You can manipulate asset data using functions.
  * You can nest functions (functions within functions).
  * You can include in mathematical functions (add, divide, max, min, multiply, subtract, sum) only number value types, and in the subtract function you can alternatively include two date-time fields. Otherwise, the function fails, which in turn causes the entire statement to fail.
  * The min/max functions work for all statement types for number values only.
  * You can apply a mathematical function, such as min/max, on a list field to return a single value field, and then apply a mathematical function, such as subtract, on that single value.
  * If one or more fields are missing a value, the function fails and the action field in the asset is set to the fallback static value. Refer to [Example 21 in Dynamic Value Statements and Use Cases](/docs/condition-statement-examples-and-use-cases#example-21).
  * When you use operators, such as concat and join, it is important to choose the relevant field types - list or single value. For example, Aggregated fields generally hold lists of values while Preferred fields mostly hold single values.

* Field tips:
  * It is recommended to match source field type with target field type. For example, when you use an adapter array field as input for a single string action field type, set-value takes the first value. However, the functions within the statement usually fail (although some transformations are available).
  * If an Adapter source field contains a list of values (array) and the target Action field is a single value field, the first value from the source field list is used for the comparison. It is recommended that you use specific adapter fields rather than aggregated fields that tend to be multi-value.
  * Tags are called 'labels' in the adapters.
  * It is advisable to give a meaningful default Tag name, such as Fallback, so that it isn't mistaken for a Tag name that is based on an asset field value.
  * The **Adapter Connection Label** field is not supported. You can use the following workaround: Create a custom data field, copy the Adapter Connection Label value to that field, and then use the custom field in the Dynamic Value statement.
  * All fields in a Dynamic Value statement must exist on the assets returned from the query. The Syntax Helper shows only the fields relevant for the asset type, and should be used to select the fields. For example, if the query runs on Security Findings, the fields in the statement must both exist in Security Finding records. Otherwise, it falls to the fallback static value.

* Custom field tips:
  * When you create a Dynamic Value Statement for adding a custom date field, make sure to use **form.field\_date.specific** with **Date type** set to **Specific date**, as a dynamic date can be written only to this type of Date field.  Do not use **form.field\_date.now** or a field with **Date type** set to **Now**, as this type of field cannot accept dynamic input and regardless of the statement, its value is always the action runtime.
  * When you create an Axonius custom field, the field name in the database is different depending on its type. For example, form.field\_date.specific for type date and form.field\_number for float. Use the Syntax Helper to select the correct field type.

.