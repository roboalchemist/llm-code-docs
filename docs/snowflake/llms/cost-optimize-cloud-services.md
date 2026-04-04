# Source: https://docs.snowflake.com/en/user-guide/cost-optimize-cloud-services.md

# Optimizing cloud services for cost

If you find that your [cloud services usage](cost-understanding-compute.md) is higher than expected, check if your use of
Snowflake follows any of the following patterns. Each pattern includes a recommendation that might help you reduce costs associated with
cloud services.

* Pattern: Copy commands with poor selectivity
* Pattern: High-frequency DDL operations and cloning
* Pattern: High-frequency, simple queries
* Pattern: High-frequency INFORMATION_SCHEMA queries
* Pattern: High-frequency SHOW commands (by data applications and third-party tools)
* Pattern: Single-row inserts and fragmented schemas (by data applications)
* Pattern: Complex SQL queries

Pattern: Copy commands with poor selectivity
:   Executing copy commands involves listing files from Amazon Simple Storage Service (S3). Because listing files uses only cloud services
    compute, executing copy commands with poor selectivity can result in high cloud services usage.

    **Recommendation:** Consider changing the structure of your S3 bucket to include some kind of date prefix, so you list only the targeted
    files you need.

Pattern: High-frequency DDL operations and cloning
:   Data Definition Language (DDL) operations, particularly cloning, are entirely metadata operations, meaning they use only cloud services
    compute. Frequently creating or dropping large schemas or tables, or cloning databases for backup, can result in significant cloud
    services usage.

    **Recommendation:** Cloning uses only a fraction of the resources needed to do deep copies, so you should continue to clone. Review your
    cloning patterns to ensure they are as granular as possible, and aren’t being executed too frequently. For example, you might want to
    clone only individual tables rather than an entire schema.

Pattern: High-frequency, simple queries
:   The consumption of cloud services by a single simple query is negligible, but running queries such as `SELECT 1`,
    `SELECT sequence1.NEXTVAL`, or `SELECT CURRENT_SESSION()` at an extremely high frequency (tens of thousands per day) can result in
    significant cloud services usage.

    **Recommendation:** Review your query frequency and determine whether the frequency is appropriately set for your use case. If you
    observe a high frequency of `SELECT CURRENT_SESSION()` queries originating from partner tools using the JDBC driver, confirm that
    the partner has updated their code to use the `getSessionId()` method in the
    [SnowflakeConnection interface](../developer-guide/jdbc/jdbc-api.md). This takes advantage of caching and reduces cloud services usage.

Pattern: High-frequency INFORMATION_SCHEMA queries
:   Queries against the [Snowflake Information Schema](../sql-reference/info-schema.md) consume only cloud services resources. The consumption of cloud services by a single
    query against INFORMATION_SCHEMA views might be negligible, but running these queries at extremely high frequency (tens of thousands per
    day) can result in significant cloud services usage.

    **Recommendation:** Review your query frequency and determine whether the frequency is appropriately set for your use case.
    Alternatively, you can query a view in the [ACCOUNT_USAGE schema](../sql-reference/account-usage.md) instead of an INFORMATION_SCHEMA
    view. Querying the ACCOUNT_USAGE schema uses a virtual warehouse rather than cloud services.

Pattern: High-frequency SHOW commands (by data applications and third-party tools)
:   SHOW commands are entirely metadata operations, meaning they consume only cloud services resources. This pattern typically occurs when
    you have created an application built on top of Snowflake that executes SHOW commands at a high frequency. These commands might also be
    initiated by third-party tools.

    **Recommendation:**
    Review your query frequency and determine whether the frequency is appropriately set for your use case. In the case of partner tools,
    reach out to your partner to see if they have any plans to adjust their usage.

Pattern: Single-row inserts and fragmented schemas (by data applications)
:   Snowflake is not an OLTP system, so single-row inserts are suboptimal, and can consume significant cloud services resources.

    Building a data application that defines one schema per customer might result in several data loads in a given time period, which can
    result in high cloud services consumption.

    This pattern also results in a lot more metadata that Snowflake needs to maintain, and metadata operations consume cloud services
    resources. Each metadata operation individually consumes minimal resources, but consumption might be significant in aggregate.

    **Recommendation:** In general, do batch or bulk loads rather than single-row inserts.

    Using a shared schema is significantly more efficient, which saves costs. You’ll likely want to cluster all tables on `customer_ID` and
    use [secure views](views-secure.md).

Pattern: Complex SQL queries
:   Queries can consume significant cloud services compute if they include a lot of joins/Cartesian products, use the IN operator with large
    lists, or are very large queries. These types of queries all have high compilation times.

    **Recommendation:** Review your queries to confirm they are doing what you intend them to do. Snowflake supports these queries and will
    charge you only for the resources consumed.
