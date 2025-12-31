# Source: https://docs.oxla.com/sql-reference/sql-mutations/update.md

# UPDATE

## **Overview**

The `UPDATE` mutation is used to modify the existing records in a table. This support has limitations:

* Only **one data mutation (DELETE or UPDATE)** at given moment is possible, trying to run another one will result in failure.
* Data mutations rewrite all files containing the data from the UPDATE/DELETE condition. Please note that running `DELETE from table` without any condition is possible, but it will be much slower than just `DROP TABLE table`.
* The syntax is simplified in comparison to Postgres. For example, the `SET column=<value>` operation doesn’t support sub-SELECT as the value, also the `WHERE` clause cannot contain sub-SELECT.

<Check>**Feature Update: Initial Release**. <br />
This marks the initial release of our new Mutation feature, providing you with the ability to update data. The Mutations involve rewriting entire files which take several minutes and could generate infrastructure costs. We are aiming to enhance and optimize this feature in future updates!</Check>

## Syntax

The syntax for `UPDATE` mutation is as follows:

```sql  theme={null}
UPDATE table
SET column1 = expression1,
    column2 = expression2
    ...
WHERE conditions;
```

In this syntax:

* `table`: The name of the table you want to update.
* `column1, column2`: The columns that you wish to update.
* `expression1, expression2`: The new values to assign to column1, column2, and so on. Each column is set to its corresponding expression.
* `WHERE conditions` **(Optional)**: The conditions that must be met for the update to execute. If no conditions are provided, all table records will be updated.

## Examples

Let's create a sample table called tasks:

```sql  theme={null}
CREATE TABLE tasks (
    task_id INT,
    task_name TEXT,
    status TEXT
);

INSERT INTO tasks (task_id, task_name, status)
VALUES
    (1001, 'Task A', 'pending'),
    (1002, 'Task B', 'in-progress'),
    (1003, 'Task C', 'pending');
```

The tasks table will be created as shown below:

```sql  theme={null}
 task_id | task_name |   status    
---------+-----------+-------------
    1001 | Task A    | pending
    1002 | Task B    | in-progress
    1003 | Task C    | pending
```

Now, let's see the following cases for updating the table:

### Case #1: Update a Single Column

1. In this case, we want to update the `status` column to “completed” for the record where `task_id` is 1001.

```sql  theme={null}
UPDATE tasks
SET status = 'completed'
WHERE task_id = 1001;
```

2. The output below shows that the update was successful.

```sql  theme={null}
UPDATE
```

3. Check the updated table by running the `SELECT` query below:

```sql  theme={null}
SELECT * FROM tasks;
```

4. The `UPDATE` mutation updates the status to “completed” for the task with ID 1001.

```sql  theme={null}
 task_id | task_name |   status    
---------+-----------+-------------
    1001 | Task A    | completed
    1002 | Task B    | in-progress
    1003 | Task C    | pending
```

### Case #2: Update Multiple Columns

1. Let’s assume we want to update the `task_name` and `status` columns for the record where `task_id` is 1002.

```sql  theme={null}
UPDATE tasks
SET task_name = 'Updated Task B',
    status = 'completed'
WHERE task_id = 1002;
```

2. The output below shows that the update was successful.

```sql  theme={null}
UPDATE
```

3. Check the updated table by running the `SELECT` query below:

```sql  theme={null}
SELECT * FROM tasks;
```

4. Here, the task name and status columns are updated for the task with ID 1002.

```sql  theme={null}
 task_id |   task_name    |  status   
---------+----------------+-----------
    1001 | Task A         | completed
    1002 | Updated Task B | completed
    1003 | Task C         | pending
```
