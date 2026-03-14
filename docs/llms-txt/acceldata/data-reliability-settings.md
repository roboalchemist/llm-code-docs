# Source: https://docs.acceldata.io/documentation/data-reliability-settings.md

# Data Reliability Settings

The **Data Reliability Settings** page gives you full control over how reliability data is stored, protected, optimized, validated, and audited. These settings directly affect compliance, operational cost, and system performance, making them critical for managing large-scale enterprise data operations.

ADOC groups reliability configurations into five categories:

- [Data Retention](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#1-data-retention)
- [Data Protection](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#2-data-protection)
- [Data Persistence and Optimization](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#3-data-persistence-and-optimization)
- [Asset Validation Schedule](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#4-asset-validation-schedule)
- [Profile Metrics Capabilities](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#5-profile-metrics-capabilities)
- [Score Aggregation Methodology](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/score-aggregation-methodology)
- [Audit](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings#7-audit)

## Accessing Reliability Settings

To access Reliability settings:

1. In the ADOC UI, click the  **Settings** icon in the left navigation pane.
2. Under **Data Reliability**, use the tabs to navigate between **Retention**, **Protection**, **Data** **Persistence and Optimization**, **Asset Validation Schedule**, **Profile Metric Capabilities, Score Aggregation Methodology** and **Audit**.

## 1. Data Retention

Data Retention controls how long reliability data (such as profiling metrics, validation results, and rule execution logs) is stored in ADOC before being purged.

- Keeping data longer supports compliance requirements, auditing, and long-term trend analysis.
- Shorter retention reduces storage usage and system costs.

**Example**:

- A **financial services company** may keep reliability logs for **365 days** to meet audit requirements.
- A **cost-sensitive project** may set retention to **30–60 days**.

**MinHash Calculation**

MinHash is a statistical technique used to identify similar or duplicate datasets without scanning every record.

- When enabled, ADOC can highlight duplicate or overlapping data assets, which helps with data governance, quality monitoring, and cost optimization.
- When disabled, the system skips duplicate detection, saving compute resources but reducing visibility into redundancy.

**Examples**:

- An enterprise managing large data lakes may enable MinHash to detect duplicate customer tables across business units.
- A small project with limited resources may disable MinHash to reduce compute load.

**Limitations of MinHash**

- Results are **probabilistic, not exact** — very close datasets may still be missed, or false positives may occur.
- The technique works best on **large, diverse datasets**; for small datasets, detection accuracy is limited.
- Enabling MinHash can **increase compute and storage overhead**, especially on very large data sources.

**Recommendation:** Use MinHash for enterprise-scale environments where duplicate datasets are common and governance is a priority. For cost-sensitive or smaller projects, weigh the benefits of duplicate detection against the added resource usage.

### How to Configure

1. Navigate to the **Data Retention** tab.
2. To manage **MinHash**, toggle the setting **ON** (enabled) or **OFF** (disabled).
3. Enter the desired number of days for retention.
4. Click **Save Changes**.
5. Use **Reset to Default** if you want to return to system defaults.

Recommendation

- Compliance-focused organizations: **180–365** days.
- Cost-focused teams: **30–90** days.

## 2. Data Protection

Data Protection enforces security rules on sensitive data columns (such as **PII, financial information, or regulated fields**) across ADOC. When enabled, ADOC automatically applies **masking** or restrictions to these columns if they are flagged as protected.

**Note PII (Personally Identifiable Information)** refers to any data that can identify an individual directly (e.g., name, SSN, email) or indirectly when combined with other data (e.g., date of birth, zip code). Handling PII requires stricter privacy, security, and compliance controls under regulations such as GDPR, HIPAA, and CCPA.

- **When enabled**: PII data is masked and hidden from both unauthorized users and automated workflows such as crawlers, profilers, or reporting jobs.
- **When disabled**: Masking is not applied, and flagged PII fields remain fully visible.

This ensures your organization’s **governance and compliance policies** are enforced at the system level, reducing the risk of **data leaks or unauthorized access**.

### How to Configure

1. Navigate to the **Data Protection** tab.
2. Toggle **Data Protection Enabled** to **ON** or **OFF**.
    - **ON**: PII fields are masked automatically.
    - **OFF**: No masking is applied, even if fields are flagged as PII.

3. Click **Save Changes** to apply.
4. Use **Reset to Default** if you need to revert the setting.

Recommendation Work with your **data governance or compliance team** to decide whether Data Protection should always remain enabled. For most regulated industries (finance, healthcare, retail), enabling Data Protection is strongly recommended to ensure compliance with **GDPR, HIPAA, or similar regulations**.

## 3. Data Persistence and Optimization

Data persistence settings control how ADOC handles the storage and availability of **policy execution results**. These options let you balance between **data availability** and **system efficiency**.

- **Data Persistence Enabled**
    - When **ON**: Policy execution results are stored and available for review and auditing.
    - When **OFF**: Results are not persisted, which reduces storage usage but prevents historical tracking.

- **Data Violation Download Enabled**
    - When **ON**: Users can export or download data violation results for further analysis, reporting, or integration with external systems.
    - When **OFF**: Violation results remain visible in ADOC but cannot be downloaded.

### How to Configure

1. Navigate to the **Data** **Persistence and Optimization** tab.
2. Toggle the switches for **Data Persistence Enabled** and **Data Violation Download Enabled** according to your needs.
3. Click **Save Changes** to apply.
4. Use **Reset to Default** if you need to restore original settings.

Recommendation

- Enable **Data Persistence** for production or compliance-focused environments where audit trails and policy history are important.
- Disable **Data Persistence** for test or cost-sensitive environments where long-term storage is not required.
- Enable **Data Violation Download** if your teams need to export violations for external reporting, ticketing, or investigations.
- Keep it **disabled** if you want to restrict sensitive violation data from being downloaded outside ADOC.

## 4. Asset Validation Schedule

Asset validation schedules define when ADOC runs **reference asset validation** to check the consistency and health of lookup or reference datasets. Scheduling validation helps ensure that reference data stays accurate and aligned with your operational needs.

- **Frequent validation**: Detects issues early in business-critical reference datasets.
- **Less frequent validation**: Reduces system overhead for non-critical datasets.

### How to Configure

1. Navigate to the **Asset Validation Schedule** tab.
2. Set the **frequency** (for example, daily, weekly, or a specific interval).
3. Choose the **time zone** and select the **day(s)** and **time** for validation.
4. Enter the **parallelization count** (1–5) to control how many validation jobs run in parallel.
    - Higher values: Faster completion, but more resource usage.
    - Lower values: Less resource usage, but longer execution times.

5. Toggle **Enable Asset Validation** to turn the schedule on or off.
6. Click **Apply** to save your schedule.

**Example**

- Weekly, Monday 12:00 AM (Asia/Calcutta): Suitable for moderately critical reference datasets.
- Daily, off-peak hours: Recommended for business-critical datasets where stale reference data could impact downstream processes.

Recommendation

- Use **weekly schedules** for non-critical or slowly changing reference data.
- Use **daily schedules** for high-impact datasets (e.g., currency exchange rates, compliance lists).
- Set **parallelization** higher in production clusters with more resources, and lower in cost-sensitive environments.

## 5. Profile Metrics Capabilities

The **Profile Metrics Capabilities** tab allows **tenant-level administrators** to manage how profiling operates across all assets in the tenant. It ensures consistent governance and balanced resource usage for profiling tasks.

### Access Control

Only **tenant administrators** can view and edit these configurations.

### Accessing Profile Metrics Configuration

1. Navigate to **Settings &gt; Data Reliability &gt; Profile Metrics Capabilities**.
2. Update configuration options as required.
3. Click **Save Changes** to apply the updates.

All tenant-level changes apply globally across assets unless overridden by system-level or API-based configurations.

### Configuration Options

| **Setting** | **Description** | **Value/Actions** | 
| ---- | ---- | ---- | 
| **Auto Tag** | Automatically tags columns based on detected characteristics. | Toggle ON/OFF | 
| **Histogram** | Enables distribution histograms for profiled columns. | Toggle ON/OFF | 
| **Patterns** | Enables pattern detection for profiled data. | Toggle ON/OFF | 
| **Pattern Frequency Type** | Defines pattern sampling (e.g., HEAD, TAIL). | Select value | 
| **Max Patterns** | Sets maximum number of detected patterns. | Default: 10 | 
| **Exact Count Distinct Column Values** | Enables exact distinct value computation. | Toggle ON/OFF | 


Each setting can be reverted using **Reset to Default**.

### Behavior

- Settings apply globally across all assets and users.
- Changes take effect immediately after saving.
- Tenant-level settings override user or system defaults.

### Apply Settings Confirmation

When saving tenant-level updates, ADOC prompts the administrator with a confirmation dialog to prevent unintentional overwrites.
 The **Apply Settings** dialog appears as follows:

> **Apply Settings**_Are you sure you want to update the Profile Metrics Capabilities? This action will update the default profile settings of the asset._

Administrators can choose to:

- **Overwrite profile settings for all assets:**
Select this option to replace all asset-level configurations with the updated tenant-level defaults.
> Note Any custom changes made to profile settings at the asset level will be lost.

- **Confirm or Cancel the change:**
    - Click **Confirm** to apply the new configuration.
    - Click **Cancel** to discard changes.

This safeguard ensures administrators have clear control over whether global profile settings should override localized configurations.

### Governance and Control

Tenant-level configuration helps ensure:

- **Consistency** in profiling across teams.
- **Performance Management** by disabling heavy computations if needed.
- **Flexibility** to adjust settings as operational requirements evolve.

### Example Configuration

An administrator might choose to:

- Enable **Auto Tag**, **Histogram**, and **Patterns** for enhanced profiling insight.
- Set **Pattern Frequency Type** to _HEAD_ and **Max Patterns** to _10_ for efficient sampling.
- Keep **Exact Count Distinct Column Values** disabled to minimize compute costs.

When saved, a confirmation dialog appears. Selecting **Overwrite profile settings for all assets** ensures all assets adopt the updated defaults.

Recommendation 

- Use tenant-level configuration for **enterprise-wide consistency**.
- Avoid frequent overwrites if teams manage asset-specific profiling settings.
- Review these settings periodically to align profiling behavior with performance and cost objectives.

## 6. Score Aggregation Methodology

This setting lets you select how the reliability score is calculated for your data assets driven by your DQ (Data Quality) and Reconciliation policies: whether by policy, or by rule with row-weighted averages.

For a complete explanation of each strategy, implications in UI (reports, dashboards, asset pages), and examples, see [Score Aggregation Methodology](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/score-aggregation-methodology).

## 7. Audit

The **Audit** feature provides a complete record of system and user activities within the Acceldata platform (ADOC). It enables transparency, accountability, and compliance by logging every system change and user action, helping organizations track and analyze operational and security events.

Audit logs help:

- Prevent missed incidents or unauthorized changes.
- Support compliance reviews and internal audits.
- Provide visibility into data usage and platform adoption.
- Enable root cause analysis and security forensics.

### When to Use

- **Compliance Verification:** Confirm that required policies, crawls, and configurations were executed successfully.
- **Security Oversight:** Review user activity to identify unauthorized or abnormal actions.
- **Operational Troubleshooting:** Investigate failed executions, performance delays, or workflow issues.
- **Adoption Analysis:** Track usage patterns across features to understand platform engagement.

### How to View

1. Navigate to  **Settings** -&gt; **Data Reliability -&gt; Audit**.
2. Use the filters to refine results by **Action**, **Type**, **User**, **Action Status**, **Method**, or **Entity ID**.
3. Adjust the **Date Range** (e.g., "Last 7 days").
4. Search by **Entity ID** or **Entity Name** to locate specific records.
5. Optionally, download logs as a CSV file for compliance or offline analysis.

### Audit Event Data Model

Each event captures detailed metadata to ensure a complete audit trail:

| Field | Description | 
| ---- | ---- | 
| **Tenant ID** | Internal organization identifier. | 
| **Date** | Timestamp of the change or event. | 
| **User** | Email address of the user who performed the action. | 
| **Entity Type** | The component affected (e.g., API Key, Policy, Integration). | 
| **Entity ID** | Unique ID of the entity where the event originated. | 
| **Entity Name** | Name of the entity that was changed or created. | 
| **Action** | Type of operation: Create, Update, Delete, Execute, Login, Logout, Crawl Start/End/Stop, Import, Export, etc. | 
| **Method** | Source of action — Browser or API/SDK. | 
| **Action Status** | Indicates Success, Fail, or Unknown. | 
| **Message** | Readable description (e.g., “Rule Set ‘PII Policy’ was updated”). If a user enters a custom message in the delete confirmation dialog while deleting a policy, that message is displayed in this column. | 
| **Event Data** | Optional additional context or payload. | 
| **Client IP** | IP address of the user initiating the action. | 
| **On Behalf Of** | Captures user details if the system performed an action for another user. | 


### Event Coverage

Audit logs capture both **user-initiated** and **system-generated** events across multiple areas:

| **Category** | **Entity / Area** | **Audit Events Covered** | 
| ---- | ---- | ---- | 
| **User Management** | Users / Roles / Groups | Create, Update, Delete | 
|  | API Keys | Create, Delete | 
|  | SSO Settings | Create, Update, Delete | 
| **General** | Data Sources | Create, Update, Delete, Crawl Start, Execute, Complete | 
|  | Data Plane | Create, Update, Delete | 
|  | Notification Channels | Create, Update, Delete | 
|  | Notifications Delivered | Create | 
| **Alerts & Settings** | Alerts | Update | 
|  | Data Policies (Retention, Protection, Persistence) | Create, Update, Delete | 
|  | Glossary and Templates | Create, Update, Delete | 
| **Reliability & Pipeline** | Assets and Views | Create, Update, Delete | 
|  | Rules / Rule Sets / Policies | Create, Update, Delete, Execute | 
|  | KPIs & Reports | Create, Update, Delete | 
|  | Pipelines & Policies | Create, Update, Delete | 
|  | Compute (Monitors, Orgs, Budgets, Recommendations) | Create, Update, Delete | 


### Filters

Use filters to narrow down the audit trail to specific events:

- **Time** – Today, This Week, or custom date range.
- **User** – Filter by user email or name.
- **Entity Name / Type** – Filter by affected components.
- **Action** – Filter by Create, Delete, Update, Execute, etc.
- **Status** – Success, Fail, or Unknown.
- **Method** – Browser or API/SDK.

### Download and Export

Audit data can be exported for offline use:

- **From UI:** Download filtered logs in CSV format by clicking the  download button.
- **From API:** Query and retrieve audit data programmatically using the same filters applied in the UI.

This ensures audit evidence can be archived or integrated with external governance systems.

### Retention

#### Retention Policy

Admins can configure how long audit data is retained within the Acceldata platform.

- **Retention Period:** Configurable in Days or Months.
- **Default Limit:** Acceldata retains active logs for up to **6 months**.

Recommendation  Review audit logs regularly (weekly or monthly) and before compliance reviews. Pay attention to:

- Unauthorized changes or unusual system calls.
- Repeated failures in policy execution or data crawls.
- Activities outside normal business hours.