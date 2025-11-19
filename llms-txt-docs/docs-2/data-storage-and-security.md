# Source: https://docs.datafold.com/faq/data-storage-and-security.md

# Data Storage and Security

<Accordion title="What data does Datafold ingest and store?">
  Datafold ingests and stores various types of data to ensure accurate data quality checks and insights:

  * **Metadata**: This includes table names, column names, and queries executed in the data warehouse.
  * **Data for Data Diffs**:
    * For **in-database diffs**, all data visible in the app, including data samples, is fetched and stored.
    * For **cross-database diffs**, all data visible in the app, including data samples, is fetched and stored. Larger amounts of data are fetched for comparison purposes, but only data samples are stored.
  * **Table Profiling in Data Explorer**: Datafold stores samples and distributions of data to provide detailed profiling.
</Accordion>
