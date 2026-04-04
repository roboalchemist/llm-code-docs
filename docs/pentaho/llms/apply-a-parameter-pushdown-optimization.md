# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization.md

# Apply a parameter pushdown optimization

The Parameter Pushdown optimization technique can be applied to any step in the transformation.

Although similar to the Query Pushdown optimization, Parameter Pushdown optimization differs because it can applied to any step and it maps a field value to a parameter in a simple `WHERE` clause in which a parameter is assigned a specific value using the equal operator like the following example: `WHERE region= "South"`.
