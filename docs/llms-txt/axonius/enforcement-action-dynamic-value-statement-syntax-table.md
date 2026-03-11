# Source: https://docs.axonius.com/docs/enforcement-action-dynamic-value-statement-syntax-table.md

# Enforcement Action Dynamic Value Statement Syntax Table

The following table describes the syntax of all Dynamic Value statement (also referred to as "statement") types and the available functions and operators.

The syntax in the table includes:

* **\[asset type]** - The asset type on which to apply the statement.
* **form.field** - A field in the selected Enforcement Action Configuration dialog.
* **adapter.field** - A field from the selected adapter.
* **itemN** - A value or single value field (number or string type).

In a Dynamic Value statement, form.field and adapter.field must be of the same field type (e.g., both number or both string).

Learn some [useful tips and tricks for working with dynamic value statements](/docs/useful-tips-and-tricks).

See [Dynamic Value Statement Examples and Use Cases](/docs/condition-statement-examples-and-use-cases) for some detailed examples.

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Element
      </th>

      <th>
        Type
      </th>

      <th>
        Syntax
      </th>

      <th>
        Notes
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        all
      </td>

      <td>
        Statement
      </td>

      <td>
        \[asset type] all then form.field set\_value
      </td>

      <td>
        Examples: device all then form.field set\_value user all then form.field set\_value vulnerability all then form.field set\_value software all then form.field set\_value See **set\_value** below for options.
      </td>
    </tr>

    <tr>
      <td>
        switch/case
      </td>

      <td>
        Statement
      </td>

      <td>
        switch \[adapter.field] case operator then form.field set\_value
      </td>

      <td>
        Operators support functions. A value can be used instead of an operator.
      </td>
    </tr>

    <tr>
      <td>
        add
      </td>

      <td>
        Function
      </td>

      <td>
        add (item1, item2,…, itemN)
      </td>

      <td>
        Supports a list of number arguments (values and/or single value number type fields). Adds the number arguments in the list.
      </td>
    </tr>

    <tr>
      <td>
        array
      </td>

      <td>
        Function
      </td>

      <td>
        array (\[adapter.field1],\[adapter.field2],..., \[adapter.fieldN])
      </td>

      <td>
        Creates an array of multiple fields. Each field input to the function can be an adapter field or text string. The array resulting from this function can be written into a single multi-value custom field (of type array (list)).
      </td>
    </tr>

    <tr>
      <td>
        average
      </td>

      <td>
        Function
      </td>

      <td>
        average (\[adapter.field])
      </td>

      <td>
        Returns the average of the number values in the list. The field type of adapter.field is a list (array) of numbers.
      </td>
    </tr>

    <tr>
      <td>
        by\_key
      </td>

      <td>
        Function
      </td>

      <td>
        by\_key (\[adapter\_complex\_field\_path], field\_to\_compare, by\_value, field\_to\_pick)
      </td>

      <td>
        **adapter\_complex\_field\_path** - The path to the complex field.\
        **field\_to\_compare** - The field in the object to compare with by\_value.\
        **by\_value** - The string value to match against the field\_to\_compare.\
        **field\_to\_pick** - The field value from the first matched object.The function checks each object of the complex field

        <br />

        (\[**adapter\_complex\_field\_path**]), checks each object until it finds a match between the specified field (**field\_to\_compare**) and the specified value (**by\_value**). The function returns the value in another specified field (**field\_to\_pick**) from that first object with a match.\
        **Notes:**\
        This function supports only an exact comparison. It does not support a comparison between one value from a list field (field\_to\_compare) and a by\_value.\
        This function does not support aggregated complex fields (which are in fact arrays of complex fields).\
        For example, *device all then form.tag\_name set\_value by\_key (\[device.specific\_data.data.plugin\_and\_severities], "plugin\_id", " 10395", "severity")* does not work, as **Plugins Information** (**device.specific\_data.data.plugin\_and\_severities**) is not supported as it is an aggregated complex field, which combines several similar adapter fields into an aggregated one. In order for this function to work, use an adapter specific field, such as Tenable IO **Plugins Information** (**device.adapters\_data.tenable\_io\_adapter.plugin\_and\_severities**).
      </td>
    </tr>

    <tr>
      <td />

      <td />

      <td />

      <td />
    </tr>

    <tr>
      <td>
        concat
      </td>

      <td>
        Function
      </td>

      <td>
        concat (item1, item2,…, itemN)
      </td>

      <td>
        Supports a list of string arguments (values and/or single value string type fields).\
        Concatenates the string arguments in the list.
      </td>
    </tr>

    <tr>
      <td>
        concat\_array
      </td>

      <td>
        Function
      </td>

      <td>
        concat\_array (\[adapter.field], \[adapter.field],...,\[adapter.field])
      </td>

      <td>
        Joins one or more arrays into a single array.\
        For example: **concat\_array** (list1 `{a, b, c}`, list2 \[d, e, f, g]) --> \[a, b, c, d, e, f, g]
      </td>
    </tr>

    <tr>
      <td>
        concat\_prefix
      </td>

      <td>
        Function
      </td>

      <td>
        concat\_prefix ("prefix", \[adapter.field])
      </td>

      <td>
        Appends a prefix to each field value in a list (array). The field type of adapter.field is a list (array) of values.\
        For example:**concat\_prefix** ("prefix", \[adapter.field]) --> \[prefixfield1, prefixfield2]
      </td>
    </tr>

    <tr>
      <td>
        count
      </td>

      <td>
        Function
      </td>

      <td>
        count (\[adapter.field])
      </td>

      <td>
        Counts and returns the number of values in a list. The field type of adapter.field is a list (array) of numbers.
      </td>
    </tr>

    <tr>
      <td>
        date\_format
      </td>

      <td>
        Function
      </td>

      <td>
        date\_format (\[adapter.field], "format")
      </td>

      <td>
        Formats a date field using any of the following formats for the date and time:\
        \*\*%Y -\*\*Year (four digits)\
        **%m -** Month (01-12)\
        **%d -** Day of the month (01-31)\
        **%H -** Hour (00-23)\
        **%M -** Minute (00-59)\
        **%S** - Second (00-60)\
        **%L -** Millisecond (000-999)\
        **%j -** Day of the year (001-366)\
        **%w -** Day of the week (0-6, Sunday is 0)\
        **%a -** Abbreviated weekday name (Sun, Mon, Tue, etc.)\
        **%A -** Full weekday name (Sunday, Monday, Tuesday, etc.)\
        **%Z -** Timezone (e.g., EST, PST, UTC)\
        **Note:**\
        **M** = minute; **m** = month\
        The date\_format function does not work with lists (arrays). In order for this function to work when used on list fields, add a function that selects one value from the list, for example, date\_format ((max(\[adapter.field]), "format")
      </td>
    </tr>

    <tr>
      <td>
        divide
      </td>

      <td>
        Function
      </td>

      <td>
        divide (item1, item2,…, itemN)
      </td>

      <td>
        Supports a list of number arguments (values and/or single value number type fields). Divides the number values in the list from left to right.
      </td>
    </tr>

    <tr>
      <td>
        filter
      </td>

      <td>
        Function
      </td>

      <td>
        filter (\[field], Operator, Criteria)
      </td>

      <td>
        The **filter** function filters values from single values or arrays (lists). This gives the flexibility to configure a filter within a workflow without being limited to a predefined saved query.\
        The function has the following parameters:\
        **field**- A Single Value String or a Multiple Values String field.\
        **Operator**- The comparison to be applied. Supported operators are **contains**, **not\_contains**, **gt** (greater than), **lt** (less than), and **regex**.\
        It is possible to combine multiple operators and criteria.\
        **Example**: **filter** (\[1,5,3], gt, "2") returns the output: \[5,3]
      </td>
    </tr>

    <tr>
      <td>
        filter\_by\_key
      </td>

      <td>
        Function
      </td>

      <td>
        filter\_by\_key (\[adapter\_complex\_field\_path], field\_to\_compare, by\_value, field\_to\_pick)
      </td>

      <td>
        The **filter\_by\_key** function iterates through every object in the specified complex field path. In each object, it compares the **field\_to\_compare** value to **by\_value**. It extracts the value from another specified object field (**field\_to\_pick**) from each matched object and returns them as a comma-separated list.

        * **adapter\_complex\_field\_path** - The path to the complex field being filtered.
        * **field\_to\_compare** - The field in the object to compare with **by\_value**.
        * **by\_value** - The string value to match against the value in **field\_to\_compare**.
        * **field\_to\_pick** - The field whose values are added to the resulting list for all matched objects.

        **Note:**

        * This function fetches a field from each object in the complex field with a matching field value, as opposed to the **by\_key** function, which only fetches a field from the first object with a match.
        * This function supports only an exact comparison. It does not support a comparison between a single value from a list field (field\_to\_compare) and a by\_value.
        * This function does not support aggregated complex fields (which are, in fact, arrays of complex fields). See the example in the by\_key function above.
      </td>
    </tr>

    <tr>
      <td>
        filter\_by\_key\_with\_operator
      </td>

      <td>
        Function
      </td>

      <td>
        filter\_by\_key\_with\_operator (\[adapter\_complex\_field\_path], field\_to\_compare, operator, by\_value)
      </td>

      <td>
        The **filter\_by\_key\_with\_operator** function iterates through every object in the specified complex field path. It checks each object against a condition defined by the **field\_to\_compare**, **operator**, and **by\_value**. It returns a comma-separated list of the **full objects** that match the condition.

        * **adapter\_complex\_field\_path** - The path to the complex field being filtered.
        * **field\_to\_compare** - The field in the object on which the operator is applied, and the result is then compared with by\_value.
        * **operator** - The operator applied to **field\_to\_compare**. Supported operators include:
          * **contains**,
            **not\_contains** - Checks for a substring in a string or an item in an array (list). For example, it checks if Tags contains VIP.
          * **greater\_than**, **lower\_than** - Numerical comparison. For example, check if Priority is greater than 5.
          * **regex** - Advanced pattern matching. For example, check if Name matches a specific email format.
          * **equals**, **not\_equals** - Exact match comparison. For example, check if Status equals Active.
        * **by\_value** - The string value to match against the result of applying the **operator** on **field\_to\_compare**.

        **Note:** See notes in the **filter\_by\_key** function above.
      </td>
    </tr>

    <tr>
      <td>
        filter\_value\_by\_key\_with\_operator
      </td>

      <td>
        Function
      </td>

      <td>
        filter\_value\_by\_key\_with\_operator (\[adapter\_complex\_field\_path], field\_to\_compare, operator, by\_value, field\_to\_pick)
      </td>

      <td>
        The **filter\_value\_by\_key\_with\_operator** function iterates through every object in the specified complex field path. It checks each object against a condition defined by the **field\_to\_compare**, **operator**, and **by\_value**.  It extracts the value from another specified object field (**field\_to\_pick**) from each matched object and returns them as a comma-separated list.

        * **adapter\_complex\_field\_path** - The path to the complex field being filtered.
        * **field\_to\_compare** - The field in the object on which the operator is applied. The result is then compared with **by\_value**.
        * **operator** - The operator applied to **field\_to\_compare**. See supported operators in **filter\_by\_key\_with\_operator** above
        * **by\_value** - The string value to match against the result of applying the operator to **field\_to\_compare**.
        * **field\_to\_pick** - The field whose values are added to the resulting list for all matched objects.

        **Note:** See notes in the **filter\_by\_key** function above.
      </td>
    </tr>

    <tr>
      <td>
        generate\_string
      </td>

      <td>
        Function
      </td>

      <td>
        generate\_string (Length, Character Mode)
      </td>

      <td>
        The **generate\_string** function creates secure, random strings of a specified length and character composition. This function is useful for generating unique identifiers, temporary passwords, security tokens, or other security-related strings directly within an automation workflow. The function has the following parameters:\
        **Length** - The total number of characters in the generated string (default: 16).\
        **Character Mode**- Determines the types of characters included in the string.\
        **alphanumeric** (default) - Generates a string composed of uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9), and symbols. Example output: mYp@$$wOrd123\
        **hex** - Generates a string using only hexadecimal characters (0-9 and a-f). Each pair of characters (e.g., "4b") can be converted to a byte (8 bits) of binary data. Example output: 4b7a9c3f2e1d6a4b (a sequence of 16 hexadecimal characters).\
        **letters**- Generates a string using only uppercase and lowercase letters. Example output: AvsgYjdnV\
        **numbers**- Generates a string using only numbers. Example output: 673913487
      </td>
    </tr>

    <tr>
      <td>
        join
      </td>

      <td>
        Function
      </td>

      <td>
        join (\[adapter.field], delimiter)
      </td>

      <td>
        Converts/flattens a list (array) into a single string of values separated by a delimiter.
      </td>
    </tr>

    <tr>
      <td>
        max
      </td>

      <td>
        Function
      </td>

      <td>
        max (\[adapter.field]) max (item1, item2,…, itemN)
      </td>

      <td>
        Returns the highest number value in the list. The field type of adapter.field is a list (array) of numbers.
      </td>
    </tr>

    <tr>
      <td>
        min
      </td>

      <td>
        Function
      </td>

      <td>
        min (\[adapter.field]) min (item1, item2,…, itemN)
      </td>

      <td>
        Returns the lowest number value in the list. The field type of adapter.field is a list (array) of numbers.
      </td>
    </tr>

    <tr>
      <td>
        multiply
      </td>

      <td>
        Function
      </td>

      <td>
        multiply (item1, item2,…, itemN)
      </td>

      <td>
        Supports a list of number arguments (values and/or single value number type fields). Multiplies the number values in the list.
      </td>
    </tr>

    <tr>
      <td>
        multiply\_array\_values
      </td>

      <td>
        Function
      </td>

      <td>
        multiply\_array\_values (value1, value2,…, value3)
      </td>

      <td>
        Multiplies all numerical values provided in the list of arguments by each other.

        * Supports an array (list) of string arguments (string1, string2, etc.).
        * Automatically converts all string arguments to their numerical equivalent (Integer or Float) before performing the multiplication.
        * Returns the product of all numerical values. Returns Null if the array of arguments is empty.
      </td>
    </tr>

    <tr>
      <td>
        now
      </td>

      <td>
        Function
      </td>

      <td>
        now ()
      </td>

      <td>
        Returns today's date and time formatted YYYY-mm-dd HH:MM:SS. For example: 2023-08-22 10:03:04
      </td>
    </tr>

    <tr>
      <td>
        regex\_extract
      </td>

      <td>
        Function
      </td>

      <td>
        regex\_extract(\[adapter.field], "regex\_expression", index)
      </td>

      <td>
        The Regular Expression function **regex\_extract** extracts from adapter.field the string that matches regex\_expression so that it can be used to populate Custom Fields or Tags. If **index** is not specified, it captures the first occurrence of the string in adapter.field. If **index** is specified (optional), it extracts the occurrence of the string specified by the index (**0**is first occurrence, **1 i**s second, and so on).\
        Example: **device all then form.field\_value set\_value regex\_extract(\[device.specific\_data.data.name],"(\[a-zA-Z]`{2}`\d`{3}`)",1)**
      </td>
    </tr>

    <tr>
      <td>
        regex\_replace
      </td>

      <td>
        Function
      </td>

      <td>
        regex\_replace(\[adapter.field], regex\_expression, replace\_value)
      </td>

      <td>
        The **regex\_replace** function returns the string value in adapter.field, and replaces the part of the string that matches regex\_expression with the value in replace\_value. Note that replace\_value can also be a function that returns a string. Example: device all then form.tag\_name set\_value regex\_replace (\[device.specific\_data.data.name], "(.\*?)-", "banana")
      </td>
    </tr>

    <tr>
      <td>
        relation
      </td>

      <td>
        Function
      </td>

      <td>
        \[relation.\[asset type]\("\[relationship name] ").\[adapter.field]]
      </td>

      <td>
        The  **relation** function fetches data from a field in a related asset (i.e., an asset that is related to the Action Center action asset via a Relationship). For example, when running an action on a ticket, it is possible to retrieve data from an associated user based on a defined ticket-user Relationship.\
        **\[asset type]** - The related asset type to pull data from.\
        **\[relationship name]** - The name of the Relationship defined in the system. Learn more about [Relationships](/docs/exploring-connections-and-asset-relationships).\
        **\[adapter.field]** - The name of the field in the related asset. You can retrieve the entire Relationship field name in the format *relation.asset\_type("relationship\_name").adapter\_field* via the **Relationship Fields** tab in the [Syntax Helper](/docs/using-the-syntax-helper) and then enclose it in \[] . For example, *relation.disk("Has").specific\_data.data.asset\_type* This function is supported by the [Dynamic Value Statement Wizard](/docs/using-the-dynamic-value-statement-wizard).
      </td>
    </tr>

    <tr>
      <td>
        split
      </td>

      <td>
        Function
      </td>

      <td>
        split(\[adapter.field], delimiter)
      </td>

      <td>
        Splits the string (in adapter.field) at the delimiter character and creates a list of the separate strings separated by commas.
      </td>
    </tr>

    <tr>
      <td>
        substring
      </td>

      <td>
        Function (string manipulation)
      </td>

      <td>
        substring(\[adapter.field], start\_index, length)
      </td>

      <td>
        Returns a substring of the field value, beginning from the specified start position in the string for the length specified. For example: substring('firstmiddlelast', 6, 3) = mid
      </td>
    </tr>

    <tr>
      <td>
        subtract
      </td>

      <td>
        Function
      </td>

      <td>
        subtract(item1, item2)
      </td>

      <td>
        Returns the result of subtracting item2 from item1. Supports two numbers (typed or values from fields) or two date-time fields. When subtracting two date-time fields, the result is the number of days with one decimal point. For example: 2.3\
        **Note:** This function expects exactly two numbers or dates. When using list (array) fields in the subtraction, it is recommended to add **min** or **max** functions so that the subtract is done on single value fields. Otherwise, if a list (array) field is used in the function instead of a single value field, although the syntax validates successfully, the function fails and the action field in all assets is set to the fallback static value.
      </td>
    </tr>

    <tr>
      <td>
        sum
      </td>

      <td>
        Function
      </td>

      <td>
        sum (\[adapter.field])
      </td>

      <td>
        Returns the sum of all the number values in the list. The field type of adapter.field is a list (array) of numbers.
      </td>
    </tr>

    <tr>
      <td>
        title\_case
      </td>

      <td>
        Function
      </td>

      <td>
        title\_case (\[adapter.field])
      </td>

      <td>
        Converts the input string to title case.

        * Capitalizes the first letter of each word.

          Does not alter numeric characters or special symbols.

          If a word begins with a number or symbol, the first letter after that number or symbol is capitalized.

          Example: \*user all then form.mailSubject set*value title\_case(\[user.specific\_data.data.username])\*Input:* john doe\_123-example\_Output: *John Doe\_123-Example*
      </td>
    </tr>

    <tr>
      <td>
        to\_date
      </td>

      <td>
        Function
      </td>

      <td>
        to\_date (number of milliseconds)
      </td>

      <td>
        Converts the results of a date calculation (epoch date in milliseconds) to a date in human-readable Date format. For example: *device all then form.field\_date.now set\_value to\_date (add(now(),2592000000))* sets the date to 30 days (=2592000000 milliseconds) from the current date.\
        **Note:** When you create a Dynamic Value Statement for adding a custom date field, ensure to use**form.field\_date.specific** with **Date type** set to *Specific date*, as a dynamic date can be written only to this type of Date field.\
        Do not use **form.field\_date.now** or a field with **Date type** set to *Now*, as this type of field cannot accept dynamic input, and regardless of the statement, its value is always the action runtime.
      </td>
    </tr>

    <tr>
      <td>
        to\_int
      </td>

      <td>
        Function
      </td>

      <td>
        to\_int (\[adapter.field])
      </td>

      <td>
        Converts a string or float value in an array (list field) or single value field to an integer value. The value type of adapter.field is String or Float. For example: *device all then form.field\_value set\_value to\_int (\[device.specific\_data.data.cpus.cores])* converts a field value of 7.0 (float) to 7 (integer)
      </td>
    </tr>

    <tr>
      <td>
        to\_lower
      </td>

      <td>
        Function (string manipulation)
      </td>

      <td>
        to\_lower (\[adapter.field])
      </td>

      <td>
        Converts the string in adapter.field to lowercase.
      </td>
    </tr>

    <tr>
      <td>
        to\_table
      </td>

      <td>
        Function
      </td>

      <td>
        to\_table (\[adapter.field], column definitions)
      </td>

      <td>
        Converts a complex field (list of objects) into a formatted HTML table by mapping specified data fields to table headers.\
        *to\_table (\[adapter.field], \[(header: "Column 1 Name", field: "field\_1"), (header: "Column 2 Name", field: "field\_2")])*

        <br />

        **adapter.field** - The complex field (list of objects) that you want to convert into a table. Each object in this list provides the data for a single row in the output.

        <br />

        **column** definitions (list of objects) - This list defines the headers and corresponding data fields for each column. Each object in this list requires two properties:\
        **header** (string) - The column title that will be displayed in the HTML table.\
        **field**(string)\_\_\*\*- The name of the sub-field (property) within each object in *adapter.field* from which to extract data for the column.

        <br />

        **Example**: The following example converts a list of software objects into an HTML table with two columns 'SW UID' and 'Name\`.\*\*

        <br />

        *to\_table(\[device.specific\_data.data.installed\_software], \[(header: "SW UID", field: "sw\_uid"), (header: "Name", field: "name")])*\
        **Output**: Renders a complete HTML table with \`SW UID' and 'Name' as headers. The rows are populated with the *sw\_uid* and *name* values from the installed\_software list.
      </td>
    </tr>

    <tr>
      <td>
        to\_upper
      </td>

      <td>
        Function (string manipulation)
      </td>

      <td>
        to\_upper (\[adapter.field])
      </td>

      <td>
        Converts the string in adapter.field to uppercase.
      </td>
    </tr>

    <tr>
      <td>
        unique
      </td>

      <td>
        Function
      </td>

      <td>
        unique (\[adapter.field]) unique (nested function)
      </td>

      <td>
        unique (\[adapter.field]) returns the unique values in the list. The field type of adapter.field is a list (array) of values. unique (nested function) returns the unique results of a function.
      </td>
    </tr>

    <tr>
      <td>
        also
      </td>

      <td>
        Operator
      </td>

      <td>
        form.field1 set\_value "string1" also form.field2 set\_value "string2"
      </td>

      <td>
        Applies dynamic content to two or more fields in an action.\
        For example: form.field1 set\_value "aaa" also form.field2 set\_value "XXX"
      </td>
    </tr>

    <tr>
      <td>
        contains
      </td>

      <td>
        Operator
      </td>

      <td>
        case contains (“string”)
      </td>

      <td>
        For lists - True if at least one item="string".\
        For string fields - True if part of the string value in the field ="string".\
        For example: case contains (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        not\_contains
      </td>

      <td>
        Operator
      </td>

      <td>
        case not\_contains (“string”)
      </td>

      <td>
        For lists - True if at least one item not ="string".\
        For string fields - True if "string" does not appear in all or part of the string value in the field.\
        For example: case not\_contains (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        count
      </td>

      <td>
        Operator
      </td>

      <td>
        case count (number value)
      </td>

      <td>
        Counts and matches the number of items in a list.\
        For example: case count (10)
      </td>
    </tr>

    <tr>
      <td>
        starts\_with
      </td>

      <td>
        Operator
      </td>

      <td>
        case starts\_with (“string”)
      </td>

      <td>
        For lists - True if at least one item starts with "string".\
        For string fields - True if the string value starts with "string".\
        See also **not\_starts\_with**.\
        For example: case starts\_with (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        ends\_with
      </td>

      <td>
        Operator
      </td>

      <td>
        case ends\_with (“string”)
      </td>

      <td>
        For lists - True if at least one item ends with "string".\
        For string fields - True if the string value in the field ends with "string".\
        See also **not\_ends\_with**.\
        For example: case ends\_with (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        in
      </td>

      <td>
        Operator
      </td>

      <td>
        case in (\[“string1”, "string2", ..., "stringN"])
      </td>

      <td>
        For lists - True if at least one item is equivalent to one of the strings in the square brackets \[string1, string2,..., stringN].\
        See also **not\_in**.\
        For example: case in (\[“aaa”, "bbb", "ccc"])
      </td>
    </tr>

    <tr>
      <td>
        not\_in
      </td>

      <td>
        Operator
      </td>

      <td>
        case not\_in (\[“string1”, "string2", ..., "stringN"])
      </td>

      <td>
        For lists - True if at least one item is not equivalent to one of the strings in the square brackets \[string1, string2,..., stringN].\
        For example: case not\_in (\[“aaa”, "bbb", "ccc"])
      </td>
    </tr>

    <tr>
      <td>
        not\_starts\_with
      </td>

      <td>
        Operator
      </td>

      <td>
        case not\_starts\_with (“string”)
      </td>

      <td>
        For lists - True if at least one item does not start with "string".\
        For string fields - True if the string value in the field does not start with "string".\
        For example: case not\_starts\_with (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        not\_ends\_with
      </td>

      <td>
        Operator
      </td>

      <td>
        case not\_ends\_with (“string”)
      </td>

      <td>
        For lists - True if at least one item does not end with "string".\
        For string fields - True if the string value in the field does not end with "string".\
        For example: case not\_ends\_with (“aaa”)
      </td>
    </tr>

    <tr>
      <td>
        field\_equal
      </td>

      <td>
        Operator
      </td>

      <td>
        case field\_equal (“string”)
      </td>

      <td>
        True if the exact given string is identical to the string value in the field.\
        Examples:\
        case field\_equal (“google”) for string fields\
        case field\_equal (“8.3”) for number fields\
        case field\_equal (true) for boolean fields
      </td>
    </tr>

    <tr>
      <td>
        field\_not\_equal
      </td>

      <td>
        Operator
      </td>

      <td>
        case field\_not\_equal (“string”)
      </td>

      <td>
        True if the exact given string is not identical to the string value in the field.\
        Examples:\
        case field\_not\_equal (“google”)\
        case field\_not\_equal (“8.3”)\
        case field\_not\_equal (true)
      </td>
    </tr>

    <tr>
      <td>
        field\_exists
      </td>

      <td>
        Operator
      </td>

      <td>
        switch adapter.field case field\_exists then form.field set\_value “value”
      </td>

      <td>
        Tests whether adapter.field exists. If true, sets the value of form.field to "value".
      </td>
    </tr>

    <tr>
      <td>
        field\_not\_exists
      </td>

      <td>
        Operator
      </td>

      <td>
        switch adapter.field case field\_not\_exists then form.field set\_value “value”
      </td>

      <td>
        Tests whether adapter.field exists. If false, sets the value of form.field to "value".
      </td>
    </tr>

    <tr>
      <td>
        in\_net
      </td>

      <td>
        Operator
      </td>

      <td>
        switch \[adapter.field] case in\_net (subnet range) then form.field set\_value “value”
      </td>

      <td>
        Tests if a subnet range in adapter.field (list field) or a single subnet in adapter.field (string field) is within the specified range.\
        If the subnet or subnet range is within the specified range, sets the value of form.field to "value".\
        Accepts subnet ranges in CIDR notation\
        Example of IPv4 subnet range: "172.16.0.0/20". 172.16.0.0 is the network address. This range includes IP addresses from 172.16.0.0 to 172.16.15.255. 172.16.0.1 - 172.16.15.254 is the range expressed with a hyphen, and shows the first and last usable host address within the subnet.\
        Allows comparison against multiple comma-separated subnets. Supports both IPv4 and IPv6 subnet masks.
      </td>
    </tr>

    <tr>
      <td />

      <td />

      <td />

      <td />
    </tr>

    <tr>
      <td>
        not\_in\_net
      </td>

      <td>
        Operator
      </td>

      <td>
        switch \[adapter.field] case not\_in\_net (subnet range) then form.field set\_value “value”
      </td>

      <td>
        Tests if a subnet range in adapter.field (list field) or a single subnet in adapter.field (string field) is not within the specified range.\
        If the subnet or subnet range is *not* within the specified range, sets the value of form.field to "value".\
        Accepts subnet ranges in CIDR notation\
        Example of IPv4 subnet range: "192.168.1.0/24". 192.168.1.0 is the network address. This range includes IP addresses from 192.168.1.0 to 192.168.1.255 192.168.1.1 - 192.168.1.254 is the range expressed with a hyphen, and shows the first and last usable host address within the subnet.\
        Allows comparison against multiple comma-separated subnets. Supports both IPv4 and IPv6 subnet masks.
      </td>
    </tr>

    <tr>
      <td>
        gt
      </td>

      <td>
        Operator
      </td>

      <td>
        switch \[adapter.field] case gt(number value) switch \[adapter.field1] case gt(\[adapter.field2])
      </td>

      <td>
        Tests whether the number value in adapter.field is greater than the specified number value (for example, 10).\
        OR\
        Tests whether the number value in adapter.field1 is greater than the number value in adapter.field2.
      </td>
    </tr>

    <tr>
      <td>
        lt
      </td>

      <td>
        Operator
      </td>

      <td>
        switch \[adapter.field] case lt(number value) switch \[adapter.field1] case lt(\[adapter.field2])
      </td>

      <td>
        Tests whether the number value in adapter.field is less than the specified number value (for example, 20).\
        OR\
        Tests whether the number value in adapter.field1 is less than the number value in adapter.field2.
      </td>
    </tr>

    <tr>
      <td>
        set\_value
      </td>

      <td>
        Operator
      </td>

      <td>
        set\_value “string” set\_value \[adapter.field] set\_value \[adapter.field\_path] set\_value true; set\_value false for Boolean fields set\_value function () set\_value item1 or item2 ... or itemN
      </td>

      <td>
        Multiple (nested) functions can be used. The field type of adapter.field and adapter.field\_path must match the field type of form.field. For example, both fields must be string type or both number type. Note that "or" is supported with set\_value inside a Case statement to set the value of the action field to the first field value in the "or" list that exists on the asset. item1 or item2 ... or itemN
      </td>
    </tr>
  </tbody>
</Table>