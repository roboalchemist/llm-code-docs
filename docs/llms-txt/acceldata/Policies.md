# Source: https://docs.acceldata.io/documentation/Policies.md

# Policies

| **Concepts** | **Descriptions** | 
| ---- | ---- | 
| Policy | Policies in Acceldata Data Observability Cloud (ADOC) are used to create rules that ensure data quality and evaluate the health of data sources. Each policy can include multiple rules, and the policy passes if all rules are met. \n\nPolicies can be executed manually or at scheduled intervals, with the system tracking execution results to monitor success. | 
| Rules | Specific checks applied to data to ensure it meets defined standards. In ADOC, rules validate data against criteria like null values or specific formats. For example, a rule might check that the "Email" column contains no null values | 
| Rule Sets | Collections of related rules grouped together for application on data assets. ADOC uses rulesets to apply multiple rules simultaneously to a dataset. For example, a ruleset might include checks for null values, data formats, and value ranges on a customer data table. | 
| Enforce Policy | The act of applying defined policies to data to ensure compliance with data quality standards. In ADOC, enforcing a policy means executing the associated rules on the data. For example, enforcing a data quality policy on a sales dataset to ensure all entries have valid dates and amounts. | 
| Monitor | The continuous observation of data to detect issues or anomalies. ADOC monitors data pipelines and assets to ensure data quality and reliability. For example, monitoring a data pipeline to detect delays in data ingestion. | 
| Remediate | The process of correcting data issues identified during monitoring. In ADOC, remediation involves actions taken to fix data quality problems. For example, automatically correcting data format inconsistencies in a dataset after detection. | 
| Data Quality Policy | A set of rules and standards applied to data to ensure its quality. ADOC uses data quality policies to validate data accuracy, completeness, and consistency. For example, a policy that checks for duplicate entries and missing values in a customer database. | 
| Freshness Policy | A policy that ensures data is up-to-date and timely. In ADOC, freshness policies monitor the age of data to detect staleness. For example, alerting if the latest data in a sales report is older than 24 hours. | 
| Reconciliation Policy | A policy that compares data across different sources to ensure consistency. ADOC uses reconciliation policies to detect discrepancies between datasets. For example, comparing transaction records between two systems to identify mismatches. | 
| Anomaly Policy | A policy designed to detect unusual patterns or outliers in data. ADOC applies anomaly policies to identify data points that deviate from expected behavior. For example, detecting a sudden spike in website traffic that doesn't align with historical trends. | 
| Data Drift Policy | A policy that monitors changes in data distribution over time. In ADOC, data drift policies detect shifts that may affect data quality. For example, identifying a gradual change in customer demographics in a marketing dataset. | 
| Schema Drift Policy | A policy that tracks changes in the structure of data, such as added or removed fields. ADOC uses schema drift policies to detect structural changes that may impact data processing. For example, alerting when a new column is added to a database table. | 
| Composite Policy | A policy that combines multiple individual policies to provide a comprehensive data quality check. In ADOC, composite policies allow for complex validations by aggregating various rules. For example, a composite policy that includes data quality, freshness, and anomaly detection checks on a financial dataset. | 
