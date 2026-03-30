# Source: https://docs.snowflake.com/en/sql-reference/constructs/for-update.md

Categories:
:   [Query syntax](../constructs.md)

# FOR UPDATE

Locks the rows that the query selects until the transaction that contains the query commits or
aborts.

This clause is supported for use with hybrid tables only, and is useful for transactional
workloads in which multiple transactions attempt to access the same rows at the same time.
Rows are locked for update in the sense that other transactions cannot write data to these
rows until the transaction doing the locking has been fully committed or rolled back.
However, other transactions can read the locked rows, and other rows in the same table can be
read, updated, or deleted.

```sqlsyntax
SELECT ...
  FROM ...
  [ ... ]
  FOR UPDATE [ NOWAIT | WAIT <wait_time> ]
```

## Parameters

`NOWAIT`
:   Returns an error if the transaction cannot lock the selected rows immediately.
    NOWAIT is the default.

`WAIT wait_time`
:   Specifies the maximum time (in seconds) that the query waits to acquire row-level locks. If
    the wait time expires, the query returns an error.

## Restrictions

The FOR UPDATE clause:

* Cannot be used with [AUTOCOMMIT transactions](../parameters.md).
* Must be the last clause in the [SELECT statement](../constructs.md).
* Cannot be used in a [CTAS statement](../sql/create-table.md).
* Cannot be used inside [subqueries](../../user-guide/querying-subqueries.md).
* Cannot select from [multiple tables (joins)](join.md) or
  [set operations](../operators-query.md).
* Cannot be used when the query contains:

  * [DISTINCT](../../user-guide/querying-distinct-counts.md)
  * [Aggregation functions](../functions-aggregation.md)
  * [GROUP BY](group-by.md)
  * [HAVING](having.md)
  * [Sequences](../../user-guide/querying-sequences.md)

## Usage notes

Because hybrid tables support the READ COMMITTED isolation level, FOR UPDATE clauses do not
guarantee read stability. For example, assume that a table `T` with a single column named `ID`
contains two rows with values `5` and `10`.

1. The following query is run in transaction `T1`:

   ```sqlexample
   SELECT * FROM T WHERE ID < 20 FOR UPDATE;
   ```

   The query returns the values `5` and `10` and locks those two rows.
2. Another transaction, `T2`, runs the following DELETE operation:

   ```sqlexample
   DELETE FROM T WHERE ID = 5;
   ```

   Transaction `T2` has to wait until `T1` completes (that is, until it commits or rolls back).
3. However, a third transaction, `T3`, can complete the following INSERT operation:

   ```sqlexample
   INSERT INTO T VALUES 12;
   ```

4. A subsequent query in `T1` now returns three values (rows), not two: `5`, `10`, and `12`:

   ```sqlexample
   SELECT * FROM T WHERE ID < 20;
   ```

## Examples

Open a new transaction, select all of the rows from a hybrid table (`ht`), and lock those
rows until the transaction commits. Update some selected rows and run another query before
committing the transaction.

```sqlexample
BEGIN;
...
SELECT * FROM ht ORDER BY c1 FOR UPDATE;
...
UPDATE ht set c1 = c1 + 10 WHERE c1 = 0;
...
SELECT ... ;
...
COMMIT;
```

Apply a maximum wait time of 60 seconds for row locking:

```sqlexample
BEGIN;
...
SELECT * FROM ht FOR UPDATE WAIT 60;
...
COMMIT;
```
