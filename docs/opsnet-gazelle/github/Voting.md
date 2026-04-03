# Voting Implementation

**Orpheus Development Papers #3 - Voting Implementation**
Version 2 | From: Spine | Date: 2020-11-28

## Overview

When a person upvotes or downvotes a release group, that information is recorded
in the `users_votes` table (user id, group id, direction and timestamp).

The aggregate votes for a release group are denormalized and stored in the
`torrents_votes` table. For the purpose of scoring, the algorithm looks at total
positive votes compared to overall votes.

For example, if a torrent has received two downvotes and three upvotes, there
will be 5 rows (from the five voters) in the `users_votes` table, and the
`torrents_votes` table will contain one row with `Total = 5`, `Ups = 3`.

If the `torrents_votes` table is ever corrupted, it may be recreated with:

```bash
bin/rebuild-votes
```

There is some discrepancy in the code between the above formula and the use of
`binomial_ci(Ups, Total)`.

The user and group vote information are both cached. As the user object can
become quite large, care must be taken to update the cache on writes. This is
probably one of the few places where it is too expensive to simply delete the
key and rely on the next read to refresh it.

## Vote Tables

### Table 1: Upvotes by user

```sql
SELECT UserID, group_concat(GroupID ORDER BY GroupID) AS upvotes
FROM users_votes WHERE Type = 'Up' GROUP BY UserID;
```

| UserID | upvotes                              |
|--------|--------------------------------------|
|      1 | 14,27,30,31,54,68,71,73,78           |
|      2 | 6,14,49,64,69,70                    |
|      6 | 14,46,54,58,64                      |

### Table 2: Downvotes by user

```sql
SELECT UserID, group_concat(GroupID ORDER BY GroupID) AS downvotes
FROM users_votes WHERE Type = 'Down' GROUP BY UserID;
```

| UserID | downvotes    |
|--------|-------------|
|      1 | 58,60,69,72 |
|      2 | 21,30,60,73 |
|      6 | 31,68,69    |

### Table 3: Votes by release group

| GroupID | Ups | Total |
|---------|-----|-------|
|       6 |   1 |     1 |
|      14 |   3 |     3 |
|      21 |   0 |     1 |
|      27 |   1 |     1 |
|      30 |   1 |     2 |
|      31 |   1 |     2 |
|      46 |   1 |     1 |
|      49 |   1 |     1 |
|      54 |   2 |     2 |
|      58 |   1 |     2 |
|      60 |   0 |     2 |
|      64 |   2 |     2 |
|      68 |   1 |     2 |
|      69 |   1 |     3 |
|      70 |   1 |     1 |
|      71 |   1 |     1 |
|      72 |   0 |     1 |
|      73 |   1 |     2 |
|      78 |   1 |     1 |

## "People Who Liked X Also Liked Y"

A further denormalization takes place entirely within the cache,
to implement the "people who liked X also liked Y" functionality. This can be
expressed as: "Get the list of people who upvoted this group and see what other
groups they upvoted".

### Example: Group 58

For group 58 (upvoted by user 6), the algorithm:

```sql
SELECT v.GroupID, sum(if(v.Type = 'Up', 1, 0)) AS Ups, count(*) AS Total
FROM users_votes AS v
INNER JOIN (
    SELECT UserID FROM users_votes WHERE Type = 'Up' AND GroupID = 58
) AS a USING (UserID)
WHERE v.GroupID != 58
GROUP BY v.GroupID
HAVING Ups > 0;
```

Table 4: Vote scores for groups other than 58 also upvoted by user 6

| GroupID | Ups | Total |
|---------|-----|-------|
|      14 |   1 |     1 |
|      46 |   1 |     1 |
|      54 |   1 |     1 |
|      64 |   1 |     1 |

As user 6 is the only person who upvoted group 58, the "X likes Y" for that
group consists of only their other (non-group-58) upvotes.

### Adding More Upvoters

At a later point, user 2 also upvotes group 58. The "X likes Y" now consists of
the upvotes from users 2 and 6:

Table 5: Other groups than 58 also upvoted by users 2, 6

| GroupID | Ups | Total |
|---------|-----|-------|
|       6 |   1 |     1 |
|      14 |   2 |     2 |
|      46 |   1 |     1 |
|      49 |   1 |     1 |
|      54 |   1 |     1 |
|      64 |   2 |     2 |
|      69 |   1 |     2 |
|      70 |   1 |     1 |

