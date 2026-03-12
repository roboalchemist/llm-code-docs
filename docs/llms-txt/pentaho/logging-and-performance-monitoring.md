# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/logging-and-performance-monitoring.md

# Logging and performance monitoring

**Pentaho Data Integration** provides you with several methods in which to monitor the performance of jobs and transformations. Logging offers you summarized information regarding a job or transformation such as the number of records inserted and the total elapsed time spent in a transformation. In addition, logging provides detailed information about exceptions, errors, and debugging details.

You may want to enable logging and step performance monitoring to determine if a job completed with errors or to review errors that were encountered during processing. In headless environments, most ETL in production is not run from the graphical user interface and you need a place to watch initiated job results. Performance monitoring can provide you with useful information for both current performance problems and capacity planning.

To see what effect your transformation will have on the data sources it includes, go to the **Action** menu and click on **Impact**. PDI will perform an impact analysis to determine how your data sources will be affected by the transformation if it is completed successfully.

If you are an administrative user and want to monitor jobs and transformations, you must first set up logging and performance monitoring in the PDI client (Spoon). For more information about monitoring jobs and transformations, see the **Administer Pentaho Data Integration and Analytics** document.
