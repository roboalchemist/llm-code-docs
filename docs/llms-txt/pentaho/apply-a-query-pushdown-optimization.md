# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization.md

# Apply a query pushdown optimization

Use the Query Pushdown optimization technique to translate the `WHERE` clause in a SQL query run against a data service to a corresponding `WHERE` clause in the Table Input or MongoDB Input steps. Queries in these input steps are then filtered down and more efficiently handled at the data source.
