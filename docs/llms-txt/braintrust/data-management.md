# Source: https://braintrust.dev/docs/admin/automations/data-management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage data

> Export to S3 and configure retention policies

Automate data export to S3 and configure retention policies to manage storage costs and comply with data privacy regulations.

## Export to S3

Periodically export logs, experiments, or datasets to AWS S3 buckets.

<Warning>
  For hybrid deployments, S3 export is available starting with v1.1.0.

  We plan to support export to Google Cloud Storage and Azure Blob Storage in the future. If you'd like to see this feature, please [get in touch](mailto:support@braintrust.dev).
</Warning>

### Create S3 export

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="database-zap" /> **Data management**.
3. Click **+ Create automation**.
4. Select **S3 export** type.
5. Configure export settings:
   * **Name**: Identify the export.
   * **Data to export**: Logs (traces), Logs (spans), or Custom BTQL query.
   * **S3 path**: Target bucket and prefix (e.g., `s3://my-bucket/braintrust/logs`). Once the automation is created, this path cannot be changed.
   * **Role ARN**: IAM role ARN that Braintrust will assume.
   * **Format**: JSON Lines or Parquet.
   * **Interval**: How often to export (5 min to 24 hr).
6. Click **Test automation** to verify S3 access.
7. Click **Save**.

### Configure AWS IAM

When creating an S3 export, Braintrust provides step-by-step instructions to configure the required IAM role.

1. In the export configuration dialog, expand **Role creation instructions**.
2. Follow the guided steps to create an IAM role with the correct trust policy and S3 permissions.

### Export data types

**Logs (traces)**: One row per trace with scores, metrics, and metadata. Use this for high-level analysis.

**Logs (spans)**: One row per span for detailed execution traces. Use this for debugging or fine-grained analysis.

**Custom query**: Define exactly what data to export using SQL or BTQL:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  SELECT id, input, output, scores, metadata
  FROM project_logs('project-id', shape => 'traces')
  WHERE metadata.environment = 'production'
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  select: id, input, output, scores, metadata
  from: project_logs('project-id') traces
  filter: metadata.environment = 'production'
  ```
</CodeGroup>

### S3 folder structure

Exported files are organized by export run date:

```
s3://my-bucket/braintrust/logs/
  2025-12-08/
    export_001.jsonl
    export_002.jsonl
  2025-12-09/
    export_001.jsonl
```

The folder date represents when the automation ran, not when records were created. Historical data exports may contain records from multiple creation dates in a single folder.

### Export throughput

Each export interval can process up to 100,000 rows:

* For traces: 100,000 traces per interval
* For spans: 100,000 spans per interval
* For custom queries: 100,000 result rows per interval

If you're ingesting data faster than this limit, decrease the interval (e.g., from 1 hour to 30 minutes) to prevent backlog.

### Historical data

New S3 exports start from the beginning of your data, not from creation time. The automation processes all historical records before catching up to current data.

For large datasets, initial catch-up may take multiple intervals. This is expected behavior.

### Monitor exports

View export status and history:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="database-zap" /> **Data management**.
3. Click the status icon next to your export.
4. View run history, rows processed, data size, and timing.

From this modal:

* **Run once**: Manually trigger an immediate export.
* **Reset automation**: Clear history and restart from the beginning.
* **View errors**: See failure details and troubleshoot issues.

### Troubleshooting

**Export falling behind**: If you see "Max iterations reached" warnings:

* This is normal during initial historical data processing.
* If it persists after catch-up, decrease the interval to run more frequently.
* Consider splitting into multiple exports with BTQL filters.

**Query timeouts**: For trace exports timing out:

* Ensure you're on data plane v1.1.27 or later.
* Use the **Reset automation** button to restart.
* If problems persist, create a new trace export automation.

**IAM errors**: If test automation fails with permission errors:

* Verify the IAM role ARN is correct.
* Check the trust policy includes the correct external ID.
* Ensure S3 policy grants required permissions.
* Confirm the bucket and prefix exist.

### Create S3 exports via API

When creating an S3 export automation via the API, you must perform two steps:

1. **Create the automation** using [`POST /v1/project_automation`](https://www.braintrust.dev/docs/api-reference/projectautomations/create-project_automation).
2. **Register the cron job** using `POST /automation/cron`.

<Warning>
  If you create an S3 export automation via the API, you must call `POST /automation/cron` after creating the automation to register it. This step is automatically handled when creating automations through the UI, but is required when using the API directly. If you skip this step, you will encounter validation errors when attempting to view the automation status or trigger it manually.
</Warning>

Here's an example of registering the cron job after creating an automation:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
curl -X POST https://api.braintrust.dev/automation/cron \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -d '{
    "automation_id": "<YOUR_AUTOMATION_ID>",
    "cron": {
      "type": "btql_export"
    },
    "service_token": "<YOUR_API_KEY>"
  }'
```

Replace `<YOUR_AUTOMATION_ID>` with the ID returned from the `POST /v1/project_automation` call, and `<YOUR_API_KEY>` with your API key or service token. Use your API key for the `Authorization` header to authenticate the API call. For the `service_token` field in the request body, you can use either an API key (`sk-*`) or a service token (`bt-st-*`) that has **read permission on the project** containing the automation. This can be the same API key used for authentication.

## Configure retention

Automatically delete old data to manage storage and comply with regulations.

### Create retention policy

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="database-zap" /> **Data management**.
3. Click **+ Create automation**.
4. Select **Data retention** type.
5. Configure settings:
   * **Object type**: Logs, Experiments, or Datasets.
   * **Retention period**: Days to keep data before deletion.
6. Click **Save**.

<Warning>
  Retention policies permanently delete data. Deleted logs, experiments, and dataset rows cannot be recovered.
</Warning>

### How retention works

**Logs**: Individual logs are deleted when their creation timestamp exceeds the retention period.

**Experiments**: Entire experiments (metadata and all rows) are deleted when the experiment creation timestamp exceeds the retention period.

**Datasets**: Individual dataset rows are deleted when their creation timestamp exceeds the retention period. The dataset itself remains and can accept new rows.

### Soft deletion

For hybrid deployments (v1.1.21+), data is soft-deleted by marking it unused. A background process purges unused files within 24 hours, providing a grace period to restore accidentally deleted data.

<Note>
  Configure a service token for your data plane to enable retention. See [Data plane manager](/admin/self-hosting/advanced#data-plane-manager) for details.
</Note>

### Common retention patterns

**Production logs**: 90 days

```
Keep recent logs for debugging, delete older data to manage costs.
```

**Development logs**: 7 days

```
Keep short-term history for active development, clean up test data quickly.
```

**Experiments**: 180 days

```
Retain completed evaluations for half a year, then archive or delete.
```

**Compliance**: 30 days

```
Meet regulatory requirements by automatically deleting user data after 30 days.
```

## Next steps

* [Set up alerts](/admin/automations/alerts) to monitor data quality
* [View logs](/observe/view-logs) to understand what gets exported
* [Export data](/annotate/export) via the API for one-time exports
* [Self-hosting advanced](/admin/self-hosting/advanced) for data plane configuration
