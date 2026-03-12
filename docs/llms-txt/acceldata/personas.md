# Source: https://docs.acceldata.io/documentation/personas.md

# Personas

ADOC helps your data teams manage complex data systems reliably and cost effectively. 

These are few of the critical ADOC personas:

### Persona: Data Engineer

Data Engineers are responsible for building and maintaining scalable, reliable data pipelines. 

| Task | Reference | 
| ---- | ---- | 
| Tracks data pipeline execution across environments to verify planned jobs run and spot any delays or failures. | [Understanding the Pipeline Run Details](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/understanding-the-pipeline-run-details) | 
| Track and observe schema changes across datasets to avoid task failures or report field level changes. | [Schema Changes](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/schema-drift-policy) | 
| Ensure that critical data are fresh and up to date. | [Data Freshness Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-freshness) | 
| Monitor data volume and ingestion lag to detect silent pipeline failures or data loss | [Cadence](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/asset-details#navigation-tabs) | 
| Tracks data flow from source to destination to quickly review changes, troubleshoot issues, and detect dependencies. | [Lineage](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/lineage) | 
| Automates work failure, data anomaly, and SLA breach warnings. Receives Slack, email, or ticketing notifications to act before users are affected. | [Alerts & Notifications](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/alerts-and-notifications) | 


---

### Persona: DevOps/Site Reliability Engineer

DevOps and SREs focus on the performance, availability, and cost-efficiency of the data infrastructure. 

| Task | Reference | 
| ---- | ---- | 
| Monitors CPU, RAM, disk I/O, and service availability to identify data processing or ingestion bottlenecks. | [Data Plane Observability](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-plane-health-monitor) | 
| Integrates real-time notifications to quickly address pipeline, service, and data access incidents. Reduces mean time to resolution(MTTR). | [Notifications and Notification Groups](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/notifications-and-notification-groups) | 
| Investigates data stack component logs and traces to fix faults, latency, and service outages. | [Alerts](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/alerts) | 
| Performs root cause analysis (RCA) when data delivery, pipeline completion, and platform uptime SLAs are missed. | [Control Pipeline](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/control-pipeline) | 


### Persona: Data Steward

Data Stewards manage data ownership, quality, and associated costs across teams. Using Spend Intelligence, Chargeback Dashboards, and policy-based Recommendations in ADOC, they track usage and enforce data standards. This ensures data is accurate, cost-effective, and aligned with business needs.

### Persona: Data Leader / FinOps Manager

Data Leaders and FinOps Managers focus on maintaining trust, compliance, and governance at scale. In ADOC, they leverage Data Reliability Policies, Rulesets, Lineage, and Asset Profiling to ensure data quality and auditability. These capabilities support strategic decision-making and regulatory alignment across the organization.

| **Task** | **Reference** | 
| ---- | ---- | 
| Ensure all data is trustworthy, compliant, & governed. | - [Data Reliability Policies](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/apply-policies-and-monitor-reliability)\n- [Rules and Rule Sets](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/rules-and-rulesets)\n- [Data Lineage](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/lineage)\n- [Profile Assets](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/profile-assets) | 
