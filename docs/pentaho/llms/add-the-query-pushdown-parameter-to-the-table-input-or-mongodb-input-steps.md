# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/add-the-query-pushdown-parameter-to-the-table-input-or-mongodb-input-steps.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/add-the-query-pushdown-parameter-to-the-table-input-or-mongodb-input-steps.md

# Add the query pushdown parameter to the Table Input or MongoDB Input steps

The input step allows you to query the data source. These instructions explain how to add a parameter that will act as a `WHERE` clause in the SQL query or the equivalent type of clause in the MongoDB query.

1. [Create a transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/create-a-transformation) that has a Table Input or MongoDB Input step.
2. [Run your transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation) to ensure it executes properly.
3. Double-click the input step (Table Input or MongoDB Input) that contains the query you want to optimize.
4. Add a parameter to the location of the `WHERE` clause value, like this:
   * SQL Query Example: `SELECT * FROM media WHERE ${countryParam}`
   * MongoDB Query Example: `{$match : ${mongoDbParam}}`
5. Press CTRL SPACE to view the list of parameters. Click on a parameter from the list to add it to the query.
6. Select the **Replace Variables in Script?** checkbox.
7. Click the **OK** button.
8. [Set up the Query Pushdown Parameter Optimization](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/set-up-query-pushdown-parameter-optimization).
