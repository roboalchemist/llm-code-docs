# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY FROM

## Overview

`COPY FROM` statement is used to import data from a file into a table by reading from the file's content directly. When using the `COPY FROM`, each field in the file is inserted sequentially into the specified column.

<Info>The file must be accessible and able to be read and written to</Info>

## Syntax

The syntax for THE `COPY FROM` is as follows:

```sql  theme={null}
COPY table_name FROM 'file_path';
```

where:

* `table_name`: the table that will receive the data from the file
* `file_path`: the link to the file location accessible from the server

## Example

### Creating CSV Files

Firstly, you should create a CSV file and store it on your local computer. Here, we make a file called **“feature2.csv”** that stores information about features with their versions:

> create a table, 1.0
> modify a table, 1.2
> drop a table, 2.2
> rename a table, 2.0

### Importing Files from Local to Server

You can use the syntax and the example presented below for importing the file to the server:

```typescript  theme={null}
aws s3 cp ~/[file location on your local computer] s3://[server location]/[file name]
```

```typescript  theme={null}
aws s3 cp ~/Documents/feature2.csv s3://oxla-testdata/test/feature2.csv
```

After a successful import, you will get the following result:

```typescript  theme={null}
upload: Documents/feature2.csv to s3://oxla-testdata/test/feature2.csv
```

### Connecting to Oxla Server

Now that the file has been successfully uploaded to the server, you need to connect to Oxla using the command below:

```sql  theme={null}
psql -h buildfarm.oxla.com -p 6000
```

Once you successfully connected to an Oxla server, you should get a similar output:

```sql  theme={null}
psql (15.1 (Ubuntu 15.1-1.pgdg22.10+1), server Oxla 1.0)
WARNING: psql major version 15, server major version 0.0.
         Some psql features might not work.
Type "help" for help.
```

### Creating a Table

Once you proceed to table creation stage, firstly it's worth checking for duplicate tables, by executing the statement below:

```sql  theme={null}
DESCRIBE DATABASE
```

In return, you will retrieve a list of all existing tables in Oxla:

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

After that, you need to create a table to retrieve the data from the CSV file. Here, we will create a `featurelist` table:

```sql  theme={null}
CREATE TABLE featurelist(featurename text, version float);
```

### Copying the CSV File Into the Table

Now, you can copy the **“feature2.csv”** by executing the `COPY FROM` query, as shown below:

```sql  theme={null}
COPY featurelisttable FROM 's3://oxla-testdata/cayo/feature2.csv';
```

### Retrieving the Table

To verify that the data was imported correctly from the server, you can retrieve all the data using the `SELECT` statement:

```sql  theme={null}
SELECT * FROM featurelisttable;
```

Now you should have the same data in the table as in the CSV file.

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
