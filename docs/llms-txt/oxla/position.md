# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/position.md

# POSITION

## Overview

The `POSITION()` function returns the position of the first occurrence of a substring in a string. It works the same as
[STRPOS](/sql-reference/sql-functions/string-functions/strpos), but it has slightly different syntax.

## Syntax

The syntax for this function is as follows:

```sql  theme={null}
POSITION(substring IN string)
```

The position of the substring within the string starts from 1. If the substring is not found, it returns 0.

## Examples

### Example 1

This query looks for the position of the substring `world` within the string `Hello, world!`.

```sql  theme={null}
SELECT POSITION('world' IN 'Hello, world!');
```

The result would be the starting position of the substring `world`, which is 7.

```sql  theme={null}
position 
----------
        7
```

### Example 2

The query looks for the position of the substring `123` within the string `1a2b3c`.

```sql  theme={null}
SELECT POSITION('123' IN '1a2b3c');
```

`123` is found starting at position 1, the result would be 1.

```sql  theme={null}
position 
----------
        7
```

### Example 3

The query tries to find the position of the substring `abc` within the string `xyz`.

```sql  theme={null}
SELECT POSITION('abc' IN 'xyz');
```

`abc` is not found in `xyz`, the result would be 0.

```sql  theme={null}
position 
----------
        0
```

### Example 4

This query searches for the position of the substring `cde` within the string `cde`.

```sql  theme={null}
SELECT POSITION('cde' IN 'cde');
```

`cde` is the entire string, the result would be 1.

```sql  theme={null}
position 
----------
        1
```
