# Source: https://docs.acceldata.io/api/introduction.md

# Source: https://docs.acceldata.io/documentation/introduction.md

# Introduction

Modern data platforms power critical business decisions. As data systems grow in scale and complexity, ensuring that data remains **accurate, timely, consistent, and trustworthy** becomes increasingly difficult. Data moves across pipelines, platforms, and teams, often without a single place to understand whether it is reliable, or what to do when it is not.

The **Acceldata Data Observability Cloud (ADOC)** exists to solve this problem.

ADOC provides a centralized system of record for data reliability. It continuously observes data across the lifecycle, validates it against defined expectations, and surfaces issues before they impact downstream analytics, applications, or business decisions.

On top of this foundation, **ADM (Agentic Data Management)** extends ADOC from _observability_ to _intelligent assistance_. ADM uses context from your data assets, policies, executions, and lineage to help users **ask questions, investigate issues, and take action faster**, without needing to manually navigate across tools or pages.

Together, ADOC and ADM help teams move from **reactive firefighting** to **proactive, guided data reliability management**.

## Why Data Observability Matters

In most organizations, data issues are discovered too late, after dashboards are incorrect, reports don’t reconcile, or downstream systems fail. Common challenges include:

- Data arriving late or not at all
- Incomplete or missing records after ETL jobs
- Schema changes breaking pipelines
- Mismatches between source and target systems
- Silent data drift impacting analytics and ML models

Without observability, teams rely on manual checks, fragmented tools, or user complaints to detect these problems. Even when issues are detected, understanding _why_ they happened and _what to fix_ often requires deep platform knowledge and time-consuming investigation.

ADOC addresses this gap by continuously observing data at rest and in motion, validating it against defined expectations, and making reliability **visible, measurable, and auditable**.

ADM complements this by helping users **interact with that observability context more effectively**—guiding investigations, summarizing failures, and assisting with decision-making using the full operational context of ADOC.

## How ADOC and ADM Work Together

ADOC establishes **what is happening** across your data ecosystem.
ADM helps you understand **why it happened and what to do next**.

Together, they enable organizations to:

- Discover and catalog data assets across cloud and on-prem systems
- Define expectations for data quality, freshness, consistency, and stability
- Continuously monitor data reliability using automated policies
- Detect anomalies and failures early, with contextual alerts and reports
- Investigate issues faster using lineage, execution history, and profiling
- Ask contextual questions and get guided insights using ADM
- Communicate data reliability clearly to technical and business stakeholders

This creates a shared, actionable understanding of data health across engineering, operations, and business teams.

## Key Capabilities

ADOC is built around three core capabilities, with ADM enhancing how users interact with each of them.

## 1. Discovery

Discovery is the foundation of data observability.

ADOC automatically connects to your data ecosystem and identifies available data assets—including databases, tables, files, and streams. This creates a continuously updated inventory of data across your organization.

With Discovery, you can:

- Connect to more than 60 supported data sources
- Automatically scan schemas and metadata
- Track schema and structural changes over time
- Understand where data lives and how it evolves

**Example:**
A data platform team connects Snowflake, Databricks, and S3 to ADOC. Discovery automatically catalogs all datasets, tracks schema changes, and keeps the inventory current without manual tracking.

ADM builds on this by allowing users to ask questions such as:

- _“Which assets changed schema last week?”_
- _“What downstream reports depend on this table?”_

## 2. Policies

Policies define what “good data” means for your organization.

In ADOC, policies are rule-based checks that continuously validate data against expectations such as completeness, freshness, consistency, volume, and schema stability. Policies can be applied per dataset and executed automatically or on demand.

ADOC supports multiple policy types, including:

- Data Quality
- Reconciliation
- Data Freshness
- Schema Drift
- Data Drift
- Profile Anomaly

Policies enable teams to move from assumptions about data quality to **measurable guarantees**.

**Example:**
A data team applies:

- A Data Quality policy to ensure `customer_email` is never null
- A Freshness policy to ensure daily sales data arrives before 6 AM

ADM assists by:

- Explaining why a policy failed
- Summarizing which rules contributed most to the failure
- Helping users decide whether to adjust thresholds or investigate upstream data

## 3. Insights and Actions

Insights and Actions turn monitoring into outcomes.

ADOC surfaces policy results through dashboards, alerts, execution history, lineage views, and reliability reports. These insights help teams understand **what failed, where it failed, and what is impacted**.

Actions include:

- Real-time alerts via Slack, Email, Teams, or Webhooks
- Reliability reports shared with stakeholders
- Execution-level drilldowns for root cause analysis
- Recommendations to improve data reliability

ADM enhances this experience by acting as a **guided interface** over these insights—helping users navigate failures, summarize trends, and focus on the most impactful issues.

**Example:**
A reconciliation policy fails after an ETL job. ADOC raises an alert and shows unmatched records and lineage. ADM helps summarize the failure, highlights likely causes, and guides the engineer to the relevant upstream pipeline and assets.

## Navigating ADOC

ADOC is organized to support how teams work with data day to day.

### Asset-Centric Workflow

Most actions in ADOC start from the **Asset Details page**.

From a single asset page, you can:

- View metadata and schema
- Analyze profiling statistics
- Apply and manage policies
- Review execution history
- Investigate alerts and incidents
- Understand upstream and downstream lineage

This asset-centric approach keeps context intact and reduces time spent switching tools.

### Key Areas of the Platform

- **Discover Assets** – Browse and search cataloged datasets
- **Data Reliability**– Create and manage policies
- **Alerts & Notifications** – Investigate reliability failures
- **Reports** – Track reliability trends over time
- **Settings** – Configure integrations, scoring, and permissions
- **ADM** – Interact with data reliability context using guided, agent-based assistance

## Who Uses ADOC

ADOC is designed to support multiple roles across the data organization, while providing a shared view of data reliability.

- **Data Engineers** use ADOC to monitor pipelines, detect schema changes, and validate ETL outputs.
- **Platform and SRE teams** use ADOC to track system health, execution failures, and SLA breaches.
- **Data Stewards** use ADOC to enforce data standards and ensure policy coverage.
- **Data Leaders and FinOps teams** use ADOC to measure reliability trends, control cost, and communicate trust in data.

While each role interacts with ADOC differently, the platform provides a **single, consistent source of truth** for data health.

## How to Get Started

1. **Connect your data sources:**
Set up integrations so ADOC can discover and monitor your data.
2. **Explore discovered assets:** Review schemas, profiling stats, and metadata.
3. **Apply policies to critical datasets:**
Start with high-impact tables and essential checks.
4. **Monitor results and alerts:**
Use execution history, alerts, and reports to track reliability.
5. **Expand coverage over time:**
Add more assets, policies, and reporting as needs grow.

## What’s Next

After completing this section, explore:

- [Architecture](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/adoc-architecture-an-overview) – How ADOC is deployed and secured
- [Personas](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/personas) – How different teams use ADOC and ADM
- [Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/Policies) – Deep dives into each reliability policy
- [ADM](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/adm) – How agent-based workflows help investigate and act on data issues
- [Alerts](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/alerts)  and  [Reporting](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reliability-reports) – Operationalizing data reliability at scale