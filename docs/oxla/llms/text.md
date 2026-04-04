# Source: https://docs.oxla.com/sql-reference/sql-data-types/text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text

## Overview

The text data type is a UTF8-encoded text with Unicode support, which stores a sequence of characters (text).

## Examples

Let's create an employee table with a text data type in each column:

```sql  theme={null}
CREATE TABLE employee (
    employeeName text,
    employeeDept text,
    employeeRole text
);
INSERT INTO employee (employeeName, employeeDept, employeeRole)
VALUES ('John','Finance','Staff'),
       ('Maya','Product','Staff'),
       ('Jane','Finance','Staff'),
       ('Phil','HR','Manager');
```

<Check>Insert the text value between the single quotes **' '**.</Check>

The created table is shown below:

```sql  theme={null}
+---------------+---------------+---------------+
| employeename  | employeedept  | employeerole  |
+---------------+---------------+---------------+
| John          | Finance       | Staff         |
| Maya          | Product       | Staff         |
| Jane          | Finance       | Staff         |
| Phil          | HR            | Manager       |
+---------------+---------------+---------------+
```

## Text With SUBSTR Function

The `substr()` function extracts a specific number of characters from a text.&#x20;

### Syntax

```sql  theme={null}
substr( text, start_position, length )
```

Let's analyze the above syntax:

* `text`is the specified text.
* `start_position` is used as the starting position, specifying the part from which the substring will be returned. It is written as an int value.
* `length` is used to determine the number of characters to be extracted. It can be one or more characters.

<Note>The first position in the `text` is 1.</Note>

### Example

Insert a value into the text column.

```sql  theme={null}
SELECT substr('Watermelon',6,5) AS "Fruit";
```

The updated table is shown below:

```sql  theme={null}
+-------------+
| Fruit       |    
+-------------+
| melon       |
+-------------+
```

## Text With LENGTH Function

The `length()` function returns the number of characters in a text.&#x20;

<Note>The number of characters might be different from the byte length.</Note>

### Syntax

The length function will take a text as a parameter.

```sql  theme={null}
LENGTH (text);
```

### Example

Insert a value into the text column.

```sql  theme={null}
SELECT LENGTH ('UNITED STATES');
```

The updated table is shown below.

```sql  theme={null}
+---------+
| f       |
+---------+
| 13      | 
+---------+
```

<Info>The `length()` function will also count spaces.</Info>
