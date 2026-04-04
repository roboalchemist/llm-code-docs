# Source: https://braintrust.dev/docs/reference/index.md

# Source: https://braintrust.dev/docs/observe/index.md

# Source: https://braintrust.dev/docs/integrations/sdk-integrations/index.md

# Source: https://braintrust.dev/docs/integrations/index.md

# Source: https://braintrust.dev/docs/integrations/ai-providers/index.md

# Source: https://braintrust.dev/docs/instrument/index.md

# Source: https://braintrust.dev/docs/index.md

# Source: https://braintrust.dev/docs/evaluate/index.md

# Source: https://braintrust.dev/docs/deploy/index.md

# Source: https://braintrust.dev/docs/cookbook/index.md

# Source: https://braintrust.dev/docs/api-reference/index.md

# Source: https://braintrust.dev/docs/annotate/index.md

# Source: https://braintrust.dev/docs/admin/self-hosting/index.md

# Source: https://braintrust.dev/docs/admin/index.md

# Source: https://braintrust.dev/docs/admin/automations/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automations

> Automate alerts and data management

Automations trigger actions based on events in Braintrust. Stay informed about production issues, export data to external systems, and manage data retention automatically.

## Automation types

Braintrust supports three automation types:

### Alerts

Send notifications when events occur:

* **Log alerts**: Notify when conditions are met on production logs
* **Environment alerts**: Notify when prompt environments are updated

Both alert types support:

* **Webhooks**: POST JSON payloads to custom endpoints
* **Slack**: Send messages to Slack channels

Use log alerts to catch errors, track quality degradation, or monitor usage patterns. Use environment alerts to track prompt deployments and version changes.

### S3 export

Periodically export data to AWS S3 buckets:

* **Logs**: Export traces or spans in JSON Lines or Parquet format
* **Custom queries**: Use SQL to define exactly what data to export

Use exports for archiving, offline analysis, or feeding data warehouses like Snowflake or Databricks.

### Data retention

Automatically delete old data based on time-based policies:

* **Logs**: Remove logs older than a specified period
* **Experiments**: Delete completed experiments after retention window
* **Datasets**: Remove dataset rows past their retention date

Use retention policies to manage storage costs and comply with data privacy regulations.

## Test automations

Before saving, test automations to verify configuration:

* **Alerts**: Sends a test payload to your webhook or Slack channel
* **S3 exports**: Writes and deletes a test file to your S3 bucket
* **Data retention**: Previews which data would be deleted

Testing ensures automations work correctly before they run in production.

## Monitor automation runs

View execution history and status:

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="bell" /> **Alerts** or <Icon icon="database-zap" /> **Data management**.
3. View run history, timing, and any errors

For S3 exports, you can also:

* Manually trigger exports with **Run once**
* Reset automation state to re-export all data

## Next steps

<CardGroup cols={2}>
  <Card title="Set up alerts" icon="bell" href="/admin/automations/alerts">
    Configure webhooks and Slack notifications
  </Card>

  <Card title="Manage data" icon="database" href="/admin/automations/data-management">
    Export to S3 and configure retention policies
  </Card>
</CardGroup>
