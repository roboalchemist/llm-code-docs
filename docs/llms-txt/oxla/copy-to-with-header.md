# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-to/copy-to-with-header.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY TO with HEADER

## **Overview**

When you export data from a table to a CSV file using the `COPY TO` command, you can include or skip the header. Oxla provides three options for handling headers: `HEADER OFF`, `HEADER ON`, and `HEADER MATCH`.

## **Syntax**

The syntax for `COPY TO` with `HEADER` is as follows:

```sql  theme={null}
COPY table_name TO 'file_path' (Header_Syntax);
```

Parameters in the syntax include:

* `table_name`: The table containing the data to be exported.
* `file_path`: The CSV file location where the data will be saved.
* `Header_Syntax`: The specified header options.

## Header Options

* **HEADER OFF**

This option will not skip the header of the CSV file. The available syntax is:

```none  theme={null}
HEADER OFF
HEADER FALSE
HEADER 0
```

<Info>This option is a default behaviour if `HEADER` is not provided.</Info>

* **HEADER ON**

This option skips the header of the CSV file and follows only the previously specified columns. The available syntax is:&#x20;

```none  theme={null}
HEADER ON
HEADER TRUE
HEADER 1
```

## Examples

First, create a **"personal\_details"** table.

```sql  theme={null}
CREATE TABLE personal_details (
  id int,
  first_name text,
  last_name text,
  gender text
);
INSERT INTO personal_details 
    (id, first_name, last_name, gender) 
VALUES 
    (1,'Mark','Wheeler','M'),
    (2,'Tom','Hanks','M'),
    (3,'Jane','Hopper','F'),
    (4,'Emily','Byers','F'),
    (5,'Lucas','Sinclair','M');
```

The table and data were created successfully.

```sql  theme={null}
COMPLETE
INSERT 0 5
```

Now, let’s explore some cases of `COPY TO` with different header options:

### Case #1: HEADER OFF

<Info>Please ensure that the directory where you save the file has a write permissions.</Info>

1. Run the query below to export the table.

```sql  theme={null}
COPY personal_details TO '/home/acer/Documents/personalinfo.csv';
```

2. You will get the following output, indicating that the table has successfully exported to the CSV file.

```sql  theme={null}
--
(0 rows)
```

3. The data in the table is copied directly to the `personalinfo` file without considering the first row as a header.

```sql  theme={null}
1,'Mark','Wheeler','M'
2,'Tom','Hanks','M'
3,'Jane','Hopper','F'
4,'Emily','Byers','F'
5,'Lucas','Sinclair','M'
```

<Check>To include headers, use the `HEADER ON` option.</Check>

### Case #2: HEADER ON

1. Run the query below to export the table.

```sql  theme={null}
COPY personal_details TO '/home/acer/Documents/personalinfo.csv' (HEADER ON);
```

2. You will get a successful output below.

```sql  theme={null}
--
(0 rows)
```

3. In this case, the header from the table will be included in the CSV file.

```none  theme={null}
id,first_name,last_name,gender
1,'Mark','Wheeler','M'
2,'Tom','Hanks','M'
3,'Jane','Hopper','F'
4,'Emily','Byers','F'
5,'Lucas','Sinclair','M'
```
