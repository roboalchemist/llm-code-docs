# Source: https://docs.oxla.com/sql-reference/sql-data-types/json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON

## **Overview**

JSON stands for **JavaScript Object Notation**. It is an open standard format with key-value pairs to transport data between a server and a web application.

## Syntax

The JSON data type in Oxla has the following syntax:

```sql  theme={null}
variable_name JSON  
```

## Examples

### 1. Create a Table

First, create the **orders table** using the below command:

```sql  theme={null}
CREATE TABLE orders (  
    orders_Detail JSON  
);  
```

This will create a table with the `orders_Detail`column to store key-value pairs of data.

### 2. Insert Data

Next, insert data into the orders table as follows:

```sql  theme={null}
INSERT INTO orders (orders_Detail)  
VALUES
('{ "customer": "Dean Smith", "items": {"product": "cup","qty": 2}}'),
('{ "customer": "Sissy Kate", "items": {"product": "knife","qty": 1}}'),
('{ "customer": "Emma Stone", "items": {"product": "spoon","qty": 4}}'),
('{ "customer": "Chris Bale", "items": {"product": "fork","qty": 5}}'),
('{ "customer": "Mike Stuart", "items": {"product": "spatula","qty": 2}}');
```

This will insert data values where `orders_Detail`has the following keys:

* `customer`: it will store a customer’s data who purchased the product.
* `items`: it will store the order details, `product` & `qty`.

### 3. Retrieve Data

Use the `SELECT` command to retrieve the orders table's data.

```sql  theme={null}
SELECT * FROM orders;
```

You will get the following output:

```sql  theme={null}
+--------------------------------------------------------------------------+
| orders_detail                                                            | 
+--------------------------------------------------------------------------+
| {"customer":"Dean Smith","items":{"qty":2.000000,"product":"cup"}}       |
| {"customer":"Sissy Kate","items":{"product":"knife","qty":1.000000}}     |                                                        
| {"customer":"Emma Stone","items":{"qty":4.000000,"product":"spoon"}}     |
| {"customer":"Chris Bale","items":{"product":"fork","qty":5.000000}}      |
| {"customer":"Mike Stuart","items":{"qty":2.000000,"product":"spatula"}}  |
+--------------------------------------------------------------------------+
```

<Tip>It is normal for the JSON type’s result to look disordered.</Tip>
