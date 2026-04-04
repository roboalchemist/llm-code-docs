# Source: https://docs.pentaho.com/pdc-use/ldc-explore-your-data-cp/data-sampling.md

# Data sampling

In Data Catalog, the data sampling process is initiated without the need for a preliminary pre-analysis step. Samples are selected in a semi-random manner, with a focus on including the most recent entry in the respective table whenever possible.

The overall process involves worker implementations tailored to the specific database type. Inputs for this process include essential information like REST polling endpoints, challenge tokens for authentication, database connection details for both the source and Data Catalog, and the scope of data to be ingested. The process allows for the selection of a defined number of samples, typically ranging from 20 to 50, and can optionally purge existing schema and relationships for testing purposes.

The process outputs include progress updates during processing, such as estimated completion percentage and error counts, along with the final sample set sent to the database, replacing any existing samples. It's important to note that detailed status information about active workers may be viewable on a Worker page due to the potential presence of multiple concurrent workers.