The difference between Table 4 and Table 5 is the addition of the upvotes by
user 2 (6,14,49,64,69,70). This creates new rows for groups 6, 49, 69 and 70,
and increments the existing scores for 14 and 64 that both users voted on.

### Known Issue

User 6 downvoted group 58, and won't be factored into the vote scores... but
they too have also downvoted release 69. This means the scores for both 58 and
69 are higher than they should be.

To correct this, the `Type = 'Up'` is removed from the inner select query,
which includes all votes (up and down):

Table 6: Any groups paired with a vote on group 58

```sql
SELECT v.GroupID, sum(if(v.Type = 'Up', 1, 0)) AS Ups, count(*) AS Total
FROM users_votes AS v
INNER JOIN (SELECT UserID FROM users_votes WHERE GroupID = 58) AS a USING (UserID)
WHERE v.GroupID != 58
GROUP BY v.GroupID
HAVING Ups > 0;
```

| GroupID | Ups | Total |
|---------|-----|-------|
|       6 |   1 |     1 |
|      14 |   3 |     3 |
|      27 |   1 |     1 |
|      30 |   1 |     2 |
|      31 |   1 |     2 |
|      46 |   1 |     1 |
|      49 |   1 |     1 |
|      54 |   2 |     2 |
|      64 |   2 |     2 |
|      68 |   1 |     2 |
|      69 |   1 |     3 |
|      70 |   1 |     1 |
|      71 |   1 |     1 |
|      73 |   1 |     2 |
|      78 |   1 |     1 |

### Binomial Confidence Interval

Adding the binomial score makes the picture clearer.

Table 7: Binomial score from users who upvoted 58

```sql
SELECT v.GroupID,
    sum(if(v.Type = 'Up', 1, 0)) AS Ups,
    count(*) AS Total,
    binomial_ci(sum(if(v.Type = 'Up', 1, 0)), count(*)) AS score
FROM users_votes AS v
INNER JOIN (
    SELECT UserID FROM users_votes WHERE Type = 'Up' AND GroupID = 58
) AS a USING (UserID)
WHERE v.GroupID != 58
GROUP BY v.GroupID
HAVING Ups > 0
ORDER BY score DESC, v.GroupID DESC;
```

| GroupID | Ups | Total | score    |
|---------|-----|-------|----------|
|      64 |   2 |     2 | 0.424928 |
|      14 |   2 |     2 | 0.424928 |
|      70 |   1 |     1 | 0.269784 |
|      54 |   1 |     1 | 0.269784 |
|      49 |   1 |     1 | 0.269784 |
|      46 |   1 |     1 | 0.269784 |
|       6 |   1 |     1 | 0.269784 |
|      69 |   1 |     2 | 0.120834 |

Versus:

Table 8: Binomial score from users who voted either way on 58

```sql
SELECT v.GroupID,
    sum(if(v.Type = 'Up', 1, 0)) AS Ups,
    count(*) AS Total,
    binomial_ci(sum(if(v.Type = 'Up', 1, 0)), count(*)) AS score
FROM users_votes AS v
INNER JOIN (
    SELECT UserID FROM users_votes WHERE GroupID = 58
) AS a USING (UserID)
WHERE v.GroupID != 58
GROUP BY v.GroupID
HAVING Ups > 0
ORDER BY score DESC, v.GroupID DESC;
```

| GroupID | Ups | Total | score     |
|---------|-----|-------|-----------|
|      14 |   3 |     3 |  0.525699 |
|      64 |   2 |     2 |  0.424928 |
|      54 |   2 |     2 |  0.424928 |
|      78 |   1 |     1 |  0.269784 |
|      71 |   1 |     1 |  0.269784 |
|      70 |   1 |     1 |  0.269784 |
|      49 |   1 |     1 |  0.269784 |
|      46 |   1 |     1 |  0.269784 |
|      27 |   1 |     1 |  0.269784 |
|       6 |   1 |     1 |  0.269784 |
|      73 |   1 |     2 |  0.120834 |
|      68 |   1 |     2 |  0.120834 |
|      31 |   1 |     2 |  0.120834 |
|      30 |   1 |     2 |  0.120834 |
|      69 |   1 |     3 | 0.0782419 |

In other words, the scores of 14 and 54 are revised upwards and some new entries
(27, 71, 78, upvoted by user 1) are brought into consideration.

**Note:** The `binomial_ci()` function is not used to calculate the score in PHP.
Instead, a different formula is used. This discrepancy exists in the codebase.

The vote_pair data structures are generated from a query and cached. The code is
greatly simplified as a result. If this ends up being too slow then that bridge
will be crossed later on.
