# Source: https://render.com/docs/postgresql-performance-troubleshooting.md

# Troubleshooting Render Postgres Performance

You might observe performance issues with your database as it grows in size, query complexity, and connection count. If you do, use these tips to help diagnose and resolve the underlying cause.

## Identify long-running queries

Long-running queries can degrade performance by monopolizing shared compute resources and locks required by other operations. Some of these might be "runaway" queries (such as a `SELECT *` against a very large table without a `LIMIT`), while others might require more nuanced optimization.

Run the following query on your instance to fetch all of its actively running processes, ordered by age (oldest first):

```sql
WITH activity_with_age AS (
    SELECT
        pid,
        usename AS user,
        application_name AS app_name,
        query,
        CASE WHEN state = 'active'
            THEN NOW() - query_start
            ELSE NULL
        END AS query_age,
        query_start,
        state,
        wait_event_type,
        wait_event
    FROM pg_stat_activity
    WHERE query != current_query()
)
SELECT * FROM activity_with_age
WHERE
    state = 'active'

    -- Uncomment the following condition to hide queries
    -- that started only within the last five minutes.
    -- AND query_age > '5 minutes'::interval
ORDER BY
    query_age DESC,
    pid;
```

Again, this query shows only _active_ processes. To show _all_ processes, remove the `state = 'active'` condition. Inactive processes include processes that are awaiting a new command from a user, either inside or outside of a transaction.

The `pg_stat_activity` view queried above contains [several other columns](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW), but here we're fetching the data that provides the most utility for common troubleshooting scenarios:

------

###### Field

`pid`

###### Description

The unique _process identifier_ for each running process. This identifier is specific to the PostgreSQL instance and is distinct from the PID of the associated operating system process. As a last resort, you can terminate a misbehaving query by providing its `pid` to the following: ```sql
SELECT pg_terminate_backend(PID_GOES_HERE);
```

---

###### Field

`app_name`

###### Description

A free-form tag used to identify the _source application_ of a particular client.

- For clients connecting to the instance directly via a shell, this value is usually the name of the tool (such as `psql` or `pgcli`).
- For application clients, this value is empty by default, but can (*and should!*) be supplied on the connection string (e.g., `postgresql://myuser@my-host:5432/mydb?application_name=myapp`).

---

###### Field

`state`

###### Description

The _current state_ of the backend process. This value is `active` when the backend is currently in the process of executing a particular query and `idle` when the backend is awaiting a new user request. This value is `idle in transaction` or `idle in transaction (aborted)` when the backend is awaiting a user request within an existing transaction context. In the case of `idle in transaction (aborted)`, the transaction encountered an error in a previous query and has been rolled back.

---

###### Field

`query`

###### Description

For client backend processes, this is the _exact text of the most recent query executed_ by the process.

- This is the query that's _currently_ executing, if any.
- By default, this value is truncated to 1024 characters (you can extend it by setting `track_activity_query_size`).
- This value is empty for background processes.

---

###### Field

`query_age`

###### Description

This alias contains the _age of the active query_, instead of the age of its associated transaction or process. We report the age of any _active_ query, but _not_ the time since an _idle_ query started. This partitions the output into active and inactive sections, which is helpful because long-running active queries are more likely to be of interest when querying this view.

---

###### Field

`wait_event_type` and `wait_event`

###### Description

For an `active` backend, the wait event type indicates _whether query processing is blocked_ on some type of event. The specific event is unique to the specified wait event type (such as reading from disk or waiting on a lock).

------

### Example output

The following example output lists client backend processes where `state = active` (query strings are omitted for brevity):

*Show example output*

