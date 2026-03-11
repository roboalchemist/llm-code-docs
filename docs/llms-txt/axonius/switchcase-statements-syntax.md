# Source: https://docs.axonius.com/docs/switchcase-statements-syntax.md

# Switch/Case Statement Syntax

switch/case statements allow you to create complex Dynamic Value statements (also referred to as 'statements'). They check an asset field (declared in the switch) for multiple criteria (each declared by a case) and use those values to populate the Action fields.
Only assets matching the filter are affected using the matching value for the Action field.

<Callout icon="📘" theme="info">
  IMPORTANT

  All values, operators, and syntax elements in statements are lower case and case sensitive.
</Callout>

The basic syntax of switch/case statements for the various asset types is presented in the following table, followed by a description of the statement elements.

| Asset Type    | Basic Syntax                                                                                                                                                                                                                                    |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device        | `switch device.adapters_data.adaptername.fieldname case starts_with ("a") then form.form_field set_value "aaa" case starts_with ("b") then form.form_field set_value "bbb" case starts_with ("c") then form.form_field set_value "ccc"`         |
| User          | `switch user.adapters_data.adaptername.fieldname  case starts_with ("a") then form.form_field set_value "aaa" case starts_with ("b") then form.form_field set_value "bbb" case starts_with ("c") then form.form_field set_value "ccc"`          |
| Vulnerability | `switch vulnerability.adapters_data.adaptername.fieldname  case starts_with ("a") then form.form_field set_value "aaa" case starts_with ("b") then form.form_field set_value "bbb" case starts_with ("c") then form.form_field set_value "ccc"` |
| Software      | `switch software.adapters_data.adaptername.fieldname  case starts_with ("a") then form.form_field set_value "aaa" case starts_with ("b") then form.form_field set_value "bbb" case starts_with ("c") then form.form_field set_value "ccc"`      |

**Where**

* **switch** - Configure the field on which to apply the filter defined by the **case** statements that follow.
* **\[.adapters\_data.adaptername.fieldname]** - The source field of the Adapter (as displayed in the query bar). The asset-type prefix (for example: *device*, *user*, *vulnerability*, or *software*) must reflect the type of asset query. This value must be enclosed in square brackets. For example, \[device.adapter\_data.adaptername.fieldname]. Use [Syntax Helper](/docs/using-the-syntax-helper) or the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) to get the correct field name.

<Callout icon="📘" theme="info">
  Note

  Adapter field names must be written in square brackets in the following format. For example:

  * \[device.adapters\_data.active\_directory\_adapter.hostname]

  * \[user.adapters\_data.active\_directory\_adapter.username]

  * \[vulnerability.adapters\_data.active\_directory\_adapter.username]

  * \[software.adapters\_data.active\_directory\_adapter.username]

  * \[entity.]
</Callout>

* **case** - Define the filter criteria using one of the operators described in the following table. Autocomplete and the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) present a dropdown with a choice of operators. The examples above check if the field name **starts\_with** " ".

| Operator                                          | Description                                                                                                                                      |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **average (\[adapter.field])**                    | The average of all the number values in the list. The field type of adapter.field is a list (array) of numbers.                                  |
| **contains ("string")**                           | The field name contains the text indicated within the " ".                                                                                       |
| **count(n)**                                      | Counts and matches the n items in a list.                                                                                                        |
| **ends\_with ("string")**                         | The field name ends with the indicated text within the " ".                                                                                      |
| **field\_equal (" ")**                            | The field value is identical to the text within the " ".                                                                                         |
| **field\_exists**                                 | Tests whether the field exists.                                                                                                                  |
| **field\_not\_equal (" ")**                       | The field value is not identical to the text within the " ".                                                                                     |
| **field\_not\_exists**                            | Tests whether the field exists.                                                                                                                  |
| **gt(n)**                                         | The numeric field value is greater than the number or numeric field value n.                                                                     |
| **in(“string1”, "string2", ..., "stringN")**      | The string field value is equivalent to one of the strings in the parentheses.                                                                   |
| **in\_net(IP address range)**                     | The IP addresses in the adapter.field list field or IP address in the string field are in the IP address range specified in the parentheses.     |
| **lt(n)**                                         | The numeric field value is less than the number or numeric field value n.                                                                        |
| **not\_contains ("string")**                      | The field name does not contain the text indicated within the " ".                                                                               |
| **not\_ends\_with ("string")**                    | The field name does not end with the indicated text within the " ".                                                                              |
| **not\_in(“string1”, "string2", ..., "stringN")** | The string field value is not equivalent to any of the strings in the parentheses.                                                               |
| **not\_in\_net(IP address range)**                | The IP addresses in the adapter.field list field or IP address in the string field are not in the IP address range specified in the parentheses. |
| **not\_starts\_with ("string")**                  | The field name does not start with the indicated text within the " ".                                                                            |
| **starts\_with ("string")**                       | The field name starts with the indicated text within the " ".                                                                                    |
| **sum(\[adapter.field])**                         | The sum of all the number values in the list. The field type of adapter.field is a list (array) of numbers.                                      |

* **then** - *then* apply this value from the Adapter only to the assets whose field name **starts with** the value in *starts\_with*.
* **form\_fieldname** - The field name in the Action. Use Autocomplete or the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard) to choose the action field name or [Use the Syntax Helper](/docs/config-ec-conditions#using-syntax-helper) to find the correct action field name.
* **also** - Apply dynamic content *also* to this field.
* **set\_value** - Tells the Action to set the value of *form\_fieldname* to the value of the string or in the case that there is more than one string (item1 or item2 ... or itemN), to the first string that has a value.

More operators and functions are available than are used in these examples. See [Enforcement Action Statement Syntax Table](/docs/enforcement-action-condition-syntax-table) for a complete list of available statement elements and their syntax.

<Callout icon="📘" theme="info">
  Note

  You cannot filter Enforcement Set query results using a switch/case statement. You can only filter them by performing [data refinement](/docs/setting-page-columns-display#refining-the-data-displayed-in-table-columns-and-rows) on your saved query. Then, Dynamic Value statements will run only on the query results filtered according to the data refinement configuration (for all options with the exception of Refine field values by adapter connection).
</Callout>

### Switch/Case Statement Examples

The following examples illustrate some ways Switch/Case statements can be used.

* **Example** - Split the assets that match the query according to  the value in hostname, and use that value to determine the action form email recipient.

  * If the hostname starts with "a", then set the email recipient to [x@gmail.com](mailto:x@gmail.com)
  * If the hostname starts with "b", then set the email recipient to [y@gmail.com](mailto:y@gmail.com)

  ```
  switch device.adapters_data.active_directory_adapter.hostname
  case starts_with ("a") then form.emailList set_value "x@gmail.com"
  case starts_with ("b") then form.emailList set_value "y@gmail.com"
  ```

* **Example** - Split the assets that match the query according to the value of *fieldA*, and use that value to determine the action form tag\_name.

  * If fieldA starts with "a", then set the tag name to "x".
  * If fieldB starts with "b", then set the tag name to "y".
  * If fieldA starts with "c", then set the tag name to "z".

  ```
  switch user.adapters_fieldA 
  case starts_with ("a") then form.tag_name set_value "x" 
  case starts_with ("b") then form.tag_name set_value "y"
  case starts_with ("c") then form.tag_name set_value "z"
  ```

* **Example** - For all device adapters with qualys agent vulnerability score field value greater than 9, set the value of the Action form field number to 100.
  ```
  switch device.adapters_data.qualys_scans_adapter.qualys_agent_vulns.score 
  case gt(9) then form.field_number set_value 100
  ```