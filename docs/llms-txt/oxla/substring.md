# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/substring.md

# SUBSTRING

<Warning>SUBSTR is an alias for SUBSTRING. Learn more at [SUBSTR](/sql-reference/sql-functions/string-functions/substr) documentation.</Warning>

## Overview

The SUBSTRING() function lets you extract a part of a string and return that substring.

## Syntax

Here are the 2 basic syntaxes of the `SUBSTRING()` function in Oxla:

**2 Arguments**

```sql  theme={null}
SUBSTRING( string, start_position )
```

**3 Arguments**

```sql  theme={null}
SUBSTRING(string, start_position, length)
```

<Tip>Both syntaxes will have input and return of type `string`.</Tip>

## Example

The following example uses the `SUBSTRING()` function to extract the first 7 characters from the string.

```sql  theme={null}
SELECT SUBSTRING('OxlaDocumentation', 1, 7);
```

It will display the substring from position 6 output as shown below:

```sql  theme={null}
substring 
-----------
 OxlaDoc
```
