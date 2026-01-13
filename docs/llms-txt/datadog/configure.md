# Source: https://docs.datadoghq.com/cloudprem/configure.md

# Source: https://docs.datadoghq.com/bits_ai/bits_ai_sre/configure.md

---
title: Configure integrations and settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Bits AI > Bits AI SRE > Configure integrations and settings
source_url: https://docs.datadoghq.com/bits_ai_sre/configure/index.html
---

# Configure integrations and settings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com, ap2.datadoghq.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Configure where Bits sends investigation findings{% #configure-where-bits-sends-investigation-findings %}

By default, all investigations are listed on the [Bits AI Investigations](https://app.datadoghq.com/bits-ai/investigations) page.

For monitor alert investigations, a summary of the findings is available on the monitor's status page. If your monitor already has `@slack`, `@case`, or `@oncall` [notifications](https://docs.datadoghq.com/monitors/notify) configured, Bits automatically posts its findings to those destinations. If not, you can set up those integrations using the instructions below.

### Slack{% #slack %}

1. Ensure the [Datadog Slack app](https://docs.datadoghq.com/integrations/slack/?tab=datadogforslack) is installed in your Slack workspace.
1. In your monitor, go to **Configure notifications and automations** and add the `@slack-{channel-name}` handle. This sends monitor notifications to your chosen Slack channel.
1. Lastly, go to [**Bits AI SRE** > **Settings** > **Integrations**](https://app.datadoghq.com/bits-ai/settings/integrations) and connect your Slack workspace. This allows Bits to write its findings directly under the monitor notification in Slack.Important alert (level: info): Each Slack workspace can only be connected to one Datadog organization.

### Datadog Case Management{% #datadog-case-management %}

Datadog Case Management provides a centralized workspace for triaging, tracking, and remediating issues detected by Datadog and third-party integrations. Bits AI SRE automatically delivers its investigation findings to Jira and ServiceNow through Case Management.

To set up Case Management, and the Jira and ServiceNow integrations:

1. Create a [Case Management project](https://docs.datadoghq.com/incident_response/case_management/projects) for your team.
1. In Datadog, go to [**Case Management** > **Settings**](https://app.datadoghq.com/cases/settings). In the list of projects, expand your project, go to **Integrations** > **Datadog Monitors**, and turn on the **Enable Datadog Monitors integration for this project** toggle. This generates your project's unique handle: `@case-{project_name}`.
1. On the same page, under **Integrations**, set up the Case Management Jira and/or ServiceNow integrations. When a new case is created, Case Management can automatically open the corresponding Jira ticket or ServiceNow incident.
1. In your monitor, go to **Configure notifications and automations** and add the `@case-{project_name}` handle. When the monitor triggers:
   - Datadog automatically creates a new case
   - The case creates a linked Jira ticket or ServiceNow incident
   - Bits writes its investigation findings directly to the case, which gets appended to Jira as a timeline comment or ServiceNow as a work note

### Datadog On-Call{% #datadog-on-call %}

Datadog On-Call is a paging solution that unifies monitoring, paging, and incident response in a single platform.

To set up On-Call, in your monitor, go to **Configure notifications and automations** and add the `@oncall-{team}` handle. Bits' findings can then appear on the On-Call page in the Datadog mobile app, helping your teams triage issues on the go.

## Configure knowledge base integrations{% #configure-knowledge-base-integrations %}

Bits AI SRE integrates with Confluence to:

- Find relevant documentation and runbooks to support its monitor alert investigations
- Let you interact with your Confluence content directly through chat

To set up Bits AI SRE to use Confluence:

1. Connect your Confluence Cloud account by following the instructions in the [Confluence integration tile](https://app.datadoghq.com/integrations/confluence).
1. Optionally, enable account crawling to make Confluence a data source within Bits' chat interface. If you don't enable account crawling, Bits can still use Confluence to inform its investigation plan.
1. Add a link to a Confluence page in your monitor's message. Bits reads the page to extract Datadog telemetry links and other context when forming its investigation plan.
1. You can view all connected Confluence accounts on the [Bits Settings page](https://app.datadoghq.com/bits-ai/settings/integrations).

### Best practices: Optimize Bits' understanding of your knowledge{% #best-practices-optimize-bits-understanding-of-your-knowledge %}

Help Bits interpret and act on your documentation by following these best practices:

- Include relevant Datadog telemetry links in your Confluence pages. Bits queries these links to extract information for its investigation.
- Provide clear, step-by-step instructions for resolving monitor issues. Bits follows these instructions precisely, so being specific leads to more accurate outcomes.
- Document the services or systems involved in detail. Bits uses this information to understand the environment and guide investigations effectively.
The more precisely your Confluence page matches the issue at hand, the more helpful Bits can be.
## Configure permissions{% #configure-permissions %}

There are two RBAC permissions that apply to Bits AI SRE:

| Name                                                    | Description                            | Default role           |
| ------------------------------------------------------- | -------------------------------------- | ---------------------- |
| Bits Investigations Read (`bits_investigations_read`)   | Read Bits investigations.              | Datadog Read Only Role |
| Bits Investigations Write (`bits_investigations_write`) | Run and configure Bits investigations. | Datadog Standard Role  |

These permissions are added by default to Managed Roles. If your organization uses Custom Roles or has previously modified the default roles, an admin with the User Access Manage permission needs to manually add these permissions to the appropriate roles. For details, see [Access Control](https://docs.datadoghq.com/account_management/rbac).

## Configure rate limits{% #configure-rate-limits %}

Rate limits define the maximum number of automatic investigations Bits AI SRE can run in a rolling 24-hour period. After you reach a rate limit, you can continue to trigger [manual investigations](https://docs.datadoghq.com/bits_ai/bits_ai_sre/investigate_issues#manually-start-an-investigation).

### Types of rate limits{% #types-of-rate-limits %}

{% dl %}

{% dt %}
Per monitor limit
{% /dt %}

{% dd %}
Controls how often investigations are automatically triggered from a single monitor within a rolling 24-hour window.
{% /dd %}

{% dd %}
**Default:** Each monitor can trigger one automatic investigation per 24 hours.
{% /dd %}

{% dt %}
Organization limit
{% /dt %}

{% dd %}
Defines the total number of automatic investigations Bits AI SRE can run across your entire organization within 24 hours.
{% /dd %}

{% dd %}
**Default:** No limit.
{% /dd %}

{% /dl %}

### Set a rate limit{% #set-a-rate-limit %}

To set a rate limit:

1. Navigate to [**Bits AI SRE** > **Settings** > **Rate Limits**](https://app.datadoghq.com/bits-ai/settings/rate-limits).
1. Toggle on the rate limit you want to enable.
1. Set the maximum number of investigations you want to run within a rolling 24-hour window.
1. Click **Save**.

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/rate_limits.b0f49dcfec1cf740f07180291e3079fe.png?auto=format"
   alt="Options to set a rate limit" /%}

## Audit Trail{% #audit-trail %}

You can monitor user-initiated actions with [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/events/#bits-ai-sre). Events are sent when:

- A user manually starts an investigation and when the investigation completes
- A tool call is executed in a manual investigation
- A user enables or disables automatic investigations for a monitor
- A user modifies the monitor rate limit
