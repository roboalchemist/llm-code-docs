# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/current-schema.md

# current_schema()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-SESSION" target="_blank">current\_schema()</a> is a session information function that returns the name of the first existing schema.

## Syntax

There are two available syntax versions of `current_schema()` function:

<CodeGroup>
  ```sql Version 1 theme={null}
  SELECT current_schema();
  ```

  ```sql Version 2 theme={null}
  SELECT current_schema;
  ```
</CodeGroup>

<Info>It will return `NULL` if none of the schemas from `search_path` exist</Info>

## Example

The following example shows how to get the current schema name using this function

```sql  theme={null}
SELECT current_schema();
```

The output from the above query can be as follows:

```sql  theme={null}
+------------+
| f          |
+------------+
| public     |
+------------+
```
