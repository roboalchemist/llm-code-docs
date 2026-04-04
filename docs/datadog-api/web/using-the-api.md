# Source: https://docs.datadoghq.com/api/latest/using-the-api

## [Using the API](https://docs.datadoghq.com/api/latest/using-the-api/#using-the-api)
Use the Datadog HTTP API to access the Datadog platform programmatically. You can use the API to send data to Datadog, build data visualizations, and manage your account.
## [Send data to Datadog](https://docs.datadoghq.com/api/latest/using-the-api/#send-data-to-datadog)
Use the API to begin to send integrations data to Datadog. With some additional setup of the Agent, you can also use the API to send Synthetic test data, Logs, and Traces to Datadog.
**Integrations endpoints**
Available integrations endpoints:
  * [AWS Integration](https://docs.datadoghq.com/api/v1/aws-integration/)
  * [AWS Logs Integration](https://docs.datadoghq.com/api/v1/aws-logs-integration/)
  * [Azure Integration](https://docs.datadoghq.com/api/v1/azure-integration/)
  * [Google Cloud Integration](https://docs.datadoghq.com/api/v1/gcp-integration/)
  * [Slack Integration](https://docs.datadoghq.com/api/v1/slack-integration/)
  * [PagerDuty Integration](https://docs.datadoghq.com/api/v1/pagerduty-integration/)
  * [Webhooks Integration](https://docs.datadoghq.com/api/v1/webhooks-integration/)


**Platform endpoints**
Use these endpoints to post and fetch data to and from other parts of the Datadog platform:
  * The [metrics](https://docs.datadoghq.com/api/v1/metrics/) endpoints allow you to post [metrics](https://docs.datadoghq.com/metrics/introduction/) data so it can be graphed on Datadog’s dashboards and query metrics from any time period.
  * The [events](https://docs.datadoghq.com/api/v1/events/) endpoints allow you to post and fetch events to and from the [Datadog event explorer](https://docs.datadoghq.com/events/).
  * Use the [Synthetic Monitoring](https://docs.datadoghq.com/api/v1/synthetics/) endpoints to create, start, stop, and see [Synthetic tests](https://docs.datadoghq.com/synthetics/) results.
  * Use the [Tracing Agent API](https://docs.datadoghq.com/tracing/guide/send_traces_to_agent_by_api/) to send traces to your Datadog Agent, which then forwards them to Datadog.
  * Use the [LLM Observability Export API](https://docs.datadoghq.com/llm_observability/evaluations/export_api) to access your LLM Observability data for running external evaluations and exporting spans for offline storage.


## [Visualize your data](https://docs.datadoghq.com/api/latest/using-the-api/#visualize-your-data)
Once you are sending data to Datadog, you can use the API to build data visualizations programmatically:
  * Build [Dashboards](https://docs.datadoghq.com/api/v1/dashboards/) and view [Dashboard Lists](https://docs.datadoghq.com/api/v1/dashboard-lists/)
  * Manage [host tags](https://docs.datadoghq.com/api/v1/hosts/)
  * Create [Embeddable Graphs](https://docs.datadoghq.com/api/v1/embeddable-graphs/)
  * Take a [graph snapshot](https://docs.datadoghq.com/api/v1/snapshots/)
  * [Service Dependencies](https://docs.datadoghq.com/api/v1/service-dependencies/) - see a list of your APM services and their dependencies
  * Create [Monitors](https://docs.datadoghq.com/api/v1/monitors/)
  * [Service Checks](https://docs.datadoghq.com/api/v1/service-checks/) - post check statuses for use with monitors
  * Create and manage [Logs](https://docs.datadoghq.com/api/v1/logs/), [Logs Indexes](https://docs.datadoghq.com/api/v1/logs-indexes/), and [Logs Pipelines](https://docs.datadoghq.com/api/v1/logs-pipelines/)
  * Get [Host](https://docs.datadoghq.com/api/v1/hosts/) information for your organization
  * Create and manage [Service Level Objectives](https://docs.datadoghq.com/api/v1/service-level-objectives/)
  * Generate [Security Monitoring](https://docs.datadoghq.com/api/v2/security-monitoring/) signals


## [Manage your account](https://docs.datadoghq.com/api/latest/using-the-api/#manage-your-account)
You can also use the Datadog API to manage your account programmatically:
  * Manage [Users](https://docs.datadoghq.com/api/v1/users/)
  * Manage [Roles](https://docs.datadoghq.com/api/v1/roles/)
  * Manage your [Organization](https://docs.datadoghq.com/api/v1/organizations/)
  * Verify API and app keys with the [Authentication](https://docs.datadoghq.com/api/v1/authentication/) endpoint
  * Grant specific logs access with the [Logs Restriction Queries](https://docs.datadoghq.com/api/v2/logs-restriction-queries/)
  * Manage existing keys with [Key Management](https://docs.datadoghq.com/api/v1/key-management/)
  * Get hourly, daily, and monthly usage across multiple facets of Datadog with the [Usage Metering](https://docs.datadoghq.com/api/v1/usage-metering/) endpoints
  * See the list of IP prefixes belonging to Datadog with [IP Ranges](https://docs.datadoghq.com/api/v1/ip-ranges/)


![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c19c9c99-3145-4c4d-a347-126012f6b783&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c9c638e2-049f-4197-9417-fcdc325031a3&pt=Using%20the%20API&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusing-the-api%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261080%26600%264%2624%261080%26600%260%26na&eci=3&event=%7B%7D&event_id=c19c9c99-3145-4c4d-a347-126012f6b783&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=c9c638e2-049f-4197-9417-fcdc325031a3&pt=Using%20the%20API&tw_document_href=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusing-the-api%2F&tw_iframe_status=0&txn_id=nui23&type=javascript&version=2.3.35)![](https://id.rlcdn.com/464526.gif)
![](https://bat.bing.com/action/0?ti=4061438&Ver=2&mid=5ed4359d-7c6a-4fb2-9d64-d962c4adbe73&bo=2&sid=e9375cd0f0bd11f08bcff787fa0fba6f&vid=e9375d80f0bd11f0b5075ff6ae9d9677&vids=0&msclkid=N&pi=918639831&lg=en-US&sw=1080&sh=600&sc=24&tl=Using%20the%20API&p=https%3A%2F%2Fdocs.datadoghq.com%2Fapi%2Flatest%2Fusing-the-api%2F&r=&lt=1339&evt=pageLoad&sv=2&asc=G&cdb=AQAS&rn=861288)
