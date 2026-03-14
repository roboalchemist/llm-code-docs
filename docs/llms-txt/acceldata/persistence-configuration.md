# Source: https://docs.acceldata.io/documentation/persistence-configuration.md

# Persistence Configuration

Persistence Configuration defines **where and how ADOC stores policy execution outputs**, including:

- Good records
- Bad records
- Summary (Metadata) records

Starting from **ADOC 26.3.0**, persistence management is centralized and template-driven. This allows organizations to:

- Standardize storage paths across teams
- Organize outputs by policy, datasource, or time
- Improve governance and auditability

Persistence behavior is controlled at two levels:

1. **Tenant Level**: Define reusable storage configurations
2. **Policy Level**: Choose or override the tenant configuration

The storage **base path and credentials** continue to be defined at the data plane level.

## How Persistence Works in ADOC

Persistence path resolution happens in layers:

### Data plane - Global Storage Secret

Defines:

- Storage type
- Type specific information like bucket / container
- Credentials

This remains unchanged in 26.3.0.

### Dataplane - Application Configuration

Defines:

- `MEASURE_RESULT_SAVE_PATH`
    - Optional path component used for result storage.
    - For LOCAL storage types: Treated as the full base path (supports volume mounts).
    - For Non-LOCAL storage types (e.g., S3, ADLS, GCS): Appended to the base bucket/container path.

**Example (Non-LOCAL):** If base path = `s3a://bucket`

and `MEASURE_RESULT_SAVE_PATH = dq-results`

Final base becomes: **s3a://bucket/dq-results**

## Tenant-Level Persistence Configuration

Defines:

- Path suffix templates
- File formats for Good and Bad records
- Default behavior for policies

## Policy-Level Persistence Configuration

Allows a policy to:

- Use the tenant default configuration
- Select a saved configuration
- Define a custom path template

## How to Use Persistence Configuration

### Configure Tenant-Level Persistence

If you want consistent storage structure across policies, configure it at the tenant level.

Navigate to **Settings (gear icon)** → **Data Reliability** → **Persistence Configurations**. You will see a list of existing configurations.

Note Every tenant automatically has a **default configuration** named: `Acceldata`

- For existing tenants, this default preserves backward-compatible paths.
- For new tenants, it is created during onboarding.

Note **Any saved tenant-level configuration can be designated as the new default configuration for the tenant.** You may use this default as-is or create new configurations.

#### Create a New Configuration

Click the  **Add Configuration** button on the **Persistence Configuration** page.

Each configuration defines:

- Good Records Template
- Bad Records Template
- Metadata Template
- Output Format (Good/Bad only)

Note 

- Summary (Metadata) records are always stored in JSON format.
- Templates define only the **suffix**.
- Full paths such as: **s3://bucket/…** are not allowed in templates.
- The final storage path is: `<Dataplane Base Path> + <Dataplane Save Path (if configured)> + <Template Suffix>`

#### Example Template

`{{DATASOURCE_NAME}}/{{POLICY_NAME}}/{{REQUEST_ID}}/{{RECORD_TYPE}}`

This would organize results by:

- Datasource
- Policy
- Execution
- Record type

### Apply Configuration at Policy Level

When editing or creating a policy by navigating to  **Manage Policies** → **Open Policy** → **Edit** → **Advanced Settings**, under persistence configuration, click the drop-down to find three options:

- **SYSTEM DEFAULT** 
Uses tenant default configuration at execution time. If tenant default changes, future executions of that policy automatically use the new default.
- **Saved Configuration**
This configuration explicitly binds the policy to a selected configuration. Even if this configuration is also the tenant default, it is locked to the policy. Note that changes to tenant default do NOT affect this policy. Use this when:
    - Different teams require different folder structures.
    - Certain policies must always follow a specific storage layout.

- **CUSTOM**
Allows you to define custom suffix templates directly in the policy. Use this when:
    - Only one policy needs a unique structure.
    - You want to temporarily override the tenant configuration. 

All validation rules apply to custom templates. Define custom suffix templates directly in the policy.

### Change Good/Bad Record Path for a Policy

1. Go to **Manage Policies.**
2. Open a policy -&gt; **View Policy** -&gt; **Edit Policy**. The Edit Policy page is displayed with the policy summary details. 
3. Go to the **Configure Execution Details** step and click the  **Advanced Execution Settings** dropdown.
4. Under **Persistence Configuration**, select one of the following: **System Default, Active configurations,** or **CUSTOM.**
5. Define Good records, Bad records, and Metadata templates.
6. Click **Save**.

From the next execution onward, records will be written to the new path.

Note Previous executions prior to changing the Good/Bad record path for this policy remain unchanged.

---

## Manage Persistence Configuration Using APIs

In addition to configuring persistence paths through the ADOC user interface, administrators and automation workflows can also manage persistence configurations using **REST APIs**.

These APIs allow you to:

- Retrieve the persistence configuration associated with a policy
- Update policy-level persistence settings
- Create and manage tenant-level persistence configurations
- Validate and preview suffix templates
- Retrieve available template variables
- Determine whether a dataplane supports templated persistence paths

This enables organizations to automate persistence configuration management as part of **CI/CD pipelines, governance workflows, or infrastructure automation**.