```
  pid  | app_name |       state         |      query      |          query_start          |    query_age    | wait_event_type |   wait_event
-------+----------+---------------------+----------------------------------+--------------------------------+-----------------+---------------
 34067 | sample   | active              | ... omitted ... | 2024-02-23 14:57:37.913643-08 | 00:00:06.951026 | Lock            | transactionid
 34087 | sample   | active              | ... omitted ... | 2024-02-23 14:57:41.017026-08 | 00:00:03.847643 | Lock            | transactionid
 34083 | sample   | active              | ... omitted ... | 2024-02-23 14:57:42.057243-08 | 00:00:02.807426 | Lock            | transactionid
 34081 | sample   | active              | ... omitted ... | 2024-02-23 14:57:42.087726-08 | 00:00:02.776943 | Lock            | transactionid
 34095 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.112994-08 | 00:00:01.751675 | Lock            | transactionid
 34102 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.199889-08 | 00:00:01.664780 | Lock            | transactionid
 33998 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.648030-08 | 00:00:01.216639 | Lock            | transactionid
 34103 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.676188-08 | 00:00:01.188481 | Lock            | transactionid
 34104 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.739067-08 | 00:00:01.125602 | Lock            | transactionid
 34105 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.758841-08 | 00:00:01.105828 | Lock            | transactionid
 34106 | sample   | active              | ... omitted ... | 2024-02-23 14:57:43.794574-08 | 00:00:01.070095 | [NULL]          | [NULL]
 34059 | sample   | active              | ... omitted ... | 2024-02-23 14:57:44.369805-08 | 00:00:00.494864 | [NULL]          | [NULL]
 32902 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.238136-08 | 00:00:00.378974 | [NULL]          | [NULL]
 33104 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.252764-08 | 00:00:00.364346 | IO              | DataFileRead
 33254 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.339483-08 | 00:00:00.277627 | [NULL]          | [NULL]
 33101 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.404558-08 | 00:00:00.212552 | LWLock          | BufferMapping
 33407 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.554408-08 | 00:00:00.062702 | [NULL]          | [NULL]
 33406 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.554408-08 | 00:00:00.062702 | [NULL]          | [NULL]
 33233 | sample   | active              | ... omitted ... | 2024-02-23 14:52:42.582867-08 | 00:00:00.034318 | IPC             | BufferIO
 33409 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.612342-08 | 00:00:00.004768 | [NULL]          | [NULL]
 33393 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.612342-08 | 00:00:00.004768 | [NULL]          | [NULL]
 33043 | sample   | active              | ... omitted ... | 2024-02-23 14:52:41.621739-08 | 00:00:00.000475 | Client          | ClientRead
 33412 | sample   | active              | ... omitted ... | 2024-02-23 14:52:43.617272-08 | 00:00:00.000162 | [NULL]          | [NULL]
```

Out of the 23 listed clients:

- 9 are currently processing on the CPU (`wait_event_type` is `NULL`).
- 11 are waiting for a lock.
- 2 are waiting on the buffer manager paging in data to `shared_buffers`.
- 1 is feeding data back to the client.

An `active` query with a specified [`wait_event_type`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE) might be in one of several states, most commonly:

