# Source: https://docs.datafold.com/data-diff/in-database-diffing/best-practices.md

# Source: https://docs.datafold.com/data-diff/cross-database-diffing/best-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Best Practices

> When dealing with large datasets, it's crucial to approach diffing with specific optimization strategies in mind. We share best practices that will help you get the most accurate and efficient results from your data diffs.

## Enable sampling

[Sampling](/data-diff/cross-database-diffing/creating-a-new-data-diff#row-sampling) can be helpful when diffing between extremely large datasets as it can result in a speedup of 2x to 20x or more. The extent of the speedup depends on various factors, including the scale of the data, instance sizes, and the number of data columns.

The following table illustrates the speedup achieved with sampling in different databases, varying instance sizes, and different numbers of data columns:

|      Databases      | vCPU | RAM, GB |    Rows   | Columns | Time full | Time sampled | Speedup |    RDS type   | Diff full | Diff sampled | Per-col noise |
| :-----------------: | :--: | :-----: | :-------: | :-----: | :-------: | :----------: | :-----: | :-----------: | :-------: | :----------: | :-----------: |
| Oracle vs Snowflake |   2  |    2    | 1,000,000 |    1    |  0:00:33  |    0:00:27   |   1.22  |  db.t3.small  |    5399   |     5400     |       0       |
| Oracle vs Snowflake |   8  |    32   | 1,000,000 |    1    |  0:07:23  |    0:00:18   |  24.61  | db.m5.2xlarge |    5422   |     5423     |     0.005     |
|  MySQL vs Snowflake |   2  |    8    | 1,000,000 |    1    |  0:00:57  |    0:00:24   |   2.38  |  db.m5.large  |    5409   |     5413     |       0       |
|  MySQL vs Snowflake |   2  |    8    | 1,000,000 |    29   |  0:40:00  |    0:02:14   |  17.91  |  db.m5.large  |    5412   |     5411     |       0       |

When sampling is enabled, Datafold compares a randomly chosen subset of the data. Sampling is the tradeoff between the diff detail and time/cost of the diffing process. For most use cases, sampling does not reduce the informational value of data diffs as it still provides the magnitude and specific examples of differences (e.g., if 10% of sampled data show discrepancies, it suggests a similar proportion of differences across the entire dataset).

<Tip>
  Although configuring sampling can seem overwhelming at first, a good rule of thumb is to select an initial value of 95% for the sampling confidence and adjust it as needed. Tweaking the parameters can be helpful to see how they impact the sample size and the tradeoff between performance and accuracy.
</Tip>

## Handling data type differences

Datafold automatically manages data type differences during cross-database diffing. For example, when comparing decimals with different precisions (e.g., `DECIMAL(38,15)` in SQL Server and `DECIMAL(38,19)` in Snowflake), Datafold automatically casts values to a common precision before comparison, flagging any differences appropriately. Similarly, for timestamps with different precisions (e.g., milliseconds in SQL Server and nanoseconds in Snowflake), Datafold adjusts the precision as needed for accurate comparisons, simplifying the diffing process.

## Optimizing OLTP databases: indexing best practices

When working with row-oriented transactional databases like PostgreSQL, optimizing the database structure is crucial for efficient data diffing, especially for large tables. Here are some best practices to consider:

* **Create indexes on key columns**:

* It's essential to create indexes on the columns that will be compared, particularly the primary key columns defined in the data diffs.

* **Example**: If your data diff involves primary key columns `colA` and `colB`, ensure that indexes are created for these specific columns.

* **Use separate indexes for primary key columns:**

* Indexes for primary key columns should be distinct and start with these columns, not as subsets of other indexes. Having a dedicated primary key index is critical for efficient diffing.

* **Example**: Consider a primary key consisting of `colA` and `colB`. Ensure that the index is structured in the same order, like (`colA`, `colB`), to align with the primary key. An index with an order of (`colB`, `colA`) is strongly discouraged due to the impact on performance.

* **Example**: If the index is defined as (`colA`, `colB`, `colC`) and the primary key is a combination of `colA` and `colB`, then when setting up the diff operation, ensure that the primary key is specified as `colA`, `colB.` If the order is reversed as `colB`, `colA`, the diffing process won’t be able to fully utilize indexing, potentially leading to slower performance.

* **Leverage compound indexes**:

* Compound indexes, which involve multiple columns, can significantly improve query performance during data diffs as they efficiently handle complex queries and filtering.

* **Example**: An index defined as (`colA`, `colB`, `colC`) can be beneficial for diffing operations involving these columns, as it aligns with the order of columns in the primary key.

## Handling high percentage of differences

Data diff is optimized to perform best when the percent of different rows/values is relatively low, to support common data validation scenarios like data replication and migration.

While the tool strives to maximize the database's computational power and minimize data transfer, in extreme cases with very high difference percentages (up to 100%), it may result in transferring every row over the network, which is considerably slower.

In order to avoid long-running diffs, we recommend the following:

* **Start with diffing [primary keys](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key)** only to identify row-level completeness first, before diffing all or more columns.
* **Set an [egress](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key) limit** to automatically stop the diffing process after set number of rows are downloaded over the network.
* **Set a [per-column diff](/data-diff/cross-database-diffing/creating-a-new-data-diff#primary-key) limit** to stop finding differences for each column after a set number are found. This is especially useful in data reconciliation where identifying a large number of discrepancies (e.g., large percentage of missing/different rows) early on indicates that a detailed row-by-row diff may not be required, thereby saving time and computational resources.

In the screenshot below, we see that exactly 4 differences were found in `user_id`, but “at least 4,704 differences” were found in `total_runtime_seconds`. `user_id` has a number of differences below the per-column diff limit, and so we state the exact number. On the other hand, `total_runtime_seconds` has a number of differences greater than the per-column diff limit, so we state “at least.” Note that due to our algorithm’s approach, we often find significantly more differences than the limit before diffing is halted, and in that scenario, we report the value that was found, while stating that more differences may exist.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e5e4bc527ed248a8f06c1e6910dcf75e" data-og-width="1476" width="1476" data-og-height="1523" height="1523" data-path="images/screenshot.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=a5d6f86893b6306a12b78e7aa08bcf2a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8b1ec0d83758bfbbe37f93688390ce42 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cbb81cf1d896810821449a957e2a1f4e 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3d2aa8c5375d44bb76757f76691be05a 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=df4562154b3d6a8af753fa041a61117e 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/screenshot.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1ee252f9dccad4d836c2990ac8719f88 2500w" />
</Frame>

## Executing queries in parallel

Increase the number of concurrent connections to the database in Datafold. This enables queries to be executed in parallel, significantly accelerating the diff process.

Navigate to the **Settings** option in the left sidebar menu of Datafold. Adjust the **max connections** setting to increase the number of concurrent connections Datafold can establish with your data. Note that the maximum allowable value for concurrent connections is 64.

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=cd52afb88ab462f6b3f69f3ea6ead45b" data-og-width="1534" width="1534" data-og-height="836" height="836" data-path="images/connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4cb4a75c28a66a51fa69e7cec884ce7c 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=b7dde14c80d168e9c43fd2968b3abe51 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=45bb326072ea3b59e2f7cecaf834ecfd 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=4f2090603a806a9f4f360d889684a2ef 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=325f96db65116e034e81c64df6882339 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/connection.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=98926e3cb27d393a85d09803377423d7 2500w" />
</Frame>

## Optimize column selection

The number of columns included in the diff directly impacts its speed: selecting fewer columns typically results in faster execution. To optimize performance, refine your column selection based on your specific use case:

* **Comprehensive verification**: For in-depth analysis, include all columns in the diff. This method is the most thorough, suitable for exhaustive data reviews, albeit time-intensive for wide tables.
* **Minimal verification**: Consider verifying only the primary key and `updated_at` columns. This is efficient and sufficient if you need to validate rows have not been added or removed, and that updates are current between databases, but do not need to check for value-level differences between rows with common primary keys.
* **Presence verification**: If your main concern is just the presence of data (whether data exists or has been removed), such as identifying missing hard deletes, verifying only the primary key column can be sufficient.
* **Hybrid verification**: Focus on key columns that are most critical to your operations or data integrity, such as monetary values in an `amount` column, while omitting large serialized or less critical columns like `json_settings`.

## Managing primary key distribution

Significant gaps in the primary key column can decrease diff efficiency (e.g., 10s of millions of continuous rows missing). Datafold will execute queries for non-existent row ranges, which can slow down the data diff.

## Handling different primary key types

As a general rule, primary keys should be of the same (or similar) type in both datasets for diffing to work properly. Comparing primary keys of different types (e.g., `INT` vs `VARCHAR`) will result in a type mismatch error. You can still diff such datasets by casting the primary key column to the same type in both datasets explicitly.

<Note>
  Indexes on the primary key typically cannot be utilized when the primary key is cast to a different type. This may result in slower diffing performance. Consider creating a separate index, such as [expression index in PostgreSQL](https://www.postgresql.org/docs/current/indexes-expressional.html), to improve performance.
</Note>

<Frame>
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=aea91ec007c4c3b6f02a651d1f509141" data-og-width="1434" width="1434" data-og-height="1726" height="1726" data-path="images/data1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f77fe2030286efa0f69414ab836db7e0 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=72d4d2cfbb2ff26c44af7705b2d88c32 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=319b67c88bdd689f984061b21579496b 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dbdc457cf596af8e77748b0f288ea6f9 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=e340b852cbe1711e8ba79c496fef6d2e 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c1d00e992e47d24a9dbab3317028c7fe 2500w" />
</Frame>
