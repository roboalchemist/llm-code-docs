# Source: https://firebase.google.com/docs/data-connect/cloud-audit-logging.md.txt

# Source: https://firebase.google.com/docs/app-hosting/cloud-audit-logging.md.txt

# Source: https://firebase.google.com/docs/ai-logic/cloud-audit-logging.md.txt

# Source: https://firebase.google.com/docs/app-hosting/cloud-audit-logging.md.txt

# Source: https://firebase.google.com/docs/ai-logic/cloud-audit-logging.md.txt

<br />

This page describes the audit logs created byFirebaseas part of[Cloud Audit Logs](https://cloud.google.com/logging/docs/audit/).

## Overview

Firebase services write audit logs to help you answer the questions, "Who did what, where, and when?". These are Cloud Audit Logs, provided as part of the[Google Cloudproject connected to your Firebase project](https://firebase.google.com/docs/projects/learn-more#firebase-cloud-relationship).

Your Firebase projects each contain only the audit logs for resources that are directly within the project.

For a general overview of Cloud Audit Logs, see[Cloud Audit Logs overview](https://cloud.google.com/logging/docs/audit/). For a deeper understanding of the audit log format, see[Understand audit logs](https://cloud.google.com/logging/docs/audit/understanding-audit-logs).

## Available audit logs

The following types of audit logs are available for Firebase AI Logic:

- Admin Activity audit logs

  Includes "admin write" operations that write metadata or configuration information.

  You can't disable Admin Activity audit logs.
- Data Access audit logs

  Includes "admin read" operations that read metadata or configuration information. Also includes "data read" and "data write" operations that read or write user-provided data.

  To receive Data Access audit logs, you must explicitly enable them.

For fuller descriptions of the audit log types, see[Types of audit logs](https://cloud.google.com/logging/docs/audit#types).

## Audited operations

The following summarizes which API operations correspond to each audit log type in Firebase AI Logic:

<br />

| Permission type |                           Methods                            |
|-----------------|--------------------------------------------------------------|
| `ADMIN_READ`    | `google.firebase.vertexai.v1beta.ConfigService.GetConfig`    |
| `ADMIN_WRITE`   | `google.firebase.vertexai.v1beta.ConfigService.UpdateConfig` |

<br />

## Audit log format

Audit log entries include the following objects:

- The log entry itself, which is an object of type[`LogEntry`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Useful fields include the following:

  - The`logName`contains the resource ID and audit log type.
  - The`resource`contains the target of the audited operation.
  - The`timestamp`contains the time of the audited operation.
  - The`protoPayload`contains the audited information.
- The audit logging data, which is an[`AuditLog`](https://cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog)object held in the`protoPayload`field of the log entry.

- Optional service-specific audit information, which is a service-specific object. For older integrations, this object is held in the`serviceData`field of the`AuditLog`object; newer integrations use the`metadata`field.

For other fields in these objects, and how to interpret them, review[Understand audit logs](https://cloud.google.com/logging/docs/audit/understanding-audit-logs).

### Log name

Cloud Audit Logs resource names indicate the Firebase project or otherGoogle Cloudentity that owns the audit logs, and whether the log contains Admin Activity, Data Access, Policy Denied, or System Event audit logging data. For example, the following shows log names for project-level Admin Activity audit logs and an organization's Data Access audit logs. The variables denote Firebase project and organization identifiers.  

```
projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
```  

```
organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access
```
| **Note:** The part of the log name following`/logs/`must be URL-encoded. The forward-slash character,`/`, must be written as`%2F`.

### Service name

Firebase AI Logic audit logs use the service name`firebasevertexai.googleapis.com`.

For a full list of all the Cloud Logging API service names and their corresponding monitored resource type, see[Map services to resources](https://cloud.google.com/logging/docs/api/v2/resource-list#service-names).

### Resource types

Firebase AI Logic audit logs use the resource type`audited_resource`for all audit logs.

For a list of all the Cloud Logging monitored resource types and descriptive information, see[Monitored resource types](https://cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

## Enable audit logging

Admin Activity audit logs are always enabled; you can't disable them.

Data Access audit logs are disabled by default and aren't written unless explicitly enabled (the exception is Data Access audit logs for BigQuery, which can't be disabled).

For instructions on enabling some or all of your Data Access audit logs, see[Configure Data Access logs](https://cloud.google.com/logging/docs/audit/configure-data-access).

## Permissions and roles

[Cloud IAM](https://cloud.google.com/iam/docs)permissions and roles determine your ability to access audit logs data inGoogle Cloudresources.

When deciding which[Logging-specific permissions and roles](https://cloud.google.com/logging/docs/access-control#permissions_and_roles)apply to your use case, consider the following:

- The Logs Viewer role (`roles/logging.viewer`) gives you read-only access to Admin Activity, Policy Denied, and System Event audit logs. If you have just this role, you cannot view Data Access audit logs that are in the`_Default`bucket.

- The Private Logs Viewer role`(roles/logging.privateLogViewer`) includes the permissions contained in`roles/logging.viewer`, plus the ability to read Data Access audit logs in the`_Default`bucket.

  Note that if these private logs are stored in user-defined buckets, then any user who has permissions to read logs in those buckets can read the private logs. For more information on log buckets, see[Routing and storage overview](https://cloud.google.com/logging/docs/routing/overview).

For more information on the Cloud IAM permissions and roles that apply to audit logs data, see[Access control](https://cloud.google.com/logging/docs/access-control).

## View logs

To find and view audit logs, you need to know the identifier of the Firebase project, folder, or organization for which you want to view audit logging information. You can further specify other indexed[`LogEntry`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)fields, like`resource.type`; for details, review[Find log entries quickly](https://cloud.google.com/logging/docs/view/advanced-queries#finding-quickly).

The following are the audit log names; they include variables for the identifiers of the Firebase project, folder, or organization:  

```sql
   projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
   projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fdata_access
   projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
   projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fpolicy

   folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Factivity
   folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fdata_access
   folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
   folders/FOLDER_ID/logs/cloudaudit.googleapis.com%2Fpolicy

   organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Factivity
   organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fdata_access
   organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fsystem_event
   organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com%2Fpolicy
```

You can view audit logs in Cloud Logging using the Google Cloud console, the`gcloud`command-line tool, or the Logging API.  

### Console

You can use the Logs Explorer in the Google Cloud console to retrieve your audit log entries for your Firebase project, folder, or organization:

1. In the Google Cloud console, go to the**Logging \> Logs Explorer**page.

   [Go to the Logs Explorer page](https://console.cloud.google.com/logs/viewer)
   | **Note:** If you're using the**Legacy Logs Viewer** page, switch to the**Logs Explorer**page.
2. On the**Logs Explorer**page, select an existing Firebase project, folder or organization.

3. In the**Query builder**pane, do the following:

   - In**Resource type** , select theGoogle Cloudresource whose audit logs you want to see.

   - In**Log name**, select the audit log type that you want to see:

     - For Admin Activity audit logs, select**activity**.
     - For Data Access audit logs, select**data_access**.
     - For System Event audit logs, select**system_event**.
     - For Policy Denied audit logs, select**policy**.

   If you don't see these options, then there aren't any audit logs of that type available in the Firebase project, folder, or organization.

   For more details about querying using the Logs Explorer, see[Build log queries](https://cloud.google.com/logging/docs/view/building-queries).

### gcloud

The`gcloud`command-line tool provides a command-line interface to the Cloud Logging API. Supply a valid<var translate="no">PROJECT_ID</var>,<var translate="no">FOLDER_ID</var>, or<var translate="no">ORGANIZATION_ID</var>in each of the log names.

To read your Firebase project-level audit log entries, run the following command:  

```scdoc
gcloud logging read "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com" --project=PROJECT_ID
```

To read your folder-level audit log entries, run the following command:  

```scdoc
gcloud logging read "logName : folders/FOLDER_ID/logs/cloudaudit.googleapis.com" --folder=FOLDER_ID
```

To read your organization-level audit log entries, run the following command:  

```scdoc
gcloud logging read "logName : organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com" --organization=ORGANIZATION_ID
```

For more information about using the`gcloud`tool, see[Read log entries](https://cloud.google.com/sdk/gcloud/reference/logging/read).

### API

When building your queries, replace the variables with valid values, substitute the appropriate project-level, folder-level, or organization-level audit log name or identifiers as listed in the audit log names. For example, if your query includes a<var translate="no">PROJECT_ID</var>, then the project identifier you supply must refer to the currently selected Firebase project.

To use the Logging API to look at your audit log entries, do the following:

1. Go to the**Try this API** section in the documentation for the[`entries.list`](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list)method.

2. Put the following into the**Request body** part of the**Try this API** form. Clicking on this[prepopulated form](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list?apix_params=%7B%22resource%22:%7B%22resourceNames%22:%5B%22projects/%5BPROJECT_ID%5D%22%5D,%22pageSize%22:5,%22filter%22:%22logName%3D(projects/%5BPROJECT_ID%5D/logs/cloudaudit.googleapis.com%252Factivity+OR+projects/%5BPROJECT_ID%5D/logs/cloudaudit.googleapis.com%252Fsystem_events+OR+projects/%5BPROJECT_ID%5D/logs/cloudaudit.googleapis.com%252Fdata_access)%22%7D%7D)automatically fills the request body, but you need to supply a valid<var translate="no">PROJECT_ID</var>in each of the log names.

   ```scdoc
   {
     "resourceNames": [
       "projects/PROJECT_ID"
     ],
     "pageSize": 5,
     "filter": "logName : projects/PROJECT_ID/logs/cloudaudit.googleapis.com"
   }
   ```
3. Click**Execute**.

For more details about querying, see[Logging query language](https://cloud.google.com/logging/docs/view/logging-query-language).

For an example of an audit log entry and how to find the most important information in it, see[Sample audit log entry](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#sample).

## Route audit logs

You can[route audit logs](https://cloud.google.com/logging/docs/routing/overview)to supported destinations in the same way that you can route other kinds of logs. Here are some reasons you might want to route your audit logs:

- To keep audit logs for a longer period of time or to use more powerful search capabilities, you can route copies of your audit logs to Google Cloud Storage, BigQuery, or Google Cloud Pub/Sub. Using Cloud Pub/Sub, you can route to other applications, other repositories, and to third parties.

- To manage your audit logs across an entire organization, you can create[aggregated sinks](https://cloud.google.com/logging/docs/export/aggregated_sinks)that can route logs from any or all Firebase projects in the organization.

<!-- -->

- If your enabled Data Access audit logs are pushing your Firebase projects over your log allotments, you can create sinks that exclude the Data Access audit logs from Logging.

For instructions on routing logs, see[Configure sinks](https://cloud.google.com/logging/docs/export/configure_export_v2).

## Pricing

[Admin Activity audit logs](https://cloud.google.com/logging/docs/audit#admin-activity)and[System Event audit logs](https://cloud.google.com/logging/docs/audit#system-event)are no-cost.

[Data Access audit logs](https://cloud.google.com/logging/docs/audit#data-access)and[Policy Denied audit logs](https://cloud.google.com/logging/docs/audit#policy_denied)are chargeable.

For more information about Cloud Logging pricing, see[Google Cloud's operations suite pricing: Cloud Logging](https://cloud.google.com/stackdriver/pricing#logging-costs).