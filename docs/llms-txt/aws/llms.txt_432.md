# Source: https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/llms.txt

# Cloud Intelligence Dashboards on AWS Implementation Guide

> This implementation guide provides comprehensive instructions for deploying and using Cloud Intelligence Dashboards on AWS to gain insights into cloud cost, usage, and operations data.

- [Getting started](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/getting-started.html)
- [Data Exports](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-exports.html)
- [Generative AI Assistant](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/generative-ai.html)
- [FAQs](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/faq.html)
- [Feedback & Support](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/feedback-support.html)

## [Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/dashboards.html)

### [Foundational](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/dashboard-foundational.html)

Foundational Dashboards require CUR or Legacy CUR.

### [CUDOS, CID, KPI](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cudos-cid-kpi.html)

- [Deployment in Global Regions](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/deployment-in-global-regions.html)
- [Column Definitions](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/column-definitions.html)
- [Add Account Names ( Optional )](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/add-account-names.html)
- [Migration to CUR 2.0](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/migration-to-cur.html)
- [Deployment In China](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/deployment-in-china.html)

### [Advanced](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/dashboard-advanced.html)

Advanced Dashboards require CID Data Collection Stack.

- [Compute Optimizer Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/compute-optimizer-dashboard.html)
- [Trusted Advisor Organizational (TAO) Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/trusted-advisor-dashboard.html)
- [AWS Budgets Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/budgets-dashboard.html)
- [AWS News Feeds](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/news-feeds.html)
- [Cost Anomaly Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cost-anomaly-dashboard.html)
- [Extended Support - Cost Projection](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/extended-support.html)
- [Graviton Savings Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/graviton-savings-dashboard.html)
- [Health Events Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/health-events-dashboard.html)

### [Support Cases Radar Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/support-cases-radar.html)

AWS Support Cases Radar Dashboard provides a centralized platform to consolidate, monitor and analyze AWS Support Cases across all linked accounts and multiple AWS organizations.

### [Optional Plugins](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/optional-plugin.html)

- [Summarization Plugin](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/summarization-plugin.html)
- [AWS End User Computing (EUC) Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/euc-dashboard.html)
- [ResilienceVue Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/resiliencevue-dashboard.html)
- [Data Collection Monitor](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-monitor.html)
- [Media Services Insights Hub](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/media-services-insights.html)

### [Additional](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/dashboard-additional.html)

This section covers the following dashboards:

- [FOCUS Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/focus-dashboard.html)
- [CORA Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/cora-dashboard.html)
- [Trends Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/trends-dashboard.html)
- [DataTransfer Cost Analysis Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/datatransfer-dashboard.html)
- [AWS Marketplace Single Pane of Glass (SPG) Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/marketplace-dashboard.html)
- [Kubecost Containers Cost Allocation Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/kubecost-containers-dashboard.html)

### [SCAD Containers Cost Allocation Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard.html)

The SCAD Containers Cost Allocation Dashboard provides insights into EKS and ECS in-cluster cost based on data from CURâs Split Cost Allocation Data (SCAD) feature.

- [Prerequisites](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-prerequisites.html)
- [Deployment](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-deployment.html)

### [Post Deployment](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-post-deployment.html)

Now that you deployed the dashboard, you may proceed to the following optional post-deployment options, if theyâre relevant to your use-case:

- [Adding K8s Pods Labels or Amazon ECS Tasks Tags to the Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-add-labels-tags.html)
- [Total Cost of Ownership Using Kubernetes Labels and AWS Tags](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-tco.html)
- [Data on EKS - Cost Allocation for Spark and Flink Applications Running on EKS](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/scad-containers-dashboard-data-on-eks.html)
- [Amazon Connect Cost Insight Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/connect-cost-insight.html)

### [AWS Config Resource Compliance Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-compliance-dashboard.html)

- [Prerequisites](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-prerequisites.html)
- [Deployment: Log Archive account](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-log-archive.html)
- [Deployment: Dashboard account](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-dashboard-account.html)
- [Optional post-deployment activities and FAQ](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-post-deployment.html)
- [Teardown](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/config-resource-teardown.html)
- [Sustainability Proxy Metrics and Carbon Emissions Dashboard](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/sustainability-proxy-metrics-dashboard.html)
- [Share Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/share-dashboards.html)
- [Add organizational taxonomy](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/add-org-taxonomy.html)
- [Update Dashboards](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/update-dashboards.html)
- [Teardown](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/dashboard-teardown.html)


## [Data Collection](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection.html)

- [Deployment](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-deployment.html): Deployment of the stack consists of 2 steps.
- [Utilize Data](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-utilize-data.html)
- [Update](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-update.html)
- [Teardown](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-teardown.html)


## [Customizations](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/customizations.html)

- [Create Analysis (Required)](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/create-analysis.html)
- [Adding Cost Allocation Tags](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/adding-cost-allocation-tags.html)
- [Filtering Visuals by Cost Allocation Tags](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/filtering-visuals-by-cost-allocation.html)
- [Net Amortized cost](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/net-amortized-cost.html)
- [Organization (OU) integration](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/organization-integration.html): This content is DEPRECATED.
- [Removing Discounts](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/remove-discount.html)

### [Publishing as single sign-on (SSO) Application](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/publishing-as-sso-application.html)

- [SSO Application (Legacy Guide)](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/sso-application-legacy.html)
- [Row Level Security](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/row-level-security.html): This guide will show how you can configure Row Level Security to enable a fine grain access
- [SaaS Unit Metrics](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/saas-unit-metrics.html)
- [Tailoring Data Collector schedules](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/tailor-data-collector.html)
- [Data Collection without AWS Organizations](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/data-collection-without-org.html): When deploying AWS Cost Intelligence Dashboard (CID), customers who donât have direct access to AWS Organizations (because itâs managed by partners or separate internal teams) should first consider collaborating with the team owning AWS Management (Payer) Account to deploy CID at scale across the organization with Row Level Security implemented, ensuring each business unit can only view cost and operational data for their specific AWS accounts.
- [AWS Spend in Local Currency](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/spend-in-local-currency.html)
