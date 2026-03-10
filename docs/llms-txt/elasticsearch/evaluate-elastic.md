# Source: https://www.elastic.co/docs/get-started/evaluate-elastic

﻿---
title: Evaluate Elastic during a trial
description: Build a successful proof of concept during your Elastic trial. Learn how to define success criteria, choose the right deployment and use case, measure results, and prepare for production.
url: https://www.elastic.co/docs/get-started/evaluate-elastic
products:
  - Elastic Observability
  - Elastic Security
  - Elastic Stack
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
---

# Evaluate Elastic during a trial
Use the free 14-day Elastic Cloud trial to evaluate Elastic offerings with real data and use cases. Focus your time on the scenarios that matter most to your organization, validate key capabilities, and gather evidence to support a confident decision on whether Elastic is the right choice.
Follow this guide to complete the following:
- Define high-value use cases
- Ingest representative data
- Evaluate Elastic features against success criteria
- Measure results and document outcomes for a proof of concept (PoC)

To start your trial, go to [Sign up for a free trial](https://cloud.elastic.co/registration?page=docs&placement=docs-body).
By the end of this guide, you'll have a structured trial plan, clear evaluation results, and a solid foundation for a meaningful PoC.

## What is included in your trial

To complete each step of your evaluation, your Elastic Cloud trial provides full access to the following Elastic capabilities:
- All features available in the [Search](https://www.elastic.co/docs/solutions/search), [Observability](https://www.elastic.co/docs/solutions/observability), and [Security](https://www.elastic.co/docs/solutions/security) solutions, depending on your choice of deployment and project type.
- Integrations to ingest your data using the method that best suits your use case.
- Machine learning features to evaluate anomaly detection results and search relevance, and explore visualization tools from our trained models.
- Advanced analytics to test Elasticsearch as a vector database for building modern GenAI and semantic search applications.

To learn how Elastic Cloud works, refer to the [Elastic Cloud](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud) deployment documentation.
<tip>
  If you prefer to set up Elasticsearch and Kibana in Docker for local development or testing, refer to [Local development installation (quickstart)](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/local-development-installation-quickstart). By default, new installations have a Basic license that never expires. To explore all the available solutions and features, start a 30-day free trial by following the instructions in [Manage your license in a self-managed cluster](https://www.elastic.co/docs/deploy-manage/license/manage-your-license-in-self-managed-cluster).
</tip>


## Trial limitations

During the free 14-day trial, Elastic provides access to one hosted deployment and three Serverless projects. If all you want to do is try out Elastic, the trial includes more than enough to get you started. During the trial period, some limitations apply.
**Hosted deployments**
- You can only have one active deployment at a time.
- The deployment size is limited to 8GB RAM and approximately 360GB of storage, depending on the specified hardware profile.
- Machine learning nodes are available up to 4GB RAM, or up to 8GB when using Reranker.
- Custom Elasticsearch plugins are not enabled.
- We monitor token usage per account for the Elastic Managed LLMs. If an account uses over one million tokens in 24 hours, we will inform you, then remove access to the LLM. This is in accordance with our fair use policy for trials.

**Serverless projects**
- You can have three active Serverless projects at a time.
- Search Power is limited to 100 and Search Boost Window is limited to 7 days. These [settings](/docs/deploy-manage/deploy/elastic-cloud/project-settings#elasticsearch-manage-project-search-ai-lake-settings) apply only to Elasticsearch Serverless projects.
- Scaling is limited for Serverless projects in trials. Failures might occur if the workload requires memory or compute beyond what the above search power and search boost window setting limits can provide.
- We monitor token usage per account for Elastic Managed LLMs. If an account uses over one million tokens in 24 hours, we will inform, then remove access to the LLM. This is in accordance with our fair use policy for trials.


## Before you begin

A successful trial starts with clarity about what you want to achieve. Three foundational decisions shape your trial: defining your trial goal, identifying your primary use case, and choosing the deployment type that best supports it.

### Define your trial goal

To achieve the best results, clarify what success looks like for your trial.
Consider the following questions:
- **What is the main problem you're trying to solve?** Examples: slow root-cause analysis, rising infrastructure costs, missing search relevance, or too many disconnected data sources.
- **If you choose to move forward, which team will use Elastic?**
- **What would a successful PoC show?** Faster investigations? Better visibility? Reduced spend?
- **Have you identified the KPIs or metrics that matter most?** Examples: time to detect, ingestion speed, relevance scores, or dashboard load times.

Document your trial goal now. This clarity will guide your use case selection and help you measure success at the end of your trial.

### Identify your primary use case

With your trial goal in mind, identify which Elastic solution best addresses your challenge. Elastic can support many workloads, but a focused trial generates more precise results. You can always expand to additional use cases after establishing initial success.

| Your challenge                                                   | Primary use case                                                     |
|------------------------------------------------------------------|----------------------------------------------------------------------|
| Users struggle to find relevant information across systems       | [Search](https://www.elastic.co/docs/solutions/search)               |
| Build your first search application                              | [Search](https://www.elastic.co/docs/solutions/search)               |
| Limited visibility into application performance or system health | [Observability](https://www.elastic.co/docs/solutions/observability) |
| Slow incident response and troubleshooting                       | [Observability](https://www.elastic.co/docs/solutions/observability) |
| Identify unknown unknowns through logs, traces, and metrics      | [Observability](https://www.elastic.co/docs/solutions/observability) |
| Detect and respond to endpoint security threats                  | [Security](https://www.elastic.co/docs/solutions/security)           |
| Security logs are difficult to analyze or correlate              | [Security](https://www.elastic.co/docs/solutions/security)           |
| Compliance requires centralized security monitoring              | [Security](https://www.elastic.co/docs/solutions/security)           |


### Choose your deployment type

Once you know what you want to evaluate, choose the deployment option that best supports your goals. Elastic offers two primary deployment options on Elastic Cloud.
<applies-switch>
  <applies-item title="serverless:" applies-to="Elastic Cloud Serverless: Generally available">
    - Fully managed with automatic scaling.
    - Simplified configuration and maintenance.
    - Project-based organization (Search, Observability, or Security).
    - Ideal for fast setup and focused trials of a single use case.
  </applies-item>

  <applies-item title="ess:" applies-to="Elastic Cloud Hosted: Generally available">
    - Access to all solutions in a single deployment.
    - More control over cluster configuration and sizing.
    - Traditional Elasticsearch architecture.
    - Best for evaluating multiple use cases together or when you need specific configuration options.
  </applies-item>
</applies-switch>

<tip>
  For most trials, Serverless provides the fastest path to demonstrating value. You can always explore hosted options later or migrate to production with different requirements.
</tip>

For detailed comparisons, refer to:
- [Deployment comparison](https://www.elastic.co/docs/deploy-manage/deploy/deployment-comparison): Side-by-side feature and capability comparison.
- [Differences from other Elasticsearch offerings](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/differences-from-other-elasticsearch-offerings): Understand how Elastic Cloud differs from self-managed deployments.


## Build your proof of concept

With your trial goal defined, follow this framework to build a PoC that demonstrates clear value and helps you make an informed decision about adopting Elastic.

### Example success criteria by use case

<tab-set>
  <tab-item title="Search">
    - Reduce time to find information by X%.
    - Index and search Y documents with sub-second response times.
    - Demonstrate relevance tuning for domain-specific searches.
  </tab-item>

  <tab-item title="Observability">
    - Reduce mean time to detect (MTTD) incidents by X minutes.
    - Gain visibility into application performance across Y services.
    - Centralize logs from Z disparate systems.
  </tab-item>

  <tab-item title="Security">
    - Detect X types of threats that current tools miss.
    - Reduce investigation time by Y%.
    - Demonstrate compliance reporting for Z requirements.
  </tab-item>
</tab-set>


### Ingest real data

To build a meaningful PoC, you need real-world data and not just sample datasets.

#### Why real data matters

- Results are more trustworthy for stakeholders.
- Dashboards and alerts reflect real use cases.
- Search and relevance testing becomes meaningful.
- Performance benchmarks are accurate.


#### Recommended ingestion methods

- [Elastic Agent](https://www.elastic.co/docs/reference/fleet) for logs, metrics, traces, and security data
- [Beats](https://www.elastic.co/docs/reference/beats) or [Logstash](https://www.elastic.co/docs/reference/logstash) for existing pipelines
- [Ingest pipelines](https://www.elastic.co/docs/manage-data/ingest/transform-enrich/ingest-pipelines) for transformations and enrichment
- Elasticsearch APIs for custom application ingestion

Start with a minimal dataset if needed, then expand.

### Explore key Elastic features

Once data is flowing, use the trial to validate the features that will determine long-term adoption. Take notes on what works well and where follow-up questions might be needed.
<tab-set>
  <tab-item title="Search">
    | Feature                         | Why it matters                                        | How to try it                                                                                          |
    |---------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
    | Vector search and hybrid search | Combine semantic understanding with keyword precision | [Semantic search quickstart](https://www.elastic.co/docs/solutions/search/get-started/semantic-search) |
    | Relevance tuning                | Ensure users find the most relevant results           | [Query rules](https://www.elastic.co/docs/solutions/elasticsearch-solution-project/query-rules-ui)     |
    | Search analytics                | Understand what users search for and what they find   | [Search relevance](https://www.elastic.co/docs/solutions/search/full-text/search-relevance)            |
    | Performance at scale            | Validate response times with production-like volumes  | Index a representative dataset and benchmark queries                                                   |
  </tab-item>

  <tab-item title="Observability">
    | Feature                            | Why it matters                                                | How to try it                                                                                                                                  |
    |------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
    | Log, metric, and trace correlation | Get full-stack visibility in one place                        | [Correlate data in the Applications UI](https://www.elastic.co/docs/solutions/observability/apm/find-transaction-latency-failure-correlations) |
    | APM instrumentation                | Identify slow transactions and errors                         | [APM quickstart](https://www.elastic.co/docs/solutions/observability/get-started/quickstart-monitor-your-application-performance)              |
    | Dashboards and alerts              | Monitor SLOs and respond to incidents                         | [Create custom threshold alerts](https://www.elastic.co/docs/solutions/observability/incident-management/create-custom-threshold-rule)         |
    | Machine learning anomaly detection | Automatically detect latency, throughput, and error anomalies | [Enable anomaly detection](https://www.elastic.co/docs/solutions/observability/incident-management/create-an-apm-anomaly-rule)                 |
  </tab-item>

  <tab-item title="Security">
    | Feature                  | Why it matters                                                                         | How to try it                                                                                                                                          |
    |--------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
    | Prebuilt detection rules | Detect threats without writing custom rules                                            | [Enable detection rules](https://www.elastic.co/docs/solutions/security/detect-and-alert/manage-detection-rules)                                       |
    | Dashboards               | Get useful visualizations of your environment, or create your own custom visualization | [Security dashboards](https://www.elastic.co/docs/solutions/security/dashboards)                                                                       |
    | Endpoint protection      | Prevent malware and ransomware                                                         | [Configure Elastic Defend](https://www.elastic.co/docs/solutions/security/configure-elastic-defend/configure-an-integration-policy-for-elastic-defend) |
    | Timeline                 | Investigate threats in chronological order in an interactive workspace                 | [Investigate with Timeline](https://www.elastic.co/docs/solutions/security/investigate/timeline)                                                       |
    | Threat intelligence      | Enrich alerts with threat context                                                      | [Threat intelligence integrations](https://www.elastic.co/docs/solutions/security/get-started/enable-threat-intelligence-integrations)                 |
  </tab-item>
</tab-set>


### Build your PoC deliverables

A strong PoC is essential for a good trial. Keep it simple but meaningful.
Your PoC should:
- Address the priority problem you identified in your trial goal.
- Include dashboards, searches, or workflows that matter to your teams.
- Show how Elastic improves speed, accuracy, or cost.
- Prove that Elastic can scale with your use case.
- Include metrics that stakeholders can quickly understand.

Suggested PoC deliverables:
- A short summary of your trial goal.
- A live dashboard or search interface.
- Example alerts or detections.
- Performance benchmarks or response time comparisons.
- A brief explanation of how Elastic handled your real data.


### Document your trial findings

**Track:**
- Time to ingest data.
- Performance and query speed.
- Feature coverage for your use case.
- Ease of use for developers and analysts.

**Save:**
- Screenshots of dashboards.
- Queries and scripts you tested.
- Notes on what worked well and what was missing.


### Suggested trial timeline

Most trials run for two weeks. Here's a suggested approach to maximize your trial.

#### Week 1: Foundation and initial value

For the first week, focus on the following activities:
- Set up your deployment or project.
- Connect your first data sources.
- Demonstrate basic capabilities.
- Validate that Elastic can address your use case.

We recommend the following activities for each use case:
<tab-set>
  <tab-item title="Search">
    Follow the steps in [Get started with search](https://www.elastic.co/docs/solutions/search/get-started), which include:
    1. Identify your search goals.
    2. Ingest sample data or connect a data source.
    3. Build basic search queries and test relevance.
    For targeted learning paths, go to [Quickstarts](https://www.elastic.co/docs/solutions/search/get-started/quickstarts).
    In particular, [Index and search basics](https://www.elastic.co/docs/solutions/search/get-started/index-basics) and [Semantic search](https://www.elastic.co/docs/solutions/search/get-started/semantic-search).
  </tab-item>

  <tab-item title="Observability">
    1. Review the [Observability getting started guide](https://www.elastic.co/docs/solutions/observability/get-started).
    2. Deploy Elastic Agent to monitor 1-2 hosts or services.
    3. Collect logs from a critical application.
    4. Explore metrics and logs in Kibana.
  </tab-item>

  <tab-item title="Security">
    1. Review the [Security getting started guide](https://www.elastic.co/docs/solutions/security/get-started).
    2. [Ingest security data](https://www.elastic.co/docs/solutions/security/get-started/ingest-data-to-elastic-security) from your environment.
    3. Deploy Elastic Defend to protect critical endpoints.
    4. Enable prebuilt detection rules.
    5. Investigate sample security events or anomalous activity.
    For targeted learning paths, go to [Elastic Security quickstarts](https://www.elastic.co/docs/solutions/security/get-started/quickstarts).
  </tab-item>
</tab-set>

The following resources are recommended for all use cases:
- [Data ingestion overview](https://www.elastic.co/docs/manage-data/ingest): Learn how to bring data into Elastic.
- [Fleet and Elastic Agent](https://www.elastic.co/docs/reference/fleet): Learn about Elastic Agent and integrations for connecting data sources.
- [Discover data in Kibana](https://www.elastic.co/docs/explore-analyze/discover): Learn to explore and search your data.


#### Week 2: Expansion and measurement

For the second week, focus on the following activities:
- Add a few additional data sources relevant to your use case. Refer to [Fleet integrations](https://www.elastic.co/docs/reference/fleet/manage-integrations) for available integrations.
- Focus on metrics that demonstrate clear business value. Use [Lens visualizations](https://www.elastic.co/docs/explore-analyze/visualize/lens) to highlight KPIs.
- Set up alerts for critical conditions or thresholds. Refer to [Alerting](https://www.elastic.co/docs/explore-analyze/alerting) for configuration options.
- Create dashboards that answer key stakeholder questions. Refer to [Create a dashboard](https://www.elastic.co/docs/explore-analyze/dashboards/create-dashboard) for guidance.
- Compare results against your success criteria.
- Quantify time savings, efficiency gains, or risk reduction.


## Next steps after your trial

When you're ready to move beyond your trial into production:
1. Based on your PoC, determine production sizing needs. Refer to [Production guidance](https://www.elastic.co/docs/deploy-manage/production-guidance).
2. Review [license documentation](https://www.elastic.co/docs/deploy-manage/license) to choose the right tier, and [billing documentation](https://www.elastic.co/docs/deploy-manage/cloud-organization/billing) to understand costs.
3. If moving from trial to production, plan data migration and configuration transfer. Use [Snapshot and restore](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore) to preserve your work.
4. [Contact Elastic Sales](https://www.elastic.co/contact) to discuss your trial results and production requirements.

To retain your Elastic Cloud Hosted deployment or Serverless project, refer to [Remove trial limitations](/docs/deploy-manage/deploy/elastic-cloud/create-an-organization#remove-trial-limitations) and [Maintain access to your trial projects and data](/docs/deploy-manage/deploy/elastic-cloud/create-an-organization#general-sign-up-trial-what-happens-at-the-end-of-the-trial).
<tip>
  Depending on your organization's needs, you might want to evaluate different deployment options. Elastic offers multiple deployment types, including Elastic Cloud Enterprise and Elastic Cloud on Kubernetes. Explore the [deployment options](https://www.elastic.co/docs/deploy-manage/deploy) to find the best fit for your infrastructure.
</tip>


### Expand your implementation

After proving value with one use case:
- Consider additional solutions, such as Observability + Security.
- Add data sources and integrations.
- Implement additional features such as machine learning, custom applications, and more.
- Onboard additional users in your organization.


### Getting help

- **[Elastic Community](https://discuss.elastic.co/)**: Ask questions and learn from other users.
- **[Elastic Training](https://www.elastic.co/training)**: Develop team expertise with official courses.
- **[Elastic Consulting](https://www.elastic.co/services)**: Get expert help with implementation and optimization.
- **[Elastic customer stories](https://www.elastic.co/customers/success-stories)**: Learn from organizations with similar use cases.


## Additional resources

Continue exploring Elastic's capabilities:
- **[Solutions overview](https://www.elastic.co/docs/solutions)**: Deep dive into Search, Observability, and Security capabilities.
- **[Deploy and manage](https://www.elastic.co/docs/deploy-manage)**: Comprehensive deployment and operational guidance.
- **[Manage data](https://www.elastic.co/docs/manage-data)**: Learn about data ingestion, storage, and lifecycle management.
- **[Explore and analyze](https://www.elastic.co/docs/explore-analyze)**: Master Kibana's visualization and analysis tools.