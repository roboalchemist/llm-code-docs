# Source: https://braintrust.dev/docs/guides/automations/data-management.md

# Data management

Data management automations let you export data to S3 and manage data retention for your Braintrust project.

## S3 export

S3 export automations allow you to periodically export your Braintrust data to an AWS S3 bucket. This is ideal for archiving data, running offline analysis, or feeding data into data warehouses like
[Snowflake](https://www.snowflake.com/) or [Databricks](https://databricks.com/).

<Warning>
  If you are on a hybrid deployment, S3 export is available starting with `v1.1.0`.<br />
  We plan to support export to Google Cloud Storage and Azure Blob Storage in the future. If you'd like to see this feature, please [get in touch](mailto:support@braintrust.dev).
</Warning>

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=74be50e7a60805bbb50494af2dd11c95" alt="Create S3 export automation" data-og-width="1394" width="1394" data-og-height="1486" height="1486" data-path="guides/automations/create-s3-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=9f1e71127e312a230aefd0b8307fd3bd 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=b6c5432451f44e271f540510cb12bfcc 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=2a050154148f4a187f3c2a639b1ea751 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=db5fd771785147e3bdcbcf8e37469028 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=273f94000b38768de8f371401b4f06d0 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-s3-export.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=36e43f1b9feb9c35cba72cd3c71d4e96 2500w" />

### Configure S3 export automation

* **Automation name**: A descriptive name for your export automation
* **Description** (optional): Additional context about the export automation's purpose
* **Type**: Select **S3 export**
* **Data to export**: Choose what data to export
  * **Logs (traces)**: One row per trace, including scores, token counts, cost, and other metrics
  * **Logs (spans)**: One row per span (lower level)
  * **Custom BTQL query**: Write your own BTQL query to define the exact data to export
* **S3 export path**: The S3 path to export the results to (for example, `s3://your-bucket-name/path/to/export`). Once the automation is created, this path cannot be changed
* **Role ARN**: The ARN of an IAM role you create in AWS. The UI will help you configure this role
* **Format**: The file format for the exported data. Choose between JSON Lines and Parquet
* **Interval**: How frequently the automation should run and export data. Options: 5 minutes, 30 minutes, 1 hour, 4 hours, 12 hours, 24 hours. Defaults to 1 hour

### Export limits and throughput

Each export interval can process up to 100,000 rows. This limit applies to the data type you're exporting:

* **Logs (traces)**: Rows are traces
* **Logs (spans)**: Rows are spans
* **Custom BTQL query**: Rows are whatever your query returns

If you're ingesting data faster than this limit, the automation won't finish exporting all new data each interval, and a backlog will accumulate. See [Troubleshooting](#export-falling-behind) for how to resolve this.

### Historical data export

When you create a new S3 export automation for **Logs (traces)** or **Logs (spans)**, it starts exporting from the **beginning of your data**, not from when the automation was created. This means the automation will first process all historical records before catching up to current data. If you have a large amount of historical data, the initial catch-up may take multiple intervals to complete.

For **Custom BTQL query** exports, the starting point depends on your query. If you include a date filter (e.g., `filter: created > "2025-01-01"`), the export will only include matching records.

### S3 folder structure

Exported files are organized into date-based folders in S3. The folder date represents **when the automation ran**, not when the records were created. For example, if your automation runs on 2025-12-08 and exports records that were originally created on 2025-12-01, those records will appear in the `2025-12-08/` folder.

This means if your automation is catching up on a backlog of historical data, records from multiple creation dates may end up in the same S3 folder (the folder for the day the export ran).

### Configure AWS for S3 export

The export configuration relies on you creating an IAM role that Braintrust can assume and use to write to your S3 bucket.
This role gets assumed with an [external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) that
includes your organization ID, project ID, and an automation-specific ID. If you'd like to reuse this role for multiple export automations across your organization, you can use a wildcard, for example, `bt:<your organization ID>:*`.

### Test and run export automations

Before saving or updating an export automation, you can test it to confirm behavior using the **Test automation** button. Braintrust will attempt to write (and delete) a small test file to your S3 bucket using the configured IAM role.

### View export runs and manual triggers

After creating an export automation, click the **status icon** next to your automation to open the Automation runs modal.

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/automation-status.gif?s=883befead8b5e9508d81c83c6967a3da" alt="Automation status" data-og-width="800" width="800" data-og-height="618" height="618" data-path="guides/automations/automation-status.gif" data-optimize="true" data-opv="3" />

From this modal you can:

* **View run history**: See total rows processed, data size, and duration across all runs
* **Check last run status**: View details of the most recent run, including any errors
* **Run once**: Manually trigger the automation immediately
* **Refresh**: Re-fetch the latest status from the server
* **Reset automation**: Clear the cursor and execution history, restarting the export from the beginning of your data. This is useful if the automation has encountered errors or you want to re-export all historical data.

### Troubleshooting

#### Export falling behind

If your export automation shows the following warning in the [Automation runs modal](#view-export-runs-and-manual-triggers), the automation couldn't process all available data in a single interval:

> Max iterations reached while running the cron job. This may result in the export falling behind.

This is **expected** when you first create an automation that needs to process historical data - see [Historical data export](#historical-data-export). The automation will continue catching up over subsequent runs.

However, if you see this warning **persistently after the initial catch-up**, it indicates your ongoing data ingestion rate exceeds what the automation can process per interval. To resolve this, decrease the interval (e.g., from 1 hour to 30 minutes) to run the automation more frequently.

#### Query timeouts (trace exports)

If your trace export automation fails with a timeout error like `Failed to run BrainstoreQuery: Query cancelled: Timeout` in the [Automation runs modal](#view-export-runs-and-manual-triggers), this can occur due to a bug that was resolved in data plane v1.1.27. If you're on v1.1.27 or later, reset the automation using the "Reset automation" button. If you created the automation on an older version and resetting doesn't help, try creating a new trace export automation.

### Create S3 export automations via API

When creating an S3 export automation via the API, you must perform two steps:

1. **Create the automation** using [`POST /v1/project_automation`](https://www.braintrust.dev/docs/api-reference/projectautomations/create-project_automation)
2. **Register the cron job** using `POST /automation/cron`

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

## Data retention

Data retention automations allow you to configure objects in your project to be automatically deleted after a configurable time period. This is helpful for managing storage/cost and complying with data privacy regulations.

<Warning>
  If you are on a hybrid deployment, a preview of data retention is available on `v1.1.21`.
  Data retention will soft-delete data by marking it unused, but it will not immediately purge the unused data files. A background process will clean up unused data over the next 24 hours, allowing a grace period to restore data that was unintentionally wiped by a configured retention policy.

  Ensure you have configured a service token for your data plane. See the [data plane manager docs](/guides/self-hosting/advanced#data-plane-manager) for more details.
</Warning>

<img src="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=5c0721b06b2776131f1455a105e4f4a2" alt="Create data retention automation" data-og-width="1394" width="1394" data-og-height="1035" height="1035" data-path="guides/automations/create-retention.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=280&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=4f272415ab36c009edb9c5519ada039e 280w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=560&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=240214b6f0fb3a4d786682f959843273 560w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=840&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=fbc56ced2df0af513f2bb3a55fe4c5dc 840w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=1100&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=dc479007a01e20bccb93b6363527fa72 1100w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=1650&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=6207db7e2591c036681460802267e95a 1650w, https://mintcdn.com/braintrust/F-xMKk7Z5-KPa9n1/guides/automations/create-retention.png?w=2500&fit=max&auto=format&n=F-xMKk7Z5-KPa9n1&q=85&s=2698f953b4f53019ae2e92a3487f1b67 2500w" />

### Configure data retention

* **Automation name**: An auto-generated name for your retention automation
* **Description** (optional): Additional context about the automation's purpose
* **Type**: Select **Data retention**
* **Object type**: Target object type for this retention policy. Currently supports logs, experiments, and datasets
* **Retention period**: The time period in days to retain matching objects. Once objects are older than this time period they will be automatically marked for deletion and purged from Braintrust

### Definitions and additional details

* **Logs**: Individual logs will be deleted from your project when the log creation timestamp is outside the configured retention period.
* **Experiments**: All experiment rows and experiment metadata will be deleted from your project when the experiment creation timestamp is outside the configured retention period.
* **Datasets**: Individual dataset rows will be deleted from your dataset when the row creation timestamp is outside the configured retention period. Note that the dataset itself will not be deleted, so you may write new rows to it at any time.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt