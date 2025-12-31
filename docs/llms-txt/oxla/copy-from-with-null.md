# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-with-null.md

# COPY FROM with NULL

## Overview

NULL means **no value**. In other words, it does not have any value, not equal to 0, empty string, or spaces. In Oxla, we can specify a different string as the null value in the `COPY FROM` statement.

## Syntax

You can define a string with any strings that will replace the null value, as shown in the syntax below:

```sql  theme={null}
COPY table_name FROM 'file_path' (NULL 'string')
```

## Examples

### Case #1: Show Blank for NULL Value

1. To begin with, create a CSV file called **idvals.csv** with a null value:

> null,5
> 2,2
> 3,2

2. In addition, create a table called **idqty** by specifying the column with an integer data type:

```sql  theme={null}
CREATE TABLE idqty (id INTEGER, quantity INTEGER);
```

3. Execute the COPY FROM statement with a NULL option:

```sql  theme={null}
COPY idqty FROM idvals (NULL, 'null');
```

4. A null value from the CSV file will be displayed in a table with an empty row that has no value, as shown below:

```sql  theme={null}
+------+----------+
| id   | quantity | 
+------+----------+
|      | 5        |
| 2    | 2        |
| 3    | 2        |
+------+----------+
```

### Case #2: Show String for NULL Value

1. A string is represented with a double quote. In this case, we create a CSV file called **idvals.csv** with a null value as a string.

> "null",5
> 2,2
> 3,"null"

2. Create a table called **idqty** by specifying the column with an integer data type:

```sql  theme={null}
CREATE TABLE idqty (id INTEGER, quantity INTEGER);
```

3. Execute the COPY FROM statement with a NULL option:

```sql  theme={null}
COPY idqty FROM idvals (NULL, 'null');
```

4. You can see that a null value from the CSV file will be displayed in a table with **“null”:**

```sql  theme={null}
+------+----------+
| id   | quantity | 
+------+----------+
| null | 5        |
| 2    | 2        |
| 3    | null     |
+------+----------+
```

<Info>You can specify another string to replace the null value. Such as blank, empty, invalid, etc.</Info>
