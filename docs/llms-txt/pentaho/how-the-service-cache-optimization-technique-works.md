# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-the-service-cache-optimization/how-the-service-cache-optimization-technique-works.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/optimize-a-pentaho-data-service/apply-the-service-cache-optimization/how-the-service-cache-optimization-technique-works.md

# How the service cache optimization technique works

If you run the data service during the time that the data service results are cached, PDI will run your query against the cached data set instead of running the entire transformation again only if certain conditions are met. These conditions are determined by the other optimization techniques you choose to apply as well as whether the query results are a subset of the cached data set.

Enabling the cache tells PDI to store the results of the data service transformation for the length of time you specify.

![PDI Data Service Cache Optimization Workflow](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-167306f1bf086040aad8143933af5b1997702215%2FPDITransStep_DataService_CacheOptimization.png?alt=media)

If you do not combine the Service Cache optimization with other optimization techniques and if you query the data service more than once before the cache expires, the query will run against the cached data set if the cached data set contains all of the matching records in the original data set. For example, if the initial run of the data service populates the cache with the results of `SELECT * FROM 'employee'`, a subsequent data service call that retrieves a subset of the data (e.g. `SELECT * FROM 'employee' WHERE region = "South"`) will be run against the cached data set. For this to happen, the original query must have been run against the full data set.

When you run a test in the Test Data Service window, then adjust the query and run the test again, the query is not run against the cache. This is because when you run a test, the results only return a certain number of records (100, 500, or 1000, depending on what you selected for **Max Rows**). For example, you could run a test that uses the `SELECT * FROM 'employee'` query to return the first 100 records from a 5000 record table. The initial test query would return the first 100 records from the employee table.

Assume that the cached result set consists of records for 50 males and 50 females. If you run a second test, but adjust the query so that you only show records for females (`SELECT * FROM 'employee' WHERE gender="F"`) running the query against the cached results would result in only 50 records being returned instead of 100. To avoid this and to provide more accurate results, PDI runs the transformation again so that the second test query is run against the table and returns the first 100 matching results.
