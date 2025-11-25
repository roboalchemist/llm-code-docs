# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/substr.md

# SUBSTR

## Overview

The `SUBSTR()` function extracts a specific number of characters from a string.

## Syntax

The syntax of the function is illustrated below:

**2 Arguments**

```sql  theme={null}
substr( string, start_position)
```

**3 Arguments**

```sql  theme={null}
substr( string, start_position, length )
```

<Tip>Both syntaxes will have input and return of type `string`.</Tip>

### Start Position

The `start_position` is used as the starting position, specifying the part from where the substring is to be returned. It is written as an integer value.

| **Input**                                      | **Return**                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `start_position < 0 ``start_position < string` | The `start_position` is a given character in the string. The count starts from the first character.                                                                                                                                                                                              |
| `start_position > string`                      | Returns an empty substring.                                                                                                                                                                                                                                                                      |
| `start_position` = negative value              | The count starts from the provided negative value, with subsequent characters yielded as it approaches 0. <br /><br /> If the index is less than or equal to 0, no characters are returned. <br /><br /> Once it exceeds 0, characters from the string are yielded, starting from the first one. |

### Length

The `length` is used to determine the number of characters to be extracted\*. \*It can be one or more characters.

| **Input**                 | **Return**                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `length` = 0              | Returns an empty substring.                                                                                |
| `length` is not set       | The function will start from the specified `start_position` and end at the last character of the `string`. |
| `length` = negative value | Returns an error.                                                                                          |

## Examples

### Case 1: `SUBSTR()` function with specified `start_position` & `length`

In this example, we will set the `start_position` with the first six characters and have five characters extracted:

```sql  theme={null}
SELECT substr('Watermelon',6,5) AS "Fruit";
```

The updated table is shown below:

```sql  theme={null}
Fruit 
-------
 melon
```

### Case 2: `SUBSTR()` function with `length` = 0

The following query will extract a string with `length` = 0:

```sql  theme={null}
SELECT substr('Watermelon',6,0) AS "Fruit";
```

It will display an empty output as there is no `length` specified:

```sql  theme={null}
Fruit 
-------

```

### Case 3: `SUBSTR()` function with `length` = negative value

Here we will check if the `length` is specified with a negative value:

```sql  theme={null}
SELECT substr('Watermelon',6,-2) AS "Fruit";
```

Instead of extracting the string from the last characters, it will return an error as seen below:

```sql  theme={null}
ERROR:  Length of substring cannot be negative
```

### Case 4: `SUBSTR()` function with `start_position` > `string`&#x20;

We know that **Watermelon** only has ten characters, but this time, we will figure out if the specified `start_position` is larger than the string’s characters:

```sql  theme={null}
SELECT substr('Watermelon',20,2) AS "Fruit";
```

It will display an empty output as shown below:

```sql  theme={null}
Fruit 
-------

```

### Case 5: `SUBSTR()` Function with 2 Arguments

In this example, we will set the `start_position` with the first six characters and have five characters extracted.

```sql  theme={null}
SELECT substr('database', 6) AS "Result";
```

It will display the substring from position 6 output as shown below:

```sql  theme={null}
Result 
--------
 ase
```
