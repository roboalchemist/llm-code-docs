# Source: https://docs.xano.com/the-function-stack/functions/database-requests/bulk-operations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk Operations

> Perform actions on multiple records at once.

## Bulk Operations

Using bulk operations in Xano is largely the same between operation types. Each function expects an array of data or a custom query that it will use to apply the bulk operation, with the exception of Clear All Records.

The available bulk operations are:

* **Bulk Add Records**
* **Bulk Delete Records**
* **Bulk Patch Records**
* **Bulk Update Records**
* **Clear App Records**

For **Bulk Add Records, Bulk Patch Records, and Bulk Update Records**, you'll need to provide an array of items to add or update in the table.

**Bulk Add** and **Bulk Update** require the entire contents of the record. Make sure to include the record IDs in Bulk Update.

**Bulk Patch** only requires each object to have the ID and the fields you want updated.

For operations like **Bulk Delete**, use the custom query expression to determine which records to delete.

### Using the Expression Builder

Each conditional has four different components.

**Conditional Type**

The conditional type determines how this condition is weighted in the final return. You can choose between **AND** and **OR. AND** conditionals require the present conditional and any others before it to be satisfied, such as "where the date is before today **AND** the user is an admin". **OR** conditionals do not require any other conditionals to be satisfied, such as "if the user is an admin **OR** if the user is a manager".

**Left Value**

This is the first value you're using in the conditional. In a database query, this is usually going to be a column that you want to check against.

**Operators**

<Info>
  Please note that operators may differ based on where you are building the expression. Database queries will have different operators available than regular conditional statements. Learn More
</Info>

* **Equals (==)** - an exact match

* **Not Equals (!=)** - does not equal

* **Equals with type matching (===)** - an exact value match and an exact type match

  * Ex. Variable **var\_1** has a value of 123, with a type of text. You set up a conditional statement to check if **var\_1 === 123**, but your value in the conditional statement is of type integer. This would return false, because the types do not match.

* **Not equals with type matching (!==)** - does not equal value or type, similar to ===

* **Greater than (>)** - the value on the left is greater than the value on the right

* **Greater than or equals (≥)** - the value on the left is greater than or equals to the value on the right.

* **Less than (\<)** - the value on the left is less than the value on the right.

* **Less than or equals (≤)** - the value on the left is less than or equals to the value on the right.

* **LIKE** - Used for comparing text. Like is case-insensitive and compares if a text string is like another text string. It can be thought of as equals for text but upper case and lower case does not matter.

* **NOT LIKE** - Used for comparing text. Not Like is case-insensitive and compares if a text string is not like another. It is like not equals for text but upper case and lower case does not matter.

* **INCLUDES** - Used for comparing text. Includes is a flexible operator and is case-insensitive. It is able to determine if there is a partial match in a text string.

* **DOES NOT INCLUDE** - Used for comparing text. Does not include determines if a text string is not included in another text string.

* **IN** - If a single value is found in an array (list). Start with the single value on the left side and the right side should contain the array.

* **NOT IN** - If a single value is not found in an array (list). The single value should be on the left side and the array on the right side.

* **REGEX MATCHES** - [Regular Expression](https://regex101.com/) used for finding patterns in text.

* **REGEX DOES NOT MATCH** - [Regular Expression](https://regex101.com/) used for finding a pattern that does not match in text.

* **OVERLAPS** - Used for comparing two arrays. Overlaps determines if any values in one array are present in the second array.

* **DOES NOT OVERLAP** - Used for comparing two arrays. Does not overlaps determines if no values in the first array are present in the second array.

* **CONTAINS** - Contains is an advanced filter used for JSON and arrays. It looks for an exact schema match.

* **DOES NOT CONTAIN** - Does not contain is the opposite of contains. It determines if there is not an exact schema match.

#### Right Value

The right value is whatever you are checking against the left value. This could be a hardcoded value, a variable, or even a database field from the same record.

## Clear All Records

Clear All Records will delete every record in the table.


Built with [Mintlify](https://mintlify.com).