# Source: https://braintrust.dev/docs/admin/automations/alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up alerts

> Configure webhooks and Slack notifications

Alerts notify you when events occur in Braintrust. Send notifications to webhooks or Slack channels to catch errors, track quality issues, monitor usage patterns, or track prompt deployment changes.

<Note>
  [Enable the Slack integration](/admin/organizations#enable-slack-integration) before creating an alert to send to a Slack channel.
</Note>

## Alert types

Braintrust supports two types of alerts:

* **Log alerts**: Trigger when conditions are met on production logs
* **Environment alerts**: Trigger when prompt environments are assigned or removed

## Create a log alert

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="bell" /> **Alerts**.
3. Click **+ Alert**.
4. Enter alert name.
5. Select **Log event** as the event type.
6. Configure alert conditions:
   * **SQL filter**: Query that defines which logs trigger the alert. See [Write SQL filters](#write-sql-filters) for examples.
   * **Interval**: How often to check for matching logs (5 min, 30 min, 1 hr, 4 hr, 12 hr, 24 hr).
7. Select an action type:
   * **Webhook**: Enter the webhook URL to send a [JSON payload](#webhook-payloads) to.
   * **Slack**: Select a Slack channel using the searchable dropdown.

     The channel list refreshes automatically every 7 days. To trigger a manual refresh, click **Refresh channels**. If your channel doesn't appear, you can enter its <Tooltip tip="To find a channel ID in Slack: Right-click the channel name, click &#x22;View channel details&#x22;, and scroll to the bottom and copy the channel ID.">channel ID</Tooltip> manually.
8. Click **Test alert** to verify the configuration.

   Braintrust runs the filter on recent logs. If matching logs exist, a test payload is sent. Check your webhook endpoint or Slack channel for the test message.
9. Click **Save**.

<Tip>
  You can also create log alerts directly from the <Icon icon="activity" /> **Logs** or <Icon icon="chart-no-axes-column" /> **Monitor** pages. Apply filters to your logs, then select <Icon icon="ellipsis" /> > **Create alert from filters** in the toolbar. The SQL filter automatically populates with your current filters.
</Tip>

## Create an environment alert

Environment alerts notify you when prompt environments are updated. Use them to track deployments, monitor version changes, or trigger downstream workflows when prompts are promoted across environments.

1. Go to <Icon icon="settings-2" /> **Settings**.
2. Under **Project**, select <Icon icon="bell" /> **Alerts**.
3. Click **+ Alert**.
4. Enter alert name.
5. Select **Environment update** as the event type.
6. Optionally filter by specific environments (e.g., only alert on "production" changes).
7. Select an action type:
   * **Webhook**: Enter the webhook URL to send a [JSON payload](#webhook-payloads) to.
   * **Slack**: Select a Slack channel using the searchable dropdown.

     The channel list refreshes automatically every 7 days. To trigger a manual refresh, click **Refresh channels**. If your channel doesn't appear, you can enter its <Tooltip tip="To find a channel ID in Slack: Right-click the channel name, click &#x22;View channel details&#x22;, and scroll to the bottom and copy the channel ID.">channel ID</Tooltip> manually.
8. Click **Save**.

<Note>
  Environment alerts trigger immediately when environments are updated. Unlike log alerts, they don't have intervals or SQL filters. Testing is not available for environment alerts.
</Note>

## Common alert patterns

<Tabs>
  <Tab title="Log alerts">
    **Error monitoring**: Catch production issues immediately.

    * SQL filter: `error IS NOT NULL AND metadata.environment = 'production'`
    * Action: Post to Slack #incidents channel or create tickets in issue trackers

    **Quality thresholds**: Track when model performance drops below acceptable levels.

    * SQL filter: `scores.factuality < 0.8 AND metadata.environment = 'production'`
    * Interval: Run hourly to catch quality regressions
    * Action: Send to monitoring systems or trigger automated remediation

    **Cost monitoring**: Alert on expensive requests.

    * SQL filter: `metrics.estimated_cost > 1.0`
    * Action: Webhook to cost tracking systems or budget management tools

    **Model-specific issues**: Alert on problems with a particular model.

    * SQL filter: `metadata.model = 'gpt-4o' AND (error IS NOT NULL OR scores.accuracy < 0.8)`
    * Action: Post to team channel for model performance investigation

    **Feature-specific monitoring**: Track specific workflows or user segments.

    * SQL filter: `metadata.user_tier = 'enterprise' AND metadata.feature = 'summarization'`
    * Action: Post to team channel for priority investigation

    **Combined conditions**: Alert on multiple conditions for critical requests.

    * SQL filter: `(scores.accuracy < 0.7 OR error IS NOT NULL) AND metadata.priority = 'high'`
    * Action: Immediate Slack notification to on-call team

    **Usage spikes**: Monitor when request volume exceeds normal levels.

    * Action: Use external systems to track historical rates and webhook alerts to capture spikes
  </Tab>

  <Tab title="Environment alerts">
    **Deployment tracking**: Monitor when prompts are promoted to production.

    * Environment filter: `production`
    * Action: Post to Slack #deployments channel

    **Multi-environment monitoring**: Track changes across all environments.

    * Environment filter: Leave empty to monitor all environments
    * Action: Webhook to deployment tracking system

    **Critical environment protection**: Get immediate notification of staging or production changes.

    * Environment filter: `staging, production`
    * Action: Slack notification to team channel

    **Audit trail**: Log all environment changes to external systems.

    * Environment filter: Leave empty
    * Action: Webhook to audit logging service
  </Tab>
</Tabs>

## Webhook payloads

<Tabs>
  <Tab title="Log alerts">
    When a log alert triggers a webhook, it sends this JSON structure:

    ```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    {
      "organization": {
        "id": "org_123",
        "name": "your-organization"
      },
      "project": {
        "id": "proj_456",
        "name": "your-project"
      },
      "automation": {
        "id": "c5b32408-8568-4bff-9299-8cdd56979b67",
        "name": "High-Priority Factuality",
        "description": "Alert on factuality scores for priority logs",
        "event_type": "logs",
        "btql_filter": "metadata.priority = 0 AND scores.Factuality < 0.9",
        "interval_seconds": 3600,
        "url": "https://braintrust.dev/app/your-org/p/your-project/configuration/alerts?aid=..."
      },
      "details": {
        "is_test": false,
        "message": "High-Priority Factuality: 5 logs triggered alert in the last 1 hour",
        "time_start": "2025-05-12T10:00:00.000Z",
        "time_end": "2025-05-12T11:00:00.000Z",
        "count": 5,
        "related_logs_url": "https://braintrust.dev/app/your-org/p/your-project/logs?search=..."
      }
    }
    ```
  </Tab>

  <Tab title="Environment alerts">
    When an environment alert triggers a webhook, it sends this JSON structure:

    ```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    {
      "organization": {
        "id": "org_123",
        "name": "your-organization"
      },
      "project": {
        "id": "proj_456",
        "name": "your-project"
      },
      "automation": {
        "id": "c5b32408-8568-4bff-9299-8cdd56979b67",
        "name": "Production Environment Changes",
        "description": "Alert when production environment is updated",
        "event_type": "environment_update"
      },
      "details": {
        "environment": {
          "slug": "production"
        },
        "prompt": {
          "id": "prompt_789",
          "slug": "summarizer"
        },
        "new_version": "v3.2.1",
        "action": "update"
      }
    }
    ```

    The `action` field will be either `"update"` (environment assigned to prompt) or `"delete"` (environment removed from prompt). When `action` is `"delete"`, the `new_version` field will be `null`.
  </Tab>
</Tabs>

## Limitations

For hybrid deployments:

* Alerts are available starting with v0.0.72.
* The Slack integration is available starting with v1.1.29.

For Slack workspaces with more than 100,000 channels:

* The channel list shows the most recently active channels. If your target channel doesn't appear, use the manual <Tooltip tip="To find a channel ID in Slack: Right-click the channel name, click &#x22;View channel details&#x22;, and scroll to the bottom and copy the channel ID.">channel ID</Tooltip> entry option.

## Next steps

* [Manage data](/admin/automations/data-management) with export and retention automations
* [View logs](/observe/view-logs) to understand alert triggers
* [Monitor deployments](/deploy/monitor) with dashboards
* [SQL reference](/reference/sql) for advanced filter queries
