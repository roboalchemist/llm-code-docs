# Source: https://docs.acceldata.io/documentation/apply-policies-and-monitor-reliability.md

# Apply Policies and Monitor Reliability

After profiling a dataset, the next step is to define what “good data” looks like and monitor it continuously. In ADOC, a **policy** is a set of [Rules or Rule Sets](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/rules-and-rulesets)  that defines your expectations for a dataset. Each policy can include one or more rules, and a policy is considered **passing** only if all its rules are met.

Policies help you enforce **data quality, freshness, reconciliation, anomaly detection, data drift, and schema drift rules**, ensuring datasets remain reliable over time.

All policy actions are performed **per dataset in the Asset Details page**, which serves as the hub for monitoring and management.

**Example:**

- A **Data Quality** policy might include rules such as “customer email cannot be null” and “order total must be greater than zero.”
- A **Freshness** policy might include rules like “sales data must refresh daily before 6 AM.”

## Workflow Overview

### 1. Open the Asset Details Page

1. In **Discover Assets**, locate the dataset you want to monitor.
2. Click the dataset name to open the **Asset Details page**.

### 2. Access Policies

1. Navigate to the **Policies tab** in the Asset Details page.
2. Here you can:
    - View existing policies
    - Create new policies
    - Modify rules or thresholds

## Apply Policies

Policies are applied per dataset, and you can configure multiple policies for the same dataset depending on business needs.

Each policy type has its own criteria and configuration:

- [Data Quality Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-quality-policy)
- [Reconciliation Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/reconciliation-policy)
- [Data Freshness Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-freshness)
- [Data Anomaly Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-anomaly-policy)
- [Data Drift Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-drift-policy)
- [Schema Drift Policy](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/schema-drift-policy)

### Choosing the Right Policy Type

| **Policy Type** | **Primary Purpose** | **When to Use** | **Execution Frequency** | 
| ---- | ---- | ---- | ---- | 
| **Data Quality** | Validate data against rules | Ensure data meets business requirements | On-demand or Scheduled | 
| **Reconciliation** | Compare source and target data | Verify data integrity after movement/transformation | After ETL/ELT processes | 
| **Data Freshness** | Monitor data update timeliness | Ensure data arrives within SLA | Event-triggered (hourly | 
| **Schema Drift** | Detect structure changes | Prevent breaking changes to pipelines | Event-triggered (after crawl) | 
| **Data Drift** | Detect distribution changes | Monitor statistical pattern shifts | Event-triggered (after profile) | 
| **Profile Anomaly** | Detect unusual metric patterns | Catch data quality degradation early | Event-triggered (after profile) | 


### Policy Combinations for Comprehensive Monitoring

**Complete table monitoring:**

1. **Data Quality policy:** Validate business rules
2. **Data Freshness policy:** Ensure timely updates
3. **Schema Drift policy:** Protect against structure changes
4. **Profile Anomaly policy:** Detect quality degradation

**ETL pipeline monitoring:**

1. **Data Freshness policy:** Monitor source data arrival
2. **Reconciliation policy:** Validate transformation accuracy
3. **Data Quality policy:** Check output data quality
4. **Schema Drift policy:** Ensure schema compatibility

**Machine learning feature monitoring:**

1. **Data Drift policy:** Detect feature distribution changes
2. **Profile Anomaly policy:** Catch statistical anomalies
3. **Data Quality policy:** Validate data completeness
4. **Data Freshness policy:** Ensure training data is current

### Getting Started Checklist

**Phase 1: Critical Assets (Week 1-2)**

- Identify 3-5 most critical tables
- Create Data Quality policies with 3-5 essential rules
- Enable Data Freshness monitoring with basic SLAs
- Set up notification channels

**Phase 2: Data Movement (Week 3-4)**

- Add Reconciliation policies for ETL processes
- Enable Schema Drift monitoring on production tables
- Configure alerts to appropriate teams

**Phase 3: Advanced Monitoring (Month 2)**

- Enable profiling on critical assets
- Create Profile Anomaly policies
- Add Data Drift policies for ML features
- Fine-tune sensitivity and thresholds

**Phase 4: Expand and Optimize (Month 3+)**

- Extend monitoring to more assets
- Optimize alert thresholds based on feedback
- Document data quality standards
- Establish incident response procedures

## Monitor Compliance

Once policies are applied, ADOC continuously checks your data.

- Alerts are raised if any policy fails, allowing early intervention before downstream impacts.
- Execution history shows which rules passed or failed.
- Quality scores help track overall data health.

**Example alerts**:

- Missing or null values in a critical column.
- Daily data not arriving on schedule.
- Totals mismatching across systems.
- Revenue spikes outside normal trends.

### Take Action

- Investigate alerts directly in the **Alerts** page.
- Use system recommendations to fix data issues.
- Adjust policy thresholds or rules as needed.

## Managing Policies

- **Export & Import**: Share policies across teams or environments.
- **Policy Groups**: Organize related policies for easier management.
- **Combine with Profiling**: Policies rely on profiling statistics, so ensure profiling is up-to-date before applying policies.

## Next Steps

- Choose a dataset that has been profiled.
- Explore policy types.
- Apply a policy and monitor alerts to ensure data reliability.

Note Keep this page as a central guide to policies, linking to separate detailed docs for each policy type. Every dataset action (profiling, applying policies, investigating alerts) happens in the **Asset Details page**.