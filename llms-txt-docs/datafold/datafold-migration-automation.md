# Source: https://docs.datafold.com/data-migration-automation/datafold-migration-automation.md

# Datafold for Migration Automation

> Datafold provides full-cycle migration automation with SQL code translation and cross-database validation for data warehouse, transformation framework, and hybrid migrations.

Datafold offers flexible migration validation options to fit your data migration workflow. Data teams can choose to leverage the full power of the [Datafold Migration Agent (DMA)](../data-migration-automation/datafold-migration-agent) alongside [cross-database diffing](../data-diff/how-datafold-diffs-data#how-cross-database-diffing-works), or use ad-hoc diffing exclusively for validation.

## Supported migrations

Datafold supports a wide range of migrations to meet the needs of modern data teams. The platform enables smooth transitions between different databases and transformation frameworks, ensuring both code translation and data validation throughout the migration process. Datafold can handle:

* **Data Warehouse Migrations:** Seamlessly migrate between data warehouses, for example, from PostgreSQL to Databricks.

* **Data Transformation Framework Migrations:** Transition your transformation framework from legacy stored procedures to modern tools like dbt.

* **Hybrid Migrations:** Migrate across a combination of data platforms and transformation frameworks. For example, moving from MySQL + stored procedures to Databricks + dbt.

## Migration options

<AccordionGroup>
  <Accordion title="Option 1: DMA + Ad-Hoc Diffing">
    The AI-powered Datafold Migration Agent (DMA) provides automated SQL code translation and validation to simplify and automate data migrations. Teams can pair DMA with ad-hoc cross-database diffing to enhance the validation process with additional manual checks when necessary.

    **How it works:**

    * **Step 1:** Connect your legacy and new databases to Datafold, along with your codebase.
    * **Step 2:** DMA translates and validates SQL code automatically.
    * **Step 3:** Pair the DMA output with ad-hoc cross-database diffing to reconcile data between legacy and new databases.

    This combination streamlines the migration process, offering automatic validation with the flexibility of manual diffing for fine-tuned control.
  </Accordion>

  <Accordion title="Option 2: Ad-Hoc Diffing Only">
    For teams that prefer to handle code translation manually or are working with third-party migrations, Datafold's ad-hoc cross-database diffing is available as a stand-alone validation tool.

    **How it works:**

    * Validate data across databases manually without using DMA for code translation.
    * Run ad-hoc diffing as needed, via the [Datafold REST API](../api-reference/introduction), or schedule it with [Monitors](../data-monitoring) for continuous validation.

    This option gives you full control over the migration validation process, making it suitable for in-house or outsourced migrations.
  </Accordion>
</AccordionGroup>
