# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/jira.md

# Source: https://docs.datadoghq.com/error_tracking/ticketing_systems/jira.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/review_remediate/jira.md

---
title: Create Jira Issues for Cloud Security Issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Review and Remediate > Create Jira
  Issues for Cloud Security Issues
---

# Create Jira Issues for Cloud Security Issues
Available for:
{% icon name="icon-cloud-security-management" /%}
 Cloud Security Misconfigurations | 
{% icon name="icon-cloud-security-management" /%}
 Cloud Security Identity Risks 
Use the [Jira integration](https://docs.datadoghq.com/integrations/jira/) to create Jira issues for resources that are impacted by a Cloud Security security issue. Jira for Cloud Security is available for [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/) and [Cloud Security Identity Risks](https://docs.datadoghq.com/security/cloud_security_management/identity_risks/).

**Notes**:

- To create Jira issues, you must have the `security_monitoring_findings_write` permission. See [Role Based Access Control](https://docs.datadoghq.com/account_management/rbac/permissions/#cloud-security-platform) for more information about Datadog's default roles and granular role-based access control permissions available for Cloud Security.
- At this time, you can create only one Jira issue per finding.

## Configure the Jira integration{% #configure-the-jira-integration %}

To create Jira issues for Cloud Security security issues, you must configure the [Jira integration](https://app.datadoghq.com/integrations/jira?search=jira). For detailed instructions, see the [Jira](https://docs.datadoghq.com/integrations/jira/) integration docs.

## Create a Jira issue for impacted resources{% #create-a-jira-issue-for-impacted-resources %}

{% tab title="Cloud Security Misconfigurations" %}
To create a Jira issue for one or more resources impacted by a misconfiguration:

1. On the [Misconfigurations explorer](https://app.datadoghq.com/security/compliance), select a misconfiguration.
1. Under **Resources Impacted**, select one or more findings.
1. On the **Actions** dropdown menu that appears on top, select **Create Jira Issue**.
1. Choose whether to create a single issue or multiple issues (one issue for each resource).
1. Select a Jira account.
1. Select the Jira project you want to assign the issue to.
1. Select the issue type from the available options. Depending on the issue type, you may be required to enter additional information.
1. Click **Create Issue**.

You can also create a Jira issue from the standalone issue side panel.

1. On the [Misconfigurations explorer](https://app.datadoghq.com/security/compliance), set the Group By filter to **Resources**.
1. Select a resource.
1. On the **Misconfigurations** tab, select a misconfiguration.
1. Click **Create Jira Issue**.
1. Select a Jira account.
1. Select the Jira project you want to assign the issue to.
1. Select the issue type from the available options. Depending on the issue type, you may be required to enter additional information.
1. Click **Create Issue**.

After you create the issue, a link to the Jira issue is displayed on the side panel.
{% /tab %}

{% tab title="Cloud Security Identity Risks" %}
To create a Jira issue for one or more resources impacted by an identity risk:

1. On the [Identity Risks explorer](https://app.datadoghq.com/security/identities), select an identity risk.
1. Under **Resources Impacted**, select one or more findings.
1. On the **Actions** dropdown menu that appears on top, select **Create Jira Issue**.
1. Choose whether to create a single issue or multiple issues (one issue for each resource).
1. Select a Jira account.
1. Select the Jira project you want to assign the issue to.
1. Select the issue type from the available options. Depending on the issue type, you may be required to enter additional information.
1. Click **Create Issue**.

You can also create a Jira issue from the standalone issue side panel.

1. On the [Identity Risks explorer](https://app.datadoghq.com/security/identities), set the Group By filter to **Resources**.
1. Select a resource.
1. On the **Misconfigurations** tab, select an identity risk.
1. Click **Create Jira Issue**.
1. Select a Jira account.
1. Select the Jira project you want to assign the issue to.
1. Select the issue type from the available options. Depending on the issue type, you may be required to enter additional information.
1. Click **Create Issue**.

After you create the issue, a link to the Jira issue is displayed on the side panel.
{% /tab %}

## Further Reading{% #further-reading %}

- [Cloud Security Guides](https://docs.datadoghq.com/security/cloud_security_management/guide)
- [Datadog Jira Integration](https://docs.datadoghq.com/integrations/jira/)
