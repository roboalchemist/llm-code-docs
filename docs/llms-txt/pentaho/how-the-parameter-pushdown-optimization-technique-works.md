# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/how-the-parameter-pushdown-optimization-technique-works.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-a-parameter-pushdown-optimization/how-the-parameter-pushdown-optimization-technique-works.md

# How the parameter pushdown optimization technique works

To set up the parameter pushdown optimization, first set up the optimization, then add the parameter to the transformation step.

![PDI Parameter Pushdown Optimization Workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-fee15d9d09577c968f5b27c90b7f4d39a995ec7c%2FPDITransStep_DataService_ParameterPushdownOptimizationWorkflow.png?alt=media)

If you combine this optimization technique with Service Cache optimization and if you query the data service more than once before the cache expires, the query will run against the cached data set if the cached data set contains all of the matching records in the original data set. Also, when you run a test in in the Test Data Service window, then adjust the query and run the test again, the query is not run against the cache. When you run the test, the results only return a certain number of records (100, 500, or 1000, depending on what you selected for **Max Rows**). For more information on the optimization technique, see the **Apply a Service Cache Optimization** section.