- [`Client`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-CLIENT-TABLE), indicating that the query is expecting data to be read from or written to the client connection
- [`IO`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-IO-TABLE), indicating a blocking access to disk
- [`IPC`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-IPC-TABLE), indicating communication between parallel processes
- [`Lock`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-LOCK-TABLE) or [`LWLock`](https://www.PostgreSQL.org/docs/current/monitoring-stats.html#WAIT-EVENT-LWLOCK-TABLE), indicating that a table or row lock required by this query is currently held

## Identify active queries that are blocking other queries

Concurrent queries running on the same tables or rows can sometimes cause lock contention. If your queries are taking longer than expected to complete, run the following to fetch all queries that are currently blocked on _another_ query:

```sql
SELECT
    blocker.pid AS blocking_pid,
    blocker.query AS blocking_query,
    blocker.usename AS blocking_user,
    blocker.application_name AS blocking_app_name,
    blocked.pid AS blocked_pid,
    blocked.query AS blocked_query,
    blocked.usename AS blocked_user,
    blocked.application_name AS blocked_app_name
FROM pg_stat_activity AS blocked
JOIN pg_stat_activity AS blocker ON blocker.pid = ANY(pg_blocking_pids(blocked.pid))
ORDER BY
    blocker.query_start DESC;
```

### Example output

The following example output lists three currently blocked queries (query strings are omitted for brevity):

```
 blocking_pid | blocking_query | blocking_user   | blocking_app_name | blocked_pid | blocked_query | blocked_user | blocked_app_name
--------------+----------------+-----------------+-------------------+-------------+---------------+--------------+------------------
 311124       | ...omitted...  | user@render.com | psql              | 313674      | ...omitted... | postgres     | sample
 311124       | ...omitted...  | user@render.com | psql              | 344684      | ...omitted... | postgres     | sample
 313674       | ...omitted...  | postgres        | sample            | 344684      | ...omitted... | postgres     | sample
```

For each row, the `blocking_` columns show details about a query that's currently holding a lock, and the `blocked_` columns show details about a query that's _waiting_ on that lock.

In this result set, a query issued by `user@render.com` from a `psql` shell is blocking two queries running from an app called `sample`. Additionally, one of the blocked queries running from `sample` is blocking the other, forming a queue.

If you notice that one particular backend process is blocking many others, you can terminate it with `pg_terminate_backend` as shown [here](#pid). We recommend using this strategy only in emergencies.

## Examine query plans

If a particular query is taking longer than expected to run, you can use the `EXPLAIN` command to understand how PostgreSQL is evaluating that query:

```sql
EXPLAIN <query>;
```

`EXPLAIN` returns a *query plan*, which is a text representation of the algorithm PostgreSQL will follow to execute the query. Details of a query plan include:

- Which tables to gather data from
- Which join order and strategy to use to combine data from multiple tables
- At which point result sets are filtered by a condition or sorted for output

In addition to running `EXPLAIN`, you can also run `EXPLAIN ANALYZE` to sample the actual execution time for each step in the query plan. Examples of both are provided below.

> *Query plans for the same query can differ significantly between environments.*
>
> This is because PostgreSQL takes your data's size and distribution into account when selecting a query plan that maximizes its efficiency. For the best results, run `EXPLAIN` in the same environment where you're experiencing performance issues.

The sections below use the following example query, executed in Render's own staging environment:

```sql
SELECT id, database_id, name
FROM postgres_dbs
WHERE deleted_at IS NULL
ORDER BY created_at DESC
LIMIT 200;
```

### Example `EXPLAIN` output

Running `EXPLAIN <query>` with the example query above yields the following query plan:

```
                                               QUERY PLAN
---------------------------------------------------------------------------------------------------------
 Limit  (cost=1070.71..1071.21 rows=200 width=68)
   ->  Sort  (cost=1070.71..1071.38 rows=270 width=68)
         Sort Key: postgres_dbs.created_at DESC
         ->  Bitmap Heap Scan on postgres_dbs  (cost=181.69..1059.81 rows=270 width=68)
               Recheck Cond: (deleted_at IS NULL)
               ->  Bitmap Index Scan on postgres_dbs_owner_id_name  (cost=0.00..181.62 rows=270 width=0)
(6 rows)

Time: 63.931 ms
```

Each line in the query plan with a listed `cost` represents a step in the execution process (other lines provide additional context for these steps). Steps with the largest indent level are executed _first_.

Based on this query plan, PostgreSQL performs the following steps in order:

1. *Bitmap Index Scan*: PostgreSQL first reads from the `postgres_dbs_owner_id_name` index (a [partial index](https://www.postgresql.org/docs/current/indexes-partial.html)) to mark candidate _pages_ (groups of rows) that need to be read.
2. *Bitmap Heap Scan*: PostgreSQL goes through each of the marked pages and returns the rows that match the `Recheck Cond`. This is necessary because each candidate page contains rows that belong to the index, but might _also_ contain rows that don't (which require a post-filter).
3. *Sort*: PostgreSQL sorts the results from the heap scan by the `created_at` column in descending order.
4. *Limit*: PostgreSQL reads the first 200 rows from the sorted result set. The remainder of the rows are discarded.

### Example `EXPLAIN ANALYZE` output

> *Because `EXPLAIN ANALYZE` actually executes its query, any side effects of that query also occur.*
>
> Avoid running `EXPLAIN ANALYZE` for `INSERT`, `UPDATE`, or `DELETE` queries on a production database.

Running `EXPLAIN ANALYZE <query>` with the example query above yields the same query plan _and also executes that plan_ to gather exact timing and row details:

```
                                                                      QUERY PLAN
------------------------------------------------------------------------------------------------------------------------------------------------------
 Limit  (cost=1070.71..1071.21 rows=200 width=68) (actual time=1.493..1.522 rows=200 loops=1)
   ->  Sort  (cost=1070.71..1071.38 rows=270 width=68) (actual time=1.492..1.506 rows=200 loops=1)
         Sort Key: postgres_dbs.created_at DESC
         Sort Method: quicksort  Memory: 61kB
         ->  Bitmap Heap Scan on postgres_dbs  (cost=181.69..1059.81 rows=270 width=68) (actual time=0.411..1.423 rows=268 loops=1)
               Recheck Cond: (deleted_at IS NULL)
               Heap Blocks: exact=213
               ->  Bitmap Index Scan on postgres_dbs_owner_id_name  (cost=0.00..181.62 rows=270 width=0) (actual time=0.343..0.344 rows=3560 loops=1)
 Planning Time: 0.150 ms
 Execution Time: 1.574 ms
(10 rows)

Time: 65.136 ms
```

This output resembles the [`EXPLAIN` output](#example-explain-output) above, but it includes additional details:

- The `actual time` for each step of the query execution
- The actual number of `rows` returned from each step
- The total `Execution Time` for the query

Note that `cost` remains an estimate (use this value to compare the efficiency of two query plans).

## Case studies

To see how these queries can be used in a real debugging scenario, read our case studies. We'll be adding to this list over time:

- [A simple query with a big problem](/blog/postgresql-simple-query-big-problem)
- [From slow query to fast—via stats](/blog/postgresql-slow-query-to-fast-via-stats)
- [Taking random samples from big tables](/blog/postgresql-random-samples-big-tables)