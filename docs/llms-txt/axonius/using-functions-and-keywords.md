# Source: https://docs.axonius.com/docs/using-functions-and-keywords.md

# Using Functions, Operators, and Keywords

The following are some of the functions, operators, and keywords that you can use in Dynamic Value statements (also referred to as 'statements'):

* [*min/max* functions](#using-minmax-functions)
* [*add*, *multiply*, and *divide* functions](#using-add-multiply-and-divide-functions)
* [*subtract* function](#using-the-subtract-function)
* [*array* function](#using-the-array-function)
* [*concat\_array* function](#using-the-concat_array-function)
* <Anchor label="_multiply_array_ values_function" target="_blank" href="#using-the-multiply_array_values-function">*multiply\_array* values\_function</Anchor>
* [*concat\_prefix* function](#using-the-concat_prefix-function)
* [*average* function](#using-the-average-function)
* [Boolean operators (field\_equal, field\_not\_equal](#using-boolean-operators-in-case-statements)
* [The *contains* operator](#using-the-contains-operator)
* [The *not\_contains* operator](#using-the-not_contains-operator)
* [The *in* operator](#using-the-in-operator)
* [The *also* operator](#using-the-also-operator)
* [The *join* function](#using-the-join-function-for-array-fields)
* [The *by\_key* function](#using-the-by_key-function-for-complex-field-objects)
* [The *filter* function](#using-the-filter-function)
* [The *filter\_by\_key* function](#using-the-filter_by_key-function-for-complex-field-objects)
* [The *filter\_by\_key\_with\_operator* function](#using-the-filter_by_key_with_operator-function-for-complex-field-objects)
* [The *filter\_value\_by\_key\_with\_operator* function](#using-the-filter_value_by_key_with_operator-function-for-complex-field-objects)
* [The *generate\_string* function](#using-the-generate_string-function)
* [The *concat* function](#using-the-concat-function-for-string-arguments)
* [The *date\_format* function](#using-the-date_format-function-for-string-manipulations)
* The *regex\_extract* function
* [The *regex\_replace* function](#using-the-regex_replace-function)
* [The *relation* function](#using-the-relation-function)
* [The *split* function](#using-the-split-function)
* [The *count* function](#using-the-count-function)
* [The *starts\_with* function](#using-the-starts_with-function)
* [The *substring* function](#using-the-substring-function)
* [The *title\_case* function](#using-the-title_case-function)
* [The *to\_date* function](#using-the-to_date-function)
* [The *to\_table* function](#using-the-to_table-function)
* [The *to\_int* function](#using-the-to_int-function)
* [The *to\_lower* function](#using-the-to_lower-function)
* [The *to\_upper* function](#using-the-to_upper-function)
* [The *unique* function on array fields](#using-the-unique-function-for-array-fields)
* [The *unique* function on a nested function](#applying-the-unique-function-on-a-nested-function)
* [The *field\_exists* operator](#using-the-field_exists-operator)
* [The *field\_not\_exists* operator](#using-the-field_not_exists-operator)
* <Anchor label="The _in_net_ operator" target="_blank" href="#using-the-in_net-operator">The *in\_net* operator</Anchor>
* <Anchor label="The _not_in_net_ operator" target="_blank" href="#using-the-not_in_net-operator">The *not\_in\_net* operator</Anchor>
* [Using *lt* in Switch Statements](#using-lt-in-switch-statements)
* [Using *gt* in Switch Statements](#using-gt-in-switch-statements)
* [Using the Wildcard Character in Statements](#using-the-wildcard-character-in-statements)
* [Using Operators with Arrays (Lists)](#using-operators-with-arrays-lists)
* [Nesting Functions](#nesting-functions)

## Using *min/max* Functions

The **min/max** functions work for all statement types for number values only. It sets the value of the field in the Enforcement Action to the *min/max* value of a group of single value fields, an array (list) field, or a group of array fields indicated in the **min/max** clause.

### Using the *min/max* Function with an Array (List) Field

**min** has the syntax:

```
set_value min([adapter.arrayfield])
```

**max** has the syntax:

```
set_value max([adapter.arrayfield])
```

* **Example** - Sets the value of the **form.field\_integer** field to the *maximum* value found in the **device.specific\_data.data.software\_cves.cvss3\_score** list.
  ```
  device all then form.field_integer set_value max([device.specific_data.data.software_cves.cvss3_score])
  ```
* **Example** - Sets the value of the **form.field\_integer** field to the *minimum* value found in the **device.specific\_data.data.software\_cves.cvss3\_score** list.
  ```
  device all then form.field_integer set_value min([device.specific_data.data.software_cves.cvss3_score])
  ```

### Using the *min/max* Functions with Multiple Single Value Fields

**min** has the syntax:

```
set_value min(item1, item2, ..., itemN)
```

**max** has the syntax:

```
set_value max(item1, item2, ..., itemN)
```

* **Example** - Compares the number of logical cores in the following three fields, and sets the value of the **form.field\_integer** field to the maximum value.
  * **device.adapters\_data.aws\_adapter.cpus.logical\_cores**
  * **device.specific\_data.data.cpus.logical\_cores**
  * **device.adapters\_data.bigid\_adapter.cpus.logical\_cores**
  ```
  device all then form.field_integer set_value max([device.adapters_data.aws_adapter.cpus.logical_cores], [device.specific_data.data.cpus.logical_cores], [device.adapters_data.bigid_adapter.cpus.logical_cores])
  ```

### Using the *min/max* Functions with Multiple Array Fields

The **min/max** functions can return the minimum or maximum value from multiple array fields. The minimum or maximum value from each field is found and then the minimum or maximum of those values is used.

min/max has the syntax:

```
set_value min([....],[....],...,[....])
or
set_value max([....],[....],...,[....])
```

* **Example** - Sets the value of the **form.field\_integer** field to the *maximum* value found in either of these array fields:
  * device.specific\_data.data.software\_cves.cvss3\_score
  * device.adapters\_data.tenable\_security\_center\_adapter.software\_cves.cvss2\_score

```
device all then form.field_integer set_value max([device.specific_data.data.software_cves.cvss3_score], [device.adapters_data.tenable_security_center_adapter.software_cves.cvss2_score])
```

## Using *add*, *multiply*, and *divide* Functions

The *add*, *multiply*, and *divide* functions can be used in the same way as *concat* or *sum* to add/multiply/divide one or more single value numerical fields to/by a number or numbers.

**add** has the syntax:

```
add (value1, value2,..., valueN)
```

**multiply** has the syntax:

```
multiply([some.field.name], value)
```

or

```
multiply (value1, value2,..., valueN)
```

**divide** has the syntax:

```
divide([some.field.name], value)
```

or

```
divide (value1, value2,..., valueN)
```

* **Example** - Sets the value of the **form.field\_integer** field to the sum of the following:
  * device.custom.asset\_criticality multiplied by 0.4
  * device.custom.asset\_severity multiplied by 0.6

```
device all then form.field_integer set_value
add (multiply([device.custom.asset_criticality], 0.4), multiply([device.custom.asset_severity], 0.6))
```

* **Example** - In the following example, calculation is performed starting with the most internal parentheses, outward. Sets the value of the **form.field\_integer** field, as follows:
  * Adds the following:
    cve\_severity.critical\_count multiplied by 0.9
    and
    cve\_severity.high\_count multiplied by 0.6

  * Adds cve\_severity.high\_count and cve\_severity.critical\_count.

  * Divides the first sum by the second sum to give the result.

```text
device all then form.field_number set_value divide( add( multiply([device.specific_data.data.software_cves.cve_severity.critical_count], 0.9), multiply([device.specific_data.data.software_cves.cve_severity.high_count], 0.6) ), add([device.specific_data.data.software_cves.cve_severity.high_count], [device.specific_data.data.software_cves.cve_severity.critical_count]) )
```

## Using the *subtract* Function

The *subtract* function can be used to return the difference between two numbers (typed or values from single value fields) or two date-time fields.

<Callout icon="📘" theme="info">
  Note

  This function expects exactly two numbers or dates. When using list (array) fields in the **subtract** function, it is recommended to add **min** or **max** functions so that the  function is done on single value fields.
</Callout>

**subtract** has the syntax:

```
subtract (item1, item2)
```

* **Example** - For all devices that match the query, sets the value of the **DiffDates** field (**form.field\_number**) to the result of the current date and time (the value in **device.adapters\_data.gui.custom\_nowdate**) minus the date and time that the asset was last seen (value in **device.specific\_data.data.last\_seen**).

```
device all then form.field_number set_value subtract([device.adapters_data.gui.custom_nowdate], [device.specific_data.data.last_seen]) 
```

The following screen shows the results of the Enforcement Set run:

<Image alt="DateDifferenceRunResults" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DateDifferenceRunResults.png" />

## Using the *array* Function

The *array* function can be used to create a custom field, which is an array of multiple fields. It sets the value of the custom list field in the Enforcement Action to an *array*  of fields. This enables taking multiple values from different fields and aggregating them into a single custom list field.

<Callout icon="📘" theme="info">
  Note

  Each field input to the function can be an adapter field or text string.
</Callout>

**array** has the syntax:

```
**array** ([adapter.field1], [adapter.field2], ..., [adapter.fieldN])
```

**Example** - For all devices that match the query, create one multi-value field 'manufacturer' (**form.field\_list.value**) with values from the following aggregated fields, which have relevant manufacturer information:

* Network Interfaces: Manufacturer (**device.specific\_data.data.network\_interfaces.manufacturer**)
* Device Manufacturer (**device.specific\_data.data.device\_manufacturer**)
* Bios Manufacturer (**device.specific\_data.data.bios\_manufacturer**)

```
device all then form.field_list.value set_value
array( [device.specific_data.data.network_interfaces.manufacturer],
[device.specific_data.data.device_manufacturer],
[device.specific_data.data.bios_manufacturer] )
```

## Using the *concat\_array* Function

The *concat\_array* function joins one or more arrays into a single array.

**concat\_array** has the syntax:

```
concat_array ([adapter.field], [adapter.field],...,[adapter.field]) 
```

**Example** - For all devices that match the query, use the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action together with the Dynamic Value statement below to create a multi-value tag which contains all field values from the combination of the two list fields: 'CISA Known Exploited Vulnerabilities' (**device.specific\_data.data.cisa\_vulnerabilities** and 'Network Interfaces: IPs' (**device.specific\_data.data.network\_interfaces.ips**).

```
device all then form.tag_name 
set_value concat_array([device.specific_data.data.cisa_vulnerabilities],[device.specific_data.data.network_interfaces.ips])
```

## Using the *multiply\_array\_values* Function

The *multiply\_array\_values* function takes a single array field as input and returns the product (the result of multiplication) of the numerical equivalent of all values within that array.

**multiply\_array\_values** has the syntax:

```
multiply_array_values (value1, value2,...,valuen) 
```

**Example** - For all devices that match the query, use the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action together with the Dynamic Value statement below to create a tag with a value equal to the product of the values in the custom array field **device.adapters\_data.gui.custom\_test**. For example, for devices where the \[device.adapters\_data.gui.custom\_test] field contains the array \[2, 3, 5], the form.tag\_name is set to 30.

```
device all then form.tag_name set_value multiply_array_values([device.adapters_data.gui.custom_test])
```

## Using the *concat\_prefix* Function

The *concat\_prefix* function appends a specified string to each field value in a list (array). This enables creating a tag list field that appends a label to each field value in the array.

**concat\_prefix** has the syntax:

```
concat_prefix ("prefix", [adapter.field]) 
```

* **Example 1** - For all devices that match the query, use the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action together with the Dynamic Value statement below to create a multi-value tag where the prefix '**IPv4:** ' is appended to each IPv4 address in 'Network Interfaces: IPv4s' (**device.specific\_data.data.network\_interfaces.ips\_v4**).\
  A device with network interface IPv4 addresses \[**111.0.0.0**, **111.0.0.1**], will be assigned a tag with the label \[**"IPv4: 111.0.0.0", "IPv4: 111.0.0.0"**]

```
user all then form.tag_name set_value  
concat_prefix ("IPv4: ", [device.specific_data.data.network_interfaces.ips_v4])
```

* **Example 2** - For all devices that match the query, use the [Axonius - Add Tag to Assets](/docs/add-remove-tag) enforcement action together with the Dynamic Value statement below to create a multi-value tag where the prefix '**Owner:** ' is appended to each email address in 'All Associated Email Addresses' (**device.specific\_data.data.all\_associated\_email\_addresses**). This allows for better searching of who owns what.

```
device all then form.tag_name set_value concat_prefix ("Owner: ",[device.specific_data.data.all_associated_email_addresses]) 
```

## Using the *average* Function

The **average** function works for all statement types for number values only. It sets the value of the field in the Enforcement Action to the *average*  of the number values in an array (list) field of numbers.

**average** has the syntax:

```
average ([adapter.arrayfield])
```

* **Example** - For all vulnerabilities (Aggregated Security Findings) that match the query, sets the value of **form.field\_number** to the average CVSS score (**vulnerability.adapters\_data.tenable\_io\_adapter.cvss**).

```
vulnerability all then form.field_number set_value average ([vulnerability.adapters_data.tenable_io_adapter.cvss])
```

## Using Boolean Operators in Case Statements

The Boolean operators **true** and **false** can be used in switch/case statements to test the value of a Boolean field.

* **Example** - If **device.rapid7.some\_boolean\_field** has the value **true**, then set the value of **form.category** to **1234**. If its value is **false**, then set the value of **form.category** to **4567**.

  ```
   switch device.rapid7.some_boolean_field
   case field_equal (true) then form.category set_value "1234"
   case field_equal (false) then form.category set_value "4567"
  ```
* **Example** - If **device.rapid7.some\_boolean\_field** does not have the value **true**, then set the value of **form.category** to **0000**. If it does not have the value **false**,  then set the value of **form.category**  to **1111**.

```
switch  device.rapid7.some_boolean_field
case field_not_equal (true) then  form.category set_value "0000"
case field_not_equal (false) then form.category set_value "1111"
```

<Callout icon="📘" theme="info">
  Note

  When used on a Boolean field, **case field\_not\_equal (false)** is equivalent to **case field\_equal (true)**, and **case field\_not\_equal** (true) is equivalent to **case field\_equal (false)**.
</Callout>

## Using the *contains* Operator

The **contains** operator for switch statements applies the Enforcement action if the string or array contains the indicated value:

* A string may contain a substring.
* An array must contain the exact value.

**contains** has the syntax:

```
switch some.field.name case contains("value") then ...
```

* **Example** - This statement verifies that the labels list **device.labels** contains a value 'TAG', and if true, sets the value of the **form.color** field to 'blue'.
  For example, if the labels list has the values \[“123”, “TAG”, “ANOTHER”], the switch statement applies the enforcement action, i.e., sets the form color field to blue.
  ```
  switch device.labels case contains("TAG") then form.color set_value "blue"
  ```
* **Example** - This statement  verifies that 'ABC`is a substring of (or the entire) asset name. (e.g.,`ABCDEFG' as asset name returns true), and if yes, assigns the device (**device.specific\_data.data.assigned\_to**) to Group ABC.
  ```
  switch device.specific_data.name case contains("ABC") then device.specific_data.data.assigned_to set_value "Group ABC"
  ```

## Using the *not\_contains* Operator

The **not\_contains** operator for switch statements applies the Enforcement action if the string or array does not contain the indicated value:

* Checks that a string or substring do not contain the value.
* Checks that an array does not contain the exact value.

**not\_contains** has the syntax:

```
switch some.field.name case not_contains("value") then ...
```

* **Example** - This statement  verifies that 'x`is not a substring of (or the entire) asset name (**device.specific_data.data.name**). (e.g., `ABCDEF`as asset name returns true), and if yes, assigns the tag name (**form.tag_name**) the value`success'.

```
switch device.specific_data.data.name
case not_contains ("x") then form.tag_name set_value "sucesss"
```

## Using the *in* Operator

The **in** operator for switch statements applies the Enforcement action if the array contains at least one value that is equivalent to one of the indicated strings.

**in** has the syntax:

```
switch array.field.name case in (["aaa", "bbb", "ccc"]) then ...
```

* **Example** - If the  network operational status (device.specific\_data.data.network\_interfaces.operational\_status) is one of the following: **Dormant**, **Down**, **NotPresent**, or **Unknown**, the tag name is set to **Inactive**.

  ```
  switch device.specific_data.data.network_interfaces.operational_status case in (["Dormant", " Down", " NotPresent", " Unknown"]) then form.tag_name set_value "Inactive"
  ```
* **Example** - If the aggregated username field (user.specific\_data.data.username) in an asset contains at least one value that is equivalent to 'sales' or 'marketing', a tag set to 'g2m' is added to the user record.

```
switch [user.specific_data.data.username]
case in (["sales", "marketing"]) then form.tag_name set_value "g2m"
```

## Using the *also* Operator

The **also** operator enables applying dynamic content on multiple action fields in a single dynamic value statement.

* Relevant for 'switch/case' and 'all' statements.

**also** has the syntax:

```
form.field1 set_value "string1" also form.field2 set_value "string2"
```

* In the 'all' statement, the format is:

```
device all then form.field1 set_value [adapter.fieldX] or [adapter.fieldY] also form.field2 set_value [adapter.fieldZ]
```

This means that in all devices, set form.field1 to the value of adapter.fieldX or if empty, to the value of adapter.fieldY. Also, set form.field2 to the value of adapter.fieldZ.

* In the 'switch/case' statement, the format is:

```
switch adapter.fieldX
case starts_with "A" then form.field1 set_value "aaa" also form.field2 set_value "XXX"
```

This means that if the value in adapter.fieldX begins with 'A' then set form.field1 to 'aaa' and also set form.field2 to 'XXX'.

* **Example** -
  The following statement does the following:
  For each device that matches the query, set the tag name (form.tag-name) to "gt 2" and the tag color to green (RGB color #32a852).

```text
device all then form.tag_name set_value "gt 2" also form.color set_value "#32a852" 
```

The following screen shows the results of running the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action with the above statement.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleAlsoRunDrawer.png)

Clicking the **Successful** link displays the  'successful' devices returned from the Enforcement Set query with their tags. The green "gt2" tag is from the current run.

<Image alt="ExampleAlsoSuccessfulDevices" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleAlsoSuccessfulDevices.png" />

Clicking a device on the above screen (in this case, the one with the enclosed tag) opens its Asset Profile. You can click the **Tags** category to see the asset's tags:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleAlsoAssetrofileTag.png)

## Using the *join* Function for Array Fields

The *join* function converts a list (array) into one single string with the items separated by a delimiter. The delimiter can be any character.

**join** has the syntax:

```
join (items, delimiter)
```

* **Example** - For each device, converts the list of vulnerabilities (**device.specific\_data.data.vulnerabilities.vulnerability\_name**) found on the device into a joined string of vulnerabilities separated by a space and comma (vulnerability1, vulnerability2, ..., vulnerabilityN) and places it in the Incident Description field of the ticket.
  ```
  device all then form.incident_description set_value join ([device.specific_data.data.vulnerabilities.vulnerability_name], " ,")
  ```

* **Example** - Join the listed values into one string with the values separated by semicolon and a space.
  ```
  join(["string_1", "string_2"], "; ") 
  ```
  The output will be
  ```
  *string1; string2*.
  ```

## Using the *by\_key* Function for Complex Field Objects

The *by\_key* function accepts a complex field path \[adapter\_complex\_field\_path] as input, and searches in the specified object (field\_to\_compare) of the complex field for a specified string value (by\_value). It then returns the value from a corresponding specified object (field\_to\_pick).

**by\_key** has the syntax:

```
by_key ([adapter_complex_field_path], field_to_compare, by_value, field_to_pick)
```

* **Example** -
  The following statement does the following:
  For each device that matches the query, for all **tag\_key** objects in the AWS Adapter Tags complex field (**device.adapters\_data.aws\_adapter.tags**) that have the string 'ax:state', returns the string in the corresponding **tag\_value** object. It then creates a tag, by concatenating 'the value for the owner is ' with the returned string.

```
device all then form.tag_name set_value concat ("the value for the owner is ", by_key ([device.adapters_data.aws_adapter.tags], "tag_key", "ax:state", "tag_value")) 
```

The following screen shows the results of running the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action with the above statement.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_Tags-Run_History.png)

Clicking the **Successful** link displays the devices returned from the Enforcement Set query. The following screen shows the resulting tags of the 'successful' devices (added using **Edit Columns**).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_by_key_tagged_devices.png)

Clicking a device on the above screen (in this case, the one with the enclosed tag) opens its Asset Profile displaying **All Fields**.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfileAdapterTags.png)

Under **Tables**, you can click the **Adapter Tags** complex field to open its objects arranged in a table. Enclosed under **Tag Key** (key\_to\_search\_by) is ax:state (value\_to\_search). The function returns 'remove' under **Tag Value** (key\_to\_pick).

<Image alt="EC_by_key_Adapter-Tags_table" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_by_key_Adapter-Tags_table.png" />

You can click the Tags category to see the asset's tag:
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EC_by_key_Adapter-Tags.png)

## Using the *filter* Function

The *filter* function filters values from arrays.

The syntax for the function is:

```
filter ([field(Multi-value String)], Operator, Criteria)
```

Where:

* **Operator** - Supported operators are **contains**, **not\_contains**, **gt**, **lt**, and **regex**.

**Example 1** -
The following statement assigns the list field (**form.field\_list.value**) the email addresses that contain 'demo'.

```
device all then form.field_list.value set_value filter ([device.specific_data.data.all_associated_email_addresses], contains, "demo") 
```

Sets **form.field\_list.value** to \["[martha.hicks@demo.local](mailto:martha.hicks@demo.local)", "[wanda.alexander@demo.local](mailto:wanda.alexander@demo.local)"]

**Example 2** -
The following statement assigns the list field (**form.field\_list.value**) the email addresses that contain 'gmail.com'.

```
device all then form.field_list.value set_value filter (["User2@gmail.com", "User1@Axonius.com", "User1@gmail.com"], contains, "gmail.com")
```

Sets **form.field\_list.value** to an array of strings \["[User2@gmail.com](mailto:User2@gmail.com)", "[User1@gmail.com](mailto:User1@gmail.com)"]

## Using the *filter\_by\_key* Function for Complex Field Objects

The **filter\_by\_key** function accepts a complex field path \[**adapter\_complex\_field\_path**] as input, and searches in each object of the complex field if the specified field (**field\_to\_compare**) is equivalent to the specified string value (**by\_value**). From each object with a match, places the value from another specified field (**field\_to\_pick**) into a comma-separated list. This list is returned by this function.

**filter\_by\_key** has the syntax:

```
filter_by_key ([adapter_complex_field_path], field_to_compare, by_value, field_to_pick)
```

**Example** -
The following statement does the following:
For each user that matches the query, for all objects in the **Assigned Applications** complex field (**user.specific\_data.data.nested\_applications**) that have extension type (**user.specific\_data.data.nested\_applications.extension\_type**) equivalent to the string value 'SSO', returns the string in the corresponding **name** field (**user.specific\_data.data.nested\_applications.app\_display\_name**). The name field of each object is added to the tag with comma separation.

```
user all then form.tag_name set_value filter_by_key ([user.specific_data.data.nested_applications],"extension_type","SSO","app_display_name")
```

As seen in the simulation below, the tag is assigned a comma-separated string list.

<Image alt="SimulateFilterBy" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateFilterBy.png" />

The following screen shows the results of running the [**Axonius - Add Tag to Assets**](/docs/add-remove-tag) enforcement action with the above statement.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunResultsAssignedApps.png)

Clicking the **Successful** link displays the 'successful' users returned from the Enforcement Set query with the resulting tags.

<Image alt="AssignedAppsUsers" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignedAppsUsers.png" />

Clicking a user on the above screen opens its Asset Profile. The following screen shows the **Assigned Applications** complex field, with the Application Names that correspond to the SSO extension type.\
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetProfileAssignedApps.png)

You can click the **Tags** list field to view its tag values arranged in a table.

<Image alt="AssignedAppsTags" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssignedAppsTags.png" />

<br />

## Using the *filter\_by\_key\_with\_operator* Function for Complex Field Objects

The **filter\_by\_key\_with\_operator** function accepts a complex field path \[**adapter\_complex\_field\_path**] as input, and searches in each object of the complex field if the result of the specified operator (**operator**) applied to the specified field (**field\_to\_compare**) is equivalent to the specified string value (**by\_value**). The function returns a comma-separated list of the full objects that match the condition.

**filter\_by\_key\_with\_operator** has the syntax:

```
filter_by_key_with_operator ([adapter_complex_field_path], field_to_compare, operator, by_value)
```

**Example** -
The following statement does the following:
For each device that matches the query, for all objects in the **network interfaces** complex field (**device.specific\_data.data.network\_interfaces**) whose **name** field (**device.specific\_data.data.network\_interfaces.name**) contains the string value 'external', returns the entire object. The full object that meets the filter condition is added to the tag, separated by commas.

```
device all then form.tag_name set_value filter_by_key_with_operator ([device.specific_data.data.network_interfaces],"name", contains, "external")
```

<br />

## Using the *filter\_value\_by\_key\_with\_operator* Function for Complex Field Objects

The **filter\_value\_by\_key\_with\_operator** function accepts a complex field path \[**adapter\_complex\_field\_path**] as input, and searches in each object of the complex field if the specified field (**field\_to\_compare**) is equivalent to the specified string value (**by\_value**). From each object with a match, places the value from another specified field (**field\_to\_pick**) into a comma-separated list. This list is returned by this function.

**filter\_value\_by\_key\_with\_operator** has the syntax:

```
filter_value_by_key_with_operator ([adapter_complex_field_path], field_to_compare, operator, by_value, field_to_pick)
```

**Example** -
The following statement does the following:
For each device that matches the query, for all objects in the **network interfaces** complex field (**device.specific\_data.data.network\_interfaces**) whose **name** field (**device.specific\_data.data.network\_interfaces.name**) contains the string value 'external', returns the value in the **name** field that contains the word 'external'. The value in the **name** field of the object that meets the filter condition is added to the tag, spearated by commas. This tag will contain all the network interfaces that contain the word 'external" in their names.

```
device all then form.tag_name set_value filter_value_by_key_with_operator ([device.specific_data.data.network_interfaces],"name", contains, "external", "name")
```

<br />

## Using the *generate\_string* Function

The *generate\_string* function generates a random string based on the specified length and character type.

The syntax for the function is:

```
generate_string (Length, Character Mode)
```

Where:

* **Length** - The total number of characters in the generated string (default: 16).
* **Character Mode** - Determines the types of characters to be included in the string.
  * **alphanumeric** (default) - Generates a string with uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and symbols.
  * **hex** - Generates a string using only hexadecimal characters (0-9 and a-f).
  * **letters** - Generates a string using only uppercase and lowercase letters.
  * **numbers** - Generates a string using only numbers.

**Example** -
The following statement assigns the tag (**form.tag\_name**) a randomly generated 8-character alphanumeric string. For example: 3#r%T9&4

```
user all then form.tag_name set_value generate_string (8, alphanumeric) 
```

## Using the *concat* Function for String Arguments

The *concat* function concatenates string arguments into a single string.

**concat** has the syntax:

```
concat (item1, item2,…, itemN)
```

* **Example**
  When the statement below runs on a user resulting from an Enforcement Set query, the tag name (**form.tag\_name**) is set to the concatenation of the user`s first name (**user.specific_data.data.first_name**) and last name (**user.specific_data.data.last_name**), separated by a space. For example, if a user`s first name is **Frank** and last name is **Smith**, the tag name is set to **Frank Smith**.

```
user all then form.tag_name set_value concat ([user.specific_data.data.first_name]," ",[user.specific_data.data.last_name])
```

* **Example**
  When the statement below runs on a device resulting from an Enforcement Set query, the tag name (**form.tag\_name**) is set to the concatenation of the month (**%m** format) and year (**%Y** format) of the ServiceNow **Last Seen** date (**device.adapters\_data.service\_now\_adapter.last\_seen**), separated by **/**.

```
device all then form.tag_name set_value 
concat ( date_format([device.adapters_data.service_now_adapter.last_seen], "%m"), "/", date_format([device.adapters_data.service_now_adapter.last_seen], "%Y"))
```

For example, when a device has the **Last Seen** value in the following screen, the Tag Name is assigned **12/2023**.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleConcatDateLastSeen.png)

<Image alt="ExampleConcatDateTag" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExampleConcatDateTag.png" />

* **Example**
  When the statement below runs on a device resulting from the Enforcement Set query **JB - Tenable Plugin exists**, a custom field (**form.field\_value**) is added, which contains the concatenation of the plugin id (**device.adapters\_data.tenable\_security\_center\_adapter.plugin\_and\_severities.plugin\_id**) and plugin (**device.adapters\_data.tenable\_security\_center\_adapter.plugin\_and\_severities.plugin**)  .

```
device all then form.field_value set_value concat([device.adapters_data.tenable_security_center_adapter.plugin_and_severities.plugin_id], [device.adapters_data.tenable_security_center_adapter.plugin_and_severities.plugin])
```

* **Example**
  This example shows how you can use nested functions to concatenate a list with a string. The following statement concatenates a list flattened using *join* with the contents of a string field and character strings.

In the statement below:

1. **join** flattens the **device.field.array.1** array into its elements with a space and comma (' ,') delimiter between each two elements.
2. Then, the following are concatenated: the joined string, 'and', the string in **device.field.mystring**, and ' comment'.
3. The concatenated string is placed in the description of the incident (**form.incident\_description**).

   ```
    device all then form.incident_description set_value 
    concat (join ([device.field.array.1], " ,"), " and", [device.field.mystring]," comment")
   ```

   For an asset with array components (a, b, c, d) and mystring = 'mystring'. this statement generates a (single string) value:
   *a ,b ,c , d and mystring comment*

## Using the *date\_format* Function for String Manipulations

The *date\_format* function formats the date and time according to the specified format.

**date\_format** has the syntax:

```
date_format ([adapter.field], "format")
```

Where format can be any of the following combinations:

* **%Y** - Year (four digits)
* **%m** - Month (01-12)
* **%d** - Day of the month (01-31)
* **%H** - Hour (00-23)
* **%M** - Minute (00-59)
* **%S** - Second (00-60)
* **%L** - Millisecond (000-999)
* **%j** - Day of the year (001-366)
* **%w** - Day of the week (0-6, Sunday is 0)
* **%a** - Abbreviated weekday name (Sun, Mon, Tue, etc.)
* **%A** - Full weekday name (Sunday, Monday, Tuesday, etc.)
* **%Z** - Timezone (e.g., EST, PST, UTC)

**Note:** **M** = minute; **m** = month

<Callout icon="📘" theme="info">
  Note

  * **M** = minute; **m** = month

  * The *date\_format* function does not work with lists (arrays). In order for this function to work when used on list fields, add a function that selects one value from the list, for example, the *max* function.
    date\_format ((max(\[adapter.field]), "format")
</Callout>

* **Example** - Sets the value of the tag name (**form.tag\_name**) to the fetch time (**device.specific\_data.data.first\_fetch\_time**), formatted as YYYY-mm. For example, **2024-01**.
  ```
   device all then form.tag_name set_value date_format([device.specific_data.data.first_fetch_time], "%Y-%m")
  ```
* **Example** - Sets the value of the current date and time (**form.field\_date.now**) to the current date and time (**now()**), formatted as YYYY-mm HH-MM-SS. For example, **2024-01 21-12-58**.

```
 device all then form.field_date.now set_value date_format(now(), "%Y-%m %H-%M-%S")
```

## Using the *regex\_extract* Function

The *regex\_extract* function checks if a part of a specified field's string value matches the string in regex\_expression, and if it does, extracts from the field that part of the string so that it can be used to populate Custom Fields or Tags.

* If index is not specified, it captures the first occurrence of the string in the specified field.
* If index is specified (optional), it extracts the occurrence of the string specified by the index (**0** is first occurrence, **1** is second, and so on).

**regex\_extract** has the syntax:

```
regex_extract ([field], "regex_expression", index)
```

* **Example** (without index) - In the **Associated Hostname** string field (**device.specific\_data.data.associated\_hostname**), find the first substring (as there is no index) matching two alphabetic characters followed by three digits, and if it exists, extract and place that string in the tag action field (**form.tag\_name**).

If the string in the **Associated Hostname** string field is
*hostname-nat900-AB123-devinstance*, the first match *at900* is extracted and placed in the tag.

```
device all then form.tag_name  set_value regex_extract ([device.specific_data.data.associated_hostname], "[a-zA-Z]{2}\d{3})")
```

* **Example** (with index) - In the **Associated Hostname** string field (**device.specific\_data.data.associated\_hostname**), find the second substring (index = **1**) matching two alphabetic characters followed by three digits, and if it exists, extract and place that string in the tag action field (**form.tag\_name**).

If the string in the **Associated Hostname** string field is
*hostname-nat900-AB123-devinstance*, the second match *AB123* is extracted and placed in the tag.

```
device all then form.tag_name set_value regex_extract ([device.specific_data.data.associated_hostname], "[a-zA-Z]{2}\d{3})",1)
```

## Using the *regex\_replace* Function

The *regex\_replace* function checks if a specified field's string value matches the pattern in regex\_expression, and if it does, replaces it with the string in replace\_value.

<Callout icon="📘" theme="info">
  Note

  replace\_value can also be a function that returns a string.
</Callout>

**regex\_replace** has the syntax:

```
regex_replace ([field], regex_expression, replace_value)
```

* **Example** - If the **regex\_replace** function finds one or more digits ("\d+") in the **device.labels** field, it replaces the digits with "Catlg".

```
 regex_replace ([device.labels], "\d+", "Catlg") 
```

## Using the *relation* Function

The *relation* function fetches data from a field in a related asset (i.e., from an asset related to the Enforcement Action asset via a Relationship). Learn more about [Relationships](/docs/exploring-connections-and-asset-relationships).

**relation** has the syntax:

```
[relation.[asset type]("[relationship name] ").[adapter.field]]
```

* **Example** - A Custom Field (**form.field\_value**) is added to the device asset. The value of this field is the value of the Relationship field (**specific\_data.data.user\_manager\_mail**) taken from the related asset (**User**) that last used the device (Relationship: **Last used by**).

```
device all then form.field_value set_value [relation.user("Last used by").specific_data.data.user_manager_mail]
```

## Using the *split* Function

The *split* function splits the string in the indicated field at the specified delimiter, and creates a list of the separate strings separated by a comma.

**split** has the syntax:

```
split([field], delimiter)
```

* **Example** - A string is split at the delimiter character $.

```
split("My$Cool$String", "$") 
```

The output is a list:

```
["My", "Cool", "String"]
```

## Using the *count* Function

The count function returns the number of values in a list field.

**count** has the syntax:

```
count([field])
```

* **Example** - Counts the number of CISA vulnerabilities in the **device.adapters\_data.gui.cisa\_vulnerabilities** list field and places the number in **form.field\_number**.

```
device all then form.field_number set_value count([device.adapters_data.gui.cisa_vulnerabilities])
```

## Using the *starts\_with* Function

The *starts\_with* function checks if a specified string appears at the very beginning of a field.

* For string fields - It returns *True* if the field's value begins with the string you specify.
* For lists -  It returns *True* if at least one item within the list starts with the specified string.

**starts\_with** has the syntax:

```
starts_with ("string")
```

* **Example** - You want to quickly identify all devices that have 'Google' software installed on them. This is useful for sending emails about devices running specific software.
  The statement below: If one of a device`s installed software names (**device.specific_data.data.installed_software.name**) begins with `Google`, automatically set the email subject line (**form.mailSubject**) to `Installed Software: Google'.

```
switch device.specific_data.data.installed_software.name case starts_with ("Google") then form.mailSubject set_value "Installed Software: Google" 
```

## Using the *substring* Function

The *substring* function returns a substring of the field value, beginning from the specified start position in the string and for the length specified.

**substring** has the syntax:

```
substring([adapter.field], start_index, length)
```

* **Example** - For devices with host names (**device.specific\_data.data.hostname**) that all begin with an up to 4-character prefix, sets the value of the **form.field\_value** list field to the host name without its prefix, i.e., removes the first four characters of the hostname. The substring can be up to a length of 50 characters.

```
device all then form.field_value set_value 
substring( [device.specific_data.data.hostname],5,50)
```

## Using the *title\_case* Function

The *title\_case* function converts an input string to title case, capitalizing the first letter of each word. It doesn't change numbers or special symbols.

**title\_case** has the syntax:

```
title_case ([adapter.field])
```

* **Example** - You want to send an email for each Security Finding that matches a query (such as all remediation vulnerabilities). The email subject should include the CVE ID and a title-cased version of the CVE description. The statement below achieves this by joining (using **concat**) the following elements:
  * The text **Vulnerability Remediation Request for:**
  * The CVE ID (\[**vulnerability.specific\_data.data.id**])
  * A space
  * The title-cased CVE description (**title\_case \[vulnerability.specific\_data.data.cve\_description**])

```
vulnerability all then form.mailSubject set_value concat ("Vulnerability Remediation Request for: ", [vulnerability.specific_data.data.id], " ", title_case ( [vulnerability.specific_data.data.cve_description]))

```

## Using the *to\_date* Function

The *to\_date* function converts the results of a date calculation (epoch date in milliseconds) to a date in human-readable Date format.

**to\_date** has the syntax:

```
to_date(number of milliseconds)
```

* **Example** - If the asset has a warranty date (**device.adapters\_data.gui.custom\_warranty\_date**), sets the value of (**form.field\_date.now**) to a year later by adding 31536000000 microseconds (365 days) to the warranty date, and then converting the resulting epoch date to a human readable Date format.

```
switch device.adapters_data.gui.custom_warranty_date case field_exists
then form.field_date.now set_value to_date(add([device.adapters_data.gui.custom_warranty_date], 31536000000))
```

## Using the *to\_table*  Function

The **to\_table** function converts a complex field (list of objects) into a formatted HTML table. This is useful for presenting complex data in a clear, easy-to-read format within a text field, such as an incident description (example below).

**to\_table** has the syntax:

```
to_table ([adapter.field], column definitions)
```

Where:

* **adapter.field** - The complex field (list of objects) to be converted.
* **column definitions** - A list that specifies the headers and data fields for each column. Each object in this list requires a header (string) and a field (string)
* **Example** - This example uses the *to\_table* function to retrieve a list of installed software (**device.specific\_data.data.installed\_software**) and embed it as a formatted HTML table into the incident description field (**form.incident\_description**). The table will have two columns 'SW UID' and 'Name', with data pulled from the 'sw\_uid' and 'name' sub-fields within the installed\_software list.

```
device all then form.incident_description set_value to_table([device.specific_data.data.installed_software], [(header: "SW UID", field: "sw_uid"), (header: "Name", field: "name")])
```

**Verify your output:** In **Simulate** mode, click **to\_table** to see a preview of the generated table. This helps you instantly verify the output before saving your configuration.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HTMLTablePrevEx2.png)

## Using the *to\_int* Function

The *to\_int* function converts a string or float value to an integer value.

**to\_int** has the syntax:

```
to_int ([adapter.field])
```

* **Example** - The maximum value of **CPUs: Threads in Core** (**device.specific\_data.data.cpus.cores\_thread**) is calculated (using the **max** function) and the result is returned as a Float value. The **to\_int** function then converts the **max** Float value to an Integer value and places it in the Enforcement Action Custom Field value (**form.field\_value**; string). For example, if the max returned is 14.0, it is converted to 14.

```
device all then form.field_value set_value to_int (max ([device.specific_data.data.cpus.cores_thread]))
```

## Using the *to\_lower* Function

The to\_lower function converts a string field to lower case.

**to\_lower** has the syntax:

```
to_lower([field])
```

* **Example** - Sets the tag name value (**form.tag\_name**) to the tag source (**device.specific\_data.data.tags.tag\_source**) in lower case.

```
device all then form.tag_name set_value to_lower([device.specific_data.data.tags.tag_source])
```

## Using the *to\_upper*  Function

The to\_upper function converts a string field to upper case.

**to\_upper** has the syntax:

```
to_upper([field])
```

* **Example** - Sets the tag name value (**form.tag\_name**) to the ID (**device.specific\_data.data.id**) in device.specific\_data.data.id case.

```
device all then form.tag_name set_value to_upper([device.specific_data.data.id])
```

## Using the *unique* Function for Array Fields

The *unique* function removes all duplicate elements in the list (array) and keeps only the unique values.

**unique** has the syntax:

```
unique ([field])
```

* **Example** - For each device, removes the duplicate hostnames in the list field (**device.specific\_data.data.hostname**) and leaves only the unique hostnames in **form.field\_list.value**.
  ```
  device all then form.field_list.value set_value unique ([device.specific_data.data.hostname])
  ```

* **Example** - For each device, counts the number of unique hostnames in the **device.specific\_data.data.hostname** list field and places the number in **form.field\_integer**.

```
device all then form.field_integer set_value count (unique([device.specific_data.data.hostname]))
```

## Applying the *unique* Function on a Nested Function

The *unique* function can be applied on a nested function to return the unique results of the nested function.

**unique** has the syntax:

```
unique (nested function)
```

* **Example** - Ideally, each device should be loaded with one version only of each installed software application. For each device, the following statement counts the number of unique major/minor versions of installed software in the **device.specific\_data.data.installed\_software.major\_minor\_version** array (list) field. If the number of unique versions is greater than **1**, places the string *Needs remediation* in the **form.field\_value** string field.
  For example:
  List of major/minor versions in the device: `{1.0, 2.0, 3.0, 3.0, 3.0, 4.0, 5.0}`
  Count: 7
  Unique count: 5

```
switch unique(count([device.specific_data.data.installed_software.major_minor_version]))
case gt(1) then form.field_value set_value "Needs remediation"
```

## Using the *field\_exists* Operator

The **field\_exists** operator tests whether the specified field exists.

The following code tests whether the field **device.specific\_data.data.name** exists. If true, sets the value of **form.field\_value** to 'exists'.

```
switch device.specific_data.data.name
case field_exists then form.field_value set_value "exists"
```

## Using the *field\_not\_exists*  Operator

The **field\_not\_exists** operator tests whether the specified field does not exist (i.e., is empty).

<Callout icon="📘" theme="info">
  Note

  The **field\_not\_exists** operator should be used only when empty values are checked and are not thrown out of aggregations.
</Callout>

The following code assigns a value to **form.field\_value** based on the **device.specific\_data.data.name** field value:

* If the **device.specific\_data.data.name** field contains 'X', **form.field\_value** is set to 'aaa'.
* If the **device.specific\_data.data.name** field contains 'Y', **form.field\_value** is set to 'bbb'.
* If the **device.specific\_data.data.name** field does not exist (i.e., is empty), **form.field\_value** is set to 'ccc'.

<Callout icon="📘" theme="info">
  Note

  Conditions are checked in the order that they appear in the statement. Once a condition is met, the remaining conditions are not checked.
</Callout>

```
switch device.specific_data.data.name
case contains ("X") then form.field_value set_value "aaa"
case contains ("Y") then form.field_value set_value "bbb" 
case field_not_exists then form.field_value set_value "ccc"
```

## Using the *in\_net* Operator

The **in\_net** operator tests if a subnet range in adapter.field (list field) or a single subnet in adapter.field (string field) is within the specified range.

**in\_net** has the syntax:

```
in_net (subnet field)
```

The following code tests whether the subnet range in the list field **device.specific\_data.data.network\_interfaces.ips** is within any of the following ranges:

* 10.0.2.0/8
  * A CIDR notation that represents a network where the first 8 bits of the IP address define the network.
  * Encompasses all IP address from 10.0.0.0 to 10.255.255.255.
* 10.0.2.7/16
  * A CIDR notation that represents a network where the first 16 bits of the IP address define the network.
  * Encompasses all IP address from 10.0.0.0 to 10.0.255.255.
* 12.3.4.1/24
  * A CIDR notation that represents a network where the first 24 bits of the IP address define the network.
  * Encompasses all IP address from 12.3.4.0 to 12.3.4.255.

If the subnet range is within the specified range, sets the value of the tag name (**form.tag\_name**) to 'in network!'.

```
switch [device.specific_data.data.network_interfaces.ips]
case in_net("10.0.2.0/8,10.0.2.7/16,12.3.4.1/24") then form.tag_name set_value "in network!"
```

## Using the *not\_in\_net* Operator

The **not\_in\_net** operator tests if a subnet range in adapter.field (list field) or a single subnet in adapter.field (string field) is not within the specified range.

**not\_in\_net** has the syntax:

```
not_in_net (subnet field)
```

The following code tests whether the subnet range in the list field **device.specific\_data.data.network\_interfaces.ips** is not within any of the following IP address ranges:

* 10.0.2.0/8
* 10.0.2.7/16
* 12.3.4.1/24

If the subnet range is not within the specified range, sets the value of the tag name (**form.tag\_name**) to 'not in network!'.

```
switch [device.specific_data.data.network_interfaces.ips]
case not_in_net("10.0.2.0/8,10.0.2.7/16,12.3.4.1/24") then form.tag_name set_value "not in network!"
```

## Using *lt* in Switch Statements

The **lt** operator (less than) compares numeric field 1 to numeric field 2 or to a number, and if numeric field 1 is smaller, performs the 'then' clause.

* **Example** - The following example compares two device fields fetched from the adapter.
  * Compares the value of **custom\_intest** to the value of **custom\_intest2**.
  * If **custom\_intest** `<` **custom\_intest2**, then sets the tag-name field on the form to "failure".

```
switch device.adapters_data.gui.custom_intest
case lt ([device.adapters_data.gui.custom_intest2]) then form.tag_name set_value "failure"
```

## Using *gt* in Switch Statements

The **gt** operator (greater than) compares numeric field 1 to numeric field 2 or to a number, and if numeric field 1 is greater, performs the 'then' clause.

* **Example** - The following example compares two device fields fetched from the adapter.
  * Compares the value of **custom\_intest** to the value of **custom\_intest2**.
  * If **custom\_intest** `>` **custom\_intest2**, then set the tag-name field on the form to 'success'.

```
switch device.adapters_data.gui.custom_intest
case gt ([device.adapters_data.gui.custom_intest2]) then form.tag_name set_value "success"
```

## Using the Wildcard Character in Statements

You can use the wildcard character \* in dynamic value statements.

## Using Operators with Arrays (Lists)

When testing an array with any of the operators below, if at least one value matches, the result is TRUE.

This works for the following operators:

* contains
* not\_contains
* in
* not\_in
* starts\_with
* not\_starts\_with (no matches)
* ends\_with
* not\_ends\_with
* gt
* lt

## Nesting Functions

You can nest functions (functions within functions) when writing dynamic value statements.

* **Example** - The following statement includes a *sum* function within the *concat* function.

  * sum() - Adds the values in the **device.specific\_data.data.field** array.
  * concat("sum is", sum()) - Adds 'sum is' before the calculated sum sum().
  * set\_value concat("sum is", sum()) - Sets the tag name on the form (**form.tag\_name**) to 'sum is' followed by the calculated sum of the list values. For example: "sum is 124".

  ```
  device all then form.tag_name set_value concat("sum is", sum([device.specific_data.data.field]))
  ```