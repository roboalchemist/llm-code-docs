# Source: https://docs.datadoghq.com/security/sensitive_data_scanner/guide/investigate_sensitive_data_findings.md

---
title: Investigate Sensitive Data Findings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Sensitive Data Scanner > Sensitive Data Scanner
  Guides > Investigate Sensitive Data Findings
---

# Investigate Sensitive Data Findings

## Overview{% #overview %}

Datadog's Sensitive Data Scanner can help prevent sensitive data leaks and limit non-compliance risks by identifying, classifying, and optionally redacting sensitive data. When a sensitive data finding is found, you might have the following questions:

- What sensitive data has been exposed?
- What is the priority of the sensitive data exposure?
- How severe is the finding in terms of spread and volume?
- Where did the sensitive data come from?

The Sensitive Data Scanner's [Findings](https://app.datadoghq.com/sensitive-data-scanner/telemetry) page categorizes and prioritizes sensitive data findings so that you can investigate, collaborate, and document your findings, and answer those questions.

{% image
   source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/findings_20251014.0e5b31c352b7904297ad52541050f41d.png?auto=format"
   alt="The Findings page showing an overview of sensitive findings broken down by priority" /%}

## Triage sensitive data findings{% #triage-sensitive-data-findings %}

Navigate to the [Findings](https://app.datadoghq.com/sensitive-data-scanner/telemetry) page to see all sensitive data findings within the selected time frame and start investigating them.

{% tab title="Telemetry Data" %}
In the **Sensitive Data Rule Findings** tab, you can filter your sensitive data findings by priority status, case status, and domain.

To investigate a finding:

1. Click on the finding in the list.

1. In the finding panel, click **View Recent Changes** to navigate to [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail) and see if there are any recent configuration changes that caused the sensitive data finding.

1. Use the following options to explore different types of data matching the query:

   1. To view all logs related to the query in Log Explorer, click **View All Logs**.
   1. To view all traces matching the query in Trace Explorer, click **View All APM Spans**.
   1. To view all RUM events matching the query, click **View All RUM Events**.
   1. To view all events matching the query, click **View All Events**.

   {% image
      source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/investigate_sensitive_data_issues/findings_panel_20251015.46c1000799ef174a17d4ce4c7437d009.png?auto=format"
      alt="The findings panel showing a critical visa card scanner finding" /%}

1. In the **Blast Radius** section:

   1. View the Top 10 services, hosts, and environments impacted by this sensitive data findings.
   1. Click on a service to see more information about the service in the **Software Catalog**.
   1. Click on a host to see more information about the host in the Infrastructure List page.

   {% image
      source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/investigate_sensitive_data_issues/blast_radius_02_01_2024.43716aefb917a51eff58ee96db87b253.png?auto=format"
      alt="The findings panel showing the top 10 impacted services" /%}

If you want to modify the Scanning Rule that was used to detect the sensitive data finding, click **Modify Rule** at the top of the panel.

Additionally, you can also:

- Use [Case Management](https://docs.datadoghq.com/incident_response/case_management/) to track, triage, and investigate the finding, click **Create Case** at the top of the panel. Associated cases are surfaced in the Findings page.

- Use [Incident Management](https://docs.datadoghq.com/incident_response/incident_management/) to create an incident, you can add the finding to an existing incident or declare a new incident. Click the **Declare Incident** dropdown menu to add the finding to an existing incident. Click **Declare Incident** to declare a new incident.

- Use [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail) to see who may have accessed this sensitive data within Datadog, **View in Audit Trail** in the **Users who accessed these events** section.

  {% image
     source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/investigate_sensitive_data_issues/case_mgmt_02_01_2024.eafc139c2f426e7be94e3ba41764eea3.png?auto=format"
     alt="The case page showing information about the security finding, the assignee and creator of the case, and a timeline of events" /%}

{% /tab %}

{% tab title="Cloud Storage" %}
Click the **Datastores with Sensitive Data** tab to see all sensitive data findings for Cloud Storage.

To investigate a datastore:

1. Click on a datastore.
1. You can view files where sensitive data was found and then click on a file to inspect it in AWS. Datadog recommends doing the following:
   - Review a few files to get a sense of the classification accuracy.
   - Follow up with the team or service owner listed in the side panel to confirm whether sensitive data is meant to be in the bucket.
     - If it is not supposed to be in the bucket, delete the files or move them to an appropriate bucket.

     - If it is supposed to be in the bucket, complete the following steps to improve your security posture:

       1. Click the **Security** tab in the side panel and review the **Misconfigurations** section.
       1. Click on a misconfiguration to see details in Cloud Security.
       1. In the **Next Steps** section:
          1. Under **Triage**, click the dropdown to change the triage status of the signal. The default status is `OPEN`.
          1. Click **Assign Signal** to assign a signal to yourself or another Datadog user.
          1. Click **See remediation** to see more information on how to remediate the finding.
          1. Under **More Actions**, you can add a Jira issue, run workflows, or add a comment. To run a workflow, select **Run Workflow** and then in the workflow browser, search and select a workflow to run. See [Automate Security Workflows with Workflow Automation](https://docs.datadoghq.com/security/cloud_security_management/review_remediate/workflows/) for more information.
       1. Click on the different tabs to see the severity breakdown, related logs, and timeline of the finding.

       {% image
          source="https://datadog-docs.imgix.net/images/sensitive_data_scanner/investigate_sensitive_data_issues/datastore_side_panel.b4fadc853894fadd9a8db1ba071cebb2.png?auto=format"
          alt="The datastore finding side panel showing the S3 buckets should have Block Public Access enabled misconfiguration" /%}

{% /tab %}

## Further Reading{% #further-reading %}

- [Set up Sensitive Data Scanner for Telemetry Data](https://docs.datadoghq.com/sensitive_data_scanner/setup/telemetry_data/)
- [Set up Sensitive Data Scanner for Cloud Storage](https://docs.datadoghq.com/sensitive_data_scanner/setup/cloud_storage/)
- [Discover, triage, and remediate sensitive data issues at scale with Sensitive Data Scanner](https://www.datadoghq.com/blog/scaling-sensitive-data-scanner/)
