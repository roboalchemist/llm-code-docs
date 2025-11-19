# Source: https://docs.datafold.com/faq/data-migration-automation.md

# Data Migration Automation

<AccordionGroup>
  <Accordion title="How does DMA work?">
    Datafold performs complete SQL codebase translation and validation. It uses an AI agent architecture that performs the translation leveraging an LLM model with a feedback loop optimized for achieving full parity between migration source and target. DMA takes into account metadata, including schema, data types, and relationships in the source system.
  </Accordion>

  <Accordion title="How is this approach different from other tools on the market?">
    DMA offers several key advantages over deterministic transpilers that rely on static code parsing with predefined grammars:

    * **Full parity between source and target:** DMA not only returns code that compiles, but code that produces the same result in your new database with explicit validation.
    * **Flexible dialect handling:** Ability to adapt to any arbitrary dialect for input/output without the need to provide full grammar, which is especially valuable for numerous legacy systems and their versions.
    * **Self-correction capabilities:** DMA can self-correct mistakes, taking into account compilation errors and data discrepancies.
    * **Modernizing code structure:** DMA can convert convoluted stored procedures into dbt projects following best practices.
  </Accordion>

  <Accordion title="How do I know if the output is correct?">
    Upon delivery, customers get a comprehensive report with links to data diffs validating parity and discrepancies (if any) on dataset-, column-, and row-level between source and target.
  </Accordion>

  <Accordion title="How does my team use DMA?">
    Once source and target systems are connected and Datafold ingests the code base, translations with DMA are automatically supervised by the Datafold team. In most cases, no input is required from the customer.
  </Accordion>

  <Accordion title="What do I need to start working with DMA?">
    Connect source and target data sources to Datafold. Provide Datafold access to the codebase (usually by installing the Datafold GitHub/GitLab/ADO app or via system catalog for stored procedures).
  </Accordion>

  <Accordion title="What are the security implications of using DMA?">
    Datafold is SOC 2 Type II, GDPR, and HIPAA-compliant and provides flexible deployment options, including in-VPC deployment in AWS, GCP, or Azure. The LLM infrastructure relies on local models and does not expose data to any sub-processor besides the cloud provider. In case of a VPC deployment, none of the data leaves the customer’s private network.
  </Accordion>

  <Accordion title="How long will it take to translate?">
    After the initial setup, the migration process can take several days to several weeks, depending on the source and target technologies, scale, and complexity.
  </Accordion>

  <Accordion title="What if I want to change data model/definitions?">
    DMA is an ideal fit for lift-and-shift migrations with parity between source and target as the goal. Some customization is possible and needs to be scoped on a case-by-case basis.
  </Accordion>

  <Accordion title="How does cross-database diffing work?">
    Datafold connects to any SQL source and target databases, similar to how BI tools do. Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
  </Accordion>

  <Accordion title="What kind of information does Datafold output?">
    Datafold’s cross-database diffing will produce the following results:

    * **High-Level Summary:**
      * Total number of different rows
      * Total number of rows (primary keys) that are present in one database but not the other
      * Aggregate schema differences
    * **Schema Differences:** Per-column mapping of data types, column order, etc.
    * **Primary Key Differences:** Sample of specific rows that are present in one database but not the other
    * **Value-Level Differences:** Sample of differing column values for each column with identified discrepancies; full dataset of differences can be downloaded or materialized to the warehouse
  </Accordion>

  <Accordion title="How does a user run a data diff?">
    * Via Datafold’s interactive UI
    * Via the Datafold API
    * On schedule (as a monitor) with optional alerting via Slack, email, PagerDuty, etc.
  </Accordion>

  <Accordion title="Can I run multiple data diffs at the same time?">
    Yes, users can run as many diffs as they would like with concurrency limited by the underlying database.
  </Accordion>

  <Accordion title="What if my data is changing and replicated live, how can I ensure proper comparison?">
    In such cases, we recommend using watermarking—diffing data within a specified time window of row creation/update (e.g., `updated_at timestamp`).
  </Accordion>

  <Accordion title="What if the data types do not match between source and target?">
    Datafold performs best-effort type matching for cases where deterministic type casting is possible, e.g., comparing `VARCHAR` type with `STRING` type. When automatic type casting without information loss is not possible, the user can define type casting manually using diffing in Query mode.
  </Accordion>

  <Accordion title="Can data diff help if the dataset in the source and target databases has a different shape/schema/column naming?">
    Users can reshape input datasets by writing a SQL query and diffing in Query mode to bring the dataset to a comparable shape. Datafold also supports column remapping for datasets with different column names between tables.
  </Accordion>
</AccordionGroup>
