# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/clear-cached-database-metadata.md

# Clear cached database metadata

When working with complex transformations or jobs, Pipeline Designer might accumulate outdated or incorrect metadata due to changes in the underlying database. You can use the Clear Complete DB Cache option to clear out the outdated or incorrect metadata the next time you access the transformation or job.&#x20;

Cached metadata might include information about:

* Table structures
* Column types
* Indexes
* Primary and foreign keys
* Other schema-related metadata

**Note**: Clearing cached database metadata does not delete any data from your database, affect transformation or job files, or clear runtime data caches that are used during execution.

To clear cached database metadata, complete the following steps:

1. With a transformation or job open, on the left side of the Pipeline Designer interface, click the **View** icon. The **View** pane opens with the Transformations folder expanded, containing the **Database Connections** list.
2. Find **Database Connections**, click the **More Actions** icon, and then select **Clear Complete DB Cache**. The cache is cleared, and a Success message is displayed. Fresh metadata is retrieved from the database the next time you access it.
