# Source: https://docs.oxla.com/sql-reference/sql-statements/copy-from/copy-from-with-header.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# COPY FROM with HEADER

## Overview

When it comes to a table, we deal with its components like rows, columns, and headers. In Oxla, we provide 3 possible options for the header as follows:

* **HEADER OFF**

This option will not skip the header of the CSV file. Below are the available syntaxes besides HEADER OFF:

```sql  theme={null}
HEADER OFF
HEADER FALSE
HEADER 0
```

<Info>This is a default behavior that will be applied if you do not provide the HEADER option in your query.</Info>

* **HEADER ON**

This option will skip the header of the CSV file and only follow the columns that have been specified before. Below are the available syntaxes besides HEADER ON:

```sql  theme={null}
HEADER ON
HEADER TRUE
HEADER 1
```

* **HEADER MATCH**

This option will read the header and verify that the name matches the column names.&#x20;

## Syntax

The syntax for **COPY FROM with HEADER** is as follows:

```sql  theme={null}
COPY table_name FROM 'file_path' (Header_Syntax);
```

Two parameters need to be specified in the syntax:

* `table_name`: the table that will receive data from the file.
* `file_path`: a link to the file location in the server.
* `Header_Syntax`: the specified header options.

## Examples

Say you have created a CSV file called **idvals.csv,** and the file has been uploaded to the server:

> id,quantity
> 1,5
> 2,2
> 3,1
> 4,8
> 5,4
> 6,3

Then, you create a table by specifying the column with an integer data type:

```sql  theme={null}
CREATE TABLE idqty (id INTEGER, quantity INTEGER);
```

Now, let’s see an example case by case:

### Case #1: HEADER OFF

1. With reference to the table above, run the following query:

```sql  theme={null}
COPY idqty FROM 's3://oxla-testdata/cayo/idvals.csv';
```

2. An error output will appear.&#x20;

This happens because we specified the table with an INTEGER column. While in the CSV file, we have STRING value which is **“id”** and **“quantity”**, which are not considered headers.

```sql  theme={null}
Error while parsing f32 from csv at line:0 col:6 position:26, parsing error
```

<Check>To include the headers, use the **HEADER ON** option.</Check>

Another Option

1. If you don’t want to include the headers (**“id”** and **“quantity”**), you can modify your CSV file by deleting the headers:

> 1,5
> 2,2
> 3,1
> 4,8
> 5,4
> 6,3

2. Run the COPY FROM statement:

```sql  theme={null}
COPY idqty FROM 's3://oxla-testdata/cayo/idvals.csv';
```

3. You will get the following output which indicates that the file has successfully imported to the table:

```sql  theme={null}
--
(0 rows)
```

4. Display the table by using the SELECT statement to retrieve the table records:

```sql  theme={null}
SELECT * FROM idqty;
```

```sql  theme={null}
+----+----------+
| id | quantity | 
+---------------+
| 1  | 5        |
| 2  | 2        |
| 3  | 1        |
| 4  | 8        |
| 5  | 4        |
| 6  | 3        |
+----+----------+
```

### Case #2: HEADER ON

1. With reference to the **idqty** table above, run the following query:

```sql  theme={null}
COPY idqty FROM 's3://oxla-testdata/cayo/idvals.csv'(HEADER ON);
```

2. You will get the following output which indicates that the file has successfully imported to the table:

```sql  theme={null}
--
(0 rows)
```

3. To verify, use the SELECT statement to retrieve the table records:

```sql  theme={null}
SELECT * FROM idqty;
```

We will get the below result, which displays the **idqty** table:

```sql  theme={null}
+----+----------+
| id | quantity | 
+---------------+
| 1  | 5        |
| 2  | 2        |
| 3  | 1        |
| 4  | 8        |
| 5  | 4        |
| 6  | 3        |
+----+----------+
```

<Info>In this case, the header may be anything that has been specified before. It does not need to have column names.</Info>

### Case #3: HEADER MATCH

1. Based on the **idqty** table above, if we run the following query:

```sql  theme={null}
COPY idqty FROM 's3://oxla-testdata/cayo/idvals.csv' (HEADER MATCH);
```

2. It will produce a successful output because the specified columns in the **idqty** table are matched with the header of the **idvals.csv** file:

```sql  theme={null}
--
(0 rows)
```

3. But, you will get a mismatched output when the header isn’t matched. Say that the **idvals.csv** file has **“id”** and “**qty”** header, as shown below:

> id,qty
> 1,5
> 2,2
> 3,1
> 4,8
> 5,4
> 6,3

Then, you will get a mismatched output because it reads **“qty”** from the CSV file when the expected value is **“quantity”** as specified in the table.

```sql  theme={null}
column name mismatch in header line field 1: got "qty", expected "quantity"
```

**Another Option**

1. Furthermore, you can also define the columns that you want to match as shown below:

```sql  theme={null}
COPY idqty(id, quantity) FROM 's3://oxla-testdata/cayo/idvals.csv' (HEADER MATCH);
```

The following output shows a successful result:

```sql  theme={null}
--
(0 rows)
```

2. But, if you change the ordering by switching the order of the columns:

```sql  theme={null}
COPY idqty(quantity, id) FROM 's3://oxla-testdata/cayo/idvals.csv' (HEADER MATCH);
```

3. You will get a mismatch error message.

```sql  theme={null}
column name mismatch in header line field 1: got "id", expected "quantity"
```
