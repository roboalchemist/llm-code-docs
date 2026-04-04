# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-with-delimiter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY FROM with Delimiter

## Overview

A delimiter is a character that separates text strings. Common delimiters are:

* Commas (,)
* Semicolon (;)
* Quotes ( ", ' )
* Dash (-)
* Pipes (|)
* Slashes ( / \ ).

**By default, the COPY FROM function accepts commas (,).**

## Syntax

The syntax for **COPY FROM** is as follows:

```sql  theme={null}
COPY table_name FROM 'file_path' (DELIMITER 'delimiter');
```

Two parameters need to be specified in the syntax:

* `table_name`: the table that will receive data from the file.
* `file_path`: a link to the file location in the server.
* `DELIMITER 'delimiter'`: the delimiter used in the CSV file.

## Example

Let’s have a look at the step-by-step below:

### Step #1: Create a CSV File

First, you should create a CSV file and store it on your local computer. In this case, we use Dash ( - ) character to separate the text.

> create a table - 1.0
> modify a table - 1.2
> drop a table - 2.2
> rename a table - 2.0

### Step #2:  Import FIle from Local to Server

You can use the syntax below for importing the file to the server:

```typescript  theme={null}
aws s3 cp ~/[file location on your local computer] s3://[server location]/[file name]
```

Next, import the file to the server using the above syntax:

```typescript  theme={null}
aws s3 cp ~/Documents/feature2.csv s3://oxla-testdata/cayo/feature2.csv
```

If it’s successfully imported, you will get the following result:

```typescript  theme={null}
upload: Documents/feature2.csv to s3://oxla-testdata/cayo/feature2.csv
```

### Step #3:  Connect to Oxla Server

Connect to the Oxla server using the command below:

```sql  theme={null}
psql -h buildfarm.oxla.com -p 6000
```

You are now in the Oxla environment if you get the output below.

```sql  theme={null}
psql (15.1 (Ubuntu 15.1-1.pgdg22.10+1), server Oxla 1.0)
WARNING: psql major version 15, server major version 0.0.
         Some psql features might not work.
Type "help" for help.
```

### Step #4:  Create a Table

Before creating a table, check for duplicate tables with the statement below:

```sql  theme={null}
DESCRIBE DATABASE
```

In return, you will retrieve a list of existing tables in Oxla.

```sql  theme={null}
+----------------------------+
| name                       |
+----------------------------+
| supplier_scale_1_no_index  |
| features                   |
| orders                     |
| features2                  |
| featurestable              |
| featurestable1             |
| featurestable10            |
+----------------------------+
```

<Warning>Ensure you are not creating duplicate tables.</Warning>

Create a “**featurelisttable**” table using the command below:

```sql  theme={null}
CREATE TABLE featurelisttable (featurename text, version float);
```

### Step #5:  Copy the CSV File Into Table

Because we are using Dash ( - ), we need to add a DELIMITER param with a specified character, as shown below:

```sql  theme={null}
COPY featurelisttable FROM 's3://oxla-testdata/cayo/feature2.csv' (DELIMITER '-');
```

You will get the following successful result:

```sql  theme={null}
--
(0 rows)
```

Otherwise, you will get the error message below:

```sql  theme={null}
ERROR: unexpected data at line: 1 col: 0 position: 108, expected , but got:
```

### Step #6: Retrieve the Table

To verify that the data was imported correctly from the server, retrieve all the data using the SELECT statement:

```sql  theme={null}
SELECT * FROM featurelisttable;
```

You will have the same data in the table as in the CSV file.

```sql  theme={null}
+-----------------+----------+
| featurename     | version  | 
+-----------------+----------+
| create a table  | 1        |
| modify a table  | 1.2      |
| drop a table    | 2.2      |
| rename a table  | 2        |
+-----------------+----------+
```
