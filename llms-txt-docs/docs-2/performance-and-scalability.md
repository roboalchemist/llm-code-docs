# Source: https://docs.datafold.com/faq/performance-and-scalability.md

# Performance and Scalability

<AccordionGroup>
  <Accordion title="How scalable is Datafold?">
    Datafold is highly scalable, supporting data teams working with billion-row datasets and thousands of data transformation/dbt models. It offers powerful performance optimization features such as [SQL filtering](/deployment-testing/configuration/model-specific-ci/sql-filters), [sampling](/data-diff/cross-database-diffing/best-practices), and [Slim Diff](/deployment-testing/best-practices/slim-diff), which allow you to focus on testing the datasets that are most critical to your business, ensuring efficient and targeted data quality validation.
  </Accordion>

  <Accordion title="How can I optimize diff performance at scale?">
    Datafold pushes down compute to your database, and the performance of data diffs largely depends on the underlying SQL engine. Here are some in-app strategies to optimize performance:

    1. [Enable sampling](/data-diff/cross-database-diffing/best-practices): Sampling reduces the amount of data processed by comparing a randomly chosen subset. This approach balances diff detail with processing time and cost, suitable for most use cases.

    2. [Use SQL Filters](/deployment-testing/configuration/model-specific-ci/sql-filters): If you only need to compare a specific subset of data (e.g., for a particular city or a recent time period), adding a SQL filter can streamline the diff process.

    3. **Exclude columns/tables**: When certain columns or tables are unnecessary for critical comparisons—such as temporary tables with dynamic values, metadata fields, or timestamp columns that always differ—you can exclude these to increase diff efficiency and speed.

    You can exclude columns when you create a new Data Diff or when you clone an existing one:

    <Frame>
            <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=115abf94cf44b4455815c3ba6590fffe" alt="" data-og-width="1384" width="1384" data-og-height="884" height="884" data-path="images/faq/new_diff_exclude_columns.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=60532a82cd20ef169777bed2b18daa2f 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=7b9258cb4d2db96623ed5759de7381d4 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=958c95dc67f34afc38445e991a4cfe76 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=1675889d188645eee642fee41a3179d4 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=64fa8499cce7deddfd8f5730d04c910a 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/faq/new_diff_exclude_columns.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=394aff3dbd3bef65acc013a6baa2e521 2500w" />
    </Frame>

    To exclude them in your CI/CD pipeline, [follow this guide](/integrations/orchestrators/dbt-core#advanced-settings-configuration) to specify them in the Advanced settings of your CI/CD configuration in Datafold.

    4. **Optimize SQL queries**: Refactor your SQL queries to improve the efficiency of database operations, reducing execution time and resource usage.
    5. **Leverage database performance features**: Ensure your database is configured to match typical diff workload patterns. Utilize features like query optimization, caching, and parallel processing to boost performance.
    6. **Increase data warehouse resources**: If using a platform like Snowflake, consider increasing the size of your warehouse to allocate more resources to Datafold operations.
  </Accordion>
</AccordionGroup>
