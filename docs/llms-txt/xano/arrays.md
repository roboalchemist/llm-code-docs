# Source: https://docs.xano.com/xanoscript/function-reference/data-manipulation/arrays.md

# Source: https://docs.xano.com/the-function-stack/functions/data-manipulation/arrays.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Arrays

An array, or list, may contain a single item or many items. Arrays behave differently than other data types; you will typically iterate through them to transform data. These iterations can be performed with loops, or you can perform more wide-sweeping changes using [expressions](/xano-transform/using-xano-transform).

We have several array functions that you can use to extract and manipulate the array quickly.

Before you dive in, let's review a key concept specific to arrays: index

The **index** is the number that corresponds to the item in the list, starting at 0. You won't see this reflected in your data, but it's how arrays keep track of their defined order of items.

## Add to End of Array

Adds an item to the end of an array

## Add to Beginning of Array

Adds an item to the beginning of an array

## Remove from End of Array

Removes the item at the end of the array

## Remove from Beginning of Array

Removes the item at the beginning of the array

## Merge

Merges two arrays together

## Find First Element

Uses the expression builder to find the first matched element of an array

## Find First Element Index

Uses the expression builder to find the index of the first matched element of an array

## Has Any Element

Returns a true or false based on if the array has any elements that meet the conditions outlined in the expression builder

## Has Every Element

Returns a true or false based on if the array has **all** elements that meet the conditions outlined in the expression builder

## Find All Elements

Uses the expression builder to find all matching elements in the array

## Get Element Count

Uses the expression builder to find the count of all matching elements in the array

## Using the Expression Builder

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


Built with [Mintlify](https://mintlify.com).