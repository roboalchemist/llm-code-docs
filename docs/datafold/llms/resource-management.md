# Source: https://docs.datafold.com/faq/resource-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resource Management

<Accordion title="What is Datafold’s resource consumption footprint? How will Datafold affect my data warehouse costs?">
  Recognizing the importance of efficient data reconciliation, we provide a number of strategies to make the diffing process as efficient as possible:

  **Efficient Algorithm**

  Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.

  **Flexible Controls**

  Users can easily control the volume of data used in diffing by using:

  * [Filters](/deployment-testing/configuration/model-specific-ci/sql-filters): Focus on the most relevant part of the dataset
  * [Sampling](/data-diff/cross-database-diffing/best-practices): Set sampling as a percentage of rows or desired confidence level
  * [Slim Diff](/deployment-testing/best-practices/slim-diff): Selectively diff only the models that have dbt code changes in your pull request.

  **Workload Management**

  Users can apply controls to enforce low diffing footprint:

  * On the Datafold side: Set desired concurrency
  * On the database side: Most databases support workload management settings to ensure that Datafold does not consume more than X% CPU or Y% RAM

  Also, consider that using a data quality tool like Datafold to catch issues before production will reduce cost over time as it lowers the need for expensive reprocessing and troubleshooting. Datafold's features like filtering, sampling, and Slim Diff ensure that only relevant datasets are tested, minimizing the computational load on your data warehouse. This targeted approach can lead to more efficient resource usage and potentially lower data warehouse operation costs.
</Accordion>
