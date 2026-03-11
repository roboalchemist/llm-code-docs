# Source: https://docs.axonius.com/docs/query-wizard-operators.md

# Using Operators in the Query Wizard

Various operators are available for selection in the Query Wizard. The operators available depend on the field type.
Once a field is selected, you need to select a comparison function from a drop-down list. For each field type there is a list of possible functions:
Some available operators are listed here:

<Callout icon="📘" theme="info">
  Note

  Use the 'exists' function to filter the existence of any property value. It is available for all field types.
</Callout>

![SelectOperators](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectOperators.png)

### Operators for Text Fields

For single value text fields, the available operators are 'contains', 'equals', 'in (equals)', 'in (contains)', 'in (plain text)', 'starts', 'ends' and 'regex'  functions. All refer to a text value to compare to (see above screen).

For multiple value text fields, the available operators are 'size', 'exists', 'contains', 'equals', 'in (equals)', 'in (contains)', 'in (plain text)', 'starts', 'ends', 'regex', `count =`, `count >`,  and `count <`.

<Callout icon="📘" theme="info">
  Note

  By default, the regex operator is not case sensitive in searching the query expression. To make the query case sensitive, add (?-i) to the regex query expression, for example:
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/regex_example.png)
</Callout>

#### In Operators

Three sorts of **In** values are available. *in (equals)*, *in (contains)* or *in (plain text)*.   For more information, see [Adding Multiple Values to Query Expressions](/docs/adding-multiple-values-to-query-expression). The system limits the number of assets fetched using the 'in' operator. When the limit is exceeded, an error message is displayed. Note that *in (equals)* and *in (plain text)* values are case sensitive.

<Callout icon="📘" theme="info">
  Note

  A single query expression using the *in (equals)* or *in (contains)*, function can replace multiple query expressions using the 'equals' or 'contains' function with 'or' operands between them.
</Callout>

### Operators for Numeric Fields

'equals', `>` (greater) and `>` (lesser) functions, all refer to a numeric value to compare to.

<Callout icon="📘" theme="info">
  Note

  The **Adapter Connections** field has unique actions to filter by the number of the adapters: `count =`, `count <`, `count >`
</Callout>

### Operators for Date Fields

`>` (after), `<` (before),'=' (is) 'last days', 'next days', 'next days from now', 'next calendar days', 'last calendar days', 'next calendar days from now', 'last calendar days from now', 'last hours', 'next hours',  'next hours from now', 'previous weeks', 'previous months', 'current month' 'duration until (days)' and 'duration until (hours)' functions, all refer to a date expression to compare to.

* Use date expressions as follows:

  * '=',   `<` or `>`  the value to compare is a chosen calendar date expression.

  <Callout icon="📘" theme="info">
    **Note**

    The system interprets the `>` operator for date fields as **greater than or equals to**. This is because the comparison is performed against the earliest possible time unit of the next day (YYYY-MM-DD 00:00:00), thereby including all records from the specified date's start time.

    For example, if you run a query to fetch assets with **Field\_A > 2000-01-01**, the results will include also the date 2000-01-01, because the system starts counting from 2000-01-02 00:00:00.
  </Callout>

  * 'last days', 'next days' and 'next days from now' the value to compare to is the relative number of days (integer) whereas a day = a cycle of 24 hours, counting from the moment you run the query.
  * 'last calendar days', 'next calendar days', 'last calendar days from now', and 'next calendar days from now' represent a defined range of calendar days - full days.
    * For example: when you search for assets that were last seen in the 2 'last days', the query returns assets that were seen in the last 48 hours, as it counts two cycles of 24 hours, starting from the moment you run the query; and when you search for assets that were last seen in the 2 'last calendar days', the query returns assets that were seen in the last two full days - meaning, yesterday and the day before yesterday, with no results from current day (assuming you run the query in the middle of the day).
  * 'last hours', 'next hours' and 'next hours from now' the value to compare to is the relative number of hours (integer).
  * 'previous weeks' queries assets from the selected number of weeks since the previous Monday. For example, if today is Wednesday and you select to query for 1 previous week, the query returns values from two Mondays ago until the past Monday (two days ago).
  * ‘previous months’ the value to compare to is the previous X calendar months. For instance, when you are in the month of June and choose ‘previous 3 months’ the query will either fetch assets which fulfill the query for the months of March, April, and May, or if you choose NOT, will not fetch values for those months.
  * ‘current month’ the value to compare to the current calendar month.
  * 'duration until (days)' and 'duration until (hours)' compare the time difference between two date or timestamp fields. For instance, 'duration until (days) \< 3' shows assets where the time difference between their Field A and Field B is less than 3 days. To learn more, see [field comparison queries](https://docs.axonius.com/docs/selecting-source-options-in-the-query-wizard#/field-comparison).

### Operators for IP Address Fields

* 'size', 'exists', 'in subnet', 'not in subnet', 'contains', 'regex', 'equals', 'starts', 'in (equals)', 'isIPv4' and 'isIPv6' functions, all refer to an IP address value to compare to.
* For  'in subnet', 'not in subnet', you can specify multiple comma separated subnets.
* Count  '=',  `<` or `>` enables a numeric value for the number of IP addresses to compare to.
* For 'in (equals)', a query with this operator performs a string match against the list of subnet strings discovered and stored in the asset's Preferred Subnet field. This operator **does not** calculate a range of IPs.

  <Callout icon="📘" theme="info">
    **Note - Querying Devices by Subnet**

    The **Preferred Subnet** field stores the actual subnet value assigned to a device. Querying against this field with the 'in (equals)' operator returns only devices **with the exact subnet string**. For example, a query such as `Preferred Subnet in (equal) 192.168.1.0/24` returns only devices whose exact subnet value is `192.168.1.0/24`. It **does not** return devices whose IP addresses fall within that subnet range.

    To find all devices whose IP addresses fall **within a subnet range**, use the 'in subnet' operator with the **Network Interface: IPs** field. Such a query performs subnet membership calculations to identify all devices that have any IP address within the specified subnet range, regardless of the value stored in their Preferred Subnet field.

    ![InSubnetOperator](https://files.readme.io/e7adbf712789f447c29f82a67406130b12d4f4c6a5141476da61ccd52d89e422-image.png)
  </Callout>
* For 'size', enter a number that represents the number of values the asset has from the queried field. For example, you can query for the **Preferred IPv6** field with a 'size' operator of \[12], and this will return assets with a list of 12 IPv6 addresses.
* For 'starts', enter a value that the IP address starts with.

### Operators for Version Fields

'contains', 'equals', 'regex', 'earlier than', 'later than' functions, all refer to a version value to compare to.

<Callout icon="📘" theme="info">
  Note

  The **OS: Distribution** field has unique actions to filter devices with Windows, MAC or iOS versions lower or higher than the compared version: `<`, `>`
</Callout>

### Operators for Enumerated Fields

'equals' function along with a selection of a values from a list of pre-defined values.

### Adding Custom Count Operator Fields to the Query Wizard

The count operators (`count =`, `count >`, and `count <`) are available by default for a predefined set of fields in the Query Wizard. You can now enable these operators for up to 10 additional fields of your choice, including custom data fields and common enrichment fields. Once configured, count operators can be used in the Query Wizard for the newly added fields.

For more information, see [Query Configuration](/docs/query-configuration).