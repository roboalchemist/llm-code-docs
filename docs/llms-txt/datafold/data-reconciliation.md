# Source: https://docs.datafold.com/faq/data-reconciliation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Reconciliation

<AccordionGroup>
  <Accordion title="How does cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="What kind of information does Datafold output?">
    Datafold’s cross-database diffing will produce the following results:

    1. High-Level Summary:
       * Total number of different rows
       * Total number of rows (primary keys) that are present in one database, but not the other
       * Aggregate schema differences
    2. Schema Differences: Per-column mapping of data types, column order, etc.
    3. Primary Key Differences: Sample of specific rows that are present in one database, but not the other
    4. Value-Level Differences: Sample of differing values for each column with identified discrepancies; full dataset of differences can be downloaded or materialized to the warehouse

    You can check out [what the results look like in the App](/data-diff/cross-database-diffing/results).
  </Accordion>

  <Accordion title="How does a user run a data diff?">
    1. Via Datafold’s interactive UI
    2. Via the Datafold API
    3. On a schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.
  </Accordion>

  <Accordion title="Can I run multiple data diffs at the same time?">
    Yes, users can run as many diffs as they would like with concurrency limited by the underlying database.
  </Accordion>

  <Accordion title="How can I ensure accurate data comparison if my data is changing and being replicated in real-time?">
    In such cases, we recommend using watermarking – diffing data within a specified time window of row creation / update (e.g. `updated_at timestamp`).
  </Accordion>

  <Accordion title="What if the data types do not match between source and target?">
    Datafold performs best-effort type matching for cases when deterministic type casting is possible, e.g. comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.
  </Accordion>

  <Accordion title="Can data diff help if the source and target datasets have a different shape/schema/column naming?">
    Yes, users can reshape the input dataset by writing a SQL query and diffing in Query mode to bring the dataset to a shape that can be compared with another. Datafold also supports column remapping for datasets with different column names between tables.
  </Accordion>

  <Accordion title="How can data diffs be provisioned at scale, e.g. we need to create hundreds / thousands of data diffs?">
    To make the provisioning at scale easier, you can create data diffs via the [Datafold API](https://docs.datafold.com/reference/cloud/rest-api).
  </Accordion>
</AccordionGroup>