For detailed API reference and examples, see [Persistence Configuration APIs](https://docs.acceldata.io/acceldata-data-observability-cloud/api/persistence-paths).

---

## Template Variables

Templates use predefined variables to dynamically build storage paths. Click **View Available variables** to view the **Available Template Variables** wizard on the right.

| **Variable** | **Description** | 
| ---- | ---- | 
| `{{POLICY_TYPE}}` | Policy type, lower cased (data-quality, reconciliation, auto-anomaly) | 
| `{{POLICY_NAME}}` | Policy name (sanitized for path safety) | 
| `{{POLICY_ID}}` | System policy ID | 
| `{{REQUEST_ID}}` | Unique ID per execution (recommended for uniqueness) | 
| `{{EXECUTION_ID}}` | Internal execution ID | 
| `{{RECORD_TYPE}}` | successrecords, errorrecords, summary, topanomalies | 
| `{{ASSET_NAME}}` | Asset name (sanitized) | 
| `{{DATASOURCE_NAME}}` | Datasource name (sanitized) | 
| `{{TIME:format}}` | Execution start time in Joda-Time format | 
| `{{EPOCH_MILLIS}}` | Execution timestamp in milliseconds | 


---

## Important Template Rules

- Must include `{{RECORD_TYPE}}` to ensure that Good, Bad, and Metadata records are stored in separate folders.
- Must include atleast one `{{REQUEST_ID}}` or`{{EXECUTION_ID}}`to prevent overwriting results from multiple executions.
- Allowed Characters in Static Text:
    - Unicode Letters
    - Unicode Numbers
    - _ (underscore)
    - '-' (hyphen)
    - = (equals)

- Use / to separate path segments.
- Run Time Sanitization: User-defined values are sanitized automatically. User-defined values such as:
    - `POLICY_NAME`
    - `ASSET_NAME`
    - `DATASOURCE_NAME`

are automatically sanitized.

- The format defined will only be used by spark executions. Pushdown executions use the format set in datasource configuration.

Sanitization behavior:

- `/` replaced with `__`
- Reserved names (e.g., CON) wrapped as `__CON__`
- Invalid characters replaced
- Leading/trailing dots removed
- Maximum length: 200 characters

---

## Common Path Suffix Patterns

### Organize results by team

To store execution results in team-specific folders, create a tenant-level persistence configuration with a static team folder name.

Example: `TEAM_A/{{POLICY_NAME}}/{{EXECUTION_ID}}/{{RECORD_TYPE}}`

After you save the configuration, select it in the policy settings.

All executions of that policy will write results under the **TEAM_A** folder.

Use this approach when multiple teams share the same storage location but need logical separation.

### Organize results by data source

To group results by datasource, use the {{DATASOURCE_NAME}} variable in the template.

Example template: `{{DATASOURCE_NAME}}/{{POLICY_NAME}}/{{EXECUTION_ID}}/{{RECORD_TYPE}}`

This structure creates a separate folder for each datasource.

Use this option when you want storage organized based on data origin.

### Organize results by execution time

To organize results by date or time, use the {{TIME:format}} variable.

You can define the format using Joda time patterns.

Example Template: `{{POLICY_NAME}}/{{TIME:yyyy}}/{{TIME:MM}}/{{TIME:dd}}/{{EXECUTION_ID}}/{{RECORD_TYPE}}`

This structure creates a year/month/day folder hierarchy.

Use this option when you need chronological storage for reporting, retention, or archival purposes.

#### Valid Time Formats

| **Format** | **Example Output** | **Valid** | 
| ---- | ---- | ---- | 
| `yyyy-MM-dd` | 2026-02-04 | Yes | 
| `yyyyMMdd` | 20260204 | Yes | 
| `yyyy/MM/dd` | 2026/02/04 | Yes (creates path segments) | 
| `yyyy-MM` | 2026-02 | Yes | 
| `yyyy-MM-dd'T'HH-mm-ss` | 2026-02-04T14-30-45 | Yes | 


#### Invalid Time Formats

| **Format** | **Example Output** | **Reason** | 
| ---- | ---- | ---- | 
| `HH:mm:ss` | 14:30:45 | Colon (:) is not allowed | 
| `Z` | +0530 | Plus sign (+) is not allowed | 
| `yyyy-MM-dd'T'HH:mm:ss` | 2026-02-04T14:30:45 | Colon (:) is not allowed | 


---

## Import & Export of Policies

When exporting policies:

| Type | Behavior on Import or Export | 
| ---- | ---- | 
| System Default | Uses destination tenant default | 
| Saved Configuration | Reused if exists, otherwise created | 
| Custom | Preserved as-is | 


---

## Limitations

- Storage bucket and base path cannot be changed at tenant or policy level.
- Summary records always use JSON format.
- Dataplanes &lt; v26.3.0 continue using legacy prefix until upgraded.

---

## Related Documentations

The following resources provide additional information about configuring and managing persistence paths:

- [Persistence Configuration APIs](https://docs.acceldata.io/acceldata-data-observability-cloud/api/persistence-paths) - Manage persistence configurations programmatically using REST APIs.
- [Global Storage Configuration](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/global-storage) - Configure the storage bucket and base path used by the data plane.
- [Data Plane Installation](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) - Configure data plane storage settings and application configuration.