# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-09-30-semantic-view-derived-metrics.md

# Sep 30, 2025: Support for derived metrics in semantic views

In a [semantic view](../../../user-guide/views-semantic/overview.md), if you want to define a metric based on metrics from different
logical tables, you can define a *derived metric*. A derived metric is a metric that is scoped to the semantic view (rather than
to a specific logical table). A derived metric can combine metrics from multiple logical tables.

For more information, see [Defining derived metrics](../../../user-guide/views-semantic/sql.md).
