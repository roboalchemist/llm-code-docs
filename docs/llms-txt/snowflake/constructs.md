# Source: https://docs.snowflake.com/en/sql-reference/constructs.md

# Query syntax

Snowflake supports querying using standard [SELECT](sql/select.md) statements and the following basic syntax:

```sqlsyntax
[ WITH ... ]
SELECT
  [ TOP <n> ]
   ...
[ INTO ... ]
[ FROM ...
   [ AT | BEFORE ... ]
   [ CHANGES ... ]
   [ CONNECT BY ... ]
   [ JOIN ... ]
   [ ASOF JOIN ... ]
   [ LATERAL ... ]
   [ MATCH_RECOGNIZE ... ]
   [ PIVOT | UNPIVOT ... ]
   [ VALUES ... ]
   [ SAMPLE ... ]
   [ RESAMPLE ... ]
   [ SEMANTIC_VIEW( ... ) ] ]
[ WHERE ... ]
[ GROUP BY ... ]
[ HAVING ... ]
[ QUALIFY ... ]
[ ORDER BY ... ]
[ LIMIT ... ]
[ FOR UPDATE ... ]
```

**Next Topics:**

* [WITH](constructs/with.md)
* [TOP <n>](constructs/top_n.md)
* [INTO](constructs/into.md)
* [FROM](constructs/from.md)

  * [AT | BEFORE](constructs/at-before.md)
  * [CHANGES](constructs/changes.md)
  * [CONNECT BY](constructs/connect-by.md)
  * [JOIN](constructs/join.md)
  * [ASOF JOIN](constructs/asof-join.md)
  * [LATERAL](constructs/join-lateral.md)
  * [MATCH_RECOGNIZE](constructs/match_recognize.md)
  * [PIVOT](constructs/pivot.md)
  * [UNPIVOT](constructs/unpivot.md)
  * [VALUES](constructs/values.md)
  * [SAMPLE / TABLESAMPLE](constructs/sample.md)
  * [RESAMPLE](constructs/resample.md)
  * [SEMANTIC_VIEW](constructs/semantic_view.md)
* [WHERE](constructs/where.md)
* [GROUP BY](constructs/group-by.md)

  * [GROUP BY CUBE](constructs/group-by-cube.md)
  * [GROUP BY GROUPING SETS](constructs/group-by-grouping-sets.md)
  * [GROUP BY ROLLUP](constructs/group-by-rollup.md)
  * [HAVING](constructs/having.md)
* [QUALIFY](constructs/qualify.md)
* [ORDER BY](constructs/order-by.md)
* [LIMIT / FETCH](constructs/limit.md)
* [FOR UPDATE](constructs/for-update.md)
