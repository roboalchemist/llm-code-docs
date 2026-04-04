# Source: https://docs.datadoghq.com/security/cloud_siem/triage_and_investigate/investigate_security_signals.md

---
title: Investigate Security Signals
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud SIEM > Triage and Investigate > Investigate
  Security Signals
---

# Investigate Security Signals

## Overview{% #overview %}

A Cloud SIEM security signal is created when Datadog detects a threat while analyzing logs against detection rules. View, search, filter, and correlate security signals in the Signals Explorer without needing to learn a dedicated query language. You can also assign security signals to yourself or another user in the Datadog platform. In addition to the Signals Explorer, you can configure [Notification Rules](https://docs.datadoghq.com/security/notifications/rules/) to send signals to specific individuals or teams to keep them informed of issues.

You must have the `Security Signals Write` permission to modify a security signal, such as change the state and view signal action history in [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/events/#cloud-security-platform-events). See [Role Based Access Control](https://docs.datadoghq.com/account_management/rbac/) for more information about Datadog's default roles and granular role-based access control permissions available for Datadog Security in the Cloud Security.

## Signals explorer{% #signals-explorer %}

In the Signals Explorer, use the facet panel or search bar to group and filter your signals. For example, you can view signals by their severity, detection rules, and MITRE ATT&CK. After you have filtered your signals to your use case, create a [saved view](https://docs.datadoghq.com/logs/explorer/saved_views/) so that you can reload your query later.

### View signals by severity{% #view-signals-by-severity %}

To view all signals with specific severities, for example `HIGH` and `CRITICAL`, that are in the `open` or `under review` triage state, do one of the following:

- In the facet panel's **Severity** section, select **Critical**, **High**, and **Medium**. In the **Signal State** section, make sure only **open** and **under\_reviewed** are selected.
- In the search bar, enter `status:(high OR critical OR medium) @workflow.triage.state:(open OR under_review)`.

To add the column **Signal State**, select the **Options** button in the top right corner above the table and add the facet: `@workflow.triage.state`. This displays the signal status and allows you to sort by status through the header.

Use different visualizations to investigate the threat activity in your environment. For example, in the **Visualize by** field, you can group signals by:

- **Rules List** to see the volume and alerting trends across the different detection rules.
- **Timeseries** to view signal trends over time.
- **Top List** to see signals with the highest to lowest number of occurrences.
- **Table** to see signals by the specified tag key (for example, `source`, `technique`, and so on).
- **Pie Chart** to see the relative volume of each of the detection rules.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/signal_list2.f96e49f94534e574e80647368c4bc4fe.png?auto=format"
   alt="The Signals Explorer showing signals categorized by detection rules" /%}

### View signals by detection rules{% #view-signals-by-detection-rules %}

To view your signals based on detections rules, click **Rules List** in the **Visualize as** field under the search bar. Click on a rule to see the signals related to that rule. Click on a signal to see the signal details.

### View signals by MITRE ATT&CK{% #view-signals-by-mitre-attck %}

To view your signals by MITRE ATT&CK Tactic and Technique:

1. Select **Table** in the **Visualize as** field under the search bar, and group by **Tactic**.
1. Click the plus icon next to the first group `by` to add a second group `by`, and select **Technique** for it.
1. In the table, click one of the tactics or techniques to see options to further investigate and filter the signals. For example, you can view signals related to the tactic and technique and search for or exclude specific tactics and techniques.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/tactics_techniques.5633af613252fa21a1ad0e652bc8f0ea.png?auto=format"
   alt="The Signals Explorer table showing a list of tactics and techniques" /%}

### Triage a single signal{% #triage-a-single-signal %}

1. In Datadog, go to **Security** > **Cloud SIEM** > [**Signals**](https://app.datadoghq.com/security/siem/signals).
1. Click on a security signal from the table.
1. In the **What Happened** section, see the logs that matched the query. Hover over the query to see the query details.
   - You can also see specific information like username or network IP. In **Rule Details**, click the funnel icon to create a suppression rule or add the information to an existing suppression. See [Create suppression rule](https://docs.datadoghq.com/security/suppressions/#create-a-suppression-rule) for more details.
1. In the **Next Steps** section:
   1. Under **Triage**, click the dropdown to change the triage status of the signal. The default status is `OPEN`.
      - `Open`: Datadog Security triggered a detection based on a rule, and the resulting signal is not yet resolved.
      - `Under Review`: During an active investigation, change the triage status to `Under Review`. From the `Under Review` state, you can move the status to `Archived` or `Open` as needed.
      - `Archived`: When the detection that caused the signal has been resolved, update the status to `Archived`. When a signal is archived, you can give a reason and description for future reference. If an archived issue resurfaces, or if further investigation is necessary, the status can be changed back to `Open`. All signals are locked 30 days after they have been created.
1. Click **Assign Signal** to assign a signal to yourself or another Datadog user.
1. Under **Take Action**, you can create a case, declare an incident, edit suppressions, or run workflows. Creating a case automatically sets the triage status to `Under Review`. For more information on associating cases with signals, see Case Management.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/signal_side_panel.0ce8f9e3771f5f63728040b5d41764aa.png?auto=format"
   alt="The signal side panel of a compromised AWS IAM user access key showing two IP addresses and their locations" /%}

### Triage multiple signals{% #triage-multiple-signals %}

Use bulk actions to triage multiple signals. To use bulk actions, first search and filter your signals in the Signals Explorer, then:

1. Click on the checkbox to the left of the signals that you want to take a bulk action on. To select all signals in the Signals Explorer list, select the checkbox next to the **Status** column header.
1. Click on the **Bulk Actions** dropdown menu above the signals table and select the action you want to take.

**Note**: The Signals Explorer stops dynamically updating when performing a bulk action.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/bulk_actions2.3156833f0e7013f839b20824b416f022.png?auto=format"
   alt="The Signals Explorer showing the bulk action option" /%}

### Run Workflow Automation{% #run-workflow-automation %}

Use Workflow Automation to carry out actions to help you investigate and remediate a signal. These actions can include:

- Block an IP address from your environment.
- Disable a user account.
- Look up an IP address with a third-party threat intelligence provider.
- Send Slack messages to your colleagues to get help with your investigation.

Click the **Workflows** tab in the signal side panel to see which workflows were triggered for the signal and suggested Workflows to run. If you want to run a suggested Workflow, click **Run Workflow**. See How suggested Workflows are selected for more information. If the workflow requires additional input variables, a dialog box appears and prompts you to enter any required values before proceeding.

If you don't see the Workflow you want to run in the list, click **Search and Run Workflow**. In the workflow browser, search and select a workflow to run.

Alternatively, you can also select **Run Workflows** in the **Next Steps** section to search for and run a Workflow.

To trigger a workflow automatically for any security signal, see [Trigger a Workflow from a Security Signal](https://docs.datadoghq.com/service_management/workflows/trigger/#trigger-a-workflow-from-a-security-signal) and [Automate Security Workflows with Workflow Automation](https://docs.datadoghq.com/security/cloud_security_management/workflows/) for more information.

#### How suggested Workflows are selected{% #how-suggested-workflows-are-selected %}

To streamline incident response and reduce friction during triage, Cloud SIEM suggests Workflows that are relevant to the signal. The suggested Workflows are selected based on which ones have the highest tag similarity with the signal. Cloud SIEM uses the following information to suggest Workflows for a signal:

- **Tags automatically added from Blueprints, which are preconfigured flows**Workflows are a set of actions that are relevant to the platform, such as AWS CloudTrail. Workflows created from a Blueprint automatically have tags applied based on the source. For example, a workflow action such as "Shutdown virtual machine on AWS" has the `source` tag AWS CloudTrail.
- **Tags you added manually**You can customize which workflows are prioritized by manually adding tags to both Blueprint-derived and custom workflows.To ensure correct contextual matching, these tags should match those found on the signal, the logs that generated the alert, or the detection rule itself.
- **Tagging strategy**To ensure a workflow appears for a given signal, the workflow must include tags similar to those of the signal. A common signal tag is the signal's source or service. For example, signals from AWS resources are typically tagged with `source:cloudtrail`. By tagging a workflow with `source:cloudtrail`, the workflow is associated with signals related to AWS activity.If you want a Workflow to be suggested for a specific detection rule, tag the Workflow with that detection rule ID (for example, `ruleId:abc-123-xyz`).

When a signal is created:

- **Signals and workflows are matched using tags**When a security signal is created, Cloud SIEM checks the signal's tags, and matches them against tags defined in your existing workflows.
- **Relevant suggestions are made**A **Suggested Workflows** section appears in the side panel. It shows the top three workflows based on tags that match closest to the tags on the signal. This ensures that suggested actions are context-aware and operationally relevant.

## Investigate{% #investigate %}

A signal contains important information to determine whether the threat detected is malicious. Additionally, you can add a signal to a case in Case Management for further investigation.

### Logs{% #logs %}

Click the **Logs** tab to view the logs related to the signal. Click **View All Related Logs** to see the related logs in Log Explorer.

### Entities{% #entities %}

To investigate entities:

1. Click the **Entities** tab to see entities related to the signal, such as users or IP addresses.
1. Click the down arrow next to **View Related Logs** and:
   - Select **View IP Dashboard** to see more information about the IP address in the IP Investigation dashboard.
   - Select **View Related Signals** to open Signals Explorer and see the other signals associated with the IP address.
1. For cloud environment entities, such as an assumed role or IAM user, view the activity graph to see what other actions the user took. Click **View in Investigator** to go to the Investigator to see more details.

### Related signals{% #related-signals %}

Click the **Related Signals** tab to see the related signals and information, such as fields and attributes, that the signals share. Click **View All Related Activity** to see the signals in the Signals Explorer.

### Suppressions{% #suppressions %}

To view the suppression rules for the detection rule that generated the signal, do one of the following:

- In the **What Happened** section, hover your mouse over the funnel icon, then click **Add Suppression**.
- In the **Next Steps** section, click **Edit Suppressions** to see the suppression section of that rule in the detection rule editor.
- Click the **Suppressions** tab to see a list of suppressions, if there are any. Click **Edit Suppressions** to go to the detection rule editor to see the suppression section of that rule.

## Collaborate{% #collaborate %}

### Case Management{% #case-management %}

Sometimes you need more information than what is available in a single signal to investigate the signal. Use [Case Management](https://docs.datadoghq.com/incident_response/case_management/) to collect multiple signals, create timelines, discuss with colleagues, and keep a notebook of the analysis and findings.

#### Create and manage cases from the Signals Explorer{% #create-and-manage-cases-from-the-signals-explorer %}

In the [Signals Explorer](https://app.datadoghq.com/security/siem/signals), when you use the **List** visualization, the **Cases** column contains information about cases associated with signals. You can use that column to manage those cases:

- To manage cases for a single signal, use the **Cases** column:
  - If the signal has cases associated with it, you can roll over the case ID to view information about them, open them in a new window, or unlink them from the signal.
  - If the signal doesn't have any cases associated with it, click the **Create Case** icon to either create a case or select an existing case to associate with the signal. The Create Case window opens.
    - To create a case, in the **Create Case** window, enter the **Project**, **Title**, **Description**, and **Assignee**, then click **Create Case**.
    - To select an existing case, in the **Create Case** window, click the **Add to Existing Case** tab. Select a case and click **Attach to an Existing Case**.
- To manage cases for multiple signals:
  1. Select the signals you want to link to a case.
  1. In the **Bulk Actions** list that appears, click **Create a Case** or **Add to Existing Case**. The Create Case window opens.
     - To create a case, in the **Create Case** window, enter the **Project**, **Title**, **Description**, and **Assignee**, then click **Create Case**.
     - To select an existing case, in the **Create Case** window, click the **Add to Existing Case** tab. Select a case and click **Attach to an Existing Case**.

When you create a case, the triage status is automatically set to `Under Review`.

**Note**: If a case is determined to be critical after further investigation, click **Declare Incident** in the case to escalate it to an incident.

#### Manage security-related cases{% #manage-security-related-cases %}

The [Cases](https://app.datadoghq.com/security/siem/cases) page allows you to view cases specifically for your security projects. You can filter cases so you only see the ones that are assigned to or created by you, or cases that have a specific status or are in a specific project. You can also star projects to make them easier to navigate to.

In the **Security Signals** section for a case, you can view signals associated with it, and click **Add Signals** to search for filters to associate with the case.

### Declare an incident{% #declare-an-incident %}

Whether it is based on a single signal or after an investigation of a case, certain malicious activity demands a response. You can declare incidents in Datadog to bring together developers, operations, and security teams to address a critical security event. [Incident Management](https://docs.datadoghq.com/incident_response/incident_management/) provides a framework and workflow to help teams effectively identify and mitigate incidents.

To declare an incident in the signal panel:

1. Click **Declare Incident** in the **Next Steps** section.
1. Fill out the incident template.

If you want to add the signal to an incident, click the down arrow next to **Declare Incident** and select the incident you want to add the signal to. Click **Confirm**.

### Threat intelligence{% #threat-intelligence %}

Datadog Cloud SIEM offers integrated threat intelligence provided by our threat intelligence partners. These feeds are constantly updated to include data about known suspicious activity (for example, IP addresses known to be used by malicious actors), so that you can quickly identify which potential threats to address.

Datadog automatically enriches all ingested logs for indicators of compromise (IOCs) from its threat intelligence feeds. If a log contains a match to a known IOC, a `threat_intel` attribute is appended to the log event to provide additional insights based on available intelligence.

The query to see all threat intelligence matches in the Security Signals Explorer is `@threat_intel.indicators_matched:*`. The following are additional attributes to query for threat intelligence:

- For `@threat_intel.results.category`: attack, corp_vpn, cryptomining, malware, residential_proxy, tor, scanner
- For `@threat_intel.results.intention`: malicious, suspicious, benign, unknown

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/threat_intel_results_categories.704cc653026a6d8a222615c498fab3e6.png?auto=format"
   alt="The Signals Explorer showing a bar graph of signals broken down by the threat intel categories of residential proxy, corp_vpn, cryptomining, and malware" /%}

See the [Threat Intelligence](https://docs.datadoghq.com/security/threat_intelligence) documentation for more information on threat intelligence feeds.

### Search by network IP attributes{% #search-by-network-ip-attributes %}

When a suspicious activity is detected from your logs, determine whether the suspicious actor has interacted with your systems by searching for its network IP. Use the following query to search by IP attributes in the Log Explorer: `@network.ip.list:<IP address>`. The query searches IPs anywhere within the logs, including the tags, attributes, error, and message fields.

You can also launch this query directly from the signal panel:

1. Click on the IP address in the **IPS** section.
1. Select **View Logs with @network.client.ip:<ip\_address>**.

{% image
   source="https://datadog-docs.imgix.net/images/security/security_monitoring/investigate_security_signals/search_logs_by_ip.eee90a6b7bf9c6327ab97eebb111e826.png?auto=format"
   alt="The signal panel showing the threat options for the selected IP address" /%}

## Further reading{% #further-reading %}

- [Learn about the conditional logic of detection rules](https://docs.datadoghq.com/cloud_siem/detection_rules/)
- [Monitor 1Password with Datadog Cloud SIEM](https://www.datadoghq.com/blog/monitor-1password-datadog-cloud-siem/)
