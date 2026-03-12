# Source: https://docs.acceldata.io/documentation/export-and-import-manager.md

# Export and Import Manager

The **Export & Import Manager** is a centralized hub that lets you manage configuration movement across environments, such as development, staging, and production. It provides a unified interface for exporting and importing various configuration types, including **asset settings**, **notification groups**, and **policies**, ensuring consistency and efficiency across environments.

This feature helps administrators and platform teams replicate setups, streamline configuration management, and resolve conflicts easily during imports.

## Key Capabilities

### Centralized Management

Access all import and export actions from one location under:

**Settings &gt; Export & Import Manager**

From here, you can:

- Export or import configurations across multiple feature areas.
- Choose what type of configurations to manage (Assets, Policies, Notifications).
- Track import/export jobs and their status in a single view.

### Flexible Selection Options

When exporting configurations, you can choose how broad or specific your export should be:

- **All Assets:** Export the entire configuration of the environment.
- **Specific Data Sources:** Export configurations for selected sources (e.g., Snowflake, Databricks, ADLS).
- **Individual Assets:** Export settings for only specific datasets, tables, or files.

This flexibility allows you to move only what you need, saving time and avoiding unnecessary bulk transfers.

### Granular Configuration Control

You can select which configuration components to include in your export, giving you full control over what gets migrated.

Available configuration types include:

| Configuration Type | Description | 
| ---- | ---- | 
| **Profile Settings** | Includes profiling setup for assets, defining how data quality and metrics are assessed. | 
| **Incremental Settings** | Captures incremental strategy details such as offsets and refresh intervals. | 
| **Persistent Settings** | Exports data persistence and storage-related configurations. | 
| **Job Resource Settings** | Contains resource configurations for job execution, such as Spark executors and memory settings. | 
| **Reference Asset Settings** | Links assets to their referenced columns for validation. | 
| **Asset Segments** | Includes segment definitions configured for the asset. | 
| **Asset Tags** | Captures tags applied for categorization or governance. | 
| **UDT Variables** | Includes any user-defined template variables associated with the asset. | 


## Exporting Configuration

You can export configurations directly from the **Export Configuration** interface.

### Steps to Export

1. Navigate to **Settings &gt; Export & Import Manager &gt; Export Configuration**.
2. Choose an **Export Type**:
    1. **Asset Settings**
    2. **Policy Settings**
    3. **Rulesets**

3. Select your **Resources**:
    1. **Select All Resources** to export everything in the environment.
    2. **Specific Resources** to export only selected data sources or assets.

4. Choose which **Asset Settings** to include (profiling, job settings, incremental, etc.).
5. Review the **Summary** before finalizing.
6. Click **Export** to generate a downloadable configuration package (ZIP file).

The exported file can then be used for import in another environment.

**Recommendation:** Exporting all resources may take longer. For faster operations, use the **Specific Resources** option to export only what’s needed.

## Importing Configuration

The **Import Configuration** workflow allows you to bring previously exported configurations into another environment.

### Steps to Import

1. Navigate to **Settings &gt; Export & Import Manager &gt; Import Configuration**.
2. Click **Create Import Configuration**.
3. Upload the exported configuration file (`.zip`).
    1. Optionally, include a **mapping file** that defines how source entities correspond to existing ones in the target environment.
    2. A sample mapping file can be downloaded directly from the interface.

4. Click **Next** to proceed to **Conflict Resolution**.

### Conflict Resolution

When importing configurations, conflicts can occur if the same asset or setting already exists in the target environment.
The system automatically detects conflicts and provides options to handle them:

- **Overwrite Existing Configuration:** Replace existing configurations with the imported version.
- **Skip Conflicting Entries:** Ignore assets already present in the target environment.
- **Merge Settings:** Combine new and existing configuration details where applicable.

This ensures that administrators maintain full control over how imported settings affect their current environment.

### Review and Confirm Import

After resolving conflicts:

