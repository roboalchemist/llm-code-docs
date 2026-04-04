# Source: https://docs.datadoghq.com/incident_response/incident_management/integrations/servicenow.md

---
title: Integrate ServiceNow with Datadog Incident Management
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Incident Response > Incident Management > Incident Integrations >
  Integrate ServiceNow with Datadog Incident Management
---

# Integrate ServiceNow with Datadog Incident Management

## Overview{% #overview %}

ServiceNow is an IT service management platform that provides solutions for managing digital workflows, IT operations, and business processes. The Datadog ServiceNow integration allows you to create incidents in ServiceNow from Datadog incidents and sync data bidirectionally between the two platforms.

The ServiceNow integration with Datadog Incident Management provides you with the following benefits:

- **Improved Visibility**: Ensure that all stakeholders are immediately informed about incidents, facilitating a quicker response.
- **Bidirectional Sync**: Sync the incident's state, severity (impact and urgency), and any status updates between Datadog and ServiceNow automatically.
- **Supporting Existing Workflows**: Seamlessly integrate with your current processes, making it easier to manage incidents within your established ServiceNow workflows.

## Prerequisites{% #prerequisites %}

To use automatic incident creation and bidirectional sync with ServiceNow:

1. Install the [ServiceNow integration](https://app.datadoghq.com/integrations/servicenow) through the ServiceNow Integration tile and ensure you have the [ServiceNow tile configured](https://docs.datadoghq.com/integrations/servicenow/#configure-the-servicenow-tile-in-datadog) with your ServiceNow instance in Datadog.
1. Install the [ITOM/ITSM Integration for Datadog](https://store.servicenow.com/store/app/e0e963a21b246a50a85b16db234bcb67)(Recommended) from the ServiceNow store, or download the latest Update Set ([Datadog-Snow_Update_Set_v2.7.9.xml](https://docs.datadoghq.com/resources/xml/Datadog-Snow_Update_Set_v2.7.9.xml)) and upload it to your ServiceNow instance manually.
1. Create a [service account application key](https://docs.datadoghq.com/account_management/org_settings/service_accounts/#create-or-revoke-application-keys) in Datadog for secure authentication. **Note**: Datadog recommends creating a service account key instead of using a personal one, which risks breaking the ServiceNow sync if the user's account is deactivated or if their permissions change.

## Setup{% #setup %}

### Configure automatic incident creation{% #configure-automatic-incident-creation %}

1. Navigate to [Integration Settings](https://app.datadoghq.com/incidents/settings#Integrations).
1. In the left menu, click **Integrations**.
1. Find and click the **ServiceNow** integration tile to open the configuration.
1. Click the toggle for **Enable ServiceNow incident creation**.
1. Click the toggle for **Automatically create a ServiceNow incident**.
1. Add a condition to define when to automatically create a ServiceNow incident. If this condition is left blank, the integration creates a ServiceNow incident when Datadog creates an incident.

### Configure bidirectional sync{% #configure-bidirectional-sync %}

In ServiceNow, you can sync state, impact, and urgency bidirectionally with Incident Management.

1. In ServiceNow, click the globe icon in the top-right corner, then make sure the **Application Scope** is set to **ITOM/ITSM Integration for Datadog**.
1. In the top-left navigation menu, click **All**.
1. Type **ITOM/ITSM Integration for Datadog** in the filter.
1. Click the **Configuration** link from the filtered results, then enter the required settings:
   1. Select your **Datadog Data Center**.
   1. Paste in your **Datadog API Key**.
   1. Paste in your **Service Account Application Key** you created.
   1. Check the **Enabled** box.
1. Click **Save**.

With bidirectional sync, when an incident is created in Datadog, a corresponding incident is also created in the linked ServiceNow instance. This ServiceNow incident includes a reference to the Datadog incident and stays in sync based on the defined field mappings.

## Field mappings{% #field-mappings %}

Field mappings define how information in Datadog incidents is transferred to, and synchronized with, fields in ServiceNow incidents. This ensures that key incident details such as status, severity, and descriptions are consistent and up-to-date in both systems.

Below are the default field mappings used in the integration. You can customize mappings within ServiceNow using its [transform map](https://docs.datadoghq.com/integrations/guide/servicenow-itom-itsm-setup/#tranform-maps) mechanism if your workflow requires advanced field configuration.

The following fields are synced between Datadog Incident Management and ServiceNow:

| **Incident Management** | **ServiceNow Cases Table** | **ServiceNow Incident** | **Sync Status**                        |
| ----------------------- | -------------------------- | ----------------------- | -------------------------------------- |
| Title                   | Title - String             | Short Description       | One way sync from Datadog â ServiceNow |
| What Happened           | Description - String       | Description             | One way sync from Datadog â ServiceNow |
| State                   | State - String             | State                   | Bi-directionally synced                |
| DD Incident URL         | Incident URL - String      | Work Notes              | One way sync from Datadog â ServiceNow |
| Severity                | Incident Urgency (int)     | Urgency                 | Bi-directionally synced                |
| Severity                | Incident Impact (int)      | Impact                  | Bi-directionally synced                |

### Incident state mapping{% #incident-state-mapping %}

| **Datadog Monitor State**                      | **ServiceNow Incident State** |
| ---------------------------------------------- | ----------------------------- |
| Active                                         | In Progress                   |
| Warn                                           | In Progress                   |
| OK                                             | Resolved                      |
| Completed *(optional, configured in settings)* | Resolved                      |

### Datadog incident severity to ServiceNow priority mapping{% #datadog-incident-severity-to-servicenow-priority-mapping %}

| **Datadog Incident Severity** | **ServiceNow Urgency** | **ServiceNow Impact** | **ServiceNow Priority** |
| ----------------------------- | ---------------------- | --------------------- | ----------------------- |
| SEV-1                         | 1                      | 1                     | 1 - Critical            |
| SEV-2                         | 1                      | 2                     | 2 - High                |
| SEV-2                         | 2                      | 1                     | 2 - High                |
| SEV-3                         | 1                      | 3                     | 3 - Moderate            |
| SEV-3                         | 2                      | 2                     | 3 - Moderate            |
| SEV-3                         | 3                      | 1                     | 3 - Moderate            |
| SEV-4                         | 2                      | 3                     | 4 - Low                 |
| SEV-4                         | 3                      | 2                     | 4 - Low                 |
| SEV-5 (Minor)                 | 3                      | 3                     | 5 - Planning            |
| Unknown                       | 3                      | 3                     | 5 - Planning            |

**Note**: If `Start at SEV-0` is enabled in Incident Management settings, the values in `ServiceNow Urgency`, `ServiceNow Impact`, and `ServiceNow Priority` all stay the same, but the `Datadog Incident Severity` shifts down by one. For example, in the first row of this table, the `Datadog Incident Severity` would be `0`, but the rest of the values in the rest of the row would stay the same.

## Further Reading{% #further-reading %}

- [Install the ServiceNow Integration](https://docs.datadoghq.com/integrations/servicenow/)
- [Set up ServiceNow ITOM and ITSM](https://docs.datadoghq.com/integrations/guide/servicenow-itom-itsm-setup)
- [In-app ServiceNow integration tile](https://app.datadoghq.com/integrations/servicenow)
