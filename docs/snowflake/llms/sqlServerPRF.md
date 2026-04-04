# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/technical-documentation/issues-and-troubleshooting/performance-review/sqlServerPRF.md

# SnowConvert AI - SQL Server-Azure Synapse Performance Review Messages

Applies to

* SQL Server
* Azure Synapse Analytics

## SSC-PRF-TS0001

Performance warning - recursion for CTE not checked. Might require a recursive keyword.

### Description

This warning appears when SnowConvert AI detects a Common Table Expression (CTE) but has not verified whether the CTE contains recursive operations in its query definition.

Snowflake SQL requires the RECURSIVE keyword for recursive Common Table Expressions (CTEs). Currently, SnowConvert AI does not automatically detect recursive queries to determine whether the RECURSIVE keyword should be included. This warning notifies you that you may need to manually add the RECURSIVE keyword for recursive CTEs.

Support for this validation may be added in future releases as requirements evolve.

### Code Example

#### Input Code

```sql
 WITH Sales_CTE (SalesPersonID, NumberOfOrders)
AS
(
    SELECT SalesPersonID, 2
    FROM Sales.SalesOrderHeader
    WHERE SalesPersonID IS NOT NULL
    GROUP BY SalesPersonID
)
SELECT 2 AS "Average Sales Per Person"
FROM Sales_CTE;
```

#### Generated Code

```sql
 --** SSC-PRF-TS0001 - PERFORMANCE WARNING - RECURSION FOR CTE NOT CHECKED. MIGHT REQUIRE RECURSIVE KEYWORD **
WITH Sales_CTE (
    SalesPersonID,
    NumberOfOrders
) AS
(
    SELECT
        SalesPersonID, 2
    FROM
        Sales.SalesOrderHeader
    WHERE
        SalesPersonID IS NOT NULL
    GROUP BY
        SalesPersonID
)
SELECT 2 AS "Average Sales Per Person"
FROM
    Sales_CTE;
```

### Best Practices

* The RECURSIVE keyword is optional and won’t affect your query results. However, it may influence how Snowflake allocates resources during execution. We recommend reviewing Snowflake’s CTE documentation and contacting us if you’d like automatic RECURSIVE keyword addition for compatible CTE queries.
* For additional assistance, please email us at [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