1. Review the **import summary** showing configuration details and impact.
2. Confirm to start the import job.
3. Once the import completes, the job status and summary appear in the **Import Configuration** list with timestamps and user information.

### Monitoring Import Jobs

Each import job displays key details for audit and tracking:

- **Created At / Last Updated At**
- **Job Start / Finish Time**
- **Status** (e.g., _In Progress_, _Success_, _Failed_)
- **Import Summary** (number of policies or assets imported)
- **Created By** (user who initiated the import)

This helps administrators verify successful imports and troubleshoot failures quickly.

## Benefits

- **Centralized Hub:** Manage all import/export actions in one place.
- **Efficiency:** Move configurations quickly between environments.
- **Control:** Export specific configurations or assets instead of entire setups.
- **Conflict Resolution:** Handle duplicates and merges gracefully.
- **Auditability:** Track all import/export activities for compliance and troubleshooting.

## Best Practices

### Before Export

- **Plan your exports:** Identify whether you need all configurations or only specific ones. Use the _Specific Resources_ option to reduce export time and avoid unnecessary data movement.
- **Export in logical groups:** Export related configurations together (for example, all Data Reliability policies or assets within one data source).
- **Keep backups:** Always store exported ZIP files securely before making large-scale configuration changes. This allows you to roll back if needed.
- **Check version compatibility:** Ensure both source and target environments are on **compatible platform versions**. Importing configurations from newer versions to older environments may cause validation errors.
- **Use role-based access:** Only users with **Administrator** or **Configuration Manager** roles should perform exports to maintain data consistency.

### Before Import

- **Validate configuration file integrity:** Make sure the exported ZIP is complete and uncorrupted.
- **Review configuration details:** Open the export summary to confirm what’s included before importing.
- **Use mapping files when environments differ:** If your target environment uses different naming conventions or domains, include a **mapping file** to align entities correctly.
- **Resolve duplicates strategically:** Use the _Conflict Resolution_ options carefully, prefer **Merge** for incremental updates and **Overwrite** only when you want a complete replacement.
- **Schedule imports during low-activity hours:** For large environments, import jobs may take time and temporarily lock configurations.

### After Import

- **Verify imported data:** Check the _Import Summary_ to confirm all expected assets, policies, and configurations were successfully imported.
- **Revalidate dependent components:** For example, after importing data quality policies, validate their associated rule sets or data sources.
- **Audit logs regularly:** Review import/export history in the **Import Configuration** table for timestamps, user actions, and outcomes.
- **Test before deploying changes:** In multi-environment setups, test imported configurations in a staging environment before applying them to production.

## Troubleshooting

If issues occur during export or import operations, use the following guidance to identify and resolve them quickly.

| Issue | Possible Cause | Resolution | 
| ---- | ---- | ---- | 
| **Export fails or takes too long** | Too many resources selected for export. | Try exporting specific resources instead of all assets. Break exports into smaller batches. | 
| **Import job fails or shows partial success** | Corrupted or incomplete export file. | Re-export the configuration from the source environment and retry the import. | 
| **Validation error during import** | Platform version mismatch or incompatible settings. | Ensure both environments are on the same ADOC version or later. Update and retry. | 
| **Conflict resolution prompt keeps reappearing** | Conflicting assets already exist in the target environment. | Choose “Overwrite” to replace or “Skip” to leave the existing configuration unchanged. | 
| **Mapping file errors** | Mapping file syntax is incorrect or missing required fields. | Download the **sample mapping file** from the import screen and update your mappings accordingly. | 
| **Imported assets not visible in target environment** | The import job succeeded but metadata refresh was not triggered. | Re-run metadata synchronization or refresh the Discover Assets view. | 
| **Job stuck in “In Progress”** | Large import/export or network delay. | Wait for job completion. If the job remains stuck, restart it from the **Export & Import Manager** page. | 
| **Missing permissions** | Users lack admin privileges. | Contact your ADOC administrator to assign required roles (Administrator or Configuration Manager). | 
