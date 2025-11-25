# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-to/copy-to-stdout.md

# COPY TO STDOUT

## Overview

The `COPY TO STDOUT` command is used to export data directly from a table to the client. This approach allows for data transfer by sending the data directly to the client, eliminating the need for server-side file operations.

## Syntax

The basic syntax for using `COPY TO STDOUT` is:

```sql  theme={null}
COPY table_name TO STDOUT;
```

Parameters:

* `table_name`: The table from which the data will be exported.
* `stdout`: Indicates that the data will be sent to the standard output (client application).

<Note>- **Format**: Only .csv is supported <br /> - **Delimiter**: For CSV format, the default delimiter is a comma (,)</Note>

## Examples

### Step 1. Create the Table

1. Create the table and insert some data into it.

```sql  theme={null}
CREATE TABLE book_inventory (
    title TEXT,
    copies_available INT
);
INSERT INTO book_inventory (title, copies_available) VALUES
('To Kill a Mockingbird', 5),
('1984', 8),
('The Great Gatsby', 3),
('Moby Dick', 2),
('War and Peace', 4);
```

2. Upon successful creation, you should see the output below:

```sql  theme={null}
CREATE
INSERT 0 5
```

### Step 2. Start the Export Operation

1. Run the `COPY TO STDOUT` command to export the data from the `book_inventory` table:

```sql  theme={null}
COPY book_inventory TO STDOUT;
```

2. You will get the output with the table values, which you can use to create or copy into a CSV file:

```sql  theme={null}
"To Kill a Mockingbird",5
1984,8
"The Great Gatsby",3
"Moby Dick",2
"War and Peace",4
```
