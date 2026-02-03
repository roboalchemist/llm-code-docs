# Source: https://docs.datadoghq.com/security/cloud_security_management/review_remediate/mute_issues.md

---
title: Mute Issues in Cloud Security
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Review and Remediate > Mute Issues
  in Cloud Security
---

# Mute Issues in Cloud Security
Available for:
{% icon name="icon-cloud-security-management" /%}
 Cloud Security Misconfigurations | 
{% icon name="icon-cloud-security-management" /%}
 Cloud Security Identity Risks 
There may be times when a misconfiguration, issue, or identity risk doesn't match the use case for your business, or you choose to accept it as a known risk. To ignore them, you can mute the underlying misconfiguration, issue, or identity risk for the impacted resources.

For example, the Cloud Security Misconfigurations rule [S3 buckets should have 'Block Public Access' enabled](https://docs.datadoghq.com/security/default_rules/hkp-p6b-f7w/) evaluates whether an S3 bucket is publicly accessible. If you have an S3 bucket with static assets that are meant to be publicly shared, you can mute the misconfiguration for the S3 bucket.

**Note**: Muting a misconfiguration removes it from the calculation of your posture score.

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/mute_issue-3.814ba185372296ac819d3281e213f446.png?auto=format"
   alt="The Mute Issue dialog box contains fields for specifying the reason and duration of the mute" /%}

1. Find the triage status dropdown for the resource.
   - In the misconfiguration, identity risk, or vulnerability explorers, the dropdown is in the **Triage** column for each resource. Alternatively, you can select one or more resources, then click the **Set State** dropdown that appears, so you can mute your entire selection at once.
   - When you're viewing a resource in a side panel, under **Next Steps**, the dropdown is under **Triage**.
1. Open the dropdown with the current triage status and click **Muted**. The **Mute issue** window opens.
1. Select a reason for the mute; for example, it's a false positive, it's an accepted risk, or a fix is pending.
1. Enter an optional **Description**.
1. Select the duration of the mute.
1. Click **Mute**. The **Mute issue** window closes.

To automatically mute issues that meet certain criteria, see [Mute Rules](https://docs.datadoghq.com/security/automation_pipelines/mute).

## Unmute an issue{% #unmute-an-issue %}

Muted issues automatically unmute after the specified mute duration expires. You can also manually unmute an issue.

1. Find the triage status dropdown for the resource.
   - In the misconfiguration, identity risk, or vulnerability explorers, the dropdown is in the **Triage** column for each resource. Alternatively, you can select one or more resources, then click the **Set State** dropdown that appears, so you can unmute your entire selection at once.
   - When you're viewing a resource in a side panel, under **Next Steps**, the dropdown is under **Triage**.
1. Click **Muted** to open the dropdown, then select a new triage status. The triage status updates immediately for the selected resources.

## Audit your muted issues{% #audit-your-muted-issues %}

To view your organization's muted issues:

1. By default, all issue explorers hide muted issues. To view muted issues on the Misconfigurations and Identity Risks issue explorers, remove the `@workflow.triage.status:(open OR in-progress)` filter from the search bar.
1. Depending on the issue explorer you're using, sort or filter the issues:
   - On the Misconfigurations issue explorer, sort by the **Muted** column.
   - On the Misconfigurations or Identity Risks issue explorers, filter issues using the **Muted** facet.
   - On the Vulnerabilities issue explorer, click the **Muted** tab.

To audit the mute history for a misconfiguration:

1. Open the misconfiguration side panel.
1. Select the resource with the muted misconfiguration.
1. Click the **Timeline** tab to view a chronological history of the misconfiguration. Hover over a mute or unmute action to view additional details, such as the reason for the mute, how long the mute is intended to last, and who muted it.

{% image
   source="https://datadog-docs.imgix.net/images/security/csm/muted_finding_timeline-2.1f6241404ab5b351e33276cf9e65fe32.png?auto=format"
   alt="The Timeline tab shows a chronological history of the misconfiguration, including details on when a misconfiguration was muted" /%}

## Further reading{% #further-reading %}

- [Explore out-of-the-box security detection rules](https://docs.datadoghq.com/security/default_rules)
