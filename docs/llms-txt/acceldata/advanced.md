# Source: https://docs.acceldata.io/documentation/advanced.md

# Data Reliability

Data reliability means having data that is **accurate, consistent, and trustworthy over time**. Reliable data is the foundation for confident decision-making, whether you’re optimizing costs, reporting metrics, or powering analytics.

Acceldata Data Observability Cloud helps you define what “good data” looks like for your organization. You can set up [rules](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/rules-and-rulesets) and [policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/apply-policies-and-monitor-reliability) that capture your business standards, and ADOC will continuously check your data against them. If issues arise, ADOC alerts you early so you can take action before they impact operations or decisions.

The journey to data reliability in ADOC follows a clear flow:

## 1. Connect Your Data Sources

First, connect the systems where your data lives, for example, **Snowflake, Oracle, BigQuery, or S3**. Once connected, ADOC can **crawl** the source. Crawling is the process of discovering _what datasets exist_, such as databases, schemas, tables, or files.

**Example:** If you connect Snowflake, ADOC will list your databases, schemas, and tables in the **Discover Assets** page.

## 2. Discover Assets

The [Discover Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/discover-assets) page gives you a view of the inventory of all connected datasets. Here you can:

- Browse assets by data source (e.g., Snowflake).
- Search by name or apply filters (e.g., “last updated in 30 days”).
- See early health indicators such as active alerts or policy mappings.
- Access **Lineage**: Trace how data flows between sources and downstream systems.
- Create **Virtual Assets**: Build SQL Views or Visual Views to model or combine datasets.

At this stage, you know what data exists, how it’s related, and where it flows.

## 3. Profile Assets

[Profiling](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/profile-assets) goes deeper than crawling. Where crawling tells you _what datasets exist_, profiling tells you _what’s inside those datasets_. 

Profiling captures key statistics, such as:

- Row counts and update frequency.
- Distinct values, null percentages, and anomalies.
- Basic trends in data freshness.

**Example:** After profiling a sales table, you might discover that 10% of customer emails are missing.

Profiling prepares your datasets for policy enforcement.

## 4. Apply Policies & Monitor Reliability

A [policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/apply-policies-and-monitor-reliability) is a collection of one or more [rule](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/rules-and-rulesets) that together define what “good data” means for a dataset. Think of a policy as a wrapper around rules: instead of applying rules individually, you group them into a policy to monitor data more effectively. ADOC supports:

- **Data Quality** (e.g., customer emails must not be null).
- **Freshness** (e.g., sales data must update daily).
- **Reconciliation** (e.g., transactions in one system match another).
- **Anomaly Detection** (e.g., revenue spikes beyond normal).

Once policies are applied, ADOC monitors them continuously and raises alerts if they fail.

**Example:** If a freshness policy fails, ADOC raises an alert indicating that the expected update for your daily sales dataset did not occur within the required timeframe.

## 5. Manage Policies

Beyond monitoring, ADOC provides:

- [Import and Export Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/import-and-export-policies): Reuse rules across teams or environments.
- [Policy Groups](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/policy-groups): Organize related policies for easier management.
- [User Defined Templates](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/user-defined-templates)**:** Define custom reusable functions (business rules or transformations) once and apply them across multiple policies.

## What’s Next

After learning the flow, here’s where you might go next:

- **Get Started**: Connect your first data source
- **Discover & Explore**: Find and view your assets
- **Profile & Analyze**: Run your first data profile
- **Manage Reliability**: Apply policies and monitor alerts