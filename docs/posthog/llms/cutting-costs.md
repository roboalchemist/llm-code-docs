# Source: https://posthog.com/docs/product-analytics/cutting-costs.md

# Source: https://posthog.com/docs/feature-flags/cutting-costs.md

# Source: https://posthog.com/docs/data-warehouse/cutting-costs.md

# Cutting data warehouse costs - Docs

## Use incremental or append only sync

Full table syncs are the most expensive way to sync data into the data warehouse, but aren't always necessary.

Both [incremental](/docs/cdp/sources.md#incremental) and [append only syncs](/docs/cdp/sources.md#append-only) reduce the number of rows synced as both account for existing data.

When using these sync modes, make sure the replication key field isn't nullable. Rows where the replication key is null are skipped during sync, which can lead to incomplete data.

## Sync less frequently

Not all synced data needs to be up to date to be useful. Think about what sort of data freshness you need and change the sync frequency to match.

PostHog offers sync options from every 5 minutes to every 12 hours to monthly. For incremental and full table syncs, decreasing the sync frequency can reduce the number of rows synced.

## Audit and disable unused tables

Sources and tables continue to sync even if you aren't actively using them. This can cause unnecessary costs. You should regularly audit your sources and tables to see if you can disable ones you aren't using.

Beyond just looking at [the source synced](https://app.posthog.com/data-management/sources), you can use PostHog's [`query_log` table](/docs/data/query-log.md). This contains details on all queries run in your project. You can use this to see what tables are (or are not) being queried and how often.

For example, you can use the following query to identify potential unused or underused tables:

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=WITH+cleaned+AS+%28%0A++++SELECT+%0A++++++query%2C%0A++++++--+Normalize+SQL+for+easier+parsing%0A++++++replaceRegexpAll%28replaceRegexpAll%28replaceRegexpAll%28lowerUTF8%28query%29%2C+'--%5B%5E%5C%5Cn%5D*'%2C+'+'%29%2C+'%2F%5C%5C*%5B%5E*%5D*%5C%5C*%2B%28%3F%3A%5B%5E%2F*%5D%5B%5E*%5D*%5C%5C*%2B%29*%2F'%2C+'+'%29%2C+'%5C%5Cs%2B'%2C+'+'%29+AS+q%0A++++FROM+query_log%0A%29%2C%0Atail+AS+%28%0A++SELECT+%0A++++query%2C%0A++++--+Take+everything+after+the+*last*+%22+from+%22%0A++++arrayElement%28splitByString%28'+from+'%2C+q%29%2C%0A++++length%28splitByString%28'+from+'%2C+q%29%29%29+AS+after_from%0A++FROM+cleaned%0A%29%2C%0Atokens+AS+%28%0A++SELECT+%0A++++query%2C%0A++++--+Extract+the+first+token+after+FROM%0A++++trim%28BOTH+'+'+FROM+replaceAll%28replaceAll%28arrayElement%28splitByChar%28'%2C'%2C+arrayElement%28splitByChar%28'%28'%2C+arrayElement%28splitByChar%28'+'%2C+after_from%29%2C+1%29%29%2C+1%29%29%2C+1%29%2C+'%60'%2C''%29%2C+'%22'%2C''%29%29+AS+tok%0A++FROM+tail%0A%29%0ASELECT+%0A++tok+AS+table_after_from%2C%0A++count%28%29+AS+hits%0AFROM+tokens%0AWHERE+tok+!%3D+''%0AGROUP+BY+table_after_from%0AORDER+BY+hits+ASC)

PostHog AI

```sql
WITH cleaned AS (
    SELECT
      query,
      -- Normalize SQL for easier parsing
      replaceRegexpAll(replaceRegexpAll(replaceRegexpAll(lowerUTF8(query), '--[^\\n]*', ' '), '/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/', ' '), '\\s+', ' ') AS q
    FROM query_log
),
tail AS (
  SELECT
    query,
    -- Take everything after the *last* " from "
    arrayElement(splitByString(' from ', q),
    length(splitByString(' from ', q))) AS after_from
  FROM cleaned
),
tokens AS (
  SELECT
    query,
    -- Extract the first token after FROM
    trim(BOTH ' ' FROM replaceAll(replaceAll(arrayElement(splitByChar(',', arrayElement(splitByChar('(', arrayElement(splitByChar(' ', after_from), 1)), 1)), 1), '`',''), '"','')) AS tok
  FROM tail
)
SELECT
  tok AS table_after_from,
  count() AS hits
FROM tokens
WHERE tok != ''
GROUP BY table_after_from
ORDER BY hits ASC
```

This query fetches your most queried tables by parsing the `FROM` clause from every query. It's a bit complex, we know.

![Query to identify most queried tables](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/Clean_Shot_2025_08_28_at_08_27_54_2x_be171663f4.png)![Query to identify most queried tables](https://res.cloudinary.com/dmukukwp6/image/upload/w_1000,c_limit,q_auto,f_auto/Clean_Shot_2025_08_28_at_08_28_10_2x_883b4e4f4e.png)

It effectively lists how often each table is referenced. This means it also includes views, subqueries, and other queries that reference tables, so it's not a perfect one-to-one-map, but it might be able to help you identify unused or underused tables and disable syncs for them.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better