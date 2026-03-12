# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/transactional-databases-and-job-rollback.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/transactional-databases-and-job-rollback.md

# Transactional databases and job rollback

This section describes ways to make databases transactional and implement job rollback.

By default, when you run a [PDI job or transformation](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi) that makes changes to a database table, those changes are committed as the transformation or job executes. Sometimes, this can cause an issue if a job or transformation fails. For example, if you run a job that updates then syncs two tables, but the job fails before you can write to the second table, the first table might be updated and the other might not, rendering them both out of sync. If this is a concern, consider implementing job rollback by making the transformation or job databases (or both) transactional. When you do this, changes to a data source occur only if a transformation or job completes successfully. Otherwise, the information in both data sources remain unchanged.

The following sections provide procedural information on how to make databases transactional.

* [Make a transformation database transactional](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/transactional-databases-and-job-rollback/make-a-transformation-database-transactional)
* [Make a job database transactional](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/transactional-databases-and-job-rollback/make-a-job-database-transactional)
