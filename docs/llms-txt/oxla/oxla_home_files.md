# Source: https://docs.oxla.com/system-catalogs/oxla_home_files.md

# Oxla Home Files

## Overview

The `oxla_home_files` virtual table lists all files associated with a specific table in the oxla home directory. This approach offers a more reliable way to retrieve data than simply scanning files directly.

## Fields

| Field          | Content                                                             | Type          |
| -------------- | ------------------------------------------------------------------- | ------------- |
| `path`         | Path relative from the oxla working directory                       | TEXT          |
| `byte_size`    | Size of the file in bytes                                           | BIGINT        |
| `start_index`  | First index in the file, binary data base64 encoded (if applicable) | NULLABLE TEXT |
| `end_index`    | Last index in the file, binary data base64 encoded (if applicable)  | NULLABLE TEXT |
| `row_count`    | Number of rows in the file                                          | BIGINT        |
| `batch_count`  | Number of batches the file is divided into                          | BIGINT        |
| `table_id`     | ID of the related table                                             | BIGINT        |
| `namespace_id` | ID of the related namespace                                         | BIGINT        |
| `database_id`  | ID of the related database                                          | BIGINT        |

## Example Query

This example shows how to query the `oxla_home_files` table in an Oxla instance

### Empty Result

1. Run the `oxla_home_files` query below:

```sql  theme={null}
SELECT * FROM oxla_internal.oxla_home_files;
```

2. When the `oxla_home_files` table is empty, the query returns an empty result set:

```sql  theme={null}
 path | byte_size | start_index | end_index | row_count | batch_count | table_id | namespace_id | database_id 
------+-----------+-------------+-----------+-----------+-------------+----------+--------------+-------------
(0 rows)
```

### After Data Insertion

1. Create and insert data into the table:

```sql  theme={null}
CREATE TABLE orders (
  order_id INT,
  order_date DATE,
  total_amount INT,
  shipping_address TEXT,
  status TEXT
);

INSERT INTO orders 
    (order_id, order_date, total_amount, shipping_address, status) 
VALUES 
    (1001, '2024-07-13', 150.75, '123 Main St, Anytown, USA', 'Shipped'),
    (1002, '2024-07-12', 200.50, '456 Elm St, Othertown, USA', 'Delivered'),
    (1003, '2024-07-12', 350.25, '789 Oak St, Anotherplace, USA', 'Processing'),
    (1001, '2024-07-11', 100.00, '321 Pine St, Somewhere, USA', 'Cancelled'),
    (1004, '2024-07-10', 500.00, '555 Maple St, Nowhere, USA', 'Pending');
```

2. Run the `oxla_home_files` query:

```sql  theme={null}
SELECT * FROM oxla_internal.oxla_home_files;
```

3. After inserting data into the table, the query lists the file metadata stored in Oxla:

```sql  theme={null}
path                                                             | byte_size | start_index | end_index | row_count | batch_count | table_id | namespace_id | database_id 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 /0/0/16385/buffers/cluster-2jyd1jzvhgequov20igkxe4peyl-oxla-0/0 |       978 |             |           |         5 |           1 |    16385 |            0 |           0
(1 row)
```
