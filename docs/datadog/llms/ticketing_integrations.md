# Source: https://docs.datadoghq.com/security/ticketing_integrations.md

---
title: Ticketing Integrations
description: Security ticketing integrations
breadcrumbs: Docs > Datadog Security > Ticketing Integrations
---

# Ticketing Integrations
Available for:
{% icon name="icon-siem" /%}
 Cloud SIEM |
{% icon name="icon-cloud-security-management" /%}
 Workload Protection |
{% icon name="icon-app-sec" /%}
 App and API Protection |
{% icon name="icon-security-code-security" /%}
 Code Security |
{% icon name="icon-cloud-security-management" /%}
 Cloud Security
You can use [Datadog Case Management](https://docs.datadoghq.com/incident_response/case_management/) to manage tickets in third-party tools like [Jira](https://docs.datadoghq.com/integrations/jira/). For details, see [Case Management integration with third-party ticketing tools](https://docs.datadoghq.com/incident_response//case_management/notifications_integrations/#third-party-tickets).

This page discusses using Datadog Security with Datadog Case Management for ticketing management.

## Case management and security products{% #case-management-and-security-products %}

Case Management is supported for all security products that use signals or findings:

- Code Security (in [Findings](https://app.datadoghq.com/security/code-security))
- Cloud Security (in [Findings](https://app.datadoghq.com/security/compliance))
- Cloud SIEM (in [Signals](https://app.datadoghq.com/security/siem/signals))
- App and API Protection (in [Signals](https://app.datadoghq.com/security/appsec/signals) and [Findings](https://app.datadoghq.com/security/appsec/inventory/finding))
- Workload Protection (in [Signals](https://app.datadoghq.com/security/workload-protection/signals) and [Findings](https://app.datadoghq.com/security/workload-protection/findings))

Open any signal or finding in these products or do a bulk selection of findings in the explorers, and use the **Create Ticket** button to create a case in Datadog.

## Bidirectional ticket syncing with Jira{% #bidirectional-ticket-syncing-with-jira %}

Bidirectional syncing enables you to update Jira tickets automatically when changes occur in Datadog, and update some Datadog information when changes occur in Jira.

### Supported products{% #supported-products %}

Bidirectional syncing is supported for the following Code and Cloud Security finding categories:

- Libraries (SCA)
- Static Code (SAST)
- Runtime Code (IAST)
- Secret Scanning (SDS)
- Infrastructure as Code (IaC)
- Misconfigurations
- Identity Risks
- Host and Container Vulnerabilities
- App and API Protection
- Workload Protection

### Single source of truth{% #single-source-of-truth %}

Bidirectional syncing with Jira enables you to sync Jira tickets with Datadog cases. However, Datadog is the single source of truth for issue detection and resolution.

A Datadog finding's related Jira ticket can be closed manually. However, the Datadog finding remains open if Datadog cannot confirm that the issue is fixed. This restriction ensures that a finding is not closed and removed when someone closes a related Jira ticket.

Closing a Datadog case without remediation does not close the finding either.

Remediation of the finding in Datadog or defining an exception by [muting the finding](https://app.datadoghq.com/security/automation_pipelines/mute) are the only ways to close a finding. After the finding is remediated, its related cases and Jira tickets are closed.

### Set up bidirectional syncing{% #set-up-bidirectional-syncing %}

The following steps set up bidirectional syncing with Jira and verify that setup is successful.

1. Set up the following prerequisites in your Datadog account, or verify that they are set up already. The prerequisites are listed in their setup order.
   1. The [Datadog Jira integration](https://docs.datadoghq.com/integrations/jira/).
   1. A [webhook for the Jira integration](https://docs.datadoghq.com/integrations/jira/#configure-a-jira-webhook). Configuring a webhook enables cases created in Case Management to automatically create issues in Jira and keep both resources synced.
   1. A [new Case Management project](https://docs.datadoghq.com/incident_response/case_management/projects/). A project is a container object that holds a set of cases.
   1. The [Jira integration is configured within the project](https://docs.datadoghq.com/incident_response//case_management/notifications_integrations/#third-party-tickets).
      1. Enable the **Sync data between Case Management and Jira** option.
      1. In **Title**, select **Two-way sync**.
      1. Complete the remaining settings, and then click **Save changes**.
1. Verify that bidirectional Case Management integration with Jira is working:
   1. Open [any product supporting bidirectional ticket syncing](https://docs.datadoghq.com/security/ticketing_integrations/#supported-products).
   1. Open any Security finding.
   1. Locate the **Create Ticket** option. The option is available in **Next Steps** or **Repositories** (in **Libraries (SCA)**). The button opens a **Create Ticket** modal.
   1. Click the **Jira** tab.
   1. Verify that the **Case Management <-> Jira Integration** section exists and bidirectional sync is enabled.

{% image
   source="https://datadog-docs.imgix.net/images/security/jira_modal.941118c7581720cb43eab3946416123f.png?auto=format"
   alt="Modal used to create a Jira ticket for a Security finding, with bidirectional sync enabled." /%}

You are ready to start creating bidirectional Case Management tickets.

If you do not see the **Case Management <-> Jira Integration** section, ensure that you have completed the prerequisites.

### Create bidirectional tickets{% #create-bidirectional-tickets %}

The following steps create a bidirectional ticket for a Security finding.

1. Open [any product supporting bidirectional ticket syncing](https://docs.datadoghq.com/security/ticketing_integrations/#supported-products).
1. Open any Security finding.
1. Locate the **Create Ticket** option. The option is available in **Next Steps** or **Repositories** (in **Libraries (SCA)**). The button opens a **Create Ticket** modal.
1. Create ticket for any third-party tool supported (see sections below)

{% collapsible-section %}
#### Jira ticket

1. Click the **Jira** tab. You can use a new or existing ticket. Let's look at creating a new Jira ticket.
1. In **Case Management <-> Jira Integration**, complete the following settings:
   1. **Case Management project:** select a Case Management project that has [Jira integration enabled](https://docs.datadoghq.com/incident_response//case_management/notifications_integrations/#third-party-tickets).
   1. **Jira account:** select the Jira account where you want the ticket created.
   1. **Project:** select the Jira project to use.
   1. **Issue type:** select the Jira issue type to create.
1. To add more fields to the Jira ticket Datadog creates, use **Add Optional Field** to add the fields.
1. Click **Create Ticket**.

Notes:

- Bidirectional sync with Jira is available for certain Jira ticket attributes, such as status, assignee, and comments, but not all Jira fields are available.

{% /collapsible-section %}

### Manage bidirectional Case Management tickets{% #manage-bidirectional-case-management-tickets %}

Existing bidirectional Jira tickets are listed in the finding's **Ticketing** or **Next Steps** sections.

Here's an example from a Static Code (SAST) finding:

{% image
   source="https://datadog-docs.imgix.net/images/security/bidir-jira-existing.c5339001c41b05c0102d6bd284fef96a.png?auto=format"
   alt="finding with existing Jira ticket: in the Next Steps section, under Ticket Created, a pill with the Jira logo and text 'CJT-16'" /%}

Hover over the Jira ticket to see its details.

{% image
   source="https://datadog-docs.imgix.net/images/security/bidir-jira-existing-hover.cb7d74014b30c5480b6215bfc93d64a0.png?auto=format"
   alt="Mouseover state for pill in previous image. Modal with Jira ticket details." /%}

Details such as assignee and status are provided along with a timeline of the Jira issue and Datadog case changes.

Closed Jira tickets are green.

In **Datadog Associated Case**, the related Datadog case is provided. Click the case name to open it in [Case Management](https://docs.datadoghq.com/incident_response/case_management/).

#### Automatic detachment and ticket opening/closing{% #automatic-detachment-and-ticket-openingclosing %}

Archiving a case does not delete related Jira tickets, but deleting a case project detaches all tickets from related Security findings.

Detaching a ticket from a Security finding does not delete it.

If there are no open findings left attached to a ticket (because they are all detached or resolved or muted), it is automatically closed. Similarly, if at least one open finding is attached to a closed ticket (because it was attached or detected again or unmuted), it is automatically reopened.

### Bidirectional Case Management facets{% #bidirectional-case-management-facets %}

There are several case management facets under **Triage**, including:

- Case Key
- Jira Key
- Case Status
- Has ticket attached

You can query attributes and create dashboards using these facets.

## Ticketing integration API{% #ticketing-integration-api %}

The link between Datadog Cases and existing Security findings can be managed with the public API.

Dedicated endpoints allow users to [create Datadog case for existing security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#create-cases-for-security-findings), [attach security findings to an existing Datadog case](https://docs.datadoghq.com/api/latest/security-monitoring/#attach-security-findings-to-a-case), and [detach security findings from their case](https://docs.datadoghq.com/api/latest/security-monitoring/#detach-security-findings-from-their-case).

Users can also [create Jira issues for security findings](https://docs.datadoghq.com/api/latest/security-monitoring/#create-jira-issues-for-security-findings) and [attach security findings to a Jira issue](https://docs.datadoghq.com/api/latest/security-monitoring/#attach-security-findings-to-a-jira-issue).
