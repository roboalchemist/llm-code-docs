# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/how-the-query-pushdown-optimization-technique-works.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-query-pushdown-optimization/how-the-query-pushdown-optimization-technique-works.md

# How the query pushdown optimization technique works

To apply Query Pushdown optimization, first set the input step optimization values, then add the optimization parameter to the input step query.

The optimization requires the creation of a parameter that takes the place of the `WHERE` clause, like the following example: `SELECT * FROM 'employee' WHERE ${countryParam}`.

![PDI Data Service Query Pushdown Optimization Workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-f6236200cc28552baffe4c396e92b42e726c20d1%2FPDITransStep_DataService_QueryPushdownOptimizationWorkflow.png?alt=media)

If you combine this optimization technique with Service Cache optimization and if you query the data service more than once before the cache expires, the query will run against the cached data set if the cached data set contains all of the matching records in the original data set. Also, when you run a test in the Test Data Service window, then adjust the query and run the test again, the query is not run against the cache. When you run the test, the results only return a certain number of records (100, 500, or 1000, depending on what you selected for **Max Rows**). For more information on the optimization technique, see the **Apply a Service Cache Optimization** section.
