# Source: https://docs.datadoghq.com/security/cloud_security_management/identity_risks.md

---
title: Cloud Security Identity Risks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > Cloud Security > Cloud Security Identity Risks
---

# Cloud Security Identity Risks

Cloud Security Identity Risks is a Cloud Infrastructure Entitlement Management (CIEM) product that helps you mitigate entitlement risks across your clouds. It continually scans your cloud infrastructure and finds issues such as lingering administrative privileges, privilege escalations, permission gaps, large blast radii, and cross-account access. It also enables you to proactively resolve identity risks on an ongoing basis to secure your cloud infrastructure from IAM-based attacks. For quick remediation, it suggests downsized policies, [Datadog Workflows](https://docs.datadoghq.com/security/cloud_security_management/workflows) based remediations, and deep links to cloud consoles.

{% alert level="info" %}
Cloud Security Identity Risks is available for AWS, Azure, and GCP.
{% /alert %}

## Review identity risks{% #review-identity-risks %}

Cloud Security Identity Risk detections include users, roles, groups, policies, EC2 instances, and Lambda functions. Review your organization's active identity risks on the [Identity Risks Findings page](https://app.datadoghq.com/security/identities).

- Use the query search bar or the facet panel to filter for specific types of identity risks.
- Beside **Group by**, group identity risks by **Identity Risks**, **Resources** or **Teams** (or **None** to view identity risks individually), so you can prioritize your remediation efforts accordingly.
- Hover over **Views**, then select an existing view to apply, or click **Save as new view** to use your explorer settings again in the future.
- Select an identity risk to view up to five affected resources, or click **View All** to view all of them. Select a resource to view additional details in a side panel.

{% image
   source="https://datadog-docs.imgix.net/images/security/identity_risks/identity_risks_explorer_6.be7b32360a0c0ce6504b1059af1dd673.png?auto=format"
   alt="Cloud Security Identity Risks Findings page" /%}

## Remediate identity risks{% #remediate-identity-risks %}

For detailed insights and remediation help, click the **Remediation** tab. In the following example, the **Remediation** tab shows the usage of provisioned permissions.

{% image
   source="https://datadog-docs.imgix.net/images/security/identity_risks/side_panel_remediation_tab_1.d8de722ced7b4ee306a2972f9aad83da.png?auto=format"
   alt="The Remediation tab on the identity risks side panel shows the usage of provisioned permissions" /%}

- To remediate the identity risk, you can:

  - Click **Fix in <cloud provider>** to update the resource directly in your cloud provider console.
  - Use [Workflow Automation](https://docs.datadoghq.com/security/cloud_security_management/workflows) to create automated workflows for identity risks (with or without human involvement).
  - For supported Terraform resources:
    - Locate the file and line the identity risk is in and identify the code owners.
    - Generate a pull request in GitHub with code changes that fix the underlying misconfiguration.

- To create a Jira issue and assign it to a team, click **Add Jira issue**. See [Create Jira Issues for Cloud Security Issues](https://docs.datadoghq.com/security/cloud_security_management/guide/jira) for more information.

- To view a suggested downsized policy based on the actual usage, click **View Suggested Policy**. Then, you can click **Edit Policy in <cloud provider>** to apply the suggested changes:

  {% image
     source="https://datadog-docs.imgix.net/images/security/identity_risks/downsized_policy_3.630cc1a489d045b71f905adf068d5e8a.png?auto=format"
     alt="Review suggestions for downsizing a policy on the Suggested downsized policy dialog" /%}

## Gain visibility into at-risk resource access{% #gain-visibility-into-at-risk-resource-access %}

In Misconfigurations, Identity Risks, and the Security Inbox, you can click the **Access Insights** tab to see:

- Which entities the resource can access across your accounts
- Which principals can directly or indirectly access the resource

This example shows all the identities this AWS IAM user can access:

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/access_insights_3.2d9de48e0e54203e2649103cd880bd36.png?auto=format"
   alt="The Access Insights panel, showing a list of AWS IAM users with large permissions gaps" /%}

In the **What can this resource access?** section, you can:

- See the account associated with each entity, and details about the access type
- Search for entities, or filter them by entity type or account
- View a list of excluded policies
- Use the **All**, **Direct Access**, and **Indirect Access** tabs to filter which entities display in the table
- Click the **Actions** dropdown beside an entity to see it in Resource Catalog, or update its configuration in AWS IAM console

In the **Who can access this resource?** section, you can:

- See the risks associated with each principal in the **Risks** column, as well as the type of **Path** the principal can take (direct or indirect) to access the resource
- Filter principals by name, type, public accessibility, or administrative access
- Use the **All**, **Direct Access**, and **Indirect Access** tabs to filter which principals display in the table
- Click the **Actions** dropdown beside a principal to see it in Resource Catalog, or update its configuration in AWS IAM console

## AWS IAM Access Analyzer integration{% #aws-iam-access-analyzer-integration %}

Datadog CIEM integrates with [AWS IAM Access Analyzer](https://docs.datadoghq.com/integrations/iam-access-analyzer/), using Access Analyzer's unused-access findings to recommend downsized policies and enrich permissions-gap detections.

You can also use this integration to extend the time frame beyond Datadog's usual permissions-gap detections, which cover 90 days. You can configure Access Analyzer to analyze more (for example, 180 or 360 days), and view those longer-window findings in Identity Risks.

{% alert level="info" %}
If you are enabling AWS IAM Access Analyzer for the first time:
- There is an additional AWS cost associated with using it.
- It can take up to two hours before AWS IAM Access Analyzer's insights become available in Datadog.

{% /alert %}

## Further reading{% #further-reading %}

- [Learn more about Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/)
- [Setting Up Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup)
- [Find and remediate identity risks with Datadog CIEM](https://www.datadoghq.com/blog/datadog-ciem/)
- [Learn more about the Jira integration](https://docs.datadoghq.com/integrations/jira/)
- [Learn more about Workflow Automation](https://docs.datadoghq.com/service_management/workflows/)
- [Identify and remediate permission gaps in AWS with Datadog CIEM and AWS IAM Access Analyzer](https://www.datadoghq.com/blog/datadog-ciem-aws-iam-access-analyzer/)
- [Detect cross-account access risks in AWS with Datadog](https://www.datadoghq.com/blog/detect-cross-account-risks-aws/)
