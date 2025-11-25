# Source: https://docs.oxla.com/sql-reference/sql-data-types/bool.md

# Bool

## **Overview**

A `BOOL` is a data type mainly used for expressions that will return only two possible values, `true` and `false`.

<Info>Bool is stored as a bitmap in `u64` values.</Info>

<Warning>**BOOLEAN** is an alias for the **BOOL** data type. You can create a table using **BOOLEAN**. However, it will be stored and processed equivalently to **BOOL**.</Warning>

## Format

* `FALSE`
* `TRUE`

## **Examples**

Below are a few examples of using a bool data type:

### Case #1: Create a Table

A librarian will create a **borrowBook** table that he will use to store book borrowing data. The table comprises the borrowed ID, the book name, the borrower, and the book's returned status, which uses the **bool** data type.

```sql  theme={null}
CREATE TABLE borrowBook  (  
   borrowID INT, 
   bookName TEXT,
   borrower TEXT,
   returnedStat BOOL NOT NULL  
);  
INSERT INTO borrowBook (borrowID,bookName, borrower, returnedStat)  
VALUES  
    (101, 'The Silent Patient', 'Mike', TRUE),  
    (201, 'Malibu Rising', 'Jean', TRUE),  
    (301, 'The Guest List', 'Mark', FALSE),  
    (401, 'The Four Winds', 'Cliff', TRUE),  
    (501, 'The Vanishing Half: A Novel', 'Sarah', TRUE),  
    (601, 'Red, White & Royal Blue', 'Anna', FALSE),  
    (701, 'The Duke and I', 'Blake', FALSE),  
    (801, 'The Lord of the Rings', 'Sandra', FALSE);  
```

The **borrowBook** table has been successfully created after executing the above query:

```sql  theme={null}
COMPLETE
INSERT 0 8
```

### Case #2: Display the Table

Run the `SELECT` statement to get all records from the **borrowBook** table:

```sql  theme={null}
SELECT * FROM borrowBook;
```

It will return the result as displayed below:

```sql  theme={null}
+-----------+---------------------------------+------------+---------------+
| borrowid  | bookname                        | borrower   | returnedstat  |
+-----------+---------------------------------+------------+---------------+
| 101       | The Silent Patient              | Mike       | t             |
| 201       | Malibu Rising                   | Jean       | t             |
| 301       | The Guest List                  | Mark       | f             |
| 401       | The Four Winds                  | Cliff      | t             |
| 501       | The Vanishing Half: A Novel     | Sarah      | t             |
| 601       | Red, White & Royal Blue         | Anna       | f             |
| 701       | The Duke and I                  | Blake      | f             |
| 801       | The Lord of the Rings           | Sandra     | f             |
+-----------+---------------------------------+------------+---------------+
```

### Case #3: List of the Returned Books

In the below example, the following statement is used to retrieve all the **books** that have already been returned:

```sql  theme={null}
SELECT * FROM borrowbook       
WHERE returnedstat= 'true';
```

We will get the following results:

```sql  theme={null}
+-----------+---------------------------------+------------+---------------+
| borrowid  | bookname                        | borrower   | returnedstat  |
+-----------+---------------------------------+------------+---------------+
| 101       | The Silent Patient              | Mike       | t             |
| 201       | Malibu Rising                   | Jean       | t             |
| 401       | The Four Winds                  | Cliff      | t             |
| 501       | The Vanishing Half: A Novel     | Sarah      | t             |
+-----------+---------------------------------+------------+---------------+
```

### Case #4: List of the Unreturned Books

Now, we will acquire all of the book records that haven’t been returned yet by running the `SELECT` statement with a specified `WHERE` condition as `false`:

```sql  theme={null}
SELECT * FROM borrowbook       
WHERE returnedstat= 'false'; 
```

We will get the following results:

```sql  theme={null}
+-----------+---------------------------------+------------+---------------+
| borrowid  | bookname                        | borrower   | returnedstat  |
+-----------+---------------------------------+------------+---------------+
| 301       | The Guest List                  | Mark       | f             |
| 601       | Red, White & Royal Blue         | Anna       | f             |
| 701       | The Duke and I                  | Blake      | f             |
| 801       | The Lord of the Rings           | Sandra     | f             |
+-----------+---------------------------------+------------+---------------+
```

### Case #5: Check a Book’s Return Status

In this example, we are going to figure out the returned status of the book **“The Lord of the Rings”** by executing the `SELECT` statement with a specified column in the `WHERE` clause:

```sql  theme={null}
SELECT * FROM borrowbook  
WHERE bookname = 'The Lord of the Rings';
```

The above query will filter all records based on the specified conditions, and we know that Sandra hasn’t returned the book yet:

```sql  theme={null}
+-----------+---------------------------------+------------+---------------+
| borrowid  | bookname                        | borrower   | returnedstat  |
+-----------+---------------------------------+------------+---------------+
| 801       | The Lord of the Rings           | Sandra     | f             |
+-----------+---------------------------------+------------+---------------+
```
