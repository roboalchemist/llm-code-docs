# Source: https://docs.datafold.com/welcome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Welcome

> Datafold is the unified platform proactive data quality that combines automated data testing, data reconciliation, and observability to help data teams prevent data quality issues and accelerate their development velocity.

## Why Datafold?

Datafold automates the most error-prone and time-consuming aspects of the data engineering workflow by **preventing and detecting data quality issues**. In addition to standard observability features like monitoring, profiling, and lineage, we integrate deeply into the development cycle with automated CI/CD testing. This enables data teams to prevent bad code deployments and detect issues upstream of the data warehouse.

Whether it's for [CI/CD testing](deployment-testing/how-it-works) or [data migration automation](data-migration-automation), Datafold ensures data quality at every stage of the data pipeline.

## Key features

Data quality is a complex and multifaceted problem. Datafold’s unified platform helps embed proactive data quality testing in your workflows:

<CardGroup cols={2}>
  <Card title="Data Diffs" href="/data-diff/what-is-data-diff" horizontal>
    Use value-level data diffs to isolate and identify changes in your data. Catch unintended modifications before they disrupt production or downstream data usage.
  </Card>

  <Card title="Data Monitors" href="/data-monitoring/monitor-types" horizontal>
    Create monitors for data diffs, data quality metrics, SQL metrics, SQL rules, and schema changes to send alerts when inconsistencies are detected.
  </Card>

  <Card title="Datafold Migration Agent" href="/data-migration-automation" horizontal>
    Discover how DMA provides full-cycle migration automation with SQL code translation and cross-database validation.
  </Card>

  <Card title="Data Explorer & Column-Level Lineage" href="/data-explorer/how-it-works" horizontal>
    Learn how your data assets move and change across systems with column-level lineage, metadata, and profiles, to track the impacts of changes made upstream.
  </Card>
</CardGroup>

## Use cases

<CardGroup cols={3}>
  <Card title="CI/CD Data Testing" href="" horizontal>
    Catch data quality issues early with automated testing during development and deployment.
  </Card>

  <Card title="Accelerated Data Migrations" href="" horizontal>
    Speed up migrations with our full-cycle migration automation solution for data teams.
  </Card>

  <Card title="Data Monitoring & Observability" href="" horizontal>
    Shift monitoring upstream to proactively prevent disruptions and ensure data quality.
  </Card>
</CardGroup>

## Getting started

There are a few ways to get started with your first data diff:

<Steps>
  <Step title="Create a data diff" stepNumber="1">
    Once you’ve integrated a [data connection](/integrations) and [code repository](/integrations/code-repositories), you can run a new [in-database](/data-diff/in-database-diffing/creating-a-new-data-diff) or [cross-database](/data-diff/cross-database-diffing/creating-a-new-data-diff) data diff or explore your [data lineage](data-explorer/lineage).
  </Step>
</Steps>

<Steps>
  <Step title="Create automated monitors" stepNumber="2">
    Create [monitors](data-monitoring/monitor-types) to send alerts when data diffs fall outside predefined ranges.
  </Step>
</Steps>

<Steps>
  <Step title="Set up CI/CD testing" stepNumber="3">
    Get started with deployment testing through our universal ([No-Code](deployment-testing/getting-started/universal/no-code), [API](deployment-testing/getting-started/universal/api)) or [dbt](integrations/orchestrators/dbt-core) integrations.
  </Step>
</Steps>

## Learn more

Curious to learn more about why and how data quality matters? We wrote a whole guide (with illustrations of medieval castles, moats, and knights) called the [Data Quality Guide](https://www.datafold.com/data-quality-guide) which covers:

* A practical roadmap towards creating a robust data quality system
* Data quality metrics to keep, and metrics to ignore
* Nurturing a strong data quality culture within and beyond data teams
