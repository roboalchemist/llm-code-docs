# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-total-relation-size.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_total_relation_size()

## Overview

The <a href="https://www.postgresql.org/docs/9.1/functions-admin.html" target="_blank">pg\_total\_relation\_size()</a> is a database object size function that retrieves the size of a table and is useful for monitoring the storage requirements.

## Syntax

The syntax for the `pg_total_relation_size()` function is as follows:

```sql  theme={null}
pg_total_relation_size('relation_name');
```

It returns the size of the specified table in bytes.

## Parameters

The following parameters are required to execute this function:

* `relation_name`: name of the table for which you want to determine the size

## Example

For the needs of this section, we will create a **users** table

```sql  theme={null}
CREATE TABLE users (
    username TEXT,
    email TEXT
);
INSERT INTO users (username, email) VALUES
    ('john_doe', 'john.doe@example.com'),
    ('jane_smith', 'jane.smith@example.com'),
    ('alice_smith', 'alice.smith@example.com'),
    ('bob_jones', 'bob.jones@example.com'),
    ('susan_wilson', 'susan.wilson@example.com'),
    ('michael_jackson', 'michael.jackson@example.com'),
    ('lisa_johnson', 'lisa.johnson@example.com'),
    ('david_smith', 'david.smith@example.com');
```

Now we would like to use the `pg_total_relation_size()` function to determine the size of the **users** table (in bytes)

```sql  theme={null}
SELECT pg_total_relation_size('users');
```

By executing the query above, we will get the following output:

```sql  theme={null}
 pg_total_relation_size 
------------------------
                    556
```
