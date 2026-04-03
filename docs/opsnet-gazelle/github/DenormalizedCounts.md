# Denormalized Counts

**Orpheus Development Papers #2 - Denormalized Totals**
Version 1 | From: Spine | Date: 2020-08-04

## Overview

Certain tables in Gazelle precompute and store totals in parent tables to avoid
computing `count(*)` repeatedly. This is done by starting from zero and updating
with +1 or -1 when rows are inserted or deleted from child tables.

In production this works well, but during development values can drift out of
sync due to code errors. To correct totals, run `count(*)` on child tables and
update parent tables when results differ.

## Maintenance Queries

### collages_artists

```sql
SELECT c.ID, c.NumTorrents, count(ca.CollageID) as n
FROM collages_artists ca
INNER JOIN collages c ON (c.ID = ca.CollageID)
GROUP BY c.ID
HAVING c.NumTorrents != count(ca.CollageID);
```

Example result:

| ID  | NumTorrents | n |
|-----|-------------|---|
| 101 |           3 | 4 |
| 104 |           5 | 3 |

```sql
UPDATE collages c INNER JOIN (
    SELECT c.ID, c.NumTorrents, count(ca.CollageID) as n
    FROM collages_artists ca
    INNER JOIN collages c ON (c.ID = ca.CollageID)
    GROUP BY c.ID
    HAVING c.NumTorrents != count(ca.CollageID)
) FIX USING (ID)
SET c.NumTorrents = FIX.n;
```

### collages_torrents

```sql
SELECT c.ID, c.NumTorrents, count(ct.CollageID) as n
FROM collages_torrents ct
INNER JOIN collages c ON (c.ID = ct.CollageID)
GROUP BY c.ID
HAVING c.NumTorrents != count(ct.CollageID);
```

```sql
UPDATE collages c INNER JOIN (
    SELECT c.ID, c.NumTorrents, count(ct.CollageID) as n
    FROM collages_torrents ct
    INNER JOIN collages c ON (c.ID = ct.CollageID)
    GROUP BY c.ID
    HAVING c.NumTorrents != count(ct.CollageID)
) FIX USING (ID)
SET c.NumTorrents = FIX.n;
```

### forums_topics

```sql
SELECT ft.ID, ft.NumPosts, count(fp.ID)
FROM forums_posts fp
INNER JOIN forums_topics ft ON (ft.ID = fp.TopicID)
GROUP BY ft.ID
HAVING ft.NumPosts != count(fp.ID);
```

Update logic is left as an exercise for the reader.

## Finding Other Tables Needing Maintenance

```sql
SELECT table_name, column_name
FROM information_schema.columns
WHERE table_schema = 'gazelle'
    AND column_name LIKE 'Num%';
```
